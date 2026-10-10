---
# qou-zzwm
title: The C->D excision left published accuracy figures behind — my mass table was the first, not the only
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-30T08:06:31Z
updated_at: 2026-10-10T07:47:10Z
parent: qou-cdx1
---

FOUND while answering the owner's question "investigate 2.4 accuracy loss --
some other related issues?" after adopting the convention-D mass table (#6043).
The answer is YES, and the mass table was the FIRST case, not the only one.

=== WHAT IS ALREADY KNOWN — do not re-report this as a discovery ===

docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md ALREADY says
it, twice and explicitly:
  §3c line 124  "And the whole ladder is convention-C-frame"
  line 132      "conclusion is C-conditional"
  line 183      "Until it lands, the 164x floor is itself C-conditional"
AGENTS.md carries the same ruling (bean qou-cds1: the c_k ladder is C-frame
throughout and has NOT been re-derived under D).

So the C-conditionality of the Q_beta ladder is RECORDED. This bean is not
about that.

=== WHAT IS NEW: the label does not propagate to what publishes the numbers ===

VERIFIED BY ME, not carried from the sub-agent that surfaced it:

1. computations/per-observable-100x-status.witness.json — the L2 dashboard,
   the artifact AGENTS.md tells agents to quote for L2 status — contains ZERO
   occurrences of "convention", "markov", "Markov", "Ocneanu" or "Wenzl"
   (grep -c on each: 0,0,0,0,0). It publishes Q_beta, m_n and Delta_pn with no
   record of which convention produced them.

2. Its upstream DOES carry the label and the warning.
   computations/qbeta/qbeta-ck-cache.witness.json:
       data.markov_convention = 'C'
       data.markov_convention_note = "Convention C (z = sqrt(q)/(1+q)),
         reached only via --historical-convention-C. C was excised by owner
         ruling (2026-08-09, re-affirmed ...)"
       data.Q_beta_tiers.derived.err_ppb_vs_codata = 1278.5825421130362
   1278.58 ppb is the dashboard's Q_beta headline. The label exists one file
   upstream and is dropped at publication.

3. The producer REFUSES TO RUN under the canonical convention.
   computations/qbeta/qbeta_ck_cache.py:112-131
       if convention == "D":
           print(" REFUSING TO RUN -- convention D has no derived c_k ladder")
           ... "not a z-swap" ...
           raise SystemExit(2)
   So the L2 Q_beta figure is not merely stale — it is currently UNREPRODUCIBLE
   under the canonical convention, by the producer's own deliberate guard.
   (The guard is correct and was added on purpose, bean qou-ckwt. The defect is
   that the number it refuses to recompute is still published unlabelled.)

4. Two content blocks that quote C-frame accuracy figures mention "convention"
   ZERO times, and were NOT touched by the D-adoption commit 4691a05b8c
   (which touched 7 files, all mass-table-z1-20*):
     content/.../observations/feynman-qou-comparison.md
       "0.074 % mean, zero fitted parameters" vs SEMF 0.023 %. That 0.074 % is
       the SUPERSEDED convention-C mass table — the one this arc just replaced
       with a 0.1827 % D table. Its Table 2 still carries the pre-adoption
       per-Z values (He-4 0.167 %, Ca 0.094 %; adopted D gives 0.321 % and
       0.238 %).
     content/.../observations/atom-mass-full-hecke.md
       Jones-Markov weights y_hat ~ (0.42, 0.56, 0.02). Under D the third
       (alternating) weight is identically ZERO. A published nonzero
       alternating weight IS a convention-C fingerprint; the block's
       key-observation 2 ("the alternating block is suppressed") describes a
       channel that under D does not exist.
   (docs/precision-goals.md does mention convention 7x — it is better off than
   these two, but it also quotes the 164x/1279 ppb figures.)

=== SCOPE (a), NOT (b) ===
This is "these published figures are C-frame and their consumers do not say
so". It is NOT a claim that any of them is wrong as mathematics, and NOT a
claim that the D values are known — for Q_beta the D value is not computable
today (item 3). Do not write "refuted" anywhere near this.

=== TWO SEPARATE ITEMS I AM NOT FOLDING IN ===
  a) content/.../observations/mass-formula-validation.md publishes a Z=1-20
     table with |Delta/M| < 0.04 % at status "verified", declaring
     computations/q_pinning_50_digit.py as its producer — a script that
     computes q0 and cannot produce a mass table. That is a missing-producer
     defect, not a convention one. Separate bean.
  b) canonical-isotope-witness-Z21..Z99 (98 shards) have computedAt
     2026-08-23T17:15, BEFORE the 2026-08-24 C-excision in the symbolic Hecke
     core, while Z00-Z20 were regenerated 2026-08-24T14:40 AFTER it. A spot
     re-run of Z=26,N=19 gave 120.70 MeV against a recorded 55.088 (factor
     2.19) — which is LARGER than the z-shift alone predicts, so the cause is
     NOT isolated and must not be reported as convention drift. Separate bean.

=== WHAT I DID NOT DO ===
Nothing here is fixed. This arc's PR (#6043) adopts the D mass table and does
not touch any of the above; widening it would have buried a 6-file content
change inside a corpus-wide relabelling. Fixing item 4 is cheap (state the
frame in each block). Item 1-3 is an owner call: either the dashboard records
the frame it inherited, or the Q_beta ladder is re-derived under D — and the
latter is bean qou-cds1, which is open precisely because it is not a z-swap.

