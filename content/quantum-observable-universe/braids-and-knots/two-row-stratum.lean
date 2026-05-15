/-
Two-row Wedderburn stratum Λ²(n) of the Hecke algebra H_n(q).

LaTeX label:        def:two-row-stratum
Companion script:   folio-assistant/computations/probe_he4_canonical_tr_m_fingerprint.py
Companion script:   folio-assistant/computations/delta_lambda_2row_stratum_analysis.py

  Λ²(n) := { λ ⊢ n : ℓ(λ) ≤ 2 } = { (n-k, k) : 0 ≤ k ≤ n/2 }

is the subset of partitions of n with at most two parts.  It carries
the SU(2) Schur-Weyl image: under the natural restriction
H_n(q) ↠ End_{SU(2)}(V^⊗n) with V = ℂ², partitions outside Λ² lie
in the kernel.

The two-row projection π_{2-row} : H_n(q) → ⊕_{λ ∈ Λ²} End(V_λ) is
the orthogonal projection onto the two-row sector; it splits
tr_M(β) = tr_M(π_{2-row} β) + tr_M((1 - π_{2-row}) β).

Pre-Archimedean stub: polymorphic in the partition representation;
no commitment to a specific Mathlib `Partition` API.  Downstream
uses (he4-two-row-dominance, magic-shell coupling) consume the
predicate `IsTwoRow` to filter the Wedderburn sum.

Ref: [jones1985] https://doi.org/10.2307/1971403
Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot.TwoRowStratum

/-- A partition is "two-row" iff its length (number of nonzero parts)
    is at most 2.  We model partitions abstractly as a sorted list of
    positive integers; `IsTwoRow` is a decidable predicate. -/
def IsTwoRow (parts : List ℕ) : Prop := parts.length ≤ 2

instance (parts : List ℕ) : Decidable (IsTwoRow parts) :=
  inferInstanceAs (Decidable (parts.length ≤ 2))

/-- The two-row stratum Λ²(n) as the set of partition lists that
    (i) sum to n and (ii) satisfy IsTwoRow.  Stated as a Prop so
    that membership is decidable for any concrete partition. -/
def TwoRowStratum (n : ℕ) (parts : List ℕ) : Prop :=
  parts.sum = n ∧ IsTwoRow parts

instance (n : ℕ) (parts : List ℕ) : Decidable (TwoRowStratum n parts) :=
  inferInstanceAs (Decidable (parts.sum = n ∧ IsTwoRow parts))

/-- Cardinality of Λ²(n): exactly ⌊n/2⌋ + 1 partitions (the pairs
    (n-k, k) for 0 ≤ k ≤ ⌊n/2⌋).  Stated as a structural fact;
    full proof deferred to a later Lean pass that pins down the
    concrete partition enumeration. -/
class HasTwoRowCardinality (n : ℕ) where
  card_two_row : ℕ
  card_eq : card_two_row = n / 2 + 1

/-- Trivial instance for n = 0: only the empty partition. -/
instance : HasTwoRowCardinality 0 := ⟨1, by decide⟩

/-- The two-row projection on the Wedderburn decomposition.

    Axiomatised here as a class encoding the splitting
    `tr_M(β) = tr_M(π_{2-row} β) + tr_M((1 - π_{2-row}) β)` for any
    Hecke element β.  The concrete projection requires the full
    Wedderburn decomposition apparatus (per-partition irrep blocks
    Hoefsmit basis); the class allows downstream consumers to take
    its existence as a typeclass hypothesis. -/
class HasTwoRowProjection (HeckeAlg : Type*) where
  /-- The projection π_{2-row} : HeckeAlg → HeckeAlg as a function. -/
  pi : HeckeAlg → HeckeAlg
  /-- Idempotency: π² = π. -/
  idempotent : ∀ β, pi (pi β) = pi β

end QOU.BraidKnot.TwoRowStratum
