/-
# Whitehead-link majorant rate — brick W6 (bean qou-oiv6)

The `b = 1` Whitehead link's Kashaev sum carries Fresnel phases (vdV Lemma 1
at `4a−c+d = −1`), so `WhiteheadLinkScaffold.lean` splits the volume limit
into (i) the sorry-free triangle bound `‖J_N‖ ≤ whiteheadLinkMajorant N`,
(ii) the `VdVWhiteheadLemma4` conditional class (phases cost at most `N^p` —
the open Gaussian/erfc analytic input), and (iii) a derived conditional
squeeze needing the MAJORANT volume rate as input.  This file supplies that
missing input, sorry-free:

    (2π/N) · log (whiteheadLinkMajorant N)  →  4·Cl₂(π/2) = 4G,

which upgrades the Whitehead-link volume limit to *conditional only on the
named Lemma-4 class* (`whiteheadLink_volume_of_lemma4` below).

## The 2D continuum max, without compactness

The majorant is the phase-free double sum `Σ_n (2n+1) Σ_k S_{n,k}`, whose
per-term scaled log converges to the van der Veen 2-variable functional (in
clausen coordinates `u = 2πn/N`, `v = 2πk/N`)

    g(u,v) = clausen u + 2·clausen v − 2·clausen(u+v)

on the triangle `{u,v ≥ 0, u+v ≤ 2π}` — vdV's `f(x,y) = Λ(x)+2Λ(y)−2Λ(x+y)`
with max `4Λ(π/4)` at `(π/2, π/4)` (arXiv:math/0611181, proof of Lemma 2).
Rather than a 2-variable compactness/critical-point analysis, the max
`g ≤ 4·clausen(π/2)` decomposes into 1D monotone-split bricks in the style
of `WhiteheadSaddleClausen`:

* `u ≤ π` — the sibling brick `clausen_diff_le_shift` (shift `s = u`)
  freezes out `v`, leaving `ψ(u) = clausen u + 4·clausen(π − u/2)`, which is
  monotone up to its endpoint value `ψ(π) = 4·clausen(π/2)` (the derivative
  is `log(2cos(u/4)) − log(2sin(u/4)) ≥ 0`).
* `u ≥ π` — the antisymmetry `clausen(2π−x) = −clausen x` reflects the
  region onto `2·clausen v + 2·clausen(c−v) − clausen c` with
  `c = 2π−u ≤ π`; the symmetric-pair bound
  `clausen v + clausen(c−v) ≤ 2·clausen(c/2)` and the monotone
  `ρ(c) = 4·clausen(c/2) − clausen c ≤ ρ(π) = 4·clausen(π/2)` finish.

The two regions agree at the seam `u = π`, where the saddle
`(u,v) = (π, π/2)` attains the value exactly.

## Grid assembly

The generic W4b deviation brick `abs_log_whiteheadTerm_deviation` (its `M`
slot is a free variable, not tied to `N = 2M+1`) puts every interior grid
term within `10·masterErr N` of `g(2πn/N, 2πk/N)` — with NO grid-shift
slack, since `θ_n + θ_k = θ_{n+k}` exactly.  Upper envelope: at most `2N³`
terms below the continuum max; lower envelope: the single grid term at
`(⌊N/2⌋, ⌊N/4⌋) → (π, π/2)`.  Boundary rows `n = 0` (terms `= 1`) and
`k = 0` (`log S_{n,0} = s_n`) are handled directly.

Numeric confirmation of the target: anchor A3 of
`computations/whitehead_vdv_lemma1.py` (W-link fit `3.66520` vs
`4G = 3.66386`, err `1.3e-3` — the `b=1` row).
-/

import QOU.Knot.WhiteheadLinkScaffold
import QOU.Knot.WhiteheadSaddleClausen

namespace QOU.Knot.FigureEightVolume

open Real

/-! ## W6a — clausen antisymmetry and the 1D monotone bricks -/

