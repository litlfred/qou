/-
# The decuplet equal-spacing rule is an identity of first-order octet breaking

The companion to `GellMannOkuboIdentity.lean`, for the *other* multiplet and
the *other* historically decisive relation.

Gell-Mann's 1962 prediction of the `Ω⁻` — the eightfold way's signature
triumph — used the **equal-spacing rule**: within the baryon decuplet the
consecutive mass differences

    m(Σ*) − m(Δ),   m(Ξ*) − m(Σ*),   m(Ω) − m(Ξ*)

are all equal, so `m(Ω)` is fixed by the three lighter states.  The prediction
landed within 0.6 % and the particle was found.

**This file proves that the rule carries no information about the breaking
mechanism.**  It holds identically, for *every* choice of the first-order
octet-breaking parameters `a, b, c`, over any commutative ring — exactly as
Gell-Mann–Okubo does on the octet.  Reproducing equal spacing is therefore not
evidence for any particular dynamics, QOU's included.

## Why it collapses — the invariant

The Gell-Mann–Okubo mass operator is *quadratic* in the hypercharge:

    m(I, Y)  =  a  +  b·Y  +  c·( I(I+1) − Y²/4 ).

On the decuplet, and **only** because of the decuplet's own weight structure,
the isospin is an affine function of the hypercharge:

    2 I  =  Y + 2        (Δ, Σ*, Ξ*, Ω  at  Y = 1, 0, −1, −2).

Substituting collapses the quadratic term to a *linear* one,

    I(I+1) − Y²/4  =  (3Y + 4)/2,

so `m` is affine in `Y`.  Consecutive decuplet states step by `ΔY = −1`, hence
the mass steps are equal.  `casimir_collapses_of_isospin_affine` is that step;
`equal_spacing` is the consequence.

**The property is special to the decuplet, not generic.**  On the baryon octet
the isospin is not even a *function* of the hypercharge — `Σ` and `Λ` share
`Y = 0` with `I = 1` and `I = 0` — so the collapse has nothing to act on.
`octet_isospin_not_function_of_hypercharge` records the contrast, so the
argument above cannot be misread as applying to every multiplet.

## What remains testable

The **deviation**, exactly as for GMO.  The measured spacings are
`152.6`, `148.8`, `139.05` MeV — a `13.55` MeV spread, `≈ 9.2 %` of the mean.
That spread is the failure of first-order breaking and is the only part of the
decuplet spectrum a mechanism can be scored against.  QOU derives no
second-order term, so it currently predicts spread `0`.

Numbers are comparators only; nothing here is fitted and nothing is wired.

Conventions: everything is stated over a generic `[CommRing R]` per
`AGENTS.md` §7c — the statement is pure algebra of the breaking parameters and
needs no ordering, no `ℝ`, and no archimedean content.  Masses are multiplied
through by `4` to stay division-free, and the isospin Casimir enters as
`fourCasimir = 4·I(I+1)`, an integer on every decuplet state.

-- Ref: [gellmann1962] Gell-Mann, *Symmetries of Baryons and Mesons*,
--      Phys. Rev. 125 (1962) 1067, https://doi.org/10.1103/PhysRev.125.1067
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

namespace QOU.Eightfold.DecupletEqualSpacing

variable {R : Type*} [CommRing R]

/-- The first-order `SU(3)`-breaking mass operator, quadrupled to stay
division-free:

    4 m(I, Y)  =  4a  +  4b·Y  +  c·( 4I(I+1) − Y² ).

Identical in form to `GellMannOkuboIdentity.massSqQuadrupled`; the decuplet is
conventionally fitted with masses rather than masses-squared, but the identity
below is insensitive to that choice — it uses only the shape of the operator. -/
def massQuadrupled (a b c fourCasimir Y : R) : R :=
  4 * a + 4 * b * Y + c * (fourCasimir - Y ^ 2)

/-- `Δ(1232)`: `Y = +1`, `I = 3/2`, so `4·I(I+1) = 15`. -/
def deltaMass (a b c : R) : R := massQuadrupled a b c 15 1

/-- `Σ*(1385)`: `Y = 0`, `I = 1`, so `4·I(I+1) = 8`. -/
def sigmaStarMass (a b c : R) : R := massQuadrupled a b c 8 0

