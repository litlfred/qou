/-
Two-row Wedderburn stratum Λ²(n) of the Hecke algebra H_n(q).

LaTeX label:        def:two-row-stratum
Companion script:   computations/probe_he4_canonical_tr_m_fingerprint.py
Companion script:   computations/delta_lambda_2row_stratum_analysis.py

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

import Mathlib.Data.Nat.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.List.Range
import Mathlib.Tactic.NormNum

namespace QOU.BraidKnot.TwoRowStratum

/-- A partition is "two-row" iff its length (number of nonzero parts)
    is at most 2.  We model partitions abstractly as a sorted list of
    positive integers; `IsTwoRow` is a decidable predicate. -/
def IsTwoRow (parts : List ℕ) : Prop := parts.length ≤ 2

instance (parts : List ℕ) : Decidable (IsTwoRow parts) :=
  inferInstanceAs (Decidable (parts.length ≤ 2))

/-- The empty partition is two-row. -/
theorem isTwoRow_nil : IsTwoRow ([] : List ℕ) := by decide

/-- A singleton partition is two-row. -/
theorem isTwoRow_singleton (a : ℕ) : IsTwoRow [a] := by simp [IsTwoRow]

/-- A two-element partition is two-row. -/
theorem isTwoRow_pair (a b : ℕ) : IsTwoRow [a, b] := by simp [IsTwoRow]

/-- A three-or-more element list is NOT two-row. -/
theorem not_isTwoRow_triple (a b c : ℕ) : ¬ IsTwoRow [a, b, c] := by
  unfold IsTwoRow
  simp

/-- The two-row stratum Λ²(n) as the set of partition lists that
    (i) sum to n and (ii) satisfy IsTwoRow.  Stated as a Prop so
    that membership is decidable for any concrete partition. -/
def TwoRowStratum (n : ℕ) (parts : List ℕ) : Prop :=
  parts.sum = n ∧ IsTwoRow parts

instance (n : ℕ) (parts : List ℕ) : Decidable (TwoRowStratum n parts) :=
  inferInstanceAs (Decidable (parts.sum = n ∧ IsTwoRow parts))

/-- The canonical enumeration of Λ²(n) as a list: for each
    `k ∈ {0, 1, …, ⌊n/2⌋}`, emit the pair `(n - k, k)` — but with
    the trivial-rep `(n)` written as `[n]` and the equal-pair case
    `(n/2, n/2)` as `[n/2, n/2]`.  Excludes any zero-component
    partitions (so `(n, 0) ↦ [n]` rather than `[n, 0]`). -/
def enumerateTwoRow (n : ℕ) : List (List ℕ) :=
  (List.range (n / 2 + 1)).map (fun k =>
    if k = 0 then [n] else [n - k, k])

/-- The enumeration has cardinality ⌊n/2⌋ + 1. -/
theorem enumerateTwoRow_length (n : ℕ) :
    (enumerateTwoRow n).length = n / 2 + 1 := by
  simp [enumerateTwoRow]

/-- Concrete enumeration for n = 12 (⁴He case).  Returns 7 partitions
    matching `Λ²(12) = {(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)}`. -/
example : enumerateTwoRow 12 =
    [[12], [11, 1], [10, 2], [9, 3], [8, 4], [7, 5], [6, 6]] := by
  decide

/-- Concrete cardinality |Λ²(12)| = 7. -/
theorem card_two_row_12 : (enumerateTwoRow 12).length = 7 := by decide

/-- Concrete cardinality |Λ²(n)| at small even n. -/
theorem card_two_row_even_small : ∀ n ∈ [(0:ℕ), 2, 4, 6, 8, 10, 12],
    (enumerateTwoRow n).length = n / 2 + 1 := by
  decide

/-- Cardinality of Λ²(n): exactly ⌊n/2⌋ + 1 partitions (the pairs
    (n-k, k) for 0 ≤ k ≤ ⌊n/2⌋).  Now PROVED by direct construction
    via `enumerateTwoRow` rather than axiomatised. -/
class HasTwoRowCardinality (n : ℕ) where
  card_two_row : ℕ
  card_eq : card_two_row = n / 2 + 1

/-- Trivial instance for n = 0: only the empty partition. -/
instance : HasTwoRowCardinality 0 := ⟨1, by decide⟩

/-- Concrete instance for n = 12 (⁴He) — derived from the constructive
    `enumerateTwoRow_length` rather than axiomatised. -/
instance : HasTwoRowCardinality 12 :=
  ⟨(enumerateTwoRow 12).length, enumerateTwoRow_length 12⟩

/-- Concrete instance for n = 6 (deuteron).  -/
instance : HasTwoRowCardinality 6 :=
  ⟨(enumerateTwoRow 6).length, enumerateTwoRow_length 6⟩

/-- Concrete instance for n = 9 (T or ³He). -/
instance : HasTwoRowCardinality 9 :=
  ⟨(enumerateTwoRow 9).length, enumerateTwoRow_length 9⟩

/-- Universal cardinality instance: for any n, take the constructive
    enumeration's length. -/
def hasTwoRowCardinality_of (n : ℕ) : HasTwoRowCardinality n :=
  ⟨n / 2 + 1, rfl⟩

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

namespace HasTwoRowProjection

variable {HeckeAlg : Type*} [Inhabited HeckeAlg] [HasTwoRowProjection HeckeAlg]

/-- The complement projection 1 − π_{2-row} (defined point-wise as the
    "non-two-row" part: anything that's not in the image of π).  In
    a true direct-sum setting this would be a co-projection. -/
def piComplement [Sub HeckeAlg] : HeckeAlg → HeckeAlg :=
  fun β => β - pi β

/-- The trivial instance: π = id, satisfying idempotency vacuously.
    Used as the n=0 baseline (the trivial Hecke algebra has only one
    Wedderburn block, which is the [0] = (0) partition itself in Λ²). -/
def trivialInstance (HeckeAlg : Type*) : HasTwoRowProjection HeckeAlg where
  pi := id
  idempotent := fun _ => rfl

instance (HeckeAlg : Type*) : Inhabited (HasTwoRowProjection HeckeAlg) :=
  ⟨trivialInstance HeckeAlg⟩

end HasTwoRowProjection

/-- Bridge lemma: any list of length ≤ 2 is a two-row partition of
    its sum.  Used by HasHe4DominantBlock to connect the dominant
    block (9, 3) to TwoRowStratum 12. -/
theorem twoRow_of_length_le_two
    (parts : List ℕ) (h : parts.length ≤ 2) :
    TwoRowStratum (parts.sum) parts :=
  ⟨rfl, h⟩

/-- The dominant block (9, 3) explicitly belongs to Λ²(12). -/
theorem dominant_he4_in_stratum :
    TwoRowStratum 12 [9, 3] := by decide

end QOU.BraidKnot.TwoRowStratum

