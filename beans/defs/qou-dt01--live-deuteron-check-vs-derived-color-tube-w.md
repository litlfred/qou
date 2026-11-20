---
# qou-dt01
title: 'STILL LIVE (re-opened; ml1i was bulk-closed by hygiene sweep 43a8ec43): the deuteron binding check against the DERIVED color-tube W. Of ml1i''s two tests only (2) is genuinely moot — test (1) was never run.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T15:05:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## Why this is re-opened

Bean `qou-ml1i` was marked `completed` by the beans-hygiene sweep `43a8ec43`
("42 more beans drained via PR status"). That sweep was right about half of it
and wrong about the other half.

### (2) MOOT — correctly retired

The queued test was: *"does the derived `W` regularise the ν_SDP indefinite
Gram? a negative would be evidence against `ρ_F = ν_SDP`."*

That evidence arrived by a **stronger route** while this branch was idle. The
sibling audit
[`2026-08-02-rho-f-cap-no-derived-origin.md`](../docs/audits/2026-08-02-rho-f-cap-no-derived-origin.md)
finds `ρ_F(⁴He) = 1.889` — **not an integer**.

`ν_SDP` is by definition a **multiplicity** (the dimension of a saturating
projection in the Wedderburn decomposition), hence an integer. A non-integer
`ρ_F` therefore **refutes** `ρ_F = ν_SDP` outright, rather than merely leaving it
underived as the 2026-06-21 audit had it. Do **not** run test (2) for that
purpose — the question it was designed to answer is settled.

### (1) LIVE — never run, and it matters

The deuteron binding check against the derived weight tensor
`W_A : W_H = [1]_q : [5]_q`. Explicit tensors are already computed and committed
in [`computations/color_tube_derived_W_explicit.py`](../computations/color_tube_derived_W_explicit.py):

| channel | `W(same-color)` | `W(diff-color)` |
|---|---|---|
| `I=1` (pp, nn, pn_sym) | `0` | `1/6` |
| `I=0` (deuteron) | `0.165485393155` | `0.083923970089` |

**Blocker:** needs the per-block Markov trace with the refined generator
(`pyhecke_native`), which was unavailable in the sandbox where `W` was derived.
Runnable as-is on a machine with the engine — the tensors above are its inputs.

## Why skipping it forfeits something real

The deuteron binding was **deliberately excluded** from the whole derivation
chain (`8 → 2 → 1 → 0` free parameters; PRs #4506, #4510) precisely so it would
remain an **independent check**. Had the A/H mix been fixed against it, the check
would have been circular and the result a fit. Not running it forfeits the only
non-circular test the chain was designed to earn.

**Anti-fit (standing):** if the check misses, report the miss as a scope-(a)
finding. Do **not** re-tune the mix.

## Corroboration worth noting

The chain's one named assumption — weighting isotypic summands by **quantum**
rather than classical dimension — is independently supported by commit
`e0b42a8e`: the Ocneanu/Markov trace parameter **is** the fibre's quantum
dimension (`[N]_q` for an `N`-dimensional fibre). Different route
(subfactor/Ocneanu vs the Clebsch–Gordan side used here), same principle.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8332, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
