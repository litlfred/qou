---
# qou-zzwm
title: The C->D excision left published accuracy figures behind — my mass table was the first, not the only
status: todo
type: task
priority: normal
created_at: 2026-08-30T08:06:31Z
updated_at: 2026-08-30T08:07:30Z
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
