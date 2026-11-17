---
# qou-6poy
title: 'GAP-3: derived R(q,x) q-difference weight kernel (formalize-first)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T23:11:26Z
updated_at: 2026-10-04T15:19:34Z
parent: b9cj
---


## Reference

Gap map + anti-fit checkpoint: [`docs/workplans/2026-07-11-mnk-derivation-gaps.md`](../docs/workplans/2026-07-11-mnk-derivation-gaps.md). Parent: `qou-v0yw` (M_n(K) closure, ungated 2026-07-11 via #3607). Coordinate with #3545/#3585/#3588/#3549/#3548 before solo compute.

## Update 2026-07-11 — GAP-3 is now THE frontier (others resolved/bridged)

With GAP-1 (2-body ✓ #3630), GAP-2/2b (3-body localized, many-body = α-cluster ✓ #3633/#3638),
GAP-4 (= #3551 ✓), the single genuinely-open research-grade leg is the derived q-difference
kernel R(q,x). Bridge: docs/audits/2026-07-11-gap4-alpha-bridge-gap3-frontier.md.
**(Superseded in detail by the 2026-07-12 currency note below: R(q,x) is already derived as the
τ-recurrence — GAP-3 = the mature z2bn thread, not a from-scratch derivation.)**

## Update 2026-07-12 — GAP-3 = the MATURE `z2bn` thread (anti-duplication); my framing was under-informed

Corpus-grep before starting a GAP-3 probe found GAP-3 is NOT greenfield — it IS the active,
deeply-developed bean `z2bn` ("Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x)").
The corpus is well ahead of this bean's original "no kernel reaches 5%, derive from scratch" framing:

- **R(q,x) is already derived + formalized:** the lever-1 binding kernel is the depth-2, det=1
  recurrence `R(q,x) = x² − τx + 1`, with `τ(q₀) = 2.6424` (selection-rule anchors, #2612) and
  characteristic roots `λ₊ = 2.1846` (the extensive-growth eigenvalue that sources the A-scaling
  binding) / `λ₋ = 0.4577`. Formalized sorry-free: `QOU/Mass/BindingRecurrenceSpectral.lean`
  (`lambdaPlus_gt_one`: `τ > 2 ⇒ λ₊ > 1`). Probe: `binding_recurrence_spectral_bridge_probe.py`.
- **The frontier is reduced to ONE number: `τ = tr B`** — its geometric monodromy derivation is
  the owner-gated DG (sibling `lever1-trB`), now UNGATED (#3607). This connects directly to the
  s5-so3 keystone (τ is the fibre-trace the keystone's `W_λ` index must reproduce).
- **Kill-switch:** magic-A ⁴He +5.87% (finite-truncation residual, not yet closed).

**So GAP-3 = z2bn. Do NOT open a parallel probe.** The genuine open work is the geometric
derivation of `τ = tr B` (the s5-so3 / Beasley–Witten localization route, #2524/#2503), a
multi-session formalize-first effort best done with the Lean env online. This bean (qou-6poy) is
now a pointer to z2bn; the two-scale substrate targets (per-bond `b*`, per-α-bond `b_αα`) from the
GAP-1..4 arc are the binding-side inputs that `τ = tr B` must reproduce.

## Round 57 Progress (PR litlfred/qou#8286)
- Status updated to `in-progress` (`litlfred/qou#8286`, C1 `6c7a20f3289e7e0671ce65ef402e1a06fd77c443`, C2 `dce9c51d4a6cd8f2253c078180b4b77a6f7c1ed0`).
