# ORPH: orphaned content in qou (read-only census, 2026-10-04)

**Scope.** qou `main` @ `348e299cce` (2026-10-03). I only read the repo. **The owner's hard rule applies to every line below.** No item asks for a statement, proof, definition, Lean declaration, witness or number to be edited or removed. Each one is about *containers*: whether the structure that renders or validates a piece of content can reach it at all. `confirm-dead` means the owner looks at it, not that anything gets deleted.

**Method [M].** The scripts are in `scratchpad/orph/`.
- `dump.ts` imports every paper, chapter and block manifest with bun, so the reading is authoritative and not a regex. qou's `folio/schema/builders.ts` re-exports from `../../folio-assistant/...`, which does not exist in this checkout, so I swapped in a stub (`stub-builders.ts`).
- `analyse.py` does the classification. Reachable means: chapter dir in `paper.chapters[]`, block stem in that chapter's `sections[].blocks` or `subsections`, and the resolver only looks in the block's own dir (`schemas/types.ts` `Section.blocks`).
- Lean: I parsed declarations (namespace, section and end) across `lean/**` per package. A file counts as built only when its module is inside the lib's `globs = ["QOU","QOU.+"]`.
- References are checked against block, chapter and section labels and against `\label{}` in prose.
- Assets: a file counts as referenced if its name or stem appears as a token in the folio tree, then in tools/producers (scripts, computations, CI, qou-mass), then in docs/beans.
- `branches.sh` checked a bounded sample of branches.
- Dates come from a first-parent log of `main` that skips the `qou-yqko` content→folio move. Lazy tree fetching limited that log to on or after 2026-08-30, so older rows read `<=2026-08-30`.

Inventory: `out/ORPH_inventory.tsv` (3,383 rows, one per path×class).

## Totals per class [M]

