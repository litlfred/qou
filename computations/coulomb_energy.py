#!/usr/bin/env python3
"""Canonical electrostatic (Coulomb) energy of a nucleus — the EM-sector binding term.

The strong-sector binding forms in this repo (`B_sym`, `B_qCLT`, `B_vol`, the Borromean
tower) are purely strong: they carry NO electromagnetic contribution. Standard nuclear
physics splits the nuclear binding into a strong part and the electrostatic repulsion of
the Z protons, which REDUCES the net binding of proton-rich nuclei. This module provides
that EM term as a first-class, reusable quantity (bean 754x).

Why it matters here (bean 754x). The production inter-nucleon bond assigns the like-nucleon
crossings as `p-p ↦ σ`, `n-n ↦ σ⁻¹` — a flavor-only projection that over-breaks strong charge
symmetry by ~78% and fabricates a 3–4.5× too-large mirror-nucleus binding split. Building the
bond through flavor-blind gg production makes the strong core EXACTLY charge-symmetric (the 78%
collapses to 0; `probes/gg_production_bond_probe.py`), at which point the genuine mirror split
must come from THIS Coulomb term. The kill-switch (`probes/coulomb_mirror_killswitch_probe.py`)
confirms a charge-symmetric strong core + this Coulomb energy reproduces the ³H/³He, ⁷Li/⁷Be,
¹³C/¹³N mirror splits to ~20–40% (within the known uniform-sphere / Nolen–Schiffer over-estimate
for light nuclei), vs the production σ/σ⁻¹ form's ~200–350% error.

Model + inputs (standard nuclear physics, NOT fit to binding data):
    E_C(Z, A) = (3/5) · Z(Z−1) · α_EM · ℏc / R,    R = r₀ · A^{1/3},
with
    α_EM      = DERIVED from q₀ (Bring zero-mode / q[9]_q[10]_q), giving
                1/α_EM = 137.035935094 and α_EM·ℏc = 1.4399652199 MeV·fm.
                It was CODATA until 2026-08-09; see the α_EM block below.
    ℏc        = 197.3269804152 MeV·fm  (unit conversion, legitimately external),
    r₀        = 1.2 fm           (EMPIRICAL saturation constant — the module's
                                  largest remaining import; wrong for A ≤ 4).
The `Z(Z−1)` (rather than `Z²`) is the self-energy of Z discrete protons (no proton self-
interaction). The uniform-sphere model over-estimates the Coulomb displacement energy of light nuclei;
treat E_C as the leading EM term, not a high-precision value.

    CORRECTION 2026-08-09 — that over-estimate is NOT the Nolen–Schiffer anomaly, and the
    two have OPPOSITE SIGNS. Measured at A = 3:

      r₀ = 1.2 fm geometry     E_C = 0.998413 MeV   +30.7 %  vs experiment  (OVER)
      measured charge radius   E_C = 0.680772 MeV   −10.9 %  vs experiment  (UNDER)
      experiment (³He−³H)            0.7638   MeV

    (a) The +30.7 % is a pure GEOMETRY error. r₀ = 1.2 fm is a heavy-nucleus constant; at
        A = 3 it gives R = 1.7307 fm, while ³He's rms charge radius is 1.9661 fm, i.e. an
        equivalent uniform R = √(5/3)·r_rms = 2.5382 fm and an implied r₀ = 1.760 fm.
        Fixable by using the measured radius — at the cost of importing an experimental
        input the framework otherwise avoids.
    (b) The Nolen–Schiffer anomaly (Nolen & Schiffer, Ann. Rev. Nucl. Sci. 19 (1969) 471)
        is the OPPOSITE: once the Coulomb energy is computed properly, theory falls SHORT
        of experiment by ~7 % across medium-mass mirror pairs. That ~7 % is the standard
        literature figure; its uniformity across a wide mass range is what makes it an
        anomaly rather than a modelling defect. The −10.9 % / +0.0830 MeV quoted above is
        NOT a literature value — it is this file's own equivalent-uniform-sphere estimate
        from the measured charge radius, which is far cruder than the Faddeev calculations
        the published A = 3 residual comes from. It lands in the right range (published
        A = 3 shortfalls are roughly 0.06–0.08 MeV) but should not be cited as the
        standard number. It is not a modelling slip; it is
        the standard evidence for charge-symmetry breaking in the strong NN force,
        sourced in the SM by m_d − m_u and ρ–ω mixing — i.e. FLAVOUR effects.

    Consequence for this framework, and it is a real gap: QOU's strong mirror split comes
    from the σ / σ⁻¹ crossing-sign assignment, which carries NO flavour content, while its
    flavour-breaking parameter δ = flavor_split_leading enters ONLY the p–n bond — and
    `QOU.QBeta.InterfaceScalar.mirror_split_eq_L_diff` proves the mirror split is
    α(L_nn − L_pp), in which the p–n bond CANCELS EXACTLY. So δ contributes identically
    zero to the mirror split. QOU has its charge-symmetry breaking in the topological
    channel where the eightfold way says it belongs in the flavour channel. Bean qou-4waf.

This is a (a) scope-limited EM-sector quantity. It does NOT rewire the strong core (the canonical
charge-symmetric gg bond is gated on `conj:s5-so3-fiber-action`, the s5-so3 keystone) and does NOT
change any strong-binding witness; it is an additive term reported alongside the strong forms.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from canonical_mass import _as_formattable_mpf  # noqa: E402

set_compute_dps()

# ── α_EM: DERIVED, not CODATA (fixed 2026-08-09, bean qou-usft) ──────────
# This module used to hard-code `ALPHA_HBAR_C_MEV_FM = 1.43996`, the CODATA
# value, as a Python float. Two defects in one line:
#
#   * PROVENANCE. The framework DERIVES α_EM from q₀ (the Bring zero-mode /
#     q[9]_q[10]_q form) and already uses the derived value in the meson EM
#     sector (`meson_em_sinh_closed_form._alpha_em_inv_derived`). Consuming
#     CODATA here made every Coulomb energy in the binding dashboard — a
#     PREDICTED observable — quietly depend on an experimental input. That is
#     not a small thing when the framework's headline is that it is
#     parameter-free. Found by `audits/derived_alpha_em_usage_audit.py`.
#   * FLOAT64, against the standing owner directive. Now mpmath throughout.
#
# The numerical effect is tiny and that is the point: derived 1/α_EM =
# 137.035935094 vs CODATA 137.035999177, i.e. 468 ppb apart, shifting E_C by
# 3.6 ppm. The number barely moves; the CLAIM does.
#
# ℏc is a unit conversion (CODATA, exact-by-definition inputs), not a physical
# input being predicted, so it legitimately stays.
HBAR_C_MEV_FM = mp.mpf("197.3269804152")

# ── the nuclear length: CAL-3, not an empirical r₀ (2026-08-09, bean qou-usft) ──
# `r₀ = 1.2 fm` is an EMPIRICAL saturation constant. The corpus's own rule is
# that "all corpus lengths arise as Compton inversions ℏc/mass"
# (`deltalambda/pion_radius_and_cusp_volume_gap_probe.py:56`), and CAL-3 is m_π,
# so the framework's available nuclear length is the reduced pion Compton
# wavelength λ̄_π = ℏc/m_π = 1.4138169 fm. Measured at A = 3:
#
#     radius model                     R (fm)      err      E_C      E_C err
#     r₀·A^{1/3}, r₀ = 1.2 EMPIRICAL   1.730699  −31.81 %  0.998416  +30.72 %
#     λ̄_π·A^{1/3}          CAL-3      2.039077  −19.67 %  0.847422  +10.95 %
#     measured charge radius           2.538224    0.00 %  0.680774  −10.87 %
#
# So the CAL-3 length is both a PROVENANCE improvement (an empirical constant
# replaced by a calibration-derived one) and a NUMERICAL one (E_C error +30.7 %
# → +11.0 %). It is now the default; the empirical constant is retained below
# as `R0_FM_EMPIRICAL` for comparison only.
#
# NOT NEW WORK, and A^{1/3} IS NOT DERIVED. `deltalambda/mirror_split_continuum_em_probe.py`
# already uses exactly this radius law (`R(A) = λ̄_π·A^{1/3}`, its line 15) and
# already classifies both of its steps, more carefully than this module did:
#   * `A^{1/3}` — "radius law from VOLUME EXTENSIVITY … **WEAK STEP (named)**:
#     the hyperbolic volume of the link complement is a topological invariant,
#     NOT a Euclidean spatial volume … an archimedean identification the corpus
#     does not derive". Tier: CONDITIONAL/PARTIAL. (:39-49)
#   * `R(A) = 1·λ̄_π·A^{1/3}` — "**THE UNDERIVED STEP**. The packing radius equal
#     to the pion Compton wavelength at coefficient EXACTLY 1 is a SELECTION
#     among the framework's four mass scales". (:50-53)
# So A^{1/3} is a saturation/liquid-drop assumption, not a derivation, and
# measurement agrees: solving R = λ̄_π·A^x for x gives 0.9679 (²H), 0.4314 (³H),
# 0.5326 (³He), 0.3067 (⁴He) — it would need 0.3333 throughout. Size tracks
# BINDING, not nucleon count. Bean qou-usft.
#
# HONEST LIMIT. The COEFFICIENT is not derived. The corpus probe's GAP 1 asks
# why the packing length is λ̄_π "at coefficient EXACTLY 1" and reports it
# MEASURED at 0.985 ± 0.069 — consistent with 1, not proved to be 1. And GAP 2,
# the hyperbolic-volume → Euclidean-radius step behind A^{1/3}, is also open. So
# this is a better-sourced length, not a derived one.
#
# DO NOT read the near-symmetry of +10.95 % (λ̄_π) against −10.87 % (measured
# radius) as meaningful. They have different causes: the first is a 19.7 %-small
# radius, the second is the Nolen–Schiffer strong-CSB residual (bean qou-4waf).
LAMBDA_BAR_PI_FM = HBAR_C_MEV_FM / mp.mpf("139.57039")   # CAL-3 Compton length
R0_FM_EMPIRICAL = mp.mpf("1.2")      # retained for comparison; NOT the default
R0_FM = LAMBDA_BAR_PI_FM

# The uniform-BALL shape factor. Also an import: with the radius divided out,
# the shape-only factor spans 0.4547 (exponential) → 0.4886 (Gaussian), a 7.3 %
# spread that is the same size as the whole Nolen–Schiffer anomaly. Deriving the
# density profile rather than assuming a uniform ball is tracked on qou-usft.
#
# Do not reach for the q-CLT here: it factorises the Markov trace over BONDS
# (B_qCLT = α·bonds·ℓ̄), so it lives in trace space and is not a distribution
# over ℝ³. The corpus has assumed metrics (Fubini–Study on Bring's surface, the
# round metric on P(V) ≅ S²) but no transport from its algebraic invariants to a
# Euclidean length, and says so itself —
# `deltalambda/pion_radius_and_cusp_volume_gap_probe.py:56`: "there is NO
# categorical volume→length transport in the corpus. All corpus lengths arise as
# Compton inversions ℏc/mass." Beans qou-mumr, qou-adwi.
UNIFORM_SPHERE_FACTOR = mp.mpf(3) / 5


def _resolve_q_mpf(q=None) -> "mp.mpf":
    """Resolve optional `q` to an `mp.mpf` at ≥50 dps (defaults to `Q_50_DIGIT_STR`)."""
    with mp.workdps(max(50, mp.mp.dps)):
        if q is None:
            from q_parameter import Q_50_DIGIT_STR
            return mp.mpf(Q_50_DIGIT_STR)
        return mp.mpf(str(q))


def alpha_em_inv_bring_schwinger(q=None, loop_variant: str = "hHecke_sq") -> "mp.mpf":
    """Form-B Bring–Schwinger cubic inverse fine-structure constant 1/α_EM(q)
    (Corrected Photon, Lean `QOU.Archimedean.BringSchwingerNormalizationDerivation`):
        1/α = T_EM(q) + α · H(q) · (1 − c_loop(q) · α),
        T_EM(q) = q · [9]_q · [10]_q + 2 / (3π),
        H(q)    = [2]_q / (8π),
    where `c_loop(q)` defaults to the Kazhdan–Lusztig bar-Hermitian skein
    contraction `h² = (q − q⁻¹)²` (`loop_variant='hHecke_sq'`, giving
    1/α_EM(q₀) = 137.03599912695091242017270049642000673995567550574,
    −0.365 ppb vs CODATA 2022). Also supports `loop_variant` in
    `{'c0_quadratic', 'hbarQ_sq', 'deltaHabiroSq', 'hHecke_sq'}`.
    """
    with mp.workdps(max(60, mp.mp.dps + 10)):
        qx = _resolve_q_mpf(q)
        h = qx - 1 / qx
        q2 = qx + 1 / qx
        q9 = (qx ** 9 - qx ** (-9)) / h
        q10 = (qx ** 10 - qx ** (-10)) / h
        t_em_const = qx * q9 * q10 + mp.mpf(2) / (3 * mp.pi)
        h_norm = q2 / (8 * mp.pi)
        v = loop_variant.lower()
        if v in ("hhecke_sq", "c_hhecke_sq", "form_b", "bring_schwinger"):
            c_loop = h ** 2
        elif v in ("c0_quadratic", "c0", "quadratic", "form_a"):
            c_loop = mp.mpf(0)
        elif v in ("hbarq_sq", "c_hbarq_sq"):
            c_loop = (1 - 1 / qx) ** 2
        elif v in ("deltahabirosq", "c_deltahabirosq"):
            c_loop = q2 - 2
        else:
            raise ValueError(
                f"alpha_em_inv_bring_schwinger: unknown loop_variant {loop_variant!r}"
            )

        def _cubic(a):
            return (
                -c_loop * h_norm * (a ** 3)
                + h_norm * (a ** 2)
                + t_em_const * a
                - mp.mpf(1)
            )

        a_root = mp.findroot(_cubic, mp.mpf(1) / t_em_const)
        ainv = mp.mpf(1) / a_root
    return _as_formattable_mpf(+ainv)


alpha_em_inv_corrected_photon = alpha_em_inv_bring_schwinger


def alpha_em_inv_cs_derived(q=None) -> "mp.mpf":
    """Chern–Simons / Bring zero-mode inverse fine-structure constant 1/α_EM^{CS}(q)
    via `meson_em_sinh_closed_form._alpha_em_inv_derived(q)` (≈ 137.035935094).
    """
    from meson_em_sinh_closed_form import _alpha_em_inv_derived
    with mp.workdps(max(50, mp.mp.dps)):
        qx = _resolve_q_mpf(q)
        return _as_formattable_mpf(_alpha_em_inv_derived(qx))


def alpha_em_hbar_c_mev_fm(q=None, photon_mode: str = "bring_schwinger") -> "mp.mpf":
    """α_EM·ℏc in MeV·fm, with α_EM DERIVED from q₀ (not CODATA).

    Parameters
    ----------
    q : optional substrate parameter (defaults to `Q_50_DIGIT_STR`).
    photon_mode : {'bring_schwinger', 'corrected_photon', 'form_b', 'cs'}
        - 'bring_schwinger' (default): Form-B Bring–Schwinger cubic corrected photon
          (`alpha_em_inv_bring_schwinger`, 1/α_EM ≈ 137.035999127, −0.365 ppb vs CODATA 2022).
        - 'cs': Chern–Simons `_alpha_em_inv_derived` (1/α_EM ≈ 137.035935094).
    """
    with mp.workdps(max(50, mp.mp.dps)):
        mode = photon_mode.lower()
        if mode in ("bring_schwinger", "corrected_photon", "form_b", "cubic"):
            ainv = alpha_em_inv_bring_schwinger(q=q)
        elif mode in ("cs", "chern_simons", "legacy_cs"):
            ainv = alpha_em_inv_cs_derived(q=q)
        else:
            raise ValueError(
                f"alpha_em_hbar_c_mev_fm: unknown photon_mode {photon_mode!r} "
                "(use 'bring_schwinger' or 'cs')"
            )
        return _as_formattable_mpf(HBAR_C_MEV_FM / ainv)


def alpha_em_hbar_c_bring_schwinger_mev_fm(q=None) -> "mp.mpf":
    """α_EM·ℏc in MeV·fm using the Form-B Bring–Schwinger cubic corrected photon."""
    return alpha_em_hbar_c_mev_fm(q=q, photon_mode="bring_schwinger")


def alpha_em_hbar_c_cs_mev_fm(q=None) -> "mp.mpf":
    """α_EM·ℏc in MeV·fm using the CS `_alpha_em_inv_derived` form."""
    return alpha_em_hbar_c_mev_fm(q=q, photon_mode="cs")


def nuclear_radius_fm(A: int) -> "mp.mpf":
    """R = λ̄_π · A^{1/3} fm — the uniform-charged-sphere radius.

    The length is CAL-3 derived (ℏc/m_π), not the empirical r₀ = 1.2 fm; see the
    block above. A^{1/3} is still saturation scaling and is still wrong for
    A ≤ 4 — at A = 3 this lands −19.7 % against the measured equivalent radius,
    which is better than the empirical constant's −31.8 % but not right."""
    return R0_FM * mp.mpf(A) ** (mp.mpf(1) / 3)


