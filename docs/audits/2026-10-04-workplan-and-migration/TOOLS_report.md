# TOOLS: qou's executable artifacts mapped to folio-assistant node kinds

qou @ `afa49febf` (branch `claude/work-plan-reorg-2026-10-04`); f-a @ `origin/main 0b7b9e44e`. Read-only throughout. The 72-row inventory is in `TOOLS_inventory.tsv`. Provenance tags: [M] measured, [D] from a doc, [B] from a bean.

## 1. What there is [M]

| area | files | what it mostly is |
|---|---|---|
| `computations/` | 11,285 (4,500 non-deprecated `.py`, 3,509 non-deprecated `*.witness.json`) | producers, probes, audits, libraries, and the witnesses they write |
| `scripts/` | 230 (211 at top level) | Lean env/cache/audits (71), QA, beans, library, convention migrators, scratch |
| `tools/` | 349 | **code packages**: hecke-engine (Rust) plus 8 bindings, pyhecke(+native), qou-substrate |
| `qou-mass/` | 234 | a vendored PyPI library with 164 witness copies |
| `folio/pipeline/` | 30 `.ts` | QA audits (3 are forks of f-a modules) |
| `folio/visualizer/` | 16 | **content**: a companion paper manifest plus 3 blocks with `.lean` and `.qa.json` siblings. It is not a renderer |
| `fsh-guts/` | 109 | already-deprecated scratch, HTML simulators, one old workflow |
| `deploy/` | 22 | Hetzner/Caddy/auth-gateway |
| `.github/workflows/` | 14 | **all are `workflow_dispatch`-only** |
| `package.json` scripts | 1 | `build:docs` = typedoc |
| `pipeline/`, `simulations/`, `migration/`, `todos/`, `build-logs/` | 1 / 3 / 1 / 1 / 3 | see the TSV |

`qou.json` declares only `folio`, `library` and `computations` (as `code`). Its own comment notes that witnesses "have no graph kind on the platform yet" [M].

Heuristic classifier over non-deprecated `computations/*.py` [M]:
- 2,377 probes
- 1,157 producers whose witness no block cites
- 333 audits or validators
- 170 producers of a content-wired witness
- 163 libraries
- 263 other
- 37 test or init files

The most-imported libraries are `_path_bridge` (2,989 importers), `witness_base` (2,321), `_precision` (1,996) and `q_parameter` (1,703).

Content wiring [M]:
- Blocks declare 222 distinct `computation.script` paths. 213 of them exist.
- **8 scripts cited by 11 blocks do not exist**, for example `probe_per_wedderburn_block_ck.py` and `confinement_operator_selection.py`.
- Blocks declare 357 witness paths, and all 357 exist.
- `folio/values/registry.ts` has 68 entries over 17 witness files.
- Prose uses 12 distinct `:val[...]` and 9 distinct `{{ qou.computations.X }}`.
- In total, **356 of the 3,509 witnesses are wired** to content. That is about 10%.

## 2. What a witness is in folio-assistant terms

f-a uses the word "witness" for **three different things**:

1. **QA witness** (`qa-witness/v1`, `qa` kind, `test/results/witnesses/`): a QA verdict flattened for the docs panel. The `qa-reports` skill sends all *derived* QA output to the orphan `qa-reports` branch, keyed by commit.
2. **Lean witness** (`<file>.lean.<sha12>.witness`): a proof-check stamp. Its naming is core grammar (`content/pipeline/witness-address.ts`) and its lifecycle is sci tooling (`scripts/lean-witness.ts`).
3. **Computation witness**: the `ComputationWitness` / `Computation` interfaces in `cat-harness/schemas/types.ts`. `BlockBase.computation.witness` points at it, and `validate-value.ts`, `liquid-values.ts` and `witness-audit.ts` read it. **No graph kind exists for it, and there is no Zod schema.** The interface has drifted from what `WitnessBuilder` writes: `scriptHash` and `scriptFile` are written but not typed, a fact `witness-audit.ts` itself records [M].

