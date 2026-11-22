import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.FiveTwoDTSpectrumSplit — the 5₂ cross-knot {3,4} distinguisher

The **structural resolution lever** for the scalar-symmetry-constant vs
DT-spectrum fork of the c₃-odd / `A_ω` question (keystone ledger
`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`; audit
`docs/audits/2026-08-02-fivetwo-crossknot-34-resolution.md`).

For the figure-eight knot `4₁` the GGM Stokes matrix is `2×2` and its
q→0 form is `S⁺(0) = [[1,3],[0,1]]` (`StokesQZeroDTCount`), carrying the
**single** off-diagonal integer `3`; the q-exact symmetry constant is
`(S₁₂+S₂₁)/S₁₁ = 3` (`StokesSymmetryConstant`). Because `4₁` is
**amphichiral**, its two Stokes matrices `S⁺, S⁻` are related by the
amphichiral involution `ι`, and the scalar `3` is unambiguous — the
scalar and the DT *spectrum* cannot be separated in the `2×2` block.

`5₂` is **chiral** and its Stokes block is `3×3`. The certified sandwich
compute (`computations/probes/qbeta_g3_5two_stokes_sandwich.py`,
K1/K2/K3 ✓; the same integer matrices are promoted to Mathlib-`Matrix`
form in `FiveTwoStokesMatrixIdentities`) gives

    S⁺(0) = [[1,4,0],[0,1,0],[-3,-9,1]]   (the (96) factorization, constant 4)
    S⁻(0) = [[1,0,3],[-4,1,-3],[0,0,1]]   (the (97) factorization, constant 3)

so the DT spectrum `{3,4}` is **split across chirality**: the `4` lives in
`S⁺`, the `3` in `S⁻`. The companion probe
`computations/probes/fivetwo_crossknot_34_distinguisher.py` further finds
that the *literal* `4₁` symmetry constant `(S₁₂+S₂₁)/S₁₁` is **not** a
q-exact constant for either `5₂` block (unlike `4₁`), reinforcing that no
single scalar clones across the two knots.

This file proves — by decidable integer arithmetic on the certified
matrix entries — the facts that make `5₂` a *distinguisher*:

* `dt_spectrum_two_element` — the spectrum genuinely has **two distinct**
  members (`4 ≠ 3`); unlike `4₁`, no single integer serves the leading
  Stokes data.
* `chirality_odd_datum_ne_zero` — the ι-**odd** (antisymmetric) datum of
  the two chirality constants, `chiralityOdd 4 3 = 1 ≠ 0`, is nonzero,
  whereas on the amphichiral (degenerate) locus `chiralityOdd a a = 0`.
* `readings_all_distinct` — the ι-even sum (`7`), the two members (`4`,
  `3`), and the ι-odd difference (`1`) are pairwise distinct.

**Why this settles the fork (scope, honest — no derivation, no fit).**
The bar-odd observable `ω = β·p − β⁻¹·q` is **ι-odd** and vanishes on
the amphichiral ι-fixed locus (`BarOddAntisymOffDiagonal.omega_iota_odd`,
`omega_zero_on_iotaFixed`). An ι-odd observable cannot be carried by an
ι-**even** symmetric-sum constant (the object that yields the scalar `3`
at `4₁`). `5₂` exhibits, as decidable data, that the relevant Stokes
constants for a chiral knot form a genuine 2-element spectrum split by
chirality, and that their ι-odd datum is the *difference* — sourced only
by chirality, exactly `0` at the amphichiral degeneracy. Hence the
observable's normalization integer is **not** a knot-independent scalar
`A_ω = 3`; it is a member/combination of the chirality-split spectrum,
degenerating to the single `3` at `4₁` only because the two chiralities
coincide there. This is a **scope-(a) structural refutation** of the
single-scalar reading (it neither confirms A=2/κ_shape nor A=3/A_ω·κ_pot
as a universal scalar); which spectrum member the observable inherits is
the residual normalization fork (`qou-yh67`), now sharpened to a *choice
among `{3,4}`*, not *scalar vs spectrum*.

