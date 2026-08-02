/-
# Whitehead-chain volume — bricks W3–W4: positive-sum carrier, log identity,
# deviation (milestone qou-k49o)

Third volume-conjecture instance, following the 4₁ (E-bricks) and Borromean
(B-bricks) squeezes.  Carrier provenance and epistemic status:

* **Source.** van der Veen, "Proof of the volume conjecture for Whitehead
  chains", arXiv:math/0611181 v2 (`uploads/0611181v2.pdf`), Lemma 1: for the
  Whitehead chain `W_{a,b,c,d}` with `b ≥ 2` belts at the Kashaev point
  `t = e^{2πi/N}`, the colored Jones vanishes for even `N`, and for
  `N = 2M+1`,

      J_N(W_{a,b,c,d}) = φ_N · N^b · χ_{N,M}^{4a−c+d} · (Σ_{k=0}^{M} S_{M,k})^{c+d},
      S_{M,k} = ∏_{j=1}^{M} 2 sin²((k+j)π/N) / sin(jπ/N),

  with `φ_N, χ_{N,M}` unimodular.  Hence the EXACT modulus identity
  `|J_N| = N^b (Σ_k S_{M,k})^{c+d}` — a phase-free positive sum (unlike the
  `b = 1` Whitehead link proper, whose outer phase sum needs vdV's Lemma 4
  Gaussian analysis and is NOT treated here).  Transcription verified by the
  4-anchor battery in `computations/whitehead_vdv_lemma1.py`
  (`whitehead-vdv-lemma1.witness.json`): generic-t tangle form ↔ Lemma 1
  closed form to 3.5e-19; Borromean specialization ↔ the corpus's
  independent GL2011/Habiro transcription to 1e-41; rate → 4G; positivity /
  log-identity / vanishing / modulus checks.

