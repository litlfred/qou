---
# qou-v6wz
title: 'qbeta-ck-basis-constrained-pslq goes RED on re-run: c3 moves by 972, and the witness is stamped q0-independent while carrying q0_canonical'
status: completed
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T11:46:20Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

FOUND 2026-09-04 as a hook-triggered producer re-run in a working tree, NOT by looking for it. Re-run against main at eb2f4588ce. NOT MY BRANCH'S CHANGE - reverted rather than committed, so this bean is the only record. Reproduce with: run the producer for computations/probes/qbeta-ck-basis-constrained-pslq.witness.json on current main and diff.

THE WITNESS GOES RED. allPassed: true -> false. Its own self-check: computed 1.5835e-30 -> 972.3619589513947 against tolerance 1e-08, passed false.

c3_reproduced_canonical: -2.02018812814143945582 -> -974.382147079536184945.

THE ANCHOR RE-PIN DOES NOT EXPLAIN IT, by a factor of 7.8 MILLION. q0_canonical moved 1.1099785955573347... -> 1.109978595642739... which is the retired pin -> the live CODATA-2022 pin, a 0.0769 ppb move (the qou-3f7a drain, correct and expected). With u^3 = 6.178685604e-7 the amplification gives a c3 shift of 1.245e-04. The observed shift is 972.362. Ratio 7.813e+06. So the migration is a red herring; something else changed.

THE LIKELY CAUSE IS IN THE SAME DIFF: anchor_slope_dc3_dq 4.65741e+6 -> 3.81298e+6. That is exactly the stale-4.66e6 -> corrected-3.84e6 figure AGENTS.md documents at length (the stale-c3 twin; beans qou-3nva / qou-kt8o). So a sibling corrected the slope - correctly - and c3_reproduced, which is computed FROM the slope, was not reconciled. Note the failing check's 'computed' value 972.3619589513947 IS the c3 shift 972.362 to ten digits: the check is measuring exactly this discrepancy.

SECOND DEFECT, INDEPENDENT AND WORSE FOR THE AUDIT SURFACE. The refreshed witness is stamped
    q0Anchor: 'independent'
    q0AnchorReason: 'producer declared q0-independent at the stamp site (q0_anchor=False): no q0-dependent field in this witness'
while the witness plainly carries q0_canonical AND c3_reproduced_canonical, both q0-dependent. The stamp contradicts the file it is on. A q0-dependent witness labelled q0-independent escapes the q0-anchor-flip audit entirely - it will never be reported as a flip no matter which pin it is on. Verify at the producer's stamp site (q0_anchor=False) before fixing; the reason string suggests the flag is hand-set rather than derived from the emitted fields.

UNRELATED AND CORRECT, noted so nobody 'fixes' it: the key rename 'Vol(4_1)=2*Lambda(pi/3)' -> 'Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)' with the VALUE unchanged (2.02988321281930725004240510855) is the Lambda-vs-Cl_2 naming drain (qou-zdz5) landing properly.

WHY THIS IS NOT MINE TO FIX HERE: PR #6584 is the eightfold/hyperbolic-volume arc; this is the c_k ladder producer, a different domain, and the change that broke it came from main. Fixing it would widen the PR and the reviewer is not loaded on that area. Also do NOT make it green by widening the tolerance or re-baselining - AGENTS.md forbids that explicitly; fix at the producer by reconciling c3_reproduced with the corrected slope.

