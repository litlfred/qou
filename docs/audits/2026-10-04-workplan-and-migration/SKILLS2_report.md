# SKILLS2: qou agent guidance mapped to folio-assistant Skill, Process, Role and Ruling nodes

This was a read-only pass on 2026-10-04. qou was at `afa49febf` (branch `claude/work-plan-reorg-2026-10-04`) and f-a at `origin/main` `0b7b9e44e`. It reuses `out/SKILLS_report.md`. Two inventories go with it: `SKILLS2_inventory.tsv` has 151 artefact rows, and `SKILLS2_agents_sections.tsv` has 101 AGENTS.md headings (outside code fences), each with a class and a target.

## 0. Three findings that change the plan

1. **qou declares no skills graph.** `qou.json` declares only `folio`, `library` and `computations` [M]. That means `.claude/skills/local/` (96 `.md` files and 20 `.ts` files) is not reached by `resolveSkillDirs`, `skill_list` or `kg:audit`. It is the inverse of the `dh4f` defect: a directory that exists but is undeclared. This has to be fixed before any overlay can work.
2. **The "skill overlay" is replacement at package level, not merging at skill level.** I read `discoverLocalPackages` (`cat-harness/scripts/skill-packages.ts`) and `locateLocalSkill` (`src/tools/skill-fetch.ts`) on origin/main [M]:
   - Later directories win **by package name**. The root goes last, so a qou package called `folio-paper-adapter` would shadow all of sci's package.
   - When two packages hold a skill with the same name, a bare-name fetch returns *"held by N packages … Pass one as package_name"*.
   
   **No mechanism lets a qou skill extend an f-a skill.** So "thin overlay" needs either a naming convention (`qou/formalizer` that starts with "base: `folio-paper-adapter/formalizer`") or a new `overlays:` front-matter key that `skill_fetch` composes. That is GAP-1.
3. **Neither `attestations` nor `interaction` is a home for owner rulings.**
   - `attestations` (`qa-attestations/v1`) stores QA *judgements about a subject path*, keyed by a mirrored path [M, cat-harness.json].
   - `interaction` (`folio-interaction/v1`) stores *how a person wants to be asked*. It already holds litlfred's `low-dexterity` profile [M], so qou's 212-line "User accessibility" section is redundant with it.
   
   The nearest existing kinds are `convention` (`schemas/convention.ts`: id, statement, rationale, applies, bound to process/lane/activity, "absent binding means none") and ODRL `policies/` (what an actor may do). Neither stores a dated, verbatim, superseding owner decision. That is GAP-2 (§4).

## 1. AGENTS.md (6,179 lines), classified by section

Lines are counted per leaf heading, outside code fences [M]. The script is `SKILLS2_agents_sections.py`.

