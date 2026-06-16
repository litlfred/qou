# Tooling extraction + skills/MCP consolidation — workplan

**Date:** 2026-06-11 · **Owner direction:** (a) extract `pyhecke` +
`hecke-engine` (+ Clarabel-fork SDP backend) into a standalone open-source
repo with all QOU references removed, history preserved via slow curated
cherry-pick; soft outreach to the math OSS community; (b) finish the
started-not-finished move of agent skills/MCP into `folio-assistant`;
(c) endpoint: the qou repo becomes content-centric.

**Status:** workplan; census appendix:
[`2026-06-11-tooling-extraction-census-appendix.md`](2026-06-11-tooling-extraction-census-appendix.md)
(per-package verdicts: pyhecke/pyhecke-native/witness-schema mechanical;
**hecke-engine needs-refactor** — 83 physics-coupled files, hardcoded Q_0 +
nucleon-named functions in `src/gram.rs`; bindings trivial; Clarabel
confirmed as the `litlfred/Clarabel.rs` fork @ `9673209` patched in two
Cargo.tomls; 221/778 compute scripts consume the tools via the
`hecke_core.py` choke point; skills migration = revive the archived
`FOLIO_MIGRATION_PLAN.md` §Skills Audit).

## Confirmed structural facts (2026-06-11 spot-checks)

1. **The coupling is import-time, not just dependency-listing.**
   `tools/pyhecke/python/pyhecke/gram.py` computes module-level constants
   (`z`, `W_SYM/W_STD/W_ALT`, `TR_M`, `G`, `G_INV`) **at import** from the
   substrate q₀ (`q_parameter` shim → `qou_substrate.constants` fallback).
   `wedderburn.q_hook_product` evaluates "numerically at the global
   substrate q = q₀". De-QOU therefore means an **API change**
   (parametrize q), not a find-replace.
2. **The external-use fallback chain already exists** ("Sage docker, PyPI
   installs, Pyodide" per gram.py comments) — the package anticipated
   standalone use; the extraction completes that intent.
3. **Clarabel** is a feature-flagged SDP backend in
   `tools/hecke-engine/Cargo.toml` (`required-features = ["clarabel-sdp"]`,
   dedicated bins/tests). Fork-vs-crates.io status: census appendix.

## Phases (prioritized)

### Phase 0 — coordination + freeze (immediate, this week)

- **Intent comments** on overlapping siblings: #2104 (compute-pipeline
  generalization — its "generalized infra" scope may BE part of Phase 2;
  reconcile before either side restructures `tools/`), #2103 (per-isotope
  stack — heavy pyhecke consumer; API-stability notice).
- **The Wall lint gate (soft):** CI grep gate asserting no *new* `qou`
  references enter `tools/pyhecke`, `tools/hecke-engine*` (warn-only until
  Phase 2 completes, then hard). Prevents drift while extraction proceeds.
