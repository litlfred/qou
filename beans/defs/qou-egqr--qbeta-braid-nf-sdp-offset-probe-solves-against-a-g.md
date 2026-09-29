---
# qou-egqr
title: qbeta_braid_nf_sdp_offset_probe solves against a Gram that is singular under convention D
status: todo
type: task
created_at: 2026-08-16T11:29:16Z
updated_at: 2026-08-16T11:29:16Z
---

Parent: qou-cdx1. Split out of qou-cds2, which migrated pyhecke's mpmath path to
convention D and exposed this as the one real downstream consequence.

## The measurement

`computations/probes/qbeta_braid_nf_sdp_offset_probe.py` asserts
`G1_solve_consistent`: that `G x* = nf` holds to `1e-40`, solving against the
50-dps Gram from `gram.gram_matrix_mp()`.

Under convention C, G was invertible on the full NF basis and the probe met that
bound. Under D the Markov-Gram form on that basis is **singular** — corank 1 —
and the residuals become:

    muon (4_1)     2.127e-10
    proton (B_3)   1.313e-10

The solve did not fail. It **lost thirty orders of magnitude of precision**,
which is the fingerprint of the null direction, and the 1e-40 gate correctly
catches it. The probe exits 1 and says so.

## The repair is named, and it is the one the float64 side already took

Quotient by the radical — `QOU/QBeta/GramSignature.lean`. The float64 path did
exactly this in `6086572c4`: `G_INV` was deleted rather than renamed, and the
inverse is now taken on `H_3/rad`.

## Why it was NOT done in qou-cds2

Moving the probe from solving on the full NF basis to solving on `H_3/rad`
changes what it measures: `x*` is unique only modulo the radical, so the
"offset from the symmetric point" the probe reports becomes an offset in the
quotient. That is a decision about what the probe means, not a library
migration, and folding it into one would have hidden a science change inside a
convention change.

## State

Its witness is committed WITH the failure recorded. That is deliberate: a
witness claiming 1e-40 consistency the code no longer produces would be the
stale-artifact defect (detector-blindness taxonomy row 10). The red is honest
and should stay until the quotient repair lands.

Note the probe's own docstring already anticipated the precision it was relying
on: "the float64 version of this gate could only ask for 1e-6". At 1e-6 this
failure would have been invisible.
