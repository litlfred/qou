---
# qou-8274
title: 'OWNER DECISION: is the level-local H_6 deuteron word the right binding object, or only the faster one? (qou-w6x3 residual)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T07:39:47Z
updated_at: 2026-10-04T15:21:55Z
parent: qou-v2om
---

Residual of `qou-w6x3` (option 2 of `qou-hxz4`, PR #7202). Nothing is enacted;
the default is a safe no-op. Framed here so it can be read cold.

## The decision, in one paragraph

The **binding producer** — `hecke_core_legacy.unified_iterative_correction`,
reached from `binding_energy(Z, N)` — builds, for each atom, a word of Hecke
letters whose Markov trace gives the binding energy. That word currently lives
in a **fixed `H_k`** (`k <= 11`, chosen by the partition table, not by the
atom's size), and #7173 measured that it is therefore not "level-local", so the
fast dimension-free path sum of #7160 cannot be used on it.

`qou-w6x3` asked whether re-laying the word on **`3A` strands** (three per
nucleon, the layout the MASS word uses) fixes that. Answer: **no for A >= 3**,
for a structural reason now proved in Lean — but **yes for the deuteron**,
where it also runs 7.8x faster. **The question for the owner is whether the
deuteron's 3A word is the RIGHT object, given that it is a different element of
the algebra and produces different numbers.** It is an owner call and not an
agent call, because it cannot be settled by accuracy without committing exactly
the defect AGENTS.md forbids.

## Why A = 2 is special (and nothing above it is)

The binding word couples **every pair** of nucleons — one inter-nucleon letter
per (new nucleon, earlier nucleon) pair, `C(A,2)` of them, the complete graph
`K_A`. A contiguous 3A layout can only couple **consecutive** nucleons, `A-1`
of them, the path `P_A` (proved general-A:
`QOU/Hecke/ContiguousCouplingGraph.lean::complete_coupling_forces_A_le_two`).
At `A = 2` those coincide — one pair, one adjacency — so the deuteron word
re-embeds exactly. From `A = 3` it does not, and every escape route was
measured and costs more than it buys (details in `qou-w6x3`).

## What is at stake numerically

At `A = 2` both words live in the **same `H_6`**, carry the **same 23 letters**
with the same coefficients, and differ **only** in which generator each letter
sits on. The characters then differ on **9 of the 11 partitions of 6** — max
relative 1.43, and `lambda = [5,1]` goes `-0.827 -> +3.216`, a sign change. So
this is not a refactor; the deuteron binding number would move.

## The options

### 1. Do nothing (THE DEFAULT)
- **What it means.** The binding producer keeps the fixed-`H_k` embedding for
  every atom including the deuteron. `qou-w6x3` stands as a recorded negative.
- **What it costs.** Nothing. The deuteron stays at the measured 942 s
  kernel-live cost recorded in `qou-hxz4`.
- **What it risks.** Nothing moves. The 118x / 7.8x figures stay as
  measurements nobody acted on.
- **What it commits to.** Nothing. Re-openable at any time; the probe, the
  witness and the Lean are on `main` and re-runnable.

### 2. Adopt the 3A embedding for the deuteron only
- **What it means.** `binding_energy(1, 1)` computes a different Hecke element
  than `binding_energy(Z, N)` for every other atom.
- **What it costs.** A new producer path plus the partition table redefined on
  `lambda |- 6` rather than `lambda |- k`; `qou-hxz4` also flags the `C_lambda`
  / Pass-2 gate as needing re-definition. The deuteron binding number is
  regenerated.
- **What it risks.** A **per-case dispatch** — one rule for A = 2, another for
  A >= 3 — which §"NO FITTING" names explicitly as a fitting pattern ("a formula
  that branches on A ... has one free choice per branch"). It would also make
  the deuteron incomparable with the rest of the A-series.
- **What it commits to.** Defending why the deuteron's binding object differs
  in kind from every other atom's.

### 3. Re-derive the whole binding producer on 3A strands
- **What it means.** Abandon the all-pairs coupling and define the binding on
  the chain coupling the layout can carry — i.e. change the physics of the
  model, not its indexing.
- **What it costs.** A full re-derivation. Every recorded binding number moves
  (the A-series -7.27...-8.14, `hadron-knot-table`).
- **What it risks.** The all-pairs coupling may be the content: `qou-ib3g` and
  `qou-556v` already record that the *coordination* structure is where the
  binding's extensive term is being sought, and dropping to a chain is a
  substantive claim about that, not a reindexing.
- **What it commits to.** The chain coupling as the binding model.

## Recommendation (my judgement, not a finding)

**Option 1.** Not because the deuteron speedup is unattractive, but because the
only argument currently available for option 2 is that it is faster and that
`A = 2` happens to be the case where it is expressible — and "this branch is the
one where the construction works" is the selection-against-the-target shape the
anti-fit directive names. If the 3A embedding is right it should be right for a
reason about the coupling, and that reason would have to explain why `K_A`
should become `P_A`, which is option 3's question.

## Blast radius if option 2 or 3 were taken

`binding_energy` (`computations/hecke_core_legacy.py:2987`) feeds
`computations/canonical_mass_table_extended.py` and the external-researcher
facade `qou-mass` (`src/qou_mass/api.py`, `prediction.py`, `__init__.py`), plus
four `computations/deltalambda/` probes.
`unified_iterative_correction` has nine importers, one of which
(`computations/audits/lp_accumulator_kernel_gate.py`) is a gate.

## Evidence

- Probe: `computations/probes/binding_word_3A_reembedding_probe.py` (18/18)
- Witness: `computations/probes/binding-word-3A-reembedding.witness.json`
- Lean: `QOU/Hecke/ContiguousCouplingGraph.lean` (sorry-free)
- Audit: `docs/audits/2026-09-12-binding-word-3A-reembedding.md`

## Progress Update (Round 64 — PR #8263)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8263`](https://github.com/litlfred/qou/pull/8263) (branch `feat/round64-hooksum-formality-charge-ocneanu-coupling-43c1`, Commit 1 `30d0d4f4e437e19904cd4438468a9ecf56eadd3a`, Commit 2 / Head `545135545dc8e721846ea1fb0e54556f69a5a166`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Hecke/ContiguousCouplingGraph.lean (`isCoupling_of_ne_iff_boundary_strand`, `coupled_consecutive_pair`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/hooksum_formality_charge_ocneanu_coupling_probe.py` (`scriptHash: dae747aae6b4`) + `test/results/witnesses/hooksum-formality-charge-ocneanu-coupling.witness.json` (`allPassed: true`).
