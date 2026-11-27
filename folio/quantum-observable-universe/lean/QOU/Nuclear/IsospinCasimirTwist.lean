import BraidKnotOctonion.SeminormalContentCasimir
import HeckeTemperleyLieb.OcneanuWeightBranching

/-!
# `QOU.Nuclear.IsospinCasimirTwist` — the `T(T+1)` term of the braid channel, block by block

Gap **G2** of the term-completeness ledger (`docs/audits/2026-11-27-term-completeness-ledger.md`,
bean `qou-tcl2` under `qou-myts`): the binding closed form `τ_p^Z τ_n^N ∏ f_i` and the q-CLT proxy
do not depend on the convention-D block, so they carry no `T(T+1)` term, and `Q_β` has no
isobaric parabola.  The ledger's method: evaluate the convention-D trace block by block at level
`n = 3A`, over its `⌊n/2⌋ + 1` two-row blocks.

This file does that for the one central element whose block scalar is forced by the
representation theory alone: the **Murphy product** `Φ_n = L_0 L_1 ⋯ L_n ∈ H_{n+1}(q)`.

## What is proved (no hypothesis beyond genericity of `q`)

1. `seminormalRep_murphyProd_scalar` — on the seminormal block `ρ_μ` of **every** Young
   diagram `μ`, `Φ_n` acts by the scalar `q^{2 c(μ)}`, `c(μ) = Σ_{□∈μ} content(□)`.
   `heckeWedderburn_murphyProd` — the same on every Wedderburn block of `H_{n+1}(q)` (char 0).
   Built from `QJucysMurphyEigen.seminormalRep_qJM` (Ram 1997 Thm 4.1, proved in the corpus) and
   `sum_cellOf_range`.  Since the image is scalar on every Wedderburn block, `Φ_n` is central.
2. `four_contentSum_twoRow` — for the two-row block `λ = (m, k)`, with `n = m + k` strands and
   `t = m − k = 2T` (twice the isospin of the block),

       4·c(λ) = t(t + 2) + n(n − 4),     i.e.     c(λ) = T(T+1) + n(n−4)/4.

   Pure arithmetic over `ℤ`.
3. `twoRow_murphyScalar_sq` — so the block scalar is

       (q^{2c(λ)})² = q^{t(t+2)} · q^{n(n−4)}      (= q^{4T(T+1)} · q^{n(n−4)}).

   `twoRow_murphyScalar_ratio` — at fixed `n` the `n`-only factor cancels between blocks:
   the **whole** block dependence of `Φ_n` is `q^{2T(T+1)}`, with coefficient `2` (in powers of
   `q`) on `T(T+1)`, the same at every level `n`.  Nothing is fitted: the coefficient is the
   factor `2` of the corpus Murphy convention `L_k ↦ q^{2·content}` (`QJucysMurphy` §Convention).
4. The isobaric parabola (`ℤ` arithmetic).  A nucleus with `Z` protons and `N` neutrons has
   `T_z = (Z − N)/2`, and the blocks that contain that weight have `T ≥ |T_z|`, `T ≡ T_z (mod 1)`.
   On the lowest one, `T = |T_z|`, with `d = N − Z`:

       4T(T+1) = d² + 2|d|                                        (`casimir4_lowest`)

   which is a parabola in `T_z` with a cusp at `T_z = 0`.  One `β⁻` step `(Z,N) → (Z+1,N−1)`
   sends `d ↦ d − 2`, and the change of `4T(T+1)` is

       4d   (d ≥ 2),     0   (d = 1),     4d − 8   (d ≤ 0)       (`casimir4_beta_step_*`).

   `casimir4_lowest_le` — `T = |T_z|` is the block of least `T(T+1)` among those containing the
   weight `T_z`.  Which block a nucleus occupies is **not** decided here; the lowest-block choice
   is stated as a hypothesis wherever it is used.

## What is NOT proved, and the scope

