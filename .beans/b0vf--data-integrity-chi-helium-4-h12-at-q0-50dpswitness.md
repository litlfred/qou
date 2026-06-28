---
# b0vf
title: 'Data-integrity: chi-helium-4-h12-at-q0-50dps.witness.json only 17/77 complete (22%) — needs He4 H12 chi producer re-run'
status: todo
type: task
created_at: 2026-06-28T06:38:41Z
updated_at: 2026-06-28T23:30:00Z
---

## Environment block (2026-06-28) — pyhecke_native unbuildable in-sandbox

The producer `computations/chi_4he_via_rust_lossless.py` needs `pyhecke_native.chi_q_via_gp` (Rust)
for the H₁₂ χ evaluation. Building `tools/pyhecke-native` here FAILS: its `clarabel` Cargo dep is
pinned to `github.com/litlfred/Clarabel.rs` — a repo OUTSIDE this session's `litlfred/qou` GitHub
scope — so the agent proxy returns HTTP 403 on the git fetch (via libgit2 AND
`CARGO_NET_GIT_FETCH_WITH_CLI=true`). Hard environment restriction, not code. Also: completing the
witness is ~2.8 h (committed partial = 17/77 in 2241 s). Needs an env where `litlfred/Clarabel.rs` is
reachable (or a prebuilt pyhecke_native wheel) + a dedicated long run. No change made. Audit:
`docs/audits/2026-06-28-adhb-r5-multiterm-insufficient-b0vf-native-blocked.md`.

