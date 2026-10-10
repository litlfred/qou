import QOU.Mathlib.RSSYTSchur
import QOU.SchurWeyl.SchurPrincipalBetaForm

/-!
# QOU.Mathlib.PrincipalSchurHook — the branching Schur polynomial at `x_i = Qⁱ`

`Bialternant.alt_add_stair` gives `a_{ν+δ} = a_δ · s_ν` for the branching Schur polynomial, and
`RSSYTSchur.bsum_eq_schur` identifies `s_ν` with the sum over reverse tableaux with entries `< N`.
This file evaluates at the principal point `x_i = Qⁱ`.  There the alternant is a Vandermonde, and
the corpus Frame–Robinson–Thrall identity `SchurWeyl.hookSide_betaR` turns it into hooks:

| | |
|---|---|
| `alt_pow` | `a_α(1, Q, …, Q^{N−1}) = ∏_{a<b} (Q^{α_b} − Q^{α_a})` |
| `prod_Ioi_eq_prod_pairs` | a `Fin N` pair product as a product over `{(i,j) : i < j < N}` |
| `alt_principal` | `a_{α^μ}(Qⁱ) = M · Q^{e(μ)} · ∏_{i<j<N} (1 − Q^{β_i − β_j})`, `M` independent of `μ` |
| `hook_mul_schur_principal` | **`∏_c (1 − Q^{h(c)}) · s_μ(1, …, Q^{N−1}) = Q^{e(μ)} · ∏_{i<N} ∏_{t<μ_i} (1 − Q^{N−i+t})`** |

Here `α^μ_j = μ_{N−1−j} + j`, `β_i = μ_i + (N−1−i)` (so `α^μ_j = β_{N−1−j}`), and
`e(μ) = ∑_{j<N} j · μ_j`.

The last row is the hook-content formula for the principal specialisation, division-free.  Its
only hypotheses are that `Q` is not zero and no `1 − Q^k` (`k ≥ 1`) vanishes, in a domain — they are
used to cancel the `μ`-independent factor `M · ∏_{i<N} (Q;Q)_{N−1−i}` that the empty diagram
contributes.

## Base ring (§7c)

Generic `[CommRing R]`; the cancellation step adds `[IsDomain R]`.  No `ℝ`, no ordering.

LaTeX label: `lem:principal-schur-hook`
-/

namespace QOU.Mathlib.PrincipalSchur

open Finset YoungDiagram QOU.Mathlib.Bialternant QOU.Mathlib.RSSYTSchur QOU.Mathlib.SYTBeta

variable {R : Type*} [CommRing R]

/-! ## Pair products -/

/-- The pairs `i < j < N`. -/
def pairs (N : ℕ) : Finset (ℕ × ℕ) := (range N ×ˢ range N).filter (fun p => p.1 < p.2)

theorem mem_pairs {N : ℕ} {p : ℕ × ℕ} : p ∈ pairs N ↔ p.1 < p.2 ∧ p.2 < N := by
  unfold pairs
  simp only [mem_filter, mem_product, mem_range]
  omega

/-- The corpus spelling of a pair product, `∏_{i<N} ∏_{k<N−(i+1)} g(i, i+1+k)`. -/
theorem prod_range_eq_prod_pairs {M : Type*} [CommMonoid M] (N : ℕ) (g : ℕ → ℕ → M) :
    ∏ i ∈ range N, ∏ k ∈ range (N - (i + 1)), g i (i + 1 + k) = ∏ p ∈ pairs N, g p.1 p.2 := by
  unfold pairs
  rw [prod_filter, prod_product]
  refine prod_congr rfl fun i hi => ?_
  rw [← prod_filter, ← prod_Ico_eq_prod_range]
  congr 1
  ext j
  simp only [mem_Ico, mem_filter, mem_range]
  rw [mem_range] at hi
  omega