/-- `Ξ*(1530)`: `Y = −1`, `I = 1/2`, so `4·I(I+1) = 3`. -/
def xiStarMass (a b c : R) : R := massQuadrupled a b c 3 (-1)

/-- `Ω⁻(1672)`: `Y = −2`, `I = 0`, so `4·I(I+1) = 0`. -/
def omegaMass (a b c : R) : R := massQuadrupled a b c 0 (-2)

/-! ### The structural cause -/

/-- **The decuplet's Casimir term is affine in `Y`.**  Whenever the isospin is
affine in the hypercharge in the decuplet's pattern — encoded division-free as
`fourCasimir = (Y + 2)(Y + 4)`, which is `4·I(I+1)` at `2I = Y + 2` — the
quadratic combination `4I(I+1) − Y²` collapses to `6Y + 8`.

This is the whole mechanism: the `Y²` cancels, so the breaking operator becomes
affine in `Y` and equal steps in `Y` give equal steps in mass. -/
theorem casimir_collapses_of_isospin_affine (Y fourCasimir : R)
    (h : fourCasimir = (Y + 2) * (Y + 4)) :
    fourCasimir - Y ^ 2 = 6 * Y + 8 := by
  subst h; ring

/-- The four decuplet states do satisfy that pattern. -/
theorem decuplet_isospin_affine :
    ((15 : R) = (1 + 2) * (1 + 4)) ∧ ((8 : R) = (0 + 2) * (0 + 4)) ∧
    ((3 : R) = (-1 + 2) * (-1 + 4)) ∧ ((0 : R) = (-2 + 2) * (-2 + 4)) := by
  refine ⟨by ring, by ring, by ring, by ring⟩

/-! ### The identity -/

/-- The three consecutive decuplet spacings all equal `−4b − 6c`. -/
theorem spacing_sigma_delta (a b c : R) :
    sigmaStarMass a b c - deltaMass a b c = -4 * b - 6 * c := by
  unfold sigmaStarMass deltaMass massQuadrupled; ring

theorem spacing_xi_sigma (a b c : R) :
    xiStarMass a b c - sigmaStarMass a b c = -4 * b - 6 * c := by
  unfold xiStarMass sigmaStarMass massQuadrupled; ring

theorem spacing_omega_xi (a b c : R) :
    omegaMass a b c - xiStarMass a b c = -4 * b - 6 * c := by
  unfold omegaMass xiStarMass massQuadrupled; ring

/-- **The decuplet equal-spacing rule is an identity of the first-order octet
ansatz.**  All three consecutive spacings coincide for *every* `a, b, c`, over
any commutative ring.

`a` drops out (it is the common centroid) and the *pattern* of the breaking
survives only as the single number `−4b − 6c`.  Two mechanisms with different
`(b, c)` but the same `4b + 6c` are indistinguishable here, and *every*
mechanism whatsoever satisfies the equality of the three spacings. -/
theorem equal_spacing (a b c : R) :
    sigmaStarMass a b c - deltaMass a b c = xiStarMass a b c - sigmaStarMass a b c
    ∧ xiStarMass a b c - sigmaStarMass a b c = omegaMass a b c - xiStarMass a b c := by
  rw [spacing_sigma_delta, spacing_xi_sigma, spacing_omega_xi]
  exact ⟨rfl, rfl⟩

/-- **The `Ω` mass is not an independent prediction.**  It is determined by two
of the lighter states alone: `m(Ω) = 2 m(Ξ*) − m(Σ*)`, identically in
`a, b, c`.  So Gell-Mann's extrapolation extracts no dynamical information —
it reads off a value already fixed by the ansatz's affine `Y`-dependence. -/
theorem omega_eq_two_xi_minus_sigma (a b c : R) :
    omegaMass a b c = 2 * xiStarMass a b c - sigmaStarMass a b c := by
  unfold omegaMass xiStarMass sigmaStarMass massQuadrupled; ring