* **`Φ_n = Δ²` (the full twist).**  That the Murphy product equals the full twist of `B_{n+1}` in
  `H_{n+1}(q)` is the standard identity `Δ² = L_1 ⋯ L_n` ([murphy1992] §2; [kassel-turaev2008]
  §4.3).  It is cited, not proved here.  Nothing below uses it: every theorem is about `Φ_n` as
  defined.  `KeystoneJucysMurphyTwist.JucysMurphySpectrum` carries the twist's block scalar as a
  hypothesis; item 1 is that hypothesis for `Φ_n`, discharged.
* **That a nucleus's operator contains `Φ_{3A}`.**  The ledger audits a formula for missing
  index entries; it does not choose the word (gap G5).  This file supplies the block-dependent
  entry with its coefficient for the twist.  For a general braid word the block character
  `χ_T(β)` is word-dependent and need not be a function of `T(T+1)`.
* **Energies.**  No energy scale, no `ln`, no measured value appears.  Turning `q^{2T(T+1)}` into a
  binding contribution needs the braid channel's existing trace-to-energy map; that is producer
  work, recorded in the audit note.

## Base ring (§7c)

Items 1 and 3 hold over any field with `q ≠ 0` not a root of unity (the genericity Ram 4.1
presupposes); the Wedderburn form adds `CharZero`.  Items 2 and 4 are over `ℤ`.

Refs: [ram1997] Theorem 4.1; [murphy1992]; [hoefsmit1974]; [kassel-turaev2008].
-/

namespace QOU.Nuclear.IsospinCasimirTwist

open QOU.SchurWeyl
open QOU.Mathlib (StandardYoungTableau)
open TableauCells QOU.SchurWeyl.SeminormalRep

/-! ## 1. The Murphy product and its block scalar -/

section Murphy

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- The Murphy product `Φ = L_0 L_1 ⋯ L_k ∈ H_{n+1}(q)` (left to right).  The `L_j` commute
(`qJM_commute`), so the order is immaterial; it is fixed here to make the definition a plain
recursion.  At `k = n` this is the element that `[murphy1992]` identifies with the full twist. -/
noncomputable def murphyProd : ℕ → Hecke K q qi n
  | 0 => qJM K q qi n 0
  | k + 1 => murphyProd k * qJM K q qi n (k + 1)

theorem murphyProd_zero : murphyProd K q qi n 0 = qJM K q qi n 0 := rfl

theorem murphyProd_succ (k : ℕ) :
    murphyProd K q qi n (k + 1) = murphyProd K q qi n k * qJM K q qi n (k + 1) := rfl

end Murphy

section Block

variable {μ : YoungDiagram}

