---
# qou-3e5m
title: 'GAP: 56 self-fulfilling MEASURED assertions, hidden by a positional-only detector'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T03:40:10Z
updated_at: 2026-08-30T04:23:47Z
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