| class | lines | % | what it is | target |
|---|---|---|---|---|
| GENERIC (pointer to an existing f-a skill) | 2,099 | 34 | Work-plan policy (536), branch/PR rules (391), Lean-for-agents rules (sorry citation, vacuity, naming, block kinds, conjecture taxonomy, remarks, glossary, authorNotes; about 450), accessibility (212), subagent memory (125), GitHub links (64), strict-Lean items | `todo-manager`, `bean-coordination`, `continual-progress`, `prepare-merge`, `agent-memory`, `interaction-modality` + `interaction.json`, `delivery-summary`; sci `lean-*` and `proof-status-tracking` |
| RULING-MATH (math conventions; **verbatim only**) | 2,056 | 33 | Precision goals and the q₀-anchor block (1,318), the canonical-derivation cheat sheet (271), no-fitting/CAL-1/2/3 (57), §3b-cond Option B (124), notation and approximation, Hecke-Skein, KLR, base ring (about 215), LP/SDP duals (51) | Ruling nodes plus the qou docs that already exist: `docs/precision-goals.md` and `docs/canonical-derivation-cheat-sheet.md`. Move by rename, no rewording. |
| STALE | 605 | 10 | Content-object architecture (177; 9 of 12 cited paths are missing [M] because `content/` became `folio/` and the `folio-assistant/` submodule is absent), project structure (89; 12 of 30 paths missing [M]), gh-pages build (110; site deprecated by the owner on 2026-09-27), skill routing table (108; superseded by `skill_list`), `lean.ref` migration (46; "aliases pruned by miga"), TodoItem lifecycle (33; superseded by beans), protected `deploy/` files (14; deploy retired) | Delete from AGENTS.md only after the owner confirms |
| PROC-QOU (qou procedure) | 527 | 9 | Lean MCP and Mathlib-cache manual fallback (414; seed counts and the qou `lake-cache/qou-v4-24-0` branch), Lake workspace package table (57), billing-failure recognition (31), batch audit-job exception (19), glossary Chapter 8 (20) | qou overlay on sci `lean-environment-setup` / `lean-cache-restore`; the billing signature goes upstream to ch `ci-health` |
| PROC (generic procedure missing from f-a) | 488 | 8 | Corpus-grep before declaring something open (272), before declaring it refuted (59), defined residual ≠ decomposition (46), conditional-proved ≠ premise (27), formalize-first and probe discipline (84) | **New sci skills**: `epistemic-claims` and `formalize-first` (SKILL GAPS), with qou corpus paths as an overlay |
| RULING-PROC (process/policy rulings) | 403 | 7 | Model-by-default (08-07), ask-owner (09-07), red-team license (06-10), parallel duplication OK (07-17), QA agent-owned (06-25), CI dispatch-only/billing (06-30), strict Lean (07-27), rule 13a (09-06) | Ruling nodes, each with a `convention` binding to the processes it constrains |

On rulings: **at least 28 headed "owner ruling/directive" markers** sit in AGENTS.md [M grep]. Another **283 of 5,462 beans** and **365 docs files** mention one [M grep -l]. The branch-rules block (1122, 343 lines, counted as GENERIC) also carries three process rulings: no squash (07-29), always run `/prepare-merge` (07-29), and draft→ready by one REST call (09-05).

**Conflict needing the owner:** "parallel duplication is NOT waste" (07-17) runs against f-a's `duplicate-work-detection` direction (SKILLS gap c). The reconciliation is probably that *exploration* may duplicate and *beans* may not. I have not decided this.

### Proposed qou AGENTS.md outline (≤150 lines; the f-a banner shape)
1. Cold start (5 lines). Install beans, `beans prime`, and run the session-start sweep. Note that qou is a folio on `folio-assistant-sci`.
2. "Do not edit this file to change behaviour" banner (10). Skills, rulings and conventions are the source of truth.
3. **What qou is** (10). A mathematical model compared to measurement. The 08-07 ruling is a single pointer.
4. **Owner rulings: read before any math work** (25). A generated table (id, date, one line, link) from `rulings/`, plus the top-6 STRICT pointers: no fitting, ask owner, convention D, proton/muon pins, q₀ forever gated, 13a.
5. **Getting skills** (15). `skill_list` / `skill_fetch`; the `qou` package; how to read overlays.
6. **Processes** (15). `qou-prepare-merge`, `integration-backlog`, compute-probe, Lean verification; `workflow_next`.
7. **Actors and roles** (10). Five subagents as actors and their lanes; memory lives in `memory/`.
8. **Lean in this repo** (15). Pointers to the `lean-environment-setup` overlay and to `lean-cache-restore`.
9. **Commands** (15). `bun run gates`, the `prepare-merge` process, dashboards as Tools.
10. **Where things live** (15). `qou.json` is the list; never quote a count.
11. **Accessibility** (5). A pointer to `interaction/interaction.json`.
12. **Migration debt** (10). Links to this inventory and to epic `qou-n4r9`.

## 2. Commands: which become processes, tools or commands

