# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: the Cauchy–Schwarz relaxation is cheap (≥78.6 % of the true margin) — but tightness is not tractability, and the machinery reaches `P > N`, not the margin

> **Withdrawn inference, corrected before merge (same branch, §Reach below).** This audit's first
> version was titled *"…so the margin route is the right one"* and concluded exactly that. **The
> measurement stands; the inference does not.** "The relaxation is tight" and "the resulting bound is
> tractable" are different claims, and only the first was measured. The Fulman identity is keyed to
> an **eigenfunction** of the up-down chain, and `A` is not one — so the identity reaches `P` and `N`
> but **not** `V_A`, which is the margin route's one remaining object. See §The reach.

**Date:** 2026-09-04 · **Branch:** `claude/m1-k5r5-cs-relaxation-cost-2026-09-04` ·
**Tier:** measurement + independent re-verification of a 2026-08-21 corpus reduction · **Epic:** `qou-x631`; gap `qou-k5r5`.

## Two routes, and the relationship nobody had priced

Two sufficient conditions for `M₁ > 0` coexist in this corpus, and PRs #6500 → #6602 sharpened one of
them without ever checking it against the other.

**Fulman reduction** ([`…-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md),
2026-08-21). With `ω₃ = Σc² − C(n,2) = W` an exact eigenfunction of the up-down chain on the Young
lattice, and the split identity `Σ□ h = Σ_u D(u)² + Σ□|c|` (i.e. `Σh = D + A`):

> `M₁ = Cov(Σh, W) = P − N`, with `P := Cov(A,W) ≥ 0` and `N := −Cov(D,W) ≥ 0`, **both signs manifest
> edge by edge.** So `M₁ > 0` is *exactly* `P > N` — necessary and sufficient.

**(CS) margin** (the route I have been sharpening). `m = ρ_P − √(V_D/V_A) > 0` with
`ρ_P = P/√(V_A·V_W)`. Multiplying through by `√(V_A·V_W)`, this is exactly `P > √(V_D·V_W)`. Since
Cauchy–Schwarz gives `N = |Cov(D,W)| ≤ √(V_D·V_W)`, **the margin is the CS relaxation of `P > N`** —
sufficient, not necessary, and it discards `N`'s per-edge sign structure entirely.

**So: what does that relaxation cost?** The whole question of whether four PRs of effort went to the
right place turns on it, and it is one exactly-computable number.

## Measured ([`…_cs_relaxation_cost.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_cs_relaxation_cost.py), exit 0, exact `Fraction` over every partition to n = 40, NO float64)

| n | `P` | `N` | `M₁ = P−N` | `√(V_D·V_W)` | `ρ_D` | surviving |
|---|---|---|---|---|---|---|
| 8 | 22.7111 | 12.8444 | 9.86667 | 15.3439 | 0.8371 | 0.7467 |
| 16 | 152.552 | 92.5494 | 60.0027 | 105.391 | 0.8782 | 0.7860 |
| 24 | 435.003 | 268.202 | 166.801 | 297.510 | 0.9015 | 0.8243 |
| 32 | 920.975 | 578.074 | 342.900 | 633.745 | 0.9122 | 0.8376 |
| 40 | 1622.90 | 1024.18 | 598.715 | 1112.83 | 0.9203 | 0.8519 |

where `ρ_D := N/√(V_D·V_W)` **is** the tightness of Cauchy–Schwarz on the `(D, W)` pair (1 = free),
and *surviving* `:= (P − √(V_D·V_W))/(P − N)` is the share of the true margin the relaxation still
certifies.

> **CS is cheap.** Over `n ≥ 16`: `ρ_D ∈ [0.8782, 0.9203]`, surviving fraction
> **∈ [0.786, 0.852]**. The relaxation costs at worst **1.27×**, and both quantities *increase* with
> `n` — so at `n ≥ 79` it should be cheaper still, which is the conservative direction for the
> extrapolation.

It was not obvious in advance: had `ρ_D` come out near 0.5, four PRs would have been paying a 2×
premium avoidable by working `P > N` directly.

*(This paragraph first continued "**the margin route is therefore the right target**". That does not
follow from a tightness measurement — see the next section, which withdraws it.)*

## The reach — tightness is not tractability, and only `W` is an eigenfunction

The Fulman identity is not a general covariance formula. It reads

