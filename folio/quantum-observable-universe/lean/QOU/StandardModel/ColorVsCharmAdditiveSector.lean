/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# QOU.StandardModel.ColorVsCharmAdditiveSector — Color-Sheet Sector vs Charm Quark in the Inter-Nucleon Additive Channel

Bean `qou-q6lw` (Epic `qou-8lxd` — Eightfold Way / Standard Model derived from QOU).

Resolves the owner question:
> *"Is the additive term for charm or is it the color sector? Look in the
> existing repo to see what we have already done for this."*

Three distinct objects in the QOU corpus carry the letter `c` / `C` or a
quark-sector label:

1. **The inter-nucleon additive term acts on the 3-strand COLOR-SHEET sector**
   (`conj:inter-nucleon-channel-color-tube`,
   `QOU.BraidsAndKnots.InterNucleonChannelColorTube`,
   `QOU.BraidsAndKnots.ColorPairIsotypicDecomposition`).
   Each nucleon carries three quark color sheets `(r, g, b)` spanning the
   3-dimensional icosahedral irrep `T₁` of `A₅ ≅ I`. At an inter-nucleon
   interface, gluon exchange couples the `3 × 3 = 9` ordered color-sheet pairs
   `(c₁, c₂) ∈ {r, g, b}²`, with the flavor-blind bar-symmetric average
   `σ + σ⁻¹ = 2σ − h` (Markov trace factor `z − h/2`) and subleading light
   `(u, d)` color-tube asymmetry `4z − 2h + hδ = 2(2z − h) + hδ`.

2. **The symbol `C` in `c-from-color-flavor-swap` is discrete CHARGE
   CONJUGATION, not the charm quark `𝔠`**
   (`conj:c-from-color-flavor-swap`, `QOU.BraidsAndKnots.CFromColorFlavorSwap`).
   `LightSignedFlavor.conj` swaps `u ↔ ū` and `d ↔ d̄` on each of the three color
   sheets (`p ↔ p̄`, `n ↔ n̄`, `C² = id`), preserving the base flavor (`up` or
   `down`) on every sheet and leaving the chirality sign `ε(c₁, c₂, F₁, F₂)`
   invariant across all `16 × 9 = 144` nucleon/color cells.

3. **The charm quark `𝔠` (`QuarkSixFlavor.charm`) lives in the heavy-meson mass
   dressing sector (`def:flavor-dressing-functor`,
   `QOU.FlavorDressing.Flavor`) and has ZERO projection onto the 3-strand
   `(u, d)` nucleon color-sheet channel.**
   Every `LightSignedFlavor` carried by a nucleon or antinucleon color sheet maps
   to `{up, down}`, disjoint from `charm` (and from `strange`, `bottom`, `top`).
   Consequently, the charm occupation count on any nucleon color-sheet triple
   and the charm-projected contact sum across all 9 inter-nucleon color-sheet
   pairs are identically zero.

All theorems in this file are division-free (§7c) and proved with `0` `sorry`.

-- Ref: [manuscript] conj:inter-nucleon-channel-color-tube
-- Ref: [manuscript] conj:c-from-color-flavor-swap
-- Ref: [manuscript] def:flavor-dressing-functor
-/

namespace QOU.StandardModel.ColorVsCharmAdditiveSector

/-! ## 1. Color sheets, 6-quark flavors, and signed nucleon-sheet flavors -/

/-- The three quark color sheets `(r, g, b)` of a 3-strand baryon braid,
    spanning the 3-dimensional icosahedral irrep `T₁` of `A₅ ≅ I`. -/
inductive ColorSheet where
  | r | g | b
  deriving DecidableEq, Repr

/-- The list of all three color sheets. -/
def ColorSheet.allList : List ColorSheet := [.r, .g, .b]

/-- The 9 ordered color-sheet pairs `(c₁, c₂) ∈ {r, g, b}²` coupled by
    inter-nucleon gluon exchange. -/
def colorPairs : List (ColorSheet × ColorSheet) :=
  [(.r, .r), (.r, .g), (.r, .b),
   (.g, .r), (.g, .g), (.g, .b),
   (.b, .r), (.b, .g), (.b, .b)]

/-- Dimension of the `T₁ ⊗ T₁ = A ⊕ T₁ ⊕ H` color-pair space (`1 + 3 + 5 = 9`). -/
def t1TensorSummandDims : List Nat := [1, 3, 5]

