# MIG: migrate qou onto current folio-assistant, retire legacy QOU rendering

This epic changes formats and containers only. No math or physics content may be edited or deleted (owner hard rule). Legacy LaTeX/PDF is out of scope (owner ruling: `legacy-ignored`). Survivor epic bean: **`qou-n4r9`**, retitled. `qou-ty42` is absorbed into it.

## 1. Target: what folio-assistant requires of a folio (f-a main 0a45837f4, 2026-10-04)

- **Dependency chain, by declaration.** `folio-assistant-sci.json` needs `folio-assistant-core`. Core needs `cat-harness` and `cat-harness-tools`. `cat-harness` needs `bootstrap` and `bootstrap-tools` [M]. A sibling is resolved by name only inside one checkout (`dependenciesFromNeeds`, `cat-harness/schemas/harness-config.ts:813`). An external edge has to be **authored** in `<slug>.config.json` `dependencies[]` as `{name, git, ref}` ("a name gives no git URL and no version") [D]. So qou declares `needs: ["folio-assistant-sci"]` in `qou.json`, plus a git+ref dependency in `qou.config.json`. It must never use a monorepo path.
- **Paper adapter.** `PaperContentAdapter extends DocumentContentAdapter` lives at `folio-assistant-sci/adapters/paper/index.ts:43` [M]. `cat-harness/adapters/paper/` no longer exists [M].
- **Content-object triple.** Each block is `<root>.ts` + `.md` + `.lean` (+ `.qa.json`) (`cat-harness/docs/guides/agent-onboarding.md` §4). Block manifests import `../schema/builders`, and only the shim names the platform (`cat-harness/scripts/init-folio.ts:372-420`).
- **Layout** (`init-folio.ts:503`): `folio/<slug>/…`, `folio/schema/`, `library/`, `uploads/`, `beans/`, `todos/`, `<slug>.json` + `<slug>.config.json`, AGENTS/CLAUDE/GEMINI stubs, `.mcp.json`, README section markers (`skills/ui/ui-core/readme-sections.md`).
- **Workflows `folio_init` writes:** `cat-harness/templates/document/github/workflows/{qa-sweep,qa-sweep-nightly,section-title-audit}.yml` plus paper `{blueprint,lean-build,lean-build-sidecar,lean_ci}.yml`, and a `staging.yml` that calls the reusable `folio-staging.yml` [M].
- **QA results go to the `qa-reports` branch** (AGENTS.md). **f-a inconsistency:** the init-folio README template still says "Commit those files" for `test/results/block-qa/` (`init-folio.ts:527`).

### Worked example: litlfred/folio-test

- `claude/ojcx-edit-handbook` (2026-09-25) has a `staging.yml` that calls `litlfred/folio-assistant/.github/workflows/folio-staging.yml@main` with `build_command: … ../platform/cat-harness/scripts/build-document-site.ts`, `folio_dir: handbook/folio` and `platform_dir: platform`. The handbook carries `cold-chain.json` + `cold-chain.config.json` [M].
- `gh-pages` holds `STAGING/<branch>/{index.html,<slug>/index.html,review/,changeset.json,outline.json,block-qa.json,visual/*.png}` [M].
- `zmdo-proof` (2026-10-04) sparse-checks-out one layer plus its `needs` closure, with `persist-credentials:false` and plain-git submodules [M].

**Three findings:**

1. **The folio render is not just-the-docs.** Staging HTML is `build-document-site.ts` (remark-html, inline CSS, no KaTeX/MathJax) [M]. just-the-docs renders only f-a's own docs site and the FHIR IG sites. **There is no paper-folio site renderer**: no math typesetting, no Lean links, no theorem styling. This is a **folio-assistant gap**, not qou work. Every qou rendering story is blocked on it.
2. **The example itself is stale.** It points at `../platform/cat-harness/adapters/document`, `cat-harness/viewer` and `cat-harness/scripts/build-document-site.ts`. The last of these now lives at `folio-assistant-core/scripts/` [M].
3. **folio-test `main` (2026-08-29) lags further.** It has `.beans/`, `folio.config.json` and a submodule. This is a small f-a-side item, not qou work.

