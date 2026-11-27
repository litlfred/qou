import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Algebra.Group.Prod
import Mathlib.Data.Int.Cast.Lemmas
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.StandardModel.GaugeHeckeCanonicalFaithfulness — what `conj:gauge-hecke-realization` asks, made precise

The block `conj:gauge-hecke-realization` says the conjectural content is *faithfulness of the
canonical quotient* `B_n → H_n(q)` on gauge automorphisms ("the Hecke relation is a quotient,
and a quotient can collapse symmetry").  Its Lean class `GaugeHeckeRealization` instead asks
for **some** injective monoid homomorphism `End X →* H`.  That is strictly weaker: it does not
mention the quotient at all.  This module

1. states the canonical reading (`FaithfulVia`) and proves it implies the existence reading
   (`exists_injective_of_faithfulVia`), so the existence class is the weaker of the two;
2. proves the `n = 2` instance of the canonical reading exactly: on `B₂ ≅ ℤ`, the Hecke
   quotient `σ ↦ T`, with `T` acting on the two eigenlines of `(T - q)(T + q⁻¹) = 0` by
   `q` and `-q⁻¹`, is injective **iff `q` is not a root of unity**
   (`braidTwo_hecke_injective_iff`).

## What is NOT closable here, and why (literature, not proved in this file)

For `n ≥ 3` the canonical reading with `End X = B_n` is the faithfulness of the
Iwahori–Hecke ("Jones") representation of `B_n`.  The reduced Burau representation is a
summand of it, so faithfulness of Burau gives faithfulness of the Hecke representation:
`n = 3` (Magnus–Peluso) and `n = 4` (Bharathram–Birman–Brendle, arXiv:2607.05283, 2026
preprint).  Burau is **unfaithful** for `n ≥ 5` (Moody, Long–Paton, Bigelow), and whether the
full Hecke representation of `B_n` is faithful for `n ≥ 5` is an open problem.  So for
`n ≥ 5` the conjecture contains a known open problem of low-dimensional topology.

Base: an arbitrary field `K`; nothing archimedean, no numerical anchor for `q`.
-/

namespace QOU.StandardModel.GaugeHeckeCanonical

/-- **Canonical reading.**  A gauge automorphism monoid `M` is *faithfully realised via* a
given monoid homomorphism `φ` (intended: the Hecke quotient) when `φ` is injective. -/
def FaithfulVia {M H : Type*} [Monoid M] [Monoid H] (φ : M →* H) : Prop :=
  Function.Injective φ

/-- The canonical reading implies the existence reading used by the class
`GaugeHeckeRealization`; the converse fails in general, since the existence reading does not
name the quotient. -/
theorem exists_injective_of_faithfulVia {M H : Type*} [Monoid M] [Monoid H] (φ : M →* H)
    (h : FaithfulVia φ) : ∃ Φ : M →* H, Function.Injective Φ :=
  ⟨φ, h⟩

/-! ## The `n = 2` instance -/

variable {K : Type*} [Field K]

/-- The Hecke image of `σ₁^k ∈ B₂ ≅ ℤ`, read on the two eigenlines of `T`
(eigenvalues `q` and `-q⁻¹`): the pair `(q^k, (-q⁻¹)^k)`. -/
def braidTwoHecke (q : Kˣ) : Multiplicative ℤ →* Kˣ × Kˣ :=
  zpowersHom (Kˣ × Kˣ) (q, -q⁻¹)

theorem braidTwoHecke_apply (q : Kˣ) (k : ℤ) :
    braidTwoHecke q (Multiplicative.ofAdd k) = (q ^ k, (-q⁻¹) ^ k) := by
  simp [braidTwoHecke, zpowersHom_apply, Prod.pow_def]

/-- The two eigenvalues satisfy the Hecke relation `(T - q)(T + q⁻¹) = 0`. -/
theorem eigen_hecke (q : Kˣ) :
    ((q : K) - q) * ((q : K) + (q⁻¹ : Kˣ)) = 0 ∧
    (((-q⁻¹ : Kˣ) : K) - q) * (((-q⁻¹ : Kˣ) : K) + (q⁻¹ : Kˣ)) = 0 := by
  constructor <;> simp

/-- **`n = 2`: the Hecke quotient is faithful on `B₂` iff `q` is not a root of unity.** -/
theorem braidTwo_hecke_injective_iff (q : Kˣ) :
    FaithfulVia (braidTwoHecke q) ↔ ∀ k : ℤ, k ≠ 0 → q ^ k ≠ 1 := by
  constructor
  · intro hinj k hk hqk
    -- `σ^{2k}` and the identity have the same image `(1, 1)`.
    have e1 : q ^ (2 * k) = 1 := by rw [mul_comm, zpow_mul, hqk, one_zpow]
    have e2 : (-q⁻¹) ^ (2 * k) = 1 := by
      rw [Even.neg_zpow ⟨k, by ring⟩, inv_zpow', zpow_neg, e1, inv_one]
    have h2 : braidTwoHecke q (Multiplicative.ofAdd (2 * k)) =
        braidTwoHecke q (Multiplicative.ofAdd 0) := by
      rw [braidTwoHecke_apply, braidTwoHecke_apply, e1, e2]
      simp
    have h3 : (2 * k : ℤ) = 0 := by
      have := hinj h2
      simpa using this
    omega
  · intro hroot a b hab
    have h1 := congrArg Prod.fst hab
    simp [braidTwoHecke] at h1
    have hz : q ^ (Multiplicative.toAdd a - Multiplicative.toAdd b) = 1 := by
      rw [zpow_sub, h1, mul_inv_cancel]
    by_contra hne
    apply hroot _ _ hz
    intro h0
    apply hne
    have : Multiplicative.toAdd a = Multiplicative.toAdd b := by omega
    simpa using congrArg Multiplicative.ofAdd this

end QOU.StandardModel.GaugeHeckeCanonical
