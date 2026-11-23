import QOU.BraidsAndKnots.S5SO3FiberAction
import QOU.BraidsAndKnots.BringFiberActionInstance
import Mathlib.Algebra.Order.Ring.Rat
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.InterNucleonChannelColorTube — the D6-upstream color-tube channel class

§3b-cond class axiomatisation for content block
`conj:inter-nucleon-channel-color-tube` (color-tube weighted inter-nucleon
Hecke channel assignment), replacing the former sibling stub's vacuous
`holds : Prop` placeholder with the content-bearing structure sketched in the
block's "Lean axiomatisation (sketch)" section.

**What is encoded here (statable today):**
- the color-sheet / quark-flavor ground types (`ColorSheet`, `QuarkFlavor`,
  `NucleonColorContent`, proton/neutron content);
- the chirality-sign rule `ε(c₁, c₂, F₁, F₂) ∈ {+1, −1, 0}` exactly as stated
  in the block (+1 matter–matter match, −1 flavor-conjugate, 0 mixed) — a
  *definition*, with its value-range proved;
- the class `InterNucleonChannelColorTube` carrying the weight tensor
  `W_{c₁c₂}(F₁, F₂) ∈ ℚ≥0` with its normalisation `Σ_{c₁c₂} W = 1`
  (ℚ is used, not a generic ring, because the block's nonnegativity
  constraint genuinely requires an order — §7c);
- the uniform-flavor projection `W = 1/9` as a **named witness of
  satisfiability** (`uniformColorTubeData`) — deliberately NOT registered as
  an instance, because the conjecture's content is that the true weights
  derive from the Bring SO(3)-fiber tensor, and the uniform projection is
  exactly the flavor-only collapse the block identifies as missing structure;
- the fiber-action wiring facts that are already derivable from the
  discharged `BringFiberAction` instance: the color sheets are the T₁
  irrep's basis (dim T₁ = 3 = #sheets, T₁ = the ℓ = 1 Hopf selection), and
  the color-sheet fiber rotation is pinned to the icosahedral Reeb phase
  `arccos(φ/3)`.

