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
    r"^cat/round", r"^claude/round\d+-devacuify", r"^claude/round\d+-trd0-9nnz-fixes",
    r"^claude/round\d+-", r"^claude/qou-rtxm-",
    # multi-bean feat/<topic>-xxxx-xxxx-xxxx-xxxx(-xxxx) (same generator, 2026-11-17)
    r"^feat/[a-z0-9-]+?(?:-[a-z0-9]{4}){4,}$",
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
            if "(?:" in p:
                return "feat/<topic>-<4+ bean ids>"
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


CORE_IDENTS = set("""Int Nat ℤ ℕ ℚ ℝ ℂ R S Type Prop Sort True False Bool true false fun let in if then else
match with by at have show from this x y z a b c d e f g h k m n p q r s t u v w i j l o
Int.ofNat Nat.succ Nat.zero id Fin List Prod Option HAdd HMul HSub HPow Neg Eq Ne Iff And Or Not
abs max min Even Odd Int.natAbs Int.toNat List.sum List.length List.map List.range""".split())
RING_AXIOM_FIELDS = {"add_assoc", "mul_assoc", "mul_comm", "left_distrib", "add_left_neg", "zero_add", "one_mul"}
BIG_LIT = re.compile(r"(?<![\w.])\d{3,}(?![\w.])")


def _namespaced(code: str):
    """Yield (kind, fullname, text) with a light namespace/section stack."""
    events = []
    for m in re.finditer(r"^(namespace|section|end)\b[ \t]*([^\s]*)", code, re.M):
        events.append((m.start(), m.group(1), m.group(2)))
    decls = list(split_decls(code))
    starts = [m.start() for m in DECL_RE.finditer(code)]
    stack, ei, out = [], 0, []
    for (kind, name, text), st in zip(decls, starts):
        while ei < len(events) and events[ei][0] < st:
            _, ev, nm = events[ei]; ei += 1
            if ev in ("namespace", "section"):
                stack.append((ev, nm))
            elif stack:
                stack.pop()
        ns = ".".join(nm for ev, nm in stack if ev == "namespace" and nm)
        full = name if (not ns or name.startswith("_root_.")) else f"{ns}.{name}"
        out.append((kind, full.replace("_root_.", ""), text))
    return out


