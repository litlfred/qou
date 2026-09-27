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

## 🟧 OWNER RULING 2026-09-27 — the `lean` grammar goes to f-a-sci; my recommendation is OVERRULED

Verbatim: *"field sits on shared kinds (remark, example, algorithm, simulator),
so the grammar genuinely is  vocabulary that goes tp f-a-sci"*, following
*"f-a-sci __should__ have scehams for math/science papers."*

**What is overruled.** The recommendation above (option 3, document the split)
rested on `lean-packages.ts`'s own docstring section *"Why this is core and not
the science layer"*, which argues: the `lean` field is on **shared** kinds
(`remark`, `example`, `algorithm`, `simulator`), therefore *"the grammar
belongs wherever the field does, which is core"*. The owner reverses the
inference. A `lean` field appearing on a shared kind does **not** make the
grammar core; it makes **that field on those kinds** part of the science
vocabulary. The platform docstring's argument is rejected at its premise, not
at its conclusion.

**So `lean-packages.ts` carries a superseded rationale**, and it is the module
whose docstring a future agent will read first when deciding where any of this
belongs. Fixing that docstring is part of enacting the ruling.

### The obstacle, stated precisely

Two things describe one set of block kinds:

- `Block` (`types.ts:1027-1049`) — a discriminated union of 19 interfaces.
  `Block["kind"]` is therefore the compile-time type
  `"definition" | "theorem" | … | "figure"`.
- `BLOCK_KINDS` (`block-kinds.ts:42`) — a runtime array of the same 19 strings.

`types.ts:1067` makes the compiler refuse to build if they disagree:

```ts
type _MutuallyExhaustive<A, B> = [A] extends [B] ? ([B] extends [A] ? true : never) : never;
const _blockKindsAreExhaustive: _MutuallyExhaustive<Block["kind"], BlockKind> = true;
```

**It is not decoration.** `types.ts:933` records what its absence cost:
`algorithm` and `table` reached the union and never reached **five
hand-maintained copies** of the kind list, with no error anywhere, excluding
**461 qou blocks — 13 % of the corpus — from every sweep.**

A registry in the shape of `content-type.ts` accepts entries **at load time**.
A union is fixed **at compile time**. So "sci registers `theorem` at runtime"
and "the compiler proves the list matches the union" cannot both hold in the
present shape — that is the whole difficulty, and it is a real one rather than
a preference.

### Options, with what each buys and gives up

**A — parameterise `Block`; the math union and its kind list BOTH move to
f-a-sci, each layer keeping its own closed proof.**
Core becomes `Block<Extra = never> = DocumentBlock | Extra`; f-a-sci declares
`MathBlock`, `MATH_BLOCK_KINDS`, and its own `_MutuallyExhaustive` over them.
- *Buys:* honours the ruling in full; **keeps the 461-block guarantee**, one
  closed proof per layer; DAK can follow the same route, so
  `DAK_BLOCK_KINDS` leaves core too.
- *Costs:* every core consumer of `Block` becomes generic. `constraints.ts`
  rules keyed `appliesTo: ["definition"]` need the same treatment.
  Type-level surgery across `types.ts` (1500) + `constraints.ts` (933) and
  every pipeline consumer.
- *Risks:* a half-done generic `Block` is worse than either end state —
  `unknown`/`any` leaks at the boundary would silently re-admit drift.
- *Commits to:* a generic `Block` permanently.

**B — open registry, drop the proof.**
- *Buys:* matches `content-type.ts`; cheapest to write.
- *Costs / risks:* **hands back exactly the guarantee that 461 blocks paid
  for.** A kind in the union with no registry entry silently drops out of every
  sweep again, with no error. **Do not take this one.**