/-- The 9 color-sheet pairs match `dim(T₁)² = 1 + 3 + 5 = 9`. -/
theorem colorPairs_dim_eq_t1_tensor :
    colorPairs.length = 9 ∧
    ColorSheet.allList.length = 3 ∧
    t1TensorSummandDims.sum = colorPairs.length := by
  decide

/-- The six quark flavors of the flavor-dressing category
    (`QOU.FlavorDressing.Flavor`). -/
inductive QuarkSixFlavor where
  | up | down | strange | charm | bottom | top
  deriving DecidableEq, Repr

/-- Signed light quark flavors `(u, d, ū, d̄)` carried on nucleon/antinucleon
    color sheets (`QOU.BraidsAndKnots.QuarkFlavor`). -/
inductive LightSignedFlavor where
  | u | d | ubar | dbar
  deriving DecidableEq, Repr

/-- Discrete charge conjugation `C` (`u ↔ ū`, `d ↔ d̄`) on a single color sheet
    (`conj:c-from-color-flavor-swap`). -/
def LightSignedFlavor.conj : LightSignedFlavor → LightSignedFlavor
  | .u => .ubar
  | .ubar => .u
  | .d => .dbar
  | .dbar => .d

/-- `C` is an involution on `LightSignedFlavor`. -/
theorem LightSignedFlavor.conj_involutive (f : LightSignedFlavor) :
    f.conj.conj = f := by
  cases f <;> rfl

/-- Underlying base flavor in `QuarkSixFlavor` of a signed light nucleon-sheet
    flavor. -/
def LightSignedFlavor.baseFlavor : LightSignedFlavor → QuarkSixFlavor
  | .u => .up
  | .ubar => .up
  | .d => .down
  | .dbar => .down

/-- **Charge conjugation `C` preserves the base flavor (`up` or `down`) on every
    color sheet**: `C` is matter↔antimatter conjugation within generation 1,
    never a transition to `QuarkSixFlavor.charm`. -/
theorem baseFlavor_conj_invariant (f : LightSignedFlavor) :
    f.conj.baseFlavor = f.baseFlavor := by
  cases f <;> rfl

/-- Every nucleon-sheet flavor belongs to the generation-1 light doublet
    `{up, down}`. -/
theorem baseFlavor_mem_light_doublet (f : LightSignedFlavor) :
    f.baseFlavor = .up ∨ f.baseFlavor = .down := by
  cases f <;> decide

/-- No nucleon-sheet flavor is the charm quark `QuarkSixFlavor.charm`. -/
theorem baseFlavor_ne_charm (f : LightSignedFlavor) :
    f.baseFlavor ≠ .charm := by
  cases f <;> decide

/-- More generally, nucleon-sheet flavors are disjoint from all four heavy
    quark flavors `(s, c, b, t)`. -/
theorem baseFlavor_disjoint_heavy (f : LightSignedFlavor) :
    f.baseFlavor ≠ .strange ∧
    f.baseFlavor ≠ .charm ∧
    f.baseFlavor ≠ .bottom ∧
    f.baseFlavor ≠ .top := by
  cases f <;> decide

/-! ## 2. Nucleon color-sheet triples, `C`-invariance, and zero charm projection -/

/-- A nucleon's 3-strand color-sheet flavor content `(r, g, b)`. -/
abbrev NucleonSheetTriple :=
  LightSignedFlavor × LightSignedFlavor × LightSignedFlavor

/-- Proton `(u, u, d)`, neutron `(u, d, d)`, antiproton `(ū, ū, d̄)`, and
    antineutron `(ū, d̄, d̄)`. -/
def protonTriple : NucleonSheetTriple := (.u, .u, .d)
def neutronTriple : NucleonSheetTriple := (.u, .d, .d)
def antiprotonTriple : NucleonSheetTriple := (.ubar, .ubar, .dbar)
def antineutronTriple : NucleonSheetTriple := (.ubar, .dbar, .dbar)

/-- Flavor carried by a nucleon triple `F` on color sheet `c`. -/
def NucleonSheetTriple.flavorAt : NucleonSheetTriple → ColorSheet → LightSignedFlavor
  | (f, _, _), .r => f
  | (_, f, _), .g => f
  | (_, _, f), .b => f

/-- Discrete charge conjugation `C` applied across all three color sheets. -/
def NucleonSheetTriple.conj : NucleonSheetTriple → NucleonSheetTriple
  | (f₁, f₂, f₃) => (f₁.conj, f₂.conj, f₃.conj)

