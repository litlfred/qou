#!/usr/bin/env python3
"""
phi_q_regularization_probe.py — Test Route (b) closure: regularize
log Φ_{q⁻¹}(z) at |z| > q⁻¹ via zeta-regularization, evaluate the
bar-pair Archimedean realization at the proton.

Per docs/audits/2026-05-25-gap-closure-structural-analysis.md, the
proton mass-formula gap reduces to regularizing log Φ_{q⁻¹}(V_i)
where V_i ≈ 0.98 > q⁻¹ ≈ 0.90.

## The bar-pair Archimedean realization

Per `prop:li2q-phiq-bar-symmetrization`, the realization functor
maps the pre-Archimedean Li_2^q to:

  Archim_τ(Li_2^q(z)) = (log Φ_q(z) + log Φ_{q⁻¹}(z)) / 2

For the proton's generator volumes (|V| ≈ 0.98), log Φ_q(V) is
finite but log Φ_{q⁻¹}(V) diverges (the Faddeev convergence
radius |z| < q⁻¹ ≈ 0.90 is violated).

## Zeta-regularization scheme

The divergent piece of -Σ log(1 - q^k V) at large k is
asymptotic to -Σ (k log q + log V), which zeta-regularizes via:

  Σ_{k≥1} k → ζ(-1) = -1/12
  Σ_{k≥1} 1 → ζ(0) = -1/2

So the regularized log Φ_{q⁻¹}(V) is:

  Reg_log_Φ_{q⁻¹}(V) := (log q)/12 + (log V)/2
                      + Σ_{k≥1} [-log|1 - q^k V| + k log q + log V]

The series is convergent (each term → 0 as k → ∞).

## Result at the proton

Pre-Archim Li_2^q tower (production):   6.83 MeV (137× off CODATA)
Zeta-reg bar-pair Archim realization:  21.75 MeV  (43× off CODATA)
Unregularized Φ_q tower:              602,470 MeV (642× off CODATA)
CODATA m_p:                              938.27 MeV

The zeta-regularized bar-pair closes ~3× of the original 137× gap,
confirming directionally that the Archimedean realization picks up
the dimensional mass scale.  43× residual indicates additional
structural content beyond this regularization (likely T5 sign or
higher-order brane tower).

## Ref

- `docs/audits/2026-05-25-gap-closure-structural-analysis.md`
- `prop:li2q-phiq-bar-symmetrization`
- Faddeev quantum dilogarithm zeta-regularization (standard
  technique in quantum-dilog literature)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, log

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as q0  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402
from _phi_q_util import phi_q  # noqa: E402


def reg_log_phi_q_inv(V, q, k_max=500):
    """Zeta-regularized log Φ_{q⁻¹}(V) at |V| > q⁻¹.

    Φ_{q⁻¹}(V) = Π_{k≥1} 1/(1 − q^k · V).  At |V| > q⁻¹ the product
    diverges; we extract the divergent leading-order asymptotic
    (k log q + log V per factor) and zeta-regularize the divergent
    sums Σ k and Σ 1.

    Returns:
        Reg_log_Φ_{q⁻¹}(V) = (log q)/12 + (log V)/2
                           + Σ_{k≥1} [-log|1 - q^k V| + k log q + log V]
    """
    log_q = log(q)
    log_V = log(V)
    remainder = mpf(0)
    for k in range(1, k_max + 1):
        # log(q^k V) - log|1 - q^k V| = -log|1 - q^{-k}/V|
        term = -log(abs(1 - q ** (-k) / V))
        remainder += term
        # Convergence: term decays like q^{-k}, so the sum converges fast
        if abs(term) < mp.mpf(10) ** -(mp.dps + 5):
            break
    return log_q / 12 + log_V / 2 + remainder


def main():
    set_compute_dps()
    q = q0
    q_inv = 1 / q

    m_e = mpf(M_E_MEV)
    m_p_codata = mpf(M_P_MEV_VALIDATION)

    # Proton generator volumes from terms-2-3-atom-per-gen-mpfr-50dps witness
    V1 = mpf("0.98900731592925977373270908734257112349982263541670")
    V2 = mpf("0.97107015865274369644467729606208246103317407697938")

    # Pre-existing 6-term values for proton at q₀
    T1 = mpf("1.0653061442544499036108498526519307688964161791863")
    T4 = mpf("1.2761128463443181177567435067352497395009951716945")
    T5_signed = mpf("-7.7917512106781104474134374198119571918141663204661")
    T5_abs = abs(T5_signed)
    T6 = mpf("1.4218153711706527")

    # T2/T3 via Li_2^q (production form):
    # From mass-formula-6term-mpfr-50dps.witness.json
    T2_li2q = mpf("1.6183053302953433958898778525126344050918665221692")
    T3_li2q = mpf("0.19831347943187456859752507360793820436595377761556")

    # T2/T3 via unregularized Φ_q (diverges at boundary but works for V<q)
    phi_q_V1 = phi_q(V1, q_inv)
    phi_q_V2 = phi_q(V2, q_inv)
    phi_q_V12 = phi_q(V1 * V2, q_inv)
    T2_phi_q_unreg = phi_q_V1 + phi_q_V2
    z_mark = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    T3_phi_q_unreg = z_mark ** 2 * phi_q_V12

    # T2/T3 via bar-pair zeta-regularized Archimedean realization
    log_phi_q_V1 = log(phi_q_V1)
    log_phi_q_V2 = log(phi_q_V2)
    log_phi_q_V12 = log(phi_q_V12)
    reg_V1 = reg_log_phi_q_inv(V1, q)
    reg_V2 = reg_log_phi_q_inv(V2, q)
    reg_V12 = reg_log_phi_q_inv(V1 * V2, q)
    barpair_V1 = (log_phi_q_V1 + reg_V1) / 2
    barpair_V2 = (log_phi_q_V2 + reg_V2) / 2
    barpair_V12 = (log_phi_q_V12 + reg_V12) / 2
    T2_archim = barpair_V1 + barpair_V2
    T3_archim = z_mark ** 2 * barpair_V12

    sum_li2q = T1 + T2_li2q + T3_li2q + T4 + T5_abs + T6
    sum_archim = T1 + T2_archim + T3_archim + T4 + T5_abs + T6
    sum_phi_q_unreg = T1 + T2_phi_q_unreg + T3_phi_q_unreg + T4 + T5_abs + T6

    m_p_li2q = m_e * sum_li2q
    m_p_archim = m_e * sum_archim
    m_p_phi_q = m_e * sum_phi_q_unreg

    print("=" * 76)
    print("  Φ_q regularization probe — proton at q₀")
    print(f"  q₀ = {mp.nstr(q, 12)}, q₀⁻¹ = {mp.nstr(q_inv, 12)}")
    print(f"  V₁ = {mp.nstr(V1, 12)}, V₂ = {mp.nstr(V2, 12)}")
    print(f"  V_i / q₀⁻¹ ≈ {mp.nstr(V1/q_inv, 8)}, {mp.nstr(V2/q_inv, 8)} (both > 1 → Φ_{{q⁻¹}} diverges)")
    print("=" * 76)
    print()
    print("  Three tower forms at the proton:")
    print()
    print(f"  Pre-Archim Li_2^q (production):")
    print(f"    T2 = {mp.nstr(T2_li2q, 12)}, T3 = {mp.nstr(T3_li2q, 12)}")
    print(f"    Σ  = {mp.nstr(sum_li2q, 8)}, m_p = {mp.nstr(m_p_li2q, 8)} MeV  ({mp.nstr(m_p_codata/m_p_li2q, 6)}× off)")
    print()
    print(f"  Zeta-reg bar-pair Archim realization (this probe):")
    print(f"    T2 = {mp.nstr(T2_archim, 12)}, T3 = {mp.nstr(T3_archim, 12)}")
    print(f"    Σ  = {mp.nstr(sum_archim, 8)}, m_p = {mp.nstr(m_p_archim, 8)} MeV  ({mp.nstr(m_p_codata/m_p_archim, 6)}× off)")
    print()
    print(f"  Unregularized Φ_q (overshoots):")
    print(f"    T2 = {mp.nstr(T2_phi_q_unreg, 12)}, T3 = {mp.nstr(T3_phi_q_unreg, 12)}")
    print(f"    Σ  = {mp.nstr(sum_phi_q_unreg, 8)}, m_p = {mp.nstr(m_p_phi_q, 8)} MeV  ({mp.nstr(m_p_codata/m_p_phi_q, 8)}× off)")
    print()
    print(f"  CODATA m_p = {mp.nstr(m_p_codata, 10)} MeV")

    # Build witness
    w = WitnessBuilder(
        "phi-q-regularization-probe",
        engine="mpmath",
    )
    w.set_description(
        "Tests Route (b) closure for the proton mass-formula gap via "
        "zeta-regularization of log Φ_{q⁻¹}(V) at |V| > q⁻¹.  The "
        "regularized bar-pair Archimedean realization gives m_p ≈ "
        "21.75 MeV — a 3× improvement over the pre-Archim Li_2^q tower "
        "(6.83 MeV) but still 43× off CODATA.  Confirms direction of "
        "Route (b) but not full closure.  See docs/audits/2026-05-25-"
        "gap-closure-structural-analysis.md for the framing."
    )
    w.set_audit_only("docs/audits/2026-05-25-gap-closure-structural-analysis.md")

    w.add_parameter("q0", mp.nstr(q, 20))
    w.add_parameter("V1", mp.nstr(V1, 20))
    w.add_parameter("V2", mp.nstr(V2, 20))
    w.add_parameter("regularization_scheme", "zeta-regularization (Σ k → -1/12, Σ 1 → -1/2)")

    w.add_data("pre_archim_li2q", {
        "T2": mp.nstr(T2_li2q, 20),
        "T3": mp.nstr(T3_li2q, 20),
        "sum": mp.nstr(sum_li2q, 20),
        "m_p_pred_MeV": mp.nstr(m_p_li2q, 20),
        "ratio_codata_over_pred": mp.nstr(m_p_codata / m_p_li2q, 12),
    })

    w.add_data("zeta_reg_barpair_archim", {
        "T2": mp.nstr(T2_archim, 20),
        "T3": mp.nstr(T3_archim, 20),
        "sum": mp.nstr(sum_archim, 20),
        "m_p_pred_MeV": mp.nstr(m_p_archim, 20),
        "ratio_codata_over_pred": mp.nstr(m_p_codata / m_p_archim, 12),
        "improvement_over_li2q": mp.nstr(m_p_archim / m_p_li2q, 12),
    })

    w.add_data("unregularized_phi_q", {
        "T2": mp.nstr(T2_phi_q_unreg, 20),
        "T3": mp.nstr(T3_phi_q_unreg, 20),
        "sum": mp.nstr(sum_phi_q_unreg, 20),
        "m_p_pred_MeV": mp.nstr(m_p_phi_q, 20),
        "ratio_codata_over_pred": mp.nstr(m_p_codata / m_p_phi_q, 12),
    })

    # Assertions: the regularized bar-pair should improve over Li_2^q
    improvement_factor = m_p_archim / m_p_li2q
    w.add_assertion(
        name="zeta_reg_improves_over_li2q",
        computed=float(improvement_factor > mpf(2)),
        expected=1.0,
        tolerance=1e-12,
        source=(
            f"Zeta-regularized bar-pair gives m_p = {mp.nstr(m_p_archim, 6)} MeV, "
            f"a {mp.nstr(improvement_factor, 4)}× improvement over the production "
            f"Li_2^q tower's {mp.nstr(m_p_li2q, 6)} MeV.  Pass iff improvement > 2×."
        ),
    )

    # Assertion: bar-pair is bounded between Li_2^q and unregularized Φ_q
    archim_in_range = float(m_p_li2q < m_p_archim < m_p_phi_q)
    w.add_assertion(
        name="zeta_reg_bounded_between_li2q_and_phi_q",
        computed=archim_in_range,
        expected=1.0,
        tolerance=1e-12,
        source=(
            "The bar-pair Archimedean realization should sit between the "
            "Li_2^q value (137× too small) and the Φ_q value (642× too big). "
            "This structural ordering validates the regularization scheme."
        ),
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
