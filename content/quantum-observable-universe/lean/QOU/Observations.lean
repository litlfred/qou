/-!
# QOU.Observations — Ch observations stubs (Lake-buildable)

Real-statement upgrades of the four observations-chapter stubs.
Where a claim is a direct numerical bound on a CODATA or PDG
observable the statement is stated in closed form with a
sorry-bridged proof; more structural claims (regime switches
indexed by `(Z, N)`, magic-number peaks in a second-difference
signal) are packaged as records so consumers can project the
individual invariants without committing to the full Hecke /
semidefinite-programming layer.
-/

import Mathlib.Tactic

namespace QOU.Observations

/-- **prop:magic-numbers-from-q** — the nuclear magic numbers
    `{2, 8, 20, 28}` emerge as peaks in the Wedderburn-weighted
    second-difference signal `δ²Φ(Z)` computed from Hoefsmit
    seminormal characters at Hecke levels `k = 3 … 10`. -/
structure MagicNumbersFromQ where
  /-- Wedderburn-weighted character signal `Φ : ℕ → ℝ`. -/
  Φ : ℕ → ℝ
  /-- The forward second difference `δ²Φ(Z) = Φ(Z) - 2Φ(Z-1) + Φ(Z-2)`. -/
  δ2Φ : ℕ → ℝ
  /-- Recurrence definition. -/
  δ2Φ_eq : ∀ Z, 2 ≤ Z → δ2Φ Z = Φ Z - 2 * Φ (Z - 1) + Φ (Z - 2)
  /-- The signal peaks (is strictly positive) at every magic number. -/
  peaks_at_magic : ∀ Z ∈ ({2, 8, 20, 28} : Set ℕ), 0 < δ2Φ Z

/-- Existence form of the magic-numbers claim: there is a uniform
    positive lower bound on `δ²Φ` across the four magic numbers. -/
theorem magic_numbers_from_q (m : MagicNumbersFromQ) :
    ∃ c : ℝ, 0 < c ∧ ∀ Z ∈ ({2, 8, 20, 28} : Set ℕ), c ≤ m.δ2Φ Z := by
  -- Ref: [manuscript] §observations/magic-numbers-from-q
  sorry

/-- **prop:sdp-regime-switch** — at fixed substrate parameter `q₀`,
    the SDP-dual cross-block coupling `c_{λλ'}` between conjugate
    partition pairs changes sign discretely as `(Z, N)` varies;
    isolated zeros mark nuclear-structure regime switches. -/
structure SDPRegimeSwitch where
  /-- Substrate parameter. -/
  q₀ : ℝ
  q₀_gt_one : 1 < q₀
  /-- Cross-block coupling, indexed by `(Z, N)`. -/
  c : ℕ → ℕ → ℝ

/-- If the coupling vanishes at `(Z, N)` then the sign-crossing
    product against any neighbour vanishes identically. -/
theorem sdp_regime_switch (s : SDPRegimeSwitch) (Z N : ℕ)
    (h : s.c Z N = 0) :
    s.c Z N * s.c (Z + 1) N = 0 ∧ s.c Z N * s.c Z (N + 1) = 0 := by
  -- Ref: [manuscript] §observations/sdp-regime-switch
  refine ⟨?_, ?_⟩ <;> simp [h]

/-- **prop:strangelet-crossing-energy** (neutrality): a
    `(u, d, s)` Borromean triple has zero Coulomb charge. -/
theorem strangelet_neutrality : (2 : ℚ) / 3 - 1 / 3 - 1 / 3 = 0 := by
  -- Ref: [manuscript] §observations/strangelet-crossing-energy
  norm_num

/-- **prop:strangelet-crossing-energy** (energy): the crossing
    energy of an `N`-unit strangelet is non-negative, scaling
    linearly with `N` via the single-triple strong channel. -/
theorem strangelet_crossing_energy
    (E_triple : ℝ) (hE : 0 ≤ E_triple) (N : ℕ) :
    0 ≤ (N : ℝ) * E_triple := by
  -- Ref: [manuscript] §observations/strangelet-crossing-energy
  positivity

/-- **prop:substrate-consistency-window** — the lepton-mass,
    electromagnetic-coupling, and tritium half-life determinations
    of `q` each pin `q` to a narrow range, and those ranges
    overlap on `[1.109, 1.112]`.  Recorded as the non-emptiness
    of the triple intersection. -/
theorem substrate_consistency_window :
    ({ q : ℝ | |q - 1.10997| ≤ 0.001 } ∩
     { q : ℝ | |q - 1.11023| ≤ 0.00002 } ∩
     { q : ℝ | 1.109 ≤ q ∧ q ≤ 1.112 }).Nonempty := by
  -- Ref: [manuscript] §observations/substrate-consistency-window
  refine ⟨1.11023, ?_⟩
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · show |(1.11023 : ℝ) - 1.10997| ≤ 0.001
    rw [show (1.11023 : ℝ) - 1.10997 = 0.00026 by norm_num,
        abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 0.00026)]
    norm_num
  · show |(1.11023 : ℝ) - 1.11023| ≤ 0.00002
    simp
  · exact ⟨by norm_num, by norm_num⟩

end QOU.Observations
