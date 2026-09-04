---
# qou-9ugp
title: 'GAP: retired muon pin literal 1.10997859555733471 still hardcoded in ~180 computations/ producers outside the alpha cluster — all unstamped, invisible to the qou-3f7a anchor drain'
status: todo
type: task
priority: normal
tags:
    - sm-26
created_at: 2026-09-03T16:32:23Z
updated_at: 2026-09-04T00:30:23Z
---

Measured 2026-09-03 (session qou-ggdk) after the alpha-cluster tranche (PR #6519, commits 577367a41b f3bafde098 9218877589). Method: grep -rlF '1.10997859555733471' computations --include=*.py. The literal is the self-certified muon pin A, retired 2026-08-22/28 (fca08de7d2, 83bab99730); the live muon anchor is q_muon_at() over the CODATA-2022 lepton ratio (…56427390…) and the proton default is Q_50_DIGIT_STR. These producers are UNSTAMPED, so q0_anchor_consistency_audit files them under Q0_ANCHOR_MISSING and the corpus-wide drain qou-3f7a (which keys on stamps) cannot see them. Recipe that worked on the 14 alpha producers, in three shapes: (A) dead fallback 'q_at(50) if the substrate imports else the literal' → hard refusal, import q_at from q_parameter (NOT qou_substrate.constants, or the witness gets no stamp), declare the stem under physical_proton; (B) explicit proton-vs-muon comparison (E1) → both pins by name, mpf residuals via _precision.fmt, assertion booleans as strings, wb.save(q0_comparison(muon=…, proton=…, reason=…)); (C) muon-only with no comparison purpose → proton default (2026-08-30 rule), stamp proton. Per-producer: run, diff the witness with volatile keys masked, expect proton legs unchanged past the 9th digit and muon legs shifted by the −0.0769 ppb pin migration; precision-gates.sh --changed must show zero NEW-dirty and only drained entries. Never re-pin an anchor-DEFINING witness (q-pinning-50-digit). Land manifest + witnesses together (constraint 4). Scope by subdirectory (deltalambda/, qbeta/, …) — a tranche per directory keeps each PR reviewable.

FOLLOW-UP found 2026-09-03 while verifying the colored-tower unit: computations/probes/qbeta_5two_colored_tower_barodd_qstar_probe.py:269 computes rel_slope = float(abs(B_mu-B_pr)/abs(B_mu)/(Q_MUON-Q_PROTON)) — float64 arithmetic on a value the witness PUBLISHES (data.qstar_scan_UNCERTIFIED_diagnostic.*.rel_slope). The raw-float64 ratchet does not see it because it is serialised as a formatted string, so this is a detector blind spot of the same family as the taxonomy's rows 22/25/26: a float64 computation laundered into a string before it reaches the witness. AGENTS.md permits float() only inside an f-string for display. Not fixed in the anchor tranche (scope), but the SHAPE is worth a detector: grep computations/ for float( whose result is stored rather than formatted. Likely several more instances.

TRAP found 2026-09-03 (tranche 1, probes/): REGENERATION ORDER IS FORCED WITHIN A RE-PIN TRANCHE. qbeta_5two_gk_bilinear_pairing_probe gates on reproducing the committed S+ matrix of its upstream qbeta-5two-stokes-barodd-index.witness.json at tol 1e-20 (via record_upstream). Both are in the same tranche; gk ran first, compared its new-pin S+ against the OLD-pin committed matrix, and the gate went 2.21e-25 PASS -> 7.38e-8 FAIL. Re-running gk AFTER the upstream was regenerated restores 3.14e-25 PASS. Nothing was wrong with either probe and the tolerance was not touched. CONSEQUENCE for the deltalambda/ (38) and qbeta/ (36) tranches: order the runs by the upstream graph — grep for record_upstream / add_upstream_records / load of a sibling .witness.json, topologically sort, run leaves first. A red consistency gate mid-tranche is the expected intermediate state, NOT a finding, and must not be 'fixed' by widening a tolerance. Same shape as qou-omr7 on main (he4-sparse gates on the COMMITTED triton).


## probes/ tranche COMPLETE (2026-09-04)

31 producers off the retired self-certified pin A; 24 witnesses regenerated;
allPassed unchanged in every one; no verdict touched. 8 commits, pushed.

Findings beyond the mechanical swap — each is a defect class, not a one-off:

1. MISLABEL x2 more (three total this session). `qbeta_habiro_cyclotomic` said
   "proton" in a comment, a print, its witness key `c3_empirical_at_proton_q0`
   and an audit note, over the MUON literal, while comparing against a
   proton-pin c_3 = -2.06934257. Layer straddle inside one quantity; c_3 swings
   ~2.4% between pins so every q-dependent candidate's err% was wrong.
   `qbeta_exponentiated_per_block` was stamped `proton` while computing at both
   pins. Root cause is constant across all three: a hardcoded literal cannot be
   checked against the name it is bound to, and four labels agreeing with each
   other does not make any of them right.

2. FALSE q0-INDEPENDENCE x2. `qbeta_5two_order3_barodd_tail` and
   `tau_binding_hitchin_wzw_wall` both declared `q0_anchor=False` -- "this
   result does not depend on which pin" -- while their own `_q0`-named fields
   moved under the re-pin: T_odd by 428.7 ppb (37x the pin move), and
   tau_binding_q0 / lps_sigma_real_q0 by 1.5 / 3.4 ppb. Both now stamp the pin
   they used. `keystone_lr_modulus_d2_collapse_test` keeps its declaration:
   only 1e-71 numerical zeros moved, so its conclusion really is pin-free.
   NOTE THE METHOD: the re-pin is what EXPOSED these. A false independence
   claim is invisible until something moves the pin.

3. SILENT FALLBACK x2 removed. `nastokes_surface_curvature_trefoil` had a
   try/except whose `try` imported the proton value and whose `except` bound
   the retired MUON literal, under a comment saying proton -- any environment
   without the substrate package computed at a stale muon value and said
   nothing. `qbeta_exponentiated_per_block` had a hand-typed copy of the proton
   digits behind the same shape.

4. PRE-EXISTING TEST FAILURE on this branch's HEAD, unrelated to any edit:
   `test_qbeta_habiro_anchor_guard::test_the_message_formats` asserted the
   literal "1.154e-08", the mu-p gap against the RETIRED pin. Live gap is
   1.161e-08; the 2026-08-22 re-derivation moved it and left the assertion
   behind. Fixture and expected gap now both derive from the anchors.

5. GAP-A3'S 17.7% MOVE IS NOT THE PIN (see below), and the chirality probe
   HANGS at HEAD (bean qou-0xe1).

## CORRECTION to my own claim (commit c360e0a180)

That commit said the gap-a3 witness stamps `proton` because the producer reads
by name AND is listed `physical_proton`. The manifest half is WRONG. Tested by
removing the stem from two producers and re-running: both still stamp `proton`.
`q_parameter` branches only on `ideal_muon` (one `if`), so `physical_proton`
membership is INERT for anything not in the muon list. The stamp comes from the
producer importing `q_parameter`. The entries are still worth adding -- a dozen
scripts read that list as a registry, including `gen_q0_anchor_manifest` and
`q0_manifest_finalize` -- but they document a classification, they do not cause
a stamp. Do not repeat the causal claim.

## METHOD that earned its keep: run the HEAD version

Twice this tranche a witness moved or a producer failed and the question was
whether the re-pin did it. Both times the answer came from running the
UNMODIFIED HEAD producer in the same container, not from reading the diff:

- gap_a3: HEAD already yields 16458.094 against a committed 13980.683. So
  17.7202% is pre-existing import-cone drift and the pin's own effect is
  22.14 ppb -- a factor of 8000 apart. A commit saying only "re-pin" would have
  described the smaller half by five orders of magnitude.
- chirality_state_integral: HEAD hangs at the identical line with a
  BYTE-IDENTICAL 283-byte log. Witness left at HEAD, bean qou-0xe1 opened.

## SESSION LOSS, recorded so it is not repeated

`git checkout -- computations/` -- run intending to revert the ~11
tree-measuring audit witnesses `precision-gates.sh` dirties every run --
reverted all 56 unstaged working-tree files and destroyed the tranche.
Unstaged changes are in no object database; `git fsck` had nothing. Six files
survived in session scratch copies; the other 25 were REDONE rather than
decompiled from the `__pycache__` .pyc left by an earlier compile check, since
decompiled numeric code is the wrong thing to introduce into a
precision-disciplined tree. The correct revert is the explicit path list the
gates' own output prints. Commit each unit as its witness lands.

## Remaining tranches

deltalambda/ 38 (in progress), qbeta/ 36, audits/ 11, substrate/ 9.
