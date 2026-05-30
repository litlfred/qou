"""Baryon EM sinh-channel analog of meson (3q² − 1)/(2q²) — operator-valued probe.

Exploratory probe stubbing the baryon analog of the meson
`prop:meson-em-sinh-closed-form` (PR #1448). The meson got:

  m_K²/m_π² = [3]_q·[4]_q + (α_em/π) · (3q² − 1)/(2q²)
              ──Lean-proved──   ──scalar Lean ring identity──

via the scalar H_2(q) trace of the photon-exchange insertion on
the meson's qq̄ word. The baryon (qqq, H_3(q)) needs the
**operator-valued** LR-branching of `prop:hecke-branching-trace-
decomposition` (PR #1443) since the proton/neutron states are
operator-valued projections onto specific H_3 isotypic components.

Formula (open, target of this probe):

  (m_n² − m_p²) / m_p²
    = (H_3 qCG fusion piece, no fit, framework-derived)
    + (α_em / π) · tr_{V_(2,1)}( A^{(2,1)}_{(1),(1,1)}(I_EM) )
                   / (Hoefsmit denominator at q_0)

where:
- A^{(2,1)}_{(1),(1,1)}(I_EM) is the operator-valued LR coefficient
  for the photon-exchange insertion I_EM on the H_2 ⊗ H_1 ⊂ H_3
  decomposition of the (2,1)-isotypic component (where the
  proton/neutron live);
- The Hoefsmit denominator is the q-dimension of V_(2,1).

What this probe does (with current scaffolding):
1. Construct the H_3 Hoefsmit-seminormal basis numerically at q_0.
2. Construct a STUB I_EM operator (placeholder pending #1443
   merging the operator-valued LR formula). Currently uses a
   trivial diagonal scaffold for shape verification.
3. Compute the candidate sinh-channel trace.
4. Compare against the 1.04 ppb m_n residual.

This is **exploratory / audit-only**. The stub I_EM is NOT
production-derived — it's a structural placeholder until #1443
merges the operator-valued LR formula. After #1443 lands, the
real I_EM construction replaces the stub here.

References:
- prop:hecke-branching-trace-decomposition (PR #1443)
- prop:meson-em-sinh-closed-form (#1448, merged)
- prop:em-coupling-projection (CS-corrected α_em)
- Hoefsmit 1974 Ch III (seminormal basis on H_3)
- docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md
  (companion direction — both may be needed for 100× m_n)
"""
from __future__ import annotations
import sys
import time
from pathlib import Path
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def q_int(k, q):
    """[k]_q = (q^k − q^{-k}) / (q − q^{-1})."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def hoefsmit_denominator_2_1(q):
    """q-dimension of V_(2,1) on H_3(q) — Hoefsmit denominator.

    The (2,1)-isotypic component is 2-dimensional; its q-dim is
    [3]_q (hook-content for the (2,1) partition).
    """
    return q_int(3, q)


def stub_A_lambda_mu_nu_I_em(q):
    """STUB for A^{(2,1)}_{(1),(1,1)}(I_EM) on H_2 ⊗ H_1 ⊂ H_3.

    PLACEHOLDER pending #1443 merging the operator-valued LR
    formula. The real construction will be:

      A^{(2,1)}_{(1),(1,1)}(I_EM) ∈ End(V_(1) ⊗ V_(1,1))^{⊕ c^{(2,1)}_{(1),(1,1)}}

    where c^{(2,1)}_{(1),(1,1)} = 1 is the Littlewood-Richardson
    multiplicity (single isotype), V_(1) ⊗ V_(1,1) is 2-dim, and
    I_EM is the photon-exchange insertion on the qq face inside H_3.

    Current stub: returns a diagonal scaffold with the LO meson-
    style correction factor (3q² − 1)/(2q²) — this is NOT correct
    for the baryon, just a shape probe. Real I_EM will involve
    Hoefsmit matrix elements of σ_1·γ·σ_1⁻¹ where γ is the EM
    insertion at the (1,2) crossing in the proton/neutron word.
    """
    meson_em_factor = (3 * q ** 2 - 1) / (2 * q ** 2)
    return meson_em_factor


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mpf(Q_50_DIGIT_STR)

    print("=" * 76)
    print("  Baryon EM sinh-channel operator-valued probe (STUB, pending #1443)")
    print("=" * 76)
    print()
    print(f"  q_0                                 = {mp.nstr(q, 20)}")
    print(f"  α_em⁻¹ (CS-corrected, Witten κ)     = 137.035944")
    print()

    # CLASS-A acknowledged anchor pending Witten-κ Gram-determinant
    # closure (em-coupling-chern-simons.lean §3b-cond).
    alpha_em_inv = mpf("137.035944")
    alpha_em = 1 / alpha_em_inv

    # Stub operator-valued LR coefficient (placeholder for the real
    # A^{(2,1)}_{(1),(1,1)}(I_EM) from #1443).
    A_stub = stub_A_lambda_mu_nu_I_em(q)
    print(f"  A^(2,1)_(1),(1,1)(I_EM) [STUB]      = {mp.nstr(A_stub, 20)}")

    denom = hoefsmit_denominator_2_1(q)
    print(f"  Hoefsmit denom (q-dim V_(2,1)=[3]_q) = {mp.nstr(denom, 20)}")
    print()

    # Candidate baryon sinh-channel EM correction.
    em_correction = alpha_em / mp.pi * A_stub / denom
    print(f"  Candidate baryon EM correction       = {mp.nstr(em_correction, 12)}")
    print()

    # Compare against m_n residual.
    # Current m_n at 1.04 ppb vs CODATA, residual scale ≈ 1e-9.
    # The EM correction should add to (m_n² − m_p²)/m_p², which
    # at m_p ≈ 938 MeV and Δm ≈ 1.29 MeV is of order (Δm/m_p)·2
    # ≈ 2.75e-3. The EM correction itself is much smaller; we
    # report its relative magnitude for sanity.
    m_n_residual_target = mpf("1.04e-9")  # 1.04 ppb
    em_to_residual_ratio = float(em_correction / m_n_residual_target)
    print(f"  m_n residual target (ppb)            = 1.04")
    print(f"  EM correction (mass-sq frac)         = {float(em_correction):.3e}")
    print(f"  EM correction / m_n residual         = {em_to_residual_ratio:.3e}")
    print()
    print("  Interpretation: this STUB gives the wrong magnitude (the meson")
    print("  (3q²−1)/(2q²) factor is meson-scale, ~0.094); the real")
    print("  baryon I_EM has a different scale + structure. Probe needs")
    print("  #1443's operator-valued formula to compute correctly.")
    print()
    print("  PLACEHOLDER — DO NOT USE AS PREDICTION.")
    print()

    w = WitnessBuilder("baryon-em-sinh-operator-valued-probe",
                       engine="mpmath", start_time=_t0)
    w.set_description(
        "STUB exploratory probe: baryon analog of meson EM sinh-channel "
        "correction. Placeholder I_EM pending PR #1443's operator-valued "
        "LR-branching formula. Reports candidate correction structure + "
        "scale ratio vs m_n's 1.04 ppb residual. Not a production input."
    )
    # Tag as exploratory-only — this MUST NOT feed any dashboard.
    w.set_audit_only(
        "docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md"
    )
    w.add_data("q_0", mp.nstr(q, 50))
    w.add_data("alpha_em_inv", "137.035944")
    w.add_data("A_stub_value_at_q0", mp.nstr(A_stub, 30))
    w.add_data("hoefsmit_denominator_value_at_q0", mp.nstr(denom, 30))
    w.add_data("candidate_em_correction", mp.nstr(em_correction, 30))
    w.add_data("m_n_residual_ppb", "1.04")
    w.add_data("em_to_residual_ratio", em_to_residual_ratio)
    w.add_assertion(
        "stub_placeholder_present",
        computed=1, expected=1, tolerance=0,
        source="Probe is a structural placeholder pending #1443 merge"
    )
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
