---
# qou-7ase
title: UnifiedKnotMass class fields are pinned to their own zero stubs
status: completed
type: task
priority: normal
created_at: 2026-08-27T11:56:04Z
updated_at: 2026-09-03T10:28:31Z
---

Machine-checked 2026-08-27 (bean qou-0avp). Full analysis:
docs/audits/2026-08-27-unified-knot-mass-class-is-unsatisfiable.md
Reproduce: scripts/lean/probes/unified-knot-mass-satisfiability.lean (lean exit 0).

## The defect

In content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean,
`class UnifiedKnotMass` ties two of its three mass terms to stub definitions:

    def descendedMarkov (q : ℝ) (_braid : Unit) : ℝ := 0 * q
    def braneTower      (q : ℝ) (_braid : Unit) : ℝ := 0 * q

    descended_is_markov : descended = |descendedMarkov q braid|
    tower_is_phi_q_sum  : tower     = braneTower q braid

so every instance is FORCED to `descended = 0` and `tower = 0`. The class field
does not say "descended is whatever prop:categorical-mass-markov yields"; it says
`descended = |0 * q|`. The antecedent is one no intended model can satisfy.

`trivial_vortex_vacuum_mass` then assumes `h_desc : U.descended = 1` (correctly:
tr(1) = 1 for the identity of H_n(q)), which CONTRADICTS the class. Verified:

    (U : UnifiedKnotMass) → U.descended = 1 → False
    ... and therefore also  U.total_mass = 12345

Its sibling hypothesis `h_tower : U.tower = 0` is redundant — the class already
forces it. One hypothesis restates the class, the other refutes it.

## What is NOT the problem

The stubs are DISCLOSED and no instance is ever constructed — both correct. Do
not "fix" this by deleting the stubs or by constructing an instance. The failure
is AGENTS.md §3b-cond item 5 (non-degeneracy): a conditional class must
axiomatise the HYPOTHESES so the theorem derives its conclusion from them.

## Candidate fix (not yet chosen — needs the block's author)

Replace the two pinning fields with genuine hypotheses, e.g. carry `descended`
and `tower` as opaque quantities constrained by the properties the downstream
props actually establish, rather than by an equation to a zero stub. Then
`trivial_vortex_vacuum_mass`'s `h_desc` becomes a real assumption and its proof
becomes a real derivation.

This is a content change to a mass-theory block (.lean + .ts + .md siblings, plus
the appendix-mass-binding-algorithms sync rule) and needs its own review. It was
deliberately NOT done on the audit branch.

## Two further findings in the same file (see the audit doc)

- frobenius_codim_trace_n2/n3/n4/n5: three axioms were removed by moving their
  content into `match` arms of `frobeniusCoCasimirTrace`, where the theorems read
  them back by `rfl`. Strictly worse than the axioms — `#print axioms` saw those
  and cannot see a def arm. The VALUES are separately derived in
  frobenius-codim-universal.lean, but nothing in Lean links an arm to its
  companion theorem.
- frobeniusCoCasimirTraceFallback: docstring says "returns 0 for every n >= 6",
  body is `(n : ℝ)`. Carries the Frobenius term for every nucleus past the
  smallest.

Completed 2026-09-03 on owner decision (session qou-ggdk): addressed by the UnifiedKnotMass rewrite on claude/standard-model-terms-status-ftoejr (class unpinned, partition sum proved, electron-mass literal removed; audit 2026-09-03-sm-surface-lean-best-practices-sweep.md §3.6).
