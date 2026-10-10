# LEANNODES: qou Lean as folio-assistant nodes (2026-10-04)

**Scope.** Static, read-only analysis of qou `main` @ `348e299cc` and folio-assistant `origin/main`:
- `.lean` sources were extracted with `git archive` and parsed.
- No `lake build` was run. No edits were made.
- Scripts: `scratchpad/ln/{an,an2,inv}.py`.
- Inventory: `out2/LEANNODES_inventory.tsv`, 4,197 rows. It covers every `.lean` file, the lakefiles, the workflows, 121 tools and skills, and 73 unresolved refs.

## Measured facts [M]

**Where the `.lean` files are.** 3,992 in total:
- 2,985 are library modules (QOU 2,953, UGB 30, Fred2005 2).
- 938 are chapter-directory siblings (QOU 902, UGB 22, Fred2005 12, visualizer 2).
- 69 are elsewhere (`docs/audits` 30, `tools/hecke-engine` 22, others 17).

**Library build coverage.**
- QOU and UGB use whole-tree globs.
- **Fred2005 has no `globs`.** Only its root import closure is built. That is complete today only because the library has 2 modules.
- `scratch_lean.lean` and UGB `test.lean` are in no build target.
- `QOU.scratch_matrix` is inside the glob.

**Which library modules reach a block.** I counted a module as reachable if a block's `lean.ref` names it or a sibling imports it, then followed imports.
- **863 of 2,985 are reachable**: 525 referenced directly, 338 supporting.
- **2,122 are not**: 1,375 are imported only by other non-reachable modules, and 743 are leaves.
- `QOU.Mathlib` (212 modules) has 0 direct references and `QOU.MathlibExt` (182) has 2. Both are infrastructure.

**`lean.ref` resolution (1,309 refs).**
- 654 resolve into a built library module.
- 582 resolve only to the block's **own uncompiled sibling**. In 16 of these, other siblings also declare the same name.
- 41 match only by short name (namespace drift).
- 20 name a module rather than a declaration.
- 12 resolve to nothing.

**The 938 siblings.**
- 929 file stems and 896 chapter directories are kebab-case, so they are not valid Lean identifiers.
- 878 declare under `QOU.*`. 265 import the library, 43 declare nothing (pointer stubs), and 13 have no `.ts`.
- **No sibling imports another sibling.**
- 195 siblings share a fully qualified name with another sibling. 206 re-declare names that also exist in the library.
- **0 siblings re-declare a name from their own import closure**, so each one can compile standalone.
- Lexically: 8 `sorry` in 3 files, and 88 `axiom` declarations in 45 files.

**`docs/audits/*.lean` (30 files).**
- 4 are refutations (`skein-mass-relation-is-false`, `double-magic-conjecture-is-false`, `parallelogram-axioms-inconsistent`, `qns-carriers-are-refutable`). 14 are vacuity or triviality probes, and 12 are other probes.
- None contains a `sorry` or an `axiom`.
- 7 have candidate blocks found through imports or declaration tokens, and 2 mention a block label.

**Stale paths.** 20 of the 121 Lean tools still reference `content/…`, which holds 0 files on main. One example: `lean-content-sweep.sh` finds no targets and exits 2.

**Earlier findings I am relying on.**
- [B] `qou-lsib`: a lean-direct sweep of 958 siblings found **73 failures, 69 of them real defects**. Expect red the first time the siblings are built.
- [D] The f-a reseed guide says the qou cache holds **7,268 oleans, 0 traces and 0 own-package oleans**. Bean `qou-wumn` is still todo.

## 1. Target layout

**What f-a says.**
- **`lean-generation`** asks for one Lake package per paper at `<folio>/<paper>/lean/`, with a `<Lib>/` tree, registered in `lean-packages.ts` as `{name, paperDir, lakeRoot, lib}`. Its §"CRITICAL" says a `.lean` file is never standalone. `no-orphan-lean` (in `content-validation`) enforces that for **chapter-directory files**.
- **The library tree may have no blocks.** Four things allow it:
  - `lean-formal-ref.ts` resolves to the library tree as its second candidate;
  - `lean-mathlibext-curator` treats `<Paper>/MathlibExt` as a staging area;
  - `q-usage-audit` "orphan library-tree coverage" audits unreferenced library files and does not reject them;
  - `listPackageLeanFiles` lists them.
- **Nothing in f-a compiles a sibling.**
  - The paper templates (`lean-build.yml`, `lean-build-sidecar.yml`, `lean_ci.yml`) discover `<folio>/*/lean/` and build the package only.
  - `proof-lean-compiles` reads per-file LSP diagnostics instead.
  - No graph kind covers a Lean library.
  - folio-test has no Lean at all.

**Proposed layout.** Container-only: no `.lean` file changes by a single byte.

1. **The library tree becomes a new `formal-library` node kind (gap G-L2), not content.**
   - Declare `folio/<paper>/lean/` in `qou.json`. The kind holds `content`, is rendered by doc-gen4, and is validated by `lake build`, like the `code` kind.
   - All 2,985 modules are declared in place.
   - An unreferenced module is a reported finding, never something to delete.
   - Mathlib, MathlibExt, Machinery, Common and Infra are infrastructure; Hecke and SchurWeyl are mostly infrastructure too (SchurWeyl: 1 direct ref; Hecke: 3).
