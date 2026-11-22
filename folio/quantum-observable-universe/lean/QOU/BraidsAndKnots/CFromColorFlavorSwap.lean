import QOU.BraidsAndKnots.InterNucleonChannelColorTube

/-!
# QOU.BraidsAndKnots.CFromColorFlavorSwap — D6 charge conjugation as color-sheet flavor swap

§3b-cond class axiomatisation for content block
`conj:c-from-color-flavor-swap` (D6 charge-conjugation closure), replacing
the former sibling stub's vacuous `holds : Prop` placeholder.

**Honest split — proved vs conjectural.**  The block's three claims separate
cleanly:

1. **C is an involution** — PROVED sorry-free below
   (`NucleonColorContent.conj_involutive`; proton ↦ antiproton,
   neutron ↦ antineutron by `rfl`).
2. **C commutes with the chirality sign ε** — PROVED sorry-free below
   (`chiralitySign_conj_invariant`): the ε rule of
   `conj:inter-nucleon-channel-color-tube` is flavor-conjugation invariant
   because `conj` is an involution (match ↦ match, conjugate-pair ↦
   conjugate-pair).
3. **C commutes with the weight tensor W** — the genuinely CONJECTURAL
   content, carried as the class field `weight_conj_invariant` of
   `CFromColorFlavorSwap` (sorry = conjecture per AGENTS.md §3b; no global
   instance is provided).  It cannot be derived today because the closed
   form of `W` is itself open (open question 1 of the upstream block).

Given (3), the refined generator data `(W, ε)` per color pair — and hence
the color-weighted generator `σ^(F₁,F₂) = Σ W σ^ε` and its scalar shadow
`Σ W·ε` — is C-invariant: `refined_generator_data_conj_invariant` and
`signedWeightSum_conj_invariant` DERIVE this by composing the class field
with the proved ε-invariance (a genuine derivation, not a projection).

**Not yet statable:** the CPT factorisation field
(`bar_involution = C ∘ P ∘ T`) awaits the D7/D8 carriers
(`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`), which do not
exist yet; it is deliberately omitted rather than encoded as a bare `Prop`.

Numeric cross-check at q₀: `computations/verify_c_color_swap.py`.

-- Ref: [leitner2026] conj:c-from-color-flavor-swap
-/

namespace QOU.BraidsAndKnots

/-! ## The C-action on nucleon color content -/

/-- Charge conjugation on a nucleon's color-sheet content: flavor
    conjugation `u ↔ ū`, `d ↔ d̄` applied independently on each of the three
    color sheets. -/
def NucleonColorContent.conj : NucleonColorContent → NucleonColorContent
  | (f₁, f₂, f₃) => (f₁.conj, f₂.conj, f₃.conj)

/-- Antiproton color content (ū, ū, d̄). -/
def antiproton : NucleonColorContent :=
  (QuarkFlavor.ubar, QuarkFlavor.ubar, QuarkFlavor.dbar)

/-- Antineutron color content (ū, d̄, d̄). -/
def antineutron : NucleonColorContent :=
  (QuarkFlavor.ubar, QuarkFlavor.dbar, QuarkFlavor.dbar)

/-- C maps the proton to the antiproton and the neutron to the antineutron. -/
theorem conj_proton_neutron :
    proton.conj = antiproton ∧ neutron.conj = antineutron :=
  ⟨rfl, rfl⟩

/-- **C² = id** on nucleon color content (the involution claim, proved). -/
theorem NucleonColorContent.conj_involutive (F : NucleonColorContent) :
    F.conj.conj = F := by
  obtain ⟨f₁, f₂, f₃⟩ := F
  simp [NucleonColorContent.conj, QuarkFlavor.conj_involutive]

/-- Conjugation commutes with reading off the flavor at a sheet. -/
theorem NucleonColorContent.flavorAt_conj (F : NucleonColorContent)
    (c : ColorSheet) : F.conj.flavorAt c = (F.flavorAt c).conj := by
  obtain ⟨f₁, f₂, f₃⟩ := F
  cases c <;> rfl

/-! ## ε is C-invariant (proved, not conjectural) -/

/-- Sheet-level sign invariance: the (match / conjugate-pair / mixed)
    trichotomy is stable under conjugating both flavors, because `conj` is an
    involution. -/
private theorem conj_sign_eq (f₁ f₂ : QuarkFlavor) :
    ((if f₁.conj = f₂.conj then (1 : ℤ)
      else if f₁.conj = f₂.conj.conj then -1 else 0)
      = if f₁ = f₂ then 1 else if f₁ = f₂.conj then -1 else 0) := by
  cases f₁ <;> cases f₂ <;> rfl

