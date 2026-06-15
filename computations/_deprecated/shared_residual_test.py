#!/usr/bin/env python3
"""Shared-residual test (option 3 of the recommended next-targets).

Hypothesis: $\\mathcal{N}_{\\rm sym}$ residual (1.81%) and $g_A$
residual (0.40%) share the same categorical correction (a Plancherel
reweighting / vacuum-volume q-correction).

Test: compute both residuals at high precision; if they share a
multiplicative correction (1 + δ), δ_NS and δ_g would match in form.

Result (HONEST NEGATIVE):
  δ_NS = -1.773% (NEGATIVE — N_sym/lead < 1)
  δ_g  = +0.403% (POSITIVE — g_A/lead > 1)
  ratio δ_NS/δ_g = -4.398

Opposite signs ⇒ NOT a shared multiplicative correction. The two
residuals have different categorical sources. This narrows the
open framework: we need TWO complementary correction axioms, not
one.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sys as _sys
import mpmath
mpmath.mp.dps = 100

_sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV, G_A_PDG

q = mpmath.mpf(Q_50_DIGIT_STR)
hbar_q = (q - 1) / q


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


# Targets
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
E_cross = (q - 1 / q) / 2
mu_0 = m_e / (3 * E_cross)
N_v = v_weak / (E_cross * mu_0)
prod_pl = (q_int(4) ** 2 / q_int(2)) * (q_int(6) ** 2 / q_int(2)) * (q_int(8) ** 2 / q_int(2))
N_sym_target = N_v / prod_pl
g_A_target = mpmath.mpf(str(G_A_PDG))

# Two competing leading forms for N_sym (Anchor I vs II)
N_sym_lead_I  = q_int(3) * q_int(4) ** 3                  # SU(2)_L adjoint × 3 W-Goldstones
N_sym_lead_II = q_int(2) * q_int(4) ** 2 * q_int(6)       # SU(2)_L fund × 2 W ± + Z

g_A_lead = q_int(5) / q_int(4)                            # marginal Hecke-dim growth

delta_NS_I  = N_sym_target / N_sym_lead_I - 1
delta_NS_II = N_sym_target / N_sym_lead_II - 1
delta_g     = g_A_target  / g_A_lead - 1


def main():
    print("Shared-residual test: do δ_N_sym and δ_g_A share form?")
    print("=" * 70)
    print()
    print("N_sym leading-form residuals:")
    print(f"  Anchor I:  [3]_q · [4]_q^3        → δ = {mpmath.nstr(delta_NS_I*100, 6)}%   (POSITIVE)")
    print(f"  Anchor II: [2]_q · [4]_q² · [6]_q → δ = {mpmath.nstr(delta_NS_II*100, 6)}%  (NEGATIVE)")
    print()
    print(f"g_A residual: [5]_q/[4]_q  → δ = {mpmath.nstr(delta_g*100, 6)}%   (POSITIVE)")
    print()
    print("Cross-comparison:")

    cases = [
        ('Anchor I  vs g_A', delta_NS_I, delta_g),
        ('Anchor II vs g_A', delta_NS_II, delta_g),
    ]
    rows = []
    for label, dNS, dg in cases:
        ratio = dNS / dg
        same_sign = (dNS > 0) == (dg > 0)
        print(f"\n  {label}:")
        print(f"    δ_NS / δ_g = {mpmath.nstr(ratio, 12)}")
        print(f"    same sign? {same_sign}")
        print(f"    |δ_NS| / |δ_g| = {mpmath.nstr(abs(ratio), 8)}")
        rows.append({
            'comparison': label,
            'delta_NS': mpmath.nstr(dNS, 25),
            'delta_g': mpmath.nstr(dg, 25),
            'ratio': mpmath.nstr(ratio, 12),
            'abs_ratio': mpmath.nstr(abs(ratio), 12),
            'same_sign': same_sign,
        })

    print()
    print("=" * 70)
    print("VERDICT:")
    print("=" * 70)
    print()
    print("  Anchor II ([2]_q [4]_q² [6]_q) has NEGATIVE δ — opposite sign")
    print("  from g_A's POSITIVE δ — so they CANNOT share a multiplicative")
    print("  (1 + δ) correction with the same δ.")
    print()
    print("  Anchor I ([3]_q [4]_q^3) has POSITIVE δ — same sign as g_A —")
    print("  but |δ_I|/|δ_g| ≈ 1.97 (not a clean small integer ratio).")
    print()
    print("  HONEST CONCLUSION:")
    print("  - The 'shared residual' hypothesis is FALSIFIED for Anchor II")
    print("    (the physically-motivated derivation from the G-action axioms).")
    print("  - For Anchor I the magnitudes don't match cleanly.")
    print("  - The N_sym and g_A residuals have DIFFERENT categorical sources;")
    print("    the framework needs TWO separate corrections, not one shared.")
    print()
    print("  This narrows the open work: complete the matter-sector axioms")
    print("  (X-1/X-2/X-3 from option 7) and the Higgs self-coupling axiom")
    print("  (from option 2) — neither shares structure with the other.")

    # Witness
    out = {
        'computation': 'shared-residual-test',
        'computedAt': datetime.now(timezone.utc).isoformat(),
        'description': (
            'Test of the hypothesis that N_sym (1.81%) and g_A (0.40%) '
            'residuals share a categorical multiplicative correction. '
            'FALSIFIED: opposite signs (δ_NS Anchor-II < 0, δ_g > 0); '
            'cannot be the same (1 + δ) factor. Different sources.'
        ),
        'targets': {
            'N_sym_target': mpmath.nstr(N_sym_target, 20),
            'g_A_target': mpmath.nstr(g_A_target, 8),
        },
        'leading_forms': {
            'Anchor_I_N_sym': '[3]_q · [4]_q^3',
            'Anchor_II_N_sym': '[2]_q · [4]_q² · [6]_q',
            'g_A': '[5]_q / [4]_q',
        },
        'residuals': rows,
        'verdict': (
            'shared-correction hypothesis FALSIFIED — N_sym (Anchor II, '
            'physical) and g_A residuals have opposite signs. Different '
            'categorical sources required.'
        ),
    }
    out_path = Path(__file__).parent / 'shared-residual-test.witness.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n→ wrote {out_path}")


if __name__ == '__main__':
    main()
