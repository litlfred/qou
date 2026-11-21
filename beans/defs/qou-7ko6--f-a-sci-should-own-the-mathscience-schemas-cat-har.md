---
# qou-7ko6
title: 'f-a-sci should own the math/science schemas: cat-harness holds MATH_BLOCK_KINDS and DAK_BLOCK_KINDS as closed enums while its newer registries are open'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T05:52:03Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
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

## 2026-09-27 — MEASURED: the ruling costs exactly six edges, and two modules move free

Platform PR: **litlfred/folio-assistant#1453** (branch
`claude/sci-owns-lean-grammar-probe-2026-09-27`). The options analysis above is
superseded on one point — **the layering was already declared**, so this was
never a question of inventing a target, only of correcting one assignment.

### What was already true before touching anything

`cat-harness/scripts/partition/` is a partition engine (`check:partition` →
`scripts/repo-partition.ts`) that assigns every module to a target repo and
reports wrong-direction imports against a declared DAG
(`ALLOWED`: `sci -> [sci, core, harness]`, `harness -> [harness]`). Baseline on
the pin:

```
Partition — 1172 modules, 2638 internal import edges
  cat-harness           310     folio-assistant-core  256
  folio-assistant-sci    39     smart-base             11
Wrong-direction edges: 0
```

So `folio-assistant-sci` **already had 39 modules assigned** — `adapters/paper/`,
the LaTeX pipeline, `schemas/formalization-types.ts`,
`schemas/precision-scalar.ts`, `schemas/refactor-strategy.ts`,
`scripts/check-duplicate-decls.ts`, `check-mirror-drift.ts`,
`check-self-discharging-instances.ts`, and a keyword rule
`/(lean|latex|tex|proof|witness|simulator|sage|formaliz|knot)/i`. My
"option D mover set" was, near enough, a rediscovery of that list.

**Correction to this bean's own earlier entry:** it says the vocabulary "is in
`cat-harness/schemas/`". That is the *physical directory* and is correct; the
**declared target layer** for `types.ts`, `constraints.ts`, `block-kinds.ts`,
`narrative.ts` is **`folio-assistant-core`**, not `cat-harness`. Say which you
mean — the split's whole point is that the two differ today.

### The ruling reaches FOUR entries, because the overruled test was applied five times

`instance-rules.ts` has a core triage block whose header states the test in
words and then says *"Same test again"* and *"Same test a third time"*:

> *"The test applied is not 'does the name mention Lean' but 'would core
> compile and function without the science layer installed'. For
> `lean-packages.ts` it would not: `BlockBase` carries an optional `lean` field
> … the field is on shared block kinds by design … **So the grammar belongs
> wherever the field does.** Only the package list is a property of a folio,
> and that is injected."*

That is the ruling's target verbatim, in the platform's own words. Entries
resting on it: `schemas/lean-packages.ts`, `content/pipeline/lean-signature.ts`,
`content/pipeline/lean-lexer.ts`, `content/pipeline/witness-address.ts`.

Two entries in the same block are **not** affected and were left alone —
`validate-simulator.ts` (core on a *measured* argument: `simulator` is in
`DOCUMENT_BLOCK_KINDS`, not `MATH_BLOCK_KINDS`) and `qa-witness.ts` (core
because it imports only `block-qa`/`kg-qa`/`script-qa`). Neither cites the
rejected test.

### The probe, and the price

Reassigning all four and re-running the engine:

```
Wrong-direction edges: 6      folio-assistant-core → folio-assistant-sci: 6

  schemas/constraints.ts        -> schemas/lean-packages.ts
  adapters/mcp-server/server.ts -> schemas/lean-packages.ts
  adapters/document/resolver.ts -> schemas/lean-packages.ts
  adapters/manifest-entries.ts  -> schemas/lean-packages.ts
  content/pipeline/qa-utils.ts  -> schemas/lean-packages.ts
  content/pipeline/qa-utils.ts  -> content/pipeline/lean-signature.ts
```

**Five of the six point at one target.** `lean-lexer.ts` and
`witness-address.ts` cost **zero** — so the ruling splits cleanly into a free
half and a priced half, which is not something the options above anticipated.