def scan_lean(text: str) -> dict:
    code = strip_comments(text)
    imports = re.findall(r"^import\s+(\S+)", code, re.M)
    r = collections.Counter()
    r["imports_qou_or_mathlib"] = int(any(i.startswith(("QOU", "Mathlib", "UGB")) for i in imports))
    r["imports_qou"] = int(any(i.startswith("QOU") for i in imports))
    r["sorry"] = len(re.findall(r"\bsorry\b", code))
    r["native_decide"] = len(re.findall(r"\bnative_decide\b", code))
    decls, local_defs, local_types = [], set(), set()
    nd = _namespaced(code)
    arith_defs = set()
    for kind, name, body in nd:
        short = name.split(".")[-1]
        if kind in ("def", "abbrev", "opaque", "instance"):
            local_defs.add(short)
            dsig, _, dbody = body.partition(":=")
            # a one-line INTEGER arithmetic expression (ℤ/ℕ only: a real/rational one-liner such as
            # z_D = q^3/(q^2+1) is often the genuine corpus formula, so it is NOT flagged)
            if (dbody.strip() and len(dbody.strip().splitlines()) <= 2
                    and re.fullmatch(r"[\w\s+\-*/^()0-9,.']*", dbody.strip())
                    and not re.search(r"\b(match|fun|if|let)\b", dbody)
                    and not re.search(r"[ℝℚℂ]|\b(Real|Complex|Rat)\b", dsig)
                    and not re.search(r"[A-Za-z]", re.sub(r"\b(Int|Nat|ℤ|ℕ)\b|[({\[][^:]*:", "", dsig.split(None, 2)[-1] if len(dsig.split()) > 2 else "").replace(short, ""))):
                arith_defs.add(short)
        if kind in ("structure", "class", "inductive"):
            local_types.add(short)
            fields = set(re.findall(r"^\s+(\w+)\s*:", body, re.M))
            if len(fields & RING_AXIOM_FIELDS) >= 4:
                r["reimplements_ring_axioms"] += 1
        if kind in ("def", "abbrev", "structure") or (kind == "instance"):
            r["big_literals_in_defs"] += len(BIG_LIT.findall(body))
    for kind, name, body in nd:
        r[f"n_{kind}"] += 1
        sig, _, proof = body.partition(":=")
        # statement = text after the first top-level ':' following the binders
        head = re.sub(r"^\S+\s+\S+", "", sig, count=1)
        depth, cut = 0, None
        for i, ch in enumerate(head):
            if ch in "([{⦃": depth += 1
            elif ch in ")]}⦄": depth -= 1
            elif ch == ":" and depth == 0:
                cut = i; break
        stmt = head[cut + 1:] if cut is not None else ""
        binders = set(re.findall(r"[({⦃\[]\s*([\w' ]+?)\s*:", head[:cut] if cut else ""))
        bnames = {w for b in binders for w in b.split()}
        fl = []
        if kind == "axiom":
            fl.append("axiom")
        if re.fullmatch(r"\s*True\s*", stmt or "x"):
            fl.append("true-conclusion")
        if kind in ("structure", "class") and re.search(r"\w+\s*:\s*True\b", body):
            fl.append("true-field")
        if kind in ("theorem", "lemma", "example"):
            m = re.fullmatch(r"\s*(.+?)\s*=\s*(.+?)\s*", stmt.replace("\n", " "))
            if m and m.group(1) == m.group(2):
                fl.append("tautology")
            idents = set(re.findall(r"[A-Za-z_][\w'.]*", stmt))
            used_local = {w.split(".")[-1] for w in idents} & (local_defs | local_types)
            if idents and not used_local and idents <= (CORE_IDENTS | bnames):
                fl.append("generic-identity")
            elif used_local and used_local <= arith_defs and \
                    {w.split(".")[-1] for w in idents} <= (CORE_IDENTS | bnames | arith_defs):
                fl.append("unfolds-int-arith-def")
            if TRIV_BODY.search(":=" + proof.rstrip()) and len(proof.strip().splitlines()) <= 3:
                fl.append("rfl-only-on-local-def" if used_local else "one-tactic")
                if used_local and (BIG_LIT.search(stmt) or re.search(r"canonical|ledger|census|count|audit", stmt, re.I)):
                    fl.append("ledger-literal")
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
    base = p.get("base_sha")
    out["conflict_candidates"] = []
    out["missing_qou_imports"] = []
    for f in p["files"]:
        fn = f["filename"]
        # a file the PR touches that ALSO changed on main since the PR's base
        # is where a textual conflict can be (GitHub only says "dirty").
        b = subprocess.run(["git", "-C", GITDIR, "rev-parse", f"{base}:{fn}"], capture_output=True, text=True)
        mm = subprocess.run(["git", "-C", GITDIR, "rev-parse", f"origin/main:{fn}"], capture_output=True, text=True)
        bid = b.stdout.strip() if b.returncode == 0 else "absent"   # rev-parse echoes the arg on failure
        mid = mm.stdout.strip() if mm.returncode == 0 else "absent"
        if base and bid != mid:
            out["conflict_candidates"].append(fn)
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
            pr_paths = {x["filename"] for x in p["files"]}
            for imp in s["imports"]:
                if imp.startswith("QOU."):
                    rel = "folio/quantum-observable-universe/lean/" + imp.replace(".", "/") + ".lean"
                    on_main = subprocess.run(["git", "-C", GITDIR, "cat-file", "-e", f"origin/main:{rel}"],
                                             capture_output=True).returncode == 0
                    if not on_main and rel not in pr_paths:
                        out["missing_qou_imports"].append(imp)
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



# ---------------------------------------------------------------------- lean
STD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
QOU_LEAN = "folio/quantum-observable-universe/lean/"


def _lean_env():
    """PATH/LEAN_PATH exactly as scripts/lean-direct-env.sh sets them."""
    out = subprocess.run(["bash", "-c", f"source {ROOT}/scripts/lean-direct-env.sh >/dev/null && "
                          "printf '%s\\n%s' \"$PATH\" \"$LEAN_PATH\""], capture_output=True, text=True)
    if out.returncode:
        return None
    path, lp = out.stdout.split("\n", 1)
    return {**os.environ, "PATH": path, "LEAN_PATH": lp.strip()}


def _module_of(fn: str):
    for root in ("folio/quantum-observable-universe/lean/", "folio/unital-groebner-bases/lean/",
                 "folio/fred2005-formal-groups/lean/"):
        if fn.startswith(root) and re.match(r"[A-Z]", fn[len(root):]):
            return fn[len(root):-5].replace("/", ".")
    return None


