---
# qou-e4eu
title: '19 Lean -- Ref: keys resolve to nothing — 7 of them are not citations at all'
status: todo
type: bug
priority: high
created_at: 2026-08-31T05:06:11Z
updated_at: 2026-08-31T05:06:46Z
---

`folio-assistant/content/pipeline/validate-references.ts` is the only checker
that cross-checks Lean `-- Ref: [key]` against `content/schema/references.ts`.
**It has never been runnable in this folio**, so its surface has never been
measured. Made runnable via `scripts/run-validate-references.ts`; first run
reports **19 errors, 173 warnings, 411 info** over 367 Lean / 189 LaTeX / 345
`.ts` citations.

## Why it never ran — TWO stacked blockers, not one

1. **No registry.** It imports `references` from the DI shim at module scope
   and touches it in the schema loop before anything else, so running it
   directly throws immediately: *"Reference registry not configured."* No
   partial run.
2. **`requirePaper`.** Past that, it throws again at line 133: *"5 papers found
   (bach2013-double-slit, fred2005-formal-groups, quantum-observable-universe,
   unital-groebner-bases, visualizer) — name one explicitly."* It accepts
   `--paper`, which nothing passed.

Nothing invokes it either — no workflow, no script, no `package.json` entry;
every other mention of the name in the tree is prose describing what it would
do. Same defect family as `qou-cite`/`qou-idxg`.

## The 19, and they are two different things

**Twelve are real works missing from the bibliography** — all standard,
identifiable, and attached to `sorry` justifications:

`frenkel2020`, `koroteev-zeitlin2022`, `stanley1999ec2`, `rockafellar1970`,
`schrijver1986`, `murakami1996`, `neumann1985`, `bjorner-brenti2005`,
`wielenberg1978`, `ratcliffe2006`, `murakami2013`, `ggmw2020`.

**Seven are not citation keys at all** — a different convention leaking into
the citation slot:

`audit`, `probe`, `probe-w`, `probe-j`, `probe-q`, `bean`, `metallichierarchy`

concentrated in `QOU/AlgebraicSubstrate/MetallicLPIdentities.lean` and
`QOU/KnotTheory/MetallicPiecewise.lean`. An author used `-- Ref:` to point at
an audit doc, a probe script, or a bean. Those are legitimate things to point
at; `-- Ref:` is not the slot for them, because the slot means "the published
work justifying this `sorry`".

## Why this matters more than `qou-cite`'s ten

`qou-cite`'s ten orphaned `cites[]` keys support no written claim. **These do.**
AGENTS.md §1 makes `-- Ref:` the mandatory justification for a `sorry` — *"A
`sorry` without `-- Ref:` is always a review failure"* — so a `-- Ref:` naming
nothing is a `sorry` whose stated warrant does not exist. Seven of them name a
kind of thing that could never be a warrant.

## Next

- Add the twelve to `references.ts` (ordinary bibliography work, each is a
  well-known text).
- Decide what the seven should be: either a real citation, or `[manuscript]`
  per §1, or a non-`Ref:` comment form pointing at the audit/probe/bean.
- Wire `scripts/run-validate-references.ts` into the preflight so this cannot
  silently regrow.
