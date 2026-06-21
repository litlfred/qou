#!/usr/bin/env python3
"""
Q_β counit/trace consistency at the substrate loop value — ground-truth
evaluation at the CURRENT (proton-anchored) substrate q₀.

Pins the archimedean numbers behind the *merged* counit/transition framing
(PR #2363, docs/audits/2026-06-16-q-beta-path-a-counit-transition-resolution.md;
Lean QOU/Interactions/qbeta_counit_vs_trace.lean + qbeta_energy_scale.lean) at
the live proton-anchored q₀ — confirming the +0.17 % counit value is **not
stale** (the anchor re-pin was 2026-05-28) and characterising the N=0
truncation remainder that the one remaining open item — the *convergence /
consistency leg* — must shrink to zero.

The merged Lean fixed the generic-field algebra with the Markov loop value z
left symbolic, in the N=0 neutron−proton normal-form difference
``(n−p) = [h²/2, −h/2, −h/2, 0, 0, 0]`` (basis [γ, σ₀, σ₁, L₊, L₋, e⁻],
h = q − q⁻¹):

    ε(n−p)        = h²/2 − h          (Frobenius counit / augmentation; the
                                       *right* functional for a transition)
    tr_M(n−p)|z   = h²/2 − h·z        (Markov trace at loop value z; axiom M1
                                       weights γ=𝟙 by 1, each crossing by z)
    ε − tr_M|z    = h·(z − 1)         (exact gap; the two agree iff z = 1)

This script instantiates z at the physical substrate Markov loop value
    z_sub = 1/(√q + 1/√q) = √q/(q + 1) ≈ 0.4993
and multiplies the dimensionless N=0 reduction content by the per-Hecke-step
energy 𝔈₀ = m_e · c_q² · ℏ_q^E = m_e/(q(q−1)) to get the two N=0 Q_β
predictions:

    counit:  Q_β = |ε(Δ)·𝔈₀| = m_e(q+1)|q²−2q−1|/(2q³)   → +0.17 %  (right tool)
    trace :  Q_β = |tr_M(Δ)|_{z_sub}·𝔈₀|                  → −56 %    (wrong tool)

Reproducing BOTH signatures at the live q₀ validates the substrate loop value
(z_sub) and confirms the merged framing is current. It then checks the audit's
structural claim that the +0.17 % counit residual is the N=0 *truncation*
remainder, bounded by O(ℏ_q²/(1−ℏ_q²)) ≈ 1 % — the same order as the 0.74 %
𝔈₀ derived-vs-calibrated gap. That bound is the falsifiable invariant the open
convergence leg must respect (formalize-first: the higher-N brane-tower
corrections must carry the counit N=0 value into CODATA, leaving ≤ ~1 %).

NO fit, NO scan, NO new production wiring. Audit:
docs/audits/2026-06-18-qbeta-counit-substrate-consistency.md.
"""

import pathlib
import sys

import mpmath as mp

_REPO = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.constants import M_E_MEV, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 50
mp.mp.dps = DPS + 15

# CODATA 2022 free-neutron β-decay Q-value (the experimental face of Q_β).
CODATA_QBETA_MEV = mp.mpf("0.78233341")


def rel_pct(computed, reference):
    """Signed relative deviation in percent."""
    return (computed - reference) / reference * 100


