---
name: paper-relevance-triage
roles: [collaborator, owner]
description: >
  Review one uploaded source document at a time: identify it, judge whether it
  bears on this folio, extract the results the folio could actually use, check
  whether it is already cited, and propose concrete linkage actions (add a
  reference, cite at a block, aid a proof, write a remark, import a block,
  cross-check a computation). Records the verdict in the source ledger and
  queues each accepted action as a bean. Use for "triage the uploads", "is this
  paper relevant", "what can we use from X", "which uploads aren't cited".
allowed-tools: Read Write Edit Bash Grep Glob Agent
---

# Paper relevance triage

`paper-importer` converts a paper into content blocks. `document-intake` owns
the extraction pipeline. **This skill sits before both**: it decides whether a
document is worth importing at all, and what the author should do with it.

Most uploads do not become content blocks. They supply a lemma, corroborate a
constant, or turn out to be background the paper already has. Triage produces
the judgement — and does it one document at a time, because relevance is not a
property a batch job can compute.

## Where the answers go

One file: `content/bib-qa-verifications.json`, the **source ledger**
(`source-ledger/v1`, typed in
[`folio-assistant/schemas/bib-verification.ts`](../../../folio-assistant/schemas/bib-verification.ts)).

**The ledger stores judgements and joins only.** It carries no title, author,
year, or DOI — those live in `content/schema/references.ts` and nowhere else. A
row points at a reference by `id`; consumers join. Writing a title into the
ledger is a review failure, not a convenience.

| Fact | Sole owner |
|---|---|
| title, authors, year, DOI, URL, type | `content/schema/references.ts` |
| document ↔ reference join | ledger `source` + `id` |
| was the source examined | ledger `status` |
| is it relevant, what to do about it | ledger `relevance` |
| the resulting work items | `.beans/` |

Consequence worth internalising: **when a triage judges an orphan worth citing,
creating the `ref()` entry is the first action, not the last.** Metadata is born
in `references.ts` or it is not recorded at all. Never park a title in the
ledger "until the ref exists".

## Before you start

Seed and refresh the ledger so every document has a row:

```bash
python3 scripts/extract-upload-titles.py -o /tmp/matches.json      # optional accelerator
bun run folio-assistant/content/pipeline/source-ledger-index.ts --write --matches /tmp/matches.json
```

The indexer is idempotent and never overwrites a `relevance` block. It resolves
what a filename can prove (arXiv ids, unambiguous title matches) and leaves the
rest at `status: "unreviewed"`, `id: null`.

Pick the next document from the unreviewed rows. Work highest-signal first:
orphans in the folio's own subject areas, then orphans generally, then
already-cited documents (where the question is whether the citation is
load-bearing).

## The per-document pass

### 1. Identify

Read the document's front matter (`Read` handles PDFs natively; use `pages` to
stay in the first few). Establish title, authors, year, venue, and arXiv id or
DOI. Two of the corpus's documents have no text layer — read those as images.

If `id` is already set, confirm it actually matches the document. A seeded join
is a machine guess; you are the first thing that checks it. A mismatch is a
finding — say so and fix the row.

### 2. Check the citation status

```bash
grep -n "<refid>" content/schema/references.ts                 # does the entry exist
grep -rn "cite{<refid>}\|\[<refid>\]" content/ --include=*.md  # is it cited anywhere
grep -rn "Ref: \[<refid>\]" content/ --include=*.lean          # does a sorry lean on it
```

Three distinct states, and they matter for what you propose:

- **No `ref()` entry** → orphan. If relevant, `add-reference` is the first action.
- **Entry exists, no citation site** → a bib orphan. Either propose
  `cite-in-block` at a named block, or record that it is not needed.
- **Cited** → check the citation is load-bearing. A reference cited once in
  passing, whose actual results the paper never uses, is worth flagging.

### 3. Judge relevance

Read enough to answer honestly. Skim the abstract, introduction, and the
statement of the main results; read a proof only when you are claiming it
supplies something.

| Verdict | Means |
|---|---|
| `core` | supplies a result the paper uses, or demonstrably should |
| `supporting` | technique, background, or context worth citing; not load-bearing |
| `tangential` | same field, no result this paper can consume |
| `not-relevant` | no bearing |
| `undetermined` | could not identify or could not read it |

**`undetermined` is a legitimate outcome.** A scanned document you cannot read,
or a paper whose relevance genuinely turns on a question you cannot settle, is
`undetermined` with a rationale saying why. Guessing `tangential` to clear the
queue is the failure mode this skill exists to prevent.

### 4. Extract key results — only the usable ones

For `core` and `supporting`, list the results the folio could actually consume.
Each needs an in-source locator (`Thm 3.2`, `§4.1`, `eq. (12)`, `p. 87`), the
statement in one sentence, and — the field that earns the entry — what this
folio would *do* with it.

Do not list a paper's main theorem because it is the main theorem. List it
because there is a specific place here that wants it. If you cannot name that
place, the paper is `supporting` at best and the key-results list is empty.