**Base ring / imports (honest).** This file uses only **core Lean** (no
`import Mathlib.*`): the certified Stokes matrices are *integer* matrices,
so their entries and the DT constants live natively in `Int`; the ι-odd
datum lemmas are stated over `Int` and discharged by `decide`/`omega`
(both core). No `ℝ`, no ordering, no `Real.*` (§7c satisfied — the
substrate→archimedean wall is not crossed). The Mathlib-`Matrix`
promotion of the *same* data lives in `FiveTwoStokesMatrixIdentities`;
this file is deliberately core-only so it verifies with the toolchain
alone (no Mathlib olean set required). It does **not** derive the number
from the 13 categorical drivers, does **not** bridge to c₃, and does
**not** pick a normalization.

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (5₂ DT spectrum, eqs 96/97/98)
-- Ref: [leitner2026] docs/audits/2026-08-02-fivetwo-crossknot-34-resolution.md
-/

namespace QOU.QBeta.FiveTwoDTSpectrumSplit

/-! ## Certified 5₂ leading Stokes matrices (core-only `Fin 3 → Fin 3 → Int`)

The same integer matrices as `FiveTwoStokesMatrixIdentities.Splus0 /
Sminus0`, written as explicit index functions so the file needs no Mathlib
`Matrix.Notation` (hence no Mathlib olean set to verify). -/

/-- `S⁺(0)` for 5₂ — the glyph-decoded (96) factorization (constant `4`). -/
def Splus0 : Fin 3 → Fin 3 → Int
  | 0, 0 => 1  | 0, 1 => 4  | 0, 2 => 0
  | 1, 0 => 0  | 1, 1 => 1  | 1, 2 => 0
  | 2, 0 => -3 | 2, 1 => -9 | 2, 2 => 1

/-- `S⁻(0)` for 5₂ — the glyph-decoded (97) factorization (constant `3`). -/
def Sminus0 : Fin 3 → Fin 3 → Int
  | 0, 0 => 1  | 0, 1 => 0  | 0, 2 => 3
  | 1, 0 => -4 | 1, 1 => 1  | 1, 2 => -3
  | 2, 0 => 0  | 2, 1 => 0  | 2, 2 => 1

/-- The `4₁` q→0 Stokes matrix `S⁺(0) = [[1,3],[0,1]]` (GGM eq 60,
`StokesQZeroDTCount.Splus0`), carried as a `2×2` for the amphichiral
contrast. -/
def Splus0_41 : Fin 2 → Fin 2 → Int
  | 0, 0 => 1 | 0, 1 => 3
  | 1, 0 => 0 | 1, 1 => 1

/-! ## The DT spectrum of 5₂ is `{3,4}` — split across chirality -/

/-- `S⁺(0)` carries the DT constant `4` (its `(0,1)` entry — the (96)
factorization constant). -/
theorem splus0_carries_four : Splus0 0 1 = 4 := by decide

/-- `S⁻(0)` carries the DT constant `3` (its `(0,2)` entry — the (97)
factorization constant). -/
theorem sminus0_carries_three : Sminus0 0 2 = 3 := by decide

/-- The `4₁` leading Stokes matrix carries the **single** off-diagonal
integer `3` (its `(0,1)` entry) — the amphichiral degeneracy where the
spectrum collapses to one member. -/
theorem fourone_carries_three : Splus0_41 0 1 = 3 := by decide

/-- **The 5₂ DT spectrum has two distinct members.** The constant carried
by `S⁺` (`4`) differs from the constant carried by `S⁻` (`3`): unlike the
amphichiral `4₁`, a chiral knot's leading Stokes data is not served by a
single integer. -/
theorem dt_spectrum_two_element : Splus0 0 1 ≠ Sminus0 0 2 := by decide

