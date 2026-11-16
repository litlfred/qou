---
# qou-3e5m
title: 'GAP: 56 self-fulfilling MEASURED assertions, hidden by a positional-only detector'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T03:40:10Z
updated_at: 2026-11-16T19:43:00Z
parent: qou-trd0
---

Surfaced while draining `qou-p77d`. The detector
`computations/audits/self_fulfilling_assertion_audit.py` read only the
POSITIONAL calling form of `add_assertion`, and positional is the minority:

    add_assertion calls    487 positional    3300 KEYWORD

So it scanned 13% of the corpus and its headline read **"MEASURED (cannot
report a regression): 0"**. With both forms read the figures are **MEASURED 56,
LITERAL 187**. The detector is fixed (this PR); the 56 findings are not, and
they are a triage job rather than a sweep.

## Why the MEASURED ones matter and the LITERAL ones mostly do not

The audit's own framing: a LITERAL self-comparison (`probe_completed = True`
against itself) is a documentary flag — it records that a step ran and was
never going to fail. The 187 of those are noise unless one is masquerading.

A **MEASURED** self-comparison is different: it computes something, compares it
to itself, and is recorded as a passing assertion. It looks like a check and
cannot fail. The sharpest instance:

    computations/habiro/habiro_exact_qbeta.py:197
      habiro_tr_M_proton_matches_direct
        computed = tr_M_p / tr_M_p_direct ...   expected = the same expression

The NAME asserts a cross-check between two routes. The code compares one route
to itself. Anything reading this witness sees `passed: true` for a
cross-validation that never happened.

## The originating instance

    computations/m_p_m_e_li2q.py:134
      codata_mp_me_loaded   computed=1836.152  expected=1836.152  tol=1e-10

Named as though it verifies the CODATA value LOADED; no variable is read.
Note also that CODATA 2022 m_p/m_e is 1836.152673426 — 1836.152 is a truncation,
so even a real check against the loaded constant would need the fuller value.

## Work order (suggested, not measured)

1. Take the 56 MEASURED first; ignore the 187 LITERAL unless one is named like
   a check.
2. For each, find the INTENDED second value. Usually one of: an independent
   route (the habiro case), a published/CODATA reference, or a prior witness.
3. Where no independent value exists, the honest fix is to demote it — record
   the quantity with `add_data` instead of dressing it as an assertion.
4. Do NOT delete the assertion to make the count go down.

## Trap worth carrying

The selftest did not catch this and its docstring claimed it would — "guards
against a future narrowing quietly reporting a clean tree". It exercised only
positional calls, so it validated the one branch that worked and never touched
the branch that did not exist. **A selftest built from the same assumption as
the code tests the assumption's consequences, not the assumption.** This is a
new row for the detector-blindness taxonomy
(`docs/audits/2026-08-15-detector-blindness-taxonomy.md`): calling-form
blindness, where the detector is correct on the shape it reads and simply does
not read the shape the corpus uses.


## First one fixed: habiro_tr_M_proton_matches_direct (56 -> 55)

`computations/habiro/habiro_exact_qbeta.py:197`. `expected` repeated the
`computed` expression verbatim, so the ratio was compared to itself. Now
`expected="1"` — the target the NAME states — and it passes:

    computed 1.000000000000001672503680645958090545156   expected 1   tol 0.01

The guard `float(tr_M_p_direct) != 0` is also now exact (`tr_M_p_direct != 0`):
an mpf underflowing a double would have read as zero and silently substituted
0 for the ratio.

### An observation the fix exposes, NOT a claim about its cause

The two routes agree to **1.7e-15** against a tolerance of **1e-2** — the check
is ~13 orders of magnitude looser than the agreement it certifies. A tolerance
that loose is only marginally better than the self-comparison it replaced: the
routes could diverge by 1% and it would still pass.

