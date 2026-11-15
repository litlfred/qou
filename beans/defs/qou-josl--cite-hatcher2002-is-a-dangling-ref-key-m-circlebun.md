---
# qou-josl
title: 'CITE: [hatcher2002] is a dangling Ref key — M — CircleBundleBettiObstruction.lean:63, and the Gysin count is ''cited not derived'''
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:04:51Z
updated_at: 2026-10-04T15:14:44Z
parent: qou-mub3
---

**Class M — a `-- Ref:` key that resolves to nothing, in a file merged this session.**

`folio/quantum-observable-universe/lean/QOU/Eightfold/CircleBundleBettiObstruction.lean:63`:

```
-- Ref: [hatcher2002] §4.D (the Gysin sequence of an oriented sphere bundle;
```

**`hatcher2002` does not exist in `content/schema/references.ts`.** Measured: zero
hits for `hatcher` anywhere in that file, and the string `hatcher2002` occurs
**exactly once in the whole corpus** — at this line. AGENTS.md §1 is explicit:
*"The `[key]` must match an entry in `content/schema/references.ts` exactly
(case-sensitive)."*

**Why it matters more than a typo.** The file's own docstring (`:38-52`, `:83`)
says the Gysin count **is** the model — *"the count is the model, cited"*,
*"**This is the model** — the Gysin count, cited not derived"* — and separates it
from what the file does prove (the case analysis, the `b₁ = 8` vs `0` recovery,
the scope-(b) conclusion that `M_S` is not `S³`). So the citation is the *only*
support for the load-bearing input, and it points at nothing.

**Fix.** Add a `ref()` entry:

- Hatcher, Allen, *Algebraic Topology*, Cambridge University Press, 2004
  (corrected reprint of 2002), ISBN 9780521795401, freely available at
  <https://pi.math.cornell.edu/~hatcher/AT/ATpage.html>. The Gysin sequence is
  **§4.D**, which the citation already gives — the locator is right, only the key
  is missing.

`references.ts` already registers uncheld books this way (`fulton-harris1991`,
`ratcliffe`), so no ingest is required; a `ref()` entry with ISBN/URL suffices.

**Three other non-conforming `-- Ref:` keys were found in the same sweep** across
`Eightfold/`, `QuantumObservableUniverse/`, `BringsSurface/` and `Archimedean/`
(70 distinct keys checked, 4 unresolved): `[ohtsuki2016-52]` (separate bean), and
`[conj:jet-convergence-classical-limit]` / `[conj:jet-filtered-knot-factor]` at
`Archimedean/SkewSYT.lean:1058,1113,1165` and `Archimedean/BranchingConvergence.lean:286`,
which are **content-block labels used in a bibliography slot** — arguably fine as
`[manuscript] conj:…`, which is the shape the rest of the corpus uses.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