METHOD NOTE, carried from the survey: a numeric fingerprint scan over 3230
witnesses (z_C = 0.4993203 vs z_D = 0.6126880) found 244 convention hits and
MISSED qbeta-ck-cache.witness.json entirely — because that witness records its
convention as a STRING LABEL and never writes z numerically. The single most
load-bearing C artifact in the repo was invisible to the value-based detector
and was found by tracing the L2 producer's imports instead. Consistent with
docs/audits/2026-08-15-detector-blindness-taxonomy.md: every detector here is
blind to some spelling. Treat the list above as a LOWER BOUND.



=== THE LABELLING HALF IS DONE (PR #6156) — the ladder half is NOT, by design ===

Owner asked to work this. Split it deliberately: the LABELLING half is
mechanical and unowned, the RE-DERIVATION half has a live owner (qou-cds1), and
AGENTS.md permits research overlap while giving mechanical work ONE owner. So I
took the half that neither waits on the ladder nor duplicates anyone.

DONE — three artifacts, ZERO values changed:

1. per_observable_100x_status.py: added _convention_frame_check, the convention
   sibling of the existing _anchor_layer_check. That function's own docstring
   already states the principle -- "This does NOT regenerate the muon witness
   (a tracked migration). It makes the mismatch loud."
   Before: grep -c on the committed witness = 0 convention / 0 markov / 0
   Markov. After: 7 / 0 / 2. Verified pure labelling: 9 fields added, 0
   removed, 1 prose note extended, ZERO numeric fields changed.

   ONE DELIBERATE ASYMMETRY, and it is the part worth reviewing. The anchor
   check SIZES its error; this one emits induced_error_ppb: null with the
   reason. There the D-frame counterpart exists and the error is a derivative
   away; here qbeta_ck_cache.py raises SystemExit(2) under D, so no D-frame
   counterpart exists and any figure would be MANUFACTURED. Naming a number
   that cannot be computed is the exact failure this check exists to prevent.

2. atom-mass-full-hecke.md: VERIFIED the alternating-weight claim myself rather
   than carrying the survey's word. y_lambda_at(3, q) at the proton pin returns
   [0.5054, 0.2473, 0.0] raw = (0.5054, 0.4946, 0.0000) dimension-weighted.
   y_alt is EXACTLY ZERO under D, not merely small. The block's key observation
   ("the alternating block is suppressed") describes a channel that under D does
   not contribute at all. Both frames now tabulated.

   Note for anyone re-checking: the survey reported (0.5054, 0.4946, 0.0000) and
   I first measured [0.5054, 0.2473, 0.0]. Not a discrepancy -- the std block has
   dimension 2 and 0.2473 x 2 = 0.4946. The block's three values sum to 1, so it
   uses the dimension-weighted convention. Check which you are reading.

3. feynman-qou-comparison.md: headline "achieves 0.074 %" was the SUPERSEDED
   convention-C table. Corrected to 0.183 % (adopted D), which moves the SEMF
   comparison from 3.2x to 7.9x worse -- stated plainly. The
   zero-fitted-parameter claim is UNAFFECTED and now says so explicitly:
   convention D introduces no parameter.

   Table 2 SCOPED, NOT regenerated. Its QOU column is confirmed the same
   superseded table (938.910 for H-1 vs the adopted 935.352; the D producer's
   own shift_from_published_C_MeV reproduces the difference exactly). It
   declares NO `computation` block and the SEMF column has no derivation in the
   corpus, so there is nothing to re-run. Inventing a producer to reproduce the
   published numbers would be manufacturing provenance -- the qou-lvx7 class.

VERIFICATION: both .md render through the folio-assistant pipeline at exit 0
(machine-validated, not a hand grep); both sidecars refreshed via qa-sweep;
gates 8 red, all inherited (raw-float64 is newly ARMED, not newly broken -- it
evaluates only when a witness is touched; this witness carries 0 raw float64
fields before AND after).

NOT DONE, and not mine to do: re-deriving the ladder under D. Bean qou-cds1,
live owner, and the 2026-08-30 bar-weight prune (add3a7304a) established the
obstruction is the OFFSET, not z -- alpha = (z-1)h/2 mixes bar-weight -4 (z_D)
with weight 0 (the constant 1), so it is not a bar-eigenvector and a z-swap is
invalid. Until that lands, Q_beta / m_n / Delta_pn stay unreproducible under
canon and the dashboard now SAYS SO instead of publishing them bare.

COORDINATED: posted findings on #6144 (their 95-field C->D movement profile was
measured against the pre-fix TR_M[5] = z^3 -- the h*z^2+z fix landed 14 min
before their last commit and their branch does not carry it; verified directly)
and on #6058 (their finding 1 landed on main as 064eff1240 / 8a505f2b5a).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

The C->D excision left PUBLISHED ACCURACY FIGURES behind. Live, and confirmed
in kind by today's paper scan: 159 convention mentions over 89 files, 136
explicitly scoped and 23 residual. Scoped figures are the correct disposition;
the live work is the citations that quote them as current.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.
