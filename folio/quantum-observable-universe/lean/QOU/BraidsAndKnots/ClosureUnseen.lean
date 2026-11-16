/-
Closure cannot see a commutator difference.

A closure (braid closure, or any closing of a word by cups and caps) evaluates an element of an
algebra through a *trace*: a linear map `t` with `t (x * y) = t (y * x)`. This file proves:

* `unseen_iff`: two elements `a b` have the same value under **every** trace iff their
  difference lies in the commutator span `[A, A]`. The universal trace is the quotient map
  `A → A ⧸ [A, A]` (the zeroth Hochschild homology `HH₀`).
* `unseen_conj`: an emitted-and-reabsorbed subword `u * w * u⁻¹` is unseen against `w`.
* `trace_factors`: every trace factors through `HH₀` (closure = annular step, then read-out).
* `isTrace_sum`: a weighted average of traces is a trace (the Markov step averages sectors).
* `trace_conserved_of_conj`: under conjugation dynamics every closure invariant is conserved.
* `kron_one_mulVec_bell`, `ricochet`, `bell_pairing`: with the maximally entangled vector
  `Ω = Σᵢ eᵢ ⊗ eᵢ` (the coevaluation), `(X ⊗ 1) Ω = (1 ⊗ Xᵀ) Ω` and `⟨Ω, (X ⊗ 1) Ω⟩ = tr X`.
  So a closure is "prepare pairs, act on one half, project back onto the pairs".

Everything is over a generic commutative ring (§7c); no archimedean input.
-/
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.BraidsAndKnots.ClosureUnseen

universe u v

section Trace

variable {R : Type u} [CommRing R] {A : Type v} [Ring A] [Algebra R A]

/-- A linear map is a trace if it is invariant under cyclic rotation of a product. -/
def IsTrace {M : Type*} [AddCommGroup M] [Module R M] (t : A →ₗ[R] M) : Prop :=
  ∀ x y : A, t (x * y) = t (y * x)

variable (R A) in
/-- The commutator span `[A, A]`: the `R`-span of all `x * y - y * x`. -/
def commSpan : Submodule R A :=
  Submodule.span R {z | ∃ x y : A, z = x * y - y * x}

/-- The universal trace `A → A ⧸ [A, A]` (zeroth Hochschild homology). -/
def univTrace : A →ₗ[R] A ⧸ commSpan R A := (commSpan R A).mkQ

theorem univTrace_isTrace : IsTrace (univTrace (R := R) (A := A)) := by
  intro x y
  unfold univTrace
  rw [Submodule.mkQ_apply, Submodule.mkQ_apply, Submodule.Quotient.eq]
  exact Submodule.subset_span ⟨x, y, rfl⟩

/-- Every trace kills the commutator span. -/
theorem trace_vanishes_on_commSpan {M : Type*} [AddCommGroup M] [Module R M]
    {t : A →ₗ[R] M} (ht : IsTrace t) {z : A} (hz : z ∈ commSpan R A) : t z = 0 := by
  induction hz using Submodule.span_induction with
  | mem z hz =>
      obtain ⟨x, y, rfl⟩ := hz
      rw [map_sub, ht x y, sub_self]
  | zero => exact map_zero t
  | add a b _ _ ha hb => rw [map_add, ha, hb, add_zero]
  | smul r a _ ha => rw [map_smul, ha, smul_zero]

/-- `a` and `b` are *unseen-equivalent*: no trace (no closure) distinguishes them. -/
def Unseen (a b : A) : Prop :=
  ∀ (M : Type v) [AddCommGroup M] [Module R M] (t : A →ₗ[R] M), IsTrace t → t a = t b

/-- **No closure distinguishes `a` from `b` iff `a - b` lies in the commutator span.** -/
theorem unseen_iff (a b : A) : Unseen (R := R) a b ↔ a - b ∈ commSpan R A := by
  constructor
  · intro h
    have hab := h (A ⧸ commSpan R A) univTrace univTrace_isTrace
    unfold univTrace at hab
    rwa [Submodule.mkQ_apply, Submodule.mkQ_apply, Submodule.Quotient.eq] at hab
  · intro hab M _ _ t ht
    have h0 := trace_vanishes_on_commSpan ht hab
    rwa [map_sub, sub_eq_zero] at h0

/-- Conjugating by a unit changes an element by a commutator. -/
theorem conj_sub_mem (u : Aˣ) (w : A) :
    (u : A) * w * (↑u⁻¹ : A) - w ∈ commSpan R A := by
  refine Submodule.subset_span ⟨(u : A) * w, (↑u⁻¹ : A), ?_⟩
  rw [← mul_assoc (↑u⁻¹ : A), Units.inv_mul, one_mul, mul_assoc]

