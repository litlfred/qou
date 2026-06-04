"""Discover + verify structural product identities c_3·c_4 = c_8 and c_3·c_6 = c_9.

Per user prompt 2026-06-04 (option 3: "derive c_4 separately"). The
honest negative for constant-kernel recursion (see
`qbeta_constant_kernel_depth_test.py`) left the c_4 categorical origin
open. This probe hunts for PRODUCT identities c_i · c_j = c_k between
the documented + this-session-derived closed forms.

## Discovery

Symbolic search over (i, j, k) ∈ {3..10}³ on the closed forms

  c_2 = -1
  c_3 = -2                  (J_Hopf at q=1)
  c_4 = -2·b⁴
  c_5 = -(b² + 1/2)
  c_6 = 4·b²
  c_7 = -8
  c_8 = 4·b⁴
  c_9 = -8·b²
  c_10 = 4·b⁶

finds exactly **two** product identities:

  c_3 · c_4 = c_8   [symbolic in b, EXACT for all b]
  c_3 · c_6 = c_9   [symbolic in b, EXACT for all b]

## What this gives for the c_4 derivation question

The first identity REARRANGES to derive c_4 from c_3 and c_8:

  c_4 = c_8 / c_3 = (4·b⁴) / (-2) = -2·b⁴

So **IF** `c_8 = c_3 · c_4` is a structural categorical identity (a
Markov-trace product law in some categorical tower), THEN c_4 = -2·b⁴
is forced — derived, not stipulated.

The categorical interpretation candidate: c_k labels an object in a
graded categorical tower where c_3 = J_Hopf (degree 1) acts as a
"multiply by Hopf-link trace" operator. The product c_3 · c_4 = c_8
then reads as "applying one more Hopf-trace twist to the c_4 object
gives the c_8 object."

This is exactly the "k-dependent kernel" route mentioned in PR #1786 +
CKRecursion on main — but realised here as a MULTIPLICATIVE relation,
not an additive (linear-recursion) one.

## Silver-ratio verification (b² = 7/8 exact)

  c_3 · c_4  at silver = (-2) · (-49/32) = 49/16 = c_8 silver  ✓
  c_3 · c_6  at silver = (-2) · (7/2)    = -7    = c_9 silver  ✓

Both identities hold as pure ℚ-rational equalities at silver — Lean-
formalisable via `norm_num`. Companion proof file:
content/quantum-observable-universe/mass-theory/qbeta-c4-structural-products.{ts,md,lean}

## Honest caveats

- The product identity `c_8 = c_3·c_4` is observed symbolically;
  whether it follows from a categorical theorem (e.g. via Markov-trace
  composition or a Hopf-link tensoring axiom) is NOT yet derived.
- The identity `c_3 · c_5 = ?` does NOT match any documented c_k —
  c_5 (averaging-resonance outlier) is outside the product algebra.
- Searching all (i,j) products gives ONLY these two hits; this is a
  sparse identity, NOT a full multiplicative closure.

So the discovery is genuine but limited — it derives ONE structural
value (c_4 from c_3 and c_8) via ONE identity, leaving c_5 (and the
question of why c_8 has this specific value at q₀) still open.

EXPLORATORY. No production wiring. No fit.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
COMPUTATIONS_ROOT = HERE.parent
if str(COMPUTATIONS_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPUTATIONS_ROOT))
import _path_bridge  # noqa: F401, E402


def main() -> int:
    mp.mp.dps = 60
    b = sp.symbols('b', positive=True)
    c_sym = {
        2:  sp.Integer(-1),
        3:  sp.Integer(-2),
        4:  sp.Integer(-2) * b**4,
        5:  -(b**2 + sp.Rational(1, 2)),
        6:  sp.Integer(4) * b**2,
        7:  sp.Integer(-8),
        8:  sp.Integer(4) * b**4,
        9:  sp.Integer(-8) * b**2,
        10: sp.Integer(4) * b**6,
    }

    print("=" * 78)
    print(" Structural product identities c_i · c_j = c_k (symbolic search)")
    print("=" * 78)
    print()

    hits = []
    for i in range(3, 11):
        for j in range(i, 11):
            prod = sp.expand(c_sym[i] * c_sym[j])
            for k in range(2, 11):
                if sp.expand(prod - c_sym[k]) == 0:
                    hits.append((i, j, k, str(prod)))

    print(f"  Found {len(hits)} structural product identities:")
    for i, j, k, prod_str in hits:
        print(f"    c_{i} · c_{j} = c_{k}    [= {prod_str}]")
    print()

    # Derive c_4 from c_3 and c_8 (if the identity holds)
    print("  ── DERIVATION ROUTE: c_4 from c_3 and c_8 ──")
    print()
    derived_c4 = sp.simplify(c_sym[8] / c_sym[3])
    derived_match = (sp.expand(derived_c4 - c_sym[4]) == 0)
    print(f"    c_4 = c_8 / c_3 = ({c_sym[8]}) / ({c_sym[3]}) = {derived_c4}")
    print(f"    documented c_4 = {c_sym[4]}")
    print(f"    match? {derived_match}")
    print()

    # Silver-ratio verification (b² = 7/8 exact)
    print("  ── Silver-ratio verification (b² = 7/8 exact, ℚ-rationals) ──")
    print()
    b2_silv = Fraction(7, 8)
    silv = {
        3: Fraction(-2),
        4: Fraction(-2) * b2_silv ** 2,
        6: Fraction(4) * b2_silv,
        8: Fraction(4) * b2_silv ** 2,
        9: Fraction(-8) * b2_silv,
    }
    silv_matches = {}
    for (i, j, k) in [(3, 4, 8), (3, 6, 9)]:
        lhs = silv[i] * silv[j]
        rhs = silv[k]
        match = (lhs == rhs)
        silv_matches[f"c_{i}·c_{j}_eq_c_{k}"] = bool(match)
        flag = "✓" if match else "✗"
        print(f"    c_{i} · c_{j} = {silv[i]} · {silv[j]} = {lhs}   "
              f"  c_{k} = {rhs}   {flag}")
    print()

    print("  ── VERDICT ──")
    print("    Two product identities discovered. c_8 = c_3 · c_4 gives")
    print("    a closed-form DERIVATION of c_4 from c_3 (J_Hopf) and c_8")
    print("    (the σ-action tower seed) — modulo the categorical proof")
    print("    of the product identity itself.")

    out = {
        "computation": "qbeta-c4-structural-product-identities",
        "description": (
            "Discovers and verifies the two structural product identities "
            "c_3·c_4 = c_8 and c_3·c_6 = c_9 (symbolic in b, exact at silver "
            "ratio). The first identity derives c_4 = c_8/c_3 = -2·b⁴, "
            "answering the 'c_4 categorical origin' question with a "
            "Markov-trace-style multiplicative law (modulo categorical proof "
            "of the product identity itself). EXPLORATORY; no fit."),
        "closed_forms_used": {f"c_{k}": str(v) for k, v in c_sym.items()},
        "product_identities_found": [
            {"i": i, "j": j, "k": k, "product_value": prod}
            for i, j, k, prod in hits
        ],
        "n_product_identities": len(hits),
        "c4_derivation": {
            "formula": "c_4 = c_8 / c_3",
            "derived_form": str(derived_c4),
            "documented_form": str(c_sym[4]),
            "match": bool(derived_match),
        },
        "silver_ratio_matches": silv_matches,
        "all_silver_match": all(silv_matches.values()),
        "verdict": (
            "Two product identities found. c_8 = c_3·c_4 derives c_4 = "
            "-2·b⁴ from c_3 (J_Hopf) and c_8 (σ-action seed) — closing "
            "the c_4 categorical-origin question modulo proof of the "
            "underlying multiplicative law. c_5 (averaging-resonance) "
            "remains outside the product algebra."),
    }
    out_path = COMPUTATIONS_ROOT / "qbeta-c4-structural-product-identities.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\n  Witness: {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
