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
    α_EM · ℏc = 1.43996 MeV·fm   (CODATA fine-structure × ℏc; the framework's derived
                                  α_EM ≈ 1/137 substitutes 1:1 to the quoted precision),
    r₀        = 1.2 fm           (standard uniform-charged-sphere nuclear radius constant).
The `Z(Z−1)` (rather than `Z²`) is the self-energy of Z discrete protons (no proton self-
interaction). The uniform-sphere model is known to over-estimate the Coulomb displacement energy
of light nuclei by ~5–10% per pair (the Nolen–Schiffer anomaly); treat E_C as the leading EM
term, not a high-precision value.

This is a (a) scope-limited EM-sector quantity. It does NOT rewire the strong core (the canonical
charge-symmetric gg bond is gated on `conj:s5-so3-fiber-action`, the s5-so3 keystone) and does NOT
change any strong-binding witness; it is an additive term reported alongside the strong forms.
"""
from __future__ import annotations

# Standard nuclear-physics inputs (not fit to binding data).
ALPHA_HBAR_C_MEV_FM = 1.43996   # α_EM · ℏc  (CODATA); framework α_EM ≈ 1/137 substitutes 1:1
R0_FM = 1.2                      # uniform-sphere nuclear radius constant, R = r₀ · A^{1/3}


def nuclear_radius_fm(A: int) -> float:
    """R = r₀ · A^{1/3} fm — the uniform-charged-sphere radius."""
    return R0_FM * A ** (1.0 / 3.0)


def coulomb_energy_mev(Z: int, A: int) -> float:
    """Electrostatic energy E_C = (3/5)·Z(Z−1)·α_EM·ℏc/(r₀·A^{1/3}) in MeV.

    Z = proton number, A = mass number. Returns 0 for Z < 2 (no proton pair).
    This is the energy by which the EM repulsion REDUCES the net nuclear binding."""
    if Z < 2 or A < 1:
        return 0.0
    return 0.6 * Z * (Z - 1) * ALPHA_HBAR_C_MEV_FM / nuclear_radius_fm(A)


def mirror_displacement_mev(Z_hi: int, Z_lo: int, A: int) -> float:
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