/-- `C` maps proton ↔ antiproton and neutron ↔ antineutron, and satisfies
    `C² = id` on every 3-sheet triple. -/
theorem NucleonSheetTriple.conj_involutive (F : NucleonSheetTriple) :
    F.conj.conj = F := by
  obtain ⟨f₁, f₂, f₃⟩ := F
  simp [NucleonSheetTriple.conj, LightSignedFlavor.conj_involutive]

/-- `C` commutes with reading off the flavor at a color sheet `c`. -/
theorem NucleonSheetTriple.flavorAt_conj (F : NucleonSheetTriple) (c : ColorSheet) :
    F.conj.flavorAt c = (F.flavorAt c).conj := by
  obtain ⟨f₁, f₂, f₃⟩ := F
  cases c <;> rfl

/-- Sheet-level chirality sign rule on two signed light flavors. -/
def flavorPairSign (f₁ f₂ : LightSignedFlavor) : Int :=
  if f₁ = f₂ then 1
  else if f₁ = f₂.conj then -1
  else 0

/-- `flavorPairSign` is invariant under simultaneous charge conjugation `C`
    (16-cell check). -/
theorem flavorPairSign_conj_invariant (f₁ f₂ : LightSignedFlavor) :
    flavorPairSign f₁.conj f₂.conj = flavorPairSign f₁ f₂ := by
  cases f₁ <;> cases f₂ <;> rfl

/-- Chirality sign `ε(c₁, c₂, F₁, F₂) ∈ {+1, -1, 0}` of a color-sheet contact
    (`conj:inter-nucleon-channel-color-tube`). -/
def chiralitySign (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonSheetTriple) : Int :=
  flavorPairSign (F₁.flavorAt c₁) (F₂.flavorAt c₂)

/-- **The chirality sign `ε` commutes with discrete charge conjugation `C`
    across all color-sheet pairs and nucleon triples.** -/
theorem chiralitySign_conj_invariant (c₁ c₂ : ColorSheet)
    (F₁ F₂ : NucleonSheetTriple) :
    chiralitySign c₁ c₂ F₁.conj F₂.conj = chiralitySign c₁ c₂ F₁ F₂ := by
  unfold chiralitySign
  rw [NucleonSheetTriple.flavorAt_conj, NucleonSheetTriple.flavorAt_conj]
  exact flavorPairSign_conj_invariant (F₁.flavorAt c₁) (F₂.flavorAt c₂)

/-- Base flavors `(r, g, b)` of a nucleon color-sheet triple. -/
def NucleonSheetTriple.sheetBaseFlavors (F : NucleonSheetTriple) :
    List QuarkSixFlavor :=
  ColorSheet.allList.map (fun c => (F.flavorAt c).baseFlavor)

/-- Number of color sheets in `F` carrying `QuarkSixFlavor.charm`. -/
def NucleonSheetTriple.charmCount (F : NucleonSheetTriple) : Nat :=
  (F.sheetBaseFlavors.filter (fun fl => decide (fl = .charm))).length

/-- **Zero charm occupation on every nucleon/antinucleon color-sheet triple.** -/
theorem NucleonSheetTriple.charmCount_eq_zero (F : NucleonSheetTriple) :
    F.charmCount = 0 := by
  obtain ⟨f₁, f₂, f₃⟩ := F
  cases f₁ <;> cases f₂ <;> cases f₃ <;> rfl

/-- Indicator (`1` or `0`) for whether a color-sheet contact `(c₁, c₂)` between
    nucleons `F₁, F₂` involves `QuarkSixFlavor.charm` on either strand. -/
def charmContactIndicator (c₁ c₂ : ColorSheet)
    (F₁ F₂ : NucleonSheetTriple) : Int :=
  if (F₁.flavorAt c₁).baseFlavor = .charm ∨
     (F₂.flavorAt c₂).baseFlavor = .charm then 1 else 0

/-- Every color-sheet contact `(c₁, c₂)` between two nucleon triples has zero
    charm indicator. -/
theorem charmContactIndicator_eq_zero (c₁ c₂ : ColorSheet)
    (F₁ F₂ : NucleonSheetTriple) :
    charmContactIndicator c₁ c₂ F₁ F₂ = 0 := by
  unfold charmContactIndicator
  have h₁ : (F₁.flavorAt c₁).baseFlavor ≠ .charm :=
    baseFlavor_ne_charm (F₁.flavorAt c₁)
  have h₂ : (F₂.flavorAt c₂).baseFlavor ≠ .charm :=
    baseFlavor_ne_charm (F₂.flavorAt c₂)
  simp [h₁, h₂]

