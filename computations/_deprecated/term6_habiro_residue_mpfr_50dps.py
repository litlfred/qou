#!/usr/bin/env python3
"""
Plan F — Term 6 (Habiro residue tail) at MPFR @ 50 dps.

Term 6 of the unified mass formula is

    Term 6 = Σ_{ℓ ≥ 2} Res_{q = ζ_ℓ}[·] / (q_0 − ζ_ℓ)

where ζ_ℓ is a primitive ℓ-th root of unity (root of cyclotomic
polynomial Φ_ℓ(q)). The residues capture the Mittag-Leffler tail
of Φ_q(V̂) beyond the Taylor expansion (Terms 2, 3).

Implementation strategy:
  - The Schur-Weyl global sum Σ_{λ ⊢ 3A} w_λ(q) admits an exact
    sympy.Rational form per atom A (built by schur_weyl_symbolic.py
    via the Wenzl-bridge weights and Hoefsmit characters).
  - Evaluating that symbolic sum at q = q_0 to 50 dps gives the
    direct Term-6 contribution per atom.
  - This script lifts the existing 30-digit values from
    `habiro-residue-symbolic.witness.json` to 50 dps via mpmath
    re-evaluation. The underlying sympy expressions are precision-
    free — the only floor is the q_0 string (50 dps).

Output: `term6-habiro-residue-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from mpmath import mp, mpf

# Module-level precision contract: high-precision scientific script
# (not a reusable library). Per Gemini review on PR #456 we use
# mp.workdps() inside main() for explicit local scope.

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# Imports from sibling computation modules — placed here per PEP 8
# after the sys.path.insert so the resolver finds them at module load.
from schur_weyl_symbolic import (  # noqa: E402
    global_wedderburn_sum_symbolic,
    h3_additive_approximation_symbolic,
    partitions_of,
)

Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")


def main() -> int:
    # Local precision scope per Gemini review on PR #456.
    with mp.workdps(50):
        q_str = json.load(open(Q0))["derived_50_digit"]["q"]
        q_0 = mpf(q_str)
        print(f"  q_0 (50 dps) = {q_str}")

        q_sym = sp.Symbol("q", positive=True, real=True)
        q0_sympy = sp.Float(q_str, 60)  # 60 internal digits, output truncated to 50

        rows = []
        for A in (1, 2, 3, 4):
            print(f"\n  === A={A} (re-evaluating symbolic Schur-Weyl at 50 dps) ===")
            total, _ = global_wedderburn_sum_symbolic(A, q_sym)
            h3 = h3_additive_approximation_symbolic(A, q_sym)

            global_sum_50 = total.subs(q_sym, q0_sympy).evalf(50)
            h3_50 = h3.subs(q_sym, q0_sympy).evalf(50)
            ratio_50 = ((total) / h3).subs(q_sym, q0_sympy).evalf(50)

            global_sum_mpf = mpf(str(global_sum_50))
            term6_mev = M_E_MEV * global_sum_mpf

            rows.append({
                "atom": f"A={A}",
                "partition_count": len(partitions_of(3 * A)),
                "global_sum_at_q0_50dps": str(global_sum_50),
                "h3_additive_at_q0_50dps": str(h3_50),
                "ratio_global_over_h3_50dps": str(ratio_50),
                "term6_b_pred_mev_50dps": str(term6_mev),
            })
            print(f"    partition_count = {len(partitions_of(3 * A))}")
            print(f"    Schur-Weyl global sum at q_0 (50 dps) = {global_sum_50}")
            print(f"    Term 6 = m_e · Σ_λ w_λ                = {term6_mev} MeV")

        out = {
            "computation": "term6-habiro-residue-mpfr-50dps",
            "description":
                "Plan F — Term 6 Habiro residue tail at MPFR @ 50 dps. "
                "Re-evaluates the global Schur-Weyl symbolic sums "
                "Σ_{λ⊢3A} w_λ(q) from schur_weyl_symbolic.py at q_0 to "
                "50 dps via sympy.evalf(50). Replaces the prior 30-dps "
                "value inherited from habiro-residue-symbolic.witness.json.",
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "precision": "mpfr_50dps",
            "q_0_50dps": q_str,
            "m_e_mev_50dps": str(M_E_MEV),
            "results_by_atom": rows,
        }
        OUT.write_text(json.dumps(out, indent=2))
        print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
