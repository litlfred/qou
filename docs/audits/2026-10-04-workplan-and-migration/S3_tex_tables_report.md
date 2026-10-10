# S3 — `.tex` tables vs table blocks (bean `qou-4rhu`)

Read-only audit, measured 2026-10-05 on `main` at `e780e63569`. Per-table rows:
[`S3_tex_tables.tsv`](S3_tex_tables.tsv) (787 rows + header).

## Bottom line

**No hand-written `.tex` file in this repository holds a content table.** All 786
`tabular` environments behind the "786" figure are in one file,
`qou-all-tables.tex`. That file is a **generated layout-test harness**: its own
body text says *"Every `tabular` extracted from the rendered chapters … Regenerate
with `scripts/make-all-tables.py`"*. It is a snapshot of pipeline output, not a
source.

Matched back to the current corpus:

- **784 of 786** are matched to a current source block.
- **1** has **no source anywhere in the current tree** (`[appendix-surreals] #12`,
  listed below). This is the only table where the harness is the last copy.
- **1** is the Lean-status legend in the copied preamble. It is not content, and
  its source is the platform preamble.

Retiring `.tex` therefore risks **one** table, not 342.

## What was counted, and how

### 1. Tracked `.tex` files

`git ls-files '*.tex'`, excluding `node_modules`, `.lake/` and the `folio-assistant`
symlink (which points to `../fa-test`), gives **4 files**:

| file | `table` | `tabular` | `longtable` | `tabularx` | `array` | what it is |
|---|---:|---:|---:|---:|---:|---|
| `qou-all-tables.tex` | 0 | **786** | 0 | 0 | 0 | generated harness (`scripts/make-all-tables.py`): main.tex's preamble plus every rendered `tabular`. 785 are in the body and **1 is the preamble's Lean-status legend** (line 609, before `\begin{document}` at line 632) |
| `main.tex` | 0 | 1 | 0 | 0 | 0 | pipeline-generated main file (`build.ts --generate-main`). Its one `tabular` is the Lean-status legend from the platform `paper-preamble.tex` |
| `standalone-index-of-definitions.tex` | 0 | 1 | 0 | 0 | 0 | generated standalone build. It matches `.gitignore:62 standalone-*.tex` but is tracked anyway. Holds the same legend |
| `folio/quantum-observable-universe/latex/notation-preamble.tex` | 0 | 0 | 0 | 0 | 0 | notation macros only |

No `.tex` file is tracked under `docs/` or `library/`, and none is tracked in a
chapter directory under `folio/`. **`array` occurs 0 times** in tracked `.tex`.

The rendered chapters, `chapters/*.tex` (36 files), are **gitignored**
(`.gitignore:16 chapters/*.tex`). They exist locally from a render at
2026-10-04 18:49 and hold 683 `tabular`, 445 `table` and 2 `array`. They are listed
for context only and are not in the TSV. The `table` count, 445, is close to the 444
table blocks, which suggests the renderer wraps each table block in a `table`
float. That reading was not verified.

### 2. Table blocks

There are **444** `.ts` manifests whose default export is the `table(...)` builder,
under `folio/` (excluding `schema/`, `pipeline/` and `node_modules/`). This
**confirms the "444"**. A bare grep for `table(` finds 450 files, but the other 6
are TypeScript declaration files under `folio/node_modules`. Every one of the 444
has a `.md` sibling. No manifest uses `kind: "table"` without the builder.

### 3. Why 786 is not "444 plus 342 orphans"

The two figures count different things, so their difference is not a list of
missing tables:

- **786** counts every rendered `tabular`. A markdown pipe table inside **any**
  block kind renders to a `tabular`. One table block can also render more than one
  (for example, `hecke-log-decomposition-table-data.md` has two). And 1 of the 786
  is the preamble legend.
- **444** counts table-kind blocks only.

Here is the source-block kind for the 784 matched tables:

| source block kind | tabulars |
|---|---:|
| table | 440 |
| remark | 167 |
| proof | 54 |
| proposition | 37 |
| conjecture | 34 |
| prose | 23 |
| definition | 18 |
| example | 6 |
| algorithm | 3 |
| theorem | 2 |

These come from **599 distinct source files**. So about **344 tabulars are tables
embedded in non-table blocks**. They are content held in `.md` files, not content
held only in `.tex`.

Going the other way, **430 of the 444** table blocks appear in the harness. The
other **14** table blocks are newer than the harness snapshot, or were edited past
recognition. They are safe either way, because they are blocks.

### 4. Matching method

Each harness table carries its chapter tag (`[chapter] #n`). Each table was matched
against all **1,079** tables parsed from `folio/**/*.md`: pipe tables, including
those inside blockquotes, plus fenced `\begin{tabular}`. The script tried these
methods in order and took the first that matched:

