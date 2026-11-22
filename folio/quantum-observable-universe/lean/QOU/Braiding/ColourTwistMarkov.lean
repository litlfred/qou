/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Colour-twisted Markov traces on `(R³)^⊗n`: the rank-2 twist is convention D

On `V = R³` the Jimbo `U_q(gl₃)` R-matrix `Ř` gives an action of the Hecke tower on `V^⊗n`
(`σᵢ ↦ Ř` on factors `i, i+1`). A diagonal twist `K = diag(k₀, k₁, k₂)` gives the functional
`x ↦ tr(K^{⊗n} x)`. This file proves, over a generic field `R` (no `ℝ`, no `q₀`):

* `jimboR_hecke`: `Ř` satisfies the Hecke relation `(Ř − q)(Ř + q⁻¹) = 0`.
* `twistPartialTrace_eq_diagonal`: the partial trace `P = tr₂((1 ⊗ K) Ř)` is diagonal,
  `P_aa = q·k_a + (q − q⁻¹)·Σ_{b > a} k_b`.
* `twisted_trace_markov` (**all `n`**): if `P·K = s·K` (scalar on the range of `K`; the `K` on
  the last factor comes from cyclicity), then for **every** finite index type `β`, **every** diagonal
  weight `w` on `β` (take `β = Fin 3^{n-1}`, `w = K^{⊗(n-1)}`) and **every** `x ∈ End(β × R³)`,
  `tr(diag(w ⊗ K ⊗ K)·(x ⊗ 1)·(1 ⊗ Ř)) = s · tr(diag(w ⊗ K)·x)`.
  So the normalised functional `tr(K^{⊗n}·)/(tr K)^n` satisfies the Markov property
  `τ_{n+1}((x ⊗ 1)σ_n) = z·τ_n(x)` with `z = s / tr K` (`twisted_trace_markov_normalised`).
  This is the Markov step only. The trace property `τ_n(xy) = τ_n(yx)` on the image of `H_n` (which
  needs that image to commute with `K^{⊗n}`) is **not** proved here; the probe checks it on `H₃`.
* Classification of `z` by the rank of `K` (`z_of_rank_one`, `z_of_rank_two`, `z_of_rank_three`):
  rank 1 gives `z = q`, rank 2 (any of the three supports) gives `z_D = q³/(q²+1)`,
  rank 3 gives `z₃ = q⁵/(q⁴+q²+1) = q³/[3]_q`. Existence witnesses: `twistOne`, `twistD`,
  `twistPivotal`.
* `rank_two_twist_conventionD`: the rank-2 parameter satisfies the convention-D pin
  `z·(q + q⁻¹) = q²`, and composing with `ocneanuWeight_conventionD_eq_zero_of_three_rows`, the
  Ocneanu weight at that `z` vanishes on every shape with three or more rows.
* Colour invariance (`invariant_twist_eq`, `invariant_twist_not_rank_two`,
  `pivotal_twist_invariant`): a diagonal `M` whose functional `tr(M·)` is invariant under the
  adjoint action of `E₁, E₂` is `m₂·diag(q⁻⁴, q⁻², 1)`; so a nonzero invariant diagonal twist is
  invertible, is never rank 2, and (`invariant_markov_z_ne_zD`) never gives `z_D`.

**What is NOT proved here.** The braid relation for `Ř` on `(R³)^⊗3` (checked exactly in the probe);
the identification of `τ_n` with a Markov trace of `H_n(q)` on all of `H_n` (needs the trace
property and that the image of `H_n` lies in the commutant of `K^{⊗n}`); Ocneanu uniqueness
(a Markov trace is fixed by `z`), which is what turns "`z = z_D`" into "the weights are convention
D's". The convention-D corollary below is therefore a statement about the Ocneanu weight **at** the
rank-2 twist's `z`, not a proof that the twisted functional's Wedderburn weights equal it.

Source: `computations/probes/qcd_colour_full_tower/qcd_colour_full_tower_probe.py`
(T1, exact over `ℚ(q)`, `R upper = True`, coproduct variant B), `RESULT.md` in the same directory;
bean `qou-ni4b`.

Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
Ref: [jones1987] https://www.jstor.org/stable/1971403
-/
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import QOU.SchurWeyl.OcneanuWeight

