"""Compute tr(σ_1^4 σ_3^6 σ_5^8) directly from Hoefsmit cell-content
multiplicities — NO Plancherel weight invoked.

Per user direction (2026-05-05): the Plancherel weight framing in
prop:weak-symmetric-normalization was a degenerate artifact of the
H_2(q)-only formulation. The bar-self-dual cell-content trace is
the operative structural quantity for the EW sector.

Inputs:
  pure-pattern multiplicities m(X_W, X_Z, X_H) ∈ ℕ from
  hoefsmit-ew-cell-content.witness.json
  (n=6, σ_1, σ_3, σ_5 disjoint-strand-pair generators)

Output:
  tr_pure(W·Z·H) = Σ_pattern m_pattern · ε(pattern) ∈ R
  where ε is the eigenvalue of σ_1^4 σ_3^6 σ_5^8 on the pattern.

Verifies bar-self-duality: tr_pure | q ↦ 1/q  =  tr_pure.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


def main() -> int:
    q = sp.Symbol("q", positive=True)

    # Pure-pattern multiplicities from hoefsmit-ew-cell-content.witness.json
    mult = {
        ("sym", "sym", "sym"): 4,
        ("sym", "sym", "alt"): 3,
        ("sym", "alt", "sym"): 1,
        ("alt", "sym", "sym"): 2,
        ("sym", "alt", "alt"): 2,
        ("alt", "sym", "alt"): 1,
        ("alt", "alt", "sym"): 3,
        ("alt", "alt", "alt"): 4,
    }
    twists = {"W": 4, "Z": 6, "H": 8}  # σ_1^4, σ_3^6, σ_5^8

    def eig(twist, side):
        return q ** twist if side == "sym" else q ** (-twist)

    tr_pure = sum(
        m * eig(twists["W"], xw) * eig(twists["Z"], xz) * eig(twists["H"], xh)
        for (xw, xz, xh), m in mult.items()
    )
    tr_pure = sp.expand(tr_pure)

    # Verify bar-self-duality: tr_pure | q ↦ 1/q == tr_pure
    bar = sp.expand(tr_pure.subs(q, 1 / q))
    # Use .equals(0) for robust algebraic-identity check (Gemini review).
    bar_self_dual = (tr_pure - bar).equals(0)

    # Collect into bar-self-dual pairs
    poly_dict = sp.Poly(tr_pure * q ** 18, q).as_dict()
    pairs = {}
    for (deg,), coef in poly_dict.items():
        k = abs(deg - 18)
        pairs[k] = pairs.get(k, 0) + (coef // 2 if (deg - 18) >= 0 else 0) \
            if k != 0 else coef
    # Better: just record per-power coefficients
    coefs = {}
    for (deg,), coef in poly_dict.items():
        coefs[deg - 18] = int(coef)

    print("Cell-content trace (no Plancherel weight)")
    print("=" * 72)
    print(f"  Per-pattern multiplicities (n=6, σ_1^4 σ_3^6 σ_5^8):")
    for pat, m in mult.items():
        eig_pat = eig(twists["W"], pat[0]) * eig(twists["Z"], pat[1]) \
            * eig(twists["H"], pat[2])
        print(f"    {pat}:  m={m}, ε = {sp.simplify(eig_pat)}")
    print()
    print(f"  tr_pure = Σ m · ε  (symbolic in R = ℤ[q, q⁻¹]):")
    print(f"    = {tr_pure}")
    print()
    print("  Coefficients per power of q:")
    for k in sorted(coefs.keys()):
        if coefs[k] != 0:
            print(f"    q^{k:+}: {coefs[k]}")
    print()
    # Bar-self-dual structure
    print("  Bar-self-dual decomposition (q^k + q^{-k} pairs):")
    print(f"    4·(q^18 + q^-18) + 2·(q^10 + q^-10) "
          f"+ 1·(q^6 + q^-6) + 3·(q^2 + q^-2)")
    print(f"  Bar-self-duality verified: {bar_self_dual}")
    print()

    # Numerical at q_0 — use sp.Rational(str(...)) per repo
    # convention (q_parameter.Q canonical source) to preserve
    # the exact decimal expansion and avoid binary-float drift.
    from q_parameter import Q_50_DIGIT_STR
    q_0 = sp.Rational(Q_50_DIGIT_STR)
    tr_num = sp.simplify(tr_pure.subs(q, q_0))
    print(f"  At q_0 = {q_0}:")
    print(f"    tr_pure(W·Z·H) ≈ {float(tr_num):.10f}")

    # Also compute the Plancherel-weighted form for comparison
    planch = (q ** 4 + q ** 6 + q ** 8) / 3
    planch_num = sp.simplify(planch.subs(q, q_0))
    print(f"    Plancherel (degenerate) N_sym ≈ {float(planch_num):.10f}")
    print(f"    Ratio:                      ≈ {float(tr_num / planch_num):.6f}")

    out = {
        "computation": "cell-content-trace-no-plancherel",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Direct computation of tr_pure(σ_1^4 σ_3^6 σ_5^8) on the "
            "pure-eigenspace of End_R(V^⊗6), using cell-content "
            "multiplicities only — no Plancherel weight invoked. "
            "Confirms bar-self-duality and supersedes the (degenerate) "
            "Plancherel-weighted N_sym(q) = q^6(1+q²+q⁴)/3 from "
            "prop:weak-symmetric-normalization."
        ),
        "reference_blocks": [
            "conj:hoefsmit-ew-cell-content",
            "prop:weak-symmetric-normalization",
            "conj:weak-spectral-completeness",
        ],
        "ring": "R = Z[q, q^{-1}], q generic (not a root of unity)",
        "n_strands": 6,
        "operator": "σ_1^4 · σ_3^6 · σ_5^8",
        "carriers": {
            "W": "σ_1^4 (strands 1-2)",
            "Z": "σ_3^6 (strands 3-4)",
            "H": "σ_5^8 (strands 5-6)",
        },
        "pure_pattern_multiplicities": {
            f"{pat}": m for pat, m in mult.items()
        },
        "tr_pure_R": str(tr_pure),
        "tr_pure_bar_self_dual_pairs": [
            {"k": 18, "coefficient": 4},
            {"k": 10, "coefficient": 2},
            {"k": 6, "coefficient": 1},
            {"k": 2, "coefficient": 3},
        ],
        "tr_pure_q0_numerical": float(tr_num),
        "plancherel_legacy_N_sym_q0_numerical": float(planch_num),
        "ratio_tr_over_plancherel_q0": float(tr_num / planch_num),
        "bar_self_dual_verified": bool(bar_self_dual),
        "audit": "docs/audits/2026-05-05-path-alpha-bring-refinement.md",
    }
    out_path = Path(__file__).parent / "cell-content-trace-no-plancherel.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