/-- A `Fin N` pair product over `Ioi`, as a product over `pairs N`. -/
theorem prod_Ioi_eq_prod_pairs {M : Type*} [CommMonoid M] (N : ℕ) (g : ℕ → ℕ → M) :
    ∏ i : Fin N, ∏ j ∈ Ioi i, g i j = ∏ p ∈ pairs N, g p.1 p.2 := by
  rw [← prod_range_eq_prod_pairs]
  have h1 : ∀ i : Fin N, ∏ j ∈ Ioi i, g i j
      = ∏ j ∈ range N, (if (i : ℕ) < j then g i j else 1) := by
    intro i
    rw [← Fin.prod_univ_eq_prod_range (fun j => if (i : ℕ) < j then g i j else 1) N,
      ← prod_filter]
    congr 1
    ext j
    simp only [mem_Ioi, mem_filter, mem_univ, true_and, Fin.lt_def]
  simp_rw [h1]
  rw [Fin.prod_univ_eq_prod_range (fun i => ∏ j ∈ range N, (if i < j then g i j else 1)) N]
  refine prod_congr rfl fun i hi => ?_
  rw [← prod_filter, ← prod_Ico_eq_prod_range]
  congr 1
  ext j
  simp only [mem_Ico, mem_filter, mem_range]
  rw [mem_range] at hi
  omega

/-- Reversing both indices, `(i, j) ↦ (N−1−j, N−1−i)`, permutes the pairs. -/
theorem prod_pairs_reverse {M : Type*} [CommMonoid M] (N : ℕ) (g : ℕ → ℕ → M) :
    ∏ p ∈ pairs N, g p.1 p.2 = ∏ p ∈ pairs N, g (N - 1 - p.2) (N - 1 - p.1) := by
  refine prod_nbij' (fun p => (N - 1 - p.2, N - 1 - p.1)) (fun p => (N - 1 - p.2, N - 1 - p.1))
    ?_ ?_ ?_ ?_ ?_
  · intro p hp
    rw [mem_pairs] at hp ⊢
    simp only
    omega
  · intro p hp
    rw [mem_pairs] at hp ⊢
    simp only
    omega
  · intro p hp
    rw [mem_pairs] at hp
    ext <;> simp only <;> omega
  · intro p hp
    rw [mem_pairs] at hp
    ext <;> simp only <;> omega
  · intro p hp
    rw [mem_pairs] at hp
    dsimp only
    congr 1 <;> omega

/-- A pair product depending only on the larger index is a power product. -/
theorem prod_pairs_snd {M : Type*} [CommMonoid M] (N : ℕ) (c : ℕ → M) :
    ∏ p ∈ pairs N, c p.2 = ∏ j ∈ range N, c j ^ j := by
  unfold pairs
  rw [prod_filter, prod_product_right]
  refine prod_congr rfl fun j hj => ?_
  rw [← prod_filter]
  dsimp only
  rw [prod_const]
  congr 1
  rw [mem_range] at hj
  have : (range N).filter (fun i => i < j) = range j := by
    ext i
    simp only [mem_filter, mem_range]
    omega
  rw [this, card_range]

/-! ## The alternant at the principal point -/

/-- **The alternant at `x_i = Qⁱ` is a Vandermonde.** -/
theorem alt_pow {N : ℕ} (Q : R) (α : Fin N → ℕ) :
    alt (fun i : Fin N => Q ^ (i : ℕ)) α = ∏ i : Fin N, ∏ j ∈ Ioi i, (Q ^ α j - Q ^ α i) := by
  rw [← Matrix.det_vandermonde, ← Matrix.det_transpose, alt]
  congr 1
  ext i j
  simp only [Matrix.of_apply, Matrix.transpose_apply, Matrix.vandermonde_apply, ← pow_mul,
    mul_comm]

/-- `e(μ) = ∑_{j<N} j · μ_j`, the exponent the principal specialisation carries. -/
def eExp (N : ℕ) (μ : YoungDiagram) : ℕ := ∑ j ∈ range N, j * μ.rowLen j

/-- **The alternant at the principal point, factored.**

