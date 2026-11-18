---
# qou-gjkv
title: 'wave5: post-C-to-D corpus-wide witness regen (162 producers)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T03:14:24Z
updated_at: 2026-10-04T15:14:23Z
parent: qou-5vkl
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


## 🛑 RETRACTION of the append above — this wave's LABEL IS RIGHT

I wrote here that the C→D component of `binding-single-pipeline-comparison` is
"measurably zero". **That is false and is retracted.** Measured one step further
(bean `qou-5c64`): isolating the bond types from the ordering-invariant ratio
`tr_atom/tr_free`, the **p-p bond IS the Markov parameter `z`** —
`0.61268805054558909984` today, matching `z_D = q³/(q²+1)` to **3.2e-51**, and
`0.49932034618370936279` in June, matching `z_C` to 2.4e-8 (the residue being
the q₀ anchor). Its residual is `z_D/z_C = 1.227044`.

My error: I tested **one carrier** of the convention — the C-vs-D swap inside
`y_lambda_at`, which is genuinely a no-op — and reported the convention inert.
The convention also lives in `z` itself, which never goes through that function.

**So this wave's "post-C-to-D" label fits this member.** What survives, and is
still worth acting on before acceptance: the same witness moved from **three**
changes, only one of them C→D. The other two — `qou-hu1f`'s intra-nucleon
ordering (owner ruling, **2026-09-05**) and the colour-weighting δ de-wire
(`9928f3f4a79`, **2026-06-29**, whose own commit message says *"WIP: witness
cascade pending"*) — sit after and before this wave's measurement date of
2026-08-09 respectively. So the wave's recorded numbers are **incomplete** for
this member rather than wrongly attributed, and a reviewer accepting on the
C→D rationale alone would still be accepting two further undiagnosed changes.

Not claimed, same as before: how many of the 162 this applies to. One measured.


## Follow-up: C→D is the WHOLE bond side, not one factor of three

Correcting my own correction above (bean `qou-5c64`, second retraction). I had
credited the p-n colour-weighting δ de-wire (`9928f3f4a79`) with part of this
member's motion. It has none: I had backed `d` out of the June bond by
subtracting `z_D` when June was on `z_C`.

Against each side's own `z`, all three bond `d` are unchanged —
p-p `0`, p-n `-0.1044582` / `-0.1044582`, n-n `-h` / `-h` — and
`(z_D + d)/(z_C + d)` with `d` fixed predicts every measured bond residual to
**2e-7**.

So for `binding-single-pipeline-comparison` the split is:

- **bond side: 100 % convention C→D** — this wave's stated cause, and it is the
  whole of it;
- **ordering: `qou-hu1f`** (owner ruling, 2026-09-05) — postdates this wave;
- **per-nucleon free factors** (proton 1.0755215, neutron 1.0698745) —
  unidentified, and the only thing left open.

**Net effect on this bean: my flag was over-stated twice and the label was right
all along.** What still stands, and is the only actionable part: the wave's
numbers were measured 2026-08-09 and cannot include the 2026-09-05 ordering
ruling, so for this member they are incomplete — a reviewer accepting on them
would be accepting one further undiagnosed change, not a mis-attributed one.


---

UPDATE 2026-09-13 (from bean `qou-5c64`, which flagged this bean twice today and
was wrong both times — see below). The decomposition of
`binding-single-pipeline-comparison`'s motion is now **complete and measured**,
and it confirms this bean's 2026-08-09 classification without qualification.

**`tr_atom(now)/tr_atom(June) = [free] x [bonds]`, two components, nothing else:**

- **bonds — pure convention C->D.** Each bond factor moves by
  `(z_D + d)/(z_C + d)` with the interface shift `d` **unchanged**:
  `d_pp = 0`, `d_pn = -h(1/2 - delta/4)`, `d_nn = -h`, all three derived in
  `qbeta_bond_factors_derived_probe.py` and independently reproduced here by
  witness differencing to 2.73e-11. Factors 1.227044031 / 1.287106862 /
  1.390572916.
- **free side — the `qou-hu1f` intra-ordering ruling**, `0.590749626^Z .
  0.5146405906^N`: the per-nucleon trace was the `chi-{proton,neutron}-h3-at-q0-50dps`
  witness (1.065306865 / 0.9232333461) and is now the canonical borromean word
  (0.6293296323 / 0.4751333545).

Reconstruction verified on all six atoms with CHAIN bond counts; **every residual
is below its own recording floor** (worst 2.43e-03 at ⁷Li against a 1e-02 floor —
its `tr_atom` carries 3-4 significant figures). Table in `qou-5c64`.

**Two corrections to what `qou-5c64` told this bean earlier today, both retracted
there in full:** that "the C->D component is measurably zero" (false — it is the
entire bond side), and that the δ de-wire contributed a third of the motion (an
artefact of subtracting `z_D` from a June value computed on `z_C`).

**Nothing is enacted here.** Regenerating the witness is this bean's call and an
owner decision under the 2026-09-07 ASK-THE-OWNER directive; the re-run done for
the measurement was reverted. The 299-field raw-float64 drain on that witness
stays blocked behind the decision (PR #7268 documents it as out of scope).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
