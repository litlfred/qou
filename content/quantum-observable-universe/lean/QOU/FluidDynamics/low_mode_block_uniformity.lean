import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# QOU.FluidDynamics.low_mode_block_uniformity

**The ε-uniformity reduction** — the millennium remainder of epic
`qou-a3n3` reduced to one named spectral hypothesis (bean `qou-habm`;
formalize-first: this file states and proves the invariant that any
future probe or estimate must target, before any wide search runs).

`low_mode_block_global.lean` proved large-data global persistence *at
the fixed block* with the bound `Ω ≤ kmax²·E₀`, non-uniform in `ε`
because the block's top rung `kmax = [m]_{1+ε}` diverges as `q → 1⁺`.
This file splits the enstrophy at a **fixed** band `B` (independent of
`ε`; `K` is reserved for the coefficient field) and proves:

  `Ω  =  Ω_{≤B} + Ω_{>B}  ≤  kB²·E + Ω_{>B}`,

so the `ε`-uniform large-data bound holds **iff** the above-band tail
enstrophy `Ω_{>B}` is uniformly bounded — *"no enstrophy pile-up at
the receding damping threshold."*  The fixed-band part is proved
(`banded_enstrophy_le`); the tail is the named hypothesis
(`uniformity_reduction`), and the trivial converse (`tail_le_total`)
closes the equivalence.  Everything is finite-sum algebra over a
generic ordered field (§7c) on a spectral energy distribution
`e : ℕ → K` with ladder `k : ℕ → K`.

**Structural observation recorded alongside (vanishing viscosity).**
The q-ladder viscosity is `ν_q = (q−1)/(2q) = ε/(2(1+ε))`, which
**vanishes in the classical limit** — so the discrete Leray bound of
`low_mode_block_global` degrades at the explicit rate
`∑Ω ≤ 2(1+ε)·E₀/(δ·ε)` (`leray_bound_scaling` below), and the in-QOU
classical limit is a *vanishing-viscosity* (Euler-type) limit, not a
fixed-`ν` Navier–Stokes limit.  Mapping the in-QOU statement onto the
fixed-`ν` millennium formulation therefore requires the
substrate-to-physical rescaling of time/length units — a modeling step
that must be chosen explicitly, and is flagged (not chosen) here.

What this file does **not** do: prove or refute the tail hypothesis.
It is the honest open frontier; the reduction tells the next agent
exactly what to measure (the above-fixed-band enstrophy fraction as
`ε → 0` — a candidate SF5 shell probe) or what estimate to attempt
(a flux bound localizing dissipation below a fixed band).
-/

namespace QOU.FluidDynamics.LowModeUniformity

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Block energy: the total spectral energy over the block `range m`. -/
def blockEnergy (e : ℕ → K) (m : ℕ) : K := ∑ n ∈ Finset.range m, e n

/-- Block enstrophy: the `k²`-weighted spectral energy. -/
def blockEnstrophy (k e : ℕ → K) (m : ℕ) : K :=
  ∑ n ∈ Finset.range m, (k n) ^ 2 * e n

/-- Above-band tail enstrophy: the part of the block enstrophy carried
    by rungs past the fixed band `B`. -/
def tailEnstrophy (k e : ℕ → K) (B m : ℕ) : K :=
  ∑ n ∈ (Finset.range m).filter (fun n => B < n), (k n) ^ 2 * e n

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **Enstrophy splits at any band**: block enstrophy = banded part +
    tail (a partition of the finite sum). -/
theorem enstrophy_split (k e : ℕ → K) (B m : ℕ) :
    blockEnstrophy k e m
      = (∑ n ∈ (Finset.range m).filter (fun n => ¬ B < n),
          (k n) ^ 2 * e n) + tailEnstrophy k e B m := by
  unfold blockEnstrophy tailEnstrophy
  rw [add_comm]
  exact (Finset.sum_filter_add_sum_filter_not (Finset.range m)
    (fun n => B < n) _).symm

/-- **The banded part is uniformly controlled by the energy**: if the
    ladder is bounded by `kB` on the band (`n ≤ B`) and the spectral
    energies are nonnegative, then the banded enstrophy is at most
    `kB²·E`.  This constant depends only on the *fixed* band, never on
    the block width `m` — the `ε`-uniform half of the split. -/
