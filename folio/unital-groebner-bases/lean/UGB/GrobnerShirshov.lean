import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.CompositionLemma
import UGB.GrobnerShirshov.NormalForms
import UGB.GrobnerShirshov.NormalFormExistsRefutation
import UGB.GrobnerShirshov.QSerreCriticalPairs
import UGB.GrobnerShirshov.QSerreGS
import UGB.GrobnerShirshov.Quotient
import UGB.GrobnerShirshov.NormalFormBasisProof
import UGB.GrobnerShirshov.QSerrePBW
import UGB.GrobnerShirshov.QSerreStandard
import UGB.GrobnerShirshov.Flatness
import UGB.GrobnerShirshov.StrongMultiplicativity
import UGB.GrobnerShirshov.JetOrder
import UGB.GrobnerShirshov.SplayPBW
import UGB.GrobnerShirshov.LiePBW
import UGB.GrobnerShirshov.QuadraticPBW
import UGB.GrobnerShirshov.BlockSplayPBW

/-!
# Gröbner–Shirshov Bases — Module Root

This module re-exports the Gröbner–Shirshov formalization, which
provides the algebraic engine behind the QOU lifting mechanism.

## Module structure

| File | Contents |
|------|----------|
| `Basic` | Monomial orders, rewriting systems, S-polynomials |
| `CompositionLemma` | Diamond lemma / confluence proof |
| `NormalForms` | PBW-type bases for `U_q(sl₂)` and `Dist(G)` |
| `NormalFormExistsRefutation` | proof that the `normal_form_exists` axiom is **false** |
| `QSerreCriticalPairs` | reduces `qSerre_is_gs_basis` to its 8 genuine critical pairs |
| `QSerreGS` | resolves all 8 and proves `qSerre_is_gs_basis` (formerly an axiom) |
| `Quotient` | the quotient algebra `k⟨G⟩ / (Σ)` and `NormalFormBasis` |
| `NormalFormBasisProof` | proof that a GS basis with unit leading coefficients gives `NormalFormBasis` (commutative `k`) |
| `QSerrePBW` | PBW basis of `U_q(sl₂)`: normal words are `E_-^c E_+^a K^n`, `(c,a,n) ∈ ℕ×ℕ×ℤ`, and are a `k`-basis (`qSerre_pbw_basis`) |
| `QSerreStandard` | The q-Serre rules and the standard presentation of `U_q(sl₂)` (`KK⁻¹=1=K⁻¹K`, `KEK⁻¹=q²E`, `KFK⁻¹=q⁻²F`, `[E,F]=(K−K⁻¹)/(q−q⁻¹)`) generate the same two-sided ideal (`uq_ideal_eq`); PBW basis `F^c E^a K^n` there (`uq_pbw_basis`) |
| `Flatness` | Flat deformation from GS confluence |
| `StrongMultiplicativity` | tensor-product presentation (Bokut–Chen); see `leitner2006` Def. 1.11 for strong multiplicativity |
| `SplayPBW` | twisted splay rewriting system `ab → c·ba + π(a,b)`; its compositions are trivial iff the Jacobi condition holds; sorted words then form a basis |
| `QuadraticPBW` | quadratic rewriting systems `ab → R(a,b)`: trivial compositions iff the triple-overlap condition `a·R(b,c) − R(a,b)·c ∈ JM(abc)`; normal words then form a basis |
| `BlockSplayPBW` | Thm. 1.9 of leitner2006 for basis-presented coordinate algebras: block products + cross-block commutations; associativity, the two derivation conditions and Jacobi give the PBW basis of ordered monomials |
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
