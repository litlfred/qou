---
id: qou-lskl
title: "Lean KG Stage 1b: Modernize All 18 Lean/KG Skills, CI Processes, `#lint` Gates & Consolidate the 75 `scripts/*lean*` Tools for Mathlib4 / Reservoir Best Practices"
status: todo
type: task
priority: high
parent: qou-lnkg
created_at: 2026-11-23T20:27:30Z
updated_at: 2026-11-23T20:27:30Z
---

## Measured Diagnosis (`origin/main`)

1. **Stale / Contradictory Lean & KG Skills (`18` `.claude/skills/local/*.md` files):**
   - `formalizer.md` still advertises *"sorry-bridged partial proofs"* (violating zero-sorry discipline) and `\lean{QOU.X}` LaTeX macros.
   - `lean-proof-review.md` still points to legacy `proof-objects.json` and LaTeX reviews instead of `.qa.json` sidecars, `#lint` (`docBlame`, `simpNF`, `unusedArguments`, `dupNamespace`), `set_option autoImplicit false`, `snake_case`/`UpperCamelCase` Mathlib4 naming, and minimal targeted `import Mathlib.*` discipline.
   - `ontologist.md` still invokes `chapters/*.tex` and `.github/scripts/ontologist.py`.
   - `lean-mathlibext-curator.md` still describes a single 5-section `QOU/MathlibExt.lean` file rather than the Two-Tier (`MathlibExt` core PRs + 6 Reservoir-ready standalone `lean_lib` community packages) architecture with strict zero-`QOU`-import enforcement.
   - `content-graph.md` & `detangler-integration-watcher.md` lack Lean import-DAG / subgraph-purity rules (`L1..L6`) and carry a stale `PR1` chapter table.
2. **Sprawl of `~75` Overlapping `scripts/*lean*` Scripts:**
   - Over a dozen competing build/verify wrappers (`lean-verify.sh`, `lean-verify-cone.sh`, `lean-verify-changed.sh`, `verify-lean-direct.sh`, `lean-direct-cone.sh`, `lean-build-cone.py`, `lean_cone_build.py`, `leancheck-worktree.sh`, etc.) with no single canonical entry point or automated Mathlib4-style/purity linter gate.

## Deliverables

1. **Update All Lean, Proof & KG Skills (`.claude/skills/local/`):**
   - Align `formalizer.md`, `lean-generation.md`, `lean-proof-review.md`, `lean-environment-setup.md`, `lean-build-fix.md`, `lean-completeness-audit.md`, `lean-proof-vacuity-audit.md`, `lean-substantive-pass.md`, `lean-mathlibext-curator.md`, `proof-integration-watcher.md`, `ontologist.md`, `content-graph.md`, and `detangler-integration-watcher.md` to enforce:
     * Official `Mathlib4` / Reservoir community package style (`snake_case` defs/lemmas, `UpperCamelCase` types/props/classes, `/-! ... -/` module docs, `/-- ... -/` declaration docs, `set_option autoImplicit false`, minimal targeted `import Mathlib.<Module>`, `@[simp]`/`@[ext]` API completeness, `#lint` clean);
     * Strict **subgraph-placement & import-boundary discipline** (new non-QOU math goes directly into the appropriate Reservoir community `lean_lib` subgraph with **0 `QOU.*` imports**; QOU model theorems go into the single canonical chapter subgraph — never spawning synonym folders!);
     * Single-threaded `nice -n 10` overlay cone verification (`lean-direct-cone.sh`, never `lake build` from scratch) + §7c generic base-ring discipline.
2. **Build `scripts/lean-best-practices-lint.py` & Rationalize `scripts/*lean*`:**
   - Add a fast static + `#lint` gate checking: (a) zero `import Mathlib` umbrella imports, (b) zero `QOU.*` imports inside Tier-A/Tier-B community subgraphs, (c) `set_option autoImplicit false` & module/public-decl docstrings on community subgraphs, (d) synonym-directory creation blocklist, and (e) clear `README`/router index over `scripts/*lean*` deprecating redundant wrappers into canonical entry points.
