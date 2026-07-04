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
   [`content/pipeline/qa-flag-preservation-audit.ts`](../../content/pipeline/qa-flag-preservation-audit.ts)
   (this doc's §6 explains how the new checkers must interact with it).
2. **Coverage gaps** — three of the four defect classes have **no deterministic
   criterion in the registry at all**, and the one axis that could catch the
   fourth (`proof-narrative-lean-equiv`) was *loosened* by a rerate that treats
   "honest deferral" as a pass. These are folio-assistant-side and are the
   subject of this document.

This document specifies **three new deterministic checkers** and **one fix to an
existing rerate rule**. It is written to be self-contained: the implementing
agent should not need the originating chat transcript.

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

## 6. SPEC — interaction with the qou-side distrust-clear guard

The qou repo now ships
[`content/pipeline/qa-flag-preservation-audit.ts`](../../content/pipeline/qa-flag-preservation-audit.ts),
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
