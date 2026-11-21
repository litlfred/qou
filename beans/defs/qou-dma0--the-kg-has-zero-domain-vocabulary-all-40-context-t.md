---
# qou-dma0
title: The KG has ZERO domain vocabulary — all 40 context terms are structural
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T05:11:12Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

## Where this came from

Owner, 2026-09-27, answering the `@type` prefix question with a question:
**"use qou: prefix?"**

The answer for `@type` is no — `@type` names the block KIND (`Remark`,
`Proposition`, `Theorem`), that taxonomy types blocks in all **four** folios in
this repo, it sits beside `doco:Section` (DoCO, a published standard), and `qou`
is not defined in the context at all so `qou:Remark` would expand to nothing.
Paper identity needs no prefix either: `@base` is
`https://litlfred.github.io/folio/` and `@id` is `papers/<paper>/blocks/<label>`,
so the paper is already a path segment.

**But the question found something real, which is why this bean exists.**

## The gap, measured

`folio-assistant/cat-harness/ns/content/v1.jsonld` at the pinned platform defines
**10 prefixes** and **40 terms**. Every one of the 40 is **structural**:

    label  kind  title  tags  text  meta  provenance  uses  cites  defines
    interprets  examples  proofs  foreshadows  narrative  derivedFrom  contains
    leanRef  leanSource  sorryFree  strength  refs  sourceDocument  pageStart
    pageEnd  file  format  headers  header_vocabulary  sheets  n_sheets
    archive  entries  n_entries  n_files  n_directories  uncompressed_bytes
    source  $schema  @version

Each maps to `folio-assistant-core:` or an external standard (`cito:`, `dcterms:`,
`prov:`, `doco:`, `skos:`, `oa:`, `csvw:`, `deo:`, `fhir:`).

**ZERO domain terms.** Nothing for `q₀`, the Markov parameter `z`, convention C
vs D, Wedderburn blocks, the partition weights `y_λ` / `w_λ(q)`, the CAL-1/2/3
triple, `ℏ_q`, `Vol(4₁)`, the L1/L2 precision legs — none of the vocabulary this
paper is *about*.

## Why that matters under the 2026-09-26 ruling

The owner's ruling makes the KG *"the json(ld)+scheme as authority of
public/rendered content"*. As it stands the graph records **that** a block is a
`Proposition` and **what** it `uses` — and nothing about the physics or
mathematics it asserts. So a consumer can ask "which propositions depend on
`def:markov-trace`" and cannot ask "which blocks are convention-D", "which pin
to the proton anchor", or "which assert a value compared against CODATA".

Every one of those questions is currently answered by **grep over prose**, which
is exactly the fragility AGENTS.md's corpus-grep checklist opens by naming: *"a
grep finds prior work only if it used your words."*

## What this is NOT

- **Not** a rename of `@type`. That is settled and landed
  (`folio-assistant-core:`, PR for the 3613-file regeneration).
- **Not** a platform change. A `qou:` namespace for domain terms is **additive**:
  the platform owns the structural vocabulary, a folio would own its domain
  vocabulary, and a JSON-LD `@context` composes the two.

## Open questions, none of them mine to settle

1. **Does the platform support a per-folio context extension at all?** Still
   unmeasured as a *capability* — the generator emits a single
   `"@context": CONTENT_CONTEXT_URL` string, and whether it can emit an array
   (`[platform, folio]`) has not been tested.

   **But where the work would have to happen IS now measured, and it is not
   here.** qou holds **no schema of its own**. `content/schema/` is 59 lines of
   pass-through:

   | file | lines | content |
   |---|---:|---|
   | `types.ts` | 5 | `export * from ".../cat-harness/schemas/types"` |
   | `constraints.ts` | 5 | `export * from ".../cat-harness/schemas/constraints"` |
   | `index.ts` | 20 | `export * from ".../cat-harness/schemas/index"` |
   | `builders.ts` | 29 | named re-export (`definition`, `theorem`, …) |
   | `references.ts` | 17264 | **self-contained** — the bibliography, i.e. content |

   So the block taxonomy (`typesForKind`), the Zod layer and the `@context` URL
   all live in `folio-assistant/cat-harness/`. There is no qou-side schema
   surface to hang a `qou:` type on, which means a `qou:` domain vocabulary is
   **necessarily a platform change first** (a context-extension hook), and only
   then a qou change (the terms themselves). That ordering is the practical
   answer to the owner's question: qou cannot do this unilaterally even if the
   terms were agreed.
2. **Which domain terms are worth minting?** This is an ontology decision, not a
   mechanical one, and the corpus already has an authority for term naming —
   `folio/quantum-observable-universe/notation/notation-register.md` and
   `notation-collisions.md`, which AGENTS.md §7aa makes authoritative for every
   symbol. A `qou:` vocabulary that disagreed with the notation register would be
   a second truth.
3. **What consumes it?** No in-repo consumer reads `@type` today (measured:
   `scripts/cited-source-availability-audit.py` is the only `.jsonld` reader and
   mentions `@type` zero times). A vocabulary with no consumer is speculative
   schema, and the anti-laundering discipline's spirit applies — build it when
   something asks a question it answers.

**Default if nobody acts: nothing changes.** The KG stays structurally correct
and domain-silent, and the questions above stay answered by grep. That is safe;
it is just not what the authority ruling implies the KG should eventually be.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
