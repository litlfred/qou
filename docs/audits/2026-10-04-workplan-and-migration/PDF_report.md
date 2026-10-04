# PDF generation tooling → folio-assistant-sci: inventory and plan

Owner request (2026-10-04): move the PDF generation tooling to f-a-sci. This sits under qou bean `qou-feso` (S7) and platform beans `folio-assistant-jh2j` (TOOL 7/13, Task_Render) and `d308`. **This is read-only analysis. No math or physics content is touched.** Rows: `PDF_inventory.tsv` (50). [M] measured, [R] read.

## Findings

1. **The shared paper preamble now exists only inside qou's `main.tex`.** Commit `34a70659c7` (2026-09-24, bean `0uu2`) removed `cat-harness/latex/preamble.tex` because "qou has it as main.tex". [M] Since then the platform contains no paper preamble at all. qou does not contain one either, apart from the copy inlined into three generated files (`main.tex`, `qou-all-tables.tex`, `standalone-index-of-definitions.tex`). [M] The default `--preamble` of `generate-main-tex.ts` points to nothing. So do four steps in `publish.yml` (`../latex/preamble.tex`), the core `paper_render_pdf` tool and qou's `/build-pdf` command. [M] **Today nobody can regenerate qou's PDF.** That makes the styling port the real job, not an optional extra.
2. **The renderer and the preamble share an unwritten contract.** `render-latex.ts` and `generate-main-tex.ts` emit `\blockannot`, `\defterm`/`\refterm`, `\uses`, `\proofstatuslegend`, `\ifshowaffiliations` and the theorem environments in `ENV_NAMES` (including `algorithmblock`). [M] The only definition of these is qou's `main.tex`. They belong in sci together with the renderer. This is the strongest argument for sci owning a print template.
3. **Moving the files breaks layering in four places unless the order below is followed.** The layers run bootstrap → cat-harness → cat-harness-tools → core → sci (separation-arc ruling C1). [R] Measured edges [M]:
   - `folio-assistant-core/adapters/document/tools/render.ts:156` imports `generate-block-tex.ts` dynamically by path. Its `registerLatexRenderTools` is registered only by sci's `adapters/paper/index.ts:37`.
   - The document adapter's `audit.ts` and `qa.ts` spawn `latex-overfull-report`, `audit-tex-source`, `validate-tex` and `latex-preflight` by name.
   - `cat-harness/schemas/render-targets.ts` names `content/pipeline/render-latex.ts` as the built-in paper renderer.
   - `cat-harness-tools/adapters/mcp-server/server.ts` (×2) and `tools/validate.ts` spawn `build.ts`. Five Tool nodes in `cat-harness/tools/index.ts` also invoke `cat-harness/...` paths.
   Not affected: `render-value.ts` and `render-discovery.ts`. Generic code imports both, and they stay in cat-harness. sci importing them is the allowed direction.
4. **The mechanisms for these moves already exist.**
   - `pipeline-plugins.ts`: bean `squu` already moved `latex-preflight` into a slot that sci fills in `contributions.ts`. [M]
   - `ContributionRegistry.renderer(format)`: `render-discovery.ts:78` already looks it up before falling back to `RENDER_TARGETS`. [M]
   - The physical-move precedent is bean `y5si` / PR #1599 (`adapters/paper` → sci). It moved the files, rewrote specifiers, extended the `tsconfig` include, declared the directory in `folio-assistant-sci.json`, re-pointed `BUILTIN_ADAPTERS` and ran gates against origin/main. [R]
   `instance-rules.ts` already partitions the group to sci (exact rules plus the `latex|tex` keyword rule). [R]
5. **Two items in the TeX group belong elsewhere.**
   - `headless-render-qc.ts` checks the HTML viewer and is partitioned to **core**. [R]
   - `refresh-authors-note.ts` writes coverage numbers into qou's `authors-note.md` prose. It is not PDF tooling, and it must not run during the migration.
6. **qou-specific data has leaked into platform code.**
   - The `QOU_FAST_PREVIEW` environment variable in `generate-main-tex.ts`.
   - `split-pdf-by-chapter.py`, whose `--paper` defaults to `quantum-observable-universe`.
   - `publish.yml` hardcodes the qou paper path and `cd content` (qou is `folio/` now).
   - The docker image is named `qou-latex`.
   - `latex-known-macros.json` contains qou words (`\Bring`, `\Descartes`, `\Dirac`).
   - `render-tex/preamble.tex` declares `\ev \coev \Hom \Rep \Spec \Tr`, "keep in sync with main.tex". None of the six besides `\id` appears in qou's `.md` files. [M]
