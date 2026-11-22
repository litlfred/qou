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

    * `c1Slope := 1/2` and `ggmSlopes := (-1, 1)` are DEFINITIONS. **Both are
      now also DERIVED** — see the Newton-polygon section at the bottom of this
      file: `c1Slope_eq_newton` and `ggmSlopes_eq_newton` compute them from the
      operators' coefficient valuations, and `newtonSlopes_c1_ne_ggm` gives
      Door-i straight off the two polygons. So `pullback_cannot_reach_ggm` is no
      longer ℚ arithmetic over hand-entered constants.
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
  cannot both be the Newton slope. The Newton polygon of `L1` is now computed
  (bottom of this file), which pins the NUMBER `½`; it does not by itself say
  which growth quantity that number is. That identification — Newton slope ↔
  q-Gevrey order, or ↔ level — is the premise that remains.

  -- Ref: [leitner2026] docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md
  -- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §1.3.2 (order/level), §2.2 (Newton polygon), §2.3.2 + Ex. 3.3.3 (level = slope difference)
-/

import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas

namespace QOU.Mass.ThetaSlopeArithmetic

open Polynomial

/-- Bar involution `q ↦ q⁻¹` on the Newton-polygon slope (theta order): it
    negates the slope (it inverts the q-Gevrey growth direction). -/
def bar (s : ℚ) : ℚ := -s

/-- Product of two solutions adds their slopes. -/
def prodSlope (s t : ℚ) : ℚ := s + t

/-- Ramified pullback `x ↦ x^{1/ℓ}` scales every slope uniformly by `ℓ`
    (RSZ Thm 2.2.1(iv)). -/
def pullback (l s : ℚ) : ℚ := l * s

/-- C1 — the proved q-lift kernel — is pure isoclinic of slope `½`.

**DERIVED** as of 2026-08-08: `c1Slope_eq_newton` at the bottom of this file
proves this value is the computed Newton slope of `L1` at `∞`. It remains a
`def` so the theorems above keep their shape. What is still a premise is which
q-Gevrey growth quantity this number is — see the "order vs level" note in the
module docstring. -/
def c1Slope : ℚ := 1 / 2

/-- GGM eq-49 slope multiset `{−1, +1}`.

**DERIVED** as of 2026-08-08 by `ggmSlopes_eq_newton`, from the Newton polygon
of `L2 = σ² − (2 − qx)σ + 1` at `∞`. -/
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


/-! ## The Newton polygons, computed — `c1Slope` and `ggmSlopes` are no longer stipulated

Added 2026-08-08 (bean `qou-slpd` item 4). Everything above took the two slope
values as definitions. This section derives them from the operators, so the
Door-i obstruction rests on a computation rather than on two hand-entered
rationals.

Operators in `x = q^m` with `σ : x ↦ qx`
(`docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md` §1), then pushed to
`∞` in the RSZ frame `w = 1/x`, `σ̃ : w ↦ qw`, denominators cleared:

* **C1** `L1 = (q²x − 1)σ² − (q−1)σ − (q−1)`
  ⟶ `−(q−1)w·σ̃² − (q−1)w·σ̃ + (1−w)`, valuations `(0, 1, 1)`.
* **GGM eq-49** `L2 = σ² − (2 − qx)σ + 1`
  ⟶ `qw·σ̃² + (1−2qw)·σ̃ + qw`, valuations `(1, 0, 1)`.

The valuations are **proved** from the coefficient polynomials
(`c1_valuations`, `ggm_valuations`) via `natTrailingDegree`, not read off by
eye; RSZ §2.2.1's lower hull is then `newtonSlopes`. C1's middle point `(1,1)`
sits strictly above the segment `(0,0) → (2,1)` (mid-height `½ < 1`), giving one
edge `(r,d) = (2,1)` — slope `½` with multiplicity 2, pure isoclinic and
non-integral. GGM's `(1,0)` is a vertex, giving two edges of slopes `−1`, `+1`.

The audit called this "exact hand algebra" and asked for formalize-first. This
is that.

**Sign convention.** RSZ changed terminology so that module slopes are the
negatives of the older operator convention (Astérisque 355, footnote 2 p. 16,
Example 2.2.2, `r_{M∨}(µ) = r_M(−µ)`); the change negates every slope uniformly,
so `newtonSlopes_c1_ne_ggm` — the only thing Door-i needs — is unaffected.

**Still not settled by this**: whether the Newton slope is the q-Gevrey *order*
or *level* of a given solution sequence. See the order/level note in the module
docstring. Computing the polygon pins the number `½`; it does not by itself say
which growth quantity that number is. -/

/-- The three `w`-adic valuations `(v(a₀), v(a₁), v(a₂))` of an order-2
q-difference operator `a₂σ̃² + a₁σ̃ + a₀`. -/
structure Order2Valuations where
  v0 : ℤ
  v1 : ℤ
  v2 : ℤ

/-- **RSZ §2.2.1 Newton slopes, order 2.** Lower convex hull of
`{(0,v₀), (1,v₁), (2,v₂)}`. The middle point lies strictly *above* the segment
`(0,v₀) → (2,v₂)` exactly when `v₀ + v₂ < 2v₁`; then the hull is one edge of
horizontal length `2` and the slope `(v₂−v₀)/2` occurs with multiplicity `2`.
Otherwise the hull breaks at `(1,v₁)` into two edges of length `1`. -/
def newtonSlopes (d : Order2Valuations) : Multiset ℚ :=
  if d.v0 + d.v2 < 2 * d.v1 then
    Multiset.replicate 2 (((d.v2 - d.v0 : ℤ) : ℚ) / 2)
  else
    {((d.v1 - d.v0 : ℤ) : ℚ), ((d.v2 - d.v1 : ℤ) : ℚ)}

