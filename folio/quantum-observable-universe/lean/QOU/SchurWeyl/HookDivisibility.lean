import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import QOU.SchurWeyl.HeckeSchurElements

/-!
# QOU.SchurWeyl.HookDivisibility — the Schur element divides the `q`-factorial

For a Young diagram `μ` with `n` cells, the Schur element of `H_n(Q)` is
`c_λ = Q^{−n(λ)} ∏_{x ∈ μ} [h(x)]_Q` (`HeckeSchurElements.schurElt_eq`). This file proves, sorry-free,
that `[n]_Q! / c_λ` is `Q^{n(λ)}` times an **integer polynomial** in `Q`:

* `hookProd_dvd_qFactorial` — `∏_{x ∈ μ} [h(x)] ∣ ∏_{m=1}^{n} [m]` in `R[X]`, any commutative ring `R`.
* `exists_qFactorial_eq_schurElt_mul` — `[n]_Q! = c_λ(Q) · Q^{n(λ)} · P(Q)` with `P ∈ ℤ[X]`, in every
  field, for `Q ≠ 0, 1`.

## Route

`[m] = ∏_{d ∣ m, d ≥ 2} Φ_d` (Mathlib `prod_cyclotomic_eq_geom_sum`), so `Φ_d` occurs
`#{x : d ∣ h(x)}` times in the hook product and `⌊n/d⌋` times in `[n]!`. The divisibility therefore
reduces to the classical hook inequality

```text
  d · #{x ∈ μ : d ∣ h(x)}  ≤  |μ|        (every d ≥ 1)          -- mul_card_filter_dvd_hook_le
```

