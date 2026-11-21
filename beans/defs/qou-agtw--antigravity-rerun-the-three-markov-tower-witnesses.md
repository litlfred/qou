---
# qou-agtw
title: 'Antigravity: re-run the three two-row Markov tower witnesses (about 7 h) so they carry q0Anchor'
status: todo
type: task
priority: normal
owner: Antigravity
parent: qou-c20n
created_at: 2026-11-21T07:45:00Z
updated_at: 2026-11-21T07:45:00Z
---

Owner ruling 2026-11-21: work that fails here on time or resource limits goes
to a bean for Antigravity. Found while draining the q0-anchor refill ratchet
(PR #8751).

These three witnesses have no top-level `q0Anchor`, so they stay on the
ratchet. All three are proton-pinned (`Q0_STR` = the 50-digit proton pin):

| witness | producer | last recorded cost |
|---|---|---|
| `computations/probes/markov-trace-two-row-tower-rust.witness.json` | `tools/hecke-engine/src/bin/tower_trace.rs` (`hecke-tower-trace`) | Z=9: 799 s, Z=10: 3511 s, Z=10 (A=21): 9438 s at main dps; check dps about the same again |
| `computations/probes/markov-trace-two-row-tower-colwise.witness.json` | `tools/hecke-engine/src/bin/two_row_tower_trace.rs` | per-isotope JSONs, assembled outside the repo |
| `computations/probes/markov-trace-two-row-tower.witness.json` | `computations/probes/markov_trace_two_row_tower_probe.py` chains, collected by `markov_trace_two_row_tower_collect.py` | chain JSONs are not committed |

Already done in #8751: both Rust binaries now write `q0Anchor` / `q0Value`
(they wrote only snake_case `q0_anchor`); the Python probe and collector
already carry it. `cargo check --features mpfr` passes.

## To do
1. `cargo build --release --features mpfr --bin hecke-tower-trace` and
   re-run with the arguments recorded in the witness (`--compare` against the
   Python reference). Same for `two_row_tower_trace`, then reassemble colwise.
2. Re-run the Python chains and collect into
   `markov-trace-two-row-tower.witness.json`.
3. Confirm every `tr_markov_d` is unchanged against the committed values
   (they are pin-identical; only the stamp should move), then commit.
