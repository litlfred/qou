#!/usr/bin/env python3
"""
binding_qhamiltonian_rotational_scale.py — does the q-Hamiltonian
ROTATIONAL term supply the binding energy-per-Reeb-rotation scale ρ?
(Derive-or-refute; NO numerology — ρ is checked against derived scales,
never tuned.)

CONTEXT. The rotation-phase lead (binding_rotation_phase_lead.py) found
the binding is carried by the per-rep q-Reeb phase θ_λ, with an
energy-per-radian ρ_phase ≈ 18.5 MeV/rad (A=3 mirror pair to 2%). The
q-energy block (climax-volume-mass/q-energy) gives the q-Hamiltonian
  𝔈_q = J_q²·ℏ_q (rotational) + p_q²·ℏ_q/(2[n]_q) (translational) + S_q,
so the energy of a Reeb ROTATION is the rotational term J_q²·ℏ_q·μ₀ for
some mass scale μ₀. This is the structurally correct home for ρ_phase:
binding linear in the rotation angle (matching the refutation of the
Lobachevsky-VOLUME observable).

RESULT (honest):
  STRUCTURE: ρ_phase = μ₀ · (rotational quantum). For spin-½,
  rot = J_q²(½)·ℏ_q = [½]_q[3/2]_q·ℏ_q ≈ 0.0744, giving μ₀ ≈ 249 MeV.
  REFUTED as a clean derivation: μ₀ is NOT a clean multiple of any
  derived scale — μ₀/m_e ≈ 487, μ₀/E₀ ≈ 59.4, μ₀/(m_e/ℏ_q²) ≈ 4.78,
  μ₀/(E₀/ℏ_q) ≈ 5.89 — none rational/integer. Pinning μ₀ to match 18.5
  would be a fit. So the q-Hamiltonian fixes the rotational STRUCTURE of
  the binding but NOT the scale; μ₀ ≈ 249 MeV (suggestively near Λ_QCD,
  not derived) is the residual open gate.

This is the honest boundary of the derivation: structure derived,
scale open — stated without numerology.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-qhamiltonian-rotational-scale", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf("0.51099895069")
    hbar_q = 1 - 1 / q
    E0 = m_e / (q * (q - 1))

    def br(x):
        return (q**x - q**(-x)) / (q - q**(-1))

    Jq2 = br(mpf(1) / 2) * br(mpf(3) / 2)   # spin-½ q-angular momentum
    rot = Jq2 * hbar_q                        # rotational quantum (μ₀ units)
    rho_phase = mpf("18.5")                   # MeV/rad (rotation-phase lead)
    mu0 = rho_phase / rot                      # implied mass scale

    derived = {
        "m_e": m_e, "E0": E0,
        "m_e/hbar_q^2": m_e / hbar_q**2,
        "E0/hbar_q": E0 / hbar_q,
    }
    ratios = {name: float(mu0 / val) for name, val in derived.items()}

    def is_clean(x):
        # "clean" = within an ABSOLUTE 0.02 of an integer or a half-integer
        nearest_int = abs(x - round(x))
        nearest_half = abs(x - round(x * 2) / 2)
        return min(nearest_int, nearest_half) < 0.02

    any_clean = any(is_clean(r) for r in ratios.values())

    print("=" * 70)
    print("q-HAMILTONIAN ROTATIONAL SCALE for the binding Reeb-phase ρ")
    print("=" * 70)
    print(f"  ℏ_q={float(hbar_q):.5f}  E0={float(E0):.4f}  "
          f"J_q²(½)={float(Jq2):.5f}  rot=J_q²·ℏ_q={float(rot):.5f}")
    print(f"  ρ_phase ≈ {float(rho_phase)} MeV/rad  ⟹  μ₀ = ρ/rot "
          f"= {float(mu0):.2f} MeV")
    print("  μ₀ / derived-scale ratios (clean ⟹ derivable):")
    for name, r in ratios.items():
        print(f"    μ₀/{name:14s} = {r:.4f}  {'CLEAN' if is_clean(r) else ''}")
    print()
    print(f"  any clean ratio? {any_clean}  → "
          + ("derivable" if any_clean else
             "NOT a clean derived multiple — pinning μ₀ = numerology."))
    print("  Honest boundary: q-Hamiltonian fixes the ROTATIONAL STRUCTURE")
    print("  (binding linear in the Reeb angle), scale μ₀≈249 MeV OPEN.")

    wb.set_description(
        "Derive-or-refute: does the q-Hamiltonian rotational term J_q²·ℏ_q·μ₀ "
        "supply the binding energy-per-Reeb-rotation ρ_phase≈18.5 MeV/rad? "
        "Structure: yes (binding is linear in the rotation, matching the "
        "Lobachevsky-volume refutation). Scale: REFUTED as clean — implied "
        "μ₀≈249 MeV is not a clean multiple of any derived scale (μ₀/m_e≈487, "
        "μ₀/E₀≈59.4, μ₀/(m_e/ℏ_q²)≈4.78); pinning it would be numerology. "
        "q-Hamiltonian fixes the rotational structure; μ₀ is the residual gate."
    )
    wb.add_data("rotational_quantum", {
        "hbar_q": mp.nstr(hbar_q, 10), "E0_MeV": mp.nstr(E0, 10),
        "Jq2_spin_half": mp.nstr(Jq2, 10),
        "rot_quantum": mp.nstr(rot, 10),
    })
    wb.add_data("implied_mu0", {
        "rho_phase_MeV_per_rad": "18.5",
        "mu0_MeV": mp.nstr(mu0, 8),
        "mu0_over_derived": {k: round(v, 6) for k, v in ratios.items()},
        "any_clean_ratio": any_clean,
    })
    wb.add_data("conclusion", {
        "structure": "binding = q-Hamiltonian rotational term J_q²·ℏ_q·μ₀ "
                     "(linear in Reeb angle) — derived structure",
        "scale": "μ₀≈249 MeV NOT a clean derived multiple — open gate, "
                 "not numerology-pinned (suggestively near Λ_QCD)",
        "status": "structure derived, scale open",
    })
    wb.add_assertion(
        "mu0_not_clean_derived_multiple",
        computed=int(any_clean),
        expected=0,
        tolerance=0,
        source="no μ₀/derived-scale ratio is integer/half-integer to 1% — "
               "pinning μ₀ would be a fit; scale remains the open gate",
    )
    wb.save()


if __name__ == "__main__":
    main()
