---
# qou-6jty
title: RETRACTED before it was ever filed — the "two convention-D tr_M routes disagree by 0.92" question is closed, and was closed in a docstring since 2026-05-17
status: completed
type: task
priority: normal
created_at: 2026-08-24T23:51:25Z
updated_at: 2026-08-25T00:05:00Z
---

## What this bean was going to say

That `cross_check_trM_wenzl_lr_1ppb` shows **two current, convention-D routes to
the atomic Markov trace `tr_M` disagreeing by 0.92 relative on 12 of 12
pair-tests**, that this was neither staleness nor a convention mismatch (both
having been chased and closed by measurement), and that it therefore constituted
a substantive disagreement between independent derivations deserving research
attention.

**It is none of those things, and the bean was never filed.** It is recorded here
in its corrected form because the error is more instructive than the finding
would have been.

## Why it is wrong

The checker does not compare two routes to one quantity. It compares
`|tr_M(β_canonical(Z, N))|` against `|tr_M(β_p ⊗ β_n ⊗ …)|` — **different
objects**. The Wenzl LR identity applies to tensor-product (disjoint) braids; the
canonical atomic braid is not one, because it carries the inter-nucleon arc
crossings the disjoint product omits. The ~0.9 *is* those crossings.

`rho_k_full_via_wenzl_lr.py` says this in its own docstring, dated **2026-05-17**,
and even states the expected size: *"The two diverge by ~80 % relative on D, T,
³He."* A `1e-9` tolerance was being applied across a documented inequality.
`atomic_mass_via_rho_k` layer 4 had already been disabled over it.

Closed on `main` by `7823271e66` (bean `qou-u6n2`, a different session), which
marks those pair-types `compares_same_object: false`, attaches a `scope_note`, and
excludes them from `any_diverge` — leaving the genuinely comparable pair asserted
at `max |Δ_rel| = 4.4e-50`.

## The reasoning error, stated so it is reusable

I formed two candidate explanations — the Wenzl/LR leg is C-era; its witness is
stale — and refuted both by measurement. Refuting them took real work, including
two false positives of my own in opposite directions (a degraded re-run with the
Rust binary absent, reporting `available: 0/4`; then an unmasked
`duration_ms_total` where 6 of 291 fields moved and **no** `rho_k` value did).
Having closed every explanation *I had thought of*, I concluded the effect was
real.

**That is an argument from exhaustion of my own hypothesis list.** The
corpus-grep checklist exists because that list is not the corpus. I ran the
checklist on the cross-check's identifiers and never on the producer supplying
the outlying leg — the one file whose first 55 lines answer the question outright.

The near-miss is the point: the work that made the wrong conclusion feel earned
(two refutations, each correcting a prior error of mine) is exactly what made it
persuasive. Effort spent eliminating candidates is not evidence that the candidate
set was complete.

## Corrected artifacts

- `.beans/qou-2wtx…` — retraction appended; the seminormal-leg root cause
  (191 % → 6.7e-8) and the peel regeneration are unaffected and stand.
- `docs/audits/2026-08-24-peel-witness-convention-d-regeneration.md` — the
  consumer-survey row and its section rewritten from "⚠ WORSE / not established"
  to **SCOPE**, with the docstring quoted.

## Nothing is open here

No follow-up. Do not re-open this as a research question; if a future reader sees
`markov_peel_vs_wenzl_lr` diverging at ~0.9, that is the designed behaviour of a
comparison between a canonical braid and a disjoint product.
