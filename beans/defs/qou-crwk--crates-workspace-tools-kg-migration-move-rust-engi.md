---
# qou-crwk
title: "crates/ workspace & tools KG migration: move Rust engines to top-level crates/* + Cargo workspace + defineTool KG nodes + local skill"
status: in-progress
type: task
priority: high
tags:
    - stability
    - crates
created_at: 2026-11-28T11:57:00Z
updated_at: 2026-11-28T11:57:00Z
parent: qou-s028
---

2026-11-28 (Antigravity coordinator `92bff8c9-777d-458a-a380-8dd5bf5cc0f3`, worktree `ws1-precision` -> branch `claude/crates-workspace-and-tools-kg-20261128`): Move `tools/hecke-engine*`, `tools/pyhecke-native`, and `tools/borromean-recurrence-crt` into top-level `crates/*` with a root `Cargo.toml` workspace, add `scripts/gen-crate-tools.ts` / `tool-defs/crates.json` (`tools` KG `defineTool` nodes), and author `.claude/skills/local/rust-crates-and-values.md`. Strictly proton-pinned (`physical_proton`) where `q_0` enters.