/-- The combination form: the second difference vanishes identically. -/
theorem second_difference_vanishes (a b c : R) :
    (omegaMass a b c - xiStarMass a b c)
      - (xiStarMass a b c - sigmaStarMass a b c) = 0 := by
  rw [spacing_omega_xi, spacing_xi_sigma]; ring

/-- **The discriminating-power statement.**  Two arbitrarily different breaking
patterns `(a,b,c)` and `(a',b',c')` — hence arbitrarily different physics —
give the *same* value of the equal-spacing combination, namely zero.  Equal
spacing cannot tell them apart.

This is the decuplet analogue of `GellMannOkuboIdentity.gmo_cannot_discriminate`,
and it carries the same consequence: reproducing the rule is not evidence for
any mechanism. -/
theorem equal_spacing_cannot_discriminate (a b c a' b' c' : R) :
    (omegaMass a b c - xiStarMass a b c)
        - (xiStarMass a b c - sigmaStarMass a b c)
      = (omegaMass a' b' c' - xiStarMass a' b' c')
        - (xiStarMass a' b' c' - sigmaStarMass a' b' c') := by
  rw [second_difference_vanishes, second_difference_vanishes]

/-! ### Negative control — the collapse is special to the decuplet

Without this, `casimir_collapses_of_isospin_affine` could be misread as a
generic fact about `SU(3)` multiplets.  It is not: it needs the isospin to be a
function of the hypercharge at all, which fails on the baryon octet. -/

/-- The baryon octet as `(Y, 4·I(I+1))` pairs: `N(Y=1, I=1/2)`, `Σ(Y=0, I=1)`,
`Λ(Y=0, I=0)`, `Ξ(Y=−1, I=1/2)`.  This list is *data* — the octet weight
diagram, imported, not derived here — and it is the only input to the theorem
below. -/
def octetStates : List (ℤ × ℤ) := [(1, 3), (0, 8), (0, 0), (-1, 3)]

/-- The decuplet as `(Y, 4·I(I+1))` pairs, same convention. -/
def decupletStates : List (ℤ × ℤ) := [(1, 15), (0, 8), (-1, 3), (-2, 0)]

/-- **On the baryon octet the Casimir is not a function of the hypercharge.**
Two distinct octet states share `Y = 0` while carrying different `4·I(I+1)` —
`Σ` at `8` and `Λ` at `0`.  Hence no substitution `fourCasimir = g(Y)` exists
for the octet, and `casimir_collapses_of_isospin_affine` has nothing to act on:
the decuplet's collapse to an affine mass operator has **no octet counterpart**.

This is what stops the equal-spacing argument from being read as a generic fact
about `SU(3)` multiplets. The claim is derived from `octetStates`, not asserted. -/
theorem octet_casimir_not_function_of_hypercharge :
    ∃ Y k₁ k₂ : ℤ, k₁ ≠ k₂ ∧ (Y, k₁) ∈ octetStates ∧ (Y, k₂) ∈ octetStates :=
  ⟨0, 8, 0, by decide, by decide, by decide⟩

/-- **On the decuplet it *is* a function of the hypercharge**, and specifically
the affine one `casimir_collapses_of_isospin_affine` needs: every state
satisfies `4·I(I+1) = (Y + 2)(Y + 4)`.

Together with the previous theorem this is the contrast in full — the collapse
holds on the decuplet and fails on the octet, both derived from the state
lists rather than asserted. -/
theorem decuplet_casimir_is_affine_in_hypercharge :
    ∀ p ∈ decupletStates, p.2 = (p.1 + 2) * (p.1 + 4) := by decide

/-- Sanity: `equal_spacing` is a statement about four *different* states, not a
repetition of one — the decuplet hypercharges are pairwise distinct. -/
theorem decuplet_hypercharges_distinct :
    (decupletStates.map Prod.fst).Nodup := by decide

/-- Negative control on the identity itself: the common spacing `−4b − 6c` is
*not* identically zero, so `equal_spacing` is not the degenerate statement that
all four masses coincide.  Witnessed at `b = 1, c = 0` over `ℤ`. -/
theorem spacing_not_identically_zero :
    ∃ b c : ℤ, -4 * b - 6 * c ≠ 0 := ⟨1, 0, by decide⟩

end QOU.Eightfold.DecupletEqualSpacing
