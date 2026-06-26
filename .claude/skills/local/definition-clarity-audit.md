---
name: definition-clarity-audit
roles: [reader, collaborator, owner]
user_invocable: true
description: >-
  Definition / statement clarity + concision audit. A content block can
  validate (schema-clean, refs resolve, Lean sibling present) and still read
  badly: the defined term is never emphasised, the definition is buried under
  paragraphs of motivation, or one `definition` block silently bundles three or
  four distinct definienda. No existing QA axis (voice / wall / q-usage /
  canonical / detangler / bib / proof / compute) measures clarity of the
  statement itself. Use when asked to "bold defined terms", "tighten
  definitions", "no rambling definitions", "one definition per block", "tight
  theorem/proposition/lemma statements", or to set up / run a clarity audit.
  Emits per-block QA sidecar params under the `clarity-*` criteria via
  `content/pipeline/definition-clarity-audit.ts`.
---

# definition-clarity-audit

A content block can be **schema-clean, ref-resolving, Lean-backed** and still be
hard to read. The four QA axes that already exist guard *correctness* and
*voice*; none guards **clarity of the statement itself**. This skill adds that
axis — `clarity` — with four audit parameters.

The owner's framing (2026-06-26):

> *bold defined terms… there is a lot of preamble which should not be in defn…
> a lot of the definitions are long and very unclear… each thing should get its
> own definition… no multiple definitions in a content block… similarly,
> theorem/prop/lemma should have a no-rambling/tight-statement audit param.*

## The four audit parameters (criterion ids)

| Criterion | Applies to | Passes when | Fails when |
|---|---|---|---|
| **`clarity-defterm-bold`** | `definition` | the principal defined term is marked at its definition site by markdown bold `**…**` **or** a `:defterm[…]{#slug}` directive | the term appears only as plain text / `*italic*` — never emphasised |
| **`clarity-defn-single`** | `definition` | the block defines exactly **one** concept | the block bundles several definienda (many bold section-headers, ≥2 `defines[]` entries, or several "we define / is defined as" lead-ins) |
| **`clarity-defn-tight`** | `definition` | the definition is stated tightly, near the top | rambling: long prose, a stack of downstream-realisation sub-sections, or a long motivational preamble before the actual definition |
| **`clarity-stmt-tight`** | `theorem` / `proposition` / `lemma` / `corollary` | the claim is stated tightly | the statement rambles. Proofs live in separate `*-proof` blocks in this corpus, so a provable block is *just* its statement and should not ramble |

### Worked example — `def:q-dilogarithm`

[`q-dilogarithm.md`](../../../content/quantum-observable-universe/quantum-observable-universes/q-dilogarithm.md)
is the motivating case and trips three criteria at once:

