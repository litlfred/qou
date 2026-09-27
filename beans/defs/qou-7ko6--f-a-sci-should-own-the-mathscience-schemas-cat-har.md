---
# qou-7ko6
title: 'f-a-sci should own the math/science schemas: cat-harness holds MATH_BLOCK_KINDS and DAK_BLOCK_KINDS as closed enums while its newer registries are open'
status: todo
type: task
created_at: 2026-09-27T05:52:03Z
updated_at: 2026-09-27T05:52:03Z
---


## 2026-09-27 — measured, on platform pin `37a36ce9296`

Owner, verbatim, two messages: *"f-a-sci __should__ have scehams for
math/science papers."* and *"(like proposition. theorem, proof, etc.... some
schemas exist somewhere, may ned to be ingreated/updated to cat-harness
f-a-c)"*.

They do exist, and they are in **neither** `folio-assistant-core/` nor
`folio-assistant-sci/`. They are in `cat-harness/schemas/`.

### Where the theorem/proposition/proof vocabulary actually lives

| what | file | evidence |
|---|---|---|
| the kind names | `cat-harness/schemas/block-kinds.ts:42` | `BLOCK_KINDS = ["definition","theorem","lemma","proposition","corollary",…,"conjecture",…,"proof",…]` |
| the math subset, already named | same file, `:223` | `MATH_BLOCK_KINDS = ["definition","theorem","lemma","proposition","corollary","conjecture","proof"]` |
| the block types carrying `lean` | `cat-harness/schemas/types.ts` | `:691 lean: LeanRef` (required), `:704/:769/:778/:803/:837 lean?: LeanRef`, `:706 proofs?: string[]`, `:99 sorryFree?: boolean` |
| narrative statement / narrative proof | `types.ts:1028 narrative?: Narrative` + `schemas/narrative.ts` | `:248` comment *"The proof's .md file contains the narrative proof."*; `narrative.ts` is a 4-state machine `not-authored \| draft \| confirmed \| rejected` where `confirmed_by.kind` must structurally be `"human"` |
| the validation rules | `cat-harness/schemas/constraints.ts` (933 lines, 105 math hits) | e.g. `definition-lean-exists` at `:722` |
| formalization status / review records | `cat-harness/schemas/formalization-types.ts` (695 lines, 104 hits) | `FormalizationStatus`, `LeanReference`, `LeanReviewStatus`, `ReviewRecord` |
| the `lean.ref` grammar | `cat-harness/schemas/lean-packages.ts` | see the sibling bean |
| `mpf`-style exact scalars | `cat-harness/schemas/precision-scalar.ts` (71 lines) | `precisionScalar`, `precisionScalarOrNumber` |

`folio-assistant-core/schemas/` (22 files) is **platform infrastructure** —
`adjudication`, `catalogue`, `changeset`, `dublin-core`, `extraction`,
`fhir-artifact-index`, `glossary`, `library-ref`, `masked-region`,
`materialization`, `review-comment`, `review-verdict`. Not one math kind.

`folio-assistant-sci/` has **no `schemas/` directory at all** — only
`AGENTS.md`, `README.md`, `content`, `contributions.ts`, two config files,
`library`, `skills`. Its `folio-assistant-sci.json` describes itself as
*"Scientific source material used by folios that formalise mathematics — one
document today"*, i.e. a **library**, not a schema layer. Nothing in its
`AGENTS.md` mentions schemas (grep: 0 hits).

### The sharp finding: the pattern is already established, and was not applied here

`cat-harness` has TWO open registries, both built precisely to stop a layer's
vocabulary living in the platform, and both carrying the rule in their own
docstrings:

- `content-type.ts` — *"a registry rather than an enum … each type declares its
  own filename"*, owner's rule 2026-09-20.
- `content-types-base.ts` — *"the registry is a mechanism and the entries are a
  layer's opinion. **A layer that does not own a type must not be the place it
  is declared**, and the split is what makes that enforceable rather than
  merely stated."*
- `graph-kind-registry.ts` — same shape; `folio-graph-kind.ts` registers `folio`
  rather than the harness declaring a kind it cannot serve.

