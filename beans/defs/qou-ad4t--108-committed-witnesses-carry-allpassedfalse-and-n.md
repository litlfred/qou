---
# qou-ad4t
title: 111 committed witnesses carry a recorded assertion failure and nothing reads them
status: todo
type: bug
priority: normal
created_at: 2026-08-21T15:08:23Z
updated_at: 2026-08-21T15:21:12Z
---

Found while fixing `qou-4e5k`: the witness whose assertion named that defect had
been sitting on main, failing, for twelve days. It is not alone.

## Measured on origin/main, 2026-08-21

Scanned every `*.witness.json` under `computations/` excluding `_deprecated/`:

    2681 dict-shaped witnesses scanned
     108 carry allPassed == false   (4.0%)

By month of `computedAt`:

    2026-05:  1      2026-06: 38      2026-07: 25      2026-08: 44

These are not detector *gaps*. The detectors fired, wrote a correct verdict to
disk, and the file was committed with the failure recorded in it. Nothing
consumes the field.

## The instance that proves it matters

`computations/tr-m-algebraic-q.witness.json`, computedAt 2026-08-09:

    allPassed: false
    symbolic_delta_matches_li2q   computed=1.3381598e-06  tol=1e-12  passed=FALSE

That assertion names, precisely and numerically, a real defect: two definitions
of the colour split δ disagreeing by exactly ℏ³. I rediscovered it independently
twelve days later by measuring a deuteron trace, having no idea the repo had
already written it down. Fixed under `qou-4e5k`; the same witness now reports
6.51e-19 and `allPassed: true`.

Its sibling assertion is the other half of the lesson. `algebraic_q0_matches_transfer`
was **passing** at `6.88e-08` against `tolerance=1e-07` — 69% of a budget whose
`source` string explained the residual away as a *"~1e-8 float64-eval floor of
the exact ℚ(q) form"*. It was not a floor; it was the same δ error. With δ
corrected the value is 3.50e-15, so the "floor" sat ~17 orders above the real
one. **A tolerance chosen to fit an unexplained gap converts a detector into a
rationalisation**, and it will pass forever.

## Why this is worth more than 108 individual fixes

A recorded-but-unread failure is strictly worse than no check, because the
existence of the check is what stops anyone looking. Three of the four items in
this arc's PR were found by hand-measuring things the corpus had already
measured.

Sample of what is sitting there (full list reproducible with the scan below):

    2026-08-15  canonical-derivation-pipeline-compliance   contract: WitnessBuilder usage (P30)
                                                           contract: Witness reproducibility (P32)
    2026-08-15  chi-convention-audit                       no_unknown_convention
                                                           no_unlabeled_chi_witness
    2026-08-19  audits/fitted-labelled-canonical-audit     no_fitted_labelled_canonical
    2026-08-10  probes/canonical-ordering-dof              closed_form_matches_full_trace

The `chi-convention-audit` and `fitted-labelled-canonical-audit` rows are
especially pointed: those are *the corpus's own discipline checks*, red, ignored.

## Next step

Two things, in order:

1. **A gate.** Something must fail when a witness with `allPassed: false` is
   committed. `scripts/precision-gates.sh` is the established hand-run preflight
   and has the right shape; a `--changed` mode makes it cheap. Note the standing
   ruling (AGENTS.md, 2026-08-09) that `witness-staleness.yml` stays
   `workflow_dispatch`-only — so this belongs in the preflight, not in CI, and
   re-proposing the trigger is out of scope.
2. **Triage the 108, oldest first.** Each is one of: a real defect (fix it), a
   tolerance that was always wrong (fix the tolerance and say why), or a probe
   recording an expected negative (which should not be using `allPassed` at all).
   The third category is the one to identify first, because it is the reason the
   field became ignorable.