theorem banded_enstrophy_le (k e : ℕ → K) (B m : ℕ) (kB : K)
    (he : ∀ n, 0 ≤ e n) (hk : ∀ n ≤ B, (k n) ^ 2 ≤ kB ^ 2) :
    (∑ n ∈ (Finset.range m).filter (fun n => ¬ B < n), (k n) ^ 2 * e n)
      ≤ kB ^ 2 * blockEnergy e m := by
  unfold blockEnergy
  calc ∑ n ∈ (Finset.range m).filter (fun n => ¬ B < n), (k n) ^ 2 * e n
      ≤ ∑ n ∈ (Finset.range m).filter (fun n => ¬ B < n), kB ^ 2 * e n := by
        apply Finset.sum_le_sum
        intro n hn
        have hnB : n ≤ B := le_of_not_gt (Finset.mem_filter.mp hn).2
        exact mul_le_mul_of_nonneg_right (hk n hnB) (he n)
    _ = kB ^ 2 * ∑ n ∈ (Finset.range m).filter (fun n => ¬ B < n), e n := by
        rw [Finset.mul_sum]
    _ ≤ kB ^ 2 * ∑ n ∈ Finset.range m, e n := by
        apply mul_le_mul_of_nonneg_left _ (sq_nonneg kB)
        exact Finset.sum_le_sum_of_subset_of_nonneg
          (Finset.filter_subset _ _) (fun n _ _ => he n)

/-- **The ε-uniformity reduction**: block enstrophy is at most
    `kB²·E + tail`.  Since `kB` and (via energy monotonicity,
    `low_mode_block_global.energy_le_initial`) `E ≤ E₀` are uniform in
    the block width, an `ε`-uniform enstrophy bound holds **iff** the
    above-band tail enstrophy is uniformly bounded.  The tail is the
    named open hypothesis — "no enstrophy pile-up at the receding
    threshold"; nothing in the corpus proves or refutes it. -/
theorem uniformity_reduction (k e : ℕ → K) (B m : ℕ) (kB : K)
    (he : ∀ n, 0 ≤ e n) (hk : ∀ n ≤ B, (k n) ^ 2 ≤ kB ^ 2) :
    blockEnstrophy k e m
      ≤ kB ^ 2 * blockEnergy e m + tailEnstrophy k e B m := by
  rw [enstrophy_split k e B m]
  exact add_le_add_right (banded_enstrophy_le k e B m kB he hk) _

/-- The trivial converse: the tail never exceeds the total (spectral
    energies nonnegative), so unbounded tail forces unbounded total —
    the reduction is an equivalence, not just an upper bound. -/
theorem tail_le_total (k e : ℕ → K) (B m : ℕ)
    (he : ∀ n, 0 ≤ e n) :
    tailEnstrophy k e B m ≤ blockEnstrophy k e m := by
  unfold tailEnstrophy blockEnstrophy
  exact Finset.sum_le_sum_of_subset_of_nonneg
    (Finset.filter_subset _ _)
    (fun n _ _ => mul_nonneg (sq_nonneg (k n)) (he n))

/-- **The vanishing-viscosity scaling of the Leray bound**: with the
    q-ladder viscosity `ν_q = ε/(2(1+ε))`, the discrete Leray bound
    `δ·ν_q·∑Ω ≤ E₀` of `low_mode_block_global` rearranges to
    `∑Ω ≤ 2(1+ε)·E₀/(δ·ε)` — the cumulative-enstrophy control
    degrades at the explicit rate `ε⁻¹` because the in-QOU classical
    limit sends the viscosity itself to zero.  (The fixed-`ν`
    millennium formulation therefore sits across a substrate-to-
    physical rescaling; flagged in the module docstring.) -/
theorem leray_bound_scaling (ε δ E0 S : K) (hε : 0 < ε) (hδ : 0 < δ)
    (hbound : δ * (ε / (2 * (1 + ε))) * S ≤ E0) :
    S ≤ 2 * (1 + ε) * E0 / (δ * ε) := by
  rw [le_div_iff₀ (by positivity)]
  have h2 : (0 : K) < 2 * (1 + ε) := by positivity
  calc S * (δ * ε)
      = (2 * (1 + ε)) * (δ * (ε / (2 * (1 + ε))) * S) := by
        field_simp
    _ ≤ (2 * (1 + ε)) * E0 := by
        exact mul_le_mul_of_nonneg_left hbound (le_of_lt h2)
    _ = 2 * (1 + ε) * E0 := rfl

end QOU.FluidDynamics.LowModeUniformity
