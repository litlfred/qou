# Vassiliev (finite-type) invariant scaffold — design + honesty audit

**Date:** 2026-08-01
**Branch:** `claude/vassiliev-finite-type-infra-2026-08-01`
**PR:** #4479 (draft)
**Status:** infrastructure scaffold — definitional layer **sorry-free**; deep
theorems are **honest content-bearing conjecture classes (no instance, NOT
axiomatized)**.

## Why this exists

`QOU/MassTheory/MilnorParitySignLaw.lean` (the #4471 line of work) proves the A=3
Milnor leading order + sign from the Borromean closed form and records A=4 as
measured, but leaves the **general exact law** — `order(D_A) = 2(A−1)` *exactly*
(not merely `≥`), with leading coefficient `= ±μ̄(12…A) ≠ 0` — as the open
`MilnorParitySignConjecture`. The general proof needs the topology theorem

> **(Bar-Natan 1995; Habegger–Masbaum 2000; Meilhan–Yasuhara 2012)** The first
> non-vanishing Vassiliev invariant of an `A`-component Brunnian link is at
> degree `2(A−1)` and equals `±μ̄(12…A) = ±1`.

Mathlib has **no finite-type invariant theory**. This scaffold builds the
foundation so that theorem becomes formalizable by future work; it does **not**
prove it.

## What is sorry-free (definitional / algebraic layer)

All files verified with `lean`-direct (exit 0), no `sorry` / `admit` /
`native_decide` / `axiom`.

| File | Content |
|------|---------|
| `QOU/KnotTheory/Vassiliev/ChordDiagram.lean` | `ChordDiagram n` = fixed-point-free involution on `Fin (2n)`; `degree`, `ext`, the `Perm`-conjugation relabelling action **proved** to preserve involutivity + fixed-point-freeness and to be a group action (`conj_one`, `conj_mul`); the single-chord diagram `oneChord` + `Inhabited (ChordDiagram 1)`. |
| `QOU/KnotTheory/Vassiliev/FourTermRelation.lean` | Free `R`-module `CDModule R n`; `oneTermSubmodule` (1T / framing independence, isolated adjacent-endpoint chords — **faithful**); `fourTermSubmodule` (4T in commutator / Kohno–Drinfeld form via the endpoint-slide action — **encoded**, see honesty note); `relationsSubmodule`; membership lemmas proved **relation-agnostically**. |
| `QOU/KnotTheory/Vassiliev/WeightSystem.lean` | `AReduced R n = CDModule / relations`; `WeightSystem R n = AReduced →ₗ R`; framing-independence + 4T annihilation of any weight system; the functional characterization (`pullback_vanishes`, `descend`, `descend_mk`). |
| `QOU/KnotTheory/Vassiliev/FiniteTypeInvariant.lean` | **The core.** `VassilievSetup` (abstract singular-resolution datum carrying the skein relation `resolve_step`); `vExt` `R`-linear extension (`vExt_add`, `vExt_smul`, `vExt_zero`); `vExt_desingularize` (the first-difference / discrete-derivative structure); `IsFiniteType m`; monotonicity + add/smul closure ⇒ `finiteTypeSubmodule m`; **the Vassiliev filtration** `finiteTypeSubmodule_mono`; the `symbol` map. |

## What is honest conjecture-class (the deep theorems — NOT axiomatized)

`QOU/KnotTheory/Vassiliev/MilnorVassilievBridge.lean`. Two **content-bearing**
`Prop` classes (real fields carrying the claim's shape, §3b-tax), each with
**NO instance** — the open state is represented honestly by a content class with
no inhabitant.

1. **`SymbolIsWeightSystem`** — Kontsevich universality: the degree-`m` symbol of
   an order-`≤ m` invariant equals a weight system evaluated on the double-point
   chord diagram (`symbol_is_weight`), and every weight system is realized
   (`weight_is_realized`).
2. **`BrunnianVassilievBridge`** — the Milnor = leading-Vassiliev bridge:
   `muBar_realized` (at degree `2(A−1)` an invariant takes value `±1` on the
   Brunnian link) + `vassiliev_trivial_below` (every lower-order invariant
   vanishes on it, so the first non-vanishing invariant is at `2(A−1)`).

**Proved (sorry-free) hooks to #4471:**

* `vassilievDegree_eq_leadingOrder : 2 * (A - 1) = leadingOrder A` — alignment
  with `MilnorParitySignLaw.leadingOrder`.
* `brunnian_exact_leadingOrder` — **conditional** (§3b-cond) on
  `[BrunnianVassilievBridge]`: the A-component Brunnian link carries a Vassiliev
  invariant of order `leadingOrder A` valued `±1`, and every strictly-lower-order
  invariant vanishes on it. This **is** the exact-order statement #4471 needs;
  the only unproved input is the (instance-less) class.

## Honesty notes (STRICT discipline compliance)

* **NOT axiomatized.** There is no `axiom bridge : P`. The bridge and Kontsevich
  universality are `class … : Prop` carriers with content fields and **no
  instance** — per §"Axiomatization is NOT a Proof" and §3b-tax. Consuming the
  class downstream (`brunnian_exact_leadingOrder`) is an *explicit conditional
  hypothesis* (§3b-cond), not a laundered assumption.
* **No trivial-true / self-assuming projection.** The conjecture-class fields are
  existentials with `±1` equalities and order-vanishing quantifiers — genuinely
  falsifiable, not `True`, not the block's own conclusion re-projected.
* **4T encoding is a documented design choice, load-bearing for NO theorem.**
  The `fourTermSubmodule` is a specific commutator/endpoint-slide encoding of the
  four-term relation; its exact faithfulness to Bar-Natan's Figure-3 4T (up to
  sign/indexing) is asserted with citation, not proved. **Every** structural
  lemma (`WeightSystem.lean`) holds for an *arbitrary* relations submodule, so no
  false theorem is asserted by the encoding. Cross-checking the encoding against
  `barnatan1995` §3 is filed as follow-up (see below). The 1T submodule is a
  faithful encoding (isolated adjacent-endpoint chord).
* **Base ring §7c.** The chord-diagram module / weight systems are generic
  `[CommRing R]`; no gratuitous `ℝ`. `FiniteTypeInvariant` uses generic `R` for
  `vExt`/filtration and `ℤ` only in the bridge classes (integer-valued Milnor /
  Vassiliev invariants), where it is genuinely required.
* **Universe §7d.** `VassilievSetup.{u, v}` pins the `Type v`-valued `Sing`
  field; all consumers thread `S` so the universe is carried consistently.
* **Free-parameter count: 0.** Pure infrastructure — no fitted constant, no
  physical anchor.

## Intended consumer

A future PR proves `BrunnianVassilievBridge` (or supplies an instance from a
formalized Kontsevich integral / tree-level Milnor identification), then combines
`brunnian_exact_leadingOrder` with `MilnorParitySignLaw` to discharge the exact
`order = 2(A−1)` half of `MilnorParitySignConjecture` — closing the gap between
the `≥ 2(A−1)` lower bound and the *exact* leading order + nonvanishing leading
coefficient.

## Follow-up (beaned)

* Cross-check the `fourTermSubmodule` commutator encoding against Bar-Natan 1995
  §3 (sign/indexing faithfulness). Definitional only; no proved lemma depends on
  it.
* Provide the `chord : Sing m → ChordDiagram m` double-point-pattern map for a
  concrete `VassilievSetup` on braid-word links (`QOU.KnotTheory.BraidWord`),
  connecting this scaffold to the corpus's existing knot representation.
* Attempt an instance / partial proof of `SymbolIsWeightSystem` at low degree
  (`m ≤ 2`), where the weight-system space is small and computable.
