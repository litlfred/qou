#!/usr/bin/env python3
"""alpha_em_schwinger_ladder_probe.py

The α_EM O(α²) tower at the CORRECT (proton) anchor — 80-dps evaluation of:
  - form A  (quadratic, α²H + αT − 1 = 0; NO Schwinger)        1/α resid = +0.9937 ppb (6.48 σ_α)
  - form B  (cubic, +derived 4-topology Schwinger (1−h²α))     1/α resid = −0.3652 ppb (−2.38 σ_α)
  - form C  (cubic, +conditional 2-loop Bloch-B_3(C) defect)   1/α resid = −0.0241 ppb (−0.16 σ_α)

1-LOOP SCHWINGER DERIVATION STATUS (updated after PR #9360, `0 sorry`):
`QOU.Archimedean.EmFermionLoopFourTopology` proved symbolically over Q(q) that
summing all **4** signed chiral 2-vertex crossing topologies (ε₁, ε₂) ∈ {+1, −1}²
on the U_q(sl₂) `EmFermionLoop` module under the bar-Hermitian skein pairing
(−ε₁·ε₂) σ^{ε₁} σ^{ε₂} cancels the order-(q−1)¹ chiral tadpoles ±h·m(σ₂)
identically (the 1-topology +0.1281 check of 2026-07-14 evaluated only the
unchiralised (+,+) topology where the Markov tadpole z = q³/(q²+1) dominated)
and yields **−1 · h²** (`four_topology_bar_hermitian_sum = -h^2`). This makes
the (1 − h²α) factor in Form B derived (`137.03599912695`, `−0.3652 ppb`,
`−2.383σ`), while the Bring zero-mode classes (`ArchimedeanLimit`,
`BlochSuslinUniqueness`, `BringZeroModeBlochClass`) and un-averaged U(1) skein
vertex normalization remain the named conditional (`§3b-cond`) inputs.

2-LOOP BLOCH-B_3(C) DIAGNOSTIC (`form_C_bloch_b3`, PR #9360, `0 sorry` `§3b-cond`):
`QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger` evaluates the zero-parameter
weight-3 Bloch-group trilogarithm defect Δ_{B_3}(q) = ζ(3) − Li₃(q⁻²) normalized
on H₁(Σ₄) (b₁ = 8): c₂_Bloch = H(q)·(ζ(3) − Li₃(q⁻²))/(8π), solving
`(c2_bloch_b3 − H·h²)·α³ + H·α² + T·α − 1 = 0` → `1/α = 137.035999173696...`
(`−0.024112 ppb`, `−0.1573σ`, conditional on `AlphaEmTwoLoopBlochSchwingerClass`).

🛑 THE REFERENCE IS READ FROM THE REGISTRY (CODATA 2022):
The 2018→2022 edition shift is 0.6787 ppb — **2.2× the form-B residual itself** —
flipping Form B from +0.3134 ppb (vs 2018) to −0.3652 ppb (vs 2022). Against the
L2 100× target (`0.0015325 ppb`), Form B misses by `238.3×` and conditional Form C
misses by `15.73×`.

Companion: alpha_em_anchor_preference_probe.py, alpha_em_form_ladder_probe.py,
QOU/Archimedean/EmFermionLoopFourTopology.lean,
QOU/Archimedean/AlphaEmTwoLoopBlochSchwinger.lean,
QOU/Archimedean/EmCouplingBringZeroMode.lean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402

set_compute_dps(80)
mp.mp.dps = max(mp.mp.dps, 80)

_ALPHA_INV = _codata.codata("inverse fine-structure constant")
CODATA = mpf(_ALPHA_INV.value_str)
SIGMA_PPB = mpf(_ALPHA_INV.uncertainty_str) / CODATA * mpf(10) ** 9
CODATA_2018 = mpf("137.035999084")

Q_PROTON = q_at(80)
assert mp.nstr(Q_PROTON, 48) == mp.nstr(mpf(Q_50_DIGIT_STR), 48)
KAPPA1_OHTSUKI = mpf(11) * mp.sqrt(mpf(3)) * mp.pi / mpf(108)


def qb(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def ppb(v: mpf) -> mpf:
    """Signed residual against CODATA-2022 in ppb, carried as 80-dps ``mpf``."""
    return (v - CODATA) / CODATA * mpf(10) ** 9


def _solve_cubic(c3: mpf, c2: mpf, c1: mpf, c0: mpf, init: mpf) -> mpf:
    """Solve c3*a^3 + c2*a^2 + c1*a + c0 = 0 at full mp.dps via Newton iteration."""
    a_val = init
    for _ in range(35):
        f_val = c3 * (a_val ** 3) + c2 * (a_val ** 2) + c1 * a_val + c0
        fp_val = mpf(3) * c3 * (a_val ** 2) + mpf(2) * c2 * a_val + c1
        step = f_val / fp_val
        a_val -= step
        if abs(step) < mpf("1e-85"):
            break
    return a_val


def main() -> int:
    set_compute_dps(80)
    mp.mp.dps = max(mp.mp.dps, 80)

    print("=" * 78)
    print(" α_EM O(α²) tower at the proton anchor — form-A → form-B → form-C ladder")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-schwinger-ladder", engine="mpmath")
    wb.set_description(
        "80-dps alpha_EM ladder at the proton pin, scored against CODATA 2022 read from "
        "qou_substrate.codata: form A (quadratic, no Schwinger) resid +0.9937 ppb (6.48 sigma) "
        "-> form B (cubic with 1-loop Schwinger factor (1-h^2 alpha), proved symbolically "
        "over Q(q) in QOU.Archimedean.EmFermionLoopFourTopology (#9360, 0 sorry) by summing "
        "all 4 signed chiral 2-vertex crossing topologies (eps1,eps2) in {+,-}^2 on U_q(sl_2) "
        "EmFermionLoop, cancelling the +/-h*m(sigma_2) chiral tadpoles identically to -1*h^2; "
        "Bring zero-mode classes ArchimedeanLimit / BlochSuslinUniqueness / BringZeroModeBlochClass "
        "remain the named conditional inputs) resid -0.3652 ppb (-2.383 sigma, 238.3x L2 100x bar) "
        "-> form C (conditional §3b-cond AlphaEmTwoLoopBlochSchwingerClass two-loop Bloch-B_3(C) "
        "trilogarithm defect c2_bloch_b3 = H*(zeta(3) - Li_3(q^-2))/(8*pi), #9360, 0 sorry) "
        "1/alpha = 137.035999173696..., resid -0.024112 ppb (-0.1573 sigma, within 1 sigma_exp)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    q = Q_PROTON
    h2 = (q - mpf(1) / q) ** 2
    T = q * qb(9, q) * qb(10, q) + mpf(8) / (mpf(12) * mp.pi)
    H = qb(2, q) / (mpf(8) * mp.pi)

    # form A: quadratic α²H + αT − 1 = 0
    aA = (-T + mp.sqrt(T * T + mpf(4) * H)) / (mpf(2) * H)
    # form B: cubic, 1/α = T + αH(1 − h²α)  ⇒  −H·h²·α³ + H·α² + T·α − 1 = 0
    aB = _solve_cubic(-H * h2, H, T, -mpf(1), mpf(1) / T)
    # form C: two-loop Bloch-B_3(C) cubic, (c2_bloch_b3 − H·h²)·α³ + H·α² + T·α − 1 = 0
    delta_b3 = mp.zeta(3) - mp.polylog(3, q ** (-2))
    c2_bloch_b3 = H * delta_b3 / (mpf(8) * mp.pi)
    aC = _solve_cubic(c2_bloch_b3 - H * h2, H, T, -mpf(1), aB)

    invA, invB, invC = mpf(1) / aA, mpf(1) / aB, mpf(1) / aC
    rA, rB, rC = ppb(invA), ppb(invB), ppb(invC)
    sigA = rA / SIGMA_PPB
    sigB = rB / SIGMA_PPB
    sigC = rC / SIGMA_PPB

    print(f"\n  proton pin q0 = {mp.nstr(q, 18)}   h² = {mp.nstr(h2, 12)}")
    print(f"  form A (no Schwinger)     : 1/α = {mp.nstr(invA, 16)}   resid = {mp.nstr(rA, 6)} ppb  ({mp.nstr(sigA, 4)} σ)")
    print(f"  form B (+4-topo 1−h²α)    : 1/α = {mp.nstr(invB, 16)}   resid = {mp.nstr(rB, 6)} ppb  ({mp.nstr(sigB, 4)} σ)")
    print(f"  form C (+Bloch-B3 2-loop) : 1/α = {mp.nstr(invC, 16)}   resid = {mp.nstr(rC, 6)} ppb  ({mp.nstr(sigC, 4)} σ)  [conditional §3b-cond]")
    print(f"  Schwinger 1-loop term closes {mp.nstr(rA - rB, 6)} ppb (proved 4-topology EmFermionLoop sum = -1*h^2)")

    resB = invB - CODATA
    c2_emp = resB / (aB ** 2)

    wb.add_data("ladder_proton", {
        "form_A_no_schwinger_ppb": fmt(rA, 80),
        "form_B_schwinger_ppb": fmt(rB, 80),
        "schwinger_shift_ppb": fmt(rA - rB, 80),
        "form_A_sigma": fmt(abs(sigA), 80),
        "form_B_sigma": fmt(abs(sigB), 80),
        "form_B_signed_sigma": fmt(sigB, 80),
        "form_A_miss_vs_100x": fmt(abs(rA) / (SIGMA_PPB / mpf(100)), 80),
        "form_B_miss_vs_100x": fmt(abs(rB) / (SIGMA_PPB / mpf(100)), 80),
        "form_A_alpha_inv": fmt(invA, 80),
        "form_B_alpha_inv": fmt(invB, 80),
        "form_B_schwinger_derivation": (
            "derived: QOU.Archimedean.EmFermionLoopFourTopology (#9360, 0 sorry) proves "
            "4-topology signed skein sum (eps1,eps2) in {+,-}^2 on U_q(sl_2) EmFermionLoop "
            "cancels +/-h*m(sigma_2) chiral tadpoles identically to -1*h^2 over Q(q); "
            "conditional on ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass"
        ),
        "form_C_alpha_inv": fmt(invC, 80),
        "form_C_ppb": fmt(rC, 80),
        "form_C_sigma": fmt(sigC, 80),
        "form_C_miss_vs_100x": fmt(abs(rC) / (SIGMA_PPB / mpf(100)), 80),
        "form_C_bloch_b3": {
            "c2_bloch_b3": fmt(c2_bloch_b3, 80),
            "delta_b3_zeta3_minus_li3_q_inv2": fmt(delta_b3, 80),
            "form_C_alpha_inv": fmt(invC, 80),
            "form_C_ppb": fmt(rC, 80),
            "form_C_sigma": fmt(sigC, 80),
            "form_C_miss_vs_100x": fmt(abs(rC) / (SIGMA_PPB / mpf(100)), 80),
            "lean_module": "QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger",
            "status": "conditional (§3b-cond AlphaEmTwoLoopBlochSchwingerClass)",
        },
        "q0": fmt(q, 80),
    })
    wb.add_data("codata_reference", {
        "alpha_inv": _ALPHA_INV.value_str,
        "uncertainty": _ALPHA_INV.uncertainty_str,
        "sigma_ppb": fmt(SIGMA_PPB, 80),
        "source": "qou_substrate.codata registry (data/allascii.txt, CODATA 2022)",
        "hardcoded_previously": "137.035999084 (CODATA 2018), sigma_ppb 0.15 (a 2% rounding of 0.15325)",
        "edition_shift_ppb": fmt((CODATA - CODATA_2018) / CODATA * mpf(10) ** 9, 80),
        "note": (
            "the edition shift is 2.2x the form-B residual and flips its sign "
            "(+0.3134 ppb vs 2018 -> -0.3652 ppb vs 2022); the magnitude and the "
            "sigma count barely move, the sign does"
        ),
    })
    wb.add_data("two_loop", {
        "one_loop_four_topology_sum": "-1 * (q - q^-1)^2 (proved in QOU.Archimedean.EmFermionLoopFourTopology, 0 sorry)",
        "c2_empirical_from_form_B": fmt(c2_emp, 80),
        "c2_bloch_b3_candidate": fmt(c2_bloch_b3, 80),
        "kappa1_ohtsuki": fmt(KAPPA1_OHTSUKI, 80),
        "c2_vs_kappa1": f"c2 ~ {mp.nstr(KAPPA1_OHTSUKI / abs(c2_emp), 3)}x smaller — different object",
        "status": "conditional two-loop Bloch-B_3(C) evaluated (§3b-cond AlphaEmTwoLoopBlochSchwingerClass: -0.0241 ppb, -0.157 sigma)",
    })
    wb.add_assertion(
        "schwinger_brings_alpha_within_3sigma",
        computed=("1" if abs(rB) < mpf(3) * SIGMA_PPB else "0"),
        expected="1",
        tolerance="0.5",
        source="form B (proton + derived 4-topology Schwinger (1-h^2 alpha)) |resid| = 0.3652 ppb < 3*sigma (0.4598 ppb)",
    )
    wb.add_assertion(
        "schwinger_improves_over_form_A",
        computed=("1" if abs(rB) < abs(rA) else "0"),
        expected="1",
        tolerance="0.5",
        source="Schwinger 1-loop term reduces |resid| from +0.9937 ppb to 0.3652 ppb",
    )
    wb.add_assertion(
        "form_C_bloch_b3_within_1sigma",
        computed=("1" if abs(rC) < SIGMA_PPB else "0"),
        expected="1",
        tolerance="0.5",
        source="conditional 2-loop Bloch-B_3(C) cubic |resid| = 0.0241 ppb < 1*sigma (0.1533 ppb)",
    )
    wb.save()

    print(
        f"\n  RESULT: Form B (4-topology 1−h²α proved) = {mp.nstr(rB, 5)} ppb ({mp.nstr(sigB, 4)} σ); "
        f"Form C (conditional Bloch-B3) = {mp.nstr(rC, 5)} ppb ({mp.nstr(sigC, 4)} σ)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
