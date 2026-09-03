---
# qou-b3l8
title: sublemma-2-1-alpha-shift-extract is a muon-era witness whose only regeneration path drops its provenance block
status: todo
type: bug
priority: normal
created_at: 2026-08-23T13:22:16Z
updated_at: 2026-08-29T00:15:13Z
---

Two independent defects on one witness, neither caused by #5517 — measured with
that PR's branch point and head both giving the same answer.

**1. The committed witness is muon-pinned; the producer is proton-pinned.**

    committed  parameters.q_0 = 1.1099785955541805   (muon)
    fresh      parameters.q_0 = 1.1099785827513808   (proton, q_parameter.Q)
                                        rel = 1.153e-8  (11.53 ppb)

`sublemma_2_1_alpha_shift_extract.py` reads `from q_parameter import Q as Q0`,
so any regeneration silently re-pins it. The observable moves with it:
`alpha_shift.value_re` committed -> fresh is **1.745e-7**, and it is the same
1.745e-7 whether the producer runs at #5517's branch point or at its head. So
the move is the 2026-05-28 re-pin, not the symbolic rep.

**2. Regenerating it drops four provenance fields.** The committed witness
carries `scriptFile`, `commitSha`, `engine`, `auditOnly`; a fresh run emits
none of them. This is the bare-producer class AGENTS.md warns about — re-running
DELETES the fields an audit keys on. Fix the producer to emit provenance BEFORE
anyone regenerates this witness.

**Do not fold either into #5517.** #5517's own effect on this witness is
7.34e-14 on `value_re` — and this producer is float64 throughout
(`chi_lambda_fast`, not the `_mp` variant), so at its own resolution that is
round-off, not an accuracy claim in either direction.


---

## 2026-08-28 — §2's cause is retired; a SECOND, larger drift is now live (PR #5923)

Found while sweeping hand-rolled producers for `1j39`. Both defects this bean
records for `sublemma-2-1-alpha-shift-extract` have moved on:

**1. The muon -> proton re-pin (§2's 1.745e-7) HAS HAPPENED.** The committed
witness's `parameters.q_0` now reads the proton pin
`1.10997858275138080759…`, so that particular regeneration hazard is spent.

**2. A different, ~400x larger drift replaced it: 7.19e-5.** A fresh run moves
92 lines — `value_re` in the 4th significant digit (1.00544843… ->
1.00552033…), `max_relative_residual` 25.3556 -> 25.5245. The cause is the
**float64 -> mpmath port**, and the committed values are the OLD ones:

    witness computedAt   2026-08-24T08:06:59
    253e2ffaf5 landed    2026-08-24T08:10:43     <- 3 min 44 s later

`253e2ffaf5` swapped `chi_lambda_fast` -> `chi_lambda_fast_mp` and `Q` (float)
-> `Q_MP` (mpf). So this is the same *"stamped minutes before the commit that
superseded it"* signature as §0 of the PR-5517 audit, and the drift is a
**correction** — the fresh values are the better ones.

**Note for anyone re-reading §2:** it is correct as written and about the right
file, but quoting its 1.745e-7 / muon-re-pin explanation for what a re-run does
*today* would be a confident wrong attribution. Two different causes, five days
apart, in one witness.

**3. Provenance-stripping: FIXED.** §2's second defect (*"a fresh run drops
`scriptFile`, `commitSha`, `engine`, `auditOnly`"*) is closed for the three
fields a producer can own — it now emits `scriptFile` / `engine` /
`auditOnly` itself, so a re-run no longer deletes them. Its `auditOnly` was
also **dangling**: the target had moved to `docs/audits/_deprecated/` and the
witness still named the pre-move path. `commitSha` is deliberately still not
emitted, per `qou-4un2`'s reasoning.

**What is left for this bean:** the regeneration itself. It is now justified as
a correction rather than deferred as a risk — but it must be its own deliberate
commit, not folded into a provenance change. #5923 leaves the witness
byte-identical for exactly that reason.
