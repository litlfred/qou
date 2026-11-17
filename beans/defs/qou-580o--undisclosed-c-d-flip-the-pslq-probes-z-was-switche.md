---
# qou-580o
title: 'UNDISCLOSED C->D FLIP: the PSLQ probe''s z was switched to convention D inside a Lambda-Cl2 naming commit, and its witness was never regenerated'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-18T08:21:15Z
updated_at: 2026-11-17T08:14:00Z
parent: qou-cdx1
---

## Found by re-running, not by reading (2026-08-18, while draining qou-zdz5)

I renamed one mislabelled dict key in
computations/probes/qbeta_ck_basis_constrained_pslq.py and re-ran the producer
to regenerate its witness.  A key rename cannot move a number.  The re-run
moved this:

  c3_reproduced_canonical   committed  -2.02018812814143945582016855395
                            re-run     -974.382476607697851630950275826
  assertion 'passed'        committed  true
                            re-run     FALSE  (allPassed true -> false)

-974.38 is EXACTLY the registry §9g convention-D muon c_3.

## Cause: the probe's z was flipped C -> D, in a naming-drain commit

  90140791d 2026-08-10  z = 1 / (mp.sqrt(q) + 1/mp.sqrt(q))     <- convention C
  98e78d396 2026-08-15  z = q**3 / (q**2 + 1)                   <- convention D

98e78d396 is titled 'fix(vol-4_1): 9 Lambda<->Cl2 sites -- this does NOT
complete the drain'.  A CONVENTION CHANGE rode inside a NAMING commit, and the
witness was not regenerated.  The committed witness has been C-frame, and
passing, ever since; the failure only appears if you actually re-run.

Note the pre-flip spelling: 1/(sqrt(q) + 1/sqrt(q)) IS sqrt(q)/(q+1) exactly.
That is one of the DETECTOR-BLIND C spellings AGENTS.md warns about, and it is
why convention-c-producer-audit.py's '0 actionable producers' does not mean the
C surface is clear.  Live example of the documented blind spot.

## What I did NOT do, deliberately

I did NOT commit the regenerated witness.  Committing it would:
  (a) RATIFY an undisclosed convention flip that no ruling authorised for this
      probe, and
  (b) wire c_3 = -974 into the corpus -- which qou-cds1 states explicitly is
      'a sensitivity measurement, not a proposed value.  Do not wire it
      anywhere.'
I also did NOT revert the z line to C: the owner ruling makes D canonical, so
silently reverting would be its own unilateral convention decision.

So the witness stays stale AND is now documented as stale.  That is the honest
intermediate state; ratifying either frame is the thing to avoid.

## What resolution requires (belongs with qou-cds1)

The ladder must be RE-DERIVED under D, not re-evaluated -- proved by
QOU.QBeta.decayLadder_zC_threeRow_ne_zero.  This probe currently does exactly
the forbidden thing: it substitutes z_D into the C-frame functional form
alpha = (z-1)h/2.  That is why it returns -974 rather than anything meaningful.
Fixing the witness is downstream of deriving the D-frame phase.

## Kept from the same pass (real naming fixes, no numbers touched)

  docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md:18
    Vol(4_1) = 2\Lambda(\pi/3) -> 2\,\mathrm{Cl}_2(\pi/3) = 6\Lambda(\pi/3)
    (the value 2.02988 was already correct -- wrong NAME, right NUMBER)
  qbeta_ck_basis_constrained_pslq.py:313  dict key
    'Vol(4_1)=2*Lambda(pi/3)' -> 'Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)'
    (vol41 = 2*Im Li_2(e^{i pi/3}) = 2*Cl_2(pi/3), computed correctly)


# ================= RETRACTION (2026-08-18, same day) =================
# THE TITLE OF THIS BEAN IS WRONG.  There was no undisclosed flip, and
# 98e78d396 is innocent.  Read this section, not the one above.

## What I got wrong, and how

I claimed commit 98e78d396 ('fix(vol-4_1): 9 Lambda<->Cl2 sites') silently
flipped this probe's z from C to D while claiming to be comment-only.  That is
FALSE.  Its actual diff on this file is ONE docstring line (41), and its
commit message's claim -- 'All comment- or docstring-level; the code beside
them is correct, so no output changes' -- is TRUE.

My method was the bug.  I used:

    git log -L 93,93:computations/probes/qbeta_ck_basis_constrained_pslq.py

'-L' maps the CURRENT line range onto older revisions.  Line numbering had
shifted, so it reported the last commit touching a DIFFERENT line as though it
had touched the z line.  I then read a genuine C-vs-D difference between two
commits and attributed it to the nearest plausible commit without ever
diffing that commit.  One 'git show <sha> -- <path>' would have caught it.

'git log -- <path>' also misled me a second way: history simplification hid
the real change across a merge, so the per-commit walk showed D at every
commit and I briefly concluded there had been no flip at all.  Only
'git log --full-history' shows the truth.

