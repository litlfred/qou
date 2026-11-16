/-!
# Framing Spin–Orbit Splitting, the Mayer–Jensen Magic Ladder, and the `A₅` Intruder Wall

Beans `qou-frso` (`Framing spin-orbit: the 2l+1 shape is derived, the scale is not`) and
`qou-mgq3` (`Magic-number derivation: measured attack surface, and the two walls`).

## Mathematical content

1. **Derived `2ℓ + 1` Landé spin–orbit shape (`qou-frso`):**
   In `SU(2)` twice-spin coordinates `twoJ = 2j`, the quadratic Casimir scaled by `4` is
   `fourCasimir twoJ = twoJ * (twoJ + 2) = 4 j(j + 1)`. For a spin-`1/2` fermion (`2s = 1`,
   `fourCasimir 1 = 3`) coupled to orbital angular momentum `ℓ` (`twoL = 2ℓ`,
   `fourCasimir (2ℓ) = 4ℓ(ℓ + 1)`), the aligned channel `twoJAligned ℓ = 2ℓ + 1` (`j = ℓ + 1/2`)
   and anti-aligned channel `twoJAntiAligned ℓ = 2ℓ - 1` (`j = ℓ - 1/2`) satisfy:
   - `fourCasimir (twoJAligned ℓ) - fourCasimir (2 * ℓ) - fourCasimir 1 = 4 * ℓ`,
   - `fourCasimir (twoJAntiAligned ℓ) - fourCasimir (2 * ℓ) - fourCasimir 1 = -4 * (ℓ + 1)`,
   - `fourCasimir (twoJAligned ℓ) - fourCasimir (twoJAntiAligned ℓ) = 4 * (2 * ℓ + 1)`,
   - and the `2 L · S` eigenvalue splitting is `ℓ - (-(ℓ + 1)) = 2 * ℓ + 1`
     (`twoLdotS_eigen_diff`, `fourCasimir_spin_orbit_diff`).
   The `2ℓ + 1` shape is parameter-free representation theory; the radial scale `V_ls` is an
   independent multiplicative parameter (`framingSpinOrbitShift_injective_in_scale`).

2. **Two magic ladders: pure 3D harmonic oscillator vs Mayer–Jensen spin–orbit intruder
   (`qou-frso`, `qou-mgq3`):**
   - Pure 3D harmonic-oscillator shell `n` has spin-doubled degeneracy
     `hoShellDeg n = (n + 1)(n + 2)` and cumulative closures
     `hoCumulative n = (n + 1)(n + 2)(n + 3) / 3`, taking values
     `[2, 8, 20, 40, 70, 112, 168]` at `n = 0..6`.
   - When the spin–orbit splitting pulls down the maximal-`j` subshell
     `j_max(n + 1) = (n + 1) + 1/2` from oscillator shell `n + 1` (with subshell capacity
     `2 j_max + 1 = 2(n + 2)`), the intruder-shifted cumulative closure is
     `soIntruderCumulative n = hoCumulative n + 2(n + 2)`, taking values
     `[20 + 8 = 28, 40 + 10 = 50, 70 + 12 = 82, 112 + 14 = 126]` at `n = 2..5`.
   - The empirical nuclear magic sequence `[2, 8, 20, 28, 50, 82, 126]` (`QOU.Common.magicList`)
     switches from the pure oscillator branch (`n = 0, 1, 2`) to the intruder branch
     (`n = 2, 3, 4, 5`).

3. **The `A₅` icosahedral branching wall (`qou-mgq3`):**
   The irreducible representations of `A₅` have dimensions `[1, 3, 3, 4, 5]`, with maximum
   dimension `5`. Tensoring with the spin-`1/2` doublet (`dim = 2`) caps any single
   `A₅ × SU(2)` irreducible multiplet at dimension `2 × 5 = 10`. However, the `1h_{11/2}`
   intruder subshell (`ℓ = 5, j = 11/2`) that closes magic number `82 = 70 + 12` has
   degeneracy `2j + 1 = 12 > 10` (`a5_spin_doubled_max_lt_h11_half`), and `1i_{13/2}`
   (`ℓ = 6, j = 13/2`, closing `126 = 112 + 14`) has degeneracy `14 > 10`. Under
   `SO(3) ↓ A₅`, the `ℓ = 5` (`dim 11`) orbital representation branches into the reducible
   sum `3 ⊕ 3' ⊕ 5` (`3 + 3 + 5 = 11`).

