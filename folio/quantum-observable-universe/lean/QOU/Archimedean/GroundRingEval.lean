import QOU.GroundRingCore
import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.Data.Real.Basic

/-!
# QOU.Archimedean.GroundRingEval — the specialisation `ι : R_q → ℝ, q ↦ q₀`

Bean `qou-d8m1`, the other half of `qou-mt7r`.

The §7c split (`qou-6ome`) left the library with two layers and nothing
between them:

| layer | field |
|---|---|
| `QOU.SubstrateParameter M` | `field : M → R_q` (categorical) |
| `QOU.ArchimedeanSubstrateField M` | `field : M → ℝ` (order axioms) |

`ArchimedeanSubstrateField`'s own docstring said it was "obtained by
specialising the categorical field through `ι : R_q → ℝ, q ↦ q₀`" — and the
type said no such thing. Its `field` was independent, so an instance could pair
a real field with a completely unrelated categorical one and every archimedean
proposition downstream still held. The prose asserted a tie the structure did
not carry.

## `ι` is constructed here, not assumed

This is the difference from `QOU/Shared/ArchimedeanEval.lean`, and it is worth
stating because the two files look alike. There the coefficient ring is an
opaque `CommRing R`, so `eval : R →+* ℝ` has to be a **hypothesis**. Here the
ground ring is concrete — `R_q = LaurentPolynomial ℤ` — and evaluation at a
real unit is an ordinary ring homomorphism:

* `evalAt q₀ : R_q →+* ℝ` for `q₀ : ℝˣ`, built from `AddMonoidAlgebra.lift`
  applied to `zpowersHom` at `q₀`;
* `evalAt_T : evalAt q₀ (T n) = q₀ ^ n`, so it really is "substitute `q₀` for
  the indeterminate" and not some other map;
* `evalAt_q_param` / `evalAt_q_inv_param` pin the two named generators.

`evalAt_q_param_mul_inv` checks the constructed hom respects
`q_param * q_inv_param = 1` — the relation `GroundRingCore` proves — so the
image of the formal inverse really is the inverse of the image.

**`q₀ : ℝˣ` rather than `q₀ : ℝ` with a side condition.** `R_q` is
`ℤ[q, q⁻¹]`: the indeterminate is *invertible*, so any evaluation must send it
somewhere invertible. Taking a unit is not a convenience — a plain real with
`q₀ ≠ 0` would need the inverse rebuilt at every use, and over a general
codomain nonzero would not even suffice. This is the same distinction
`CategoricalQExtDeriv` ran into (bean `qou-u87j`): over a ring, invertible is
not implied by nonzero.

## What the tie does and does not settle

`ArchimedeanRealisation` bundles a categorical `SubstrateParameter`, a choice
of `q₀`, and the two archimedean axioms *stated about the realised values*.
`toArchimedeanSubstrateField` then produces the archimedean layer rather than
letting it be posited independently.

The order axioms are still genuinely assumed, and that is correct: `1 ≤ q₀^n`
and "not a root of unity" are archimedean facts about the chosen `q₀`, not
consequences of the categorical layer. What is no longer assumed is the
*field itself*.

**This is not the archimedean τ-functor.** `ι` is an evaluation of the ground
ring; τ is a functor from the braided category
(`QOU/Archimedean/TauFunctorTargetSpec.lean`, still open). That `ι` turns out
to be constructible says nothing about τ, and `evalAt` should not be cited as
progress on it.

-- Ref: [leitner2026] quantum-observable-universe/substrate-parameter.md
-/

namespace QOU.Archimedean

open LaurentPolynomial

/-- **The specialisation `ι : R_q → ℝ`, `q ↦ q₀`** — constructed, not assumed.

    `R_q = ℤ[q, q⁻¹] = AddMonoidAlgebra ℤ ℤ`, so a ring map to `ℝ` is exactly a
    monoid map `Multiplicative ℤ →* ℝ`, i.e. a choice of unit. -/
noncomputable def evalAt (q0 : ℝˣ) : QOU.GroundRing.R_q →+* ℝ :=
  (AddMonoidAlgebra.lift ℤ ℤ ℝ ((Units.coeHom ℝ).comp (zpowersHom ℝˣ q0))).toRingHom

/-- `ι` substitutes `q₀` for the indeterminate: `T n ↦ q₀ ^ n`.

    Without this the definition above would be untethered in exactly the way
    this bean is about — *some* ring hom, with no reason to call it `q ↦ q₀`. -/
theorem evalAt_T (q0 : ℝˣ) (n : ℤ) : evalAt q0 (T n) = (q0 : ℝ) ^ n := by
  show (AddMonoidAlgebra.lift ℤ ℤ ℝ ((Units.coeHom ℝ).comp (zpowersHom ℝˣ q0)))
        (AddMonoidAlgebra.single n (1 : ℤ)) = (q0 : ℝ) ^ n
  rw [AddMonoidAlgebra.lift_single]
  simp

/-- `ι q = q₀` on the named generator. -/
theorem evalAt_q_param (q0 : ℝˣ) : evalAt q0 QOU.GroundRing.q_param = (q0 : ℝ) := by
  unfold QOU.GroundRing.q_param
  rw [evalAt_T]
  simp

/-- `ι q⁻¹ = q₀⁻¹` on the named generator. -/
theorem evalAt_q_inv_param (q0 : ℝˣ) :
    evalAt q0 QOU.GroundRing.q_inv_param = (q0 : ℝ)⁻¹ := by
  unfold QOU.GroundRing.q_inv_param
  rw [evalAt_T]
  simp

