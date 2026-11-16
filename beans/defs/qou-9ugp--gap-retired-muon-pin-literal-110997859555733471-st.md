---
# qou-9ugp
title: 'GAP: retired muon pin literal 1.10997859555733471 still hardcoded in ~180 computations/ producers outside the alpha cluster — all unstamped, invisible to the qou-3f7a anchor drain'
status: in-progress
pr: 8184
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - sm-26
created_at: 2026-09-03T16:32:23Z
updated_at: 2026-11-16T20:16:00Z
parent: qou-2002
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


## 🛑 CORRECTION (2026-09-04): the probes/ tranche is NOT complete — 31 of ~45

The section above says "probes/ tranche COMPLETE". That is WRONG and the
number it rests on was never measured. **I inherited a 31-file list from the
drain agent and never ran a discovery grep on the directory myself.** The
PR body's own scope line said "probes 44", so 13 were unaccounted before a
single detector was involved.

Found by reading sibling PR #6537 (`qou-y98b`), whose
`computations/audits/producer_baked_pin_audit.py` decides whether a producer
bakes a pin BY VALUE rather than by spelling. Running it over
`computations/probes/*.py`: **54 of 1001 bake a q0 pin**, and only 4 of those
are files this branch touched.

Measured properly, splitting live code from prose with an AST walk:

    probes/*.py carrying the RETIRED pin      26   (+1 value-only, below)
      live code   21   -> 8 fixed here, 13 REMAIN
      prose only   5   ->  3 fixed here,  2 remain (lower priority)
    probes/*.py carrying ANY 1.10997 literal 135
    probes/*.py baking a pin by VALUE         54   (38 proton, 4 muon-retired,
                                                    2 codata2018, 5 truncated)

REMAINING with the retired pin in LIVE CODE (13):
  _gap_a4_qsafe, difference_knot_binding_probe,
  he4_partition_dominance_audit_probe, he_nu_sdp_barfold_h9_test,
  he_nu_sdp_psd_count_test, he_nu_sdp_saturation_obstruction,
  markov_stab_trace_axis_probe, mn_dpn_xq_cross_anchor_probe,
  pentagon_rt_torus_knot_higgs_probe, qbeta_sdeformed_leading_bound_probe,
  rho_f_categorical_probe, su4_1111_markov_trace_probe,
  trefoil_complex_volume_probe

Plus `aomega_6y1p_swing_reframe_not_tractable`, which carries NO `1.10997`
string at all: it bakes the pin in an integer-ratio form only the value audit
sees. That is the 14th and it is the one a grep can never find.

## THE TWO DETECTORS ARE COMPLEMENTARY AND NEITHER IS COMPLETE

This is the AGENTS.md detector-blindness pattern again, and worth stating as
a rule rather than an instance:

- A **grep** sees a literal in a comment or docstring, which the value audit
  cannot parse. 26 files by grep vs 4 muon-retired by value.
- The **value audit** sees `mpf(693736614219613004744793)` and
  `Rational(693736614219613/62500000)`, which no `1.10997` prefix matches.
  38 proton-baking producers in probes/ are invisible to the grep entirely.

Use the UNION. A clean run of either one is evidence about that detector, not
about the tree. And a file list inherited from another agent is not a
measurement — re-run the discovery yourself before writing "complete".

The 38 proton-baking producers are a WEAKER defect than the 14: the value is
correct, only the method is wrong (hardcoded rather than read by name). They
do not go stale when the muon anchor moves. Priority order is the 14 first.


## probes/ VERIFIED COMPLETE (2026-09-04) — by BOTH detectors, 0 and 0

35 producers landed. The completion claim now rests on a measurement rather
than on a file list, and on both detectors rather than one:

    AST live-code scan (retired pin as an AST constant, not a comment):  0
    producer_baked_pin_audit --quiet, muon-retired lines by VALUE:       0

The four the first sweep missed:

- `aomega_6y1p_swing_reframe_not_tractable` -- both pins as 15-DIGIT
  TRUNCATIONS, and this probe's ENTIRE output is their difference (the mu-p
  tension), so the truncation landed on the reported quantity itself. Measured
  understatement: 11.5372 ppb reported against a true 11.6141 ppb, 0.67% low.
  Grep-invisible: no `1.10997` string survives in the source at all.
- `difference_knot_binding_probe` -- retired pin, sole anchor. Witness stays at
  HEAD: needs `snappy`, absent in this container, and fails identically at HEAD.
- `rho_f_categorical_probe` -- retired pin labelled "(MUON layer)". See the
  correction below; this one did NOT go to proton.
- `su4_1111_markov_trace_probe` -- retired pin as an ANCHOR-NAMING fixture, so
  `_anchor_of` could not have recognised the LIVE muon anchor as muon. Payload
  moved 0 fields, so the fix is provably behaviour-neutral apart from the
  classification it exists to perform. NOTE: this producer RUNS here
  (allPassed=True), against the AGENTS.md line listing it as one of two
  genuinely broken producers -- that line is either stale or the scipy-sparse
  crash is conditional.

## 🛑 CORRECTION 2: `Q_50_DIGIT_STR` IS ANCHOR-RESOLVED PER PRODUCER

This is the most consequential thing found this tranche and it corrects my own
d15ca14cbb note. `Q_50_DIGIT_STR` is NOT a proton constant. `q_parameter` reads
the manifest at import and, for any producer whose stem is in `ideal_muon`,
binds the MUON anchor to that same name.

So "read the anchor by name" does NOT mean "use proton". For the 19 producers
on `ideal_muon` it means the opposite, and the manifest is entirely
load-bearing for them -- the exact opposite of the "inert" finding, which holds
only for producers NOT on that list.

Consequence, caught only because the witness diff showed a muon value where I
had written a proton comment: `rho_f_categorical_probe` is on `ideal_muon`, so
patching it to `Q_50_DIGIT_STR` moved it from the RETIRED muon literal to the
LIVE CODATA-2022 muon derivation (+0.0769 ppb, same layer) -- not to proton at
11.54 ppb as my first comment claimed. Comment corrected in the file.

Audited the rest on that basis: NONE of the other 34 probes are listed
`ideal_muon`, so they are all correctly on proton.

RULE FOR THE REMAINING TRANCHES: check `ideal_muon` membership BEFORE writing
what a by-name patch does. The same edit means different things for a listed
and an unlisted producer, and only the witness diff distinguishes them.

## Open owner question (not taken unilaterally)

Whether `rho_f_categorical_probe` belongs on the muon layer at all. Exception
E2 of the 2026-08-30 ruling covers the ideal CAL-1/2/3 layer; nothing examined
here establishes that this probe is part of it. Moving it is an 11.54 ppb
change and belongs to the `ideal_muon` migration (qou-1c4y), which AGENTS.md
requires to land its manifest and witnesses together.


## SCOPE RE-MEASURED 2026-09-04 — 48 live, not 137

The tranche sizes quoted when this bean was opened (probes 44, deltalambda 38,
qbeta 36, audits 11, substrate 9) were GREP counts, and grep over-counts this
defect badly: most hits are comments documenting a fix that already landed.
Measured with an AST walk that excludes comments AND docstrings:

    tranche        grep    LIVE   prose
    deltalambda      39       0      39     <- COMPLETE
    qbeta            45      31      14
    audits           17      11       6
    substrate        10       6       4
    probes           26       0      26     <- COMPLETE
    TOTAL           137      48      89

So the remaining work is 48 producers, not 137. The 89-file gap is entirely
fix-documentation: a comment that says "this was the retired literal
1.1099785955573347, now read by name" is a grep hit forever.

deltalambda reads 0 live. Its 39 grep hits are the agent's own fix comments.

WHY THIS MATTERS BEYOND THE NUMBER: I over-counted the probes/ remainder the
same way earlier today, reporting "13 remain in live code" against a true 3,
because my first AST pass treated a `#` comment as live (comments never become
AST constants, so a comment-only file had NO constant carrying the literal and
fell through to the wrong bucket). Both a raw grep and a careless AST walk
inflate this surface ~3x. State which measure you used.


RESOLVED 2026-09-04 — the 1.4% cp_trace move flagged as UNVERIFIED in 56fdff0d2e
is PRE-EXISTING STALENESS, not the pin. Measured by running the UNMODIFIED HEAD
producer (git show HEAD:...he4_binding_k_fingerprint_stage1_probe.py, run in
place so _HERE/output_dir resolve identically):

  quantity            committed@HEAD        HEAD-producer re-run   my re-pinned run
  target_canonical    0.055358426266783106  0.1609741454424074     0.16097414544240738183
  cp_trace_no_binding 0.89307385932774589   0.905400288181         0.90540033019518634354
  best K word         [3, -6, 9]            [3, 6, -9]             [3, 6, -9]
  best tr_M           0.0634900512741141    0.145898300376         0.1458983071527361
  best rel delta      0.14689               0.09365                0.0936538

The HEAD producer reproduces EVERY structural difference on its own: the 2.91x
target, the 1.38e-2 cp move, the different winning K word, and rel 0.147 ->
0.0937. The re-pin accounts for 4.64e-8 on cp and 4.65e-8 on the best trace,
i.e. a pin sensitivity of 4.02 (= 4.64e-8 / 1.1541e-8), NOT the ~1.2e6 the
commit message hypothesised. Pre-existing / pin = 297437.

ROOT CAUSE, and it is the stale-consumer class: target_canonical_trace is READ
from canonical-tr-m-via-chi-cache.witness.json, whose helium-4 tr_M_q0 is
0.16097414544240738182587344098071685392360735413344 on origin/main AND in the
working tree. The sibling he4_binding_k_averaged_interface_probe reads the SAME
field with the SAME walk() code and its committed witness already carried
0.16097414544240738183. So the fingerprint witness alone was a generation
behind, its assertions passed before and after (allPassed True both), and
nothing looking at it in isolation could tell.

CONSEQUENCE FOR THE RESULT, not just the bookkeeping: the committed record
ranked candidates against a target 2.91x too small and named [3, -6, 9] as the
best plain inter-nucleon K at rel 0.14689. The live answer is [3, 6, -9] at rel
0.09365 — a different word and a 36% better residual. The rankings in the
committed top10 were not measuring what their labels said.

The refreshed witness in 56fdff0d2e is correct; only the commit message's open
question needed answering.

METHOD NOTE for the next agent doing this: the HEAD copy must live in the
producer's OWN directory (Path(__file__).parent drives _HERE and output_dir).
Mine was deleted mid-run by a concurrent agent's untracked-file cleanup and the
producer died with FileNotFoundError at file_content_hash() — after printing the
verdict, which is why the comparison survived. If you need the witness rather
than the stdout, keep the copy out of a shared checkout.


## CORRECTION 2026-09-04 — "the stamp comes from importing q_parameter" is NOT sufficient

This bean and PR #6519's body both record, as a correction to an earlier wrong
claim, that the `q0Anchor` stamp comes from importing `q_parameter` rather than
from `q0_anchor_manifest.json` membership. The manifest half of that stands.
**The import half is necessary, not sufficient**, and there are two measured
counterexamples on this very branch:

    qbeta_c3_candidate_audit    imports q_parameter: yes   writes: .save()   stamped: NO
    qbeta_c3_mq0_nk_scan        imports q_parameter: yes   writes: wb.save() stamped: NO

Both were migrated on this branch to read the anchor by name (so both import
`q_parameter`), both write through the `save()` path rather than `wrap_legacy`
— and both witnesses still carry no `q0Anchor`, on `origin/main` and after the
re-run alike. No regression: they were unstamped before and are unstamped now.

**What gates the stamp is therefore still unidentified.** I have a
counterexample, not a mechanism, and I am not guessing at one. Do not rely on
"it imports q_parameter, so it will stamp" — check the witness.

Found while attributing the q0-anchor refill ratchet during prepare-merge for
PR #6519; it is the third time this session that a claimed mechanism for this
stamp has turned out to be wrong.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.

## Progress Update (2026-11-16, PR #8184)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/AnchorManifestTriageAndAmeFloatDrain.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/anchor_manifest_triage_and_ame_float_drain_probe.py` and stamped witness `computations/probes/anchor-manifest-triage-and-ame-float-drain.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 100f1be37af2187c6d27ac18b72a859b25538c6c`).
- [ ] Awaiting merge of PR [`litlfred/qou#8184`](https://github.com/litlfred/qou/pull/8184) (`0a6bb0fe54cf925fb3bdc7285374e8ee0913d6dd`).

