---
# qou-fxym
title: 'A3 (headline): prove REV_n = O(sqrt n) — the beta-bound is the weak step, not the (l,W) reduction'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:49Z
updated_at: 2026-10-11T12:00:00Z
parent: qou-3e6w
---

Parent epic `qou-3e6w`.  **This is the arc's headline problem**, and it has been untouched by every
tranche since 2026-09-13 — each of which says so explicitly in `qou-hok7`.  Split out on
2026-10-10 so it stops being a closing caveat on other people's work.

## The claim to prove

`REV_n = O(√n)` — equivalently, `M_n ≤ e_∞·√(2n) + o(√n)`, with `e_∞` the certified constant of
#7335/#7349.  `REV_n` is the **free energy over partition shapes**: energy = excess hook length,
entropy = shape multiplicity.

## What is established

- The `Θ(√n)` **coefficient is identified**: `A√2` with `A = e_∞` (#7294).
- `e_∞` has a **value** and, since #7349, is a **maximum over a proved window** rather than a
  search result: `2.43929645512078402706542884314` at `(s_t, s_b) = (8,8)`, window `s ≤ 27`.
- `deg Z_n` is **derived in closed form** (2026-09-07), and the exact divisor is `q^{deg_n}`,
  computable cheaply at any `n` by the max-plus route.
- `log p(n) ~ π√(2n/3) = 2.5651√n` is itself `Θ(√n)`, measured to `n = 4000`.
- **The `(ℓ,W)` reduction is TIGHT** (#7081) — Jensen is optimal per distance class and the
  inter-class coupling factor *shrinks* with `ℓ` (1.208 at `ℓ=8` → 1.072 at `ℓ=60`; 1.128 at the
  maximiser's `ℓ=22`, i.e. 8.2 % of `B` against a ~3× gap).

## 🛑 The honest status of the bound itself

**Sub-linearity is MEASURED over `n ≤ 44`, not proved.**  Nothing in the arc proves it.

**And I diagnosed the weak step backwards once; the correction is the finding.**  The `(ℓ,W)`
reduction being tight means the loss is *not* there — so the **β-bound of #7070 is itself the weak
step**.  The reduction is a faithful instrument, and what it faithfully reports is that the thing
feeding it is loose.

## 🛑 The data cannot distinguish `√n` from `n^{3/4}` (2026-09-07)

Measured, with a control I ran because the inference was tempting: with `α = 1/8`, `C·α = 0.771`
far exceeds what the composition allows — **and `n ≤ 40` sits below the peak of the very statistic
being read**, so the exponent read off it is not the asymptotic exponent.  I refused that
inference; do not re-draw it.

The discriminator is the sibling bean **`qou-0ie7`** (the dropped `Σβ = n + ℓ(ℓ−1)/2` constraint),
which is the one remaining relaxation of size and is a *fresh formulation*, not another bound on
the same object.

## Four routes already tried, all through MOMENTS, all failed

Recorded in `qou-hok7` (2026-09-06, "Four routes to REV closed").  **The suggested attack is to
stop going through moments.**  Three further conjectures of mine on the Jensen step were refuted
in #7093, and the reformulation that survived is worth reusing: write the `β`'s by their partial
gap sums, which makes the object the **ground state of a one-dimensional repulsive gas with hard
walls**.  That is what to bound.

## Formalize-first note

Per the repo's §"Formalize-first probe discipline": this is exactly a *wide/expensive search over
a hypothesis class*, so find the invariant the whole class must satisfy before scanning again.
The `e_∞` leg's own history is the precedent — the concave-relaxation + supergradient certificate
replaced an unenumerable 1e10-block search with a 27-wide proved window.

**Do not close this bean** — its subject is an open conjecture.  And do not report a measured
exponent as a proved one.


## 2026-10-11 — the SHARP COEFFICIENT is proved as an upper bound: `M_n ≤ A√(2n) + O(n^{1/4})`

### 🛑 First, this bean's title and claim are stale and garbled — read before acting on them

- **`REV_n = O(√n)` is already a theorem.** #7185 (2026-09-11, `qou-0ie7`;
  `HookSumRowTangentBound.lean`, sorry-free) proved `M_n ≤ (C + L/2)√(2n) + C²/(2L) − C` and
  hence `REV_n ≤ 11.37√n + 176.3`. This bean was split out on 2026-10-10 from `qou-hok7`'s
  2026-09-07 text and carried the pre-#7185 framing forward. The open item was never "O(√n)" after
  2026-09-11; it was the **coefficient** of the upper bound.
- **"`M_n ≤ e_∞·√(2n)`, with `A = e_∞`" conflates two constants.** `A = Σ_j ε(2j−1) = 3.6034` is
  the coefficient (`lim M_n/√(2n) = A`, measured #7294); `e_∞ = 2.43930` is the **additive**
  excess over the staircase in the conjectured `M_n = A√(2n+1/4) − A/2 − B − C + e_∞ + o(1)`
  (hok7, 2026-09-13). `e_∞·√(2n)` is neither. The same conflation is in epic `qou-3e6w`'s
  "settled" list ("`e_∞ = A` is a k-free constant"). Not edited there — flagged here.

### What is now PROVED (modulo one numerically-verified attainment, below)

    M_n  ≤  A√(2n) + (A + c)(2n)^{1/4} + K₀          for every n ≥ 1,

    c  = Σ_k |ε'(2k)|√(2k) = 1.531799066065797,   |ε'(x)| = 2L/(q₀^{2x} − 1)
    K₀ = S₂ + c²/(2L) + c/2 + (A + c/2)²/L = 201.636,   S₂ = Σ_k k ε(2k) = 6.662469

**Consequence: `limsup M_n/√(2n) ≤ A`.** With the staircase (`V(δ_k) = Ak − B − F(n) + rem_k`,
exact) this is `lim M_n/√(2n) = A` along triangular `n` — the coefficient #7294 measured is now
proved on both sides there. The `[A√2, C√2]` bracket of #7286 is closed at its lower end.

**The argument (no moments, no Jensen, no `(ℓ,W)` summary).** In β-coordinates with
`t_i = β_i − m_i`, `m_i = ℓ + ½ − 2i`:

1. **Tangent lines per neighbour order.** `β_i − β_{i+k} − 2k = t_i − t_{i+k}`, so convexity of ε
   at `2k` gives `P ≥ Σ_{k<ℓ}(ℓ−k)ε(2k) − Σ_k |ε'(2k)|Δ_k(t)`, `Δ_k(v) = Σ_i (v_i − v_{i+k})`.
   With `F(β_i) ≤ C`: `Σ_c ε(h) ≤ ℓA + S₂ + Σ_k|ε'(2k)|Δ_k(t)`. This is #7185's step with the
   pair term **kept** instead of discarded.
2. **The hard-wall reference — this is the one-dimensional repulsive gas with walls the bean asked
   for.** An ℓ-row partition is `t ≥ w`, `w_i = i + ½` (the wall `β_ℓ ≥ 1`), `Σt = n + ℓ²/2`, and
   `2H = Σt² − Σm²` (#7294). Its ground state over the reals is the water-filling
   `p_i = max(τ, w_i)`. Three facts: **(Pythagoras)** `Σt² ≥ Σp² + ‖t−p‖²`; **(monotone)** `p`
   is nondecreasing so `Δ_k(p) ≤ 0` — the ground state widens no mean neighbour distance and loses
   nothing on the pair term; **(rounding)** rounding `p`'s flat part to the half-integer grid is a
   feasible ℓ-row partition, so `2(H − H_ℓ^min) ≥ max(0, ‖t−p‖² − ℓ/4)`.
   Then `Δ_k(t) ≤ Δ_k(t−p) ≤ √(2k)‖t−p‖` (Cauchy–Schwarz) and the pair-term loss is `≤ c·y`,
   `y = ‖t−p‖`, **paid by the within-row-count energy**: `sup_y [cy − (L/2)max(0,y²−ℓ/4)] ≤
   (c/2)√ℓ + c²/(2L)`.
3. **Row count.** For `ℓ ≤ √(2n)`, `ℓA ≤ A√(2n)` with no energy at all. For `ℓ > √(2n)`, #7185's
   `2(H_ℓ^min − H_min) ≥ (ℓ−k)² − r` with `r ≤ k` costs `A√k + A²/L`.

**Why the error is `O(n^{1/4})` and not `O(1)`, and why the earlier routes stalled.** The only
Θ(ℓ) quantity left is the integrality defect `ℓ/4` of rounding the water-fill to the half-integer
grid; through the trade-off it costs `√ℓ ~ n^{1/4}`. #7185's `r/2` defect is the same object one
level up and costs `A√r` here instead of `Lr/2`. The four moment routes and #7070's `(ℓ,W)` route
bounded the energy without the hard wall. The wall-free completed-square floor (my computation,
this session) is `Q(ℓ) = n²/ℓ + nℓ − ℓ³/12 + ℓ/12`, which has ZERO curvature at `ℓ = √(2n)` and
falls cubically past it — the same kind of failure as #7081's `Ĥ` ("negative energy no shape
has"), though `Ĥ` is a different Cauchy–Schwarz and I have not checked they coincide. The wall is what makes the reference monotone,
and monotonicity is what makes the pair-term loss vanish at the reference.

### Evidence

- Probe `computations/deltalambda/rev_sharp_coefficient_upper_bound_probe.py`, **8/8**, 31.6 s;
  witness `computations/rev-sharp-coefficient-upper-bound.witness.json`. Every step checked on
  **all 28,628 partitions with n ≤ 30**, exact rationals for (b), (d1)–(d4), (e): 0 violations each;
  the rounding excess reaches its bound `ℓ/4` exactly (so the `ℓ/4` is tight, not slack). The
  tangent pair bound has min slack exactly 0 (on staircases). The per-shape assembled chain holds
  on all 28,628 shapes; exact `M_n ≤ U(n) ≤` closed form for n = 1..40 (full scan, 37,338 shapes at
  n = 40, `M_40 = 19.7497` matching the arc's recorded value).
- Rate of the proved bound `U(n)` (closed form, no enumeration):
  `U/√(2n)` = 8.62, 5.23, 4.15, 3.81, 3.70, 3.66, 3.63, 3.62, **3.614** at n = 1e2..1e10, → `A =
  3.6034`. **The approach is slow** (+0.30 % at 1e10), as an `n^{−1/4}` correction must be. At
  reachable `n` it is far above the truth (U(40) = 103.5 vs M_40 = 19.7; #7185's bound there is
  232.0) — it is an asymptotic statement, not a numerical tool.
- Lean `folio/quantum-observable-universe/lean/QOU/BraidKnot/HardWallProjection.lean`, 4
  declarations, 0 sorry, `lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` =
  `[propext, Classical.choice, Quot.sound]` on all four: `waterfill_pythagoras`,
  `shiftDiff_nonpos_of_monotone`, `shiftDiff_le_of_reference`, `linear_sub_excess_le`. Generic
  ordered ring/field (§7c). Imports Mathlib only; wired into `QOU.BraidKnot`.

### What is NOT established — scope it exactly

- **The assembly is not in Lean.** The four lemmas are the non-trivial order-theoretic steps; the
  composition (tangent-line pair bound on ε, the β/t bookkeeping, the water-fill's explicit form
  and rounding feasibility) is verified per shape by the probe, not formalised.
- **Attainment `H(λ⁺) = P_k + r(k+1)`** — inherited from #7185's step (e); only `H_min(n) ≤ H(λ⁺)`
  is used, which is attainment by `λ⁺`. Verified exactly for n ≤ 30 here and in #7185, not in Lean.
- **The lower half at non-triangular `n`.** `liminf M_n/√(2n) ≥ A` is proved along triangular `n`
  only (staircase). For general `n` it follows from `H(λ⁺) = H_min(n)` exactly (verified, not
  proved); from the tangent bound alone `λ⁺`'s energy is only `≤ Lr/2`.
- **NOT `e_∞`.** The conjecture `M_n = A√(2n+1/4) + κ + o(1)` (κ = −10.72317, i.e. `e_n → e_∞`
  and the excess BOUNDED) needs the error `O(1)`; this argument gives `O(n^{1/4})`. Boundedness of
  `e_n` remains MEASURED (to n = 3916, #7294), not proved.
- **REV_n's coefficient.** `REV_n ≤ M_n + log p(n)` now gives `REV_n ≤ (A√2 + π√(2/3))√n + o(√n)
  = 7.661√n + o(√n)` (was 11.37); the entropy term is not sharp, so this is not REV's coefficient.

### Next step (judgement, not finding)

The O(1) target is now a precise statement about **one** defect: the `y`-trade-off charges the
pair loss linearly in `y` against an energy with a `ℓ/4` integer floor. To reach O(1), replace
`c·y` by the **integer** loss — at the rounded water-fill `q` (not `p`), `Δ_k(q) ≤ 0` still holds
(`q` is monotone), and `Σt² − Σq²` is the true excess over `H_ℓ^min`; what fails is Pythagoras at
`q` (it is not a projection). A discrete Pythagoras on the half-integer lattice (an L♮-convex
quadratic, where the integer minimiser does satisfy a local-optimality certificate — Murota 2003
Ch. 7, the same machinery as #7669's `Xbot` certificate) is the natural candidate. If it holds with
an O(1) defect, the argument gives `M_n ≤ A√(2n) + O(1)`, i.e. `e_n` BOUNDED — the headline that
`e_∞` presupposes.

**Do not close this bean** — the O(1) (bounded-excess) statement is still a conjecture, and this
bean's own title is superseded rather than settled by this entry.
