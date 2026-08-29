---
# qou-pi4m
title: 'GAP: _li_2_q_util yekutieli norm (sqrt(q)+1/sqrt(q))^2 - is it 1/z_C^2 or [2]_q+2'
status: completed
type: task
priority: normal
created_at: 2026-08-25T01:22:22Z
updated_at: 2026-08-25T07:37:29Z
---


## The site

`computations/_li_2_q_util.py` ~line 770, in the Yekutieli / Family-A
Borromean h^2 extraction helper:

    sq   = mp.sqrt(q)
    sqi  = mpf(1) / sq
    ...
    norm = (sq + sqi) ** 2
    return jones / norm

Found while migrating this module's two `z` definitions to convention D
(PR #5738). **Not migrated — the intent is genuinely ambiguous, and
guessing would move a published number on a coin flip.**

## Why it is ambiguous

`(sqrt(q) + 1/sqrt(q))^2` has two readings that are numerically
identical but conventionally opposite:

1. **`1/z_C^2`.** Convention C is `z_C = 1/(sqrt(q) + 1/sqrt(q))`, so
   this is exactly `z_C^-2` and `jones/norm = jones * z_C^2`. Under that
   reading it is a **convention-C Markov normalisation** and must become
   `jones * z_D^2` — a substantial change, since
   `z_C^2 = 0.24932` and `z_D^2 = 0.37539` at the proton pin.
2. **`[2]_q + 2`.** Expand it: `(sqrt(q) + 1/sqrt(q))^2 = q + 2 + q^-1`,
   which is rational, has no half-integer power, and equals `4` at
   `q = 1`. The docstring's own arithmetic is `(3/16) x 4 = 3/4`, and it
   describes the operation as "renormalized to the H_4 Wedderburn sum".
   Under that reading it is a **dimension count**, convention-independent,
   and must be left exactly as it is.

The docstring supports reading 2. The algebraic form supports reading 1.
They cannot both be the intent.

## Why the detectors do not settle it

- `convention-c-producer-audit.py` does not list this site: it keys on
  `z`-named assignment targets, and this binds `sq`/`norm`.
- The audit's own "C-SPECIALISED CLOSED FORMS" pass — which exists for
  precisely this failure mode ("a square root in one is z_C showing
  through") — flags only
  `computations/probes/qbeta_5two_categorical_markov_volume_probe.py:133`
  and misses this one.

So a clean detector run is not evidence about this site, in either
direction.

## How to settle it

Do not settle it by reading the code again — both readings survive that.
Settle it against the source the docstring cites,
`yekutieli_borromean_h2_extraction.py`, and against
`prop:mass-endomorphism-tower` / the Family-A linking-weight identity in
`lambda-scale-substrate-form.lean`:

- If the `4` in "(3/16) x 4" is the **q -> 1 limit of the normaliser**,
  reading 2 is right and the site is convention-independent. Rewrite it
  as `q + 2 + qi` anyway, so the square roots stop reading as z_C to the
  next agent and to the next detector.
- If the normaliser is the **Markov loop value**, reading 1 is right, it
  is a live convention-C site the audit never saw, and it needs
  `z_D^2 = q^6/(q^2+1)^2`.

Either way the fix includes removing the `sqrt`: under D nothing in this
module should carry a half-integer power of q, and leaving one here
guarantees this question gets re-asked.

## Blast radius

`per_knot_density_borromean` / `vol_density_borromean` and the
`linking_weight_family_a` path. Note this is a DIFFERENT cone from the
`load_q_50dps` `z` migrated on PR #5738 — measured there, the
`vol_density_*` functions take `q`/`q_inv` and never touch that `z`. This
helper is how a convention question could still reach the mass-density
path, which is what makes it worth settling rather than leaving.
