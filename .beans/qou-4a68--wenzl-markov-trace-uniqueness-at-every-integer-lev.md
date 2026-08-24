---
# qou-4a68
title: Wenzl Markov-trace uniqueness at every integer level r
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:34:24Z
updated_at: 2026-08-24T19:59:28Z
---

## Landed — PR #5705, sorry-free, axiom-clean

**The framing was wrong in one specific way, and it is the main finding.**
The tranche was scoped as "uniqueness is still r = 2 only; generalise it."
`HeckeCoset.markovTrace_unique` never mentioned a level. It is stated for two
`MarkovTraceFamily K q qi z` at a common `z` over generic `[CommRing K]`, and its
proof runs on the coset spanning family alone. The r-dependence lived entirely in
`MarkovTraceInstance.ocneanuMarkovTrace` — the INSTANCE. There was no uniqueness
proof to generalise; there were missing instances, one per level.

### What landed
- `markovTraceOfWeight` — weight-generic constructor. Isolates which of the four
  MarkovTraceFamily axioms depend on the weight (three) and which does not
  (cyclicity — `seminormalRep` is an AlgHom, so `Matrix.trace_mul_comm` blockwise).
- `wenzlMarkovTrace` / `eq_wenzlWtrace_of_markov` — the level-r instance and
  uniqueness at every r, at z_r = Q^r/(q·[r]_Q), Q = q².
- `wenzlMarkovTrace_two_tr` — conservativity: at r = 2 the trace IS `wtrace`.
- `MarkovTraceFamily.param_eq` — z = tr₁(σ₀): the parameter is a value of the trace.
- `level_unique_of_wenzlMarkovTrace_eq` / `wtraceW_ne_of_level_ne` — distinct
  levels give distinct traces, separated at the single element σ₀ ∈ H_1(q).
- `realGen_of_sq_ne_one` — over ℝ, `hgen` follows from q² ≠ 1.

### The two uniqueness questions are different — do not conflate
- Trace given parameter: `markovTrace_unique`. A z has at most one trace. No levels.
- Level given parameter: `level_unique_of_markovParameter`. A z is hit by at most
  one level. No traces.
Neither implies the other. `level_unique_of_wenzlMarkovTrace_eq` is their composition
in the one direction that composes, and is a statement about neither alone.

### Second finding — the genericity hypothesis is vacuous over ℝ
Q = q² is a positive real, and a positive real is a root of unity only by being 1.
So "Q is not a root of unity" adds nothing over ℝ beyond q² ≠ 1. The scope notes on
the level-r files read as though it were a live restriction. Over ℂ or a cyclotomic
field it is; the ℝ specialisation is what is vacuous. It does not exclude the
substrate value — q₀² ≈ 1.232, so the level-r trace exists at q₀ for every r ≥ 1.

### Third finding — a stale open-item note, corrected
`WenzlWeightLevelR`'s "What is NOT here" recorded general-r branching as open on
bean qou-j7ln. That bean is completed and the identity is proved sorry-free in
three files that import it. The note was right about the literature (Pieri at the
principal specialisation is Orellana Lemma 5.1 via LR + rational continuation,
neither half in Mathlib) and wrong that "therefore open here" followed: the proof
that landed goes through `schurPrincipal_addCell_eq`'s β-factor form instead.

### Verification (no CI in this repo)
Whole affected chain rebuilt lean-direct in dependency order, all exit 0.
`#print axioms` on 15 declarations: [propext, Classical.choice, Quot.sound], no
sorryAx. `param_eq` needs neither Classical.choice nor a field.
Pre-verified in exact sympy first: z_r·q·(1−Q^r) − Q^r(1−Q) = 0 for r = 1..6.
`check-sidecars.sh` clean.