> `Cov(f, g) = E_π[(f − f*)(g − g*)] / (2(1 − β))`, valid **when `J g = β g`**

— it computes the covariance of *any* `f` against an **eigenfunction** `g` of the up-down chain `J`.
The corpus's reduction takes `g = ω₃ = W`, which is why `P` and `N` come out as local per-edge sums.
`V_A = Cov(A, A)` would need **`A` itself** to be an eigenfunction.

Measured ([`…_eigenfunction_reach.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_eigenfunction_reach.py),
exit 0, exact `Fraction`, `n = 3…12`, NO float64), quantified over the **family** — every
non-degenerate `n`, not any single one:

| statistic | eigenfunction at every n | consequence |
|---|---|---|
| `W` | **YES**, `β₃ = (n−2)/(n+1)` exactly | `Cov(·, W)` reachable ⟹ **`P` and `N` both reachable** |
| `A` | **NO** — at no non-degenerate `n` | `V_A = Cov(A,A)` **not** reachable by this identity |
| `D` | **NO** — constant (hence vacuously one) at `n = 3` only | `V_D` **not** reachable either |

**Positive control.** `W` is *known* to be an eigenfunction with `β₃ = (n−2)/(n+1)` (corpus,
2026-08-21, verified there to `n ≤ 13`). This probe's chain reproduces that **exactly** at every `n`,
and `J` is row-stochastic throughout — so a negative on `A` is a fact about `A`, not about the chain.

**The identity itself is verified, not cited — and it is the load-bearing check.** "`P` and `N` are
exact local per-edge sums" is the entire reason to prefer `P > N`, and the eigenfunction table only
establishes what *licenses* the identity, not that it is right. So for `f ∈ {A, D}` the probe
compares the direct Plancherel covariance against the edge sum:

> `Cov(f, W) == E_π[(f − f*)(W − W*)] / (2(1 − β₃))` — **exact agreement at every `n = 3…12`, for
> both `f`.**

At `n = 8`: `P = Cov(A,W) = 1022/45`, edge sum `= 1022/45`, `N = −Cov(D,W) = 578/45`. `1022/45 =
22.7111` also reproduces the `P(8)` entry of the table above, which was computed independently by the
other probe — two separate routes to the same rational.

**Cross-check, from an independent direction.** #6627 found `V_W` an exact polynomial
`n(n−1)(n−2)/3` while `V_A`, `V_D` and `P` are not polynomial at all. That is the same boundary seen
from the other side: **the one object with a closed form is the one whose statistic is the
eigenfunction.** Two independent measurements, one split.

> **So the two routes are not symmetric in tractability.** `P > N` needs only covariances against
> `W` — both reachable, both local per-edge sums with manifest signs. The margin route needs `V_A`,
> which the named machinery does not reach and which #6627 showed has no polynomial closed form
> either. **#6651's tightness measurement stands; its inference that the margin route is the right
> target is withdrawn.**

**Scope — (a), not (b).** This says the *named identity* does not apply to `V_A`. It does **not**
exclude `V_A`: a spectral decomposition of `A` in the chain's eigenbasis, or a different chain for
which `A` is an eigenfunction, are both untested here. What it settles is where the roadmap's own
tool points.

### A quantifier bug in this probe, caught before commit

The first run reported *"D is an eigenfunction ⟹ `V_D` reachable"* on the strength of **n = 3
alone**, where `D ≡ 3` is **constant** — and a constant is trivially an eigenfunction of any
stochastic chain (`β = 1`), carrying no information. The summary used `any(n)` where reachability is
a claim about the **family**, so it needs `every(n)`, with constants excluded. Fixed to quantify over
non-degenerate `n` and to mark the constant case explicitly (`YES*` in the table). Same shape as the
`da-arity-conflation` class, and the second quantifier slip of this arc — #6602 had the mirror of it,
testing a family claim at a point.

## The corpus's reduction, independently re-verified

The probe does not assume the 2026-08-21 result it is pricing. `Σh` is computed **per cell** as an
explicit hook sum, never as `D + A`, and two assertions gate every number above:

| self-check | result |
|---|---|
| split identity `Σh == D + A` at **every partition**, `n ≤ 40` | **PASS** |
| Fulman reduction `Cov(Σh, W) == P − N` at **every n** | **PASS** |

If either had failed, the probe refuses to print a cost figure. Both pass, so the split identity and
the exchangeable-pair reduction are now confirmed from a second, independent computation.

## What this does not do

It prices the relaxation; it closes neither route. Both still need a rigorous finite-`n` argument —
`δ_A` for the margin, `P > N` for Fulman. The window ends at `n = 40` while the requirement is
`n ≥ 79`, so nothing here is a bound.

## Status of `qou-k5r5`

Gap **OPEN**. Two things are now known that were not, and they point in opposite directions:

- **The CS relaxation is cheap** — it forfeits at most ~21 % of the true margin, so the 40.5×
  headroom measured in #6576 is not being spent on a detour. Whichever route runs, this is not
  where the budget goes.
- **But the machinery reaches `P > N`, not the margin.** `V_A` is neither an eigenfunction covariance
  (this PR) nor a polynomial in `n` (#6627), while `P` and `N` are both exact local per-edge sums
  with manifest signs.

**So the recommended next target changes from `δ_A` to `P > N`** — the necessary-and-sufficient form,
whose two objects are the ones the roadmap's own tool can compute. `C ≤ m_∞√79 = 2.6681` remains the
requirement on the margin side if that route is taken anyway (empirical envelope 0.0580; `n ≤ 78`
certified exhaustively). That is a recommendation from a reach measurement, not a proof that the
margin route is dead — see the scope note above.

## `P > N` in local form — and a false corpus claim found on the way

With `P > N` established as the target, the natural question is whether it is *edge-wise* true: if
`Δ(Σh)·Δω₃ ≥ 0` on every single-box edge, `M₁ > 0` follows for all `n` immediately and the gap
closes. Measured ([`…_edge_sign_census.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_edge_sign_census.py),
exit 0, exact `Fraction`, every edge to n = 12), with every figure gated on the census exactly
reconstructing `M₁` — **PASS**.

