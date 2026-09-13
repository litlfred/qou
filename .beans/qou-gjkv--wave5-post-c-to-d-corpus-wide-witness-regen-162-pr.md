---
# qou-gjkv
title: 'wave5: post-C-to-D corpus-wide witness regen (162 producers)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T03:14:24Z
updated_at: 2026-09-13T10:32:45Z
---


Branch: claude/anchor-followups-2026-08-08. CLAIMED by this session.
Continues qou-c6xo (wave 4), which STOOD DOWN at 27/162 because the C->D
excision was landing and any witness regenerated then would be stale on arrival.
C->D is now landed (73311b57, 33a6c7aa), so this is the re-run it called for.

Base: 13a5ebfa. Driver: computations/witness_regen_wave.py --timeout 900.
Launched under setsid (own SID, so a pgid kill aimed at the shell cannot reach
it -- see qou-c6xo, though note its "external reaper" analysis is retracted
there; setsid is cheap insurance, not a proven fix).
Report: scratchpad/wave5.json   Log: scratchpad/wave5.log

## Two of wave 4's six failures are already fixed going in

- delta_lambda_alexander_phase4.py and delta_lambda_jsj_phase3.py both died on
  `ModuleNotFoundError: probe_he4_jsj_topology` (wave 4's "fourth bug class").
  FIXED in 561fe967: helpers extracted to computations/atom_braid_words.py and
  both producers repointed; load_atom_braids() verified to return
  ['D','T','3He','4He'] in each.

## Three will fail again, and that is CORRECT -- do not "fix" them

- audits/delta_n2_placeholder_audit.py, audits/deuteron_delta_i_audit.py,
  compound_binding_via_differences.py all need
  atomic-braid-mass-table.witness.json. That witness was DELIBERATELY RETIRED
  (methodology-deprecation.witness.json:66, "six-term formula 24-54 % errors").
  Regenerating it is an explicit FORBIDDEN USE of that record. See the
  correction appended to qou-c6xo. Expect 3 FAILED here permanently.
  (compound_binding_via_differences prints its error to STDOUT, so a
  stderr-only triage mis-buckets it as a genuine bug -- it is not.)

## One chronic timeout expected

- audits/term5_aK_audit.py, 900 s, known. Plus alpha/alpha_k_jones_markov_h12
  (900 s) is the other slow one -- NOT on the historical known-slow list.
  Budget ~2 x 900 s, not 5 x (4 of the 5 historical slow producers declare no
  upstream and are excluded from the 162).

## Discipline for the commit

- NEVER hand-edit a witness number. Regenerate from the producer or leave it.
- Commit by explicit path. NEVER `git add -A`.
- Check for ORPHAN producers after any kill: they outlive the wave and WILL
  dirty the tree unattributed (qou-c6xo saw two).
- binding_energy_categorical_deuteron.py returned ANCHOR_MIGRATION_INFERRED in
  wave 4 -- verdict 'review' by design, not in KEEP, reverted. It will resurface
  here and needs a human look.

## RESULT — 162/162, clean exit, no orphans

Base 13a5ebfa, 03:13:55Z -> 04:55:13Z (1h41m). Report: scratchpad/wave5.json.

  NOCHANGE 68 · VALUES 57 · FAILED 23 · ANCHOR_MIGRATION_INFERRED 10 ·
  NEW 1 · DECLARED 3   ·   kept 3

COMMITTED (be1baa1f): the 3 DECLARED (provenance-only diffs -- computedAt,
commitSha, scriptHash, scriptCommitSha, durationMs; no numeric field moved) plus
the 1 NEW witness, delta-lambda-alexander-phase4.witness.json, which is the
proof 561fe967 worked -- that producer had NEVER emitted a witness.

## The 57 VALUES were REVERTED by design. Classification, by magnitude:

59 VALUES witnesses across 58 producers (a producer can touch >1).

  A. < 1e-9      noise / solver jitter                     3
  B. 1e-9..1e-3  small                                    21
  C. >= 1e-3     LARGE, convention-scale                  20
  non-numeric    allPassed / string fields                14
  unparsed                                                 1

Bucket C is where the C->D signal actually is, and the top of it is extreme:

     3.89e+08  probe-9b-perlambda-brane-tower           (1 field)
     4.06e+03  qbeta-li2q-spectral-combiner-crossanchor (14)
     4.72e+00  nucleus-operator-selection-sdp           (17)
     3.49e+00  a-K-via-lp-dual-hecke-basis              (48)
     1.00e+00  lambda-scale-derivation-probes-123, probe-d-cocasimir-barparity,
               qbeta-habiro-element-probe, low-isotope-mass-table
     9.95e-01  qbeta-1ppq-achieved

THREE SIGN FLIPS -- qualitative, not magnitude, so these want eyes first:
     delta-lambda-jsj-phase3.witness.json
     he4-canonical-tr-m-block-fingerprint.witness.json
     probes/qbeta-li2q-spectral-combiner-crossanchor.witness.json

Largest non-numeric movers are assertion/string churn at scale:
a-K-via-lp-dual-full (1969 fields), binding-single-pipeline-comparison (763),
borromean-axial-coupling (109).

ACCEPTANCE IS NOT DONE AND IS NOT MINE TO DO. The driver's
KEEP = {DECLARED, ANCHOR_MIGRATION, SUBFLOAT_MOVE} deliberately excludes VALUES,
so this wave CLASSIFIES; it does not accept. The report carries per-witness
evidence (fields moved, sign flips, triggering field + magnitude) so the review
pass needs no re-run.

## FAILED triage — 23, and only ONE was mine

  8  HABIRO CLUSTER, single root cause, PRE-EXISTING (not C->D).
     7x `CoercionFailed: expected an integer, got -74*check_q - 74`
     1x `TypeError: Cannot convert symbols to int`
     PROVED not mine: neither qbeta_habiro_wenzl_tower_zeta_n.py nor
     qbeta_habiro_delta_am_factorization.py imports wedderburn_jones_markov or
     y_lambda_at at all, and the C excision touched only that module. They
     surfaced now because 453b2a86 (2026-08-08) added record_upstream to 112
     producers, which is what put them in the 162 -- they had never been swept.
     Likely cascades into several of the 6 "missing upstream" below.
     NOT FIXED HERE: 8 pre-existing producers is its own piece of work.
  6  missing upstream ("Run its producer first"). 3 are the retired
     atomic-braid-mass-table consumers (CORRECT, do not fix -- see qou-c6xo);
     the other 3 are plausibly Habiro cascade.
  4  TIMEOUT at 900 s: term5_aK_audit (known chronic) + fr_pullback_borromean_h3a_test,
     probes/ksel2id_u1_promotion_probe, rho_k_co_casimir_extended (new, may just
     be slow -- rho_k is multiprocessing).
  2  FileNotFoundError on a missing upstream witness (dependency ordering):
     probes/delta_coupling_closed_form_probe, probes/lr_hecke_character_probe.
  1  EMPTY stderr: compound_binding_via_differences (prints to stdout; known).
  1  MINE: deltalambda/a4_brunnian_deficit_closed_form -- FIXED, see below.

## The one regression I caused, and its fix

a4_brunnian called y_lambda_at(4, None) / (3, None) -- the symbolic path I made
RAISE during the C excision. Fixed across two commits:

  b9a0232a / (solver commit): y_lambda_su_n_symbolic(n, q, N) -- the same
  hook-content product over sympy, exact in q. Self-tests 33 -> 43, all pass:
  symbolic == numeric at n=2,3,4 worst 5.35e-51 (compared at 50 dps, NOT the
  self-test's 30, since at 30 the numeric side caps the test at round-off,
  measured 9.86e-32); Sum y_l f^l = 1 exactly; row cap exact; and
  z = q^3/(q^2+1) EXACTLY -- registry D falls out symbolically, difference 0.
  Instant, vs the C path's ~18 min solve at n=4.

  b9a0232a: the producer's q-unification guard used `is` where the danger is
  `==`. Q_SYM is Symbol('q', positive=True); the producer's qs is
  Symbol('q', positive=True, real=True); positive implies real, so they are
  `==` but not `is`, and subs/xreplace both see nothing to replace. Measured
  that subs(qs, s**2) works fine on such an expression, so it was a false alarm.
  Bare Symbol('q') is still `!= qs` and still caught.

  Also tagged that producer's symbolic cache by CONVENTION. It was keyed on bare
  file existence, so a C-era cache would have been reused past the excision and
  silently reintroduced C. No such cache exists today -- prevention, not repair.

  a4_brunnian now runs (exit 0, 6.2 s) and reports VALUES on 9 fields, 0 flips.
  The mover is tau_L4_matches_independent_f64_measurement, whose
  expected=1.000145898 is a hardcoded C-era FLOAT64 reference. NOT retuned --
  that belongs in the VALUES review, and the f64 reference is itself worth
  flagging against the standing no-float64 directive.

## NEXT

1. VALUES review pass, bucket C and the 3 sign flips first.
2. The 8-producer Habiro `check_q` coercion bug (pre-existing, own bean).
3. The 3 stale doc citations of atomic-braid-mass-table (doc-only, from qou-c6xo).


---

## 🛑 At least one member of the 162 did NOT move for C→D — measured 2026-09-13 (bean `qou-5c64`)

`binding-single-pipeline-comparison`, which this bean lists by name among its
results, moves by **3.29×** on the traces it reads. Four hypotheses were tested
against the June witness recovered at full 50-dps precision:

| candidate | contribution |
|---|---|
| q₀ anchor, muon → proton | **3.9e-8** — negligible |
| `y_lambda_at` convention **C → D** | **NO-OP.** All 11 partitions at `n = 6` agree to displayed precision; substituting `_y_lambda_at_convention_C_HISTORICAL` inside `tr_m_atom_zn` returns the same trace to 30 digits. |
| `atom_braid_word_3A` intra-nucleon ordering, **grouped → borromean** (owner ruling `qou-hu1f`, 2026-09-05, `7db032fb48` / `deb9ff5728`) | **dominant** — forcing `grouped` moves `tr_free` 0.29901503 → 1.13171707 against June's 0.98352620 |
| residual | 15 % (free) / 48 % (atom), unidentified |

So this member's motion is driven by an **owner ruling four weeks LATER than
this wave**, not by the C→D excision this wave is named for. The C→D component
is measurably zero for it.

**Consequence for acceptance, which is this bean's open item.** The wave's label
is load-bearing: a reviewer accepting 162 witnesses "because C→D landed" would,
for at least this one, be accepting a change from a different ruling that had
not happened when the wave was measured. Before acceptance the 162 want
re-triage against `qou-hu1f` as well — cheaply, since any producer whose cone
reaches `atom_braid_word_3A` is a candidate and the parameter is directly
forceable (`intra_order="grouped"`).

Not claimed: how many of the 162 this applies to. One was measured. The wave's
own numbers were taken 2026-08-09, before the ordering ruling existed, so no
figure in this bean can distinguish the two causes.

Full measurement, including the two hypotheses it killed (one of them mine):
bean `qou-5c64`.