/-- **An emitted-and-reabsorbed subword is unseen**: `u * w * u⁻¹` and `w` agree under every
trace. -/
theorem unseen_conj (u : Aˣ) (w : A) :
    Unseen (R := R) ((u : A) * w * (↑u⁻¹ : A)) w :=
  (unseen_iff _ _).2 (conj_sub_mem u w)

/-- **Every closure factors through the annular step.** A trace `t` is the universal trace
`A → A ⧸ [A, A]` followed by a unique linear map: closure = annular closure (`HH₀`), then a
read-out. -/
theorem trace_factors {M : Type*} [AddCommGroup M] [Module R M] {t : A →ₗ[R] M}
    (ht : IsTrace t) :
    t = ((commSpan R A).liftQ t
        (fun _ hz => (LinearMap.mem_ker).2 (trace_vanishes_on_commSpan ht hz)))
      ∘ₗ univTrace := by
  ext x
  rfl

/-- **Averaging traces gives a trace.** A weighted sum `Σᵢ cᵢ • tᵢ` of traces (for example the
Markov trace as a weighted sum of sector characters) is again a trace. -/
theorem isTrace_sum {ι : Type*} (s : Finset ι) (c : ι → R) (tr : ι → A →ₗ[R] R)
    (h : ∀ i ∈ s, IsTrace (tr i)) : IsTrace (∑ i ∈ s, c i • tr i) := by
  intro x y
  simp only [LinearMap.coeFn_sum, Finset.sum_apply, LinearMap.smul_apply]
  exact Finset.sum_congr rfl (fun i hi => by rw [h i hi x y])

/-- **A closure invariant is conserved along conjugation dynamics.** If a word evolves in
discrete time by conjugation by units, `β (s+1) = g s * β s * (g s)⁻¹`, then every trace takes
the same value at every time. -/
theorem trace_conserved_of_conj {M : Type*} [AddCommGroup M] [Module R M]
    {t : A →ₗ[R] M} (ht : IsTrace t) (β : ℕ → A) (g : ℕ → Aˣ)
    (hstep : ∀ s, β (s + 1) = (g s : A) * β s * (↑(g s)⁻¹ : A)) :
    ∀ s, t (β s) = t (β 0) := by
  intro s
  induction s with
  | zero => rfl
  | succ s ih =>
      rw [hstep s, ← ih]
      have h0 := trace_vanishes_on_commSpan ht (conj_sub_mem (g s) (β s))
      rwa [map_sub, sub_eq_zero] at h0

end Trace

section Bell

open Matrix
open scoped Kronecker

variable {R : Type u} [CommRing R] {n : Type v} [Fintype n] [DecidableEq n]

/-- The maximally entangled vector `Ω = Σᵢ eᵢ ⊗ eᵢ` (the coevaluation of `Rⁿ`). -/
def bell : n × n → R := fun p => if p.1 = p.2 then 1 else 0

/-- Acting on one half of the pairs turns `Ω` into the matrix entries of `X`. -/
theorem kron_one_mulVec_bell (X : Matrix n n R) :
    (X ⊗ₖ (1 : Matrix n n R)) *ᵥ bell = fun p => X p.1 p.2 := by
  funext ⟨i, j⟩
  simp [mulVec, dotProduct, kroneckerMap_apply, Fintype.sum_prod_type, one_apply, bell]

/-- **Ricochet**: an operator on one half of `Ω` equals its transpose on the other half. -/
theorem ricochet (X : Matrix n n R) :
    (X ⊗ₖ (1 : Matrix n n R)) *ᵥ bell = ((1 : Matrix n n R) ⊗ₖ Xᵀ) *ᵥ bell := by
  rw [kron_one_mulVec_bell]
  funext ⟨i, j⟩
  simp [mulVec, dotProduct, kroneckerMap_apply, Fintype.sum_prod_type, one_apply, bell]

/-- **Closure as a Bell pairing**: preparing `Ω`, acting with `X` on one half and projecting
back onto `Ω` gives the trace of `X`. -/
theorem bell_pairing (X : Matrix n n R) :
    bell ⬝ᵥ ((X ⊗ₖ (1 : Matrix n n R)) *ᵥ bell) = trace X := by
  rw [kron_one_mulVec_bell]
  simp [dotProduct, Fintype.sum_prod_type, bell, trace, diag]

end Bell

end QOU.BraidsAndKnots.ClosureUnseen
