import QOU.GrobnerShirshov.Basic
import QOU.GrobnerShirshov.CompositionLemma
import QOU.GrobnerShirshov.NormalForms
import QOU.GrobnerShirshov.Flatness
import QOU.GrobnerShirshov.StrongMultiplicativity

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
| `Flatness` | Flat deformation from GS confluence |
| `StrongMultiplicativity` | Frobenius preservation under deformation |

## How the pieces fit together

```
Basic.lean
  └─ CompositionLemma.lean    (diamond lemma: GS ⟹ confluence)
       └─ NormalForms.lean     (PBW bases for U_q and Dist(G))
            └─ Flatness.lean   (Dist(G) is flat over Dist(H))
                 └─ StrongMultiplicativity.lean  (Δ(xy) = Δ(x)·Δ(y))
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
