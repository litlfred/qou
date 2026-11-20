#!/usr/bin/env python3
"""Triage the machine-generated Lean batch PRs (rerunnable).

Classifies every OPEN PR whose head matches one of the batch-formalization
branch families (feat/round*, feat/qou-*, qou-10v9-*, ... see BATCH_PATTERNS)
at three levels, breadth first:

  1. metadata   GET pulls/{n} (.mergeable / .mergeable_state), pulls/{n}/files,
                cited bean ids (title/body/branch) checked against the bean mount
                (beans/defs/*.md frontmatter: status, pr:), file-overlap and
                declaration-overlap clusters between PRs.
  2. static     the PR head is fetched (refs/pull/N/head) and every ADDED/CHANGED
                .lean file is scanned with comments stripped: real `sorry`,
                `axiom`, `native_decide`, `: True` conclusions/fields, `X = X`
                tautologies, theorems whose body is a bare `rfl`/`trivial`/
                `by rfl`/`by decide`/`by norm_num`/`by simp` on a one-line
                statement ("rfl-only"), import-free files (no QOU/Mathlib import),
                and witness JSON / probe precision (`mp.dps`, "dps" fields; the
                batch PRs claim an 80-dps mpmath witness).
  3. lean       optional (`--lean`): `lean`-direct on changed files if a
                toolchain + olean tree is available (LEAN_PATH from
                scripts/lean-direct-env.sh). Skipped with a recorded reason
                otherwise -- a skipped check is never reported as a pass.

Verdicts (heuristic; the coordinator decides):
  CLOSE-SUPERSEDED  every cited bean is completed by ANOTHER pr / all its
                    Lean files already exist identically on main / a newer
                    open PR re-does the same beans or declarations.
  CLOSE-VACUOUS     the scanned Lean is dominated by vacuity red flags
                    (`: True`, tautologies, rfl-only on local defs, import-free
                    Int/Bool proxies) with no substantive declaration.
  NEEDS-REWORK      conflicts with main (mergeable=false / dirty), real sorry
                    or uncited axiom, partial vacuity, precision below claim,
                    or file collision with another open PR.
  MERGE-CANDIDATE   mergeable, sorry/axiom-free, no strong vacuity flag, no
                    collision, beans not already completed elsewhere. This is a
                    STATIC verdict: Lean exit-0 is still owed unless
                    lean_status == "pass".

Usage:
  python3 scripts/batch-pr-triage.py gather   # API metadata (cached)
  python3 scripts/batch-pr-triage.py fetch    # git fetch PR heads
  python3 scripts/batch-pr-triage.py scan     # static Lean/witness scan
  python3 scripts/batch-pr-triage.py report --out docs/coordination/<date>-batch-pr-triage
  python3 scripts/batch-pr-triage.py all --out ...

Cache: $TRIAGE_CACHE (default /tmp/batch-pr-triage). Read-only towards GitHub:
this script never merges, closes or comments.
"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures as cf
import json
import os
import pathlib
import re
import subprocess
import sys
import time

REPO = "litlfred/qou"
ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = pathlib.Path(os.environ.get("TRIAGE_CACHE", "/tmp/batch-pr-triage"))
BEANS = pathlib.Path(os.environ.get("BEANS_DIR", "/home/claude/qou/beans/defs"))
GITDIR = os.environ.get("TRIAGE_GIT", str(ROOT))

BATCH_PATTERNS = [
    r"^feat/round", r"^feat/qou-", r"^qou-10v9-", r"^qou-8lxd-", r"^qou-mub3-",
    r"^cat/round", r"^claude/round\d+-devacuify", r"^claude/qou-rtxm-",
    r"^claude/r46-", r"^claude/qou-9634-", r"^claude/qou-3l2l-",
    r"^fix/qou-rtxm-", r"^fix/qou-wxhi-",
]
BEAN_RE = re.compile(r"\bqou-([0-9a-z]{4})\b")


# --------------------------------------------------------------------- utils
def gh(path: str, retries: int = 4):
    for k in range(retries):
        p = subprocess.run(["gh", "api", path], capture_output=True, text=True)
        if p.returncode == 0:
            return json.loads(p.stdout or "null")
        time.sleep(3 + 5 * k)
    raise RuntimeError(f"gh api {path}: {p.stderr[:300]}")


def git(*args, check=True):
    p = subprocess.run(["git", "-C", GITDIR, *args], capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr[:400]}")
    return p.stdout


def family(head: str) -> str | None:
    for p in BATCH_PATTERNS:
        if re.match(p, head):
            return p.strip("^").replace("\\d+", "N")
    return None


# -------------------------------------------------------------------- gather
def gather(args):
    CACHE.mkdir(parents=True, exist_ok=True)
    prs = []
    for page in range(1, 10):
        batch = gh(f"repos/{REPO}/pulls?state=open&per_page=100&page={page}")
        prs += batch
        if len(batch) < 100:
            break
    batch_prs = [p for p in prs if family(p["head"]["ref"])]
    print(f"open PRs: {len(prs)}  batch-family: {len(batch_prs)}", flush=True)
    (CACHE / "open_pulls.json").write_text(json.dumps(prs))

    def one(p):
        n = p["number"]
        f = CACHE / f"pr_{n}.json"
        if f.exists() and not args.refresh:
            d = json.loads(f.read_text())
            if d.get("head_sha") == p["head"]["sha"] and d.get("mergeable") is not None:
                return n
        det = gh(f"repos/{REPO}/pulls/{n}")
        if det.get("mergeable") is None:  # GitHub computes lazily
            time.sleep(4)
            det = gh(f"repos/{REPO}/pulls/{n}")
        files = []
        for page in range(1, 31):
            b = gh(f"repos/{REPO}/pulls/{n}/files?per_page=100&page={page}")
            files += b
            if len(b) < 100:
                break
        d = {
            "number": n, "head": p["head"]["ref"], "head_sha": p["head"]["sha"],
            "family": family(p["head"]["ref"]), "title": p["title"],
            "body": p.get("body") or "", "created_at": p["created_at"],
            "updated_at": p["updated_at"], "draft": p.get("draft"),
            "base_sha": det["base"]["sha"],
            "mergeable": det.get("mergeable"), "mergeable_state": det.get("mergeable_state"),
            "additions": det.get("additions"), "deletions": det.get("deletions"),
            "changed_files": det.get("changed_files"), "commits": det.get("commits"),
            "files": [{"filename": x["filename"], "status": x["status"],
                       "additions": x["additions"], "deletions": x["deletions"],
                       "patch": x.get("patch", "")[:200000]} for x in files],
        }
        f.write_text(json.dumps(d))
        return n

    with cf.ThreadPoolExecutor(8) as ex:
        for i, n in enumerate(ex.map(one, batch_prs)):
            if i % 25 == 0:
                print(f"  gathered {i+1}/{len(batch_prs)} (#{n})", flush=True)
    (CACHE / "batch_numbers.json").write_text(json.dumps([p["number"] for p in batch_prs]))


def load_prs():
    nums = json.loads((CACHE / "batch_numbers.json").read_text())
    return [json.loads((CACHE / f"pr_{n}.json").read_text()) for n in nums]


# --------------------------------------------------------------------- fetch
def fetch(args):
    prs = load_prs()
    need = [p for p in prs
            if subprocess.run(["git", "-C", GITDIR, "cat-file", "-e", p["head_sha"] + "^{commit}"],
                              capture_output=True).returncode]
    print(f"fetch: {len(need)} of {len(prs)} heads missing locally", flush=True)
    for i in range(0, len(need), 40):
        chunk = need[i:i + 40]
        specs = [f"+refs/pull/{p['number']}/head:refs/remotes/pr/{p['number']}" for p in chunk]
        for k in range(4):
            r = subprocess.run(["git", "-C", GITDIR, "fetch", "--no-tags", "--depth=1", "origin", *specs],
                               capture_output=True, text=True)
            if r.returncode == 0:
                break
            print(f"  fetch retry {k}: {r.stderr[-200:]}", flush=True)
            time.sleep(8 + 6 * k)
        print(f"  fetched {min(i+40, len(need))}/{len(need)}", flush=True)


# ---------------------------------------------------------------------- scan
def strip_comments(src: str) -> str:
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and src.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            if src[i] == "\n":
                out.append("\n")
            i += 1; continue
        if src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        out.append(src[i]); i += 1
    return "".join(out)


DECL_RE = re.compile(
    r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
    r"(theorem|lemma|def|abbrev|instance|structure|class|axiom|inductive|opaque|example)\b\s*([^\s:({\[]*)",
    re.M)


def split_decls(code: str):
    """Yield (kind, name, text) for each top-level declaration."""
    ms = list(DECL_RE.finditer(code))
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(code)
        yield m.group(1), m.group(2), code[m.start():end]


TRIV_BODY = re.compile(
    r":=\s*(?:by\s+)?(?:rfl|trivial|True\.intro|⟨⟩|decide|norm_num|simp|ring|rfl\s*)\s*$|"
    r":=\s*by\s*(?:\n\s*)?(?:rfl|trivial|decide|norm_num(?:\s*\[[^\]]*\])?|simp(?:\s*\[[^\]]*\])?|"
    r"ring|ring_nf|exact\s+rfl|constructor\s*<;>\s*(?:rfl|norm_num|simp|ring)|"
    r"refine\s*⟨[^⟩]*⟩\s*<;>\s*(?:rfl|norm_num|simp|ring)|"
    r"(?:unfold|simp only|dsimp|show)\b[^\n]*\n?\s*(?:<;>\s*)?(?:rfl|norm_num|ring|simp|decide|omega)?)\s*$",
    re.S)


def scan_lean(text: str) -> dict:
    code = strip_comments(text)
    imports = re.findall(r"^import\s+(\S+)", code, re.M)
    r = collections.Counter()
    r["imports_qou_or_mathlib"] = int(any(i.startswith(("QOU", "Mathlib", "UGB")) for i in imports))
    r["sorry"] = len(re.findall(r"\bsorry\b", code))
    r["native_decide"] = len(re.findall(r"\bnative_decide\b", code))
    decls, flags = [], []
    local_defs = set()
    for kind, name, body in split_decls(code):
        if kind in ("def", "abbrev"):
            local_defs.add(name.split(".")[-1])
    for kind, name, body in split_decls(code):
        r[f"n_{kind}"] += 1
        sig, _, proof = body.partition(":=")
        stmt = sig.split(":", 1)[1] if ":" in sig else ""
        fl = []
        if kind == "axiom":
            fl.append("axiom")
        if re.search(r":\s*True\s*$", sig.strip()) or re.search(r"^\s*True\s*$", stmt.strip()):
            fl.append("true-conclusion")
        if kind in ("structure", "class") and re.search(r"\w+\s*:\s*True\b", body):
            fl.append("true-field")
        if kind in ("theorem", "lemma", "example"):
            m = re.fullmatch(r"\s*(.+?)\s*=\s*(.+?)\s*", stmt.replace("\n", " "))
            if m and m.group(1) == m.group(2):
                fl.append("tautology")
            if TRIV_BODY.search(":=" + proof.rstrip()) and len(proof.strip().splitlines()) <= 3:
                used = {w for w in re.findall(r"[A-Za-z_][\w']*", stmt)} & local_defs
                fl.append("rfl-only-on-local-def" if used else "one-tactic")
            if re.search(r"\bsorry\b", proof):
                fl.append("sorry")
        decls.append({"kind": kind, "name": name, "flags": fl})
        for f in fl:
            r[f] += 1
    r["n_provable"] = sum(1 for d in decls if d["kind"] in ("theorem", "lemma"))
    return {"counts": dict(r), "decls": decls, "imports": imports}


DPS_RE = re.compile(r"mp\.dps\s*=\s*(\d+)|[\"'](?:dps|mp_dps|precision_dps|working_dps)[\"']\s*:\s*(\d+)")


def scan_pr(p: dict) -> dict:
    sha = p["head_sha"]
    out = {"lean_files": {}, "dps": [], "py_float64_hits": 0, "scan_error": None}
    if subprocess.run(["git", "-C", GITDIR, "cat-file", "-e", sha + "^{commit}"],
                      capture_output=True).returncode:
        out["scan_error"] = "head not fetched"
        return out
    for f in p["files"]:
        fn = f["filename"]
        if f["status"] == "removed":
            continue
        try:
            txt = git("show", f"{sha}:{fn}")
        except RuntimeError as e:
            out["scan_error"] = str(e)[:200]
            continue
        if fn.endswith(".lean"):
            s = scan_lean(txt)
            main_txt = subprocess.run(["git", "-C", GITDIR, "show", f"origin/main:{fn}"],
                                      capture_output=True, text=True)
            s["identical_on_main"] = main_txt.returncode == 0 and main_txt.stdout == txt
            s["exists_on_main"] = main_txt.returncode == 0
            out["lean_files"][fn] = s
        elif fn.endswith((".py", ".json")):
            for m in DPS_RE.finditer(txt):
                out["dps"].append(int(m.group(1) or m.group(2)))
            if fn.endswith(".py"):
                out["py_float64_hits"] += len(re.findall(r"\bfloat\(|np\.float64|math\.(?:sqrt|exp|log|pi)\b", txt))
    return out


def scan(args):
    prs = load_prs()
    res = {}
    with cf.ThreadPoolExecutor(8) as ex:
        for p, s in zip(prs, ex.map(scan_pr, prs)):
            res[p["number"]] = s
    (CACHE / "scan.json").write_text(json.dumps(res))
    print(f"scanned {len(res)}", flush=True)


# --------------------------------------------------------------------- beans
def load_beans():
    beans = {}
    for f in BEANS.glob("*.md"):
        head = f.read_text(errors="replace")[:1500]
        m = re.search(r"^#\s*(qou-[0-9a-z]{4})", head, re.M) or re.match(r"(qou-[0-9a-z]{4})", f.name)
        bid = m.group(1) if m else "qou-" + f.name[:4]
        st = re.search(r"^status:\s*(\S+)", head, re.M)
        pr = re.search(r"^pr:\s*(\d+)", head, re.M)
        beans[bid] = {"status": st.group(1) if st else "?", "pr": int(pr.group(1)) if pr else None}
    return beans


# -------------------------------------------------------------------- report
def classify(args):
    prs = load_prs()
    scan_res = json.loads((CACHE / "scan.json").read_text()) if (CACHE / "scan.json").exists() else {}
    lean_res = json.loads((CACHE / "lean.json").read_text()) if (CACHE / "lean.json").exists() else {}
    beans = load_beans()
    open_nums = {p["number"] for p in json.loads((CACHE / "open_pulls.json").read_text())}

    # overlap maps (code files only; ledger/registry files are expected shared)
    SHARED_OK = re.compile(r"(^|/)(QOU\.lean|lakefile|lake-manifest|.*\.qa\.json$|beans/|docs/|"
                           r".*registry.*|.*ledger.*|.*index.*\.json$|mapping\.json|proof-objects\.json|glossary\.json)")
    file2 = collections.defaultdict(set)
    decl2 = collections.defaultdict(set)
    for p in prs:
        n = p["number"]
        for f in p["files"]:
            if not SHARED_OK.search(f["filename"]):
                file2[f["filename"]].add(n)
        for fn, s in scan_res.get(str(n), {}).get("lean_files", {}).items():
            if s.get("identical_on_main"):
                continue
            for d in s["decls"]:
                if d["kind"] in ("theorem", "lemma", "def", "structure", "class", "abbrev") and d["name"]:
                    decl2[d["name"]].add(n)
    bean2 = collections.defaultdict(set)
    for p in prs:
        p["beans"] = sorted(set("qou-" + b for b in BEAN_RE.findall(p["title"] + " " + p["head"]))
                            or set("qou-" + b for b in BEAN_RE.findall(p["body"][:3000])))
        for b in p["beans"]:
            bean2[b].add(p["number"])

    rows = []
    for p in prs:
        n = p["number"]
        s = scan_res.get(str(n), {})
        lf = s.get("lean_files", {})
        tot = collections.Counter()
        flagged_decls, provable = 0, 0
        for fn, x in lf.items():
            if x.get("identical_on_main"):
                continue
            for k, v in x["counts"].items():
                tot[k] += v
            tot["import_free_files"] += 0 if x["counts"].get("imports_qou_or_mathlib") else 1
            for d in x["decls"]:
                if d["kind"] in ("theorem", "lemma"):
                    provable += 1
                    if set(d["flags"]) & {"true-conclusion", "tautology", "rfl-only-on-local-def"}:
                        flagged_decls += 1
        new_lean = [fn for fn, x in lf.items() if not x.get("identical_on_main")]
        same_lean = [fn for fn, x in lf.items() if x.get("identical_on_main")]
        bstat = {b: beans.get(b, {"status": "missing", "pr": None}) for b in p["beans"]}
        done_elsewhere = [b for b, v in bstat.items()
                          if v["status"] in ("completed", "scrapped") and v.get("pr") not in (n,)]
        # collisions with other OPEN batch PRs
        file_coll = sorted({m for f in p["files"] if f["filename"] in file2
                            for m in file2[f["filename"]] if m != n})
        decl_coll = sorted({m for fn, x in lf.items() if not x.get("identical_on_main")
                            for d in x["decls"] if d["name"] in decl2
                            for m in decl2[d["name"]] if m != n})
        bean_coll = sorted({m for b in p["beans"] for m in bean2[b] if m != n})
        newer_dupe = [m for m in set(decl_coll) | set(bean_coll) if m > n]
        dps = s.get("dps", [])
        lean = lean_res.get(str(n), {"status": "not-run", "reason": "no lean toolchain/oleans in this container"})

        reasons, verdict = [], None
        nlean = len(new_lean)
        vac_ratio = flagged_decls / provable if provable else 0.0
        if p["files"] and nlean == 0 and same_lean:
            verdict = "CLOSE-SUPERSEDED"; reasons.append("all Lean files already byte-identical on main")
        elif p["beans"] and len(done_elsewhere) == len(p["beans"]) and done_elsewhere:
            verdict = "CLOSE-SUPERSEDED"; reasons.append("every cited bean completed/scrapped via another PR: " + ",".join(done_elsewhere))
        elif provable and (tot["true-conclusion"] + tot["tautology"]) and vac_ratio >= 0.5:
            verdict = "CLOSE-VACUOUS"; reasons.append(f"{flagged_decls}/{provable} theorems True/tautology/rfl-on-local-def")
        elif provable and vac_ratio >= 0.8:
            verdict = "CLOSE-VACUOUS"; reasons.append(f"{flagged_decls}/{provable} theorems rfl-only on locally-defined defs")
        if verdict is None:
            if p["mergeable"] is False or p["mergeable_state"] == "dirty":
                reasons.append("conflicts with main")
            if tot["sorry"]:
                reasons.append(f"{tot['sorry']} real sorry")
            if tot["axiom"]:
                reasons.append(f"{tot['axiom']} axiom")
            if tot["native_decide"]:
                reasons.append(f"{tot['native_decide']} native_decide")
            if tot["true-conclusion"] or tot["true-field"] or tot["tautology"]:
                reasons.append(f"vacuity flags True/field/taut={tot['true-conclusion']}/{tot['true-field']}/{tot['tautology']}")
            if provable and vac_ratio >= 0.5:
                reasons.append(f"{flagged_decls}/{provable} rfl-only-on-local-def")
            if tot["import_free_files"]:
                reasons.append(f"{tot['import_free_files']} import-free .lean")
            if dps and min(dps) < 80 and re.search(r"80[- ]dps", p["body"]):
                reasons.append(f"claims 80-dps, min dps found {min(dps)}")
            if done_elsewhere:
                reasons.append("partly superseded beans: " + ",".join(done_elsewhere))
            if decl_coll:
                reasons.append("decl collision with " + ",".join(f"#{m}" for m in decl_coll[:6]))
            if s.get("scan_error"):
                reasons.append("scan: " + s["scan_error"][:60])
            if not lf and not p["files"]:
                reasons.append("empty PR")
            if lean.get("status") == "fail":
                reasons.append("lean-direct FAIL")
            verdict = "NEEDS-REWORK" if reasons else "MERGE-CANDIDATE"
        rows.append({
            "number": n, "head": p["head"], "family": p["family"], "created_at": p["created_at"],
            "title": p["title"][:160], "beans": p["beans"], "bean_status": bstat,
            "mergeable": p["mergeable"], "mergeable_state": p["mergeable_state"],
            "changed_files": p["changed_files"], "additions": p["additions"], "deletions": p["deletions"],
            "lean_files_new_or_changed": new_lean, "lean_files_identical_on_main": same_lean,
            "provable_decls": provable, "vacuity_flagged_decls": flagged_decls,
            "counts": dict(tot), "dps": sorted(set(dps)),
            "file_collisions": file_coll, "decl_collisions": decl_coll, "bean_collisions": bean_coll,
            "newer_duplicate_prs": sorted(newer_dupe),
            "lean": lean, "verdict": verdict, "reasons": reasons,
        })
    return rows


def report(args):
    rows = classify(args)
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    agg = collections.Counter(r["verdict"] for r in rows)
    fam = collections.defaultdict(collections.Counter)
    for r in rows:
        fam[r["family"]][r["verdict"]] += 1
    meta = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "main": git("rev-parse", "origin/main").strip(),
            "script": "scripts/batch-pr-triage.py", "n": len(rows), "verdicts": dict(agg),
            "by_family": {k: dict(v) for k, v in fam.items()}}
    out.with_suffix(".json").write_text(json.dumps({"meta": meta, "rows": rows}, indent=1) + "\n")
    cands = sorted([r for r in rows if r["verdict"] == "MERGE-CANDIDATE"], key=lambda r: r["created_at"])
    L = []
    L.append(f"# Batch-formalization PR triage — {meta['generated'][:10]}\n")
    L.append(f"Generated by `{meta['script']}` against `origin/main` = `{meta['main'][:10]}`. "
             f"JSON twin: `{out.with_suffix('.json').name}`. **Read-only triage: no PR was merged, closed or commented on.**\n")
    L.append("Verdicts are heuristic and STATIC unless the `lean` column says `pass`/`fail`; "
             "a MERGE-CANDIDATE still owes the Phase-4 gate (`lean`-direct exit 0 against the real import cone + "
             "`#print axioms` no `sorryAx`). Sorry-free is not derived (AGENTS.md); a `rfl`/`norm_num` "
             "proof about a definition introduced in the same file is flagged `rfl-only-on-local-def` — it may be "
             "honest notation-checking, but it is not a derivation.\n")
    L.append("## Aggregate\n")
    L.append("| verdict | count |\n|---|---:|")
    for k in ("MERGE-CANDIDATE", "NEEDS-REWORK", "CLOSE-SUPERSEDED", "CLOSE-VACUOUS"):
        L.append(f"| {k} | {agg.get(k, 0)} |")
    L.append(f"| **total** | **{len(rows)}** |\n")
    L.append("| family | " + " | ".join(("MERGE", "REWORK", "SUPERSEDED", "VACUOUS")) + " |\n|---|---:|---:|---:|---:|")
    for k, v in sorted(fam.items()):
        L.append(f"| `{k}` | {v['MERGE-CANDIDATE']} | {v['NEEDS-REWORK']} | {v['CLOSE-SUPERSEDED']} | {v['CLOSE-VACUOUS']} |")
    rc = collections.Counter()
    for r in rows:
        for x in r["reasons"]:
            rc[re.sub(r"[\d#,]+.*$", "", x).strip() or x[:30]] += 1
    L.append("\n## Reason frequency (NEEDS-REWORK / CLOSE-*)\n")
    L.append("| reason | PRs |\n|---|---:|")
    for k, v in rc.most_common(25):
        L.append(f"| {k} | {v} |")
    L.append("\n## MERGE-CANDIDATEs (oldest first)\n")
    L.append("| PR | created | beans | files | +/- | thm | flagged | dps | lean |\n|---|---|---|---:|---|---:|---:|---|---|")
    for r in cands:
        L.append(f"| #{r['number']} | {r['created_at'][:10]} | {' '.join(r['beans'][:5])} | {r['changed_files']} | "
                 f"+{r['additions']}/-{r['deletions']} | {r['provable_decls']} | {r['vacuity_flagged_decls']} | "
                 f"{','.join(map(str, r['dps'])) or '-'} | {r['lean']['status']} |")
    L.append("\n## Full table\n")
    L.append("| PR | family | mergeable | beans (status) | lean files | thm/flag | sorry/ax | collisions | verdict | why |\n"
             "|---|---|---|---|---:|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: r["number"]):
        bs = " ".join(f"{b}({v['status'][:4]})" for b, v in list(r["bean_status"].items())[:6])
        coll = ",".join(f"#{m}" for m in (r["decl_collisions"] or r["file_collisions"])[:4])
        L.append(f"| #{r['number']} | `{r['family']}` | {r['mergeable_state']} | {bs} | {len(r['lean_files_new_or_changed'])} | "
                 f"{r['provable_decls']}/{r['vacuity_flagged_decls']} | {r['counts'].get('sorry', 0)}/{r['counts'].get('axiom', 0)} | "
                 f"{coll} | {r['verdict']} | {'; '.join(r['reasons'])[:180]} |")
    out.with_suffix(".md").write_text("\n".join(L) + "\n")
    print(json.dumps(meta, indent=1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["gather", "fetch", "scan", "report", "all"])
    ap.add_argument("--out", default=f"docs/coordination/{time.strftime('%Y-%m-%d')}-batch-pr-triage")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    if a.stage in ("gather", "all"):
        gather(a)
    if a.stage in ("fetch", "all"):
        fetch(a)
    if a.stage in ("scan", "all"):
        scan(a)
    if a.stage in ("report", "all"):
        report(a)


if __name__ == "__main__":
    main()
