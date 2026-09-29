import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.confinementUniversality

**Canonical declaration** for content block
[`prop:confinement-universality`](../../../quantum-observable-universe/particle-interactions/confinement-universality.md): *Confinement universality: nucleon NF independent of photon polarization*.

This module states the manuscript claim conditional on the §3b hypothesis class.
-/

namespace QOU.Interactions

/-- Abstract context for the `confinementUniversality` claim — manuscript-named
    typed fields below. -/
class ConfinementUniversalityContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Nucleon NF as a function of photon polarisation coefficients
      `(φ_0, φ_1, φ_01)`. -/
  N_F : ℝ → ℝ → ℝ → ℝ
  /-- Reference zero-polarization nucleon NF value. -/
  N_F_zero : ℝ

/-- The physical hypotheses carried by the Confinement Universality Conjecture. -/
class ConfinementUniversalityConjecture (ctx : ConfinementUniversalityContext) : Prop where
  /-- Zero-polarization case equals reference. -/
  h_N_F_zero : ctx.N_F 0 0 0 = ctx.N_F_zero
  /-- General polarization case equals reference. -/
  h_N_F : ∀ φ_0 φ_1 φ_01 : ℝ, ctx.N_F φ_0 φ_1 φ_01 = ctx.N_F_zero

/-- **Proposition statement** (from manuscript):

Let $\gamma_k = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ be a 4-term photon
([Breit--Wheeler](#def:breit-wheeler-pair-production)).
Let $\mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})$ denote the
nucleon NF obtained by the derivation chain
([4-term pair nucleon](#prop:four-term-pair-nucleon)):
$\gamma\gamma \to q\bar{q} \to \mathcal{B}_3 \cdot \mathrm{crossings} \to \mathfrak{N}$.*

*Then for all $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$:*

$$
  \mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})
  =
  \mathfrak{N}(0, 0, 0)
  =
  \mathrm{NF}(\mathcal{B}_3 \cdot \mathrm{crossings}).
$$

*The nucleon NF depends only on $q$ and the quark flavor assignment.*

## Proof

The Lean encoding below derives the equality from the hypothesis class. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/confinement-universality.ts
theorem confinementUniversality (ctx : ConfinementUniversalityContext)
    [hc : ConfinementUniversalityConjecture ctx] :
    ∀ (φ_0 φ_1 φ_01 : ℝ), ctx.N_F φ_0 φ_1 φ_01 = ctx.N_F 0 0 0 := by
  intro φ_0 φ_1 φ_01
  rw [hc.h_N_F, hc.h_N_F_zero]

end QOU.Interactions
