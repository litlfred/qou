---
# qou-kgdt
title: 'Lean KG Stage 1: Upgrade KG & Detangler Skills (`content-graph`, `lean-mathlibext-curator`, `lean-kg-detangler.py`) and Map Full 4,545-File Lean Subgraph DAG'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-23T23:30:34Z
parent: qou-lnkg
---

## Deliverables
1. Build `scripts/lean-kg-detangler.py` (emitting `.jsonld` / JSON + Markdown DAG report) analyzing all `~4,545` `.lean` files: import condensation DAG, strongly-connected/bipartite coupling ratios, QOU-purity boundary (`0` `QOU` model types in `Mathlib`-candidate modules), unused imports, and synonym-folder overlap (`7` knot dirs, `7` mass dirs, `3` Hecke dirs, `3` Bring dirs).
2. Update `.claude/skills/local/content-graph.md` (fix stale `PR1` chapter table + add Lean-subgraph heuristics `L1..L6`), `detangler-integration-watcher.md`, and `lean-mathlibext-curator.md` (update from single-file `MathlibExt.lean` to multi-subgraph `Mathlib` upstreaming curation).