/-- The constructed hom respects the defining relation of `GroundRingCore`:
    the image of the formal inverse is the inverse of the image. -/
theorem evalAt_q_param_mul_inv (q0 : ℝˣ) :
    evalAt q0 QOU.GroundRing.q_param * evalAt q0 QOU.GroundRing.q_inv_param = 1 := by
  rw [← map_mul, QOU.GroundRing.q_param_mul_inv, map_one]

/-- **An archimedean realisation of a categorical substrate parameter.**

    The archimedean layer is *produced from* the categorical one through `ι`,
    rather than posited beside it. The two order axioms remain assumptions —
    they are archimedean facts about the chosen `q₀` and do not follow from the
    categorical layer — but they are now stated about the realised values. -/
structure ArchimedeanRealisation (M : Type*) where
  /-- The categorical substrate parameter being realised. -/
  sp : QOU.SubstrateParameter M
  /-- The chosen specialisation point, a unit because `q` is invertible in `R_q`. -/
  q0 : ℝˣ
  /-- **Classicality bound**, stated about the realised value. -/
  ge_one : ∀ p : M, 1 ≤ evalAt q0 (sp.field p)
  /-- Not a root of unity, stated about the realised value. -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → (evalAt q0 (sp.field p)) ^ k ≠ 1

/-- The tie: an `ArchimedeanSubstrateField` whose `field` is `ι ∘ sp.field`,
    not an independent function. -/
noncomputable def ArchimedeanRealisation.toArchimedeanSubstrateField {M : Type*}
    (r : ArchimedeanRealisation M) : QOU.ArchimedeanSubstrateField M where
  field := fun p => evalAt r.q0 (r.sp.field p)
  field_ge_one := r.ge_one
  not_root_of_unity := r.not_root_of_unity

/-- **The classical limit transfers.** Where the categorical parameter is `1`,
    so is its realisation — for every choice of `q₀`.

    This is the payoff, and the test of whether the tie is worth anything. With
    `ArchimedeanSubstrateField.field` independent it was not provable: a point
    could sit at the classical value of the categorical parameter and at an
    arbitrary real simultaneously. -/
theorem ArchimedeanRealisation.realised_one {M : Type*}
    (r : ArchimedeanRealisation M) (p : M) (h : r.sp.field p = 1) :
    r.toArchimedeanSubstrateField.field p = 1 := by
  show evalAt r.q0 (r.sp.field p) = 1
  rw [h, map_one]

/-- **Realisations are inhabited, and can hit a prescribed value.**

    The categorical parameter is constantly the indeterminate `q`, so the
    realised field is constantly `q₀`. The two order axioms remain exactly the
    archimedean facts about `q₀`: they cannot be discharged from the
    categorical layer, which is the honest situation rather than a gap. -/
noncomputable def constRealisation (M : Type*) (q0 : ℝˣ)
    (h1 : 1 ≤ (q0 : ℝ)) (hroot : ∀ k : ℕ, k ≥ 1 → (q0 : ℝ) ^ k ≠ 1) :
    ArchimedeanRealisation M where
  sp := ⟨fun _ => QOU.GroundRing.q_param⟩
  q0 := q0
  ge_one := by intro _; rw [evalAt_q_param]; exact h1
  not_root_of_unity := by intro _ k hk; rw [evalAt_q_param]; exact hroot k hk

@[simp] theorem constRealisation_field {M : Type*} (q0 : ℝˣ)
    (h1 : 1 ≤ (q0 : ℝ)) (hroot : ∀ k : ℕ, k ≥ 1 → (q0 : ℝ) ^ k ≠ 1) (p : M) :
    (constRealisation M q0 h1 hroot).toArchimedeanSubstrateField.field p
      = (q0 : ℝ) :=
  evalAt_q_param q0

/-- **The `d_q²` counterexample witness is realisable.**

    `QOU/Elaboration.lean`'s `dq_squared_nonvanishing` refutes a statement
    quantified over *arbitrary* `ArchimedeanSubstrateField`s, using a witness
    with `field ≡ 2` on `PUnit`. Because that structure's field is independent
    of any categorical parameter, the refuted statement could in principle have
    been a strawman — a real-valued function with no substrate behind it.

    It is not. The witness arises from a genuine `ArchimedeanRealisation`: the
    categorical parameter is the indeterminate `q`, specialised at `q₀ = 2`. So
    `d_q²` fails to vanish on a substrate the framework can actually produce.

    This is the first thing the tie buys beyond hygiene, and it is why
    `qou-w7sc` concluded the migration it proposed was the wrong shape: there
    was exactly one construction site of a bare `ArchimedeanSubstrateField` in
    the library, and it is this witness, which should keep its concrete form. -/
theorem dq_witness_realisable :
    ∃ r : ArchimedeanRealisation PUnit,
      ∀ p, r.toArchimedeanSubstrateField.field p = 2 := by
  have hroot : ∀ k : ℕ, k ≥ 1 → ((Units.mk0 (2 : ℝ) (by norm_num) : ℝˣ) : ℝ) ^ k ≠ 1 := by
    intro k hk
    have h2 : (2 : ℝ) ≤ 2 ^ k := by
      calc (2 : ℝ) = 2 ^ 1 := (pow_one 2).symm
        _ ≤ 2 ^ k := pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 2) hk
    intro h
    simp only [Units.val_mk0] at h
    rw [h] at h2
    norm_num at h2
  refine ⟨constRealisation PUnit (Units.mk0 (2 : ℝ) (by norm_num)) (by norm_num) hroot, ?_⟩
  intro p
  rw [constRealisation_field]
  simp

end QOU.Archimedean