| command | lines | disposition |
|---|---|---|
| `/prepare-merge` | 679 | **BPMN** `qou-prepare-merge` as a call activity extending ch `prepare-merge`. Each qou step becomes an activity bound to a skill: §1a witness-drift auto-resolve (`compute-audit`), §1a `lean.ref` migration (stale, drop), §2a reuse/simplify (`proposition-consolidation-audit`), §3 one-voice, §4 Lean 100% (`lean-build-fix`), §4a mirror-drift gate, §4b precision gates (`witnessed-values`), §6 external reviews. f-a has `merge-base`, `merge-train` and `merge-refusal` BPMN but **no prepare-merge BPMN and no content-type hook point** [M] (GAP-3). |
| `/dispatch-merge` | 90 | A command that starts the process above with a background actor. It is not a separate process. |
| `/integration-backlog` | 77 | **BPMN** in cat-harness: cluster → batch PR (≤49 files) → prepare-merge → address comments, as a loop. |
| `/dashboard-low`, `/dashboard-sweep` | 86 / 31 | **Tool nodes** wrapping `computations/mass_binding_dashboard.py --group {low,sweep}`, under qou `tools/`. The output is math data and must be printed verbatim. |
| `/coordinate`, `/dispatch-agent`, `/integration-audit`, `/integration-watch` | 35–81 | Thin wrappers. f-a already has the same commands [M], so qou keeps none once the skill deltas go upstream. |
| `/build-docs` | 33 | An f-a sci command already exists. Point to it. |
| `/build-pdf` | 35 | **Retire.** The owner ruled the legacy LaTeX/PDF build out of scope. |

## 3. qou skills: final disposition

| group | n | action | target |
|---|---|---|---|
| Stale forks (ch) | 24 | `upstream-to:cat-harness`; deleting the qou copy needs confirmation | already upstream |
| Stale forks (sci) | 30 (incl. `build-docs`) | `upstream-to:folio-assistant-sci` | already upstream |
| Generic deltas | 8 | Diff hunk by hunk, then upstream | ch; `markdown-render-check` to core |
| Generic, missing in f-a | 3 + rule | `sandbox-egress` and `language-trap-agent-audit` to ch; `paper-relevance-triage` to core; `.agents/rules/lean-infra-rule.md` to sci (merge into `lean-build-fix`/`formalizer`) | |
| **qou overlays** | 21 | Keep a qou skill named `qou/<name>` that names its base. Generic deltas go upstream first. | see below |
| qou-only | 2 | Move by rename into the declared qou `skills/` package | `lean-q-substitution`, `lean-substrate-numerics` |
| Obsolete stubs | 5 | needs-owner (repoint or remove) | `deployment-auth`, `editor`, `readability-editing`, `symbiotic-interaction`, `todo-review` |
| `build-pdf` | 1 | retire | |

**Overlay bases**, in the form overlay → base package/skill:
- `formalizer`, `compute-author`, `lean-environment-setup`, `lean-proof-vacuity-audit`, `lean-witness-audit`, `witnessed-values`, `critical-path-analysis`, `scientific-accuracy`, `production-vs-exploratory-discipline`, `canonical-watcher`, `compute-integration-watcher`, `compute-audit`, `verify-local-substrate`, `ffi-roundtrip-audit`, `groebner-basis` → `folio-paper-adapter/*` (sci).
- `one-voice-style-guide`, `bib-qa`, `ontologist`, `devils-advocate-watcher`, `detangler-integration-watcher` → cat-harness.
- `rendering-fixes` → core.

**What an overlay may contain:** qou instance data (paths, the package table, cache branch names, the q₀ pins *by reference to a ruling node*) and qou worked examples. It must not restate generic rules.

**Other agent-surface artefacts:**
- **The five subagents** (`compute-precision-auditor`, `convention-auditor`, `corpus-grepper`, `lean-verifier`, `merge-coordinator`) become **Actors** under qou `scenarios/actors/`. Their lanes become roles: `convention-auditor` → a role whose skills are the ruling nodes; `merge-coordinator` → the merge-steward lane.
- **Agent memory** (6,961 lines) becomes `memory/` nodes. `MEMORY.md` is over 200 lines in 4 of the 5 agents (513, 268, 336, 792) [M], and AGENTS.md:444 records that injection was measured absent on 2026-09-03.
- **`.claude/skills/{actors,capabilities,requirements,framework}` TS** (576 lines) map to ch scenarios, capabilities and conventions. `requirements/content-change-review.ts` maps to core's `content-change-review.bpmn`, which exists [M].

## 4. Owner rulings as nodes

**Proposal: a new `rulings` graph kind** (`holds: context`, read and never written by a process) with an `owner-ruling/v1` node. It belongs in **cat-harness** `schemas/`, because it is generic: every folio has an owner. The qou instance data goes in qou `rulings/`.

