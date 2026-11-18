---
# qou-l7j1
title: 'GAP (detector): the sqrt(q)/(q+1) spelling is unseen, and a fully-C file hides its own C closed forms'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T01:38:04Z
updated_at: 2026-10-04T15:19:29Z
parent: qou-trd0
---

Found during the probe/derived-tower C→D drain (PR #5739), while acting on the
warning in `qou-4bq3` that the detector's list is a floor rather than a census.
Companion to `qou-4bq3` (the `re.I` `C_`→`c_` classifier collision) — that one
is about *false skips*, this one is about *sites never listed at all*.

## Two distinct blind spots, both confirmed by hand

**1. The direct spelling `sqrt(q)/(q+1)` is not matched.**
`scan()` finds `1/(sqrt q + 1/sqrt q)`. The algebraically identical
`sqrt(q)/(q+1)` — the SAME NUMBER, 0.4993203342 — goes unreported when bound to
an ordinary name like `z`. This is the `_li_2_q_util.py:302` tuple-return
problem generalised: it is not only the *position* that hides a site, it is the
*spelling*.

**2. Worse, and the reason 1 matters: a file that is WHOLLY on C hides its own
C-specialised closed forms.** `scan_closed_forms()` documents that it reports
"only for files that ALSO define `z` the convention-D way", on the reasoning
that "in a file still wholly on C a square root is expected and is `scan()`'s
business". That reasoning has a hole: it assumes `scan()` SEES the file. When
the file's `z` uses spelling 1, `scan()` misses it, `scan_closed_forms()` skips
it by design, and the file is invisible to **both** halves of the audit.

## Three instances, read and confirmed (none in PR #5739's assigned set)

`computations/deltalambda/mirror_split_milnor_one_third_probe.py:127-131` —
the clearest case, and it demonstrates both blind spots at once:

    z = mp.sqrt(q0) / (q0 + 1)                                    # unlabelled z_C
    f_nn = (q0 ** mp.mpf("1.5") - q0**3 - q0**2 + q0 + 1) / (q0 * (q0 + 1))
    f_pn = (q0 ** mp.mpf("1.5") - (q0 + 1) * (q0**2 - 1) / 2) / (q0 * (q0 + 1))

Those `q0 ** 1.5` terms are **exactly** the half-integer fingerprint
`scan_closed_forms` exists to catch, in `f_pp`/`f_pn`/`f_nn` bond weights. Both
halves of the audit miss them. No comment names a convention anywhere.

`computations/probes/pauli_young_spin_isospin_delta_lambda_probe.py:301` —
`z = mp.sqrt(q0) / (q0 + 1)`, unlabelled, feeding `f_pn = z - h*(0.5 -
delta_cf/4)` in a deuteron pn-weight cross-check.

`computations/deltalambda/nuclear_quotient_jones_torus_link_probe.py:16,133` —
a documentation defect rather than a computation one, but it propagates: the
docstring and the emitted witness field both call C **"the canonical Markov
parameter"**. That assertion has been false since 2026-08-15 and it ships in a
witness.

## Scope, honestly

A shape-census over `computations/**/*.py` matching the C algebra in any
position (assignment, return, tuple, dict value, argument) returns **92 hits**
against the detector's 27 actionable + 15 deliberate. **The 92 is not a defect
count** — most are legitimate: labelled comparison arms, "EXCISED" records,
docstrings, and a large family of `(sqrt(q) + 1/sqrt(q))**4` "spin_carrier"
terms in the gap_a3/gap_a4 probes which are `[2]_{sqrt q}` **quantum
dimensions, a different object from the Markov parameter**. Do not bulk-migrate
off that number. The three above are the ones read individually and confirmed.

## Next honest step

Add the `sqrt(q)/(q+1)` shape to `scan()`, and drop the "D-defining files only"
restriction from `scan_closed_forms()` (or gate it on `scan()` having actually
proved the file D, rather than assuming). Then re-triage — expect the actionable
count to RISE, which is the mechanism working, not a regression.

Not fixed here deliberately: `qou-4bq3` owns the tooling and two drains were
running against it live.
