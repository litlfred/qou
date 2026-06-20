# Categorical scoping: `|content(λ)|` as Hecke-energy density

> **Status: scoping note, NOT a derivation attempt.** This doc
> identifies the categorical chain that would have to be assembled
> to upgrade the [`d7c56c17e`](https://github.com/litlfred/qou/commit/d7c56c17e)
> `abs_content` lead (`Σ|c(i,j)|` matches binding A-growth at ~5 %)
> from a *selected-from-6-candidates* near-match into a derived
> identity. **Per AGENTS.md Δ_λ gate, this is NOT itself a fitted
> ansatz proposal**; the doc only states the open categorical
> question and lists the upstream objects that would have to land.

## The empirical observation (already on main)

In [`d7c56c17e`](https://github.com/litlfred/qou/commit/d7c56c17e)
(2026-06-02 17:35Z), six candidate per-block weights `w_λ` were
tested for `B = E · Σ_λ w_λ |Δθ_λ|` over D / T / ³He / ⁴He:

| candidate | A-growth ratio S(⁴He) / S(D) | worst \|err\| |
|---|---:|---:|
| **`abs_content` = Σ \|c(i,j)\|** | **13.40 vs 12.72 (~5 %)** | **20 %** |
| `y_λ` (Markov / q-Schur Plancherel) | 0.04 (anti-correlated) | 199 % |
| `dim_classical(λ)` | — | 600× |
| `dim_q(λ)` | — | ~700× |
| bar-`y_λ` | — | 1200× |
| `1 / y_λ` | — | 90 000× |

`abs_content` is the standout by a factor of ~10× over the next
candidate (`y_λ`) on the worst-error axis. **20 % is not closure**;
the lead is structural, not numerical.

## Definitions

For a partition `λ = (λ_1, λ_2, …, λ_ℓ)` (rows of a Young diagram,
1-indexed or 0-indexed by convention):

- **Cell content** `c(i, j) := j − i` for each cell `(i, j) ∈ λ`
- **Signed content sum** `c(λ) := Σ_{(i,j) ∈ λ} (j − i)` — the
  q-Casimir eigenvalue on V_λ (Lusztig 1990; standard q-Schur fact).
  This is what appears in `ySchurClosedForm = q^{c(λ)} / [n]_q!`.
- **Absolute content sum** `|c|(λ) := Σ_{(i,j) ∈ λ} |j − i|` — the
  L¹ norm of the content distribution over `λ`'s cells. This is the
  `abs_content` from `d7c56c17e`.

Worked examples:

| λ | cells | c(i,j) values | c(λ) | \|c\|(λ) |
|---|------|---------------|------|--------|
| `(2)` | (0,0),(0,1) | 0, 1 | 1 | 1 |
| `(1,1)` | (0,0),(1,0) | 0, −1 | −1 | 1 |
| `(3)` | (0,0),(0,1),(0,2) | 0, 1, 2 | 3 | 3 |
| `(2,1)` | (0,0),(0,1),(1,0) | 0, 1, −1 | 0 | 2 |
| `(1,1,1)` | (0,0),(1,0),(2,0) | 0, −1, −2 | −3 | 3 |
| `(2,2)` | (0,0),(0,1),(1,0),(1,1) | 0, 1, −1, 0 | 0 | 2 |

Notes:
- `|c|(λ) ≥ |c(λ)|` always (triangle inequality on sum); equality
  iff all cells have the same sign content.
- For "balanced" partitions (e.g. `(2,1)`, `(2,2)`), `c(λ) = 0` but
  `|c|(λ) > 0`. The bar-involution (`λ ↦ λ^T`) preserves `|c|(λ)`
  but negates `c(λ)`.

## The categorical question

**Is `|c|(λ)` the natural Hecke-energy density on V_λ?**

Specifically: does there exist a categorical construction in
`H_n(q)` (or `U_q(sl_n)`) whose evaluation on the irreducible
V_λ yields `|c|(λ)`?

Candidate constructions (each is a research direction, NOT a
claimed identification):

1. **Trace of `|Ω_q|` on V_λ.** The q-Casimir `Ω_q` acts on V_λ
   with eigenvalue `c(λ)`. The "absolute-value operator" `|Ω_q|`
   in a chosen basis (Hoefsmit seminormal? Kashiwara crystal?)
   would have eigenvalue `|c(i,j)|` on the cell-indexed basis
   vector. `tr(|Ω_q| · ϕ_λ) = |c|(λ)` where `ϕ_λ` is the
   character projector.

   *Categorical objection*: `|Ω_q|` is not a Hecke-algebra
   element; the "absolute value" requires a choice of basis,
   which is the same convention-dependence flagged by [PR
   #1641 / #1643](https://github.com/litlfred/qou/pull/1641)
   as a *structural choice*, not a categorical statement.

2. **Hilbert-Schmidt norm of `Ω_q` in the seminormal basis.**
   `‖Ω_q · v_{(i,j)}‖_HS² = Σ |c(i,j)|² ≠ |c|(λ)`. So this is
   `(|c|² )(λ)`, not `|c|(λ)`. Wrong norm.

3. **Sum of arm-lengths + leg-lengths** (hook-related):
   `Σ_{(i,j) ∈ λ} (arm(i,j) + leg(i,j))`.
   For `(3)`: arms = {2,1,0}, legs = {0,0,0}, sum = 3 = `|c|((3))`.
   For `(2,1)`: arms = {1,0,0}, legs = {1,0,0}, sum = 2 =
   `|c|((2,1))` — match on these two cases. **FALSIFIED in
   general**: for `(2,2)` the arm+leg sum is 4
   (`(0,0)`: 1+1, `(0,1)`: 0+1, `(1,0)`: 1+0, `(1,1)`: 0+0)
   whereas `|c|((2,2)) = 2`. So the hook arm+leg sum is NOT `|c|(λ)`
   — the `(3)`/`(2,1)` agreement is an accidental small-case
   coincidence (both are hooks / near-hooks; the identity breaks
   at the first non-hook, the 2×2 square). Recorded as a refuted
   candidate, not a lead.

4. **Half the L¹-distance of `λ` to its transpose `λ^T`** in
   the dominance order — a combinatorial measure of how
   non-self-conjugate `λ` is. **FALSIFIED**: for `(3)`,
   `½·‖(3,0,0) − (1,1,1)‖₁ = ½·4 = 2` but `|c|((3)) = 3`; for
   `(2,1)` (self-conjugate) the distance is 0 but `|c|((2,1)) = 2`.
   So this is not `|c|(λ)` either. Recorded as refuted.

5. **Sum of `χ^λ(s_k)` over an explicit set of Coxeter generators**.
   The character value `χ^λ(s_k)` of a transposition on V_λ is
   classical; summing over the `n−1` simple generators (or all
   `(n choose 2)` transpositions — they're conjugate, same value)
   was conjectured to equal `|c|(λ)` in some normalisation.
   **FALSIFIED (2026-06-03 follow-up)**: by Murnaghan-Nakayama,
   `χ^λ(s_k) = f^λ · 2·c(λ) / (n(n-1))` — proportional to the
   *signed* content sum `c(λ)`, not `|c|(λ)`. Summing over
   simple-only gives `2·f^λ·c(λ)/n`; over all transpositions gives
   `f^λ·c(λ)`. Both vanish at `(2,2)` (where `c((2,2)) = 0`
   because the partition is self-conjugate), but `|c|((2,2)) = 2`.
   Recorded as refuted — the construction gives the wrong invariant
   (signed-content moment, not L¹ moment).

## Status of the 5 candidates (2026-06-03)

| # | construction | status |
|---|---|---|
| 1 | trace of `|Ω_q|` on `V_λ` (basis-dependent) | open with basis-convention objection |
| 2 | Hilbert-Schmidt norm of `Ω_q` | wrong norm (gives `|c|²(λ)` not `|c|(λ)`) |
| 3 | sum of arm + leg lengths | falsified at `(2,2)` |
| 4 | ½ L¹-distance `λ → λ^T` | falsified at `(3)`, `(2,1)` |
| 5 | sum of `χ^λ(s_k)` over Coxeter generators | falsified at `(2,2)` (signed content sum, not L¹) |

**4 of 5 candidates refuted; only candidate 1 remains, and it has the
basis-convention objection that PRs [#1641](https://github.com/litlfred/qou/pull/1641) and
[#1643](https://github.com/litlfred/qou/pull/1643) flagged as a structural choice rather
than a categorical statement.**

The structural conclusion: **`|c|(λ)` is unlikely to have a single
scalar categorical-invariant identity** in the standard Hecke /
q-Casimir / symmetric-function library. The 20% A-growth match
that surfaced this scoping is more likely the **shadow** of an
operator-valued construction (the LR branching trace decomposition
gated on [#1443](https://github.com/litlfred/qou/pull/1443) / IwahoriHecke Sprint 2 in
[#1524](https://github.com/litlfred/qou/pull/1524)) than a hidden hook-content statistic.

Sharpened Δ_λ-gate discipline: **do not propose further scalar
combinatorial candidates** for `|c|(λ)`. The next productive probe
is the operator-valued combiner, after the upstream sibling PRs
land — not a 6th scalar guess.

## What would have to land to derive (not fit) `|c|(λ)`

Three independent pieces:

1. **Operator-valued LR branching trace decomposition** (open;
   live in [`prop:hecke-branching-trace-decomposition`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md)
   / [#1443](https://github.com/litlfred/qou/pull/1443) / IwahoriHecke
   Sprint 2 in [#1524](https://github.com/litlfred/qou/pull/1524)).
   The operator-valued combiner that replaces the failing scalar
   `tr_M` collapse.

2. **A canonical signed-vs-modulus discipline at step 5** (the
   `|·|` audit per [PR #1641 / #1643](https://github.com/litlfred/qou/pull/1641)
   and cheat-sheet §9.2 "preserve information until observation").
   Without this, any `|c|`-based identification is structurally
   ambiguous (which basis? which sign convention?).

3. **A categorical identification of `|c|(λ)` with one of the
   candidates above** (or another not yet on this list). Almost
   certainly needs (1) and (2) first; otherwise it slides into
   selection-bias fitting (Δ_λ gate).

## Pre-stated falsification signatures

Per AGENTS.md flip-flop prevention discipline, any future
derivation attempt must declare its failure-mode signatures in
advance. For `|c|(λ)` as Hecke-energy density:

- **Anchor cross-check at multiple q_0**: if the categorical
  evaluation of the proposed object lands within compute precision
  at one anchor but not at another (proton-pin vs muon-pin vs
  hypothetical cross-anchor), the identification is q_0-dependent,
  i.e. a near-match — NOT Taylor-exact. Retract.
- **A=4 ⁴He magic peak**: any candidate must reproduce the
  `f(⁴He) = 8.286` (i.e. ratio 2.07 over `Z·N`) within compute
  precision. The retracted 2026-05-30 leads (1+q, 2√q, exact 2)
  ALL failed this at 1.7–3.6 %. The bar for `|c|(λ)`-via-categorical
  is the same.
- **Cross-anchor A-growth**: the A-growth ratio 13.40 vs the
  target 12.72 should hold to compute precision (1 ppQ) at any
  q_0, not just substrate. 20 % is the current gap.

## Honest disposition

This doc is a **scoping note**, NOT a derivation attempt. The
`|c|(λ)` lead is at 20 % residual after selection from 6
candidates — that is selection-bias-prone and far from compute
precision. Upgrading it to a derivation requires (1) + (2) + (3)
above, all of which depend on upstream sibling work that is not
yet on main.

**Action**: do not propose a categorical identification of
`|c|(λ)` until the operator-valued LR branching trace
decomposition lands. The 20 % near-match remains a *suggestive
structural lead*, on par with the 2026-05-30 retracted leads
(`f ≈ Z·N`, 1+q, 2√q, κ ≈ 2√3/(3π)) — not a derivation.

## Cross-refs

- [`docs/coordination/2026-06-02-mass-sweep-a4-plus-status-refresh.md`](2026-06-02-mass-sweep-a4-plus-status-refresh.md) — the parent A≥4 status refresh; cross-links this scoping note
- [`docs/workplans/2026-05-29-a567-atom-knot-sdp.md`](../workplans/2026-05-29-a567-atom-knot-sdp.md) — the original A≥4 workplan (with 2026-05-30 critical-discipline retraction)
- [`docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md`](2026-05-30-a567-and-alpha-em-coupling.md) — cross-thread context
- AGENTS.md §"Δ_λ gate" — the seventh-fit prohibition this scoping note avoids
- AGENTS.md §7a + §7b — Hecke-Skein convention + symmetric-crystal authoring guidance
- PR [#1641](https://github.com/litlfred/qou/pull/1641) / [#1643](https://github.com/litlfred/qou/pull/1643) — Φ_q signed-vs-modulus structural choice
- PR [#1443](https://github.com/litlfred/qou/pull/1443) / [#1524](https://github.com/litlfred/qou/pull/1524) — operator-valued LR branching trace decomposition