I did NOT tighten it. Picking the right tolerance is a claim about what the two
routes are supposed to guarantee, and I could not establish that. If the Habiro
series genuinely TERMINATES at M=8 (as the producer's own `method` field says),
two exact routes should agree at compute precision, ~1e-40, not 1e-15. Either
M=8 is a truncation rather than a termination, or something else limits one
route. Worth someone's attention; not settled here.

### Correcting a hypothesis of mine mid-investigation

I first proposed the 1.7e-15 was float64 ingress via the upstream, on the
strength of sibling witnesses — `habiro-coefficients-boron-12` and
`-beryllium-9` DO store `tr_M_at_q0` as 16-digit JSON floats. **Wrong for this
producer.** The upstream it actually reads,
`habiro/habiro-coefficients-atomic.witness.json`, stores the proton value as a
**29-significant-digit STRING**. So the disagreement is real arithmetic, not a
serialization artifact, which makes it more interesting rather than less.

Generalising from sibling witnesses of other isotopes was the error. Read the
upstream the producer names.

### Work-order note for the remaining 55

This one was unusually clean: the assertion's NAME stated the target ("matches
direct" -> ratio should be 1), so the intended second value was recoverable
from the name alone. Expect that to be the exception. Where the name does not
state a target, the honest fallback is demotion to `add_data`, not invention of
an expected value.


## Second fixed, and the two together give the whole disposition rule (56 -> 54)

    habiro_tr_M_proton_matches_direct   TWO routes exist -> supply expected=1
    S-at-q0-matches-sdp-witness         ONE source only  -> demote to add_data

**The discriminator is NOT the name.** Both names promise a comparison
("matches X"). Only one producer has two things to compare. `S_at_q0` IS the
SDP witness's `tau_M_at_q0`, loaded 40 lines above the assertion, so no
expected value can be supplied honestly — demoted, with the value already
present in `add_data` (0.186893667721512196644439995907, 30 digits) and
verified still in the regenerated witness.

So: read what the producer HAS, not what the assertion is called.

## Classification of the remaining 54 (name-based, so approximate)

     10  A. name states a target -> may be recoverable
     22  B. documentary count dressed as an assertion
     25  C. ambiguous — the source must be read

(Buckets sum past 54 because the classifier also scans `tools/`; see the count
note below.)

**Bucket B is the big mechanical one** and it is a demotion batch, not a fix
batch: `deuteron_scan_completed = len(candidates)` against itself,
`h4_plancherel_scan_completed`, `alt_geometry_scan_completed`, and ~19 more of
exactly that shape. A count of what a scan found is data, not a check. Note
`add_assertion` cannot express `len(candidates) > 0` — it compares with a
tolerance — which is plausibly WHY these were written as self-comparisons in
the first place. Demote each to `add_data` and confirm the value survives.

**Bucket A is smaller than it looks.** Several are "finite"/"nonzero" claims —
`shift_neutron_h3_finite`, `c_8_extracted_finite`,
`v-leading-eps-coefficient-nonzero`. `add_assertion` cannot express those
either. The honest form is to compute the predicate and assert it equals 1, or
demote. Do NOT fabricate a numeric expected for a predicate.

**A structural observation worth carrying upstream:** three separate shapes
here (a count, a finiteness claim, a nonzero claim) are all things
`add_assertion` has no way to say. That is a gap in the WitnessBuilder API, and
the self-comparison is the workaround authors reached for. Fixing the 54 one at
a time treats the symptom; an `add_check(name, predicate, source)` would remove
the incentive. Not proposed as work here — recorded so the next agent sees the
pattern rather than 54 unrelated bugs.

## Count note — reconciled, quote the detector

My ad-hoc classifier reported 57 where the committed detector reports 55 (now
54). Neither is wrong: `self_fulfilling_assertion_audit.py` has
`ROOTS = ("computations",)` and does not scan `tools/`; my script did. Quote
the detector for `computations/`, and note `tools/` is outside its scope —
3 further self-comparisons live there, all LITERAL.


## Batch 1 of bucket B: 4 landed (54 -> 50), 2 held. The 2 are the finding.

Landed, each verified after re-run (key present in `data`, gone from
`assertions`, `allPassed` unchanged, producer keeps other real assertions):

    qbeta_5two_stokes_population_bridge_probe   assembly_scan_completed
    qbeta_5two_gk_bilinear_pairing_probe        confrontation_completed
    qbeta_5two_masbaum_cyclo_level_probe        scan_completed
    qbeta_5two_masbaum_block_row_probe          solve_family_completed

### 🛑 A STATIC COUNT OF `add_assertion` CALLS OVERCOUNTS — failure branches

`binding_per_bond_decomposition` was classified "safe" because the file has
**2** `add_assertion` calls and only 1 was a hit. The other is inside
`if not HAVE_INFRA:` — a failure path that never fires — so at RUNTIME the
witness carries exactly **1** assertion and demoting it leaves ZERO. Reverted.

**Consequence for the open decision: the zero-assertion set is >= 17, not 16,
and the source scan cannot get it right.** Establishing the true count needs a
RUN per producer, comparing `len(witness["assertions"])` against the number of
hits, not a source count. Do that before quoting a figure.

### `fr_pullback_borromean_h3a_test` — reverted, NOT verifiable here

Two independent reasons, either sufficient:

  * Its witness `fr-pullback-borromean-h3a-test.witness.json` is **not
    committed anywhere** — not at HEAD, not on disk. So there is no artifact to
    verify a demotion against. (Note this means the self-fulfilling-assertion
    detector legitimately flags producers whose output is untracked: it scans
    SOURCE. The defect is real; only the verification path is missing.)
  * It is slow — killed at >159 s having emitted 17 progress lines.

**And a measurement trap of my own, worth carrying:** the first batch recorded
`fr_pullback ... exit=0` after 2.2 s. That was FALSE. The process had been
killed by an earlier `pkill -f fr_pullback_borromean` of mine, and the runner
captured `$?` after a redirect, so a killed producer was recorded as a clean
success. **A recorded exit code is only trustworthy if nothing else could have
killed the process.** Cross-check a suspiciously fast exit-0 against whether the
producer actually wrote its artifact — that is what caught this.

### The `source=` prose nearly went missing

The first version of the demotion transform replaced `add_assertion(...)` with
`add_data(name, value)` and dropped `source=` — e.g. "all 21 pre-registered
exact solves completed and recorded", the only place that description exists.
Applied to six files and re-runs started before I noticed. It now emits
`{'value': ..., 'source': ...}`. **A demotion must carry the prose, or it is a
deletion wearing a demotion's commit message.**


## 2026-08-30 — 26 of 56 resolved; the other 30 triaged, not applied

**Attribution re-measured after rebasing onto `a917f3da1e`** (925 incoming
commits). The only comparison that means anything is **this branch's fixed
detector run against main's tree**, because main still carries the blind
detector and reports 0 there:

| tree | MEASURED | LITERAL | files |
|---|---|---|---|
| `origin/main` (fixed detector applied to it) | 56 | 189 | 183 |
| this branch | **30** | 187 | 159 |

So the 26 resolutions are this branch's and none was duplicated by the 925.

**Triage of the remaining 30 is written up in full:**
`docs/audits/2026-08-30-self-fulfilling-assertion-triage-of-the-remaining-30.md`.
Partition is total and disjoint — 1 + 12 + 9 + 8 = 30.

- **1 misnamed claim.** `audits/brundan_kleshchev_audit.py:189` asserts
  `dim_centre_eq_pn_{n}` by computing `p(n)` and comparing it to `p(n)`. It
  never computes a centre dimension and has no route to one. Five passing
  assertions per run for a theorem that was not tested. **Author decision**;
  recommendation is rename-and-demote.
- **12 repairable** — the falsifiable claim is already in the assertion's own
  name or `source`; only `expected` is wrong. `shift_from_nf_basis.py:256,262`
  are outright deletable: lines 271-278 already check the same two shifts
  against `expected=20` / `expected=16`.
- **9 author-documented recordings** — the source says "recorded", "informational",
  or, at `qbeta_singularity_cross_anchor_probe.py:303`, literally *"it does not
  assert it"*, attached to an `add_assertion` call.
- **8 counts and labels** — same shape as the 17 already demoted.
  `hadron_knot_table.py` is the expensive one (>50 min per bound atom).

**Not applied, and the reason is code-read rather than assumed.** The container
was replaced mid-session and is strictly weaker than what the witnesses record
(python 3.11.15 vs 3.13.12, mpmath 1.3.0 vs 1.4.1, `clarabel` absent). `save()`
guards the environment only on the *preserve* path, gated on
`_witnesses_substantively_equal` — and every disposition above changes the
`assertions` array, so none is substantively equal, all take the rewrite path,
and the weaker block lands under a warn-only check. The guard fires exactly
when there was nothing to protect. **Do this work in a matching container.**

**The API gap is the deeper fix.** 16 of 30 exist because nothing in
`WitnessBuilder` says "measured result, not a check", nor expresses is-nonzero /
is-finite / exceeds-threshold. Class R hand-rolls all three as 1/0 flags. Until
a constructor exists this population regrows.

Also landed: taxonomy **row 18 — calling-form blindness**
(`docs/audits/2026-08-15-detector-blindness-taxonomy.md`), the first row in that
file from outside the convention-C arc.


## 🛑 2026-08-30, LATER — superseded by `qou-26f2`; the real marginal number is 6, not 26

Corrects the entry above, which was written before rebasing onto a `main` that
had moved 990 commits.

**A sibling ran bean `qou-26f2` as a multi-batch campaign over the same 56
sites** and got there first. Re-measured with the same detector against both
trees: `main` 56 -> **17**; this branch on top of it -> **11**. So the branch's
marginal contribution is **6**, not the 26 recorded above.

**In every case where our dispositions differ, theirs is better.** Not close:

- `brundan_kleshchev_audit.py` — my headline "theorem name over a tautology",
  which I flagged as needing an author decision. They renamed it
  `partition_count_p_{n}` with `expected=KNOWN_P_N[n]` (an independent table)
  and wrote the scope distinction into the source. That KEEPS a falsifiable
  check; my recommendation was rename-and-demote, which removes one.
- `qbeta_5two_stokes_population_bridge_probe` — I demoted the count. They
  derive `expected=_n_channels * len(weights_x) * len(cand)`, so the scan now
  fails if it misses combinations.
- `qbeta_decay_sdp_extended_ck` — I wrote three copy-pasted finiteness flags
  plus a hand-rolled `_is_finite`, then argued int-vs-string with Copilot. They
  write one loop over `mp.isfinite` with `expected=True`; the question is moot.
- `mn_flavor_split_h4_plancherel` — I thought they missed this one. Batch 3
  covered it.

All superseded files taken from `main` wholesale in the rebase.

**Adopt their rule, which is sharper than mine:** assert `> 0` when finding
nothing is the outcome the name exists to exclude; demote ONLY when finding
nothing is a legitimate result. By it, my `alpha_em_4pi_q_hyperbolic_b3_pslq`
demotion is right (`pslq_executed…` — no relation IS the answer) and my
`mn_flavor_split_h4_plancherel` demotion was wrong.

**What survives is worth more than the count.** Two agents partitioned the same
population independently and converged on compatible dispositions, including on
the one case I singled out as needing human judgement. The four classes in
`docs/audits/2026-08-30-self-fulfilling-assertion-triage-of-the-remaining-30.md`
are therefore a second independent derivation, not one agent's taxonomy.

**Live remainder: 11** — 7 class R, 3 class D, 1 class C. Named in that doc.

**Coordination lesson for this bean:** `qou-3e5m` and `qou-26f2` are the same
work under two names. This is mechanical drain, not open research, so per
AGENTS.md it has ONE owner — and neither of us posted intent. Check `.beans/`
for an existing bean on the same population before opening one.


---

## REGRESSION 2026-08-31: MEASURED 2 -> 9, and this gate has been RED the whole time

Measured on `main` `e8f5a64a81`:

    MEASURED (cannot report a regression):   9
    LITERAL  (documentary flag):           119
    exit code:                               1

This bean drove MEASURED 56 -> 2 (its own campaign plus sibling `qou-26f2`).
It is now **9**, and none of the seven new ones came from the `qou-srvu` drain
that landed today — checked, not assumed: none of the five drain merges
(`500a4df1a291`, `4a58860b7308`, `7e9b622eb00f`, `d27cfd2c782d`,
`2ea086408b20`) touches any flagged file.

| file | hits | note |
|---|---:|---|
| `probes/gs_filtration_jet_shape_magic_probe.py` | 5 | |
| `probes/symbolic_nf_q_degree_magic_probe.py` | 1 | |
| `probes/tower_walk_magic_replication_probe.py` | 1 | |
| `fr_pullback_borromean_h3a_test.py` | 1 | `float(best_bor)` |
| `lambda_scale_all_c_i_family_a.py` | 1 | `str(value)` |

## The new sub-shape: a string-formatted RATIO as an assertion value

Five of the nine — and every hit in the three `*_magic_probe.py` files — have
this form:

    f"{v['n_magic']}/{v['n_non_magic']}"
    f"{len(sweep_seen)}/{len(sweep_rows)}"
    f"{MAX_GRADE + 1} vs {comb(4, 2) + 1}"

That is a **rendered string**, not a number, being handed to `add_assertion`
as the computed value. It is worse than the positional-argument blindness this
bean was opened for, because the defect is not that the detector misses it —
the detector caught it — but that the assertion *cannot fail informatively*
even when it fires: comparing `"3/7"` to `"3/7"` tells a reader nothing about
which side moved, and comparing it to a literal freezes a formatting choice
as if it were a result. Two of the three probes assert the identical
`n_magic/n_non_magic` shape, so this is a copied idiom spreading, not three
independent slips.

## THE PART THAT IS MY FAULT, and it is the reason this went unnoticed

`self_fulfilling_assertion_audit.py:228` is `return 1 if measured else 0` —
**no `--strict` needed, any nonzero MEASURED is a non-zero exit.** So this
gate has been RED continuously for this entire session, at MEASURED 2, before
any of today's regressions.

I ran it five times while verifying the `qou-srvu` slices and reported
*"MEASURED 2, unchanged"* each time, treating **unchanged** as **clean**. It
was neither. A count that is stable at 2 on a gate whose pass condition is 0
is a red gate holding still, and I read the stability instead of the
threshold. That is the same class of error as reading `all([]) == True` as a
pass — which is the entire subject of the sibling bean `qou-srvu` I was
verifying at the time.

## Disposition

The five `*_magic_probe` hits want one owner and one fix (assert the two counts
separately as numbers, drop the rendered ratio). `fr_pullback_borromean_h3a_test`
and `lambda_scale_all_c_i_family_a` are separate and unrelated.

Do NOT read the 2 -> 9 as this bean's campaign regressing. The campaign held;
new probes arrived carrying a new spelling of the same defect. That is the
`qou-mnrd` revolving-door shape in a second gate, and it is the third time
today a "known, stable" audit number turned out to be masking a substitution.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-31 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 47 Execution Update (2026-11-16, PR #8152)

- **PR:** https://github.com/litlfred/qou/pull/8152 (`d0d9e522bf023310f599b4d6724b0703e39ccbd4`)
- **Action taken:**
  - Added `--self-test` alongside `--selftest` in `computations/audits/self_fulfilling_assertion_audit.py`.
  - Replaced all 15 remaining live `MEASURED` self-comparisons across 9 probes in `computations/probes/` (`cyclic_square_does_not_reopen_milnor_probe.py`, `frobenius_admissibility_net_row_probe.py`, `gs_filtration_jet_shape_magic_probe.py`, `milnor_mubar_vanishes_on_every_triple_probe.py`, `milnor_one_separated_component_and_the_chain_residual_probe.py`, `milnor_vanishing_is_generic_for_monotone_probe.py`, `nf_bond_count_injectivity_probe.py`, `symbolic_nf_q_degree_magic_probe.py`, `tower_walk_magic_replication_probe.py`) with genuine boolean/expected assertions.
  - Verified `python3 computations/audits/self_fulfilling_assertion_audit.py` now reports `MEASURED (cannot report a regression): 0` and exits `0`.
- **Status:** Kept `in-progress` pending PR #8152 merge and owner review.