All declarations in this module are sorry-free and axiom-free (`0` `sorry`, `0` `axiom`).
-/

namespace QOU.MassTheory

/-! ## §1. Spin–Orbit Angular-Momentum Square Identity and Landé `2ℓ + 1` Splitting (`qou-frso`) -/

/-- Four times the `SU(2)` total angular-momentum square `4 j(j + 1) = (2j)(2j + 2)` in twice-spin
integer coordinates `twoJ = 2j`. -/
def fourSpinSquare (twoJ : Int) : Int := twoJ * (twoJ + 2)

/-- Twice the aligned total angular momentum `2 j₊(ℓ) = 2ℓ + 1` (`j₊ = ℓ + 1/2`). -/
def twoJAligned (ℓ : Int) : Int := 2 * ℓ + 1

/-- Twice the anti-aligned total angular momentum `2 j₋(ℓ) = 2ℓ - 1` (`j₋ = ℓ - 1/2`). -/
def twoJAntiAligned (ℓ : Int) : Int := 2 * ℓ - 1

/-- Eigenvalue `ℓ` of `2 L · S` on the aligned spin–orbit branch `j = ℓ + 1/2`. -/
def twoLdotSAligned (ℓ : Int) : Int := ℓ

/-- Eigenvalue `-(ℓ + 1)` of `2 L · S` on the anti-aligned spin–orbit branch `j = ℓ - 1/2`. -/
def twoLdotSAntiAligned (ℓ : Int) : Int := -(ℓ + 1)

/-- Helper expansion `(2ℓ + 1)(2ℓ + 3) = 4ℓ² + 8ℓ + 3`. -/
theorem fourSpinSquare_aligned_expand (ℓ : Int) :
    fourSpinSquare (twoJAligned ℓ) = 4 * (ℓ * ℓ) + 8 * ℓ + 3 := by
  unfold fourSpinSquare twoJAligned
  have h1 : (2 * ℓ + 1) * (2 * ℓ + 1 + 2) = (2 * ℓ + 1) * (2 * ℓ) + (2 * ℓ + 1) * 3 := by
    rw [← Int.mul_add]
    have : 2 * ℓ + 1 + 2 = 2 * ℓ + 3 := by omega
    rw [this]
  have h2 : (2 * ℓ + 1) * (2 * ℓ) = 4 * (ℓ * ℓ) + 2 * ℓ := by
    rw [Int.add_mul, Int.one_mul, Int.mul_assoc, ← Int.mul_assoc ℓ 2 ℓ, Int.mul_comm ℓ 2,
      Int.mul_assoc 2 ℓ ℓ, ← Int.mul_assoc 2 2 (ℓ * ℓ)]
    rfl
  omega

/-- Helper expansion `(2ℓ - 1)(2ℓ + 1) = 4ℓ² - 1`. -/
theorem fourSpinSquare_antiAligned_expand (ℓ : Int) :
    fourSpinSquare (twoJAntiAligned ℓ) = 4 * (ℓ * ℓ) - 1 := by
  unfold fourSpinSquare twoJAntiAligned
  have h1 : (2 * ℓ - 1) * (2 * ℓ - 1 + 2) = (2 * ℓ - 1) * (2 * ℓ) + (2 * ℓ - 1) * 1 := by
    rw [← Int.mul_add]
    have : 2 * ℓ - 1 + 2 = 2 * ℓ + 1 := by omega
    rw [this]
  have h2 : (2 * ℓ - 1) * (2 * ℓ) = 4 * (ℓ * ℓ) - 2 * ℓ := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_assoc, ← Int.mul_assoc ℓ 2 ℓ, Int.mul_comm ℓ 2,
      Int.mul_assoc 2 ℓ ℓ, ← Int.mul_assoc 2 2 (ℓ * ℓ)]
    rfl
  omega

/-- Helper expansion `4 C(ℓ) = (2ℓ)(2ℓ + 2) = 4ℓ² + 4ℓ`. -/
theorem fourSpinSquare_orbital_expand (ℓ : Int) :
    fourSpinSquare (2 * ℓ) = 4 * (ℓ * ℓ) + 4 * ℓ := by
  unfold fourSpinSquare
  rw [Int.mul_add, Int.mul_assoc, ← Int.mul_assoc ℓ 2 ℓ, Int.mul_comm ℓ 2,
    Int.mul_assoc 2 ℓ ℓ, ← Int.mul_assoc 2 2 (ℓ * ℓ)]
  omega

