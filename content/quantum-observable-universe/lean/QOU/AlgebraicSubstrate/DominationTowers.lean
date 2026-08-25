import QOU.AlgebraicSubstrate.DominationSqueeze

/-!
# QOU.AlgebraicSubstrate.DominationTowers — infinite towers, Ohtsuki, and the sweep

Three things `DominationSqueeze` left open, per beans `qou-w1bi`, `qou-7jbz`,
`qou-syf4`.

## §1 Filtration completeness (bean `qou-w1bi`)

`Domination.val_add_sum_eq` covers a **finite** tail (`List.sum`). A brane tower
is infinite, so it needs a convergence notion. `DeepTail` supplies one without
any topology: the tail `T` is *deeper than grade `γ`* when (a) every term is,
and (b) every finite truncation approximates `T` to arbitrary depth. Then
`lt_val_of_deepTail` gives `γ < val T`, and `leading_survives_infinite_tail`
concludes `val (a₀ + T) = val a₀` — **the infinite tower does not collapse onto
its leading term.**

## §2 The Ohtsuki tower (bean `qou-7jbz`, route to `qou-7jok`)

The Ohtsuki tower `𝔙_b = 𝔙₀ + Σ_{n≥1} κₙ (2πb²)ⁿ`
([`rem-ohtsuki-tower-bar-parity`](../../../quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md))
is a coefficient sequence in `ℏ = 2πb²` with the complex volume at grade `0`.
That is exactly `jetDomination`'s home, so no new structure is needed —
`ohtsukiVal := jetVal` on the coefficient sequence.

The payoff is `grade_pos_iff_leading_vanishes`: for a tower `κ`,

  `0 < jetVal κ  ↔  κ 0 = 0`.

Read on a polynomial combination of three towers, that is precisely the
criterion the 2026-08-09 audit identified as the productive route:
**`ord_ω(P(𝔙)) > 0` exactly when `P(Vol) = 0`.** The grade genuinely separates
relation from non-relation at the lifted level — unlike on `ℝ`, where
`QOU.Archimedean.SurrealGradingPrune` shows every non-relation shares one grade.

`relation_forces_positive_grade` and `no_relation_of_grade_zero` are the two
directions, in the shape `qou-7jok` consumes.

## §3 The millennium sweep (bean `qou-syf4`)

