---
# qou-as81
title: 'A1 (live): certify an UPPER bound on Xbot so the e_inf join needs no G1'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:48Z
updated_at: 2026-10-11T08:00:00Z
parent: qou-3e6w
blocking:
    - qou-jz80
---

**The arc's live front.**  Parent epic `qou-3e6w`.  Carries PR
[#7419](https://github.com/litlfred/qou/pull/7419) (open, 5 commits, `mergeable_state: dirty`).

## Why an upper bound on `Xbot`, and not G1

The `e_∞` join (#7335) substitutes `Xbot := Xblock`, which is licensed only by **G1**
(`Xbot(s) ≤ Xblock(s)`, bean A2).  But the join does not *need* a pointwise inequality — it
needs a **finite window**.  Separate certified caps `B_top` and `B_bot` give the same cut
with G1 nowhere in the argument.  So this task **bypasses** G1 rather than proving it.

## State as of 2026-09-15 (on the PR branch, not on `main`)

**The per-row coercivity transfers, and is 9.6× too loose.**  0 violations over 17,534
`(profile, pe)` pairs, tightest slack `0.4012`; uniform cap **20.7758** against an enumerated
`Xbot` maximum of **2.1598**.  #7349's top-edge analogue was 1.82× and *even that* gave an
unenumerable cut.  (A bug of mine first summed caps across all nine `pe` frames for **171.11**;
a block occupies exactly one frame, so the bound is the max over `pe` — `20.78` at `pe = 6`.
3.9× inflation, caught before it was quoted.)

**The concave relaxation reaches the bottom edge.**  Four premises verified rather than assumed:

- **The real-`u` extension is EXACT at integers, not merely valid.**  `delta_excess`'s one-body
  term `fi(β) − fi(b0)` is a partial sum with no canonical real extension.  The obvious integral
  extension `∫₀ᵘ eps(b0+t)dt` is concave *and* an upper bound — and **not exact at integers**, so
  it would carry avoidable slack at every one.  `R(b0) − R(b0+u)` with `R(x) = Σ_{j≥1} eps(x+j)`
  is both, because the constant `Σ_m eps(m)` cancels.  36 `(pe, block)` pairs, worst diff **8.66e-25**.
- **Concave:** min gap `0.0057` over 300 random feasible triples.
- **Closed-form tails and the analytic gradient** agree with direct sums to `6.2e-25` / `4.2e-16`.
- **`Γ_j` is exactly block-length-free** (`1.7e-23` across `T = 3, 7, 11`): the block rows above
  `j` and the undisplaced tail above the block are one sum split at an arbitrary place.  So a
  length-`T` program is the restriction of **one** program to its first `T` coordinates, and a
  certificate at a zero-padded ascent point bounds every length at once.

**Result:** 0 monotonicity violations, worst KKT residual `8.9e-14`, per-program certificate
closing with slack `3.9e-12` at **1.23×** the enumerated maximum (`T ≤ 6` smoke range).
Enumerated `Xbot` max (`BMAX=10, BUMAX=3`): `2.159802376118285961604` at `s = 14`,
`bot [1,1,1,1,2,2,2,2,1,1]`, `pe = 3`.  The relaxed sup peaks at **`pe = 3`** (2.742) and declines
(4: 2.672, 5: 2.414, 6: 1.978) — so the enumeration's `P_EXT_MAX = 8` is comfortably past the peak
and the integer argmax frame matches the relaxed one.

## 🛑 The one structural obstruction, and it is about the CLASS not the analysis

**#7349's block-length bound does NOT transfer.**  Its blocks have every entry `≥ 1`, so a row
whose tangent slope falls below `ln q₀/2` contributes a strictly **negative** cap and the
cumulative cap eventually drops below the certified bound.  The bottom class permits **zero**
entries (`bot_profiles` requires only the leading one positive), so `u ≥ 0`, every row cap is
`≥ 0`, and the cumulative cap **never falls**.

I wrote the transfer first and asserted padded rows are charged zero.  **They are not** — every
`Γ_j` is strictly positive, in the pure AP exactly `Σ_{i odd ≥ 1} gx(b0_j + i)`, the odd gaps the
one-body term reaches and the gap-2 ladder does not.  Measured padded charge **2.4707** at `pe = 2`.
Caught by a guard that refused to return a truncated sum, not by reading the code: the termination
test was written for `cap == 0`, which never fires.

## The open step

**The plain relaxation is valid and measurably NOT tight** — a real `u` collects a gain from an
arbitrarily small displacement on arbitrarily many rows; no integer block can, since entries jump
`0 → 1`.  At `pe = 2` the relaxed sup is still rising by `+0.2301` at `T = 6`.

So the gap is an **integrality gap**, and the attack is a valid inequality rather than more compute:
every integer `u_j ≥ 0` has `u_j² ≥ u_j`, hence

    sup_integer G  ≤  sup_{real u ≥ 0} [ G(u) + λ Σ (u_j² − u_j) ]   for any λ ≥ 0,

and `+λΣu²` eats into `G`'s own `−(ln q₀/2)Σu²`, so the program stays **concave** for
`λ < ln q₀/2`.

**Select `λ` on the CERTIFICATE, never on the T-free tangent sum** — that proxy goes the *wrong*
way (14.17 at `λ=0` rising to 251 near the concavity limit), because the cap is
`Γ'²/(2(ln q₀ − 2λ))` and the denominator collapses faster than the numerator shrinks on the
dominant row.  Selecting by it returns `λ = 0` and discards the whole tightening.

**And the incumbent must be the INTEGER maximum.**  `B_RELAX` (the `λ=0` ascent value) is *not*
a lower bound on `sup G_λ`, because `G_λ(u) = G(u) + λΣu(u−1)` is smaller wherever coordinates sit
below 1.  What survives the change of program is the integer maximum, where `Σu(u−1) ≥ 0`.

## Two search bugs, both caught by invariants rather than inspection

1. **Cold start + value-based stopping.**  `pe = 2` returned `1.8466` at `T = 6` against `2.0310`
   at `T = 5` — impossible, since padding the `T=5` optimum with a zero is feasible at `T=6`.
   From `u = 0` every barrier is at its tightest and coordinates unlock one sweep at a time; and
   `|G_k − G_{k−1}| < 1e-16` was satisfied while the largest coordinate gradient was still `1.12`.
   **Warm-start across `T`; stop on the projected gradient, not the value.**
2. **The lower barrier is not 0.**  A row *below* `i` displaced by more than the gap forces
   `u_i > u_j − (b0_i − b0_j) > 0`.  The search maximised over `[0, hi]` and evaluated the
   derivative at an infeasible `0`, where `gx` returns a **plausible negative number** rather than
   failing.  `gx` now **refuses** a non-positive argument and `_lo_for` keeps it from having to.

## Also two apples-to-oranges comparisons of mine, fixed

`B_BOT = max(B_CERT, B_ALLT)` (B_CERT covers only `T ≤ TMAX`), and `_TIGHTENS` comparing a
max-over-`pe` figure at `λ*` against a single-frame figure at `λ=0`.  The λ gain must be reported
like for like at the scan frame.

## Artifacts

- `computations/deltalambda/rev_e_infinity_xbot_relaxation_probe.py` (R1–R6) — on the PR branch.
- `computations/deltalambda/rev_e_infinity_xbot_coercivity_probe.py` (X1–X4, 4/4) + witness.
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean` — nine
  sorry-free declarations, `#print axioms` → `propext, Classical.choice, Quot.sound` only.

## Next concrete step

Re-run the full probe (the final `B_allT`, the λ scan, `pe0` and the G1-free cut were only
partially observed before a container restart), then land it via task A6.

**Do not close on a partial run.**


## 2026-10-10 — R5 partial, the tightness number, and a BUDGET finding that blocks the PR

Full re-run attempted on `main` + `claude/xbot-upper-bound-2026-09-15` (#7419). **R1–R4
complete and green; R5 reached 7 of 9 frames; R6 never ran.** The corrections this forced
to `qou-hok7`'s recorded figures are on that bean, including one that is inverted rather
than stale.

### 🛑 The probe does not fit in one run window, and that is the live blocker

Measured: **~58 min to complete R1–R4, then ~30 min for 7 of R5's 9 frames**, at which
point the 90-minute background limit killed it. Remaining when killed: 2 frames, the `lam`
scan (a grid of ascents at the worst frame), and R6. The script is **straight-line with no
`--only` / no resume** — a restart re-runs R1–R4 from scratch before reaching R5, so a
second attempt is a coin flip against the 2-hour maximum.

**So #7419 cannot be merged on its own stated standard yet**, and the obstruction is not
mathematical. Three ways out, in the order I would try them:

1. **Checkpoint R1–R4.** They are cheap verifications whose results do not change between
   runs; caching them to a sidecar and skipping on a hash match recovers ~58 min, which is
   the whole shortfall. This is the fix I would make.
2. **A `--only` selector.** Smaller than (1) and makes the probe usable interactively, but
   it does not help an unattended full run.
3. Narrow `TMAX`/`JPAD`. **Rejected** — that is fitting the test to the budget, and the
   `T <= 12` sweep is exactly what corrected `qou-hok7`'s `pe` profile.

### R5 as far as it got — ascent at 26 rows, all-T bound over 32

| `pe` | relaxed sup at the ascent point | all-T bound | KKT residual |
|---|---|---|---|
| 0 | 1.53872109027161153 | 2.15980237611828596 | 8.691e-14 |
| 1 | 2.31171169398245923 | 2.31171169400596190 | 9.826e-14 |
| 2 | 2.81390919493735196 | 2.81390919496107597 | 9.320e-14 |
| 3 | 3.10309806570584077 | 3.10309806572697677 | 7.974e-14 |
| 4 | 3.23776802870188959 | 3.23776802872415138 | 8.297e-14 |
| 5 | 3.27638211927474961 | 3.27638211929654931 | 7.697e-14 |
| 6 | 3.27708095409687544 | 3.27708095412283411 | 9.445e-14 |

Three things worth keeping from that table, none of which needed the last two frames:

- **The all-T bound agrees with the ascent value to ~2.4e-11 at every frame.** That is the
  T-freeness of `Gamma_j` doing its job: the certificate at a zero-padded point bounds every
  longer block, so one certificate covers all lengths and the 32-row evaluation adds
  essentially nothing over the 26-row ascent.
- **`pe = 0`'s all-T bound is the enumerated maximum to 18 digits** (`2.15980237611828596`
  vs `2.159802376118285961604`). Not a coincidence and not a bug: the certificate is
  reported against `max(integer incumbent, G_lam(w))`, and at `pe = 0` the relaxed value
  (1.5387) sits *below* the integer maximum, so the incumbent dominates.
- **Padded charge is exactly 0.0 at every frame**, for the reason
  `box_charge_eq_zero_of_nonpos` names (`g <= 0`, `lo = w = 0`). See the inverted claim on
  `qou-hok7`.

### The tightness number to watch — 1.517x, not 1.23x

Peak all-T bound so far is **3.27708** at `pe = 6`, against the enumerated `Xbot` maximum
**2.159802376118285961604**: a ratio of **1.517x**. The `T <= 6` smoke range suggested
**1.23x**, so the gap widens with the window rather than closing, and `pe = 6` was still
rising (3.27638 -> 3.27708, nearly flat) when the run died.

Compare: #7349's certified top edge closed at **1.04x** and even its 1.82x predecessor gave
an unenumerable cut of 90. The coercivity route was **9.62x**. So 1.517x keeps the concave
route clearly alive and clearly not yet a tool — **and the honest statement of the result
is "1.5x with the cut not yet computed", not "the certificate closes with slack 3.9e-12"**,
which is a statement about the *smoke range* and is how this would get over-reported.

What is still unmeasured, and would decide it: the two remaining frames, the `lam` scan
(which is the only thing that can pull 1.517x down, since the gap is an integrality gap),
and R6's actual cut width.

**Do not quote 1.23x. Do not merge #7419 until R5/R6 complete.**


## 2026-10-10 (later) — R5 COMPLETE and PASSED, and it refutes three claims I made an hour earlier

Second full re-run, killed at the **2-hour maximum** (the harness's longest window) with
**5 of 6 checks green**: R1-R4 and **R5 complete**. R6 printed its banner and nothing else.
So the arc now has a real `B_allT`, and it is not the number I was quoting.

### The result

    B_allT = 3.37712160481715115067163  at pe = 8, lam = 0.010434072
           = 1.56363x the enumerated Xbot maximum 2.159802376118285961604
    Gamma_max measured      = 1.418957192   (uniform bound 2*Rg(0) = 4.392059968)
    wall depth bound: pe0   = 66  for blocks of length <= 26
    worst KKT residual over the 9 frames ~ 9.2e-14

`lam* = 0.010434072` is **non-zero**, so the `u^2 >= u` tightening was selected and exercised
rather than discarded — which is what the "select on the certificate, never on the tangent sum"
rule was written for. 1.56363x is therefore the **post-tightening** figure.

### The full R5 profile, and why I misread it

| pe | ascent value | all-T bound | padded charge |
|---|---|---|---|
| 0 | 1.53872109027161153 | 2.15980237611828596 | 0.0 |
| 1 | 2.31171169398245923 | 2.31171169400596190 | 0.0 |
| 2 | 2.81390919493735196 | 2.81390919496107597 | 0.0 |
| 3 | 3.10309806570584077 | 3.10309806572697677 | 0.0 |
| 4 | 3.23776802870188959 | 3.23776802872415138 | 0.0 |
| 5 | 3.27638211927474961 | 3.27638211929654931 | 0.0 |
| 6 | 3.27708095409687544 | 3.27708095412283411 | 0.0 |
| 7 | 3.27708095409687544 | 3.27708095412057675 | 0.0 |
| **8** | 3.27705877732425894 | **3.37712160481715115** | **0.100063** |

### 🛑 Three claims of mine, all wrong, all from reading an incomplete run

1. **"The bound has saturated in `pe` — a plateau, not a climb."** Wrong. `pe = 6` and `pe = 7`
   agreeing to 18 digits is a **local flat**, and `pe = 8` jumps **+0.10004**. The maximum sits
   on the **last frame scanned**.
2. **"`PEMAX` is adequate for R5 on R5's own showing."** Wrong, and backwards: a maximum at the
   boundary of the scanned range is precisely the "still rising at the edge" signature I had
   just claimed was retired. It is the same defect that made this bean's `T <= 6` `pe` profile
   wrong, one check later. **`PEMAX = 8` is NOT self-justifying for R5** — R4's turnover at
   `pe = 4` does not transfer, because R5 runs a different program (full padded length, `lam`
   tightening) and its profile is monotone where R4's turns over.
3. **"Padded charge is 0.0 on every single frame, so `sum_charge_extend` is the operative lemma
   and `sum_charge_extend_le` is never exercised."** Wrong at `pe = 8`: **0.100063**. The zero
   holds at `pe <= 7` only.

Note what 1 and 3 have in common: both were true of the **8 frames that had run** and false of
the **9th**, and in both cases the 9th is the one that matters. Reading a monotone-looking
prefix as a converged whole is the error, and it is the third time this session the same shape
has bitten (the `T <= 6` profile; the stale `.lake` tree; this).

### What survives, and one conservative choice that paid off within the hour

- **`fe54aa347ff` is still correct as Lean.** `padded_tail_charge_eq_zero` is *conditional* on
  `Gamma J <= lam`; at `pe = 8` that premise evidently fails for some row, so the theorem simply
  does not apply there. A conditional lemma is not refuted by its hypothesis failing.
- **Keeping `sum_charge_extend_le` was right, for exactly the reason given.** Its retention note
  read: *"nothing yet proves the charge is zero at EVERY admissible ascent point rather than at
  the nine measured ones."* The counterexample arrived two frames later. The tail-bounded form
  is **load-bearing at `pe = 8`** and must not be removed.
- `tail 0.0` still holds at all nine frames — it is the *padded block*, not the geometric tail,
  that is non-zero at `pe = 8`.

### 🛑 The probe cannot complete in one harness window — the checkpoint is now REQUIRED

Run 1: killed at 90 min with R5 at 7/9. Run 2: killed at **120 min, the maximum**, with R5
complete and R6 unstarted. Timings are reproducible: R1-R4 ~58 min both times, R5 ~55 min.
R6 needs more than the ~2 min left. **Do not simply restart it** - the harness note is explicit
that a job already at the longest window should not be re-run unchanged, and two data points say
it does not fit.

So the checkpoint is no longer a nice-to-have. Design constraints, measured:

- R5 needs **`_r4`** (the per-`(pe,T)` records, to pick the worst frame) and **`_ARG[(pe,T)]`**
  (the ascent point, as a warm start). A flag cannot skip R4; state must persist.
- The probe is **deterministic**: `pe = 2` returned `2.74201217067973621` byte-identically across
  both runs. So a checkpoint is sound in principle.
- Key it on a hash of **both** sources - this probe and the executed
  `rev_e_infinity_edge_limit_probe.py` - and make a key mismatch **refuse to load**, loudly, so
  no report can claim 6/6 fresh from a resumed run.
- **Do NOT** pass the worst frame in as a hint. That turns R5's frame selection from a
  measurement into an input.
- **Do NOT** narrow `TMAX`/`JPAD`/`PEMAX` to fit the budget. Correction 2 above makes that
  worse, not better: `PEMAX` may need to **grow**.

### Consequences for the arc

- **#7419 still cannot merge on its own standard.** R6's cut is the one number its conclusion
  needs and it has never been computed.
- **`PEMAX` must be re-measured**, not inherited. If `B_allT` keeps rising past `pe = 8` the
  1.56363x is itself a lower bound and the G1-free cut is wider still.
- **Quote 1.56363x, not 1.23x and not 1.517x.** Both earlier figures were partial-run artifacts
  of mine; 1.23x was the `T <= 6` smoke range and 1.517x was the 8-frame prefix.


## 🛑 2026-10-10 — R6 EVALUATED, AND IT FAILS. Scope-(a) negative, with the target quantified

R6 never ran inside either killed run. Evaluated directly from R5's recorded `B_allT`, executing
the probe's own prelude so `cut_for`, `xrun`, `E_INF_7335` and `B_TOP_CERT` are the **committed**
definitions (nothing retyped), with `xrun` memoised across the two thresholds — which cannot
change the answer, since the two `cut_for` calls differ only in `th`.

    E_INF_7335  = 2.439296455120784027065
    B_TOP_CERT  = 2.253735567000904882966        (#7349, certified)
    B_allT      = 3.37712160481715115067163      (R5, pe = 8, lam = 0.010434072)

    cut via G1   (B_top, B_top)  = 27     ->  6,325,874 blocks   ENUMERABLE
    cut G1-FREE  (B_top, B_allT) = 48     ->  NOT enumerable (> 32)
    widening                     = 21

    R6 verdict (cut_free <= 32):  FALSE

**`cut via G1 = 27` reproduces #7349's cut exactly**, which is the consistency check that makes
the 48 credible rather than a harness artifact.

### The verdict, scoped per AGENTS.md

**Scope (a), not (b).** What is established: *the concave relaxation plus the `u^2 >= u`
tightening, as assembled, gives a `B_bot` that is not tight enough to make the G1-free cut
enumerable.* That constrains a **magnitude**, not an ingredient. Nothing here shows no `B_bot`
can be tight enough — and the required tightness is now a number rather than a hope.

### How tight `B_bot` has to be — the forward target

`cut_for = max{ell : xrun(ell) > th}` with `th = E_INF - B_top - B_bot`, so
`cut <= K  iff  xrun(K+1) <= th  iff  B_bot <= E_INF - B_top - xrun(K+1)`:

| goal | `xrun(K+1)` | `B_bot` must be <= | as a ratio of the enumerated max | overshoot now |
|---|---|---|---|---|
| **cut <= 32** (enumerable at all) | `xrun(33) = -2.37879957477410162` | **2.5643604628939807681** | **1.1873125x** | **0.8127611419** |
| cut <= 27 (lose nothing vs G1) | `xrun(28) = -2.11794595238436931` | 2.3035068405042484508 | 1.0665359x | 1.073614764 |

So the bypass needs `B_bot` tightened from **1.5636x to 1.1873x** — a **24 % improvement** — to
be enumerable at all, and to **1.0665x** to cost nothing against the G1 route. For calibration,
#7349's top edge reached **1.04x** by the same concave-relaxation route, so 1.1873x is not
obviously out of reach. **That is the number the next attempt is aiming at, and it was not
available before this evaluation.**

### Where the remaining looseness is, and what it is NOT

- **`lam` is already doing work** — `lam* = 0.010434072` is non-zero, so the integrality-gap
  tightening is exercised, not discarded. The residual 1.5636x is what survives it.
- **`PEMAX` is the open flank.** `B_allT`'s maximum sits at `pe = 8`, the **last frame scanned**
  (`pe = 6 ≡ pe = 7` is a local flat; `pe = 8` jumps +0.10004). If the bound keeps rising,
  1.5636x is itself a lower bound and the cut of 48 is optimistic. **Re-measure `PEMAX` before
  trusting 48 as the gap to close.**
- The padded charge at `pe = 8` is **0.100063** — the only frame where it is non-zero, and
  almost exactly the `pe = 7 -> 8` jump. Worth checking whether the `pe = 8` excess IS the
  padded charge: if so, a tighter padding argument at that one frame recovers most of it.

### 🛑 R6's real cost, and the probe's true total

Measured: `cut_for` is `max(ell for ell in range(1, 3000) if xrun(ell) > th)`, i.e. ~2,999 calls
to the committed `_ap_value` on a length-`ell` word at 1e-40 scale. **2610 s (43.5 min)** for the
first threshold; the second was **0 s** purely because of the memoisation. Un-memoised, as the
probe runs it, **R6 is ~87 min on its own.**

So the probe's true total is **R1-R4 ~58 min + R5 ~55 min + R6 ~87 min = ~200 min** against a
**120-min** harness ceiling. It does not fit, and no single-window restart can make it fit. This
also corrects my own claims twice over: I called R6 "seconds of work", then "minutes". It is
three quarters of an hour even memoised.

**Two safe speedups, both verifiable, neither changing a result:**

1. **Memoise `xrun`.** The two `cut_for` calls share every value. Halves R6. Zero semantic change.
2. **Early-break on monotonicity.** `best` stops moving at `ell ~ 250` and `xrun` is antitone over
   the range (checked: `xrun(33) > xrun(49)`). Verify antitonicity over the scanned window and
   break once `xrun(ell) <= th`, and R6 becomes near-instant — the scan to 3000 is ~12x wasteful.
   **Verify, do not assume**: the probe deliberately scans the full range, so the monotonicity
   has to be established rather than asserted.

### Consequence for the arc and for #7419

- **A1 does not close as assembled.** The G1 bypass is live but not yet a tool, and that is now a
  measured statement with a target attached rather than a verdict.
- **#7419's conclusion needs rewriting, not just its figures.** Its body says the next step is
  "the same tightening rather than a new idea"; the tightening has now been applied and leaves
  1.5636x. The honest headline is: *the concave route transfers, the `u^2 >= u` tightening is
  exercised, and the resulting cut is 48 — unenumerable, 21 wider than the G1 route, needing a
  further 24 % on `B_bot`.*
- **G1 itself is untouched** (`qou-o7c0`): still neither proved nor refuted. It has not become
  more necessary — the bypass is a magnitude short, not wrong.

## 2026-10-10 (afternoon) — integer hi_j floor, checkpoint, and the Murota lead CHECKED

**Integer box (`hi_j` floor), scope (a) negative.** Rounding the per-row confinement box to
`[ceil lo_j, floor U_j]` (sound: Xbot is an integer maximum) moves the all-T bound at `lam*`,
`JPAD = 26` from `3.377121604817151150672` to `3.376047226439865682559` at `pe = 8`
(gain 1.07e-3; pe 6/7 gain < 1e-12). Ratio 1.5636x -> 1.5631x; the cut stays 48. The boxes are
wide (U 12..35) and the ascended rows carry gradient ~1e-12, so almost nothing is charged.

**Checkpoint.** R1–R5 are keyed (sha256 of source-to-stage-end + evaluator + q0 + dps + env);
restore measured at 2.2 s, stdout and witness identical apart from timestamps. Commit f3556b276.

**The L♮ (Murota) lead holds, and it is the route.** `G(u) = sum_j phi_j(u_j) +
sum_{j<j'} psi_{jj'}(u_j' - u_j)` with every piece univariate concave and a domain cut out by
box and difference constraints — the L♮-concave form (Murota, *Discrete Convex Analysis*, 2003).
For such functions an integer point is a global maximum iff no move `u ± chi_S` improves it,
and the best move is an s–t min cut (the gain is supermodular with pairwise structure).

Measured with a scratch script (not committed; `/tmp/claude-0/hj/lnat.py`):
- split form of `G` equals the probe's `G` to 8e-25; zero-padding leaves `G` unchanged.
- steepest ascent from `u = 0`, exact min-cut moves, converges in <= 2 steps in every frame.
  Integer max per frame: pe 0: 1.0762795, 1: 1.7009977, 2: 2.0254822, and **pe = 3..20:
  2.159802376118285961604** (N = 40 rows), the same profile shifted up by one row per frame.
  This equals the BMAX=10/BUMAX=3 enumeration exactly — the enumeration cap was not binding.
- brute force over every `S ⊆ 10 rows`, both signs, all 9 frames at the found optimum:
  best gain **-0.000759** (pe = 2). No improving move exists, so the min cut is right there.
- Frame identity, exact: frame `pe+1` with `u_0 = 0` IS frame `pe` shifted — the one-body term
  `R(b) - R(b+u)` is precisely the pair interaction with the infinite sea of rows below.

**What it would buy.** With `B_bot = 2.159802376118285961604` the G1-free cut is **25**
(`xrun(25) = -1.96143 > threshold -1.97424 >= xrun(26) = -2.01360`), against 48 now and the
enumerability limit 32. That would close this bean's goal.

**Still open — do not quote 2.1598 as certified for all T and all pe until both land:**
1. *Tail lemma (all T).* Rows above the support never help. Sketch: split `S = S1 ∪ S2` with S2
   in the zero region; each maximal run in the gap-2 AP loses `sum_d mult(d)[delta(2d-1) -
   delta(2d)] > 0` by reflection symmetry, plus `eps(b_j+1) - ln(q0)/2` per row, plus terms
   `O(T2^{-2m})` from the support `m` rows below.
2. *All pe.* Wall rows satisfy `u_j <= u_{j+1}` (gap 1) and pay `ln q0 (pe - j)` each, so deep
   wall rows cost quadratically against bounded gains.
Also pending: the midpoint-concavity spot test (running).

## 2026-10-10 (evening) — final checkpointed run recorded

**Final full run** (witness `rev-e-infinity-xbot-relaxation.witness.json`, computedAt
2026-10-10T18:15:06Z, two windows from the R1–R5 checkpoint): R1, R2, R3, R4, R5, R5b **pass**;
R6 **fails by design**. R6 asserts the G1-free cut is enumerable (<= 32). With
`B_bot = 3.37604722643986568255` (integer box, 1.563x the enumerated maximum 2.1598) the G1-free
cut is **48**, against **27** via G1 (6,325,874 blocks). So the script exits 1; the red check is
this bean's open goal, not a defect. PR #7419 carries this run.

**Midpoint-concavity spot test: result NOT recorded.** It was running in the previous session's
scratch (`/tmp/claude-0/hj/`), and that container was reclaimed before its output was written
anywhere durable. Absence of a recorded result is not a result; re-run it in the Murota follow-up.
The scratch `lnat.py` (steepest ascent / min-cut check) was lost the same way, so the follow-up
re-implements it in-repo rather than porting it.

**Next:** the Murota / L♮ certificate as a new PR (owner decision 2026-10-10: new PR after
#7419), targeting R6 green at cut 25, with the tail lemma (all T) and the all-pe lemma still open.

## 2026-10-10 (night) — L♮ certificate committed as a probe

`computations/deltalambda/rev_e_infinity_xbot_lnatural_probe.py` (re-implements the lost scratch
`lnat.py`): M1–M6 pass at `pe = 0..20`, `N = 40` rows, `ELLMAX = 3000`. Integer maximum
**2.159802376118285961604** for every `pe >= 3` (pe 0/1/2: 1.0762795 / 1.7009977 / 2.0254822),
each certified by min cut; the best NON-EMPTY move at any optimum loses >= 0.000759 (pe = 2).
Cut **25** (threshold -1.97424; xrun(25) = -1.96143, xrun(26) = -2.01360), limit 32.
**Still conditional** on the tail lemma (T > 40) and the all-pe lemma (pe > 20); this bean stays open.

## 2026-10-11 — CLOSED: both lemmas proved, e_inf join certified with no G1

**Lemmas** (proofs in the `rev_e_infinity_xbot_lnatural_probe.py` docstring, "The two lemmas"):
- *Tail (all T > N):* on the bi-infinite lattice the antisymmetric ψ terms cancel, so displacing
  rows above N gains at most `eps(b_N + 1) + cbar_N`, which is below `ln q0 / 2` at every certified
  frame (M7). The padded optimum at T = N + 4 and N + 12 has no improving ±χ_S move (M7b).
- *All pe > 20:* `G_{pe+1}(0, u) = G_pe(u)` exactly (M8, 40 random points). Displacing the bottom
  row of a deep wall costs at least `ln q0 · (pe + 1)` and gains at most `eps(1) = 1.66947`, and
  `eps(1) / ln q0 = 16.0002 < 21` (M9).

Full run (`pe = 0..20`, `N = 40`): **10/10**, witness `rev-e-infinity-xbot-lnatural.witness.json`,
`open_gaps = []`. Cut **25**.

**Join without G1** (`rev_e_infinity_xbot_join_probe.py`, 4/4, witness
`rev-e-infinity-xbot-join.witness.json`). The per-sum bottom bound comes from a Lagrange multiplier:
`Xbot(s) ≤ h(μ) + μ s`, with h(μ) certified by the same min-cut method for
μ ∈ {0.4, …, 0}. With μ ≥ 0 the tail condition relaxes to `bracket < ln q0/2 + μ` and the wall
condition to `eps(1) − μ < ln q0 · (pe + 1)` (J2, J3). Over the window `s_t + s_b ≤ 25`, the
maximum of `Xblock(s_t) + xrun(s_t + s_b) + Xbot(s_b)` is **2.439296455120784027065** at
(8, 8), equal to e_inf (J4). The bottom bound equals the top block at s = 1, 3, 6, 7, 8, 11..14.

**Single external input:** Murota (2003), Ch. 7, which says the best ±χ_S move of an L♮-concave
function is a min cut (`murota2003`). Everything else is computed at mp.dps 25/30 at the proton q0.
Not Lean-formalised; that is a possible follow-up, not this bean's goal.
