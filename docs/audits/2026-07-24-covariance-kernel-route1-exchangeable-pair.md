# Covariance-kernel epic (qou-x631) — Route 1: the Fulman-analogue exchangeable pair for the 3-cycle

**Date:** 2026-07-24 · **Branch:** `claude/deltalambda-covariance-epic-phase3-2026-07-24` ·
**Tier:** construction + exact reformulation (verified `n ≤ 9`, exact `Fraction`) · **Discipline:**
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`.

## What this is

Fulman (`math/0305423`) proves a Stein-method CLT **with error** for the transposition character ratio
by building an exchangeable pair from the Plancherel-reversible down-up Markov chain on Young diagrams,
for which the transposition central character is an **eigenfunction**. This note carries that
construction to the **3-cycle** — the central element the kernel needs — and uses it to reformulate
the kernel as a **local** one-step statement.

## The chain

On partitions of `n`, the down-up chain

- **down:** `λ → μ` (remove a corner box), probability `dim μ / dim λ`;
- **up:** `μ → λ*` (add a box), probability `dim λ* / (n · dim μ)`;

is stochastic and **reversible w.r.t. the Plancherel measure** `P(λ) = (dim λ)²/n!` (verified `n ≤ 9`).

## Eigenfunction + exact eigenvalue

The content-power central characters `ω_j(λ) := Σ_□ c(□)^j − E_Planch[Σc^j]` are eigenfunctions of the
chain for `j = 1, 2`, with **exact rational eigenvalues**:

| `j` | statistic | conjugacy class | eigenvalue contraction `τ` |
|---|---|---|---|
| 1 | `Σc` | transposition (Fulman's object) | **`τ₁ = 2/n`** |
| 2 | `Σc² − C(n,2) = ω₃` | 3-cycle (**our object**) | **`τ₃ = 3/n`** |

`j ≥ 3` mix (not pure eigenfunctions) — but they are not needed. `ω₃` being a pure eigenfunction with
`τ₃ = 3/n` is the **direct k=2 analogue of Fulman's k=1**, and gives exactly

> `E[ω₃(λ*) | λ] = (1 − 3/n)·ω₃(λ)`,

the hypothesis `E_W(W*) = (1−τ)W` that Fulman's Stein bound (his Thm 1.3) requires.

## Local reformulation of the kernel

With `f = dim`, `Δf := f(λ*) − f(λ)`, reversibility + the eigenfunction property give the **exact
identity** (derivation below, verified `n ≤ 9`):

> `E_P[ Δf · ω₃(λ) ] = −τ₃ · Cov_P(f, ω₃) = −(3/n) · cov(n)/n!`.

*Derivation.* `E_P[ω₃·Kf] = E_P[(Kω₃)·f] = (1−τ₃)⟨ω₃,f⟩_P` (reversibility + eigenfunction), and
`E_P[Δf·ω₃] = E_P[ω₃(Kf−f)] = (1−τ₃)⟨ω₃,f⟩_P − ⟨ω₃,f⟩_P = −τ₃⟨ω₃,f⟩_P`. Since `⟨ω₃,f⟩_P =
Cov_P(f,ω₃) = cov(n)/n!` (as `E_P[ω₃]=0`), the identity follows. ∎

Since `τ₃ = 3/n > 0`, the kernel's sign flips to a **local** correlation:

> **`cov(n) ≤ 0`  ⇔  `Cov_P(f, ω₃) ≤ 0`  ⇔  `E_P[(f(λ*) − f(λ))·ω₃(λ)] ≥ 0`**

— the correlation between the **one-step dimension increment** `Δf` and the current content-spread
`ω₃`. The global sign is now a one-step-increment question.

## Honesty — what remains

This **builds the machinery and the reformulation**; it does **not** close the sign. The identity is
exact but, on its own, circular (it restates `Cov_P(f,ω₃)`). Closing requires computing
`E_P[Δf·ω₃]` a *different* way with a definite sign — either

1. an **explicit combinatorial evaluation** of the one-step increment `Δf = f(λ*)−f(λ)` (removing a
   corner via a hook-ratio, adding a box) and its correlation with `ω₃`; or
2. the **joint Stein CLT** of `(f, ω₃)` with an **effective Berry–Esseen error** bounding the
   transfer-factor deviation below the negative main term for `n > n₀` (then exact `n ≤ 40` closes it).

Neither is in the literature for the 3-cycle-with-dimension covariance (Fulman gives only the
*marginal* transposition CLT at rate `40.1 n^{−1/4}`). This is genuine further research.

## The Dirichlet-form sign, and why the per-edge certificate fails (Phase 5b)

Symmetrising the exchangeable pair (both `λ, λ*` Plancherel-distributed) gives, for `Δg := g(λ*)−g(λ)`,

> `E_P[(Δf)(Δω₃)] = 2·ℰ(f, ω₃)`,  where `ℰ(g,h) := ½ Σ_{λ,λ*} P(λ)K(λ,λ*)·(Δg)(Δh)`

is the **Dirichlet form** of the reversible chain, and `ℰ(f,ω₃) = ⟨f,(I−K)ω₃⟩_P = τ₃⟨f,ω₃⟩_P =
(3/n)·cov(n)/n!` (verified exactly, `n ≤ 9`). So the kernel is exactly a **Dirichlet-form sign**:

> **`cov(n) ≤ 0  ⇔  ℰ(f, ω₃) ≤ 0`.**

`ℰ(f,ω₃)` sums over chain **edges** with **non-negative** weights `P(λ)K(λ,λ*)`, of `(Δf)(Δω₃)` where
`Δω₃ = c_add² − c_rm²` (contents of the moved box). The clean hope: `(Δf)(Δω₃) ≤ 0` on **every** edge
(dimension and content-spread always move oppositely) ⇒ `ℰ ≤ 0` ⇒ done.

**This per-edge certificate is ELIMINATED.** "Bad" edges (`(Δf)(Δω₃) > 0`) exist and their count grows
with `n` (`n=3..9`: `0, 4, 4, 12, 16, 32, 40`). Archetype at `n=4`: the move `(3,1) → (2,2)` has
`Δf = −1`, `Δω₃ = −4` — the **more balanced** square `(2,2)` has **lower** dimension (2) than the
hook-like `(3,1)` (dim 3). So **"max-dimension diagram = most balanced" is false at finite `n`** (it
holds only asymptotically, VKLS), and the kernel's sign is a **weighted cancellation** over edges, not
a local per-edge fact — mirroring every earlier phase. The Dirichlet-form sign `ℰ(f,ω₃) ≤ 0` therefore
still requires the full (joint Stein CLT / effective-error) analysis; there is no shortcut via a
local edge certificate.

- Probe (5b): [`computations/deltalambda/wlambda_covariance_epic_phase5b_dirichlet_peredge.py`](../../computations/deltalambda/wlambda_covariance_epic_phase5b_dirichlet_peredge.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase5b-dirichlet-peredge.witness.json`

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase5_route1_exchangeable_pair.py`](../../computations/deltalambda/wlambda_covariance_epic_phase5_route1_exchangeable_pair.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase5-route1-exchangeable-pair.witness.json`

## Cross-references

- Literature assessment: [`2026-07-24-covariance-kernel-literature-assessment.md`](2026-07-24-covariance-kernel-literature-assessment.md)
- Interval / FKG reframing (+ Phase 4b eliminations): [`2026-07-24-covariance-kernel-interval-fkg-reframing.md`](2026-07-24-covariance-kernel-interval-fkg-reframing.md)
- Fulman, *Stein's Method and Plancherel Measure* (`math/0305423`, TAMS 2005)
