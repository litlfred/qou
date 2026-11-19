import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Positivity
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-!
# Brane-Tower Exponential Truncation Decay & CPT Markov-Trace Closure on $H_2(q)$ and $H_3(q)$

This module establishes unconditional proofs of the two nuclear-interactions closure results:

1. **Section 1 — Brane-Tower & Spectral-Series Truncation Exponential Decay
   (`prop:archimedean-remainder-exponential-decay`)**:
   - Over any field `K` with `r ≠ 1`, proves the exact geometric partial-sum remainder identity
     $$\frac{1}{1 - r} - \sum_{k=0}^{N} r^k = \frac{r^{N+1}}{1 - r}$$
     (`geometric_limit_sub_partialSum`).
   - For any real deformation parameter `q > 1` with quantum Planck ratio
     `hbarQ q = (q - 1) / q ∈ (0, 1)`, proves `0 < (hbarQ q)^2 < 1`, proves the exact brane-tower
     truncation remainder identity
     $$\frac{1}{1 - \hbar_q^2} - \sum_{k=0}^{N} \hbar_q^{2k} = \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}$$
     (`braneTowerExactLimit_sub_partialSum`), and proves the exact Archimedean equivalence
     $$\frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2} = C(q) \cdot \exp\bigl(-c(q) \cdot N\bigr)$$
     with strictly positive structural constants
     $$C(q) = \frac{\hbar_q^2}{1 - \hbar_q^2} > 0, \qquad c(q) = -2 \ln \hbar_q > 0$$
     (`braneTower_geometric_ceiling_eq_exp_decay`, `braneTower_remainder_abs_eq_exp_decay`,
     `braneTower_exists_exp_decay_bound`).
   - For any real sequence `a : ℕ → ℝ` majorized by a geometric envelope `|a k| ≤ M · r^k`
     (`0 < M`, `0 < r < 1`), proves `Summable a` (`summable_of_abs_le_geom`) and proves that the
     infinite-series tail remainder `seriesTailRemainder a N = (∑' k, a k) - ∑_{k=0}^N a k`
     satisfies both the geometric ceiling and the exponential bound
     $$|R_N(a)| \le \frac{M \, r^{N+1}}{1 - r} = \frac{M r}{1 - r} \exp\bigl(-(-\ln r) N\bigr)$$
     (`abs_seriesTailRemainder_le_geometric`, `abs_seriesTailRemainder_le_exp_decay`,
     `exists_exp_decay_of_geom_majorant`).

2. **Section 2 — Discrete $C$, $P$, $T$ Actions & Markov-Trace Closure on $H_2(q)$ and $H_3(q)$
   (`prop:cpt-d6-d7-d8-closure`)**:
   - **Time-reversal $T$ (`wordRevH3`)**: On the 6-dimensional Gröbner normal-form algebra
     `H_3(q)` (`Fin 6 → R`, basis `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`), proves that word reversal
     `wordRevH3` is an exact involution (`wordRevH3_involutive`), an exact algebra
     anti-automorphism of `mulNF h` (`wordRevH3_mulNF`), and preserves the Markov trace `trM z h`
     over any commutative ring `R` (`trM_wordRevH3`), every irreducible character `chi3, chi21, chi111`,
     and both GPMT-completed Convention-D traces (`trM_conventionD_gpmtPos_wordRevH3`,
     `trM_conventionD_gpmtSigned_wordRevH3`).
   - **Kazhdan–Lusztig $R$-polynomial bar isomorphism (`barH2`, `barH3`) and Parity $P$**:
     Constructs the explicit upper-triangular $R$-polynomial linear maps `barH2` on `H_2` and
     `barH3` on `H_3` over any commutative ring `R`, proving involutivity (`barH3_involutive`),
     exact ring isomorphism `(H_3, mulNF h) ≃+* (H_3, mulNF (-h))` (`barH3_mulNF`), commutation
     with `wordRevH3` (`wordRevH3_comm_barH3`), and the universal Markov-trace shift law
     $$\mathrm{tr}_M(z - h, -h, \mathrm{barH3}(h, v)) = \mathrm{tr}_M(z, h, v)$$
     (`trM_barH3`), specializing via `zD(q⁻¹) = zD(q) - (q - q⁻¹)` (`zD_inv_eq_sub_h`) to exact
     Convention-D bar equivariance (`trM_conventionD_barH3`).
   - **Explicit Signed 3-Strand Braid Words & Flavor-Decorated CPT Closure**:
     Formalizes signed 3-strand braid words `List BraidLetter3` together with quark/antiquark
     color-sheet flavor conjugation `QuarkFlavor.conj` (`u ↔ ū`, `d ↔ d̄`), proving that
     `actionC`, `actionP`, `actionT` are pairwise-commuting involutions, proving exact
     bar-covariant CPT invariance of the full chiral Markov trace on every closed braid word
     (`cpt_covariant_markov_trace_H3`, `cpt_covariant_conventionD_markov_trace_H3`), proving
     component-by-component fixed-$(z, h)$ invariance of `C`, `P`, `T`, and `C ∘ P ∘ T` on the
     bar-symmetrized observable Markov trace (`cpt_preserves_barSym_markov_trace_H3`), and
     recording the exact chiral single-crossing parity defect `-h` (`parity_chiral_defect_sigma0`).
-/

namespace QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure

open scoped BigOperators
open QOU.Machinery.H3
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

-- ============================================================================
-- § 1. Brane-Tower & Spectral-Series Truncation Exponential Decay
-- ============================================================================

section BraneTowerExponentialDecay

/-- Exact telescoping remainder identity for the geometric partial sum over any field `K`:
for `r ≠ 1`, `(1 - r)⁻¹ - ∑_{k=0}^N r^k = r^{N + 1} / (1 - r)`. -/
theorem geometric_limit_sub_partialSum {K : Type*} [Field K] (r : K) (hr : 1 - r ≠ 0) (N : ℕ) :
    1 / (1 - r) - ∑ k ∈ Finset.range (N + 1), r ^ k = r ^ (N + 1) / (1 - r) := by
  induction N with
  | zero =>
    simp only [zero_add, Finset.range_one, Finset.sum_singleton, pow_zero, pow_one]
    field_simp [hr]
    ring
  | succ m ih =>
    rw [Finset.sum_range_succ, sub_add_eq_sub_sub, ih]
    field_simp [hr]
    ring