/-- Antisymmetry of `clausen` about `π` on `[0, 2π]`:
    `clausen(2π − x) = −clausen x` — the integral-side transport of the
    series identity `Cl_2_two_pi_sub` through the `clausen = Cl₂` bridge,
    with the endpoints closed by `clausen_zero` / `clausen_two_pi`. -/
theorem clausen_two_pi_sub_eq {x : ℝ} (h0 : 0 ≤ x) (h2 : x ≤ 2 * π) :
    clausen (2 * π - x) = -clausen x := by
  have hpi := Real.pi_pos
  rcases eq_or_lt_of_le h0 with hx0 | hx0
  · rw [← hx0]
    norm_num [clausen_two_pi, clausen_zero]
  rcases eq_or_lt_of_le h2 with hx2 | hx2
  · rw [hx2]
    norm_num [clausen_two_pi, clausen_zero]
  have hb1 : clausen (2 * π - x) = QOU.Archimedean.Cl_2 (2 * π - x) :=
    clausen_eq_series ⟨by linarith, by linarith⟩
  have hb2 : clausen x = QOU.Archimedean.Cl_2 x :=
    clausen_eq_series ⟨hx0, hx2⟩
  rw [hb1, hb2, Cl_2_two_pi_sub]

/-- `clausen` never exceeds twice its saddle value on `[0, 2π]`:
    `clausen y ≤ 2·clausen(π/2)`.  On `[0, π]` this is the sibling brick
    `clausen_diff_le` plus `clausen(y+π) = −clausen(π−y) ≤ 0`; on `[π, 2π]`
    the function is `≤ 0` by antisymmetry. -/
theorem clausen_le_double_saddle {y : ℝ} (h0 : 0 ≤ y) (h2 : y ≤ 2 * π) :
    clausen y ≤ 2 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  have hsp : 0 ≤ clausen (π / 2) :=
    QOU.Knot.WhiteheadSaddle.clausen_nonneg (by positivity) (by linarith)
  rcases le_total y π with hyπ | hyπ
  · have hdiff := QOU.Knot.WhiteheadSaddle.clausen_diff_le h0 hyπ
    have hshift : clausen (y + π) = -clausen (π - y) := by
      have h := clausen_two_pi_sub_eq (x := π - y) (by linarith) (by linarith)
      rw [show 2 * π - (π - y) = y + π by ring] at h
      exact h
    have hnn : 0 ≤ clausen (π - y) :=
      QOU.Knot.WhiteheadSaddle.clausen_nonneg (by linarith) (by linarith)
    have : clausen y - clausen (y + π) ≤ 2 * clausen (π / 2) := hdiff
    rw [hshift] at this
    linarith
  · have hanti := clausen_two_pi_sub_eq (x := 2 * π - y) (by linarith)
      (by linarith)
    rw [show 2 * π - (2 * π - y) = y by ring] at hanti
    have hnn : 0 ≤ clausen (2 * π - y) :=
      QOU.Knot.WhiteheadSaddle.clausen_nonneg (by linarith) (by linarith)
    linarith [hanti]

/-- **Symmetric-pair brick.**  For `0 ≤ v ≤ c ≤ π`,
    `clausen v + clausen(c−v) ≤ 2·clausen(c/2)` — the symmetric sum peaks at
    the midpoint (monotone on `[0, c/2]` since
    `sin(t/2) ≤ sin((c−t)/2)` there, then reflect). -/
