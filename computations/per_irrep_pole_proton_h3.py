#!/usr/bin/env python3
"""
per_irrep_pole_proton_h3.py — SUPERSEDED shim; delegates to
`per_irrep_pole_atom.py proton`.

Path A verification of the per-proton shift exponent in
`prop:per-nucleon-shift-additive-linearity`, for Z=1, N=0, A=1, n=3.

WHY THIS IS A SHIM (bean `qou-okl8`).  This script and `per_irrep_pole_atom.py`
both wrote the SAME witness name: the generalised producer emits
`f"per-irrep-pole-{atom}-h{n}"`, which at (1, 0) is exactly the literal this
file used to write.  Whichever ran last won.  The committed
`per-irrep-pole-proton-h3.witness.json` records
`scriptFile: per_irrep_pole_atom.py`, so the generalised producer is its
de-facto owner and this file was the intruder.  `WitnessBuilder.save()` now
refuses such an overwrite (`_check_producer_takeover`); delegating keeps this
entry point working instead of leaving it permanently unable to write.  Full
context: `docs/audits/2026-08-16-chi-cache-drain-and-the-y-lambda-zero-saving.md`.

READING CORRECTION — KEPT, because it is still right and still easy to get
wrong.  The per-irrep maximum at H_3 is **11** (at lambda = (2, 1)), NOT 18.
The "18" in `shift_NF(beta) = 18 Z + 21 N + 1` is the per-proton additive
coefficient of the FULL u-pole order of tr_M, not a per-irrep q-pole order.
Do not read one for the other.

STALE CLAIM REMOVED.  This file used to advertise "**Verified result:**
ord_{u=0}(tr_M(beta_p)) = 19, matching shift_NF(beta_p) = 19".  The generalised
producer reports max pole **18** against the predicted 19 — Path A is
**inconclusive** at A=1, not verified.  (The deuteron's stale claim was worse:
it named lambda = (4, 1, 1) as the maximizer, a three-row partition whose
y_lambda is identically zero.)  Do not restore either claim from git history
without re-deriving it.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


# KEPT AT MODULE LEVEL — `per_irrep_pole_atom.py:69` does
# `from per_irrep_pole_proton_h3 import negative_q_pole_order`, so this file is
# a library for the very producer that supersedes it as a script. Shimming the
# CLI must not take the function with it: removing it broke the atom producer's
# top-level import, which is how this dependency was found. Note the resulting
# cycle is fine only because the shim's `per_irrep_pole_atom` import lives
# inside `main()` — do not hoist it to module level.
def negative_q_pole_order(chi_q: sp.Expr, var: sp.Symbol | None = None) -> int:
    """Order of pole at `var` = 0 of `chi_q` (Laurent series).

    For a rational expression $\\chi = N/D$ in `var`:

        ord_{var=0}(N/D)  =  ord_{var=0}(N) - ord_{var=0}(D)

    where `ord_{var=0}(P)` is the **lowest** non-zero exponent of
    `var` in `P` (the multiplicity of `var=0` as a zero/pole of P).
    The pole order at `var = 0` is `max(0, -ord(N/D))`.

    Default `var = q` (positive), but pass any symbol for
    substitutions like `q = u^2`.
    """
    if var is None:
        var = sp.symbols("q", positive=True)
    chi_simp = sp.simplify(chi_q)
    n, d = sp.fraction(chi_simp)
    n_poly = sp.Poly(n, var)
    d_poly = sp.Poly(d, var)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
    d_low = min(m[0] for m in d_poly.monoms()) if d_poly.monoms() else 0
    # ord(N/D) = ord(N) - ord(D); pole order at 0 = max(0, -ord)
    return max(0, d_low - n_low)


def main() -> int:
    import argparse

    from per_irrep_pole_atom import ATOMS, run_atom

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workers", type=int, default=None,
        help="multiprocessing.Pool size for the chi cache build",
    )
    args = parser.parse_args()

    print("per_irrep_pole_proton_h3.py is superseded — "
          "delegating to per_irrep_pole_atom.py proton (bean qou-okl8).\n")
    Z, N = ATOMS["proton"]
    return run_atom(Z, N, workers=args.workers)


if __name__ == "__main__":
    sys.exit(main())