namespace QOU.Braiding.ColourTwist

open Matrix

variable {R : Type*} [Field R]

/-! ### The Jimbo R-matrix on `R³ ⊗ R³` -/

/-- The Jimbo `U_q(gl₃)` R-matrix (upper convention). Column `(a, b)` is the image of
`e_a ⊗ e_b`: `q·e_a⊗e_a` if `a = b`; otherwise `e_b⊗e_a`, plus `(q − q⁻¹)·e_a⊗e_b` when `a < b`. -/
def jimboR (q : R) : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R := fun cd ab =>
  if ab.1 = ab.2 then (if cd.1 = ab.1 ∧ cd.2 = ab.2 then q else 0)
  else (if cd.1 = ab.2 ∧ cd.2 = ab.1 then 1 else 0) +
    (if cd.1 = ab.1 ∧ cd.2 = ab.2 ∧ ab.1 < ab.2 then q - q⁻¹ else 0)

set_option maxHeartbeats 2000000 in
/-- **Hecke relation** `(Ř − q)(Ř + q⁻¹) = 0`. (81 entries, each a finite sum; the heartbeat
budget is raised for the case split only.) -/
theorem jimboR_hecke (q : R) (hq : q ≠ 0) :
    (jimboR q - q • (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)) *
      (jimboR q + q⁻¹ • (1 : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R)) = 0 := by
  ext ⟨c, d⟩ ⟨a, b⟩
  simp only [mul_apply, Fintype.sum_prod_type, Fin.sum_univ_three, sub_apply, add_apply,
    smul_apply, one_apply, zero_apply, smul_eq_mul]
  fin_cases c <;> fin_cases d <;> fin_cases a <;> fin_cases b <;>
    simp [jimboR] <;> field_simp <;> ring

/-- The entries `Ř_{(c,b),(a,b)}` that a partial trace over the second factor sees: zero unless
`c = a`. -/
theorem jimboR_diag_col (q : R) (a b c : Fin 3) :
    jimboR q (c, b) (a, b) =
      if c = a then (if a = b then q else if a < b then q - q⁻¹ else 0) else 0 := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [jimboR]

/-! ### The partial trace `P = tr₂((1 ⊗ K) Ř)` -/

/-- `P_{ac} = Σ_b k_b · Ř_{(a,b),(c,b)}`. -/
def twistPartialTrace (q : R) (k : Fin 3 → R) : Matrix (Fin 3) (Fin 3) R :=
  fun a c => ∑ b, k b * jimboR q (a, b) (c, b)

/-- `P` is diagonal, `P_aa = q·k_a + (q − q⁻¹)·Σ_{b > a} k_b`. -/
theorem twistPartialTrace_eq_diagonal (q : R) (k : Fin 3 → R) :
    twistPartialTrace q k =
      diagonal (fun a => q * k a + (q - q⁻¹) * ∑ b, if a < b then k b else 0) := by
  ext a c
  fin_cases a <;> fin_cases c <;>
    simp [twistPartialTrace, jimboR, Fin.sum_univ_three, diagonal] <;> ring

/-- The Markov condition `P·K = s·K` is the pointwise condition `P_aa·k_a = s·k_a`. -/
theorem markov_cond_iff (q : R) (k : Fin 3 → R) (s : R) :
    twistPartialTrace q k * diagonal k = s • diagonal k ↔
      ∀ a, (q * k a + (q - q⁻¹) * ∑ b, if a < b then k b else 0) * k a = s * k a := by
  rw [twistPartialTrace_eq_diagonal, diagonal_mul_diagonal, ← diagonal_smul]
  constructor
  · intro h a
    have := congrFun (congrFun h a) a
    simpa only [diagonal_apply_eq, Pi.smul_apply, smul_eq_mul] using this
  · intro h
    congr 1
    funext a
    simpa only [Pi.smul_apply, smul_eq_mul] using h a

