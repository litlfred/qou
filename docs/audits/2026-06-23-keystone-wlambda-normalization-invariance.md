# The C1 normalization fork is a no-op for the generation ratio (Lean-proved, then confirmed)

**Date:** 2026-06-23
**Branch:** `claude/keystone-wlambda-norm-invariance-2026-06-23`
**Status:** Formalize-first result (Lean sorry-free) + numerical confirmation. Bounds the PR #2524 C1 question. No fit; nothing wired.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Answers:** the C1-normalization fork raised on [PR #2524](https://github.com/litlfred/qou/pull/2524#issuecomment-4780936341)
**Lean:** [`QOU/BraidKnot/WLambdaNormalizationInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaNormalizationInvariance.lean) (lean-direct exit 0, v4.24.0)
**Script:** [`docs/audits/scripts/keystone_wlambda_norm_invariance_check.py`](scripts/keystone_wlambda_norm_invariance_check.py)

## The question (from #2524)

The Beasley–Witten/RT geometric mechanism produces `W_λ = d_q²/D²` (`D²=Σ_λ d_q²`),
the **true Plancherel measure** (sums to 1). The keystone consumer uses
`W_λ = d_q²/[n]_q!`, which sums to `Z(n)=D²/[n]_q! ≠ 1`. Does swapping to the
geometric normalization **change a prediction** (falsifiable substance) or **not**
(exposition / tautological re-naming)?

## Formalize-first answer (Lean, before any probe)

Per the owner directive *"need lean prove first"*, the structural fact is proved
in Lean over a generic field — `d_q : ι → R`, `D² = Σ_λ d_q²`, `F = [n]_q!`:

| theorem | content |
|---|---|
| `wPlanch_eq_global_factor` | `d_q²/D² = (F/D²)·(d_q²/F)` — the two normalizations differ by **one λ-independent global factor** `F/D²` |
| `wPlanch_sum_one` | `Σ_λ d_q²/D² = 1` (geometric = genuine probability measure) |
| `wKey_sum_eq_Z` | `Σ_λ d_q²/F = D²/F = Z(n)` |
| `ratio_invariant` | **same-block ratios are normalization-invariant** — `F/D²` cancels |
| `ratio_eq_qdim_ratio` | both ratios `= d_l²/d_m²` (the bare q-dimension ratio) |

Because the change is a single λ-independent rescale, **any same-`n` ratio of
weights is invariant** under the choice. The lepton generations live in the same
block `n=5` — electron `(3,1,1)`, muon `(3,2)` — so the muon/electron mass
**ratio** is invariant. The choice can move a number only through a cross-`n` or
absolute (un-normalized) use of `W_λ`.

## Numerical confirmation (n=5, q₀)

`keystone_wlambda_norm_invariance_check.py` (50 dps), confirming each Lean theorem:

| quantity | value |
|---|---|
| `Σ_λ wPlanch` | `1.0` (✓ `wPlanch_sum_one`) |
| `Σ_λ wKey` | `0.982224…` `= Z(5)` (✓ `wKey_sum_eq_Z`) |
| `F/D²` (global factor) | `1.018098…` |
| `wPlanch` ratio μ/e `(3,2)/(3,1,1)` | `0.70432327509478738188…` |
| `wKey` ratio μ/e | `0.70432327509478738188…` |
| bare `d²` ratio | `0.70432327509478738188…` |
| **\|wPlanch ratio − wKey ratio\|** | **`0.0`** (to 1e-40) |

The same-`n` generation ratio is **identical to 30 digits** under both
normalizations. The only shift is for an absolute use: exactly `F/D² = 1.0181`
(a 1.81 % rescale at n=5; per-`n` the defect `1−Z` is `0.0126` at n=3 and
**sign-flips at n=7**, [`keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py)).

## Verdict (critical distance)

For the **generation mass ratio** — the observable the keystone is meant to
deliver (m_μ/m_e and the generation split) — the geometric `d_q²/D²` reframing
is **a no-op**: it cannot be confirmed *or* falsified there, so for that
observable it is **exposition** (a true-Plancherel re-naming of `W_λ`), **not a
new prediction**. This is the concrete form of the tautology risk the s5bb
background-agent scoping flagged: the geometric route's value-add is real
*structurally* (it supplies the index mechanism and the `D²` normalizer) but is
**invisible to the same-`n` ratio**.

The C1 choice becomes a genuine, falsifiable prediction **only** if the consumer
uses `W_λ` **absolutely** (un-normalized) or **across different `n`** (different
generations / isotopes at different block sizes) — there the shift is exactly
`Z(n)`, with the `n=7` sign change as the sharp signature. So the productive
question for #2524 is narrowed: *does the mass/binding consumer use `W_λ` as a
same-`n` weight (→ C1 is exposition) or absolutely/cross-`n` (→ C1 is a `Z(n)`
prediction)?* That is now a definite, checkable question rather than an open fork.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [PR #2524](https://github.com/litlfred/qou/pull/2524) — the Beasley–Witten geometric `W_λ` = `d_q²/D²` construction + the C1 finding this bounds.
- [`keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) — the `Z(n)` defect (sign-changes at n=7).
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the `144·C(n)=−n(n−1)(2n−13)` defect closed form (sibling keystone Lean).
- `docs/coordination/s5-so3-keystone.md` — keystone ledger.