def lean_one(p: dict, env: dict, timeout: int) -> dict:
    n, sha = p["number"], p["head_sha"]
    work = CACHE / "lean" / str(n)
    subprocess.run(["rm", "-rf", str(work)])
    (work / "src").mkdir(parents=True)
    files = [f["filename"] for f in p["files"] if f["filename"].endswith(".lean")
             and f["status"] != "removed" and not f["filename"].endswith("lean/QOU.lean")]
    if not files:
        return {"status": "no-lean"}
    texts = {fn: git("show", f"{sha}:{fn}") for fn in files}
    mods = {_module_of(fn): fn for fn in files if _module_of(fn)}
    # order: a changed module imported by another changed file compiles first, into a
    # hard-linked shadow of the QOU olean tree (a partial root would SHADOW the full one).
    deps = {fn: [m for m in re.findall(r"^import\s+(\S+)", strip_comments(texts[fn]), re.M) if m in mods]
            for fn in files}
    order, seen = [], set()

    def visit(fn, stack=()):
        if fn in seen or fn in stack:
            return
        for m in deps[fn]:
            visit(mods[m], stack + (fn,))
        seen.add(fn); order.append(fn)
    for fn in files:
        visit(fn)
    lenv = dict(env)
    need_shadow = any(deps[fn] for fn in files)
    if need_shadow:
        shadow = work / "olean"
        src_tree = ROOT / QOU_LEAN / ".lake/build/lib/lean"
        shadow.mkdir()
        subprocess.run(["cp", "-al", str(src_tree / "QOU"), str(shadow / "QOU")], check=False)
        if (src_tree / "QOU.olean").exists():
            subprocess.run(["cp", "-al", str(src_tree / "QOU.olean"), str(shadow / "QOU.olean")])
        lenv["LEAN_PATH"] = lenv["LEAN_PATH"].replace(str(src_tree), str(shadow))
    res = {"status": "pass", "files": {}, "axioms": {}, "sorryAx": [], "nonstandard_axioms": {},
           "compiled_against": "restored olean snapshot (see report caveat)"}
    for fn in order:
        code = texts[fn]
        sc = scan_lean(code)
        names = [d["name"] for d in sc["decls"] if d["kind"] in ("theorem", "lemma") and d["name"]
                 and not d["name"].startswith("private")]
        nlines = code.count("\n") + 1
        aug = code.rstrip("\n") + "\n\n" + "".join(f"#print axioms {x}\n" for x in names)
        dst = work / "src" / fn
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(aug)
        cmd = ["lean", "-DautoImplicit=false", "-s", "65536", str(dst)]
        m = _module_of(fn)
        if need_shadow and m and any(m in deps[g] for g in files):
            target = work / "olean" / (m.replace(".", "/") + ".olean")
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                target.unlink()  # never write through a hard link into the real tree
            pkgroot = work / "src" / fn[: len(fn) - len(m.replace(".", "/") + ".lean")]
            cmd[1:1] = [f"--root={pkgroot}", "-o", str(target)]
        t0 = time.time()
        try:
            pr = subprocess.run(cmd, capture_output=True, text=True, env=lenv, timeout=timeout)
            out, rc = pr.stdout + pr.stderr, pr.returncode
        except subprocess.TimeoutExpired:
            res["files"][fn] = {"status": "timeout", "secs": timeout}
            res["status"] = "timeout"
            continue
        errs = [l for l in out.splitlines() if re.search(r":\d+:\d+: error", l)]
        body_errs = [l for l in errs if int(re.search(r":(\d+):\d+: error", l).group(1)) <= nlines]
        missing = re.findall(r"object file '?\S*?/([\w/]+)\.olean'? of module (\S+) does not exist", out)
        st = "pass"
        if rc < 0:      # killed by a signal (OOM with two Mathlib-sized processes): not a verdict
            st = "killed"
        elif missing and not [e for e in body_errs if "object file" not in e]:
            st = "blocked"
        elif body_errs or (rc and not errs):
            st = "fail"
        for mm in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", out):
            ax = [a.strip() for a in mm.group(2).split(",") if a.strip()]
            res["axioms"][mm.group(1)] = ax
            if "sorryAx" in ax:
                res["sorryAx"].append(mm.group(1))
            ns = [a for a in ax if a not in STD_AXIOMS and a != "sorryAx"]
            if ns:
                res["nonstandard_axioms"][mm.group(1)] = ns
        for mm in re.finditer(r"'([^']+)' does not depend on any axioms", out):
            res["axioms"][mm.group(1)] = []
        res["files"][fn] = {"status": st, "secs": round(time.time() - t0, 1), "rc": rc,
                            "errors": body_errs[:5], "tail": "" if rc == 0 else out[-400:], "missing_olean": [x[1] for x in missing][:5],
                            "print_axioms_unresolved": len(errs) - len(body_errs)}
        if st != "pass" and res["status"] in ("pass", "timeout"):
            res["status"] = st
            if body_errs:
                res["first_error"] = re.sub(r"^.*?/src/", "", body_errs[0])
            elif missing:
                res["first_error"] = "snapshot lacks olean: " + missing[0][1]
            else:
                res["first_error"] = out.strip().splitlines()[-1][:200] if out.strip() else f"rc={rc}"
    if res["sorryAx"] and res["status"] == "pass":
        res["status"] = "fail"
        res["first_error"] = "sorryAx in " + res["sorryAx"][0]
    res["theorems_checked"] = len(res["axioms"])
    return res


