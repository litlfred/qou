/-
  DeuteronNaiveZMagnitude.lean

  The naive per-pair magnitude `z = 1/[2]_v` (v = √q₀) is PHYSICAL at A=2 (the
  deuteron) but does NOT close it — completing the explicit open thread of the
  A=4 interface-magnitude audit (docs/audits/2026-08-02-a4-interface-magnitude-
  one-scalar-gate.md; QOU/MassTheory/A4InterfaceMagnitude.lean).

  Derive-then-check, 0-fit.  The A=4 audit proved `z` is scope-(b) EXCLUDED for
  ⁴He: the `[1⁴]` complete-graph exchange spectrum `{±√5,±1}` gives
  `det(I + z·S) = (1 − 5z²)(1 − z²) < 0` (because `5z² > 1`).  The DEUTERON (A=2,
  1p+1n) has exchange graph `K₂`, spectrum `{±1}`, `det(I + m·S) = 1 − m²`, so
  `1 − z² > 0` — `z` is PHYSICAL there.  Yet it still does not close the deuteron.

  This file is deliberately **Mathlib-free core Lean** (Int / decide / omega only)
  so it is machine-checkable under the ~5 GB-olean disk wall.  It encodes the
  structural facts as decidable integer inequalities, with `z` pinned by the
  rational enclosure `4993/10000 ≤ z ≤ 4994/10000` (of `1/[2]_v = 0.4993203…`,
  verified to 50 dps in the companion probe
  `computations/deltalambda/deuteron_naive_z_physical_probe.py`); the Lean proves
  the physics CONSEQUENCES of that enclosure.

  Scope: (a) insufficiency at A=2 + (b) cross-A death of the uniform-`z` per-pair
  mechanism.  Nothing fitted; `B_AME` enters only as a diagnostic integer bound,
  never inverted; nothing wired.
-/

namespace QOU.MassTheory.DeuteronNaiveZMagnitude

/-! ### The rational enclosure of the derived magnitude `z = 1/[2]_v`

`z` is a pure substrate object; `[2]_v = √q₀ + 1/√q₀` at the canonical q₀.
The enclosure `4993/10000 ≤ z ≤ 4994/10000` is verified numerically in the probe;
everything below is a decidable consequence of it.  Denominator `D = 10000`. -/

/-- Numerator lower bound of `z` over `D = 10000`. -/
def zLo : Int := 4993
/-- Numerator upper bound of `z` over `D = 10000`. -/
def zHi : Int := 4994
/-- Common denominator for the rational enclosure of `z`. -/
def zDen : Int := 10000

/-! ### A=2 (deuteron, K₂): `det(I + m·S) = 1 − m²`, physical ⟺ `m² < 1`

`z` is PHYSICAL at A=2: `1 − z² > 0`.  Cleared of denominators with the UPPER
bound `zHi/zDen` (worst case for physicality): `zHi² < zDen²`. -/
theorem z_physical_at_A2 : zHi * zHi < zDen * zDen := by decide

/-- The A=2 interface determinant `1 − z²` is strictly positive (scaled form):
`zDen² − zHi² > 0`. -/
theorem detK2_pos_scaled : zDen * zDen - zHi * zHi > 0 := by decide

/-! ### A=4 (⁴He, `[1⁴]`): `det(I + m·S) = (1 − 5m²)(1 − m²)`, needs `5m² < 1`

`z` is EXCLUDED at A=4: `5z² > 1` ⟹ `1 − 5z² < 0` ⟹ `det < 0`.  Cleared with the
LOWER bound `zLo/zDen` (worst case for exclusion): `5·zLo² > zDen²`. -/
theorem z_excluded_at_A4 : 5 * (zLo * zLo) > zDen * zDen := by decide

/-- The A=4 factor `1 − 5z²` is strictly negative (scaled form):
`zDen² − 5·zLo² < 0`, so `det(I+zS) < 0` at A=4 — no attractive `−ln det` branch. -/
theorem detHe4_factor_neg_scaled : zDen * zDen - 5 * (zLo * zLo) < 0 := by decide

/-- **The physicality SPLIT** (the derived cited invariant): the very same derived
`z` gives a positive A=2 determinant and a negative A=4 first factor.  The A=4
writhe ceiling `1/√5` is below `z`; the A=2 ceiling `1` is above it. -/
theorem z_physical_A2_but_excluded_A4 :
    (zDen * zDen - zHi * zHi > 0) ∧ (zDen * zDen - 5 * (zLo * zLo) < 0) :=
  ⟨detK2_pos_scaled, detHe4_factor_neg_scaled⟩

