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

## CORRECTION (2026-06-28, same day) — NOT env-blocked; the above "not fixable" was WRONG

Owner pushed back ("Clarabel.rs in scope"). Re-diagnosed: the 403 was a git MISROUTING, not an
egress denial. `litlfred/Clarabel.rs` IS reachable via the HTTPS egress proxy (40609); the 403 came
from the global `insteadOf` rewrite forcing github.com through the SCOPED git proxy (41729, qou-only).
Building with a git config that uses the egress proxy WORKS → `pyhecke-native 0.9.0` installs +
imports (trace_weights_n + chi_q_via_gp). Recipe + correction:
`docs/audits/2026-06-28-pyhecke-native-buildable-clarabel-egress-proxy.md`.

Re-scoped b0vf: (1) the canonical lossless `chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json` is
ALREADY 77/77 on main (the bean cites the separate non-`-matrix-m` 22/77 partial). (2) Running the
Rust producer with my fresh 0.9.0 build reproduced 77/77 in 3.4 s but tr_M drifted at 1e-7 from the
committed value (dev-branch engine ≠ canonical engine) — so regen needs the VERSION-MATCHED
pyhecke-native; I reverted rather than commit engine-drifted values. Remaining b0vf work = a
version-matched regen of the partial (data-integrity), no longer a hard block. The ~2.8 h estimate
was also wrong (it was the deprecated pure-Python producer; the Rust producer is ~3 s).