2. **Siblings stay where they are, as triple members, and are compiled by a second library in the same paper package.** This keeps f-a's one package per paper and its discovery job intact.
   ```toml
   [[lean_lib]]
   name = "QOUBlocks"
   srcDir = ".."                         # folio/quantum-observable-universe/
   globs = ["braids-and-knots.+", …]     # one per chapter, GENERATED from the paper manifest
   ```
   - Use one glob per chapter, not a bare `..` glob. A bare glob would pull in `lean/` a second time as `lean.QOU.*`.
   - A check should fail if the generated globs drift from the manifest's `chapters`.
   - Add `UGBBlocks` and `Fred2005Blocks` the same way, and give Fred2005 `globs = ["Fred2005","Fred2005.+"]`.
   - **Do not add an aggregator root module.** With 195 siblings sharing names, importing them all fails with "already declared". doc-gen4, Atlas and the formal-edges extractor must load siblings one module at a time (G-L6).
3. **Add a root `[[lean_lib]] QOUAudits`** with `srcDir = "docs/audits"`. This compiles the refutations where they sit. They can move by rename later, per the owner's ruling.
4. **Result.** 1,236 of 1,309 refs (654 + 582) resolve into a CI-built target; the other 73 are handled in §2d. A new paper-adapter rule `lean-ref-built` (G-L1) enforces this. It needs `LeanPackage.libs[]` next to `lib`.

**Risks.** One cheap probe settles both. Neither justifies editing content.
- **R1:** Lake v4.24 may not accept kebab-case globs and module names. No evidence either way.
- **R2:** `srcDir` may not be allowed to point outside the package.
- **Fallback:** a generated, build-time shadow tree of symlinks to identifier-safe module paths. `lean.ref` is unaffected, because declaration names come from in-file namespaces and no sibling is imported by module name.
- **Renaming the source files is rejected.** It breaks the matching stems that `no-orphan-lean` relies on.

## 2. Migration plan

**a. Baseline (L0).** Take the static census (§3) before any change.

**b. Lakefile-only edits (L2).** Add the Blocks libraries, `QOUAudits` and the Fred2005 globs. Library traces do not change, so a warm cache stays valid and only the new modules compile.

**c. Siblings that fail to compile (L3).**
- Lake keeps building independent jobs after a failure. `lean-build-sidecar.py` writes per-module status to `lean-build-status.json`.
- The first run's red set is committed as a **known-red baseline**.
- The gate: no new red module, and no module silently turning green. This follows the `lean-axiom-guard` pattern.
- Red modules get a `proof-lean-compiles: fail` verdict on their blocks. Fixing them is content work in separate beans and is never part of the migration.

**d. The 73 refs (L4).** `lean.ref` is manifest metadata, outside the statement fields covered by MIG check P. But it is a **claim of formal backing**, so I recommend edits only under an owner ruling, with evidence per row:
- **41 short-name matches:** repoint only when there is a unique candidate and a `proof-narrative-lean-equivalence` verdict.
- **20 module refs:** this is the `qou-cu0a` aggregator trap. Repoint only if the module has exactly one claim-shaped declaration and an equivalence verdict.
- **12 that resolve to nothing:** never invent a target. Keep the ref and record it as dangling.

**e. `docs/audits` (L5).**
- Compile the files in `QOUAudits`.
- Add evidence links as metadata (`docs/audits/lean-evidence.json`: file → refuted declaration → blocks), plus block-QA attestations that cite `{kind:"file"}`.
- The refutations target library classes such as `QOU.HadronicMass.SkeinMassRelationHolds`. Join them to blocks through `lean-formal-edges`, not lexically. Only 7 of 30 have lexical candidates.

**f. Orphans and scratch (L6).** 19 needs-owner rows:
- 13 siblings with no `.ts`: write a block manifest, or move them to `fsh-guts` by rename.
- 4 scratch files.
- 2 visualizer stubs (that paper has no Lake package).

**g. Branch-only Lean (L8).** Twelve modules on seven branches. Salvage them as add-only PRs into a glob, with owner sign-off per branch.

## 3. Verification and budget

**P-Lean**, the parity check every story must pass:
1. **Byte parity:** the sha256 of all 3,992 `.lean` files is unchanged. For the container-only steps this is sufficient.
2. **Static declaration census:** the multiset of fully qualified names per file is unchanged. Baseline: library 45,889, siblings 6,031 (heuristic parser).
3. **Lexical `sorry`/`axiom` counts per file are unchanged.** Baseline: library 1/24, siblings 8/88.
4. **Elaborated census:** a meta-program dumps the constants per module with a type hash and `collectAxioms` (G-L5).
   - The library census must be identical before and after.
   - **Siblings and audit files have never been Lake-built, so they have no "before".** Parity for them is checks 1–3. The first build *establishes* their baseline (known-red list, axioms, `sorryAx`). It reveals existing defects; it introduces none.