/-- **The chirality sign ε commutes with C** (claim 2 of the block, proved
    sorry-free): `ε(c₁, c₂, F̄₁, F̄₂) = ε(c₁, c₂, F₁, F₂)`. -/
theorem chiralitySign_conj_invariant (c₁ c₂ : ColorSheet)
    (F₁ F₂ : NucleonColorContent) :
    chiralitySign c₁ c₂ F₁.conj F₂.conj = chiralitySign c₁ c₂ F₁ F₂ := by
  unfold chiralitySign
  rw [NucleonColorContent.flavorAt_conj, NucleonColorContent.flavorAt_conj]
  exact conj_sign_eq (F₁.flavorAt c₁) (F₂.flavorAt c₂)

/-! ## The §3b-cond class: W is C-invariant (the conjectural content) -/

/-- **CONJECTURE (§3b-cond class).**  D6 charge conjugation commutes with the
    color-tube weight tensor: `W_{c₁c₂}(F̄₁, F̄₂) = W_{c₁c₂}(F₁, F₂)` (the
    weights are flavor-conjugation invariant).  This is claim 1 of
    `conj:c-from-color-flavor-swap`'s "conjectural content" list; it is the
    only claim that cannot be derived today, because the closed form of `W`
    is itself open.  Conditional on the upstream channel-assignment class;
    no global instance is provided. -/
-- Ref: [leitner2026] conj:c-from-color-flavor-swap
class CFromColorFlavorSwap [BringFiberAction] [InterNucleonChannelColorTube] where
  /-- The weight tensor is flavor-conjugation invariant. -/
  weight_conj_invariant : ∀ (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonColorContent),
    InterNucleonChannelColorTube.weight c₁ c₂ F₁.conj F₂.conj
      = InterNucleonChannelColorTube.weight c₁ c₂ F₁ F₂

/-! ## Derived: the refined generator is C-invariant -/

/-- **The refined generator data is C-invariant** (derived, conditional): for
    every color pair, both the weight and the chirality exponent are unchanged
    by conjugating the flavor content.  Since the color-weighted generator
    `σ^(F₁,F₂) = Σ_{c₁c₂} W_{c₁c₂}(F₁,F₂) · σ^{ε(c₁,c₂,F₁,F₂)}` depends on
    `(F₁, F₂)` only through the per-pair data `(W, ε)`, this is exactly the
    statement that C leaves the canonical Hecke generator of every
    inter-nucleon arc invariant.  Derivation: class field (weights) composed
    with the proved `chiralitySign_conj_invariant` (exponents). -/
theorem refined_generator_data_conj_invariant
    [BringFiberAction] [InterNucleonChannelColorTube] [CFromColorFlavorSwap]
    (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonColorContent) :
    (InterNucleonChannelColorTube.weight c₁ c₂ F₁.conj F₂.conj,
      chiralitySign c₁ c₂ F₁.conj F₂.conj)
      = (InterNucleonChannelColorTube.weight c₁ c₂ F₁ F₂,
          chiralitySign c₁ c₂ F₁ F₂) := by
  rw [CFromColorFlavorSwap.weight_conj_invariant, chiralitySign_conj_invariant]

/-- The scalar shadow of the refined generator: the signed weighted sum
    `Σ_{c₁c₂} W_{c₁c₂}(F₁,F₂) · ε(c₁,c₂,F₁,F₂)` over the 9 color pairs. -/
def signedWeightSum [BringFiberAction] [InterNucleonChannelColorTube]
    (F₁ F₂ : NucleonColorContent) : ℚ :=
  (colorPairs.map (fun p =>
    InterNucleonChannelColorTube.weight p.1 p.2 F₁ F₂
      * (chiralitySign p.1 p.2 F₁ F₂ : ℚ))).sum

/-- **The signed weighted sum is C-invariant** (derived, conditional):
    `Σ W·ε` is unchanged by flavor conjugation — the scalar face of the
    generator invariance, numerically cross-checked at q₀ by
    `computations/verify_c_color_swap.py`. -/
theorem signedWeightSum_conj_invariant
    [BringFiberAction] [InterNucleonChannelColorTube] [CFromColorFlavorSwap]
    (F₁ F₂ : NucleonColorContent) :
    signedWeightSum F₁.conj F₂.conj = signedWeightSum F₁ F₂ := by
  unfold signedWeightSum
  simp only [CFromColorFlavorSwap.weight_conj_invariant,
    chiralitySign_conj_invariant]

end QOU.BraidsAndKnots