/-- **Partial products on a seminormal block.**  `ρ_μ(L_0 ⋯ L_k)` is diagonal, with entry
`q^{2 Σ_{j ≤ k} content(cell of j+1)}` at the tableau `T`. -/
theorem seminormalRep_murphyProd {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (hN : μ.cells.card = n + 1) :
    ∀ k : ℕ, k ≤ n →
      seminormalRep q hq0 hq2 n hN (murphyProd K q q⁻¹ n k)
        = Matrix.diagonal (fun T : StandardYoungTableau μ =>
            q ^ (2 * ∑ j ∈ Finset.range (k + 1), cellContent (cellOf T (j + 1))))
  | 0, _ => by
      rw [murphyProd_zero, seminormalRep_qJM q hq0 hq2 n hN 0 (Nat.zero_le _), jmDiagVal]
      simp
  | k + 1, hk => by
      rw [murphyProd_succ, map_mul, seminormalRep_murphyProd q hq0 hq2 n hN k (by omega),
        seminormalRep_qJM q hq0 hq2 n hN (k + 1) hk, jmDiagVal, Matrix.diagonal_mul_diagonal]
      congr 1
      funext T
      rw [← zpow_add₀ hq0, Finset.sum_range_succ (n := k + 1), mul_add]

/-- **The Murphy product acts on every seminormal block by `q^{2c(μ)}`**, `c(μ)` the content
sum of `μ`.  The diagonal of the partial product is constant at `k = n` because the values
`1, …, n+1` sweep every cell of `μ` once (`sum_cellOf_range`). -/
theorem seminormalRep_murphyProd_scalar {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (hN : μ.cells.card = n + 1) :
    seminormalRep q hq0 hq2 n hN (murphyProd K q q⁻¹ n n)
      = q ^ (2 * ∑ c ∈ μ.cells, cellContent c)
          • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K) := by
  classical
  rw [seminormalRep_murphyProd q hq0 hq2 n hN n le_rfl]
  ext T U
  by_cases h : T = U
  · subst h
    simp only [Matrix.diagonal_apply_eq, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul,
      mul_one]
    rw [sum_cellOf_range T hN (fun c => cellContent c)]
  · simp [Matrix.diagonal_apply_ne _ h, Matrix.one_apply_ne h]

end Block

section Wedderburn

/-- **The Murphy product on the Wedderburn decomposition of `H_{n+1}(q)`.**  Under
`heckeWedderburn : H_{n+1}(q) ≃ ∏_{λ ⊢ n+1} M_{d_λ}(K)`, `Φ_n` goes to the tuple of scalars
`q^{2c(λ)}`.  Every block is covered and no weight vector is assumed. -/
theorem heckeWedderburn_murphyProd {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (lam : Partition (n + 1)) :
    heckeWedderburn q hq0 hq2 n (murphyProd K q q⁻¹ n n) lam
      = q ^ (2 * ∑ c ∈ (QOU.Mathlib.partitionShape lam).cells, cellContent c) • 1 := by
  show heckeProduct q hq0 hq2 n (murphyProd K q q⁻¹ n n) lam = _
  rw [heckeProduct_apply]
  exact seminormalRep_murphyProd_scalar q hq0 hq2 n (partitionShape_card_succ lam)

end Wedderburn

/-! ## 2. The content sum of a two-row block is `T(T+1)` plus a function of `n` -/

section TwoRow

/-- `2 · Σ_{j<m} j = m(m − 1)` over `ℤ`. -/
theorem two_mul_sum_range_int (m : ℕ) :
    2 * ∑ j ∈ Finset.range m, (j : ℤ) = (m : ℤ) * ((m : ℤ) - 1) := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_range_succ, mul_add, ih]
      push_cast
      ring

variable {m k : ℕ}

/-- **Content sum of the two-row diagram `(m, k)`.**  Row 0 holds contents `0, …, m−1`, row 1
holds `−1, …, k−2`, so `2c = m(m−1) + k(k−3)`. -/
theorem two_mul_contentSum_twoRow (h : k ≤ m) :
    2 * ∑ c ∈ (twoRow m k h).cells, cellContent c
      = (m : ℤ) * ((m : ℤ) - 1) + (k : ℤ) * ((k : ℤ) - 3) := by
  rw [cells_twoRow h, Finset.sum_union (by simp [Finset.disjoint_left]),
    Finset.sum_image (by intro a _ b _ hab; simpa using hab),
    Finset.sum_image (by intro a _ b _ hab; simpa using hab)]
  have h1 := two_mul_sum_range_int m
  have h2 := two_mul_sum_range_int k
  have e0 : ∑ j ∈ Finset.range m, cellContent ((0 : ℕ), j) = ∑ j ∈ Finset.range m, (j : ℤ) := by
    refine Finset.sum_congr rfl (fun j _ => ?_)
    simp [cellContent]
  have e1 : ∑ j ∈ Finset.range k, cellContent ((1 : ℕ), j)
      = ∑ j ∈ Finset.range k, (j : ℤ) - (k : ℤ) := by
    rw [Finset.sum_congr rfl (fun j _ => show cellContent ((1 : ℕ), j) = (j : ℤ) - 1 by
      simp [cellContent]), Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range]
    simp
  rw [e0, e1]
  linear_combination h1 + h2

/-- **The isospin form.**  With `n = m + k` strands and `t = m − k = 2T`,
`4c(λ) = t(t+2) + n(n−4)`, i.e. `c(λ) = T(T+1) + n(n−4)/4`. -/
theorem four_contentSum_twoRow (h : k ≤ m) :
    4 * ∑ c ∈ (twoRow m k h).cells, cellContent c
      = ((m : ℤ) - k) * ((m : ℤ) - k + 2) + ((m : ℤ) + k) * ((m : ℤ) + k - 4) := by
  have := two_mul_contentSum_twoRow h
  linear_combination 2 * this

/-- **Block scalar, squared, in isospin form.**  `(q^{2c(λ)})² = q^{t(t+2)} · q^{n(n−4)}`:
the factor `q^{t(t+2)} = q^{4T(T+1)}` carries all the dependence on the block. -/
theorem twoRow_murphyScalar_sq {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0) (h : k ≤ m) :
    (q ^ (2 * ∑ c ∈ (twoRow m k h).cells, cellContent c)) ^ 2
      = q ^ (((m : ℤ) - k) * ((m : ℤ) - k + 2)) * q ^ (((m : ℤ) + k) * ((m : ℤ) + k - 4)) := by
  rw [← zpow_natCast, ← zpow_mul, ← zpow_add₀ hq0]
  congr 1
  have := four_contentSum_twoRow h
  push_cast
  linear_combination this

/-- **Only `T(T+1)` distinguishes blocks at the same level.**  For two two-row blocks with the
same number of strands `m + k = m' + k'`, the squared Murphy scalars differ exactly by
`q^{t(t+2)} / q^{t'(t'+2)}` (cleared of division). -/
theorem twoRow_murphyScalar_ratio {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    {m' k' : ℕ} (h : k ≤ m) (h' : k' ≤ m') (hn : m + k = m' + k') :
    (q ^ (2 * ∑ c ∈ (twoRow m k h).cells, cellContent c)) ^ 2
        * q ^ (((m' : ℤ) - k') * ((m' : ℤ) - k' + 2))
      = (q ^ (2 * ∑ c ∈ (twoRow m' k' h').cells, cellContent c)) ^ 2
        * q ^ (((m : ℤ) - k) * ((m : ℤ) - k + 2)) := by
  rw [twoRow_murphyScalar_sq q hq0 h, twoRow_murphyScalar_sq q hq0 h']
  have hn' : ((m : ℤ) + k) = ((m' : ℤ) + k') := by exact_mod_cast hn
  rw [hn']
  ring

/-- **The seminormal block of `(m, k)`, assembled.**  `Φ_n` acts on it by a scalar whose square
is `q^{t(t+2)} · q^{n(n−4)}`. -/
theorem seminormalRep_murphyProd_twoRow {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (h : k ≤ m)
    (hN : (twoRow m k h).cells.card = n + 1) :
    ∃ s : K, seminormalRep q hq0 hq2 n hN (murphyProd K q q⁻¹ n n)
        = s • (1 : Matrix (StandardYoungTableau (twoRow m k h))
            (StandardYoungTableau (twoRow m k h)) K)
      ∧ s ^ 2 = q ^ (((m : ℤ) - k) * ((m : ℤ) - k + 2))
          * q ^ (((m : ℤ) + k) * ((m : ℤ) + k - 4)) :=
  ⟨_, seminormalRep_murphyProd_scalar q hq0 hq2 n hN, twoRow_murphyScalar_sq q hq0 h⟩

/-! ### Non-vacuity at the levels in use -/

/-- One nucleon, `n = 3`: `(3)` (`T = 3/2`) has content sum `3`, `(2,1)` (`T = 1/2`) has `0`. -/
theorem contentSum_level_three :
    4 * ∑ c ∈ (twoRow 3 0 (by norm_num)).cells, cellContent c = 12
      ∧ 4 * ∑ c ∈ (twoRow 2 1 (by norm_num)).cells, cellContent c = 0 := by
  constructor
  · rw [four_contentSum_twoRow]; norm_num
  · rw [four_contentSum_twoRow]; norm_num

/-- Two nucleons, `n = 6`: the four blocks `T = 3, 2, 1, 0` have `4c = 36, 16, 4, 0`, i.e.
`4c − 4T(T+1) = n(n−4) = 12` on each. -/
theorem contentSum_level_six :
    4 * ∑ c ∈ (twoRow 6 0 (by norm_num)).cells, cellContent c = 4 * 3 * 4 + 12
      ∧ 4 * ∑ c ∈ (twoRow 5 1 (by norm_num)).cells, cellContent c = 4 * 2 * 3 + 12
      ∧ 4 * ∑ c ∈ (twoRow 4 2 (by norm_num)).cells, cellContent c = 4 * 1 * 2 + 12
      ∧ 4 * ∑ c ∈ (twoRow 3 3 (by norm_num)).cells, cellContent c = 4 * 0 * 1 + 12 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> (rw [four_contentSum_twoRow]; norm_num)

end TwoRow

/-! ## 3. The isobaric parabola from `T(T+1)` -/

section Isobar

/-- `4T(T+1)` written in `t = 2T`. -/
def casimir4 (t : ℤ) : ℤ := t * (t + 2)

/-- On the lowest block containing the weight `T_z = (Z−N)/2`, `t = 2T = |N − Z|`, and
`4T(T+1) = d² + 2|d|` with `d = N − Z`: a parabola in `T_z` with a cusp at `T_z = 0`. -/
theorem casimir4_lowest (d : ℤ) : casimir4 |d| = d ^ 2 + 2 * |d| := by
  unfold casimir4
  rw [mul_add, abs_mul_abs_self, sq]
  ring

/-- **The lowest block minimises `T(T+1)`.**  Every block containing the weight has
`t ≥ |d|` (and `t ≡ d mod 2`); `t ↦ t(t+2)` is increasing on `t ≥ 0`. -/
theorem casimir4_lowest_le (d t : ℤ) (ht : |d| ≤ t) : casimir4 |d| ≤ casimir4 t := by
  unfold casimir4
  have h0 : 0 ≤ |d| := abs_nonneg d
  nlinarith

/-- One `β⁻` step `(Z, N) → (Z+1, N−1)` sends `d = N − Z` to `d − 2`.  For `d ≥ 2` the lowest-block
`4T(T+1)` drops by `4d`. -/
theorem casimir4_beta_step_pos (d : ℤ) (hd : 2 ≤ d) :
    casimir4 |d| - casimir4 |d - 2| = 4 * d := by
  rw [abs_of_nonneg (by omega : (0 : ℤ) ≤ d), abs_of_nonneg (by omega : (0 : ℤ) ≤ d - 2)]
  unfold casimir4
  ring

/-- At `d = 1` (`N = Z + 1`) the step goes to the mirror nucleus `d = −1`, inside the same
`T = 1/2` block: no change. -/
theorem casimir4_beta_step_one : casimir4 |(1 : ℤ)| - casimir4 |(1 : ℤ) - 2| = 0 := by
  norm_num [casimir4]

/-- For `d ≤ 0` the step moves away from `T_z = 0`, and `4T(T+1)` changes by `4d − 8`. -/
theorem casimir4_beta_step_nonpos (d : ℤ) (hd : d ≤ 0) :
    casimir4 |d| - casimir4 |d - 2| = 4 * d - 8 := by
  rw [abs_of_nonpos hd, abs_of_nonpos (by omega : d - 2 ≤ 0)]
  unfold casimir4
  ring

end Isobar

end QOU.Nuclear.IsospinCasimirTwist
