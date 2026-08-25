#!/usr/bin/env python3
"""proton_pin_assertion_check.py — does this producer's OWN assertions still
pass when it runs at the proton pin?

WHY THIS AND NOT THE ANCHOR-FLIP AUDIT

`anchor_flip_straddle_audit` answers "does a layer STRADDLE exist" and is sound
only for producers with a q of their own. Most `ideal_muon` entries do not have
one — they read `q_parameter`'s manifest-resolved shim, so flipping the anchor
changes their ONLY q and everything moves. That is a re-pin, trivially true, and
tells you nothing about whether the producer may be migrated.

The question a migration actually needs is narrower and cheaper:

    if I move this producer to the proton pin, does it still WORK?

A producer answers that itself, through its own assertions. `aoperator_a5_
crosscheck` is the worked case: its source never mentions muon, so a header scan
put it in the "safe to migrate" pile — and its `/allPassed` goes true -> false at
the proton pin, because an assertion compares a q-dependent computed value
against an anchor-INDEPENDENT expected one. Migrating it would have turned a
passing producer into a failing one.

So: silence in the source is not evidence of accidental listing. Run it.

COST. One leg per producer, against the audit's two — but a leg can still be
long (`binding_via_interface_knot` exceeded 1700 s unfinished). TIMEOUT is
reported as UNKNOWN, never as pass.

Usage:
    python3 proton_pin_assertion_check.py <producer.py> [...] [--timeout N]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__")


def _tree_witnesses() -> dict:
    """Snapshot every witness — producers write SIBLING witnesses (AGENTS.md)."""
    out = {}
    for f in REPO.rglob("*.witness.json"):
        if any(x in f.parts for x in SKIP):
            continue
        try:
            out[f] = f.read_bytes()
        except OSError:
            pass
    return out


def _restore(saved: dict) -> None:
    for f, b in saved.items():
        try:
            if f.read_bytes() != b:
                f.write_bytes(b)
        except OSError:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(b)
    for f in REPO.rglob("*.witness.json"):
        if any(x in f.parts for x in SKIP):
            continue
        if f not in saved:
            f.unlink(missing_ok=True)


def check(prod: Path, timeout: int):
    """(verdict, detail) — does the producer pass its own assertions at proton?"""
    saved = _tree_witnesses()
    env = dict(os.environ)
    env["QOU_Q0_ANCHOR"] = "physical"
    try:
        try:
            r = subprocess.run([sys.executable, "-u", prod.name], cwd=prod.parent,
                               capture_output=True, timeout=timeout, env=env)
        except subprocess.TimeoutExpired:
            return "UNKNOWN", f"exceeded {timeout}s — not a pass, not a fail"
        if r.returncode != 0:
            tail = (r.stderr or b"").decode()[-120:].replace("\n", " ")
            return "FAILS-AT-PROTON", f"exit {r.returncode}: {tail}"

        # Which witnesses did this run write?
        wrote = {f: json.loads(f.read_text())
                 for f in REPO.rglob("*.witness.json")
                 if not any(x in f.parts for x in SKIP)
                 and f.read_bytes() != saved.get(f)}
        if not wrote:
            return "NO-WITNESS", "writes nothing — no assertions to check"

        bad = []
        for f, doc in wrote.items():
            if doc.get("allPassed") is False:
                bad.append(f"{f.name}: allPassed=false")
            for a in doc.get("assertions", []):
                if a.get("passed") is False:
                    bad.append(f"{f.name}: assertion {a.get('name')!r} FAILED")
        if bad:
            return "FAILS-AT-PROTON", "; ".join(bad[:3])
        n = sum(len(d.get("assertions", [])) for d in wrote.values())
        return "PASSES-AT-PROTON", f"{len(wrote)} witness(es), {n} assertion(s), all pass"
    finally:
        _restore(saved)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("producers", nargs="+")
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args(argv)

    print("=" * 72)
    print("proton-pin assertion check — may this producer be migrated?")
    print("=" * 72)
    rc = 0
    for p in args.producers:
        path = Path(p) if Path(p).is_absolute() else REPO / p
        v, d = check(path, args.timeout)
        print(f"  {v:17s} {path.stem}: {d}", flush=True)
        if v == "FAILS-AT-PROTON":
            rc = 1
    print("=" * 72)
    print("  PASSES-AT-PROTON -> safe to migrate (still diff its witness on the real move)")
    print("  FAILS-AT-PROTON  -> HOLD: it depends on the muon pin, whatever its source says")
    print("  UNKNOWN          -> untested; do NOT read as either")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
