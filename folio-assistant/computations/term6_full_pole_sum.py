#!/usr/bin/env python3
"""Term 6 — Mittag-Leffler full pole sum per prop:full-pole-structure-mass-trace.

Per content/.../full-pole-structure-mass-trace.md:

  tr_M(T_w, q_0) = tr_M^entire(T_w, q_0)
                  + Σ_{n≥2} Σ_{gcd(j,n)=1} r_n^{(j)}(T_w) / (q_0 - ζ_n^{(j)})

with poles at every primitive n-th root of unity ζ_n^{(j)}, residues
r_n^{(j)}(T_w), and Cauchy kernel 1/(q_0 − ζ_n^{(j)}).  Sum is
absolutely convergent on the regular locus by Habiro's theorem.

**Caveat (per `tr_M is a Habiro-ring element, not a function on ℂ`):**
the primitive roots are dense in S¹, so this is NOT a complex-analytic
Mittag-Leffler in the ordinary sense.  In the Habiro ring `Ẑ[q]`, the
sum is symbolic / cyclotomic and converges in the q-adic topology.
At q_0 ≈ 1.11 (just outside |q|=1), the truncated sum gives a
meaningful Term-6 contribution whose magnitude this script measures.

Input:
  folio-assistant/computations/habiro-coefficients-atomic.witness.json
  (provides full polynomial tr_M(T_w, q) for proton, neutron;
   deuteron currently MISSING in that witness)

This script:
  1. Loads atom-specific tr_M(T_w, q) as a rational function in q
  2. Factors denominator into cyclotomic polynomials Φ_n(q)
  3. For each ζ_n^{(j)}, computes residue r_n^{(j)} symbolically
  4. Computes Σ r_n^{(j)} / (q_0 − ζ_n^{(j)}) up to cutoff n_max
  5. Compares to direct evaluation tr_M(T_w, q_0)

Output: term6-full-pole-sum.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from experimental_constants import M_E_MEV
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder

HERE = Path(__file__).parent
HABIRO_WITNESS = HERE / "habiro-coefficients-atomic.witness.json"

q = sp.Symbol("q", complex=True)


def primitive_roots_of_unity(n: int):
    """Generate primitive n-th roots of unity (j with gcd(j, n) = 1)."""
    from math import gcd
    if n < 1:
        return
    if n == 1:
        yield 1
        return
    for j in range(1, n):
        if gcd(j, n) == 1:
            yield sp.exp(2 * sp.pi * sp.I * sp.Rational(j, n))


def cyclotomic_residue(tr_M_expr, zeta, n: int):
    """Compute r_n^{(j)}(T_w) = lim_{q → ζ_n^{(j)}} (q − ζ) · tr_M(T_w, q).

    Uses symbolic limit. If tr_M is regular at ζ, the residue is 0.
    """
    expr = (q - zeta) * tr_M_expr
    try:
        return sp.limit(expr, q, zeta)
    except Exception:
        return None


def mittag_leffler_term6(tr_M_poly_expr, q0_value: float, n_max: int = 6):
    """Compute Term-6 Mittag-Leffler sum up to cutoff n_max.

    Uses symbolic ζ_n^{(j)}, complex residue + 1/(q_0 − ζ) kernel.
    Returns (total_term6_real, per_n_breakdown).
    """
    total = sp.Rational(0)
    per_n = []
    q0_sym = sp.Rational(round(q0_value * 10**16), 10**16)
    for n in range(2, n_max + 1):
        n_contribution = sp.Rational(0)
        roots_data = []
        for j_idx, zeta in enumerate(primitive_roots_of_unity(n)):
            try:
                residue = cyclotomic_residue(tr_M_poly_expr, zeta, n)
                if residue is None or residue == 0:
                    roots_data.append({
                        "j_index": j_idx, "zeta": str(zeta),
                        "residue": "0 or None", "contribution": 0.0,
                    })
                    continue
                kernel = 1 / (q0_sym - zeta)
                contribution = residue * kernel
                contribution_complex = complex(sp.N(contribution))
                # Take real part (imaginary parts cancel by symmetry over Φ_n)
                contribution_real = float(contribution_complex.real)
                n_contribution += sp.N(contribution)
                roots_data.append({
                    "j_index": j_idx,
                    "zeta_real": float(complex(sp.N(zeta)).real),
                    "zeta_imag": float(complex(sp.N(zeta)).imag),
                    "residue_complex": [
                        float(complex(sp.N(residue)).real),
                        float(complex(sp.N(residue)).imag),
                    ],
                    "kernel_complex": [
                        float(complex(sp.N(kernel)).real),
                        float(complex(sp.N(kernel)).imag),
                    ],
                    "contribution_real": contribution_real,
                })
            except Exception as e:
                roots_data.append({
                    "j_index": j_idx, "zeta": str(zeta),
                    "error": str(e), "contribution": 0.0,
                })
        n_total_real = float(complex(sp.N(n_contribution)).real)
        per_n.append({
            "n": n, "n_real_contribution": n_total_real, "roots": roots_data,
        })
        total += n_contribution
    return float(complex(sp.N(total)).real), per_n


def evaluate_atom_term6(atom_label: str, atom_data: dict, n_max: int = 6):
    """Evaluate Term 6 for a single atom from its Habiro witness data."""
    print(f"\n━━ {atom_label}")
    p_in_u_str = atom_data.get("p_in_u")
    denom_in_u_str = atom_data.get("denom_in_u")
    if not p_in_u_str or not denom_in_u_str:
        print("    SKIP: no p_in_u / denom_in_u in witness")
        return None
    u = sp.Symbol("u")
    try:
        p_in_u = sp.sympify(p_in_u_str)
        denom_in_u = sp.sympify(denom_in_u_str)
    except Exception as e:
        print(f"    SKIP: sympify failed: {e}")
        return None
    # Convert u = q^{1/2} → tr_M(T_w, q) = p_in_u(u) / denom_in_u(u) at u = sqrt(q)
    sqrt_q = sp.sqrt(q)
    p_in_q = p_in_u.subs(u, sqrt_q)
    denom_in_q = denom_in_u.subs(u, sqrt_q)
    tr_M_expr = p_in_q / denom_in_q
    # Sanity check at q_0
    tr_M_at_q0_check = float(complex(sp.N(tr_M_expr.subs(q, Q_0))).real)
    print(f"    tr_M(T_w, q_0) [from polynomial] = {tr_M_at_q0_check:.6f}")
    print(f"    tr_M_at_q0 [from witness]        = {atom_data.get('tr_M_at_q0', 'N/A')}")

    # Compute Term-6 sum
    total, per_n = mittag_leffler_term6(tr_M_expr, Q_0, n_max=n_max)
    print(f"    Term-6 Mittag-Leffler total (n≤{n_max}) = {total:.6e}")
    print(f"    in MeV: {total * M_E_MEV:.6e}")
    for n_data in per_n:
        n = n_data["n"]
        cn = n_data["n_real_contribution"]
        print(f"      n={n}: contribution = {cn:+.6e}")
    return {
        "atom": atom_label,
        "n_max": n_max,
        "tr_M_at_q0_polynomial": tr_M_at_q0_check,
        "term6_total_real": total,
        "term6_in_MeV": total * M_E_MEV,
        "per_n_breakdown": per_n,
    }


def main():
    print("=" * 78)
    print("Term 6 — Mittag-Leffler full pole sum")
    print("=" * 78)
    print(f"q_0 = {Q_0}")
    print(f"m_e = {M_E_MEV} MeV")
    print()

    if not HABIRO_WITNESS.exists():
        print(f"ERROR: {HABIRO_WITNESS} not found")
        sys.exit(1)
    with open(HABIRO_WITNESS) as f:
        d = json.load(f)
    results = d.get("results", {})
    print(f"Atoms with Habiro coefficients: {list(results.keys())}")
    print()

    n_max = 6  # cutoff: enough to see the pattern, not too slow
    out_atoms = []
    for atom_label, atom_data in results.items():
        result = evaluate_atom_term6(atom_label, atom_data, n_max=n_max)
        if result:
            out_atoms.append(result)

    print()
    print("=" * 78)
    print("Conclusion: Term 6 magnitude vs A≥5 5–20% errors")
    print("=" * 78)
    for r in out_atoms:
        print(f"  {r['atom']:<25} Term-6 = {r['term6_in_MeV']:+.6f} MeV")
    print()
    print("NOTE: this witness has only proton and neutron Habiro data.")
    print("To assess Term 6 for D, T, ³He, ⁴He, ⁶Li–¹⁶O (the A≥5 atoms")
    print("with large residuals), need to extend habiro-coefficients-")
    print("atomic.witness.json to those atoms first.")

    # Build witness
    w = (
        WitnessBuilder("term6-full-pole-sum", engine="python+sympy")
        .set_description(
            "Term 6 Mittag-Leffler full pole sum per "
            "prop:full-pole-structure-mass-trace. Computes Σ_{n≥2} "
            "Σ_{gcd(j,n)=1} r_n^{(j)}(T_w) / (q_0 − ζ_n^{(j)}) using "
            "symbolic Habiro residues + 1/(q_0 − ζ) kernel up to "
            "cutoff n_max=6. Currently only proton, neutron have "
            "Habiro coefficients in the upstream witness; D, T, ³He, "
            "⁴He need extension to assess A≥5 5–20% error closure."
        )
        .set_content_block("prop:full-pole-structure-mass-trace")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("n_max_cutoff", n_max)
        .add_data("atoms", out_atoms)
        .add_caveat(
            "Primitive roots of unity are dense in S¹, so this is NOT "
            "a complex-analytic Mittag-Leffler in the ordinary sense. "
            "tr_M is a Habiro-ring element; convergence is q-adic. "
            "Truncation at n_max=6 captures the dominant Cauchy-kernel "
            "weighted residues (smaller n → closer to q_0 = 1.11 → "
            "larger 1/|q_0 − ζ| kernel)."
        )
        .add_caveat(
            "Extend habiro-coefficients-atomic.witness.json to D, T, "
            "³He, ⁴He, ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹²C, ¹⁶O before this script "
            "can answer 'does Term 6 close the A≥5 5-20% errors?'"
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
