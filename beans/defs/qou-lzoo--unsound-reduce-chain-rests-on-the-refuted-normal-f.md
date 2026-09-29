---
# qou-lzoo
title: 'UNSOUND: reduce chain rests on the refuted normal_form_exists — thread IsUnit(lc) through reduce and its 6 consumers'
status: completed
type: task
priority: normal
created_at: 2026-08-10T02:59:04Z
updated_at: 2026-08-10T04:29:18Z
---


---

## 2026-08-10 — done: the false axiom is gone from the tree

`normal_form_exists` is no longer an axiom anywhere in UGB. It is a **theorem**
in `Basic.lean` §6, from `reduction_well_founded` plus
`hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)`, and **without** the `hgs` it used to
take (existence is pure termination; confluence has nothing to do with it).

`reduction_well_founded` moved `CompositionLemma` → `Basic` so `reduce` could be
defined from the proved statement rather than the false one. Same namespace, so
no call site changed on that account.

Threaded `hlc` through exactly the sites that needed it — four, all found by the
compiler:

| site | disposition |
|---|---|
| `reduce`, `reduce_is_normal`, `reduce_reduces` | takes `hlc` in place of `hgs` |
| `composition_lemma`, `retraction_property` | takes both — `hlc` makes `reduce` defined, `hgs` makes its value canonical |
| `unital_groebner_decomposition`, `pbw_corollary`, `main_theorem_statement` | `hlc` added as a hypothesis |
| `ugb_pbw_corollary` | `hlc` added as a hypothesis, **not** discharged — see below |

### Why `ugb_pbw_corollary` does not discharge it

`qSerreRewritingSystem` is **itself an axiom**, so its rules cannot be inspected
to show their leading coefficients are units. Asserting monicity as a fresh
axiom to discharge this one would be assuming the thing rather than proving it
(§"Axiomatization is NOT a Proof"), so the hypothesis stays visible in the type.
The honest close is a strengthened specification of `qSerreRewritingSystem`
carrying monic rules — the q-Serre relations are monic by construction, each
oriented so its leading monomial has coefficient 1. Left for whoever de-axiomatises
that system.

### Verification

`#print axioms`, after — no result in the main-theorem chain mentions a false
axiom, and `normal_form_exists` is not an axiom at all:

```
normal_form_exists                  + reduction_well_founded
reduce                              + reduction_well_founded
composition_lemma                   + local_confluence, reduction_well_founded
retraction_property                 + local_confluence, reduction_well_founded
unital_groebner_decomposition       + gs_implies_flat, reduction_well_founded
pbw_corollary                       + local_confluence, reduction_well_founded
main_theorem_statement              + local_confluence, reduction_well_founded
ugb_pbw_corollary                   + local_confluence, reduction_well_founded,
                                      pbw_monomials_are_normal_forms,
                                      qSerreRewritingSystem, qSerre_is_gs_basis
```

All 28 UGB modules compile with `lean`-direct, exit 0. Zero `sorry` in the tree
— the five `sorry` hits in these files were **stale prose** in module docstrings
("the single remaining `sorry` is the existence/termination half"), which was
false after this change and is corrected; `Quotient.lean`'s "five standing
axioms" is now "two".

### The framework's standing axioms are now two

`reduction_well_founded` (Dershowitz–Manna termination) and `local_confluence`
(the S-polynomial case analysis). Both have real mathematical content and are
untouched. That is the honest floor for the diamond lemma; `NormalFormBasis` and
`CompositionDiamond` remain unproved definitions.
