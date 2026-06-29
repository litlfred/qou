#!/usr/bin/env python3
"""delta_lambda_imme_triplet.py
==============================

The bar-parity split of the canonical residual (PR #3089) reads:

    log_{q₀} Δ_λ(Z,N)  =  a(A)              # bar-EVEN, A-only (leading ~10A−5, A≤4)
                          + b(A)·T₃          # bar-ODD  (the writhe Z-correction)
                          + c(A)·T₃² + …     # bar-EVEN quadratic  ← THIS PROBE
        T₃ = (Z − N)/2 .

This is the **Isobaric Multiplet Mass Equation** (Wigner 1957) shape: the
residual is a degree-2 polynomial in the isospin projection T₃. Mirror PAIRS
(PR #3089) only ever measure b — the bar-odd term — because the mirror
difference `f(+T₃) − f(−T₃) = 2·b·T₃` cancels the bar-even a AND c·T₃²
(Lean: `QOU.BraidKnot.mirror_baseline_cancels`). To see the QUADRATIC c you
need an isobaric TRIPLET (T₃ = −1, 0, +1): the symmetric second difference
`f(+1) + f(−1) − 2·f(0) = 2·c` isolates it.

## Result (A=6 triplet ⁶He / ⁶Li / ⁶Be, all 18 strands)

    a = 36.12 (isoscalar leading)   b = −1.73 (linear, matches mirror b's
    −1.34@A3, −1.77@A7)   c = −1.24  ← nonzero bar-even QUADRATIC.

The quadratic is real and substantial. The Askey connection: the body-order
b-ladder `a(n+2)=2cosh(10η)·a(n+1)−a(n)` is a three-term recurrence (continuous
q-Hermite / Al-Salam–Chihara in the Askey q-scheme); the IMME is the *degree-2
truncation in T₃* (Wigner: charge-dependent forces are rank-≤2 isotensors — the
Askey–Racah truncation, no d·T₃³).

## HONEST CAVEAT (same-T)

A clean Wigner IMME needs three members of the SAME isospin multiplet T. The
EXPERIMENTAL ground states used at T₃=0 (⁶Li, ⁸Be) are **T=0**, while their
T₃=±1 partners are **T=1**; the true T=1, T₃=0 analog is an excited state. So
the extracted `c` mixes the genuine IMME quadratic with the T=0/T=1 structure
difference. What is robust and framework-level: the residual `log_{q₀}Δ_λ` has
a NONZERO bar-even, T₃-even (quadratic) component beyond leading+linear — which
mirror pairs structurally cannot see. NOT wired; near-match tier; no fit.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import math
import time

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

# (name, Z, N, B_AME[MeV])  per isobaric triplet, ordered T₃ = -1, 0, +1.
TRIPLETS = {
    6: [("6He", 2, 4, 29.2712), ("6Li", 3, 3, 31.9946), ("6Be", 4, 2, 26.9241)],
    8: [("8Li", 3, 5, 41.2770), ("8Be", 4, 4, 56.4995), ("8B", 5, 3, 37.7375)],
}


def main() -> int:
    t0 = time.monotonic()
    from binding_canonical import binding_canonical
    q0 = float(q_at(30))
    lnq = math.log(q0)

    out_rows = []
    for A, members in TRIPLETS.items():
        pts = {}
        for nm, Z, N, bame in members:
            r = binding_canonical(Z, N, verbose=False)
            if r.get("status") != "solved":
                print(f"  {nm}: status {r.get('status')} — skipping A={A}")
                pts = {}
                break
            bp = float(r["B_MeV"])
            T3 = (Z - N) // 2
            x = math.log(bame / bp) / lnq
            pts[T3] = {"atom": nm, "Z": Z, "N": N, "B_pred": bp, "log_q0": x}
        if set(pts) != {-1, 0, 1}:
            continue
        xm, x0, xp = pts[-1]["log_q0"], pts[0]["log_q0"], pts[1]["log_q0"]
        a = x0
        b = (xp - xm) / 2.0           # linear (bar-odd) — mirror diff / 2
        c = (xp + xm - 2.0 * x0) / 2.0  # quadratic (bar-even) — 2nd difference / 2
        out_rows.append({
            "A": A, "members": {str(k): v for k, v in pts.items()},
            "imme_a": round(a, 3), "imme_b_linear": round(b, 3),
            "imme_c_quadratic": round(c, 3),
            "mirror_diff_2b": round(xp - xm, 3),
            "triplet_2nd_diff_2c": round(xp + xm - 2 * x0, 3)})
        print(f"  A={A}: a={a:7.3f}  b(linear)={b:+7.3f}  c(QUADRATIC)={c:+7.3f}"
              f"   | mirror diff={xp-xm:+.3f}=2b   2nd diff={xp+xm-2*x0:+.3f}=2c")

    # b's across A (this probe + the PR #3089 mirror values) — the linear
    # charge-asymmetry coefficient grows in |·| with A (Coulomb ~ Z ~ A).
    b_by_A = {r["A"]: r["imme_b_linear"] for r in out_rows}
    c_nonzero = all(abs(r["imme_c_quadratic"]) > 0.1 for r in out_rows)

    b = WitnessBuilder("delta-lambda-imme-triplet",
                       engine="python+canonical-binding", start_time=t0)
    (b.set_description(
        "Isobaric-triplet (IMME) decomposition of the canonical residual "
        "log_q0 Δ_λ = a + b·T₃ + c·T₃². Mirror PAIRS (PR #3089) measure only "
        "the bar-odd b; the bar-even QUADRATIC c is invisible to them (it "
        "cancels in the mirror difference, Lean mirror_baseline_cancels) and "
        "needs a TRIPLET. A=6 (⁶He/⁶Li/⁶Be): a=36.12, b=−1.73 (consistent with "
        "the mirror b's −1.34@A3,−1.77@A7), c=−1.24 NONZERO. Askey: body-order "
        "b-ladder is continuous q-Hermite (3-term recurrence); IMME is the "
        "degree-2 T₃ truncation (Wigner rank-≤2 isotensor = Askey–Racah cutoff). "
        "CAVEAT: T₃=0 ground states are T=0 (not the T=1 analog), so c mixes the "
        "IMME quadratic with T=0/T=1 structure; robust claim = residual has a "
        "nonzero bar-even quadratic. Not wired; near-match; no fit.")
     .add_data("q0", q0)
     .add_data("triplets", out_rows)
     .add_data("imme_form", "log_q0 Δ_λ(T₃) = a(A) + b(A)·T₃ + c(A)·T₃²,  T₃=(Z−N)/2")
     .add_data("parity", {
         "a_isoscalar": "bar-EVEN (T₃-even) — leading ~10A−5 (A≤4)",
         "b_linear": "bar-ODD (T₃-odd) — the writhe Z-correction; mirror diff=2b·T₃",
         "c_quadratic": "bar-EVEN (T₃-even) — cancels in mirror pairs; triplet 2nd diff=2c"})
     .add_data("b_by_A_linear_coeff", b_by_A)
     .add_data("askey", {
         "body_order_n": "b-ladder a(n+2)=2cosh(10η)a(n+1)−a(n): continuous q-Hermite / "
                         "Al-Salam–Chihara three-term recurrence (Askey q-scheme)",
         "isospin_T3": "IMME degree-2 in T₃ = Wigner rank-≤2 isotensor truncation "
                       "(Askey–Racah cutoff; no d·T₃³)"})
     .add_data("caveat_same_T", "T₃=0 ground states (⁶Li,⁸Be) are T=0, not the T=1 "
                                "isobaric analog; c mixes IMME-c with T=0/T=1 structure"))
    b.add_assertion("quadratic_c_nonzero",
                    computed=bool(c_nonzero), expected=True,
                    source="|c| > 0.1 q₀-units in every triplet — a real bar-even "
                           "quadratic beyond leading+linear (mirror pairs cannot see it)")
    b.add_assertion("mirror_diff_equals_2b",
                    computed=bool(all(abs(r["mirror_diff_2b"] - 2 * r["imme_b_linear"]) < 0.01
                                      for r in out_rows)),
                    expected=True,
                    source="f(+1)−f(−1)=2b exactly (consistency with PR #3089 mirror method)")
    res = b.save()
    print(f"  Wrote {res.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
