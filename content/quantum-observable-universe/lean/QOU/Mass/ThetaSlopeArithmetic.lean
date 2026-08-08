/-
  Slope (theta-order) arithmetic for the sinh/cosh bridge between the proved
  q-lift kernel C1 and the GGM/Stokes carrier.

  Setting (docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md): five routes
  proved C1 (`[m+2]_q b_{m+2} = b_{m+1} + b_m`, Newton-polygon slopes {½,½})
  and GGM eq-49 (`y_{m+1} = (2−q^m) y_m − y_{m−1}`, slopes {−1,+1}) are
  inequivalent q-difference MODULES. Door-i proved the obstruction permanent:
  a ramified pullback `x ↦ x^{1/ℓ}` scales every slope uniformly by `ℓ`
  (RSZ Thm 2.2.1(iv)), so it maps the equal pair {½,½} to {ℓ/2,ℓ/2} — always
  an equal pair, never the distinct {−1,+1}.

  The owner's insight: the surviving NON-module carve-out is a sinh/cosh
  (bar-even/odd) twist. This file formalizes the SLOPE-LEVEL arithmetic making
  that precise: under PRODUCT of solutions slopes ADD (theta exponents:
  q^{s₁m²/2}·q^{s₂m²/2} = q^{(s₁+s₂)m²/2}); under the bar involution q ↦ q⁻¹
  slope NEGATES. Hence the symmetric square of a slope-½ solution f gives f² at
  slope 2·½ = 1 and its bar-conjugate (f̄)² at slope 2·(−½) = −1, so the
  bar-even (cosh) and bar-odd (sinh) parts of {f², (f̄)²} carry exactly the
  GGM slope multiset {+1,−1}.

  HONEST SCOPE. This proves the NECESSARY slope-matching — a dimensional
  consistency of the sinh/cosh bridge — NOT that GGM's solution space equals
  the sinh/cosh image of C1's (that exact-coefficient identity is the numerical
  Door-iii target, bean qou-ceg6, and a harder Lean goal). It does NOT
  contradict Door-i: the operation shown to reach {−1,+1} is nonlinear (a
  square), i.e. exactly the non-module class Door-i left open. Pure ℚ
  arithmetic on slopes; no archimedean content (§7c: slopes are rationals).

  WHAT IS INPUT AND WHAT IS OUTPUT (added 2026-08-08, bean qou-slpd). Read the
  theorems below as CONDITIONAL on two stipulations:

    * `c1Slope := 1/2` and `ggmSlopes := (-1, 1)` are DEFINITIONS. They are read
      off the numerics and the literature; nothing here derives them. So
      `pullback_cannot_reach_ggm` — genuinely proved — is ℚ arithmetic GIVEN
      them, and the "permanent invariant" conclusion inherits their status, not
      a theorem's.
    * `bar` and `prodSlope` are NOT in that category: `QGevreyOrder.bar_negates`
      and `QGevreyOrder.prod_adds` derive exactly those two laws from
      `IsQGevreyOrder`. Only the two slope VALUES are stipulated.

  ORDER vs LEVEL — the `½` is ambiguous as written. Ramis–Sauloy–Zhang §1.3.2
  define q-Gevrey ORDER `s` by `aₙ = O(Aⁿ q^{s n²/2})` and LEVEL as `1/s`; the
  two are reciprocal, and RSZ attaches the LEVEL to the Newton polygon (§2.3.2:
  "the one level case, because the q-Gevrey level `µ₂ − µ₁` is the fundamental
  parameter"; Ex. 3.3.3: `d := µ₂ − µ₁`, kernel growth `q^{n²/2d}`). In this
  corpus:

    * Route-B kernel `q^{m²/4}`  — order ½, level 2  (`routeB_gaussian_order_half`)
    * C1 `∞`-side `q^{n²}`       — order 2, level ½  (`c1InfCoeff_order_two`)

  Both are `½` in reciprocal senses (`routeB_and_c1Inf_are_reciprocal`). The
  grounding claimed for `c1Slope = ½` runs through the Route-B ORDER
  (`theta_eq_half_gs_bridge`), while RSZ would tie the slope to the LEVEL. Those
  cannot both be the Newton slope. This is NOT resolved by relabelling: it needs
  the Newton polygon of `L1` computed directly (bean `qou-slpd` item 4). Until
  then `c1Slope` is a stipulated rational whose identification with a Newton
  slope is a premise.

  -- Ref: [manuscript] docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md
  -- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §1.3.2 (order/level), §2.2 (Newton polygon), §2.3.2 + Ex. 3.3.3 (level = slope difference)
-/

import Mathlib.Tactic

namespace QOU.Mass.ThetaSlopeArithmetic

/-- Bar involution `q ↦ q⁻¹` on the Newton-polygon slope (theta order): it
    negates the slope (it inverts the q-Gevrey growth direction). -/
def bar (s : ℚ) : ℚ := -s

/-- Product of two solutions adds their slopes. -/
def prodSlope (s t : ℚ) : ℚ := s + t

/-- Ramified pullback `x ↦ x^{1/ℓ}` scales every slope uniformly by `ℓ`
    (RSZ Thm 2.2.1(iv)). -/
def pullback (l s : ℚ) : ℚ := l * s

/-- C1 — the proved q-lift kernel — is pure isoclinic of slope `½`.

**STIPULATED, not derived** — see the "what is input and what is output" and
"order vs level" notes in the module docstring. Every theorem below that
mentions `c1Slope` is conditional on this value being the Newton-polygon slope,
which is bean `qou-slpd` item 4. -/
def c1Slope : ℚ := 1 / 2

/-- GGM eq-49 slope multiset `{−1, +1}`.

**STIPULATED, not derived** — read off GGM eq-49; see the module docstring. -/
def ggmSlopes : ℚ × ℚ := (-1, 1)

/-- GGM is **anisoclinic**: its two slopes differ. (C1's are equal.) This is
    the invariant that separates the two modules. -/
theorem ggm_anisoclinic : ggmSlopes.1 ≠ ggmSlopes.2 := by
  simp only [ggmSlopes]; norm_num

/-- **Door-i obstruction, slope form: no ramified pullback reaches GGM.** A
    pullback of the equal pair `(½,½)` is again an equal pair `(ℓ/2, ℓ/2)`;
    it can never equal the distinct GGM pair `{−1,+1}`, for any `ℓ`. -/
theorem pullback_cannot_reach_ggm (l : ℚ) :
    (pullback l c1Slope, pullback l c1Slope) ≠ ggmSlopes := by
  simp only [pullback, c1Slope, ggmSlopes, ne_eq, Prod.mk.injEq]
  rintro ⟨h1, h2⟩
  rw [h1] at h2; norm_num at h2

/-- **The sinh/cosh twist reaches the GGM slope pair.** The symmetric square of
    a slope-`½` solution `f` sits at slope `2·½ = 1` (`f²`) and its
    bar-conjugate `(f̄)²` at slope `2·(−½) = −1`. The pair equals `(1, −1)`. -/
theorem sinhcosh_reaches_ggm :
    (prodSlope c1Slope c1Slope, prodSlope (bar c1Slope) (bar c1Slope))
      = (1, -1) := by
  simp only [prodSlope, bar, c1Slope]; norm_num

/-- …and `(1, −1)` **is** the GGM multiset (up to order). So the sinh/cosh
    (square + bar-even/odd) operation is dimensionally exactly the bridge that
    every module transform (Door-i) provably could not be. -/
theorem sinhcosh_eq_ggm_swap :
    (prodSlope c1Slope c1Slope, prodSlope (bar c1Slope) (bar c1Slope))
      = (ggmSlopes.2, ggmSlopes.1) := by
  simp only [prodSlope, bar, c1Slope, ggmSlopes]; norm_num

/-- The bar involution is an involution on slopes (`bar (bar s) = s`) — the
    algebraic reason the {+1,−1} pair is bar-stable as a set while the sole
    slope `½` of C1 is not. -/
theorem bar_involutive (s : ℚ) : bar (bar s) = s := by
  simp only [bar, neg_neg]

/-- GGM's slope multiset is bar-stable as a set (`bar` swaps its two slopes);
    C1's single slope `½` is not bar-fixed (`bar ½ = −½ ≠ ½`). This is the
    slope-level shadow of "GGM is bar-symmetric (sinh/cosh), C1 is not". -/
theorem ggm_bar_stable :
    (bar ggmSlopes.1 = ggmSlopes.2) ∧ (bar ggmSlopes.2 = ggmSlopes.1) := by
  simp only [bar, ggmSlopes]; norm_num

theorem c1_not_bar_fixed : bar c1Slope ≠ c1Slope := by
  simp only [bar, c1Slope]; norm_num

/-! ### GS/jet-filtration cumulative degree (the categorical side)

    The theta-order probe (docs/audits/2026-07-20-theta-jet-gb-filtration.md)
    observed NUMERICALLY that the binding kernel's leading Gaussian `θ_m ~ m²/4`
    is HALF the Gröbner–Shirshov cumulative q-degree `C(m,2) ~ m²/2`. Per the
    proof≠probe discipline, only the GS side is Lean-provable here (pure
    combinatorics); the analytic identification `θ-coeff = ¼` is probe evidence
    (Route B curvature `Δ²θ → ½`), NOT proved, and is deliberately NOT
    asserted in Lean. -/

/-- **GS-filtration cumulative q-degree = C(m,2).** The Hecke reducer's
    Gröbner–Shirshov normal forms are graded by Coxeter/word length; level `k`
    contributes degree `k`, so the cumulative degree through level `m` is
    `∑_{k<m} k = m(m−1)/2 = C(m,2)` — the top degree `ℓ(w₀)` of the longest
    element (corpus witness `gb-filtration-jet-order`). Pure ℕ combinatorics
    (`Finset.sum_range_id_mul_two`). This is the categorical grading the theta
    Gaussian is (numerically) half of. -/
theorem gs_cumulative_degree (m : ℕ) :
    (∑ k ∈ Finset.range m, k) * 2 = m * (m - 1) :=
  Finset.sum_range_id_mul_two m

/-- The GS cumulative degree in the `C(m,2)` closed form. Records the top-degree
    identity `∑_{k<m} k = ℓ(w₀) = C(m,2)` explicitly. -/
theorem gs_cumulative_degree_choose (m : ℕ) :
    (∑ k ∈ Finset.range m, k) = m.choose 2 := by
  have h := Finset.sum_range_id_mul_two m
  rw [Nat.choose_two_right]
  omega

end QOU.Mass.ThetaSlopeArithmetic