def lean_stage(args):
    env = _lean_env()
    if env is None:
        print("lean: no toolchain (scripts/lean-direct-env.sh failed) -- nothing recorded", flush=True)
        return
    prs = {p["number"]: p for p in load_prs()}
    lf = CACHE / "lean.json"
    done = json.loads(lf.read_text()) if lf.exists() else {}
    rows = classify(args)
    order = sorted((r for r in rows if r["verdict"] in ("MERGE-CANDIDATE", "NEEDS-REWORK")),
                   key=lambda r: (not r["mergeable"], r["created_at"]))
    def stale(n):
        c = done.get(str(n), {})
        return (args.refresh or c.get("head_sha") != prs[n]["head_sha"]
                or (args.retry_blocked and (c.get("status") in ("blocked", "killed")
                                            or any(v.get("status") in ("blocked", "killed")
                                                   for v in c.get("files", {}).values()))))
    todo = [r["number"] for r in order if stale(r["number"])]
    todo = todo[: args.max]
    print(f"lean: {len(todo)} PRs to check (cached {len(done)})", flush=True)
    t_end = time.time() + args.budget
    with cf.ThreadPoolExecutor(args.jobs) as ex:
        futs = {}
        for n in todo:
            futs[ex.submit(lean_one, prs[n], env, args.timeout)] = n
        for i, fu in enumerate(cf.as_completed(futs)):
            n = futs[fu]
            try:
                r = fu.result()
            except Exception as e:  # recorded, never reported as a pass
                r = {"status": "error", "first_error": str(e)[:200]}
            r["head_sha"] = prs[n]["head_sha"]
            done[str(n)] = r
            lf.write_text(json.dumps(done))
            print(f"  [{i+1}/{len(todo)}] #{n} {r['status']} thm={r.get('theorems_checked', 0)} "
                  f"sorryAx={len(r.get('sorryAx', []))} {r.get('first_error', '')[:80]}", flush=True)
            if time.time() > t_end:
                print("  budget exhausted; remaining PRs left not-run", flush=True)
                for f2 in futs:
                    f2.cancel()
                break



def lean_control(args):
    """For every file that FAILED, compile origin/main's version of the same path with
    the same toolchain and olean snapshot. Main red too => the failure is not the PR's
    (pre-existing on main, or an artifact of the snapshot); main green => the PR broke it."""
    env = _lean_env()
    lf = CACHE / "lean.json"
    done = json.loads(lf.read_text())
    jobs = []
    for n, r in done.items():
        for fn, v in r.get("files", {}).items():
            if v["status"] == "fail" and "main_control" not in v:
                jobs.append((n, fn))
    print(f"control: {len(jobs)} failed files", flush=True)

    def one(job):
        n, fn = job
        mt = subprocess.run(["git", "-C", GITDIR, "show", f"origin/main:{fn}"], capture_output=True, text=True)
        if mt.returncode:
            return job, "absent-on-main"
        dst = CACHE / "lean" / "control" / fn
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(mt.stdout)
        try:
            pr = subprocess.run(["lean", "-DautoImplicit=false", "-s", "65536", str(dst)],
                                capture_output=True, text=True, env=env, timeout=args.timeout)
        except subprocess.TimeoutExpired:
            return job, "timeout"
        out = pr.stdout + pr.stderr
        if "object file" in out and "does not exist" in out:
            return job, "blocked"
        return job, "pass" if pr.returncode == 0 and ": error" not in out else "fail"

    cache = {}
    with cf.ThreadPoolExecutor(args.jobs) as ex:
        for (n, fn), st in ex.map(one, [j for j in jobs if j[1] not in cache]):
            done[n]["files"][fn]["main_control"] = st
            print(f"  #{n} {fn.rsplit('/', 1)[-1]}: main {st}", flush=True)
    for n, r in done.items():
        fails = [v for v in r.get("files", {}).values() if v["status"] == "fail"]
        if fails and all(v.get("main_control") in ("fail", "blocked") for v in fails):
            r["fail_also_on_main"] = True
    lf.write_text(json.dumps(done))

# --------------------------------------------------------------------- beans
# A bean whose title is about tooling/QA/bookkeeping, not mathematics. A Lean
# file "formalizing" such a bean can only restate the measured counts.
INFRA_RE = re.compile(r"\b(gate|witness|sidecar|audit|census|script|CI\b|drift|stale|stamp|refresh|registry|hook|"
                      r"ledger|detector|scanner|producer|AGENTS|doc(?:s|umentation)?\b|float64|regex|grep|"
                      r"dashboard|harness|pipeline|validator|checker|backlog|queue|sweep|mirror|vendor|cache)", re.I)