theorem clausen_pair_le {c v : ℝ} (hcπ : c ≤ π) (hv0 : 0 ≤ v) (hvc : v ≤ c) :
    clausen v + clausen (c - v) ≤ 2 * clausen (c / 2) := by
  have hpi := Real.pi_pos
  have hc0 : 0 ≤ c := le_trans hv0 hvc
  rcases eq_or_lt_of_le hc0 with hc0' | hc0'
  · have hv0' : v = 0 := by linarith
    rw [← hc0', hv0']
    norm_num [clausen_zero]
  -- the symmetric function and its monotonicity on [0, c/2]
  set G : ℝ → ℝ := fun t => clausen t + clausen (c - t) with hGdef
  have hcont : Continuous G :=
    continuous_clausen.add
      (continuous_clausen.comp (continuous_const.sub continuous_id))
  have hderiv : ∀ t ∈ Set.Ioo (0:ℝ) (c / 2),
      HasDerivAt G (-Real.log (2 * Real.sin (t / 2))
        + Real.log (2 * Real.sin ((c - t) / 2))) t := by
    intro t ht
    have hd1 := hasDerivAt_clausen (θ := t) ht.1 (by linarith [ht.2])
    have hlin : HasDerivAt (fun s : ℝ => c - s) (-1) t := by
      simpa using (hasDerivAt_id t).const_sub c
    have hd2 := (hasDerivAt_clausen (θ := c - t)
      (by linarith [ht.2]) (by linarith [ht.1])).comp t hlin
    have hcomb := hd1.add (by simpa using hd2)
    convert hcomb using 1
  have hmono : MonotoneOn G (Set.Icc 0 (c / 2)) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]
      intro t ht
      exact (hderiv t ht).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hderiv t ht).deriv]
      have hs1 : 0 < Real.sin (t / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1])
          (by linarith [ht.1, ht.2])
      have hcmp : Real.sin (t / 2) ≤ Real.sin ((c - t) / 2) := by
        apply Real.strictMonoOn_sin.monotoneOn
        · constructor <;> [linarith [ht.1]; linarith [ht.1, ht.2]]
        · constructor <;> [linarith [ht.2]; linarith [ht.1, ht.2]]
        · linarith [ht.2]
      have := Real.log_le_log (by linarith : (0:ℝ) < 2 * Real.sin (t / 2))
        (by linarith : 2 * Real.sin (t / 2) ≤ 2 * Real.sin ((c - t) / 2))
      linarith
  have hGhalf : G (c / 2) = 2 * clausen (c / 2) := by
    simp only [hGdef, show c - c / 2 = c / 2 by ring]
    ring
  rcases le_total v (c / 2) with hle | hge
  · have := hmono ⟨hv0, hle⟩ ⟨by linarith, le_refl _⟩ hle
    rw [hGhalf] at this
    exact this
  · have hv' : c - v ≤ c / 2 := by linarith
    have hv'0 : 0 ≤ c - v := by linarith
    have := hmono ⟨hv'0, hv'⟩ ⟨by linarith, le_refl _⟩ hv'
    rw [hGhalf] at this
    simp only [hGdef, show c - (c - v) = v by ring] at this
    linarith

/-- Double-angle log split: `log(2 sin(x/2)) = log(2 sin(x/4)) + log(2 cos(x/4))`
    for `0 < x < 2π` (both factors positive). -/
theorem log_two_sin_half_split {x : ℝ} (h0 : 0 < x) (h2 : x < 2 * π) :
    Real.log (2 * Real.sin (x / 2))
      = Real.log (2 * Real.sin (x / 4)) + Real.log (2 * Real.cos (x / 4)) := by
  have hpi := Real.pi_pos
  have hs : 0 < Real.sin (x / 4) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hc : 0 < Real.cos (x / 4) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hsplit : 2 * Real.sin (x / 2)
      = (2 * Real.sin (x / 4)) * (2 * Real.cos (x / 4)) := by
    rw [show x / 2 = 2 * (x / 4) by ring, Real.sin_two_mul]
    ring
  rw [hsplit, Real.log_mul (by positivity) (by positivity)]

/-- The shared derivative sign: `log(2 cos(x/4)) ≥ log(2 sin(x/4))` for
    `0 < x ≤ π` (i.e. `x/4 ≤ π/4`, where sine is below cosine). -/
theorem log_sin_quarter_le_log_cos_quarter {x : ℝ} (h0 : 0 < x) (h2 : x ≤ π) :
    Real.log (2 * Real.sin (x / 4)) ≤ Real.log (2 * Real.cos (x / 4)) := by
  have hpi := Real.pi_pos
  have hs : 0 < Real.sin (x / 4) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hcmp : Real.sin (x / 4) ≤ Real.cos (x / 4) := by
    rw [← Real.sin_pi_div_two_sub]
    apply Real.strictMonoOn_sin.monotoneOn
    · constructor <;> linarith
    · constructor <;> linarith
    · linarith
  exact Real.log_le_log (by linarith) (by linarith)