### Split / cutover state

- **Repo split (`zmdo`, in-progress)** [B]:
  - Proven standalone in empty repos for `cat-harness` and `folio-assistant-core` only.
  - **`folio-assistant-sci` is not proven standalone.**
  - The layer repos are not seeded. `seed:ready` reports 472 failing tests for cat-harness.
  - `litlfred/folio-assistant-sci` is an empty placeholder.
- **State-branch cutover (`9ofm`/`fs43`):** this is the f-a work plan moving off `main`. It is not yet cut over: one irreversible commit, waiting on the owner [B]. It does not block qou.

## 2. Current qou state (main 348e299cce)

| item | measurement | class |
|---|---|---|
| `qou.json` / `qou.config.json` | present. **No `needs`**, no `dependencies` [M] | migrate (S1) |
| `folio.config.json` | still present; #7484 deletes it | retire (S1) |
| `adapterModule` | `folio-assistant/cat-harness/adapters/paper/index.ts`, **absent at f-a main** [M] | migrate (S2) |
| platform link | gitignored symlink `folio-assistant/` (absent in this checkout), `.folio-assistant-pin` cb194b1. **87 tracked files** contain `folio-assistant/cat-harness` [M] | migrate (S2) |
| `folio/` | 4 folios plus `visualizer/`. QOU: **37 chapter dirs, 3,658 `.ts`, 3,635 `.md`, 3,855 `.lean` (2,953 under `lean/`), 3,596 `.qa.json`**. Groebner 37/33/52, fred2005 14/12/14, bach2013 11/9/0 [M] | keep-as-content |
| builder shim | `folio/schema/builders.ts` re-exports `../../folio-assistant/cat-harness/schemas/builders`. **10 blocks bypass the shim** (simulator blocks) [M] | migrate (S2) |
| `beans/` | `beans.json` + `defs/`, no `.beans/` [M] | done |
| README | 5 markers: toc, lean-coverage, lean-modules, simulators, workflows [M] | migrate (S3) |
| `.qa.json` in tree | 3,596+ committed | needs-owner (S3) |
| `docs/` | 3,082 `.md`, just-the-docs `remote_theme`. `docs-site.yml` builds an artifact only; gh-pages deprecated by owner 2026-09-27 [M][B] | renderer: retire. `.md`: keep-as-content |
| `.github/workflows/build.yml` | dispatch-only, calls f-a `publish.yml@cb194b1` (LaTeX/PDF to gh-pages) | legacy-ignored |
| `paper-builder-image.yml`, `main.tex`, `qou-all-tables.tex`, `standalone-index-of-definitions.tex`, `scripts/split-pdf-by-chapter.py`, `papers/*.pdf` (7.6 MB), `build-logs/` | LaTeX/PDF path | legacy-ignored |
| `deploy/` | Hetzner + Caddy + OAuth gateway serving the viewer and MCP server [M] | retire: needs-owner, since it is a live service |
| simulators | 10 blocks reference `fsh-guts/deprecated/simulators/*.html`. **3 targets missing**. `qou.config.json simulators.dir` points at absent `simulators/` [M] | gap (f-a: no simulator embed in the site renderer) |
| `folio/visualizer/` | companion folio (jsonld, lean, md) | keep-as-content |
| other workflows (10 QA gates), `migration/` (upstream proposals, owner 2026-09-26), `human-agent-discussions/`, `todos/` | — | keep |
| `fsh-guts/deprecated/` | ruby viewer, root-scratch, simulators, `doc-gen4.yml` | retire (already parked) |

**Content-preservation risk for the owner (do not drop):**

- `main.tex` (and the two other `.tex` copies of the same preamble) defines **47 macros**. Some are content-level notation: `\frakr`, `\frakg`, `\ordw`, `\bigbowtie`, `\pp`, `\yng`. Any web render needs them, or the prose silently changes.
- `qou-all-tables.tex` has **786 table environments**, but only **444 `table(` blocks** exist [M]. It may hold tables that exist only in `.tex`. A parity audit (S3) is needed before anyone treats it as generated.

