---
# qou-uh5f
title: 'RESEARCH: fix the Moebius classical-limit constant to a knot-type invariant'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T20:01:59Z
updated_at: 2026-10-10T14:00:00Z
parent: qou-v2om
---

## What is open

`CategoricalMobiusEnergy` (`folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean`)
encodes the classical limit as

    classicalLimit : energy = (1 / 4) * classicalEnergy.value + classicalLimitConst

with `classicalLimitConst : ℝ` a **free field of the same structure**. As of
2026-09-15 that is not a suspicion, it is proved sorry-free in the same file:

- `shiftEnergy cme d` adds a real `d` to `energy`, to `energyUnderMobius` and to
  `classicalLimitConst`, and re-derives both `mobiusInvariant` and
  `classicalLimit`. So the shift is an endomorphism of the structure.
- `classicalLimitConst_surjective` — for any `k : ℝ` there is an instance with
  the SAME `classicalEnergy` and `classicalLimitConst = k`.
- `no_universal_classicalLimitConst` — `¬ ∃ k, ∀ c, c.classicalLimitConst = k`.

Axioms on all of them: `[propext, Classical.choice, Quot.sound]`.

The `.md` and an `authorNotes` entry on `mobius-energy.ts` now state the scope:
the block establishes the **shape** of the limit (affine in the classical Möbius
energy, slope 1/4), not a topological normalisation.

## The research target

Give the categorical Möbius energy an additive zero, so that `const` becomes a
function of the knot type of ϱ rather than a free parameter. Equivalently: find
the structure that `CategoricalMobiusEnergy` is missing.

**Why this is not a Lean exercise.** The theorem above says the constant is
unconstrained *as the structure is encoded*. Adding a field `constIsTopological :
classicalLimitConst = f (knotType knot)` would make it constrained by fiat and is
the §"Axiomatization is NOT a Proof" move — it assumes exactly the content at
issue. What is wanted is a construction in which the zero is forced.

**Candidate routes, none tested here.**

1. **Normalise at the round circle.** The classical Möbius energy has
   `E(unknot round circle) = 4` (O'Hara / Freedman–He–Wang). If `E_cat` inherits
   a value there from the categorical side, the constant is determined by one
   equation. Needs: an `E_cat` of the round circle computed from the
   Frobenius–Hopf kernel, not assumed.
2. **Self-energy subtraction as the zero.** Step 3 of the Proposition's own proof
   sketch says the diagonal regularisation matches the arc-length subtraction via
   the antipode `S`. If that matching is exact rather than up to a constant, the
   constant is 0 and the claim is stronger than the block states. If it is only
   up to a constant, the constant is whatever that regularisation leaves.
3. **`q → 1` continuity.** The limit is stated as `q → 1`; the structure carries
   `q_gt_one` and a single `energy`, so the limit is not actually taken. A
   formulation with a `q`-family and a genuine limit may force the constant from
   the family's behaviour.

## Status / how to know when it is closed

Closed when a sorry-free Lean declaration derives `classicalLimitConst` from data
already in the structure (or from a construction that supplies the missing
datum), WITHOUT a field asserting it. Until then the `.md` scoping stands and is
the honest statement.

**Do not close this bean on documentation work** — the subject is open
mathematics (AGENTS.md §13a). The scoping edit is a body-append, not a
completion.

## Related

- `qou-pzsi` — the arc this came out of (no map from a braid word to a curve).
- `qou-6xt9` — knot-energy literature ingest (O'Hara, FHW). Route 1 above needs
  `E(round circle) = 4` cited from held text, and FHW's Theorem B is already
  established as inapplicable to the scored elements (all 2-component links).
- `qou-15oa` / `vta3` / `ne0m` — the Frobenius–Hopf kernel, which route 2 needs
  explicitly.

## 2026-10-10 — regulator universality proved (sorry-free); constant is a scheme datum

New library file `folio/quantum-observable-universe/lean/QOU/MobiusRegulator.lean`
(Mathlib-only imports, imported by nothing). lean-direct
`lean -DautoImplicit=false -s 65536` exit 0; `#print axioms` on all eight
declarations: `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.

- `bfhw_regularization_integral`: `∫₀^l 2∫_ε^{l/2} v⁻² = 2l/ε − 4` (l, ε > 0).
  **Sign checked against `library/arxiv-math-9301212v1` eqs. (1),(3):** the
  integral as printed equals `2l/ε − 4`; BFHW's "`= 4 − 2l/ε`" is the signed
  contribution of the subtracted `−∬D⁻²` term (`bfhw_regularization_term`).
- `regulator_difference` / `regEnergy_sub` / `regEnergy_sub_indep`: if
  `E_R(γ) = lim_{ε→0⁺}(A_ε(γ) − R(ε,L(γ)))` and `R₁ − R₂ → c`, then
  `E_{R₁}(γ) − E_{R₂}(γ) = −c` for every γ where both limits exist, same for all γ.
- `bfhw_minus_minimalSubtraction`: `E_BFHW(γ) = E_{2l/ε}(γ) + 4` for every curve of
  positive length where both limits exist — the round-circle "4" is exactly the
  finite part of the BFHW regulator.
- `regulator_shift`: `R − k` is an admissible regulator with the same divergent
  part and moves every energy by `+k`.

**What this does and does not settle.** It shows, at the classical level, that an
additive classical-limit constant is fixed by the choice of the regulator's finite
part and by nothing in the energy density — the classical-side counterpart of
`classicalLimitConst_surjective`. It does NOT derive `classicalLimitConst` for
`CategoricalMobiusEnergy`: that still needs the categorical side to *supply* a
regulator (route 2: is the antipode/diagonal subtraction exactly `R_BFHW`, or
`R_BFHW` up to a constant?). Bean stays open.

## Round 68 Formalization Progress (PR #8285)
- Formalized `QOU.MobiusRegulator.bfhwRegulator_sub_msRegulator_eq_neg_four` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/twobody_deficit_regulator_sdp_milnor_probe.py`, `scriptHash: 39a564805d3e`, Commit 1 `70bec575bb493c7f91cf1b39cb54e58ef8343777`, Commit 2 / Witness `250465c60a6cea44d9f569e88cc79ee2c8d8051b`, PR `litlfred/qou#8285`).