- **Decisions needed from owner:** target repo name + org; license
  (recommend MIT OR Apache-2.0 dual, Rust-ecosystem convention);
  provenance line for the new README ("developed within a private research
  monorepo" — no QOU naming).

### Phase 1 — the Wall (API boundary spec)

Per-module disposition table (draft; census appendix will finalize):

| module | disposition | refactor required |
|---|---|---|
| `tools/hecke-engine` (Rust core: GS reducer, Hoefsmit, Markov trace, Clarabel SDP) | **goes** | strip QOU-flavored docs/tests; neutral fixtures |
| `tools/pyhecke` | **goes** | **parametrize q** (kill import-time q₀ constants); substrate becomes a *caller*, not a dependency |
| `tools/pyhecke-native` | **goes** | path-dep repoint to new workspace |
| `tools/hecke-engine-{wasm,node}` | **goes** | flag Tier-3 maintenance status |
| `tools/hecke-engine-{r,jvm,c}` | **goes** (Tier-3) | community-maintenance banner |
| Clarabel fork | **goes** (workspace member or `[patch]`) | document the delta vs upstream; upstream what's upstreamable |
| `tools/qou-substrate` | **stays** (q₀, calibration, witness defaults are physics) | depends on extracted pyhecke, inverted from today |
| `tools/witness-schema` | **split decision** (owner): neutral "computation witness" schema is part of the OSS value-prop; QOU-specific fields stay behind | TBD |

Dependency-inversion principle: **generic layer never imports substrate;
substrate configures the generic layer at call sites.**

### Phase 2 — de-QOU in place (inside qou, before any extraction)

Rationale: 14+ sibling PRs are in flight against these files; extracting
first forks the code and creates merge hell. Restructure in-place with one
source of truth; each de-QOU commit is authored clean (neutral message, no
physics values) so the later cherry-pick is a replay of already-sanitized
units — this IS the "slow historical cherry-pick" preparation.

- 2a. q-parametrization API for `gram`/`wedderburn`/`trace*` (+ deprecation
  shims for the 19 in-repo importers; mechanical consumer migration PR).
- 2b. Neutral test fixtures (symmetric-group data, generic q ∈ {2, 3/2,
  golden}, exact Fractions) replacing physics-pinned assertions; physics
  regression tests MOVE to `computations` (they are qou's,
  not the library's).
- 2c. READMEs/docstrings rewritten neutrally; no `q₀`, no MeV, no CAL-*.
- 2d. Wall gate flips to hard.

### Phase 3 — new repo bring-up + history transplant

- Curated cherry-pick, batched per package and era; per-commit
  sanitization checklist: no physics constants in messages/diffs, no
  witness payloads, no `content/` paths; authorship/dates preserved
  (cherry-pick keeps author); provenance note in README. Documented
  alternative (NOT chosen, owner preference): `git filter-repo
  --replace-text` — fast but leaks monorepo structure.
- Cargo workspace + maturin + pure-python package; CI: cargo test, pytest,
  wheel matrix; docs.rs + readthedocs or mkdocs.
- PyPI/crates.io metadata repoint (homepage/repository URLs) + first
  release from the new repo.

### Phase 4 — qou consumes the extracted packages

Pin published versions (or a git dependency during stabilization); migrate
the in-repo importers; delete `tools/{pyhecke,hecke-engine*}` from qou.
**Endpoint: "this branch becomes more about content."**

### Phase 5 — skills/MCP → folio-assistant (parallel with 2–3)

Finish the started migration: skills under folio-assistant's registry
(served via `skill_list`/`skill_fetch`), `.claude/skills/local/` reduced to
thin pointers/shims so Claude Code sessions still resolve; `.mcp.json` /
`folio.config.json` / `skills-config.json` rewiring. Generic skills
authored since the census (e.g. `symbiotic-interaction`, the
three-register author-input protocol) join the move list. Census appendix will
record what already moved and the intended finished state. (Horizon note,
out of scope here: folio-assistant itself is the *second* extraction
candidate — the symbiotic-authoring product.)

### Phase 6 — soft outreach (gated on owner approval per outward-action rule)

README quickstart (Jones polynomial / Markov trace in five lines),
benchmark table, examples notebook; quiet channels only (a sage-devel
note, a Rust-sci forum post). **No physics framing anywhere.** Every
outward message pre-approved by owner.

## Priorities

| # | item | size | priority |
|---|---|---|---|
| 1 | Phase 0 intent comments + wall gate (warn) | S | **P1 — now** |
| 2 | Phase 1 wall table finalized (census + owner decisions) | S | **P1** |
| 3 | Phase 2a q-parametrization | M | **P2** |
| 4 | Phase 2b–2d fixtures, docs, hard gate | M | **P2** |
| 5 | Phase 5 skills/MCP consolidation | M | **P2** (parallel) |
| 6 | Phase 3 new repo + transplant | L (slow by design) | **P3** |
| 7 | Phase 4 qou repoint + tools/ deletion | M | **P3** |
| 8 | Phase 6 outreach | S | **P4 — owner-gated** |

## Coordination ledger

`docs/coordination/tooling-extraction.md` (created with this plan) tracks
per-phase claims, sibling overlaps, and decisions. All extraction-touching
sessions append there.