**Landed (#1453):** the two free ones move to `sci`; the core triage header is
corrected to record the ruling, name the six edges, and tell the next reader
that the two remaining entries are core **because of the six edges, not because
of the test**. Verified `sci 39 → 41`, `core 256 → 254`,
**wrong-direction 0**, `--strict` exit 0, and `repo-partition.test.ts` +
`partition-imports.test.ts` + `partition-names.test.ts` **28 pass / 0 fail**.

**Held:** `lean-packages.ts` and `lean-signature.ts`. The six edges exist
because the overruled header is, *as a statement of fact about today's code*,
**correct** — core really does reach into the grammar. Honouring the ruling on
them needs `lean` off `BlockBase`, with the grammar behind the same injection
`configureLeanPackages` already established for the package **list**, extended
to the **grammar**. That changes `BlockBase`, so it is an owner call.

### The de-qou-ification the second directive asked for is nearly free

Measured across all 12 candidate modules (~5,479 lines), separating hits in
**code** from hits in **prose**: only **4 qou-specific lines of code** exist.

| site | what |
|---|---|
| `content/pipeline/migrate-lean-refs.ts:48` | `visualizer: "qou"` — a genuine hardcode |
| `scripts/check-self-discharging-instances.ts:423` | a qou bean id in a `console.log` |
| `scripts/check-mirror-drift.ts:116` | imports `ARCHIMEDEAN_TYPE_RE` (qou vocabulary) |
| `scripts/partition/instance-rules.ts:1398` | a path string, not qou-specific |

`schemas/lean-packages.ts`, `precision-scalar.ts`, `lean-lexer.ts`,
`conditional-class-banner-audit.ts`, `conjectural-propagation-audit.ts`,
`witness-address.ts`, `check-duplicate-decls.ts` have **zero** code-level qou
hits. `formalization-types.ts`'s single hit is `| "BraidedMonoidal"` — general
category theory, not qou. So the raw grep counts (2–12 per file) are almost
entirely **docstring examples**, and the generalisation burden is four lines,
not a rewrite.

### Open, and it is the one thing waiting on the owner

Whether to take `lean` off `BlockBase` and put the grammar behind injection.
**What it costs:** `constraints.ts`, `adapters/mcp-server/server.ts`,
`adapters/document/resolver.ts`, `adapters/manifest-entries.ts` and
`content/pipeline/qa-utils.ts` rewired, plus a `.folio-assistant-pin` bump here.
**What it risks:** a half-done injection leaks `unknown` at the boundary and
silently re-admits the drift `_blockKindsAreExhaustive` exists to stop — the
461-block failure mode. **What it commits to:** core never naming a
formal-reference vocabulary again. **Default if nothing is decided:** the two
stay in core under a header that flags itself as overruled; nothing breaks, and
the note directs the next agent to cite the six edges.

---

## 2026-09-27 (later) — 🟩 DONE on the platform side: the six edges are PAID, and `BlockBase` never had to change

Pushed as `folio-assistant` `claude/sci-owns-lean-grammar-probe-2026-09-27`
(`c9b5781fdb3` + `fef2f9e6ecf`). Partition: **6 wrong-direction edges → 0**;
core 258 → 256, sci 41 → 44.

### The earlier note's blocker did not exist

`partition/instance-rules.ts` recorded that honouring the ruling *"needs core to
carry a formal reference whose vocabulary it does not own — `lean` off
`BlockBase` … That changes `BlockBase`, so it is the owner's call and is not made
here."*

**`BlockBase` is unchanged.** Core still carries a field named `lean` with a
`ref` string; it simply no longer knows the grammar of that string. The whole
price was five call sites, one of which dissolved:

| site | what it needed | how |
|---|---|---|
| `schemas/constraints.ts` | the ref pattern + candidate paths | injected |
| `adapters/document/resolver.ts` | candidate paths | injected |
| `adapters/mcp-server/server.ts` | candidate paths | injected |
| `adapters/manifest-entries.ts` | a parse helper | **`tryParseLeanRef` DELETED** — its only two consumers were the two resolvers above |
| `content/pipeline/qa-utils.ts` | canonical resolution, statement hash, source listing | injected; ~327 lines moved verbatim to sci |

New: `schemas/formal-ref.ts` (core socket, third instance of the
`references-registry-di` / `value-registry-di` pattern) and
`content/pipeline/lean-formal-ref.ts` (sci plug).

### Three things worth carrying forward

1. **`LeanRefSchema` had to stop using `.regex()`.** A `z.object({...})` literal
   evaluates at module init, strictly before any layer can install itself, so
   `.regex(pattern)` freezes the unconfigured fallback forever. It is now
   `superRefine`, which runs per `parse()`. This is why the pattern could not be
   injected before.
2. **The resolution record carries TWO path lists.** Merging `candidatePaths`
   and `fallbackPaths` was the obvious move and is a behaviour change in the
   worse direction: the module-path candidate may be an import-only aggregator
   (`qou-cu0a`, 65 of 1220 blocks), and merging would put it AHEAD of the real
   declaration file for the two resolvers — so the MCP server would start
   serving an `import` list as a block's source. `constraints.ts` accepted that
   file before and still does; neither resolver did and neither now does.
3. **NINE core modules import `lean-packages`, not six.** `export-json.ts`,
   `conjectural-propagation-audit.ts` and `conditional-class-banner-audit.ts`
   are composition roots (`import.meta.main`), which `partition/engine.ts`
   exempts from the direction rule while still counting the edge in
   `totalEdges`. Re-measure with `--edges`, never by grep.

### 🛑 The qou side is BLOCKED on the pin, and must land as ONE commit

Two lines — `configureLeanPackages` imported from `lean-formal-ref` instead of
`lean-packages` in `scripts/preload-registry.ts` and `scripts/run-validate.ts` —
and they **must be in the same commit as the `.folio-assistant-pin` advance**.
Split them and validation regresses in the window between: after the platform
commit, configuring the package list without importing the installer leaves
`lean-file-exists` failing CLOSED for every `definition` whose formalisation
lives in the library tree. Same rule as the q₀-sweep constraint 4 in AGENTS.md,
for the same reason.

qou keeps working unchanged at the current pin, so there is no urgency and no
half-state.

### Measured while here: `qou-i2ed` is bigger than its own title says

`0 of 1301` `lean.ref`s resolve in `check-base-ring.ts`, `check-wall-side.ts`
and `content/pipeline/qa-agent-entry.ts` (which configure nothing), against
**745** with the layer installed. Both directions of that correction are on
`qou-i2ed`; that bean's title is wrong and should not be quoted.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
