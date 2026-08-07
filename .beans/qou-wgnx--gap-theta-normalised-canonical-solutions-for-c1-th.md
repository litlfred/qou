---
# qou-wgnx
title: 'GAP: theta-normalised canonical solutions for C1 — the genuine untried route to the Stokes multipliers'
status: in-progress
type: task
priority: high
created_at: 2026-08-07T08:45:09Z
updated_at: 2026-08-07T10:04:33Z
---

Two routes are closed with NEGATIVES (steps 3 and 4): the sector data is
simply not visible in b_m asymptotics. Both tried to shortcut past building
the canonical solutions, and failed for that same underlying reason.

The untried route is the real one: construct the theta-normalised canonical
solutions in the ramified single-slope picture and read the connection
matrix off them directly.

Prerequisites ALREADY IN HAND (both algebraic, both survived):
  - B_1,2 = ±sqrt(q-1)/q from the ramified edge polynomial (bean qou-pw8l)
  - q-Gevrey order = Newton slope = 1/2, cross-checked independently

This is real work, not a refinement of steps 3-4. Level d=2 q-Borel /
theta-kernel resummation (RSZ, Asterisque 355 §3.3).

## 2026-08-07 — canonical solutions BUILT; connection matrix NOT obtained

**Done and solid.**
- Both theta-normalised canonical solutions at ∞ constructed and verified by
  substitution (residual ~1e-62 at 60 dps, z = 50/200/1000).
  `computations/qbeta/c3_w2_c1_theta_canonical.py`
- The theta-normalised series `h` is **entire in 1/z** — `|h_n|^{1/n}` falls
  monotonically to 0.128 by n=80, `h_n ~ T^n p^{-n(n-1)/2}`. So the theta
  normalisation fully absorbs the q-Gevrey divergence, and the ∞-solutions are
  genuinely analytic rather than merely asymptotic. This is what makes a
  numerical connection matrix feasible at all.
- 0-side: indicial `t² + (q−1)t + (q−1) = 0`, discriminant `(q−1)(q−5)`, so a
  conjugate pair exactly for `1 < q < 5` (substrate q₀ ≈ 1.11 is inside).
  `|t| = √(q−1) = 0.33163018974662244642` (20 digits). Series recursion
  derived; radius exactly 1. Lean: `QOU/QBeta/C1ZeroSideExponents.lean`.

**NOT obtained — and the first attempt produced a false positive.**

The bases share no domain (`g` radius 1, `h` entire in 1/z), so the 0-solutions
must be propagated outward by the functional equation
`y(p²w) = [(p²−1)y(pw) + (p²−1)y(w)]/(p⁴w²−1)`. Doing that and forming
`P = Y₀⁻¹Y_∞` gave `P(pz) = P(z)` to all printed digits — which looks like the
ellipticity check passing and is **vacuous**. The basis is degenerate:

    normalised determinant |det|/max²
      k=0   2.4e-18      k=30  2.4e-20      k=60  9.1e-22      k=98  8.5e-23

Already 1e-18 **at the matching point, before any propagation**. A
rank-collapsed matrix satisfies `P(pz) = P(z)` trivially, so the agreement
carried no information. Recorded as a negative.

**Cause.** The normalisation `e_t(z) = θ_p(z)/θ_p(z/t)` puts the two conjugate
exponents ~17 orders of magnitude apart (`col0/col1 ~ 1e17` at k=0), so the two
columns are near-parallel numerically from the start. This is a construction
problem, not only propagation loss.

**Next honest step.** A numerically stable 0-side basis. Candidates, none
tried: rescale each column by its own magnitude before forming the matrix;
backward (Miller) recurrence, which is stable in the direction the forward one
is not; or work with the solution *ratio* `y₁/y₂` and its elliptic transform
directly, avoiding the matrix inverse entirely. Until one of these lands the
Stokes multipliers stay open.