def coulomb_energy_mev(
    Z: int, A: int, q=None, photon_mode: str = "bring_schwinger"
) -> "mp.mpf":
    """Electrostatic energy E_C = (3/5)·Z(Z−1)·α_EM·ℏc/(r₀·A^{1/3}) in MeV.

    Z = proton number, A = mass number, q = optional substrate parameter
    (defaults to canonical `Q_50_DIGIT_STR`), photon_mode = 'bring_schwinger'
    (Form-B Bring–Schwinger cubic corrected photon, default) or 'cs'.
    Returns 0 for Z < 2 (no proton pair).
    This is the energy by which the EM repulsion REDUCES the net nuclear binding.

    Returns an `mpf`, not a float — strictly more precise than the previous
    float64 return, so callers that wrap it in `mp.mpf(str(...))` are unaffected."""
    with mp.workdps(max(50, mp.mp.dps)):
        if Z < 2 or A < 1:
            return _as_formattable_mpf(mp.mpf(0))
        return _as_formattable_mpf(
            UNIFORM_SPHERE_FACTOR * Z * (Z - 1)
            * alpha_em_hbar_c_mev_fm(q=q, photon_mode=photon_mode) / nuclear_radius_fm(A)
        )


def coulomb_energy_bring_schwinger_mev(Z: int, A: int, q=None) -> "mp.mpf":
    """Electrostatic energy E_C(Z, A) in MeV using the Form-B Bring–Schwinger corrected photon."""
    return coulomb_energy_mev(Z, A, q=q, photon_mode="bring_schwinger")