def load_beans():
    beans = {}
    for f in BEANS.glob("*.md"):
        head = f.read_text(errors="replace")[:1500]
        m = re.search(r"^#\s*(qou-[0-9a-z]{4})", head, re.M) or re.match(r"(qou-[0-9a-z]{4})", f.name)
        bid = m.group(1) if m else "qou-" + f.name[:4]
        st = re.search(r"^status:\s*(\S+)", head, re.M)
        pr = re.search(r"^pr:\s*(\d+)", head, re.M)
        ti = re.search(r"^title:\s*(.+)$", head, re.M)
        title = ti.group(1).strip().strip("'\"") if ti else ""
        beans[bid] = {"status": st.group(1) if st else "?", "pr": int(pr.group(1)) if pr else None,
                      "title": title[:140], "infra": bool(INFRA_RE.search(title))}
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
            if s.get("identical_on_main") or fn.endswith("lean/QOU.lean"):
                continue
            for d in s["decls"]:
                if d["kind"] in ("theorem", "lemma", "def", "structure", "class", "abbrev") and "." in d["name"]:
                    decl2[d["name"]].add(n)
    bean2 = collections.defaultdict(set)
    for p in prs:
        p["beans"] = sorted(set("qou-" + b for b in BEAN_RE.findall(p["title"] + " " + p["head"] + " " + p["body"][:4000])))
        for b in p["beans"]:
            bean2[b].add(p["number"])

    # bean sets per PR, for "a newer PR re-does exactly these beans"
    # umbrella/epic beans (cited by many PRs, e.g. qou-6qbv, qou-10v9, qou-8lxd) say nothing
    # about which leaf work a PR does; compare leaf sets only.
    umbrella = {b for b, ns in bean2.items() if len(ns) >= 6}
    beanset = {p["number"]: frozenset(set(p["beans"]) - umbrella) for p in prs}
    AGG = re.compile(r"(^|/)QOU\.lean$|(^|/)[A-Z]\w+\.lean$")  # aggregator import lists
    rows = []
    for p in prs:
        n = p["number"]
        s = scan_res.get(str(n), {})
        lf = {fn: x for fn, x in s.get("lean_files", {}).items() if not fn.endswith("lean/QOU.lean")}
        tot = collections.Counter()
        provable = generic = ledger = flagged = arith = 0
        new_lean = [fn for fn, x in lf.items() if not x.get("identical_on_main")]
        same_lean = [fn for fn, x in lf.items() if x.get("identical_on_main")]
        standalone = bool(new_lean)
        for fn in new_lean:
            x = lf[fn]
            for k, v in x["counts"].items():
                tot[k] += v
            if x["counts"].get("imports_qou_or_mathlib"):
                standalone = False
            else:
                tot["import_free_files"] += 1
            for d in x["decls"]:
                if d["kind"] in ("theorem", "lemma"):
                    provable += 1
                    fs = set(d["flags"])
                    if "generic-identity" in fs:
                        generic += 1
                    if fs & {"true-conclusion", "tautology", "rfl-only-on-local-def", "ledger-literal"}:
                        ledger += 1
                    if "unfolds-int-arith-def" in fs:
                        tot["unfolds_arith"] += 1
                    if fs & {"true-conclusion", "tautology", "rfl-only-on-local-def", "unfolds-int-arith-def"}:
                        arith += 1
                    if fs & {"generic-identity", "true-conclusion", "tautology", "rfl-only-on-local-def",
                             "unfolds-int-arith-def"}:
                        flagged += 1
        vac = flagged / provable if provable else 0.0          # counts generic identities (standalone only)
        arith_ratio = arith / provable if provable else 0.0    # named one-line arithmetic, rfl on local defs, True
        bstat = {b: beans.get(b, {"status": "missing", "pr": None, "title": "", "infra": False}) for b in p["beans"]}
        infra_frac = (sum(1 for v in bstat.values() if v.get("infra")) / len(bstat)) if bstat else 0.0
        done_elsewhere = [b for b, v in bstat.items()
                          if v["status"] in ("completed", "scrapped") and v.get("pr") not in (n, None)]
        file_coll = sorted({m for f in p["files"] if f["filename"] in file2
                            for m in file2[f["filename"]] if m != n})
        decl_coll = sorted({m for fn in new_lean for d in lf[fn]["decls"] if d["name"] in decl2
                            for m in decl2[d["name"]] if m != n})
        bean_coll = sorted({m for b in p["beans"] if b not in umbrella for m in bean2[b] if m != n})
        newer_same_beans = sorted(m for m in bean_coll if m > n and beanset[n] and beanset[n] <= beanset[m])
        dps = s.get("dps", [])
        cc = s.get("conflict_candidates", [])
        cc_code = [f for f in cc if not (AGG.search(f) and f.endswith(".lean") and f.count("/") <= 4)
                   and not f.startswith("beans/")]
        lean = lean_res.get(str(n), {"status": "not-run", "reason": "not reached in this run"})
        dirty = p["mergeable"] is False or p["mergeable_state"] == "dirty"

        # theorems ADDED by the diff (the per-file counts above include pre-existing ones)
        added_thm = sub_restate = 0
        for f in p["files"]:
            if f["filename"].endswith(".lean") and not f["filename"].endswith("lean/QOU.lean"):
                for l in f.get("patch", "").splitlines():
                    if re.match(r"^\+\s*(?:@\[[^\]]*\]\s*)?(?:private\s+)?(theorem|lemma) ", l):
                        added_thm += 1
                        if re.search(r"_sub_eq_zero\b|_sub_self\b", l):
                            sub_restate += 1
        signals = []
        if sub_restate:
            signals.append(f"{sub_restate}/{added_thm} added theorems are `_sub_eq_zero` restatements of existing equalities")
        if standalone:
            signals.append("standalone (no Mathlib/QOU import)")
        if tot["reimplements_ring_axioms"]:
            signals.append("re-implements ring axioms as a structure")
        if provable and generic:
            signals.append(f"{generic}/{provable} generic Int/R identities unrelated to the named objects")
        if provable and ledger:
            signals.append(f"{ledger}/{provable} rfl/decide on locally-defined literal ledgers")
        if tot["big_literals_in_defs"] >= 5:
            signals.append(f"{tot['big_literals_in_defs']} hardcoded >=3-digit literals in defs")
        if tot["unfolds_arith"]:
            signals.append(f"{tot['unfolds_arith']}/{provable} theorems unfold one-line Int arithmetic defs")
        if infra_frac >= 0.5:
            signals.append(f"{infra_frac:.0%} of cited beans are tooling/QA tasks"
                           + (" -- bean attribution does not match the Lean content; do not close these beans on merge"
                              if provable and not standalone else ""))

        reasons, verdict, rework_kind = [], None, None
        if p["files"] and not new_lean and same_lean and not any(
                f["filename"].endswith((".py", ".json")) and f["status"] != "removed" for f in p["files"]):
            verdict = "CLOSE-SUPERSEDED"; reasons.append("all Lean files already byte-identical on main")
        elif p["beans"] and done_elsewhere and len(done_elsewhere) == len(p["beans"]):
            verdict = "CLOSE-SUPERSEDED"; reasons.append("every cited bean completed/scrapped via another PR: " + ",".join(done_elsewhere))
        elif newer_same_beans:
            verdict = "CLOSE-SUPERSEDED"; reasons.append("a newer open PR cites the same bean set: " + ",".join(f"#{m}" for m in newer_same_beans[:4]))
        elif provable and (tot["true-conclusion"] + tot["tautology"]) * 2 >= provable:
            verdict = "CLOSE-VACUOUS"; reasons.append(f"{tot['true-conclusion'] + tot['tautology']}/{provable} theorems conclude True or X = X")
        elif provable and arith_ratio >= 0.6:
            verdict = "CLOSE-VACUOUS"; reasons.append(f"{arith}/{provable} theorems unfold one-line arithmetic defs named after "
                                                      "corpus objects (or rfl/True on local literals): restatement, not derivation")
        elif standalone and provable and vac >= 0.6:
            verdict = "CLOSE-VACUOUS"; reasons.append(f"standalone file, {flagged}/{provable} theorems are generic Int identities, "
                                                      "unfoldings of one-line Int arithmetic defs, or rfl on local literals")
        elif standalone and infra_frac >= 0.5 and tot["big_literals_in_defs"] >= 5:
            verdict = "CLOSE-VACUOUS"; reasons.append("standalone file restating tooling-bean audit counts as Int literals")
        if verdict is None:
            if dirty:
                reasons.append("conflicts with main" + (f" ({', '.join(x.rsplit('/', 1)[-1] for x in cc_code[:3])})" if cc_code else " (aggregator/bean files only)"))
            if tot["sorry"]:
                reasons.append(f"{tot['sorry']} real sorry")
            if tot["axiom"]:
                reasons.append(f"{tot['axiom']} axiom")
            if tot["native_decide"]:
                reasons.append(f"{tot['native_decide']} native_decide")
            if tot["true-conclusion"] or tot["true-field"] or tot["tautology"]:
                reasons.append(f"vacuity True/field/taut={tot['true-conclusion']}/{tot['true-field']}/{tot['tautology']}")
            if standalone:
                reasons.append("standalone proxy: no Mathlib/QOU import, cannot reference the corpus objects it names")
            if provable and arith_ratio >= 0.3:
                reasons.append(f"{arith}/{provable} theorems unfold one-line arithmetic defs / rfl on local literals")
            if tot["reimplements_ring_axioms"]:
                reasons.append("re-implements ring axioms (§7c: use [CommRing R])")
            if added_thm and sub_restate * 5 >= added_thm * 3:
                reasons.append(f"{sub_restate}/{added_thm} added theorems only restate an existing `a = b` as `a - b = 0`")
            if s.get("missing_qou_imports"):
                reasons.append("imports modules not on main (stacked): " + ",".join(s["missing_qou_imports"][:3]))
            if dps and min(dps) < 80 and re.search(r"80[- ]dps", p["title"] + p["body"]):
                reasons.append(f"claims 80-dps, min dps found {min(dps)}")
            if done_elsewhere:
                reasons.append("partly superseded beans: " + ",".join(done_elsewhere))
            if s.get("scan_error"):
                reasons.append("scan: " + s["scan_error"][:60])
            if not p["files"]:
                reasons.append("empty PR")
            if lean.get("status") == "fail":
                tag = " (same file also red on main: not this PR's regression)" if lean.get("fail_also_on_main") else ""
                reasons.append("lean-direct FAIL" + tag + ": " + lean.get("first_error", "")[:100])
            if lean.get("status") == "blocked":
                reasons.append("lean-direct BLOCKED: olean snapshot lacks " + lean.get("first_error", "")[-60:])
            if lean.get("sorryAx") and lean.get("status") not in ("blocked", "fail"):
                reasons.append("#print axioms shows sorryAx")   # (in a failed/blocked file it is error recovery)
            verdict = "NEEDS-REWORK" if reasons else "MERGE-CANDIDATE"
            if verdict == "NEEDS-REWORK" and dirty and len(reasons) == 1 and not cc_code:
                rework_kind = "rebase-only"
        rows.append({
            "number": n, "head": p["head"], "family": p["family"], "created_at": p["created_at"],
            "title": p["title"][:160], "beans": p["beans"], "bean_status": bstat,
            "mergeable": p["mergeable"], "mergeable_state": p["mergeable_state"],
            "conflict_candidates": cc,
            "changed_files": p["changed_files"], "additions": p["additions"], "deletions": p["deletions"],
            "lean_files_new_or_changed": new_lean, "lean_files_identical_on_main": same_lean,
            "provable_decls": provable, "generic_identity_decls": generic, "ledger_decls": ledger,
            "added_theorems": added_thm, "sub_eq_zero_restatements": sub_restate,
            "vacuity_flagged_decls": flagged, "arith_proxy_decls": arith, "standalone": standalone, "signals": signals,
            "counts": dict(tot), "dps": sorted(set(dps)), "py_float64_hits": s.get("py_float64_hits", 0),
            "missing_qou_imports": s.get("missing_qou_imports", []),
            "file_collisions": file_coll, "decl_collisions": decl_coll, "bean_collisions": bean_coll,
            "newer_same_bean_prs": newer_same_beans,
            "lean": lean, "verdict": verdict, "rework_kind": rework_kind, "reasons": reasons,
        })
    # second pass: a PR that touches the same code file / declaration as an OLDER open PR
    # which is itself not being closed must wait for that one and rebase (merge order =
    # oldest first). Collisions only with newer PRs do not block this one.
    verdict_of = {r["number"]: r["verdict"] for r in rows}
    for r in rows:
        if r["verdict"] not in ("MERGE-CANDIDATE", "NEEDS-REWORK"):
            continue
        older = sorted({m for m in r["file_collisions"] + r["decl_collisions"]
                        if m < r["number"] and verdict_of.get(m) in ("MERGE-CANDIDATE", "NEEDS-REWORK")})
        r["blocked_by_older"] = older
        if older:
            r["reasons"].append("touches the same file/declaration as older open PR " + ",".join(f"#{m}" for m in older[:6])
                                + ": rebase after it lands")
            if r["verdict"] == "MERGE-CANDIDATE":
                r["verdict"] = "NEEDS-REWORK"
            r["rework_kind"] = None
    return rows


