/-
  Borromean rings (B_3 = L6a4) Kashaev invariant at the root of unity —
  the positive-sum carrier (Borromean squeeze brick B2, bean qou-jor3).

  ⟨B_3⟩_N = Σ_{l=⌈(N-1)/2⌉}^{N-1}  kashaevProd(N,l)³ / D(N,l),

    D(N,l) = ∏_{j=l+1, j≠N}^{2l+1} (2 sin(πj/N))²,

  the root-of-unity evaluation of Habiro's cyclotomic formula for the
  colored Jones of the Borromean rings (GL2011 Appendix A; corpus
  transcription `computations/habiro_borromean_colored_jones.py`, bean
  n920): at q = e^{2πi/N} with all colors N, terms with 2l+1 < N vanish
  ({N} = 0), the survivors carry {N+j}{N-j} = 4sin²(πj/N) cubed —
  `kashaevProd(N,l)³` — and the leftover squared denominator absorbs
  Habiro's (−1)^l sign exactly.  Full sign analysis + numeric rate check
  ((2π/N)·log⟨B_3⟩_N → 8G from above, saddle at l/N → 3/4):
  docs/audits/2026-07-26-borromean-kashaev-positive-sum-feasibility.md.

  WHAT IS PROVABLE IN LEAN (sorry-free, below):
    * every summand is strictly positive on the surviving range;
    * ⟨B_3⟩_N > 0 for N ≥ 2, so log ⟨B_3⟩_N is well-defined;
    * the single-term floor borromeanTerm ≤ borromeanKashaev.

  EPISTEMIC STATUS (mirrors `FigureEightVolume.lean`): `borromeanKashaev`
  is DEFINED by this explicit real sum; its identification with the
  diagrammatic Kashaev invariant / colored Jones at the root of unity is
  the cited literature input (Habiro/GL2011 + the audit's sign analysis),
  exactly as `kashaev` is defined by its explicit sum for 4₁.  The squeeze
  target `(2π/N)·log borromeanKashaev N → 8·Cl₂(π/2) = Vol(B_3)` (bricks
  B3–B5) will be a theorem about THIS object.

  Archimedean (ℝ).

  -- Ref: [garoufalidis-le-2011] https://doi.org/10.2140/gt.2011.15.2135
  -- Ref: [habiro2000] RIMS Kokyuroku 1172 (2000) 34-43
  -- Ref: [manuscript] binding-scale-catalan
-/

import QOU.Knot.FigureEightVolumeSqueeze

namespace QOU.Knot.FigureEightVolume

open Real

/-- The Borromean denominator `D(N,l) = ∏_{j=l+1, j≠N}^{2l+1} (2 sin(πj/N))²`.
    No mirror bookkeeping needed: squaring absorbs the sign of `sin` past
    `j = N`. -/
noncomputable def borromeanDen (N l : ℕ) : ℝ :=
  ∏ j ∈ (Finset.Icc (l + 1) (2 * l + 1)).erase N,
    (2 * Real.sin (π * j / N)) ^ 2

/-- One surviving term of the Borromean Kashaev sum. -/
noncomputable def borromeanTerm (N l : ℕ) : ℝ :=
  kashaevProd N l ^ 3 / borromeanDen N l

/-- The Borromean Kashaev invariant at the `N`-th root of unity, as the
    positive sum over the surviving range `2l+1 ≥ N` (see file header for
    provenance and epistemic status). -/
noncomputable def borromeanKashaev (N : ℕ) : ℝ :=
  ∑ l ∈ Finset.Icc (N / 2) (N - 1), borromeanTerm N l

/-- Every denominator factor index is a non-multiple of `N` in `(0, 2N)`,
    so its sine is nonzero and the squared factor strictly positive. -/
theorem borromeanDen_pos {N l : ℕ} (hN : 1 ≤ N) (hl : l ≤ N - 1) :
    0 < borromeanDen N l := by
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN
  unfold borromeanDen
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hjne, hjmem⟩ := Finset.mem_erase.mp hj
  obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hjmem
  have hj0 : 1 ≤ j := by omega
  have hjN : j ≤ 2 * N - 1 := by omega
  have hsin : Real.sin (π * j / N) ≠ 0 := by
    rcases lt_or_gt_of_ne (show j ≠ N from hjne) with hlt | hgt
    · -- 1 ≤ j < N: the angle is in (0, π), sine positive
      have hj' : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj0
      have hjN' : (j:ℝ) < (N:ℝ) := by exact_mod_cast hlt
      have : 0 < Real.sin (π * j / N) := by
        apply Real.sin_pos_of_pos_of_lt_pi
        · positivity
        · rw [div_lt_iff₀ hNpos]
          nlinarith
      exact this.ne'
    · -- N < j ≤ 2N−1: the angle is in (π, 2π), sine negative
      have hjN' : (N:ℝ) < (j:ℝ) := by exact_mod_cast hgt
      have hj2N : (j:ℝ) ≤ 2 * (N:ℝ) - 1 := by
        have h : ((j:ℕ):ℝ) ≤ ((2 * N - 1 : ℕ):ℝ) := by exact_mod_cast hjN
        push_cast [Nat.cast_sub (by omega : 1 ≤ 2 * N)] at h
        linarith
      have hkey : Real.sin (π * j / N)
          = -Real.sin (π * (j - N : ℝ) / N) := by
        rw [show π * (j:ℝ) / N = π * ((j:ℝ) - N) / N + π by
          field_simp
          ring]
        rw [Real.sin_add_pi]
      have hneg : 0 < Real.sin (π * ((j:ℝ) - N) / N) := by
        apply Real.sin_pos_of_pos_of_lt_pi
        · have : (0:ℝ) < (j:ℝ) - N := by linarith
          positivity
        · rw [div_lt_iff₀ hNpos]
          nlinarith
      rw [hkey]
      exact (neg_neg_of_pos hneg).ne
  have h2s : 2 * Real.sin (π * j / N) ≠ 0 := by
    intro h
    exact hsin (by linarith [h] : Real.sin (π * j / N) = 0)
  exact pow_two_pos_of_ne_zero h2s

/-- Every surviving Borromean term is strictly positive. -/
theorem borromeanTerm_pos {N l : ℕ} (hN : 1 ≤ N) (hlN : l < N)
    (hl : l ≤ N - 1) : 0 < borromeanTerm N l :=
  div_pos (pow_pos (kashaevProd_pos hlN) 3) (borromeanDen_pos hN hl)

/-- **The Borromean Kashaev sum is positive for `N ≥ 2`** — `log` of it is
    well-defined, the floor the B5 squeeze stands on. -/
theorem borromeanKashaev_pos (N : ℕ) (hN : 2 ≤ N) :
    0 < borromeanKashaev N := by
  unfold borromeanKashaev
  apply Finset.sum_pos
  · intro l hl
    obtain ⟨hl1, hl2⟩ := Finset.mem_Icc.mp hl
    exact borromeanTerm_pos (by omega) (by omega) hl2
  · exact ⟨N / 2, Finset.mem_Icc.mpr ⟨le_refl _, by omega⟩⟩

/-- Single-term floor: each surviving term bounds the sum below (the E1-style
    lower envelope hook for the B5 squeeze). -/
theorem borromeanTerm_le_borromeanKashaev {N l : ℕ} (hN : 2 ≤ N)
    (hl : l ∈ Finset.Icc (N / 2) (N - 1)) :
    borromeanTerm N l ≤ borromeanKashaev N := by
  unfold borromeanKashaev
  apply Finset.single_le_sum (f := borromeanTerm N) _ hl
  intro i hi
  obtain ⟨hi1, hi2⟩ := Finset.mem_Icc.mp hi
  exact (borromeanTerm_pos (by omega) (by omega) hi2).le

end QOU.Knot.FigureEightVolume
