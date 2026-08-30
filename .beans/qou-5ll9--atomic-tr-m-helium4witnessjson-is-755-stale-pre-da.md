---
# qou-5ll9
title: atomic-tr-m-helium4.witness.json is 7.55% stale — pre-dates the C→D excision
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:25:32Z
updated_at: 2026-08-30T06:26:14Z
---

Found while finishing the pin-straddle fix in `atomic_tr_m_helium4.py`
(PR #6104, bean qou-y313). It is a DIFFERENT and OLDER defect, and the
pin-straddle fix does not touch it — recorded separately so the two are not
conflated.

## Measured

    live producer output   tr_p = 1.1457596924573    tr_n = 0.98774368811581
    committed witness      tr_p = 1.06530622861316   tr_n = 0.92323329718615
                                  ratio 1.0755214 — a 7.55% gap

## Why this is NOT the pin straddle

The muon-vs-proton difference on these same quantities is **78 ppb**
(1.14575978232 vs 1.14575969246). The gap above is **7.55%** — five orders
larger. Fixing which layer gets read moves this by 78 ppb and leaves 7.55%
untouched. Do not report the pin fix as addressing it.

## The witness is THREE-WAY inconsistent

1. it records the **proton** q0 (1.109978582751380807591669),
2. its `source_witness` field names the **muon** file
   (`atomic-tr-m-mpfr-50dps.witness.json`),
3. and its tr_p / tr_n match **neither** committed layer.

Leg 2 is fixed in PR #6104 (the field now reports the file actually read).
Legs 1 and 3 are this bean.

## Dates — consistent with the convention C→D excision, NOT established as it

    witness scriptCommitSha  d27b00274555  2026-06-15
    witness commitSha        85da4f431339  2026-07-07
    convention C→D excision  70d1ade383    2026-08-09  ("176 producer sites")
    upstream input last written                2026-08-29

So the record pre-dates the excision by ~1 month while its upstream input has
been regenerated since. A 7.55% shift is convention-scale rather than
pin-scale, and `docs/audits/2026-08-23-habiro-mass-table-convention-c-attribution.md`
shows the corpus already tracks a convention-C attribution problem in this
area — read that first.

**HYPOTHESIS, not a finding.** The dates and the magnitude are consistent with
"convention-C-era witness never regenerated after D". I have NOT computed the
C-frame value and shown it equals 1.06530622861316. Do that before writing the
attribution anywhere durable.

## Blast radius (9 Python consumers + a reader-facing block)

    computations/tr_m_q_hecke_seminormal.py
    computations/closed_form_tau_M.py
    computations/rho_k_full_via_wenzl_lr.py
    computations/atomic_tr_m_mpfr_50dps.py
    computations/atomic_mass_via_rho_k.py
    computations/atomic_tr_m_helium4_canonical.py
    computations/canonical_tr_m_helium4_stub.py
    computations/probes/nucleon_h3_marshalling_divergence_probe.py
    content/quantum-observable-universe/observations/atom-mass-full-hecke.ts   <-- READER-FACING

The content block is the one that matters for the paper: `atom-mass-full-hecke`
is an observations block, so a 7.55% stale |tr_M| feeding it is not an internal
bookkeeping issue.

## Why I did not just regenerate it

Regenerating inside PR #6104 would silently absorb a convention migration into
a PR scoped to pin straddles, changing numbers whose provenance I have not
established, on a witness with 9 consumers and a reader-facing block
downstream. The honest step is to establish leg 3's cause first.
