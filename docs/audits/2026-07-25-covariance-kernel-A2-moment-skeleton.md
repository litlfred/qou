# Covariance-kernel epic (`qou-x631`) — the surviving structure: the A2 moment skeleton

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-moment-skeleton-2026-07-25` · **Tier:**
structure isolation + provable sub-target · **Discipline:** scope-(a); no fit; nothing wired; no
`c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Context

The A2 *pointwise* reduction `Cov_Planch(H_s, ω₃) ≤ 0 ∀s>0` is **false for n≥29**
([correction](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)). This note isolates
what **survives**, explains *why* the pointwise route died, and hands the next attempt a concrete
provable sub-target.

## The moment skeleton (robust)

With `ν_v = Cov_Planch(N_v, ω₃)`, define `M_k = Σ_v v^k ν_v = Cov_Planch(Σ_□ h^k, Σ_□ h²)` (the
constants in `ω₃ = Σh² − n² − C(n,2)` drop from the covariance). Then

> `M_0 = 0`, `M_2 = |C₃| = n(n−1)(n−2)/3`, and **`M_k > 0` for all `k = 1..12`** — verified `n ≤ 40`.

This is **robust**, in sharp contrast to the pointwise property, which failed at `n = 29`.

## The generating-function dichotomy — why the pointwise route died but the moments survive

Both sides live in one generating function `G(t) = Σ_v ν_v e^{tv} = Σ_{k≥1} t^k M_k / k!`:

| half-line | object | sign |
|---|---|---|
| `t > 0` (increasing weight) | `G(t) = Σ_{k≥1} t^k M_k/k!` | **> 0** — every term positive (`M_k>0`); robust |
| `t = −s < 0` (decreasing weight) | `G(−s) = Cov_Planch(H_s, ω₃)` | terms **alternate**; goes positive for `n≥29` |

So the pointwise failure and the moment survival are the **same generating function on opposite
half-lines**. The A2 weight `ln(v)` is *increasing* (sits with the surviving `t>0` / power family), and
`A2 = −Σ_v ln(v) ν_v ≤ 0` holds robustly. But `ln` is *concave* — not a positive combination of the
powers `v^k` — so `M_k>0` does **not** by itself close A2; that needs the global (full-integral)
argument the correction identified.

## The proof lead — even-`k` moments are provable

For **even** `k`, both `Σ_□ h^{k}` and `Σ_□ h²` are shifted-symmetric functions on Young diagrams, so

> `M_{2j} = Cov_Planch(Σ h^{2j}, Σ h²)` is an **exact polynomial in `n`** with positive leading
> coefficient (Ivanov–Olshanski Prop 5.1, [`math/0304010`](https://arxiv.org/abs/math/0304010)).

Verified degrees: `deg_n M_2 = 3`, `deg_n M_4 = 4`, `deg_n M_6 = 5` (i.e. `deg_n M_{2j} = j+2`), all
with positive values / positive leading term. Positivity of `M_{2j}` for all `n` therefore reduces to a
**finite polynomial-positivity check** (the leading term handles the tail) — it is **provable**. Odd-`k`
moments are non-polynomial (not shifted-symmetric) and remain empirical.

## Status / honesty

Isolates the robust surviving structure (`M_k>0`, the `t>0` half of `G`) and a concrete provable even-`k`
sub-target. It does **not** prove A2 or the kernel — both remain open (and both verified exactly
`k,n ≤ 40` in the correction probe). The A2 proof still needs a global argument for the concave `ln`
weight; the even-`k` moment positivity is the rigorous foothold.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_moment_skeleton.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_moment_skeleton.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-moment-skeleton.witness.json`

## Cross-references

- The pointwise-route correction: [`2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)
- Epic map: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`. Ivanov–Olshanski `math/0304010`.
