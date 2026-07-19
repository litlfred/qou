import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Ring

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

/-- `B · v` commutes with finite sums in the left argument. -/
theorem B_sum_left (hBaddl : ∀ u u' v, B (u + u') v = B u v + B u' v)
    (hBzerol : ∀ v, B 0 v = 0) (s : Finset ι) (f : ι → (ι → R)) (v : ι → R) :
    B (∑ i ∈ s, f i) v = ∑ i ∈ s, B (f i) v := by
  induction s using Finset.induction with
  | empty => simp [hBzerol]
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, hBaddl, ih]

/-- `B u ·` commutes with finite sums in the right argument. -/
theorem B_sum_right (hBaddr : ∀ u v v', B u (v + v') = B u v + B u v')
    (hBsmulr : ∀ (c : R) u v, B u (c • v) = c • B u v)
    (u : ι → R) (s : Finset ι) (f : ι → (ι → R)) :
    B u (∑ j ∈ s, f j) = ∑ j ∈ s, B u (f j) := by
  have hBzeror : B u 0 = 0 := by
    have h := hBaddr u 0 0; rw [add_zero] at h; exact self_eq_add_right.mp h
  induction s using Finset.induction with
  | empty => simpa using hBzeror
  | @insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, hBaddr, ih]

/-- `τ` commutes with finite sums (additivity). -/
theorem tau_sum (hτadd : ∀ u v, τ (u + v) = τ u + τ v)
    (hτsmul : ∀ (c : R) v, τ (c • v) = c * τ v)
    (s : Finset ι) (f : ι → (ι → R)) :
    τ (∑ i ∈ s, f i) = ∑ i ∈ s, τ (f i) := by
  have hτzero : τ (0 : ι → R) = 0 := by
    have h := hτadd 0 0; rw [add_zero] at h; exact self_eq_add_right.mp h
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
  rw [B_sum_left B hBaddl hBzerol, tau_sum τ hτadd hτsmul]
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
  rw [B_sum_right B hBaddr hBsmulr, tau_sum τ hτadd hτsmul]
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

end QOU.Machinery.BilinearTrace