/-- **Zero charm projection on the 9-pair inter-nucleon color-tube sum.** -/
theorem charm_projected_color_tube_sum_eq_zero
    (F₁ F₂ : NucleonSheetTriple) :
    (colorPairs.map (fun p => charmContactIndicator p.1 p.2 F₁ F₂)).sum = 0 := by
  simp [charmContactIndicator_eq_zero, colorPairs]

/-! ## 3. Division-free Hecke & Markov identities of the color-averaged additive term -/

/-- **Division-free color-averaged Hecke generator identity (§7c).**
    When `σ_inv = σ - h` (the Hecke quadratic skein relation `σ² = h·σ + 1`
    multiplied by `σ⁻¹`), the bar-symmetric sum of the positive and negative
    braid generators satisfies `σ + σ_inv = 2·σ - h` (i.e. `σ_avg = σ - h/2`). -/
theorem hecke_color_average_division_free (σ σ_inv h : Int)
    (h_skein : σ_inv = σ - h) :
    σ + σ_inv = 2 * σ - h := by
  omega

/-- **Division-free Markov trace factor identity (§7c).**
    With positive-crossing Markov factor `f_pp = z` and negative-crossing Markov
    factor `f_nn = z - h`, their sum is `2·z - h` (so the flavor-blind
    color-averaged interface factor is `z - h/2`). -/
theorem markov_color_average_division_free (z h : Int) :
    z + (z - h) = 2 * z - h := by
  omega

/-- **Subleading Bring color-tube p-n interface factor decomposition.**
    The division-free `4×` scaled Bring color-tube factor `4·z - 2·h + h·δ`
    splits into the flavor-blind color average `2·(2·z - h)` plus the light
    `(u, d)` flavor-split shift `h·δ`. -/
theorem bring_color_tube_pn_factor_split (z h δ : Int) :
    4 * z - 2 * h + h * δ = 2 * (2 * z - h) + h * δ := by
  omega

/-! ## 4. Capstone classification theorem (`qou-q6lw`) -/

/-- **Capstone (`qou-q6lw`): Color-sheet additive channel vs `C` charge
    conjugation vs `QuarkSixFlavor.charm`.**
    Certifies simultaneously that:
    1. The inter-nucleon channel acts on the `3 × 3 = 9` color-sheet pairs
       spanning `T₁ ⊗ T₁` (`colorPairs.length = 9` and
       `t1TensorSummandDims.sum = 9`);
    2. `C` in `conj:c-from-color-flavor-swap` is an involution preserving the
       base flavor on every sheet and leaving `ε(c₁, c₂, F₁, F₂)` invariant;
    3. `QuarkSixFlavor.charm` has zero occupation on every nucleon/antinucleon
       color-sheet triple (`F.charmCount = 0`) and zero contact indicator across
       every color-sheet pair (`charmContactIndicator c₁ c₂ F₁ F₂ = 0`). -/
theorem color_vs_charm_additive_sector_summary
    (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonSheetTriple) :
    (colorPairs.length = 9 ∧ t1TensorSummandDims.sum = 9) ∧
    (F₁.conj.conj = F₁ ∧
      (F₁.conj.flavorAt c₁).baseFlavor = (F₁.flavorAt c₁).baseFlavor ∧
      chiralitySign c₁ c₂ F₁.conj F₂.conj = chiralitySign c₁ c₂ F₁ F₂) ∧
    (F₁.charmCount = 0 ∧ F₂.charmCount = 0 ∧
      charmContactIndicator c₁ c₂ F₁ F₂ = 0) := by
  refine ⟨⟨rfl, rfl⟩, ?_, ?_⟩
  · refine ⟨NucleonSheetTriple.conj_involutive F₁, ?_,
      chiralitySign_conj_invariant c₁ c₂ F₁ F₂⟩
    rw [NucleonSheetTriple.flavorAt_conj]
    exact baseFlavor_conj_invariant (F₁.flavorAt c₁)
  · exact ⟨NucleonSheetTriple.charmCount_eq_zero F₁,
      NucleonSheetTriple.charmCount_eq_zero F₂,
      charmContactIndicator_eq_zero c₁ c₂ F₁ F₂⟩

end QOU.StandardModel.ColorVsCharmAdditiveSector