**What remains OPEN (the conjecture, per the block's §Open questions):** the
closed form of `W_{c₁c₂}` as a tensor in the SO(3)-fiber data over Bring
(open question 1) and the derivation of the ε rule from the S₅-orbit / CPT
structure (open question 2). No global instance is provided; downstream
results consume `[InterNucleonChannelColorTube]` as a genuine hypothesis.

The substrate-pure realisation of the flavor-only projection is implemented
in `computations/closed_form_tau_M.py` under
`pn_convention="bring_color_weighted"` (PROVED, PR #690/#942).

-- Ref: [leitner2026] conj:inter-nucleon-channel-color-tube
-/

namespace QOU.BraidsAndKnots

/-! ## Ground types: color sheets and quark flavors -/

/-- Color-sheet label r/g/b of a nucleon's three quark color sheets. -/
inductive ColorSheet
  | r | g | b
  deriving DecidableEq, Repr

/-- The three color sheets. -/
def ColorSheet.allList : List ColorSheet := [.r, .g, .b]

/-- Quark flavor including the antimatter conjugates (u, d, ū, d̄).
    The matter/antimatter doubling is what the D6 charge-conjugation
    conjecture (`conj:c-from-color-flavor-swap`) acts on. -/
inductive QuarkFlavor
  | u | d | ubar | dbar
  deriving DecidableEq, Repr

/-- Flavor conjugation u ↔ ū, d ↔ d̄ (the D6 C-action on a single sheet). -/
def QuarkFlavor.conj : QuarkFlavor → QuarkFlavor
  | .u => .ubar
  | .ubar => .u
  | .d => .dbar
  | .dbar => .d

/-- Flavor conjugation is an involution. -/
theorem QuarkFlavor.conj_involutive (f : QuarkFlavor) : f.conj.conj = f := by
  cases f <;> rfl

/-- A nucleon's color-sheet content: the flavor carried on each of the three
    color sheets (r, g, b order). -/
def NucleonColorContent : Type := QuarkFlavor × QuarkFlavor × QuarkFlavor

/-- Proton color content (u, u, d). -/
def proton : NucleonColorContent := (QuarkFlavor.u, QuarkFlavor.u, QuarkFlavor.d)

/-- Neutron color content (u, d, d). -/
def neutron : NucleonColorContent := (QuarkFlavor.u, QuarkFlavor.d, QuarkFlavor.d)

/-- The flavor a nucleon carries on a given color sheet. -/
def NucleonColorContent.flavorAt : NucleonColorContent → ColorSheet → QuarkFlavor
  | (f, _, _), .r => f
  | (_, f, _), .g => f
  | (_, _, f), .b => f

/-! ## The 9 color-sheet pairs of an inter-nucleon arc -/

/-- The 9 color-sheet pairs `(c₁, c₂) ∈ {r,g,b}²` of an inter-nucleon arc. -/
def colorPairs : List (ColorSheet × ColorSheet) :=
  [(.r, .r), (.r, .g), (.r, .b),
   (.g, .r), (.g, .g), (.g, .b),
   (.b, .r), (.b, .g), (.b, .b)]

/-- All 9 color pairs are listed. -/
theorem colorPairs_length : colorPairs.length = 9 := rfl

/-! ## The chirality sign ε (the block's stated rule) -/

/-- The chirality sign `ε(c₁, c₂, F₁, F₂)` of a color-sheet pair, exactly as
    stated in `conj:inter-nucleon-channel-color-tube` §"The conjectural
    refinement": +1 when the flavors at the contact match (matter–matter),
    −1 when they are flavor-conjugate (matter–antimatter), 0 otherwise
    (mixed-flavor pairs that average to `σ_avg`).  The *derivation* of this
    rule from the S₅-orbit / CPT structure is the block's open question 2;
    the rule itself is the conjecture's stated data. -/
def chiralitySign (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonColorContent) : ℤ :=
  if F₁.flavorAt c₁ = F₂.flavorAt c₂ then 1
  else if F₁.flavorAt c₁ = (F₂.flavorAt c₂).conj then -1
  else 0

/-- ε takes values in {+1, −1, 0}. -/
theorem chiralitySign_mem (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonColorContent) :
    chiralitySign c₁ c₂ F₁ F₂ = 1 ∨ chiralitySign c₁ c₂ F₁ F₂ = -1 ∨
      chiralitySign c₁ c₂ F₁ F₂ = 0 := by
  unfold chiralitySign
  split_ifs <;> simp

/-! ## The §3b-cond class: the color-tube weight tensor -/

/-- **CONJECTURE (§3b-cond class).** Inter-nucleon Hecke channel assignment
    from Bring color-tube weighting: the canonical color-pair weight tensor
    `W_{c₁c₂}(F₁, F₂) ∈ ℚ≥0`, normalised to `Σ_{c₁c₂} W = 1` per flavor pair,
    so the refined generator `σ^(F₁,F₂) = Σ W_{c₁c₂} σ^{ε(c₁,c₂,F₁,F₂)}` is a
    categorical average over the 9 color-sheet pairs.

    The `[BringFiberAction]` binder records the conditional structure of the
    block ("conditional on `conj:s5-so3-fiber-action`"); that supplier class
    is now discharged by the icosahedral Reeb instance
    (`bringFiberAction_icosahedral`).  The remaining open content — the
    closed form of `W` as a tensor in the SO(3)-fiber data over Bring, with
    no residual degrees of freedom — is exactly what an instance of this
    class must supply.  No global instance is provided: the uniform-flavor
    projection `uniformColorTubeData` below witnesses satisfiability but is
    deliberately not registered, because it is the flavor-only collapse the
    conjecture identifies as missing the per-arc structure. -/
-- Ref: [leitner2026] conj:inter-nucleon-channel-color-tube
class InterNucleonChannelColorTube [BringFiberAction] where
  /-- The categorical weight of a color-sheet pair given the source/target
      nucleon flavor content. -/
  weight : ColorSheet → ColorSheet → NucleonColorContent → NucleonColorContent → ℚ
  /-- Weights are nonnegative (`W ∈ ℚ≥0` per the block statement). -/
  weight_nonneg : ∀ c₁ c₂ F₁ F₂, 0 ≤ weight c₁ c₂ F₁ F₂
  /-- Normalisation: the 9 color-pair weights sum to 1 for each flavor pair
      (the refined generator is a categorical average). -/
  weight_normalized : ∀ F₁ F₂,
    (colorPairs.map (fun p => weight p.1 p.2 F₁ F₂)).sum = 1

/-! ## The uniform-flavor projection — satisfiability witness (NOT an instance) -/

/-- The uniform color-pair weight `W_{c₁c₂} = 1/9`. -/
def uniformWeight (_ _ : ColorSheet) (_ _ : NucleonColorContent) : ℚ := 1 / 9

/-- The uniform weights are normalised. -/
theorem uniformWeight_normalized (F₁ F₂ : NucleonColorContent) :
    (colorPairs.map (fun p => uniformWeight p.1 p.2 F₁ F₂)).sum = 1 := by
  simp [colorPairs, uniformWeight]
  norm_num

/-- **Satisfiability witness — deliberately NOT an instance.**  The
    uniform-flavor projection `W = 1/9` satisfies the class shape (the block's
    §"Uniform-flavor projection": it recovers the current production
    assignment).  It is not registered as an instance because it is exactly
    the flavor-only collapse the conjecture identifies as missing the
    load-bearing per-arc structure (the sign-flip diagnostic's R² = 0.83
    arc-count correlation); registering it would dishonestly "discharge" the
    conjecture with the very projection it refines. -/
noncomputable def uniformColorTubeData [BringFiberAction] :
    InterNucleonChannelColorTube where
  weight := uniformWeight
  weight_nonneg := fun _ _ _ _ => by norm_num [uniformWeight]
  weight_normalized := uniformWeight_normalized

/-! ## Fiber-action wiring: color sheets = the T₁ irrep basis -/

/-- **Color sheets carry the T₁ irrep.**  The three color sheets are the
    basis of the 3-dimensional icosahedral irrep T₁ — the ℓ = 1 Hopf
    generation selection (`hopfGenerationSelect 1 = T₁`,
    `icosBranchingMult 1 = V₁ = T₁`).  This is the derivable half of the
    "weight tensor from SO(3)-fiber data" wiring: the fiber datum the tensor
    must be built from is the T₁ block of the discharged fiber action. -/
theorem color_sheets_carry_T1 :
    ColorSheet.allList.length = A5Irrep.T₁.dim ∧
    hopfGenerationSelect 1 = A5Irrep.T₁ := by
  exact ⟨rfl, rfl⟩

/-- **The color-sheet fiber rotation is the icosahedral Reeb phase.**  Under
    the discharged `bringFiberAction_icosahedral` instance, the T₁ (color
    sheet) fiber rotation angle is pinned to `arccos((1+√5)/6) = arccos(φ/3)`
    — the concrete SO(3)-fiber datum over Bring that the conjectural weight
    tensor `W_{c₁c₂}` must derive from. -/
theorem colorSheet_fiber_rotation_angle :
    (bringFiberAction_icosahedral.irrepToRotation A5Irrep.T₁).asSO3.angle
      = Real.arccos ((1 + Real.sqrt 5) / 6) := rfl

/-! ## Proton–neutron contact split and linear contraction (`qou-dx1t`) -/

/-- **Proton–neutron contact counts (`qou-dx1t`).** Across the 9 color-sheet
    contacts of `(proton, neutron)` (`uud × udd`), there are exactly:
    - `4` matched contacts (`ε = +1`: `2` `u–u` and `2` `d–d`),
    - `5` mixed contacts (`ε = 0`: `u–d` and `d–u`),
    - `0` flavor-conjugate contacts (`ε = -1`: no antiquarks in matter–matter). -/
theorem proton_neutron_contact_counts :
    (colorPairs.filter (fun p => decide (chiralitySign p.1 p.2 proton neutron = 1))).length = 4 ∧
    (colorPairs.filter (fun p => decide (chiralitySign p.1 p.2 proton neutron = 0))).length = 5 ∧
    (colorPairs.filter (fun p => decide (chiralitySign p.1 p.2 proton neutron = -1))).length = 0 := by
  decide

/-- Sum of `W_{c₁c₂}(proton, neutron)` over the 5 mixed-flavor (`ε = 0`)
    color-sheet contacts (`c(W)` in bean `qou-dx1t`). -/
def pnMixedWeightSum
    (W : ColorSheet → ColorSheet → NucleonColorContent → NucleonColorContent → ℚ) : ℚ :=
  (colorPairs.map (fun p =>
    if chiralitySign p.1 p.2 proton neutron = 0 then W p.1 p.2 proton neutron else 0)).sum

/-- The color-pair-contracted `(proton, neutron)` crossing offset `t_{pn}`
    (measured in units of `−h`), when a matched contact (`ε = +1`, `σ_g`) has
    offset `0`, a conjugate contact (`ε = -1`, `σ_g⁻¹`) has offset `1`, and a
    mixed contact (`ε = 0`, `σ_avg`) has offset `x` (`x = 1/2` for the raw
    symmetrised channel, or `x = 1/2 - δ/4` on the weighted channel). -/
def pnContractedOffset
    (W : ColorSheet → ColorSheet → NucleonColorContent → NucleonColorContent → ℚ)
    (x : ℚ) : ℚ :=
  (colorPairs.map (fun p =>
    W p.1 p.2 proton neutron *
      (if chiralitySign p.1 p.2 proton neutron = 1 then (0 : ℚ)
       else if chiralitySign p.1 p.2 proton neutron = -1 then 1
       else x))).sum

/-- **Linear contraction identity (`qou-dx1t`).** Because `(proton, neutron)` has
    `0` contacts with `ε = -1` and `4` contacts with `ε = +1` (whose offset is `0`),
    the contracted `(p, n)` offset is strictly linear in the mixed-contact datum `x`:
    `t_{pn} = c(W) · x`. The colour-tube weight tensor `W` scales `x` by `c(W)`
    and does not eliminate `x` as an input unless `c(W) = 0`. -/
theorem pnContractedOffset_eq_mixedWeightSum_mul
    (W : ColorSheet → ColorSheet → NucleonColorContent → NucleonColorContent → ℚ)
    (x : ℚ) :
    pnContractedOffset W x = pnMixedWeightSum W * x := by
  simp [pnContractedOffset, pnMixedWeightSum, colorPairs, ColorSheet.allList,
    chiralitySign, proton, neutron, NucleonColorContent.flavorAt, QuarkFlavor.conj]
  ring

/-- Under uniform color-pair weighting `W = 1/9`, the 5 mixed contacts sum to
    `c(W) = 5/9`. -/
theorem uniform_pnMixedWeightSum :
    pnMixedWeightSum uniformWeight = 5 / 9 := by
  simp [pnMixedWeightSum, uniformWeight, colorPairs, ColorSheet.allList,
    chiralitySign, proton, neutron, NucleonColorContent.flavorAt, QuarkFlavor.conj]
  norm_num

/-- Under uniform color-pair weighting `W = 1/9`, the contracted `(p, n)` offset
    is `t_{pn} = (5/9) · x`. -/
theorem uniform_pnContractedOffset (x : ℚ) :
    pnContractedOffset uniformWeight x = (5 / 9) * x := by
  rw [pnContractedOffset_eq_mixedWeightSum_mul, uniform_pnMixedWeightSum]

end QOU.BraidsAndKnots
