---
# qou-n62l
title: Witness descriptions hardcode findings and drift; no gate reads a description
status: todo
type: task
created_at: 2026-09-06T11:31:55Z
updated_at: 2026-09-06T11:31:55Z
---

## The gap

Every staleness mechanism here compares a witness against its **producer** —
`scriptHash`, `q0Anchor`, the raw-float64 ratchet, the dps floor. **None reads
a `description`.** So a description that hardcodes a finding keeps asserting it
after the data moves underneath, and the witness ends up contradicting itself
inside a single file while staying green.

## Measured

`rho-binding-constancy.witness.json` said

> "the ratio varies ~182% (D 5.73, T 81.5, ³He 37.4)"

while carrying D 3.87 / T 36.99 / ³He 19.12 — and after regeneration under the
corrected atom word, 14.64 / 291.0 / 131.7. **The prose matched neither the
committed data nor the fresh data**: stale across at least two regenerations.
The same description also claimed "the D ratio 5.728 reproduces the published
α_M 5.729 (cross-validates the pipeline)" — a *claim* that had quietly stopped
holding.

## Built: `computations/audits/witness_prose_drift_audit.py`

Pulls every decimal number out of each `description` and buckets it by distance
to the nearest number anywhere else in the same document.

| bucket | rel | reported |
|---|---|---|
| EXACT | digits verbatim in data | no |
| ROUNDING | < 5e-3 | no |
| NEAR | < 5e-2 | no |
| **DRIFT** | **5e-2 .. 0.6** | **yes** |
| UNRELATED | > 0.6 | no |

`--selftest` passes **10/10**, including every calibrated false positive below.

### The calibration is the work — three passes, each driven by a measurement

1. **Distance, not presence.** `l1-ceiling-sign-prune`'s prose says `0.59`
   where the data has `0.5661` — an honest 3-sig-fig rounding at 4 %. A boolean
   "is the string present" test flags it exactly as loudly as a 49 %
   contradiction. Bucketing by distance clears it.
2. **Zeros destroy the ranking.** `|0 − x| / |x|` is **exactly 1.0 for every
   x**, and witnesses are full of zero counts and flags — so every prose number
   in every such witness scored 1.0 and the ranking saturated. A zero is never a
   drifted copy of a nonzero result. Dropping them: 233 → 210.
3. **The band needs an upper edge too.** Ranking by raw distance put a prose
   tolerance of `9.0e-18` beside data of order 1e-2 at **5e15**, burying
   everything real. The edge is set FROM the measured cases (0.058, 0.069,
   0.079, 0.33, 0.55), not guessed. 210 → 185.