**Classification.** A qou computation witness is **tool output that content reads**. It is *derived* in f-a's `holds` sense, the same as `substrate-snapshot`, because re-running the producer regenerates it. But it is also the evidence a block's claim rests on, and `:val` and Liquid read it at render time. Recommendation:
- Add a new sci-layer kind, `computation-witness`, with `holds: "derived"`, `renderable: false`, `perInstance`, and a Zod `computation-witness/v1`.
- The directory stays in qou under `computations/`.
- Witnesses stay on `main`. They do **not** go to `qa-reports`. That skill's own test ("reproducible → branch") points the other way, but moving them would break every `:val`, and a run of some producers costs hours. **This needs an owner ruling.**
- Real QA output from `computations/` *does* go to `qa-reports` by the existing owner ruling. That covers the 1,230 `script-qa/v1` sidecars (f-a bean `2634` thinks this family has zero instances) and the verdicts written by `computations/audits/`.

## 3. Bit-for-bit parity, measured

I copied `computations/`, `tools/qou-substrate` and `tools/pyhecke` into the scratchpad and re-ran one content-wired producer, `chi_sym_alt_closed_form.py` (it backs `prop:chi-sym-alt-closed-form`) [M]:
- It exits 0 and all 16 assertions are **equal**.
- The raw file differs in 35 lines.
- After stripping `_EPHEMERAL_META_FIELDS` (`commitSha`, `scriptCommitSha`, `computedAt`, `durationMs`, the `duration`/`elapsed` variants and `environment`), the `data` block still differs at about the 60th significant digit. For example, `chi_sym_direct …612092` against the committed `…612091`.
- qou's own `_witnesses_substantively_equal` reports **False**.
- The committed witness was produced with `pyhecke_native 0.9.0` and `clarabel`. Neither is in this container. Pinning mpmath 1.3.0 and sympy 1.14.0 did not close the gap, so the native MPFR path is the likely cause.

**What this means for done-when.** "Bit-for-bit" is only achievable as follows:
- **(a) Wrapping that does not run the producer:** the sha256 of every witness is unchanged. This is trivially true and is the main guarantee.
- **(b) Re-running:** the output must be byte-identical *after stripping the ephemeral fields*, **in the environment recorded in the witness's `environment` block**. That means installing `pyhecke-native` (`scripts/build-pyhecke-native.sh`) first. If that environment cannot be reproduced, the result is `unknown`, never pass.

The builder already refuses to downgrade the environment block, and it leaves the file untouched when the output is substantively equal [M]. That makes it a sound parity oracle once the environment matches.

## 4. Classification rules applied

- **A producer of a content-wired witness** becomes a **Tool node** in qou. It is declared with `defineTool` and invoked as a shell command, so no code is copied (the f-a precedent is `folio-assistant-core/tools/index.ts`). It uses `io.outputs` = the witness and `downstream {output: witness, inputs: [script, imported libs], judgedAt: "checkout"}`, which puts it under the `tool-downstream-fresh` criterion. It must stay qou-side. **Blocker:** qou's `tools/` is a *code* directory (Rust/Python packages), while f-a reserves `tools` as the Tool-node kind. The packages should be renamed (for example to `packages/`) as a container-only move before any Tool nodes are declared.
- **Probes and unwired producers (3,534)** are declared once as `code` plus `computation-witness`. Do **not** create one Tool per probe, because nothing consumes them.
- **QA gates:**
  - Domain gates stay in qou as Tools: precision/float64, LP duals, braid-word provenance, trace convention, witness substitution, convention C/D.
  - Generic gates go **upstream**:
    - Lean vacuity, axiom, orphan and sibling audits go to `folio-assistant-sci`.
    - Prose, library and `uses[]` audits go to `folio-assistant-core`.
    - Beans, QA-sidecar and SDLC hooks go to `cat-harness`.
- **Multi-step workflows become BPMN Processes:**
  - `run_pipeline.py` (staleness DAG plus topological rerun) becomes **witness-refresh**.
  - The witness-staleness, lp-dual, probe-float64 and word-provenance workflows become one **compute-QA** process.
  - The overnight `run-*.sh` drivers become **long-run regeneration**.
  - `gen-gluing-lean.py` becomes a **regenerate-and-diff** process. The exact pattern already exists as `folio-assistant-sci/processes/content/atomic-mass-drift-check.bpmn`.