def _ev(r):
    """One-line evidence string for a row."""
    lean = r["lean"]
    st = lean.get("status", "not-run")
    if st in ("pass", "fail", "blocked", "timeout"):
        ax = set()
        for v in lean.get("axioms", {}).values():
            ax |= set(v)
        ev = f"lean-direct {st}, {lean.get('theorems_checked', 0)} thm `#print axioms`: {{{', '.join(sorted(ax)) or 'none'}}}"
        if lean.get("nonstandard_axioms"):
            ev += f", NON-STANDARD in {len(lean['nonstandard_axioms'])}"
        if lean.get("sorryAx") and st == "pass":
            ev += f", sorryAx in {len(lean['sorryAx'])}"
    elif st == "no-lean":
        ev = "no Lean in PR (compute/QA only: precision-gates owed)"
    else:
        ev = "lean not run"
    return ev


def report(args):
    rows = classify(args)
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    agg = collections.Counter(r["verdict"] for r in rows)
    fam = collections.defaultdict(collections.Counter)
    for r in rows:
        fam[r["family"]][r["verdict"]] += 1
    lean_st = collections.Counter(r["lean"].get("status", "not-run") for r in rows)
    meta = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "main": git("rev-parse", "origin/main").strip(),
            "script": "scripts/batch-pr-triage.py", "n": len(rows), "verdicts": dict(agg),
            "lean_status": dict(lean_st),
            "by_family": {k: dict(v) for k, v in fam.items()}}
    out.with_suffix(".json").write_text(json.dumps({"meta": meta, "rows": rows}, indent=1) + "\n")

    def cand_key(r):  # merge order: Lean-verified first, then oldest
        return (r["lean"].get("status") != "pass", r["created_at"])
    cands = sorted([r for r in rows if r["verdict"] == "MERGE-CANDIDATE"], key=cand_key)
    L = []
    L.append(f"# Batch-formalization PR triage — {meta['generated'][:10]}\n")
    L.append(f"Generated by `{meta['script']}` against `origin/main` = `{meta['main'][:10]}` at {meta['generated']}. "
             f"JSON twin: `{out.with_suffix('.json').name}` (one row per PR, every signal and reason). "
             "**Read-only triage: no batch PR was merged, closed or commented on.** The coordinator decides.\n")
    L.append("Rerun: `TRIAGE_CACHE=<dir> python3 scripts/batch-pr-triage.py gather && ... fetch && ... scan && "
             "... lean && ... control && ... report --out docs/coordination/<date>-batch-pr-triage`.\n")
    L.append("## Aggregate\n")
    L.append("| verdict | count |\n|---|---:|")
    for k in ("MERGE-CANDIDATE", "NEEDS-REWORK", "CLOSE-SUPERSEDED", "CLOSE-VACUOUS"):
        L.append(f"| {k} | {agg.get(k, 0)} |")
    L.append(f"| **total** | **{len(rows)}** |\n")
    L.append("Lean-direct status over all rows: " + ", ".join(f"{k} {v}" for k, v in lean_st.most_common()) + ".\n")
    L.append("| family | PRs | MERGE | REWORK | SUPERSEDED | VACUOUS |\n|---|---:|---:|---:|---:|---:|")
    for k, v in sorted(fam.items(), key=lambda kv: -sum(kv[1].values())):
        L.append(f"| `{k}` | {sum(v.values())} | {v['MERGE-CANDIDATE']} | {v['NEEDS-REWORK']} | "
                 f"{v['CLOSE-SUPERSEDED']} | {v['CLOSE-VACUOUS']} |")
    rc = collections.Counter()
    for r in rows:
        for x in r["reasons"]:
            rc[re.sub(r"\s*\d+/\d+\s*", " N/M ", re.split(r"[:(]", x)[0]).strip()] += 1
    L.append("\n## Reason frequency\n")
    L.append("| reason (numbers normalised) | PRs |\n|---|---:|")
    for k, v in rc.most_common(20):
        L.append(f"| {k} | {v} |")
    L.append("\n## MERGE-CANDIDATEs (Lean-verified first, then oldest)\n")
    L.append("A MERGE-CANDIDATE is clean against `main`, has no static vacuity/sorry/axiom/collision flag, and "
             "(where `lean` = pass) its changed `.lean` files compile with `lean -DautoImplicit=false -s 65536` "
             "against the restored olean snapshot, every theorem's `#print axioms` taken. It is NOT a claim "
             "that the content is a derivation (sorry-free ≠ derived), and a dependent of a modified module "
             "is not re-checked.\n")
    L.append("| # | PR | created | Lean files | +thm | evidence | signals |\n|---:|---|---|---:|---:|---|---|")
    for i, r in enumerate(cands, 1):
        L.append(f"| {i} | #{r['number']} | {r['created_at'][:10]} | {len(r['lean_files_new_or_changed'])} | "
                 f"{r['added_theorems']} | {_ev(r)} | {'; '.join(r['signals'])[:200]} |")
    L.append("\n## Full table\n")
    L.append("| PR | family | merge | thm/arith | lean | verdict | why |\n|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: r["number"]):
        L.append(f"| #{r['number']} | `{r['family']}` | {r['mergeable_state']} | "
                 f"{r['provable_decls']}/{r.get('arith_proxy_decls', 0)} | {r['lean'].get('status', '-')} | "
                 f"{r['verdict']} | {'; '.join(r['reasons'])[:220]} |")
    body = "\n".join(L) + "\n"
    hdr = pathlib.Path(args.header) if getattr(args, "header", None) else None
    if hdr and hdr.exists():
        body = body.replace("## Aggregate\n", hdr.read_text().rstrip() + "\n\n## Aggregate\n", 1)
    out.with_suffix(".md").write_text(body)
    print(json.dumps({k: meta[k] for k in ("generated", "n", "verdicts", "lean_status")}, indent=1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["gather", "fetch", "scan", "lean", "control", "report", "all"])
    ap.add_argument("--retry-blocked", action="store_true", help="lean: re-run PRs that were blocked on a missing olean")
    ap.add_argument("--max", type=int, default=10000, help="lean: at most this many PRs")
    ap.add_argument("--jobs", type=int, default=2, help="lean: parallel lean processes")
    ap.add_argument("--timeout", type=int, default=900, help="lean: seconds per file")
    ap.add_argument("--budget", type=int, default=6 * 3600, help="lean: wall-clock budget, seconds")
    ap.add_argument("--out", default=f"docs/coordination/{time.strftime('%Y-%m-%d')}-batch-pr-triage")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--header", help="report: markdown file inserted before ## Aggregate (findings prose)")
    a = ap.parse_args()
    if a.stage in ("gather", "all"):
        gather(a)
    if a.stage in ("fetch", "all"):
        fetch(a)
    if a.stage in ("scan", "all"):
        scan(a)
    if a.stage == "lean":
        lean_stage(a)
    if a.stage == "control":
        lean_control(a)
    if a.stage in ("report", "all"):
        report(a)


if __name__ == "__main__":
    main()