**Process note.** This is the fourth object in this arc whose name outran its
content, and the first where the agent nearly committed the error rather than
finding it — the check that caught it was looking at the *conditioning* of a
matrix whose ellipticity had already "passed".

## 2026-08-07 (later) — THE NEGATIVE ABOVE IS REFUTED; connection matrix OBTAINED

Everything under "NOT obtained" is wrong, and none of the three proposed
repairs was needed. `computations/qbeta/c3_w2_c1_connection_matrix.py`,
witness `c3-w2-c1-connection-matrix.witness.json`, 7/7 checks.

**The basis was never degenerate — it cannot be.** `p = √q` is real, so `θ_p`
has real coefficients and `θ_p(conj w) = conj θ_p(w)`. The exponents are a
conjugate pair, so for real `z`, `|e_{t₁}(z)| = |e_{t₂}(z)|` **exactly**.
Measured ratio `1.0`; max deviation `0.0`. The "~17 orders of magnitude apart"
diagnosis describes something that cannot happen. Scale-invariant conditioning
`|det|/(‖col₀‖‖col₁‖)` is **0.59 … 0.72** across the disc, not `1e-18`.

**Three premises, all wrong:**

1. *"|det|/max² ≈ 2.4e-18 means rank collapse."* `|det|/max²` is not
   conditioning — it is not invariant under rescaling one column. The
   Casoratian obeys `W(pz) = −(q−1)W(z)/(p⁴z²−1)` **exactly** (verified to
   `1e-150`), so it decays under outward propagation analytically, columns
   staying independent. The decay that looked like collapse is a theorem.
2. *"The two bases share no domain."* `h` **entire in 1/z** means `Σ hₖz^{-k}`
   converges for *every* `z ≠ 0`. With the 0-side radius 1 they overlap on the
   whole punctured disc and match directly. The propagation that lost the
   conditioning was never required.
3. *"`P(pz) = P(z)` passed, but vacuously."* It is **automatic** — for any two
   fundamental matrices, `Y₀(pz) = A(z)Y₀(z)` and `Y_∞(pz) = A(z)Y_∞(z)`, so
   `A` cancels. Never evidence, at any conditioning. Correctness check only.

Most likely origin of the original numbers: a fixed symmetric truncation of
`θ_p`. Its dominant term sits at `n* = log|w|/log p − 1/2`, already `~96` at
`|w| ~ 150`, so a window like `n ∈ [−50, 50]` misses the peak entirely. This
script uses an adaptive window centred on `n*`.

**Result.** `P = [[c₊, c₋], [conj c₊, conj c₋]]` — conjugate structure exact
(dev `0.0`), elliptic per entry `1e-27 … 1e-55`, converged in (dps, NG, NH) to
`1.4e-38`. `c₋` has **simple poles exactly at `z ∈ T·p^ℤ`** (zeros of
`θ_p(−z/T)`); `|c₋·θ_p(−z/T)| → 1.1846e-18`, finite.

**NOT claimed — flagging before it becomes the fifth instance.** `c₊` looks
constant at the substrate (`z`-spread `2.0e-27`, `arg c₊ =
1.26603946254300268722`) and I was about to call it *the connection constant*
on Liouville grounds. It is **not** an exact constant: the `z`-variation is real
and grows with `q` — `3.1e-23` at `q=1.35`, `1.2e-10` at `1.8`, `6.9e-6` at
`2.5`, `2.5e-3` at `3.4`, `0.72` at `4.8` — and is **identical across dps
140→320, NG 800→2200**, so it is not a precision artifact. "Connection constant"
is a `q → 1` statement only. The law behind it is unidentified: fitting
`ln(variation)` vs `1/log p` gives local slopes bouncing over `8.0 … 10.5`, and
the small-`q` points go non-monotonic at the numerical floor. `π² = 9.8696` (the
q-modular scale) sits in that band — **observation, not identification**.

**Stokes multipliers: STILL OPEN.** The connection matrix is a prerequisite for
them, not the same thing. That is the remaining work on this bean.
