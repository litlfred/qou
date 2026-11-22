import Mathlib.Tactic

/-!
# QOU.Interactions.confinementUniversality

**Canonical declaration** for content block
[`prop:confinement-universality`](../../../quantum-observable-universe/particle-interactions/confinement-universality.md): *Confinement universality: nucleon NF independent of photon polarization*.

This module states the manuscript claim conditional on the §3b hypothesis class.

**Definitional reading (owner E1 = (a), 2026-11-15, bean `qou-qs2u`).** The quark
flavours are an input to the confinement stage, and the confinement word contains no
photon coefficient. So the class is satisfied **by construction** whenever the nucleon NF
is computed from a fixed flavour assignment: `ofFlavourInput` builds the instance. The
class is not a physical decoupling hypothesis, and nothing here derives asymptotic
freedom. The substantive question, which photon states produce a given flavour
assignment, is separate and open.

**Coefficient ring (bean `qou-qs2u`, owner D2, 2026-11-15).** The context is
parametrised by the coefficient type `K` of the photon polarisation and the type `M` of
the nucleon NF. Nothing in the statement or proof uses any structure of `K`; until
2026-11-15 it was fixed at `ℝ`, which restricted the claim to real coefficients
(linear polarisations, under the reading `φ ↦ [v₁ : v₂]`) for no mathematical reason.
`K = ℂ` covers circular polarisations. The γγ channel coefficients are polynomials with
integer coefficients in `φ` and `h` (`QOU/Interactions/GammaGammaPairChannels.lean`),
so they are defined over any commutative ring.
-/

namespace QOU.Interactions

/-- Abstract context for the `confinementUniversality` claim — manuscript-named
    typed fields below. -/
class ConfinementUniversalityContext (K : Type*) (M : Type*) where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Nucleon NF as a function of photon polarisation coefficients
      `(φ_0, φ_1, φ_01)`. -/
  N_F : K → K → K → M
  /-- Reference zero-polarization nucleon NF value. -/
  N_F_zero : M

/-- The physical hypotheses carried by the Confinement Universality Conjecture. -/
class ConfinementUniversalityConjecture {K M : Type*} [Zero K]
    (ctx : ConfinementUniversalityContext K M) : Prop where
  /-- Zero-polarization case equals reference. -/
  h_N_F_zero : ctx.N_F 0 0 0 = ctx.N_F_zero
  /-- General polarization case equals reference. -/
  h_N_F : ∀ φ_0 φ_1 φ_01 : K, ctx.N_F φ_0 φ_1 φ_01 = ctx.N_F_zero

/-- **Proposition statement** (from manuscript, definitional reading): with the quark
flavours `f` supplied as input, the nucleon NF of the chain
`γγ → q q̄ → B₃ · crossings` does not depend on the photon coefficients
`(φ₀, φ₁, φ₀₁)`, because the confinement word contains none of them. It depends only on
`q` and `f`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/confinement-universality.ts
theorem confinementUniversality {K M : Type*} [Zero K]
    (ctx : ConfinementUniversalityContext K M)
    [hc : ConfinementUniversalityConjecture ctx] :
    ∀ (φ_0 φ_1 φ_01 : K), ctx.N_F φ_0 φ_1 φ_01 = ctx.N_F 0 0 0 := by
  intro φ_0 φ_1 φ_01
  rw [hc.h_N_F, hc.h_N_F_zero]

/-- **True by construction.** A context whose nucleon NF is a fixed value `G`, the NF
of the confinement word for a fixed flavour assignment, satisfies the class. -/
theorem ofFlavourInput {K M : Type*} [Zero K] (Z N : ℕ) (G : M) :
    ConfinementUniversalityConjecture
      (⟨Z, N, fun _ _ _ => G, G⟩ : ConfinementUniversalityContext K M) :=
  ⟨rfl, fun _ _ _ => rfl⟩

/-- **Corollary (a one-line consequence of the class field `h_N_F`).** If a
quantity `U` of the photon (for instance the chirality unit `u` read off the photon
polarisation, bean `qou-qs2u`) can be read off the nucleon NF by some `g`, then `U` is
constant. So under the conjecture a photon-inherited chirality unit is hidden at
nucleon level; it does not contradict the conjecture. -/
-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement/confinement-universality.md
theorem inherited_unit_invisible_of_confinement {K M : Type*} [Zero K]
    (ctx : ConfinementUniversalityContext K M)
    [h : ConfinementUniversalityConjecture ctx] {X : Type*}
    (U : K → K → K → X) (g : M → X)
    (hg : ∀ a b c, g (ctx.N_F a b c) = U a b c) (a b c a' b' c' : K) :
    U a b c = U a' b' c' := by
  rw [← hg, ← hg, h.h_N_F, h.h_N_F]

end QOU.Interactions