/-- On the aligned branch `j = ℓ + 1/2`, `4(C(j₊) - C(ℓ) - C(1/2)) = 4ℓ`. -/
theorem fourSpinSquare_aligned_sub_orbital_spin (ℓ : Int) :
    fourSpinSquare (twoJAligned ℓ) - fourSpinSquare (2 * ℓ) - fourSpinSquare 1 =
      4 * twoLdotSAligned ℓ := by
  rw [fourSpinSquare_aligned_expand, fourSpinSquare_orbital_expand]
  unfold fourSpinSquare twoLdotSAligned
  omega

/-- On the anti-aligned branch `j = ℓ - 1/2`, `4(C(j₋) - C(ℓ) - C(1/2)) = -4(ℓ + 1)`. -/
theorem fourSpinSquare_antiAligned_sub_orbital_spin (ℓ : Int) :
    fourSpinSquare (twoJAntiAligned ℓ) - fourSpinSquare (2 * ℓ) - fourSpinSquare 1 =
      4 * twoLdotSAntiAligned ℓ := by
  rw [fourSpinSquare_antiAligned_expand, fourSpinSquare_orbital_expand]
  unfold fourSpinSquare twoLdotSAntiAligned
  omega

/-- **Landé interval theorem (`qou-frso`):** the angular-momentum square difference between the
aligned channel `j₊ = ℓ + 1/2` and anti-aligned channel `j₋ = ℓ - 1/2` is identically `2ℓ + 1`
(scaled by `4` in twice-spin coordinates: `4 C(j₊) - 4 C(j₋) = 4 (2ℓ + 1)`). -/
theorem fourSpinSquare_spin_orbit_diff (ℓ : Int) :
    fourSpinSquare (twoJAligned ℓ) - fourSpinSquare (twoJAntiAligned ℓ) = 4 * (2 * ℓ + 1) := by
  rw [fourSpinSquare_aligned_expand, fourSpinSquare_antiAligned_expand]
  omega

/-- The splitting between the two spin–orbit eigenvalues of `2 L · S` is `2ℓ + 1` for all `ℓ`. -/
theorem twoLdotS_eigen_diff (ℓ : Int) :
    twoLdotSAligned ℓ - twoLdotSAntiAligned ℓ = 2 * ℓ + 1 := by
  unfold twoLdotSAligned twoLdotSAntiAligned
  have h1 : ℓ - -(ℓ + 1) = ℓ + (ℓ + 1) := by omega
  have h2 : ℓ + (ℓ + 1) = 2 * ℓ + 1 := by omega
  omega

/-- The `2ℓ + 1` shape is parameter-free while the radial coupling `V_ls` is an independent
scale: for any `ℓ : Int` (`2ℓ + 1 ≠ 0`), two scales `V₁, V₂` give the same splitting
`V · (2ℓ + 1)` if and only if `V₁ = V₂`. -/
theorem framingSpinOrbitShift_injective_in_scale (ℓ V₁ V₂ : Int) :
    V₁ * (twoLdotSAligned ℓ - twoLdotSAntiAligned ℓ) =
      V₂ * (twoLdotSAligned ℓ - twoLdotSAntiAligned ℓ) ↔ V₁ = V₂ := by
  rw [twoLdotS_eigen_diff]
  constructor
  · intro h
    have hsub : (V₁ - V₂) * (2 * ℓ + 1) = 0 := by
      rw [Int.sub_mul, h, Int.sub_self]
    cases Int.mul_eq_zero.mp hsub with
    | inl hV => omega
    | inr hL => omega
  · intro h
    rw [h]

/-! ## §2. Harmonic-Oscillator vs Spin–Orbit Intruder Magic Closures (`qou-frso`, `qou-mgq3`) -/

/-- Spin-doubled degeneracy `(n + 1)(n + 2)` of 3D isotropic harmonic-oscillator shell `n`. -/
def hoShellDeg (n : Nat) : Nat := (n + 1) * (n + 2)

/-- Cumulative nucleon count `N_HO(n) = (n + 1)(n + 2)(n + 3) / 3` through oscillator shell `n`. -/
def hoCumulative (n : Nat) : Nat := (n + 1) * (n + 2) * (n + 3) / 3

/-- The first seven 3D harmonic-oscillator cumulative closures are `[2, 8, 20, 40, 70, 112, 168]`. -/
theorem hoCumulative_first_seven :
    List.map hoCumulative [0, 1, 2, 3, 4, 5, 6] = [2, 8, 20, 40, 70, 112, 168] := by
  decide

