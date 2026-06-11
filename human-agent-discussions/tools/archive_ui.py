#!/usr/bin/env python3
"""Local web UI for archive_sessions.py — drag-drop exports, one-click
account selection, checkbox archiving, and a git panel (staging + commit +
push results). Runs against the local git clone, served on localhost only.

    python3 human-agent-discussions/tools/archive_ui.py [--port 8123] [--open]

Zero third-party dependencies (stdlib http.server + the sibling archiver).
The browser page is the sibling archive_ui.html. All state lives on disk in
the repo (accounts = directories), so "remembered accounts" survive across
machines once committed.

Endpoints (JSON unless noted):
    GET  /                    UI page (archive_ui.html)
    GET  /api/state           accounts, archived sessions, repo + engine info
    POST /api/upload          ?account=&filename= raw body (.json/.jsonl/.zip)
    GET  /api/scan            ?account= (optional) -> matched conversations
    POST /api/archive         {selections:[{account,id}], redact_pii, force}
    GET  /api/git/status      branch, ahead/behind, staged/unstaged files
    POST /api/git/commit      {message, push} -> commit sha + push output
    GET  /files/<rel>         serve archived session.md / session.pdf
"""

import argparse
import json
import re
import shutil
import socket
import sys
import tempfile
import threading
import zipfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archive_sessions as core  # noqa: E402

UI_VERSION = "1.0.0"
MAX_UPLOAD = 2 * 1024 * 1024 * 1024  # 2 GiB — exports can be large
SAFE_FILE_RE = re.compile(r"[^A-Za-z0-9._-]+")
ALLOWED_SUFFIXES = {".json", ".jsonl", ".zip"}


def make_opts(**over):
    """argparse.Namespace with every field the archiver core reads."""
    base = dict(
        include_thinking=False, tools="summary", attachment_chars=0,
        force=False, github=False, no_redact=False, redact_pii=False,
        pdf_mainfont=None, pdf_monofont=None,
        no_default_keywords=False, keyword=None, keywords_file=None,
        export=None,
    )
    base.update(over)
    return argparse.Namespace(**base)


def safe_filename(name):
    base = Path(name).name
    base = SAFE_FILE_RE.sub("-", base).strip("-.") or "upload"
    return base


def origin_https(repo):
    """origin remote URL normalized to a clickable https form (or None)."""
    rc, out, _ = core.run(["git", "remote", "get-url", "origin"], cwd=repo.path)
    if rc != 0:
        return None
    u = out.strip()
    m = re.match(r"git@([^:]+):(.+?)(?:\.git)?$", u)
    if m:
        return "https://%s/%s" % (m.group(1), m.group(2))
    u = re.sub(r"\.git$", "", u)
    return u if u.startswith("http") else None