7. **Duplicates and drift.**
   - `paper_render_pdf/html` and `formula_render` are implemented twice: once in core's document adapter and once in `cat-harness-tools/.../tools/render.ts` (layer `sci`). [M]
   - There are three versions of the chapter splitter. The platform script takes `--pdf/--out-dir`, qou's takes positional arguments, and `publish.yml` passes `--input/--output-dir`. None of the three agree. [M]
   - qou `skills/local` forks five sci skills (`build-pdf` differs by 212 lines). [M]
8. **What sci already has:** the paper adapter, the preflight contribution, `authoring-a-paper.bpmn` Task_Render (`latex-authoring`), and the skills `build-pdf`, `latex-*` and `rendering-*`. It has **no** `.sty`, `.cls`, preamble or `tools/` declaration. [M] One conflict: the Task_Render documentation says *"The preamble, class and macros belong to the folio, never to the platform."* [R] Porting styling to sci contradicts that sentence. See decision D1.

## Styling port list (qou `main.tex` → sci print template)

Everything below is **copied verbatim, never edited**. Line references are to qou `main.tex`. [M]

| Port to sci (generic) | Stays qou (folio fragment, verbatim) |
|---|---|
| `\documentclass[11pt,a4paper]{report}` and the package list (l.13–42: amsmath/amssymb/amsthm/mathtools, geometry, graphicx, cite, ccicons, titlesec, tikz/tikz-cd, xcolor[dvipsnames], booktabs, array, enumitem with `\setlist`, mathrsfs, textcomp, newunicodechar, algorithm/algpseudocode, ulem[normalem], microtype, adjustbox, `\emergencystretch`, hyperref, xurl) | `\bigbowtie` |
| fvextra breaking verbatim (l.51–70) | `\varTheta` via `\providecommand`+`\renewcommand` (used in 130 .md files) |
| `\unimathsafe` and the 133 `\newunicodechar` entries; `\unitextsafe` and the 163 `\DeclareUnicodeCharacter` entries (U+00C0–017F) | `\pp` (p-adic prime; the manifest deliberately omits it) |
| geometry margins and marginnote (l.246–251) | `\yng` stub, `\unicode` stub |
| hyperref/pdfstring warning suppression (l.253–279) | the 8 manifest macros (`\nn`, `\frakr`, `\frakg`, `\frakb`, `\frakI`, `\frakK`, `\frakP`, `\ordw`), already folio-provided |
| titlesec chapter/section formats, `tocdepth` (l.280–317) | title, author, date and hypersetup metadata (generated) |
| `condensed`/`condenseddef` theorem styles and 12 `\newtheorem`, including `algorithmblock`; the `\qedsymbol` proof styling (l.318–373) | any unicode entry the owner rules is notation, e.g. `𝓑`→`\mathcal{B}` |
| LeanBlueprint macros: `\lean`, `\leanok`, `\notready`, `\mathlibok`, `\uses`, `\proves`, and the `\folio*base` links (l.374–400) | |
| Lean status palette, margin annotations (`\blockannot`, `\leanstatusmark`, `\sectionannot`, `\chapterannot`, `\tracker`, `\bcomment`) (l.401–569) | |
| `\defterm` / `\refterm` (l.570–597), `\proofstatuslegend` (l.598–620), `\ifshowaffiliations` (l.621–634) | |

## Story plan

**Platform PRs (folio-assistant).** These go one agent at a time, serialised with S5 `70lx`, because they touch the same imports.

- **P1. Recover the preamble as sci data.** Extract qou `main.tex` lines 1–828 into `folio-assistant-sci/latex/paper-preamble.tex`. Declare the directory in `folio-assistant-sci.json`. Remove the qou-only notation lines and the five rows above, and place them in the qou fragment produced by Q1.
  - *Done when:* `cat sci-preamble qou-fragment` reproduces lines 1–828 with only the moved lines reordered, and a line-set diff is empty.
- **P2. Invert the remaining edges without moving files.**
  - Contribute the latex renderer through `registry.renderer` and delete `RENDER_TARGETS.paper`.
  - Move `registerLatexRenderTools` and the four TeX tool entries in `audit.ts`/`qa.ts` into `folio-assistant-sci/adapters/paper/tools/`.
  - Reach `build.ts` through a contributed slot or tool instead of a path spawn.
  - Give sci its own `tools/` declaration holding the five TeX Tool nodes.
  - *Done when:* `check:import-direction` and `check:reference-direction` show no new edges, and the rendered `.tex` of a sample of 30 qou blocks (`renderBlock`) is byte-identical before and after.
