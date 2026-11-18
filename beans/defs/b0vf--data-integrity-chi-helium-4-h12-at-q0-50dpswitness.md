---
# b0vf
title: 'Data-integrity: chi-helium-4-h12-at-q0-50dps.witness.json only 17/77 complete (22%) — needs He4 H12 chi producer re-run'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-28T06:38:41Z
updated_at: 2026-10-04T15:18:35Z
parent: qou-5vkl
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

## ROOT CAUSE of the 1e-7 drift (2026-06-29) — q₀ PIN, not the engine (corrects "dev-engine≠canonical")

Chased it fully. NOT a pyhecke-native version issue: both engine builds (clarabel-default AND
`--no-default-features`) give the SAME `tr_M=0.885616920128525`; they differ from the committed witness
ONLY via q₀: committed `q_0_50dps=1.1099785827513808…` vs current `Q_50_DIGIT_STR=1.1099785955573347…`
(muon). Δq₀≈1.3e-8 = the muon↔proton ~11.5 ppb spread; χ(q₀) amplifies it to ~1e-7 (all 77 chi differ,
all 77 y_lambda identical). So the engine is canonical + consistent; the He4 χ cache is a
**q₀-convention witness refresh** (tnjb/z5vu owner-gated class), NOT engine-blocked. Do NOT regen this
one witness to the other pin in isolation (silent-q₀-flip hazard). No regen committed; tree clean.
Audit: `docs/audits/2026-06-29-b0vf-chi-drift-is-q0-pin-not-engine.md`.

## SCALAR already solved via markov-peel (2026-06-29) — re-scope: per-partition is the only open need

Cross-checked the partial against the **independent markov-peel** method (Hecke NF + trace, no
per-partition seminormal matrices). markov-peel He-4 `tr_M = 0.055358426266783106…` is **complete**,
at the **same muon pin** (`…955573347`) as the 27/77 partial, in **96.8 s** — already on main
(`markov/markov-peel-atomic-tr-m.witness.json`). The 27/77 χ-sum `0.055414100…` is the same observable
at the same pin but incomplete: gap = **5.567e-5 (0.1006 %)** = the net of the 50 missing (≥3-row)
partitions. So:
- **Scalar tr_M(He-4):** DONE — use markov-peel `0.055358426…`. The χ-sum producer (full Hoefsmit
  dim≈5600 mpmath matrices/partition at 50 dps; one partition `[6,3,2,1]` took 12.2 h) is NOT needed
  for the scalar; completing it is multi-week, infeasible in-sandbox.
- **Per-partition χ_λ(He-4)** is the ONLY thing the χ-sum adds (Δ_λ decomposition). A complete 77/77
  table exists in the `-matrix-m` sibling but at the retired-proton pin → cross-pin merge is the
  owner-gated q₀ migration (tnjb/z5vu), not in scope.
- The dominance probe's "tail ≤ 5.3e-52" is **circular** (reported_tr_M = cached_sum); the real tail is
  5.6e-5, established by markov-peel.

Partial witness flagged known-incomplete (benign note field; no numeric/q₀ change). No regen; tree clean.
Audit: `docs/audits/2026-06-29-b0vf-markov-peel-crosscheck-he4-scalar.md`.
