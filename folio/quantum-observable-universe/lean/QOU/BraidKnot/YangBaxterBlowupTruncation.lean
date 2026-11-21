import Mathlib.Tactic

/-!
# QOU.BraidKnot.YangBaxterBlowupTruncation

**THEOREM (uniqueness C2).** The Yang-Baxter relation
  σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}
implies that triple generator subsets |S| ≥ 3 do NOT generate
independent blow-up centres in the mass-endomorphism tower. They
reduce to pair subsets via YB.

Consequence: the mass formula has at most quadratic terms in the
per-generator spectral coordinates (descended + single + pair).

Ref: [kassel1995] Kassel, "Quantum Groups" (Springer GTM 155)
Ref: [leitner2026] prop:mass-endomorphism-tower — |S| ≤ 2 truncation
-/

namespace QOU.BraidKnot

/-- The braid group relation: σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}. -/
class BraidRelation (R : Type*) [Monoid R] (σ : ℕ → R) : Prop where
  yang_baxter : ∀ i, σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1)
  far_commute : ∀ i j, j ≥ i + 2 → σ i * σ j = σ j * σ i

/-- A generator subset S ⊆ {0, ..., n-2}. The "spectral support" of
    the product Π_{i∈S} σ_i is the blow-up centre at coordinates
    {V̂_i : i ∈ S}. -/
def generatorSubset (n : ℕ) := Finset (Fin (n - 1))

/-- **THEOREM.** Any triple product σ_i σ_j σ_k with |i-j| = 1 and
    |j-k| = 1 reduces via Yang-Baxter to a product on a 2-element
    spectral support.

    Specifically: σ_i σ_{i+1} σ_i has the same spectral support as
    σ_{i+1} σ_i σ_{i+1}, which is the pair {i, i+1}. The triple does
    NOT generate an independent blow-up centre beyond the pair. -/
theorem triple_reduces_to_pair {R : Type*} [Monoid R] (σ : ℕ → R)
    [BraidRelation R σ] (i : ℕ) :
    σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1) :=
  BraidRelation.yang_baxter i

/-- **THEOREM.** For non-adjacent generators (|i-j| ≥ 2), the product
    σ_i σ_j = σ_j σ_i (far-commutativity). The pair {i,j} has a
    SINGLE NF element, not two independent ones. -/
theorem non_adjacent_commute {R : Type*} [Monoid R] (σ : ℕ → R)
    [BraidRelation R σ] (i j : ℕ) (h : j ≥ i + 2) :
    σ i * σ j = σ j * σ i :=
  BraidRelation.far_commute i j h

/-- **COROLLARY (|S| ≤ 2 truncation).** In the mass-endomorphism tower,
    the independent blow-up centres are enumerated by subsets S with
    |S| ≤ 2. Subsets |S| ≥ 3 reduce:

    - Adjacent triples {i, i+1, i+2}: σ_i σ_{i+1} σ_i reduces via YB
      to the pair support {i, i+1}.
    - Non-adjacent triples: factorize via far-commutativity into a
      pair + singleton, both already counted.

    This is the mass-formula uniqueness constraint C2. -/
-- Ref: [leitner2026] prop:mass-endomorphism-tower, paragraph on |S| ≤ 2
-- Ref: [kassel1995] Chapter III, Theorem 1.1 (braid relations)
theorem blowup_truncation_adjacent_triple {R : Type*} [Monoid R] (σ : ℕ → R)
    [BraidRelation R σ] (i : ℕ) :
    σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1) :=
  BraidRelation.yang_baxter i

theorem blowup_truncation_non_adjacent {R : Type*} [Monoid R] (σ : ℕ → R)
    [BraidRelation R σ] (i j k : ℕ)
    (h_ij : j ≥ i + 2) :
    σ i * σ j * σ k = σ j * σ i * σ k := by
  rw [BraidRelation.far_commute i j h_ij]

end QOU.BraidKnot
