# The general-`n` OV / Identity-I chain is closed — measured, 2026-08-25

**Verdict.** Bean `sv8b` ("GAP: `seminormalVector_base_exists` — the last labelling sorry"),
priority **high**, status **todo**, describes a gap that **no longer exists**. So does the
s5-so3 keystone ledger's statement that *"only the general-`n` discharge … remains open"*.
Both are corrected here.

This audit records the measurement, not new mathematics. No Lean was written for it.

## What was measured

The bean carries an explicit caveat — *"Do not audit sorry-status from restored oleans"* —
because a restored `lake-cache` tree once reported a **phantom** `sorryAx` that vanished on a
source rebuild. The root Mathlib cache in this container is restored (`oleans=6990 traces=0`),
so that caveat applies directly.

Accordingly the entire transitive `QOU.*` import cone was **rebuilt from source** with
`lean -o`, in topological order, before any axiom was printed:

```
CONE_REBUILD_DONE  files=115  failures=0
EXTRA_DONE         files=4    failures=0
```

`#print axioms` against that fresh cone:

| declaration | axioms |
|---|---|
| `SeminormalBaseExists.seminormalVector_base_exists'` | `propext, Classical.choice, Quot.sound` |
| `JucysMurphy.seminormalVector_base_exists` | `propext, Classical.choice, Quot.sound` |
| `SnIsotypicSpechtSplitInstance.instSnIsotypicSpechtSplit` | `propext, Classical.choice, Quot.sound` |
| `OVTopAssembly.identityB_general` | `propext, Classical.choice, Quot.sound` |
| `PlancherelSnDataGeneral.plancherelSnDataGeneral` | `propext, Classical.choice, Quot.sound` |
| `PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general` | `propext, Classical.choice, Quot.sound` |
| `PlancherelSnDataGeneral.twoM_eq_plancherel_hook_sum_general` | `propext, Classical.choice, Quot.sound` |

**No `sorryAx` anywhere.** Every file in the chain also carries zero literal `sorry`.

## What that means, stated carefully

1. **`sv8b` is closed.** `seminormalVector_base_exists` is proved, not stubbed. It could not be
   discharged in place — the proof runs through `ColSuperstandardEigen.jm_eigen_colSuperstandard'`,
   which is *downstream* of the statement — so it is stated and proved again in
   `SeminormalBaseExists.lean` and the upstream declaration delegates to it. That indirection is
   why a grep for `sorry` in `JucysMurphy.lean` and a glance at the bean disagree.

2. **The conditional class is inhabited.** `SnWedderburnPartitionBridge.SnIsotypicSpechtSplit` was
   the §3b-cond carrier for the isotypic Wedderburn split; `SnIsotypicSpechtSplitInstance` provides
   an instance for every characteristic-zero field. Results carrying `[SnIsotypicSpechtSplit ℚ]`
   are therefore unconditional, not merely conditional-proved.

3. **Identity I holds at every `n`, with no hypothesis.**
   `PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general` and
   `twoM_eq_plancherel_hook_sum_general` take no class argument. The per-`n` `decide` instances
   (`n = 2 … 12`) remain registered and remain the ones instance resolution picks inside their
   range; `plancherelSnDataGeneral` is deliberately a `def` rather than an `instance`, because
   `PlancherelSnData` carries **data** and a competing general instance would make `h.parts` /
   `h.dim` depend on which one resolution chose.

## What is corrected

| artifact | said | says now |
|---|---|---|
| `docs/coordination/s5-so3-keystone.md` §status | "Only the **general-`n`** discharge … remains open, scoped as the P1–P5 program" | closed; the P1–P5 program is complete for this target |
| `docs/coordination/2026-06-29-ov-standard-basis-brick4.md` | `identityB_general` axioms `[propext, sorryAx, …]` | accurate when written; superseded — now `sorryAx`-free |
| bean `sv8b` | todo / high / "single highest-value open lemma" | completed |

The brick4 line was **correct on the day it was written**; it is superseded rather than wrong,
and is annotated in place rather than edited away.

## The lesson worth keeping

This was found by attempting to *work* `sv8b`, not by auditing it. A high-priority bean pointing
at closed work costs the next agent a session — this session nearly spent one — and it is the
mirror image of the failure the corpus-grep checklist exists to prevent. Beans go stale exactly
as source-file `## Status` notes do, and the same rule applies: **the corpus is the source of
truth, and the corpus means a source-rebuilt `#print axioms`, not a docstring and not a bean.**

Bean `sv8b` itself warned about this class of error, in its own caveat, about its own file.
