#!/usr/bin/env python3
# polynomial_q_not_applicable: static JSON comparison, emits no numeric physics.
"""Report witnesses that LOST keys against a git ref.

## Why this exists

A pass that re-runs producers — even incidentally, to check they still
import — also REGENERATES their witnesses. `70ae502091` did exactly that for
109 witnesses while draining reference literals, and four of them came out
SMALLER: `chi-deuteron-h6-at-q0-50dps` lost `tr_M_at_q0`, `N`, `Z`,
`contribution`, `convention` and `description`, and the loss reached `main`
and stayed there until a sibling session noticed.

The verification behind that commit asked two questions — did the values get
CORRECTED, did the environment block GROW — and both answered yes. Neither
answers *did anything disappear*. This script asks the third question.

## What it does NOT do

It does not judge whether a shrink is wrong. Some are legitimate: an audit's
own witness shrinks as its findings drain, which is the gate working. It
reports the loss and names the keys, and a human or agent decides. A checker
that guessed here would either block real progress or wave through real
damage.

## Usage

    scripts/witness-shrink-check.py                 # working tree vs HEAD
    scripts/witness-shrink-check.py --against main  # vs another ref
    scripts/witness-shrink-check.py --strict        # exit 1 if any key lost
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# Environment / provenance keys. Losing one is DEGRADATION — the container
# ran without a library the recording container had — and it is a different
# thing from losing a computed payload key, needing a different response
# (install the library and re-run, vs restore the value). Reported apart so
# the payload signal is not buried: the run that motivated this script showed
# 11 shrunk witnesses of which only 4 had lost payload.
_PROVENANCE_KEYS = {
    "clarabel", "mpmath", "numpy", "scipy", "sympy", "python",
    "pyhecke_native", "pyhecke_native_build", "engineVersion",
    "environment", "invocation", "argv", "durationMs",
}


def _keys(obj, out: set[str]) -> set[str]:
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.add(k)
            _keys(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _keys(v, out)
    return out


def _at_ref(ref: str, rel: str) -> set[str] | None:
    r = subprocess.run(["git", "show", f"{ref}:{rel}"],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        return None
    try:
        return _keys(json.loads(r.stdout), set())
    except ValueError:
        return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--against", default="HEAD")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)

    losses = []
    for f in sorted(ROOT.rglob("*.witness.json")):
        if ".git" in f.parts:
            continue
        rel = str(f.relative_to(ROOT))
        before = _at_ref(a.against, rel)
        if before is None:
            continue  # new file: nothing to lose
        try:
            after = _keys(json.loads(f.read_text()), set())
        except (OSError, ValueError):
            continue
        lost = before - after
        if lost:
            payload = sorted(lost - _PROVENANCE_KEYS)
            prov = sorted(lost & _PROVENANCE_KEYS)
            losses.append((rel, payload, prov))

    print("=" * 74)
    print(f"WITNESS SHRINK CHECK — keys lost vs {a.against}")
    print("=" * 74)
    if not losses:
        print("  no witness lost a key")
        return 0
    pay = [x for x in losses if x[1]]
    prov_only = [x for x in losses if not x[1]]
    print(f"  PAYLOAD keys lost : {len(pay)} witness(es)   <- damage")
    print(f"  provenance only   : {len(prov_only)} witness(es)   <- degradation")
    for rel, payload, prov in pay:
        print(f"\n    {rel}")
        print(f"        payload lost: {', '.join(payload[:8])}"
              + (f" (+{len(payload) - 8} more)" if len(payload) > 8 else ""))
        if prov:
            print(f"        (also provenance: {', '.join(prov[:4])})")
    for rel, _, prov in prov_only:
        print(f"\n    {rel}")
        print(f"        provenance lost: {', '.join(prov[:6])}")
    print("\n  A shrink is not automatically wrong — an audit's own witness")
    print("  shrinks as its findings drain, which is the gate working. But a")
    print("  PRODUCER witness that lost a payload key is damage: RESTORE it")
    print("  from the ref rather than regenerating, when regenerating would")
    print("  decide an open question someone else owns.")
    print("  Provenance loss means the container lacked a library: install")
    print("  it and re-run rather than committing the weaker record.")
    return 1 if (a.strict and pay) else 0


if __name__ == "__main__":
    sys.exit(main())
