import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.CompositionLemma
import UGB.GrobnerShirshov.NormalForms
import UGB.GrobnerShirshov.NormalFormExistsRefutation
import UGB.GrobnerShirshov.QSerreCriticalPairs
import UGB.GrobnerShirshov.QSerreGS
import UGB.GrobnerShirshov.Quotient
import UGB.GrobnerShirshov.NormalFormBasisProof
import UGB.GrobnerShirshov.Flatness
import UGB.GrobnerShirshov.StrongMultiplicativity
import UGB.GrobnerShirshov.JetOrder
import UGB.GrobnerShirshov.SplayPBW
import UGB.GrobnerShirshov.LiePBW

/-!
# Gröbner–Shirshov Bases — Module Root

This module re-exports the Gröbner–Shirshov formalization, which
provides the algebraic engine behind the QOU lifting mechanism.

## Module structure

| File | Contents |
|------|----------|
| `Basic` | Monomial orders, rewriting systems, S-polynomials |
| `CompositionLemma` | Diamond lemma / confluence proof |
| `NormalForms` | PBW-type bases for `U_q(su(2))` and `Dist(G)` |
| `NormalFormExistsRefutation` | proof that the `normal_form_exists` axiom is **false** |
| `QSerreCriticalPairs` | reduces `qSerre_is_gs_basis` to its 8 genuine critical pairs |
| `QSerreGS` | resolves all 8 and proves `qSerre_is_gs_basis` (formerly an axiom) |
| `Quotient` | the quotient algebra `k⟨G⟩ / (Σ)` and `NormalFormBasis` |
| `NormalFormBasisProof` | proof that a GS basis with unit leading coefficients gives `NormalFormBasis` (commutative `k`) |
| `Flatness` | Flat deformation from GS confluence |
| `StrongMultiplicativity` | tensor-product presentation (Bokut–Chen); see `leitner2006` Def. 1.11 for strong multiplicativity |
| `SplayPBW` | twisted splay rewriting system `ab → c·ba + π(a,b)`; its compositions are trivial iff the Jacobi condition holds; sorted words then form a basis |
| `LiePBW` | PBW for a Lie algebra with a finite basis: the Jacobi condition from Mathlib's `lie_jacobi`, under a rank deg-lex order |
| `JetOrder` | Jet-stratified reduction: ordering extension + complexity |

## How the pieces fit together

```
Basic.lean
  ├─ AlgOps.lean              (algebra operations: add, smul, leftMulGen)
  ├─ CompositionLemma.lean    (diamond lemma: GS ⟹ confluence)
  │    └─ NormalForms.lean     (PBW bases for U_q and Dist(G))
  │         └─ Flatness.lean   (Dist(G) is flat over Dist(H))
  │              └─ StrongMultiplicativity.lean  (tensor-product presentation)
  └─ JetOrder.lean            (jet-stratified reduction algorithm)
       ├─ imports: Basic, AlgOps, CompositionLemma, Flatness
       └─ uses: filtration + Hilbert function from Flatness
```

The composition lemma does triple duty:
1. **Normal forms** — unique representatives in the quotient algebra
2. **Flatness** — the deformation preserves Hilbert series
3. **Strong multiplicativity** — comultiplication is an algebra map

## References

- [fred2005] L. Fred, PhD thesis, University of Arizona, 2005.
- Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978).
- Bokut & Chen, *Gröbner–Shirshov bases*, Bull. Math. Sci. 4 (2014).
-/