**C — open registry plus a RUNTIME exhaustiveness check** (startup assertion +
a test asserting every `Block` variant's `kind` is registered).
- *Buys:* open registry; the guarantee survives in weaker form.
- *Costs:* moves the failure from compile time to run time, and only where the
  check actually runs. This corpus's own repeated lesson is that a gate nobody
  invokes is documentation — `precision-gates.sh` sat unrun in prose while
  three dirty witnesses reached `main`.

**D — move the science MACHINERY now, leave the vocabulary in core.**
Measured, the unambiguously science-only modules under `cat-harness` are
**9 files / 4,579 lines**: `content/pipeline/lean-lexer.ts` (289),
`conditional-class-banner-audit.ts` (473), `conjectural-propagation-audit.ts`
(324), `migrate-lean-refs.ts` (219), `witness-address.ts` (65),
`scripts/check-duplicate-decls.ts` (375),
`scripts/check-self-discharging-instances.ts` (444),
`scripts/check-mirror-drift.ts` (711), `scripts/partition/instance-rules.ts`
(1679) — plus three schemas, `formalization-types.ts` (695),
`lean-packages.ts` (134), `precision-scalar.ts` (71). **≈ 5,479 lines.**
- *Buys:* no type surgery, no proof change, immediately doable; f-a-sci gets a
  real `schemas/` + pipeline instead of being a library-only layer.
- *Costs:* does **not** satisfy the ruling as stated — `theorem`,
  `proposition`, `proof` and the `lean` field stay in core.
- *Note:* the remaining core importers of `lean-packages` are the genuinely
  mixed ones — `types.ts`, `constraints.ts`, `render-latex.ts`, `qa-utils.ts`,
  `export-json.ts`, the three `adapters/` files — so D does not invert the
  layering for the 9; it removes them from the count entirely.

**E — D now, A next.**
D is a no-regret prefix of A: those 5,479 lines have to move under A anyway,
and moving them first shrinks A's surface and *reveals empirically* which core
consumers actually need the math arms of `Block`.

**My judgement, marked as judgement, not a finding:** **E**. D is mechanical,
large, and satisfies *"f-a-sci should have schemas for math/science papers"* in
substance this week; A is then the only route that honours the ruling on the
**vocabulary** without giving back the 461-block guarantee. **B is the option to
refuse**, and it is the one that will look most attractive to whoever picks this
up, because it is a one-file change that appears to match an existing pattern.

**Default if nothing further is decided:** nothing moves. `f-a-sci` stays
library-only, the math vocabulary stays in `cat-harness`, and
`lean-packages.ts` keeps a docstring the owner has now rejected.

### One measured absence worth recording

There is an extension-namespace mechanism (`schemas/namespaces.ts`:
`CANONICAL_EXTENSION_PREFIX = "folio"`, `isOwnExtensionNamespace`,
`extension-namespace.test.ts`) and `convention.ts:87` uses it
(`CONVENTION_EXT = "folio:convention"`) — but it is **BPMN**-side. Grepped
`types.ts` for an extension field on `BlockBase`: **zero hits**. So "make
`lean` a sci-namespace extension rather than a base field" has **no precedent
on blocks**; it is a sub-question of A, not a shortcut past it.

### Where this lands

All of it is the **platform** repo (`litlfred/folio-assistant`), pinned here at
`.folio-assistant-pin` = `37a36ce9296b95a9ad4862d51dc496ac44053143`, plus a pin
bump in qou afterwards. qou's exposure is the same 1,306 blocks carrying a
`lean.ref`.

## 🟧 OWNER DIRECTIVE 2026-09-27 (same session, after the ruling above)

Verbatim: *"if gaps, generalize from qou content types so not qou specific and
move to f-a-sci"*.

This settles the direction — **move** — and adds the constraint that decides how:
**generalise on the way out.** A module does not go to `f-a-sci` as-is if it
carries qou specifics; it gets de-qou-ified first, so `f-a-sci` ends up with
schemas for *mathematics/science papers*, not schemas for *this* paper.

Read against the options above, this is **E** with D's contents filtered: the
5,479 lines are the candidate set, and each one needs a qou-specificity check
before it moves. Note the trap the directive is guarding against — the same one
`lean-packages.ts` already fell into once and was repaired for on 2026-09-18,
when `DEFAULT_LEAN_PACKAGES = [qou, ugb, fred2005]` shipped inside the platform.
Moving a module from `cat-harness` to `f-a-sci` **without** that check relocates
the defect rather than fixing it: `f-a-sci` is still a platform layer, so one
folio family's data is just as wrong there.

Per-module qou-specificity triage is the next step and is recorded as it is done.
