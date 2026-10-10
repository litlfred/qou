# Requirements — folio-assistant proof/narrative QA checkers

**Status:** requirements (for a `litlfred/folio-assistant` implementing agent)
**Author of requirements:** qou side, PR #3289 follow-up
**Target repo:** `litlfred/folio-assistant` (the QA checker platform; **not** `qou`)
**Date:** 2026-07-04
**Motivating incident:** [`docs/audits`-adjacent] — `prop:positive-definite-dagger`
sat green in QA while carrying four visible narrative-proof defects. Root-cause
investigation (qou PR #3289) found two independent failures:

1. **Flag-loss** — true-positive `fail` verdicts were discarded by a wholesale
   "distrust-clear" that overwrote them with `n/a`. *Fixed on the qou side* by
   [`folio/pipeline/qa-flag-preservation-audit.ts`](../../folio/pipeline/qa-flag-preservation-audit.ts)
   (this doc's §6 explains how the new checkers must interact with it).
2. **Coverage gaps** — three of the four defect classes have **no deterministic
   criterion in the registry at all**, and the one axis that could catch the
   fourth (`proof-narrative-lean-equiv`) was *loosened* by a rerate that treats
   "honest deferral" as a pass. These are folio-assistant-side and are the
   subject of this document.

This document specifies **three new deterministic checkers** (§2–§4), **one fix to
an existing rerate rule** (§5), and **one new agent-judged exposition rater**
(§5A, `expo-milnor-clarity` — added 2026-07-04 at owner request; a strict gating
rater, `pass` iff a perfect 16/16). It is written to
be self-contained: the implementing agent should not need the originating chat
transcript.

---

## 0. How to use this document

- Every section marked **SPEC** is a hard requirement. Sections marked **NOTE**
  are rationale/context.
- Field names, function signatures, and file paths below are given as the
  **contract the implementation must satisfy**. Where a name is my best
  reconstruction of the live folio-assistant API (the qou checkout does not vendor
  the platform source), it is marked `⟨confirm against live source⟩`. Confirm the
  exact symbol, then honor the *semantics* specified here regardless of the exact
  name.
- The canonical interchange types are `block-qa/v1`
  (`folio-assistant/schemas/block-qa.ts`) and `qa-script/v1`. Do not invent a new
  schema; add criteria to the existing registry.

### 0.1 Where things live `⟨confirm against live source⟩`

| Concern | File |
|---|---|
| Criterion registry (`QA_CRITERIA_REGISTRY`) | `folio-assistant/content/pipeline/qa-criteria-registry.ts` |
| Deterministic script checkers | `folio-assistant/content/pipeline/qa-checkers-extended.ts` (proof/structure axis) |
| Reactive sweep driver | `folio-assistant/content/pipeline/qa-sweep.ts` |
| Sidecar producing types | `folio-assistant/schemas/block-qa.ts` (`QaCriterionEntry`, `BlockQaSidecar`) |
| Agent-drain queue filter | consumes `QA_CRITERIA_REGISTRY.filter(c => !c.automated)` |
| The rerate to fix (§5) | `local/narrative-lean-rerate` (script; grep the registry `reviewer.id`) |

### 0.2 The `block-qa/v1` sidecar shape (reference)

```jsonc
{
  "schema": "block-qa/v1",
  "label": "prop:positive-definite-dagger",
  "kind": "proposition",
  "paths":         { "md": "...", "ts": "...", "lean": "..." },
  "source_hashes": { "md": "8da7…", "ts": "5f55…", "lean": "2dab…" }, // 12-char sha-256 prefix
  "criteria": {
    "<criterion-id>": [
      {
        "field_hash":  { "md": "8da7…", "ts": "5f55…", "lean": "2dab…" },
        "result":      "pass" | "warn" | "fail" | "n/a",
        "notes":       "human-readable one-liner",
        "reviewed_at": "2026-07-04T00:00:00.000Z",
        "reviewed_sha":"<git sha the review ran against>",
        "reviewer":    { "kind": "script", "id": "content/pipeline/qa-checkers-extended.ts",
                         "version": "v1", "script_hash": "…", "script_commit_sha": "…" }
      }
    ]
  }
}
```

### 0.3 `result` semantics — STRICT (this is the hill the whole incident died on)

| `result` | Meaning | Counts as a finding? |
|---|---|---|
| `pass` | criterion checked, block is clean | no |
| `warn` | minor / advisory issue | yes (non-blocking) |
| `fail` | criterion violated | yes (blocking in `--ci`) |
| `n/a` | **criterion does not apply to this block** (wrong kind, no such content) | **no — excluded from roll-up** |

`n/a` means *out of scope*, **never** "we distrust the verdict." A checker must
emit `n/a` **only** when the block genuinely lacks the thing the criterion checks
(see each checker's "Applies to / n/a when" clause). Emitting `n/a` as a way to
suppress a result is the exact anti-pattern the qou-side guard (§6) now fails CI
on.

### 0.4 Registry entry contract `⟨confirm against live source⟩`

Each new criterion is one object appended to `QA_CRITERIA_REGISTRY`:

```ts
{
  id: "proof-sketch-vs-kind",         // kebab-case, unique
  axis: "proof",                       // existing axis; groups it under the proof watcher
  severity: "major",                   // "critical" | "major" | "minor"
  automated: true,                     // true ⇒ script checker, runs in qa-sweep; false ⇒ agent-drained
  description: "A provable-kind block must present a complete proof, not a sketch.",
  reviewer: { kind: "script", id: "content/pipeline/qa-checkers-extended.ts" },
}
```

- **All three new checkers are `automated: true`** (deterministic scripts). They
  must **not** be routed to the agent-drain queue.
- Wire each into `qa-sweep.ts` so it runs reactively on the blocks it applies to,
  keyed on `field_hash` staleness like the sibling `proof-*` script checkers.

### 0.5 Checker function contract `⟨confirm against live source⟩`

Match the signature the other `qa-checkers-extended.ts` functions use. Expected shape:

```ts
// Input: the resolved block (paths + already-read contents + parsed manifest).
interface BlockInput {
  label: string;
  kind: string;                    // "proposition" | "theorem" | "lemma" | "corollary" | "definition" | "remark" | "prose" | …
  md: string | null;              // .md contents
  ts: string | null;              // .ts contents (or parsed manifest fields)
  lean: string | null;           // sibling .lean contents, if any
  leanRef?: string;              // "qou:QOU.Foo.bar" if the manifest sets lean.ref
  paths: { md?: string; ts?: string; lean?: string };
  manifest: { uses?: string[]; interprets?: string; authorNotes?: unknown[]; /* … */ };
  // Optional: a corpus handle for cross-block checkers (see §4).
}
type CheckResult = { result: "pass" | "warn" | "fail" | "n/a"; notes: string };
```

A checker returns exactly one `CheckResult`; the sweep wraps it into a
`QaCriterionEntry` (stamping `field_hash`, `reviewed_at`, `reviewed_sha`,
`reviewer`). Checkers **do not** write sidecars themselves.

---

## 1. Defect → criterion map (what we are closing)

| Observed defect (from `prop:positive-definite-dagger`) | New criterion | §|
|---|---|---|
| `## Proof (sketch)` header on a `proposition` | `proof-sketch-vs-kind` | §2 |
| Prose says *"The Lean sibling states … defers via `sorry`"* | `proof-no-lean-mention-in-prose` | §3 |
| Same proof duplicated across `positive-definite-dagger.md` and `…-proof.md` (and the two disagree) | `proof-cross-block-duplication` | §4 |
| Narrative "sketch" that points at a `sorry` counts as a passing "honest deferral" | fix `narrative-lean-rerate` | §5 |

---

## 2. SPEC — `proof-sketch-vs-kind`

**Intent.** A block whose `kind` asserts a *proved* statement
(`theorem`/`proposition`/`lemma`/`corollary`) must present a **complete proof**,
not a sketch/outline. Sketches are legitimate only for `remark`/`prose`/`example`
(interpretive) blocks, or when the block is explicitly `conjecture`.

**Applies to.** `kind ∈ { theorem, proposition, lemma, corollary }`.
**`n/a` when.** `kind` is anything else (definition, remark, prose, conjecture,
example, equation, diagram, simulator). For those the notion "proof completeness"
does not apply.

**Inputs.** `md`, `kind`.

**Detection algorithm.**
1. Locate the proof region in `md`. The proof region is the content under a proof
   header. Recognize these header forms (case-insensitive, allowing markdown
   `#{1,6}` prefixes and bold `**…**`):
   - `Proof` / `## Proof`
   - `Proof (sketch)` / `Proof sketch` / `Proof outline` / `Sketch of proof` /
     `Proof idea` / `Proof (idea)` / `Proof (informal)`
2. **FAIL** if any proof header carries a **sketch qualifier**: a parenthetical or
   trailing word in the set
   `{ sketch, outline, idea, informal, heuristic, rough }`
   — e.g. matches `/^\s*#{0,6}\s*\**\s*proof\s*[\(:]\s*(sketch|outline|idea|informal|heuristic|rough)/im`
   or the bare-word `Proof sketch` / `Sketch of proof` variants.
3. **FAIL** if the proof body contains an explicit incompleteness admission in
   prose: case-insensitive whole-phrase match on
   `{ "we omit", "omitted here", "left to the reader", "details are left",
      "we only sketch", "a full proof will", "beyond the scope",
      "we do not prove", "sketch only" }`.
4. Otherwise **PASS**.

**False-positive guards.**
- Do **not** fire on the *word* "sketch" appearing in the mathematical content
  (e.g. "the sketch of the moduli space") — only on the **proof header** and on
  the fixed admission phrases above. Anchor rule 2 to the header line; anchor
  rule 3 to whole-phrase matches, not substrings.
- A `conjecture`-kind block is `n/a` (rule "Applies to"), so a "Proof sketch"
  under a conjecture never fires.
- The §3b-cond **conditional** theorems are still provable-kind and still in
  scope: a conditional theorem must present a *complete conditional* proof
  (proof modulo the named class hypothesis), not a sketch. Do not exempt them.

**Severity.** `major`. **`automated`.** `true`.

**Opt-out.** None. (If a genuine exception arises, the correct action is to change
the block `kind` to `remark`/`conjecture`, not to silence the checker.)

**Sidecar entry examples.**
- FAIL: `notes: "proposition block presents 'Proof (sketch)'; a provable-kind block must give a complete proof (or be re-kinded remark/conjecture)."`
- PASS: `notes: "Proof header present with no sketch qualifier or incompleteness admission."`
- N/A: `notes: "kind=remark; proof-completeness criterion does not apply."`

**Test fixtures (add under the platform's checker test dir).**
| Fixture | kind | md proof header | Expected |
|---|---|---|---|
| `sketch-on-prop` | proposition | `## Proof (sketch)` | fail |
| `sketch-of-proof` | theorem | `**Sketch of proof.**` | fail |
| `omit-admission` | lemma | `## Proof` + body "we omit the routine check" | fail |
| `full-proof` | proposition | `## Proof` + complete body | pass |
| `conditional-full` | theorem | `## Proof` (modulo class) complete | pass |
| `remark-sketch` | remark | `## Proof (sketch)` | n/a |
| `conjecture-sketch` | conjecture | `## Proof sketch` | n/a |
| `word-sketch-in-body` | proposition | `## Proof` + body mentions "sketch of the curve" | pass |

---

## 3. SPEC — `proof-no-lean-mention-in-prose`

**Intent.** Scholarly narrative must not break the fourth wall by describing its
own formalization apparatus. Sentences like *"The Lean sibling states existence
of a `PositiveDefiniteStructure` and defers the construction via `sorry`"* leak
build-status/tooling into the published voice. This is a one-voice violation the
existing `voice-*` axis does not cover (it only migrates status **banners**).

**NOTE — relation to `proof-narrative-lean-equivalence`.** That skill *wants* the
narrative to be faithful to the Lean, and even to note what is deferred. This
checker does **not** contradict it: faithfulness is about *mathematical content*;
this checker bans *prose references to the formalization machinery as such*. "The
result is proved modulo the positivity of the pairing" is fine; "the Lean file
uses a `sorry`" is not.

**Applies to.** All blocks that render into the paper: `kind ∈ { theorem,
proposition, lemma, corollary, definition, remark, prose, example, conjecture,
equation }`. In practice: any block with an `md`.
**`n/a` when.** No `md` content (e.g. `simulator`/`diagram`-only blocks), or the
block is a Chapter-8 glossary block (tag `glossary`) whose whole purpose is to
name Mathlib decls.

**Inputs.** `md`, `kind`, manifest tags.

**Detection algorithm.** Scan the **rendered prose** of `md` — i.e. text
**outside** math (`$…$`, `$$…$$`) and outside fenced code blocks (```` ``` ````,
including ```` ```lean ````/```` ```tex ````). Within prose only, **FAIL** on a
case-insensitive match of any apparatus token as a whole word/phrase:

- `Lean` (as a whole word — guard against "clean", "Boolean": require word
  boundaries and, to cut FPs, require it to co-occur in the same sentence with one
  of the apparatus context words below, OR match the multiword phrases directly)
- Multiword phrases (match directly, no co-occurrence needed):
  `"Lean sibling"`, `"Lean file"`, `"Lean encoding"`, `"Lean formalization"`,
  `"Lean proof"`, `"the .lean"`, `"sorry stub"`, `"via sorry"`, `"a sorry"`,
  `"defers … via sorry"`, `"Mathlib"`, `"lake build"`, `"content-block sibling"`.
- Apparatus context words (for the bare-`Lean` co-occurrence rule):
  `{ sibling, file, formaliz, encoding, stub, sorry, theorem-name, declaration }`.

**FAIL** if any match; else **PASS**.

**False-positive guards.**
- Never scan inside math or code fences. A ```` ```lean ```` block that is
  *legitimately* showing Lean (some remark blocks include a Lean snippet as
  content) is **not** prose and must be skipped. (If the platform later wants to
  ban Lean-in-content-fences too, that is a *separate* criterion, not this one.)
- The word `sorry` in ordinary English ("sorry for the digression" — should not
  occur in scholarly voice anyway) is not the target; require it near an apparatus
  context word or as one of the fixed phrases (`via sorry`, `sorry stub`).
- Glossary blocks (`tag: glossary`) legitimately name Mathlib types → `n/a`.

**Severity.** `major`. **`automated`.** `true`.

**Opt-out.** A per-block escape hatch for the rare legitimate case (a block whose
*subject* is the formalization itself — e.g. a methodology remark): honor an
explicit manifest marker `authorNotes` of kind `note` containing the token
`@allow-lean-mention`, OR an HTML-comment marker `<!-- qa-allow: proof-no-lean-mention-in-prose -->`
in the `md`. When present, emit `n/a` with `notes: "opt-out marker present."`
Keep the opt-out mechanism identical to whatever the platform already uses for
other criteria `⟨confirm against live source⟩`; do not invent a second style.

**Sidecar entry examples.**
- FAIL: `notes: "narrative prose references the formalization apparatus ('The Lean sibling … defers via sorry'); move to authorNotes or delete — scholarly prose must not describe its own Lean/sorry machinery."`
- PASS: `notes: "no Lean/sorry/Mathlib apparatus references in prose."`

**Test fixtures.**
| Fixture | md prose contains | Expected |
|---|---|---|
| `lean-sibling-sentence` | "The Lean sibling states … via `sorry`." | fail |
| `mathlib-mention` | "…wraps the Mathlib type `Monoidal`." (non-glossary) | fail |
| `clean-word` | "…a clean quotient…" | pass |
| `boolean-word` | "…a Boolean algebra…" | pass |
| `lean-in-code-fence` | ```` ```lean\ntheorem foo … ```` only | pass |
| `sorry-in-math` | `$\sorry$`-free legit math | pass |
| `glossary-mathlib` | glossary block naming `Mathlib.CategoryTheory…` | n/a |
| `opt-out` | apparatus sentence + `<!-- qa-allow: proof-no-lean-mention-in-prose -->` | n/a |

---

## 4. SPEC — `proof-cross-block-duplication`

**Intent.** The same proof/argument must not be authored twice across sibling
blocks. In the incident, the proof lived in **both** `positive-definite-dagger.md`
(a `proposition` with an inline proof) **and** `positive-definite-dagger-proof.md`
(a separate `prf:` block) — and the two even **disagreed** on the argument. This
is a maintenance and correctness hazard: the two copies drift.

**NOTE — this is a *corpus-level* checker.** Unlike §2/§3, it needs to compare a
block against other blocks. It still runs deterministically in the sweep, but its
input is the block **plus** its immediate relatives (see "Scope of comparison").

**Applies to.** Blocks that contain a proof region: `kind ∈ { theorem,
proposition, lemma, corollary }` **with** an inline proof, and dedicated proof
blocks (`kind` proof / label prefix `prf:`).
**`n/a` when.** The block has no proof region at all.

**Scope of comparison (bounded — do not diff against the whole corpus).**
For a block `B`, compare `B`'s proof region against the proof regions of:
1. Any block `P` whose `uses[]` or `interprets` points at `B` (typical `prf:`
   pattern: the proof block `uses: [B.label]`), **and**
2. Any block `B` itself points at via `interprets`/`uses` that is a proof block,
   **and**
3. Sibling blocks sharing the same file-root stem (`foo.md` ↔ `foo-proof.md`).

This keeps the comparison O(neighbors), not O(corpus²).

**Detection algorithm.**
1. Extract the proof region text of `B` and of each in-scope relative `R`
   (strip markdown, normalize whitespace, drop math-delimiter noise but keep the
   math token stream).
2. Compute a similarity score (token-shingling / Jaccard over 4-grams, or the
   platform's existing text-similarity util `⟨confirm against live source⟩`).
3. **FAIL** if `similarity(B, R) ≥ 0.80` for any in-scope `R` **and** `B` and `R`
   are *distinct* blocks both claiming to be authoritative (i.e. both carry a
   proof region rather than one `interprets`-ing the other as a sketch). Report
   which relative and the score.
4. **WARN** if `0.55 ≤ similarity < 0.80` (near-duplicate; likely drifted copies —
   the incident's two disagreeing proofs land here if they were paraphrased).
5. Otherwise **PASS**.

**Disambiguation — legitimate proof block vs duplication.**
The correct architecture is: `proposition` (statement, no inline proof) →
`prf:` proof block (`uses: [prop]`). That is **not** a duplication — the statement
has no proof region to collide with. Duplication is specifically **two proof
regions** for the same statement. So:
- If `B` is a `proposition` with **no** inline proof and `R` is its `prf:` block →
  PASS (canonical split).
- If `B` is a `proposition` **with** an inline proof **and** `R` is a `prf:` block
  proving the same statement → FAIL (the proof exists twice; delete the inline one
  or merge).

**False-positive guards.**
- Boilerplate openers ("By the universal property…", "Immediate from the
  definition.") are short; require a minimum proof-region length (e.g. ≥ 40
  tokens) before scoring, so one-liners don't collide.
- Two genuinely different proofs of the same statement (a second proof offered
  deliberately) should be labeled — honor an opt-out marker
  `<!-- qa-allow: proof-cross-block-duplication (second proof) -->` → `n/a`.

**Severity.** `major` (FAIL), surfaced as `warn` in the 0.55–0.80 band.
**`automated`.** `true`.

**Sidecar entry examples.**
- FAIL: `notes: "proof region duplicates prf:positive-definite-dagger (Jaccard 0.83); statement carries an inline proof AND a separate proof block. Keep one authoritative proof."`
- WARN: `notes: "proof region near-duplicates …-proof.md (Jaccard 0.61) and the two arguments diverge; reconcile."`
- PASS: `notes: "canonical statement/proof split; no duplicate proof region."`

**Test fixtures.**
| Fixture pair | Shape | Expected |
|---|---|---|
| `inline+prfblock-identical` | prop w/ inline proof + `prf:` copy | fail |
| `inline+prfblock-paraphrased-divergent` | prop w/ inline proof + `prf:` paraphrase that disagrees | warn |
| `canonical-split` | prop w/o inline proof + `prf:` block | pass |
| `two-distinct-proofs-optout` | two proofs + opt-out marker | n/a |
| `short-boilerplate-collision` | two lemmas both "Immediate from def." | pass (below length floor) |

---

## 5. SPEC — fix `narrative-lean-rerate` ("honest deferral = pass")

**Problem.** On 2026-06-24 (qou PR #2715) the `local/narrative-lean-rerate` script
flipped `proof-narrative-lean-equiv` from **fail → pass** on
`prop:positive-definite-dagger`, with rationale: *"Honest deferral proof added:
narrative gives the argument and cites the upstream result the Lean `sorry`
defers."* That rule is too permissive: it accepted a **sketch that points at a
`sorry`** as equivalent to the Lean, greenlighting exactly the defect in §2.

**Required change.** Tighten the rerate's "honest deferral" branch so it can only
return `pass` when the narrative is a **genuine complete argument**, not a sketch
or a deferral-by-pointer. Concretely, `narrative-lean-rerate` must return `pass`
on the honest-deferral branch **only if all** of:

1. **The narrative is not a sketch.** Run the §2 `proof-sketch-vs-kind` predicate
   on the block; if it would FAIL (sketch qualifier or incompleteness admission),
   the rerate must **not** pass — return `fail` (or defer to agent) instead.
2. **The narrative does not itself invoke the deferral as its proof.** If the
   narrative's completeness *depends on* a sentence describing the Lean `sorry`
   / "deferred via `-- Ref:`" as the justification (i.e. the §3
   `proof-no-lean-mention-in-prose` predicate FAILs on the proof region), the
   rerate must not pass.
3. **The Lean side's `sorry` is covered by a legitimate deferral contract** — a
   `conjecture`/`§3b-cond` class hypothesis with a `-- Ref:` citation — **and**
   the narrative carries the matching **conditional banner** ("Theorem
   (conditional on `conj:…`)"), so the reader knows the result is conditional.
   A bare `sorry` with `-- Ref: [manuscript]` and an unconditional narrative
   claim is **not** honest deferral — it is an unproved claim dressed as proved.

If (1)–(3) do not all hold, `narrative-lean-rerate` must leave the criterion at
`fail` (or route to agent re-audit), **never** upgrade to `pass`.

**NOTE.** This aligns the rerate with the honest dispositions the qou side already
applied to the incident block: `prop:positive-definite-dagger` was **re-kinded to
a conditional theorem** (qou commit `ae708c05`) rather than left as a
"sketch + sorry = pass". The rerate must produce the same judgment mechanically.

**Test fixtures.**
| Fixture | Narrative | Lean | Expected rerate |
|---|---|---|---|
| `sketch-points-at-sorry` | "Proof (sketch)… deferred via sorry" | `sorry` | fail (was: pass) |
| `full-conditional-banner` | complete proof modulo named class + banner | class hypothesis + `-- Ref:` | pass |
| `full-unconditional-vs-sorry` | complete-looking unconditional claim | bare `sorry` | fail |
| `genuine-equiv` | complete proof | complete Lean, no sorry | pass |

---

## 5A. SPEC — `expo-milnor-clarity` (agent-judged exposition rater)

**NOTE — this criterion is a different class from §2–§4.** "Does this block read
with the clarity of John Milnor's exposition?" is an **aesthetic judgment**, not a
deterministic property. It is therefore an **agent-reviewed** criterion
(`automated: false`) that emits a **score + rationale**. **Per owner ruling
(2026-07-04) it is a GATING criterion with a strict bar**: only a perfect score
`pass`es; anything short of perfect is `warn` (near-miss) or `fail`. The paper's
exposition is held to Milnor's standard, not merely nudged toward it.

**Intent.** Nudge narrative blocks toward the expository virtues that make
Milnor's writing a gold standard: economy, concreteness-before-abstraction, plain
motivation, minimal notation, and a visibly linear argument. The rater surfaces
where a block is muddy, over-notated, or unmotivated — as an author aid, not a
gate.

**Exemplar corpus (the standard the rater judges against).** John Milnor's
expository works: *Morse Theory*; *Characteristic Classes* (with Stasheff);
*Topology from the Differentiable Viewpoint*; *Lectures on the h-Cobordism
Theorem*; and his survey articles. The rater is not asked "did Milnor write this"
— it is asked "does this block exhibit the **operational hallmarks** below."

**Applies to.** Narrative-bearing blocks: `kind ∈ { definition, theorem,
proposition, lemma, corollary, remark, prose, example, conjecture }` with
non-trivial `md` prose (≥ ~50 words).
**`n/a` when.** Pure `equation`/`diagram`/`simulator` blocks, glossary blocks, or
blocks with essentially no prose (a bare statement + formula). Aesthetic clarity
does not apply to a one-line formula.

**Operational hallmarks (the rubric — 8 dimensions, each scored 0–2).**
H7 and H8 were added at owner request (2026-07-04) to capture the specific
Milnor sub-aspects: *surgical cleanliness / right-tool framing* and *respect for
the reader's time and intelligence*.

| # | Dimension | 2 (Milnor-like) | 0 (un-Milnor) |
|---|---|---|---|
| H1 | **Economy** | no wasted words; short declarative sentences; every sentence load-bearing | padded, throat-clearing, restating the obvious |
| H2 | **Concrete-before-abstract** | a guiding example / picture / special case appears before or alongside the general statement | abstraction dumped with no anchor |
| H3 | **The "Why" precedes the "What"** | the reader is told the *purpose / goal* before the machinery; motivation is stated up front, not back-filled | machinery introduced with no stated purpose; the "why" (if any) arrives after the "what" |
| H4 | **Uncluttered notation** | notation is lightweight; the reader wrestles only with concepts, never with symbols; each symbol introduced at point of first use; no glyph reuse | a wall of symbols defined before any are used; the reader fights the notation |
| H5 | **Linear argument** | each step visibly follows the previous; no forward references to un-introduced ideas | non-sequiturs; "as we will see" leaning on later material |
| H6 | **Prose carries the argument** | sentences explain; formulas punctuate | formulas replace explanation; the reader must reverse-engineer intent |
| H7 | **Surgical cleanliness / right-tool framing** | every unnecessary technicality is stripped; when a heavy result (a big theorem, a hard lemma) is invoked, it is framed so its *necessity is obvious* — the reader sees *why it is the exact tool* for the problem at hand | technicalities piled in "for completeness"; heavy tools dropped in unframed, so the reader cannot see why they are needed |
| H8 | **Respect for the reader's time and intelligence** | trusts the reader — no belaboring the trivial, no condescension, no ceremony; also no disrespectful *gaps* (nothing load-bearing hand-waved) | over-explains the obvious *or* hand-waves the hard part; wastes the reader's attention either way |

**Score → result mapping (owner ruling 2026-07-04 — STRICT gate).** Total
`T = Σ Hi ∈ [0,16]`.
- `T = 16` → **pass** (perfect — every one of H1–H8 scored 2). `notes` records the
  full score vector.
- `12 ≤ T ≤ 15` → **warn** (near-miss; `notes` names every dimension scored < 2
  with a one-sentence concrete fix each).
- `T ≤ 11` → **fail** (`notes` names the failing dimensions and recommends a full
  exposition pass).

This is a deliberately strict bar: the Milnor standard is *perfection*, and a
single non-perfect dimension already drops the block out of `pass`. The rater
**blocks** in `--ci` on `fail` like any gating criterion.

**Agent prompt template (the reviewer runs this).**
> You are reviewing one narrative block from a formal-mathematics paper for
> **expository clarity**, using John Milnor's writing (*Morse Theory*,
> *Characteristic Classes*, *Topology from the Differentiable Viewpoint*) as the
> gold standard. Do **not** judge mathematical correctness, novelty, or whether
> the result is true — only how *clearly and economically it is written*. Score
> each of the eight dimensions H1–H8 (0, 1, or 2) using the rubric. Pay particular
> attention to H7 (is every heavy tool framed so its necessity is obvious? is every
> unnecessary technicality stripped?) and H8 (does it respect the reader — neither
> belaboring the trivial nor hand-waving the hard part?). Return JSON:
> `{ "scores": {H1..H8}, "total": T, "weakest": ["Hk", …],
>    "suggestions": ["concrete one-liner per weak dimension"],
>    "result": "pass" | "warn" | "fail", "notes": "≤ 200-char summary" }`.
> Return `pass` ONLY if every dimension scored 2 (T = 16); `warn` for T in 12–15;
> `fail` for T ≤ 11.
> Be terse and specific; cite the offending sentence/notation. Reward
> understatement; penalize hype, padding, and notation dumped before use.

**Reviewer.** `{ kind: "agent", id: "local/expo-milnor-rater", version: "1.0" }`.
The rater is registered `automated: false`, so it enters the agent-drain queue
(`QA_CRITERIA_REGISTRY.filter(c => !c.automated)`) and is satisfied when an agent
writes a fresh sidecar entry. Staleness: re-run when `field_hash.md` drifts (the
`.md` is the only input that matters — `.ts`/`.lean` changes do not restale it).

**Severity.** `major` (gating — it can `fail`; owner ruling 2026-07-04).
**`automated`.** `false`. **Axis.** `expo` — registered in the
folio-assistant `qa-criteria-registry.ts` `EXPO` domain and
`WATCHER_CRITERIA_BY_AXIS.expo` (as of 2026-07-05), alongside the
companion `milnor-brevity` rater (§5B).

**Anti-flag-loss note (ties to §6).** Because this is an agent rater, it is exactly
the class of verdict that the 2026-06-25 distrust-clear damaged. Two safeguards:
1. The rater records the **full per-dimension score vector** in `notes`/a
   structured field, so a re-review is a *re-score*, not a from-scratch reguess —
   reducing verdict volatility and the temptation to distrust a whole batch.
2. Per §6, a distrusted rater verdict must be **re-run**, never cleared to `n/a`.
   Because the gate can now produce `fail`, this is a genuine blocking flag — a
   distrusted `fail`/`warn` must be re-audited, never silently `n/a`-cleared (the
   exact anti-pattern the §6 guard fails CI on).

**Test fixtures (agent-rater fixtures are calibration prompts, not exact-match).**
| Fixture | Character | Expected band |
|---|---|---|
| `milnor-clean` | tight, example-first, motivated, few symbols — every dimension a 2 | pass (`T = 16`) |
| `one-dim-off` | otherwise clean but one dimension scores < 2 | warn (`T` 12–15) |
| `several-dims-off` | muddy on ≥ 3 dimensions | fail (`T ≤ 11`) |
| `notation-wall` | 8 symbols defined before any used | warn, weakest = H4 |
| `unmotivated-machinery` | abstract construction, no stated purpose | warn, weakest = H3 |
| `padded-prose` | verbose, throat-clearing, restates statement | warn, weakest = H1 |
| `formula-dump` | argument carried entirely by displayed equations | warn, weakest = H6 |
| `unframed-heavy-tool` | invokes Sard's theorem with no framing of why it's the right tool | warn, weakest = H7 |
| `technicality-pileup` | correct but padded with "for completeness" technicalities | warn, weakest = H7 |
| `condescending-over-explain` | belabors a trivial step over three sentences | warn, weakest = H8 |
| `handwaves-hard-part` | glosses the load-bearing step as "clearly" | warn, weakest = H8 |
| `bare-equation-block` | one formula, no prose | n/a |

**Design decision recorded (owner ruling 2026-07-04 — so the implementing agent
does not re-litigate it):** this rater is **gating with a strict bar** —
`pass` iff `T = 16`, `warn` for 12–15, `fail` for `T ≤ 11`. An earlier draft made
it advisory (pass/warn only); the owner overrode that: the paper's exposition is
held *to* the Milnor standard, not merely nudged toward it. Because agent scoring
of a 0–2 rubric carries some variance, implementers should (a) keep the per-block
score vector in the sidecar so re-reviews re-score rather than re-guess, and
(b) treat a `fail` as an author-actionable exposition defect (name the failing
dimensions), not a mysterious rejection.

---

## 5B. SPEC — `milnor-brevity` (agent-judged intra-block de-duplication)

**Added 2026-07-05 at owner request.** A **companion** to
`expo-milnor-clarity` (§5A). Where §5A scores overall Milnor quality
(H1–H8), `milnor-brevity` isolates one sub-property — **no content is
repeated within a block** — and gives it a **stricter, deletion-aware
resolve discipline**. It is registered separately (and reviewed more
carefully) precisely *because* its remedy can involve **deleting** prose,
which the clarity drain otherwise treats conservatively.

**Intent.** Milnor's economy (H1) forbids restating the same point twice.
`milnor-brevity` surfaces where a block says the *same thing* more than
once — a claim, a definition, a motivation, an example, or a numeric
result repeated in two places — so the redundant copy can be removed *or*
the block restructured. It is the "same content is not repeated /
duplicated in the block" check.

**Applies to.** The same narrative-bearing kinds as §5A: `definition,
theorem, proposition, lemma, corollary, remark, prose, example,
conjecture` with ≥ ~50 words of prose. **`n/a`** on pure
equation/diagram/simulator/glossary and near-empty blocks.

**What the rater detects (audit).** Intra-block semantic duplication.
For each duplicated span, the rater **classifies** it into exactly one of
two kinds — this classification is what governs the (strict) resolve:

| Class | Meaning | Deletion permitted? |
|---|---|---|
| **exact-dup** | the two occurrences are **semantically identical** — the second adds, qualifies, or changes *nothing* | **Yes** — one copy may be deleted |
| **differs** | the second occurrence **adds or changes** content (a new qualifier, a sharper bound, a different framing, an extra case) | **No** — deletion forbidden; the distinct content must be preserved |

**Score → result.** Total redundancy is scored by the count of duplicated
spans `k`: `k = 0` → `pass`; `1 ≤ k ≤ 2` → `warn`; `k ≥ 3` (or a whole
paragraph restated) → `fail`. The **`duplications` array** is the detailed
record — each entry carries the span, its class (`exact-dup` / `differs`),
and the two source locations; **`notes` is only the ≤ 200-char summary**
(it does not re-list the spans).

**Resolve discipline (STRICT — this is the point of the separate
criterion).** The resolve agent may:

1. **Delete a repeat ONLY when its class is `exact-dup`** (content
   unchanged between the two occurrences). Cite the deleted span + the
   surviving copy in the resolve record.
2. **NEVER delete a `differs` span.** If the content changed, deletion
   would lose information. Instead **merge** the two occurrences into one
   statement that preserves *every* distinct point, or keep both.
3. **NEVER delete math content** — a diagram, display equation, `align`
   environment, or derivation body — even if it *looks* duplicated
   (inherits the §5A / drain `NO-DELETE-MATH-CONTENT` rule). A repeated
   equation is re-expressed by prose reference, not deleted.
4. **A block MAY be split** into two or more blocks when de-duplication
   would otherwise cram distinct ideas together, or when separating a
   repeated setup from its result aids explication (e.g. a `prose` setup
   block + the `proposition` it motivates). Splitting is the *preferred*
   remedy when content differs but is entangled.

**Careful-review gate (STRICT).** Because the remedy involves deletion,
`milnor-brevity` resolves are **not** auto-mergeable in an autonomous
exposition drain. Every `milnor-brevity` edit — and unconditionally every
**deletion** — is held for **human / reviewer sign-off before merge**
(Gemini + Copilot review at minimum; owner sign-off for any block split
or any deletion the reviewer flags). The autonomous `expo-milnor-clarity`
drain runs `milnor-brevity` in **audit-only** mode by default (it *flags*
duplication into the sidecar); the *resolve* is a deliberate, reviewed
pass.

**Agent prompt template.**

> You are auditing one narrative block from a formal-mathematics paper for
> **intra-block redundancy**, the Milnor economy sub-property "the same
> content is never stated twice in one block." Do not judge overall
> clarity (that is `expo-milnor-clarity`) or correctness — only whether
> any content is **duplicated within this block**. For each duplicated
> span, record the two locations and classify it: **exact-dup** (the
> second occurrence adds/changes nothing) or **differs** (the second adds
> a qualifier, a sharper claim, a new case, or a different framing).
> Return JSON of this shape (do not emit literal `|` — each field holds one
> string value from the allowed set): `{ "duplications": [{ "span": "...",
> "loc_a": "...", "loc_b": "...", "class": "..." }], "result": "...",
> "notes": "≤ 200-char summary" }`, where each `class` is `"exact-dup"` or
> `"differs"`, and `result` is `"pass"`, `"warn"`, or `"fail"`. `pass` iff
> `duplications` is empty; `warn` for 1–2 duplicated spans; `fail` for ≥ 3
> or a restated paragraph.
>
> **Resolve (only when authorised — this criterion is human-reviewed):**
> Edit the `.md` prose. Delete a span ONLY if its class is `exact-dup`.
> Never delete a `differs` span — merge preserving every distinct point,
> or split the block. Never delete a diagram / equation / derivation.
> Prefer splitting the block over cramming distinct ideas together.

**Reviewer.** `{ kind: "agent", id: "local/milnor-brevity-rater",
version: "1.0" }`. Registered `automated: false`; enters the agent-drain
queue; satisfied by a fresh sidecar entry. Staleness: re-run when
`field_hash.md` drifts.

**Severity.** `major`. **`automated`.** `false`. **Axis.** `expo`
(grouped with `expo-milnor-clarity`; both registered in the folio-assistant
`qa-criteria-registry.ts` `EXPO` domain / `WATCHER_CRITERIA_BY_AXIS.expo`).

**Relationship to §5A.** A block can be `expo-milnor-clarity: warn`
(muddy) yet `milnor-brevity: pass` (not repetitive), or vice-versa. They
are scored independently and stored as two sidecar entries. Clarity's
resolve is conservative-additive (motivation-first, reorderings);
brevity's resolve is the deletion-aware pass and therefore carries the
extra review gate above.

**Test fixtures (calibration prompts).**
| Fixture | Character | Expected |
|---|---|---|
| `no-repeat` | every point stated once | pass |
| `exact-restate` | a sentence's claim restated verbatim later | warn, one `exact-dup` |
| `qualified-restate` | a claim restated *with an added qualifier* | warn, one `differs` (NO deletion) |
| `paragraph-echo` | a whole paragraph's content repeated | fail |
| `repeated-equation` | same display equation twice | warn, but resolve re-refs, never deletes |
| `entangled-two-ideas` | two distinct ideas interleaved + partly repeated | warn, resolve = **split** |

---

## 6. SPEC — interaction with the qou-side distrust-clear guard

The qou repo now ships
[`folio/pipeline/qa-flag-preservation-audit.ts`](../../folio/pipeline/qa-flag-preservation-audit.ts),
which **fails CI** if any criterion's latest sidecar entry is a distrust-`n/a`
masking a prior `fail`/`warn`. The new checkers must respect the same principle:

1. **Never emit a distrust-`n/a`.** These are deterministic scripts; they either
   apply (pass/warn/fail) or genuinely don't apply (`n/a` per the "Applies to /
   n/a when" clause). There is no "distrusted verdict" state for a script checker.
2. **When a script checker supersedes a prior agent verdict**, it does so with a
   real result (pass/warn/fail), which is legitimate — the deterministic check is
   more trustworthy than the distrusted agent batch. This is the *intended*
   healing path: adding these checkers lets the sweep re-verdict the 9 files /
   20 criteria that PR #3289 reinstated, clearing the guard.
3. **Do not let a new criterion regress a block to green via `n/a`** where the old
   agent verdict was `fail` for a *different* reason. The new criteria are
   additive; they must not overwrite unrelated criteria's entries.

---

## 7. Acceptance criteria (definition of done)

A folio-assistant PR implementing this doc is complete when:

- [ ] `proof-sketch-vs-kind`, `proof-no-lean-mention-in-prose`, and
      `proof-cross-block-duplication` are registered in `QA_CRITERIA_REGISTRY`
      with `automated: true`, correct axis/severity, and are wired into
      `qa-sweep.ts`.
- [ ] Each checker has the fixtures in its §-table passing (green for
      pass/n/a, red for fail/warn as specified) in the platform test suite.
- [ ] Running the sweep over the qou corpus (`bun run …/qa-sweep.ts <qou-content>`)
      flags `prop:positive-definite-dagger`'s **historical** state:
      `proof-sketch-vs-kind` = fail on the pre-fix `.md` (sketch header),
      `proof-no-lean-mention-in-prose` = fail on the pre-fix `.md` (Lean-sibling
      sentence), and `proof-cross-block-duplication` = fail/warn on the
      `…-proof.md` pair. (After qou commit `ae708c05` these should clear on the
      current `.md`, which is the regression test.)
- [ ] `narrative-lean-rerate` no longer returns `pass` on the
      `sketch-points-at-sorry` fixture (§5).
- [ ] None of the four changes ever emits a distrust-`n/a` (§6).
- [ ] The registry additions are documented in the platform's QA criteria doc /
      `AGENTS.md` skill-routing table as appropriate.

---

## 8. Out of scope (explicitly)

- Migrating the ~840 muon-q₀ witnesses, any q₀ convention work — unrelated.
- The qou-side flag-preservation guard (already shipped in PR #3289).
- Re-auditing the reinstated 20 criteria by hand — the new deterministic checkers
  in §2–§4 are precisely what will re-verdict them once merged; that is the
  intended mechanism, not a manual backfill.