## 3. Stories (ordered)

Every "done when" includes the **parity check P**:

- block, chapter and `.lean` counts are unchanged;
- the sha256 of every `.md` and `.lean`, and the canonical JSON of every manifest's statement fields, are byte-identical before and after;
- the Lean declaration set (`lake env` print of decl names) is unchanged;
- witness files are unchanged.

| # | story | size | blocked on | done when |
|---|---|---|---|---|
| S1 | **Declaration + config by dependency, not path.** `qou.json` gets `needs:["folio-assistant-sci"]`. `qou.config.json` gets `dependencies:[{name:"folio-assistant-sci", git, ref}]`, with the sha kept equal to the pin. Delete `folio.config.json` (#7484). Fix `feedbackDir`. | S | nothing (git URL = monorepo until sci is seeded; the swap is a one-line edit) | `check:instance-config` and `check:needs-dependencies` are green at the pinned f-a; no `folio.config.json`; P trivially holds |
| S2 | **Retire the symlink and monorepo paths.** `adapterModule` resolves through the declared dependency. The 10 direct imports go through the shim (import line only). The 87 files are re-pointed. Replace `setup-folio-assistant.sh` with dependency resolution. Pin bump to f-a main with before/after `run-validate` counts. | M | f-a S2-gap: a supported way for a downstream paper folio to resolve `adapterModule` and builders by dependency name. **Fully done only after the sci repo is seeded** (zmdo/seed:ready) | `git grep 'folio-assistant/(cat-harness\|folio-assistant-)'` returns 0 outside history comments; `run-validate` issue set is identical to the pre-bump set; P holds; the qou proof job (zmdo-style sparse closure) is green |
| S3 | **Folio conformance to folio_init.** Install the template workflows. Update README markers via `readme:sync:check`. Manifest the 3 root `.md` files (`qou-os3o`) without editing their text. Audit table parity between `qou-all-tables.tex` and the blocks, and *report* any table that exists only in `.tex`. QA sidecars: move to `qa-reports` or keep committed (**needs-owner**, given the f-a inconsistency). | M | owner ruling on QA location | `readme:sync:check` green; the table-parity report is delivered to the owner; P holds |
| S4 | **Simulator pages.** Decide the home of the 11 simulator HTML files: keep-as-content assets declared in `qou.json`, served beside the site. Rewrite only the `html:` path field. Report the 3 missing pages; do not invent them. | S | f-a gap: the site renderer embeds `simulator` blocks | each simulator block's target exists or is listed as missing-for-owner; P holds |
| S5 | **Retire legacy rendering.** Mark `docs-site.yml`, `deploy/` and `fsh-guts/deprecated/doc-gen4.yml` deprecated. Add `staging.yml` calling `folio-staging.yml@<pin>` with sci's paper site build. Fix the AGENTS.md gh-pages section (`qou-9olr`). Retiring `deploy/` (a live server) is **needs-owner**. | M | **f-a gap G1** (paper-folio site renderer: just-the-docs + math + Lean links + macros). S2 | the staging preview of a qou PR renders every block anchor (count = block count); the rendered-page diff is reviewed by the owner; no qou workflow writes to gh-pages except staging; P holds |
| S6 | **KG authority (`qou-j34j`).** JSON-LD becomes the authority and `.ts` is rendered. Sub-epic, after S5. | L | f-a support; owner scope | **needs-owner**: if any field cannot round-trip, stop and report; never edit content to fit |
| S7 *(home: folio-assistant-sci)* | **Salvage PDF styling.** Generic, move up: geometry, `titlesec` chapter/section formats, the `condensed`/`condenseddef` theorem styles plus 12 `\newtheorem`, the booktabs/longtable table style, microtype/fonts, and the Lean status marks (`\leanok`, `\mathlibok`, `\notready`, `\leanstatusmark`, `\blockannot`, `\proofstatuslegend`). qou-specific, stays with qou content: the notation macros (`\frakr`, `\frakg`, `\frakb`, `\frakI`, `\frakK`, `\frakP`, `\ordw`, `\bigbowtie`, `\pp`, `\yng`, `\nn`). There is no `.sty` or `.cls` [M]. Today f-a ships only a 15-line standalone `cat-harness/scripts/render-tex/preamble.tex` ("keep in sync with main.tex"), with no theorem styles [M]. | S | none | sci owns a paper preamble; qou's notation macros are declared in qou and consumed by both PDF and web |

The f-a beans that **must exist** (not qou):

- **G1:** a paper-folio site render (just-the-docs) that consumes the folio's notation macros and Lean links.
- **G2:** downstream resolution of `adapterModule` and builders by dependency.
- **G3:** a `simulator` block embed.
- **G4:** reconcile the init-folio "commit block-qa" text with `qa-reports`.
- **G5:** the folio-test reference branch is stale (the `cat-harness/adapters/document` and `build-document-site` paths), and its `main` predates the pipeline.
- **G6:** the sci layer standalone proof (zmdo covers core and cat-harness only).
- Already filed: `5xfr` (the pin bump must rename the config and add qaAxes), `2lzp` (`atomic-mass-gen-check.yml` is qou residue in f-a), and `hs08` (the `content/`→`folio/` readers).

**Can proceed now:** S1, S3 (except the QA-location ruling), S4 inventory, S7.

**Blocked on the split:** S2 completion (sci seeded), S5 (G1), S6.

## 4. Content-preservation guarantees

1. Every story is gated on P. Any diff in `.md`, `.lean`, statement fields, witnesses or the Lean declaration set fails the story.
2. Path rewrites are confined to import lines, `html:` paths and config. A changed line must match `^import|from "|html:|"path"|adapterModule`, and this is checked mechanically.
3. No `.tex` file and no `docs/*.md` is deleted. Retirement means workflow triggers are removed and a deprecation note is added. Files move only into `fsh-guts/deprecated/`, by an owner-confirmed `git mv`.
4. Anything not representable in the new schema (S6), tables that exist only in `.tex`, and missing simulator pages are **reported to the owner**, never rewritten.
5. The rendered-page diff (before and after staging) is reviewed by the owner before S5 closes.

## 5. Existing beans mapped

See `MIG_mapping.tsv` (27 rows):

- **Epic:** `qou-n4r9`.
- **Absorbed:** `qou-ty42` into `qou-n4r9`; `qou-4t05` is a duplicate of `qou-9olr`.
- **Close-evidence:** `qou-utbr`, `qou-w02s`, `qou-29i6`. `qou-yf1y`, `qou-sm2c` and `qou-qqia` close after #7484.
- **Scrap:** `qou-w3ju` (`simulators/` no longer exists).
- **Sub-epics:** `qou-p7z5` becomes S4; `qou-j34j` becomes S6.
- **Stalled claims:** `qou-7ko6`, `qou-yf1y` and `qou-utbr` have been in-progress with no activity since 2026-09-26/27. That is about 8 days, under the 14-day threshold.
- **Platform bean:** `qou-7ko6` is an f-a concern. Mirror it upstream.

## 6. Rendering-related open PRs (from `open_prs.txt`)

- **#7484:** deletes `folio.config.json` and repoints skills (S1). Merge first.
- **#7453:** imports the QOU blueprint from f-a (S5/G1-adjacent).
- **#7451:** removes a stray f-a home-page PDF from `uploads/`.
- **#7494** (draft): moves WHO uploads to `fsh-guts`.
- **#7483:** resolution options for the seven open blockers (audit doc).

## 7. Owner decisions

1. **QA sidecars:** keep them committed, or move them to `qa-reports`?
2. **`deploy/` live server:** retire it, or keep it until G1 ships?
3. **Notation macros:** what is their home: a qou `notation` declaration, or left in `main.tex`?
4. **S6 scope.**
