---
# qou-jv64
title: 'A=3 magnitude ROUTE 1: operator-valued branching combiner'
status: completed
type: task
priority: normal
tags:
    - a3-cross-channel
created_at: 2026-08-01T23:37:11Z
updated_at: 2026-08-01T23:48:59Z
---

## Verdict — REFUTE (scope-(b) structural exclusion)

ROUTE 1 tested the qou-tnvz surviving hypothesis: keep the operator (matrix)
structure through the H9->H6->H3 Wenzl branching (instead of collapsing to a
scalar Sigma_lambda y_lambda chi_lambda trace at each level), on the premise that
a single trace loses cross-channel info the branching retains, thereby supplying
r* = mu3/c3 ~ 1.585 (mu3=+0.4708, c3=0.297).

Premise is FALSE at the observable level. The observable is a cyclic additive
trace tau of the assembled operator sliced by the branching's isotypic projectors
{P i}. Governing invariant (PROVED): partition-of-unity trace collapse
tau X = Sigma_i tau(P_i X P_i) -- off-diagonal blocks vanish under the closed
trace, per-block weight identically 1. So the block-resolved operator-combiner
readout EQUALS the scalar Markov trace EXACTLY: keeping operator structure
multiplies by factor EXACTLY 1.0 (0% of needed +58.5%; gap ==0). Reproduces
c3=0.297, never mu3=0.4708.

Numerical shadow (independent): canonical_tr_m_via_branching.py already records
branching == fine-Bratteli transfer trace to 4.7e-15 for A>=3.

By how much: weightedReadout_sub_trace proves the ONLY way a block decomposition
yields a value != tau X is a non-uniform per-block weight w_i != 1 = a
Delta_lambda per-partition weight, a DIFFERENT functional than the trace
(Delta_lambda gate; a fit if inverted from mu3). The combiner does NOT retain it.

NOT excluded: the non-uniform w_i / Delta_lambda route stays open (A=4 PROBE-2
geometric-W_lambda bracket is the live instance of such a w_i).

Lean: content/quantum-observable-universe/lean/QOU/BraidKnot/A3OperatorCombinerMagnitude.lean
sorry-free, lean-direct exit 0, v4.24.0, generic [CommRing R]. Decls:
trace_partition_collapse, operatorCombiner_eq_scalarTrace, weightedReadout_sub_trace,
weightedReadout_eq_of_uniform, magnitude_change_forces_nonuniform_weight.
Audit: docs/audits/2026-08-01-a3-magnitude-operator-branching-combiner.md.
Ledger: docs/coordination/option-e.md row appended.
Branch: claude/a3-magnitude-operator-branching-combiner-2026-08-01.
Nothing wired; mu3 never inverted; free_parameters=0.
