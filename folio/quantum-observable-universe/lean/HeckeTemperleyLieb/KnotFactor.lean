import HeckeTemperleyLieb.TauSchurElement

/-!
# QOU.Hecke.KnotFactor — every trace on `H_n(q)` is the τ-pairing with a central knot factor

The braid-level half of `conj:knot-factor-frobenius-pairing` says: the Markov trace of
a braid equals its Frobenius pairing with a fixed "knot factor".  Read in the
Hecke algebra, with the Frobenius pairing `⟨x, y⟩ = τ(x y)` given by the canonical
symmetrizing trace `τ`, this is a **theorem**, and it holds for *every* trace, not
only the Markov one.

## The argument

Fix a splitting `E : H_n(q) ≃ₐ ∏_i M_{d_i}(K)` (Wedderburn).

1. Every trace is a weighted sum of block traces
   (`QOU.MathlibExt.eq_weightedTrace_of_algEquiv`): `t = Σ_i y_i tr_i`, `τ = Σ_i c_i tr_i`.
2. `c_i ≠ 0` for every block and every `q ≠ 0`
   (`QOU.Hecke.TwBasis.traceWeight_tau_ne_zero`; the abstract Schur element is
   `s_i = 1 / c_i`).
3. So the central element `κ := E⁻¹(i ↦ (y_i / c_i) · 1) = Σ_i y_i s_i e_i`
   satisfies `τ(x κ) = Σ_i c_i (y_i / c_i) tr_i(x) = t(x)`.
4. `κ` is unique: `τ` is nondegenerate (`tau_eq_zero_of_forall_mul`).

## What is proved

* `knotFactor` — the element `κ`, for a splitting, a trace `t`, and the pairing trace.
* `knotFactor_comm` — `κ` is central.
* `trace_eq_mul_knotFactor` — `t x = τ'(x κ)` for any trace `τ'` with nonzero weights.
* `knotFactor_block` — block `i` of `E κ` is `(y_i · s_i) · 1`, i.e. `κ = Σ y_λ s_λ e_λ`.
* `hecke_trace_eq_tau_mul_knotFactor` — the Hecke instance with `τ`, for every `q ≠ 0`.
* `hecke_knotFactor_unique` — any `k` with `t x = τ(x k)` for all `x` equals `κ`.

## What this is not

* It is **not** a statement about the Markov trace specifically: the Ocneanu/Markov
  trace is not yet defined as a linear functional on `QOU.Hecke.IwahoriHecke K q n`.
  Once it is, it is one instance of `t` and the result applies verbatim.
* It says nothing about binding energy.  The binding half of the conjecture
  (`binding = E₀ (tr(W_free) − tr(W_atom))`) is a definition plus a comparison
  point, and is re-scoped separately (`QOU.Conjectures.KnotFactorFrobeniusPairing`).
* The splitting `E` is a hypothesis, as in `TauSchurElement`; at generic `q` it is
  `AnyChar.heckeWedderburnF`.

Generic over `[Field K]` with `q : K`; no ordering, no archimedean structure (§7c).
-/

namespace QOU.Hecke.KnotFactor

open QOU.MathlibExt Matrix

section General

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
variable {A : Type*} [Ring A] [Algebra K A]

/-- **The knot factor** of a trace `t` relative to a pairing trace `τ` and a
    splitting `E`: the pullback of the block scalars `y_i / c_i`. -/
noncomputable def knotFactor (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t τ : A →ₗ[K] K) (a : ∀ i, J i) : A :=
  E.symm (fun i => (traceWeight E t a i / traceWeight E τ a i) • (1 : Matrix (J i) (J i) K))

omit [Fintype ι] in
/-- Block `i` of the knot factor is the scalar `y_i / c_i`. -/
theorem knotFactor_apply (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t τ : A →ₗ[K] K) (a : ∀ i, J i) (i : ι) :
    E (knotFactor E t τ a) i
      = (traceWeight E t a i / traceWeight E τ a i) • (1 : Matrix (J i) (J i) K) := by
  simp [knotFactor]

omit [Fintype ι] in
/-- **The knot factor is central.** -/
theorem knotFactor_comm (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t τ : A →ₗ[K] K) (a : ∀ i, J i) (x : A) :
    knotFactor E t τ a * x = x * knotFactor E t τ a := by
  apply E.injective
  rw [map_mul, map_mul]
  funext i
  rw [Pi.mul_apply, Pi.mul_apply, knotFactor_apply, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.one_mul, Matrix.mul_one]