**Budget.**
- The owner's billing directive keeps this dispatch-only.
- Mathlib is minutes via `cache get` [D].
- The qou package cache has no own-package oleans [D], so the first run builds all 2,951 QOU modules (a 4,346-job full build per `qou-rc7b` [B]), plus 938 siblings and 30 audit files.
- **Estimate [E]:** one owner-dispatched run, sharded by chapter so each job stays under the 6-hour limit, then `lake-cache.sh contribute` with traces.
- After that, builds cover changed chapters only and take minutes.
- **Precondition:** `qou-wumn`, `qou-z9bx` and `qou-lb0f` must be fixed first. Otherwise every run pays the full cold-build cost.

## 4. Tools and skills (121 files [M])

**111 move to folio-assistant-sci:**
- **13 already have an f-a counterpart**: the cache-restore, stage-push, reseed and toolchain scripts, `lib/lean-env.sh`, `lean-build-bg.sh`, and the capability and actor nodes. Bean `9io2` already makes sci the owner of lake-cache.
- **14 skill forks, manifests and the requirement node.** Diff-merge them into `folio-paper-adapter/`, then pin.
- **`lean-axiom-guard.py`** (362 QOU tokens) splits: the engine goes to sci, the registry stays in qou as data.
- **83 generic QA and build tools**, configured through `lean-packages`:
  - the sweeps;
  - `lean_decl_scan`;
  - `lean-orphan-audit.ts`, which f-a's `prepare-merge` already cites;
  - `lean-vacuity-axiom-audit.ts`, which f-a's `lean-proof-vacuity-audit` documents but does not ship;
  - the vacuity, self-assuming and staleness families.
  - The shadow-tree tools exist only because the cache has no traces; re-check need after L3.

**10 stay in qou, declared in place.** These are specific to the qou substrate or to this paper:
- `lean-q-substitution`, `lean-substrate-numerics`;
- `gen-gluing-lean.py`, the Markov-convention, Hecke-consumer and tranche-scope tools, `build-meromorphic-cone.sh`, `lean-qa-progress-table.py`;
- `mathlib-modules.txt`;
- the `lean-verifier` agent and its memory.

**All 5 workflows go to the sci paper templates.** `lean-content-siblings.yml` is superseded once siblings are a Lake target.

## Proposed stories

These go under `qou-n4r9`, or a new sibling epic "Lean as nodes". Every story's done-when includes P-Lean (§3).

| id | title | done when | size | depends |
|---|---|---|---|---|
| L0 | Lean parity baseline | Static census witness on `qa-reports`; a re-run is byte-identical | S | – |
| L1 | Probe R1/R2 | One dispatch builds one chapter's glob; result recorded; fallback chosen if Lake rejects | S | L0, owner dispatch |
| L2 | Blocks libraries, `QOUAudits`, Fred2005 globs | Only lakefiles change; a check confirms the generated globs equal the manifest; P-Lean 1–3 | M | L1 |
| L3 | First full build and known-red baseline | Sharded run; status JSON, known-red list and elaborated census recorded; cache contributed with traces; library census unchanged | L | L2, `qou-wumn`/`z9bx`/`lb0f` |
| L4 | `lean.ref` ledger | 73 rows with candidate and verdict; only owner-approved edits applied; statement fields byte-identical | S | owner, L3 |
| L5 | Audit evidence links | All 30 files linked; attestations recorded; 4 refutations adjudicated via formal edges | M | L3 |
| L6 | Orphan and scratch dispositions | 19 owner rulings applied by rename or metadata only | S | owner |
| L7 | Upstream tools and skills | 111 rows done; stale `content/` paths fixed in the copies; qou callers pinned | L | G-L1..G-L6 |
| L8 | Branch-only Lean salvage | Add-only PRs; P-Lean holds; owner sign-off per branch | M | L2 |

## Skill gaps for folio-assistant (folio-assistant-sci unless noted)

- **G-L1 `lean-ref-built` rule.** Every `lean.ref` must land in a CI-built target, with `LeanPackage.libs[]`. "Unknown" is never reported as green.
- **G-L2 `formal-library` graph kind.** Lets a library tree exist without blocks. Also states that `no-orphan-lean` covers chapter directories only.
- **G-L3 Sibling compile convention.** A `<Lib>Blocks` library in `lean-generation`, the `folio_init` template and the discovery job.
- **G-L4 Formal-evidence citation or attestation pattern.** Also fix the dangling references to `lean-vacuity-axiom-audit.ts` and `lean-orphan-audit.ts`.
- **G-L5 `lean-decl-census` tool.** Shared with the `xqdi` merge gate.
- **G-L6 Duplicate-name awareness.** Resolve to the block's own sibling first; never co-import siblings during extraction.
- **G-L7 (sci/cat-harness) Lake cache with own-package oleans and traces.**

**Caveats.** Heuristic parser (no `mutual`/`open … in`); lexical reachability; build times are estimates; audit-to-block candidates need adjudication.