* **What is formalized here** (sorry-free): the positive sum
  `P_M = Σ_{k=0}^{M} S_{M,k}` as `whiteheadKashaev`, its positivity, the
  single-term floor, the exact log identity
  `log S_{M,k} = 2(s_{k+M} − s_k) − s_M` in the E4/E5 Riemann sums
  `s_m = Σ_{j≤m} log(2 sin(jπ/N))`, and the k-uniform deviation
  `|(π/N) log S_{M,k} − Ψ_N(k)| ≤ 5·masterErr N` against the Clausen
  primitive.  The identification of `P_M` with the diagrammatic invariant
  via Lemma 1 is the cited input (same epistemic tier as the Borromean
  carrier's GL2011/Habiro identification).
  -- Ref: [manuscript] docs/audits/2026-08-02-whitehead-chain-positive-sum-route.md

* **Target** (brick W5, separate): `(2π/(2M+1)) log P_M → 4·Cl₂(π/2) = 4G
  = 8Λ(π/4) = Vol(W_{a,2,1,0})` (volume by vdV's octahedral decomposition,
  his ref [10] = van der Veen's master thesis).

Indices are well-inside the grid: `j ∈ [k+1, k+M]` with `k ≤ M` gives
`j ≤ 2M = N − 1`, so every sine factor is strictly positive — no
vanishing-term analysis and no mirror-sign bookkeeping (simpler than the
Borromean carrier on both counts).
-/

import QOU.Knot.FigureEightVolumeSqueeze

namespace QOU.Knot.FigureEightVolume

open Real

/-- Numerator of `S_{M,k}`: `∏_{j=k+1}^{k+M} (2 sin(jπ/N))²`. -/
noncomputable def whiteheadNum (N M k : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc (k + 1) (k + M), (2 * Real.sin ((j : ℝ) * (π / N))) ^ 2

/-- Denominator of `S_{M,k}`: `∏_{j=1}^{M} 2 sin(jπ/N)`. -/
noncomputable def whiteheadDen (N M : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc 1 M, (2 * Real.sin ((j : ℝ) * (π / N)))

/-- One term of the Whitehead-chain Kashaev sum:
    `S_{M,k} = ∏_{j=1}^{M} 2 sin²((k+j)π/N)/sin(jπ/N)` (vdV Lemma 1),
    written as the reindexed quotient of `2 sin` products. -/
noncomputable def whiteheadTerm (N M k : ℕ) : ℝ :=
  whiteheadNum N M k / whiteheadDen N M

/-- The Whitehead-chain positive sum `P_M = Σ_{k=0}^{M} S_{M,k}` at
    `N = 2M+1` (the `N` parameter is kept general; the chain instance takes
    `N = 2M+1`).  By vdV Lemma 1 the invariant modulus is
    `|J_N(W_{a,b,c,d})| = N^b · P_M^{c+d}` for `b ≥ 2`, `N = 2M+1`. -/
noncomputable def whiteheadKashaev (N M : ℕ) : ℝ :=
  ∑ k ∈ Finset.range (M + 1), whiteheadTerm N M k

/-- Interior grid sines are positive: `0 < sin(jπ/N)` for `1 ≤ j ≤ N−1`. -/
theorem sin_grid_pos {N j : ℕ} (hj1 : 1 ≤ j) (hjN : j ≤ N - 1) :
    0 < Real.sin ((j : ℝ) * (π / N)) := by
  have hN2 : 2 ≤ N := by omega
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hj1' : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj1
  have hjN' : (j:ℝ) < (N:ℝ) := by exact_mod_cast (by omega : j < N)
  have hh : (0:ℝ) < π / N := by positivity
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  apply Real.sin_pos_of_pos_of_lt_pi
  · nlinarith
  · nlinarith

/-- The numerator is positive whenever the window stays inside the grid
    (`k + M ≤ N − 1`). -/
theorem whiteheadNum_pos {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    0 < whiteheadNum N M k := by
  unfold whiteheadNum
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
  have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
  positivity

/-- The denominator is positive for `M ≤ N − 1`. -/
theorem whiteheadDen_pos {N M : ℕ} (hM : M ≤ N - 1) :
    0 < whiteheadDen N M := by
  unfold whiteheadDen
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
  have hsin := sin_grid_pos (N := N) (j := j) hj1 (by omega)
  positivity

/-- Every term `S_{M,k}` with an in-grid window is strictly positive —
    no vanishing terms, no sign analysis (contrast the Borromean carrier). -/
theorem whiteheadTerm_pos {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    0 < whiteheadTerm N M k :=
  div_pos (whiteheadNum_pos hkM) (whiteheadDen_pos (by omega))

/-- **The Whitehead-chain sum is positive** (`2M ≤ N − 1`, satisfied by the
    chain instance `N = 2M+1`) — `log` of it is well-defined, the floor the
    W5 squeeze stands on. -/
theorem whiteheadKashaev_pos {N M : ℕ} (h2M : 2 * M ≤ N - 1) :
    0 < whiteheadKashaev N M := by
  unfold whiteheadKashaev
  apply Finset.sum_pos
  · intro k hk
    have hk' := Finset.mem_range.mp hk
    exact whiteheadTerm_pos (by omega)
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- Single-term floor: each term bounds the sum below (the lower-envelope
    hook for the W5 squeeze). -/
theorem whiteheadTerm_le_whiteheadKashaev {N M k : ℕ} (h2M : 2 * M ≤ N - 1)
    (hk : k ∈ Finset.range (M + 1)) :
    whiteheadTerm N M k ≤ whiteheadKashaev N M := by
  unfold whiteheadKashaev
  apply Finset.single_le_sum (f := whiteheadTerm N M) _ hk
  intro i hi
  have hi' := Finset.mem_range.mp hi
  exact (whiteheadTerm_pos (by omega)).le

/-- **Whitehead brick W4a — the log identity (sorry-free, exact).**  With the
    E4/E5 Riemann sums `s_m = Σ_{j∈Icc 1 m} log(2 sin(jπ/N))`,

        log S_{M,k} = 2·(s_{k+M} − s_k) − s_M

    — the numerator window `(k, k+M]` splits off the prefix `[1, k]`, and the
    squared factors contribute the `2`. -/
theorem log_whiteheadTerm {N M k : ℕ} (hkM : k + M ≤ N - 1) :
    Real.log (whiteheadTerm N M k)
      = 2 * ((∑ j ∈ Finset.Icc 1 (k + M),
                Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
             - ∑ j ∈ Finset.Icc 1 k,
                Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 M,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
  have hnum := whiteheadNum_pos (N := N) (M := M) (k := k) hkM
  have hden := whiteheadDen_pos (N := N) (M := M) (by omega)
  -- log of the quotient
  unfold whiteheadTerm
  rw [Real.log_div hnum.ne' hden.ne']
  -- numerator: log of a product of squares
  have hlognum : Real.log (whiteheadNum N M k)
      = 2 * ∑ j ∈ Finset.Icc (k + 1) (k + M),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    unfold whiteheadNum
    rw [Real.log_prod]
    · rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
      have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
      rw [Real.log_pow]
      push_cast
      ring
    · intro j hj
      obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
      have hsin := sin_grid_pos (N := N) (j := j) (by omega) (by omega)
      positivity
  -- denominator: log of a product
  have hlogden : Real.log (whiteheadDen N M)
      = ∑ j ∈ Finset.Icc 1 M,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    unfold whiteheadDen
    rw [Real.log_prod]
    intro j hj
    obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hj
    have hsin := sin_grid_pos (N := N) (j := j) hj1 (by omega)
    positivity
  -- window split: Σ_{Icc (k+1) (k+M)} = Σ_{Icc 1 (k+M)} − Σ_{Icc 1 k}
  have hsplit : ∑ j ∈ Finset.Icc (k + 1) (k + M),
        Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
      = (∑ j ∈ Finset.Icc 1 (k + M),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    have hconsec := Finset.sum_Ioc_consecutive
      (f := fun j : ℕ => Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      (Nat.zero_le k) (Nat.le_add_right k M)
    have h1 : Finset.Icc 1 (k + M) = Finset.Ioc 0 (k + M) := by
      exact Finset.Icc_succ_left_eq_Ioc 0 _
    have h2 : Finset.Icc 1 k = Finset.Ioc 0 k := by
      exact Finset.Icc_succ_left_eq_Ioc 0 _
    have h3 : Finset.Icc (k + 1) (k + M) = Finset.Ioc k (k + M) := by
      exact Finset.Icc_succ_left_eq_Ioc k _
    rw [h1, h2, h3]
    linarith [hconsec]
  rw [hlognum, hlogden, hsplit]

/-- **Whitehead brick W4b — the k-uniform deviation (sorry-free).**  For
    `1 ≤ k` and `k + M ≤ N − 1`, the scaled log-term deviates from the
    Clausen-primitive combination

        Ψ_N(k) = 2·(F((k+M)π/N) − F(kπ/N)) − F(Mπ/N),
        F(x) = −clausen(2x)/2

    by at most `5·masterErr N` — coefficient sum `2+2+1` of the E5c-4
    k-uniform bound applied at the indices `k+M`, `k`, `M`. -/
theorem abs_log_whiteheadTerm_deviation {N M k : ℕ} (hN : 4 ≤ N)
    (hM1 : 1 ≤ M) (hk1 : 1 ≤ k) (hkM : k + M ≤ N - 1) :
    |(π / N) * Real.log (whiteheadTerm N M k)
        - (2 * ((-clausen (2 * (((k : ℝ) + (M : ℝ)) * (π / N))) / 2)
                - (-clausen (2 * ((k : ℝ) * (π / N))) / 2))
           - (-clausen (2 * ((M : ℝ) * (π / N))) / 2))|
      ≤ 5 * masterErr N := by
  -- the three deviation instances
  have hA : |(π / N) * (∑ j ∈ Finset.Icc 1 (k + M),
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * (((k : ℝ) + (M : ℝ)) * (π / N))) / 2)| ≤ masterErr N := by
    have h := abs_deviation_le_masterErr (N := N) (k := k + M) hN (by omega) hkM
    have hcast : (((k + M : ℕ) : ℝ)) = (k : ℝ) + (M : ℝ) := by push_cast; ring
    rwa [hcast] at h
  have hB : |(π / N) * (∑ j ∈ Finset.Icc 1 k,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)| ≤ masterErr N :=
    abs_deviation_le_masterErr (N := N) (k := k) hN hk1 (by omega)
  have hC : |(π / N) * (∑ j ∈ Finset.Icc 1 M,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((M : ℝ) * (π / N))) / 2)| ≤ masterErr N :=
    abs_deviation_le_masterErr (N := N) (k := M) hN hM1 (by omega)
  -- rewrite the scaled log via the W4a identity
  rw [log_whiteheadTerm hkM]
  rw [abs_le] at hA hB hC ⊢
  constructor <;> [skip; skip] <;>
    · obtain ⟨hA1, hA2⟩ := hA
      obtain ⟨hB1, hB2⟩ := hB
      obtain ⟨hC1, hC2⟩ := hC
      nlinarith [hA1, hA2, hB1, hB2, hC1, hC2]

end QOU.Knot.FigureEightVolume