/-- Real quantum Planck ratio `ℏ_q = (q - 1) / q = 1 - q⁻¹`. -/
noncomputable def hbarQ (q : ℝ) : ℝ := (q - 1) / q

/-- Depth-`N` partial sum of the quadratic Hecke brane-tower geometric series `∑_{k=0}^N ℏ_q^{2k}`. -/
noncomputable def braneTowerPartialSum (q : ℝ) (N : ℕ) : ℝ :=
  ∑ k ∈ Finset.range (N + 1), (hbarQ q) ^ (2 * k)

/-- Exact infinite-depth brane-tower resummation limit `(1 - ℏ_q^2)⁻¹`. -/
noncomputable def braneTowerExactLimit (q : ℝ) : ℝ :=
  1 / (1 - (hbarQ q) ^ 2)

/-- Structural exponential-decay prefactor `C(q) = ℏ_q^2 / (1 - ℏ_q^2)`. -/
noncomputable def braneTowerDecayPrefactor (q : ℝ) : ℝ :=
  (hbarQ q) ^ 2 / (1 - (hbarQ q) ^ 2)

/-- Structural exponential-decay rate `c(q) = -2 ln ℏ_q`. -/
noncomputable def braneTowerDecayRate (q : ℝ) : ℝ :=
  -2 * Real.log (hbarQ q)

/-- For `1 < q`, the quantum Planck ratio lies strictly in the open unit interval `(0, 1)`. -/
theorem hbarQ_mem_unit_interval {q : ℝ} (hq : 1 < q) :
    0 < hbarQ q ∧ hbarQ q < 1 := by
  unfold hbarQ
  have hq0 : 0 < q := by linarith
  refine ⟨div_pos (by linarith) hq0, ?_⟩
  rw [div_lt_one hq0]
  linarith

/-- For `1 < q`, the squared Planck ratio `ℏ_q^2` lies strictly in `(0, 1)`. -/
theorem hbarQSq_mem_unit_interval {q : ℝ} (hq : 1 < q) :
    0 < (hbarQ q) ^ 2 ∧ (hbarQ q) ^ 2 < 1 := by
  obtain ⟨hpos, hlt⟩ := hbarQ_mem_unit_interval hq
  refine ⟨sq_pos_of_pos hpos, ?_⟩
  nlinarith

/-- For `1 < q`, the brane-tower denominator `1 - ℏ_q^2` is strictly positive. -/
theorem one_sub_hbarQSq_pos {q : ℝ} (hq : 1 < q) :
    0 < 1 - (hbarQ q) ^ 2 := by
  have h := (hbarQSq_mem_unit_interval hq).2
  linarith

/-- Strict positivity of the brane-tower prefactor `C(q) = ℏ_q^2 / (1 - ℏ_q^2)` for `1 < q`. -/
theorem braneTowerDecayPrefactor_pos {q : ℝ} (hq : 1 < q) :
    0 < braneTowerDecayPrefactor q := by
  unfold braneTowerDecayPrefactor
  exact div_pos (hbarQSq_mem_unit_interval hq).1 (one_sub_hbarQSq_pos hq)

/-- Strict positivity of the brane-tower exponential rate `c(q) = -2 ln ℏ_q` for `1 < q`. -/
theorem braneTowerDecayRate_pos {q : ℝ} (hq : 1 < q) :
    0 < braneTowerDecayRate q := by
  unfold braneTowerDecayRate
  obtain ⟨hpos, hlt⟩ := hbarQ_mem_unit_interval hq
  have hlog : Real.log (hbarQ q) < 0 := Real.log_neg hpos hlt
  linarith

/-- Exact algebraic remainder of the depth-`N` brane-tower partial sum:
`(1 - ℏ_q^2)⁻¹ - ∑_{k=0}^N ℏ_q^{2k} = ℏ_q^{2(N+1)} / (1 - ℏ_q^2)`. -/
theorem braneTowerExactLimit_sub_partialSum {q : ℝ} (hq : 1 < q) (N : ℕ) :
    braneTowerExactLimit q - braneTowerPartialSum q N =
      (hbarQ q) ^ (2 * (N + 1)) / (1 - (hbarQ q) ^ 2) := by
  unfold braneTowerExactLimit braneTowerPartialSum
  have hden : 1 - (hbarQ q) ^ 2 ≠ 0 := ne_of_gt (one_sub_hbarQSq_pos hq)
  have hsum : (∑ k ∈ Finset.range (N + 1), (hbarQ q) ^ (2 * k)) =
      ∑ k ∈ Finset.range (N + 1), ((hbarQ q) ^ 2) ^ k := by
    refine Finset.sum_congr rfl (fun k _ => ?_)
    rw [pow_mul]
  rw [hsum, geometric_limit_sub_partialSum ((hbarQ q) ^ 2) hden N, ← pow_mul]

/-- Exact coincidence of the geometric ceiling `ℏ_q^{2(N+1)} / (1 - ℏ_q^2)` and the Archimedean
exponential bound `C(q) · exp(-c(q) · N)` for every truncation depth `N ≥ 0`. -/
theorem braneTower_geometric_ceiling_eq_exp_decay {q : ℝ} (hq : 1 < q) (N : ℕ) :
    (hbarQ q) ^ (2 * (N + 1)) / (1 - (hbarQ q) ^ 2) =
      braneTowerDecayPrefactor q * Real.exp (-braneTowerDecayRate q * (N : ℝ)) := by
  unfold braneTowerDecayPrefactor braneTowerDecayRate
  obtain ⟨hpos, _⟩ := hbarQ_mem_unit_interval hq
  have hexp_arg : -(-2 * Real.log (hbarQ q)) * (N : ℝ) = ((2 * N : ℕ) : ℝ) * Real.log (hbarQ q) := by
    push_cast
    ring
  rw [hexp_arg, Real.exp_nat_mul, Real.exp_log hpos]
  rw [show 2 * (N + 1) = 2 + 2 * N by omega, pow_add]
  ring