### 5. Propose actions

| Action | When |
|---|---|
| `add-reference` | relevant, no `ref()` entry yet |
| `cite-in-block` | reference exists; a named block should cite it and does not |
| `aid-proof` | supplies a lemma or technique for a named `sorry` or proof gap |
| `new-remark` | the result deserves a `remark` interpreting it for this folio |
| `new-block` | warrants importing a definition or proposition as a content block |
| `compute-check` | carries a numerical claim worth cross-checking against a witness |
| `no-action` | read and judged to need nothing |

Every action names a `target` — a block label, a Lean declaration, a script
path. An action without a target is a wish, not a proposal; either find the
target or drop the action.

**`aid-proof` has a higher bar.** Claiming a paper closes a gap here means you
have read the relevant statement and checked the hypotheses actually hold in
this setting. "Related to" is not "aids". If unsure, propose `new-remark` and
say what would need checking.

### 6. Write the row

```jsonc
{
  "source": { "kind": "upload", "file": "library/arxiv-math-0409565v2/0409565v2.pdf" },
  "id": "leitnerpawloski2004",
  "status": "verified-clean",
  "relevance": {
    "verdict": "core",
    "rationale": "Supplies the unital Gröbner basis machinery the PBW argument uses...",
    "keyResults": [
      {
        "locator": "Cor. 4.3",
        "statement": "A unital Gröbner basis over any commutative ground ring yields a PBW basis.",
        "useForFolio": "Discharges the base-ring generality assumed in prop:hecke-pbw.",
        "targets": ["prop:hecke-pbw"]
      }
    ],
    "proposedActions": [
      {
        "action": "cite-in-block",
        "rationale": "prop:hecke-pbw asserts the ground-ring generality without a source.",
        "target": "prop:hecke-pbw",
        "bean": "qou-ab12"
      }
    ],
    "assessed_by": { "kind": "agent", "model": "claude-opus-5" },
    "assessed_at": "2026-08-08T00:00:00Z",
    "source_sha": "3f9a1c88de41"
  }
}
```

`source_sha` is the 12-char SHA-256 prefix of the document
(`sha256sum <file> | cut -c1-12`) — a re-upload changes it and marks the
assessment stale, the same staleness idiom the `.qa.json` sidecars use.

### 7. Create the beans

Every proposed action other than `no-action` becomes a bean, and the bean id
goes back into the action's `bean` field so the ledger and the work-plan stay
joined:

```bash
beans create "Cite [leitnerpawloski2004] at prop:hecke-pbw — ground-ring generality is unsourced" --type task
```

Bean titles name the action and the target, not the paper. "Read Smith 2024" is
not a work item; "Cite [smith2024] at prop:foo" is.

Batch note: create beans for `core` findings as you go. For `supporting`
findings, one bean per document covering all its actions is enough — a dozen
beans for one background reference buries the queue rather than serving it.

## Honesty discipline

This skill produces judgements that redirect the author's attention, so the
corpus rules bite here directly:

- **A relevance verdict is a claim, not a fact.** It is recorded under
  `assessed_by: { kind: "agent" }` and stays an agent claim until a human
  adjudicates it. Never write a verdict into a durable artifact as settled.
- **Do not inflate relevance to justify the reading.** `not-relevant` after a
  careful read is a complete, useful result. A queue of 169 orphans that comes
  back "all supporting" is a triage that did not happen.
- **The "refuted" rule applies.** "This paper does not help" is a scope-(a)
  negative — *this document, as read, supplies nothing usable here*. It is not
  a claim that the technique is excluded. Phrase it that way.
- **Corpus-grep before declaring a gap.** Proposing `aid-proof` against a
  "gap" means running the corpus-grep checklist first — the gap may already be
  closed elsewhere in the tree. See AGENTS.md §"Before declaring open".
- **Numerical claims are `compute-check`, never wired.** A paper reporting a
  constant that matches one of ours is a cross-check to run, not a result to
  adopt. Adopting an external number because it matches is a fit.

## Parallelism

Documents are independent, so triage parallelises cleanly: dispatch background
agents over disjoint slices, each writing its own findings to a scratch JSON,
and merge into the ledger in one pass. Do **not** have parallel agents write
`content/bib-qa-verifications.json` concurrently — it is one file and they will
clobber each other.

Give each agent the identification and citation-status steps as well as the
judgement; an agent handed only "is this relevant" without the corpus in front
of it will guess.

## Checklist

- [ ] Ledger reseeded; the document has a row
- [ ] Document identified from its own front matter, not from its filename
- [ ] Seeded `id` confirmed against the document, or corrected
- [ ] Citation status checked all three ways (entry / site / Lean `-- Ref:`)
- [ ] Verdict recorded with a rationale that gives the reasoning
- [ ] Key results carry in-source locators and a named use
- [ ] Every action names a target
- [ ] `assessed_by`, `assessed_at`, `source_sha` set
- [ ] Beans created for non-`no-action` proposals, ids written back
- [ ] No title, author, or year written into the ledger