- **P3. `git mv` the group** listed as sci in the TSV. Tests move with their subjects. Follow the y5si checklist: the tsconfig include, the specifiers, re-running `skill:register` and the coverage sidecar, and `bun run gates` compared with a clean origin/main worktree.
  - *Done when:* gates are green, `tool-coverage` is unchanged, and the sample-block `.tex` is byte-identical.
- **P4. De-qou the platform.**
  - Rename `QOU_FAST_PREVIEW` to a folio-neutral name and keep the old name as an alias.
  - Take the splitter's `--paper` from the manifest.
  - Split `latex-known-macros.json` into a generic part and a per-folio part.
  - Derive `render-tex/preamble.tex` from P1.
  - Fix the three-way splitter flag mismatch.
  - Pick one `paper_render_pdf` implementation.
  - *Done when:* grepping `cat-harness` and `folio-assistant-sci` code for `quantum-observable-universe` or `QOU_` finds no code hits.
- **P5. Repair `publish.yml`**: switch to `folio/` paths, read the paper from the manifest, use the sci preamble plus the folio fragment, and fix the splitter flags. It stays at the monorepo root until `litlfred/folio-assistant-sci` is live, because a reusable workflow must live in `.github/workflows` of the repository being called.
  - *Done when:* a dispatched qou `build.yml` produces `main.pdf` with no fatal `! ` errors.

**qou PRs.**

- **Q1. Notation fragment.** Copy the 5 preamble-only notation definitions verbatim into a qou-owned file, for example `folio/quantum-observable-universe/latex/notation.tex`, and have the manifest or build point at it.
  - *Done when:* the macro bodies are byte-identical to `main.tex` l.211–244, and the content parity baseline (`CONTENT_parity_baseline.tsv`) is unchanged.
- **Q2. Repoint the build.** Move `build.yml` to the repaired workflow and the pin, and remove the `/latex` symlink entry from `.gitignore`.
  - *Done when:* a PDF builds. Visual parity is checked against `papers/.../quantum-observable-universe.pdf` on pages sampled from 5 chapters, and the regenerated `main.tex` matches the committed one except for the comment and fragment order.
- **Q3. Reconcile the skill forks.** Fold qou-only lessons from `skills/local/{build-pdf,latex-*,rendering-*}` into the sci copies through a platform PR. Then remove the qou copies and `.claude/commands/build-pdf.md`.
  - *Done when:* the forks are no longer listed in qou routing, and their diff lines are accounted for in the sci PR.
- **Q4. Retire legacy outputs** into qou `fsh-guts/`: `scripts/split-pdf-by-chapter.py`, `qou-all-tables.tex`, `standalone-index-of-definitions.tex`, and `make-all-tables.py` unless D4 says to port it. This is done only after Q2 regenerates them, and with the owner's confirmation.
  - *Done when:* each retired file is reproducible by sci tooling or listed as not.

## Owner decisions

- **D1.** Does sci own a paper print template, against the Task_Render text "preamble belongs to the folio"? (Recommended: yes for generic styling and the renderer contract; notation stays with the folio.)
- **D2.** Which unicode-map entries count as notation and go qou-side?
- **D3.** Is the builder Docker image a folio asset (current `build.yml` comment) or sci's? There are two Dockerfiles today.
- **D4.** Port or retire `make-all-tables.py`, `qou-all-tables.tex`, `standalone-index-of-definitions.tex` and the tracked 7.9 MB PDF.
- **D5.** jh2j Finding 1 (exit-2 contract) and Finding 2 (a skill for compiling) are still open.
- **D6.** Where does `refresh-authors-note.ts` go: sci, or a qou script?
- **D7.** Which of the two `paper_render_pdf` implementations survives?

## Risks

- **Dependency direction.** Moving files before P2 creates core → sci edges: the dynamic import, the spawns by name, the `render-targets` string and the Tool nodes. P2 must land first. The move must also not take along `render-value.ts` or `render-discovery.ts`.
- **Math content.**
  - The notation macros and the unicode map decide how mathematics prints. One changed character silently changes the printed math, as the 2026-08-22 `\pic` incident did. Copy them byte-for-byte and verify by hash.
  - `render-tex-blocks.ts` writes `.ts` manifests and `refresh-authors-note.ts` writes prose. Neither may run against qou during the migration.
  - Do not delete `main.tex` before P1 has captured it, because it is the last copy of the preamble.
- **S5 collision:** `70lx`/`txue` also plans to move `render-latex`. Coordinate there.