/-! ### Insufficiency at A=2: one interface factor cannot supply the 5.85× deficit

Master-Σ deuteron binding `B_cat = m_e·|S(D)| = 0.380 MeV`; `B_AME(²H) = 2.2246`
MeV; the fitted deficit is `C_knot = B_AME/B_cat = 5.853`.  Integers in units of
`10⁻³ MeV`: `B_cat = 380`, `B_AME = 2225`.

The A=2 interface DRESSING factor is `1/(1 − z²)`.  Since `z² < 1/2`
(`zHi² < zDen²/2`), we have `1 − z² > 1/2`, hence `1/(1 − z²) < 2`.  So one
interface factor at most DOUBLES `B_cat`, and `2·B_cat < B_AME` by a wide
margin — the interface cannot bridge the 5.85× deficit. -/

/-- `z² < 1/2`: `2·zHi² < zDen²`.  (⟹ `1 − z² > 1/2` ⟹ interface factor `< 2`.) -/
theorem z_sq_lt_half : 2 * (zHi * zHi) < zDen * zDen := by decide

/-- Master-Σ deuteron binding in `10⁻³ MeV` (committed `|S(D)| = 0.7438`, `m_e`). -/
def BcatMilli : Int := 380
/-- AME2020 deuteron binding in `10⁻³ MeV` (diagnostic bound only, never inverted). -/
def BAmeMilli : Int := 2225

/-- **Single interface factor is insufficient.**  Even the over-generous doubling
bound `2·B_cat` (the sup of `B_cat/(1 − z²)` since `1/(1−z²) < 2`) falls short of
`B_AME`: `2·B_cat < B_AME`. -/
theorem one_interface_factor_insufficient : 2 * BcatMilli < BAmeMilli := by decide

/-! ### The deuteron is not a `[1^A]` singlet — the He4-local cumulant does not transfer

The nucleon-flavour antisymmetriser rank is `rank Λ^A(ℂ⁴) = C(4,A)` (proved in
`b4_slater_antisymmetrizer_exchange_sign.py`).  Only `A = 0` and `A = 4` are the
rank-1 SINGLET (closed-shell) cases; the deuteron `A = 2` has rank `C(4,2) = 6`,
so there is no He4-local `[1⁴]`-singlet cumulant to transfer to it. -/

/-- Binomial `C(4,k)` (finite, decidable). -/
def choose4 : Nat → Nat
  | 0 => 1
  | 1 => 4
  | 2 => 6
  | 3 => 4
  | 4 => 1
  | _ => 0

/-- `A = 2` is NOT a `[1^A]` singlet: `C(4,2) = 6 ≠ 1 = C(4,4)`. -/
theorem deuteron_not_singlet : choose4 2 ≠ 1 ∧ choose4 4 = 1 := by decide

/-! ### Cross-A verdict: the naive-uniform-`z` per-pair mechanism is dead across A -/

/-- **Uniform `z` is dead across A.**  It is scope-(b) EXCLUDED where it is NEEDED
(A=4: `det < 0`) and INSUFFICIENT where it is PHYSICAL (A=2: one interface factor
`< 2×`, far below the `5.85×` deficit).  No single derived per-pair magnitude
`z = 1/[2]_v` supplies the deuteron binding magnitude. -/
theorem naive_uniform_z_dead_across_A :
    (zDen * zDen - 5 * (zLo * zLo) < 0) ∧ (2 * BcatMilli < BAmeMilli) :=
  ⟨detHe4_factor_neg_scaled, one_interface_factor_insufficient⟩

/-- Total exterior-algebra dimension sum `∑_{k=0}^4 C(4, k) = 16 = 2^4` and strict
insufficiency even at five times `B_cat`: `5 * BcatMilli < BAmeMilli` (`1900 < 2225`). -/
theorem choose4_row_sum_and_five_Bcat_lt_BAme :
    choose4 0 + choose4 1 + choose4 2 + choose4 3 + choose4 4 = 16 ∧
      5 * BcatMilli < BAmeMilli := by
  decide

end QOU.MassTheory.DeuteronNaiveZMagnitude
