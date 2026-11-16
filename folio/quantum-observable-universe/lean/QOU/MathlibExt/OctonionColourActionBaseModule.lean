import QOU.MathlibExt.OctonionSU3BracketClosure

set_option maxHeartbeats 4000000
set_option maxSynthPendingDepth 5

/-!
# QOU.MathlibExt.OctonionColourActionBaseModule — the octonion base-module
instance, and what it does NOT close

The Dubois-Violette–Todorov base module (`dubois-violette-todorov2018`
Sec. 2): at a fixed imaginary unit `e` the octonions split `𝕆 = ℂ ⊕ ℂ³`
and the colour stabilizer acts on `𝕆` itself — the `1 ⊕ 3` colour
decomposition. In the corpus this action is *tautological*: `su3 e` is by
construction a submodule of `Der𝕆 ⊆ End(𝕆)`, so the double subtype
inclusion is already an injective ℚ-linear map `su3 e →ₗ End(𝕆)`.

Proved here, sorry-free:

* `su3ToEndOct` / `su3ToEndOct_injective` — the inclusion and its
  injectivity;
* `instance : ColourStabilizerAction ↥(su3 e) (Fin 8 → ℚ)` — the
  abstract conjecture class of `conj:sm-colour-stabilizer-action` is
  **satisfied** by the octonion base module, for every `e`;
* `colourStabilizerActionOnSU3_octonions` — the concrete wiring
  `ColourStabilizerActionOnSU3 e (Fin 8 → ℚ)` holds.

**Calibration finding (the honest point of this file).** The abstract
class `ColourStabilizerAction g V` quantifies over an arbitrary state
space `V`, so exhibiting *some* faithful module — here the octonions
themselves — closes the class without touching the physics. The open
content of `conj:sm-colour-stabilizer-action` is therefore NOT "does a
faithful `su3 e`-module exist" (it does, trivially) but whether the
**framework's own Hecke three-strand state space** carries such an
action compatibly with its braid structure. The conjecture block's
narrative is sharpened accordingly; the class stays as the abstract
interface, this instance documents exactly how far the tautology
reaches, and the remaining gap (bean `qou-ni4b`) is the Hecke-side
instantiation. Consistency with `colour_needs_three_strands`: the
octonion module has `dim_ℚ = 8`, comfortably above the proved minimum
of 3, and `8 ≤ 8²` clears the dimension obstruction — but the
*three-strand Hecke state space* the framework intends is a different
module, and no instance is claimed for it here.

Base ring ℚ; nothing archimedean.
-/

namespace QOU.MathlibExt.OctonionDerivations

open QOU.StandardModel

/-- The double subtype inclusion `su3 e ⊆ Der𝕆 ⊆ End(𝕆)` as a ℚ-linear
map into the endomorphisms of the octonions. -/
def su3ToEndOct (e : Fin 8 → ℚ) :
    ↥(su3 e) →ₗ[ℚ] Module.End ℚ (Fin 8 → ℚ) where
  toFun D := (D.1 : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ))
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem su3ToEndOct_injective (e : Fin 8 → ℚ) :
    Function.Injective (su3ToEndOct e) := by
  intro D₁ D₂ h
  exact Subtype.ext (Subtype.ext h)

/-- **The octonion base module realizes the abstract colour-action
class** (DV–Todorov `1 ⊕ 3`): `su3 e` acts faithfully on `𝕆` by its
defining inclusion. This is the tautological instance — see the module
docstring for what it does and does not close. -/
instance (e : Fin 8 → ℚ) : ColourStabilizerAction ↥(su3 e) (Fin 8 → ℚ) :=
  ⟨⟨su3ToEndOct e, su3ToEndOct_injective e⟩⟩

/-- The concrete wiring holds for the octonion base module. -/
-- Ref: [dubois-violette-todorov2018] §2 (octonion base module 𝕆 = ℂ ⊕ ℂ³ for the colour stabilizer su(3))
theorem colourStabilizerActionOnSU3_octonions (e : Fin 8 → ℚ) :
    ColourStabilizerActionOnSU3 e (Fin 8 → ℚ) :=
  inferInstance

end QOU.MathlibExt.OctonionDerivations