/-- **The ρ brick.**  `ρ(c) = 4·clausen(c/2) − clausen c` is monotone on
    `[0, π]` (derivative `log(2cos(c/4)) − log(2sin(c/4)) ≥ 0`), so it is at
    most its endpoint value `ρ(π) = 4·clausen(π/2)`. -/
theorem whiteheadRho_le {c : ℝ} (h0 : 0 ≤ c) (h2 : c ≤ π) :
    4 * clausen (c / 2) - clausen c ≤ 4 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  set ρ : ℝ → ℝ := fun t => 4 * clausen (t / 2) - clausen t with hρdef
  have hcont : Continuous ρ := by
    have h1 : Continuous fun t : ℝ => clausen (t / 2) :=
      continuous_clausen.comp (continuous_id.div_const 2)
    exact (continuous_const.mul h1).sub continuous_clausen
  have hderiv : ∀ t ∈ Set.Ioo (0:ℝ) π,
      HasDerivAt ρ (-2 * Real.log (2 * Real.sin (t / 4))
        + Real.log (2 * Real.sin (t / 2))) t := by
    intro t ht
    have hlin : HasDerivAt (fun s : ℝ => s / 2) (1 / 2) t := by
      simpa using (hasDerivAt_id t).div_const 2
    have hd1 := (hasDerivAt_clausen (θ := t / 2)
      (by linarith [ht.1]) (by linarith [ht.2])).comp t hlin
    have hd2 := hasDerivAt_clausen (θ := t) ht.1 (by linarith [ht.2])
    have hcomb := (hd1.const_mul (4:ℝ)).sub hd2
    convert hcomb using 1
    rw [show t / 2 / 2 = t / 4 by ring]
    ring
  have hmono : MonotoneOn ρ (Set.Icc 0 π) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]
      intro t ht
      exact (hderiv t ht).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hderiv t ht).deriv,
        log_two_sin_half_split ht.1 (by linarith [ht.2])]
      linarith [log_sin_quarter_le_log_cos_quarter ht.1 (le_of_lt ht.2)]
  have hend : ρ π = 4 * clausen (π / 2) := by
    simp only [hρdef, clausen_pi]
    ring
  have := hmono ⟨h0, h2⟩ ⟨by linarith, le_refl _⟩ h2
  rw [hend] at this
  exact this

/-- **The ψ brick.**  `ψ(u) = clausen u + 4·clausen(π − u/2)` is monotone on
    `[0, π]` (same derivative sign as ρ after `sin(π/2 − u/4) = cos(u/4)`),
    so it is at most its endpoint value `ψ(π) = 4·clausen(π/2)`. -/