| method | tables |
|---|---:|
| exact header-cell match, after removing `\refterm`/`:refterm`, `**`, `$`, braces and whitespace; same chapter preferred, ties broken by body overlap | 609 |
| first-column row keys (≥80–90 % of row labels found in one table in the same chapter) | 135 |
| body-token containment ≥ 0.85 | 30 |
| header-token Jaccard = 1 | 2 |
| hand-verified (the 9 left undetermined by the script; 8 resolved, see below) | 8 |
| **undetermined after hand check** | **1** |
| preamble legend (not content) | 3 rows: 1 in the harness preamble, plus `main.tex` and `standalone-index-of-definitions.tex` |

The 135 row-key matches include **119 per-element isotope tables** in
`appendix-knot-periodic-table`. Their source block,
`recursive-atom-knot-atlas-registry.md`, now has different columns: `Binding B_q …
Mass Error (ppb) … CAL-3 Bound` replaced `Prediction (MeV) | Reference (MeV) |
Error`. So the harness holds an **older version** of tables that still exist. The
rows (`³H` = 2809.4453, and so on) were checked by hand for one table. The others
match by row labels only.

The 8 hand-resolved tables are all in the same situation: the source still exists
and was edited after the harness snapshot.

- `particle-interactions #14, #15` → `nuclear-interactions/q-beta-spectral-bridge-table-data.md`
  and `q-beta-form-a-n1-symbolic-table-data.md`. Re-pinned q₀ and moved to convention D.
- `mass-theory #44` → `markov-trace-frobenius-selection.md`, and `#46` →
  `bring-residue-resolvent-context.md`. Columns changed.
- `information-theory #11, #12` → `toffoli-lp-stability-table2-data.md` and
  `-table1-data.md`. Rewritten after Φ was retired. The old rows are kept and
  marked "retired frame".
- `appendix-knot-periodic-table #26` → the neutron row of the registry
  (`939.5654`). This is a one-row table, so the row-key rule could not fire.
- `climax-volume-mass #3` ("Block | Current structure | Simplification") →
  **no longer a table**. The same three rows survive as prose in an `authorNotes`
  entry of `climax-volume-mass/skein-bar-antisymmetry-proof.ts`, marked *"working
  channel, not for publication"*. The content is kept, but is no longer published.

## Tables that exist ONLY in `.tex`

| tex_path:line | harness tag | header | status |
|---|---|---|---|
| `qou-all-tables.tex:15472` | `[appendix-surreals] #12` | Round & Commit & Key contribution | **No current source.** It is an 11-row development-history table (rounds 1–11, commits `12202fb0` … `710039e7`, "(this)"). Neither the header nor any commit hash appears in any `folio/**/*.md` or `.ts` file, and it is absent from the current render (`chapters/*.tex`). Git confirms the hash `12202fb0` occurs only in `qou-all-tables.tex` (`git grep -lF 12202fb0 HEAD`). The block that once carried it was not identified (see *Not established* below). |

**Hand-written `.tex` tables that are only in `.tex`: 0.**

## Not established

- **Where the one orphan table came from.** A `git log -S'12202fb0'` restricted to
  the `appendix-surreals` paths, in both the old `content/` tree and the new
  `folio/` tree, did not finish within the session's time limit. Its neighbours in
  the harness are `b1-current-status-table2-data` (#11) and
  `calculus-up-to-epsilon-table-data` (#13), so it probably came from a
  `b1-current-status*` block. That is an inference, not a measurement.
- **Exact row-for-row agreement.** A match means the source was found. It does not
  mean the harness copy is identical to it. About 140 tables match only by row
  keys, by drifted body, or by hand, and in those cases the source has been edited
  since the harness was made. The harness is a **stale snapshot**: the file's last
  commit is `b7accffcbc` (2026-09-27), a prose sweep rather than a regeneration.
- The row-key and body-overlap rules can in principle pick the wrong block when two
  blocks share row labels. Spot checks found no such case. One wrong attribution
  that body-overlap produced (a match to `definition-index.md`) was fixed by
  ranking exact header-cell matches first.

## Recommendation (judgement, not a finding)

1. **Treat `qou-all-tables.tex` as a derived artefact, not a content store.**
   Retiring it, or retiring `.tex` in general, loses no hand-authored table. Do
   **not** count its 786 tabulars as content to migrate.
2. **Before it is removed or regenerated, decide on the one orphan table**
   (`[appendix-surreals] #12`). It is a history-of-rounds table with commit hashes,
   which is the kind of status leak that one-voice rules move into `authorNotes`.
   It was likely removed on purpose. But the corpus does not show that, and this
   file is the last copy. Two options. (a) Leave it: the content stays recoverable
   from git history at `b7accffcbc:qou-all-tables.tex`. (b) Restore it as an
   `authorNotes` entry on the `b1-current-status` block once the source block is
   confirmed. Either is cheap. If nobody chooses, nothing changes.
3. **If the harness is regenerated**, its counts will move (the current render has
   683 `tabular`, not 785). The S3 "786" figure should then be retired rather than
   updated, because it never measured content at risk.
