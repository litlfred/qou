# CONTENT: qou `folio/` (non-Lean) against current folio-assistant

**Measured on:** qou `afa49febf` (2026-10-04) and f-a `origin/main` `0b7b9e44e`, the same commit TARGET used. All work was read-only. I made two sandbox copies under `scratchpad/content/`:
- `qfull/`: a `git archive` of qou HEAD, plus f-a main at `folio-assistant/`, plus the `bootstrap` and `bootstrap-tools` submodules at their pinned SHAs.
- `qou/folio/`: a `.lean`-free copy, used for `tsc`.

I ran three things against those copies:
- f-a's real validators, through qou's own wrappers (`scripts/run-validate.ts`, `scripts/run-validate-references.ts`).
- `tsc --strict` over every manifest.
- A bun import dump of every manifest, using a stub for the builders (reusing ORPH's `dump.ts` approach, extended to recurse fully: `content/w/dump2.ts` → `rows2.json`).

**Outputs:**
- `CONTENT_inventory.tsv` has 7,446 rows: one per block root, one per sidecar, one per manifest, plus misc rows.
- `CONTENT_parity_baseline.tsv` has a git blob id for each block's `.ts`, `.md` and `.lean`, taken at `afa49febf`. It is the before half of every story's parity check.

## Headline

**The content is already schema-conformant. The defects are in its containers.**

- **Validator [M].** `run-validate` at f-a main reports all five folios valid (issues: qou 5, ugb 2, fred2005 2, bach2013 5, visualizer 2). Two per folio are sandbox/registry notices. Real ones: qou has 1 lemma without Lean (`piece-a-corner-removal-obligation`) and 2 missing simulator pages; bach2013 has 3 remarks without `interprets`.
- **Type check [M].** `tsc --strict` over 3,727 manifests found **one** class of manifest field the current schema lacks: `computation.consumers`, on 6 blocks. The only other error is inside `values/registry.ts`.
- **What follows** is container work: sidecars, JSON-LD, the shim, and data files. It also produces a short owner list.

## 1. Block kinds [M]

There are 3,677 blocks:

(QOU 3,620; ugb 33; fred2005 12; bach2013 9; visualizer 3.)

By kind: remark 1,022, proposition 630, proof 447, table 444, prose 391, definition 286, conjecture 182, example 107, theorem 66, lemma 51, corollary 19, algorithm 16, simulator 11, diagram 5.

Structural manifests: 42 chapters, 5 papers and 1 folio.

**No kind is unknown.** Every kind used is in `BLOCK_KINDS`. `equation` and `figure` are unused.

The shim `folio/schema/builders.ts` does **not re-export `figure`**, although f-a `builders.ts:220` exports it. This is latent: it only bites the first time someone authors a `figure` block.

Two files are not manifests at all: `identity.ts`, which deliberately has no default export, and `values/registry.ts`.

## 2. Field census vs `types.ts` [M]

Top-level fields: every field used is declared by `BlockBase` or by the kind's own interface. There are **0 unknown top-level fields**.

Most-used fields: label 3,614, title 3,341, uses 3,213, tags 2,689, lean 1,309, interprets 1,083, cites 724, authorNotes 652, computation 289.

**The one schema gap:** `computation.consumers: string[]`, on 6 blocks in `mass-theory/` and `nuclear-interactions/`. It names the Python scripts that read the witness.

- `ComputationSchema` (`constraints.ts:422`) is a non-strict `z.object`, so the field is **silently stripped**.
- `validate.ts:395` warns about unknown fields only at the top level, so nothing reports the loss.
- Proposed home: `upstream-to:cat-harness`. Add `consumers?: string[]` to `Computation`. It is container-only and the manifests do not change.

No manifest uses `companions`, `audience`, `renamedFrom`, `lang` or `poSources`.

## 3. Shapes of `uses[]`, `interprets`, `lean.ref`, `computation` and `simulator` [M]

**`uses`** holds 5,044 string entries. 14 entries look unresolved at first, but most are cross-paper (`<paper>:<label>`, which `isCrossPaperRef` skips).

- I re-resolved those against the target paper. Exactly **2 do not exist**: `unital-groebner-bases:thm:main-theorem` and `unital-groebner-bases:prop:jet-stratified-reduction`.
- 1 `sec:` reference is unresolved.

**`interprets`, `of` and `foreshadows`** all resolve: 1,083, 12 and 38 entries.

**`proofs[]`** has 2 unresolved targets: `prf:torus-knot-generators` and `prf:embeddability-closure`.

**`examples[]`** has 1 unresolved target: `rem:crossing-energy-decomposition`.

**`lean`** is always an object (1,309), with fields: `ref` 1,309, `validation` 1,176, `sorryFree` 9, `mathlibLinks` 1.
- Every `validation` value is legal.
- Package prefixes: `qou:` 1,275, `ugb:` 22, `fred2005:` 12.
- Sibling `.lean` resolution belongs to LEANNODES.

**`computation`** (289) is legal on all of its declared fields.
- Engines: python 125, mpmath 69, sympy 48, python+mpmath 31, numpy 5, snappea 3, scipy 3, python+numpy+cvxpy 2, rust 2, closed-form 1.
- Statuses: verified 225, experimental 52, failed 7, not_run 4, error 1.

**`authorNotes`** kinds are all legal: note 497, status 281, caveat 104, refined-framing 62, deprecated 6.

**`simulator`**:
- All 4 `simulator.ref` values resolve.
- The 11 simulator blocks point `html:` into `fsh-guts/deprecated/simulators/`. Two of those files are absent:
  - `descent_rate_probe.html`
  - `multi_level_jet_sum.html`
- 9 simulator manifests import `../../../folio-assistant/cat-harness/schemas/builders` directly, bypassing the shim. MIG counted "10". The 10th is the tool `pipeline/prefixless-ref-audit.ts`, not a block.

**Labels:**
- One duplicate across papers: `def:witt-vector-lift`, in `models-of-qous/` and in fred2005.
- 63 prose blocks have no label.
- 14 prose labels use prefixes outside `KNOWN_LABEL_PREFIXES`: `ssec`, `subsec`, `viz`, and bare `tm-*`. `isCrossPaperRef("ssec:x")` returns true, so a `uses` pointing at one of them would be skipped silently.

**Section membership:** 4 blocks are in no section, so they never render:
- `delta-max-numerical-scale`
- `atomic-q-reeb-universal-rho`
- `qbeta-toroidal-harmonics-basis`
- `audit/wigner-su4-alpha-cluster-probe`

No chapter lists a block that does not exist (0 dangling).

## 4. Content-object triple [M]

- **`.md`:** every block has one (0 missing).
- **`.qa.json`:** 25 blocks have none.
- **`.md` with no `.ts`:** there are 14, all under `*/audit/` (probe write-ups). They are not blocks; classify only.
- **`.jsonld`** is the fourth, generated companion (`gen-block-jsonld.ts`):
  - 3,613 are committed, and **all 3,613 are stale** against f-a main.
  - I regenerated QOU's 3,556 in the sandbox and diffed them: **every difference is in `@context` and nothing else**. Main adds `{"@base": "https://litlfred.github.io/folio/"}`.
  - 64 blocks have no `.jsonld`: the 63 unlabeled prose blocks plus 1 audit remark.
- **`.lean`:** 1,309 blocks carry a `lean.ref`. 897 of them have a co-located `.lean`; the rest resolve through the Lake tree, which is LEANNODES' scope.
  - 1 definition has a sibling `.lean` but no `lean.ref`.

## 5. `.qa.json` sidecars: derived vs judgement [M]

There are 3,653 files, 211 MB. All are `block-qa/v1`, holding 345,529 criterion entries.

Entries by `reviewer.kind`:

| reviewer.kind | entries | criteria | goes to |
|---|---|---|---|
| `script` | 219,086 | 103 | the **qa-reports branch** (derived; regenerate, do not copy by hand) |
| `agent` | 126,299 | 53 | **`test/attestations/block-qa/<mirror>.attestations.json`** (`qa-attestations/v1`, family `block-qa`) |
| `human` | 16 | 2 | attestations: q-usage-archimedean 14, fixed-q0 2 |
| `null` | 128 | 1 | **needs-owner**: unclassifiable (`milnor-amalgamated-flow`) |

The 128 null entries sit in 128 different files.

By file:

| file class | files |
|---|---|
| mixed (script + judgement) | 3,595 |
| derived-only | 45 |
| judgement-only | 13 |

So **3,608 files must be split, not moved**.

`AUDIT-REPORT.qa.json` is not a block sidecar.

**Schema conformance against f-a `BlockQaReport` [M]:** 256 of 3,653 files parse. **Every failure is in a judgement entry. All script entries conform.** The judgement-entry defects:

- 68,379 agent entries have no `field_hash`. All of them carry `[EXPIRED-NO-FIELD-HASH]`, and the file-level `$expired` note (on 3,398 files) explains why.
- 3,294 `score` objects (`proof-rater-*`) lack `max`.
- ~914 `severity` values are free-text reasons, not `critical|major|minor` (`trap-*` criteria).

The attestation store treats entries as opaque (`AttestedEntrySchema` is a record). So the rule is: **move judgements verbatim and never "repair" them**. Repairing would be editing judgements.

**Location.** f-a reads the legacy sibling location as a fallback and writes only `test/results/block-qa/`. Removing committed copies needs owner confirmation (as `5hox`). Unverified: whether `qa:attestations:migrate` reads downstream sibling sidecars. The stray `get_*.py` scripts read an `evaluations` key no sidecar carries, so they are dead.

## 6. values/, visualizer, other data

**`values/registry.ts`: a value-registry DI node.**
- It has 70 entries, injected through f-a `configureValueRegistry`.
- It is being superseded by Liquid `{{ qou.computations.<witness>.<path> }}` (58 uses) and `{{ qou.library.* }}` (6 uses).
- 4 `:val[...]` directives remain, in 2 `.md` files (`confinement-operator-selection-table1-data`, `benzene-threading-selection`). Converting them changes `.md` bytes → **needs-owner**, with rendered-output parity as the check.
- The registry restates f-a's `WitnessedValueEntry` instead of importing it.
- Entry `vol_4_1_decimal_50` writes `unit` instead of `units` and has no `defaultPrecision`. This is a `tsc` error.
- 7 Python scripts read the registry by path. Action: keep-as-data for now.

**The visualizer** is a `paperRef` in `folio.ts`. Its 3 blocks (`def:viz-brings-surface`, `def:viz-knot-complement`, `viz:intro`) define viewer-state types and carry `lean.ref`, so they are content. Whether the container is a *paper* or a viewer/tile is **needs-owner**. It is also why the folio has 5 papers. f-a's `validate-references` throws with more than one paper unless `--paper` is passed, and qou's `run-validate-references.ts` does not pass it, so it **exits 1 at f-a main** [M].

Other data: regenerate `foreshadows.json` and `lean-coverage.json` (stale: 3,144 vs 3,620 blocks); `topic-keywords.json` is context config; `bib-qa-verifications.json` maps to f-a `bib-verification`; the 148 `rendered/` files are `RenderedAsset` companions. **needs-owner:** `glossary.json` (stale since 2026-05-20), `jwst-observational-data.json` (5 fit numbers with no producer; values untouched), `references.review.json` (a human judgement with no attestation family), and bach2013 (tagged `imported`: library entry rather than paper?).

**`folio/pipeline/` (30 files).** TOOLS may overlap here.

- **Three are stale forks** of f-a `cat-harness/content/pipeline/` (`language-trap-audit`, `qa-agent-entry`, `qa-agent-drain-queue`). Action: `upstream-to:cat-harness`, after a diff.
- **The rest are qou Tools** with their tests. Two of them compute math (`braid-alexander`, `braid-word-closure-check`); keep those byte-identical.
- **`triage_stubs.ts` is destructive:**
  - it calls `unlinkSync` on `.lean` "shadows";
  - it rewrites placeholder files;
  - it has no docblock;
  - **it must not run during migration** (needs-owner).

## Proposed stories (epic `qou-n4r9`, or a sibling "C: content conformance")

**Common parity done-when, P-C.** Recompute `git ls-files -s folio` and compare it with `CONTENT_parity_baseline.tsv`:
- every `.md` and `.lean` blob is identical;
- every `.ts` blob is identical, except the lines the story names.

`run-validate` must produce the same issue set, per folio.

1. **C1: Regenerate JSON-LD at the pin** (S; depends on the S2 pin bump).
   - Run `gen-block-jsonld.ts`.
   - Done when: `--check` is green; each `.jsonld` diff touches only `@context`, or the file is new; P-C holds with zero `.ts` exceptions.
2. **C2: Shim conformance** (S; S2).
   - Route 9 simulator imports through `../../schema/builders` (one import line each).
   - Add `figure` to the shim.
   - Done when: `grep "folio-assistant/" folio/**/*.ts` hits only the shim and `pipeline/`; P-C holds with an exception for line 1 of those 9 files only.
3. **C3 (platform, cat-harness): `computation.consumers`, and nested unknown-field reporting** (S; none).
   - Done when: `tsc` over qou shows 0 TS2353; a test shows a nested unknown field is warned about; P-C holds with 0 qou edits.
4. **C4: Split the 3,653 sidecars** (L; S1 declares `test/attestations` + `qa` storage; owner confirm for removal).
   - Derived: `qa:refresh` → `qa:publish` to qou's qa-reports branch.
   - Judgements: `qa:attestations:migrate`, verbatim.
   - Done when: the attestation store holds exactly 126,315 agent+human entries; the 128 null entries have an owner ruling; `qa:verify-moved` answers IDENTICAL; `qa:attestations:migrate:check` exits 0; P-C holds.
5. **C5: Owner list of editorial references** (S; none).
   - Items: 2 cross-paper `uses` to missing labels, 2 `proofs[]`, 1 `examples[]`, the duplicate `def:witt-vector-lift`, 4 unsectioned blocks, 63 unlabeled prose blocks, 14 non-standard prose prefixes.
   - Done when: there is a ruling per item; any `.ts` change is to a reference field only; P-C holds.
6. **C6: Close out values → Liquid** (S; owner).
   - The 4 `:val` directives, the `vol_4_1` entry, and importing the type from f-a.
   - Done when: rendered TeX/HTML is byte-identical before and after; the `.md` diff is directive syntax only and is owner-approved.
7. **C7: Classify the data and stray files** (S; owner).
   - Covers glossary/lean-coverage/foreshadows (regenerate), jwst, bach2013-as-library, visualizer-as-paper, `references.review.json`, `get_*.py`, `triage_stubs.ts`, `folio/package.json`, and the empty `bib-qa-images/`.
   - Done when: there is a ruling per row; nothing is deleted without confirmation; P-C holds.
8. **C8: `folio/pipeline` → Tools** (M; coordinate with TOOLS).
   - Diff the 3 forks and upstream them; declare 26 Tool and test nodes.
   - Done when: each script resolves as a Tool node; the math scripts are byte-identical; P-C holds.

## Skill and platform gaps for folio-assistant

1. **Nested unknown fields are stripped silently.** Non-strict nested zod schemas plus a top-level-only warning (`validate.ts:395`). This is the `dh4f` class one level down.
2. **Multi-paper folios.** `validate-references` / `leanArchiveDir` require a sole paper. No skill says a downstream wrapper must pass `--paper`.
3. **The `qa-reports` skill covers f-a's own `test/results`.** It is silent on:
   - a downstream folio whose block sidecars sit **beside** the blocks;
   - judgement entries that fail `BlockQaReport` (expired, malformed). These should be carried verbatim, and the skill does not say so.
4. **No container-migration parity skill.** Nothing defines a blob-id baseline census that proves "container-only", which is the owner's hard rule. Suggested home: `deletion-requires-confirmation`'s neighbour in conduct-core.
5. **Shim drift is unchecked.** No gate compares the folio shim's re-export list with `builders.ts` (`figure` is missing).
6. **Label prefixes.** `KNOWN_LABEL_PREFIXES` lacks `ssec`/`subsec`. Prefix-less prose labels mint JSON-LD ids, but unlabeled prose gets no `.jsonld` at all, and nothing reports that.
7. **Simulator HTML has no declared-directory convention** (it overlaps MIG S4).
