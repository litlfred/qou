---
# qou-e15u
title: 'main regression: theorem() with conj: label — motivic-perpetual-obstruction has not loaded since 1d3988bc31'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T20:53:15Z
updated_at: 2026-08-22T20:53:43Z
---

## The defect

`1d3988bc31` ("docs(motivic): rewire 15 downstream blocks — conjecture → theorem")
changed the builder on
`content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.ts`:

    -import { conjecture } from "../../schema/builders";
    +import { theorem } from "../../schema/builders";
    -export default conjecture({
    +export default theorem({
       label: "conj:motivic-perpetual-obstruction",

and states, in its own commit message, *"Label conj:motivic-perpetual-obstruction
preserved for link stability."* The schema rejects exactly that pairing:

    { "code": "invalid_string",
      "validation": { "startsWith": "thm:" },
      "message": "Label for theorem must start with \"thm:\"",
      "path": ["label"] }

So the block has **thrown at import** — not merely failed a rule, *not loaded at
all* — since that commit landed. The rationale failed on its own terms: keeping
the `conj:` label to preserve links is what broke every link to it.

## Blast radius, measured

QOU paper validate on `origin/main`: **5 issues → 21**.

- 15 blocks: `Undefined cross-reference(s) in .md: conj:motivic-perpetual-obstruction`
- `chi-minus-six-chain`, `perpetual-obstruction-depth-omega`: `Unresolved uses` (hard ✗)
- `perpetual-obstruction-depth-omega`: `interprets` target not found (hard ✗)

## Why nothing caught it

Same shape as `qou-lwyo`: the commit's verification was the **Lean** build, and
the break is **content-pipeline**. Two verification surfaces; the failure landed
in the one that was not run. CI is `workflow_dispatch`-only, so nothing else ran
either.

## Fix (on PR #5462, riding the active motivic branch)

Rename the label `conj:` → `thm:` — which is what the commit intended, since the
`.md` has read **"Theorem (motivic perpetual obstruction)"** since the Route-A
proof landed. 29 occurrences across 22 files: `.ts` labels / `uses` / `interprets`
/ chapter manifests, `.md` cross-references, `foreshadows.json`, and the `.lean`
doc-comment `LaTeX label:` lines.

**`.qa.json` sidecars deliberately not rewritten** (3 files, 3 occurrences). They
record what a reviewer saw at a given content hash; editing the label inside a
recorded verdict would falsify the record. The `.md`/`.ts` edits stale their
`field_hash` anyway, so the checkers re-run on their own.
