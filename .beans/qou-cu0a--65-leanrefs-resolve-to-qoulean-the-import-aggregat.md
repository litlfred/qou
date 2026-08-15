---
# qou-cu0a
title: 65 lean.refs resolve to QOU.lean (the import aggregator) — checkers audit an import list and pass vacuously
status: todo
type: task
priority: normal
created_at: 2026-08-15T20:32:39Z
updated_at: 2026-08-15T20:32:39Z
---

Found while adjudicating `def:yekutieli-triple` (session `qou-xz6t`, branch `claude/mtcx-7c-verify-close-2026-08-15`).

## The failure mode — silent, not loud

A `lean.ref` naming a declaration that does not exist does **not** resolve to nothing. `parseLeanRef` splits at the last dot, so `qou:QOU.YekutieliTripleMapping` has module `QOU` — and the resolver's final *safe fallback* returns the direct module-path file, `lean/QOU.lean`. That is the **954-line root import aggregator**: a file of `import` lines that declares nothing.

Every checker consuming such a block's `.lean` therefore audits a bare import list — and **passes**. `wall-side-correct` sees no archimedean markers: pass. `q-usage-*` sees no `q`: pass/na. `proof-no-bare-sorries` sees no `sorry`: pass. The block looks formalised and green while nothing of the kind was checked.

This is worse than an unresolved ref, which at least yields an honest `n/a`.

## Measured across the corpus (2026-08-15)

Scanned every `.ts` block under `content/quantum-observable-universe/` carrying a `qou:` ref, resolving through the canonical `qa-utils.resolveCanonicalLean` with a shared Lake-tree cache:

| | count |
|---|---|
| blocks with a `qou:` lean.ref | 1220 |
| **resolve to `QOU.lean` (aggregator)** | **65** |
| unresolved (no file at all) | 319 |

Examples: `braids-and-knots/so3-generators.ts` (`qou:QOU.So3Generators`), `brings-surface/hyperelliptic-quintic.ts` (`qou:QOU.HyperellipticQuintic`), `fluid-dynamics/observable-mtc.ts` (`qou:QOU.ObservableMTC`), `information-theory/q-heat-kernel-peter-weyl.ts` (`qou:QOU.qHeatKernelPeterWeyl`).

The common shape is a **single-segment decl name** (`QOU.Foo`): module `QOU` → `QOU.lean`.

## This is a deliberate trade-off, not an implementation bug

`resolveCanonicalLean` already *has* aggregator rejection — candidate (a) is gated on `fileDeclaresName`, and candidates (b)/(c) try basename and fully-qualified-decl lookups. But the function ends with:

```
// (safe fallback) preserve legacy behaviour: a ref that resolved to the
//   direct module-path before the (a)-gate still resolves to it, so no
//   previously-resolving ref regresses to `undefined`.
if (directExists) return direct;
```

So the gate fires and the fallback hands the aggregator back anyway. That choice was made to avoid regressing refs to `undefined`; the cost, now measured, is 65 vacuous passes. **The question this bean poses is whether an honest `n/a` beats a false green** — I did not change the resolver, since that is a folio-assistant-side policy call with corpus-wide blast radius.

## Options

1. **Per-block (safe, incremental).** Repoint each of the 65 at a real module, as done for `yekutieli-triple.ts` in this branch. Note the module segment must be the **file**, not the Lean namespace — see that block's comment for the trap.
2. **Resolver-side (one change, corpus-wide).** Drop or narrow the safe fallback so an aggregator-only match returns `undefined`. Turns 65 false greens into honest `n/a`s; needs a folio-assistant PR + a re-sweep, since cached sidecar verdicts would flip.
3. **Checker-side.** Have the QA layer treat "resolved file declares nothing / is import-only" as `n/a` regardless of how resolution got there.

## Relation to existing beans

Distinct from `qou-qe41` (29 sibling stubs with no candidate-2 resolution) and `qou-ref10` (ten refs with no formalisation): both are about refs that **fail** to resolve. This bean is about refs that **succeed** into the wrong file and therefore never surface. The 319-unresolved figure above suggests those two beans undercount their own class as well.
