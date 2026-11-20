---
# qou-vnqe
title: Formalize a reusable saddle/potential pipeline (triangulation -> potential -> critical value) for QOU and for chipping at unproved knot volumes
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:01:39Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---


## Ask

Owner: can the saddle/potential infrastructure be formalized so it serves both
QOU's own needs and an attack on the unproved knot volumes?

## First, roast the version of this I said in session

> "Automating the first three [potential, critical value, saddle location] so
> human/Lean effort lands only on the homotopy is a real reduction."

Two defects.

**(a) I asserted a page-count split I never measured.** `ki6c` is 72 pp / 37
sections; the per-knot sections are "Proof of Theorem 1.1", "Estimate of the
range of Δ′", "Calculation of the critical value", "Verifying the assumption of
the Poisson summation formula", "Verifying the assumption of the saddle point
method". Whether the pages sit in the *verifying* sections or the *estimate*
sections decides whether my claim is true, and I did not open the PDF to check.
Do that before quoting this.

**(b) It conflates two different costs.** Ohtsuki does not spend pages
evaluating Li₂ at a saddle — that is a line for him. Automating it reduces the
**formalizer's** burden, not the **mathematician's**. My sentence claimed a
reduction in the 50–150 pp, and the argument only supports a reduction in the
Lean effort to *re-do* it. Those are different projects with different
customers, and only the second is ours.

There is also a trap: "certified numerics to locate the saddle" discharges
nothing. Knowing numerically where a saddle sits does not prove the contour can
be moved there. Numeric saddle-hunting against a known target is exactly the
failure mode already measured on 8₁₁ — 1200 convention choices, 1184 distinct
values, 19 within 5 % of Vol **by chance**.

## What is actually reusable, and what QOU already has

| stage | reusable? | in-repo today |
|---|---|---|
| triangulation → shape field | yes, mechanical | `six_crossing_shape_field_discriminant.py` stores 6₁/6₂ shapes at 90 dp **with minimal polynomials** |
| potential function `Σ Li₂(z_i)` | yes | `_li_2_q_util`, Clausen in Lean (`QOU/Knot/Clausen.lean`) |
| critical value / saddle | yes, numerically | `fivetwo_stokes_matrix_zq.py`, `qbeta_5two_stokes_population_bridge_probe.py` (per-saddle Gaussians `1/√(V₀'')`, phases `e^{iV_σ/x₀}`, resummed `φ_σ`) |
| transseries / Stokes weights | partly | same probes; Sauzin mould calculus in `library/` |
| **domain homotopy / assumption verification** | **no** | nothing — this is the irreducible part |

So three of five stages exist in some form, scattered across probes written for
other purposes. The build item is not new mathematics; it is **consolidation**:
one module that takes a knot and returns (shapes, potential, saddles, critical
value, per-saddle amplitudes) with provenance, instead of five probes each
rebuilding a piece.

## Proposed scope, preflight-gated

1. **Preflight first** (cheap, decisive): for each target knot, does a positive
   sum exist at the Kashaev point? If yes → squeeze route, skip all of this.
   If no → this pipeline is the only route, and the homotopy is still open.
   Do not skip this gate; see bean `qou-okh4`.
2. Consolidate stages 1–3 into one module with a per-knot registry, reusing
   `knot_volumes.vol_at` for the target value.
3. Keep the numerics **advisory**: the module must not emit an assertion of the
   form "saddle matches volume", which is the numerology trap. It should emit
   the saddle data and let a proof consume it.
4. Only then ask what Lean can carry.

## Honest expectation

This does **not** close 8₁₁ or any 8/10-crossing knot. The obstruction is the
domain homotopy, which is exactly the stage that does not automate — and
Ohtsuki–Yokota reportedly describe their homotopy step as "quite non-trivial"
(recorded in `qou-b5h9` from the 2026-08-25 audit; **not independently verified
from the PDF here** — verify before citing). What it buys is that the mechanical
stages stop being re-derived per probe, and that the Stokes/transseries data QOU
already computes for 5₂ becomes available uniformly.


## Round 80 Execution Note (2026-11-17T08:30:05Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8281`](https://github.com/litlfred/qou/pull/8281) (`feat/qou-b9cj-2g9j-mf2v-ql68-vnqe-yaz9`, HEAD `a1a5cc9d31f5e1ebdd07e681f60c9089a97bff5f`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/QJetProlongationSymbolAndMellorMelvinMilnorBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/q_jet_prolongation_symbol_and_mellor_melvin_milnor_brick_probe.py` & `computations/probes/q-jet-prolongation-symbol-and-mellor-melvin-milnor-brick.witness.json` (`scriptCommitSha = 806124de41e190e32fc1067832d4c70dbfefebc0`, `outputHash = b877931046495a3920ba02d962916c3947a2eeb70cc28395bac6afca4f75490d`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8281, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
