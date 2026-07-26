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
import QOU.Knot.CatalanValueBounds

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

/-- The Borromean continuum functional
    `G(a) = −4·clausen(2a) + clausen(4a − 2π)` — the limit of the scaled
    term-log `8F(a) − 2F(2a−π)` (the B3c target with the vanishing
    `F((N−1)π/N)` and the one-cell `F`-shift dropped). -/
noncomputable def borromeanFunctional (a : ℝ) : ℝ :=
  -4 * clausen (2 * a) + clausen (4 * a - 2 * π)

theorem continuous_borromeanFunctional : Continuous borromeanFunctional := by
  have h1 : Continuous fun a : ℝ => clausen (2 * a) :=
    continuous_clausen.comp (continuous_const.mul continuous_id)
  have h2 : Continuous fun a : ℝ => clausen (4 * a - 2 * π) :=
    continuous_clausen.comp ((continuous_const.mul continuous_id).sub
      continuous_const)
  exact (continuous_const.mul h1).add h2

theorem hasDerivAt_borromeanFunctional {a : ℝ} (h1 : π / 2 < a) (h2 : a < π) :
    HasDerivAt borromeanFunctional
      (8 * Real.log (2 * Real.sin a)
        - 4 * Real.log (2 * Real.sin (2 * a - π))) a := by
  have hpi := Real.pi_pos
  have hc1 : HasDerivAt (fun a : ℝ => clausen (2 * a))
      (-Real.log (2 * Real.sin (2 * a / 2)) * 2) a := by
    have hd := hasDerivAt_clausen (θ := 2 * a) (by linarith) (by linarith)
    have hlin : HasDerivAt (fun a : ℝ => 2 * a) 2 a := by
      simpa using (hasDerivAt_id a).const_mul 2
    exact hd.comp a hlin
  have hc2 : HasDerivAt (fun a : ℝ => clausen (4 * a - 2 * π))
      (-Real.log (2 * Real.sin ((4 * a - 2 * π) / 2)) * 4) a := by
    have hd := hasDerivAt_clausen (θ := 4 * a - 2 * π)
      (by linarith) (by linarith)
    have hlin : HasDerivAt (fun a : ℝ => 4 * a - 2 * π) 4 a := by
      simpa using ((hasDerivAt_id a).const_mul 4).sub_const (2 * π)
    exact hd.comp a hlin
  have hsum := (hc1.const_mul (-4)).add hc2
  convert hsum using 1
  rw [show (2:ℝ) * a / 2 = a by ring,
    show ((4:ℝ) * a - 2 * π) / 2 = 2 * a - π by ring]
  ring

theorem borromeanFunctional_pi_div_two : borromeanFunctional (π / 2) = 0 := by
  unfold borromeanFunctional
  rw [show (2:ℝ) * (π / 2) = π by ring,
    show (4:ℝ) * (π / 2) - 2 * π = 0 by ring, clausen_pi, clausen_zero]
  ring

theorem borromeanFunctional_pi : borromeanFunctional π = 0 := by
  unfold borromeanFunctional
  rw [show (4:ℝ) * π - 2 * π = 2 * π by ring, clausen_two_pi]
  ring

/-- The saddle value: `G(3π/4) = 4·Cl₂(π/2)` — B1 antisymmetry route. -/
theorem borromeanFunctional_three_quarters :
    borromeanFunctional (3 * π / 4) = 4 * QOU.Archimedean.Cl_2 (π / 2) := by
  have hpi := Real.pi_pos
  unfold borromeanFunctional
  rw [show (2:ℝ) * (3 * π / 4) = 3 * π / 2 by ring,
    show (4:ℝ) * (3 * π / 4) - 2 * π = π by ring, clausen_pi]
  have h32 : clausen (3 * π / 2) = QOU.Archimedean.Cl_2 (3 * π / 2) :=
    clausen_eq_series ⟨by linarith, by linarith⟩
  have hanti := Cl_2_two_pi_sub (π / 2)
  rw [show 2 * π - π / 2 = 3 * π / 2 by ring] at hanti
  rw [h32, hanti]
  ring

/-- **Borromean brick B4 — the continuum max (sorry-free).** On `[π/2, π]`
    the Borromean functional never exceeds its saddle value `4·Cl₂(π/2)`,
    attained at `a = 3π/4` (the `x = 3/4` Kashaev saddle): compactness gives
    a maximiser; the boundary values vanish while the saddle value is
    positive (certified Catalan bounds), so the maximiser is interior and
    critical; the critical equation `(2 sin a)² = 2 sin(2a−π)` forces
    `sin a + cos a = 0`, hence `cos 2a = 0` with `2a ∈ (π, 2π)`, hence
    `a = 3π/4`. (bean qou-jor3) -/
