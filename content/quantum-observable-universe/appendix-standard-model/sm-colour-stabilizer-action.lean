import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Tactic.Linarith

/-!
# Conjecture: colour stabilizer action on the state space

The corpus realises the colour Lie algebra as the stabilizer
`su3 e := ker (evOct e) ⊂ Der(𝕆)` of a unit imaginary octonion
(`QOU.MathlibExt.OctonionSU3Stabilizer`, with the proved rank–nullity
gate `finrank su3 = 8 ⟺ rank(ev_e) = 6`). What is missing for the
Standard-Model truncation is the *action*: no construction makes that
stabilizer act on the framework's 3-strand state space. This file is
the formalize-first artifact for that gap (bean `qou-ni4b`).

The conjecture class is stated over an abstract colour-algebra slot
`g` rather than importing `su3 e` directly: the intended
instantiation is `g = su3 e`, and wiring the class to that concrete
type is a recorded follow-up (the import pulls the octonion
`decide`-heavy dependency cone; see the bean). The class is
content-bearing — a faithful linear action — and **no instance is
provided**; the open state is a class with no instance. This is a
**primary conjecture** (AGENTS.md §3b-tax).

What IS proved here, sorry-free: the dimension obstruction. A
faithful linear action of `g` on `V` forces
`finrank g ≤ (finrank V)²`; hence an 8-dimensional colour algebra
admits no faithful action on a state space of dimension ≤ 2, and
dimension 3 — the framework's 3-strand space — is the minimal
faithful host. This is a structural (b)-grade exclusion with the
invariant cited: rank of the endomorphism algebra.

## References

- [manuscript] Appendix: Toward the Standard Model
- [baez2002] The Octonions (Der(𝕆) ≅ 𝔤₂; §4.1)
- [dubois-violette2016] SU(3) from colour unimodularity / Albert algebra
-/

namespace QOU.StandardModel

open Module

/-- **Conjecture (colour stabilizer action).** The colour algebra `g`
(intended: the octonion stabilizer `su3 e`, 8-dimensional by the
corpus gate) acts faithfully and linearly on the state space `V`
(intended: the 3-strand state space): there is an injective linear
map `g →ₗ End(V)`. Bracket compatibility is the obvious
strengthening; it is deliberately not required here because bracket
closure of the concrete stabilizer is itself unproved in the corpus.
No instance is provided for the intended instantiation — providing
one is the open derivation. -/
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