## Reproduce

    python3 - <<'PY'
    import json, pathlib
    for p in sorted(pathlib.Path("computations").rglob("*.witness.json")):
        if "_deprecated" in str(p): continue
        try: w = json.loads(p.read_text())
        except Exception: continue
        if isinstance(w, dict) and w.get("allPassed") is False:
            fails = [a.get("name") for a in (w.get("assertions") or [])
                     if isinstance(a, dict) and a.get("passed") is False]
            print(str(w.get("computedAt",""))[:10], p, fails)
    PY

## GATED 2026-08-21 — and the count was 111/137, not 108

`computations/witness_failed_assertion_audit.py`, wired **blocking** into
`scripts/precision-gates.sh`, baselined at 111 witnesses / 137 failed
assertions. Self-test 8/8. Full suite: all blocking gates green, exit 0.

**Correcting my own figure above.** I reported 108. The real count is **111
witnesses / 137 assertions**. My first scan keyed only on `allPassed is False`
and therefore missed witnesses carrying a per-assertion `passed: false` **while
`allPassed` is not set false** — an inconsistency that is itself worth
surfacing, and which the checker now reports. The bean's "4.0%" becomes 4.1% of
2681. Low, not stale-high.

### Why a ratchet and not a boolean

A gate red on arrival gets skipped — `precision-gates.sh` records that reasoning
in its own comments about the provenance audit, and that is exactly how a
checker goes quiet. So the backlog is baselined and tolerated, on the same terms
as the raw-float64 and padding ratchets: **a witness not in the baseline that is
red fails; a baselined witness whose count grows fails; counts shrink, never
grow.** The class stops growing today, and the drain proceeds on its own clock.

This is the mirror of `witness_hollowness_audit`, which catches `allPassed: true`
with `assertions: []` — green with nothing behind it. Nothing caught the
opposite, which measures commoner.

### What the checker deliberately does NOT catch, named where it will be looked for

The `tr-m-algebraic-q` sibling assertion that **passed** at `6.88e-08` against a
`tolerance=1e-07` whose `source` explained the residual away as a "~1e-8
float64-eval floor". It was a real defect; post-fix the value is `3.50e-15`, so
the claimed floor sat ~17 orders above the real one. No mechanical check sees a
tolerance chosen to fit an unexplained gap. It is written into the module
docstring because that is where someone will go looking.

### Distribution — the drain order this implies

    66  (59.5%)  computations/ (top level)
    17  (15.3%)  computations/probes/
    14  (12.6%)  computations/qbeta/
    11  ( 9.9%)  computations/audits/
     2  ( 1.8%)  computations/markov/
     1  ( 0.9%)  computations/substrate/

I expected `audits/` to dominate and it does not — 11 of 111. But its *shape*
is the structural finding, so check it first anyway: **all eleven assert
`no_<something>`** —

    content-block-label-audit        no_missing_labels
    fitted-labelled-canonical-audit  no_fitted_labelled_canonical
    float64-leak-audit               no_i8_violations
    guarded-off-audit                no_guarded_off_candidates
    hardcoded-literal-audit          no_hardcoded_registry_matches
    i1-no-probe-audit                no_i1_no_probe_blocks
    i2-probe-only-audit              no_i2_probe_only_witnesses
    lean-ref-resolution-audit        ok_count_matches_total_minus_failures
    stale-probe-audit                no_stale_probes
    validation-as-input-audit        no_i11_violations
    witness-provenance-audit         no_missing_provenance

— i.e. each asserts "this backlog is empty" and is red because it is not. These
are **backlog counters wearing a pass/fail assertion**, and they will stay red
until their backlogs drain, which is category 3 of the module docstring. Eleven
permanently-red discipline audits is a large share of the reason a reader learns
that a red witness is normal. Fixing them is a schema change (carry the count in
`data`, assert on the ratchet), not a maths change, and it is the cheapest way
to make the remaining 100 legible.

The top-level 66 are the real defect surface and need per-file reading.

### Next step

1. Re-schema the 11 `audits/` backlog counters so red means red.
2. Then drain the 66 top-level, oldest first.

