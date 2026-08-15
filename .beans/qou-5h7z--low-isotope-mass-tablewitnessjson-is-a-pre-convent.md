---
# qou-5h7z
title: low-isotope-mass-table.witness.json is a pre-convention-D artifact (3 rows), needs regeneration where pyhecke_native exists
status: todo
type: task
priority: normal
created_at: 2026-08-15T20:37:31Z
updated_at: 2026-08-15T20:37:33Z
---

Found by the qou-gscs re-audit witness sweep (16 rows across the corpus carry a recorded braid word for a Z>=1,N>=1 atom; 3 were collapsed, all in this one file).

## Two defects, one file

1. COLLAPSED CTYPES. braid_word_canonical records the p-n interface as the colour-blind 'averaged':
     Z=1 N=1  averaged 5  (truth: averaged 4 + averaged_weighted 1)
     Z=1 N=2  averaged 7  (truth: averaged 6 + averaged_weighted 1)
     Z=2 N=1  averaged 7  (truth: averaged 6 + averaged_weighted 1)
   Same defect as the cmte witness (#5042) and the d-chain recipe literal (#5029), in a third medium.

2. PRE-CONVENTION-D tr_M. The bigger one, and it is not visible from the labels. Regenerating moves the multi-nucleon rows by exactly the known C->D deltas:
     2H   0.38828647 -> 0.57509096
     3H   0.10407107 -> 0.22931015
     3He  0.20657848 -> 0.40376714
   Those are the SAME values the qou-mass shard moved through when it was migrated (0.38829->0.57509 etc.), so this witness is a third pre-migration artifact. computedAt 2026-08-09, which predates #4928.

## Why I did NOT commit the regeneration

The p and n rows changed too, and for a different reason: chi_cache_witness moved from 'computed live via laurent_q_rust' to 'laurent_q (auto-fallback)' because pyhecke_native is not built in this sandbox. B_AME_MeV and the err columns shift at ~1e-9 MeV. That is a METHOD SUBSTITUTION caused by my environment, not a correction I derived, and writing it into a canonical witness is the same trap as committing the sandbox-skewed q0 audit witnesses -- which I reverted earlier in this arc for exactly this reason.

Committing the file wholesale would smuggle two sandbox-computed rows in alongside three genuine convention fixes, and a witness cannot be partially written without hand-editing, which the precision discipline forbids.

## To close

Re-run $ /usr/local/bin/python3 -u /home/user/qou/computations/canonical_mass_table_extended.py --atoms p,n,D,T,3He --method auto --target-dps 11
==========================================================================================
  Canonical mass table — method=auto (precision=f64 if Rust)
==========================================================================================

  q_0 = 1.1099785955573347
  Method: auto (Rust dps=50; markov_peel uses symbolic-q)
  COMPUTE_DPS / OUTPUT_DPS / target_dps = 70 / 60 / 11
  Paper hard floor: 780.0 ppb (~6.1 dps; CAL-2 propagation)
  Active-set pruning at target_dps=11: SAFE (within paper bound)

  atom    A   n |tr_M(q_0)|            B_pred(existing)      B_AME origin                 method        wall(s)
  --------------------------------------------------------------------------------------------------------------------------
  p       1   3 1.14575978228784               938.2721   938.2721 canonical_mass facad   laurent_q (auto-fallback: laurent_q_rust unavailable)      0.0
  n       1   3 0.987743756687661              939.5654   939.5654 canonical_mass facad   laurent_q (auto-fallback: laurent_q_rust unavailable)      0.0
  D       2   6 0.575090958682447                2.2488     2.2246 hyp: census-assigned   branching         0.1
  T       3   9 0.229310147182827                8.4686     8.4818 hyp: census-assigned   branching         0.0
  3He     3   9 0.403767138483831                7.4889     7.7180 hyp: census-assigned   branching         0.0
✓ Witness: canonical-mass-table-extended.witness.json  (0 assertions, all passed)

  Witness: canonical-mass-table-extended.witness.json
  canonical finished in 0.9s (rc=0)
✓ Witness: low-isotope-mass-table.witness.json  (0 assertions, all passed)

  Wrote low-isotope-mass-table.witness.json (5 atoms) in an environment WITH pyhecke_native built, so p and n keep the laurent_q_rust route. Expect: 3 multi-nucleon rows move C->D and gain averaged_weighted 1; p and n unchanged. Verify chi_cache_witness still reads laurent_q_rust before committing.

Worth checking at the same time whether any OTHER witness carries pre-D tr_M without a recorded braid word -- the sweep that found this keys on braid_word_canonical, so a witness holding only tr_M would not have been caught.