DEFECT 2 FIXED 2026-09-05 (PR #6824, branch claude/fervent-noether-zssd1k). Producer stamp q0_anchor=False -> q0_anchor='ambiguous' (the manifest's own classification for this stem; reads both pins on purpose, pin undetermined). No bare q0Value. Verified clean: not a flip in q0_anchor_consistency_audit, not listed in q0_value_drift_audit. The stale '# no q0 in this producer's cone' comment corrected.

DEFECT 1 STILL OPEN (deferred): the c3_reproduced_canonical ~ -974 RED. cds1-gated c_k-derivation work: a sibling corrected anchor_slope_dc3_dq 4.66e6 -> 3.84e6 (qou-3nva/qou-kt8o) and c3_reproduced (computed FROM the slope) was not reconciled. Fix by reconciling at the producer under the cds1 c_k re-derivation; do NOT widen tolerance/re-baseline. Bean stays open for defect 1.

## 🛑 DEFECT 1 DIAGNOSIS WITHDRAWN 2026-09-14 — it is a CONVENTION mismatch, not an unreconciled slope

The proposed fix above (*'reconcile at the producer'*, *'c3_reproduced computed
FROM the slope'*) would have been wrong work. Two independent reasons.

**1. Structurally, c3 is not computed from the slope.** `ladder_chain(q)` in
computations/probes/qbeta_ck_basis_constrained_pslq.py takes q ALONE:

    z        = q**3 / (q**2 + 1)          # line ~119
    alpha    = (z - 1) * h / 2
    b        = sqrt(d1*d2 + 1);  hbar_q = (q-1)/q;  u = b*hbar_q**2
    Q_N1     = Q_A * cos(alpha - b*hbar_q**2/2)
    Q_N2     = Q_N1 * (1 - u**2)
    c3       = (Q_BETA_CODATA_MEV / Q_N2 - 1) / u**3

`anchor_slope_dc3_dq` is an independent OUTPUT field. There is no
reconciliation operation to perform. The slope correction 4.66e6 -> 3.81e6 is
real, correct, and in the same diff — a coincidence of timing, not a cause. The
bean's own arithmetic already says the slope-explainable shift is 1.245e-04
against an observed 972.362.

**2. The actual cause: the producer is convention D, the constant it checks
against is convention C.**

    line ~119   z = q**3 / (q**2 + 1)                        <- convention D
    line  110   C3_EMP_CACHE = -2.02018812814143945582...    <- the ck-cache,
                                                                convention C

So the self-check compares a D-frame computation against a C-frame cached
constant, and the 972.362 discrepancy IS the C->D extraction shift.

**Corroborated independently, to every printed digit.**
computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json
(on main since 2026-09-05, 10/10 PASS, 60 dps) reports

    result.c3.D_muon                      = -974.3821470795362
    this producer's c3_reproduced_canonical = -974.382147079536184945277477315

and its `extraction_shift_D_minus_C.muon = -972.362286768` against this
witness's failing `computed = 972.3619589513947` (they differ at the 7th digit
because the two runs sit at different pins; the 16-digit c3 match is the
decisive one).

**Correction to the bean's history too:** the witness has been RED in BOTH of
its committed revisions on main (638f298ffb and 41ac6e9804, both 2026-09-05).
`git log -L` on the z line shows it arrived already reading q**3/(q**2+1) —
there is no C->D flip in this file's main history. The green version described
above existed only pre-merge.

## THE FRAMING INVERTS: this RED is the gate working, not a regression

The producer is on the CANONICAL convention. What it is reporting is that the
C-frame cached c_3 is **not reproducible under convention D** — which is exactly
bean qou-cds1, surfacing through a self-check. Going green requires the D-frame
c_k ladder, blocked on the N=1 eigenphase alpha (qou-pdix), NOT a fix here.

This is the compute-side manifestation of the D2 scope finding recorded in
qou-cds1 the same day (PR #7343): **one phase to derive, five values to
re-extract.** This witness is the five-values half, made visible.

## Done here

Labelled C3_EMP_CACHE at the site with its frame, why the check is RED by
construction, the corroborating witness, and both 'do NOT' rules (no
reconciliation; no tolerance widening / re-baselining). Comment-only —
producer re-run, exit 0, **payload byte-identical** under a volatile-key mask,
allPassed still False (the honest state), no sibling witness touched; scriptHash
08bad77e0fbb-era -> bf5cbed1eeff refreshed so the witness is not self-stale.

**Bean stays OPEN.** Defect 1 is real; only its diagnosis was wrong. It is now
correctly parented to the cds1/pdix blocker rather than to a slope
reconciliation.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** All actionable work is landed. The remaining RED is qou-cds1 surfacing (a C-frame constant vs a hybrid-D producer), not a separate defect. Close and point to cds1. The "-974" it reproduces is a retired-base hybrid, not a D value.

Evidence: Defect 2 was fixed in PR #6824: the witness has `q0Anchor: "ambiguous"`. Defect 1 was re-diagnosed as a D producer vs a C constant and labelled at `computations/probes/qbeta_ck_basis_constrained_pslq.py:110-116`. The witness has `allPassed: false` (honest) and `c3_reproduced_canonical` -974.382147…, which equals the sensitivity witness `D_muon` -974.3821470795362.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