theorem whiteheadPsi1D_le {u : ℝ} (h0 : 0 ≤ u) (h2 : u ≤ π) :
    clausen u + 4 * clausen (π - u / 2) ≤ 4 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  set ψ : ℝ → ℝ := fun t => clausen t + 4 * clausen (π - t / 2) with hψdef
  have hcont : Continuous ψ := by
    have h1 : Continuous fun t : ℝ => clausen (π - t / 2) :=
      continuous_clausen.comp (continuous_const.sub (continuous_id.div_const 2))
    exact continuous_clausen.add (continuous_const.mul h1)
  have hderiv : ∀ t ∈ Set.Ioo (0:ℝ) π,
      HasDerivAt ψ (-Real.log (2 * Real.sin (t / 2))
        + 2 * Real.log (2 * Real.sin (π / 2 - t / 4))) t := by
    intro t ht
    have hd1 := hasDerivAt_clausen (θ := t) ht.1 (by linarith [ht.2])
    have hlin : HasDerivAt (fun s : ℝ => π - s / 2) (-(1 / 2)) t := by
      simpa using (hasDerivAt_const t π).sub ((hasDerivAt_id t).div_const 2)
    have hd2 := (hasDerivAt_clausen (θ := π - t / 2)
      (by linarith [ht.2]) (by linarith [ht.1])).comp t hlin
    have hcomb := hd1.add (hd2.const_mul (4:ℝ))
    convert hcomb using 1
    rw [show (π - t / 2) / 2 = π / 2 - t / 4 by ring]
    ring
  have hmono : MonotoneOn ψ (Set.Icc 0 π) := by
    refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) hcont.continuousOn ?_ ?_
    · rw [interior_Icc]
      intro t ht
      exact (hderiv t ht).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hderiv t ht).deriv, Real.sin_pi_div_two_sub,
        log_two_sin_half_split ht.1 (by linarith [ht.2])]
      linarith [log_sin_quarter_le_log_cos_quarter ht.1 (le_of_lt ht.2)]
  have hend : ψ π = 4 * clausen (π / 2) := by
    simp only [hψdef, clausen_pi, show π - π / 2 = π / 2 by ring]
    ring
  have := hmono ⟨h0, h2⟩ ⟨by linarith, le_refl _⟩ h2
  rw [hend] at this
  exact this

/-! ## W6a capstone — the 2D functional and its max -/

/-- The van der Veen 2-variable functional in clausen coordinates:
    `g(u,v) = clausen u + 2·clausen v − 2·clausen(u+v)` — the continuum
    limit of `(2π/N)·log S_{n,k}` along `2πn/N → u`, `2πk/N → v`. -/
noncomputable def whiteheadFunctional2 (u v : ℝ) : ℝ :=
  clausen u + 2 * clausen v - 2 * clausen (u + v)

/-- **W6a — the 2D continuum max (sorry-free, no compactness).**  On the
    triangle `{u,v ≥ 0, u+v ≤ 2π}` the functional never exceeds its saddle
    value `4·clausen(π/2) = 4G`, attained at `(π, π/2)`. -/
theorem whiteheadFunctional2_le {u v : ℝ} (hu : 0 ≤ u) (hv : 0 ≤ v)
    (huv : u + v ≤ 2 * π) :
    whiteheadFunctional2 u v ≤ 4 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  have hsp : 0 ≤ clausen (π / 2) :=
    QOU.Knot.WhiteheadSaddle.clausen_nonneg (by positivity) (by linarith)
  unfold whiteheadFunctional2
  rcases le_total u π with hA | hB
  · -- region A: freeze v with the sibling shift brick, then the ψ brick
    rcases eq_or_lt_of_le hu with hu0 | hu0
    · rw [← hu0]
      simp only [clausen_zero, zero_add]
      linarith
    · have hshift := QOU.Knot.WhiteheadSaddle.clausen_diff_le_shift
        (θ := v) (s := u) hu0 hA hv (by linarith)
      rw [show v + u = u + v by ring] at hshift
      have hψ := whiteheadPsi1D_le (le_of_lt hu0) hA
      linarith
  · -- region B: reflect by antisymmetry, then the pair and ρ bricks
    set c : ℝ := 2 * π - u with hcdef
    have hc0 : 0 ≤ c := by simp only [hcdef]; linarith
    have hcπ : c ≤ π := by simp only [hcdef]; linarith
    have hvc : v ≤ c := by simp only [hcdef]; linarith
    have h1 : clausen u = -clausen c := by
      have h := clausen_two_pi_sub_eq (x := c) hc0 (by linarith)
      rw [show 2 * π - c = u by simp only [hcdef]; ring] at h
      linarith [h]
    have h2 : clausen (u + v) = -clausen (c - v) := by
      have h := clausen_two_pi_sub_eq (x := c - v) (by linarith)
        (by linarith)
      rw [show 2 * π - (c - v) = u + v by simp only [hcdef]; ring] at h
      linarith [h]
    have hpair := clausen_pair_le hcπ hv hvc
    have hρ := whiteheadRho_le hc0 hcπ
    rw [h1, h2]
    linarith

