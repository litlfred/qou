---
# qou-odh5
title: 'C1 infinity: extract the TWO Stokes multipliers via q-Borel/theta resummation (leading blocks now known)'
status: in-progress
pr: 8230
updated_at: 2026-11-17T06:37:48Z
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T23:30:00Z
updated_at: 2026-10-04T15:10:50Z
parent: qou-frzo
---

## Why this matters

The 1ppq L2 two-front survey names the `c₃` closure as the shared root of
**three of the five L2 misses** (Q_β, m_n, Δ_pn), and KC22 closed the entire
(q-)holonomic search — the object is in the Écalle acceleration class, so
**q-Borel / Stokes is the only surviving route**. This is that route's
concrete next step.

## What just landed (do not redo)

`computations/qbeta/c3_w2_c1_ramification_leading_blocks.py` + witness
`c3-w2-c1-ramification-leading-blocks.witness.json`, 3/3 assertions.

The `2026-08-01-c1-inf-slope-half-rsz-stokes.md` audit recorded
*"ramification: square roots `B₁,B₂` of the leading blocks — **open**
(compute the `A_i`)"*. That is now closed:

- `L₁ = (q²x−1)σ² − (q−1)σ − (q−1)`; at ∞ the valuation is `v = −deg`, and
  the lower hull is the single edge `(0,0) → (2,−1)`, **slope −½**.
- The nilpotency of `A(∞) = [[0,1],[0,0]]` that blocked the earlier script
  is not an obstacle to route around — it is exactly what a non-integral
  slope looks like in the companion frame.
- Ramifying with index `d = 2` (`x = z²`, `q = p²`, so `τF(z) = F(pz)`
  realises `σ` on functions of `z²`) moves the hull to `(0,0) → (2,−2)`,
  **slope −1, integral**. The `q^{1/2}` introduced here *is* the source of
  the "square roots".
- Edge polynomial `p⁴T² − (p²−1) = 0`, giving

      B₁,₂  =  ± √(q−1) / q

  distinct for `q ≠ 1`, hence two non-degenerate sectors — consistent with
  RSZ §3.3 `F(P₁,P₂) ≅ Matr_{1,1}(ℂ)² = ℂ²`, i.e. **exactly two Stokes
  multipliers**.

## The task

Extract the two multipliers `U ∈ ℂ²`. Ingredients now all present:

1. **Leading blocks** `B₁,₂ = ±√(q−1)/q` — landed above.
2. **q-Borel kernel** at level `d`: `t_{n+1} = qⁿ·tₙ`, Jacobi-theta
   coefficients — `QBorelKernel` formalized in Lean (`d = 1` case);
   the `d = 2` family is built from theta functions on the ramified cover.
3. **0-side canonical solution** — already CONFIRMED
   (`c3_w2_c1_module_exponents.py`: exponents = roots of `t²+(q−1)t+(q−1)`,
   discriminant `(q−1)(q−5)`).

Route: q-Borel transform the ramified operator at level `d = 2`, build the
two sector solutions from the theta kernel, and read the connection matrix
between them. The multipliers are the off-diagonal entries.

## Cross-check available

`qou-105e` (completed) verified the FW eq(73) `4₁` Stokes integer q-series =
divisor-function Lambert series with constant term `−1/4`. That is an
independent handle on Stokes data for `4₁` and should be used to sanity-check
whatever the C1 extraction produces, rather than treating the two as
unrelated.

`qou-0e66` (todo) proposes the complementary **diagrammatic** route
(McPhail–Snyder per-edge integer state-sum over crossings, worked for the
`5₂` Kashaev invariant). A state-sum plausibly *produces two numbers*; that
is only a sensible target now that the unknown is finite-dimensional.

## Discipline

- Anti-fit gated. A multiplier obtained by inverting `c₃` against its
  measured value is a **fit**, must be labelled one, and may not be wired.
- Report honest negatives. If the resummation shows the multipliers cannot
  supply the `c₃` bar-odd signature, that is a scope-(a) negative on this
  route and is worth as much as a closure.
- **Ownership:** the c₃/GGM front is flagged OWNED, "do not fork", in
  `docs/coordination/2026-07-17-1ppq-program-ownership-map.md`. Post intent
  and name the distinct angle before attacking; measured research overlap is
  permitted per AGENTS.md but must be deliberate and visible.


---

## STEP 2 LANDED (PR #4647) — the singularities are located

`computations/qbeta/c3_w2_c1_qborel_singularity.py` + witness, 4/4 assertions.

**q-Gevrey order = Newton slope = ½.** Fit `-log_q|b_m| = A m² + Bm + C` on
m ∈ {600,700,800} at 500 dps gives **A = 0.25 exactly**. The slope is an
algebraic invariant of the operator; the Gevrey order is the measured decay of
its solutions. They agree — an independent cross-check of step 1.

(Subtlety: the naive reading gives ½ not ¼. One expects
`b_{m+2} ≈ K q^{−m} b_{m+1}`. But `b_{m+1}/b_m ~ q^{−m/2} → 0`, so
`b_{m+1}+b_m ≈ b_m` and the recurrence is effectively **two-step**,
`b_{m+2} ≈ K q^{−m} b_m`, halving the exponent.)