def main():
    q = q_at(DPS)                      # proton-anchored substrate q₀ (live)
    me = mp.mpf(str(M_E_MEV))

    # ── q-Planck primitives ───────────────────────────────────────────
    h = q - 1 / q                      # Hecke parameter h = q − q⁻¹
    hbar_q = 1 - 1 / q                 # ℏ_q = 1 − q⁻¹
    hbar_q_sq = hbar_q ** 2
    # 𝔈₀ = m_e · c_q² · ℏ_q^E = m_e/(q−1)² · (q−1)/q = m_e/(q(q−1)).
    E0 = me / (q * (q - 1))

    # ── N=0 reduction content (two functionals) ───────────────────────
    eps = h ** 2 / 2 - h               # ε(Δ): Frobenius counit
    z_sub = mp.sqrt(q) / (q + 1)       # substrate Markov loop value
    trM_zsub = h ** 2 / 2 - h * z_sub  # tr_M(Δ) at the substrate loop
    gap = eps - trM_zsub               # exact gap = h·(z_sub − 1)

    # ── N=0 Q_β predictions (magnitudes; sign encodes the bar-odd sinh) ─
    counit_qbeta = abs(eps * E0)
    trace_qbeta = abs(trM_zsub * E0)

    # closed form cross-check: m_e(q+1)|q²−2q−1|/(2q³)
    counit_closed = abs(me * (q + 1) * (q ** 2 - 2 * q - 1) / (2 * q ** 3))

    counit_res = rel_pct(counit_qbeta, CODATA_QBETA_MEV)
    trace_res = rel_pct(trace_qbeta, CODATA_QBETA_MEV)

    # ── N=0 truncation remainder bound (the falsifiable invariant) ────
    n0_bound_pct = mp.mpf(100) * hbar_q_sq / (1 - hbar_q_sq)
    # 𝔈₀ derived-vs-calibrated gap (the "same residual" the audit cites):
    #   calibrated 𝔈₀ = CODATA Q_β / |ε(Δ)| (the energy/step that would make
    #   the N=0 counit content exact); derived 𝔈₀ = m_e/(q(q−1)).
    E0_cal = CODATA_QBETA_MEV / abs(eps)
    E0_gap_pct = rel_pct(E0, E0_cal)

    # ── report ────────────────────────────────────────────────────────
    print(f"q₀ (proton-anchored)      = {mp.nstr(q, 30)}")
    print(f"h = q − q⁻¹               = {mp.nstr(h, 20)}")
    print(f"ℏ_q² = (1−q⁻¹)²           = {mp.nstr(hbar_q_sq, 20)}")
    print(f"𝔈₀ = m_e/(q(q−1))         = {mp.nstr(E0, 20)} MeV")
    print(f"z_sub = √q/(q+1)          = {mp.nstr(z_sub, 20)}")
    print(f"ε(Δ) = h²/2 − h           = {mp.nstr(eps, 20)}")
    print(f"tr_M(Δ)|z_sub = h²/2−h·z  = {mp.nstr(trM_zsub, 20)}")
    print(f"gap = ε − tr_M = h(z−1)   = {mp.nstr(gap, 20)}")
    print("-" * 64)
    print(f"COUNIT  Q_β = |ε·𝔈₀|      = {mp.nstr(counit_qbeta, 20)} MeV  "
          f"({float(counit_res):+.3f} %)   [right tool]")
    print(f"  closed form cross-check  = {mp.nstr(counit_closed, 20)} MeV")
    print(f"TRACE   Q_β = |tr_M·𝔈₀|   = {mp.nstr(trace_qbeta, 20)} MeV  "
          f"({float(trace_res):+.3f} %)   [wrong tool]")
    print("-" * 64)
    print(f"N=0 truncation bound  ℏ_q²/(1−ℏ_q²) = {float(n0_bound_pct):.4f} %")
    print(f"  observed counit residual           = {float(abs(counit_res)):.4f} %"
          f"   ({'WITHIN' if abs(counit_res) <= n0_bound_pct else 'EXCEEDS'} bound)")
    print(f"  𝔈₀ derived-vs-cal gap              = {float(abs(E0_gap_pct)):.4f} %"
          f"   ({'WITHIN' if abs(E0_gap_pct) <= n0_bound_pct else 'EXCEEDS'} bound)")

    # ── witness ───────────────────────────────────────────────────────
    w = WitnessBuilder("qbeta-counit-substrate-consistency", engine="mpmath")
    w.set_description(
        "Q_β counit/trace consistency at the proton-anchored substrate q₀: "
        "reproduces the merged PR #2363 +0.17 % counit and −56 % trace "
        "signatures at the live anchor (confirming non-staleness), and pins "
        "the N=0 truncation remainder bound O(ℏ_q²/(1−ℏ_q²)) ≈ 1 % that the "
        "open convergence leg must respect."
    )
    w.set_audit_only("docs/audits/2026-06-18-qbeta-counit-substrate-consistency.md")
    w.add_parameter("dps", DPS)
    w.add_parameter("anchor", "proton (m_p/m_e identity, re-pin 2026-05-28)")
    w.add_parameter("q0", mp.nstr(q, DPS))
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("codata_qbeta_MeV", str(CODATA_QBETA_MEV))

    # The counit closed form must equal the ε·𝔈₀ product (algebraic identity,
    # the merged Lean `Qbeta_closed`) — a same-q cross-check, tol 1e-40.
    w.add_assertion(
        "counit_eps_E0_eq_closed_form",
        computed=mp.nstr(counit_qbeta, DPS),
        expected=mp.nstr(counit_closed, DPS),
        tolerance=1e-40,
        unit="MeV",
        source="Lean Qbeta_closed (qbeta_energy_scale.lean)",
    )
    # Counit residual reproduces the merged +0.17 % at the live anchor.
    w.add_assertion(
        "counit_residual_pct",
        computed=float(counit_res),
        expected=0.17,
        tolerance=0.02,
        unit="percent",
        source="PR #2363 audit (+0.17 %)",
    )
    # Trace-at-substrate reproduces the merged −56 % wrong-tool signature.
    w.add_assertion(
        "trace_substrate_residual_pct",
        computed=float(trace_res),
        expected=-56.0,
        tolerance=1.0,
        unit="percent",
        source="PR #2363 audit (−56 %)",
    )
    # The +0.17 % counit residual is within the N=0 truncation bound.
    w.add_assertion(
        "counit_residual_within_N0_bound",
        computed=1.0 if abs(counit_res) <= n0_bound_pct else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="ℏ_q²/(1−ℏ_q²) ≈ 1 % truncation bound",
    )

    w.add_data("h", mp.nstr(h, DPS))
    w.add_data("hbar_q_sq", mp.nstr(hbar_q_sq, DPS))
    w.add_data("E0_MeV", mp.nstr(E0, DPS))
    w.add_data("z_substrate", mp.nstr(z_sub, DPS))
    w.add_data("eps_reduction_content", mp.nstr(eps, DPS))
    w.add_data("trM_at_z_substrate", mp.nstr(trM_zsub, DPS))
    w.add_data("gap_eps_minus_trM", mp.nstr(gap, DPS))
    w.add_data("counit_qbeta_MeV", mp.nstr(counit_qbeta, DPS))
    w.add_data("trace_qbeta_MeV", mp.nstr(trace_qbeta, DPS))
    w.add_data("counit_residual_pct", float(counit_res))
    w.add_data("trace_residual_pct", float(trace_res))
    w.add_data("N0_truncation_bound_pct", float(n0_bound_pct))
    w.add_data("E0_derived_vs_cal_gap_pct", float(E0_gap_pct))

    w.add_caveat(
        "N=0 only. The counit value ε(Δ)·𝔈₀ is built from the N=0 neutron−"
        "proton normal-form difference; its +0.17 % deviation from CODATA is "
        "the N=0 truncation remainder, NOT a fit. The open convergence leg "
        "(prove the full per-braid mass-tower difference m(n)−m(p)−m_e → "
        "ε(Δ)·𝔈₀, remainder ≤ O(ℏ_q²/(1−ℏ_q²))) is unproved here and is the "
        "named structural target — this witness only pins its invariant."
    )
    w.add_caveat(
        "The −56 % trace value is the WRONG functional (Markov trace, a static-"
        "loop mass), not a truncation error — it documents why the counit, not "
        "the trace, is the correct transition functional (merged PR #2363)."
    )
    path = w.save()
    print(f"\nwitness → {path}")


if __name__ == "__main__":
    main()