theorem borromeanFunctional_le {a : ℝ} (ha : a ∈ Set.Icc (π / 2) π) :
    borromeanFunctional a ≤ 4 * QOU.Archimedean.Cl_2 (π / 2) := by
  have hpi := Real.pi_pos
  obtain ⟨a₀, ha₀mem, hmax⟩ :=
    (isCompact_Icc (a := π / 2) (b := π)).exists_isMaxOn
      (Set.nonempty_Icc.mpr (by linarith))
      continuous_borromeanFunctional.continuousOn
  have hval : 4 * QOU.Archimedean.Cl_2 (π / 2) ≤ borromeanFunctional a₀ := by
    have h := hmax (show (3 * π / 4 : ℝ) ∈ Set.Icc (π / 2) π from
      ⟨by linarith, by linarith⟩)
    simp only [Set.mem_setOf_eq] at h
    rwa [borromeanFunctional_three_quarters] at h
  have hpos := Cl_2_pi_div_two_pos
  have hne1 : a₀ ≠ π / 2 := by
    intro h
    rw [h, borromeanFunctional_pi_div_two] at hval
    linarith
  have hne2 : a₀ ≠ π := by
    intro h
    rw [h, borromeanFunctional_pi] at hval
    linarith
  have hint : a₀ ∈ Set.Ioo (π / 2) π :=
    ⟨lt_of_le_of_ne ha₀mem.1 (Ne.symm hne1), lt_of_le_of_ne ha₀mem.2 hne2⟩
  have hloc : IsLocalMax borromeanFunctional a₀ :=
    hmax.isLocalMax (Icc_mem_nhds hint.1 hint.2)
  have hd := hasDerivAt_borromeanFunctional hint.1 hint.2
  have hzero : 8 * Real.log (2 * Real.sin a₀)
      - 4 * Real.log (2 * Real.sin (2 * a₀ - π)) = 0 := by
    rw [← hd.deriv]
    exact hloc.deriv_eq_zero
  have hsa : 0 < Real.sin a₀ :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [hint.1]) hint.2
  have hsb : 0 < Real.sin (2 * a₀ - π) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [hint.1]) (by linarith [hint.2])
  have hexp : (2 * Real.sin a₀) ^ 2 = 2 * Real.sin (2 * a₀ - π) := by
    have h2 : Real.log ((2 * Real.sin a₀) ^ 2)
        = Real.log (2 * Real.sin (2 * a₀ - π)) := by
      rw [Real.log_pow]
      push_cast
      linarith [hzero]
    have hpos1 : (0:ℝ) < (2 * Real.sin a₀) ^ 2 := by positivity
    have hpos2 : (0:ℝ) < 2 * Real.sin (2 * a₀ - π) := by linarith
    calc (2 * Real.sin a₀) ^ 2
        = Real.exp (Real.log ((2 * Real.sin a₀) ^ 2)) :=
          (Real.exp_log hpos1).symm
      _ = Real.exp (Real.log (2 * Real.sin (2 * a₀ - π))) := by rw [h2]
      _ = 2 * Real.sin (2 * a₀ - π) := Real.exp_log hpos2
  have hsin2 : Real.sin (2 * a₀ - π) = -Real.sin (2 * a₀) := by
    rw [show 2 * a₀ - π = -(π - 2 * a₀) by ring, Real.sin_neg,
      Real.sin_pi_sub]
  have hkey : Real.sin a₀ + Real.cos a₀ = 0 := by
    have hs2 := Real.sin_two_mul a₀
    rw [hsin2, hs2] at hexp
    have hz : Real.sin a₀ * (Real.sin a₀ + Real.cos a₀) = 0 := by
      nlinarith [hexp]
    rcases mul_eq_zero.mp hz with h | h
    · exact absurd h hsa.ne'
    · exact h
  have hcos2 : Real.cos (2 * a₀) = 0 := by
    rw [Real.cos_two_mul']
    have hc : Real.cos a₀ = -Real.sin a₀ := by linarith [hkey]
    rw [hc]
    ring
  have ha3 : a₀ = 3 * π / 4 := by
    rcases Real.cos_eq_zero_iff.mp hcos2 with ⟨k, hk⟩
    have hklo : (2:ℝ) < ((2 * k + 1 : ℤ) : ℝ) := by
      have h1 : π < 2 * a₀ := by linarith [hint.1]
      rw [hk] at h1
      push_cast at h1 ⊢
      nlinarith
    have hkhi : ((2 * k + 1 : ℤ) : ℝ) < 4 := by
      have h1 : 2 * a₀ < 2 * π := by linarith [hint.2]
      rw [hk] at h1
      push_cast at h1 ⊢
      nlinarith
    have hk3 : (2 * k + 1 : ℤ) = 3 := by
      have hlo : (2:ℤ) < 2 * k + 1 := by exact_mod_cast hklo
      have hhi : (2 * k + 1 : ℤ) < 4 := by exact_mod_cast hkhi
      omega
    have hcast : (2 * (k:ℝ) + 1) = 3 := by exact_mod_cast hk3
    have h2a : 2 * a₀ = 3 * (π / 2) := by
      rw [hk, hcast]
      ring
    linarith
  have hfin := hmax ha
  simp only [Set.mem_setOf_eq] at hfin
  calc borromeanFunctional a ≤ borromeanFunctional a₀ := hfin
    _ = borromeanFunctional (3 * π / 4) := by rw [ha3]
    _ = 4 * QOU.Archimedean.Cl_2 (π / 2) := borromeanFunctional_three_quarters

end QOU.Knot.FigureEightVolume