**Fields:** `id`, `date`, `verbatim` (required), `source` (chat/bean/doc), `scope` ∈ {math-convention, process, permission}, `supersedes[]`/`supersededBy`, `reaffirms[]`, `appliesTo` (processes, block labels, scripts), `record` (audit doc).

**How it connects:**
- `scope: process` rulings also emit a `convention` binding, so they load only in the processes they constrain.
- `scope: permission` rulings become ODRL prohibitions in qou `policies/` (no squash, protected files).
- Math-convention rulings keep the **verbatim text moved byte-for-byte** from AGENTS.md and audit docs, and the node only *points* at it.
- A gate checks: no dangling `supersededBy`, every AGENTS.md "OWNER RULING" marker resolves to a node id, and a superseded ruling cannot be bound.

**Top 20 rulings with their sources:**

| # | date | ruling | source |
|---|---|---|---|
| 1 | 06-26 | Canonical calibration is the decay-width triple (m_e, 𝔇_β, 𝔇_π), not masses | AGENTS.md:2295; `docs/audits/2026-06-28-calibration-canon-decay-width-ruling.md` |
| 2 | 08-15 (re-affirms 08-09) | Convention D `z=q³/(q²+1)` is canonical; C is excised | AGENTS.md:3076; `docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md` |
| 3 | 08-15 | Proton pin and colour weighting are canonical | same |
| 4 | 08-22 (re-confirmed 08-30) | The muon pin is CODATA 2022; the frozen value is retired | AGENTS.md:2999; `docs/audits/2026-08-30-p77d-job1-anchor-ruling-applied.md` |
| 5 | 08-07 | All code defaults to the experimental proton anchor q₀ | AGENTS.md:3422 |
| 6 | 08-02 | Deriving substrate q₀ is permanently gated; this supersedes the 07-11 reversal | AGENTS.md:2795; `docs/audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md` |
| 7 | 08-11 | Absolute mass is excised | AGENTS.md:2423; bean `qou-exam` |
| 8 | 06-24 | `m_e·Vol·ρ/ℏ_q²` is not the canonical absolute nucleon mass | AGENTS.md:2427 |
| 9 | 08-29 | Deuteron ruling A: braid closure; binding is not a volume term | AGENTS.md:2935; `docs/audits/2026-08-29-deuteron-knot-owner-decision.md` |
| 10 | 09-08 | ε is the Markov trace at z_D; D7 | AGENTS.md:2329; 09-07 D7 option 1 in beans |
| 11 | 09-13 | Wenzl adopted; SDP scope (B) whole element | AGENTS.md:2598; beans `qou-za3q` family |
| 12 | 08-16 | `w̃_λ` retired; bare `w_λ` = `w_λ(q)` | AGENTS.md:5048 |
| 13 | 09-03 | Full tower in SM derivations | AGENTS.md:2537; `docs/audits/2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md` |
| 14 | 07-19 | α_em R2 | `docs/audits/2026-07-19-alpha-em-r2-owner-ruling.md` |
| 15 | 09-05 | No fitting except CAL-1/2/3 | AGENTS.md:264 |
| 16 | 08-07 | The paper is a mathematical model by default | AGENTS.md:224 |
| 17 | 09-07 | Ask the owner before changing things (overrides standing sweeps) | AGENTS.md:321 |
| 18 | 09-06 | Rule 13a: never close a bean that tracks an open conjecture | AGENTS.md:6163 |
| 19 | 06-30 | CI is dispatch-only (Actions billing) | AGENTS.md:5990; 7 beans |
| 20 | 07-29 | Never squash; always run `/prepare-merge` before merging to main | AGENTS.md:1226, 1396 |

Also: 05-02 §3b-cond Option B (AGENTS.md:4349); 07-27 strict Lean (6072); 10-04 migration decisions 1/10/11 (beans `b9cj`, `qou-2dsk`, `qou-4rhu`); 03-20 editorial rules 1–10 (`.claude/decision-log.md`).

## 5. Proposed stories (under epic `qou-n4r9`, or a sibling epic "qou agent surface → nodes")

