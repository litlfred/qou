/-
Copyright (c) 2026 litlfred. All rights reserved.

# Parity constraint on the odd (GGM/decay) face of the q-cubic graded split

Formalize-first structural brick feeding the keystone graded-split wall of the
super-DM / Berezinian route (sibling PR #4140, bean `qou-jqof`): the open target
`qCubicGradedSplit` decomposes the q-cubic as **even = C1/mass (cosh, bar-even)**
and **odd = GGM/decay (sinh, bar-odd)**, with the first even/odd *mixing* order
`c₃` realized as the Berezinian cross-term `B·D⁻¹·C`
(bean `qou-1dnr`: `1279 ppb miss ≈ |c₃|·u³`).

This file supplies the **parity certificate the odd face must satisfy**,
standalone and on-`main` — it depends only on established on-`main` facts, never
on PR #4140's unmerged `SuperDMBerezinian.lean`:

* the odd/decay weight `γ` is exactly bar-ODD — the `(−1)^m` sign alternation of
  the GGM growing solution, upgraded to a scope-(b) invariant in
  `QOU.Mass.DoorVParityNoIdentity` (Door-v);
* the bar-parity bookkeeping (`fixed_eval_two_mul_kills_bar_odd`,
  `bar_even_mul_bar_odd`) proved in `QOU.QBeta` (`ZBarParity.lean`).

The derived constraints (all sorry-free):

1. `oddWeight_shadow_zero` — the odd decay weight `γ`, being exactly bar-odd, has
   **vanishing q=1 (classical) shadow**: `2·φ(γ) = 0` for every bar-compatible
   evaluation `φ` (`φ ∘ σ = φ`), i.e. `φ(γ) = 0` over a target of characteristic
   `≠ 2`. The GGM/decay face carries no classical content at the bar-fixed point.
2. `crossTerm_bar_odd` — the first even/odd mixing cross-term modeled as
   `c = g · γ` with `g` the bar-EVEN even-block dressing (the `B·D⁻¹·C` scalar
   assembled from the even C1/mass block) and `γ` the bar-ODD odd weight, is
   itself **bar-ODD** (`bar_even_mul_bar_odd`): a single even/odd mixing flips
   the bar-parity.
3. `crossTerm_shadow_zero` — hence the mixing cross-term `c₃` also has vanishing
   q=1 shadow.

**Honest scope (constraint, not closure).** This is a *necessary condition* on
any derivation of the open wall `q_cubic = C1`, not a derivation of it. It says:
the classical (nonzero q=1) mass/binding content of the graded split must be
sourced by the **bar-even even face** — the pure bar-odd odd/mixing sector
contributes zero at q=1. In particular the c₃ "`−2 = J_Hopf(q=1)`" classical
near-match cannot be the pure Berezinian cross-term evaluated at q=1 (that
evaluation is forced to zero here); it is the same T3-2 shadow tension
(`fixed_eval_two_mul_kills_bar_odd`) made precise for the graded split. No c_k
value is derived, no registry tier changes, and nothing is wired: this narrows
*how* the split can close, it does not close it.

§7c: the ring is a generic `{R : Type*} [CommRing R]` with an abstract bar
involution `σ : R →+* R`; no archimedean construct appears, so no `ℝ`.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-odd-face-parity-constraint.md
-- Ref: [ramis-sauloy-zhang2013] q-difference formal classification / Stokes
-/
import QOU.QBeta.ZBarParity

namespace QOU.QBeta.OddDecayWeightParity

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **Bar-oddness of the odd/decay face weight.** Abbreviation matching the
    Door-v `(−1)^m` GGM alternation: `σ γ = −γ`. Kept as a plain predicate (no
    class carrier) — the hypothesis is an on-`main` established fact
    (`QOU.Mass.DoorVParityNoIdentity`), threaded explicitly. -/
def IsOddFaceWeight (γ : R) : Prop := σ γ = -γ

/-- **The odd decay weight has vanishing q=1 shadow.** For every bar-compatible
    evaluation `φ` (`φ ∘ σ = φ`, e.g. the q=1 / classical shadow), the exactly
    bar-odd odd-face weight `γ` satisfies `2·φ(γ) = 0` — division-free; over a
    target of characteristic `≠ 2` this is `φ(γ) = 0`. The GGM/decay face
    contributes nothing at the bar-fixed point. Direct from
    `fixed_eval_two_mul_kills_bar_odd`. -/
theorem oddWeight_shadow_zero {S : Type*} [CommRing S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ) (γ : R) (hγ : IsOddFaceWeight σ γ) :
    2 * φ γ = 0 :=
  QOU.QBeta.fixed_eval_two_mul_kills_bar_odd σ φ hcomm γ hγ

/-- **The first even/odd mixing cross-term is bar-ODD.** Model the Berezinian
    cross-term `B·D⁻¹·C` as `c = g · γ`, where `g` is the bar-EVEN even-block
    dressing (the scalar assembled from the even C1/mass block, `σ g = g`) and
    `γ` the bar-ODD odd-face weight. A single even/odd mixing flips the
    bar-parity: `σ c = −c` (`bar_even_mul_bar_odd`). -/
theorem crossTerm_bar_odd (g γ : R) (hg : σ g = g) (hγ : IsOddFaceWeight σ γ) :
    σ (g * γ) = -(g * γ) :=
  QOU.QBeta.bar_even_mul_bar_odd σ g γ hg hγ

/-- **The mixing cross-term `c₃` has vanishing q=1 shadow.** Being bar-odd
    (`crossTerm_bar_odd`), the cross-term `c = g · γ` is annihilated by every
    bar-compatible evaluation `φ`: `2·φ(c) = 0`. Hence the c₃ "`−2 = J_Hopf(1)`"
    classical near-match is NOT the pure Berezinian cross-term evaluated at q=1 —
    that evaluation is forced to zero. -/
theorem crossTerm_shadow_zero {S : Type*} [CommRing S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ)
    (g γ : R) (hg : σ g = g) (hγ : IsOddFaceWeight σ γ) :
    2 * φ (g * γ) = 0 :=
  QOU.QBeta.fixed_eval_two_mul_kills_bar_odd σ φ hcomm (g * γ)
    (crossTerm_bar_odd σ g γ hg hγ)

/-- **The classical mass content is carried by the even face.** For the graded
    split `qCubic = e + c` with `e` the bar-EVEN even/mass face (`σ e = e`) and
    `c = g · γ` the bar-ODD odd/mixing cross-term, every bar-compatible
    evaluation `φ` into a characteristic-`≠ 2` field satisfies `φ(qCubic) = φ(e)`:
    the nonzero q=1 (classical) shadow of the q-cubic is sourced ENTIRELY by the
    bar-even even face, never by the pure bar-odd mixing sector. This is the
    necessary condition on the open wall `q_cubic = C1` — the mass/binding
    classical content must live on the even (C1/cosh) block. -/
theorem classical_shadow_on_even_face {S : Type*} [Field S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ)
    (qCubic e g γ : R) (hsplit : qCubic = e + g * γ)
    (he : σ e = e) (hg : σ g = g) (hγ : IsOddFaceWeight σ γ)
    (h2 : (2 : S) ≠ 0) :
    φ qCubic = φ e :=
  QOU.QBeta.shadow_carried_by_even_part σ φ hcomm qCubic e (g * γ)
    hsplit he (crossTerm_bar_odd σ g γ hg hγ) h2

end QOU.QBeta.OddDecayWeightParity