- **Already upstream:**
  - `setup-elan-symlinks.sh` is byte-identical to f-a.
  - 7 more scripts share a basename with f-a but differ: `install-beans.sh`, `lean-build-bg.sh`, `setup-lean-toolchain.sh`, `session-start-coord-sweep.sh`, `lib/lean-env.sh`, `refresh-authors-note.ts`, `split-pdf-by-chapter.py`.
  - 3 `folio/pipeline` modules fork `cat-harness/content/pipeline/` (89, 67 and 198 diff lines).
  - `lake-cache-refresh.yml` has 113 diff lines against the f-a copy.
  - `kg-vocabulary-gate.yml` only runs f-a's `gen-block-jsonld.ts --check`.
  - `build.yml` already calls f-a's reusable `publish.yml`.
  - For all of these: reconcile the deltas, then retire the qou copy.
- **Renderer and deploy paths are retired:**
  - `deploy/`, by owner ruling: moved to fsh-guts, never deleted.
  - `paper-builder-image.yml`, `make-all-tables.py` and `split-pdf-by-chapter.py` (LaTeX, now out of scope).
  - `build-lean-mcp.yml`, in favour of f-a's Dockerfile.
  - `docs-site.yml`, in favour of `cat-harness/processes/sdlc/docs-site-publish.bpmn`.
  - typedoc `build:docs`.
  - None of these touch content.
- **Content and data that must not move or change:**
  - `q_parameter.py` and `qou_substrate/constants.py`, which are the single source of q₀.
  - `folio/visualizer/`, which is content.
  - The 84 `*.derivation.json` files, which are authored derivation DAGs carrying target values. One of them, `D-tau-M-q0`, has a `target_value` of 0.38829 while its description says "≈ 0.336821". This is flagged for the owner and was not edited.

**Actions billing.** All 14 qou workflows are `workflow_dispatch`-only by the owner's directive of 2026-06-30 [M][D]. f-a's copies of `witness-pipeline.yml` and `witness-refresh.yml` are also dispatch-only, and bean `folio-assistant-1l13` (keep, template or retire) is still open [M]. **The replacement is that the Process becomes the trigger rather than CI.** `workflow_start` / `workflow_next` drive the steps locally or agent-side, each step is a Tool with a `downstream` record, and instance state goes under `beans/workflows/`. A workflow YAML is then optional: one thin `workflow_dispatch` file per Process, with a `# bpmn-node:` back-reference so `check:workflow-coverage` can see it.

## 5. Needs-owner [M]

1. Whether computation witnesses stay on `main` as a new `computation-witness` kind (recommended) or go to `qa-reports`.
2. 8 producers that content cites but that do not exist, cited by 11 blocks.
3. `todos/qa-q-CAL-1-2-3-audit.json`. It plans to "mechanically update all expository literature", which would edit content.
4. The convention migrators and bulk regenerators (`convention-c-producer-migrate.py`, `regen-witnesses-mpmath141.py`, `regenerate-convention-c-witnesses.py`, `migrate_bare_producer_provenance.py`). They rewrite producers or witnesses, so they must never run as part of the migration.
5. `simulations/q_dynamics_engine.py`, which hardcodes `Q0_VACUUM = 1.1097` outside `q_parameter.py`.
6. The new home for the code packages in `tools/`, which have to move off the name f-a reserves for Tool nodes.
7. `qou-mass`: 12 of its 164 vendored witnesses differ from source. The fix is `sync-qou-mass-vendor.py`, which is a regeneration, so it needs the owner.
8. The 24 `computations/*.md` audit docs (classify-only by owner ruling).

## 6. Proposed stories (epic `qou-n4r9`, or a sibling epic named "qou executables → nodes")

**Global parity invariant.** Unless a story says it re-runs producers: `git ls-files -s 'computations/**' 'folio/**' '*.lean' | sha256sum` is identical before and after, and `git diff --stat -- '*.witness.json' '*.lean' 'folio/**/*.md'` is empty.