/-- The saddle value: `g(π, π/2) = 4·clausen(π/2)` (antisymmetry at `3π/2`). -/
theorem whiteheadFunctional2_saddle :
    whiteheadFunctional2 π (π / 2) = 4 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  unfold whiteheadFunctional2
  have h32 : clausen (π + π / 2) = -clausen (π / 2) := by
    have h := clausen_two_pi_sub_eq (x := π / 2) (by positivity) (by linarith)
    rw [show 2 * π - π / 2 = π + π / 2 by ring] at h
    linarith [h]
  rw [clausen_pi, h32]
  ring

/-! ## W6b — the per-term grid ceiling -/

/-- The empty window: `S_{0,k} = 1`. -/
theorem whiteheadTerm_zero_left (N k : ℕ) : whiteheadTerm N 0 k = 1 := by
  unfold whiteheadTerm whiteheadNum whiteheadDen
  rw [Finset.Icc_eq_empty (by omega : ¬k + 1 ≤ k + 0),
    Finset.Icc_eq_empty (by omega : ¬(1:ℕ) ≤ 0)]
  simp

set_option maxHeartbeats 1000000 in
/-- **W6b — the per-term ceiling (sorry-free).**  Every majorant grid term
    obeys `(2π/N)·log S_{n,k} ≤ 4·clausen(π/2) + 10·masterErr N`: interior
    terms by the generic W4b deviation landing exactly on
    `whiteheadFunctional2` (no grid-shift slack), the `n = 0` row by
    `S_{0,k} = 1`, the `k = 0` column by the bare `s_n` deviation plus
    antisymmetry. -/