**Two nearby singularities — the sector structure is visible.** With
`c_m = b_m q^{m(m−1)/4}` the level-½ q-Borel transform converges. Within a
branch `c_{m+1}/c_m` settles to ~1e-10 by m=400 and holds to m=900. But the
limit **differs between branches at 3.7e-4**:

    b^(1) (1,0)   ξ_s = 2.36571876588619
    b^(2) (0,1)   ξ_s = 2.36485280484881
    mix   (1,1)   ξ_s = 2.36515076658802

A single simple pole would be branch-independent. Branch-dependence is the
signature of **two nearby singularities**, each branch a different linear
combination — exactly what `B₁,₂ = ±√(q−1)/q` predicts. `q^{33/4} = 2.36507786`
sits inside the spread.

## REMAINING — this is now the whole task

Turn "two singularities are there" into **two complex numbers**:

1. **Resolve the pair.** They are ~3.7e-4 apart, so the plain ratio test
   returns a blend. Use a two-pole Padé (or a 2×2 Hankel/Prony fit on the
   `c_m`) to separate `ξ_s^{(1)}, ξ_s^{(2)}` individually.
2. **Match to sectors.** Check the separated pair against the exponentials
   indexed by `B₁,₂ = ±√(q−1)/q`, i.e. verify each singularity sits on the
   q-spiral `ξ q^ℤ` attached to its leading block.
3. **Take residues.** The Stokes multipliers are the connection data — the
   jump between the two Borel sums across the singular direction, i.e. the
   residues at the separated singularities.
4. **Cross-check** against `qou-105e` (completed): FW eq(73) gives the `4₁`
   Stokes integer q-series as the divisor-function Lambert series with
   constant term `−1/4`. Independent handle; use it.

Anti-fit gate unchanged: a multiplier obtained by inverting `c₃` against its
measured value is a fit, must be labelled one, and may not be wired.


---

## STEP 4 — theta-normalised route attempted; HONEST NEGATIVE (2026-08-07)

After the step-3 negative (the antipodal pair is two-step decoupling, not
sectors), the next idea was that the sector-mixing information *is* the
exponentially suppressed `b_{m+1}` coupling that the two-step asymptotic
discards. With `(b₀,b₁) = (1,0)` the odd subsequence is generated **purely**
by that coupling, so it isolates the mixing.

**Measured.** `t_m = b_{m+1}/b_m` obeys the Riccati recurrence
`t_{m+1} = (1 + 1/t_m)/[m+2]_q`, and

    b_{m+1}/b_m · q^{m/2}  →  C

converges, with `d(log_q t_m)/dm = −0.5` exactly. Stable to **5.5e-15**
within a branch by m = 800.

**But C is BRANCH-DEPENDENT:**

    C from (1,0) = 0.4227045134950364687
    C from (0,1) = 0.4228592992974597357
    relative spread = 3.7e-4

A Stokes multiplier is a property of the module and its connection data, not
of which solution you happened to start from. **A branch-dependent constant
cannot be one.** So `C` is not the target, and this route does not reach it
either.

**Leading-order structure of C.** The Riccati fixed point gives
`C² = (q − q⁻¹)·q^{−3/2}`, i.e. `C_pred = 0.42281446251`. That sits *between*
the two measured branch values and agrees with each only to ~2.6e-4 — the
same scale as the branch spread itself.

**The recurring 3.7e-4.** This same spread has now appeared in three
independent estimators: the step-2 single-pole ratio test, the step-3 Prony
blend, and this `C`. It is a real feature of the problem at that scale. What
it *is* has not been established — and identifying it is probably the actual
next question, ahead of any further attempt at the multipliers.

## Process note (worth recording)

Three times across steps 2–4 I wrote an interpretive conclusion into the
probe's output *before* seeing the numbers, and the data contradicted it each
time: "ratios are NOT settling" (they settled to 10 digits), "same
singularity ⇒ module invariant" (branches disagreed), "SAME ⇒ module
invariant" for `C` (branches disagreed again). Each was caught, but only
because the numbers were printed alongside. **Print the measurement; derive
the label afterwards.**

## Status

`qou-odh5` remains **open**. Two routes are now closed with scope-(a)
negatives — Prony/ratio (step 3) and the Riccati mixing constant (step 4).
Neither touches steps 1–2, which are algebraic and stand:
`B₁,₂ = ±√(q−1)/q`, and q-Gevrey order = Newton slope = ½.

The untried route remains the genuine one: construct the theta-normalised
canonical solutions in the ramified single-slope picture (`QBorelKernel`,
level d=2) and read the connection matrix between them. Nothing attempted so
far actually builds those solutions — steps 3 and 4 both tried to shortcut
past them with asymptotics of the raw coefficients, and both failed for the
same underlying reason: the sector data is not visible in `b_m` asymptotics.


## TAKEOVER 2026-09-07 (stalled-claim protocol)

Claimed under the AGENTS.md stalled-claim rule. Evidence it is stale, not live:

