import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Ring
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Algebra.Hom

/-!
# Abstract bilinear-trace cyclicity: cyclic ⟺ Gram-symmetric

The `Fin`-index-agnostic core of trace cyclicity on a finite free module.

Every concrete Markov-trace level (`H₃` on `Fin 6`, `H₄` on `Fin 24`, …) is a
linear functional `τ` on `ι → R` together with a bilinear "product" `B`. The
`whnf`-free half of `tr_M(u·v) = tr_M(v·u)` — the reduction to the finite Gram
base — is entirely formal (bilinear expansion + a `Finset.sum_comm` swap) and
does **not** depend on the level. This file isolates it once, over an arbitrary
`Fintype` index:

  cyclicity for all `u, v`  ⟺  symmetry of the Gram matrix `G i j = τ (B (e i) (e j))`.

`QOU.Machinery.H4.trM_cyclic_of_gram_symm` (PR #4046) is the `Fin 24` instance of
`cyclic_of_gram_symm` below; the same lemma serves `H₃`, `H₅`, and any future
level. The *residual* — Gram symmetry itself — is what a per-level computation or
the abstract Ocneanu-induction / character-decomposition argument supplies; this
file does not close it, it reduces to it (honestly).
-/

namespace QOU.Machinery.BilinearTrace

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- Standard basis vector `e i = Pi.single i 1` on `ι → R`. -/
def e (i : ι) : ι → R := Pi.single i (1 : R)

/-- Basis decomposition `u = ∑ᵢ uᵢ • eᵢ`. -/
theorem basis_decomp (u : ι → R) : u = ∑ i, u i • (e (R := R) i) := by
  funext j
  rw [Finset.sum_apply]
  simp [e, Pi.single_apply, smul_eq_mul, Finset.sum_ite_eq]

section Reduction

variable (B : (ι → R) → (ι → R) → (ι → R)) (τ : (ι → R) → R)

omit [Fintype ι] in
/-- `B · v` commutes with finite sums in the left argument. -/
theorem B_sum_left (hBaddl : ∀ u u' v, B (u + u') v = B u v + B u' v)
    (hBzerol : ∀ v, B 0 v = 0) (s : Finset ι) (f : ι → (ι → R)) (v : ι → R) :
    B (∑ i ∈ s, f i) v = ∑ i ∈ s, B (f i) v := by
  induction s using Finset.induction with
  | empty => simp [hBzerol]
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, hBaddl, ih]

omit [Fintype ι] in
/-- `B u ·` commutes with finite sums in the right argument. -/
theorem B_sum_right (hBaddr : ∀ u v v', B u (v + v') = B u v + B u v')
    (u : ι → R) (s : Finset ι) (f : ι → (ι → R)) :
    B u (∑ j ∈ s, f j) = ∑ j ∈ s, B u (f j) := by
  have hBzeror : B u 0 = 0 := by
    have h := hBaddr u 0 0; rw [add_zero] at h; exact left_eq_add.mp h
  induction s using Finset.induction with
  | empty => simpa using hBzeror
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, hBaddr, ih]

omit [Fintype ι] in
/-- `τ` commutes with finite sums (additivity). -/
theorem tau_sum (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (s : Finset ι) (f : ι → (ι → R)) :
    τ (∑ i ∈ s, f i) = ∑ i ∈ s, τ (f i) := by
  have hτzero : τ (0 : ι → R) = 0 := by
    have h := hτadd 0 0; rw [add_zero] at h; exact left_eq_add.mp h
  induction s using Finset.induction with
  | empty => simpa using hτzero
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, hτadd, ih]

/-- Expand `τ (B u v)` over the left basis. -/
theorem tau_B_left_expand
    (hBaddl : ∀ u u' v, B (u + u') v = B u v + B u' v)
    (hBsmull : ∀ (c : R) u v, B (c • u) v = c • B u v)
    (hBzerol : ∀ v, B 0 v = 0)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (u v : ι → R) :
    τ (B u v) = ∑ i, u i * τ (B (e i) v) := by
  conv_lhs => rw [basis_decomp u]
  rw [B_sum_left B hBaddl hBzerol, tau_sum τ hτadd]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [hBsmull, hτsmul]

