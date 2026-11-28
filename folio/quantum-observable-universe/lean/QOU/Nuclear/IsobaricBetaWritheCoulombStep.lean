/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Division-Free Isobaric `β⁻` Step Identity: Writhe `T(T+1)`, Weight Multiplicity, and Coulomb Arms

Formalizes the exact isobaric `β⁻` binding and `Q`-value step across `(Z, N + 1) → (Z + 1, N)` at
conserved mass number `A = Z + N + 1` over an arbitrary commutative ring `R` (`[CommRing R]`),
combining gaps **G2** (`qou-tcl2`, `QOU.Nuclear.IsospinCasimirTwist`,
`QOU.Nuclear.IsospinTwistWrithe`, `QOU.Nuclear.IsospinWeightMultiplicity`) and **G3**
(`qou-tcl3`, `QOU.Nuclear.CoulombIsospinChannel`, `QOU.Nuclear.CoulombBlockSize`, and the two
labelled cell-radius arms `c = 1` and `c³ = 3/2` of `docs/audits/2026-11-28-coulomb-cell-radius.md`).

## Main Definitions and Theorems

1. **Isobaric `β⁻` kinematics and flat `T_z`-even baseline (`§1`):**
   - `qBetaMinus_eq_free_add_binding_step`: `Q_β⁻(Z, N+1) = (m_n - m_p - m_e) + (B(Z+1, N) - B(Z, N+1))`.
   - `ruledTzEvenChainBinding_interior_eq` and `qBetaMinus_ruled_interior_flat`: for every interior
     mixed transition (`Z ≥ 1`, `N ≥ 1`, i.e. parent neutron count `N + 1 ≥ 2`), the `T_z`-even
     ruled 1D log-law chain binding (`PR #9675`) is invariant across `(Z, N + 1) → (Z + 1, N)`,
     forcing `Q_β⁻` to equal the flat free-neutron value `m_n - m_p - m_e` identically.
2. **Exact lowest-block `T(T+1)` step vs `T_z²` and down-quark weight multiplicity (`§2`):**
   - `casimirFour_wigner_cusp_split`: `4 T(T+1) = (N - Z)² + 2 |N - Z|` (`T = |N - Z| / 2`).
   - `tzSqFour_beta_step`: the quadratic projection `4 T_z² = d²` steps by `4 (d - 1)` for all
     `d ∈ ℤ` (`-Δ[T_z²] = N_parent - Z - 1`).
   - `casimirFour_beta_step_eq_four_mul_ttStepInt`: on the lowest isospin block `T = |d| / 2`,
     `casimirFour |d| - casimirFour |d - 2| = 4 * ttStepInt d` is divisible by `4` for **every**
     `d ∈ ℤ`, with `ttStepInt d = d` for `d ≥ 2` (neutron-rich, where the Wigner linear piece adds
     `+1` to `d - 1`), `0` at the mirror doublet `d = 1` (`N_parent = Z + 1`, where both nuclei sit
     in `T = 1/2`), and `d - 2` for `d ≤ 0`.
   - `downQuarkWeight_beta_step`: for `IsospinWeightMultiplicity`'s `T_z`-sector state count
     `C(3A, n_d)` (`n_d = Z + 2 N_parent`), one `β⁻` step shifts `n_d ↦ n_d - 1` and satisfies the
     exact polynomial identity `C(3A, n_d - 1) * (2Z + N + 2) = C(3A, n_d) * (Z + 2N + 2)` over any
     `[CommRing R]`, whose factor difference `(Z + 2N + 2) - (2Z + N + 2) = N - Z = N_parent - Z - 1`
     recovers the `N_parent - Z - 1` linear numerator.
3. **Coulomb proton-pair step and the two `#9866` cell-radius arms (`§3`):**
   - `coulombBinding_isobaric_step`: `coulombBindingTerm eps (Z + 1) - coulombBindingTerm eps Z = -Z * eps`
     over `[CommRing R]` (division-free via `C(Z + 1, 2) = C(Z, 2) + Z`).
   - `coulomb_size_law_ring` and `coulomb_step_armA_armB_cubic`: under homogeneity `eps * R = κ_EM`
     and cell volume `R³ = c³ * A * v_π`, Arm A (`c = 1`) and Arm B (`2 * c³ = 3`, strand-volume
     ratio `3/2`) satisfy `3 * epsB³ = 2 * epsA³` and `3 * (Δ_EM,B)³ = 2 * (Δ_EM,A)³`.