## What actually happened

  08-02 .. 08-10 02:21   z = 1/(mp.sqrt(q) + 1/mp.sqrt(q))     convention C
  08-10 03:44 63db38885  z = q**3/(q**2 + 1)                   convention D
  08-10 05:23 a135537ed  Merge #4899: 'excise convention C from the producer
                          layer -- 178 sites -> 0, witnesses regenerated'

The flip is REAL, dated 2026-08-10, and it is AUTHORISED AND DISCLOSED: it is
part of the owner-ruled convention-C excision campaign (#4899), consistent
with the rulings making D canonical.  Not undisclosed.  Not smuggled.  Not in
a naming commit.

## The finding that SURVIVES, correctly scoped

#4899's own summary says 'witnesses regenerated across 68 producers'.
THIS WITNESS WAS NOT AMONG THEM.  Its c3_reproduced_canonical is
-2.020188128141439455820168553 at EVERY commit in its history -- the pre-flip
C value -- while its producer has computed D since 08-10.

So: an authorised migration regenerated 68 witnesses and missed this one.  The
committed witness has been C-frame and passing ever since; the mismatch is
invisible until someone re-runs, which is how it survived.  That is a real
gap, and it is a narrow one -- an omission in an otherwise careful migration,
NOT a concealed convention change.

## What this does NOT change

The measurement stands: re-running gives c_3 = -974.382476607697851630950275826
and flips allPassed to false.  And I still should not commit that witness,
for the ORIGINAL reason and one better one:

  - qou-cds1 forbids wiring -974 ('a sensitivity measurement, not a proposed
    value'), and
  - per qou-cds1's own measurement (2026-08-18), -974 is 1/u^3 amplification
    of a 0.06% cos difference -- so regenerating would bake an amplifier
    reading into the corpus as if it were a result.

The right fix is the one #4899 intended: regenerate this witness as part of
resolving cds1, once the D-frame ladder is re-derived rather than
re-substituted.

## Scope of the retraction

Retracted wherever I published it: PR #5265 body, commit 70b10900e's message,
and the qou-zdz5 note.  The zdz5 naming fixes themselves are unaffected --
they were correct and remain correct.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-18 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

An undisclosed C->D flip inside a Lambda/Cl2-named key rename, where a rename
that cannot move a number moved one. Live: the defect is an unrecorded
provenance change, not a surviving C binding.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10: the "falsely passing" state is GONE — somebody regenerated it, and the bean never recorded that

Measured on `main` `8fadf3a6d6`. The honest-intermediate state this bean
describes — *"the witness stays stale AND is now documented as stale"*, with a
C-frame value and `allPassed: true` — **no longer exists.**
`computations/probes/qbeta-ck-basis-constrained-pslq.witness.json` was
regenerated **2026-09-15**, a month after this bean, and now reads:

| field | the bean's "committed" | on `main` today |
|---|---|---|
| `c3_reproduced_canonical` | `-2.02018812814143945582016855395` | **`-974.382147079536184945277477315`** |
| `allPassed` | `true` | **`false`** |

So the D-frame value is recorded and the assertion fails honestly. **Nothing
was ratified** — `verdict.conclusion` is still `ENTROPY-BLOCKED`, Stage 2 PSLQ
was not run, and `-974` is not wired anywhere. That is the state this bean
wanted; it simply arrived from elsewhere and was never written down here.

### What WAS still live, and is now fixed at the producer

Two labelling defects, both on the one artifact where the frame *is* the entire
content:

**1. No convention stamp at all.** `markov_convention` was **absent** from a
witness whose recorded number is, per registry §9g, the convention-**D** muon
`c_3`, and whose entire history is an undisclosed C→D flip. That is the
`qou-ng7j` coverage gap (1.3 % of witnesses carry the field) biting exactly
where it costs most. Now stamped `"D"` with a separate
`markov_convention_reason`, matching the `q0Anchor` / `q0AnchorReason` shape the
same module already uses — and the reason says in words that `-974.38` is
`qou-cds1`'s *sensitivity measurement*, **not** a proposed `c_3`.

**2. The failing assertion named the wrong axis.** Its `source` read *"same
chain + same Q_codata + same q0 as `qbeta-ck-cache.witness.json`"* — three axes
of sameness, while the mismatch that makes it fail is on a **fourth it did not
mention**: the Markov convention. So the failure read as a defect in the
extraction chain when it is two artifacts in different frames. Verified
directly: this probe binds `z = q**3/(q**2+1)` (D) while
`qbeta-ck-cache.witness.json` declares `markov_convention: "C"` and its `c_3` is
reachable only via `--historical-convention-C`. The `source` now says so, and
says the assertion is **left FAILING on purpose** — silencing it would ratify
one frame, which is this bean's whole point.

**Re-run, masking provenance: 3 non-provenance fields moved and ZERO are
numeric.** `-974.382147079536184945277477315` reproduces byte-identically and
`allPassed` stays `false`. The changes are the two new stamp fields and the
corrected `source` prose — a label, not a number.

### A 3.38e-7 discrepancy I could not account for, and an exclusion I will NOT claim

The bean's 2026-08-18 re-run gave `-974.382476607697851630950275826`; the
committed 2026-09-15 value is `-974.382147079536184945277477315`. That is
`3.295e-4` absolute, **`3.38e-7` relative** — far above any rounding.

The obvious suspect is the muon CODATA re-pin (`fca08de7d2`, ruling
2026-08-22), which lands **between** the two runs, and this probe does derive
its pin live (`Q0_CANONICAL = q_muon_at(50)`), so it flowed through. Measured:
the pin moved `0.0798 ppb` on `q₀` and `1.454e-9` on `u`, so the `1/u³`
prefactor in `c_3 = (Q_codata/Q_N2 − 1)/u³` scales `c_3` by only
**`-4.36e-9`** — **77.6× too small** to explain the move.

🛑 **That is not an exclusion, and I am stating the limit rather than the
headline.** I tested the `1/u³` **prefactor only**. The numerator
`(Q_codata/Q_N2 − 1)` is a near-cancellation of two almost-equal quantities and
can carry far more `q₀` sensitivity than the prefactor does, so the re-pin
remains a live candidate — what is established is only that the *amplification
route* does not account for it. Cause **undetermined**; settling it needs the
full chain differentiated at both pins, which I did not do.

### Status

**Re-scoped, not closed.** The undisclosed-flip defect is recorded and the
artifact now states its own frame; what stays open is the `3.38e-7`
discrepancy above and, upstream of everything here, `qou-cds1`'s re-derivation
of the ladder under D. Neither is a labelling job.

## 2026-11-15 — 50-dps resolution of the `3.38e-7` shift: 100% explained to all 30 printed digits by `fca08de7d2`

Evaluated the full extraction chain `ladder_chain(q)` in
`computations/probes/qbeta_ck_basis_constrained_pslq.py` (`mp.mp.dps = 60`,
`c_3 = (Q_BETA_CODATA_MEV / Q_N2(q) − 1) / u(q)³` under convention D,
`z = q³/(q² + 1)`) at both the **pre-`fca08de7d2` retired self-certified muon
pin A** (`q_mu_old`) and the **post-`fca08de7d2` live CODATA-2022 muon pin**
(`q_mu_new = q_muon_at(50)`):

| quantity | pre-`fca08de7d2` muon pin (`q_mu_old`, 2026-08-18 run) | post-`fca08de7d2` CODATA-2022 muon pin (`q_mu_new`, 2026-09-15 witness) | difference / ratio |
|---|---|---|---|
| `q₀` (50 dps) | `1.1099785955573347198997632204832250266562084087801` | `1.1099785956427390466817951293800017527000655610290` | `Δq/q = +7.6942318639171e-11` (`+0.07694 ppb`) |
| `c3_reproduced_canonical` (computed) | `-974.38247660769785163095027582608578` | `-974.38214707953618494527747731514523` | `Δc₃ = +0.0003295281616666856728` (`-3.38191797962064e-7` rel) |
| bean / witness recorded (30 dps) | `-974.382476607697851630950275826` (bean 2026-08-18) | `-974.382147079536184945277477315` (`main` witness) | **0 residual across all 30 printed digits on both** |
| denominator `u³` shift | — | — | `Δ(u³)/u³ = +4.20555490308842e-9` |
| numerator `(Q_codata/Q_N2 − 1)` shift | — | — | `Δnum/num = -3.33986244481259e-7` (**79.4× larger than `u³` shift**) |
| chain derivative `dc₃/dq` | — | — | `+3.85844809136783e6` |

**Conclusion.** The `3.3819e-7` relative (`+3.29528e-4` absolute) discrepancy is
**100% accounted for, to all 30 printed digits**, by the `fca08de7d2` muon
CODATA-2022 re-pin (`+0.07694 ppb` on `q₀`), driven by the near-cancellation in
the numerator `Q_codata/Q_N2(q₀) − 1 ≈ −6.0176e-4` (`dc₃/dq = +3.85845e6`).
Bean remains `todo`, blocked upstream on `qou-cds1` / `qou-wxhi` for the
convention-D `c_k` ladder derivation.

## Implementation & Witness Progress (PR #8273)
- Branch: `qou-10v9-34oo-43v0-580o-5ovu-5pgl` (`f56a97d3d6ca66bf63033f62ab41236e038a488a`), PR: `litlfred/qou#8273`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/probe2_shortfall_frame_chi_cache_clobber_pslq_detector_spelling_stage2_cache_guard_and_borromean_literal_probe.py` -> `computations/probes/probe2-shortfall-frame-chi-cache-clobber-pslq-detector-spelling-stage2-cache-guard-and-borromean-literal.witness.json` (`allPassed: true`, `scriptCommitSha: e98d91d4e01bb7197ccdfc0c0a05bab481cf2839`)
