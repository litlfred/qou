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

/-- **Borromean brick B3a — the window identity (sorry-free, exact).** On the
    surviving range, the log-denominator is an exact combination of the E4/E5
    Riemann sums `S(k) = Σ_{j≤k} log(2 sin(jπ/N))`:
    `log D(N,l) = 2·(S(N−1) − S(l) + S(2l+1−N))` — the window `(l, 2l+1]∖{N}`
    splits at `N` and the upper half mirrors down by `sin(x+π) = −sin x` with
    `Real.log` absorbing the sign. No new deviation machinery needed.
    (bean qou-jor3) -/
theorem log_borromeanDen {N l : ℕ} (hN : 1 ≤ N) (hsurv : N ≤ 2 * l + 1)
    (hl : l ≤ N - 1) :
    Real.log (borromeanDen N l)
      = 2 * ((∑ j ∈ Finset.Icc 1 (N - 1),
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
          - (∑ j ∈ Finset.Icc 1 l,
              Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
          + ∑ j ∈ Finset.Icc 1 (2 * l + 1 - N),
              Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) := by
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast hN
  have hN0 : (N:ℝ) ≠ 0 := ne_of_gt hNpos
  -- each squared factor is nonzero (the B2 positivity argument, factor-level)
  have hfac : ∀ j ∈ (Finset.Icc (l + 1) (2 * l + 1)).erase N,
      (2 * Real.sin (π * j / N)) ^ 2 ≠ 0 := by
    intro j hj
    obtain ⟨hjne, hjmem⟩ := Finset.mem_erase.mp hj
    obtain ⟨hj1, hj2⟩ := Finset.mem_Icc.mp hjmem
    have hj0 : 1 ≤ j := by omega
    have hjN : j ≤ 2 * N - 1 := by omega
    have hsin : Real.sin (π * j / N) ≠ 0 := by
      rcases lt_or_gt_of_ne (show j ≠ N from hjne) with hlt | hgt
      · have hj' : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj0
        have hjN' : (j:ℝ) < (N:ℝ) := by exact_mod_cast hlt
        exact (Real.sin_pos_of_pos_of_lt_pi (by positivity)
          (by rw [div_lt_iff₀ hNpos]; nlinarith)).ne'
      · have hjN' : (N:ℝ) < (j:ℝ) := by exact_mod_cast hgt
        have hj2N : (j:ℝ) ≤ 2 * (N:ℝ) - 1 := by
          have h : ((j:ℕ):ℝ) ≤ ((2 * N - 1 : ℕ):ℝ) := by exact_mod_cast hjN
          push_cast [Nat.cast_sub (by omega : 1 ≤ 2 * N)] at h
          linarith
        have hkey : Real.sin (π * j / N)
            = -Real.sin (π * ((j:ℝ) - N) / N) := by
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
    exact pow_ne_zero 2 (by
      intro h
      exact hsin (by linarith [h] : Real.sin (π * j / N) = 0))
  unfold borromeanDen
  rw [Real.log_prod _ _ hfac]
  -- split the erased window at N and mirror the upper half
  have hset : (Finset.Icc (l + 1) (2 * l + 1)).erase N
      = Finset.Icc (l + 1) (N - 1) ∪ Finset.Icc (N + 1) (2 * l + 1) := by
    ext x
    simp only [Finset.mem_erase, Finset.mem_Icc, Finset.mem_union]
    omega
  have hdisj : Disjoint (Finset.Icc (l + 1) (N - 1))
      (Finset.Icc (N + 1) (2 * l + 1)) := by
    rw [Finset.disjoint_left]
    intro x hx1 hx2
    simp only [Finset.mem_Icc] at hx1 hx2
    omega
  rw [hset, Finset.sum_union hdisj]
  -- each squared factor: log((2 sin(πj/N))²) = 2 log(2 sin(j·(π/N)))
  have hconv : ∀ s : Finset ℕ,
      (∑ j ∈ s, Real.log ((2 * Real.sin (π * j / N)) ^ 2))
        = ∑ j ∈ s, 2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    intro s
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Real.log_pow, show π * (j:ℝ) / N = (j:ℝ) * (π / N) by ring]
    push_cast
    ring
  rw [hconv, hconv]
  -- lower half: Σ_{Icc(l+1,N−1)} = S(N−1) − S(l)
  have hpart1 : (∑ j ∈ Finset.Icc (l + 1) (N - 1),
        2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      = (∑ j ∈ Finset.Icc 1 (N - 1),
          2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ∑ j ∈ Finset.Icc 1 l,
            2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    have hsplit : Finset.Icc 1 (N - 1)
        = Finset.Icc 1 l ∪ Finset.Icc (l + 1) (N - 1) := by
      ext x
      simp only [Finset.mem_Icc, Finset.mem_union]
      omega
    have hdisj2 : Disjoint (Finset.Icc 1 l) (Finset.Icc (l + 1) (N - 1)) := by
      rw [Finset.disjoint_left]
      intro x h1 h2
      simp only [Finset.mem_Icc] at h1 h2
      omega
    rw [hsplit, Finset.sum_union hdisj2]
    ring
  -- upper half mirrors: Σ_{Icc(N+1,2l+1)} = S(2l+1−N)
  have hpart2 : (∑ j ∈ Finset.Icc (N + 1) (2 * l + 1),
        2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      = ∑ j ∈ Finset.Icc 1 (2 * l + 1 - N),
          2 * Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
    have hmap : Finset.Icc (N + 1) (2 * l + 1)
        = Finset.map ⟨fun i => i + N, fun a b h => by simpa using h⟩
            (Finset.Icc 1 (2 * l + 1 - N)) := by
      ext x
      simp only [Finset.mem_Icc, Finset.mem_map, Function.Embedding.coeFn_mk]
      constructor
      · intro hx
        exact ⟨x - N, by omega, by omega⟩
      · rintro ⟨y, hy, rfl⟩
        omega
    rw [hmap, Finset.sum_map]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [Function.Embedding.coeFn_mk]
    have hcast : ((i + N : ℕ) : ℝ) * (π / N) = (i : ℝ) * (π / N) + π := by
      push_cast
      field_simp
    rw [hcast, Real.sin_add_pi,
      show (2:ℝ) * -Real.sin ((i:ℝ) * (π / N))
        = -(2 * Real.sin ((i:ℝ) * (π / N))) by ring,
      Real.log_neg_eq_log]
  rw [hpart1, hpart2]
  simp only [← Finset.mul_sum]
  ring

/-- **Borromean brick B3b — the term log identity (sorry-free, exact).**
    `log borromeanTerm(N,l) = 8·S(l) − 2·S(N−1) − 2·S(2l+1−N)` — combining
    the E5a bridge (`log kashaevProd = 2·S`) cubed with the B3a window
    identity. -/
theorem log_borromeanTerm {N l : ℕ} (hN : 1 ≤ N) (hsurv : N ≤ 2 * l + 1)
    (hlN : l < N) (hl : l ≤ N - 1) :
    Real.log (borromeanTerm N l)
      = 8 * (∑ j ∈ Finset.Icc 1 l,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - 2 * (∑ j ∈ Finset.Icc 1 (N - 1),
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - 2 * ∑ j ∈ Finset.Icc 1 (2 * l + 1 - N),
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
  unfold borromeanTerm
  rw [Real.log_div (pow_ne_zero 3 (kashaevProd_pos hlN).ne')
      (borromeanDen_pos hN hl).ne',
    Real.log_pow, log_kashaevProd hlN, log_borromeanDen hN hsurv hl]
  push_cast
  ring

/-- **Borromean brick B3c — the uniform deviation (sorry-free).** On the
    surviving range with `N ≥ 4`, the scaled term-log deviates from its
    Clausen-primitive continuum value by at most `12·E(N)`:
    `|(π/N)·log borromeanTerm(N,l) − (8F(lπ/N) − 2F((N−1)π/N) −
    2F((2l+1−N)π/N))| ≤ 12·masterErr N`, `F(x) = −clausen(2x)/2` —
    one E5c-4 deviation per `S`-index (`8+2+2` copies of `E(N)`), the
    `2l+1−N = 0` edge exact (`S(0) = F(0) = 0`). (bean qou-jor3) -/
theorem abs_log_borromeanTerm_deviation {N l : ℕ} (hN : 4 ≤ N)
    (hsurv : N ≤ 2 * l + 1) (hl : l ≤ N - 1) :
    |(π / N) * Real.log (borromeanTerm N l)
        - (8 * (-clausen (2 * ((l : ℝ) * (π / N))) / 2)
           - 2 * (-clausen (2 * (((N - 1 : ℕ) : ℝ) * (π / N))) / 2)
           - 2 * (-clausen (2 * (((2 * l + 1 - N : ℕ) : ℝ) * (π / N))) / 2))|
      ≤ 12 * masterErr N := by
  have hN1 : 1 ≤ N := by omega
  have hlN : l < N := by omega
  have hl1 : 1 ≤ l := by omega
  have hlog := log_borromeanTerm hN1 hsurv hlN hl
  have hd1 := abs_deviation_le_masterErr (N := N) (k := l) hN hl1 hl
  have hd2 := abs_deviation_le_masterErr (N := N) (k := N - 1) hN
    (by omega) (by omega)
  rw [abs_le] at hd1 hd2
  rw [hlog]
  rcases Nat.eq_zero_or_pos (2 * l + 1 - N) with hm0 | hm1
  · -- edge 2l+1 = N: the third sum and its Clausen value are both zero
    rw [hm0]
    simp only [Finset.Icc_eq_empty_of_lt (by omega : (0:ℕ) < 1),
      Finset.sum_empty, Nat.cast_zero, zero_mul, mul_zero, clausen_zero]
    rw [abs_le]
    have hEnn := masterErr_nonneg N
    constructor <;> nlinarith [hd1.1, hd1.2, hd2.1, hd2.2]
  · have hd3 := abs_deviation_le_masterErr (N := N) (k := 2 * l + 1 - N) hN
      hm1 (by omega)
    rw [abs_le] at hd3
    rw [abs_le]
    constructor <;> nlinarith [hd1.1, hd1.2, hd2.1, hd2.2, hd3.1, hd3.2]

end QOU.Knot.FigureEightVolume
