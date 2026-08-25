---
# qou-b3l8
title: sublemma-2-1-alpha-shift-extract is a muon-era witness whose only regeneration path drops its provenance block
status: todo
type: bug
created_at: 2026-08-23T13:22:16Z
updated_at: 2026-08-23T13:22:16Z
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
