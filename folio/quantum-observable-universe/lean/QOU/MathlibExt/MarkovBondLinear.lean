/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.MarkovBondRule
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Basic

/-!
# The bond rule reduces to its `d = 0` case

`QOU.MathlibExt.MarkovBondRule.BondRule` carries the one trace-level input of
the bond-product formula as an unproved hypothesis:

  `tr (x * (σ_g + d • 1)) = (z + d) * tr x`   for `g` unused by `x`.

This file removes the parameter `d` from that hypothesis, **unconditionally**.
For any linear functional on any `R`-algebra,

  `tr (x * (s + d • 1)) = tr (x * s) + d * tr x`

so the `d`-family holds for a given `x, g` **iff** its `d = 0` member does
(`bondRule_iff_sigma_case`). The whole `(z + d)` shape is a consequence of
linearity; the mathematical content sits entirely in the single equation
`tr (x * σ_g) = z * tr x`.

This matters because it is exactly half of what `qou-g8i1` has to prove, and it
is the half that needs no Hecke-algebra machinery: a trace, an algebra, and
linearity. The remaining half — the `σ_g` case — is where the Markov property
and the unused-generator hypothesis actually do their work, and it stays open.

## Scope

Nothing here asserts the bond rule. `bondRule_iff_sigma_case` is an *iff*: it
transports the hypothesis, it does not discharge it. `MarkovLinear` below is a
plain bundling of "linear functional on an algebra" and is instantiated for the
trivial example only, to show the structure is inhabited and therefore not
vacuous.

## Base ring

Generic `[CommRing R]` and a generic `R`-algebra `A`. No `ℝ`, no `q`-specifics,
no archimedean content — the statement is about linearity and nothing else.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md
-/

namespace QOU.MathlibExt.MarkovBondLinear

open QOU.MathlibExt.MarkovBondRule

variable {R : Type*} [CommRing R]
variable {A : Type*} [Ring A] [Algebra R A]

/-- A linear functional on an `R`-algebra — the minimum a "trace" must be for
the reduction below. Deliberately *not* asked to be a trace in the
`tr (a*b) = tr (b*a)` sense: the reduction does not need it. -/
structure MarkovLinear (R : Type*) [CommRing R] (A : Type*) [Ring A]
    [Algebra R A] where
  /-- The underlying functional. -/
  tr : A →ₗ[R] R

variable (T : MarkovLinear R A)

/-- **Appending `d • 1` is linear.**

`tr (x * (s + d • 1)) = tr (x * s) + d * tr x`, for any `x`, `s`, `d`. This is
the whole reason the bond rule has the shape `z + d`. -/
theorem tr_mul_add_smul_one (x s : A) (d : R) :
    T.tr (x * (s + d • (1 : A))) = T.tr (x * s) + d * T.tr x := by
  have hx : x * (s + d • (1 : A)) = x * s + d • x := by
    rw [mul_add, mul_smul_comm, mul_one]
  rw [hx, map_add, map_smul, smul_eq_mul]

/-- **The bond rule holds for all `d` iff it holds at `d = 0`.**

The `(z + d)` family collapses to one equation. `↤` is the direction that
matters: proving the single `σ_g` case yields the whole family. -/
theorem bondRule_iff_sigma_case (x s : A) (z : R) :
    (∀ d : R, T.tr (x * (s + d • (1 : A))) = (z + d) * T.tr x)
      ↔ T.tr (x * s) = z * T.tr x := by
  constructor
  · intro h
    have h0 := h 0
    simpa using h0
  · intro h d
    rw [tr_mul_add_smul_one T x s d, h]
    ring

/-- The `d`-family, written out: given the `σ_g` case, every bond letter's
contribution is `z + d`. A proton-proton bond (`d = 0`) contributes `z`; a
neutron-neutron bond (`d = -h`) contributes `z - h`, which
`QOU.MathlibExt.MarkovBondRule.markovZ_sub_h` identifies with `z (1/q)`. -/
theorem tr_bond_of_sigma_case (x s : A) (z : R)
    (h : T.tr (x * s) = z * T.tr x) (d : R) :
    T.tr (x * (s + d • (1 : A))) = (z + d) * T.tr x :=
  (bondRule_iff_sigma_case T x s z).mpr h d

/-- The structure is inhabited: the zero functional is a `MarkovLinear`.

Present so `MarkovLinear` is demonstrably not an empty abstraction. It is a
*witness of inhabitation only* — the zero functional satisfies the bond rule
trivially for every `z`, so it is evidence about the definition's
well-formedness and about nothing else. -/
def trivialMarkovLinear : MarkovLinear R A where
  tr := 0

/-- Sanity check on the reduction, on the trivial functional: both sides are
`0`, for every `z` and `d`. This confirms `bondRule_iff_sigma_case` is
applicable, not that any interesting trace satisfies the rule. -/
theorem trivial_satisfies (x s : A) (z d : R) :
    (trivialMarkovLinear (R := R) (A := A)).tr (x * (s + d • (1 : A)))
      = (z + d) * (trivialMarkovLinear (R := R) (A := A)).tr x := by
  simp [trivialMarkovLinear]

end QOU.MathlibExt.MarkovBondLinear
