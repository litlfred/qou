---
# qou-lvx7
title: mass-formula-validation publishes a Z=1-20 accuracy table at status:verified with NO producer that can make it
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T08:08:02Z
updated_at: 2026-10-04T15:11:37Z
parent: qou-9nnz
---

Surfaced by the qou-zzwm survey (owner question: "investigate 2.4 accuracy
loss -- some other related issues?"). Filed separately because it is a
MISSING-PRODUCER defect, not a convention one.

THE CLAIM: folio/quantum-observable-universe/observations/mass-formula-validation.md:41
publishes "all beta-stable nuclei satisfy |Delta/M| < 0.04 %", with a Table 5
spanning 1e-6 .. 0.04 %.

THE PROBLEM: its .ts declares
    script: computations/q_pinning_50_digit.py
    status: "verified"
That script solves for q0 to 50 digits. It cannot produce a mass table, and no
other producer for this block resolves.

WHY IT MATTERS BEYOND BOOKKEEPING: 0.04 % is roughly 5x TIGHTER than the table
this repo just adopted (convention D, mean 0.1827 %, max 0.3214 % over Z=1..20,
PR #6043). Two published accuracy claims about overlapping nuclei differ by 5x
and only one of them has a producer. A reader comparing them has no way to tell
which is current.

NOT ESTABLISHED, do not write it down as if it were: whether the 0.04 % figure
is wrong, whether it is convention-C, or where it came from. It is UNDETERMINED
-- absence of a producer is not evidence about a convention. What IS established
is that status:"verified" is unsupported: nothing in the corpus regenerates it.

HONEST NEXT STEP: either find/write the producer and re-derive the table (then
the status is earned), or downgrade the status and mark the figure as carried
from an unrecoverable prior computation. Do NOT fit a producer to reproduce
0.04 % -- that would be manufacturing provenance for a number whose origin is
unknown, which is worse than the missing producer.


## Addressed in PR #6532 (branch claude/mass-formula-validation-scope-2026-09-03)

Both halves done as the bean specified, and the one thing it forbade was
not done.

**1. False producer attribution removed.** `computation` is OPTIONAL on
`remark` and other observation blocks omit it, so the honest form was to
delete the block rather than downgrade the status of a producer that was
never the producer. Provenance moved to `authorNotes` per §4d, including
the bean's own UNDETERMINED list verbatim: whether 0.04 % is wrong, whether
it is convention-C, and where it came from are all open, and absence of a
producer is not evidence about a convention. The figure is LEFT STANDING.

**No producer written**, per the bean's explicit prohibition.

**2. A second defect, not in the original bean.** `Delta/M` in Table 5
divides by the ATOMIC MASS, which the 2026-08-11 owner ruling (`qou-exam`)
excised as a prediction target — absolute mass is `m_e` x ratio and `m_e`
fixes the MeV scale by fiat. So the table divides a binding-scale residual
by a nucleon-scale mass and the percentage is small for that reason.

Computed from Table 5's own Delta against AME2020 binding:

    4He  +0.079  0.002 %   B 28.296  ->  0.28 %
    6Li  +2.191  0.039 %   B 31.995  ->  6.85 %
    7Li  +1.740  0.027 %   B 39.245  ->  4.43 %
    9Be  +1.234  0.015 %   B 58.165  ->  2.12 %
    10B  +0.648  0.007 %   B 64.751  ->  1.00 %
    12C  +0.618  0.006 %   B 92.162  ->  0.67 %

**6Li — the row the 0.04 % bound is tightest against — is 6.85 % of the
binding it is meant to reproduce. A factor of 176.** This does NOT show the
0.04 % figure is wrong (still undetermined); it shows the bound is a claim
about the denominator as much as about the formula.

**1H is not an accuracy result at all**: free nucleon, no binding energy
(Table 1 says so), so its 1e-6 % is the `m_e` scale returning what was put
in — the same round-trip the per-observable dashboard excludes `m_p` for.

## Verification

Render-QA battery clean; manifest imported under bun (builds, `computation`
absent, 2 authorNotes); `check-sidecars.sh` clean.
**`run-validate.ts` could not run** — `Cannot find module
'.../references-registry-di'`, identical with the changes stashed, so a
pre-existing qou/platform version skew, not this change. Reported as
un-run rather than as green.

---

## Earlier record of the same finding (from PR #6388, 2026-08-31)

Kept alongside the section above rather than replaced: that one records
the finding as ADDRESSED (#6532, merged); this one records it as FOUND,
three days earlier. The two overlap substantially by construction.

## 2026-08-31 — the "5x tighter" is BACKWARDS, and the missing producer is the least of it

Measured with the repo's own AME2020 accessor (`ame_2020_binding_energies._binding_mev_exact`,
Decimal-exact) against table 5's published Delta column:

       iso   |D| MeV       M MeV   |D|/M %     B MeV   |D|/B %
       4He     0.079    3728.401  0.002119    28.296     0.279
       6Li     2.191    5603.051  0.039104    31.994     6.848
       7Li     1.740    6535.367  0.026624    39.245     4.434
       9Be     1.234    8394.794  0.014700    58.164     2.122
       10B     0.648    9325.513  0.006949    64.751     1.001
       12C     0.618   11177.929  0.005529    92.162     0.671
       16O     0.548   14899.169  0.003678   127.619     0.429
      40Ca     0.230   37224.920  0.000618   342.052     0.067
      56Fe     2.605   52103.063  0.005000   492.260     0.529
      238U    13.097  221742.900  0.005906  1801.690     0.727

    convention-D table (PR #6043, Z=1..20): mean 0.1827 %, max 0.3214 %, on BINDING

### (a) The two figures have DIFFERENT DENOMINATORS and are not comparable

This bean recorded "0.04 % is roughly 5x TIGHTER than the table this repo just
adopted". That comparison does not hold: table 5 divides by **absolute atomic
mass**, the D table by **binding**. On the same denominator table 5 runs
**0.067 %–6.848 %** — worse than D everywhere in the light region, and **~37x
worse than D's mean at 6Li**. The 0.04 % is flattery from dividing a
binding-scale error by an m_e-scale baseline.

So the direction of the discrepancy is the opposite of what was filed, and the
question "which of these two is current?" was malformed — they measure
different things.

### (b) It publishes ABSOLUTE MASSES IN MeV as predictions

Table 5 is an `M_QOU` column with error bars for 1H through 238U. The owner
ruling of 2026-08-11 (bean `qou-exam`, AGENTS.md) excised exactly this: the
framework no longer claims, targets or scores absolute nucleon/atomic mass in
MeV as a prediction, because m_e (CAL-1) fixes the MeV scale by fiat and the
number double-counts the calibration. This is a standing-ruling conflict, and
it is larger than the missing-producer defect this bean was filed for.

### (c) The 1H row is an anchor round-trip

`M_obs = 938.783`, `M_QOU = 938.783`, `-0.000001 %`. That is the proton pin
coming back out — the same tautology AGENTS.md corrects for `m_e` and `m_p` in
the L2 dashboard, and the reason the canonical L2 count is 1/5 scoreable rather
than 3/7. It is not a prediction and must not be scored as one.

### RECOMMENDATION: do NOT write the missing producer

A producer reconstructed to reproduce 0.04 % would manufacture provenance for a
figure that should not be published in that form regardless of whether it is
reproducible — which is the failure mode this bean's own "HONEST NEXT STEP"
already warned against, for a different reason.

Instead, one content-only PR:

  1. Drop `status: "verified"` — nothing regenerates it.
  2. Delete the "all beta-stable satisfy |Delta/M| < 0.04 %" sentence, or
     restate it on the binding denominator where it reads 0.28 %–6.85 %.
  3. Re-express or remove table 5's absolute-mass columns per the excision
     ruling. The binding content is already carried, correctly, by the D table.
  4. Mark the 1H row as an anchor round-trip, not a prediction.

Then the producer question dissolves: what is left to produce is a binding
table, and #6043 already produces one.

**NOT DONE HERE.** No content edited; this entry is the measurement and the
recommendation only. Awaiting the owner's word, since (b) touches published
claims across a whole block.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