| class | inventory rows | what was measured |
|---|---|---|
| unreferenced-block | 3 | 3 of 3,676 QOU block manifests are in no chapter section. All chapter dirs are in the paper manifest (36/36), and all 5 papers are clean at chapter level. |
| isolated | 3 | The same 3: no section lists them **and** nothing points to them (no `uses`, `interprets` or `\ref`). |
| missing-sibling | 14 | 0 `.ts` without `.md`. 14 `.md` with no `.ts`, all in chapter `audit/` subdirs (probes). |
| lean-not-built | 1,417 | **833** chapter-dir `.lean` siblings (821 QOU, 12 UGB) declare names that are absent from any lake target. **582** block `lean.ref`s resolve *only* to such an uncompiled sibling. 2 files sit outside the globs (`lean/scratch_lean.lean`, UGB `test.lean`). |
| lean-unlinked | 759 | 13 sibling `.lean` with no `.ts` (breaks folio-assistant's `no-orphan-lean`). 746 built modules that no block `lean.ref` names and no module imports. |
| dangling-ref | 82 | `lean.ref`: 30 resolve to nothing, 17 name a module path rather than a declaration, 26 have only a same-short-name match (namespace drift). 5 `.ts` refs and 4 prose refs point to no label (2 are cross-paper `unital-groebner-bases:` labels that do not exist). |
| missing-file | 60 rows (107 findings) | 12 `computation.script` paths are absent. 86 relative links in prose are broken: 23 use the wrong `../` depth (the target exists), and 63 have no target (e.g. dissolved chapters `archimedean-universe/`, `particle-interactions/`). 9 simulator manifests import `../../../folio-assistant/...`, which is absent, so they cannot load. |
| unused-asset | 533 | 246 live `computations/` files are named by nothing (`_deprecated/`, 1,738 files, was not counted). 38 of 40 `uploads/` files. 249 `library/` dirs are not registered in `references.ts`: 232 are in the intake ledger, 17 are in nothing. |
| outside-tree-math | 499 | `docs/audits`: 30 `.lean`, 68 `.py`, 272 derivation/probe `.md`. `fsh-guts` 46, `qou-mass` 33, `simulations/` 2, plus other `docs/` notes, `qou-all-tables.tex` and `standalone-index-of-definitions.tex`. None is named by any block. |
| branch-only-math | 13 | In the sample: 12 distinct Lean modules on 7 unlanded branches that exist nowhere under `folio/` on main. |

Not rows, but measured:
- `lean.ref` health: 654 of 1,309 refs resolve into the compiled library. That is **50%**.
- 513 of the references in `references.ts` are cited by no block, and 4 cites point to no reference: `bokut1978`, `faddeev1996`, `manuscript`, `milnor1950`.
- One label is duplicated across papers: `def:witt-vector-lift` exists in both QOU and fred2005.
- 4 macros used in prose are defined only in `main.tex` and not in the paper manifest's `macros`: `\pp`, `\bigbowtie`, `\varTheta`, `\yng`.

## Branch-only math (item 7) [M]

The sample was the 60 most recent unlanded branches in `branch_status.tsv`, with tip dates from 2026-09-07 to 2026-10-02 (59 in September, 1 in October). The full census is the other analyst's.
- 32 of the 60 touch block, `.md` or `.lean` content. 28 touch none.
- **27 carry content that is not on main.** 16 files are absent on main and 55 differ from main. A "differs" can also mean main moved on since the branch, so it is not counted as math.
- Absent on main after excluding schema files: **12 Lean modules on 7 branches.**
  - `p-neq-np-gaps-n8dxxl` (6: `CasimirBlockValue`, `TauDualBasis`, `CasimirBasisIndependence`, `CasimirBlockScalar`, `CasimirTransport`, `WenzlCandidateNormalisation`)
  - `brng-class-d-fibre-tower` (2)
  - `ModularDoubleLocusSeparation`, on 2 branches
  - `TLCarrierBridge`
  - `SingleCrossingChainFactorizes`
  - `CyclotomicEvaluationRingHom`
- `find` shows none of these names anywhere on main.
- All the sampled branches use the old `content/` paths, so landing any of them now requires remapping to `folio/`.

## The 20 most important orphans

1. **582 blocks whose `lean.ref` resolves only to an uncompiled sibling.** Examples: `QOU.TannakaDual`, `QOU.HadronFibreEmbedding`, `QOU.BraidKnot.Hecke1dIrrep.hecke_1d_irrep_closed_form_character`. The formal backing these blocks advertise is checked only by `lean-content-siblings.yml`, which is dispatch-only (owner billing directive, 2026-06-30). A migration that trusts the `lean.ref` → lake target mapping would mark them all as resolved or failed incorrectly. **S1/S6**
2. **821 QOU sibling `.lean` files with names absent from the built library.** This is formal content that `lake build QOU` never compiles. Only 265 of all 938 siblings `import QOU`. **S1**
3. **30 `docs/audits/*.lean`.** Several are refutation or vacuity results about paper content, e.g. `2026-08-30-skein-mass-relation-is-false.lean`, `2026-08-31-double-magic-conjecture-is-false.lean`, `2026-08-24-parallelogram-axioms-inconsistent.lean`, `2026-08-30-qns-carriers-are-refutable.lean`. No block links to them and no build covers them. They are the highest-risk outside-tree math: a migration that carries only `folio/` drops the evidence that some paper claims are false or vacuous. **S3/S6**
4. **12 branch-only Lean modules** (list above), including the P≠NP-gap Casimir work. **S6**
5. **13 sibling `.lean` with no block**, e.g. `braids-and-knots/chi-std-pernucleon-closed-form.lean` (32 declarations, none built), `frobenius-antipode-lean-stub.lean`, `pentagon-uv-commutation-woronowicz.lean`, `molecular-construction/aufbau-open-strand-perron.lean`. folio-assistant's `no-orphan-lean` rejects these. **S6**
6. **3 isolated propositions:**
   - `prop:atomic-q-reeb-universal-rho` (Lever 3, mass-theory)
   - `prop:qbeta-toroidal-harmonics-basis` (mass-endomorphism)
   - `prop:delta-max-numerical-scale` (appendix-mass-binding-algorithms)

   Each has `.md`, `.ts` and a QA sidecar, but they render nowhere. The first two relate to Q_β and binding (the L2 1ppQ programme). **S3**
7. **30 dangling `lean.ref`s**, e.g. `QOU.FluidDynamics.QNavierStokes`, `NSObstruction`, `QOU.DescentLemma`, `QOU.BraidKnot.confined_knot_binding`, 3 UGB `LeadingTerm`/`RemainderModule` refs. The block claims formal backing that the parser can find nowhere. **S6**
8. **12 absent `computation.script` files** (`probe_per_wedderburn_block_ck.py`, `probe_q_beta_*`, `confinement_operator_selection.py`, …) behind 12 blocks, including χ closed-form proofs. The computational provenance cannot be reproduced. **S3**
9. **68 `docs/audits/*.py` computations** that live outside `computations/` and are linked by no block. **S3**
10. **272 `docs/audits` derivation and probe notes.** This is narrative math with no block home. **S3/S6**
11. **9 simulator blocks** that import the absent `../../../folio-assistant/cat-harness/schemas/builders`. They cannot load without the monorepo layout. **S2/S4**
12. **14 `audit/*.md` probes inside chapter dirs** (nuclear-interactions ×8, knots-particles-confinement ×4, both surreals appendices ×1 each). These are in-tree but in no structure. **S3**
13. **33 unlinked `qou-mass/` modules** (mass pipeline: `hecke_core`, `markov_trace_canonical`, `closed_form_tau_M`, …). The code behind mass numbers has no block anchor. **S3**
14. **26 namespace-drift `lean.ref`s**, e.g. `QOU.QFlatConnection` vs the built `QOU.QGeometricLanglands.QFlatConnection`. These are pointer errors, not missing math. **S6**
15. **86 broken relative links in prose**, 63 of them to dissolved chapters or files. **S2/S5**
16. **4 macros only in `main.tex`** (`\pp`, `\bigbowtie`, `\varTheta`, `\yng`) are used in prose. Retiring legacy rendering loses them unless they move into the manifest's `macros`. **S5/S7**
17. **`qou-all-tables.tex` (16,700 lines) and `standalone-index-of-definitions.tex`** are generated by legacy scripts, are linked from nothing, and are consumed only by the layout-test harness. **S3** (tables audit) and **S5**
18. **246 unreferenced live computations** (`.py` and witnesses). Witnesses carry numbers. **S3**
19. **249 unregistered library entries and 513 uncited references.** This is source material outside the citation graph, not authored math. **S3/S6**
20. **38 of 40 `uploads/`**, including WHO guideline PDFs that look like another folio's material. **S3**

## Which migration story each class affects

| class | S1 decl/config | S2 symlink/monorepo paths | S3 folio_init layout + tables | S4 simulators | S5 legacy render | S6 KG authority | S7 PDF→sci |
|---|---|---|---|---|---|---|---|
| lean-not-built | ●● (lake targets vs sibling triple) | | | | | ● | |
| lean-unlinked | | | | | | ●● | |
| dangling-ref | | | | | | ●● | |
| unreferenced-block / isolated | | | ●● | | ● | ● | |
| missing-sibling (audit/*.md) | | | ●● | | | | |
| missing-file | | ●● (`../` depth, monorepo import) | ● | ●● (9 simulators) | ● | | |
| unused-asset | ● (`computations` has no witness graph kind) | | ●● | | | | |
| outside-tree-math | | ● (fsh-guts) | ●● | ● (simulations/) | ●● (main.tex, tables) | ● | ● (macros) |
| branch-only-math | | ● (content/→folio/) | | | | ●● | |

## Proposed handling by class (no deletions)

- **Lean.** Bring the siblings under a compiled target, or record the decision not to: `link-into-structure` (S1, owner's call between a sibling lake lib and the folio-assistant triple-compile path). For the 30 dangling refs: `owner-review`. For the docs/audits `.lean` files: `migrate-as-content` into an audit graph or a sibling.
- **Blocks.** The 3 isolated blocks: `link-into-structure` (the owner picks the section) or `confirm-dead`.
- **Branch-only math.** `owner-review` per branch, together with the census analyst.
- **Generated files.** `qou-all-tables.tex` and the index tex: `regenerate`.
- **Assets.** `confirm-dead (owner decides)` for computations referenced by nothing. `link-into-structure` for library entries in the ledger.

## Skill gaps: generic orphan detection folio-assistant should own

1. **Structure reachability (cat-harness, generic `document`).** `validate.ts` has `no-orphan-sidecar` but no check for "on disk but in no section" or "listed but absent". qou needed a custom bun stub to measure this. The fix is a `no-unlisted-block` and `listed-block-exists` rule in `content/pipeline/validate.ts`, run per adapter.
2. **`lean.ref` resolves into a *compiled* target (folio-assistant-sci, paper adapter).** `no-orphan-lean` only checks for a `.ts` sibling. Nothing asks whether the referenced declaration sits in a lake target that CI builds. The paper adapter should own a `lean-ref-built` rule that reads `lakefile.toml` globs.
3. **Outside-tree content inventory (cat-harness `repo-conversion` skill).** Extend its read-only scan to classify `docs/**/*.lean|*.py|*.md` derivations as `outside-tree-math` against block links. It is the only migration step that sees these files.
4. **Asset and link resolution (cat-harness).** Relative links, `computation.script`/`witness` paths and `{{ <instance>.computations… }}` should be resolved against the *declared* directories. Also the `computations` witness graph kind that qou already filed (folio-assistant bean, 2026-09-30).
5. **Branch-only content (cat-harness sdlc, `goal-review` / `ci-health` family).** Count block, `.md` and `.lean` files that exist only on unlanded branches, with layout remapping.
6. **Platform hard-codes qou.** `cat-harness/content/pipeline/audit-wiring.ts` still walks `content/quantum-observable-universe/`. That is folio content baked into the platform, and stale since the move to `folio/`. **S1/S2**

## Caveats

- **Reachability check.** Chapter manifests were read only for block stems. Blocks placed through `proofs[]`/`examples[]` labels are treated as referenced rather than rendered.
- **Lean parser.** The declaration parser is heuristic: no `variable`, `open`-scoped or `mutual` handling. The 26 fuzzy refs show where it is uncertain.
- **Asset references.** A "referenced" asset is a token match, so its count is generous and the unused counts are lower bounds.
- **Dates.** Dates older than 2026-08-30 are bounded, not exact.
- **Workspace incident.** One mis-scoped shell command created two empty files (`br_files.tsv`, `br_sample.tsv`) in `/home/user/qou`. I moved them to `scratchpad/orph/stray_*` within minutes, and `git status --porcelain` is now empty.