/-- Expand `τ (B w v)` over the right basis. -/
theorem tau_B_right_expand
    (hBaddr : ∀ u v v', B u (v + v') = B u v + B u v')
    (hBsmulr : ∀ (c : R) u v, B u (c • v) = c • B u v)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (w v : ι → R) :
    τ (B w v) = ∑ j, v j * τ (B w (e j)) := by
  conv_lhs => rw [basis_decomp v]
  rw [B_sum_right B hBaddr, tau_sum τ hτadd]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [hBsmulr, hτsmul]

/-- **Gram form.** `τ (B u v) = ∑_{i,j} u_i v_j · G_{i,j}` with `G_{i,j} = τ (B (e i) (e j))`. -/
theorem tau_B_gram
    (hBaddl : ∀ u u' v, B (u + u') v = B u v + B u' v)
    (hBaddr : ∀ u v v', B u (v + v') = B u v + B u v')
    (hBsmull : ∀ (c : R) u v, B (c • u) v = c • B u v)
    (hBsmulr : ∀ (c : R) u v, B u (c • v) = c • B u v)
    (hBzerol : ∀ v, B 0 v = 0)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (u v : ι → R) :
    τ (B u v) = ∑ i, ∑ j, u i * v j * τ (B (e i) (e j)) := by
  rw [tau_B_left_expand B τ hBaddl hBsmull hBzerol hτadd hτsmul]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [tau_B_right_expand B τ hBaddr hBsmulr hτadd hτsmul, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  ring

/-- **Cyclicity from Gram symmetry** — the `whnf`-free reduction, over any
`Fintype` index. Given the finite Gram matrix `G_{i,j} = τ (B (e i) (e j))` is
symmetric, `τ (B u v) = τ (B v u)` for all `u, v`. -/
theorem cyclic_of_gram_symm
    (hBaddl : ∀ u u' v, B (u + u') v = B u v + B u' v)
    (hBaddr : ∀ u v v', B u (v + v') = B u v + B u v')
    (hBsmull : ∀ (c : R) u v, B (c • u) v = c • B u v)
    (hBsmulr : ∀ (c : R) u v, B u (c • v) = c • B u v)
    (hBzerol : ∀ v, B 0 v = 0)
    (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (hsymm : ∀ i j, τ (B (e i) (e j)) = τ (B (e j) (e i)))
    (u v : ι → R) :
    τ (B u v) = τ (B v u) := by
  rw [tau_B_gram B τ hBaddl hBaddr hBsmull hBsmulr hBzerol hτadd hτsmul u v,
      tau_B_gram B τ hBaddl hBaddr hBsmull hBsmulr hBzerol hτadd hτsmul v u,
      Finset.sum_comm]
  refine Finset.sum_congr rfl (fun x _ => Finset.sum_congr rfl (fun y _ => ?_))
  rw [hsymm y x]; ring

end Reduction

/-! ## Character route to Gram symmetry (bricks toward the all-`n` closure)

The `whnf`-free reduction above leaves the finite Gram symmetry itself. The
light, level-agnostic way to discharge it: a Markov/Ocneanu trace on a
semisimple algebra is a nonnegative combination of irreducible **characters**
`tr_M = ∑_λ w_λ · χ_λ`, and every character `χ_λ = trace ∘ ρ_λ` is cyclic for
free via `Matrix.trace_mul_comm`. These bricks build that argument abstractly;
the remaining keystone is the concrete decomposition (the `ρ_λ`, e.g. Hoefsmit /
seminormal reps of `H_n(q)`, and the weights `w_λ`), which supplies the `∑`. -/

section Character

variable {A : Type*} [Ring A] [Algebra R A]

/-- A functional `τ : A → R` is **cyclic** (a trace) if `τ (x·y) = τ (y·x)`. -/
def IsCyclic (τ : A → R) : Prop := ∀ x y : A, τ (x * y) = τ (y * x)

/-- **Brick — characters are cyclic.** The trace of any matrix representation
`ρ : A →ₐ[R] Matrix n n R` is a cyclic functional (`Matrix.trace_mul_comm`). -/
theorem isCyclic_trace_comp {n : Type*} [Fintype n] [DecidableEq n]
    (ρ : A →ₐ[R] Matrix n n R) : IsCyclic (R := R) (fun x => (ρ x).trace) := by
  intro x y
  simp only [map_mul]
  rw [Matrix.trace_mul_comm]

omit [Algebra R A] in
/-- **Brick — cyclic functionals are closed under `+`.** -/
theorem add {σ τ : A → R} (hσ : IsCyclic σ) (hτ : IsCyclic τ) :
    IsCyclic (fun x => σ x + τ x) := by
  intro x y; show σ (x * y) + τ (x * y) = σ (y * x) + τ (y * x); rw [hσ x y, hτ x y]

omit [Algebra R A] in
/-- **Brick — cyclic functionals are closed under a scalar multiple.** -/
theorem smul {τ : A → R} (c : R) (hτ : IsCyclic τ) :
    IsCyclic (fun x => c * τ x) := by
  intro x y; show c * τ (x * y) = c * τ (y * x); rw [hτ x y]

omit [Algebra R A] in
/-- **Brick — a finite weighted sum of cyclic functionals is cyclic.** This is
the shape of `tr_M = ∑_λ w_λ · χ_λ`: given each `χ_λ` cyclic (the previous
bricks), the Markov trace is cyclic, hence Gram-symmetric. -/
theorem isCyclic_weighted_sum {κ : Type*} (s : Finset κ) (w : κ → R) (χ : κ → A → R)
    (hχ : ∀ k ∈ s, IsCyclic (χ k)) :
    IsCyclic (fun x => ∑ k ∈ s, w k * χ k x) := by
  intro x y
  show ∑ k ∈ s, w k * χ k (x * y) = ∑ k ∈ s, w k * χ k (y * x)
  exact Finset.sum_congr rfl (fun k hk => by rw [hχ k hk x y])

end Character

/-! ## Bridge — Gram symmetry from a representation decomposition

The keystone brick that connects the character route back to the concrete
`whnf`-free reduction. It needs **no ring/associativity structure** on the NF
module (so the `Fin 24` associativity `whnf` wall is avoided): only that the
trace `τ` decomposes as a finite weighted sum of representation-traces, each
representation being multiplicative on the bilinear product `B`. Then the finite
Gram symmetry — the residual left by `cyclic_of_gram_symm` — holds. What remains
for a concrete level is exactly the *content*: the representations `ρ_λ` (e.g.
Hoefsmit / seminormal at `H_n(q)`) and the Markov weights `w_λ`. -/

section Bridge

variable {Λ : Type*} {dim : Λ → Type*} [∀ l, Fintype (dim l)] [∀ l, DecidableEq (dim l)]

omit [Fintype ι] [(l : Λ) → DecidableEq (dim l)] in
/-- **Bridge brick.** If `τ = ∑_λ w_λ · trace ∘ ρ_λ` with each `ρ_λ` multiplicative
on the bilinear product `B` (`ρ_λ (B u v) = ρ_λ u * ρ_λ v`), then the Gram matrix
`G_{i,j} = τ (B (e i) (e j))` is symmetric. Combined with `cyclic_of_gram_symm`,
this gives full cyclicity with no per-pair `Fin`-computation. -/
theorem gram_symm_of_rep_decomp
    (B : (ι → R) → (ι → R) → (ι → R)) (τ : (ι → R) → R)
    (s : Finset Λ) (w : Λ → R) (ρ : ∀ l, (ι → R) → Matrix (dim l) (dim l) R)
    (hmul : ∀ l u v, ρ l (B u v) = ρ l u * ρ l v)
    (hdecomp : ∀ x, τ x = ∑ l ∈ s, w l * (ρ l x).trace)
    (i j : ι) :
    τ (B (e i) (e j)) = τ (B (e j) (e i)) := by
  rw [hdecomp, hdecomp]
  refine Finset.sum_congr rfl (fun l _ => ?_)
  rw [hmul, hmul, Matrix.trace_mul_comm]

end Bridge

end QOU.Machinery.BilinearTrace