`a_{α^μ}(1, Q, …, Q^{N−1}) = C_N · Q^{e(μ)} · ∏_{i<j<N} (1 − Q^{β_i − β_j})`, with
`C_N = ∏_{j<N} (−Q^{N−1−j})^j` independent of `μ`. -/
theorem alt_principal (Q : R) (N : ℕ) (μ : YoungDiagram) :
    alt (fun i : Fin N => Q ^ (i : ℕ)) (fun j => seq N μ j + stair N j)
      = (∏ j ∈ range N, (-Q ^ (N - 1 - j)) ^ j) * Q ^ eExp N μ *
        ∏ i ∈ range N, ∏ k ∈ range (N - (i + 1)),
          (1 - Q ^ (SchurWeyl.betaR N μ i - SchurWeyl.betaR N μ (i + 1 + k))) := by
  rw [alt_pow]
  refine (prod_Ioi_eq_prod_pairs N (fun a b =>
    Q ^ (μ.rowLen (N - 1 - b) + b) - Q ^ (μ.rowLen (N - 1 - a) + a))).trans ?_
  rw [prod_pairs_reverse N (fun a b =>
      Q ^ (μ.rowLen (N - 1 - b) + b) - Q ^ (μ.rowLen (N - 1 - a) + a)),
    prod_range_eq_prod_pairs N (fun i j => 1 - Q ^ (SchurWeyl.betaR N μ i - SchurWeyl.betaR N μ j)),
    ← prod_pairs_snd N (fun j => -Q ^ (N - 1 - j))]
  have h2 : Q ^ eExp N μ = ∏ p ∈ pairs N, Q ^ μ.rowLen p.2 := by
    rw [prod_pairs_snd N (fun j => Q ^ μ.rowLen j), eExp, ← prod_pow_eq_pow_sum]
    exact prod_congr rfl fun j _ => by rw [← pow_mul, mul_comm]
  rw [h2, ← prod_mul_distrib, ← prod_mul_distrib]
  refine prod_congr rfl fun p hp => ?_
  rw [mem_pairs] at hp
  have hlt := SchurWeyl.betaR_lt (μ := μ) hp.1 hp.2
  have e1 : μ.rowLen (N - 1 - (N - 1 - p.1)) + (N - 1 - p.1) = SchurWeyl.betaR N μ p.1 := by
    rw [SchurWeyl.betaR, show N - 1 - (N - 1 - p.1) = p.1 by omega]
  have e2 : μ.rowLen (N - 1 - (N - 1 - p.2)) + (N - 1 - p.2) = SchurWeyl.betaR N μ p.2 := by
    rw [SchurWeyl.betaR, show N - 1 - (N - 1 - p.2) = p.2 by omega]
  rw [e1, e2, show Q ^ SchurWeyl.betaR N μ p.1 = Q ^ μ.rowLen p.2 * Q ^ (N - 1 - p.2) *
      Q ^ (SchurWeyl.betaR N μ p.1 - SchurWeyl.betaR N μ p.2) by
    rw [← pow_add, ← pow_add]; congr 1; unfold SchurWeyl.betaR at hlt ⊢; omega,
    show Q ^ SchurWeyl.betaR N μ p.2 = Q ^ μ.rowLen p.2 * Q ^ (N - 1 - p.2) by
    rw [← pow_add]; rfl]
  ring

/-- `descFactF f (a + b) = descFactF f a · ∏_{t<b} f(a+1+t)`. -/
theorem descFactF_add {M : Type*} [CommMonoid M] (f : ℕ → M) (a b : ℕ) :
    descFactF f (a + b) = descFactF f a * ∏ t ∈ range b, f (a + 1 + t) := by
  induction b with
  | zero => simp
  | succ b ih =>
    rw [← add_assoc, descFactF_succ, ih, prod_range_succ, show a + b + 1 = a + 1 + b by omega]
    ac_rfl

theorem rowLen_bot (i : ℕ) : (⊥ : YoungDiagram).rowLen i = 0 := by
  by_contra h
  have := (mem_iff_lt_rowLen (μ := ⊥) (i := i) (j := 0)).2 (Nat.pos_of_ne_zero h)
  simp at this

/-- **The hook-content formula at the principal point, division-free.**

