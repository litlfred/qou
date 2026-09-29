import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Tactic.Linarith

/-!
# QOU.StandardModel.ColourStabilizerAction — the colour-action conjecture

Library home of the conjecture class for `conj:sm-colour-stabilizer-action`
(appendix "Toward the Standard Model"). The class is stated over an abstract
colour-algebra slot `g`; the intended instantiation is the corpus's octonion
stabilizer `su3 e` (`QOU.MathlibExt.OctonionSU3Stabilizer`, `finrank = 8`
gate). The concrete specialisation and the bracket closure of the stabilizer
live in `QOU.MathlibExt.OctonionSU3BracketClosure`, which imports this file.

Per §3b-tax this is a **primary conjecture**: a content-bearing class with
**no instance** — providing an instance for the intended instantiation is the
open derivation. The two theorems below are proved unconditionally:
the dimension obstruction `finrank g ≤ (finrank V)²`, and its colour
instantiation — an 8-dimensional colour algebra needs `finrank V ≥ 3`
(three strands are the minimal faithful colour host).

Base ring ℚ throughout (the colour algebra and state space are exact
rational objects on the substrate side of the wall; nothing archimedean).
-/

namespace QOU.StandardModel

open Module

/-- **Conjecture (colour stabilizer action).** The colour algebra `g`
(intended: the octonion stabilizer `su3 e`, 8-dimensional by the
corpus gate) acts faithfully and linearly on the state space `V`
(intended: the 3-strand state space): there is an injective linear
map `g →ₗ End(V)`. Bracket compatibility is the obvious
strengthening; it is deliberately not required here — bracket
*closure* of the concrete stabilizer is proved
(`QOU.MathlibExt.OctonionSU3BracketClosure.bracketDer_mem_su3`), but
requiring `Φ` to intertwine brackets would strengthen the conjecture
beyond what the appendix's gap ledger records as the minimal missing
ingredient. No instance is provided for the intended instantiation —
providing one is the open derivation. -/
class ColourStabilizerAction (g : Type*) [AddCommGroup g] [Module ℚ g]
    (V : Type*) [AddCommGroup V] [Module ℚ V] : Prop where
  /-- The colour algebra embeds linearly in the endomorphisms of `V`. -/
  faithful_linear_action : ∃ Φ : g →ₗ[ℚ] Module.End ℚ V, Function.Injective Φ

/-- **Dimension obstruction** (proved): a faithful linear action
forces `finrank g ≤ (finrank V)²`. -/
theorem not_colourStabilizerAction_of_dim_sq_lt
    (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g]
    (V : Type*) [AddCommGroup V] [Module ℚ V] [FiniteDimensional ℚ V]
    (h : finrank ℚ V * finrank ℚ V < finrank ℚ g) :
    ¬ColourStabilizerAction g V := by
  rintro ⟨Φ, hΦ⟩
  have hle : finrank ℚ g ≤ finrank ℚ (V →ₗ[ℚ] V) :=
    LinearMap.finrank_le_finrank_of_injective hΦ
  have hEnd : finrank ℚ (V →ₗ[ℚ] V) = finrank ℚ V * finrank ℚ V :=
    Module.finrank_linearMap ℚ ℚ V V
  omega

/-- **Three strands are the minimal colour host** (proved): an
8-dimensional colour algebra — the dimension of the octonion
stabilizer under the corpus's `finrank su3 = 8` gate — admits no
faithful linear action on a state space of dimension ≤ 2, since
`2² = 4 < 8 ≤ 3² = 9`. The framework's choice of a 3-strand state
space is thus the smallest one on which colour can act faithfully. -/
theorem colour_needs_three_strands
    (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g]
    (h8 : finrank ℚ g = 8)
    (V : Type*) [AddCommGroup V] [Module ℚ V] [FiniteDimensional ℚ V]
    (hV : finrank ℚ V ≤ 2) :
    ¬ColourStabilizerAction g V := by
  apply not_colourStabilizerAction_of_dim_sq_lt
  nlinarith

end QOU.StandardModel
