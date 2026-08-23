---
# qou-w701
title: 'Deferred verification came due and failed: the a_operator pn interface is colour-weighted on one leg only'
status: completed
type: task
priority: normal
created_at: 2026-08-23T22:31:23Z
updated_at: 2026-08-23T23:26:58Z
---

Commit **`3dcf933c5`** (2026-08-10, *"a_operator: the pn interface is
colour-weighted too"*) rewrote five interface constructions in
`a_operator_gauge_align` from colour-blind `-h/2` to
`_d_pn(h) = -h(1 - δ/2)/2`, and changed `a_operator_categorical`'s pn
descriptor to match. Its own closing paragraph deferred a verification:

> *"NOT re-verified here: the 1.5e-49 reconstruction figure itself. The claim
> now rests on a different interface than when it was measured, so it needs a
> fresh run before it is cited again — the expectation is that it stays exact,
> because both sides moved together, but expectation is not measurement."*

That fresh run has now happened. **The expectation is refuted.**

    cyclic-intertwiner-verify.witness.json
      HEAD (computedAt 2026-06-30)   h6 max_abs_residual 6.7123064e-49
                                     h9 max_abs_residual 3.3561532e-49
                                     PASS (tolerance 1e-25)
      NOW                            h6 max_abs_residual 0.0011504265
                                     h9 max_abs_residual 0.00057521327
                                     FAIL

**46 orders of magnitude.** Structural, not numerical, and measured as such:
`QOU_COMPUTE_DPS` = 50, 60 and 70 all give 0.0011504265 / 0.00057521327 to
every printed digit. Precision is exonerated. (h6 is exactly 2x h9 at all
three, which is its own structural signature.)

## The same commit predicted this scale

It states that leaving the interfaces colour-blind *"would have degraded a
verified 1.5e-49 result to the ~1e-4 scale of the colour weighting,
silently."* The measurement is 1.15e-3 — that scale. The colour-weighting
delta is

    |-0.10445824776972629 - (-0.10453014939781966)| = 7.19e-5   (~6.9e-4 relative)

same order as the residual. So **both sides did NOT move together**: one leg of
the pairing `chi^lambda(W . I . beta) = Sum Tr[A . (rho_mu (x) rho_nu)]` is on
the colour-weighted interface and the other is still colour-blind.

## Why nothing caught it for two weeks

`cyclic_intertwiner_verify.py` changed once since its witness was computed —
`726eecfe6` added `set_compute_dps()`, nothing semantic. **The producer's own
hash barely moved.** What moved is what it IMPORTS, and the self-staleness axis
does not follow imports: it compares a witness against its producer's hash, not
against the transitive closure of that producer's dependencies.

That is a gap in the staleness family, not an oversight by anyone. It took
RUNNING the thing. Worth considering whether `scriptHash` should cover a
producer's first-party imports, at least for producers that declare no
`upstream_witness_hashes` — but note that would re-stale a large fraction of
the corpus on any shared-module edit, so it is a design question, not a patch.

## What is actually needed

Identify which leg of the pairing is still colour-blind and bring it onto
`_d_pn`. The two candidate sites are the `W . I . beta` character side and the
`rho_mu (x) rho_nu` trace side; `3dcf933c5` changed five constructions and the
descriptor, so the unconverted one is most likely a sixth construction it
missed, or a consumer rebuilding the interface locally.

Do NOT widen the 1e-25 tolerance. A 1e-3 residual against 1e-49 is not a
tolerance question, and the exactness of the original result is the whole
claim.

The 6.7123064e-49 figure at the colour-blind interface is the BEFORE half and
should be kept, not deleted — it is worth keeping precisely because a commit
staked a prediction on it and the prediction failed.

Found on `claude/mass-table-comprehensive-triage` while draining self-staleness;
tracked alongside the branch's other recorded assertion failures in qou-60r9.


---

## RESOLVED 2026-08-23 (a819eb1ab) — it was a SIXTH interface, in the verifier

    h6 max_abs_residual   0.0011504265    ->  6.7076893e-49
    h9 max_abs_residual   0.00057521327   ->  3.3538446e-49

The bean's two candidate sites were "the `W·I·β` character side or the
`ρ_μ⊗ρ_ν` trace side", with the guess that the unconverted one was "a sixth
construction it missed, or a consumer rebuilding the interface locally". It
was both at once: a sixth construction, in a consumer.

`computations/a_operator/cyclic_intertwiner_verify.py:67`

    I_if = mats[n_inner - 1] - (h / 2) * mp.eye(dim)      # colour-BLIND

`3dcf933c5` swept the five `I_iface` sites in `a_operator_gauge_align.py`
(lines 340, 568, 680, 780, 863). This one lives in the VERIFIER, so the sweep
never reached it — leaving the `A` side colour-weighted (built by
`gauge_aligned_A_combiner_general_cyclic`, which goes through the converted
module) and the `I` side blind.

Fixed to `mats[n_inner - 1] + g._d_pn(h) * mp.eye(dim)`. Calling the single
definition rather than restating `-h * (1 - delta/2) / 2` is the point: a
second copy of that formula is exactly how the two legs drifted apart, and the
underscore is worth crossing to keep one source of truth.

## The prediction was exact

`3dcf933c5` warned that leaving an interface blind *"would have degraded a
verified 1.5e-49 result to the ~1e-4 scale of the colour weighting,
silently."* Measured: **1.15e-3**, with the colour-weighting delta 7.19e-5
(~6.9e-4 relative) at the same order. The commit both deferred the
verification and named the failure mode it would show.

## What this does NOT close

The structural gap that let it sit for two weeks. `cyclic_intertwiner_verify.py`
changed once in that time — `726eecfe6` added `set_compute_dps()`, nothing
semantic — so its own `scriptHash` barely moved, re-running it was "correct",
and **the drift axis does not follow IMPORTS**. Nothing in the staleness
family could have surfaced this; it took running the thing.

Making `scriptHash` cover a producer's first-party imports would catch this
class, but would also re-stale a large fraction of the corpus on any
shared-module edit. That is a design question, not a patch, and it remains
open.

A cheaper partial measure worth weighing: when a commit DEFERS a verification
in its own message — "expectation is not measurement" — that is a bean, not a
paragraph. This one was findable the moment it was written down.
