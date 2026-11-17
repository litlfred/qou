---
# qou-6dzi
title: triv_hecke and triv_wedderburn are globally registered PUnit instances that discharge real hypotheses by typeclass search
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T16:32:45Z
updated_at: 2026-10-04T15:25:12Z
parent: qou-6qbv
---

Branch `claude/wedderburn-instance-artin-2026-08-21`, PR #5387.

Opened because the finding was cited to me as bean `qou-h56b`, and **that bean
does not exist** -- `beans show qou-h56b` returns "bean not found", and grep over
`.beans/` for `triv_wedderburn` returns zero files. The CODE is real and is
verified below; only the bean reference was phantom. Recording it so the next
agent has an ID that resolves.

## THE CODE

`folio/quantum-observable-universe/lean/QOU/Mathlib/HeckeAlgebra.lean`:

- `:118` `class WedderburnDecomposition (R) [CommRing R] (n) (q : R)
  [H : IwahoriHeckeAlgebra R n q]` -- fields `blocks_sum_to_one : Prop` +
  `blocks_sum_holds : blocks_sum_to_one`, `blocks_orthogonal : Prop` +
  `blocks_orthogonal_holds`. These are Prop-VARIABLE fields: the class does not
  say WHAT is asserted, only that something is.
- `:166` `instance triv_wedderburn (R) [CommRing R] (n) (q : R) :
  WedderburnDecomposition R n q` -- fills them with `True` / `True.intro`,
  `block_proj _ := PUnit.unit`. GLOBALLY REGISTERED.
- `:151` `instance triv_hecke ... : IwahoriHeckeAlgebra R n q` with
  `carrier := PUnit`, every relation `True`. Also globally registered.

## WHY THIS IS WORSE THAN A LOCAL VACUITY

`triv_hecke` being a global instance means that even a GENUINE
`WedderburnDecomposition` instance would be shadowed: typeclass search finds the
PUnit Hecke algebra first and discharges the `[IwahoriHeckeAlgebra R n q]`
hypothesis with it. So the whole `QOU/Mathlib/HeckeAlgebra.lean` class family
currently discharges by search, with no content, at every hypothesis site.

The file's own docstring is honest about intent ("Discharges the 3b-cond
hypothesis at the audit level; genuine instances at R = Q(q) arrive when
Mathlib's Iwahori-Hecke library lands"), and it deliberately declines to give a
trivial `MarkovTrace` because `tr(1) = 1` forbids the constant-zero map. The
problem is the global registration, not the existence of a placeholder.

## DISTINGUISH FROM THE OTHER TWO OBJECTS OF THE SAME NAME

Three distinct things share the `WedderburnDecomp*` name; do not conflate them.

1. `QOU.Hecke.WedderburnDecomp` -- `QOU/Hecke/Wedderburn.lean:72`. A class with
   NINE fields, all GENUINE Props (real equations, not Prop-variable). No
   instance in the tree. This is the one `qou-luq7` and `qou-hah4` are about.
2. `QOU.Mathlib.HeckeAlgebra.WedderburnDecomposition` -- the subject of THIS
   bean. Prop-variable fields, trivial global instance.
3. `QOU.HeckeAlgebra.Wedderburn.WedderburnDecomposition` --
   `QOU/HeckeAlgebra/Wedderburn.lean:68`. Not a class at all:
   `abbrev ... : Type := forall (lam : Nat.Partition n), Matrix ...`, a function
   type. Carries `axiom wedderburnEmbed` at `:110`.

## FIX OPTIONS (not done here -- needs coordination, it is not this branch's file)

[ ] 1. De-register: make `triv_hecke` / `triv_wedderburn` plain `def`s, or
       `scoped instance`s in a namespace callers must opt into. The precedent
       is in this branch: `QOU/Hecke/WedderburnRankDegeneracy.lean` keeps its
       degenerate witnesses `scoped` for exactly this reason.
[ ] 2. Replace the Prop-variable fields with the real equations, as
       `QOU.Hecke.WedderburnDecomp` already does.
[ ] 3. Decide whether this class family is still wanted at all now that
       `QOU/Hecke/*` carries a genuine `HeckeAlgebra` class with real
       instances at n = 2, 3, 4 (PR #4857).

## Progress Update (Round 58 — PR #8304)
- **Status:** `in-progress` (opened `litlfred/qou#8304`, branch `claude/round58-devacuify-6qbv-b9cj`, HEAD `e72e4e04168ffebca669be8e58b6df711ee7f5ed`, C1 `e3528dd09222e2ddccf5556168d0aa31aca7f5d7`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean` + 80-dps witness `computations/probes/round58-devacuify-6qbv-b9cj.witness.json` (`scriptHash = a44d91e59ddc`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:34:25Z`.