4. **Master division-free combined step identity and `#9747` writhe specialisations (`§4`):**
   - `clearedCompositeBinding_isobaric_step` and `strandPairDenom_mul_qBetaMinus`: clears the
     `3A(3A - 1)` Murphy-product strand-pair denominator over `[CommRing R]`, with specialisations
     to `writhe = 0` (`γγ`-selected words, `IsospinTwistWrithe` `bb1d29c6df6`), neutron-rich
     `N_parent - Z ≥ 2`, mirror doublets `N_parent = Z + 1`, and full twist `writhe = 3A(3A - 1)`.

## Base-Ring Generality (§7c)

All ring-valued definitions and theorems hold over an arbitrary `[CommRing R]` with zero division,
zero `[Field]` hypotheses, and zero analytic or transcendental imports. Combinatorial Casimir steps
are proved over `ℤ` and `ℕ`.

Refs: [ram1997]; [murphy1992]; [wigner1957] (IMME).
-/

set_option autoImplicit false

namespace QOU.Nuclear.IsobaricBetaWritheCoulombStep

/-! ## §1. Isobaric `β⁻` Kinematics and Flat `T_z`-Even Baseline -/

section Kinematics

variable {R : Type*} [CommRing R]

/-- Constituent nuclear mass `Z m_p + N m_n - B` in a commutative ring `R`. -/
def nuclearMass (mp mn B : R) (Z N : ℕ) : R :=
  (Z : R) * mp + (N : R) * mn - B

/-- Isobaric `β⁻` decay `Q`-value for `(Z, N + 1) → (Z + 1, N)` at fixed `A = Z + N + 1`:
`Q_β⁻ = M(Z, N + 1) - M(Z + 1, N) - m_e`. -/
def qBetaMinus (mp mn me Bparent Bdaughter : R) (Z N : ℕ) : R :=
  nuclearMass mp mn Bparent Z (N + 1) - nuclearMass mp mn Bdaughter (Z + 1) N - me

/-- Mass number `A = Z + N + 1` is conserved across `(Z, N + 1) → (Z + 1, N)`. -/
theorem isobaric_mass_number_eq (Z N : ℕ) : Z + (N + 1) = (Z + 1) + N := by
  omega

/-- **Exact `Q_β⁻` decomposition.** Every composite `β⁻` `Q`-value equals the single-nucleon
baseline `m_n - m_p - m_e` plus the isobaric binding step `ΔB_β⁻ = B(Z + 1, N) - B(Z, N + 1)`. -/
theorem qBetaMinus_eq_free_add_binding_step (mp mn me Bparent Bdaughter : R) (Z N : ℕ) :
    qBetaMinus mp mn me Bparent Bdaughter Z N = (mn - mp - me) + (Bdaughter - Bparent) := by
  unfold qBetaMinus nuclearMass
  push_cast
  ring

/-- The `T_z`-even free-baseline ruled 1D chain binding (`mass_table_comprehensive.binding_ruled_tz_even`,
`PR #9675`): `(A - 2) * lLike + lPn` when both species are present (`Z ≥ 1` and `N ≥ 1`), and
`(A - 1) * lLike` on a pure-species chain (`Z = 0` or `N = 0`). -/
def ruledTzEvenChainBinding (lLike lPn : R) (Z N : ℕ) : R :=
  if 1 ≤ Z ∧ 1 ≤ N then (((Z + N : ℕ) : R) - 2) * lLike + lPn
  else (((Z + N : ℕ) : R) - 1) * lLike

