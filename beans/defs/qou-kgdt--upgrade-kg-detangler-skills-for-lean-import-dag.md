---
# qou-kgdt
title: 'Lean KG Stage 1: Upgrade KG & Detangler Skills (`content-graph`, `lean-mathlibext-curator`, `lean-kg-detangler.py`) and Map Full 4,545-File Lean Subgraph DAG'
status: completed
type: task
priority: high
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-24T09:20:35Z
parent: qou-lnkg
---

## Deliverables
1. Build `scripts/lean-kg-detangler.py` (emitting `.jsonld` / JSON + Markdown DAG report) analyzing all `~4,545` `.lean` files: import condensation DAG, strongly-connected/bipartite coupling ratios, QOU-purity boundary (`0` `QOU` model types in `Mathlib`-candidate modules), unused imports, and synonym-folder overlap (`7` knot dirs, `7` mass dirs, `3` Hecke dirs, `3` Bring dirs).
2. Update `.claude/skills/local/content-graph.md` (fix stale `PR1` chapter table + add Lean-subgraph heuristics `L1..L6`), `detangler-integration-watcher.md`, and `lean-mathlibext-curator.md` (update from single-file `MathlibExt.lean` to multi-subgraph `Mathlib` upstreaming curation).



## Worker 27 Delivery (2026-11-23 — Issue #9235, Ready PR #9236)
- Implemented `scripts/lean-kg-detangler.py` (`10.54s` across `4,751` `.lean` files: `3,842` in `lean/` across `83` `QOU/*` dirs + `909` chapter siblings; `unassigned_modules=0`, `unassigned_edges=0`).
- Generated `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json` and `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md` comparing 3 concrete `AskUserQuestion` refactor options (`12` `QOU.<Subgraph>` homes + Tier-A `MathlibExt` `321` + 6 Tier-B Reservoir `lean_lib` targets `1,359` = `1,680` pure community modules, `188` cut-edges).
- Ready PR: https://github.com/litlfred/qou/pull/9236 (holding merge for owner OK).

Closed via post-merge reconciliation: landed on origin/main in PR #9236 (e54c69cdd49).
