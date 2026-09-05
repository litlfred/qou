---
# qou-xql6
title: The beta rate carries ONE s^2 not s^4, and the vertex factor is double-counted
status: completed
type: task
priority: high
created_at: 2026-09-05T08:49:05Z
updated_at: 2026-09-05T09:13:24Z
---

## Three defects, two of them mine, all read off the source

**Source fact.** `prf:trace-ratio-observable`: `|ℳ_q|² = |skein_amp|²·|tr(par)/tr(dau)|²`
with `skein_amp = q^{1/2} − q^{−1/2}`, *"the Skein amplitude at the beta-decay vertex"*.
So `s` enters the rate squared **once**. Nothing else carries an `s`: `[2]_q` is
full-scale, the pair-Skein denominator is the half-scale **sum**, `Q ∝ q − q⁻¹`.

### D1 — mine, mechanical, 92×
`substitutionRateFactor := (weakVertexTrace q)²/(sSq q)²` and `sSq` **is** `s²`, so it
computed `|W|²/s⁴`. `11875.4418937 → 129.405107404`; error `1/s² = 91.7694991484`.
A name reading "s, squared" consumed as "s".

**Verdict unchanged, evidence improved.** The qou-ix74 assertion read "every substituted
half-life below 0.1 % of observed" — true only of the wrong factor. Measured at the
right power all six land at **0.8–0.9 %** (~110× too short, against a wanted 10–17 %
shortening), and the assertion is now a two-sided band that fails if the numbers move.

### D2 — mine, a RETRACTION
qou-q2l7 claimed the *order* of the substitution factor was derived (`96²` vs `11875`).
`lim_{q→1} |W|²/s^k = +∞` for every `k ≥ 1` because `W(1) = 1/4 ≠ 0`, so there is no
leading constant. `−96` belongs to `(J−1)/s²`, whose numerator vanishes (`V_K(1) = 1`
for every knot). Two different ratios. Every exact identity of qou-q2l7 survives.

### D3 — the corpus's, an AUTHOR DECISION, not picked
`prf:hadron-half-life` item 1 says `|𝒲|²` replaces `s²`; item 3 retains `s²` inside
`|ℳ_q|²`; both multiply into the same rate. (A) double-count ⇒ rate too small by `s²`,
half-lives too long by ~92×; (B) "replaces" is wrong, a factor was added; (C) item 3 is
stale and the tables match neither formula. Recorded as an `authorNotes` caveat on the
block. No figure here depends on the choice.

## Artifacts
Producer `computations/markov/beta_rate_skein_power_audit.py` (9/9); witness
`beta-rate-skein-power-audit.witness.json`. Lean: `substitutionRateFactor` re-powered,
`substitutionRateFactor_near_one_hundred_thirty` +
`..._denominator_vanishes_numerator_does_not` +
`..._has_no_classical_leading_value` replacing the three withdrawn envelope theorems.
Three producers re-run green, two audit docs corrected in place, three beans annotated.
PR #6793.
