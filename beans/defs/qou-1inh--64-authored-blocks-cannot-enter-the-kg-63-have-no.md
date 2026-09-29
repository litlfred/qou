---
# qou-1inh
title: 64 authored blocks cannot enter the KG — 63 have no label, 1 is in a nested subdir
status: todo
type: task
created_at: 2026-09-27T05:11:12Z
updated_at: 2026-09-27T05:11:12Z
---

## Measured, both causes identified rather than guessed

After a full `gen-block-jsonld` run wrote **3613** siblings, the corpus holds
**3677** blocks (a `.ts` with a same-named `.md`). So **64 blocks have no
`.jsonld` even after regeneration**, and they split cleanly:

| cause | count |
|---|---|
| no `label:` field at all | **63** |
| in a nested chapter subdirectory | **1** |

### The 63 — no label, so no `@id`, so not a graph node

They are `prose({ title: … })` and nothing else:

```ts
import { prose } from "../../schema/builders";
export default prose({
  title: "Chapter close — Braids and Knots",
});
```

`blockToJsonLd` mints the node identity with `mintNodeId(loaded.label, paper)`.
A block with no label has no identity, so it **cannot** be a node — this is a
design consequence, not a generator bug.

They are mostly `outro-*` / `intro-*` connective material, by directory:
`mass-theory/` 16, `predicted-spectra/` 7, `knots-particles-confinement/` 4,
`quantum-observable-universes/` 4, `mass-endomorphism/` 3,
`nuclear-interactions/` 3, `stochastic-mechanics/` 3, `brings-surface/` 2, tail.

**My first hypothesis was wrong and is recorded so nobody repeats it.** I guessed
these were *orphans* — authored pairs no chapter manifest references. Measured:
`outro-braids-and-knots` **IS** referenced in
`braids-and-knots/braids-and-knots.ts`. They are in the rendered paper and absent
from the graph.

### The 1 — nested subdirectory

`content/quantum-observable-universe/nuclear-interactions/audit/wigner-su4-alpha-cluster-probe`
has a `label:` and still gets no sibling. Confirmed cause: **0** of the 3613
`.jsonld` live at `content/<paper>/<chapter>/<subdir>/<block>` depth and all 3613
live at `content/<paper>/<chapter>/<block>`, so the generator does not walk
nested chapter subdirectories.

## Why this is filed and not fixed

Adding `label:` to 63 blocks **changes the corpus**: a label is a citable
identity, it becomes a `\hyperref` target, and it enters the `uses[]` namespace
where a collision is a validation error. Which 63 labels, and whether a chapter
close should be citable at all, is an authoring decision. AGENTS.md's
ASK-THE-OWNER rule puts exactly this outside an agent's remit — it is neither a
precision fix nor corpus-derived.

The nested-subdir one is smaller but is a **platform** fix (the generator's walk),
not a qou fix.

## Consequence to be aware of

The `kg-vocabulary-gate` workflow added alongside this deliberately does **not**
report these 64 as drift — a gate that did would fail on every PR forever. So
their absence from the KG is silent, which is the reason this bean exists rather
than a comment in the workflow.

Under the KG-as-authority ruling these 64 are blocks a reader sees in the paper
and a graph consumer cannot find at all.