| # | title | done-when (incl. parity) | size | depends-on |
|---|---|---|---|---|
| T1 | f-a: `computation-witness` graph kind + Zod `computation-witness/v1` (sci) | kind registered with `holds: derived`; Zod parses **all 3,509 qou witnesses** (or lists the failures as a finding, without "fixing" them); `ComputationWitness` reconciled with `scriptHash`/`scriptFile`; `check:kind-validators` green | M | — |
| T2 | qou: declare `computations/` witnesses and `fsh-guts/` in `qou.json` | both declared; global invariant holds; `kg:validate` reports per-file results | S | T1 |
| T3 | Rename qou `tools/` → `packages/` (container only) | git sees pure renames (0 insertions, 0 deletions); every importer resolves (`build-pyhecke-native.sh`, the `_path_bridge` search); witnesses unchanged | M | owner (§5.6) |
| T4 | Parity harness: `witness-parity` Tool | Given a producer, it records the env from the witness, re-runs it in a scratch copy, compares with `_EPHEMERAL_META_FIELDS` stripped, and reports pass/fail/**unknown** (unknown when the env cannot be matched). Calibration: with `pyhecke_native` installed, `chi_sym_alt_closed_form.py` reproduces its committed witness, and without it the result is unknown. qou tree untouched | M | — |
| T5 | Wrap the 170 content-wired producers as Tool nodes (`downstream` = witness) | one Tool per producer, generated from the block manifests rather than hand-listed; global invariant holds; T4 run on a sample of ≥10 cheap producers, each pass or unknown, **zero fail** | L | T1, T3, T4 |
| T6 | `witness-refresh` BPMN process over `run_pipeline.py` (+ the overnight drivers) | process loads in `workflow_list`; a dry run lists stale producers identical to `run_pipeline.py --dry-run`; no witness rewritten; f-a bean `1l13` answered | M | T5 |
| T7 | `compute-QA` process (precision-gates, staleness-gates, lp-dual, float64, word-provenance, witness-staleness audits as Tools) | each workflow YAML reduced to a dispatch of the process with a `# bpmn-node:` back-reference; gate verdicts identical on `main` before and after; verdict files written to `qa-reports`, not committed | M | T5 |
| T8 | `script-qa/v1` → qa nodeSchema; publish the 1,230 sidecars via `qa-store.ts` | `qa:verify-moved` IDENTICAL; f-a bean `2634`'s "family dead?" answered with the count | M | — |
| T9 | Regenerate-and-diff process for the Lean content producers `gen-gluing-lean.py` and `gen-hecke-corner-column.py` | regenerated `GeneratedGluing.lean` is byte-identical to the committed file; process modelled on `atomic-mass-drift-check.bpmn` | S | — |
| T10 | Upstream generic Lean audits to `folio-assistant-sci` (`folio/pipeline` Lean audits; `scripts/lean-*` vacuity/axiom/orphan; lean-axiom-guard; lean-content-siblings) | each one exists in sci, takes the root as a parameter, and reproduces qou's current output on qou (same finding set); the qou copy is retired only after that | L | — |
| T11 | Reconcile and retire 8 forked scripts, 3 forked pipeline modules and `lake-cache-refresh.yml` | each qou-only delta is either upstreamed or recorded as qou-specific; afterwards qou calls the f-a path | M | — |
| T12 | Upstream library/bib/uses tooling to `folio-assistant-core`, and beans/QA/SDLC hooks to `cat-harness` | same output-parity rule as T10 | L | — |
| T13 | Retire renderers and deploy into `fsh-guts/` (`deploy/`, `paper-builder-image`, `build-lean-mcp`, `docs-site.yml`, typedoc, `make-all-tables`, `split-pdf`) and move `computations/_deprecated` → `fsh-guts/` | pure renames; `convention-c-deprecated-citation-audit.py` shows 0 content citations into `_deprecated` before the move | S | owner ack on `_deprecated` |
| T14 | `qou-mass` vendor drift → a declared Tool with `maintains`, plus a drift gate | the gate reports 12/164 today without regenerating anything | S | owner (§5.7) |

## 7. Skill gaps in folio-assistant

1. **There is no `computation-witness` skill or graph kind.** `compute-author`, `compute-audit` and `witnessed-values` (sci) say how to *write* compute, not what a witness *is* as a node, where it lives, or why it is exempt from `qa-reports`.
2. **No parity / reproducibility skill.** Nothing defines the volatile-field set, the environment matching, or the third state "env not reproducible = unknown". qou's `_EPHEMERAL_META_FIELDS` is the de-facto spec.
3. **No skill for wrapping a producer as a Tool.** It would cover how `downstream` applies to a witness, when *not* to create a Tool (probes), and generating Tool nodes from `computation.script`.
4. **Dispatch-only CI.** No skill describes a Process as the trigger when Actions are switched off (the billing case).