Percent forms are matched against both `x` and `x/100`, because prose says
"~189.6 %" where the data carries `1.89576`. A decimal point is required, which
drops years, PR numbers (#1105) and bean ids without needing a list of them.

### Validated against the four cases whose status was already known

| witness | result | expected |
|---|---|---|
| `delta-lambda-qdim-route-probe` | FLAGGED 0.41, 5.62 | known stale ✓ |
| `delta-lambda-cancellation-ascaling` | FLAGGED 0.28, 1.27, 1.31 | known stale ✓ |
| `delta-lambda-l1-ceiling-sign-prune` | clean | known ROUNDING ✓ |
| `rho-binding-constancy` | FLAGGED 5.728, 5.729 | — see below |

The last is **the documented limitation demonstrating itself**, and is the most
useful line in this bean. That description was FIXED to interpolate its numbers,
and none of its live figures (189.6, 14.64, 291.0, 131.7) is flagged. What is
flagged is the sentence *withdrawing* the old claim. Those digits are quoted
history and an external constant, correctly absent from the data. **No static
rule separates a withdrawn number from a live one**, and the audit does not
pretend to.

## Result

    3528 witnesses scanned | 383 without a description
    185 witnesses with candidates | 239 candidate numbers

~6 % of witnesses carrying a description. That is a **triage list, not a defect
list** — the audit narrows a 3500-file haystack to 185 descriptions worth
reading.

## The durable fix is not to correct the numbers

Correcting a stale number only resets the clock. The fix is to make the prose
**derive** them: `rho_binding_constancy_probe.py` now interpolates its
description from the computed ratios and cannot go stale again. That is the
pattern the 185 want, and it has been applied to exactly one producer.

## Unclaimed

Nothing corrected here. The two known-stale descriptions
(`qdim-route`, `cancellation-ascaling`) still state convention-dependence
findings nobody here has studied, and rewriting an unverified conclusion is
worse than leaving it visibly flagged.

---

## Wired into the gates array (2026-09-06)

`scripts/precision-gates.sh` now carries it, blocking:

    "…|--strict --no-witness|yes|yes"

**Ratchet, not bare `--strict`.** A blocking gate that is red on arrival gets
skipped — the failure mode that file's own header warns about — so it tolerates
the committed backlog via a `*-baseline.json` and blocks only what is NEW or
GREW. `--rebaseline` refuses to run if any count went up: draining only.

Confirmed by EXECUTION, not by reading the array:

- green at its own baseline (exit 0) under the harness's exact invocation;
- **red on an injected regression** — a throwaway probe with one unbound name
  made it exit 1 and name the file, then was removed. A detector that cannot be
  shown to fire is a no-op, which is why the harness self-tests at all.

### The harness caught a defect in the wiring itself

`precision-gates.sh` invokes `python3 <script> --self-test` — **hyphenated** —
and treats a non-zero exit as "a detector that cannot be shown to fire". Both
audits were written with `--selftest` only (copied from
`retired_pin_live_code_audit.py`, which is in no array and so never had to
match). They would have failed their gate on arrival, silently, for a reason
having nothing to do with what they detect. Both spellings are accepted now.

That is the qou-j6gb lesson landing a third time: a gate outside the array is a
gate nobody runs — and a gate inside it that the harness cannot invoke is the
same thing wearing a badge.

### Not verified here

The full `precision-gates.sh` run fails PREFLIGHT in this container
(`missing: qou_substrate`, needs `pip install -e tools/qou-substrate`). The
script itself says that is not a gate failure. So the two gates were exercised
by replaying the harness's own `--self-test` + `$args` sequence against them,
not by a whole-suite run; the remaining 25 gates are unexercised here.

---

## 2026-09-07 — the two known-stale descriptions, and what interpolating them exposed

Both now DERIVE their numbers and are clean; the population drained
185 → 183 witnesses, 239 → 234 numbers.

### `delta-lambda-qdim-route-probe` — two errors, one of them not numeric

Prose said "⁴He spans **0.41→5.62**"; the data said 0.433→3.103. Now
interpolated from the row the run computes, and also recorded as
`he4_ceiling_span` so prose and payload cannot diverge.

Interpolating caught a second error the drift detector could not see: the
description opened "across **3** q-dimension conventions" while
`ceiling_over_target` carries **four** (classic, balanced, unbalanced,
fake_degree). The count is now derived too.

A third thing surfaced and was NOT fixed: "net −82.9 % vs fake-degree ℓ¹
+462 % on ⁴He" is **not computed by this producer at all** — it appears only in
prose, here and in the module docstring, and the witness carries nothing to
check it against. I could not attribute it either: a substring search for the
digits matched 1250 witnesses, because "462" occurs inside any long decimal —
a useless result, not a finding. The description now says plainly that the
figure is inherited from the surrounding analysis and is not this run's
measurement.

### `delta-lambda-cancellation-ascaling` — the numbers were the smaller problem

Prose: "heavy isotopes (³He **1.27**, ⁴He **1.31** at fake-degree) **overshoot**
while light ones (D 0.28, T 0.91) undershoot."

Derived from the current rows: D 0.23, T 0.458, ³He 0.647, ⁴He **−0.066**.

So interpolating exposed that the QUALITATIVE claim is stale as well: **none of
the four overshoots +1 any more, and ⁴He has changed sign.** The
non-uniformity in A survives; the direction does not. Almost certainly the
qou-hu1f braid-word correction, which is what moved every atom trace.

**Flagged, not rewritten.** The description now reports the derived figures and
states in terms that the qualitative reading predates them and no longer
describes them. Restating a refutation is a scientific judgement; substituting
my own reading of a convention-dependence result I have not studied would have
been worse than leaving it visibly wrong.

### What this says about the detector

It found stale DIGITS. Fixing them found a stale COUNT and a stale CONCLUSION,
neither of which any number-matching rule could reach. The detector's value is
as a triage pointer to descriptions worth reading — which is what its docstring
claims and, on this evidence, understates.

---

## 2026-09-07 (later) — sampled the backlog, then fixed what the sample showed

The 183 remaining candidates were unexamined, so the honest question was
whether that is a backlog or noise. Read a random sample of **10**:

| witness | flagged | verdict |
|---|---|---|
| `qbeta-5two-n5-cable-qstar` | 5.4 | **false** — `A5.4`, a bean section |
| `derived-chi-catalogue-matrix-m-mu-n-prototype` | 1.3 | **false** — `Phase 1.3` |
| `proton-m_e-derivation` | 1.4283 | **false** — explicitly a DEPRECATED literal being named |
| `qbeta-level-k-operator-and-real-decays` | 8.9 | **false** — a superseded control being CORRECTED |
| the other six | — | plausible real quantities (ratios, exponents, residuals) |

**4 of 10 false positives, in two clean classes.**

**Class 1 — identifiers. Fixed.** `A5.4`, `Phase 1.3`, `Step 23.5`, `Rule 14.2`
are labels, not measurements. A negative lookbehind drops digits glued to a
preceding character; the label words needed a post-filter instead, because
Python's `re` requires a FIXED-WIDTH lookbehind and an alternation is not one.
Population: **183 → 172 witnesses, 234 → 218 numbers.** Selftest 10 → 14 cases.

**Class 2 — deliberately quoted superseded values. NOT fixable statically, and
should not be.** `proton-m_e-derivation` names the deprecated literal it
replaced; `qbeta-level-k` quotes the control figure it corrects. Both are
exactly the shape of this branch's own withdrawal sentences in
`rho-binding-constancy` and `cancellation-ascaling`. Quoting the number you are
retiring is GOOD practice, and no rule that reads only digits can tell it from
a claim that went stale. The docstring already says so; the sample now
quantifies it at roughly 2 in 10.

**Read that as: the 173 is a triage list of which perhaps a fifth is quoted
history.** It is not 173 defects, and reporting it as one would be the same
overstatement this bean exists to catch.

### The ratchet caught my "improvement" regressing

The first version of the identifier filter put the guard inside the pattern:
`(?<![0-9A-Za-z.])-?\d+\.\d+`. That looked equivalent and was not. The
lookbehind sits before the **optional sign**, so where a `-` follows an
alphanumeric the engine is blocked at the sign and **retries at the digit** —
turning `-3.79` into `3.79`. Flipping the sign changes the distance to the
nearest data value, so it INVENTED findings: two witnesses gained candidates
even as the population fell.

`--rebaseline` refused, because per-file counts had gone UP:

    NEW   probes/c5_sign_is_robust_convergence_claim_is_not_probe   (2)
    GREW  probes/the_intra_ordering_moves_absolute_traces...        5 -> 6

I would have taken the falling total as success. The ratchet's per-file
accounting is what stopped it, on its first outing against a change of mine —
which is the argument for `--rebaseline` refusing on any increase rather than
on a net increase.

Fixed by filtering WHOLE matches the plain pattern already found, which has no
retry to exploit. Verified against those two witnesses specifically: no
candidate the old pattern did not also produce.
