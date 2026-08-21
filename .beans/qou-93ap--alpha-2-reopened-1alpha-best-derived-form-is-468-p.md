---
# qou-93ap
title: 'ALPHA-2 reopened: 1/alpha best derived form is -468 ppb, not resolved at 6.7'
status: todo
type: task
created_at: 2026-08-21T15:13:57Z
updated_at: 2026-08-21T15:13:57Z
---


## What happened

`computations/DERIVATION-STATUS.md` carried, in three places, that the
fine-structure residual was *"resolved at 6.7 ppb … no further derivation
required"*. The form it cited —
`1/α = 45[3]_q(1 + δ_CS + 8q δ_CS²)`, `δ_CS = ℏ_q⁴[5]_q` — is **ruled out
structurally** by `archimedean-functor-uniqueness-context` as "a legacy
PSLQ-empirical conjecture" requiring "arbitrary integer ratios … from a
non-pentagon source". Corrected in PR #5361.

## State, measured (proton pin, CODATA-2022)

| form | status | residual |
|---|---|---|
| bare `q[9]_q[10]_q` | derived | −0.155 % |
| bare + `2/(3π)` zero-mode (superseding) | derived | −4259.7 ppb |
| CS tower resummed (registry) | derived | **−467.6 ppb**, structural |
| `45[3]_q(1+δ+8qδ²)` | **ruled out** | 2.6 ppb |

Reproduce: `python3 computations/alpha/alpha_em_form_comparison_probe.py`.

## What is actually open

The best *derived* α⁻¹ is **−468 ppb**, and `pyhecke/constants.py` argues that
residual is **structural**: the CS tower is geometric with ratio
`c₁κ ≈ 2.7e-3` and sums in closed form, so no further orders can close it.
Closing this needs a *new mechanism*, not more orders of the existing one.

## What NOT to do

- **Do not re-wire the `45[3]_q` form.** Its residual is the smallest of any
  form here, which is the signature of a fit, not evidence for it. It is
  excluded structurally, not merely superseded.
- **Do not read the superseding zero-mode form as an improvement.** At
  −4260 ppb it is 9× worse than the CS tower it supersedes. "Superseding"
  there means derivationally cleaner, not numerically closer — worth keeping
  straight before anyone quotes it as progress.

## Anti-fit note

This item is a worked example of why the anti-laundering rule exists: an
empirical fit sat in a live status doc as a closed derivation for months,
cited under a proposition label that contained no such formula, with all its
supporting audits already deprecated.