| n | Fact A | Fact B | combined ≥ 0 | #pos | #neg | neg frac | pos/neg mass |
|---|---|---|---|---|---|---|---|
| 6 | ok | ok | no | 20 | 4 | 0.167 | 22.0 |
| 8 | ok | ok | no | 52 | 4 | 0.071 | 112.0 |
| 10 | ok | **FAIL** | no | 144 | 16 | 0.100 | 30.9 |
| 12 | ok | **FAIL** | no | 328 | 36 | 0.099 | 52.3 |

### Finding 1 — Fact B is false as stated (a corpus correction)

The 2026-08-21 audit states `Δ(ΣD²)·Δω₃ ≤ 0` "on every single-box edge … verified n≤13". It **fails
first at n = 10**. Hand-verified counterexample:

> `λ* = (5,4,1) → λ = (5,5)`, joined via `μ = (5,5,1)`. `ΣD²: 16 → 18`, `ω₃: −5 → 0`, so the product
> is `(+2)(+5) = +10 > 0`.

The stated reason — *larger `|content|` ⟹ shorter diagonal ⟹ `ΣD²` decreases* — describes the
**equilibrium shape**, not the actual diagonal lengths. Landing a box on a diagonal of current length
`d` raises its square by `2d+1` regardless of content; here the box leaves a length-1 diagonal
(`1→0`) and lands on another (`1→4`), net **+2**.