## RETRACTION 2026-08-21 — my "next step" was wrong, and so was my reading of it

I proposed re-schemaing the 11 `computations/audits/` witnesses as category 3,
"backlog counters wearing a pass/fail assertion". **Retracted.** I checked three
before touching them:

    fitted-labelled-canonical-audit  no_fitted_labelled_canonical  computed=8   expected=0
    witness-provenance-audit         no_missing_provenance         computed=10  expected=0
    stale-probe-audit                no_stale_probes               computed=0.0 expected=1.0

These are **honest reds**. Each asserts a discipline invariant, and each is red
because the invariant is violated — 8 real hardcoded-literal sites, 10 real
missing-provenance witnesses. Converting them to ratchets would turn "no
violations" into "no NEW violations", which is precisely the baseline-widening
AGENTS.md forbids in the strongest terms. **The 11 audits are category 1 — fix
the violations — not category 3.** They are the system working, and the only
correct response is to drain what they name.

That reclassification does not change the gate committed above: it is a
meta-check on the witness FILE, and baselining these 11 records them rather than
excusing them.

## And I misread the thing I went to drain — twice over

I opened `fitted-labelled-canonical-audit`'s 8 rows expecting anti-fit
laundering. They are **hardcoded q₀ literals** — a practice defect (type the
number instead of importing `q_parameter`), not a fitted value passed off as
canonical. Already covered by the `q0-value drift ratchet` already wired into
`precision-gates.sh`.

Then, on two of them (`metallic_q_n4_character_sweep.py:59`,
`metallic_q_wenzl_sign_sweep.py:61`), I measured the literal `1.1099785955541805`
against the muon string in `q-pinning-50-digit.witness.json`, found a 2.84e-12
gap, and drafted it as a **corrupted muon transcription**. It is the opposite.
From `computations/q0_provenance_audit.py:44`:

    Q_MUON = 1.1099785955541805        # <- the CANONICAL muon
    Q_MUON_50 = "1.10997859555418057528159407960950937799328227995870"
      "DERIVED not typed: q_muon_at(60) from CODATA m_mu/m_e and Vol(4_1)
       reproduces exactly this. Owner ruling 2026-08-15: the muon string is
       the correct one."

The string I compared *against* — `1.10997859555733471989…`, carried by **243
witnesses** — is the NON-REPRODUCIBLE one. So the literal in those two sweeps is
the correct muon, and my "corruption" was me holding the wrong reference.

Worth carrying forward, because that file already calibrates it and I would have
overclaimed the same way: the 2.84e-12 gap is **431× smaller than the
experimental uncertainty on q_muon** (CODATA `m_mu/m_e = 206.7682830 ± 4.6e-6`
→ 1.22e-9 relative). Both strings are physically meaningless past ~digit 8.
What is wrong with the 243-witness string is **reproducibility, not accuracy** —
it cannot be regenerated from the stated inputs.

Net: the two sweeps are off-canon only by *pin choice* (proton is the compute
default per the 2026-08-07 directive and R2), which is `qou-1c4y`'s migration and
is explicitly not authorised as a bulk sweep. No unclaimed drain for me here.

## Corrected next step

Not the 11 audits as a schema change. Drain what they NAME, and the cheapest
honest unit is `witness-provenance-audit`'s 10 missing-provenance witnesses —
`witness_provenance_audit.py` already ships `--strict`/`--list`, already runs
advisory in `precision-gates.sh`, and its offences are per-file and independently
fixable. The top-level 66 remain the real defect surface and need per-file
reading.

## An unread red witness does not just sit there — it DECAYS

Went to drain `witness-provenance-audit`, per the corrected next step. Re-ran it.
The result is the sharpest argument in this bean:

    committed 2026-08-01   scanned 2296   missing 10   ratio 0.995209
    re-run    2026-08-21   scanned 2682   missing 44   ratio 0.983221

