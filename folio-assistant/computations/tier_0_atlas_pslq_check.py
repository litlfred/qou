"""tier_0_atlas_pslq_check.py

Tier-0 falsifiability check for `BringHyperbolicDecomposition`:
does 2/(3π) lie in the Z-linear lattice spanned by the four atlas
hyperbolic-knot Bloch-Wigner values

  v₁ = 2 · Cl_2(π/3)        ≈ 2.029883   (figure-8 4_1)
  v₂ = 8 · G  = 8·Cl_2(π/2) ≈ 7.327724   (Borromean B_3)
  v₃ = Vol(6_2)             ≈ 4.401 ... (deuteron 6_2)
  v₄ = Vol(8_11)            ≈ 8.286 ... (tritium 8_11)

at 2/(3π) ≈ 0.2122065907891938.

Note: L_6a4 is omitted from the basis because Vol(L_6a4) = 8G = v₂
(established identity from binding-scale-catalan); including it
would introduce a Q-linear dependency.

The script uses mpmath PSLQ to search for an integer relation
  c₀ · (2/(3π)) + n₁ · v₁ + n₂ · v₂ + n₃ · v₃ + n₄ · v₄ = 0
with small coefficients. A non-trivial small relation would
inhabit `BringHyperbolicDecomposition` directly from the atlas.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# Ref: [manuscript] conj:bring-hyperbolic-knot-bloch-decomposition
# Ref: [manuscript] rem:figure-8-archimedean-illustration
# Ref: [manuscript] binding-scale-catalan
# Ref: [manuscript] recursive-atom-knot-atlas

import json
from witness_base import WitnessBuilder  # noqa: E402
from pathlib import Path

import mpmath
from mpmath import mp, mpf, pslq, pi as mp_pi


def main() -> None:
    mp.dps = 100  # 100-decimal-digit precision

    # Bloch-Wigner / hyperbolic-volume targets
    target = 2 / (3 * mp_pi)

    # Atlas BW basis values (numerical, 100 dps).
    # Cl_2(θ) = Σ_{k≥1} sin(kθ)/k² = mpmath.clsin(2, θ)
    # Note: mpmath.clcos(s, z) is Σ cos(kz)/k^s — different function.
    cl2_pi_third = mpmath.clsin(2, mp_pi / 3)
    cl2_pi_half = mpmath.catalan  # G = Cl_2(π/2) ≈ 0.91596
    v1 = 2 * cl2_pi_third
    v2 = 8 * cl2_pi_half
    # Hyperbolic volumes for 6_2 and 8_11 (high-precision known constants)
    # Sourced from SnapPy at high precision; values cited in
    # recursive-atom-knot-atlas.md.
    v3 = mpf("4.4008354924779311327842466420115226538195841018537"
             "9398892918725716731795829093796158929739181849")
    v4 = mpf("8.2862710479413574611146286395076196815770488043144"
             "6814620876549935732839832762283907316876")

    basis = [target, v1, v2, v3, v4]
    labels = ["2/(3π)", "2·Cl_2(π/3)", "8G", "Vol(6_2)", "Vol(8_11)"]

    relation = pslq(basis, tol=mpf("1e-80"), maxcoeff=10**8)

    result = {
        "computation": "tier-0-atlas-pslq-check",
        "description": (
            "Tier-0 falsifiability check for "
            "BringHyperbolicDecomposition: PSLQ over atlas BW "
            "values vs 2/(3π) at 100 dps."
        ),
        "contentBlock": "conj:bring-hyperbolic-knot-bloch-decomposition",
        "precision_dps": 100,
        "tolerance": "1e-80",
        "basis_labels": labels,
        "basis_values_50dp": [str(b)[:55] for b in basis],
        "target": str(target),
        "relation_found": relation is not None,
        "relation": [int(x) for x in relation] if relation else None,
        "interpretation": (
            "non-trivial small relation found — atlas suffices"
            if relation
            else (
                "NO non-trivial small relation found at 100 dps with "
                "max coeff 10^8 — atlas hyperbolic objects {4_1, B_3, "
                "6_2, 8_11} (modulo L_6a4 = B_3 via 8G identity) DO "
                "NOT span 2/(3π). Higher-tier search needed."
            )
        ),
    }

    out_path = (
        WitnessBuilder.wrap_legacy("tier-0-atlas-pslq-check", result,
                     script_path=__file__, engine="mpmath")
        .set_audit_only(
            "docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .save()
    )

    print(f"Result: {result['interpretation']}")
    if relation:
        print(f"Relation: {relation}")
        for label, coeff in zip(labels, relation):
            print(f"  {coeff:+d} * {label}")


if __name__ == "__main__":
    main()