/-- The three pointwise Markov equations, written out. -/
theorem markov_cond_explicit {q : R} {k : Fin 3 → R} {s : R}
    (hM : twistPartialTrace q k * diagonal k = s • diagonal k) :
    (q * k 0 + (q - q⁻¹) * (k 1 + k 2)) * k 0 = s * k 0 ∧
      (q * k 1 + (q - q⁻¹) * k 2) * k 1 = s * k 1 ∧ q * k 2 * k 2 = s * k 2 := by
  have h := (markov_cond_iff q k s).1 hM
  have h0 := h 0
  have h1 := h 1
  have h2 := h 2
  simp only [Fin.sum_univ_three, Fin.isValue, Fin.reduceLT, if_true, if_false,
    lt_self_iff_false] at h0 h1 h2
  exact ⟨by linear_combination h0, by linear_combination h1, by linear_combination h2⟩

/-- Sufficient pointwise form, used for the explicit twists. -/
theorem markov_of_explicit {q : R} {k : Fin 3 → R} {s : R}
    (h0 : (q * k 0 + (q - q⁻¹) * (k 1 + k 2)) * k 0 = s * k 0)
    (h1 : (q * k 1 + (q - q⁻¹) * k 2) * k 1 = s * k 1) (h2 : q * k 2 * k 2 = s * k 2) :
    twistPartialTrace q k * diagonal k = s • diagonal k := by
  rw [markov_cond_iff]
  intro a
  fin_cases a <;>
    simp only [Fin.sum_univ_three, Fin.isValue, Fin.reduceLT, if_true, if_false,
      lt_self_iff_false, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk] <;>
    [linear_combination h0; linear_combination h1; linear_combination h2]

/-! ### The Markov step, for every `n` -/