The backlog grew **10 -> 44**, 4.4x, while 386 new witnesses landed. Nobody read
the red, so nobody re-ran the audit, so the audit's own witness went three weeks
stale — and its stale number **understates the problem by 4.4x**. Anyone who
finally did read it would have been misled downward.

That is the second-order form of this bean's thesis. An unread failure is worse
than no check not only because the check's existence stops people looking, but
because the recorded number rots toward optimism while it waits.

Committed the refresh. It stays RED (44 > 0) — this is not making a red green,
it is making a stale understatement current. Failed-assertion count is unchanged
at 1, so the ratchet granularity holds and the gate stays green.
`completeness_ratio` was already a float in the committed version, so no new
float64 enters.

### The missing-provenance backlog is concentrated in the chi-* family

Of the 44, the visible majority are `chi-*-at-q0-50dps*` — missing
`['engine', 'scriptFile', 'commitSha']` or just `['scriptFile']`. That is the
same family carrying the nine colour-blind chi caches (`45789ddfa0`) and four of
the five remaining structurally-convention-C witnesses. A family with no
`scriptFile` cannot be regenerated by `run_pipeline`, which is plausibly WHY its
convention staleness persisted: nothing downstream knew how to rebuild it.
Worth checking as a common cause rather than a coincidence.

### Hazard found on the way: two files share one basename

`computations/audits/witness-provenance-audit.witness.json` records
`scriptFile: witness_provenance_audit.py` — a bare basename, and there are TWO:

    computations/witness_provenance_audit.py         verdicts WRITES / UNCONFIRMED /
                                                     NOT_A_PRODUCER / SCRIPT_MISSING
    computations/audits/witness_provenance_audit.py  prov_ok / prov_missing /
                                                     no_missing_provenance

They are different tools. I resolved the claim to the first, ran it, got
`NOT_A_PRODUCER 0 / SCRIPT_MISSING 0`, and had drafted "the committed red is
stale, a re-run turns it green" — the opposite of the truth. The right script
makes it worse, not better.

The claim is not false, it is **under-qualified**, and the file it names is
precisely the checker whose job is to verify that `scriptFile` writes the
witness. `scriptFile` should be repo-relative wherever a basename is ambiguous;
until it is, a provenance check that resolves by basename can confirm against
the wrong file. Worth its own small fix.

## Correcting myself again, and the exemption that rhymes with the whole bean

**"The visible majority of the 44 are chi-*" was wrong.** It is **14 of 44
(32%)**. I read a `tail -25` of the audit output, which happened to show the chi
block contiguously, and generalised from a truncated sample. Fifth draft of mine
this session to invert or overstate under checking.

### The regenerability hypothesis: confirmed for chi-matrix-m, NOT general

Tested directly — do the convention-stale witnesses lack `scriptFile`?

    witness                                    PROV_MISSING?   scriptFile
    chi-helium-3-h9-...-matrix-m               no (exempt)     ABSENT
    chi-helium-4-h12-...-matrix-m              YES             ABSENT
    chi-tritium-h9-...-matrix-m                YES             ABSENT
    derived-chi-catalogue                      no              derived_chi_catalogue_build.py
    y-lambda-macdonald-telescope               no              y_lambda_macdonald_telescope.py

**3 of 3 `chi-*-matrix-m` convention-stale witnesses have no `scriptFile`**, so
`run_pipeline` cannot regenerate them — a real mechanism for why their staleness
outlived the migrations that reached other families. But it is **3 of 5**, not a
universal cause: the two non-`matrix-m` entries both have working producers and
are stale anyway. Do not carry this forward as "the" explanation.

### The exemption is the finding

`chi-helium-3-h9-at-q0-50dps-matrix-m` lacks `engine`, `scriptFile` AND
`commitSha`, and is **not** counted in the 44. It sits in
**`PROV_EXEMPT_NO_READER`** — exempted because nothing reads it.

It is read. `convention-c-witness-audit.py` reads it, and flags it as one of the
five witnesses still structurally on convention C (25 entries).

