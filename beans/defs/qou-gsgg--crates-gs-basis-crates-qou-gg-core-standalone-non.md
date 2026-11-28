---
# qou-gsgg
title: "crates/gs-basis + crates/qou-gg-core: standalone non-commutative Groebner-Shirshov library + pure-Rust 4-photon & Z=0..118 T3/Hopf chart generator"
status: completed
type: task
priority: high
tags:
    - stability
    - crates
created_at: 2026-11-28T11:57:00Z
updated_at: 2026-11-28T12:42:55Z
parent: qou-s028
---

2026-11-28 (Antigravity coordinator `92bff8c9-777d-458a-a380-8dd5bf5cc0f3`, worktree `ws12-pr9180` -> branch `claude/crates-gs-basis-and-qou-gg-core-20261128`): Build standalone QOU-agnostic non-commutative Groebner-Shirshov crate `crates/gs-basis` (`1A+1B` combined: dynamic Buchberger-Shirshov + Bokut-Shiao Coxeter + `TL_n` diagram reducers, `0` C-FFI) and `crates/qou-gg-core` (pure-Rust 4-term/4-photon + `PhotonU1NeutralCut` + `Z=0..118` `T3`/Hopf atomic-chart generator).

- **2026-11-28 (merge-steward)**: Reconciled additive `Cargo.toml` / `Cargo.lock` / `tool-defs/crates.json` with `#10011` and landed PR `#10012` (`claude/crates-gs-basis-and-qou-gg-core-20261128` @ `280c1aa31f20`) onto `origin/main` at `fdc097cab80067021ed645f8af9894cc960f64da` (`MISSING: 0`, `bun run cat check:tools` PASS). Marked `completed`.
