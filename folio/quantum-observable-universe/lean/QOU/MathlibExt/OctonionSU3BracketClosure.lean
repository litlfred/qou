import QOU.MathlibExt.OctonionSU3Stabilizer
import QOU.StandardModel.ColourStabilizerAction

set_option maxHeartbeats 4000000
-- `su3 e ⊂ Der𝕆 ⊂ End` is a doubly-nested submodule: synthesizing
-- `AddCommGroup ↥(su3 e)` needs `AddCommGroup ↥Der𝕆` *during unification*,
-- which the default `maxSynthPendingDepth := 1` forbids. Raising it is the
-- fix; the two explicit instance registrations below then spare every
-- downstream importer from needing this option.
set_option maxSynthPendingDepth 5

/-!
# QOU.MathlibExt.OctonionSU3BracketClosure — `su3 e` is a Lie subalgebra

Two wirings for the colour stabilizer `su3 e = ker (evOct e) ⊂ Der𝕆`:

1. **Bracket closure** (bean `qou-51st`): the commutator of two derivations
   is a derivation (`bracket_mem_ker_leibnizDefect`, generic over any
   bilinear multiplication), and the commutator of two derivations killing
   `e` kills `e` (`bracketDer_mem_su3`) — so `su3 e` is closed under the
   commutator bracket inside `Der𝕆 = 𝔤₂`, i.e. a Lie subalgebra. Both are
   short structural proofs: the first is the classical cross-term
   cancellation, the second is `D₁ (D₂ e) − D₂ (D₁ e) = D₁ 0 − D₂ 0 = 0`.

2. **Concrete conjecture wiring** (bean `qou-iibg`): the appendix
   conjecture class `ColourStabilizerAction` specialised to the corpus's
   concrete stabilizer, `ColourStabilizerActionOnSU3 e V`. This is a
   *statement-level* wiring only — **no instance is provided**; producing
   one is the open derivation (`conj:sm-colour-stabilizer-action`). The
   specialisation makes the open problem precise on the corpus's own
   objects instead of an abstract colour-algebra slot.

Base ring ℚ; exact rational linear algebra, nothing archimedean.
-/

namespace QOU.MathlibExt.OctonionDerivations

open DerivationRankNullity

section Generic

variable {K : Type*} [Field K] {V : Type*} [AddCommGroup V] [Module K V]

/-- **Derivations are closed under the commutator** (generic): for any
bilinear multiplication `m`, if `D₁, D₂` satisfy the Leibniz rule then so
does `D₁ ∘ D₂ − D₂ ∘ D₁` — the second-order cross terms cancel. -/
theorem bracket_mem_ker_leibnizDefect {m : V →ₗ[K] V →ₗ[K] V}
    {D₁ D₂ : V →ₗ[K] V}
    (h₁ : D₁ ∈ LinearMap.ker (leibnizDefect m))
    (h₂ : D₂ ∈ LinearMap.ker (leibnizDefect m)) :
    D₁ ∘ₗ D₂ - D₂ ∘ₗ D₁ ∈ LinearMap.ker (leibnizDefect m) := by
  rw [mem_ker_leibnizDefect_iff] at h₁ h₂ ⊢
  intro x y
  simp only [LinearMap.sub_apply, LinearMap.comp_apply, h₁, h₂, map_add,
    map_sub]
  abel

end Generic

/-- `Der𝕆` is closed under the commutator bracket. -/
theorem bracket_mem_Der𝕆 {D₁ D₂ : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)}
    (h₁ : D₁ ∈ Der𝕆) (h₂ : D₂ ∈ Der𝕆) :
    D₁ ∘ₗ D₂ - D₂ ∘ₗ D₁ ∈ Der𝕆 :=
  bracket_mem_ker_leibnizDefect h₁ h₂

/-- The commutator bracket on the derivation algebra `Der𝕆 = 𝔤₂`. -/
def bracketDer (D₁ D₂ : Der𝕆) : Der𝕆 :=
  ⟨D₁.1 ∘ₗ D₂.1 - D₂.1 ∘ₗ D₁.1, bracket_mem_Der𝕆 D₁.2 D₂.2⟩

@[simp] theorem bracketDer_coe (D₁ D₂ : Der𝕆) :
    (bracketDer D₁ D₂ : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ))
      = D₁.1 ∘ₗ D₂.1 - D₂.1 ∘ₗ D₁.1 := rfl

/-- **Bracket closure of the colour stabilizer** (bean `qou-51st`): if `D₁`
and `D₂` both kill `e` then so does their commutator —
`[D₁,D₂] e = D₁ (D₂ e) − D₂ (D₁ e) = D₁ 0 − D₂ 0 = 0`. Together with
`bracket_mem_Der𝕆` this exhibits `su3 e` as a Lie subalgebra of
`Der(𝕆) = 𝔤₂`, as the Günaydin–Gürsey colour picture requires. -/
theorem bracketDer_mem_su3 {e : Fin 8 → ℚ} {D₁ D₂ : Der𝕆}
    (h₁ : D₁ ∈ su3 e) (h₂ : D₂ ∈ su3 e) :
    bracketDer D₁ D₂ ∈ su3 e := by
  rw [mem_su3_iff] at h₁ h₂ ⊢
  simp [bracketDer, LinearMap.sub_apply, LinearMap.comp_apply, h₁, h₂]

/-- The standard `AddCommGroup` structure on the stabilizer subtype,
registered with a direct head key so importers resolve it at the default
`maxSynthPendingDepth` (see the option comment at the top of this file). -/
instance instAddCommGroupSU3 (e : Fin 8 → ℚ) : AddCommGroup ↥(su3 e) :=
  Submodule.addCommGroup (su3 e)

/-- Companion `Module` registration, for the same nesting reason. -/
instance instModuleSU3 (e : Fin 8 → ℚ) : Module ℚ ↥(su3 e) :=
  Submodule.module (su3 e)

/-- **The concrete colour-action conjecture** (bean `qou-iibg`): the
appendix class `ColourStabilizerAction` specialised to the corpus's
octonion stabilizer `su3 e`. **No instance is provided** — producing one
(a faithful linear action of `su3 e` on the 3-strand state space) is the
open derivation recorded by `conj:sm-colour-stabilizer-action`; by
`colour_needs_three_strands` any host `V` must have `finrank ℚ V ≥ 3`
whenever `finrank ℚ (su3 e) = 8`. -/
abbrev ColourStabilizerActionOnSU3 (e : Fin 8 → ℚ)
    (V : Type*) [AddCommGroup V] [Module ℚ V] : Prop :=
  QOU.StandardModel.ColourStabilizerAction (su3 e) V

end QOU.MathlibExt.OctonionDerivations