- opens with a **52-word motivational preamble** ("Beyond the grouplike $\exp_q$
  … admits a canonical level-2 element …") before any definition — and never
  bolds the term **q-dilogarithm** → `clarity-defterm-bold` **fail**;
- crams **10 bold sub-sections** (`Iterated-primitive definition.`,
  `Pentagon identity.`, `Universal R-matrix interpretation.`, `Base-ring
  independence.`, `Native algebraic home.`, `Three-context behaviour.`,
  `Archimedean realisation.`, `Role in the q-heat story.`, `Physical
  meaning.`) into **641 prose words** → `clarity-defn-single` **fail** (major)
  and `clarity-defn-tight` **fail** (major).

The remedy (a follow-up, not the audit itself) is to split it into atomic
blocks — `def:level-k-primitive`, `def:q-dilogarithm` (the level-2 primitive
only, term **bolded**), `prop:q-dilogarithm-pentagon`, `rem:q-dilogarithm-r-matrix`,
`rem:q-dilogarithm-habiro`, etc. — each tight, each defining one thing.

## The scanner

`content/pipeline/definition-clarity-audit.ts` is a qou-local, **self-contained**
scanner (no schema import — `folio-assistant/` is gitignored on-branch, so it
parses `.ts` manifest + `.md` prose by regex, exactly like
`lean-vacuity-axiom-audit.ts`).

```bash
# full corpus → JSON + Markdown report
bun run content/pipeline/definition-clarity-audit.ts \
  --md   docs/audits/2026-06-26-definition-clarity-audit.md \
  --json docs/audits/2026-06-26-definition-clarity-audit.json

# one chapter, one criterion
bun run content/pipeline/definition-clarity-audit.ts \
  content/quantum-observable-universe/quantum-observable-universes \
  --only clarity-defterm-bold

# upsert reviewer.kind="script" candidate entries into <block>.qa.json
bun run content/pipeline/definition-clarity-audit.ts --write-sidecars
```

Flags: `[root …]` (default `content/`), `--json`, `--md`, `--only <criterion>`,
`--branch <name>` (blob-url branch), `--write-sidecars`, `--top N` (offenders per
criterion in the MD, default 25), `--quiet`. Exit code is **1 when candidates
exist**, so it can gate a pre-commit hook or CI.

### Heuristics & thresholds

All thresholds live in one `const T = {…}` block at the top of the scanner; tune
there, not in the per-criterion functions.

- **`clarity-defterm-bold`** — derive the principal term from the block `title`
  (text before the first parenthetical, math-stripped, stop-words dropped). The
  term counts as *marked* if any `**…**` or `:defterm[…]` span shares ≥ `0.5` of
  the term's tokens. Titles that are *fully mathematical* (no plain-text term)
  return `n/a`.
- **`clarity-defn-single`** — fail if bold section-headers ≥ `3`, or `defines[]`
  entries ≥ `2`, or defining-verb lead-ins ≥ `3`.
- **`clarity-defn-tight`** — fail if prose words > `250`, or bold sub-sections ≥
  `3`, or preamble words (before the first display-math / marked term) > `60`.
- **`clarity-stmt-tight`** — fail if prose words > `300`, or bold sub-sections ≥
  `3`, or preamble words (before the first display-math) > `80`.

## Agent-confirm protocol (high-recall → adjudicated)

Like `lean-vacuity-axiom-audit`, a `fail` is a **candidate, not a verdict**. The
heuristics are deliberately high-recall. For a durable disposition the agent:

1. opens the block `.md` + `.ts`;
2. confirms the candidate against the rubric below (or marks it a false positive
   — e.g. a `definition` whose title term is genuinely all-math is `n/a` for
   `defterm-bold`; a block with 3 short clarifying notes that are *not* separate
   definitions is a `defn-single` false positive);
3. records the adjudicated `reviewer.kind="agent"` sidecar entry (once the
   `clarity-*` ids are registered in the canonical qa-sweep registry — see the
   registry note below).

### Fix prescriptions

| Criterion | Fix |
|---|---|
| `clarity-defterm-bold` | bold the term at first definition: `the **$q$-dilogarithm**` (or register it in `defines[]` + wrap with `:defterm[…]{#slug}` per `AGENTS.md §4c`, the stronger glossary form). |
| `clarity-defn-single` | split the block — one `definition` per definiendum; demote interpretation sub-sections to `remark` blocks with `interprets:`; promote sub-statements to their own `proposition`/`lemma`. Mind the `uses[]` graph: downstream blocks that cite the old label point at the *primary* split product. |
| `clarity-defn-tight` | move motivation to a sibling `prose`/`remark` block; lead with the definition; push "downstream realisation" / "physical meaning" paragraphs out to `remark` blocks (`interprets:` the definition). |
| `clarity-stmt-tight` | strip preamble from the statement block; the hypotheses + conclusion only. Motivation → a preceding `prose` block; consequences → a following `remark`. |

> **Content fixes are collaborator-level and graph-aware.** Splitting a block
> touches `uses[]`, chapter manifests, and any `:refterm`/`#label` links. Run
> `bun run scripts/run-validate.ts content/<paper>` after, and prefer one PR per
> chapter of splits over a mega-PR.

## Relationship to existing systems

- **Complements `AGENTS.md §4c` (`\defterm`/`:defterm`).** §4c enforces that any
  term in a block's `defines[]` is wrapped *everywhere*. `clarity-defterm-bold`
  is upstream of that: it catches a `definition` whose principal term is never
  emphasised *at all* — including the common case (e.g. `def:q-dilogarithm`)
  where the term was never even registered in `defines[]`, so §4c never fires.
- **Complements `detangler-block-tanglement`.** The detangler measures
  cross-block tanglement (dependency structure); `clarity-defn-single` measures
  *intra-block* bundling (one block, many definienda). Different axis.
- **Complements `one-voice-audit`.** One-voice guards *voice* (status leaks,
  AI-slop, emoji); `clarity-*` guards *structure & concision*. A block can be
  perfect voice and still ramble.

## Registry note (folio-assistant companion)

The canonical qa-sweep criterion registry lives in the external
`litlfred/folio-assistant` repo (qou is content-only). Registering the four
`clarity-*` ids there — so `qa-sweep.ts` / `qa-staleness.ts` schedule and
hash-track them like every other criterion — is a **companion change out of qou
scope**. Until it lands, this scanner is **standalone**: it produces the
report and, with `--write-sidecars`, writes `reviewer.kind="script"` candidate
entries that the agent later upgrades. Do **not** rely on the reactive
post-commit `qa-sweep` to run these — run the scanner by hand (it is the
agent-owned QA path per `AGENTS.md §"QA is agent-owned; CI is a backup"`).
