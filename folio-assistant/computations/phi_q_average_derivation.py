#!/usr/bin/env python3
"""
⟨Φ_q⟩ closed-form attempt — the missing structural quantity blocking
categorical α derivation.

The framework's binding formula at level 3 is:
    Term6 = z³ · Σ_{triples} Φ_q(|tr_M(ξ)|)

For a categorical α derivation, we need ⟨Φ_q⟩ averaged over triple-
type sub-braid traces. This script attempts closed-form expressions
for that average.

Key empirical fact (from gs_filtration_e2_probe.py):
    At q=1 MN limit, all four triple-types (ppp, ppn, pnn, nnn) give
    IDENTICAL Markov trace |tr_M(ξ)| = 8.832e-04.

So Φ_q(8.832e-04) is the universal value — let's compute and see if
it's expressible in closed form.

Φ_q(z) = ∏_{k≥1} 1/(1 - q^(-k)·z)

For small z: Φ_q(z) ≈ 1 + z · Σ_k q^(-k) + O(z²)
                    = 1 + z · q^(-1) / (1 - q^(-1))
                    = 1 + z / (q - 1)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, z_mark, _safe_phi


def main():
    print("=" * 88)
    print("⟨Φ_q⟩ closed-form attempt")
    print("=" * 88)
    print(f"  q_0 = {float(q0):.6f}")
    print(f"  z   = {float(z_mark):.6f}")
    print()

    # The universal triple Markov trace at q=1 MN
    c = mpmath.mpf("8.8287e-04")
    print(f"  Universal triple Markov trace c = {float(c):.6e}")
    print(f"  (universal at q=1 MN — all four triple-types ppp/ppn/pnn/nnn equal)")
    print()

    # Compute Φ_q(c) directly + asymptotic approximations
    phi_q_c = _safe_phi(c)
    print(f"  Φ_q(c) (full)               = {float(phi_q_c):.10f}")

    # Asymptotic Φ_q(z) ≈ 1 + z/(q-1) for small z
    asym_1st = 1 + c / (q0 - 1)
    print(f"  Φ_q(c) (1st order: 1+c/(q-1)) = {float(asym_1st):.10f}")

    # Second-order: 1 + z/(q-1) + z²/(2(q-1)(q²-1)) ?
    # Φ_q(z) = ∏ 1/(1-q^{-k}z); log = Σ Σ z^j q^{-jk}/j = -Σ Σ ...
    # Actually: log Φ_q(z) = Σ_j z^j/j · Σ_k q^{-jk} = Σ_j z^j/j · q^{-j}/(1-q^{-j})
    # For j=1: z · q^{-1}/(1-q^{-1}) = z/(q-1)
    # For j=2: z²/2 · q^{-2}/(1-q^{-2}) = z²/(2(q²-1))
    log_2 = c / (q0 - 1) + c ** 2 / (2 * (q0 ** 2 - 1))
    asym_2nd = mpmath.exp(log_2)
    print(f"  Φ_q(c) (2nd-order log expansion) = {float(asym_2nd):.10f}")
    print()

    # Term6 / A³ asymptotic
    term6_over_A3_asym = float(z_mark) ** 3 / 6 * float(phi_q_c)
    print(f"  Term6/A³ asymptotic = z³/6 · Φ_q(c) = {term6_over_A3_asym:.6e}")
    print()

    # The categorical α prediction: B/A_∞ = α · Term6/A³_∞ + β + δ_M
    # We want α from framework only — but B/A_∞ is empirical (8.5 MeV).
    # Without a categorical B/A_∞, we can only derive α modulo a B/A_∞ input.
    print("  ── Reverse-derive α IF B/A_∞ is categorically known ──")
    BETA_FIT = 1.14
    for B_sat_label, B_sat in [
        ("8.50 MeV (SEMF saturation, empirical)", 8.50),
        ("[E_0 + m_e · ?] (categorical proxy)", None),
    ]:
        if B_sat is None:
            print(f"    {B_sat_label}: CATEGORICAL B/A_∞ NOT YET DERIVED")
            continue
        alpha_pred = (B_sat - BETA_FIT) / term6_over_A3_asym
        print(f"    With B/A_∞ = {B_sat_label}:  α = (B_sat - β) / (Term6/A³_∞) = {alpha_pred:.4f} MeV")

    print()
    print("  ── Where is the gap? ──")
    print()
    print("  The closed-form prediction for α reduces to:")
    print("    α = (B/A_∞ - β) · 6 / (z³ · Φ_q(c))")
    print()
    print("  Inputs needed:")
    print("    1. B/A_∞ — nuclear saturation binding-energy density")
    print("       Empirically ~8.5 MeV.  CATEGORICALLY: not yet derived")
    print("       from the framework's structures.")
    print("    2. β — calibration intercept")
    print("       Empirically ~1.14 MeV.  Same categorical gap.")
    print("    3. c — universal triple-type Markov trace at q=1 MN")
    print("       Empirically ~8.83e-04.  Categorical closed form")
    print("       requires explicit Schur-Weyl decomposition of the")
    print("       9-strand atom braid permutation cycle type — TBD.")
    print()
    print("  All three (B/A_∞, β, c) are framework-side gaps.")
    print("  Until at least two are derived, α stays empirical.")
    print()
    print("  Concrete next step: derive c from")
    print("      c = Σ_{λ ⊢ 9, len ≤ 2} w_λ(q_0) · χ^λ_MN(σ_atom_triple)")
    print("  where σ_atom_triple is the cycle type of the 9-strand atom")
    print("  braid for any all-same-type triple (which is the same for")
    print("  ppp/ppn/pnn/nnn at q=1 MN).")

    out = {
        "computation": "phi-q-average-derivation-attempt",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q_0": float(q0),
        "z": float(z_mark),
        "c_universal_triple_trace": float(c),
        "phi_q_c_full": float(phi_q_c),
        "phi_q_c_1st_order": float(asym_1st),
        "phi_q_c_2nd_order": float(asym_2nd),
        "term6_over_A3_asymptotic": term6_over_A3_asym,
        "alpha_prediction_modulo_B_sat": (
            "α = (B/A_∞ - β) / (z³/6 · Φ_q(c))"
        ),
        "framework_gaps": [
            "B/A_∞ saturation density (empirically ~8.5 MeV)",
            "β intercept (empirically ~1.14 MeV)",
            "c universal triple-type Markov trace at q=1 MN",
        ],
        "interpretation": (
            "Reduces the α derivation to three framework-side "
            "quantities, all currently empirical. Closes the "
            "structural reduction (α IS analytically expressible "
            "in terms of c, B/A_∞, β); the quantitative derivation "
            "awaits framework derivations of these three inputs."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-phi-q-average-attempt.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
