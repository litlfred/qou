#!/usr/bin/env python3
# polynomial_q_not_applicable: build-hygiene audit over producer source.
"""Find producers that return their OWN prior output, and score how they gate it.

MOTIVATION, from a real incident. `chi_via_rust_lossless.py` reused a cached
witness whenever it was COMPLETE (all λ present, not partial) and on nothing
else. A cache computed under a superseded convention is complete, so it was
served forever; and the hit still called `_stamp_anchor`, rewriting the file.
A routine re-run therefore looked like a refresh — new mtime, modified in
`git status` — while every number stayed stale. Two witnesses sat at convention
C across the 2026-08-09 cascade for exactly this reason, and nothing could have
fixed them short of deleting the cache by hand.

The generalisation: **a completeness gate answers "is this cache finished?" and
gets read as "is this cache current?"**. Those differ precisely when a
convention or an anchor moves underneath the cache — the case where being wrong
costs most.

WHAT IT LOOKS FOR — shape, not wording. A function containing an
`if <path>.exists()` test whose body both READS the file and RETURNS early,
where that same path is also WRITTEN somewhere in the module. The write is what
separates a self-cache from an ordinary upstream loader; without it, reading a
witness and returning is just normal consumption.

WHAT A HIT IS NOT. Most self-caches are fine and this audit is expected to be
mostly green. Three designs make one safe, and all three appear in this corpus:

  * scratch storage — /tmp, a dotfile, or .cache/, none of it committed, so a
    stale entry costs a recompute and never reaches a reader;
  * explicit opt-in — `_b0vf_complete_he4_witness` reuses only under
    `B0VF_REUSE_RAW=1`, so the default path recomputes;
  * a key that carries the inputs — `hecke_3a_weights._cache_key` hashes Q0
    into the filename, so a q₀ change invalidates the cache by construction.

The dangerous combination is a COMMITTED artifact behind an
existence-or-completeness gate with no opt-out. Measured 2026-08-24: 8 hits, of
which exactly one (`chi_via_rust_lossless`, since fixed with `--fresh`) was in
that combination.

RESIDUAL GAP, unfixed and worth knowing: a Q0-keyed hash invalidates on a q₀
change but NOT on a convention change at the same q₀. No cache in this corpus
keys on the trace convention.

Usage:  python3 computations/audits/self_caching_producer_audit.py [--root .]
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import sys

READ_METHODS = ("read_text", "load", "loads")
WRITE_METHODS = ("write_text", "write_bytes", "open")
GATE_WORDS = ("partial", "complete", "n_partitions", "total", "fresh",
              "hash", "sha", "mtime", "environ", "getenv", "q0", "anchor")


def _calls(node: ast.AST, *names: str) -> bool:
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Attribute) and f.attr in names:
                return True
            if isinstance(f, ast.Name) and f.id in names:
                return True
    return False


def _names(node: ast.AST) -> set[str]:
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def scan_module(path: pathlib.Path) -> list[dict]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return []

    written: set[str] = set()
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr in WRITE_METHODS
                and isinstance(n.func.value, ast.Name)):
            written.add(n.func.value.id)

    out = []
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for node in ast.walk(fn):
            if not (isinstance(node, ast.If) and _calls(node.test, "exists")):
                continue
            reads = any(_calls(b, *READ_METHODS) for b in node.body)
            rets = any(isinstance(x, ast.Return)
                       for b in node.body for x in ast.walk(b))
            if not (reads and rets):
                continue
            guarded = _names(node.test) & written
            if not guarded:
                continue          # ordinary upstream loader, not a self-cache
            blob = ast.dump(node.test) + "".join(ast.dump(b) for b in node.body)
            out.append({
                "function": fn.name,
                "line": node.lineno,
                "path_var": sorted(guarded),
                "gate": [w for w in GATE_WORDS if w in blob],
            })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = pathlib.Path(args.root)

    scanned, hits = 0, []
    for p in sorted(root.rglob("computations/**/*.py")):
        if "_deprecated" in str(p):
            continue
        scanned += 1
        for h in scan_module(p):
            h["file"] = str(p.relative_to(root))
            hits.append(h)

    if scanned == 0:
        print(f"ERROR: scanned 0 producers under {root.resolve()} — wrong "
              "--root, or run from the repo root.\nA scan that examined "
              "nothing is NOT a clean tree.", file=sys.stderr)
        return 2

    bare = [h for h in hits if not h["gate"]]
    print("=" * 74)
    print("SELF-CACHING PRODUCERS — functions returning their own prior output")
    print("=" * 74)
    print(f"  producers scanned        : {scanned}")
    print(f"  self-caching branches    : {len(hits)}")
    print(f"  gated on existence ALONE : {len(bare)}")
    print()
    for h in hits:
        print(f"  {h['file']}:{h['line']}  {h['function']}()  on {h['path_var']}")
        print(f"       gate: {h['gate'] or 'existence only'}")
    print("\n  A hit is not a defect. Scratch storage, an explicit opt-in, and a")
    print("  key carrying the inputs are all safe — see the module docstring.")
    print("  The dangerous case is a COMMITTED artifact behind an")
    print("  existence-or-completeness gate with no opt-out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
