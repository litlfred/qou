---
# qou-qyef
title: 'GAP: probes reading muon q-pinning-50-digit against proton-pinned inputs — straddle sweep + SDP-witness pin provenance'
status: todo
type: task
priority: normal
created_at: 2026-09-04T10:34:15Z
updated_at: 2026-09-11T14:48:38Z
---

Found while resolving qou-2364 (PR #6596, 2026-09-04). Two related provenance/straddle defects, both wider than the one probe that was fixed.

## The straddle pattern
qbeta_markov_trace_norm_probe.py read q_0 from computations/q-pinning-50-digit.witness.json (q0Anchor: MUON, value 1.109978595642739...) to build A(q) and evaluate a constraint, while its upstream input (qbeta-decay-sdp-knot-operator.witness.json) supplied S + L2 coords computed at the PROTON pin (1.1099785827513808...). Evaluating proton-pinned coords against A(q_muon) inflated the L2 residual to 3.48e-9 (the mu-p tension ~1.15e-8 scaled by dS/dlnq ~ -21), which read as a 50000x 'regression'. Fixed there by switching the probe to Q_50_DIGIT_STR (proton, owner default 2026-08-07).

## The sweep (not yet done)
Other probes that read q-pinning-50-digit.witness.json (muon) to build q-dependent objects while consuming proton-pinned witness inputs would carry the SAME straddle silently — passing or failing at the mu-p tension scale (~1e-8) rather than the true residual. Candidate finder:
  grep -rln 'q-pinning-50-digit' computations/ --include=*.py
Then for each: does it ALSO read a proton-pinned witness (q0Anchor: proton, or containing 1.1099785827)? If so, it straddles. Fix = read Q_50_DIGIT_STR (proton) unless the probe is a deliberate muon/ideal-CAL comparison (owner exception E1/E2, AGENTS.md 2026-08-30).

## The provenance gap that hid it
qbeta-decay-sdp-knot-operator.witness.json records NO q0Anchor / q0Value (both null). That is exactly what let the straddle hide — a reader cannot tell which pin its coords were computed at without grepping the raw value 1.1099785827 out of the blob. Its producer should record q0Anchor/q0Value at save(). Same likely true of other older qbeta witnesses. A witness-provenance audit keyed on 'has q0-dependent data but no q0Anchor field' would surface the class.

Priority: normal. Not blocking anything; it is a correctness-hygiene sweep.


## 2026-09-11 — the sweep is SIZED, not done: 4 measured, and the detector already exists

Pulled off the `qou-bstl` completion-candidate queue. The sweep this bean
describes as "not yet done" is still not done — but two things about it are now
measured, and one of them changes what the work is.

### 🛑 First: this bean's own candidate finder over-counts by ~28x, and I walked into it

Running the recipe as written — `grep -rln 'q-pinning-50-digit' computations/
--include=*.py`, then "does it ALSO read a proton-pinned witness" — gives
**161 files**, of which **113** look like straddles. That number is my filter,
not a finding. The second test matched `q_parameter` (an import name present in
most of the tree) and swept in:

  * the **pin audits themselves** — `q0_anchor_consistency_audit.py`,
    `muon_pin_three_values_probe.py`, `anchor_flip_straddle_audit.py`,
    `q0_producer_pin_classifier.py` — which name both pins **by design**;
  * `q_pinning_50_digit.py`, the **anchor-defining producer**;
  * `_source_normalise.py`, which is a text utility.

Same mention-vs-use class this corpus keeps hitting. Do not quote 113 or 161.

### The corpus already has the detector, and its answer is 4

[`computations/audits/pin_straddle_unguarded_audit.py`](computations/audits/pin_straddle_unguarded_audit.py)
is exactly this sweep, and it is two-stage by design:

    STAGE 1  shape candidates                       148   (high recall, each needs a verdict)
    STAGE 2  MEASURED pin mismatch                    4   (producer anchor vs artifact stamp)

The four, each "pins proton, loads an artifact built at the muon pin":

    categorical_bypass_volmatch_demo.py        <- y-lambda-wenzl-witness.json
    cross_check_trM_cw_seminormal_leg.py       <- cross-check-trM-cw-seminormal.witness.json
    qbeta_singularity_type_probe.py            <- qbeta-decay-sdp-extended-ck.witness.json
    rho_k_co_casimir_extended.py               <- y-lambda-wenzl-witness.json

**Control passes:** `qbeta_markov_trace_norm_probe.py` — the instance this bean
opened on, and which it records as fixed — reads `Q_50_DIGIT_STR` (3 sites) and
is **absent** from the measured list. So Stage 2 is detecting the thing this
bean is about, and the fix took.

Worth noting `qbeta_singularity_type_probe` in that list: it is the producer
behind the PR #1727 simple-pole verdict that `qou-tv6l` withdrew on separate
grounds. Two independent reasons to distrust the same figures.

### 🛑 But 4 is a LOWER BOUND, and this bean predicted exactly why

Stage 2 works by comparing the producer's pin against the **artifact's stamp**,
so an artifact with no stamp is invisible to it. That is precisely this bean's
third section — `qbeta-decay-sdp-knot-operator.witness.json` records no
`q0Anchor` / `q0Value`, *"exactly what let the straddle hide"*.

**Still true today**, verified: both fields are `None`.

And the population is not one file. Scanning 3374 non-deprecated witnesses,
**212 carry a `1.109978…` literal anywhere in the blob while `q0Anchor` is
absent or null.** State that as what it is: a **high-recall upper bound** on the
invisible population — the test matches either pin and matches a literal sitting
in a `description` as readily as one in a data field, so some fraction are prose.
It is not 212 unstamped q-dependent witnesses; it is "at most 212, and not
zero", and the one hand-checked member is a real one.

**So the ordering of the work inverts.** Draining the 148 shape candidates by
hand is the visible task and the smaller one; the 4 measured are cheap. What
actually bounds the sweep's completeness is that a producer can dodge Stage 2 by
not stamping — so the bean's own item 3 (*"its producer should record
q0Anchor/q0Value at save()"*) is not a hygiene afterthought, it is the
**precondition** for the sweep's result to mean anything.

Bean stays `todo`. Nothing changed; this sizes it.
