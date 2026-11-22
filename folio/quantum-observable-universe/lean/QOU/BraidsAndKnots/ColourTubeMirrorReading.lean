import QOU.BraidsAndKnots.InterNucleonChannelColorTube

/-!
# Which contacts get `σ⁻¹` under the colour-tube sign rule

Bean `qou-hlxt` asks whether the letter flip `σ ↦ σ⁻¹` reads as the antiparticle
(`rem:breit-wheeler-vertex`) or as the `u → d` flavour flip (stream 6a,
`quarkLetter`). This file records what the colour-tube sign rule
`chiralitySign` of `conj:inter-nucleon-channel-color-tube` already says. It
chooses no reading.

* Between two matter flavours (`u` or `d`), the sign is never `-1`. So two
  nucleons never exchange a `σ⁻¹` under this rule.
* Between two matter flavours, the sign is `0` (the averaged crossing) exactly
  when the flavours differ. A `u`–`d` contact therefore gets the averaged
  crossing, not `σ⁻¹`.
* The sign is `-1` exactly at a matter–antimatter contact (`f` against `f̄`).

So inside this one block, `σ⁻¹` is the antiparticle contact, matching the
Breit–Wheeler reading, and flavour difference is carried by the averaged
crossing. The rule itself is stated data of the upstream conjecture (its open
question 2), so this is a consistency statement about the corpus, not a
derivation of either reading.

-- Ref: [leitner2026] conj:inter-nucleon-channel-color-tube
-/

namespace QOU.BraidsAndKnots

/-- A matter flavour: `u` or `d`. -/
def QuarkFlavor.IsMatter : QuarkFlavor → Prop
  | .u => True
  | .d => True
  | _ => False

instance (f : QuarkFlavor) : Decidable f.IsMatter := by
  cases f <;> unfold QuarkFlavor.IsMatter <;> infer_instance

/-- The sheet-level sign rule, as used inside `chiralitySign`. -/
def sheetSign (f₁ f₂ : QuarkFlavor) : ℤ :=
  if f₁ = f₂ then 1 else if f₁ = f₂.conj then -1 else 0

theorem chiralitySign_eq_sheetSign (c₁ c₂ : ColorSheet) (F₁ F₂ : NucleonColorContent) :
    chiralitySign c₁ c₂ F₁ F₂ = sheetSign (F₁.flavorAt c₁) (F₂.flavorAt c₂) := rfl

/-- Two matter flavours never get the inverse crossing. -/
theorem sheetSign_ne_neg_one_of_matter {f₁ f₂ : QuarkFlavor}
    (h₁ : f₁.IsMatter) (h₂ : f₂.IsMatter) : sheetSign f₁ f₂ ≠ -1 := by
  cases f₁ <;> cases f₂ <;> simp_all [QuarkFlavor.IsMatter, sheetSign, QuarkFlavor.conj]

/-- Between matter flavours, the averaged crossing (sign `0`) occurs exactly
    when the flavours differ: a `u`–`d` contact. -/
theorem sheetSign_eq_zero_iff_of_matter {f₁ f₂ : QuarkFlavor}
    (h₁ : f₁.IsMatter) (h₂ : f₂.IsMatter) : sheetSign f₁ f₂ = 0 ↔ f₁ ≠ f₂ := by
  cases f₁ <;> cases f₂ <;> simp_all [QuarkFlavor.IsMatter, sheetSign, QuarkFlavor.conj]

/-- The inverse crossing (sign `-1`) occurs exactly at a flavour–antiflavour
    contact. -/
theorem sheetSign_eq_neg_one_iff (f₁ f₂ : QuarkFlavor) :
    sheetSign f₁ f₂ = -1 ↔ f₁ = f₂.conj := by
  cases f₁ <;> cases f₂ <;> simp [sheetSign, QuarkFlavor.conj]

/-- Proton and neutron contacts never carry `σ⁻¹` under the colour-tube rule. -/
theorem chiralitySign_ne_neg_one_nucleons (c₁ c₂ : ColorSheet)
    {F₁ F₂ : NucleonColorContent} (hF₁ : F₁ = proton ∨ F₁ = neutron)
    (hF₂ : F₂ = proton ∨ F₂ = neutron) :
    chiralitySign c₁ c₂ F₁ F₂ ≠ -1 := by
  rw [chiralitySign_eq_sheetSign]
  apply sheetSign_ne_neg_one_of_matter <;>
  · rcases hF₁ with rfl | rfl <;> rcases hF₂ with rfl | rfl <;>
      cases c₁ <;> cases c₂ <;> exact trivial

end QOU.BraidsAndKnots