And that bucket is not small:

    PROV_OK                  2322
    PROV_EXEMPT_NO_READER     239     <- 5x the flagged count
    PROV_AUDIT_EXEMPT          74
    PROV_MISSING               44
    PROV_EXEMPT_ACKNOWLEDGED    2
    PROV_PARSE_ERROR            1

So the headline "44 missing provenance" **excludes 239 witnesses that also lack
provenance**, on the grounds that nobody consumes them.

That exemption has the same shape as the defect this whole bean is about. "No
reader" is a statement about the present, not about correctness — and a witness
with no reader and no provenance is exactly the one that will sit stale and
wrong indefinitely, because nothing will prompt a re-run and `run_pipeline`
cannot rebuild it. The exemption is applied precisely where the risk of silent
rot is highest. Two of the five convention-C survivors are in that population.

I am NOT claiming the 239 are all wrong, or that the exemption should be
deleted — an unread scratch witness genuinely does not need provenance. The
claim is narrower and testable: **`no_reader` is being used as a proxy for
`doesn't matter`, and at least one member is demonstrably read by an audit.**
The exemption should key on "no reader **and** no audit reads it", which is a
cheap change to the same scan.

### Next step

Re-scope `PROV_EXEMPT_NO_READER` to exclude witnesses that an audit reads, and
re-measure. That is a one-predicate change and it will move witnesses from a
silent bucket into a counted one — the right direction, and it will make the
number worse, which is the point.

## My fix to the exemption was WRONG — measured, 10/10 false positives

Implemented the "no reader AND no audit reads it" idea as: when a witness has no
`scriptFile`, treat a single `.py` mention as a real reader rather than as its
own producer (threshold `> 1` -> `>= 1`). Result:

    PROV_EXEMPT_NO_READER   239 -> 72     (-167)
    PROV_MISSING             44 -> 210    (+166)

Then I sampled the newly-flagged class (no `scriptFile`, exactly 1 `.py`
mention; 162 members) and asked whether that single mention WRITES the witness
or reads it. **10 of 10 were writers** — filename-matched producers containing
`WitnessBuilder` / `json.dump`:

    qbeta-5two-route13-rogers-extension  <- qbeta_5two_route13_rogers_extension_probe.py
    hh1-h5-bar-parity                    <- hh1_h5_bar_parity.py
    c-knot-not-universal                 <- deltalambda/c_knot_not_universal_probe.py
    ... 7 more, same shape

**REVERTED.** My premise was a category error, and the same one I have now made
repeatedly today: `scriptFile` absent means *provenance was not recorded*, NOT
*no producer exists*. Almost all of these have producers that simply never wrote
themselves down. The original `> 1` heuristic is right for them, and my change
turned one true positive into ~162 false ones.

The `chi-helium-3-h9-...-matrix-m` miss is still real. The correct predicate is
not "does a producer field exist" but **"does the single mentioning `.py`
actually WRITE this witness?"** — which is exactly the WRITES/UNCONFIRMED verdict
that `computations/witness_provenance_audit.py` (the *other* file of that name,
see the basename hazard above) already computes. Wiring that verdict into
`has_reader` is the right fix and is not a one-predicate change; it needs the two
tools joined.

## And the count itself is not reproducible

While reverting I re-ran on a clean tree, twice:

    total scanned 2682   PROV_MISSING 55   PROV_EXEMPT_NO_READER 227   (stable, x2)

My commit two steps earlier recorded **44 / 239** from the same script on what
should have been the same tree, and I cannot reproduce it. I am not going to
guess at the cause — `py_counts` is built from a `grep` over `computations/`,
so anything that adds or removes a `.py` mention of a witness name shifts the
exemption boundary, and this session added files. But that is a hypothesis, not
a finding.

What it demonstrates is worth more than the number: **this audit's headline
count depends on the state of unrelated files**, so two honest runs days apart
can disagree without anything relevant having changed. A gate cannot be built on
it until that is understood. Committing the reproducible 55/227.