`rem:collatz-surreal-bound`, `rem:p-vs-np-surreal-bound` and
`rem:ns-surreal-bound` all instantiate one inequality — `δ²·ε⁻¹ > ε³`, times a
positive scalar (`2ⁿ` in the P-vs-NP case, which that remark handles by
"multiplying through by the standard-real factor `2ⁿ` preserves the
inequality"). `squeeze_scaled` is that step; the three named corollaries below
are the instantiations.

**These are restatements, not proofs of the millennium problems.** Each
corollary proves the *inference step* the corresponding remark invokes, from
hypotheses that remark supplies. The premises — Reeb-period budget accounting,
`BQP_q → P` non-compressibility, the `std`-of-the-skein assumption — are
untouched and remain exactly as conjectural as before.

## What is still open

The **Newton-polyhedron generalisation**: `Domination.val` lands in a
*linearly* ordered `Γ`, but a q-difference equation's natural invariant is its
Newton polygon, valued in a *lattice*-ordered group (`ℤⁿ`/`ℚⁿ`), where a linear
order appears only after choosing a supporting functional. In that setting an
archimedean inequality becomes a **face-membership / LP-feasibility test**
against the polyhedron. The corpus already scaffolds the one-dimensional shadow
of this in `QOU.Mathlib.QGevreyOrder` (slopes, `-- Ref: [ramis-sauloy-zhang2013]
q-difference Newton-polygon slopes / q-Gevrey`), whose own docstring lists the
Newton-polygon convolution law as out of scope — and that law is exactly the
abstract `le_val_add` axiom here. Tracked as bean `qou-filh`; not built in this
file.
-/

namespace QOU.AlgebraicSubstrate

variable {A : Type*} [AddCommGroup A] {Γ : Type*} [LinearOrder Γ]

/-! ## §1  Filtration completeness -/

/-- Finite truncation of a tower: `a 0 + … + a (n-1)`. -/
def towerTrunc (a : ℕ → A) (n : ℕ) : A := ((List.range n).map a).sum

@[simp] theorem towerTrunc_zero (a : ℕ → A) : towerTrunc a 0 = 0 := by
  simp [towerTrunc]

theorem Domination.lt_val_towerTrunc (D : Domination A Γ) {γ : Γ} {a : ℕ → A}
    (h : ∀ n, (γ : WithTop Γ) < D.val (a n)) (n : ℕ) :
    (γ : WithTop Γ) < D.val (towerTrunc a n) := by
  refine D.lt_val_sum_grade _ ?_
  intro b hb
  obtain ⟨i, _, rfl⟩ := List.mem_map.mp hb
  exact h i

/-- **The tail is deep** — convergence in the filtration, with no topology.

`terms`: every term of the tail sits strictly below grade `γ`.
`approx`: finite truncations approximate `T` to arbitrary depth. -/
structure DeepTail (D : Domination A Γ) (γ : Γ) (T : A) (a : ℕ → A) : Prop where
  /-- Every tail term is strictly deeper than `γ`. -/
  terms : ∀ n, (γ : WithTop Γ) < D.val (a n)
  /-- Truncations approximate `T` arbitrarily deeply. -/
  approx : ∀ β : Γ, ∃ N, (β : WithTop Γ) < D.val (T - towerTrunc a N)

/-- **The infinite tail is deeper than `γ`.** The finite machinery plus one
approximation step; no completion of `A` is required. -/
theorem lt_val_of_deepTail {D : Domination A Γ} {γ : Γ} {T : A} {a : ℕ → A}
    (h : DeepTail D γ T a) : (γ : WithTop Γ) < D.val T := by
  obtain ⟨N, hN⟩ := h.approx γ
  have hsplit : T = (T - towerTrunc a N) + towerTrunc a N := by
    rw [sub_add_cancel]
  rw [hsplit]
  exact D.lt_val_add' hN (D.lt_val_towerTrunc h.terms N)

/-- **The leading term survives an infinite tail.**

`val (a₀ + T) = val a₀` whenever every tail term — and hence the whole tail —
is strictly deeper than `a₀`. This is `val_add_sum_eq` freed of finiteness:
the brane tower does not collapse onto its leading level. -/
theorem leading_survives_infinite_tail {D : Domination A Γ} {a₀ T : A} {γ : Γ}
    {a : ℕ → A} (hlead : D.val a₀ = (γ : WithTop Γ)) (h : DeepTail D γ T a) :
    D.val (a₀ + T) = D.val a₀ :=
  D.val_add_eq_of_lt (by rw [hlead]; exact lt_val_of_deepTail h)

/-- **The infinite tower is non-zero.** The perpetual-obstruction statement in
algebraic form: a non-zero leading level cannot be cancelled by its tail. -/
theorem infinite_tower_ne_zero {D : Domination A Γ} {a₀ T : A} {γ : Γ}
    {a : ℕ → A} (hlead : D.val a₀ = (γ : WithTop Γ)) (h : DeepTail D γ T a) :
    a₀ + T ≠ 0 :=
  D.add_ne_zero_of_val_lt (by rw [hlead]; exact lt_val_of_deepTail h)

/-! ## §2  The Ohtsuki tower -/

/-- Grade of an Ohtsuki tower, as its `ℏ`-coefficient sequence: the leading
order in `ℏ = 2πb²`. Definitionally `jetVal`; named separately so call sites
say which object they mean. -/
noncomputable abbrev ohtsukiVal (κ : ℕ → ℝ) : WithTop ℕ := jetVal κ

/-- **The grade sees the leading coefficient — and nothing else does.**

`0 < ohtsukiVal κ ↔ κ 0 = 0`. On a polynomial combination of towers this reads:
the combination has strictly positive grade exactly when the relation holds
among the grade-`0` parts (the complex volumes).

This is the separation the surreal prune shows is *unavailable* on `ℝ`, where
every non-relation shares grade `0`. Lifting to the tower restores it. -/
theorem grade_pos_iff_leading_vanishes (κ : ℕ → ℝ) :
    (0 : WithTop ℕ) < ohtsukiVal κ ↔ κ 0 = 0 := by
  constructor
  · intro h; exact eq_zero_of_lt_jetVal (by exact_mod_cast h)
  · intro h0
    by_contra hle
    push_neg at hle
    have hz : jetVal κ = ((0 : ℕ) : WithTop ℕ) :=
      le_antisymm (by exact_mod_cast hle) (by simp)
    exact ne_zero_of_jetVal_eq hz h0

/-- **A relation among the leading parts lifts the grade** — the direction
`qou-7jok` needs: if `P(Vol) = 0`, the tower combination `P(𝔙)` is a pure
positive-grade series, so the relation imposes conditions on the arithmetic
coefficients `κₙ` (`n ≥ 1`) rather than on the volumes. -/
theorem relation_forces_positive_grade {κ : ℕ → ℝ} (h : κ 0 = 0) :
    (0 : WithTop ℕ) < ohtsukiVal κ :=
  (grade_pos_iff_leading_vanishes κ).mpr h

/-- **Contrapositive — grade `0` certifies no relation.** A tower combination of
grade `0` has a non-vanishing leading part, i.e. `P(Vol) ≠ 0`. This is the
usable test: compute the grade, read off non-vanishing. -/
theorem no_relation_of_grade_zero {κ : ℕ → ℝ} (h : ohtsukiVal κ = (0 : WithTop ℕ)) :
    κ 0 ≠ 0 := by
  intro h0
  exact absurd ((grade_pos_iff_leading_vanishes κ).mpr h0) (by rw [h]; simp)

/-! ## §3  The millennium sweep -/

section Millennium

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Surreal squeeze (shared core).** Restated here so this file is the single
place the millennium bounds cite. Identical to
`appendix-surreals/surreal-squeeze.lean`'s `surreal_squeeze`. -/
theorem squeeze_core (ε δ : K) (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    ε ^ 3 < δ ^ 2 * ε⁻¹ := by
  rw [← div_eq_mul_inv]
  exact (pow_lt_one₀ hε.le hε1 (by norm_num)).trans ((one_lt_div hε).mpr hεδ)

/-- **Scaled squeeze.** Multiplying through by a positive standard factor
preserves the inequality — the step `rem:p-vs-np-surreal-bound` performs with
the factor `2ⁿ`. -/
theorem squeeze_scaled (c ε δ : K) (hc : 0 < c)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    c * ε ^ 3 < c * (δ ^ 2 * ε⁻¹) :=
  mul_lt_mul_of_pos_left (squeeze_core ε δ hε hε1 hεδ) hc

/-- **q-Collatz bound** (`rem:collatz-surreal-bound`). The accumulated
contact-volume deviation `V(δ) ≍ δ²·ε⁻¹` over one Reeb period strictly exceeds
the mass-gap dissipation `Δ_q ≍ ε³`, so no rogue orbit with standard-real drift
`δ` can be re-absorbed.

Proves the remark's *inference step* only; the contact-boundary model and the
`std`-of-the-skein-resolution assumption are its premises, untouched here. -/
theorem collatz_drift_exceeds_dissipation (ε δ : K)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    ε ^ 3 < δ ^ 2 * ε⁻¹ :=
  squeeze_core ε δ hε hε1 hεδ

/-- **P-vs-NP bound** (`rem:p-vs-np-surreal-bound`). For an NP-complete instance
of size `n`, the classical simulation cost `2ⁿ·δₙ²·Ω_q` exceeds the mass-gap
budget `2ⁿ·Δ_q` available over the same Reeb period.

Proves the remark's *inference step* only. That remark is explicitly
conditional on an independent non-compressibility conjecture for
`BQP_q → P`, which nothing here establishes. -/
theorem pnp_simulation_exceeds_budget (twoPowN ε δ : K) (hpos : 0 < twoPowN)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    twoPowN * ε ^ 3 < twoPowN * (δ ^ 2 * ε⁻¹) :=
  squeeze_scaled twoPowN ε δ hpos hε hε1 hεδ

/-- **q-NS blowup bound** (`rem:ns-surreal-bound`). The enstrophy cost of a
standard-scale singular deviation exceeds the dissipation budget.

Proves the remark's *inference step* only; the q-NS conjecture cone
(`conj:q-aubin-lions`, `conj:ns-counterexample`, `conj:critical-exponent`,
`conj:blowup-yekutieli`, `conj:regularity-breakdown`) is its premise set and is
untouched. Note those five classes are *not* hypotheses of this lemma — the
inequality never depended on them; see the rewrite note in
`appendix-surreals/surreal-squeeze.lean`. -/
theorem ns_enstrophy_exceeds_dissipation (ε δ : K)
    (hε : 0 < ε) (hε1 : ε < 1) (hεδ : ε < δ ^ 2) :
    ε ^ 3 < δ ^ 2 * ε⁻¹ :=
  squeeze_core ε δ hε hε1 hεδ

end Millennium

end QOU.AlgebraicSubstrate
