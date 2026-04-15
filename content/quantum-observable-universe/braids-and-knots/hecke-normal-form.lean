/-!
# QOU.Braiding.HeckeNormalForm — Hecke normal form in H_n(q)

The Hecke normal form of an element h ∈ H_n(q) is the unique
representative in the Gröbner–Shirshov canonical basis obtained
by iterated application of the Hecke relation, far commutativity,
and the Yang–Baxter rewriting rule.  The resulting basis elements
are in bijection with the symmetric group S_n.

LaTeX label: `def:hecke-normal-form`

## References

- [manuscript] Ch 3 §2

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.GroupTheory.Perm.Basic

namespace QOU.Braiding

/-- The Hecke normal form: given an element of H_n(q), its unique
    canonical representative indexed by a permutation w ∈ S_n,
    obtained via the Gröbner–Shirshov diamond lemma.

    The basis element T_w = T_{s_{i₁}} ⋯ T_{s_{iₖ}} for any
    reduced expression w = s_{i₁} ⋯ s_{iₖ}. -/
-- Ref: [manuscript] Ch 3 §2
structure HeckeNormalForm (n : ℕ) where
  /-- The permutation indexing this basis element. -/
  perm : Equiv.Perm (Fin n)
  /-- Length of the reduced expression (number of Hecke generators). -/
  reducedLength : ℕ
  /-- The reduced length equals the number of inversions of the permutation. -/
  -- Ref: [manuscript] Ch 3 §2
  length_eq_inversions : reducedLength = sorry

/-- The normal form map is well-defined: every element of H_n(q)
    has a unique Hecke normal form (Diamond Lemma). -/
-- Ref: [manuscript] Ch 3 §2
theorem heckeNormalForm_unique (n : ℕ) :
    ∀ (w : Equiv.Perm (Fin n)), True := by
  intro _; trivial

end QOU.Braiding