section Operators

variable {R : Type*} [CommRing R] [IsDomain R]

/-- `L1` (C1) at `∞`, RSZ frame `w = 1/x`, denominators cleared:
`−(q−1)w·σ̃² − (q−1)w·σ̃ + (1−w)`. -/
noncomputable def c1A0 : R[X] := 1 - X
noncomputable def c1A1 (q : R) : R[X] := -(C (q - 1)) * X
noncomputable def c1A2 (q : R) : R[X] := -(C (q - 1)) * X

/-- `L2` (GGM eq-49) at `∞`: `qw·σ̃² + (1−2qw)·σ̃ + qw`. -/
noncomputable def ggmA0 (q : R) : R[X] := C q * X
noncomputable def ggmA1 (q : R) : R[X] := 1 - C (2 * q) * X
noncomputable def ggmA2 (q : R) : R[X] := C q * X

private lemma ntd_C_mul_X {c : R} (hc : c ≠ 0) : (C c * X : R[X]).natTrailingDegree = 1 := by
  rw [natTrailingDegree_mul (by simpa using hc) X_ne_zero]
  simp

private lemma ntd_one_sub {c : R} : ((1 : R[X]) - C c * X).natTrailingDegree = 0 := by
  refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
  simp

/-- The C1 valuation triple at `∞` is `(0, 1, 1)`. -/
theorem c1_valuations (q : R) (hq : q - 1 ≠ 0) :
    ((c1A0 : R[X]).natTrailingDegree, (c1A1 q).natTrailingDegree,
      (c1A2 q).natTrailingDegree) = (0, 1, 1) := by
  have h1 : (c1A1 q).natTrailingDegree = 1 := by
    have : (c1A1 q) = C (-(q - 1)) * X := by rw [c1A1]; simp
    rw [this]
    exact ntd_C_mul_X (neg_ne_zero.mpr hq)
  have h2 : (c1A2 q).natTrailingDegree = 1 := by
    have : (c1A2 q) = C (-(q - 1)) * X := by rw [c1A2]; simp
    rw [this]
    exact ntd_C_mul_X (neg_ne_zero.mpr hq)
  have h0 : (c1A0 : R[X]).natTrailingDegree = 0 := by
    have : (c1A0 : R[X]) = 1 - C (1 : R) * X := by rw [c1A0]; simp
    rw [this]; exact ntd_one_sub
  rw [h0, h1, h2]

/-- The GGM valuation triple at `∞` is `(1, 0, 1)`. -/
theorem ggm_valuations (q : R) (hq : q ≠ 0) :
    ((ggmA0 q).natTrailingDegree, (ggmA1 q).natTrailingDegree,
      (ggmA2 q).natTrailingDegree) = (1, 0, 1) := by
  have h0 : (ggmA0 q).natTrailingDegree = 1 := ntd_C_mul_X hq
  have h2 : (ggmA2 q).natTrailingDegree = 1 := ntd_C_mul_X hq
  have h1 : (ggmA1 q).natTrailingDegree = 0 := by rw [ggmA1]; exact ntd_one_sub
  rw [h0, h1, h2]

end Operators

/-- C1's Newton data at `∞`, from `c1_valuations`. -/
def c1AtInfinity : Order2Valuations := ⟨0, 1, 1⟩

/-- GGM's Newton data at `∞`, from `ggm_valuations`. -/
def ggmAtInfinity : Order2Valuations := ⟨1, 0, 1⟩

/-- **C1 is pure isoclinic of slope ½ at `∞`** — computed, not stipulated. -/
theorem newtonSlopes_c1 : newtonSlopes c1AtInfinity = Multiset.replicate 2 (1 / 2 : ℚ) := by
  norm_num [newtonSlopes, c1AtInfinity]

/-- **GGM is anisoclinic with slopes `{−1, +1}` at `∞`** — computed. -/
theorem newtonSlopes_ggm : newtonSlopes ggmAtInfinity = {(-1 : ℚ), 1} := by
  norm_num [newtonSlopes, ggmAtInfinity]

/-- **`c1Slope` is DERIVED**: the stipulated `½` is the computed Newton slope. -/
theorem c1Slope_eq_newton : newtonSlopes c1AtInfinity = Multiset.replicate 2 c1Slope := by
  rw [newtonSlopes_c1, c1Slope]

/-- **`ggmSlopes` is DERIVED**. -/
theorem ggmSlopes_eq_newton :
    newtonSlopes ggmAtInfinity = {ggmSlopes.1, ggmSlopes.2} := by
  rw [newtonSlopes_ggm, ggmSlopes]

/-- **Door-i, from the polygons rather than from two stipulated numbers.** -/
theorem newtonSlopes_c1_ne_ggm : newtonSlopes c1AtInfinity ≠ newtonSlopes ggmAtInfinity := by
  intro h
  rw [newtonSlopes_c1, newtonSlopes_ggm] at h
  have hmem : (-1 : ℚ) ∈ ({(-1 : ℚ), 1} : Multiset ℚ) := by simp
  rw [← h, Multiset.mem_replicate] at hmem
  norm_num at hmem

/-- **C1's polygon really is isoclinic**: every slope in it equals `c1Slope`. -/
theorem c1_isoclinic_of_newton : ∀ s ∈ newtonSlopes c1AtInfinity, s = c1Slope := by
  intro s hs
  rw [c1Slope_eq_newton, Multiset.mem_replicate] at hs
  exact hs.2

end QOU.Mass.ThetaSlopeArithmetic