/-- **Isobaric invariance of the `T_z`-even ruled chain binding.** For every interior composite
transition `(Z, N + 1) → (Z + 1, N)` with `1 ≤ Z` and `1 ≤ N` (both parent and daughter mixed),
the `T_z`-even 1D chain binding takes the exact same value on parent and daughter. -/
theorem ruledTzEvenChainBinding_interior_eq (lLike lPn : R) (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    ruledTzEvenChainBinding lLike lPn (Z + 1) N = ruledTzEvenChainBinding lLike lPn Z (N + 1) := by
  have hDau : 1 ≤ Z + 1 ∧ 1 ≤ N := ⟨by omega, hN⟩
  have hPar : 1 ≤ Z ∧ 1 ≤ N + 1 := ⟨hZ, by omega⟩
  unfold ruledTzEvenChainBinding
  rw [if_pos hDau, if_pos hPar, isobaric_mass_number_eq Z N]

/-- **Why `B_ruled_MeV` produces a flat composite `Q_β⁻` (`ACCURACY.md` Table 3.4b).** On every
interior composite `β⁻` transition (`1 ≤ Z`, `1 ≤ N`), `Q_β⁻` under `ruledTzEvenChainBinding`
collapses identically to the nucleus-independent constant `m_n - m_p - m_e`. -/
theorem qBetaMinus_ruled_interior_flat (mp mn me lLike lPn : R) (Z N : ℕ)
    (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    qBetaMinus mp mn me
      (ruledTzEvenChainBinding lLike lPn Z (N + 1))
      (ruledTzEvenChainBinding lLike lPn (Z + 1) N) Z N = mn - mp - me := by
  rw [qBetaMinus_eq_free_add_binding_step, ruledTzEvenChainBinding_interior_eq lLike lPn Z N hZ hN]
  ring

end Kinematics

/-! ## §2. Lowest-Block `T(T+1)` Step vs `T_z²` and Down-Quark Weight Multiplicity (`qou-tcl2`) -/

section IsospinStep

/-- Four times the `SU(2)` Casimir `4 T(T + 1) = t (t + 2)` in terms of `t = 2T ∈ ℤ`. -/
def casimirFour (t : ℤ) : ℤ := t * (t + 2)

/-- Four times the squared isospin projection `4 T_z² = d²` in terms of `d = N - Z = -2 T_z ∈ ℤ`. -/
def tzSqFour (d : ℤ) : ℤ := d ^ 2

/-- **Wigner cusp decomposition.** On the lowest block `t = 2T = |d|`, `4 T(T + 1) = d² + 2 |d|`. -/
theorem casimirFour_wigner_cusp_split (d : ℤ) :
    casimirFour |d| = tzSqFour d + 2 * |d| := by
  unfold casimirFour tzSqFour
  rw [mul_add, abs_mul_abs_self, sq]
  ring

/-- **Exact quadratic `T_z²` step.** Across `d ↦ d - 2` (`(Z, N_p) → (Z + 1, N_p - 1)`),
`4 T_z²` drops by `4 (d - 1)`, i.e. `-Δ[T_z²] = d - 1 = N_p - Z - 1 = -2 T_z - 1` for all `d ∈ ℤ`. -/
theorem tzSqFour_beta_step (d : ℤ) :
    tzSqFour d - tzSqFour (d - 2) = 4 * (d - 1) := by
  unfold tzSqFour
  ring

/-- The integer lowest-block Casimir drop `-Δ[T(T + 1)] = T_p(T_p + 1) - T_d(T_d + 1)` as a
function of parent neutron excess `d = N_parent - Z`:
- `d` for `d ≥ 2` (neutron-rich `β⁻` emitters: `(d - 1) + 1 = d` from the Wigner `|T_z|` cusp),
- `0` for `d = 1` (mirror `β⁻` doublet `(Z, Z + 1) → (Z + 1, Z)` inside `T = 1/2`),
- `d - 2` for `d ≤ 0` (proton-rich side). -/
def ttStepInt (d : ℤ) : ℤ :=
  if 2 ≤ d then d else if d = 1 then 0 else d - 2

/-- **Integrality and exact formula for `-Δ[T(T + 1)]`.** For **every** integer `d = N_parent - Z`,
`casimirFour |d| - casimirFour |d - 2|` is an exact multiple of `4`, equal to `4 * ttStepInt d`. -/
theorem casimirFour_beta_step_eq_four_mul_ttStepInt (d : ℤ) :
    casimirFour |d| - casimirFour |d - 2| = 4 * ttStepInt d := by
  unfold ttStepInt
  split_ifs with h2 h1
  · have hd0 : 0 ≤ d := by linarith
    have hd2 : 0 ≤ d - 2 := by linarith
    rw [abs_of_nonneg hd0, abs_of_nonneg hd2]
    unfold casimirFour
    ring
  · subst h1
    norm_num [casimirFour]
  · have hd0 : d ≤ 0 := by omega
    have hd2 : d - 2 ≤ 0 := by omega
    rw [abs_of_nonpos hd0, abs_of_nonpos hd2]
    unfold casimirFour
    ring

/-- On every neutron-rich `β⁻` emitter with `N_parent - Z ≥ 2`, `-Δ[T(T + 1)] = d = (d - 1) + 1`:
the Wigner linear cusp adds `+1` to the quadratic step `d - 1 = N_parent - Z - 1`. -/
theorem ttStepInt_of_two_le {d : ℤ} (hd : 2 ≤ d) :
    ttStepInt d = d ∧ ttStepInt d = (d - 1) + 1 := by
  unfold ttStepInt
  rw [if_pos hd]
  exact ⟨rfl, by ring⟩

/-- At a mirror `β⁻` doublet `d = 1` (`N_parent = Z + 1`, e.g. `³H → ³He`), both `ttStepInt 1` and
the quadratic step `d - 1` vanish because parent and daughter share `T = 1/2`. -/
theorem ttStepInt_one : ttStepInt 1 = 0 := by
  unfold ttStepInt
  norm_num

/-- On the proton-rich side `d ≤ 0`, `ttStepInt d = d - 2 = (d - 1) - 1`. -/
theorem ttStepInt_of_nonpos {d : ℤ} (hd : d ≤ 0) :
    ttStepInt d = d - 2 := by
  unfold ttStepInt
  rw [if_neg (by omega), if_neg (by omega)]

/-- **Down-quark weight-multiplicity step (`IsospinWeightMultiplicity` `d7c7d1081ba` / `9e6eb1efd6e`).**
On `3A = 3(Z + N + 1)` quark strands, `(Z, N + 1)` has `n_d = Z + 2(N + 1)` down quarks and
`(Z + 1, N)` has `n_d - 1 = Z + 2N + 1` down quarks. Over any `[CommRing R]`, the weight counts
satisfy the exact division-free step relation:
`C(3A, Z + 2N + 1) * (2Z + N + 2) = C(3A, Z + 2(N + 1)) * (Z + 2(N + 1))`. -/
theorem downQuarkWeight_beta_step {R : Type*} [CommRing R] (Z N : ℕ) :
    (((3 * (Z + N + 1)).choose (Z + 2 * N + 1) : ℕ) : R) * ((2 * Z + N + 2 : ℕ) : R)
      = (((3 * (Z + N + 1)).choose (Z + 2 * (N + 1)) : ℕ) : R)
          * ((Z + 2 * (N + 1) : ℕ) : R) := by
  have h := Nat.choose_succ_right_eq (3 * (Z + N + 1)) (Z + 2 * N + 1)
  have hk : Z + 2 * N + 1 + 1 = Z + 2 * (N + 1) := by omega
  have hsub : 3 * (Z + N + 1) - (Z + 2 * N + 1) = 2 * Z + N + 2 := by omega
  rw [hk, hsub] at h
  have hR := congrArg (Nat.cast (R := R)) h.symm
  rw [Nat.cast_mul, Nat.cast_mul] at hR
  exact hR

/-- The numerator-minus-denominator gap of the down-quark weight-multiplicity ratio
`(Z + 2(N + 1)) / (2Z + N + 2)` is `N - Z = N_parent - Z - 1`, recovering `-Δ[T_z²]`. -/
theorem downQuarkWeight_factor_gap (Z N : ℕ) :
    ((Z + 2 * (N + 1) : ℕ) : ℤ) - ((2 * Z + N + 2 : ℕ) : ℤ)
      = ((N + 1 : ℕ) : ℤ) - (Z : ℤ) - 1 := by
  push_cast
  ring

/-- Markov (quantum-trace) weight `C(nStrands, k) * q^(nStrands - k) * qi^k` of the `T_z` sector
with `k` down-quark strands (`QOU.Nuclear.IsospinWeightMultiplicity.markovSector`, `9e6eb1efd6e`),
stated over an arbitrary `[CommRing R]`. -/
def markovSectorWeight {R : Type*} [CommRing R] (q qi : R) (nStrands k : ℕ) : R :=
  ((nStrands.choose k : ℕ) : R) * q ^ (nStrands - k) * qi ^ k

/-- **Markov quantum-trace sector `β⁻` step (`9e6eb1efd6e` extension).** Whenever `q * qi = 1`,
stepping `(Z, N + 1) → (Z + 1, N)` on `3(Z + N + 1)` quark strands multiplies the classical
binomial step `downQuarkWeight_beta_step` by the `T_z`-odd factor `q²` (`T_z ↦ T_z + 1`), while
mirror symmetrization (`markov_sector_mirror`) removes `q` completely. -/
theorem markovSectorWeight_beta_step {R : Type*} [CommRing R] (q qi : R) (hq : q * qi = 1)
    (Z N : ℕ) :
    markovSectorWeight q qi (3 * (Z + N + 1)) (Z + 2 * N + 1) * ((2 * Z + N + 2 : ℕ) : R)
      = markovSectorWeight q qi (3 * (Z + N + 1)) (Z + 2 * (N + 1))
          * ((Z + 2 * (N + 1) : ℕ) : R) * q ^ 2 := by
  unfold markovSectorWeight
  have hbin := downQuarkWeight_beta_step (R := R) Z N
  have hqd : q ^ (3 * (Z + N + 1) - (Z + 2 * N + 1)) = q ^ (2 * Z + N + 1) * q := by
    rw [show 3 * (Z + N + 1) - (Z + 2 * N + 1) = (2 * Z + N + 1) + 1 by omega, pow_succ]
  have hqp : q ^ (3 * (Z + N + 1) - (Z + 2 * (N + 1))) = q ^ (2 * Z + N + 1) := by
    congr 1
    omega
  have hqi : qi ^ (Z + 2 * (N + 1)) = qi ^ (Z + 2 * N + 1) * qi := by
    rw [show Z + 2 * (N + 1) = (Z + 2 * N + 1) + 1 by omega, pow_succ]
  rw [hqd, hqp, hqi]
  calc (((3 * (Z + N + 1)).choose (Z + 2 * N + 1) : ℕ) : R)
          * (q ^ (2 * Z + N + 1) * q) * qi ^ (Z + 2 * N + 1) * ((2 * Z + N + 2 : ℕ) : R)
      = ((((3 * (Z + N + 1)).choose (Z + 2 * N + 1) : ℕ) : R) * ((2 * Z + N + 2 : ℕ) : R))
          * q ^ (2 * Z + N + 1) * qi ^ (Z + 2 * N + 1) * q * 1 := by ring
    _ = ((((3 * (Z + N + 1)).choose (Z + 2 * (N + 1)) : ℕ) : R) * ((Z + 2 * (N + 1) : ℕ) : R))
          * q ^ (2 * Z + N + 1) * qi ^ (Z + 2 * N + 1) * q * (q * qi) := by rw [hbin, ← hq]
    _ = (((3 * (Z + N + 1)).choose (Z + 2 * (N + 1)) : ℕ) : R)
          * q ^ (2 * Z + N + 1) * (qi ^ (Z + 2 * N + 1) * qi)
          * ((Z + 2 * (N + 1) : ℕ) : R) * q ^ 2 := by ring

end IsospinStep

/-! ## §3. Coulomb Proton-Pair Step and the Two `#9866` Cell-Radius Arms (`qou-tcl3`) -/

section CoulombArms

variable {R : Type*} [CommRing R]

/-- Unordered proton-pair count `C(Z, 2) = Z(Z - 1)/2` as a natural number (division-free). -/
def protonPairs (Z : ℕ) : ℕ := Z.choose 2

/-- Adding one proton adds exactly `Z` new proton pairs: `C(Z + 1, 2) = C(Z, 2) + Z`. -/
theorem protonPairs_succ (Z : ℕ) : protonPairs (Z + 1) = protonPairs Z + Z := by
  unfold protonPairs
  simpa [Nat.choose_one_right, add_comm] using Nat.choose_succ_succ Z 1

/-- Electrostatic binding contribution `-C(Z, 2) * eps` (repulsive, reducing net binding `B`). -/
def coulombBindingTerm (eps : R) (Z : ℕ) : R :=
  -((protonPairs Z : ℕ) : R) * eps

/-- **Exact isobaric Coulomb step.** At fixed mass number `A` (hence fixed pair weight `eps`),
`(Z, N + 1) → (Z + 1, N)` shifts the Coulomb binding contribution by `-Z * eps`. -/
theorem coulombBinding_isobaric_step (eps : R) (Z : ℕ) :
    coulombBindingTerm eps (Z + 1) - coulombBindingTerm eps Z = -(Z : R) * eps := by
  unfold coulombBindingTerm
  rw [protonPairs_succ]
  push_cast
  ring

/-- **Division-free Coulomb cell-size law (`CoulombBlockSize` + `#9866`).** Homogeneity
`eps * rNuc = kappaEm` and additive cell volume `rNuc³ = cCube * A * vPi` imply
`eps³ * (cCube * A * vPi) = kappaEm³` in any commutative ring `R`. -/
theorem coulomb_size_law_ring (eps rNuc kappaEm cCube A vPi : R)
    (hH1 : eps * rNuc = kappaEm) (hH2 : rNuc ^ 3 = cCube * A * vPi) :
    eps ^ 3 * (cCube * A * vPi) = kappaEm ^ 3 := by
  calc eps ^ 3 * (cCube * A * vPi) = eps ^ 3 * rNuc ^ 3 := by rw [hH2]
    _ = (eps * rNuc) ^ 3 := by ring
    _ = kappaEm ^ 3 := by rw [hH1]

/-- **Cubic relation between `#9866` Arm A (`c = 1`) and Arm B (`c³ = 3/2`, `2 c³ = 3`).**
When `epsA` satisfies Arm A (`cCube = 1`) and `epsB` satisfies Arm B (`2 * rNucB³ = 3 * A * vPi`)
with the same `kappaEm`, `A`, `vPi`, their cubes satisfy `(3 * epsB³) * (A * vPi) = (2 * epsA³) * (A * vPi)`. -/
theorem coulomb_armA_armB_pair_weight_cubic (epsA rNucA epsB rNucB kappaEm A vPi : R)
    (hH1A : epsA * rNucA = kappaEm) (hVA : rNucA ^ 3 = A * vPi)
    (hH1B : epsB * rNucB = kappaEm) (hVB : 2 * rNucB ^ 3 = 3 * (A * vPi)) :
    (3 * epsB ^ 3) * (A * vPi) = (2 * epsA ^ 3) * (A * vPi) := by
  have hA : epsA ^ 3 * (A * vPi) = kappaEm ^ 3 := by
    simpa [one_mul] using coulomb_size_law_ring epsA rNucA kappaEm 1 A vPi hH1A (by simpa using hVA)
  calc (3 * epsB ^ 3) * (A * vPi) = epsB ^ 3 * (3 * (A * vPi)) := by ring
    _ = epsB ^ 3 * (2 * rNucB ^ 3) := by rw [← hVB]
    _ = 2 * (epsB * rNucB) ^ 3 := by ring
    _ = 2 * kappaEm ^ 3 := by rw [hH1B]
    _ = 2 * (epsA ^ 3 * (A * vPi)) := by rw [← hA]
    _ = (2 * epsA ^ 3) * (A * vPi) := by ring

/-- **Cubic scaling transferred to the isobaric Coulomb `β⁻` step.** Whenever the Arm A (`c = 1`)
and Arm B (`c³ = 3/2`) pair weights satisfy `3 * epsB³ = 2 * epsA³`, their isobaric Coulomb steps
`ΔB_EM(Z) = B_EM(Z + 1) - B_EM(Z)` satisfy `3 * (ΔB_EM,B)³ = 2 * (ΔB_EM,A)³` for every `Z`. -/
theorem coulomb_step_armA_armB_cubic (epsA epsB : R) (Z : ℕ)
    (hArms : 3 * epsB ^ 3 = 2 * epsA ^ 3) :
    3 * (coulombBindingTerm epsB (Z + 1) - coulombBindingTerm epsB Z) ^ 3
      = 2 * (coulombBindingTerm epsA (Z + 1) - coulombBindingTerm epsA Z) ^ 3 := by
  rw [coulombBinding_isobaric_step, coulombBinding_isobaric_step]
  calc 3 * (-(Z : R) * epsB) ^ 3 = -((Z : R) ^ 3 * (3 * epsB ^ 3)) := by ring
    _ = -((Z : R) ^ 3 * (2 * epsA ^ 3)) := by rw [hArms]
    _ = 2 * (-(Z : R) * epsA) ^ 3 := by ring

end CoulombArms

/-! ## §4. Master Division-Free Isobaric `β⁻` Step Identity (`#9747` + `#9866`) -/

section MasterStep

variable {R : Type*} [CommRing R]

/-- Murphy-product letter count `N_strands * (N_strands - 1) = 3A(3A - 1)` on `3A` quark strands
(`QOU.Nuclear.IsospinTwistWrithe`). -/
def strandPairDenom (A : ℕ) : ℕ := (3 * A) * (3 * A - 1)

/-- `strandPairDenom` is invariant across `(Z, N + 1) → (Z + 1, N)`. -/
theorem strandPairDenom_isobaric_eq (Z N : ℕ) :
    strandPairDenom ((Z + 1) + N) = strandPairDenom (Z + (N + 1)) := by
  congr 1
  omega

/-- Total composite binding cleared by `4 * strandPairDenom (Z + N)` in `[CommRing R]`:
combines `ruledTzEvenChainBinding` (`#9675`), `coulombBindingTerm` (`#9691`/`#9866`), and the
`#9747` writhe-scaled lowest-block `T(T + 1)` term `-kappa * writhe / (3A(3A - 1)) * T(T + 1)`. -/
def clearedCompositeBinding (lLike lPn kappa eps : R) (writhe : ℤ) (Z N : ℕ) : R :=
  4 * ((strandPairDenom (Z + N) : ℕ) : R)
      * (ruledTzEvenChainBinding lLike lPn Z N + coulombBindingTerm eps Z)
    - kappa * (writhe : R) * (casimirFour |(N : ℤ) - (Z : ℤ)| : R)

/-- **Master division-free isobaric `ΔB_β⁻` step identity.** For every interior composite `β⁻`
transition `(Z, N + 1) → (Z + 1, N)` (`1 ≤ Z`, `1 ≤ N`, `A = Z + N + 1`), the `T_z`-even chain
baseline cancels identically and the cleared binding step factors through `4`:
`4 * (kappa * writhe * ttStepInt (N + 1 - Z) - strandPairDenom A * Z * eps)`. -/
theorem clearedCompositeBinding_isobaric_step (lLike lPn kappa eps : R) (writhe : ℤ)
    (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    clearedCompositeBinding lLike lPn kappa eps writhe (Z + 1) N
        - clearedCompositeBinding lLike lPn kappa eps writhe Z (N + 1)
      = 4 * (kappa * (writhe : R) * (ttStepInt (((N + 1 : ℕ) : ℤ) - (Z : ℤ)) : R)
          - ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (Z : R) * eps) := by
  unfold clearedCompositeBinding
  rw [strandPairDenom_isobaric_eq Z N, ruledTzEvenChainBinding_interior_eq lLike lPn Z N hZ hN]
  have hcoul : coulombBindingTerm eps (Z + 1) = coulombBindingTerm eps Z - (Z : R) * eps := by
    have hstep := coulombBinding_isobaric_step eps Z
    calc coulombBindingTerm eps (Z + 1)
        = (coulombBindingTerm eps (Z + 1) - coulombBindingTerm eps Z) + coulombBindingTerm eps Z := by ring
      _ = -(Z : R) * eps + coulombBindingTerm eps Z := by rw [hstep]
      _ = coulombBindingTerm eps Z - (Z : R) * eps := by ring
  set d : ℤ := ((N + 1 : ℕ) : ℤ) - (Z : ℤ)
  have hd_dau : (N : ℤ) - ((Z + 1 : ℕ) : ℤ) = d - 2 := by
    simp only [d]
    push_cast
    ring
  have hcasZ : casimirFour |d| = casimirFour |d - 2| + 4 * ttStepInt d := by
    linarith [casimirFour_beta_step_eq_four_mul_ttStepInt d]
  have hcas : (casimirFour |d| : R) = (casimirFour |d - 2| : R) + 4 * (ttStepInt d : R) := by
    have hR := congrArg (Int.cast (R := R)) hcasZ
    rw [Int.cast_add, Int.cast_mul, Int.cast_ofNat] at hR
    exact hR
  rw [hcoul, hd_dau, hcas]
  ring

/-- **Cleared `Q_β⁻` identity.** When `Bparent` and `Bdaughter` satisfy the factor-`4`-cancelled
step equation `M_A * (Bdaughter - Bparent) = kappa * writhe * ttStepInt d - M_A * Z * eps`
(`M_A = 3A(3A - 1)`), `M_A * Q_β⁻` decomposes into free-neutron baseline minus Coulomb plus the
writhe-scaled `T(T + 1)` gain. -/
theorem strandPairDenom_mul_qBetaMinus (mp mn me Bparent Bdaughter kappa eps : R) (writhe : ℤ)
    (Z N : ℕ)
    (hStep : ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (Bdaughter - Bparent)
      = kappa * (writhe : R) * (ttStepInt (((N + 1 : ℕ) : ℤ) - (Z : ℤ)) : R)
          - ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (Z : R) * eps) :
    ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * qBetaMinus mp mn me Bparent Bdaughter Z N
      = ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (mn - mp - me - (Z : R) * eps)
          + kappa * (writhe : R) * (ttStepInt (((N + 1 : ℕ) : ℤ) - (Z : ℤ)) : R) := by
  rw [qBetaMinus_eq_free_add_binding_step, mul_add, hStep]
  ring

/-- **`γγ`-selected word specialisation (`IsospinTwistWrithe` `bb1d29c6df6`, `writhe = 0`).**
On any writhe-zero word (such as products of `σ_i σ_{i+1}⁻¹`), the braid-channel `T(T + 1)` step
vanishes identically and the composite `β⁻` step reduces purely to the Coulomb shift `-Z * eps`. -/
theorem clearedCompositeBinding_step_gammaGamma (lLike lPn kappa eps : R)
    (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    clearedCompositeBinding lLike lPn kappa eps 0 (Z + 1) N
        - clearedCompositeBinding lLike lPn kappa eps 0 Z (N + 1)
      = -4 * ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (Z : R) * eps := by
  rw [clearedCompositeBinding_isobaric_step lLike lPn kappa eps 0 Z N hZ hN]
  push_cast
  ring

/-- **Neutron-rich specialisation (`N_parent ≥ Z + 2`, i.e. `Z + 1 ≤ N`).** Every non-mirror
neutron-rich `β⁻` emitter replaces `ttStepInt` by the exact neutron excess `N + 1 - Z`. -/
theorem clearedCompositeBinding_step_neutronRich (lLike lPn kappa eps : R) (writhe : ℤ)
    (Z N : ℕ) (hZ : 1 ≤ Z) (hRich : Z + 1 ≤ N) :
    clearedCompositeBinding lLike lPn kappa eps writhe (Z + 1) N
        - clearedCompositeBinding lLike lPn kappa eps writhe Z (N + 1)
      = 4 * (kappa * (writhe : R) * (((N + 1 : ℕ) : R) - (Z : R))
          - ((strandPairDenom (Z + (N + 1)) : ℕ) : R) * (Z : R) * eps) := by
  have hN : 1 ≤ N := by omega
  rw [clearedCompositeBinding_isobaric_step lLike lPn kappa eps writhe Z N hZ hN]
  have hd : (2 : ℤ) ≤ ((N + 1 : ℕ) : ℤ) - (Z : ℤ) := by omega
  rw [(ttStepInt_of_two_le hd).1]
  push_cast
  ring

/-- **Mirror `β⁻` doublet specialisation (`N = Z`, i.e. `(Z, Z + 1) → (Z + 1, Z)`).** Regardless
of the braid writhe `writhe`, a mirror `β⁻` transition stays inside `T = 1/2` (`ttStepInt 1 = 0`),
so its binding step is purely the Coulomb displacement `-Z * eps`. -/
theorem clearedCompositeBinding_step_mirror (lLike lPn kappa eps : R) (writhe : ℤ)
    (Z : ℕ) (hZ : 1 ≤ Z) :
    clearedCompositeBinding lLike lPn kappa eps writhe (Z + 1) Z
        - clearedCompositeBinding lLike lPn kappa eps writhe Z (Z + 1)
      = -4 * ((strandPairDenom (Z + (Z + 1)) : ℕ) : R) * (Z : R) * eps := by
  rw [clearedCompositeBinding_isobaric_step lLike lPn kappa eps writhe Z Z hZ hZ]
  have h1 : ((Z + 1 : ℕ) : ℤ) - (Z : ℤ) = 1 := by omega
  rw [h1, ttStepInt_one]
  push_cast
  ring

/-- **Full-twist specialisation (`writhe = 3A(3A - 1)`, `#9706`).** For the Murphy full twist,
`strandPairDenom` factors out of both terms, leaving the un-attenuated `kappa * ttStepInt` step. -/
theorem clearedCompositeBinding_step_fullTwist (lLike lPn kappa eps : R)
    (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    clearedCompositeBinding lLike lPn kappa eps (strandPairDenom (Z + (N + 1)) : ℤ) (Z + 1) N
        - clearedCompositeBinding lLike lPn kappa eps (strandPairDenom (Z + (N + 1)) : ℤ) Z (N + 1)
      = 4 * ((strandPairDenom (Z + (N + 1)) : ℕ) : R)
          * (kappa * (ttStepInt (((N + 1 : ℕ) : ℤ) - (Z : ℤ)) : R) - (Z : R) * eps) := by
  rw [clearedCompositeBinding_isobaric_step lLike lPn kappa eps _ Z N hZ hN]
  push_cast
  ring

end MasterStep

end QOU.Nuclear.IsobaricBetaWritheCoulombStep