`∏_c (1 − Q^{h(c)}) · s_μ(1, Q, …, Q^{N−1}) = Q^{e(μ)} · ∏_{i<N} ∏_{t<μ_i} (1 − Q^{N−i+t})`. -/
theorem hook_mul_schur_principal [IsDomain R] (Q : R) (hQ : Q ≠ 0)
    (hQk : ∀ k : ℕ, 0 < k → 1 - Q ^ k ≠ 0) (N : ℕ) (μ : YoungDiagram)
    (hμ : μ.colLen 0 ≤ N) :
    (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) *
        schur N (seq N μ) (fun i : Fin N => Q ^ (i : ℕ))
      = Q ^ eExp N μ * ∏ i ∈ range N, ∏ t ∈ range (μ.rowLen i), (1 - Q ^ (N - i + t)) := by
  set f : ℕ → R := fun n => 1 - Q ^ n with hf
  set x : Fin N → R := fun i => Q ^ (i : ℕ) with hx
  set C : R := ∏ j ∈ range N, (-Q ^ (N - 1 - j)) ^ j with hC
  set D0 : R := ∏ i ∈ range N, descFactF f (N - 1 - i) with hD0
  set E : R := ∏ i ∈ range N, ∏ t ∈ range (μ.rowLen i), (1 - Q ^ (N - i + t)) with hE
  set H : R := ∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c) with hH
  set Pμ : R := ∏ i ∈ range N, ∏ k ∈ range (N - (i + 1)),
    (1 - Q ^ (SchurWeyl.betaR N μ i - SchurWeyl.betaR N μ (i + 1 + k))) with hPμ
  set P0 : R := ∏ i ∈ range N, ∏ k ∈ range (N - (i + 1)),
    (1 - Q ^ (SchurWeyl.betaR N ⊥ i - SchurWeyl.betaR N ⊥ (i + 1 + k))) with hP0
  set s : R := schur N (seq N μ) x with hs
  have hb := alt_add_stair N (seq N μ) (seq_monotone N μ) x
  have hP := alt_principal Q N μ
  have hstair : alt x (stair N) = alt x (fun j => seq N ⊥ j + stair N j) := by
    congr 1
    funext j
    simp [seq, rowLen_bot]
  have hP0' := alt_principal Q N ⊥
  have heb : eExp N ⊥ = 0 := by simp [eExp, rowLen_bot]
  rw [heb, pow_zero, mul_one] at hP0'
  have hbot : (⊥ : YoungDiagram).colLen 0 ≤ N := by
    have : (⊥ : YoungDiagram).colLen 0 = 0 := by
      by_contra h
      have := (YoungDiagram.mem_iff_lt_colLen (μ := ⊥) (i := 0) (j := 0)).2 (Nat.pos_of_ne_zero h)
      simp at this
    omega
  have hH0 := SchurWeyl.hookSide_betaR f hbot
  rw [YoungDiagram.cells_bot, prod_empty, one_mul] at hH0
  have hH0' : P0 = D0 := by
    rw [hP0, hH0, hD0]
    refine prod_congr rfl fun i _ => ?_
    rw [SchurWeyl.betaR, rowLen_bot, zero_add]
  have hHμ := SchurWeyl.hookSide_betaR f hμ
  have hHμ' : H * Pμ = D0 * E := by
    rw [hH, hPμ, hHμ, hD0, hE, ← prod_mul_distrib]
    refine prod_congr rfl fun i hi => ?_
    rw [SchurWeyl.betaR, add_comm, descFactF_add]
    congr 1
    refine prod_congr rfl fun t ht => ?_
    rw [mem_range] at hi
    show 1 - Q ^ (N - 1 - i + 1 + t) = 1 - Q ^ (N - i + t)
    congr 2
    omega
  have hC0 : C ≠ 0 :=
    prod_ne_zero_iff.2 fun j _ => pow_ne_zero _ (neg_ne_zero.2 (pow_ne_zero _ hQ))
  have hD00 : D0 ≠ 0 := by
    refine prod_ne_zero_iff.2 fun i _ => ?_
    unfold descFactF
    refine prod_ne_zero_iff.2 fun j hj => hQk _ ?_
    rw [mem_range] at hj
    omega
  rw [← hstair] at hP0'
  have key : C * D0 * (H * s) = C * D0 * (Q ^ eExp N μ * E) := by
    linear_combination (-(C * H * s)) * hH0' + (-(H * s)) * hP0' + (-H) * hb + H * hP
      + (C * Q ^ eExp N μ) * hHμ'
  exact mul_left_cancel₀ (mul_ne_zero hC0 hD00) key

/-- **The same, for the bounded tableau sum.**  Reverse semistandard tableaux of shape `μ` with
entries `< N`, weighted by `Q^{|T|}`. -/
theorem hook_mul_bsum_principal [IsDomain R] (Q : R) (hQ : Q ≠ 0)
    (hQk : ∀ k : ℕ, 0 < k → 1 - Q ^ k ≠ 0) (N : ℕ) (μ : YoungDiagram)
    (hμ : μ.colLen 0 ≤ N) :
    (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) *
        bsum μ N (fun i : Fin N => Q ^ (i : ℕ))
      = Q ^ eExp N μ * ∏ i ∈ range N, ∏ t ∈ range (μ.rowLen i), (1 - Q ^ (N - i + t)) := by
  rw [bsum_eq_schur N μ hμ]
  exact hook_mul_schur_principal Q hQ hQk N μ hμ

end QOU.Mathlib.PrincipalSchur
