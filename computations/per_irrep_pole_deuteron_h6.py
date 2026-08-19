#!/usr/bin/env python3
"""
per_irrep_pole_deuteron_h6.py — SUPERSEDED shim; delegates to
`per_irrep_pole_atom.py deuteron`.

Path A verification of the deuteron shift exponent (multi-nucleon case) in
`prop:per-nucleon-shift-additive-linearity`, for Z=1, N=1, A=2, n=6.

WHY THIS IS A SHIM (bean `qou-okl8`).  This script and `per_irrep_pole_atom.py`
both wrote the SAME witness name.  The generalised producer emits
`f"per-irrep-pole-{atom}-h{n}"`, which for the deuteron is exactly the literal
this file used to write.  Whichever ran last won, and this one's schema is
strictly poorer: running it over the committed atom-produced witness deleted
`data.atom_chi_fingerprint`, `data.lean_uniqueness_ref` and
`data.per_generator_crossings` — 230 deletions against 39 insertions — with no
warning of any kind.  Both committed witnesses (`per-irrep-pole-deuteron-h6`
and `per-irrep-pole-proton-h3`) record `scriptFile: per_irrep_pole_atom.py`, so
the generalised producer is the de-facto owner of both; this file was the
intruder.

`WitnessBuilder.save()` now refuses that overwrite outright
(`_check_producer_takeover`), which turns the silent data loss into a loud
error — but it would also have left this script permanently unable to write.
Delegating is the coherent end state: the entry point keeps working, the RICH
witness is produced, and there is exactly one producer per witness name.

The 561-line generalised producer is a strict superset of what this file did:
same recipe (cached symbolic y_lambda, cached symbolic chi per partition,
q = u^2 substitution, per-term ord_{u=0}), parameterised by (Z, N), plus
multiprocessing and the three extra data fields above.  Nothing is lost.

STALE CLAIM REMOVED.  The docstring this file used to carry advertised a
"**Verified result:** ord_{u=0}(tr_M(beta_D)) = 40 ... Maximizer: lambda =
(4, 1, 1) with per-term pole = 40".  That is wrong twice over now.  (4,1,1) has
three rows, so y_lambda = 0 identically (#5217, confirmed at every n from 2 to
12) and its per-term pole is **0**, not the maximum.  Under the colour-weighted
word the maximizer is (4,2) at 46, and Path A is **inconclusive** at A=2
(46 != predicted 40).  See
`docs/audits/2026-08-16-chi-cache-drain-and-the-y-lambda-zero-saving.md`.
Do not restore the old claim from git history without re-deriving it.

MAIN'S q0-ANCHOR ANALYSIS, PRESERVED (commit 0f50c3d2, bean qou-kx04). While
this shim was on a branch, main declared this stem's anchor on the version that
still emitted:

    q0Anchor: "ambiguous" — the manifest lists this stem under `ambiguous`
    (both pin signatures present). q0 IS reachable — a 19-module import cone via
    hoefsmit_symbolic / hecke_core / mass_at_3A_proper — so this is not q0-free,
    it is q0-*undetermined*. No q0Value, because there is no single pin to
    record and writing one would claim a ruling nobody has made. Bean qou-pin1
    reached for `independent` here and was right to settle instead.

That reasoning is correct and is kept for whoever rules on it. The DECLARATION
is moot under delegation: this stem no longer emits a witness, so it has no
anchor to stamp — `per_irrep_pole_atom.py` emits, and stamps its own. The open
question main identified (which pin the H_6 per-irrep pole extraction actually
evaluates at) is NOT answered here and survives on the atom producer.

Note the interaction: main's version writes `per-irrep-pole-deuteron-h6`, a
witness whose committed copy records `scriptFile: per_irrep_pole_atom.py`, with
three fewer `data.*` fields. `WitnessBuilder._check_producer_takeover` now
REFUSES that write. So main's version and this branch's guard are incompatible
at runtime, and the shim is what reconciles them.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def main() -> int:
    import argparse

    from per_irrep_pole_atom import ATOMS, run_atom

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workers", type=int, default=None,
        help="multiprocessing.Pool size for the chi cache build",
    )
    args = parser.parse_args()

    print("per_irrep_pole_deuteron_h6.py is superseded — "
          "delegating to per_irrep_pole_atom.py deuteron (bean qou-okl8).\n")
    Z, N = ATOMS["deuteron"]
    return run_atom(Z, N, workers=args.workers)


if __name__ == "__main__":
    sys.exit(main())