1. **S9 Declare qou's skills graph.** Move `.claude/skills/local/` by rename to `skills/` (package `qou`) and add a `kg` entry to `qou.json`. Done when: `skill_list` shows the `qou` package, and `sha256sum` of every moved file matches. Size S. Depends on nothing.
2. **S10 Retire the stale forks.** Replace the 54 stale forks with pointers, after confirming that their diff against f-a is empty or that f-a is ahead. Done when: each removal is listed with its sizes and confirmed by the owner, and `skill_fetch` serves each name from f-a. Size M. Depends on S9.
3. **S11 Upstream the generic deltas.** Covers 8 diverged skills, 3 missing skills and `lean-infra-rule`; PRs go to ch, core and sci. Done when: every hunk is either upstreamed or listed as qou residue, and nothing of the qou residue is lost (diff parity). Size L. Depends on S9.
4. **S12 Write the 21 qou overlays.** Each becomes `qou/<name>` with a base pointer, holding only qou data and examples. Done when: the union of base and overlay covers every line of the old qou copy (a line-coverage check), with zero math text changed. Size L. Depends on S11 and GAP-1.
5. **S13 Build the rulings graph.** Create the node kind (ch) and seed qou `rulings/` with the 24 rulings above. Done when: every "OWNER RULING" marker in AGENTS.md resolves to a node, and verbatim quotes are byte-equal to their sources. Size M. Depends on GAP-2.
6. **S14 Model `qou-prepare-merge` as BPMN.** Use the skill-bound activities in §2, and wrap the dashboards as Tools. Done when: `workflow_next` walks every step of the 679-line command, and the old and new step lists match. Size M. Depends on GAP-3 and S12.
7. **S15 Turn subagents and memory into nodes.** The five actors go to `scenarios/actors`, their memory entries become `memory/` nodes, and `MEMORY.md` is generated. Done when: the entry count matches, the 200-line budget is met per agent, and no entry text is changed. Size M. Depends on S9.
8. **S16 Reduce AGENTS.md to the bootstrap pointer** (≤150 lines, outline in §1). Done when: every one of the 101 sections in `SKILLS2_agents_sections.tsv` has a resolvable target, the STALE removals are owner-confirmed, and the RULING-MATH text exists byte-identical at its new home. Size L. Depends on S11–S15.
9. **S17 Classify the agent docs.** Covers `docs/coordination` (198), the 3 handover dirs (9), `agent-briefs` (4) and `.claude/validation-errors-handoff.md`. Classify only, per decision 10. Done when: there is a classification TSV and no file is moved. Size S.
10. **S18 Reconcile the "parallel duplication OK" ruling against f-a duplicate detection.** This needs the owner. Size S.

## 6. Skill gaps for folio-assistant

- **GAP-1 (ch, HIGH): skill-level overlay.** Add an `overlays: <package>/<skill>` front-matter key that `skill_fetch` composes as base plus an instance appendix, with a `kg:audit` criterion that the base exists. Today the overlay is whole-package shadowing, and a same-name skill is an ambiguity error [M].
- **GAP-2 (ch, HIGH): an `owner-ruling/v1` node and `rulings` graph kind** (fields in §4), with a gate that resolves ruling markers in prose. `convention` covers how output must look, `attestations` covers judgements, and `interaction` covers asking preferences. None of them covers "the owner decided X on date D, superseding Y".
- **GAP-3 (ch, MED): a prepare-merge BPMN with a content-type extension point** (a call activity per folio). The skill says "content-type gates run", but nothing in the process can bind them.
- **GAP-4 (sci, MED): `epistemic-claims`.** A skill that holds open/refuted/residual/conditional-proved and corpus-grep-before-open (488 generic lines that today live only in qou AGENTS.md).
- **GAP-5 (sci, MED): `formalize-first`.** Covers formalize-first and probe narrowing.
- **GAP-6 (ch, LOW): billing-failure signature** in `ci-health` (a 2–3 s multi-job failure with no logs).
- **GAP-7 (ch, LOW): `agent-memory` should state the measured non-injection** in remote sessions (qou 2026-09-03), which contradicts the f-a AGENTS.md claim that the first 200 lines are injected.