proved here with beta-sets (James's abacus). Row `i` gets the bead `β_i = λ_i + (r − 1 − i)`; the
column positions `j + r − λ'_j` are exactly the gaps below `β_i` (`image_cval_row`), and the hook of
cell `(i, j)` is `β_i − (j + r − λ'_j)` (`hook_eq`). So `#{x : d ∣ h(x)} = W_d(B)`, the number of
(bead, lower gap) pairs on a common `d`-runner (`card_filter_dvd_hook`), and `|μ| = W_1(B)`. The
inequality `d · W_d(B) ≤ W_1(B)` (`mul_weight_le`) is elementary: `W_d + P_d = Σ_b ⌊b/d⌋`
(`P_d` = bead pairs on a runner), and `b ↦ (b mod d) + d · (rank of b on its runner)` is injective
(`abacus_injOn`), so `Σ (b mod d) + d · P_d ≥ C(|B|, 2) ≥ P_1`.

## Nonnegativity (proved elsewhere)

That `P` has **nonnegative** coefficients — the fake-degree / `maj` formula
`[n]_Q!/∏[h] = Σ_{T ∈ SYT(λ)} Q^{maj(T) − n(λ)}` — is not established by this route. It is proved
in `QOU.Mathlib.MajFormula` (`qFactorial_eq_schurElt_mul_fmaj`, `coeff_fmaj_nonneg`; bean
`qou-q3q2`). The integrality proved here is the polynomiality half.

Base ring (§7c): the polynomial statements are over a generic `[CommRing R]`; the evaluation
statement is over a generic `[Field F]`. No ordering or archimedean input.
-/

namespace QOU.SchurWeyl.HookDivisibility
open Finset

/-- Positions `c < b` on the same `d`-runner as `b` (`c ≡ b mod d`). -/
def runnerBelow (d b : ℕ) : Finset ℕ := (range b).filter (fun c => c % d = b % d)

/-- Gaps of the bead set `B` below `b` on its `d`-runner. -/
def gaps (B : Finset ℕ) (d b : ℕ) : Finset ℕ := (runnerBelow d b).filter (fun c => c ∉ B)

/-- Beads of `B` below `b` on its `d`-runner. -/
def beads (B : Finset ℕ) (d b : ℕ) : Finset ℕ := (runnerBelow d b).filter (fun c => c ∈ B)

/-- `W_d(B) = Σ_{b∈B} #(gaps below b on its d-runner)`. -/
def weight (B : Finset ℕ) (d : ℕ) : ℕ := ∑ b ∈ B, (gaps B d b).card

theorem card_runnerBelow {d : ℕ} (hd : 0 < d) (b : ℕ) : (runnerBelow d b).card = b / d := by
  have key : runnerBelow d b = (range (b / d)).image (fun k => b % d + d * k) := by
    ext c
    simp only [runnerBelow, mem_filter, mem_range, mem_image]
    constructor
    · rintro ⟨hcb, hcm⟩
      refine ⟨c / d, ?_, ?_⟩
      · have h1 := Nat.mod_add_div c d
        have h2 := Nat.mod_add_div b d
        have : d * (c / d) < d * (b / d) := by omega
        exact Nat.lt_of_mul_lt_mul_left this
      · have := Nat.mod_add_div c d; omega
    · rintro ⟨k, hk, rfl⟩
      have h2 := Nat.mod_add_div b d
      have : d * k < d * (b / d) := Nat.mul_lt_mul_of_pos_left hk hd
      refine ⟨by omega, ?_⟩
      rw [Nat.add_mul_mod_self_left, Nat.mod_mod]
  rw [key, card_image_of_injective _ (fun k k' h => by
    exact Nat.eq_of_mul_eq_mul_left hd (by omega)), card_range]

theorem card_gaps_add_card_beads {d : ℕ} (hd : 0 < d) (B : Finset ℕ) (b : ℕ) :
    (gaps B d b).card + (beads B d b).card = b / d := by
  rw [← card_runnerBelow hd b, gaps, beads, add_comm]
  exact filter_card_add_filter_neg_card_eq_card _

theorem beads_ssubset {B : Finset ℕ} {d b b' : ℕ} (hb : b ∈ B) (hlt : b < b')
    (hm : b % d = b' % d) : beads B d b ⊂ beads B d b' := by
  rw [ssubset_iff_of_subset]
  · refine ⟨b, ?_, ?_⟩
    · simp [beads, runnerBelow, hb, hlt, hm]
    · simp [beads, runnerBelow]
  · intro c
    simp only [beads, runnerBelow, mem_filter, mem_range]
    rintro ⟨⟨h1, h2⟩, h3⟩
    exact ⟨⟨by omega, h2.trans hm⟩, h3⟩

/-- The abacus position map `b ↦ (b mod d) + d · (rank of b on its runner)` is injective. -/
theorem abacus_injOn {B : Finset ℕ} {d : ℕ} (hd : 0 < d) :
    Set.InjOn (fun b => b % d + d * (beads B d b).card) B := by
  intro b hb b' hb' h
  simp only at h
  have hm : b % d = b' % d := by
    have := congrArg (· % d) h
    simpa [Nat.add_mul_mod_self_left, Nat.mod_mod] using this
  have hk : (beads B d b).card = (beads B d b').card := by
    exact Nat.eq_of_mul_eq_mul_left hd
      (show d * (beads B d b).card = d * (beads B d b').card by omega)
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · exact absurd hk (ne_of_lt (card_lt_card (beads_ssubset hb hlt hm)))
  · exact absurd hk.symm (ne_of_lt (card_lt_card (beads_ssubset hb' hlt hm.symm)))

/-- `n(n−1) ≤ 2 Σ S` for any `n`-element set of naturals. -/
theorem card_mul_pred_le_two_mul_sum (S : Finset ℕ) :
    S.card * (S.card - 1) ≤ 2 * ∑ x ∈ S, x := by
  induction S using Finset.induction_on_max with
  | h0 => simp
  | step a S ha ih =>
    have haS : a ∉ S := fun h => lt_irrefl a (ha a h)
    have hcard : S.card ≤ a := by
      have : S ⊆ range a := fun x hx => mem_range.mpr (ha x hx)
      simpa using card_le_card this
    rw [card_insert_of_notMem haS, sum_insert haS]
    rcases Nat.eq_zero_or_pos S.card with h | h
    · rw [h]; simp
    · have : (S.card + 1) * (S.card + 1 - 1) = S.card * (S.card - 1) + 2 * S.card := by
        cases hS : S.card with
        | zero => omega
        | succ k => simp; ring
      omega

/-- Rank bound: `Σ_{b∈B} #(beads of B below b) ≤ n(n−1)/2`, stated doubled. -/
theorem two_mul_sum_beads_one_le (B : Finset ℕ) :
    2 * ∑ b ∈ B, (beads B 1 b).card ≤ B.card * (B.card - 1) := by
  have hinj : Set.InjOn (fun b => (beads B 1 b).card) B := by
    intro b hb b' hb' h
    have := abacus_injOn (B := B) (d := 1) one_pos hb hb'
    simp only [Nat.mod_one, one_mul, zero_add] at this
    exact this h
  have himg := sum_image (f := fun y : ℕ => y) hinj
  simp only at himg
  rw [← himg]
  have hsub : B.image (fun b => (beads B 1 b).card) ⊆ range B.card := by
    intro y hy
    obtain ⟨b, hb, rfl⟩ := mem_image.mp hy
    have : beads B 1 b ⊆ B.erase b := by
      intro c hc
      simp only [beads, runnerBelow, mem_filter, mem_range] at hc
      exact mem_erase.mpr ⟨by omega, hc.2⟩
    have := card_le_card this
    rw [card_erase_of_mem hb] at this
    have : 0 < B.card := card_pos.mpr ⟨b, hb⟩
    exact mem_range.mpr (by omega)
  have h1 := sum_le_sum_of_subset (f := fun y => y) hsub
  have h2 := sum_range_id_mul_two B.card
  simp only at h1 ⊢
  omega

/-- **Abacus inequality.** `d · W_d(B) ≤ W_1(B)` for every bead set `B` and `d ≥ 1`. -/
theorem mul_weight_le {d : ℕ} (hd : 0 < d) (B : Finset ℕ) :
    d * weight B d ≤ weight B 1 := by
  -- sum split for d and for 1
  have sd : weight B d + ∑ b ∈ B, (beads B d b).card = ∑ b ∈ B, b / d := by
    rw [weight, ← sum_add_distrib]
    exact sum_congr rfl fun b _ => card_gaps_add_card_beads hd B b
  have s1 : weight B 1 + ∑ b ∈ B, (beads B 1 b).card = ∑ b ∈ B, b := by
    rw [weight, ← sum_add_distrib]
    exact sum_congr rfl fun b _ => by
      simpa using card_gaps_add_card_beads one_pos B b
  have hsplit : ∑ b ∈ B, b = d * ∑ b ∈ B, b / d + ∑ b ∈ B, b % d := by
    rw [mul_sum, ← sum_add_distrib]
    exact sum_congr rfl fun b _ => (Nat.div_add_mod b d).symm
  -- injection lower bound
  have hinj := abacus_injOn (B := B) hd
  have hlow := card_mul_pred_le_two_mul_sum (B.image fun b => b % d + d * (beads B d b).card)
  rw [card_image_of_injOn hinj, sum_image hinj, sum_add_distrib, ← mul_sum] at hlow
  have hup := two_mul_sum_beads_one_le B
  have hmul : d * weight B d + d * ∑ b ∈ B, (beads B d b).card = d * ∑ b ∈ B, b / d := by
    rw [← mul_add, sd]
  omega

/-! ## Young diagrams as bead sets -/

open YoungDiagram QOU.QBeta.WenzlWeight

section Diagram

variable (μ : YoungDiagram)

/-- The beta-number of row `i`: `λ_i + (r − 1 − i)` with `r` the number of rows. -/
def beta (i : ℕ) : ℕ := μ.rowLen i + (μ.colLen 0 - 1 - i)

/-- The bead set `{λ_i + r − 1 − i : i < r}` of `μ`. -/
def betaSet : Finset ℕ := (range (μ.colLen 0)).image (beta μ)

/-- The column position `j + r − λ'_j`; the gap of column `j`. -/
def cval (j : ℕ) : ℕ := j + μ.colLen 0 - μ.colLen j

theorem lt_rowLen_iff (i j : ℕ) : j < μ.rowLen i ↔ i < μ.colLen j :=
  mem_iff_lt_rowLen.symm.trans mem_iff_lt_colLen

theorem colLen_le (j : ℕ) : μ.colLen j ≤ μ.colLen 0 := μ.colLen_anti 0 j (Nat.zero_le _)

theorem beta_lt {i i' : ℕ} (h : i < i') (hi' : i' < μ.colLen 0) : beta μ i' < beta μ i := by
  have := μ.rowLen_anti i i' h.le
  unfold beta; omega

theorem beta_injOn : Set.InjOn (beta μ) (range (μ.colLen 0)) := by
  intro i hi i' hi' h
  simp only [coe_range, Set.mem_Iio] at hi hi'
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · exact absurd h (ne_of_gt (beta_lt μ hlt hi'))
  · exact absurd h (ne_of_lt (beta_lt μ hlt hi))

theorem cval_strictMono : StrictMono (cval μ) := fun j j' h => by
  have := μ.colLen_anti j j' h.le
  have := colLen_le μ j
  have := colLen_le μ j'
  unfold cval; omega

theorem cval_lt_beta {i j : ℕ} (hj : j < μ.rowLen i) : cval μ j < beta μ i := by
  have hi : i < μ.colLen j := (lt_rowLen_iff μ i j).mp hj
  have := colLen_le μ j
  unfold cval beta; omega

theorem cval_notMem (j : ℕ) : cval μ j ∉ betaSet μ := by
  simp only [betaSet, mem_image, mem_range, not_exists, not_and]
  intro k hk heq
  have h1 := lt_rowLen_iff μ k j
  have := colLen_le μ j
  unfold beta cval at heq
  by_cases hkj : j < μ.rowLen k
  · have := h1.mp hkj; omega
  · have : ¬ k < μ.colLen j := fun h => hkj (h1.mpr h)
    omega

theorem hook_eq {i j : ℕ} (hj : j < μ.rowLen i) : hook μ (i, j) = beta μ i - cval μ j := by
  have hi := (lt_rowLen_iff μ i j).mp hj
  have := colLen_le μ j
  simp only [hook, beta, cval]; omega

/-- The gaps below `beta i` are exactly the column positions `cval j`, `j < λ_i`. -/
theorem image_cval_row {i : ℕ} (hi : i < μ.colLen 0) :
    (range (μ.rowLen i)).image (cval μ) = gaps (betaSet μ) 1 (beta μ i) := by
  apply eq_of_subset_of_card_le
  · intro c hc
    obtain ⟨j, hj, rfl⟩ := mem_image.mp hc
    simp only [gaps, runnerBelow, mem_filter, mem_range, Nat.mod_one]
    exact ⟨⟨cval_lt_beta μ (mem_range.mp hj), trivial⟩, cval_notMem μ j⟩
  · rw [card_image_of_injective _ (cval_strictMono μ).injective, card_range]
    have hsplit := card_gaps_add_card_beads one_pos (betaSet μ) (beta μ i)
    have hsub : (Ioo i (μ.colLen 0)).image (beta μ) ⊆ beads (betaSet μ) 1 (beta μ i) := by
      intro c hc
      obtain ⟨k, hk, rfl⟩ := mem_image.mp hc
      rw [mem_Ioo] at hk
      simp only [beads, runnerBelow, mem_filter, mem_range, Nat.mod_one, betaSet, mem_image]
      exact ⟨⟨beta_lt μ hk.1 hk.2, trivial⟩, k, by simpa using hk.2, rfl⟩
    have hcard := card_le_card hsub
    rw [card_image_of_injOn (fun k hk k' hk' h => beta_injOn μ
      (by simpa using (mem_Ioo.mp hk).2) (by simpa using (mem_Ioo.mp hk').2) h),
      Nat.card_Ioo] at hcard
    simp only [Nat.div_one] at hsplit
    have hb : beta μ i = μ.rowLen i + (μ.colLen 0 - 1 - i) := rfl
    omega

theorem gaps_eq_filter (B : Finset ℕ) (d b : ℕ) :
    gaps B d b = (gaps B 1 b).filter (fun c => c % d = b % d) := by
  ext c
  simp only [gaps, runnerBelow, mem_filter, mem_range, Nat.mod_one]
  tauto

theorem row_count {d i : ℕ} (hi : i < μ.colLen 0) :
    ((range (μ.rowLen i)).filter (fun j => d ∣ hook μ (i, j))).card =
      (gaps (betaSet μ) d (beta μ i)).card := by
  rw [gaps_eq_filter, ← image_cval_row μ hi, filter_image,
    card_image_of_injective _ (cval_strictMono μ).injective]
  congr 1
  refine filter_congr fun j hj => ?_
  have hj' := mem_range.mp hj
  rw [hook_eq μ hj']
  exact (Nat.modEq_iff_dvd' (cval_lt_beta μ hj').le).symm

/-- **Hook count = abacus weight**: `#{x ∈ μ : d ∣ h(x)} = W_d(betaSet μ)`. -/
theorem card_filter_dvd_hook (d : ℕ) :
    (μ.cells.filter (fun x => d ∣ hook μ x)).card = weight (betaSet μ) d := by
  rw [card_eq_sum_card_fiberwise (f := Prod.fst) (t := range (μ.colLen 0))]
  · have hw : weight (betaSet μ) d =
        ∑ i ∈ range (μ.colLen 0), (gaps (betaSet μ) d (beta μ i)).card := by
      unfold weight
      nth_rw 1 [betaSet]
      exact sum_image (beta_injOn μ)
    rw [hw]
    refine sum_congr rfl fun i hi => ?_
    rw [← row_count μ (mem_range.mp hi)]
    rw [← card_image_of_injective ((range (μ.rowLen i)).filter (fun j => d ∣ hook μ (i, j)))
      (Prod.mk_right_injective i)]
    refine congrArg card ?_
    ext ⟨a, b⟩
    simp only [mem_filter, mem_cells, mem_image, mem_range, Prod.mk.injEq]
    constructor
    · rintro ⟨⟨hx, hd⟩, rfl⟩
      exact ⟨b, ⟨mem_iff_lt_rowLen.mp hx, hd⟩, rfl, rfl⟩
    · rintro ⟨j, ⟨hj, hd⟩, rfl, rfl⟩
      exact ⟨⟨mem_iff_lt_rowLen.mpr hj, hd⟩, rfl⟩
  · intro x hx
    simp only [coe_filter, Set.mem_setOf_eq, mem_cells] at hx
    simp only [coe_range, Set.mem_Iio]
    exact mem_iff_lt_colLen.mp (μ.up_left_mem le_rfl (Nat.zero_le _) hx.1)

/-- **The hook-divisibility inequality** `d · #{x ∈ μ : d ∣ h(x)} ≤ |μ|`. -/
theorem mul_card_filter_dvd_hook_le {d : ℕ} (hd : 0 < d) :
    d * (μ.cells.filter (fun x => d ∣ hook μ x)).card ≤ μ.cells.card := by
  have h1 := card_filter_dvd_hook μ 1
  rw [filter_true_of_mem (fun x _ => one_dvd _)] at h1
  rw [card_filter_dvd_hook, h1]
  exact mul_weight_le hd _

end Diagram

/-! ## Cyclotomic assembly -/

section Poly

open Polynomial

/-- The `q`-integer polynomial `[m] = 1 + X + ⋯ + X^{m−1}`. -/
noncomputable def qIntPoly (R : Type*) [CommRing R] (m : ℕ) : R[X] := ∑ i ∈ range m, X ^ i

variable {R : Type*} [CommRing R]

theorem qIntPoly_eq_prod_cyclotomic {m M : ℕ} (hm : 0 < m) (hmM : m ≤ M) :
    qIntPoly R m = ∏ d ∈ (Icc 2 M).filter (· ∣ m), cyclotomic d R := by
  rw [qIntPoly, ← prod_cyclotomic_eq_geom_sum hm R]
  refine prod_congr ?_ fun _ _ => rfl
  ext d
  simp only [mem_erase, Nat.mem_divisors, mem_filter, mem_Icc]
  constructor
  · rintro ⟨h1, hdvd, _⟩
    have := Nat.le_of_dvd hm hdvd
    have : d ≠ 0 := by
      rintro rfl
      rw [zero_dvd_iff] at hdvd
      omega
    exact ⟨⟨by omega, by omega⟩, hdvd⟩
  · rintro ⟨⟨h2, _⟩, hdvd⟩
    exact ⟨by omega, hdvd, by omega⟩

theorem prod_qIntPoly_eq {ι : Type*} (s : Finset ι) (h : ι → ℕ) (M : ℕ)
    (hpos : ∀ x ∈ s, 0 < h x) (hle : ∀ x ∈ s, h x ≤ M) :
    ∏ x ∈ s, qIntPoly R (h x) =
      ∏ d ∈ Icc 2 M, cyclotomic d R ^ (s.filter (fun x => d ∣ h x)).card := by
  rw [prod_congr rfl fun x hx => qIntPoly_eq_prod_cyclotomic (R := R) (hpos x hx) (hle x hx)]
  simp_rw [prod_filter]
  rw [prod_comm]
  refine prod_congr rfl fun d _ => ?_
  rw [← prod_filter, prod_const]

theorem div_le_card_filter_dvd_succ {d : ℕ} (hd : 0 < d) (n : ℕ) :
    n / d ≤ ((range n).filter (fun m => d ∣ m + 1)).card := by
  have hcard : (range (n / d)).card = n / d := card_range _
  rw [← hcard]
  refine card_le_card_of_injOn (fun k => d * (k + 1) - 1) ?_ ?_
  · intro k hk
    simp only [coe_range, Set.mem_Iio] at hk
    have h1 : d * (k + 1) ≤ d * (n / d) := Nat.mul_le_mul_left d hk
    have h2 : d * (n / d) ≤ n := Nat.mul_div_le n d
    have h3 : 1 ≤ d * (k + 1) := Nat.mul_pos hd (Nat.succ_pos k)
    simp only [coe_filter, mem_range, Set.mem_setOf_eq]
    refine ⟨by omega, ?_⟩
    rw [Nat.sub_add_cancel h3]
    exact dvd_mul_right d _
  · intro k _ k' _ h
    simp only at h
    have h3 : 1 ≤ d * (k + 1) := Nat.mul_pos hd (Nat.succ_pos k)
    have h3' : 1 ≤ d * (k' + 1) := Nat.mul_pos hd (Nat.succ_pos k')
    have : d * (k + 1) = d * (k' + 1) := by omega
    have := Nat.eq_of_mul_eq_mul_left hd this
    omega

/-- **Hook-product divisibility.** `∏_{x ∈ μ} [h(x)]` divides `[n]! = ∏_{m=1}^{n} [m]` in `R[X]`,
`n = |μ|`. -/
theorem hookProd_dvd_qFactorial (μ : YoungDiagram) :
    ∏ x ∈ μ.cells, qIntPoly R (hook μ x) ∣ ∏ m ∈ range μ.cells.card, qIntPoly R (m + 1) := by
  set n := μ.cells.card
  set M := n + ∑ x ∈ μ.cells, hook μ x
  rw [prod_qIntPoly_eq μ.cells (hook μ) M (fun x hx => one_le_hook hx)
      (fun x hx => (single_le_sum (fun _ _ => Nat.zero_le _) hx).trans (Nat.le_add_left _ _)),
    prod_qIntPoly_eq (range n) (· + 1) M (fun _ _ => Nat.succ_pos _)
      (fun m hm => by have := mem_range.mp hm; simp only; omega)]
  refine prod_dvd_prod_of_dvd _ _ fun d hd => pow_dvd_pow _ ?_
  have hd0 : 0 < d := by have := (mem_Icc.mp hd).1; omega
  have hmul := mul_card_filter_dvd_hook_le μ hd0
  have : (μ.cells.filter (fun x => d ∣ hook μ x)).card ≤ n / d :=
    (Nat.le_div_iff_mul_le hd0).mpr (by rw [mul_comm]; exact hmul)
  exact this.trans (div_le_card_filter_dvd_succ hd0 n)

end Poly

/-! ## The Schur element divides the `q`-factorial -/

section Schur

open Polynomial

variable {F : Type*} [Field F]

theorem aeval_qIntPoly {Q : F} (hQ1 : Q ≠ 1) (m : ℕ) :
    aeval Q (qIntPoly ℤ m) = (1 - Q ^ m) / (1 - Q) := by
  simp only [qIntPoly, map_sum, map_pow, aeval_X]
  rw [geom_sum_eq hQ1, ← neg_div_neg_eq, neg_sub, neg_sub]

/-- **`c_λ ∣ [n]_Q!` over `ℤ[Q]`.** For every Young diagram `μ` with `n` cells there is an integer
polynomial `P` with `[n]_Q! = c_λ(Q) · Q^{n(λ)} · P(Q)` in every field, for `Q ≠ 0, 1`. -/
theorem exists_qFactorial_eq_schurElt_mul (μ : YoungDiagram) :
    ∃ P : ℤ[X], ∀ (Q : F), Q ≠ 0 → Q ≠ 1 →
      ∏ m ∈ range μ.cells.card, (1 - Q ^ (m + 1)) / (1 - Q) =
        schurElt Q μ * (Q ^ nPart μ * aeval Q P) := by
  obtain ⟨P, hP⟩ := hookProd_dvd_qFactorial (R := ℤ) μ
  refine ⟨P, fun Q hQ0 hQ1 => ?_⟩
  have h := congrArg (aeval Q) hP
  simp only [map_mul, map_prod, aeval_qIntPoly hQ1] at h
  rw [h, schurElt_eq]
  field_simp

end Schur

end QOU.SchurWeyl.HookDivisibility
