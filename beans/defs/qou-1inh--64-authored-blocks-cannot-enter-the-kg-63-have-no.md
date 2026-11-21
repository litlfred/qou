---
# qou-1inh
title: 64 authored blocks cannot enter the KG — 63 have no label, 1 is in a nested subdir
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T05:11:12Z
updated_at: 2026-11-21T12:30:00Z
parent: qou-n4r9
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

`folio/quantum-observable-universe/nuclear-interactions/audit/wigner-su4-alpha-cluster-probe`
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

## Owner ruling & PR (2026-11-15, `Q-N4R9-1 = 2`)

- **Owner ruling (`Q-N4R9-1 = 2`, 2026-11-15):** Mint deterministic `prose:<stem>` labels for the unlabeled `prose(...)` blocks and generate their `.jsonld` companions alongside the nested `nuclear-interactions/audit/wigner-su4-alpha-cluster-probe` block.
- **Measured on `origin/main` (`05005d77682`) and implemented in `litlfred/qou#7999` (`7f54f30e7e9f44d6b242c3421ddba5ee7a464904`):**
  - Added deterministic collision-free `label: "prose:<stem>"` to all **67** unlabeled `prose(...)` `.ts` manifests under `folio/quantum-observable-universe/` (using `label: "prose:stochastic-mechanics-outro-braids-and-knots"` on `stochastic-mechanics/outro-braids-and-knots.ts` to disambiguate from `braids-and-knots/outro-braids-and-knots.ts`).
  - Generated `.jsonld` companions for all 67 newly-labeled `prose` blocks plus `folio/quantum-observable-universe/nuclear-interactions/audit/wigner-su4-alpha-cluster-probe.jsonld` (`rem:wigner-su4-alpha-cluster-probe`) at the pinned platform (`82b389982a73701b77f723d34d42c77acf41b5b4`).
  - Verified zero `.md` or `.lean` changes and unchanged `scripts/run-validate.ts` baseline (14 issues, 0 new issues).
  - Kept `status: in-progress` pending merge of `litlfred/qou#7999`.


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- PR #7999 is merged. On main, 88 `.ts` manifests under `folio/quantum-observable-universe/` carry `label: "prose:…"` (67 were added by #7999; the rest were labelled since), and `nuclear-interactions/audit/wigner-su4-alpha-cluster-probe.jsonld` exists. Both causes in the title are fixed.
