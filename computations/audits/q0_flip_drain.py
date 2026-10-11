#!/usr/bin/env python3
"""Drain the Q0_FLIP population by re-running its producers at the live anchor.

After #5500 landed, the muon anchor is DERIVED from the live CODATA-2022
m_mu/m_e rather than read from a frozen literal. Witnesses computed before that
still carry the superseded value A and are reported `Q0_FLIP` -- stamped `muon`
but disagreeing with what `muon` now means. #5921 measured the population:
74 of 83 have a producer that can be re-run.

This runs them. It is a DRAIN, so producer output is KEPT, not restored -- the
opposite of an audit run, where writing a witness is a side effect to undo.

The seven producer-runner conditions AGENTS.md records, all implemented,
because a runner missing any of them reports on itself rather than the corpus:

  1. PYTHONPATH set (qou_substrate is not importable from a bare invocation)
  2. skip scripts declaring required positionals
  3. isolate each run -- but for a DRAIN this means reverting only what a
     FAILED run touched, never cleaning beforehand: a blanket `git checkout`
     before each producer reverts the PREVIOUS producer's drained output, so
     only the last one survives. (Hit here first; the audit-flavoured version
     of this condition is wrong for a drain.)
  4. try BOTH cwd=<producer dir> and cwd=<repo root> (root-relative producers)
  5. capture STDOUT as well as stderr (guards explain themselves on stdout)
  6. check for a TRACEBACK rather than trusting the exit code (non-zero is
     often a guard working correctly, by design)
  7. check whether a traceback's exception type is a GUARD THE CORPUS DEFINES
     (a refusal raised as a domain exception is not a crash)

Plus one this population needs specifically: `scriptFile` is stored as a bare
basename in most witnesses and a repo-relative path in a few, so producers are
resolved through a basename index (#5921).
"""
from __future__ import annotations

import argparse
import ast
import collections
import glob
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
AUDIT = os.path.join(REPO, "computations/audits/q0-anchor-consistency-audit.witness.json")

# Exception types the corpus defines as refusals — a traceback ending in one of
# these is a guard working, not a defect (condition 7).
CORPUS_GUARDS = {
    "AmDifferenceInvalid", "PrecisionError", "AnchorCorruption",
    "WitnessPrecisionError", "FreeParameterError",
}


def env():
    e = dict(os.environ)
    e["PYTHONPATH"] = os.pathsep.join([
        os.path.join(REPO, "tools/qou-substrate/python"),
        os.path.join(REPO, "tools/pyhecke/python"),
        os.path.join(REPO, "computations"),
        e.get("PYTHONPATH", ""),
    ])
    return e


def needs_positional(path: str) -> bool:
    """Condition 2 — a producer requiring an argv we cannot supply."""
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except Exception:
        return False
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "add_argument"
                and n.args and isinstance(n.args[0], ast.Constant)
                and isinstance(n.args[0].value, str)
                and not n.args[0].value.startswith("-")):
            if not any(k.arg in ("nargs", "default") for k in n.keywords):
                return True
    return False


def dirty() -> list[str]:
    r = subprocess.run(["git", "status", "--porcelain", "computations"],
                       cwd=REPO, capture_output=True, text=True)
    return [l[3:] for l in r.stdout.splitlines() if l.strip()]


def clean():
    """Condition 3 — clean before as well as after."""
    subprocess.run(["git", "checkout", "--", "computations"], cwd=REPO,
                   capture_output=True)


def classify(out: str, rc: int) -> tuple[str, str]:
    """Conditions 5-7: read stdout+stderr, prefer traceback over exit code."""
    if "Traceback (most recent call last)" in out:
        last = [l for l in out.strip().splitlines() if l and not l.startswith(" ")]
        exc = last[-1].split(":")[0].strip() if last else "?"
        if exc.split(".")[-1] in CORPUS_GUARDS:
            return "GUARD", f"corpus-defined refusal: {exc}"
        return "CRASH", exc
    if rc != 0:
        return "REFUSED", f"exit {rc}, no traceback — guard or precondition"
    return "OK", ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default="/tmp/q0-flip-drain.json")
    a = ap.parse_args()

    flips = json.load(open(AUDIT))["data"]["by_verdict"].get("Q0_FLIP", [])
    widx, pidx = {}, {}
    for p in glob.glob(os.path.join(REPO, "computations/**/*.witness.json"), recursive=True):
        widx.setdefault(os.path.basename(p), []).append(p)
    for p in glob.glob(os.path.join(REPO, "computations/**/*.py"), recursive=True):
        pidx.setdefault(os.path.basename(p), []).append(p)

    producers: dict[str, list[str]] = collections.defaultdict(list)
    for r in flips:
        wp = widx.get(os.path.basename(r["witness"]), [])
        if not wp or ("_deprecated" in wp or "fsh-guts" in wp)[0]:
            continue
        sf = json.load(open(wp[0])).get("scriptFile")
        if not sf:
            continue
        c = pidx.get(os.path.basename(sf), [])
        if c:
            producers[c[0]].append(wp[0])

    todo = sorted(producers)
    if a.limit:
        todo = todo[:a.limit]
    print(f"producers to run: {len(todo)}  (timeout {a.timeout}s each)", flush=True)

    rows, verdicts, t0 = [], collections.Counter(), time.time()
    for i, prod in enumerate(todo, 1):
        rel = os.path.relpath(prod, REPO)
        if needs_positional(prod):
            verdicts["SKIP-positional"] += 1
            rows.append({"producer": rel, "verdict": "SKIP-positional"})
            print(f"[{i}/{len(todo)}] SKIP-positional  {rel}", flush=True)
            continue
        before = set(dirty())                      # condition 3, drain flavour
        best = None
        for cwd in (os.path.dirname(prod), REPO):  # condition 4, both cwds
            try:
                r = subprocess.run([sys.executable, "-u", prod], cwd=cwd, env=env(),
                                   capture_output=True, text=True, timeout=a.timeout)
                out = (r.stdout or "") + (r.stderr or "")   # condition 5
                v, d = classify(out, r.returncode)
            except subprocess.TimeoutExpired:
                v, d = "TIMEOUT", f">{a.timeout}s"
            if best is None or v == "OK":
                best = (v, d, dirty())
            if v == "OK":
                break
        v, d, changed = best
        changed = [f for f in changed if f not in before]
        verdicts[v] += 1
        rows.append({"producer": rel, "verdict": v, "detail": d,
                     "changed": changed, "n_changed": len(changed)})
        el = time.time() - t0
        print(f"[{i}/{len(todo)}] {v:<16} {rel[:56]:<58} "
              f"{len(changed)} file(s)  [{el/60:.1f}m, eta {el/i*(len(todo)-i)/60:.1f}m]",
              flush=True)
        if v != "OK":
            # revert ONLY what this run touched; never the accumulated drain
            stray = [f for f in dirty() if f not in before]
            if stray:
                subprocess.run(["git", "checkout", "--"] + stray, cwd=REPO,
                               capture_output=True)

    json.dump({"verdicts": dict(verdicts), "rows": rows}, open(a.out, "w"), indent=2)
    print("\n" + "=" * 62)
    for k, n in verdicts.most_common():
        print(f"  {k:<18} {n}")
    print(f"  wall {(time.time()-t0)/60:.1f} min   -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
