#!/usr/bin/env python3
"""delta_lambda_imme_quartet.py
==============================

Δ³ = 0 prediction check on a 4th multiplet member (the A=9, T=3/2
isobaric QUARTET ⁹Li / ⁹Be / ⁹B / ⁹C).

The IMME decomposition of the canonical residual (delta_lambda_imme_
triplet.py, PR #3104; Lean QOU.BraidKnot.DeltaLambdaIMME) is

    log_{q₀} Δ_λ(Z,N) = a(A) + b(A)·T₃ + c(A)·T₃²,   T₃ = (Z − N)/2,

i.e. a degree-2 polynomial in T₃ (Wigner rank-≤2 isotensor = the
Askey–Racah truncation). Triplets (T₃ = −1, 0, +1) can measure a, b, c
but cannot FALSIFY the degree-2 form — three points always fit a
parabola. A QUARTET (T₃ = −3/2 … +3/2) gives the first falsifiable
prediction: the third finite difference

    Δ³ = f(+3/2) − 3·f(+1/2) + 3·f(−1/2) − f(−3/2) = 6·d

must vanish (`imme_third_diff_zero`, proved for degree-2 polynomials by
`ring`). A large |d| relative to the linear |b| refutes the rank-≤2
truncation for the residual.

SAME-T discipline (as in the triplet probe): the quartet is the T=3/2
multiplet. The OUTER members (⁹Li, ⁹C) have T=3/2 ground states; the
INNER members (⁹Be, ⁹B) have T=1/2 ground states, so their T=3/2
isobaric-analog states (IAS) sit at measured excitation energies E_x —
subtract E_x from the ground-state binding to land all four members in
the same multiplet. E_x are measured inputs (TUNL A=9 evaluation),
not fits.

Experimental context: nuclear IMME d coefficients for the A=9 quartet
are ~5–10 keV — invisible at the q₀-exponent scale (10 keV / 45 MeV ≈
0.002 exponent units). Any large Δ³ measured here would therefore be a
FRAMEWORK deviation (structure in B_pred's T₃ dependence), not nuclear.

Not wired; near-match tier; no fit.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import math
import time

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

# (name, Z, N, B_AME[MeV]) ordered T₃ = -3/2, -1/2, +1/2, +3/2.
# B_AME: AME2020 total binding energies.
QUARTET_A9 = [
    ("9Li", 3, 6, 45.3414),
    ("9Be", 4, 5, 58.1645),
    ("9B",  5, 4, 56.3145),
    ("9C",  6, 3, 39.0366),
]

# T=3/2 IAS excitation energies for the inner (T=1/2 ground-state)
# members — TUNL A=9 evaluation. Outer members are T=3/2 already.
IAS_EX_MEV = {"9Be": 14.3925, "9B": 14.6550}


def main() -> int:
    t0 = time.monotonic()
    from binding_canonical import binding_canonical
    q0 = float(q_at(30))
    lnq = math.log(q0)

    pts = {}
    for nm, Z, N, bame in QUARTET_A9:
        r = binding_canonical(Z, N, verbose=False)
        if r.get("status") != "solved":
            print(f"  {nm}: status {r.get('status')} — abort")
            return 1
        bp = float(r["B_MeV"])
        t3 = (Z - N) / 2.0
        bame_sameT = bame - IAS_EX_MEV.get(nm, 0.0)
        pts[t3] = {
            "atom": nm, "Z": Z, "N": N, "B_pred": bp,
            "B_AME_gs": bame, "ias_ex_MeV": IAS_EX_MEV.get(nm, 0.0),
            "B_AME_sameT": bame_sameT,
            "log_q0_gs": math.log(bame / bp) / lnq,
            "log_q0_sameT": math.log(bame_sameT / bp) / lnq,
        }
        print(f"  {nm}: T3={t3:+.1f}  B_pred={bp:.4f}  "
              f"x_gs={pts[t3]['log_q0_gs']:.3f}  "
              f"x_sameT={pts[t3]['log_q0_sameT']:.3f}")

    t3s = sorted(pts)  # [-1.5, -0.5, 0.5, 1.5]

    def diffs(key: str) -> dict:
        f = [pts[t][key] for t in t3s]
        # third finite difference over unit spacing in T₃
        d3 = f[3] - 3 * f[2] + 3 * f[1] - f[0]
        d_cubic = d3 / 6.0
        # degree-2 coefficients from the inner symmetric combinations:
        # b from the two half-unit points, c from the outer curvature.
        b_inner = f[2] - f[1]                       # b + (c terms cancel: (1/4−1/4))
        c_outer = (f[3] + f[0] - f[2] - f[1]) / 4.0  # exact for degree-2
        a_mid = (9 * (f[1] + f[2]) - (f[0] + f[3])) / 16.0  # degree-2 midpoint
        return {"f_by_T3": {str(t): round(pts[t][key], 4) for t in t3s},
                "third_diff": round(d3, 4), "d_cubic": round(d_cubic, 4),
                "b_linear": round(b_inner, 4), "c_quadratic": round(c_outer, 4),
                "a_isoscalar": round(a_mid, 4)}

    gs = diffs("log_q0_gs")
    st = diffs("log_q0_sameT")
    print(f"\n  ground-state:  Δ³={gs['third_diff']:+.4f}  d={gs['d_cubic']:+.4f}  "
          f"b={gs['b_linear']:+.4f}  c={gs['c_quadratic']:+.4f}")
    print(f"  same-T (IAS):  Δ³={st['third_diff']:+.4f}  d={st['d_cubic']:+.4f}  "
          f"b={st['b_linear']:+.4f}  c={st['c_quadratic']:+.4f}")

    # The falsifiable check: cubic d small relative to the linear b.
    d_over_b = abs(st["d_cubic"] / st["b_linear"]) if st["b_linear"] else float("inf")
    passed = d_over_b < 0.10
    print(f"  |d/b| (same-T) = {d_over_b:.3f}  →  Δ³≈0 {'HOLDS' if passed else 'FAILS'}")

    b = WitnessBuilder("delta-lambda-imme-quartet",
                       engine="python+canonical-binding", start_time=t0)
    (b.set_description(
        "A=9 T=3/2 isobaric-quartet (⁹Li/⁹Be/⁹B/⁹C) third-difference test "
        "of the IMME degree-2 form of the canonical residual: "
        "log_q0 Δ_λ = a + b·T₃ + c·T₃² predicts Δ³ = 6d = 0 "
        "(Lean QOU.BraidKnot.DeltaLambdaIMME.imme_third_diff_zero). First "
        "falsifiable check of the rank-≤2 isotensor (Askey–Racah) "
        "truncation — triplets cannot falsify it (3 points always fit a "
        "parabola). Inner members (⁹Be, ⁹B) corrected to their measured "
        "T=3/2 IAS (14.3925 / 14.6550 MeV) for the same-T multiplet. "
        "Nuclear IMME d for A=9 is ~5–10 keV ≈ 0.002 exponent units, so "
        "any large Δ³ here would be framework structure in B_pred, not "
        "nuclear. Not wired; near-match tier; no fit.")
     .add_data("q0", q0)
     .add_data("quartet", {str(t): pts[t] for t in t3s})
     .add_data("ground_state", gs)
     .add_data("same_T", st)
     .add_data("d_over_b_sameT", round(d_over_b, 4))
     .add_data("imme_form",
               "log_q0 Δ_λ(T₃) = a + b·T₃ + c·T₃² (+ d·T₃³ ← tested here)")
     .add_data("triplet_crossref", {
         "b_by_A_triplets": {"6": -1.727, "8": -1.795, "10": -1.727, "12": -1.717},
         "c_sameT_by_A_triplets": {"6": -0.109, "8": -0.096, "10": -0.062,
                                    "12": -0.037},
         "source": "delta-lambda-imme-triplet.witness.json"}))
    b.add_assertion("third_diff_small_sameT",
                    computed=bool(passed), expected=True,
                    source="|d/b| < 0.10 on the same-T quartet — the degree-2 "
                           "IMME truncation survives its first falsifiable test")
    res = b.save()
    print(f"  Wrote {res.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