class ArchiveService:
    """Stateless-ish facade over the archiver core (one per server)."""

    def __init__(self, root, repo_path, github=False):
        self.root = Path(root).resolve()
        self.repo = core.Repo(repo_path or core.find_repo_root(self.root))
        self.github = github
        self.engine = core.detect_engine("auto")
        self._trailers = None
        self._lock = threading.Lock()

    def trailers(self):
        with self._lock:
            if self._trailers is None:
                self._trailers = self.repo.trailer_map() if self.repo.ok() else {}
            return self._trailers

    # ---- accounts ----------------------------------------------------
    def accounts(self):
        names = {}
        for sub in sorted(self.root.iterdir()) if self.root.is_dir() else []:
            if sub.is_dir() and core.ACCOUNT_RE.match(sub.name) \
                    and sub.name not in ("tools", "_incoming"):
                names.setdefault(sub.name, {"archived": 0, "incoming": 0})
                names[sub.name]["archived"] = len(list(sub.glob("*/metadata.json")))
        incoming = self.root / "_incoming"
        if incoming.is_dir():
            for sub in sorted(incoming.iterdir()):
                if sub.is_dir() and core.ACCOUNT_RE.match(sub.name):
                    names.setdefault(sub.name, {"archived": 0, "incoming": 0})
                    names[sub.name]["incoming"] = sum(
                        1 for f in sub.rglob("*")
                        if f.is_file() and f.suffix in (".json", ".jsonl"))
        return [dict(name=k, **v) for k, v in sorted(names.items())]

    # ---- archived sessions (for the index panel) ---------------------
    def sessions(self):
        out = []
        for key, (sdir, meta) in sorted(core.load_existing(self.root).items()):
            rel = sdir.relative_to(self.root).as_posix()
            related = meta.get("related", {})
            out.append({
                "account": meta.get("account"),
                "title": meta.get("title"),
                "date": (meta.get("created_at") or "")[:10],
                "dir": rel,
                "md": rel + "/session.md",
                "pdf": rel + "/session.pdf",
                "prs": [p.get("number") for p in related.get("prs", [])],
                "commits": [c.get("sha", "")[:12] for c in related.get("commits", [])],
                "branches": [b.get("name") for b in related.get("branches", [])],
            })
        out.sort(key=lambda s: s["date"] or "", reverse=True)
        return out

    # ---- scan ---------------------------------------------------------
    def scan(self, account=None):
        args = make_opts()
        pairs = core.discover_inputs(args, self.root)
        if account:
            pairs = [p for p in pairs if p[0] == account]
        keywords = core.collect_keywords(args)
        convs = []
        for acct, kind, path in pairs:
            if kind == "export":
                convs.extend(core.parse_claude_export(path, acct, args))
            else:
                c = core.parse_code_jsonl(path, acct, args)
                if c:
                    convs.append(c)
        existing = core.load_existing(self.root)
        matches = []
        for conv in convs:
            hits = core.keyword_hits(conv, keywords)
            if not hits:
                continue
            key = (conv["account"], conv["id"])
            if key not in existing:
                status = "NEW"
            else:
                prior = core.parse_ts(existing[key][1].get("updated_at"))
                status = ("UPDATED" if prior and conv["updated_at"]
                          and conv["updated_at"] > prior else "archived")
            summary = core.screen_conv(conv, redact=False)  # scan only
            matches.append({
                "account": conv["account"],
                "id": conv["id"],
                "source": conv["source"],
                "title": conv["title"],
                "date": core.iso(conv["created_at"]) or "",
                "messages": len(conv["messages"]),
                "hits": hits,
                "status": status,
                "severity": core.screen_severity(summary),
                "findings": summary["flagged"],
            })
        matches.sort(key=lambda m: m["date"] or "")
        return {"matched": matches, "scanned": len(convs)}

    # ---- archive --------------------------------------------------------
    def archive(self, selections, redact_pii=False, force=False):
        wanted = {(s.get("account"), s.get("id")) for s in selections}
        opts = make_opts(redact_pii=bool(redact_pii), force=bool(force),
                         github=self.github)
        pairs = core.discover_inputs(opts, self.root)
        keywords = core.collect_keywords(opts)
        existing = core.load_existing(self.root)
        results = []
        for acct, kind, path in pairs:
            convs = (core.parse_claude_export(path, acct, opts)
                     if kind == "export"
                     else [c for c in [core.parse_code_jsonl(path, acct, opts)] if c])
            for conv in convs:
                if (conv["account"], conv["id"]) not in wanted:
                    continue
                wanted.discard((conv["account"], conv["id"]))
                hits = core.keyword_hits(conv, keywords)
                out_dir, status = core.archive_one(
                    conv, hits, self.root, self.repo, self.trailers(),
                    self.engine, opts, existing)
                rel = out_dir.relative_to(self.root).as_posix()
                results.append({
                    "account": conv["account"], "title": conv["title"],
                    "dir": rel, "status": status,
                    "md": rel + "/session.md", "pdf": rel + "/session.pdf",
                })
        indexed = core.regenerate_index(self.root)
        return {"results": results, "indexed": indexed,
                "missing": sorted(["%s/%s" % w for w in wanted])}

    # ---- upload --------------------------------------------------------
    def upload(self, account, filename, body):
        account = (account or "").strip().lower()
        if not core.ACCOUNT_RE.match(account):
            raise ValueError("bad account alias (lowercase letters/digits/hyphens)")
        fname = safe_filename(filename or "conversations.json")
        if Path(fname).suffix not in ALLOWED_SUFFIXES:
            raise ValueError("only .json / .jsonl / .zip uploads are accepted")
        dest_dir = self.root / "_incoming" / account
        dest_dir.mkdir(parents=True, exist_ok=True)
        saved = []
        if fname.endswith(".zip"):
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tf:
                tf.write(body)
                tmp = Path(tf.name)
            try:
                with zipfile.ZipFile(tmp) as zf:
                    for info in zf.infolist():
                        base = safe_filename(info.filename)
                        if info.is_dir() or Path(base).suffix not in (".json", ".jsonl"):
                            continue
                        if not (re.match(r"conversations.*\.json$", base)
                                or base.endswith(".jsonl")):
                            continue
                        target = dest_dir / base
                        with zf.open(info) as src, open(target, "wb") as dst:
                            shutil.copyfileobj(src, dst)
                        saved.append(base)
            finally:
                tmp.unlink(missing_ok=True)
            if not saved:
                raise ValueError("zip contains no conversations*.json / *.jsonl")
        else:
            (dest_dir / fname).write_bytes(body)
            saved.append(fname)
        return {"account": account, "saved": saved,
                "incoming_dir": str(dest_dir.relative_to(self.root))}

    # ---- git -----------------------------------------------------------
    def _root_rel(self):
        try:
            return str(self.root.relative_to(self.repo.path))
        except ValueError:
            return "."

    def git_status(self):
        cwd = self.repo.path
        rc, branch, _ = core.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)
        rc2, head, _ = core.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=cwd)
        ahead = behind = None
        rc3, counts, _ = core.run(
            ["git", "rev-list", "--left-right", "--count", "@{u}...HEAD"], cwd=cwd)
        if rc3 == 0 and counts.strip():
            parts = counts.split()
            if len(parts) == 2:
                behind, ahead = int(parts[0]), int(parts[1])
        rel = self._root_rel()
        rc4, porcelain, _ = core.run(
            ["git", "status", "--porcelain", "--", rel], cwd=cwd)
        staged, unstaged = [], []
        for line in porcelain.splitlines():
            if len(line) < 4:
                continue
            x, y, path = line[0], line[1], line[3:]
            if x not in (" ", "?"):
                staged.append({"state": x, "path": path})
            if y != " ":
                unstaged.append({"state": "untracked" if y == "?" else y,
                                 "path": path})
        return {
            "branch": branch.strip() if rc == 0 else None,
            "head": head.strip() if rc2 == 0 else None,
            "ahead": ahead, "behind": behind,
            "staged": staged, "unstaged": unstaged,
            "origin": origin_https(self.repo),
            "scope": rel,
        }

    def git_commit(self, message, push=False):
        cwd = self.repo.path
        rel = self._root_rel()
        log_lines = []

        def step(cmd, timeout=120):
            rc, out, err = core.run(cmd, cwd=cwd, timeout=timeout)
            log_lines.append("$ %s\n%s" % (" ".join(cmd), (out + err).strip()))
            return rc, out, err

        step(["git", "add", "-A", "--", rel])
        rc, _, _ = core.run(["git", "diff", "--cached", "--quiet", "--", rel], cwd=cwd)
        if rc == 0:
            return {"ok": False, "error": "nothing to commit under " + rel,
                    "log": "\n".join(log_lines)}
        message = (message or "").strip() or "archive: update human-agent-discussions"
        rc, _, err = step(["git", "commit", "-m", message])
        if rc != 0:
            return {"ok": False, "error": "commit failed: " + err.strip()[:400],
                    "log": "\n".join(log_lines)}
        _, sha, _ = core.run(["git", "rev-parse", "HEAD"], cwd=cwd)
        sha = sha.strip()
        pushed = False
        push_output = ""
        if push:
            rcb, branch, _ = core.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)
            branch = branch.strip() if rcb == 0 else "HEAD"
            rc, out, err = step(["git", "push", "-u", "origin", branch], timeout=300)
            pushed = rc == 0
            push_output = (out + err).strip()
        origin = origin_https(self.repo)
        commit_url = ("%s/commit/%s" % (origin, sha)) if origin else None
        return {"ok": True, "sha": sha, "sha_short": sha[:12],
                "pushed": pushed, "push_output": push_output,
                "commit_url": commit_url, "log": "\n".join(log_lines),
                "status_after": self.git_status()}