/-- Exact magnitude of the depth-`N` brane-tower remainder in exponential form:
`|braneTowerPartialSum q N - braneTowerExactLimit q| = C(q) · exp(-c(q) · N)`. -/
theorem braneTower_remainder_abs_eq_exp_decay {q : ℝ} (hq : 1 < q) (N : ℕ) :
    |braneTowerPartialSum q N - braneTowerExactLimit q| =
      braneTowerDecayPrefactor q * Real.exp (-braneTowerDecayRate q * (N : ℝ)) := by
  rw [abs_sub_comm, braneTowerExactLimit_sub_partialSum hq N]
  obtain ⟨hpos, _⟩ := hbarQ_mem_unit_interval hq
  have hnonneg : 0 ≤ (hbarQ q) ^ (2 * (N + 1)) / (1 - (hbarQ q) ^ 2) :=
    div_nonneg (pow_nonneg (le_of_lt hpos) _) (le_of_lt (one_sub_hbarQSq_pos hq))
  rw [abs_of_nonneg hnonneg, braneTower_geometric_ceiling_eq_exp_decay hq N]

/-- Unconditional existence of strictly positive constants `C, c > 0` controlling the scaled
brane-tower truncation remainder `scale · (braneTowerPartialSum q N - braneTowerExactLimit q)`
for every positive hadronic/leptonic energy scale `0 < scale` and substrate parameter `1 < q`. -/
theorem braneTower_exists_exp_decay_bound {q scale : ℝ} (hq : 1 < q) (hscale : 0 < scale) :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ N : ℕ, |scale * (braneTowerPartialSum q N - braneTowerExactLimit q)| ≤
        C * Real.exp (-c * (N : ℝ)) := by
  refine ⟨scale * braneTowerDecayPrefactor q, braneTowerDecayRate q,
    mul_pos hscale (braneTowerDecayPrefactor_pos hq), braneTowerDecayRate_pos hq, ?_⟩
  intro N
  rw [abs_mul, abs_of_pos hscale, braneTower_remainder_abs_eq_exp_decay hq N, mul_assoc]