def coulomb_energy_cs_mev(Z: int, A: int, q=None) -> "mp.mpf":
    """Electrostatic energy E_C(Z, A) in MeV using the CS `_alpha_em_inv_derived` photon."""
    return coulomb_energy_mev(Z, A, q=q, photon_mode="cs")


def mirror_displacement_mev(
    Z_hi: int, Z_lo: int, A: int, q=None, photon_mode: str = "bring_schwinger"
) -> "mp.mpf":
    """Coulomb displacement energy ΔE_C = E_C(Z_hi, A) − E_C(Z_lo, A) for a mirror
    pair at fixed A (Z_hi > Z_lo). Positive: the higher-Z member is less bound by ΔE_C.
    On a charge-symmetric strong core this equals the mirror binding split B(lo) − B(hi)."""
    with mp.workdps(max(50, mp.mp.dps)):
        return _as_formattable_mpf(
            coulomb_energy_mev(Z_hi, A, q=q, photon_mode=photon_mode)
            - coulomb_energy_mev(Z_lo, A, q=q, photon_mode=photon_mode)
        )


def mirror_displacement_bring_schwinger_mev(
    Z_hi: int, Z_lo: int, A: int, q=None
) -> "mp.mpf":
    """Coulomb displacement energy ΔE_C in MeV using the Form-B Bring–Schwinger corrected photon."""
    return mirror_displacement_mev(Z_hi, Z_lo, A, q=q, photon_mode="bring_schwinger")


def mirror_displacement_cs_mev(Z_hi: int, Z_lo: int, A: int, q=None) -> "mp.mpf":
    """Coulomb displacement energy ΔE_C in MeV using the CS `_alpha_em_inv_derived` photon."""
    return mirror_displacement_mev(Z_hi, Z_lo, A, q=q, photon_mode="cs")


if __name__ == "__main__":
    # Quick self-check on the mirror pairs (matches the kill-switch probe).
    for (lo, Zlo, hi, Zhi, A) in [("3H", 1, "3He", 2, 3), ("7Li", 3, "7Be", 4, 7),
                                  ("13C", 6, "13N", 7, 13)]:
        print(f"{lo}/{hi} (A={A}): E_C({lo})={coulomb_energy_mev(Zlo, A):.3f}  "
              f"E_C({hi})={coulomb_energy_mev(Zhi, A):.3f}  "
              f"ΔE_C={mirror_displacement_mev(Zhi, Zlo, A):+.3f} MeV")