theorem whiteheadLink_term_ceiling {N n k : ℕ} (hN : 4 ≤ N)
    (hnk : n + k ≤ N - 1) :
    (2 * π / N) * Real.log (whiteheadTerm N n k)
      ≤ 4 * clausen (π / 2) + 10 * masterErr N := by
  have hpi := Real.pi_pos
  have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hh : (0:ℝ) < π / N := by positivity
  have hfield : (N:ℝ) * (π / N) = π := by field_simp
  have hsp : 0 ≤ clausen (π / 2) :=
    QOU.Knot.WhiteheadSaddle.clausen_nonneg (by positivity) (by linarith)
  have hme := masterErr_nonneg N
  rcases Nat.eq_zero_or_pos n with hn0 | hn1
  · -- n = 0 row: the term is 1, its log is 0
    subst hn0
    rw [whiteheadTerm_zero_left, Real.log_one, mul_zero]
    linarith
  rcases Nat.eq_zero_or_pos k with hk0 | hk1
  · -- k = 0 column: log S_{n,0} = s_n
    subst hk0
    have hdev := abs_deviation_le_masterErr (N := N) (k := n) hN
      (by omega) (by omega)
    rw [abs_le] at hdev
    have hlogT := log_whiteheadTerm (N := N) (M := n) (k := 0) (by omega)
    have hS0 : ∑ j ∈ Finset.Icc (1:ℕ) 0,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))) = 0 := by
      rw [Finset.Icc_eq_empty (by omega : ¬(1:ℕ) ≤ 0)]
      exact Finset.sum_empty
    have hlogT' : Real.log (whiteheadTerm N n 0)
        = ∑ j ∈ Finset.Icc 1 n,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
      rw [hlogT, hS0]
      simp only [Nat.zero_add]
      ring
    -- −clausen(θ_n) = clausen(2π−θ_n) ≤ 2·clausen(π/2)
    have hθn1 : (0:ℝ) ≤ 2 * ((n : ℝ) * (π / N)) := by positivity
    have hθn2 : 2 * ((n : ℝ) * (π / N)) ≤ 2 * π := by
      have hn' : (n:ℝ) ≤ (N:ℝ) := by exact_mod_cast (by omega : n ≤ N)
      nlinarith [mul_le_mul_of_nonneg_right hn' hh.le]
    have hanti := clausen_two_pi_sub_eq (x := 2 * ((n : ℝ) * (π / N)))
      hθn1 hθn2
    have hbound := clausen_le_double_saddle
      (y := 2 * π - 2 * ((n : ℝ) * (π / N))) (by linarith) (by linarith)
    rw [hanti] at hbound
    have hkey : (π / N) * Real.log (whiteheadTerm N n 0)
        ≤ -clausen (2 * ((n:ℝ) * (π / N))) / 2 + masterErr N := by
      rw [hlogT']
      linarith [hdev.2]
    have h2key := mul_le_mul_of_nonneg_left hkey (by norm_num : (0:ℝ) ≤ 2)
    calc (2 * π / N) * Real.log (whiteheadTerm N n 0)
        = 2 * ((π / N) * Real.log (whiteheadTerm N n 0)) := by ring
      _ ≤ 2 * (-clausen (2 * ((n:ℝ) * (π / N))) / 2 + masterErr N) := h2key
      _ = -clausen (2 * ((n:ℝ) * (π / N))) + 2 * masterErr N := by ring
      _ ≤ 2 * clausen (π / 2) + 2 * masterErr N := by linarith [hbound]
      _ ≤ 4 * clausen (π / 2) + 10 * masterErr N := by linarith
  · -- interior: W4b deviation lands exactly on the 2D functional
    have hdev := abs_log_whiteheadTerm_deviation (N := N) (M := n) (k := k)
      hN hn1 hk1 (by omega)
    rw [abs_le] at hdev
    have hG := whiteheadFunctional2_le
      (u := 2 * ((n:ℝ) * (π / N))) (v := 2 * ((k:ℝ) * (π / N)))
      (by positivity) (by positivity)
      (by
        have hnk' : (n:ℝ) + (k:ℝ) ≤ (N:ℝ) - 1 := by
          have h : ((n + k : ℕ) : ℝ) ≤ ((N - 1 : ℕ) : ℝ) := by
            exact_mod_cast hnk
          rw [Nat.cast_sub (by omega), Nat.cast_one] at h
          push_cast at h
          linarith
        nlinarith [mul_le_mul_of_nonneg_right hnk' hh.le, hfield, hh])
    have hpsi : 2 * (2 * ((-clausen (2 * (((k:ℝ) + (n:ℝ)) * (π / N))) / 2)
            - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
         - (-clausen (2 * ((n:ℝ) * (π / N))) / 2))
        = whiteheadFunctional2 (2 * ((n:ℝ) * (π / N)))
            (2 * ((k:ℝ) * (π / N))) := by
      unfold whiteheadFunctional2
      rw [show 2 * ((n:ℝ) * (π / N)) + 2 * ((k:ℝ) * (π / N))
          = 2 * (((k:ℝ) + (n:ℝ)) * (π / N)) by ring]
      ring
    have h2 := mul_le_mul_of_nonneg_left hdev.2 (by norm_num : (0:ℝ) ≤ 2)
    calc (2 * π / N) * Real.log (whiteheadTerm N n k)
        = 2 * ((π / N) * Real.log (whiteheadTerm N n k)) := by ring
      _ ≤ 2 * ((2 * ((-clausen (2 * (((k:ℝ) + (n:ℝ)) * (π / N))) / 2)
              - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
           - (-clausen (2 * ((n:ℝ) * (π / N))) / 2)) + 5 * masterErr N) := by
            linarith [h2]
      _ = 2 * (2 * ((-clausen (2 * (((k:ℝ) + (n:ℝ)) * (π / N))) / 2)
              - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
           - (-clausen (2 * ((n:ℝ) * (π / N))) / 2)) + 10 * masterErr N := by
            ring
      _ = whiteheadFunctional2 (2 * ((n:ℝ) * (π / N)))
            (2 * ((k:ℝ) * (π / N))) + 10 * masterErr N := by rw [hpsi]
      _ ≤ 4 * clausen (π / 2) + 10 * masterErr N := by linarith [hG]

end QOU.Knot.FigureEightVolume
