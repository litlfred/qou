---
# qou-8urh
title: 'HUNT: does the primal LP the UIC Pass-2 sign gate invokes exist, and does complementary slackness on it yield the gate?'
status: completed
type: task
priority: normal
created_at: 2026-09-12T21:31:26Z
updated_at: 2026-09-12T22:22:39Z
---

## Scope

`hecke_core_legacy.unified_iterative_correction` Pass 2 (`:2176-2199`) keeps only
Wedderburn blocks with `final_tr_sign <= 0` and returns that gated sum. Its own
comment derives the gate from **complementary slackness on a primal LP**, and
that LP is not in the file. Owner ruled 2026-09-12 to *drop the gate* AND to
*hunt the primal LP*; this bean is the hunt. A separate agent drops the gate —
**this bean does not touch the producer.**

Three outcomes: (a) the LP exists and CS yields the sign gate — would REVERSE
the drop; (b) the LP exists and CS yields something else; (c) no such LP exists.

## Finding (preliminary, 2026-09-12)

The LP **exists** and is formalized sorry-free: `prop:operator-selection-lp`
(`content/quantum-observable-universe/mass-theory/operator-selection-lp.md`),
Lean `QOU.ParticleInteractions.operator_selection_lp`
(`.../lean/QOU/ParticleInteractions/operator_selection_lp.lean`). Verdict is
shaping as **(b)**: CS on it constrains the *selected operator's* Frobenius
constraint values `(Gx*)_i`, which are non-negative on every feasible point, so
`<= 0` collapses to `= 0`. The gate's quantity is the *cost* vector `t_lambda =
tr_lambda(W_atom)`, which is a different vector and is unconstrained in sign.


## SETTLED 2026-09-12 — case (b). Does NOT reverse the drop decision.

The LP **exists** (`prop:operator-selection-lp`, Lean
`QOU.ParticleInteractions.operator_selection_lp`, sorry-free) and complementary
slackness on it does **not** yield the sign gate. Outcome (a) was the only one
that would have reversed the owner's decision to drop, and it is refuted by an
explicit counterexample inside the LP itself.

**Four independent mismatches**, all proved sorry-free in
`QOU.MassTheory.UICGateNotFromComplementarySlackness` (8 decls, lean-direct
exit 0, `#print axioms` clean):

1. LP constraints are indexed by NF basis elements (`d = n!`); the gate by
   partitions (`p(n)`). No program in the corpus is declared with
   partition-indexed Frobenius constraints.
2. CS constrains `(Gx*)_i`, a function of the operator being SELECTED; the gate
   reads `t_lambda = tr(M_lambda(W_atom))`, an input.
3. `IsFeasible` demands `0 <= (Gx)_i`, so on a feasible point `<= 0` and `= 0`
   are the same predicate — a sign gate on a constraint value IS the tightness
   gate, which keeps only blocks at exactly zero.
4. The minimiser set is a positive-dimensional face, so "the OPTIMAL
   primal-dual pair" does not name a unique object.

**Scope (b) structural exclusion**, invariant named: primal feasibility of the
Frobenius constraints + orthogonality of the Wedderburn projectors (which makes
a block-indexed Gram diagonal, so CS decouples to `s_l G_ll x_l = 0` and never
mentions the atom traces). Independent of n, q, trace convention.

**Measured** (mp.dps = 70, proton pin, convention D; 12 assertions, all passed):

    gate  2H : 4 of 10 kept, only (2,1,1) non-zero; -0.41221219 -> -0.08955968
    gate  4He: 2 of 10 kept, (2,2) and (3,1);       -0.27423977 -> -0.08058675
    LP    both atoms, all five targets: 9 of 10 active

They do not coincide at any target for either atom.

**Two corrections of my own, both caught by measurement rather than reasoning:**

* I asserted `y_0* = 0` of the BLOCK instance. False: 0.0346905 (2H), 0.0129979
  (4He). `y_0_eq_zero_of_radical` needs the cost vector to BE a Gram row, true
  for the identity-containing NF basis and false for a diagonal one. Do not
  quote "the LP's y_0* is zero" without naming the basis.
* "No partition-indexed LP exists" was too strong — two probes build block-indexed
  INSTANCES. No PROGRAM is declared that way; the discriminator is now stated.

**Finding in the producer.** `hecke_core_legacy.py:328-374` already carries an
owner-ruled correction (PR #6752, 2026-09-05) saying its `y_lambda` are not LP
duals and its `y_0` is identically zero. It never reached the gate comment 1800
lines down. One file asserts both; the correction landed at the site carrying
the offending NAME, not the site carrying the offending REASONING.

Audit: `docs/audits/2026-09-12-uic-gate-primal-lp-hunt.md`. PR #7251.
`qou-zlra` and `qou-brng` appended and stay OPEN; `qou-t6be` is not on main
(PR #7237's branch) so its append went there as a comment.

Completed because the question this bean asks is now answered, not because
anything conjectural closed.