`block-kinds.ts` is **not** one of them. It is a closed `as const` tuple, and it
hardcodes **two downstream layers' vocabularies side by side**:
`MATH_BLOCK_KINDS` (:223) and `DAK_BLOCK_KINDS` (:327), plus
`CONTENT_ADAPTERS = ["paper","dak"]` (:85). So the exact thing three other
modules were refactored to prevent is still true of the one that names theorems.

### What makes the move non-trivial

`types.ts:1068` carries a **compile-time mutual-exhaustiveness proof**:

```ts
type _MutuallyExhaustive<A, B> = [A] extends [B] ? ([B] extends [A] ? true : never) : never;
const _blockKindsAreExhaustive: _MutuallyExhaustive<Block["kind"], BlockKind> = true;
```

`BLOCK_KINDS` and the `Block` discriminated union are pinned to each other at
the type level. A science layer cannot *add* kinds at load time the way
`content-type.ts` allows without either (a) breaking that proof, or (b) the
`Block` union itself becoming extensible. That is the real design question, and
it is the owner's / platform's call, not a mechanical move.

`MATH_BLOCK_KINDS` / `DOCUMENT_BLOCK_KINDS` (:247, derived by filtering) plus
`CONTENT_PROFILES = ["document","paper"]` and `DOCUMENT_FORBIDS_LEAN = true`
(:269) mean the *profile* mechanism is already doing some of the work a layer
split would do — a document-profile folio is already forbidden from using
`lean`. So one honest option is that the current design is **deliberate** and
the split should be documented rather than performed.

### Options, and my recommendation

1. **Open `block-kinds.ts` into a registry** like `content-type.ts`, and have
   `folio-assistant-sci` register the seven math kinds. *Costs:* the
   exhaustiveness proof must be reworked or dropped; `Block` must become
   extensible; every `PROFILE_BLOCK_KINDS` / `ADAPTER_BLOCK_KINDS` consumer
   re-checked. *Risks:* dropping `_blockKindsAreExhaustive` removes the one
   compile-time guarantee that a kind cannot be added to the union without a
   name, which `types.ts:933` records as a scar already paid for once.
   *Commits to:* `Block` as an open union forever.
2. **Move the pure-science schemas only**, leaving the kind names in core:
   `formalization-types.ts` (695 lines), `lean-packages.ts` (134),
   `precision-scalar.ts` (71) → `folio-assistant-sci/schemas/`. *Costs:* 21
   importers of `lean-packages` alone, all inside `cat-harness`, would import
   upward from core into sci — which inverts the layering and is probably
   worse than the status quo. *This is why `lean-packages.ts`'s own docstring
   argues it belongs in core*: `lean` sits on shared kinds (`remark`,
   `example`, `algorithm`, `simulator`), so the grammar goes where the field
   does and only the package LIST is folio data.
3. **Document the split instead of moving anything** — record in
   `cat-harness/schemas/block-kinds.ts` and `folio-assistant-sci/AGENTS.md`
   that the math kinds are core-by-decision (the profile mechanism already
   fences them), and create `folio-assistant-sci/schemas/` only for genuinely
   sci-specific things with no core consumer.
4. **No-op** — nothing changes; the vocabulary stays in `cat-harness` and
   `folio-assistant-sci` stays a library layer.

**My judgement, not a finding:** option **3**, and only then option 1 if a
second science folio with different kinds actually appears. The reason is
`lean-packages.ts`'s own argument, which I did not expect and which survived
checking: the `lean` field is on *shared* kinds, so the grammar genuinely is
core, and the thing that was correctly pushed out was the **list**, not the
schema. Option 1 buys extensibility nobody has yet asked for at the price of
the one compile-time proof in the file. Option 2 inverts the layering outright.

**Default if nothing is decided:** the vocabulary stays where it is, no count
moves, and `folio-assistant-sci/` keeps no `schemas/`.

**Blast radius in real terms.** Everything above is in the **platform repo**
(`litlfred/folio-assistant`), reached here through the symlink and pinned at
`.folio-assistant-pin` = `37a36ce9296b95a9ad4862d51dc496ac44053143`. qou reads
it and cannot change it; any move lands there and then needs a pin bump here.
qou's exposure is **1,306 content blocks carrying a `lean.ref`** — every one of
them types against `types.ts` and validates against `constraints.ts`.