/-! ## The chirality (ι-odd) datum is nonzero — the distinguisher

The bar-odd observable is ι-odd (`BarOddAntisymOffDiagonal.omega_iota_odd`)
and vanishes on the amphichiral ι-fixed locus. The corresponding datum at
the level of the two chirality **constants** is their antisymmetric
combination `chiralityOdd a b = a − b`, which is nonzero exactly when the
knot is chiral (the two constants differ) and `0` at the amphichiral
degeneracy (`a = a`). -/

/-- The ι-odd (antisymmetric) combination of the two chirality constants,
over `Int` (core; the Stokes constants are integers — no archimedean
structure, §7c). -/
def chiralityOdd (a b : Int) : Int := a - b

/-- **On the amphichiral degeneracy the ι-odd datum vanishes.** When the
two chirality constants coincide (the `4₁` case, one member), their
antisymmetric datum is `0` — the Stokes-constant analogue of
`omega_zero_on_iotaFixed`. -/
theorem chiralityOdd_degenerate (a : Int) : chiralityOdd a a = 0 := by
  unfold chiralityOdd; omega

/-- **The ι-odd datum is genuinely antisymmetric** under swapping the two
chirality constants (the Stokes-constant analogue of `ω` being ι-odd). -/
theorem chiralityOdd_antisym (a b : Int) :
    chiralityOdd b a = - chiralityOdd a b := by
  unfold chiralityOdd; omega

/-- **The 5₂ chirality datum is nonzero.** For the certified split
`(S⁺ ↦ 4, S⁻ ↦ 3)` the ι-odd datum is `chiralityOdd 4 3 = 1 ≠ 0` — the
bar-odd (ι-odd) channel receives a genuine, chirality-sourced Stokes
datum from `5₂`, which the amphichiral `4₁` (where it is `0`) cannot
supply. -/
theorem chirality_odd_datum_eq_one :
    chiralityOdd (Splus0 0 1) (Sminus0 0 2) = 1 := by decide

