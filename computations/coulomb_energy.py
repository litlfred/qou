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

# r₀ = 1.2 fm remains an EMPIRICAL saturation constant and is the module's
# largest remaining import. It is a heavy-nucleus constant and FAILS badly for
# light nuclei: at A = 3 it gives R = 1.7307 fm against a measured equivalent
# 2.5382 fm, a −31.8 % error and the source of the +30.7 % E_C over-estimate.
# The derived replacement for A ≤ 4 is the binding length ℏc/√(2μS_sep)
# (−6.3 % at ³He, −1.9 % at ³H) — see bean qou-usft. NOT wired yet.
R0_FM = mp.mpf("1.2")

# The uniform-BALL shape factor. Also an import: with the radius divided out,
# the shape-only factor spans 0.4547 (exponential) → 0.4886 (Gaussian), a 7.3 %
# spread that is the same size as the whole Nolen–Schiffer anomaly. Deriving the
# density profile (q-CLT) rather than assuming a uniform ball is tracked on
# qou-usft.
UNIFORM_SPHERE_FACTOR = mp.mpf(3) / 5


def alpha_em_hbar_c_mev_fm() -> "mp.mpf":
    """α_EM·ℏc in MeV·fm, with α_EM DERIVED from q₀ (not CODATA)."""
    from q_parameter import Q_50_DIGIT_STR
    from meson_em_sinh_closed_form import _alpha_em_inv_derived
    return HBAR_C_MEV_FM / _alpha_em_inv_derived(mp.mpf(Q_50_DIGIT_STR))


def nuclear_radius_fm(A: int) -> "mp.mpf":
    """R = r₀ · A^{1/3} fm — the uniform-charged-sphere radius.

    Saturation scaling. Valid for heavy nuclei; see R0_FM above for why it is
    wrong for A ≤ 4."""
    return R0_FM * mp.mpf(A) ** (mp.mpf(1) / 3)


def coulomb_energy_mev(Z: int, A: int) -> "mp.mpf":
    """Electrostatic energy E_C = (3/5)·Z(Z−1)·α_EM·ℏc/(r₀·A^{1/3}) in MeV.

    Z = proton number, A = mass number. Returns 0 for Z < 2 (no proton pair).
    This is the energy by which the EM repulsion REDUCES the net nuclear binding.

    Returns an `mpf`, not a float — strictly more precise than the previous
    float64 return, so callers that wrap it in `mp.mpf(str(...))` are unaffected."""
    if Z < 2 or A < 1:
        return mp.mpf(0)
    return (UNIFORM_SPHERE_FACTOR * Z * (Z - 1)
            * alpha_em_hbar_c_mev_fm() / nuclear_radius_fm(A))


def mirror_displacement_mev(Z_hi: int, Z_lo: int, A: int) -> "mp.mpf":
    """Coulomb displacement energy ΔE_C = E_C(Z_hi, A) − E_C(Z_lo, A) for a mirror
    pair at fixed A (Z_hi > Z_lo). Positive: the higher-Z member is less bound by ΔE_C.
    On a charge-symmetric strong core this equals the mirror binding split B(lo) − B(hi)."""
    return coulomb_energy_mev(Z_hi, A) - coulomb_energy_mev(Z_lo, A)


if __name__ == "__main__":
    # Quick self-check on the mirror pairs (matches the kill-switch probe).
    for (lo, Zlo, hi, Zhi, A) in [("3H", 1, "3He", 2, 3), ("7Li", 3, "7Be", 4, 7),
                                  ("13C", 6, "13N", 7, 13)]:
        print(f"{lo}/{hi} (A={A}): E_C({lo})={coulomb_energy_mev(Zlo, A):.3f}  "
              f"E_C({hi})={coulomb_energy_mev(Zhi, A):.3f}  "
              f"ΔE_C={mirror_displacement_mev(Zhi, Zlo, A):+.3f} MeV")