- last commit `2ce063f238` **2026-08-07**, i.e. **31 days** without a commit
  (threshold is 3 h for the branch backing a live in-progress bean);
- that commit is **NOT on main** — the work never landed;
- no `odh5` activity in the last 24 h other than my own bean notes;
- bean `updated_at` still 2026-08-06 while `status` reads `in-progress`.

Continuing from `main`, not from that branch's tip. **Its branch is not touched
and will not be force-pushed.**

## Why now: this bean and `qou-hok7` need the SAME object

Three names for one gap:

- **`qou-hok7`** (deuteron q-Borel divisor) needs a **half level**: `Z_n ~ q0^{n^2}`
  requires exponent `n(n-1) = 2*C(n,2)`, and `qBorelExp d n ~ n^2/(2d)` DECREASES
  in `d`, so no integer level supplies it. Lean, sorry-free:
  `QOU.MathlibExt.QBorelKernel.two_mul_qBorelExp_one`.
- **this bean** records the hull at infinity as the single edge `(0,0) -> (2,-1)`,
  **slope −1/2**, with the ramification square roots `B_1,B_2` open.
- **`QBorelKernelLevel.lean:24-27`** names the **ramified level-2 family** as open,
  for exactly the slope-1/2 case.

Constructing it once unblocks both. That is why this is being taken over now rather
than left: it is not a second tranche, it is the same one.


## 🛑 TAKEOVER RETRACTED SAME DAY (2026-09-07) — the target rests on a retired chain

I claimed this bean above under the stalled-claim rule. **The staleness finding
stands** (last commit 2026-08-07, 31 days, never landed). **The takeover does not**,
and I am releasing it without doing the work.

Reading the corpus before building — which is what the discipline is for — turned up
that this bean's target was superseded a month ago, on the very day its three staged
sub-beans were scrapped:

- `qou-qbg2` (S1), `qou-qbr3` (S2), `qou-qbs4` (S3) were **all scrapped in one batch
  at 2026-08-08T11:35:00Z**.
- [`2026-08-08-rsz-c1-infinity-route-closed.md`](../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)
  is why. The chain this bean runs on —
  *"C1 has slope ½ ⇒ RSZ level d=2 ⇒ `B_{q,2}` ⇒ `F(P₁,P₂) ≅ ℂ² ⇒ two multipliers`"* —
  is a **mis-citation**: RSZ §3.3 is titled *"…in the case of **integral slopes**"*,
  and ½ is not integral. *"Every number in it is right. The reading is not."*
- This bean's body cites `2026-08-01-c1-inf-slope-half-rsz-stokes.md`, whose framing
  that closure explicitly supersedes.

Also relevant, and carefully scoped by the corpus itself:
[`2026-08-08-c1-infinity-has-no-stokes-multiplier.md`](../docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md)
retracts the **local isoformal** moduli at `∞` (dimension 0 — C1 is pure isoclinic
there) while insisting the **connection-matrix** multipliers are a *different object*
and remain open. So "extract the two C1 Stokes multipliers" is ambiguous between a
non-existent object and a live one, and this bean does not disambiguate.

**Where the work actually goes**, per the closure audit: **`qou-wgnx`** (theta-normalised
canonical solutions → the connection matrix and its invariant `χ`, already built) and
**q-native alien calculus** — right for the reason RSZ was wrong: `F(P₁,…,P_k)` is built
on the slope filtration and needs `k ≥ 2`, while alien derivations need no filtration.

**Recommended disposition (owner's call, not mine):** re-title this bean to the
connection-matrix object and fold it into `qou-wgnx`, or scrap it as superseded like its
three children. I have not changed its status.



## TAKEN UP 2026-09-07 (owner: "take up idle as relevant")

The owner has ruled that dormancy is not a reason to stand down. Claiming this
bean under the stalled-claim protocol, with the staleness recorded rather than
glossed:

- last genuine commit is a month old (see the dormancy table in `qou-hok7`);
- the whole C1 ∞ arc stopped on 2026-08-08, the day the RSZ route closed;
- **no sibling branch is touched and none will be force-pushed.**

Work continues from `main` on `claude/alien-calculus-surreal-integration-2t823z`.

**Scope of the takeover is the q-NATIVE ALIEN CALCULUS route**, which is what the
closure audit names as the successor — NOT the retired RSZ slope-½ chain, and NOT
the local-isoformal object that `2026-08-08-c1-infinity-has-no-stokes-multiplier.md`
proves has dimension 0.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8230)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8230` at `1bb9d799f645494190e9e4834f3982913ab5e918`).
- **Lean Formalization**: `QOU.QBeta.PentagonTwoRouteAndC1RamifiedStokesBrick.c1_ramified_edge_polynomial_and_stokes_connection_determinant` (Ramified d = 2 C1 operator edge polynomial root verification, positive spectral gap, and unit-determinant 2x2 Stokes connection product.)
- **80-dps Witness**: `computations/probes/pentagon-two-route-and-c1-ramified-stokes-brick.witness.json` (`scriptHash: ad15e8ab2a08`, `scriptCommitSha: 4eaeef60b72e32fbaaef92149ff8588e4dde4090`).