# ------------------------------------------------------------------ HTTP

class Handler(BaseHTTPRequestHandler):
    service = None  # injected
    html_path = Path(__file__).resolve().parent / "archive_ui.html"

    # quiet default request logging; errors still surface via responses
    def log_message(self, fmt, *args):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _err(self, code, msg):
        self._send(code, {"error": msg})

    def _body(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_UPLOAD:
            raise ValueError("upload too large")
        return self.rfile.read(length)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/":
                if not self.html_path.exists():
                    return self._err(500, "archive_ui.html missing next to archive_ui.py")
                return self._send(200, self.html_path.read_bytes(),
                                  "text/html; charset=utf-8")
            if u.path == "/api/state":
                s = self.service
                return self._send(200, {
                    "ui_version": UI_VERSION,
                    "archiver_version": core.VERSION,
                    "root": str(s.root),
                    "repo": str(s.repo.path),
                    "engine": "+".join(s.engine) if s.engine else "none",
                    "accounts": s.accounts(),
                    "sessions": s.sessions(),
                    "git": s.git_status() if s.repo.ok() else None,
                })
            if u.path == "/api/scan":
                return self._send(200, self.service.scan(q.get("account") or None))
            if u.path == "/api/git/status":
                return self._send(200, self.service.git_status())
            if u.path.startswith("/files/"):
                rel = u.path[len("/files/"):]
                target = (self.service.root / rel).resolve()
                root = self.service.root.resolve()
                if root != target and root not in target.parents:
                    return self._err(403, "outside archive root")
                if not target.is_file():
                    return self._err(404, "not found")
                ctype = {"pdf": "application/pdf",
                         "md": "text/markdown; charset=utf-8",
                         "json": "application/json; charset=utf-8",
                         }.get(target.suffix.lstrip("."), "application/octet-stream")
                return self._send(200, target.read_bytes(), ctype)
            return self._err(404, "unknown path " + u.path)
        except Exception as e:  # surface, don't crash the thread
            return self._err(500, "%s: %s" % (type(e).__name__, e))

    def do_POST(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/api/upload":
                body = self._body()
                return self._send(200, self.service.upload(
                    q.get("account"), q.get("filename"), body))
            payload = {}
            raw = self._body()
            if raw:
                payload = json.loads(raw.decode("utf-8"))
            if u.path == "/api/archive":
                return self._send(200, self.service.archive(
                    payload.get("selections") or [],
                    redact_pii=payload.get("redact_pii", False),
                    force=payload.get("force", False)))
            if u.path == "/api/git/commit":
                return self._send(200, self.service.git_commit(
                    payload.get("message", ""),
                    push=payload.get("push", False)))
            return self._err(404, "unknown path " + u.path)
        except ValueError as e:
            return self._err(400, str(e))
        except Exception as e:
            return self._err(500, "%s: %s" % (type(e).__name__, e))


def serve(root, repo, port, github=False, open_browser=False):
    service = ArchiveService(root, repo, github=github)
    handler = type("BoundHandler", (Handler,), {"service": service})
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = "http://127.0.0.1:%d/" % httpd.server_address[1]
    print("archive-ui %s serving %s\n  root: %s\n  repo: %s\n  engine: %s"
          % (UI_VERSION, url, service.root, service.repo.path,
             "+".join(service.engine) if service.engine else "none"))
    print("Localhost only. Ctrl-C to stop.")
    if open_browser:
        import webbrowser
        threading.Timer(0.3, webbrowser.open, args=(url,)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")
    return 0


# ------------------------------------------------------------------ self-test

def self_test():
    import urllib.request

    tmp = Path(tempfile.mkdtemp(prefix="had-ui-selftest-"))
    try:
        # isolated git repo so commit/push tests never touch the real clone
        repo_dir = tmp / "repo"
        (repo_dir / "human-agent-discussions").mkdir(parents=True)
        for cmd in (["git", "init", "-q"],
                    ["git", "config", "user.email", "selftest@example.invalid"],
                    ["git", "config", "user.name", "selftest"],
                    # hermetic: global signing config may not work in a temp repo
                    ["git", "config", "commit.gpgsign", "false"]):
            rc, _, err = core.run(cmd, cwd=repo_dir)
            assert rc == 0, err
        root = repo_dir / "human-agent-discussions"
        export = [{
            "uuid": "11111111-2222-3333-4444-555555555555",
            "name": "QOU: archive UI fixture (Hecke trace)",
            "created_at": "2026-06-05T12:00:00Z",
            "updated_at": "2026-06-05T13:00:00Z",
            "chat_messages": [
                {"sender": "human", "created_at": "2026-06-05T12:00:00Z",
                 "text": "Markov trace tr_M in litlfred/qou, see PR #1821. "
                         "Key sk-ant-api03-AAAABBBBCCCCDDDDEEEE1111 leaked."},
                {"sender": "assistant", "created_at": "2026-06-05T12:01:00Z",
                 "text": "The Hecke algebra trace is canonical."},
            ]}, {
            "uuid": "99999999-8888-7777-6666-555555555555",
            "name": "Gardening",
            "chat_messages": [
                {"sender": "human", "text": "When to plant tomatoes?",
                 "created_at": "2026-06-06T12:00:00Z"}],
            "created_at": "2026-06-06T12:00:00Z",
        }]

        service = ArchiveService(root, repo_dir)
        handler = type("TestHandler", (Handler,), {"service": service})
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        port = httpd.server_address[1]
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()
        base = "http://127.0.0.1:%d" % port

        def api(path, data=None, raw=None, headers=None):
            req = urllib.request.Request(
                base + path,
                data=raw if raw is not None else
                (json.dumps(data).encode() if data is not None else None),
                headers=headers or {})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                ct = r.headers.get("Content-Type", "")
                return (json.loads(body) if ct.startswith("application/json")
                        else body)

        # upload an export for a fresh account
        up = api("/api/upload?account=acct-one&filename=conversations.json",
                 raw=json.dumps(export).encode())
        assert up["saved"] == ["conversations.json"], up

        # zip route: same payload inside a zip
        zpath = tmp / "export.zip"
        with zipfile.ZipFile(zpath, "w") as zf:
            zf.writestr("data/conversations.json", json.dumps(export))
        up2 = api("/api/upload?account=acct-two&filename=export.zip",
                  raw=zpath.read_bytes())
        assert up2["saved"] == ["conversations.json"], up2

        state = api("/api/state")
        names = {a["name"] for a in state["accounts"]}
        assert {"acct-one", "acct-two"} <= names, names

        scan = api("/api/scan?account=acct-one")
        assert scan["scanned"] == 2 and len(scan["matched"]) == 1, scan
        m = scan["matched"][0]
        assert m["status"] == "NEW" and m["severity"] == "SECRET", m

        arch = api("/api/archive", data={
            "selections": [{"account": "acct-one", "id": m["id"]}]})
        assert len(arch["results"]) == 1 and not arch["missing"], arch
        rel_pdf = arch["results"][0]["pdf"]
        pdf = api("/files/" + rel_pdf)
        assert pdf[:5] == b"%PDF-", "served PDF invalid"
        md = api("/files/" + arch["results"][0]["md"])
        assert b"[REDACTED-anthropic-key]" in md, "secret not redacted in served md"

        # path traversal must be refused
        try:
            api("/files/../../etc/hosts")
            assert False, "traversal not blocked"
        except urllib.error.HTTPError as e:
            assert e.code in (400, 403, 404), e.code

        st = api("/api/git/status")
        assert st["unstaged"] or st["staged"], "expected dirty tree after archive"

        commit = api("/api/git/commit",
                     data={"message": "archive: ui self-test", "push": False})
        assert commit["ok"] and len(commit["sha"]) == 40, commit
        st2 = commit["status_after"]
        assert not st2["staged"] and not st2["unstaged"], st2

        # re-scan: now reported as archived, idempotent re-archive skips
        scan2 = api("/api/scan?account=acct-one")
        assert scan2["matched"][0]["status"] == "archived", scan2

        httpd.shutdown()
        print("UI SELF-TEST PASS (upload json+zip, scan, archive, files, "
              "traversal-block, git commit; port %d)" % port)
        shutil.rmtree(tmp, ignore_errors=True)
        return 0
    except AssertionError as e:
        print("UI SELF-TEST FAIL: %s\n(artifacts kept at %s)" % (e, tmp))
        return 1


def main(argv=None):
    default_root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--port", type=int, default=8123)
    ap.add_argument("--root", type=Path, default=default_root)
    ap.add_argument("--repo", type=Path, default=None)
    ap.add_argument("--github", action="store_true",
                    help="enrich tags via the gh CLI on archive")
    ap.add_argument("--open", action="store_true", help="open the browser")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--version", action="version",
                    version="%(prog)s " + UI_VERSION)
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    return serve(args.root.expanduser().resolve(), args.repo, args.port,
                 github=args.github, open_browser=args.open)


if __name__ == "__main__":
    sys.exit(main())
