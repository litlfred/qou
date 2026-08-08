#!/usr/bin/env python3
# polynomial_q_not_applicable: orchestration over producers; emits no numeric physics.
"""Re-run every producer that declares an upstream, keeping only clean results.

Owner directive: NO FLOAT64 — this drives the regeneration that lands
`upstream_witness_hashes` in the witnesses whose producers now declare them.

## Why this is a committed tool

The first version of this driver lived in a scratch script, and both of its
failures came from that:

1. **It was bypassed.** Running producers by hand and then `git add -A` staged
   four unreviewed witnesses, one of them a 13/77 partial cache captured
   mid-rebuild. A guard outside the path being used is not a guard.
2. **It discarded its own successes.** Its revert reverted *every* dirty
   witness at the moment it fired, not the one under judgement — so each
   `VALUES` verdict also wiped the `DECLARED` and `ANCHOR_MIGRATION` results
   accumulated before it. The counters read `DECLARED 26 / ANCHOR_MIGRATION 4`
   at 90/163 while leaving a clean tree: the arithmetic was right and the
   retention was not.

Both are fixed here by construction: revert is **per witness**, and keeps are
tracked so a later revert can never touch them.

## Verdicts

Delegated to `witness_regen_classify`, so the policy lives in one place with
its own self-tests. `DECLARED` and `ANCHOR_MIGRATION` are kept; everything else
is reverted, per file.

## Serial by design

Producers write into the shared tree, so two of them in flight can revert each
other's output — exactly how a ⁴He rebuild was clobbered by a concurrent wave.
Never run this alongside anything else that writes a witness.

Usage:
    python3 computations/witness_regen_wave.py --dry-run
    python3 computations/witness_regen_wave.py --timeout 150 [--limit N]
    python3 computations/witness_regen_wave.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from witness_regen_classify import classify  # noqa: E402

KEEP = {"DECLARED", "ANCHOR_MIGRATION"}


def declares_upstream(source: str) -> bool:
    """True when the module declares an upstream by either spelling."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
            if name in {"add_upstream", "record_upstream"}:
                return True
    return False


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def dirty_witnesses() -> list[str]:
    out = git("status", "--porcelain", "computations/").stdout.splitlines()
    return [ln[3:] for ln in out if ln.strip().endswith(".witness.json")]


def revert(paths) -> None:
    """Revert exactly these paths. Never a directory, never everything dirty.

    The blanket form (`git checkout -- computations/`) is what made the previous
    driver throw away results it had already accepted, and would also undo
    ported producer sources.
    """
    paths = [p for p in paths if p]
    if paths:
        git("checkout", "--", *paths)


def producers() -> list[Path]:
    out = []
    for p in sorted((ROOT / "computations").rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if ".witness.json" in src and declares_upstream(src):
            out.append(p)
    return out


def judge(rel: str) -> str:
    """Classify one dirty witness against HEAD."""
    old_raw = git("show", f"HEAD:{rel}").stdout
    if not old_raw:
        return "NEW"
    try:
        return classify(json.loads(old_raw),
                        json.loads((ROOT / rel).read_text(encoding="utf-8")))["verdict"]
    except Exception:
        return "VALUES"          # unparseable => never keep


def run_one(prod: Path, timeout: int, env: dict) -> tuple[str, list[str]]:
    """Run one producer; return (verdict, kept_paths). Reverts what it rejects."""
    before = set(dirty_witnesses())
    try:
        r = subprocess.run([sys.executable, prod.name], cwd=prod.parent,
                           capture_output=True, text=True, timeout=timeout, env=env)
    except subprocess.TimeoutExpired:
        revert(set(dirty_witnesses()) - before)
        return "FAILED", []
    if r.returncode != 0:
        revert(set(dirty_witnesses()) - before)
        return "FAILED", []

    # Only what THIS producer touched — never the accumulated set.
    touched = sorted(set(dirty_witnesses()) - before)
    if not touched:
        return "NOCHANGE", []

    keep, drop, verdicts = [], [], []
    for rel in touched:
        v = judge(rel)
        verdicts.append(v)
        (keep if v in KEEP else drop).append(rel)
    revert(drop)
    if not keep:
        return (verdicts[0] if verdicts else "NOCHANGE"), []
    return ("ANCHOR_MIGRATION" if "ANCHOR_MIGRATION" in verdicts
            else "DECLARED"), keep


SELF_TEST_NOTE = """\
Self-test covers the two structural properties the previous driver got wrong;
the verdict policy itself is tested in witness_regen_classify.
"""


def self_test() -> int:
    fails = 0

    # 1. revert() must never accept a directory or an empty entry.
    calls = []
    global git
    real_git = git
    try:
        git = lambda *a: calls.append(a) or subprocess.CompletedProcess(a, 0, "", "")  # noqa: E731
        revert(["a.witness.json", "", None])
        ok = calls and calls[0] == ("checkout", "--", "a.witness.json")
        print(f"  {'ok  ' if ok else 'FAIL'}  revert passes only real paths")
        fails += not ok
        calls.clear()
        revert([])
        ok = not calls
        print(f"  {'ok  ' if ok else 'FAIL'}  revert with nothing to do is a no-op")
        fails += not ok
    finally:
        git = real_git

    # 2. declares_upstream sees both spellings and nothing else.
    for src, want, label in [
        ("b.add_upstream(p)", True, "add_upstream"),
        ("record_upstream(p, L)", True, "record_upstream"),
        ("json.loads(p.read_text())", False, "plain read"),
        ("def (:", False, "syntax error"),
    ]:
        got = declares_upstream(src)
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  declares_upstream: {label}")

    total = 6
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=150)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true",
                    help="list the producers that would run, change nothing")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    prods = producers()
    if a.limit:
        prods = prods[:a.limit]
    print(f"{len(prods)} producer(s) declare an upstream", flush=True)
    if a.dry_run:
        for p in prods:
            print(f"  {p.relative_to(ROOT).as_posix()}")
        return 0

    if dirty_witnesses():
        print("REFUSING: witnesses are already dirty. This driver must start "
              "from a clean tree, or it cannot tell its own output from "
              "someone else's.", file=sys.stderr)
        return 2

    # Both in-repo packages, not just the substrate. `pyhecke` (the Python
    # package under tools/pyhecke) is distinct from the `pyhecke_native`
    # extension, and leaving it off the path made producers fail with
    # `ModuleNotFoundError: No module named 'pyhecke'` — which the driver then
    # recorded as FAILED, indistinguishable from a real defect. It was the
    # dominant cause of an alarming failure rate that was pure harness error.
    env = dict(os.environ, PYTHONPATH=os.pathsep.join([
        str(ROOT / "tools/qou-substrate/python"),
        str(ROOT / "tools/pyhecke/python"),
    ]))
    counts: dict[str, int] = {}
    kept: list[str] = []
    for i, prod in enumerate(prods, 1):
        verdict, keep = run_one(prod, a.timeout, env)
        counts[verdict] = counts.get(verdict, 0) + 1
        kept.extend(keep)
        if i % 10 == 0 or i == len(prods):
            print(f"  [{i}/{len(prods)}] {counts}  kept={len(kept)}", flush=True)

    print(f"\nFINAL {counts}")
    print(f"kept {len(kept)} witness(es) — verify with "
          f"`git status` before committing, and commit by explicit path")
    for k in kept[:40]:
        print(f"    {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
