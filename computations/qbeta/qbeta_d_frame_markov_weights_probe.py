#!/usr/bin/env python3
"""
The convention-D H_3(q) Markov weights: two-row, and both bar-EVEN.

Step 2 of bean `qou-cds1` (S1: re-derive the Q_beta c_k ladder under
convention D). Companion to `QOU.QBeta.MarkovWeightsConventionD` (Lean,
sorry-free) and to the step-1 probe
`qbeta_d_frame_eigenphase_bar_parity_probe.py`.

WHAT STEP 1 LEFT OPEN
---------------------
Step 1 proved the ladder eigenphase `alpha = (z-1)h/2` is bar-ODD exactly
when `z` is bar-even, so `eigenphase_bar_involution` is a convention-C
statement and under D the eigenphase carries an exact defect `h^2/2`. The
forced bar-odd projection `alpha - h^2/4` improved the D-frame extraction a
long way but did not close it. The natural next question: what bar-odd
material does the D-frame trace still have to build a phase from?

WHAT THIS FINDS
---------------
None, in the weights. Solving the three H_3(q) Markov equations for general
`z` and specialising to `z_D = q^3/(q^2+1)`:

    y_(1^3) = 0     exactly
    y_(2,1) = q^2 / (q^2+1)^2
    y_(3)   = (q^4+1) / (q^2+1)^2      (and y_3 + 2 y_21 = 1 exactly)

and BOTH surviving weights are bar-even under `q -> 1/q`.

Two things worth separating:

1. The `y_(1^3) = 0` here is an INDEPENDENT re-derivation of the two-row cap
   from the Markov side. It drops out of the linear system at `z_D`; it is
   not imported from Wenzl's theorem (`WenzlWeightVanishing.lean`, all `n`).
   The two routes corroborate each other, which is worth more than either
   alone.

2. The bar-EVENNESS is the prune. The C-frame ladder's bar-odd content comes
   from `alpha` being bar-odd, which comes from `z_C` being bar-even against
   a bar-ODD `h`. Under D the surviving Markov data is bar-even throughout,
   so no quantity built from the D-frame weights alone carries a bar-odd
   part. A D-frame phase with the C-frame's bar parity cannot be assembled
   from the weights; it must come from elsewhere — the `h` factor, the
   Kashiwara `f~_1` shift, or the framing — or not exist.

SCOPE
-----
Scope-(a) throughout, and this is a NEGATIVE result about where to look, not
a re-derivation. It narrows the search; it does not supply the D-frame
ladder. Nothing is wired, no c_k value or tier changes, and the Q_beta
channel registration stays `disputed`. In particular this does NOT show the
decay channel's trace IS the D one — that is the owner ruling of 2026-08-15
(R1), not a result proved here.

Usage:
    python3 computations/qbeta/qbeta_d_frame_markov_weights_probe.py

Output:
    computations/qbeta/qbeta-d-frame-markov-weights.witness.json
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401


def _repo_head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE),
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


def solve_markov_weights():
    """Solve the three H_3(q) Markov equations for general z, then specialise.

    The equations are the ones `decayLadder_zC_threeRow_ne_zero` consumes:
    normalisation, `tr(sigma) = z`, `tr(sigma^2) = z^2`, against the H_3(q)
    character table (eigenvalues q and -q^-1 on the two-row block).
    """
    q, z = sp.symbols("q z", positive=True)
    y3, y21, y13 = sp.symbols("y3 y21 y13")

    eqs = [
        sp.Eq(y3 + 2 * y21 + y13, 1),
        sp.Eq(q * y3 + (q - 1 / q) * y21 + (-1 / q) * y13, z),
        sp.Eq(q ** 2 * y3 + (-1) * y21 + (1 / q ** 2) * y13, z ** 2),
    ]
    sol = sp.solve(eqs, [y3, y21, y13], dict=True)
    if len(sol) != 1:
        raise RuntimeError(f"expected a unique solution, got {len(sol)}")
    return q, z, {str(k): sp.factor(sp.simplify(v)) for k, v in sol[0].items()}


def main() -> int:
    t0 = time.monotonic()
    q, z, general = solve_markov_weights()

    def bar(e):
        return sp.simplify(e.subs(q, 1 / q))

    z_d = q ** 3 / (q ** 2 + 1)
    z_c = sp.sqrt(q) / (1 + q)

    at_d = {k: sp.factor(sp.simplify(v.subs(z, z_d))) for k, v in general.items()}
    at_c = {k: sp.simplify(v.subs(z, z_c)) for k, v in general.items()}

    y13_d_zero = sp.simplify(at_d["y13"]) == 0
    y13_c_zero = sp.simplify(at_c["y13"]) == 0
    norm_exact = sp.simplify(at_d["y3"] + 2 * at_d["y21"] + at_d["y13"] - 1) == 0

    bar_defects = {k: sp.simplify(bar(v) - v) for k, v in at_d.items()}
    all_bar_even = all(d == 0 for d in bar_defects.values())

    print("=== H_3(q) Markov weights, general z ===")
    for k in ("y3", "y21", "y13"):
        print(f"  {k:4s} = {general[k]}")
    print()
    print("=== specialised to z_D = q^3/(q^2+1) ===")
    for k in ("y3", "y21", "y13"):
        print(f"  {k:4s} = {at_d[k]}        bar - self = {bar_defects[k]}")
    print(f"  normalisation y3 + 2*y21 + y13 - 1 = "
          f"{sp.simplify(at_d['y3'] + 2 * at_d['y21'] + at_d['y13'] - 1)}")
    print()
    print(f"  y_(1^3) = 0 at z_D : {y13_d_zero}")
    print(f"  y_(1^3) = 0 at z_C : {y13_c_zero}   (C keeps the third row)")
    print(f"  all D weights bar-even : {all_bar_even}")
    print()

    assertions = [
        {
            "name": "1_threeRow_vanishes_at_zD",
            "passed": bool(y13_d_zero),
            "detail": "y_(1^3) = 0 falls out of the Markov linear system at z_D — "
                      "an independent re-derivation of the two-row cap, not imported "
                      "from Wenzl",
        },
        {
            "name": "2_threeRow_survives_at_zC",
            "passed": bool(not y13_c_zero),
            "detail": "y_(1^3) != 0 at z_C — the C-frame trace does not factor "
                      "through Temperley-Lieb (consistent with "
                      "decayLadder_zC_threeRow_ne_zero)",
        },
        {
            "name": "3_two_row_weights_normalise_exactly",
            "passed": bool(norm_exact),
            "detail": "y_(3) + 2 y_(2,1) = 1 exactly at z_D; the two-row weights "
                      "alone saturate the normalisation",
        },
        {
            "name": "4_all_D_weights_bar_even",
            "passed": bool(all_bar_even),
            "detail": "bar(y) = y for every surviving D-frame weight — no bar-odd "
                      "part anywhere in the D weight data",
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-d-frame-markov-weights",
        "description": "Solves the three H_3(q) Markov equations at convention D. "
                       "y_(1^3) = 0 falls out of the linear system (an independent "
                       "re-derivation of the two-row cap), the surviving weights are "
                       "q^2/(q^2+1)^2 and (q^4+1)/(q^2+1)^2, and BOTH are bar-even. "
                       "So no quantity built from the D-frame weights alone carries a "
                       "bar-odd part — the bar-ODD eigenphase the C-frame ladder uses "
                       "cannot be assembled from them.",
        "audit_only": True,
        "tier": "symbolic-exact",
        # Q0_INDEPENDENT, not merely unrecorded: this probe is q-GENERIC. It
        # solves and factors over the symbol `q` and never evaluates at any
        # anchor, so there is no pin to record — and deliberately no
        # `q0Value`, which the q0-anchor audit correctly reads as a
        # contradiction with `independent` (it would mean something did supply
        # a pin). Contrast the step-1 probe, which evaluates the ladder at both
        # anchors and so carries one.
        "q0Anchor": "independent",
        "scope": "scope-(a), and NEGATIVE: this narrows where a D-frame ladder "
                 "derivation may look; it does not supply one. Nothing wired, no c_k "
                 "value or tier changes, channel stays `disputed`. It does NOT show "
                 "the decay trace IS the D one — that is the 2026-08-15 owner ruling.",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "general_solution": {k: str(v) for k, v in general.items()},
            "at_z_D": {k: str(v) for k, v in at_d.items()},
            "bar_defect_at_z_D": {k: str(v) for k, v in bar_defects.items()},
            "verdict": "Convention D's H_3 Markov trace is two-row with bar-EVEN "
                       "weights. The C-frame ladder's bar-odd content comes from "
                       "z_C bar-even against a bar-ODD h; under D that source is "
                       "gone from the weights. A D-frame phase carrying the C-frame's "
                       "bar parity must come from the h factor, the Kashiwara f~_1 "
                       "shift, or the framing — or not exist.",
        },
        "context": {
            "lean": "QOU.QBeta.MarkovWeightsConventionD (sorry-free): "
                    "markovWeightsD_norm / _sigma / _sigmasq / _zsq, "
                    "markovWeightsD_y21_barEven / _y3_barEven",
            "step_1": "qbeta-d-frame-eigenphase-bar-parity — bar(alpha)+alpha = h^2/2 "
                      "under D; the forced projection alpha - h^2/4 is necessary but "
                      "not sufficient",
            "corroborates": "WenzlWeightVanishing.lean (all n, z_D is Wenzl level "
                            "r = 2) — reached here independently from the Markov side",
            "bean": "qou-cds1",
            "flip_flop_guard": "registry section 8 — no c_k wired",
        },
    }

    out = os.path.join(HERE, "qbeta-d-frame-markov-weights.witness.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2)
    print(f"witness -> {out}")
    print(f"allPassed: {all_passed}  ({int((time.monotonic() - t0) * 1000)} ms)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
