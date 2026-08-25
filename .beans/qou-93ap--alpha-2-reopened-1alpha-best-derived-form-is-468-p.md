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

## The block's open question is now answered — it is κ, not the truncation

[`em-coupling-chern-simons`](../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md)
states the residual honestly and names two candidate causes: *"Either the
Gram-determinant identification of κ is wrong, or the order-$\delta_{CS}^2$
truncation omits higher-order contributions."*

Measured (`_alpha_em_inv_derived(q, order=2)` vs the exact resummation):

| effect | size |
|---|---|
| resumming the tower (all orders vs order-δ²) | **11.06 ppb** — identical at both pins |
| muon → proton pin | **79.17 ppb** — identical for both forms |

The omitted higher orders are worth **11 ppb against a ~400 ppb residual** —
1/36th of the gap. The truncation is therefore **not** the explanation, and by
elimination within the block's own two options the defect is **κ**. That
matches the block's own observation that exact CODATA matching needs
κ ≈ 1.8878 against Witten's 1.722, a ~10 % discrepancy, and κ is precisely the
quantity still carried as a `sorry`.

Both effects being invariant across the other variable is a structural check
on the measurement, not a coincidence: the tower ratio and the pin enter
multiplicatively.

## Live content is NOT over-claiming — scope note

Checked, because the correction above could be read as broader than it is.
`em-coupling-chern-simons` says κ "was never closed";
`docs/observable-sector-tracker.md` records α_EM as
**"PARTIAL … derived form OPEN"**. The false *"resolved at 6.7 ppb"* lived
only in `computations/DERIVATION-STATUS.md`. The paper content was right.

## Next, needing approval (paper content)

`em-coupling-chern-simons.md` and `em-coupling-projection-table1-data.md`
quote `137.035944` / `399 ppb` / `CODATA 2018`. Those are the truncated,
muon-pinned figures against the superseded edition; current is
`137.0359350939756` / **468 ppb** / CODATA-2022. Correcting them is a
content-block edit — `qa-sweep` + the render-QA gate apply — and it changes
numbers inside a proposition, so it is not an idle-pass fix.