**`N ≥ 0` is not refuted** — it is positive at every `n` in the table above, and `M₁ = P − N` is an
identity verified exactly. Only the *per-edge argument* for `N`'s sign fails, so "both signs manifest
edge by edge" is true of `P` and false of `N` at `n ≥ 10`. Fact A **holds**, re-verified at every
edge to n = 12 (beyond the original's n ≤ 8). The correction is applied to the 2026-08-21 audit in
place.

### Finding 2 — the combined term is not edge-wise signed, so the gap does not close here

Edge-wise non-negative only for `n < 6` (too few edges to exhibit a counterexample), and **never
after**, with no recovery through n = 12. So `M₁ > 0` does **not** follow from per-edge signs. What
must be bounded instead is the **pos/neg mass ratio** — measured in **[22.0, 112.0]** over `n ≥ 6`,
against the threshold 1.

The negative edges are ~7–17 % of all edges, i.e. a substantial fraction rather than a thin
exceptional set. That **argues against** a pairing/injection argument over them and **for** bounding
the mass ratio directly — a reading of the census, not a proof that pairing cannot work.

*(A third small-`n` quantifier trap, and the third of this arc: `any(n)` over the whole table reports
"a non-negative n exists" on the strength of n = 3,4,5, where the chain is simply too small to have a
negative edge. Reported as a threshold — where it starts failing and whether it recovers — instead.)*

## An exact criterion for the negative edges

The census left `P > N` as *"bound the pos/neg mass ratio"*, and the obvious next move is a wider
scan. Formalize-first says look for the invariant first — and **both** per-edge pieces already have
closed forms, so which edges are negative should be decidable algebraically.

Write the edge as: `λ` has a box at content `u` that `λ*` lacks; `λ*` has one at `v` that `λ` lacks;
`d_u`, `d_v` are the lengths of diagonals `u`, `v` **in `λ`**. Then

| quantity | closed form |
|---|---|
| `Δ(Σ\|c\|)` | `\|u\| − \|v\|` |
| `Δω₃` | `u² − v²` |
| `Δ(ΣD²)` | `2(d_u − d_v) − 2` |
| `Δ(Σ\|c\|)·Δω₃` | `(\|u\|−\|v\|)²(\|u\|+\|v\|) ≥ 0` — Fact A, in closed form |

With `g := |u| − |v|` **signed**, `Δω₃ = g(|u|+|v|)` so `sign(Δω₃) = sign(g)`, and
`Δ(Σ|c|) + Δ(ΣD²) = g + 2(d_u−d_v) − 2`. The combined term is negative exactly when those two
disagree:

> **negative ⟺ `g · (g + 2(d_u − d_v) − 2) < 0`**

**Verified at every edge to n = 22** — 12,518 edges at n = 22 — alongside all four closed forms and
the fact that `g = 0` edges contribute exactly `0`
([`…_negative_edge_criterion.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_negative_edge_criterion.py),
exit 0, exact integer/`Fraction`, NO float64). Read at `g > 0` it says `d_u − d_v < 1 − g/2`: a
negative edge needs the diagonal the box *leaves* to be no longer than the one it *lands on*, by a
margin growing with the content gap.

### A WLOG shortcut here is wrong, and the probe's own check caught it

The first version derived the `g > 0` case and handled `g < 0` by "swapping the roles of `u` and
`v`". **That is invalid**: `Δ(ΣD²) = 2(d_u−d_v) − 2` is not symmetric under that swap — the `−2` does
not flip with the difference — so the swapped form is off by 4. The signature was diagnostic: all
four closed forms **PASSED** while the criterion **FAILED** at every `n` that has a negative edge,
which is exactly what correct algebra plus a wrong case analysis looks like. The signed-`g` form has
no case split and so no place for that error to live.

### A Fact-B violation is *not* a negative edge

I had this backwards until the counts separated them. Fact B claims `Δ(ΣD²)·Δω₃ ≤ 0`; a **violation**
has it `> 0`, which **adds** to the non-negative `Δ(Σ|c|)·Δω₃` and makes the edge *more* positive.
The two phenomena are disjoint: negative edges first appear at **n = 6**, Fact-B violations at
**n = 10**.

### The ratio settles

| n | 6 | 8 | 12 | 16 | 19 | 22 |
|---|---|---|---|---|---|---|
| pos/neg mass | 22.0 | 112.0 | 52.3 | 44.1 | 56.3 | 54.8 |

Over `n ≥ 6` the range is [22.0, 112.0], but that is small-`n` noise: over **`n ≥ 16` it is
[44.1, 56.3]**, sitting near **54.8** at n = 22. The earlier `n ≤ 12` window could not show this.

> **What this buys.** `P > N` was a statement about a weighted sum over an *enumerated* set; it is
> now a statement about a set **cut out by an inequality in four integers**, three of which
> (`u`, `v`, `d_u`) are read off a single partition. That is the shape a finite-`n` bound can use —
> bound the weight the criterion admits, rather than enumerate. **It bounds nothing yet**, and a
> ratio settling near 55 over `n ≤ 22` is not evidence about `n ≥ 79`.

## Cross-references

- The sharper reduction being priced: [`…-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- The route it validates: [`…-ratio-route-is-the-target.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md) (#6576), [`…-ratio-is-a-constant-not-a-rate.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-is-a-constant-not-a-rate.md) (#6602)
- Why no closed form shortcuts it: [`…-variance-polynomiality.md`](2026-09-04-covariance-kernel-M1-k5r5-variance-polynomiality.md) (#6627)
- Epic `qou-x631`; gap `qou-k5r5`.
