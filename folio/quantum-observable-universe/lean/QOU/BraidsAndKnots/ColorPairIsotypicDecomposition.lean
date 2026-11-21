import QOU.BraidsAndKnots.S5SO3FiberAction
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.ColorPairIsotypicDecomposition — the color-pair space

Bean `qou-ctkw` / open question 1 of `conj:inter-nucleon-channel-color-tube`.

The three color sheets **are** the `T₁` irrep of `A₅ ≅ I`
(`InterNucleonChannelColorTube.color_sheets_carry_T1`), and `BringFiberAction` is
discharged by the icosahedral Reeb instance. So the space of *ordered color-sheet
pairs* carries `T₁ ⊗ T₁`, a 9-dimensional representation of the icosahedral group.

The exact character computation (`computations/color_tube_t1_tensor_decomposition.py`,
witness `color-tube-t1-tensor-decomposition.witness.json`; inner products over
`ℚ(√5)` on the five classes of `A₅`, after asserting table orthonormality) gives

  `T₁ ⊗ T₁ = A ⊕ T₁ ⊕ H`      (dims `1 + 3 + 5 = 9`)
  `Sym² T₁ = A ⊕ H` (dim 6),  `Alt² T₁ = T₁` (dim 3).

**What this file proves.** Not a restatement of that output — the *consequences*
that are forced, and can fail:

1. `tensor_dim_consistent` — the summand dims sum to `dim(T₁)² = 9`. This would
   fail for a wrong decomposition (`A ⊕ T₁ ⊕ G` gives `8 ≠ 9`).
2. `sym_alt_assignment_forced` — **the Sym²/Alt² assignment is forced by
   dimension alone**: given the summand dims `{1, 3, 5}` and `dim Sym²(V₃) = 6`,
   the *only* sub-collection summing to 6 is `{1, 5} = {A, H}`, leaving
   `{3} = {T₁}` for `Alt²`. So the `Z/2` grading of the color pairs is not an
   extra choice — it is determined.
3. `uniform_is_isotypy_blind_barycentre` — the three isotypic projector
   diagonals sum to the identity's, and dividing by 9 returns exactly `1/9` on
   every pair: the **uniform-flavor projection is the isotypy-blind average**.
   This is the structural reading of the projection
   `conj:inter-nucleon-channel-color-tube` identifies as lossy.

**Scope (honest).** This *narrows* open question 1 — from an arbitrary
nonnegative normalised 9-vector per flavor pair (8 free parameters) to a convex
combination of three canonical weight systems (2 free parameters) — and supplies
the canonical `Z/2` for the `ε` rule. It does **not close** it: the flavor
dependence `(F₁, F₂)` is not supplied by the color-side decomposition. No
instance of `InterNucleonChannelColorTube` is provided here, and nothing is
wired.

-- Ref: [leitner2026] folio/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md
-/

namespace QOU.BraidsAndKnots.ColorPairIsotypicDecomposition

/-! ## The decomposition data (witness transcription — asserts nothing) -/

/-- Dimensions of the three summands of `T₁ ⊗ T₁`, in the order `A, T₁, H`, as
computed by the exact character decomposition. -/
def summandDims : List ℕ := [1, 3, 5]

/-- `dim Sym²(V)` for `dim V = 3`, i.e. `3·4/2`. -/
def symSquareDim : ℕ := 6

/-- `dim Alt²(V)` for `dim V = 3`, i.e. `3·2/2`. -/
def altSquareDim : ℕ := 3

/-! ## Forced consequences (these can fail) -/

/-- **Dimension consistency.** The summand dimensions sum to `dim(T₁)² = 9`.
Falsifiable: a decomposition `A ⊕ T₁ ⊕ G` would give `1 + 3 + 4 = 8 ≠ 9`. -/
theorem tensor_dim_consistent : summandDims.sum = 3 ^ 2 := by decide

/-- `Sym²` and `Alt²` partition the tensor square: `6 + 3 = 9`. -/
theorem sym_alt_dims_partition : symSquareDim + altSquareDim = 3 ^ 2 := by decide

/-- **The Sym²/Alt² assignment is FORCED by dimension.** Among the sub-collections
of the summand dimensions `{1, 3, 5}`, exactly one sums to `dim Sym² = 6`, namely
`{1, 5}` — so `Sym² T₁ = A ⊕ H` and, by complementation, `Alt² T₁ = T₁`. The
`Z/2` grading of the 9 color pairs is therefore determined, not chosen.

Stated as: of the eight sublists of `[1,3,5]`, the ones summing to `6` are
exactly `[1,5]`. -/
theorem sym_alt_assignment_forced :
    (summandDims.sublists.filter (fun l => l.sum = symSquareDim)) = [[1, 5]] := by
  decide

/-- The complementary statement: exactly one sublist sums to `dim Alt² = 3`,
namely `[3]` — the `T₁` summand. -/
theorem alt_summand_forced :
    (summandDims.sublists.filter (fun l => l.sum = altSquareDim)) = [[3]] := by
  decide

/-! ## The uniform projection is the isotypy-blind barycentre

Diagonals of the three isotypic projectors on the 9 ordered color pairs, split by
whether the pair is same-color (`rr, gg, bb`; 3 of them) or different-color
(6 of them). Rationals, from the witness. -/

/-- Projector-diagonal entry on a **same-color** pair, per summand `A, T₁, H`. -/
def diagSame : List ℚ := [1 / 3, 0, 2 / 3]

/-- Projector-diagonal entry on a **different-color** pair, per summand. -/
def diagDiff : List ℚ := [0, 1 / 2, 1 / 2]

/-- **Projector traces recover the summand dimensions.** For each summand,
`3·diag(same) + 6·diag(diff) = dim`. A genuine consistency check on the projector
data: wrong diagonals would not reproduce `1, 3, 5`. -/
theorem projector_traces_eq_dims :
    3 * diagSame[0]! + 6 * diagDiff[0]! = 1 ∧
    3 * diagSame[1]! + 6 * diagDiff[1]! = 3 ∧
    3 * diagSame[2]! + 6 * diagDiff[2]! = 5 := by
  refine ⟨by norm_num [diagSame, diagDiff], by norm_num [diagSame, diagDiff],
    by norm_num [diagSame, diagDiff]⟩

/-- **The uniform projection `W = 1/9` is the isotypy-blind barycentre.** The
three projectors sum to the identity, whose diagonal is `1` on every pair; so
dividing the summed diagonal by 9 returns exactly `1/9` on both pair classes.
The "flavor-only projection" the conjecture identifies as lossy is precisely the
average that forgets which isotypic summand a pair sits in. -/
theorem uniform_is_isotypy_blind_barycentre :
    (diagSame.sum) / 9 = 1 / 9 ∧ (diagDiff.sum) / 9 = 1 / 9 := by
  constructor <;> norm_num [diagSame, diagDiff]

/-- **The three canonical weight systems are distinct.** Normalising each
projector diagonal by its trace gives three *different* normalised weight systems
on the color pairs (`A`: all mass on same-color; `T₁`: all on different-color;
`H`: split). So the isotypic decomposition genuinely narrows `W` — it is not
three names for one weighting. -/
theorem canonical_weight_systems_distinct :
    diagSame[0]! / 1 ≠ diagSame[1]! / 3 ∧
    diagSame[1]! / 3 ≠ diagSame[2]! / 5 ∧
    diagSame[0]! / 1 ≠ diagSame[2]! / 5 := by
  refine ⟨by norm_num [diagSame], by norm_num [diagSame], by norm_num [diagSame]⟩

end QOU.BraidsAndKnots.ColorPairIsotypicDecomposition