/-- **Every trace is the pairing with its knot factor.**  If the pairing trace `τ`
    has no zero block weight, then `t x = τ(x · κ)` for every `x`. -/
theorem trace_eq_mul_knotFactor (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t τ : A →ₗ[K] K) (ht : ∀ x y : A, t (x * y) = t (y * x))
    (hτ : ∀ x y : A, τ (x * y) = τ (y * x)) (a : ∀ i, J i)
    (hc : ∀ i, traceWeight E τ a i ≠ 0) (x : A) :
    t x = τ (x * knotFactor E t τ a) := by
  rw [eq_weightedTrace_of_algEquiv E t ht a x,
    eq_weightedTrace_of_algEquiv E τ hτ a (x * knotFactor E t τ a)]
  simp only [weightedTrace]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_mul, Pi.mul_apply, knotFactor_apply, Matrix.mul_smul, Matrix.mul_one,
    Matrix.trace_smul, smul_eq_mul]
  field_simp [hc i]

/-- **Uniqueness, given a nondegenerate pairing.**  If `τ(z y) = 0` for all `y`
    forces `z = 0`, then any `k` with `t x = τ(x k)` for all `x` is the knot factor. -/
theorem eq_knotFactor_of_forall (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t τ : A →ₗ[K] K) (ht : ∀ x y : A, t (x * y) = t (y * x))
    (hτ : ∀ x y : A, τ (x * y) = τ (y * x)) (a : ∀ i, J i)
    (hc : ∀ i, traceWeight E τ a i ≠ 0)
    (hnd : ∀ z : A, (∀ y : A, τ (z * y) = 0) → z = 0)
    (k : A) (hk : ∀ x, t x = τ (x * k)) :
    k = knotFactor E t τ a := by
  have hz : k - knotFactor E t τ a = 0 := by
    refine hnd _ fun y => ?_
    rw [hτ, mul_sub, map_sub, ← hk y, ← trace_eq_mul_knotFactor E t τ ht hτ a hc y, sub_self]
  exact sub_eq_zero.mp hz

end General

section Hecke

open QOU.Hecke.TwBasis

variable {K : Type*} [Field K] {q : K} {n : ℕ}
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **The braid-level knot-factor identity in `H_n(q)`.**  For every `q ≠ 0`, every
    splitting, and every trace `t` (the Markov trace is the intended instance),
    `t x = τ(x · κ)` with `κ` the central knot factor. -/
theorem hecke_trace_eq_tau_mul_knotFactor (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (t : QOU.Hecke.IwahoriHecke K q n →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (x : QOU.Hecke.IwahoriHecke K q n) :
    t x = tau K q n (x * knotFactor E t (tau K q n) a) :=
  trace_eq_mul_knotFactor E t (tau K q n) ht (tau_mul_comm K q n) a
    (traceWeight_tau_ne_zero hq E a) x

/-- **The knot factor is unique** in `H_n(q)`, `q ≠ 0`. -/
theorem hecke_knotFactor_unique (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (t : QOU.Hecke.IwahoriHecke K q n →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (k : QOU.Hecke.IwahoriHecke K q n)
    (hk : ∀ x, t x = tau K q n (x * k)) :
    k = knotFactor E t (tau K q n) a :=
  eq_knotFactor_of_forall E t (tau K q n) ht (tau_mul_comm K q n) a
    (traceWeight_tau_ne_zero hq E a)
    (fun _ hz => tau_eq_zero_of_forall_mul K q n hq hz) k hk

omit [Fintype ι] in
/-- **`κ = Σ_λ y_λ s_λ e_λ`**: block `i` of the knot factor is the trace weight
    times the abstract Schur element. -/
theorem knotFactor_block
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (t : QOU.Hecke.IwahoriHecke K q n →ₗ[K] K) (i : ι) :
    E (knotFactor E t (tau K q n) a) i
      = (traceWeight E t a i * abstractSchurElement E a i) • (1 : Matrix (J i) (J i) K) := by
  rw [knotFactor_apply, abstractSchurElement, div_eq_mul_inv]

end Hecke

end QOU.Hecke.KnotFactor
