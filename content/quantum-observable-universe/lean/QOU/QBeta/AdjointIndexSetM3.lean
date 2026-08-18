import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.AdjointIndexSetM3 — the knot-INDEPENDENT core of the DT index set, and what it forces

## Where this sits (Route C, milestone M3)

M2 (`AomegaM2BPSCohomology`) established — conditional on the DT/BPS bridge —
that the closed-sector BPS spectrum would be **abelian**: every Borel ray
distinct, trivial Davison–Meinhardt plethystic log, `dim BPS_d = |Ω_d|`, all
multiplicities `1`. That has a consequence worth stating plainly:

> **If the spectrum is abelian with unit multiplicities, "categorifying" it is
> nearly content-free.** A direct sum of one-dimensional spaces carries no
> information beyond *which rays exist*. So M3's real target is not "build a
> cohomological Hall algebra" — it is **derive the index set `Ω`**.

That is a much sharper target than the CoHA framing, and it is what this file
attacks.

## The observation that constrains any answer

M2 records the `4₁` index set as the meridian-charge polynomial
`s(x) = x + 1 + x⁻¹` (three unit-multiplicity states, charges `e ∈ {−1,0,+1}`),
and the corpus records that **the same `s(x)` governs `5₂`** (GGM eqs 239/277/307:
the `5₂` q→0 Stokes entries are `s(x)`, `s(x)`, `s(x)+1`). Knot-independence is
the single hardest fact for any explanation to meet: it is exactly why every
knot-specific invariant tried so far failed (`Driver14CharacterVarietyDTMenu`
tests eight of them; Route A's `R1` was the ninth).

## The hypothesis this file makes precise (NOT proved here)

`H_Ad` — the knot-independent core of the index set is the **weight set of the
adjoint representation of `sl₂`**. For a meridian holonomy with eigenvalues
`(m, m⁻¹)` and `x = m²`, the adjoint (3-dimensional) representation has
eigenvalues `(x, 1, x⁻¹)`, so its character is exactly `s(x) = x + 1 + x⁻¹`, and
at the parabolic point `x = 1` its value is `3 = dim 𝔰𝔩₂`.

Why this is a *mechanism* and not a numerical coincidence:

* In complex Chern–Simons theory the Borel singularities are differences of
  complex volumes of flat connections, and the deformation theory of a flat
  connection is governed by `H¹(M, Ad ρ)` — the **adjoint** local system is the
  canonical coefficient object, not a chosen one.
* `Ad(𝔰𝔩₂)` is multiplicity-free with weights `{2, 0, −2}`, matching M2's
  `sMultiplicities = [1,1,1]` without adjustment.
* It **predicts** knot-independence, which is the observed fact no knot-specific
  invariant could produce.
* In QOU-native terms `Ad ≅ Sym²V`, the partition-`(2)` Wedderburn block of
  `H₂(q)` — so the hypothesis is expressible in Hecke language.

**`H_Ad` is a hypothesis, not a derivation.** Identifying the index set with a
rep-theoretic object that is standard in the deformation theory is a structural
reading; it does not derive the DT spectrum from Hecke data, and this file
claims no such derivation.

## What IS proved here (decidable, no literature input in the general results)

The adjoint weight combinatorics, and — the load-bearing part — a **forcing
theorem**: any knot-independent core, `H_Ad` included, *cannot by itself* produce
the chirality-split `(4₁, 5₂) ↦ (3, 4)`; it necessarily requires a
knot-**dependent** remainder, and that remainder is forced to differ by exactly
one between the two knots. This converts the otherwise-unfalsifiable move "add
one more state for `5₂`" into a structural requirement with a definite value,
which any completion of `H_Ad` must independently derive.

-- Ref: [manuscript] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md (Route C, M3)
-/

namespace QOU.QBeta.AdjointIndexSetM3

/-! ## The adjoint weight data (knot-independent by construction) -/

/-- The `x`-exponents of the adjoint representation of `𝔰𝔩₂`, i.e. the weights
`{2, 0, −2}` written in the variable `x = m²`: `(x, 1, x⁻¹) ↦ (1, 0, −1)`. -/
def adjointExponents : List Int := [1, 0, -1]

/-- **Multiplicity-free**: the adjoint weights are pairwise distinct, matching
M2's `sMultiplicities = [1,1,1]` with no adjustment. -/
theorem adjoint_multiplicity_free : adjointExponents.Nodup := by decide

/-- **`dim 𝔰𝔩₂ = 3`** — the number of adjoint weights. -/
theorem adjoint_dim_three : adjointExponents.length = 3 := by decide

/-- **The weight set is closed under negation** (`x ↔ x⁻¹`), i.e. the index set is
bar-symmetric — the same `q ↦ q⁻¹` involution that grades the DT split in
`ChiralityGradedCount`. -/
theorem adjoint_palindromic :
    ∀ e ∈ adjointExponents, (-e) ∈ adjointExponents := by decide

/-- The character value at the parabolic point `x = 1` is the number of weights:
`s(1) = 3`. (Each weight contributes `1` because the weights are
multiplicity-free.) -/
def sAtOne : Int := (adjointExponents.map (fun _ => (1 : Int))).sum

/-- **`s(1) = 3 = dim 𝔰𝔩₂`**, matching M2's `sAtOne`. -/
theorem s_at_one_eq_three : sAtOne = 3 := by decide

/-! ## The forcing theorem — the load-bearing content

A *knot-independent* core assigns the same count to every knot. The certified DT
data does not: `4₁ ↦ 3` and `5₂ ↦ 4` (the `S⁺` entries). So a knot-independent
core cannot be the whole story, and the shortfall is pinned exactly. -/

/-- The two knots carrying certified DT data. -/
inductive KKnot where
  | fourOne : KKnot
  | fiveTwo : KKnot
  deriving DecidableEq

open KKnot

/-- **A knot-independent core forces a knot-dependent remainder differing by one.**
If a count decomposes as a constant `core` plus a per-knot `extra`, and reproduces
the certified `(3, 4)` split, then `extra` is larger at `5₂` by exactly `1` —
whatever the core is. The "extra state for `5₂`" is therefore not an optional
patch: it is forced, with a definite value. -/
theorem knot_independent_core_forces_unit_remainder
    (core : Int) (extra : KKnot → Int)
    (h41 : core + extra fourOne = 3)
    (h52 : core + extra fiveTwo = 4) :
    extra fiveTwo = extra fourOne + 1 := by
  omega

/-- **Under `H_Ad` the remainder is pinned to `0` and `1`.** Taking the
knot-independent core to be the adjoint count `s(1) = 3`, the `4₁` remainder
vanishes and the `5₂` remainder is exactly one state. Any completion of `H_Ad`
must derive that single extra `5₂` ray independently — it cannot be assumed. -/
theorem adjoint_core_pins_remainder
    (extra : KKnot → Int)
    (h41 : sAtOne + extra fourOne = 3)
    (h52 : sAtOne + extra fiveTwo = 4) :
    extra fourOne = 0 ∧ extra fiveTwo = 1 := by
  rw [s_at_one_eq_three] at h41 h52
  omega

/-- **The falsifier, stated as a theorem.** If some completion claims the count is
*purely* knot-independent (no remainder at all), it contradicts the certified
split. So `H_Ad` alone is provably incomplete — it is not a candidate for the
whole answer, and saying so is not a concession but a derived fact. -/
theorem no_purely_knot_independent_count
    (core : Int)
    (h41 : core = 3) (h52 : core = 4) : False := by
  omega

end QOU.QBeta.AdjointIndexSetM3
