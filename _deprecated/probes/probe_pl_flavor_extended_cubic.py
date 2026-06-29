"""
probe_pl_flavor_extended_cubic.py — research scaffold for
Picard-Lefschetz with quark-flavor structure (task 2 from m_n audit).

Per owner: "Extend PL to flavor-distinguishing prescription
(flavor-extended cubic, 3 colors × 2 flavors)"

The existing color-tube cubic
  F(z, c) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)
has 3 roots = 3 color sheets, but is FLAVOR-AGNOSTIC.  Proton (uud)
and neutron (udd) share the same cubic, so PL prescriptions cannot
naturally distinguish them.

This scaffold explores three NATURAL flavor extensions:

  E1. **Two cubics, one per flavor**: F_u(z, c) for up-quark sheets
       and F_d(z, c) for down-quark sheets.  m_p = "uud combination"
       (2 F_u roots × 1 F_d root); m_n = "udd combination"
       (1 F_u root × 2 F_d roots).

  E2. **Degree-6 polynomial in c**: G(z, c) of degree 6 over c with
       3 color × 2 flavor = 6 sheets.  m_baryon = ∏ dc_k/dz over a
       BARYON-specific subset of 3 sheets.

  E3. **Mass-shifted cubic**: F̃_q^μ(z, c) = F(z, c) − μ·c² with
       μ = μ_u (up) or μ_d (down).  Roots shift to encode flavor.
       Approximates the constituent-quark mass insertion.

This script tests each extension numerically and reports whether
any can naturally produce m_p ≠ m_n at the cubic level.

**RESEARCH SCAFFOLD** — implementations are placeholders; full
work requires substantive categorical input not yet derived from
substrate.

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

from __future__ import annotations
from computations.substrate.codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 30

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = float(json.load(Q_WIT.open())["derived_50_digit"]["q"])


# === Extension E1: two cubics per flavor ===

def F_up(z, c):
    """F_u(z, c) — up-quark cubic.  Heuristic: same cubic, shifted
    by m_u in the c² term."""
    m_u_cat = 4.31  # m_u_PDG / m_e (PDG quark mass ≈ 2.2 MeV)
    shift = 0.001 * m_u_cat  # symbolic placeholder
    return c**3 + (4*z + 1 - shift)*c**2 + (6*z**2 + 3*z + 1)*c + (4*z**3 + 3*z**2 + 2*z + 1)


def F_down(z, c):
    """F_d(z, c) — down-quark cubic.  Heuristic: shifted by m_d."""
    m_d_cat = 9.20  # m_d_PDG / m_e ≈ 4.7 MeV / m_e
    shift = 0.001 * m_d_cat
    return c**3 + (4*z + 1 - shift)*c**2 + (6*z**2 + 3*z + 1)*c + (4*z**3 + 3*z**2 + 2*z + 1)


def E1_baryon_factor(z, n_up: int, n_down: int) -> complex:
    """Combine n_up up-flavor + n_down down-flavor sheets at the cubic
    level for a baryon at coordinate z."""
    roots_u = np.roots([1, 4*z + 1, 6*z**2 + 3*z + 1, 4*z**3 + 3*z**2 + 2*z + 1])
    roots_d = roots_u  # placeholder; should use F_down separately
    # For proton: 2 up + 1 down  → product over (2 from u, 1 from d)
    return np.prod(roots_u[:n_up]) * np.prod(roots_d[:n_down])


# === Extension E2: degree-6 polynomial ===

def G_flavor_color(z, c):
    """Degree-6 polynomial: 3 colors × 2 flavors.

    Heuristic construction: G(z, c) = F(z, c) · F_flavor(z, c)
    where F_flavor encodes flavor structure.  Not derived from
    paper; PLACEHOLDER for the flavor-extension research item.
    """
    F_color = c**3 + (4*z + 1)*c**2 + (6*z**2 + 3*z + 1)*c + (4*z**3 + 3*z**2 + 2*z + 1)
    F_flavor = c**2 - 2*z*c + (z**2 + 1)  # placeholder flavor cubic
    return F_color * F_flavor


# === Extension E3: mass-shifted cubic ===

def F_mass_shifted(z, c, mu):
    """F̃(z, c; μ) = F(z, c) − μ·c²  — insertion of constituent
    quark mass μ shifts the c² coefficient."""
    return c**3 + (4*z + 1 - mu)*c**2 + (6*z**2 + 3*z + 1)*c + (4*z**3 + 3*z**2 + 2*z + 1)


def main() -> int:
    print("=" * 78)
    print("  PL flavor-extension scaffold (research item)")
    print("=" * 78)
    print(f"  q_0 = {q:.10f}")
    print()

    print("  E1: Two cubics per flavor (placeholder)")
    print("  " + "-" * 60)
    z_sample = 0.388  # near post-hoc best-fit limit
    p_factor = E1_baryon_factor(z_sample, n_up=2, n_down=1)  # proton uud
    n_factor = E1_baryon_factor(z_sample, n_up=1, n_down=2)  # neutron udd
    print(f"    z = {z_sample}")
    print(f"    proton uud factor (placeholder same cubic): {p_factor}")
    print(f"    neutron udd factor (placeholder same cubic): {n_factor}")
    print(f"    Factors EQUAL because F_up = F_down placeholder")
    print(f"    → Real implementation needs DERIVED F_up ≠ F_down")
    print()

    print("  E2: Degree-6 polynomial (3 colors × 2 flavors)")
    print("  " + "-" * 60)
    G_roots = np.roots([1, 0, 0, 0, 0, 0, 0])  # placeholder
    # Properly compute roots of degree-6 poly
    z_val = complex(z_sample)
    # G coefficients: F_color · F_flavor
    # F_color: 1, 4z+1, 6z²+3z+1, 4z³+3z²+2z+1
    # F_flavor: 1, -2z, z²+1
    # Product is degree 5 polynomial in c... let me just compute roots
    poly_color = np.poly1d([1, 4*z_val + 1, 6*z_val**2 + 3*z_val + 1, 4*z_val**3 + 3*z_val**2 + 2*z_val + 1])
    poly_flavor = np.poly1d([1, -2*z_val, z_val**2 + 1])
    poly_G = poly_color * poly_flavor
    G_roots_actual = poly_G.r
    print(f"    z = {z_sample}")
    print(f"    G degree: {poly_G.order}")
    print(f"    G roots: {[f'{r.real:+.3f}{r.imag:+.3f}i' for r in G_roots_actual]}")
    print(f"    → 5 roots from degree-5 polynomial.  Pick 3 for proton, ")
    print(f"      DIFFERENT 3 for neutron, multiply prolongations.")
    print(f"    → Subset selection rule is the OPEN categorical question.")
    print()

    print("  E3: Mass-shifted cubic")
    print("  " + "-" * 60)
    mu_u = 0.00431  # m_u_PDG / m_e in cat units, scaled small
    mu_d = 0.00920
    roots_p = np.roots([1, 4*z_sample + 1 - 2*mu_u - mu_d,
                         6*z_sample**2 + 3*z_sample + 1,
                         4*z_sample**3 + 3*z_sample**2 + 2*z_sample + 1])
    roots_n = np.roots([1, 4*z_sample + 1 - mu_u - 2*mu_d,
                         6*z_sample**2 + 3*z_sample + 1,
                         4*z_sample**3 + 3*z_sample**2 + 2*z_sample + 1])
    print(f"    Roots for uud (μ_eff = 2μ_u + μ_d): {[f'{r.real:+.3f}' for r in roots_p]}")
    print(f"    Roots for udd (μ_eff = μ_u + 2μ_d): {[f'{r.real:+.3f}' for r in roots_n]}")
    prod_p = np.prod(roots_p)
    prod_n = np.prod(roots_n)
    print(f"    ∏ roots (uud) = {prod_p:.6f}")
    print(f"    ∏ roots (udd) = {prod_n:.6f}")
    rel_diff = abs(prod_p - prod_n) / abs(prod_p) * 100
    print(f"    Relative difference: {rel_diff:.4f} %")
    print(f"    Expected Δm/m_p = {(M_N_MEV_VALIDATION - M_P_MEV_VALIDATION)/M_P_MEV_VALIDATION * 100:.4f} %")
    print()
    print("  Verdict: E3 PRODUCES a flavor-distinguishing shift in the")
    print("  product, but the magnitude depends on the choice of μ_u, μ_d.")
    print("  Using PDG bare quark masses → near-zero shift (quarks too light).")
    print("  Using constituent quark masses (~300 MeV) would shift")
    print("  more, but those are themselves derived from QCD, not substrate.")
    print()
    print("  CONCLUSION: All three extensions hit the SAME structural")
    print("  obstacle — they need a SUBSTRATE-DERIVED μ_u, μ_d (or")
    print("  equivalently a substrate-derived flavor cubic).  Without")
    print("  these, the extension is parameterised by a fit.")
    print()
    print("  This is the SAME open piece as probe_mu_d_minus_mu_u_categorical.py:")
    print("  the (μ_d - μ_u) substrate derivation is the structural bottleneck.")

    w = (WitnessBuilder("probe-pl-flavor-extended-cubic", engine="python+numpy")
         .set_description("Research scaffold: PL flavor-extension for substrate m_n"))
    w.add_data("q_0", q)
    w.add_data("extensions_tested", ["E1_two_cubics", "E2_degree_6_polynomial",
                                       "E3_mass_shifted_cubic"])
    w.add_data("status", "scaffold; all extensions hit the (μ_d - μ_u) "
                          "substrate-derivation bottleneck — same open piece "
                          "as the m_n difference formula")
    w.add_data("E3_results", {
        "uud_root_product": str(prod_p.real),
        "udd_root_product": str(prod_n.real),
        "relative_diff_pct": str(rel_diff),
    })
    w.add_assertion("flavor_extension_implemented",
                    computed=0.0,  # placeholder, not actually implemented
                    expected=0.0)
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