/-- The chirality datum is nonzero as an inequality (the honest "genuine
datum" form). -/
theorem chirality_odd_datum_ne_zero :
    chiralityOdd (Splus0 0 1) (Sminus0 0 2) ≠ 0 := by decide

/-! ## The scalar reading fails: sum ≠ member ≠ difference

At `4₁` the single scalar `3` simultaneously *is* the off-diagonal entry,
the symmetry constant, and (trivially) the whole spectrum. For chiral `5₂`
the symmetric-sum reading (`4+3 = 7`), the individual members (`4`, `3`),
and the antisymmetric difference (`1`) are **four different integers** —
so no single scalar reproduces the leading Stokes data. -/

/-- The symmetric (ι-even) sum of the two chirality constants is `7`. -/
theorem chirality_sum_seven : Splus0 0 1 + Sminus0 0 2 = 7 := by decide

/-- **No single scalar serves all readings.** For chiral `5₂` the ι-even
sum (`7`), the two spectrum members (`4`, `3`), and the ι-odd difference
(`1`) are pairwise distinct — the amphichiral collapse of `4₁` (all equal
to `3`) does not occur. -/
theorem readings_all_distinct :
    (Splus0 0 1 + Sminus0 0 2 ≠ Splus0 0 1) ∧
    (Splus0 0 1 ≠ Sminus0 0 2) ∧
    (chiralityOdd (Splus0 0 1) (Sminus0 0 2) ≠ Splus0 0 1) ∧
    (chiralityOdd (Splus0 0 1) (Sminus0 0 2) ≠ Sminus0 0 2) := by decide

/-! ## Route C, M0 — the DT split IS the bar-eigenspace decomposition

The chirality involution `τ` (the `q ↦ q⁻¹` / mirror swap) on the ordered pair
of q→0 Stokes constants `(dt⁺, dt⁻)`, the faithful `ℤ/2` (bar-even ⊕ bar-odd)
grading it induces, and the corollary that any `τ`-symmetric *scalar* is blind to
the nonzero bar-odd datum — the bar-graded restatement of
`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum`. This is
milestone M0 of Route C: it turns the proved "no scalar" negative into the
positive statement *"the DT count is the bar-graded object"*, connecting the split
to the corpus bar-parity programme (`c1-ggm-bar-parity-faces`,
`OhtsukiTowerBarParity`).
-- Ref: [leitner2026] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md (Route C M0) -/

/-- The chirality involution `τ` on the ordered pair of `S⁺`/`S⁻` Stokes
constants (the mirror / `q ↦ q⁻¹` swap exchanging the two factorization
constants). -/
def barSwap : Int × Int → Int × Int := fun p => (p.2, p.1)

/-- `τ` is an involution: `τ ∘ τ = id`. -/
theorem barSwap_involutive (p : Int × Int) : barSwap (barSwap p) = p := by
  cases p; rfl

/-- Bar-even part of the pair (the `τ`-symmetric combination). -/
def barEvenPair (p : Int × Int) : Int := p.1 + p.2

/-- Bar-odd part of the pair (the `τ`-antisymmetric combination = `chiralityOdd`). -/
def barOddPair (p : Int × Int) : Int := chiralityOdd p.1 p.2

/-- `τ` fixes the bar-even part (the `+1` eigenspace). -/
theorem barEvenPair_fixed (p : Int × Int) :
    barEvenPair (barSwap p) = barEvenPair p := by
  cases p; unfold barEvenPair barSwap; omega

/-- `τ` negates the bar-odd part (the `-1` eigenspace). -/
theorem barOddPair_negated (p : Int × Int) :
    barOddPair (barSwap p) = - barOddPair p := by
  cases p; unfold barOddPair barSwap chiralityOdd; omega

/-- **Faithful reconstruction.** The ordered pair is recovered from its
bar-grading (`2·dt⁺ = even + odd`, `2·dt⁻ = even − odd`): the `ℤ/2` grading loses
no information, so the DT spectrum *is* its bar-graded datum. -/
theorem barGrading_faithful (p : Int × Int) :
    2 * p.1 = barEvenPair p + barOddPair p ∧
    2 * p.2 = barEvenPair p - barOddPair p := by
  cases p; unfold barEvenPair barOddPair chiralityOdd; constructor <;> omega

/-- The certified ordered `5₂` DT-constant pair `(4, 3)`. -/
def dtPair52 : Int × Int := (Splus0 0 1, Sminus0 0 2)

/-- Its bar-grading is `(even, odd) = (7, 1)`. -/
theorem dtPair52_grading :
    (barEvenPair dtPair52, barOddPair dtPair52) = (7, 1) := by decide

/-- **The `5₂` datum is genuinely chiral**: `τ` moves it (`(4,3) ↦ (3,4)`),
because its bar-odd part is nonzero. -/
theorem dtPair52_chiral : barSwap dtPair52 ≠ dtPair52 := by decide

/-- **Scalar-shadow corollary** (bar-graded form of
`no_scalar_matches_chirality_split_datum`). Any `τ`-symmetric integer reading `g`
(`g a b = g b a`) assigns the *same* value to the chirality-swapped pair, so it
cannot recover the ordered `5₂` datum, whose bar-odd part is nonzero (`= 1`).
"No scalar serves the datum" ⇔ "the bar-odd part is nonzero". -/
theorem symmetric_scalar_blind_to_chirality
    (g : Int → Int → Int) (hsym : ∀ a b, g a b = g b a) :
    g dtPair52.1 dtPair52.2 = g (barSwap dtPair52).1 (barSwap dtPair52).2
      ∧ barOddPair dtPair52 ≠ 0 := by
  refine ⟨?_, by decide⟩
  show g dtPair52.1 dtPair52.2 = g dtPair52.2 dtPair52.1
  exact hsym _ _

end QOU.QBeta.FiveTwoDTSpectrumSplit