/-- The diagonal entries of `(x ⊗ 1)·(1 ⊗ Ř)` on `(β × R³) × R³`. -/
theorem kron_mul_diag_entry {β : Type*} [Fintype β] [DecidableEq β] (q : R)
    (x : Matrix (β × Fin 3) (β × Fin 3) R) (u : β) (a b : Fin 3) :
    (kroneckerMap (· * ·) x (1 : Matrix (Fin 3) (Fin 3) R) *
        reindex (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
          (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
          (kroneckerMap (· * ·) (1 : Matrix β β R) (jimboR q))) ((u, a), b) ((u, a), b) =
      x (u, a) (u, a) * (if a = b then q else if a < b then q - q⁻¹ else 0) := by
  simp only [mul_apply, kroneckerMap_apply, reindex_apply, submatrix_apply,
    Equiv.symm_symm, Equiv.prodAssoc_apply, Fintype.sum_prod_type, one_apply]
  simp only [mul_ite, ite_mul, mul_one, mul_zero, one_mul, zero_mul]
  simp only [Finset.sum_ite_irrel, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.sum_const_zero,
    Finset.mem_univ, if_true, jimboR_diag_col, mul_ite, mul_zero]

/-- **Markov step of the colour-twisted trace, all `n`.** If `P·K = s·K`, then for every finite
`β`, every diagonal weight `w` on `β` and every `x` on `β × R³`,
`tr(diag(w ⊗ K ⊗ K)·(x ⊗ 1)·(1 ⊗ Ř)) = s · tr(diag(w ⊗ K)·x)`.
With `β = Fin 3^{n-1}` and `w = K^{⊗(n-1)}` this is `tr_{n+1}(K^{⊗(n+1)}(x ⊗ 1)σ_n) =
s·tr_n(K^{⊗n} x)`. -/
theorem twisted_trace_markov {β : Type*} [Fintype β] [DecidableEq β]
    (q : R) (k : Fin 3 → R) (s : R)
    (hM : twistPartialTrace q k * diagonal k = s • diagonal k)
    (w : β → R) (x : Matrix (β × Fin 3) (β × Fin 3) R) :
    trace (diagonal (fun p : (β × Fin 3) × Fin 3 => w p.1.1 * k p.1.2 * k p.2) *
        (kroneckerMap (· * ·) x (1 : Matrix (Fin 3) (Fin 3) R) *
          reindex (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
            (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
            (kroneckerMap (· * ·) (1 : Matrix β β R) (jimboR q)))) =
      s * trace (diagonal (fun p : β × Fin 3 => w p.1 * k p.2) * x) := by
  simp only [trace, diag, diagonal_mul, kron_mul_diag_entry, Fintype.sum_prod_type]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun u _ => ?_)
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun a _ => ?_)
  have h := (markov_cond_iff q k s).1 hM a
  simp only [Fin.sum_univ_three] at h ⊢
  fin_cases a <;>
    simp only [Fin.isValue, Fin.reduceLT, if_true, if_false, lt_self_iff_false, Fin.zero_eta,
      Fin.mk_one, Fin.reduceFinMk, Fin.reduceEq] at h ⊢ <;>
    linear_combination (w u * x _ _) * h

/-- **Normalised Markov step.** With `c = tr K ≠ 0` and `τ_m(y) = tr(diag(w ⊗ K) y)/c^m`,
`τ_{m+1}((x ⊗ 1)σ) = (s / c)·τ_m(x)`: the Markov parameter is `z = s / tr K`. -/
theorem twisted_trace_markov_normalised {β : Type*} [Fintype β] [DecidableEq β]
    (q : R) (k : Fin 3 → R) (s : R)
    (hM : twistPartialTrace q k * diagonal k = s • diagonal k)
    (w : β → R) (x : Matrix (β × Fin 3) (β × Fin 3) R) (m : ℕ) (hc : ∑ a, k a ≠ 0) :
    trace (diagonal (fun p : (β × Fin 3) × Fin 3 => w p.1.1 * k p.1.2 * k p.2) *
        (kroneckerMap (· * ·) x (1 : Matrix (Fin 3) (Fin 3) R) *
          reindex (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
            (Equiv.prodAssoc β (Fin 3) (Fin 3)).symm
            (kroneckerMap (· * ·) (1 : Matrix β β R) (jimboR q)))) / (∑ a, k a) ^ (m + 1) =
      (s / ∑ a, k a) * (trace (diagonal (fun p : β × Fin 3 => w p.1 * k p.2) * x) /
        (∑ a, k a) ^ m) := by
  rw [twisted_trace_markov q k s hM w x]
  field_simp
  ring

/-! ### The three twists and their parameters -/

/-- Rank-1 twist `(0, 0, 1)`. -/
def twistOne (_q : R) : Fin 3 → R := ![0, 0, 1]

/-- Rank-2 twist with support `{0, 1}`: `(q⁻², 1, 0)`. -/
def twistD (q : R) : Fin 3 → R := ![q⁻¹ ^ 2, 1, 0]

/-- Rank-3 (pivotal) twist `(q⁻⁴, q⁻², 1)`. -/
def twistPivotal (q : R) : Fin 3 → R := ![q⁻¹ ^ 4, q⁻¹ ^ 2, 1]

@[simp] theorem twistOne_apply (q : R) :
    twistOne q 0 = 0 ∧ twistOne q 1 = 0 ∧ twistOne q 2 = 1 := ⟨rfl, rfl, rfl⟩
@[simp] theorem twistD_apply (q : R) :
    twistD q 0 = q⁻¹ ^ 2 ∧ twistD q 1 = 1 ∧ twistD q 2 = 0 := ⟨rfl, rfl, rfl⟩
@[simp] theorem twistPivotal_apply (q : R) :
    twistPivotal q 0 = q⁻¹ ^ 4 ∧ twistPivotal q 1 = q⁻¹ ^ 2 ∧ twistPivotal q 2 = 1 :=
  ⟨rfl, rfl, rfl⟩

theorem twistOne_markov (q : R) :
    twistPartialTrace q (twistOne q) * diagonal (twistOne q) = q • diagonal (twistOne q) := by
  obtain ⟨h0, h1, h2⟩ := twistOne_apply q
  exact markov_of_explicit (by rw [h0]; ring) (by rw [h1]; ring) (by rw [h2]; ring)

theorem twistD_markov (q : R) (hq : q ≠ 0) :
    twistPartialTrace q (twistD q) * diagonal (twistD q) = q • diagonal (twistD q) := by
  obtain ⟨h0, h1, h2⟩ := twistD_apply q
  exact markov_of_explicit (by rw [h0, h1, h2]; field_simp; ring) (by rw [h1, h2]; ring)
    (by rw [h2]; ring)

theorem twistPivotal_markov (q : R) (hq : q ≠ 0) :
    twistPartialTrace q (twistPivotal q) * diagonal (twistPivotal q) =
      q • diagonal (twistPivotal q) := by
  obtain ⟨h0, h1, h2⟩ := twistPivotal_apply q
  exact markov_of_explicit (by rw [h0, h1, h2]; field_simp; ring)
    (by rw [h1, h2]; field_simp; ring) (by rw [h2]; ring)

/-! ### Classification: the rank of `K` fixes `z = s / tr K` -/

/-- Common core of the rank-2 cases: `s = q·b`, `q²·a = b`, `b ≠ 0`, `tr K = a + b`. -/
theorem zD_of_core {q a b s t : R} (h2 : q ^ 2 + 1 ≠ 0)
    (hs : q * b = s) (hB : q ^ 2 * a = b) (hb : b ≠ 0) (ht : t = a + b) :
    s / t = q ^ 3 / (q ^ 2 + 1) := by
  have hden : t ≠ 0 := by
    intro h0
    apply mul_ne_zero hb h2
    linear_combination q ^ 2 * h0 - q ^ 2 * ht - hB
  rw [div_eq_div_iff hden h2]
  linear_combination -(q ^ 2 + 1) * hs - q * hB - q ^ 3 * ht

/-- Exactly two nonzero entries. -/
def IsRankTwo (k : Fin 3 → R) : Prop :=
  (k 0 = 0 ∧ k 1 ≠ 0 ∧ k 2 ≠ 0) ∨ (k 0 ≠ 0 ∧ k 1 = 0 ∧ k 2 ≠ 0) ∨
    (k 0 ≠ 0 ∧ k 1 ≠ 0 ∧ k 2 = 0)

/-- **Rank 2 ⇒ `z = z_D = q³/(q²+1)`**, for each of the three supports. -/
theorem z_of_rank_two (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (k : Fin 3 → R) (s : R)
    (hM : twistPartialTrace q k * diagonal k = s • diagonal k) (hk : IsRankTwo k) :
    s / ∑ a, k a = q ^ 3 / (q ^ 2 + 1) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  obtain ⟨e0, e1, e2⟩ := markov_cond_explicit hM
  rw [Fin.sum_univ_three]
  rcases hk with ⟨z0, n1, n2⟩ | ⟨n0, z1, n2⟩ | ⟨n0, n1, z2⟩
  · have hs : q * k 2 = s := mul_right_cancel₀ n2 (by linear_combination e2)
    have A : q * k 1 + (q - q⁻¹) * k 2 = s := mul_right_cancel₀ n1 (by linear_combination e1)
    exact zD_of_core (a := k 1) (b := k 2) h2 hs
      (by linear_combination q * A - q * hs + k 2 * hqi) n2
      (by rw [z0]; ring)
  · have hs : q * k 2 = s := mul_right_cancel₀ n2 (by linear_combination e2)
    have A : q * k 0 + (q - q⁻¹) * (k 1 + k 2) = s :=
      mul_right_cancel₀ n0 (by linear_combination e0)
    exact zD_of_core (a := k 0) (b := k 2) h2 hs
      (by linear_combination q * A - q * hs + k 2 * hqi - (q ^ 2 - 1) * z1 + k 1 * hqi) n2
      (by rw [z1]; ring)
  · have A1 : q * k 1 + (q - q⁻¹) * k 2 = s := mul_right_cancel₀ n1 (by linear_combination e1)
    have hs : q * k 1 = s := by linear_combination A1 - (q - q⁻¹) * z2
    have A : q * k 0 + (q - q⁻¹) * (k 1 + k 2) = s :=
      mul_right_cancel₀ n0 (by linear_combination e0)
    exact zD_of_core (a := k 0) (b := k 1) h2 hs
      (by linear_combination q * A - q * hs + k 1 * hqi - (q ^ 2 - 1) * z2 + k 2 * hqi) n1
      (by rw [z2]; ring)

/-- **Rank 3 ⇒ `z = z₃ = q⁵/(q⁴+q²+1) = q³/[3]_q`**, and the twist is forced to be
`k₂·(q⁻⁴, q⁻², 1)`. -/
theorem z_of_rank_three (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (k : Fin 3 → R)
    (s : R) (hM : twistPartialTrace q k * diagonal k = s • diagonal k)
    (n0 : k 0 ≠ 0) (n1 : k 1 ≠ 0) (n2 : k 2 ≠ 0) :
    q ^ 2 * k 0 = k 1 ∧ q ^ 2 * k 1 = k 2 ∧ s / ∑ a, k a = q ^ 5 / (q ^ 4 + q ^ 2 + 1) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  obtain ⟨e0, e1, e2⟩ := markov_cond_explicit hM
  have hs : q * k 2 = s := mul_right_cancel₀ n2 (by linear_combination e2)
  have A1 : q * k 1 + (q - q⁻¹) * k 2 = s := mul_right_cancel₀ n1 (by linear_combination e1)
  have A0 : q * k 0 + (q - q⁻¹) * (k 1 + k 2) = s :=
    mul_right_cancel₀ n0 (by linear_combination e0)
  have B : q ^ 2 * k 1 = k 2 := by linear_combination q * A1 - q * hs + k 2 * hqi
  have C : q ^ 2 * k 0 = k 1 := by
    linear_combination q * A0 - q * hs - B + (k 1 + k 2) * hqi
  refine ⟨C, B, ?_⟩
  rw [Fin.sum_univ_three]
  have hden : k 0 + k 1 + k 2 ≠ 0 := by
    intro h0
    apply mul_ne_zero n2 h3
    linear_combination q ^ 4 * h0 - q ^ 2 * C - (q ^ 2 + 1) * B
  rw [div_eq_div_iff hden h3]
  linear_combination -(q ^ 4 + q ^ 2 + 1) * hs - q ^ 3 * C - (q + q ^ 3) * B

/-- **Rank 1 ⇒ `z = q`**, for each of the three supports. -/
theorem z_of_rank_one (q : R) (k : Fin 3 → R) (s : R)
    (hM : twistPartialTrace q k * diagonal k = s • diagonal k)
    (hk : (k 0 ≠ 0 ∧ k 1 = 0 ∧ k 2 = 0) ∨ (k 0 = 0 ∧ k 1 ≠ 0 ∧ k 2 = 0) ∨
      (k 0 = 0 ∧ k 1 = 0 ∧ k 2 ≠ 0)) :
    s / ∑ a, k a = q := by
  obtain ⟨e0, e1, e2⟩ := markov_cond_explicit hM
  rw [Fin.sum_univ_three]
  rcases hk with ⟨n0, z1, z2⟩ | ⟨z0, n1, z2⟩ | ⟨z0, z1, n2⟩
  · have hs : q * k 0 = s := mul_right_cancel₀ n0 (by rw [z1, z2] at e0; linear_combination e0)
    rw [z1, z2, add_zero, add_zero, ← hs, mul_div_assoc, div_self n0, mul_one]
  · have hs : q * k 1 = s := mul_right_cancel₀ n1 (by rw [z2] at e1; linear_combination e1)
    rw [z0, z2, zero_add, add_zero, ← hs, mul_div_assoc, div_self n1, mul_one]
  · have hs : q * k 2 = s := mul_right_cancel₀ n2 (by linear_combination e2)
    rw [z0, z1, zero_add, zero_add, ← hs, mul_div_assoc, div_self n2, mul_one]

/-- The explicit twists realise the three values. -/
theorem twistD_z (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q / ∑ a, twistD q a = q ^ 3 / (q ^ 2 + 1) :=
  z_of_rank_two q hq h2 _ _ (twistD_markov q hq)
    (Or.inr (Or.inr ⟨by simp [hq], by simp, by simp⟩))

theorem twistPivotal_z (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q / ∑ a, twistPivotal q a = q ^ 5 / (q ^ 4 + q ^ 2 + 1) :=
  (z_of_rank_three q hq h3 _ _ (twistPivotal_markov q hq) (by simp [hq]) (by simp [hq])
    (by simp)).2.2

theorem twistOne_z (q : R) : q / ∑ a, twistOne q a = q :=
  z_of_rank_one q _ _ (twistOne_markov q) (Or.inr (Or.inr ⟨by simp, by simp, by simp⟩))

/-! ### Connection to convention D -/

/-- `z_D = q³/(q²+1)` satisfies the convention-D pin `z·(q + q⁻¹) = q²`. -/
theorem zD_mul_two (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) * (q + q⁻¹) = q ^ 2 := by
  field_simp

/-- `z₃ ≠ z_D` whenever `q ≠ 0`. -/
theorem z3_ne_zD (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q ^ 5 / (q ^ 4 + q ^ 2 + 1) ≠ q ^ 3 / (q ^ 2 + 1) := by
  intro h
  rw [div_eq_div_iff h3 h2] at h
  have : q ^ 3 = 0 := by linear_combination -h
  exact hq (pow_eq_zero_iff (by norm_num) |>.mp this)

/-- **The rank-2 colour twist is convention D.** For every rank-2 diagonal twist satisfying the
Markov condition, its parameter `z = s / tr K` obeys the convention-D pin `z·(q + q⁻¹) = q²`,
and the Ocneanu weight at that `z` vanishes on every Young diagram with three or more rows
(composition with `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`).

Scope: this identifies the *parameter*. That the twisted functional's own Wedderburn weights are
the Ocneanu weights at that parameter is Ocneanu uniqueness, not proved here. -/
theorem rank_two_twist_conventionD (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (k : Fin 3 → R) (s : R) (hM : twistPartialTrace q k * diagonal k = s • diagonal k)
    (hk : IsRankTwo k) :
    (s / ∑ a, k a) * (q + q⁻¹) = q ^ 2 ∧
      ∀ mu : YoungDiagram, 0 < mu.rowLen 2 →
        QOU.SchurWeyl.ocneanuWeight q (s / ∑ a, k a) mu = 0 := by
  rw [z_of_rank_two q hq h2 k s hM hk]
  exact ⟨zD_mul_two q hq h2,
    fun mu h => QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows q h2 mu h⟩

/-! ### Colour invariance: the invariant twist is the pivotal one, hence invertible -/

/-- Fundamental-representation generators of `U_q(gl₃)` (as in the probe). -/
def E₁ : Matrix (Fin 3) (Fin 3) R := single 0 1 1
def E₂ : Matrix (Fin 3) (Fin 3) R := single 1 2 1
def F₁ : Matrix (Fin 3) (Fin 3) R := single 1 0 1
def F₂ : Matrix (Fin 3) (Fin 3) R := single 2 1 1
def K₁ (q : R) : Matrix (Fin 3) (Fin 3) R := diagonal ![q, q⁻¹, 1]
def K₁i (q : R) : Matrix (Fin 3) (Fin 3) R := diagonal ![q⁻¹, q, 1]
def K₂ (q : R) : Matrix (Fin 3) (Fin 3) R := diagonal ![1, q, q⁻¹]
def K₂i (q : R) : Matrix (Fin 3) (Fin 3) R := diagonal ![1, q⁻¹, q]

/-- Adjoint actions (coproduct variant B of the probe: `ΔE = E⊗1 + K⊗E`, `ΔF = F⊗K⁻¹ + 1⊗F`,
antipode `S(E) = −K⁻¹E`, `S(F) = −FK`). -/
def adE (E K Ki : Matrix (Fin 3) (Fin 3) R) (y : Matrix (Fin 3) (Fin 3) R) :
    Matrix (Fin 3) (Fin 3) R := E * y - K * y * (Ki * E)
def adF (F K : Matrix (Fin 3) (Fin 3) R) (y : Matrix (Fin 3) (Fin 3) R) :
    Matrix (Fin 3) (Fin 3) R := F * y * K - y * (F * K)

/-- **An `E₁,E₂`-invariant diagonal functional is a multiple of the pivotal twist.** If
`tr(diag(m)·ad_{E_i}(y)) = 0` for all `y` and `i = 1, 2`, then `m = m₂·(q⁻⁴, q⁻², 1)`. -/
theorem invariant_twist_eq (q : R) (m : Fin 3 → R)
    (h1 : ∀ y, trace (diagonal m * adE E₁ (K₁ q) (K₁i q) y) = 0)
    (h2 : ∀ y, trace (diagonal m * adE E₂ (K₂ q) (K₂i q) y) = 0) :
    m 0 = q⁻¹ ^ 4 * m 2 ∧ m 1 = q⁻¹ ^ 2 * m 2 := by
  have a := h1 F₁
  have b := h2 F₂
  simp [adE, E₁, E₂, F₁, F₂, K₁, K₁i, K₂, K₂i, trace, mul_apply, Fin.sum_univ_three,
    diagonal, single] at a b
  refine ⟨?_, ?_⟩
  · linear_combination a + q⁻¹ ^ 2 * b
  · linear_combination b

/-- A nonzero `E₁,E₂`-invariant diagonal twist is invertible. -/
theorem invariant_twist_invertible (q : R) (hq : q ≠ 0) (m : Fin 3 → R)
    (h1 : ∀ y, trace (diagonal m * adE E₁ (K₁ q) (K₁i q) y) = 0)
    (h2 : ∀ y, trace (diagonal m * adE E₂ (K₂ q) (K₂i q) y) = 0) (hm : m ≠ 0) :
    ∀ a, m a ≠ 0 := by
  obtain ⟨e0, e1⟩ := invariant_twist_eq q m h1 h2
  have n2 : m 2 ≠ 0 := by
    intro z2
    apply hm
    funext a
    fin_cases a
    · simp [e0, z2]
    · simp [e1, z2]
    · simpa using z2
  intro a
  fin_cases a
  · simp [e0, hq, n2]
  · simp [e1, hq, n2]
  · simpa using n2

/-- **No colour-invariant twist is rank 2.** -/
theorem invariant_twist_not_rank_two (q : R) (hq : q ≠ 0) (m : Fin 3 → R)
    (h1 : ∀ y, trace (diagonal m * adE E₁ (K₁ q) (K₁i q) y) = 0)
    (h2 : ∀ y, trace (diagonal m * adE E₂ (K₂ q) (K₂i q) y) = 0) :
    ¬ IsRankTwo m := by
  intro hk
  have hm : m ≠ 0 := by
    intro h0
    rcases hk with ⟨_, n, _⟩ | ⟨n, _, _⟩ | ⟨n, _, _⟩ <;> exact n (by simp [h0])
  have := invariant_twist_invertible q hq m h1 h2 hm
  rcases hk with ⟨z, _, _⟩ | ⟨_, z, _⟩ | ⟨_, _, z⟩
  · exact this 0 z
  · exact this 1 z
  · exact this 2 z

/-- **A nonzero colour-invariant Markov twist gives `z₃`, never `z_D`.** -/
theorem invariant_markov_z_ne_zD (q : R) (hq : q ≠ 0) (h2q : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (m : Fin 3 → R) (s : R)
    (h1 : ∀ y, trace (diagonal m * adE E₁ (K₁ q) (K₁i q) y) = 0)
    (h2 : ∀ y, trace (diagonal m * adE E₂ (K₂ q) (K₂i q) y) = 0) (hm : m ≠ 0)
    (hM : twistPartialTrace q m * diagonal m = s • diagonal m) :
    s / ∑ a, m a = q ^ 5 / (q ^ 4 + q ^ 2 + 1) ∧ s / ∑ a, m a ≠ q ^ 3 / (q ^ 2 + 1) := by
  have hinv := invariant_twist_invertible q hq m h1 h2 hm
  have hz := (z_of_rank_three q hq h3 m s hM (hinv 0) (hinv 1) (hinv 2)).2.2
  exact ⟨hz, hz ▸ z3_ne_zD q hq h2q h3⟩

/-- **Existence:** the pivotal twist `(q⁻⁴, q⁻², 1)` is invariant under `E₁, E₂, F₁, F₂` and
under conjugation by `K₁, K₂`. -/
theorem pivotal_twist_invariant (q : R) (hq : q ≠ 0) (y : Matrix (Fin 3) (Fin 3) R) :
    trace (diagonal (twistPivotal q) * adE E₁ (K₁ q) (K₁i q) y) = 0 ∧
    trace (diagonal (twistPivotal q) * adE E₂ (K₂ q) (K₂i q) y) = 0 ∧
    trace (diagonal (twistPivotal q) * adF F₁ (K₁ q) y) = 0 ∧
    trace (diagonal (twistPivotal q) * adF F₂ (K₂ q) y) = 0 ∧
    trace (diagonal (twistPivotal q) * (K₁ q * y * K₁i q - y)) = 0 ∧
    trace (diagonal (twistPivotal q) * (K₂ q * y * K₂i q - y)) = 0 := by
  obtain ⟨t0, t1, t2⟩ := twistPivotal_apply q
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [adE, adF, E₁, E₂, F₁, F₂, K₁, K₁i, K₂, K₂i, trace, mul_apply, Fin.sum_univ_three,
      diagonal, single, t0, t1, t2] <;> field_simp <;> ring

end QOU.Braiding.ColourTwist