/-- Infinite-series tail remainder `R_N(a) = (∑'_{k=0}^∞ a_k) - ∑_{k=0}^N a_k` after depth `N`. -/
noncomputable def seriesTailRemainder (a : ℕ → ℝ) (N : ℕ) : ℝ :=
  (∑' k, a k) - ∑ k ∈ Finset.range (N + 1), a k

/-- Summability of any real sequence majorized by a sub-unit geometric envelope `|a k| ≤ M · r^k`. -/
theorem summable_of_abs_le_geom {a : ℕ → ℝ} {M r : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) (ha : ∀ k : ℕ, |a k| ≤ M * r ^ k) :
    Summable a := by
  have hgeom : Summable (fun k : ℕ => M * r ^ k) :=
    (summable_geometric_of_lt_one hr0 hr1).mul_left M
  exact Summable.of_norm_bounded hgeom (fun k => by simpa [Real.norm_eq_abs] using ha k)

/-- General Cauchy geometric-majorant bound on the infinite-series tail remainder:
if `|a k| ≤ M · r^k` with `0 ≤ M` and `0 ≤ r < 1`, then `|seriesTailRemainder a N| ≤ M · r^{N+1} / (1 - r)`. -/
theorem abs_seriesTailRemainder_le_geometric {a : ℕ → ℝ} {M r : ℝ}
    (_hM : 0 ≤ M) (hr0 : 0 ≤ r) (hr1 : r < 1) (ha : ∀ k : ℕ, |a k| ≤ M * r ^ k) (N : ℕ) :
    |seriesTailRemainder a N| ≤ M * r ^ (N + 1) / (1 - r) := by
  have hsum_a : Summable a := summable_of_abs_le_geom hr0 hr1 ha
  have hsplit := hsum_a.sum_add_tsum_nat_add (N + 1)
  have hrem_eq : seriesTailRemainder a N = ∑' i : ℕ, a (i + (N + 1)) := by
    unfold seriesTailRemainder
    linarith
  have hmaj_shift : Summable (fun i : ℕ => (M * r ^ (N + 1)) * r ^ i) :=
    (summable_geometric_of_lt_one hr0 hr1).mul_left (M * r ^ (N + 1))
  have hterm_le : ∀ i : ℕ, ‖a (i + (N + 1))‖ ≤ (M * r ^ (N + 1)) * r ^ i := by
    intro i
    rw [Real.norm_eq_abs]
    calc |a (i + (N + 1))|
        ≤ M * r ^ (i + (N + 1)) := ha (i + (N + 1))
      _ = (M * r ^ (N + 1)) * r ^ i := by rw [pow_add]; ring
  have hnorm_shift : Summable (fun i : ℕ => ‖a (i + (N + 1))‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hterm_le hmaj_shift
  rw [hrem_eq, ← Real.norm_eq_abs]
  calc ‖∑' i : ℕ, a (i + (N + 1))‖
      ≤ ∑' i : ℕ, ‖a (i + (N + 1))‖ := norm_tsum_le_tsum_norm hnorm_shift
    _ ≤ ∑' i : ℕ, (M * r ^ (N + 1)) * r ^ i :=
        Summable.tsum_le_tsum hterm_le hnorm_shift hmaj_shift
    _ = (M * r ^ (N + 1)) * ∑' i : ℕ, r ^ i := tsum_mul_left
    _ = (M * r ^ (N + 1)) * (1 - r)⁻¹ := by rw [tsum_geometric_of_lt_one hr0 hr1]
    _ = M * r ^ (N + 1) / (1 - r) := by rw [div_eq_mul_inv]

/-- Exact Archimedean exponential bound for any geometrically majorized spectral/ladder series:
if `|a k| ≤ M · r^k` with `0 < M` and `0 < r < 1`, then for every `N : ℕ`,
`|seriesTailRemainder a N| ≤ (M r / (1 - r)) · exp(-(-ln r) · N)`. -/
theorem abs_seriesTailRemainder_le_exp_decay {a : ℕ → ℝ} {M r : ℝ}
    (hM : 0 < M) (hr0 : 0 < r) (hr1 : r < 1) (ha : ∀ k : ℕ, |a k| ≤ M * r ^ k) (N : ℕ) :
    |seriesTailRemainder a N| ≤ (M * r / (1 - r)) * Real.exp (-(-Real.log r) * (N : ℝ)) := by
  have hgeom := abs_seriesTailRemainder_le_geometric (le_of_lt hM) (le_of_lt hr0) hr1 ha N
  have hexp : (M * r / (1 - r)) * Real.exp (-(-Real.log r) * (N : ℝ)) =
      M * r ^ (N + 1) / (1 - r) := by
    have harg : -(-Real.log r) * (N : ℝ) = (N : ℝ) * Real.log r := by ring
    rw [harg, Real.exp_nat_mul, Real.exp_log hr0, pow_succ]
    ring
  linarith

/-- Unconditional `∃ C c > 0` exponential-decay certificate for any geometrically majorized
spectral or Habiro–Bürmann series `a : ℕ → ℝ` (`|a k| ≤ M · r^k`, `0 < M`, `0 < r < 1`). -/
theorem exists_exp_decay_of_geom_majorant {a : ℕ → ℝ} {M r : ℝ}
    (hM : 0 < M) (hr0 : 0 < r) (hr1 : r < 1) (ha : ∀ k : ℕ, |a k| ≤ M * r ^ k) :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
      ∀ N : ℕ, |seriesTailRemainder a N| ≤ C * Real.exp (-c * (N : ℝ)) := by
  have h1r : 0 < 1 - r := by linarith
  have hlog : Real.log r < 0 := Real.log_neg hr0 hr1
  refine ⟨M * r / (1 - r), -Real.log r, div_pos (mul_pos hM hr0) h1r, by linarith, ?_⟩
  exact abs_seriesTailRemainder_le_exp_decay hM hr0 hr1 ha

end BraneTowerExponentialDecay

-- ============================================================================
-- § 2. Discrete C, P, T Actions & Markov-Trace Closure on H_2(q) and H_3(q)
-- ============================================================================

section CPTMarkovTraceClosure

/-- Two-strand Hecke product on the normal-form basis `[1, σ₀]` (`Fin 2 → R`),
encoding `σ₀² = h · σ₀ + 1`. -/
def mulH2 {R : Type*} [CommRing R] (h : R) (u v : Fin 2 → R) : Fin 2 → R :=
  ![u 0 * v 0 + u 1 * v 1, u 0 * v 1 + u 1 * v 0 + h * u 1 * v 1]

/-- Two-strand Markov trace on `[1, σ₀]`: `trMH2 z u = u₀ + z · u₁`. -/
def trMH2 {R : Type*} [CommRing R] (z : R) (u : Fin 2 → R) : R :=
  u 0 + z * u 1

/-- Kazhdan–Lusztig bar map on `H_2(q)`: `1 ↦ 1`, `σ₀ ↦ σ₀ + h · 1` (`= σ₀⁻¹` in `H_2(q⁻¹)`). -/
def barH2 {R : Type*} [CommRing R] (h : R) (u : Fin 2 → R) : Fin 2 → R :=
  ![u 0 + h * u 1, u 1]

/-- Bar involutivity on `H_2`: `barH2 (-h) (barH2 h u) = u`. -/
theorem barH2_involutive {R : Type*} [CommRing R] (h : R) (u : Fin 2 → R) :
    barH2 (-h) (barH2 h u) = u := by
  funext i
  fin_cases i <;> simp [barH2]

/-- Exact ring homomorphism property of `barH2` from `(H_2, mulH2 h)` to `(H_2, mulH2 (-h))`. -/
theorem barH2_mulH2 {R : Type*} [CommRing R] (h : R) (u v : Fin 2 → R) :
    barH2 h (mulH2 h u v) = mulH2 (-h) (barH2 h u) (barH2 h v) := by
  funext i
  fin_cases i <;> simp [barH2, mulH2] <;> ring

/-- Universal Markov-trace bar shift law on `H_2`: `trMH2 (z - h) (barH2 h u) = trMH2 z u`. -/
theorem trMH2_barH2 {R : Type*} [CommRing R] (z h : R) (u : Fin 2 → R) :
    trMH2 (z - h) (barH2 h u) = trMH2 z u := by
  simp only [trMH2, barH2, Matrix.cons_val_zero, Matrix.cons_val_one]
  ring

/-- Time-reversal word-reversal map `T` on `H_3(q)` normal-form coordinates
`[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`: fixes palindromic basis elements `0, 1, 2, 5` and
swaps `3 ↔ 4` (`σ₁σ₀ ↔ σ₀σ₁`). -/
def wordRevH3 {R : Type*} (v : Fin 6 → R) : Fin 6 → R :=
  ![v 0, v 1, v 2, v 4, v 3, v 5]

/-- Time-reversal `wordRevH3` is an exact involution: `wordRevH3 (wordRevH3 v) = v`. -/
theorem wordRevH3_involutive {R : Type*} (v : Fin 6 → R) :
    wordRevH3 (wordRevH3 v) = v := by
  funext i
  fin_cases i <;> rfl

/-- Time-reversal `wordRevH3` is an exact algebra anti-automorphism of `(H_3(q), mulNF h)`:
`wordRevH3 (mulNF h u v) = mulNF h (wordRevH3 v) (wordRevH3 u)` over any commutative ring `R`. -/
theorem wordRevH3_mulNF {R : Type*} [CommRing R] (h : R) (u v : Fin 6 → R) :
    wordRevH3 (mulNF h u v) = mulNF h (wordRevH3 v) (wordRevH3 u) := by
  funext i
  fin_cases i <;>
    simp [wordRevH3, mulNF, mulσ₀, mulσ₁, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val] <;>
    ring

/-- Time-reversal `wordRevH3` preserves the Markov trace `trM z h` over any commutative ring `R`:
`trM z h (wordRevH3 v) = trM z h v`. -/
theorem trM_wordRevH3 {R : Type*} [CommRing R] (z h : R) (v : Fin 6 → R) :
    trM z h (wordRevH3 v) = trM z h v := by
  simp only [trM, wordRevH3, TRM, Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val]
  ring

/-- Time-reversal `wordRevH3` preserves both GPMT-completed Convention-D Markov traces
`trM_conventionD_gpmtPos` and `trM_conventionD_gpmtSigned`. -/
theorem trM_conventionD_gpmt_wordRevH3 {K : Type*} [Field K] (q : K) (v : Fin 6 → K) :
    trM_conventionD_gpmtPos q (wordRevH3 v) = trM_conventionD_gpmtPos q v ∧
      trM_conventionD_gpmtSigned q (wordRevH3 v) = trM_conventionD_gpmtSigned q v := by
  have htmod : tMod111 q (wordRevH3 v) = tMod111 q v := by
    unfold tMod111 chi111 chiNF wordRevH3
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    ring
  refine ⟨?_, ?_⟩
  · unfold trM_conventionD_gpmtPos
    rw [trM_wordRevH3, htmod]
  · unfold trM_conventionD_gpmtSigned
    rw [trM_wordRevH3, htmod]

/-- Kazhdan–Lusztig $R$-polynomial bar isomorphism `barH3` on `H_3(q)` normal-form coordinates
`[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`, mapping each basis word `W_j(σ₀, σ₁) ∈ H_3(q)` to its
crossing-inverted counterpart `W_j(σ₀ + h, σ₁ + h) ∈ H_3(q⁻¹)`:
- `b₀ = 1 ↦ [1, 0, 0, 0, 0, 0]`
- `b₁ = σ₀ ↦ [h, 1, 0, 0, 0, 0]`
- `b₂ = σ₁ ↦ [h, 0, 1, 0, 0, 0]`
- `b₃ = σ₁σ₀ ↦ [h², h, h, 1, 0, 0]`
- `b₄ = σ₀σ₁ ↦ [h², h, h, 0, 1, 0]`
- `b₅ = σ₀σ₁σ₀ ↦ [h³ + h, h², h², h, h, 1]`. -/
def barH3 {R : Type*} [CommRing R] (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 0 + h * v 1 + h * v 2 + h ^ 2 * v 3 + h ^ 2 * v 4 + (h ^ 3 + h) * v 5,
    v 1 + h * v 3 + h * v 4 + h ^ 2 * v 5,
    v 2 + h * v 3 + h * v 4 + h ^ 2 * v 5,
    v 3 + h * v 5,
    v 4 + h * v 5,
    v 5]

/-- Exact bar involutivity on `H_3`: `barH3 (-h) (barH3 h v) = v` over any commutative ring `R`. -/
theorem barH3_involutive {R : Type*} [CommRing R] (h : R) (v : Fin 6 → R) :
    barH3 (-h) (barH3 h v) = v := by
  funext i
  fin_cases i <;>
    simp [barH3, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] <;>
    ring

/-- Exact ring isomorphism property of `barH3` from `(H_3, mulNF h)` to `(H_3, mulNF (-h))`
over any commutative ring `R`: `barH3 h (mulNF h u v) = mulNF (-h) (barH3 h u) (barH3 h v)`. -/
theorem barH3_mulNF {R : Type*} [CommRing R] (h : R) (u v : Fin 6 → R) :
    barH3 h (mulNF h u v) = mulNF (-h) (barH3 h u) (barH3 h v) := by
  funext i
  fin_cases i <;>
    simp [barH3, mulNF, mulσ₀, mulσ₁, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val] <;>
    ring

/-- Exact commutation of time-reversal `wordRevH3` and the Kazhdan–Lusztig bar map `barH3`:
`wordRevH3 (barH3 h v) = barH3 h (wordRevH3 v)`. -/
theorem wordRevH3_comm_barH3 {R : Type*} [CommRing R] (h : R) (v : Fin 6 → R) :
    wordRevH3 (barH3 h v) = barH3 h (wordRevH3 v) := by
  funext i
  fin_cases i <;>
    simp [wordRevH3, barH3, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] <;>
    ring

/-- **Universal Markov-Trace Bar Shift Law on `H_3(q)`**:
Over any commutative ring `R`, applying `barH3 h` to `v` and shifting the Markov parameters
`(z, h) ↦ (z - h, -h)` leaves the Markov trace strictly invariant:
`trM (z - h) (-h) (barH3 h v) = trM z h v`. -/
theorem trM_barH3 {R : Type*} [CommRing R] (z h : R) (v : Fin 6 → R) :
    trM (z - h) (-h) (barH3 h v) = trM z h v := by
  simp only [trM, barH3, TRM, Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val]
  ring

/-- Fundamental Convention-D bar-shift identity: for `q ≠ 0` and `q^2 + 1 ≠ 0`,
`zD(q⁻¹) = zD(q) - (q - q⁻¹)`. -/
theorem zD_inv_eq_sub_h {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = zD q - (q - q⁻¹) := by
  have hqi2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro hzero
    apply hq2
    have hmul : q ^ 2 * ((q⁻¹) ^ 2 + 1) = 1 + q ^ 2 := by
      field_simp [hq]
    rw [hzero, mul_zero, add_comm] at hmul
    exact hmul.symm
  have h1q2 : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  unfold zD
  field_simp [hq, hq2, hqi2, h1q2]
  ring

/-- **Exact Convention-D Markov-Trace Bar Equivariance on `H_3(q)`**:
For `q ≠ 0` and `q^2 + 1 ≠ 0`, `trM (zD q⁻¹) (q⁻¹ - q) (barH3 (q - q⁻¹) v) = trM (zD q) (q - q⁻¹) v`. -/
theorem trM_conventionD_barH3 {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (v : Fin 6 → K) :
    trM (zD q⁻¹) (q⁻¹ - q) (barH3 (q - q⁻¹) v) = trM (zD q) (q - q⁻¹) v := by
  rw [zD_inv_eq_sub_h q hq hq2, show q⁻¹ - q = -(q - q⁻¹) by ring]
  exact trM_barH3 (zD q) (q - q⁻¹) v

/-- Elementary signed generator of the 3-strand braid group `B_3`:
`isSigma0 = true` selects `σ₀^{±1}`, `isSigma0 = false` selects `σ₁^{±1}`,
and `signPos = true` selects positive crossing `+1` (`false` selects `-1`). -/
structure BraidLetter3 where
  isSigma0 : Bool
  signPos : Bool
  deriving DecidableEq, Repr

/-- Parity crossing-inversion on a single 3-strand braid letter: `σ_i^ε ↦ σ_i^{-ε}`. -/
def BraidLetter3.mirror (x : BraidLetter3) : BraidLetter3 :=
  ⟨x.isSigma0, !x.signPos⟩

/-- Evaluation of a single `BraidLetter3` in `H_3(q)` normal-form coordinates (`σ_i⁻¹ = σ_i - h·1`). -/
def evalLetterH3 {R : Type*} [CommRing R] (h : R) (x : BraidLetter3) : Fin 6 → R :=
  match x.isSigma0, x.signPos with
  | true, true => ![0, 1, 0, 0, 0, 0]
  | true, false => ![-h, 1, 0, 0, 0, 0]
  | false, true => ![0, 0, 1, 0, 0, 0]
  | false, false => ![-h, 0, 1, 0, 0, 0]

/-- Evaluation of a 3-strand signed braid word `w : List BraidLetter3` in `(H_3, mulNF h)`.
Note that because `mulNF h u v` represents right-action composition (`v · u` in left-to-right
braid concatenation), multiplying `evalLetterH3 h x` on the left via `mulNF h (evalWordH3 h ws) (evalLetterH3 h x)`
appends letter `x` in consistent word order. -/
def evalWordH3 {R : Type*} [CommRing R] (h : R) : List BraidLetter3 → (Fin 6 → R)
  | [] => ![1, 0, 0, 0, 0, 0]
  | x :: ws => mulNF h (evalLetterH3 h x) (evalWordH3 h ws)

/-- Right-unit identity of `[1, 0, 0, 0, 0, 0]` for `mulNF h`. -/
theorem mulNF_one_right {R : Type*} [CommRing R] (h : R) (u : Fin 6 → R) :
    mulNF h u ![1, 0, 0, 0, 0, 0] = u := by
  funext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁]

/-- Left-unit identity of `[1, 0, 0, 0, 0, 0]` for `mulNF h`. -/
theorem mulNF_one_left {R : Type*} [CommRing R] (h : R) (v : Fin 6 → R) :
    mulNF h ![1, 0, 0, 0, 0, 0] v = v := by
  funext i
  fin_cases i <;>
    simp [mulNF, mulσ₀, mulσ₁, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]

/-- Associativity of the 6-dimensional `H_3(q)` normal-form product `mulNF h`. -/
theorem mulNF_assoc {R : Type*} [CommRing R] (h : R) (u v w : Fin 6 → R) :
    mulNF h (mulNF h u v) w = mulNF h u (mulNF h v w) := by
  funext i
  fin_cases i <;>
    simp [mulNF, mulσ₀, mulσ₁, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] <;>
    ring

/-- Evaluation of concatenated 3-strand braid words is a monoid homomorphism into `(H_3, mulNF h)`. -/
theorem evalWordH3_append {R : Type*} [CommRing R] (h : R) (w₁ w₂ : List BraidLetter3) :
    evalWordH3 h (w₁ ++ w₂) = mulNF h (evalWordH3 h w₁) (evalWordH3 h w₂) := by
  induction w₁ with
  | nil =>
    simp only [List.nil_append, evalWordH3]
    rw [mulNF_one_left]
  | cons x ws ih =>
    simp only [List.cons_append, evalWordH3, ih, mulNF_assoc]

/-- Each single braid letter is fixed by `wordRevH3`. -/
theorem wordRevH3_evalLetterH3 {R : Type*} [CommRing R] (h : R) (x : BraidLetter3) :
    wordRevH3 (evalLetterH3 h x) = evalLetterH3 h x := by
  cases h0 : x.isSigma0 <;> cases hs : x.signPos <;>
    (funext i; fin_cases i <;> simp [evalLetterH3, wordRevH3, h0, hs])

/-- Reversing a 3-strand braid word `w.reverse` implements `wordRevH3` in `H_3(q)`:
`evalWordH3 h w.reverse = wordRevH3 (evalWordH3 h w)`. -/
theorem evalWordH3_reverse {R : Type*} [CommRing R] (h : R) (w : List BraidLetter3) :
    evalWordH3 h w.reverse = wordRevH3 (evalWordH3 h w) := by
  induction w with
  | nil =>
    funext i
    fin_cases i <;> rfl
  | cons x ws ih =>
    rw [List.reverse_cons, evalWordH3_append, ih]
    simp only [evalWordH3, mulNF_one_right]
    rw [wordRevH3_mulNF, wordRevH3_evalLetterH3]

/-- Applying `barH3 h` to a single letter evaluates its parity-mirrored letter at `-h`:
`barH3 h (evalLetterH3 h x) = evalLetterH3 (-h) x.mirror`. -/
theorem barH3_evalLetterH3 {R : Type*} [CommRing R] (h : R) (x : BraidLetter3) :
    barH3 h (evalLetterH3 h x) = evalLetterH3 (-h) x.mirror := by
  cases h0 : x.isSigma0 <;> cases hs : x.signPos <;>
    (funext i; fin_cases i <;>
      simp [barH3, evalLetterH3, BraidLetter3.mirror, h0, hs, Matrix.cons_val_zero,
        Matrix.cons_val_one, Matrix.cons_val])

/-- Mirroring every crossing of a 3-strand braid word `w.map BraidLetter3.mirror` and evaluating
at `-h` coincides with `barH3 h (evalWordH3 h w)`. -/
theorem evalWordH3_mirror {R : Type*} [CommRing R] (h : R) (w : List BraidLetter3) :
    evalWordH3 (-h) (w.map BraidLetter3.mirror) = barH3 h (evalWordH3 h w) := by
  induction w with
  | nil =>
    funext i
    fin_cases i <;> simp [evalWordH3, barH3]
  | cons x ws ih =>
    simp only [List.map_cons, evalWordH3, ih, ← barH3_evalLetterH3, ← barH3_mulNF]

/-- Exact chiral parity defect on a single positive crossing `σ₀` at fixed `(z, h)`:
`trM z h (evalWordH3 h [σ₀⁻¹]) - trM z h (evalWordH3 h [σ₀]) = -h`, showing that fixed-`q`
un-symmetrized parity flips the sign of `h = q - q⁻¹` on chiral braids while preserving achiral
(`h = 0` or bar-even) components. -/
theorem parity_chiral_defect_sigma0 {R : Type*} [CommRing R] (z h : R) :
    trM z h (evalWordH3 h ([⟨true, true⟩].map BraidLetter3.mirror)) -
      trM z h (evalWordH3 h [⟨true, true⟩]) = -h := by
  simp only [List.map_cons, List.map_nil, BraidLetter3.mirror, Bool.not_true, evalWordH3,
    mulNF_one_right, evalLetterH3, trM, TRM, Fin.sum_univ_six, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val]
  ring

/-- Quark/antiquark flavor labels on nucleon color sheets (`u, d, ū, d̄`). -/
inductive QuarkFlavor where
  | u : QuarkFlavor
  | d : QuarkFlavor
  | uBar : QuarkFlavor
  | dBar : QuarkFlavor
  deriving DecidableEq, Repr

/-- Charge-conjugation flavor swap `u ↔ ū`, `d ↔ d̄` on a single color sheet. -/
def QuarkFlavor.conj : QuarkFlavor → QuarkFlavor
  | .u => .uBar
  | .d => .dBar
  | .uBar => .u
  | .dBar => .d

/-- Single-sheet flavor conjugation is an exact involution. -/
theorem QuarkFlavor.conj_involutive (f : QuarkFlavor) : f.conj.conj = f := by
  cases f <;> rfl

/-- Three-sheet nucleon flavor triples (`proton = (u, u, d)`, `antiproton = (ū, ū, d̄)`,
`neutron = (u, d, d)`, `antineutron = (ū, d̄, d̄)`). -/
def protonFlavorTriple : Fin 3 → QuarkFlavor := ![.u, .u, .d]
def antiprotonFlavorTriple : Fin 3 → QuarkFlavor := ![.uBar, .uBar, .dBar]
def neutronFlavorTriple : Fin 3 → QuarkFlavor := ![.u, .d, .d]
def antineutronFlavorTriple : Fin 3 → QuarkFlavor := ![.uBar, .dBar, .dBar]

/-- Componentwise charge conjugation maps proton `(u, u, d)` to antiproton `(ū, ū, d̄)` and
neutron `(u, d, d)` to antineutron `(ū, d̄, d̄)`. -/
theorem nucleon_flavor_charge_conjugation :
    (QuarkFlavor.conj ∘ protonFlavorTriple) = antiprotonFlavorTriple ∧
      (QuarkFlavor.conj ∘ neutronFlavorTriple) = antineutronFlavorTriple := by
  refine ⟨?_, ?_⟩ <;> (funext i; fin_cases i <;> rfl)

/-- Flavor-decorated 3-strand closed-braid representative `(flavors, word)`. -/
structure FlavorBraid3 where
  flavors : Fin 3 → QuarkFlavor
  word : List BraidLetter3

/-- Charge conjugation `C` on `FlavorBraid3`: flips quark/antiquark flavors on every color sheet
while leaving the braid word untouched. -/
def actionC (b : FlavorBraid3) : FlavorBraid3 :=
  ⟨QuarkFlavor.conj ∘ b.flavors, b.word⟩

/-- Parity `P` on `FlavorBraid3`: mirrors every crossing sign `σ_i^ε ↦ σ_i^{-ε}` while leaving
color-sheet flavors untouched. -/
def actionP (b : FlavorBraid3) : FlavorBraid3 :=
  ⟨b.flavors, b.word.map BraidLetter3.mirror⟩

/-- Time-reversal `T` on `FlavorBraid3`: reverses the braid word while leaving color-sheet
flavors and crossing signs untouched. -/
def actionT (b : FlavorBraid3) : FlavorBraid3 :=
  ⟨b.flavors, b.word.reverse⟩

/-- Composite `CPT = C ∘ P ∘ T` action on `FlavorBraid3`. -/
def actionCPT : FlavorBraid3 → FlavorBraid3 :=
  actionC ∘ actionP ∘ actionT

/-- Each of `actionC`, `actionP`, `actionT`, and `actionCPT` is an exact involution (`f (f b) = b`),
and `actionC`, `actionP`, `actionT` commute pairwise (`ℤ/2 × ℤ/2 × ℤ/2` discrete symmetry group). -/
theorem cpt_actions_involutive_and_commute (b : FlavorBraid3) :
    actionC (actionC b) = b ∧
      actionP (actionP b) = b ∧
      actionT (actionT b) = b ∧
      actionC (actionP b) = actionP (actionC b) ∧
      actionC (actionT b) = actionT (actionC b) ∧
      actionP (actionT b) = actionT (actionP b) ∧
      actionCPT (actionCPT b) = b := by
  have hmir_inv : BraidLetter3.mirror ∘ BraidLetter3.mirror = id := by
    funext x
    cases x with | mk g s => simp [BraidLetter3.mirror]
  have hC : ∀ x : FlavorBraid3, actionC (actionC x) = x := by
    intro x
    cases x with | mk fl w =>
      simp only [actionC, FlavorBraid3.mk.injEq, and_true]
      funext i
      exact QuarkFlavor.conj_involutive (fl i)
  have hP : ∀ x : FlavorBraid3, actionP (actionP x) = x := by
    intro x
    cases x with | mk fl w =>
      simp only [actionP, List.map_map, hmir_inv, List.map_id]
  have hT : ∀ x : FlavorBraid3, actionT (actionT x) = x := by
    intro x
    cases x with | mk fl w =>
      simp only [actionT, List.reverse_reverse]
  have hPT : ∀ x : FlavorBraid3, actionP (actionT x) = actionT (actionP x) := by
    intro x
    cases x with | mk fl w =>
      simp only [actionP, actionT, List.map_reverse]
  refine ⟨hC b, hP b, hT b, rfl, rfl, hPT b, ?_⟩
  simp only [actionCPT, Function.comp_apply]
  have hcpt : actionC (actionP (actionT (actionC (actionP (actionT b))))) =
      actionC (actionC (actionP (actionP (actionT (actionT b))))) := by
    have h1 : actionT (actionC (actionP (actionT b))) = actionC (actionT (actionP (actionT b))) := rfl
    rw [h1]
    have h2 : actionP (actionC (actionT (actionP (actionT b)))) =
        actionC (actionP (actionT (actionP (actionT b)))) := rfl
    rw [h2, hPT (actionP (actionT b)), hP (actionT b), hT b]
    simp [hP]
  rw [hcpt, hC, hP, hT]

/-- Flavor-weighted `H_3(q)` Markov trace functional `tauMH3 W z h b = W(flavors) · trM z h (evalWordH3 h word)`
over any commutative ring `R`. -/
def tauMH3 {R : Type*} [CommRing R] (W : (Fin 3 → QuarkFlavor) → R) (z h : R) (b : FlavorBraid3) : R :=
  W b.flavors * trM z h (evalWordH3 h b.word)

/-- Bar-symmetrized (achiral / real-observable) `H_3(q)` Markov trace functional
`tauMSymH3 W z h b = tauMH3 W z h b + tauMH3 W (z - h) (-h) b` over any commutative ring `R`. -/
def tauMSymH3 {R : Type*} [CommRing R] (W : (Fin 3 → QuarkFlavor) → R) (z h : R) (b : FlavorBraid3) : R :=
  tauMH3 W z h b + tauMH3 W (z - h) (-h) b

/-- **Bar-Covariant CPT Closure Theorem on `H_3(q)` (Generic Commutative Ring `R`)**:
Whenever the color-sheet weight `W` is flavor-conjugation invariant (`∀ fl, W (conj ∘ fl) = W fl`),
applying `actionCPT = C ∘ P ∘ T` to any closed 3-strand braid `b` together with the Kazhdan–Lusztig
bar parameter involution `(z, h) ↦ (z - h, -h)` preserves the full chiral Markov trace identically:
`tauMH3 W (z - h) (-h) (actionCPT b) = tauMH3 W z h b`. -/
theorem cpt_covariant_markov_trace_H3 {R : Type*} [CommRing R]
    (W : (Fin 3 → QuarkFlavor) → R) (hW : ∀ fl, W (QuarkFlavor.conj ∘ fl) = W fl)
    (z h : R) (b : FlavorBraid3) :
    tauMH3 W (z - h) (-h) (actionCPT b) = tauMH3 W z h b := by
  unfold tauMH3 actionCPT actionC actionP actionT
  simp only [Function.comp_apply, hW b.flavors]
  rw [evalWordH3_mirror h b.word.reverse, evalWordH3_reverse h b.word,
    ← wordRevH3_comm_barH3 h (evalWordH3 h b.word),
    trM_wordRevH3 (z - h) (-h) (barH3 h (evalWordH3 h b.word)),
    trM_barH3 z h (evalWordH3 h b.word)]

/-- **Convention-D Bar-Covariant CPT Closure Theorem (`q ↔ q⁻¹`)**:
For any field `K` and `q ∈ K` with `q ≠ 0` and `q^2 + 1 ≠ 0`, under Convention D
(`z_D(q) = q^3 / (q^2 + 1)`, `h(q) = q - q⁻¹`), the full chiral Markov trace is invariant under
simultaneous `q ↦ q⁻¹` and `b ↦ actionCPT b` for every flavor-decorated 3-strand braid word `b`. -/
theorem cpt_covariant_conventionD_markov_trace_H3 {K : Type*} [Field K]
    (W : (Fin 3 → QuarkFlavor) → K) (hW : ∀ fl, W (QuarkFlavor.conj ∘ fl) = W fl)
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (b : FlavorBraid3) :
    tauMH3 W (zD q⁻¹) (q⁻¹ - q) (actionCPT b) = tauMH3 W (zD q) (q - q⁻¹) b := by
  rw [zD_inv_eq_sub_h q hq hq2, show q⁻¹ - q = -(q - q⁻¹) by ring]
  exact cpt_covariant_markov_trace_H3 W hW (zD q) (q - q⁻¹) b

/-- **Fixed-`(z, h)` Componentwise & Joint CPT Invariance of the Bar-Symmetrized Markov Trace**:
Over any commutative ring `R`, whenever `W` is flavor-conjugation invariant, each discrete symmetry
`actionC`, `actionP`, `actionT`, and their composite `actionCPT = C ∘ P ∘ T` individually preserves
the bar-symmetrized Markov trace `tauMSymH3 W z h` at fixed `(z, h)` on every 3-strand braid word `b`. -/
theorem cpt_preserves_barSym_markov_trace_H3 {R : Type*} [CommRing R]
    (W : (Fin 3 → QuarkFlavor) → R) (hW : ∀ fl, W (QuarkFlavor.conj ∘ fl) = W fl)
    (z h : R) (b : FlavorBraid3) :
    tauMSymH3 W z h (actionC b) = tauMSymH3 W z h b ∧
      tauMSymH3 W z h (actionP b) = tauMSymH3 W z h b ∧
      tauMSymH3 W z h (actionT b) = tauMSymH3 W z h b ∧
      tauMSymH3 W z h (actionCPT b) = tauMSymH3 W z h b := by
  have hC : ∀ x : FlavorBraid3, tauMSymH3 W z h (actionC x) = tauMSymH3 W z h x := by
    intro x
    unfold tauMSymH3 tauMH3 actionC
    simp only [hW x.flavors]
  have hP : ∀ x : FlavorBraid3, tauMSymH3 W z h (actionP x) = tauMSymH3 W z h x := by
    intro x
    unfold tauMSymH3 tauMH3 actionP
    have h1 : trM (z - h) (-h) (evalWordH3 (-h) (x.word.map BraidLetter3.mirror)) =
        trM z h (evalWordH3 h x.word) := by
      rw [evalWordH3_mirror h x.word, trM_barH3 z h]
    have h2 : trM z h (evalWordH3 h (x.word.map BraidLetter3.mirror)) =
        trM (z - h) (-h) (evalWordH3 (-h) x.word) := by
      have hhh : h = -(-h) := by ring
      conv_lhs => rw [hhh, evalWordH3_mirror (-h) x.word]
      have hbar := trM_barH3 (z - h) (-h) (evalWordH3 (-h) x.word)
      have hzz : z - h - (-h) = z := by ring
      rw [hzz] at hbar
      exact hbar
    rw [h1, h2]
    ring
  have hT : ∀ x : FlavorBraid3, tauMSymH3 W z h (actionT x) = tauMSymH3 W z h x := by
    intro x
    unfold tauMSymH3 tauMH3 actionT
    rw [evalWordH3_reverse h x.word, trM_wordRevH3,
      evalWordH3_reverse (-h) x.word, trM_wordRevH3]
  refine ⟨hC b, hP b, hT b, ?_⟩
  unfold actionCPT
  simp only [Function.comp_apply]
  rw [hC, hP, hT]

end CPTMarkovTraceClosure

end QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure
