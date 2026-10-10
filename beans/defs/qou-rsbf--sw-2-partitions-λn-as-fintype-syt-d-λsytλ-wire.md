---
# qou-rsbf
title: 'SW-2: partitions λ⊢n as Fintype + SYT + d_λ=#SYT(λ); wire Mathlib YoungDiagram/Tableau'
status: completed
type: task
priority: normal
created_at: 2026-08-02T19:30:46Z
updated_at: 2026-08-19T13:38:48Z
parent: qou-59vq
---

Foundational, no deps. Mathlib has Combinatorics.Young.YoungDiagram and SemistandardYoungTableau; check for StandardYoungTableau + a Fintype/count. Deliver: partitions of n as a Fintype, d_λ:=#SYT(λ) as a computable Nat. Ref: [macdonald1995].

## ✅ LANDED (2026-08-02, background agent) — sorry-free, verified

[`QOU/SchurWeyl/YoungTableaux.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/lean/QOU/SchurWeyl/YoungTableaux.lean)
(EXIT=0, sorry-free, independently re-verified by lean-direct). Key finding:
the repo ALREADY has an SYT stack under `QOU.Mathlib`
(`StandardYoungTableau`, `numStandardYoungTableaux`, `dimSYT`, hook-length
bridge, Schensted insertion stack). This bean = reuse + a `Fintype`
upgrade:
- `Partition n` + `instFintypePartition` (Mathlib `Nat.Partition` Fintype).
- `numSYT`, `dLambda := #SYT(λ)` as `Fintype.card` (via `Fintype.ofFinite`),
  proved equal to the pre-existing `Nat.card` count.
- `sum_dLambda_sq_eq_iff` restates the SW-3 target with `dLambda`.

**SW-3 impact:** `QOU.Mathlib.rskBurnsideHolds_le12` already proves
`Σ_{λ⊢n} dimSYT² = n!` for **n ≤ 12** by `decide`; a Schensted stack exists;
general RSK is the only missing piece. RSK is NOT in Mathlib v4.24.0.
Updating SW-3 accordingly. Wired into QOU.lean.


## VERIFIED CLOSED (2026-08-19 measurement)

`YoungTableaux.lean` sorry-free on main; `dLambda` = Fintype.card (SYT lam) is
the indexing used by `seminormalRepFin` and by the merged JM block eigenvalue
(#5290), so it is load-bearing, not shelf-ware. Status was stale at todo.