/-- Capacity `2 j_max + 1 = 2(n + 2)` of the maximal-`j` intruder subshell
`j_max = (n + 1) + 1/2` descending from oscillator shell `n + 1` into shell `n`. -/
def intruderSubshellCap (n : Nat) : Nat := 2 * (n + 2)

/-- Intruder-shifted cumulative closure `N_SO(n) = N_HO(n) + 2(n + 2)`: oscillator shells
`0..n` plus the high-`j` intruder `j = n + 3/2` pulled down from shell `n + 1`. -/
def soIntruderCumulative (n : Nat) : Nat := hoCumulative n + intruderSubshellCap n

/-- For `n = 2, 3, 4, 5` (where the intruder subshells `1f_{7/2}, 1g_{9/2}, 1h_{11/2}, 1i_{13/2}`
carry capacities `8, 10, 12, 14`), the intruder-shifted closures are `[28, 50, 82, 126]`. -/
theorem soIntruderCumulative_magic_upper :
    List.map soIntruderCumulative [2, 3, 4, 5] = [28, 50, 82, 126] := by
  decide

/-- Explicit intruder decompositions of the four upper Mayer–Jensen magic numbers:
`28 = 20 + 8`, `50 = 40 + 10`, `82 = 70 + 12`, and `126 = 112 + 14`. -/
theorem mayer_jensen_intruder_splits :
    (hoCumulative 2, intruderSubshellCap 2, soIntruderCumulative 2) = (20, 8, 28) ∧
    (hoCumulative 3, intruderSubshellCap 3, soIntruderCumulative 3) = (40, 10, 50) ∧
    (hoCumulative 4, intruderSubshellCap 4, soIntruderCumulative 4) = (70, 12, 82) ∧
    (hoCumulative 5, intruderSubshellCap 5, soIntruderCumulative 5) = (112, 14, 126) := by
  decide

/-- The combined Mayer–Jensen magic ladder (pure oscillator closures at `n = 0, 1, 2`
followed by spin–orbit intruder closures at `n = 2, 3, 4, 5`) equals the empirical
seven-element nuclear magic sequence `[2, 8, 20, 28, 50, 82, 126]`. -/
theorem mayer_jensen_ladder_eq_magicList :
    List.map hoCumulative [0, 1, 2] ++ List.map soIntruderCumulative [2, 3, 4, 5] =
      [2, 8, 20, 28, 50, 82, 126] := by
  decide

/-! ## §3. The `A₅` Icosahedral Branching Obstruction at `82` and `126` (`qou-mgq3`) -/

/-- The five irreducible character degrees of the icosahedral group `A₅`. -/
def a5IrrepDims : List Nat := [1, 3, 3, 4, 5]

/-- Sum of squares of the `A₅` irreducible dimensions equals `|A₅| = 60`. -/
theorem a5IrrepDims_burnside :
    (a5IrrepDims.map (fun d => d * d)).sum = 60 := by
  decide

/-- Every spin-doubled `A₅ × SU(2)` irreducible representation has dimension `2 d ≤ 10`,
which is strictly smaller than the `1h_{11/2}` intruder subshell capacity
`intruderSubshellCap 4 = 12` (closing magic number `82`) and the `1i_{13/2}` capacity
`intruderSubshellCap 5 = 14` (closing magic number `126`). -/
theorem a5_spin_doubled_max_lt_h11_half :
    (∀ d ∈ a5IrrepDims, 2 * d ≤ 10) ∧
    10 < intruderSubshellCap 4 ∧
    10 < intruderSubshellCap 5 := by
  decide

/-- Under `SO(3) ↓ A₅`, the `ℓ = 5` orbital representation (`dim = 2·5 + 1 = 11`) cannot be
irreducible; its dimension decomposes as `3 + 3 + 5 = 11` (`T₁ ⊕ T₂ ⊕ H`), and with spin
doubling (`11 × 2 = 22 = 12 + 10`) splits across `1h_{11/2}` (`12`) and `1h_{9/2}` (`10`). -/
theorem a5_l5_branching_dimension_split :
    3 ∈ a5IrrepDims ∧ 5 ∈ a5IrrepDims ∧
    3 + 3 + 5 = 2 * 5 + 1 ∧
    intruderSubshellCap 4 + (2 * 5) = 2 * (2 * 5 + 1) := by
  decide

end QOU.MassTheory
