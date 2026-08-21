---
# qou-a4dr
title: 'DEFECT: triv_hecke / triv_wedderburn are PUnit instances that discharge the Hecke and Wedderburn class hypotheses for any R, n, q'
status: todo
type: task
created_at: 2026-08-21T15:17:07Z
updated_at: 2026-08-21T15:17:07Z
---

Found by the TL-arc Lean infrastructure survey, PR #5352, branch claude/tl-arc-lean-infra-2026-08-21. Ledger: docs/audits/2026-08-21-tl-arc-lean-infra-ledger.md.

WHAT.
content/quantum-observable-universe/lean/QOU/Mathlib/HeckeAlgebra.lean:151

  instance triv_hecke (R : Type u) [CommRing R] (n : ℕ) (q : R) :
      IwahoriHeckeAlgebra R n q where
    carrier := PUnit
    hecke_relation := True
    hecke_holds := True.intro
    braid_relation := True
    ...

and :166 instance triv_wedderburn does the same for WedderburnDecomposition
(block_proj _ := PUnit.unit, blocks_sum_to_one := True).

Because they are registered as *instance*, typeclass resolution discharges
[IwahoriHeckeAlgebra R n q] and [WedderburnDecomposition R n q] for ANY R, n, q.
The docstring states the purpose outright: 'Discharges the §3b-cond hypothesis at
the audit level'. That is AGENTS.md §1a audit-dodging: the class fields are
Prop-valued placeholders (hecke_relation : Prop with hecke_holds : hecke_relation)
filled with True.

SCOPE -- do not inflate this. Measured blast radius is TWO, and both are inside
the same file:

  grep -rn '\[IwahoriHeckeAlgebra|\[WedderburnDecomposition|\[WenzlBridge' \
    --include=*.lean content/quantum-observable-universe/lean/QOU/
  -> 2 hits, both in Mathlib/HeckeAlgebra.lean

So no downstream module is silently laundered today. Mathlib/WenzlBridgeConcrete.lean
(93 theorems) is explicitly independent of these class hypotheses and computes
scalar values in ℝ, so it is unaffected.

WHY IT STILL MATTERS. The instances are a loaded gun: the moment anyone states a
theorem with [IwahoriHeckeAlgebra ...] as a hypothesis intending it to mean the
real algebra, resolution will hand them PUnit and the theorem will be content-free
while looking conditional-and-honest. AGENTS.md §7 (no axiom/class may substitute
for a proof) and the §3b-cond non-degeneracy rule both bite here.

FIX OPTIONS, cheapest first.
1. Demote both from 'instance' to plain 'def' (triv_hecke_def / triv_wedderburn_def).
   They stay available as explicit witnesses that the classes are inhabited -- which
   is legitimate and useful -- but resolution can no longer apply them silently.
   This is the IsOcneanuWeightSystem pattern (QBeta/WenzlWeightVanishing.lean:376),
   which is deliberately NOT an instance for exactly this reason and says so.
2. Additionally, encode the class fields as real Props rather than
   'field : Prop' + 'field_holds : field' placeholders, so a trivial filler cannot
   typecheck.

Do 1 first; it is a two-word change and removes the hazard.

RELATED. qou-fpjy (class-carried inputs invisible to #print axioms) -- the same
blind spot is what lets this sit unnoticed: #print axioms on a downstream theorem
would report clean.
