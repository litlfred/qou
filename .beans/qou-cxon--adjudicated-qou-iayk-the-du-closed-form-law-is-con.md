---
# qou-cxon
title: 'ADJUDICATED (qou-iayk): the D(u) closed-form law is convention-C by construction and must be re-derived in D'
status: todo
type: task
priority: normal
created_at: 2026-08-23T19:34:02Z
updated_at: 2026-08-23T19:35:38Z
---

Adjudicates `qou-iayk`, which blocked the Habiro convention-D regeneration on
2026-08-21 because the fresh values break a landed closed-form law.

**Verdict: reading (b) confirmed — the law must be re-derived in D. Reading (a)
(producer defect) is disfavoured by an independent computation.**

Audit: `docs/audits/2026-08-23-d-u-closed-form-is-convention-c.md`.

## The decisive fact

`d_u_closed_form_proof.py:18` defines `z = 1/(q^(1/2) + q^(-1/2))` — which is
`sqrt(q)/(q+1)`, **convention C**, in the detector-blind spelling from #5124.
The proof's own lines 339-340 derive the `(1+u^2)^(3A-1)` factor by *clearing
the denominator of that z*. So the law encodes C structurally:

    z_C = u/(1+u^2)   at q=u^2  ->  (1+u^2)^(3A-1)   <- the landed law
    z_D = u^6/(1+u^4) at q=u^2  ->  (1+u^4)^(3A-1)   <- the D-frame law

D-frame output was being tested against a C-frame law.

## The "irregular offset" is not irregular

Fitted on D/T/3He, predicts 4He exactly: `delta = 13 - 6Z - N`, so the fresh
exponent is `12Z + 20N + 14` — 4-for-4, small integers, same shape as the
C-frame `18Z + 21N + 1`. The "3He matches while T is off by 5" puzzle is where
that form crosses zero at (2,1).

Three parameters against four points is ONE degree of validation. This is
evidence the fresh data is structured (bearing on reading (a)); it is NOT a
derivation. Do not wire `12Z+20N+14` as canonical.

## Independent confirmation

`markov/peel_anchor_identification_probe.py` — separate code, its own landed
assertion `peel_denominator_is_convention_D` — re-run on this tree gives the
deuteron peel denominator `192*q**23*(q**2+1)**3`. **192 is exactly the fresh
Habiro deuteron prefactor**; the C value is `2^(2A+1) = 32`; `192/32 = 6`, the
uniform factor qou-iayk recorded as unexplained.

## Open sub-question this does NOT close

The `2^(2A+1)` prefactor is derived by crossing-counting, which is
convention-FREE — yet it moves 32 -> 192. So crossing-counting alone does not
determine it. That needs a real derivation, not a re-count.

Likewise the `u^shift` stays open, as the proof itself says it always was:
*"left as an open structural question (depends on the Hecke-NF reduction)"*.

## qou-iayk was right to revert

It declined to land values it could not justify. What was missing was the
justification, from a source it did not consult. The regeneration should land
**together with** the re-derived law, or the same mismatch recurs.
