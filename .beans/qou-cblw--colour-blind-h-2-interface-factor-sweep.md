---
# qou-cblw
title: 'p-n interface factor: colour-BLIND z - h/2 where canonical is z - h*(1/2 - delta/4)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T21:35:00Z
updated_at: 2026-08-25T21:35:00Z
---

Found 2026-08-25 while validating an exact-rational evaluation pipeline for the
Habiro chi cache (bean `qou-lrnd`). My own first implementation had this exact
bug, which is how it surfaced: I mapped every non-`sigma` crossing to
`-h/2` and all 11 cached deuteron characters came back wrong — by a
*different* ratio per partition, not a global scale, which is the signature of
one wrong factor rather than a normalisation slip.

## The two forms

    colour-WEIGHTED (canonical)   z - h*(1/2 - delta/4)
    colour-BLIND                  z - h/2

with `z = markov_z(q) = q^3/(q^2+1)` (convention D), `h = q - 1/q`, and

    delta = flavor_split_leading(q) = (q-1)^2 * (1 - q^-4) / 3

(`computations/_li_2_q_util.py`, and `flavor_split_leading_sym` in
`computations/tr_m_algebraic_q.py`). Note delta is a RATIONAL function of q —
which is what makes an exact-arithmetic evaluation of the whole atom possible.

AGENTS.md records the owner ruling of **2026-08-15 (R3): `bring_color_weighted`
is the canonical p/n convention.** So `z - h/2` is wrong wherever canonical is
intended.

## Why it is a trap rather than a typo

`closed_form_tau_M.py` (~lines 305-330) documents the mechanism in its own
comments: `canonical_interface_kinds(...)` by default emits only
`{positive, negative, averaged}`. A consumer dispatching on those three and
mapping `averaged -> z - h/2` **silently gets the colour-blind factor**. In the
file's own words it "fails by returning a slightly smaller number rather than
by raising". The `averaged_weighted` label exists, and is opt-in via
`weighted_labels=True`, precisely so a consumer either handles the weighting or
raises on an unknown kind.

`interface_factor(kind, q)` handles only the three blind kinds and raises on
anything else — so it **cannot** emit the weighted value at all.

The Rust side documents both forms in
`tools/hecke-engine/src/color_weight.rs` (`z - h/2` for `strict_averaged`,
`z - h*(1/2 - delta/4)` for `bring_color_weighted`), with the comment that the
delta-aware value "lives in the factor layer, not the label layer".

## Scope of the sweep

A background agent is sweeping `computations/`, `tools/`, `content/` for:
1. p-n / averaged interface factors computed as `h/2`;
2. three-kind `{positive, negative, averaged}` dispatches with no
   `averaged_weighted` branch in factor-computing code;
3. callers of `canonical_interface_kinds` that omit `weighted_labels=True`
   and then compute a factor from the labels;
4. Rust callers hardcoding the strict/blind form where canonical is intended.

**Not every `h/2` is a defect.** Deliberate `strict_averaged` implementations,
C-vs-D comparison probes, and tests asserting the blind value on purpose are
legitimate and must be separated out. That separation is the substance of the
sweep, not the grep.

## Open

Sweep results pending. Any genuine finding changes a NUMBER, so each needs the
usual treatment: confirm the site intends canonical, check whether a committed
witness carries the blind value, and fix at the producer.
