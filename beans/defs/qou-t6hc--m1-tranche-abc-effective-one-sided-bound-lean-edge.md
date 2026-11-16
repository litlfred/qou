---
# qou-t6hc
title: 'M1 tranche A+B+C: effective one-sided bound, Lean edge-calculus, and the kappa_n correction exponent'
status: in-progress
pr: 8187
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:43:34Z
updated_at: 2026-11-16T20:22:00Z
parent: qou-10v9
---

Tranche under qou-k5r5 (M_1 > 0 all-n), taking all three options put to the owner.

State at claim: M_1 > 0 is reduced to ONE one-sided claim -- (a) exact M_1 > 0
for n <= 12 [DONE, in fact exact to n = 50], AND (b) kappa_n >= kappa for
n >= 13, where kappa = 128/(225 pi^2) is DERIVED (not fitted) via the
Ivanov-Olshanski field. Track A (Sniady genus) is dead: sub-result (1) split
Sigma_h = p2sharp_sym + T with Cov(p2sharp_sym, omega3) = 0, so M_1 = Cov(T,
omega3) with T the non-Lambda* part, and genus only reaches Lambda* x Lambda*.
Track D (Fulman exchangeable pair) is principal because its premises need
neither leg polynomial.

- [ ] C: fit the exact kappa_n series against candidate correction exponents
      (edge/Tracy-Widom n^{-2/3} is the corpus's stated candidate) to tell A
      what order it must prove. Track B's scoped job: "guiding A's order
      prediction". Only 11 rows (n = 68..78) are stored as a witness, so the
      series n <= ~50 has to be recomputed exactly first.
- [ ] B: formalize the Fulman edge calculus in Lean -- Fact A's per-edge
      inequality d(Sum|c|) d(omega3) = (|c_r|-|c_a|)^2 (|c_r|+|c_a|) >= 0,
      giving P >= 0 UNCONDITIONALLY (half of M_1 = P - N, with a sign); the
      three local increments; and the 1-Lipschitz lemma |D(u+1) - D(u)| <= 1
      which is what bounds the per-edge ratio by 4. All four are flagged
      "Lean-formalizable, verified exact" and none is done. The omega3
      J-eigenfunction identity needs the up-down chain and is heavier -- scoped
      OUT of the first pass.
- [ ] A: the one-sided effective bound. The real gap. Elementary routes are
      already REFUTED in the parent bean: per-edge ratio is unbounded (max 4, so
      no FKG) and weight-suppression fails because N/P < 1 is an averaging
      phenomenon, not worst-case. Attempt informed by C; report honestly if it
      walls, do not launder.

Connection worth recording: the corpus's T = Sum_box(i+j) - n IS Sigma_h under
1-based box indexing (checked: difference exactly 0 on every partition of
n <= 12; exactly 2n under 0-based). So `sum_hookZ_eq_bStat`, merged today in
QOU/BraidKnot/HookSumClosedForm.lean, is the reduction's own central identity,
now machine-checked. That was accidental.


## Outcome (2026-08-30)

**B — DONE, sorry-free.** `QOU/BraidKnot/M1EdgeCalculus.lean`, 8 theorems, all on
`[propext, Classical.choice, Quot.sound]`, wired into the umbrella (not an
orphan). Two findings from doing it:

- **Fact A is not combinatorics.** `(|c_r|-|c_a|)(c_r^2-c_a^2) =
  (|c_r|-|c_a|)^2(|c_r|+|c_a|) >= 0` holds for ANY two integers, because
  `c^2 = |c|^2`. So `P >= 0` per-edge needs no property of Young diagrams at
  all; the diagrams only supply the two increment formulas. `factA_nonneg` is
  therefore stated for arbitrary `cr ca : Z`, which is the honest strength.
  Also proved `factA_eq_zero_iff`: the product vanishes iff `|c_r| = |c_a|`,
  identifying the omega_3-neutral edges a domination argument may discard.
- **The 1-Lipschitz lemma has a three-line proof.** Diagonal indices are
  downward closed, hence an initial segment; if `D c` exceeded `D (c+1)` by two,
  the two indices in the gap would both force `rowLen i = i + c + 1`, giving a
  strictly longer row below a shorter one against `rowLen_anti`. Reuses the
  corpus's own `HookSumComplete.downward_closed_eq_range`. Cross-checked: 3561
  diagonals over all partitions of n <= 14, 0 violations, max jump exactly 1 --
  so the Lean bound is tight.

**C — DONE, and it overturns the workplan's target.**
`computations/deltalambda/m1_kappa_correction_exponent_probe.py`, 8/8, witness
committed. kappa_n recomputed in exact integer arithmetic for n = 3..58 (the
series was NOT stored -- only the 11-row window n = 68..78 was) with a
Plancherel control `sum W = n!` at every n.

- Reproduces the corpus exactly: crossing at n0 = 13, peak delta = 0.001556 at
  n = 32.
- Decay exponent alpha[68..78] = 0.4310, strictly between 1/3 and 1/2, and STILL
  RISING (alpha[58..68] = 0.3853). Not converged.
- Measured local correction exponent 5/2 - alpha = **2.069 > 2**, so the
  workplan's `M_1 >= kappa n^{5/2} - C n^2` ansatz is NOT supported in the
  accessible range.

**But the order is genuinely UNSETTLED, and I nearly shipped the overclaim.**
My first version of the probe asserted "correction exponent exceeds n^2" as a
conclusion. Testing candidate FORMS by residual drift across five disjoint
windows shows two survive with drift shrinking to zero -- `n^(2/5)` and
`n^(2/3)/log n` (the corpus's own edge/Tracy-Widom candidate, with a log) --
while `n^(1/2)/log n` and `n^(2/3)/log^(3/2)` drift away. The two survivors
STRADDLE the ansatz:

    delta ~ A n^(-2/5)        =>  correction ~ n^2.1        ansatz FAILS
    delta ~ A n^(-2/3) log n  =>  correction ~ n^(11/6) log n  ansatz HOLDS

The local exponent 2.069 sits between them because a log biases it downward.
The probe now asserts the ambiguity rather than either branch.

**A — NOT CLOSED, and one route is now closed off.** The two surviving forms
differ by `n^(4/15)/log n`, which grows 1.02x by n=120, 1.06x by n=200, 1.12x
by n=400 and only 1.73x by n=10000 -- against measured residual drifts of ~0.4%
and partition counts of p(200) = 4.0e12, p(400) = 6.7e18. **Exact enumeration
can never separate the two forms.** Track B is therefore closed as a route to
deciding the correction's ORDER, not merely deprecated: only the analysis can
decide it, and it must decide it before an effective bound can be aimed.

That is the concrete handoff to A: do not target `-C n^2` until the form is
settled, because the data does not support it and cannot be made to.


## Leg A worked (2026-08-30): the target term is identified, and it is not the one the workplan aims at

Not closed. What changed is WHICH average has to be bounded, and that the
obvious analytic input is exactly critical rather than sufficient.

`computations/deltalambda/wlambda_covariance_epic_M1_edge_ratio_decomposition.py`,
6/6, witness committed, exact Fractions, n = 4..32.

Splits the Fulman ratio at the `+1`:

    N/P = S + Q,   S := 2 E_omega[(d_a - d_r)/(r - a)]   (SLOPE term)
                   Q := 2 E_omega[1/(r - a)]             (SMALL-GAP term)

**Measured:** `sqrt(n) * Q` is FLAT at 2.04..2.08 over n = 16..32 (spread
1.96%), so `Q ~ 2.065/sqrt(n) -> 0`. The small-gap term VANISHES, and the
slope term therefore carries the entire proved limit N/P -> 0.6605, i.e.
`E_omega[slope] -> 0.33025`.

**The consequence for the effective bound.** The natural limit-shape input is
pointwise: `|Omega'| <= 1` gives `|dD/dc| <= 1/2`. That yields `S <= 1`, hence
`N/P = S + Q <= 1 + Q > 1` -- it cannot prove `N/P < 1` at ANY finite n. The
pointwise bound is exactly critical and useless alone. Strictness comes entirely
from the omega-AVERAGE: 0.33025 against 0.5, a margin of ~1.51x. So the target
is an error-controlled bound on `E_omega[|dD/dc|]`, not on `|dD/dc|`.

## Two errors of mine, both caught by the measurement

1. **Signed gap.** `r - a` is a difference of ABSOLUTE VALUES and both
   orientations of every edge are enumerated, so it takes both signs, and
   `Pterm > 0` either way (that is Fact A). Summing `Pterm/(r-a)` unoriented
   cancels to EXACTLY ZERO. My `S + Q == N/P` control passed straight through
   it -- the identity holds term-by-term whatever the orientation -- so the
   control verified ALGEBRA, not MEANING. What caught it was Q = 0 being
   implausible. Fixed by orienting each edge to r > a and re-measuring the
   diagonal lengths in the source diagram of that orientation; the sign flip is
   exact because `D_mu(cA) = D_lam(cA) + 1` and `D_mu(cB) = D_lam(cB) - 1`.

2. **`d_a > d_r` is false in general.** I argued the added content is closer to
   the main diagonal so its diagonal is longer. But `d_a = D_lam(c_A)` is
   measured BEFORE the box is added, and an addable corner's diagonal can be
   empty: `lambda = (9,)` adding at content -1 has `d_a = 0`, `d_r = 1`. That is
   why S is NEGATIVE for n < 13 and only crosses zero at n = 13. The sign of S
   at small n is a transient, not the asymptotic behaviour, and reading the
   n <= 12 table alone would invert the conclusion.

Also measured: the per-edge slope does NOT reach the discrete Lipschitz bound 1
on omega-positive edges until n = 15, and exceeds it (max 2) thereafter --
because `r - a` is a gap between ABSOLUTE contents, so opposite-sign contents
give `|c_r - c_a| > r - a`. The Lean lemma `diagLen_lipschitz` bounds the slope
across ADJACENT diagonals only; the structure probe's "d_a - d_r <= r - a" holds
for SAME-SIGN contents, a qualifier I dropped when first quoting it.

Gap qou-k5r5 stays OPEN. Nothing wired; no fit; L2 unchanged.


## Leg A, second pass (2026-08-30): a far weaker sufficient condition

Still not a proof. But the target is now something much smaller than the
effective CLT the workplan scoped.

**N/P is monotone INCREASING for n >= 9**, verified in exact Fractions over
n = 9..40 (the only decreases anywhere are 5->6 and 8->9), and every value sits
below the proved limit 0.6605 (max 0.63108 at n = 40). Monotone-increasing-with-
limit-L means sup = L, so

    M_1 > 0 for all n
      <== [N/P monotone for n >= 9]      OPEN -- observed on 9..40, not proved
        + [N/P -> 0.6605 < 1]            proved, modulo the cited IO CLT
        + [exact check n <= 9]           done

That replaces "Berry-Esseen-grade effective limit-shape estimates" with
**monotonicity of a sequence**. Different kind of problem, and a far weaker
demand. It does NOT close the gap: monotonicity is observed on a finite range.

## The increments oscillate, and the oscillation is periodic in sqrt(n)

Not smooth, which is why monotonicity is not obviously safe. Measured extrema:
peaks at n = 12, 25; troughs at n = 20, 36 -- i.e. sqrt(n) = 3.46, 5.00 and
4.47, 6.00, a period of about **1.53 in sqrt(n)**.

**This was predicted before it was measured.** From the n <= 32 data alone the
extrema already looked equally spaced in sqrt(n), which forecast a trough near
n ~ 36 and a rise after. The n = 40 run put the trough at exactly n = 36 with
increments rising monotonically to n = 40. Recorded as a check in the probe.

NEXT PREDICTION, untested: a peak near n = 43 (sqrt(n) ~ 6.53). Testing it needs
nmax >= 46. Mechanism unexplained -- I have no account of why the period is 1.53
in sqrt(n), and it should not be treated as established structure until someone
does. The natural suspects (the VKLS support |c| <= 2 sqrt(n) crossing integers,
which would give period 1/2) do NOT match 1.53.

## Why the per-edge route stays dead, with the reason sharpened

There is no uniform pointwise bound on the slope. Telescoping the Lean lemma
gives |d_a - d_r| <= |c_A - c_B|, but the denominator is r - a = |c_B| - |c_A|.
For OPPOSITE-sign contents |c_A - c_B| = a + r, so slope <= (a+r)/(r-a), which
is unbounded as a -> r. That is why the measured max per-edge slope grows (0.5
at n=12, 1 at n=15, 2 at n=28) rather than sitting at the same-sign bound of 1.

Gap qou-k5r5 stays OPEN. Nothing wired; no fit; L2 unchanged.


---

## Leg A, 2026-08-30 — monotonicity 46 → 60, and a false RESULT line in our own probe

**REFORMULATION (what made the rest affordable).** `sum over edges weighted by
cc(lam,mu)` = `sum over TRIPLES lam -> Lam -> mu` = sum over `Lam |- n+1` of
ordered pairs of removable corners. No pair dict. Three collapses follow:
`dD2 = 2(D_Lam(c_x) - D_Lam(c_y))` (the +1 and -1 cancel); `D_Lam` at a corner
in row `i` is just `min(i, Lam_i - 1) + 1`, so no diagonal dictionary is built;
and the `2/((n+1)n!)` normalisation is common to N and P, so it cancels in the
ratio and the whole accumulation is INTEGER with one divide at the end.
Measured 19.3x at n=34 and 17.9x at n=38 against the pair-dict form, values
exactly equal (a second control on the rewrite). Command in the probe docstring
under MEASURED-COST.

**FINDING 1 — monotonicity survives the trough it was most likely to fail at.**
N/P monotone increasing on **n = 9..60**, exact Fractions. The n<=46 range put
troughs at n = 20, 36, spaced 1.528 in sqrt(n), so the next was predicted at
sqrt(n) ~ 7.53, n ~ 57. There is a trough at **exactly n = 57**, its increment
is **+1.727e-4 > 0**, and increments rise again after it. Still OBSERVED, not
proved.

**FINDING 2 — "worst-case per-edge ratio <= 4" is FALSE for n >= 28, and it is
our own line.** `..._edge_ratio_structure.py` prints it as a RESULT. The
derivation printed one line above carries the hypothesis "(same-sign contents)";
the RESULT drops it, and every extremal edge is OPPOSITE-sign — exactly the
case the derivation excludes. Extremal family `Lam_m = ((2m+1)^(m+1), 1)`: two
corners, at contents `m` and `-(m+1)`, with `D_Lam = m+1` and `1`, giving ratio
`2m` at `n = 2m^2+3m+1 = 6, 15, 28, 45, ...`  Hence

    max ratio_e = 2*floor((sqrt(8n+1)-3)/4) ~ sqrt(2n)      UNBOUNDED

verified against a brute-force scan of every corner pair at every level
n = 6..50, with a control (a formula shifted by +2 must disagree: 45/45). That
probe's default nmax is 16 and 4 is correct up to n = 27, so **it never ran
where it fails** — the session's recurring signature, an absent check
indistinguishable from a passing one. Corrected in place. This STRENGTHENS the
structure probe's real conclusion: if the per-edge worst case diverges, no
per-edge argument can ever reach N/P < 1, so averaging is not merely convenient
but forced.

**CORRECTION TO MY OWN PRIOR CLAIM (cf5fefe06d).** That commit said the sqrt(n)
periodicity is "refuted as a clean model" on the strength of one 6.3%
discrepancy in the maxima. With the n = 57 trough the honest description is a
systematic upward DRIFT, visible in both series — minima gaps 1.528, 1.550;
maxima 1.536, 1.633. A constant period is still wrong, so the refutation
stands; what changes is the reason.

**HYPOTHESIS (recorded, falsifiable, NOT established).** D(0) — the central
diagonal length, i.e. the Durfee side — has `D(0)/sqrt(n) -> 2/pi` under VKLS,
so D(0) advances by 1 when sqrt(n) advances by `pi/2 = 1.5708`: precisely the
value both gap series drift toward. That would make the oscillation period one
unit of D(0). It puts the next maximum at **n ~ 67** and the next minimum at
**n ~ 83**. Two gaps per series support it; the mechanism is unexplained.

**ROUTE NOTE (untried, and the reason to prefer it).** Monotonicity is
sufficient but strong; with N/P -> 0.6605 there is 0.36 of headroom to 1, so an
effective upper bound is a far cheaper target. The per-edge worst case now
provably diverges, so any route must average — and one exact DETERMINISTIC
averaging identity is available and unused. Telescoping gives

    sum_{u>=0} (D(u) - D(u+1)) = D(0)    exactly,

so the mean drop rate of the diagonal profile on the positive side is exactly
`D(0)/lambda_1`, and the same-sign contribution to N/P is twice that. Under
VKLS `D(0)/lambda_1 -> (2/pi)/2 = 1/pi = 0.31831`, i.e. a uniform-average
`S = 2/pi = 0.63662`, against the measured omega-weighted limit 0.6605: **the
omega-weighting costs only 3.75%**. So a bound that ignores the weighting
entirely still has enormous room. What it needs is `lambda_1 > 2 D(0)` with
explicit tails — and effective Plancherel concentration for `lambda_1` is
classical, which is precisely the part "Berry-Esseen-grade effective
limit-shape estimates" was standing in for.

**STILL OPEN.** Monotonicity is observed on n = 9..60, not proved. qou-k5r5
stays OPEN.


---

## Leg A, 2026-08-30 (second) — the telescoping route: half of it works, and three of my predictions were wrong

**THE ROUTE.** Replace "prove N/P monotone" with "bound N/P", using an exact
deterministic identity instead of an asymptotic one. Telescoping gives
`Σ_{t≥0}(D(t) − D(t+1)) = D(0)` exactly — no limit shape, no error term.

**WHAT SURVIVES: a two-case per-edge bound, elementary and deterministic.**
Both sides of the diagonal telescope to the SAME total `D(0)`. Writing
`N^σ(u)` for the drop-site count in `[0,u)` on side σ, so `D(±u) = D(0) − N^σ(u)`:

- **same sign**: `d_a − d_r = N^σ(v) − N^σ(u)` = #drops in `[u,v)`, so
  `0 ≤ slope ≤ 1` and the slope IS a density;
- **opposite sign**: `d_a − d_r = N^τ(v) − N^σ(u)` — **the `D(0)` cancels** —
  a difference of two counts each in `[0, D(0)]`, so `|slope| ≤ D(0)/g`.

0 violations of either over every edge at every n ≤ 46, and case 2 is **SHARP**:
`max |slope|·g/D(0) = 1` exactly. Control: the halved bound `D(0)/2g` fires.

**Formalized, sorry-free** (6 theorems in `QOU/BraidKnot/M1EdgeCalculus.lean`,
`#print axioms` = the standard three): `diagLen_antitone`,
`diagLen_le_diagLen_zero` (the main diagonal is the longest),
`diagLen_le_add_sub` (telescoped Lipschitz), `diagLen_sub_nonneg_le` (case 1),
`diagLen_transpose_zero` (the main diagonal is transpose-invariant),
`abs_diagLen_sub_transpose_le` (case 2).

**THREE PREDICTIONS OF MINE, REFUTED BY THE MEASUREMENT.** All are recorded as
refuted in the probe rather than rewritten:

1. *"The identity says nothing about opposite-sign edges."* **False** — it
   reaches them, via the D(0) cancellation above. I drafted the probe header
   asserting this and the run disproved it.
2. *"Their ω-weight vanishes, or S_opp is negative and helps."* **False on both
   counts.** w_opp sits near **0.44** (peaks ~n=40, not shrinking); S_opp is
   negative only below n≈18, then crosses and **saturates near 0.118** — about
   36% of S at n=46. For n ≥ 19 it ADDS.
3. *"λ₁ > 2·D(0)."* **False pointwise** — ~**10%** of ω-weight sits on diagrams
   violating it, min margin **−6**. ω charges atypical diagrams and a square has
   λ₁ = D(0). The pointwise form of the π/2 headroom argument is DEAD.

**WHAT THE ROUTE STILL NEEDS.** Only the AVERAGED form survives:
`E_ω[D(0)/λ₁] < 1/2`, measured 0.382 at n=46 and falling toward the VKLS
`1/π = 0.3183` — holds uninterrupted on n = 5..46 (sole exception n=4 at 25/48,
where λ=(2,2) has λ₁=D(0)). And the inflation
`E[slope|same]/E[global density|same]` is **0.494 at n=46 against π/2 = 1.571`
— comfortably inside, but *rising* (0.39 → 0.49 over n=27..46) and its limit is
NOT determined by this range.

**HONEST BOTTOM LINE.** The per-edge bounds do not close it: at n=46 the case-2
bound `B_opp = 2E[D(0)/g ; opp]` is ~an order of magnitude above the true S_opp,
and combined with the trivial same-sign bound `2·w_same` the total exceeds 1. So
averaging is required on BOTH sides. What the route buys is that the *inputs*
are now elementary and finite (a telescoping sum, a transpose symmetry) instead
of Berry–Esseen-grade asymptotics; what it does not buy is the conclusion.

**STILL OPEN.** qou-k5r5 OPEN. Monotonicity remains observed on n = 9..60.


---

## Leg A, 2026-08-30 (third) — what the inflation factor IS, and a correction to my own report

**THE IDENTITY, and it is now Lean.** By the telescoping lemmas a same-sign slope
is the density of drop sites `δ(t) := D(t) − D(t+1) ∈ {0,1}` in the edge's
content interval. Give each edge weight `w_e` and let it spread that weight
uniformly over the sites it covers, `κ(t) := Σ_{e ∋ t} w_e/g_e`. Then

    Σ_t κ(t) = Σ_e w_e          -- each edge spreads exactly its own weight
    E_ω[density] = Σ_t κ(t) δ(t) / Σ_e w_e

So **κ, normalised, is a probability distribution on SITES**, and the ω-average
interval density is exactly *the κ-mass sitting on drop sites*. There are `D(0)`
drop sites among `λ₁` (telescoping), so uniform κ gives exactly `D(0)/λ₁`, i.e.
**infl = 1**. The inflation factor is therefore not a fitted constant and not
mysterious: it is precisely κ's departure from uniform, and `infl > 1` iff ω
over-weights drop sites.

**Formalized sorry-free** in `QOU/BraidKnot/M1EdgeCalculus.lean` (now 21
theorems, up from 8 at the start of this arc; all `#print axioms` = the standard
three): `kappa` (def), `kappa_sum`, `sum_drop_eq`,
`weighted_density_eq_kappa_dot`, `kappa_uniform_dot`, `diagLen_rowLen_zero`,
`sum_drop_diagLen`. The last is the capstone for actual diagrams: the profile
falls from `D(0)` to `0` across `[0, λ₁)`, so the global drop density is exactly
`D(0)/λ₁` — an identity, not an estimate. Both κ identities verified exactly as
Fractions at every n measured.

**CORRECTION TO MY OWN REPORT.** Last turn I wrote that `infl = 0.494` against
`π/2 = 1.5708` was "comfortably inside" and treated it as headroom. **It is not
headroom.** `E_ω[D(0)/λ₁] → 1/π`, so asymptotically

    infl < π/2   ⟺   E_ω[density] < 1/2

and `1/2` is exactly the pointwise limit-shape bound that
`..._edge_ratio_decomposition.py` had *already* shown to be **critical**. So the
FALSIFIER-2 check was restating the constraint, not testing a margin on top of
it. The check text and the probe are corrected in place.

**WHAT ACTUALLY BEARS ON THE ROUTE.** `1/2` is the pointwise maximum of the VKLS
local drop density `ρ(u) = (1 − (2/π)arcsin(u/2))/2`, attained **only at u = 0**.
So `infl → π/2` requires κ to concentrate **at the origin**. Measured over
n = 12..48, κ's mean site position moves *outward* — 0.701, 0.726, 0.790, 0.809,
0.805, 0.819, 0.844, 0.856 — and then **plateaus**: 0.8563 (n=40), 0.85476 (44),
0.85348 (48), i.e. it settles near **0.853** rather than continuing to rise. The
VKLS local density there gives a ceiling of **0.3545**, also settled (0.35418,
0.35440, 0.35451), not 0.5. Taken at face value that puts `infl → π·0.3545 ≈
1.11`, well under π/2 = 1.5708.

**That is evidence, not proof**, and the weak point is explicit: the ratio of the
actual `E[density]` to that VKLS-predicted ceiling is only 0.538 at n = 48 and
still climbing (0.484, 0.517, 0.538), so while the *ceiling* now looks settled,
n ≤ 48 does not pin where `E[density]` lands under it. What the measurement does
rule out is the failure mode I flagged last turn — κ is demonstrably not heading
for the origin, so the `infl → π/2` scenario is not what is happening.

**STILL OPEN.** qou-k5r5 OPEN. No bound on infl is proved and none can be from
`diagLen` alone: κ is a property of the Plancherel up-down edge measure, not of
Young diagrams.


---

## Leg A, 2026-08-30 (fourth) — infl settled at n = 800 by exact Plancherel sampling, after I got it wrong twice

**THE UNLOCK.** The triple measure factorises: summing
`P(λ,Λ,μ) = dim(λ)dim(μ)/((n+1)n!)` over λ and using the branching rule gives
`P(Λ) = dim(Λ)²/(n+1)! = Plancherel(n+1)`. So

> **Λ ~ Plancherel(n+1) by RSK, then TWO INDEPENDENT GNW hook walks**,

and because the corner-pair probability is ∝ `dim(λ_x)dim(λ_y)`, the ω
importance weight is exactly `(r−a)²(r+a)` — **no dimension is ever computed**.
Uniform integer randomness only, `O(n√n)` per sample against enumerating
`p(n+1)` partitions. Exact enumeration dies near n = 60; this reaches **n = 800**.

**CONTROL:** reproduces the committed exact values at n = 24/40/48 to **0.52%**
worst case, with seed spreads reported. Without that the large-n numbers would
be unfalsifiable.

**MEASURED** (30k samples × 3 seeds):

| n | 100 | 200 | 400 | 800 |
|---|---|---|---|---|
| infl | 0.62299 | 0.70950 | 0.78647 | 0.84485 |
| E[D(0)/λ₁] | 0.36968 | 0.36241 | 0.35416 | 0.34706 |

infl rising, decelerating (increments per doubling 0.0865, 0.077, 0.0584);
`E[D(0)/λ₁]` falling toward the VKLS `1/π = 0.31831`.

**EXTRAPOLATED: infl → 1.028**, at **5.11σ**, with three independent seed refits
at **1.025, 1.012, 1.050**. Against `π/2 = 1.5708`. `infl = 1` is exactly the
uniform-κ case of `M1EdgeCalculus.kappa_uniform_dot` — the ω-chosen intervals
drop at the diagram's own global rate, no faster. That is the benign outcome.

**TWO ERRORS OF MINE, both in the extrapolation and both now gated.**

1. **I reported `infl → 1.01` from a fit that was 1.17σ from meaningless.** The
   estimator `I = (ac−b²)/(a−2b+c)` has a *second difference* in its denominator;
   on the narrow grid (100, 200, 400) those points are nearly collinear, so the
   denominator was `−0.0095` against a seed-propagated noise of `0.0082`. Two
   runs whose infl agreed to **under 1%** gave **1.00** and **1.41**; perturbing
   one point by a single noise unit moved the answer from 1.20 to 1.83. The 1.01
   was right by accident.
2. **My noise formula dropped a factor.** `var(a−2b+c) = σa² + 4σb² + σc²`; the
   middle coefficient was unweighted, understating the noise.

**What fixed it was LEVERAGE, not samples.** Adding n = 800 and fitting the top
three points took the denominator from 1.17σ to 5.11σ. More samples at a narrow
grid would not have: the second difference grows with grid width, the noise does
not.

**The check now applies the rule in both directions** — significance-test the
denominator first, then report only the conclusion that test supports. On the
narrow grid the same rule returns "undetermined" and refuses to quote a number.
A third check requires the three independent seed refits to agree, which is the
real guard; the point estimate alone was what misled.

**STILL OPEN.** qou-k5r5 OPEN. This is an extrapolation from three points on a
fitted form, not a limit. And it settles only the SAME-sign half: `S_opp` carried
~44% of ω-weight and was saturating near 0.118 at n = 46, and nothing here
touches it. That is now the only place the route can fail.


---

## Leg A, 2026-08-30 (fifth) — S_opp at n = 800, and the budget lands exactly on the boundary

**S_opp measured at large n** by the same exact Plancherel edge sampler
(`Λ ~ Plancherel(n+1)` by RSK, two independent GNW hook walks, ω weight exactly
`(r−a)²(r+a)`). Sample count scaled ~1/n so the control tiers get real precision.

| n | 24 | 40 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|---|
| S_opp | 0.04847 | 0.11641 | 0.18659 | 0.23233 | 0.26107 | **0.28115** |
| B_opp | 0.6369 | 0.6463 | 0.6351 | 0.6535 | 0.6580 | **0.6645** |
| slack | 13.1 | 5.55 | 3.40 | 2.81 | 2.52 | **2.36** |
| w_opp | 0.457 | 0.460 | 0.457 | 0.474 | 0.481 | 0.486 |

**CONTROL:** reproduces the exact S_opp at n = 24 and 40 to **−0.23%** and
**−0.62%**, and B_opp to within a few parts in a thousand.

**A prediction of mine, confirmed.** I wrote before the run that the budget
`S → 0.6605` with `S_same → 0.327` forces `S_opp → ≈0.33`, nearly triple its
n = 46 value of 0.118. Measured: 0.281 at n = 800 and still rising. A flat S_opp
would have meant the accounting was wrong; it is not.

**FALSIFIER did not fire.** The Lean bound's slack `B_opp/S_opp` **shrinks**
(13.1 → 2.36), so `|slope| ≤ D(0)/g` stays a bounded factor above the truth
rather than degrading. B_opp itself is roughly flat, drifting up slowly.

### The budget, and the honest verdict

Two questions that must not be conflated:

**(1) Does the accounting close?** `S_same → 2·w_same·infl/π = 0.3363` (from the
inflation extrapolation) plus the separately measured `S_opp = 0.2811` gives
**0.6175** against the independently proved **0.6605** — short by 6.5%, exactly
as expected since S_opp is still rising. Three different routes agreeing is real
evidence the decomposition is right and nothing is dropped or double-counted.

**(2) Do the BOUNDS close it?** No — and not "no" either. Granting `S_same` its
measured value **for free** (not a bound, and generous), plus the only
deterministic opposite-sign bound `B_opp`:

    S_same + B_opp = 1.00076,  range [0.99135, 1.01189]

once infl's three seed refits (1.012, 1.025, 1.050) and B_opp's seed spread are
carried through. **That range straddles 1.** The honest verdict is neither
"closes" nor "misses": the bounds land exactly on the boundary and the precision
in hand cannot separate them.

**The tie-breaker is against us.** B_opp is still *rising* with n. Landing on the
boundary with the leading term still growing is not a near miss a better constant
fixes — extrapolating the rise puts the total above 1.

**An error of mine, caught and gated.** The first version of this check reported
"over 1 by 0.00076" and asked for B_opp to fall by "0.114%" — three significant
figures on a gap eight times smaller than infl's own uncertainty. It now
propagates the seed spreads and refuses to call it either way when they overlap 1.

**A third serialisation defect.** The witness serialisers in this cluster route
everything non-int through `nstr`, which turned `infl_per_seed` into the single
string `"[...]"` and (earlier) `n` into `"12"`. Both silently broke a downstream
consumer. Fixed at source in both probes; the budget probe also reads either form
so old witnesses still work.

**STILL OPEN.** qou-k5r5 OPEN. The same-sign half has an averaging argument (the
telescoping density reading, `infl → 1.028`). The opposite-sign half has none —
and that reading provably does not apply to it. **That is the whole remaining
gap**, and it is now stated in one line rather than spread across five probes.


---

## Leg A, 2026-08-30 (sixth) — the route reduces to ONE constant

`B_opp = 2·w_opp·Ê` with `Ê := E_ω[D(0)/g | opp]` dimensionless. Splitting the
product is what turns "the bound is rising, undecided" into a statement about
*which factor* is responsible:

| n | 100 | 200 | 400 | 800 |
|---|---|---|---|---|
| `Ê` | 0.6953 | 0.6901 | 0.6845 | **0.6833** — monotonically FALLING |
| `w_opp` | 0.4567 | 0.4735 | 0.4806 | **0.4862** — monotonically RISING |

**The deterministic bound is not degrading because the per-edge estimate is
getting worse — it is improving.** It drifts because opposite-sign edges keep
taking a larger share of the ω-weight. Both monotonicities are solid.

**Neither LIMIT is.** `Ê`'s second difference is 0.00426 against a
seed-propagated noise of 0.013 — **0.33σ**, far under the 3σ bar. The same
3-point fit that is quotable for `infl` (5.11σ) is not quotable here, and the
probe says so rather than quoting the 0.6829 it would produce.

**THE REDUCTION.** Closure needs `2·w_opp·Ê < 1 − S_same = 0.6637`, i.e. with
`Ê` at its current 0.6833:

> **the limiting `w_opp` must be below ≈0.4857.**

Measured: **0.48624 at n = 800, and rising.** So the whole deterministic-bound
route now turns on a *single limiting constant* — the share of ω-weight carried
by opposite-sign content pairs. That is a far sharper target than "effective
limit-shape estimates", and unlike everything else here it may be computable in
**closed form** from the limiting edge measure (`ω ∝ (v−u)²(v+u)` over the
limiting corner-pair distribution) rather than measured.

**Threshold crossing, with error bars:** B_opp sits **1.8σ UNDER** the threshold
at n = 400 and **0.2σ OVER** at n = 800 — it has *reached* the line, not clearly
passed it.

**STILL OPEN.** qou-k5r5 OPEN. Current reading: the route is trending to fail,
by a margin that is inside the error bar, and the deciding quantity is now named.


---

## Leg A, 2026-08-30 (seventh) — the budget in CLOSED FORM: the crude bound misses by 0.57%, elementary refinements reach the line

Everything before this was measured. This is **computed** — two quadratures over
the limiting edge measure, no sampling.

**THE LIMITING PICTURE.** The sampler established the factorisation
(`Λ ~ Plancherel(n+1)`, two independent down-steps). In the limit the
co-transition measure → **semicircle** on [−2,2] (Kerov), so the two corner
contents are i.i.d. semicircle; the ω weight is `(r−a)²(r+a)`; and
`D(c√n)/√n → φ(c) = (Ω(c) − |c|)/2` from VKLS.

**`w_opp → 1/2` EXACTLY, and the argument is one line.** The ω weight depends on
the two contents *only through their absolute values*. The semicircle is
symmetric, so each sign is independent of its magnitude, hence the sign pattern
is independent of the weight — and the opposite-sign share is exactly
`P(opposite signs) = 1/2`. No integral. (Measured 0.4567 → 0.4862 at n = 100..800,
rising to it from below.) The same symmetry makes the limiting slope identical for
both sign classes, so `S_same = S_opp = S/2`.

**This kills last turn's target.** Closure needed the limiting `w_opp < 0.4857`;
it is 1/2. So the reduction moves to the other factor.

**THE CONTROL, and it is what makes the rest trustworthy.** The framework predicts
`S → 2·E[(r²−a²)(φ(a)−φ(r))]/E[(r−a)²(r+a)]`, a constant the corpus already knows
by a *completely different route* (the Ivanov–Olshanski Kerov CLT field):
`N/P → 0.6605`. Quadrature gives **0.66046945 — agreement to 0.005%**. That checks
the semicircle co-transition limit, the corners' independence, the ω weight and φ,
all at once.

**THE VERDICT.**

| bound on the opposite-sign half | B_opp → | total | |
|---|---|---|---|
| crude, `\|d_a − d_r\| ≤ D(0)` — *the one proved in Lean* | 0.675475 | **1.005709** | fails by 0.571% |
| refined (below) | 0.669299 | **0.999534** | reaches the line, by 0.047% |

The refinements are two facts already in hand:
`N^τ(r) ≤ min(r, D(0))` (at most one drop per site, `D(0)` in total) and
`N^σ(a) ≥ max(0, a − (λ₁ − D(0)))` (at most `λ₁ − D(0)` non-drops in total). The
first is `D(c) ≥ D(0) − c`, i.e. **`diagLen_le_add_sub`, already proved
sorry-free**; the second is the same telescoping identity read from the other end.
**Neither needs new mathematics.**

**0.047% IS NOT A PROOF.** Three reasons, recorded so nobody re-derives them:
1. it is **asymptotic**. M₁ > 0 needs every n; exact verification reaches n = 60,
   this reaches the limit, and the crossover is untouched;
2. the margin leaves no room for finite-n corrections — and the measured
   quantities approach these limits from *both* directions (`B_opp` from below,
   `Ê` from above), so the finite-n budget is **worse** before it is better;
3. the semicircle co-transition limit is used, not proved here.

**For scale:** the crude bound is **2.045×** the truth, the refined **2.027×**,
and the budget tolerates **2.028×**. That is why tenths of a percent decide it.

**STILL OPEN.** qou-k5r5 OPEN. But the gap is now a specific, small, *elementary*
quantity rather than "effective limit-shape estimates" — and the two refinements
that reach the line are Lean-reachable from lemmas already proved.


---

## Leg A, 2026-08-30 (eighth) — the two refinements are now Lean theorems

Both unwind to one-line statements about `diagLen`, and only one was new:

* **Refinement 1**, `N^τ(r) ≤ min(r, D(0))`, is `D(0) ≤ D(r) + r` — *exactly*
  `diagLen_le_add_sub` at `u = 0`, already proved. Nothing new needed.
* **Refinement 2**, `N^σ(a) ≥ max(0, a − (λ₁ − D(0)))`, unwinds to
  **`D(c) + c ≤ λ₁`** — the last box on diagonal `c` sits at row `D(c)−1`, column
  `D(c)−1+c`, which is inside row 0. That is the one new lemma.

**A guard that is real, not decorative.** `D(c) + c ≤ λ₁` is **false** when
`D(c) = 0` and `c > λ₁`; the ℤ form would assert `0 ≤` a negative. So it is stated
over ℕ unconditionally (truncated subtraction makes it true) and over ℤ only under
`0 < D c`, which every actual corner satisfies.

**New, sorry-free** (`M1EdgeCalculus.lean`, now 24 theorems, up from 8 at the
start of this arc; all three standard axioms): `diagLen_le_rowLen_zero_sub`,
`diagLen_add_le_rowLen_zero`, `diagLen_sub_transpose_le_refined`. The last is the
combined bound, and it fell to `omega` from four already-proved facts.

**A bug in my own verification, caught before it propagated.** My first check
reported **2417 violations** of the refined bound. The theorem was fine; the check
was wrong. When `dABS < 0` the probes' `num` is `−(d_a − d_r)`, not `d_a − d_r` —
only the ratio `num/dABS` is the slope. Re-checking against `d_a − d_r` computed
straight from λ's profile gives **0 violations** over 27,794 opposite-sign edges,
and the slope identity `num/dABS·(r−a) = d_a − d_r` holds on every one of them.

**And my control had failed to fire.** `refined − 1` was also never violated, so
it demonstrated nothing. Measuring the slack: minimum **1**, attained on 6,778
edges, against the crude bound's minimum of **2**; tightening by 2 fires on 6,778.
So the refined bound is essentially attained — the residual O(1) slack is
`o(√n)` and invisible to the rescaled integrals. Both controls are now in the
probe.

The refined bound is **strictly tighter than crude on 41%** of opposite-sign
edges, which is precisely where the gain in the quadrature comes from.

**Also verified:** the algebraic rearrangement linking the Lean statement to the
quadrature, `min(r,D0) − max(0, a−(λ₁−D0)) = min(D0, λ₁−a) − max(0, D0−r)`, on
200,000 random rationals with a control (0 mismatches; shifted variant fires
2000/2000).

**STILL OPEN.** qou-k5r5 OPEN. The asymptotic margin is 0.047% and the finite-n
crossover (n ≥ 61) is untouched — that is now the *only* thing between this and
M₁ > 0.


---

## Leg A, 2026-08-30 (ninth) — can Lean close the finite-n crossover? No, and here is exactly why

**1. Mathlib has none of the analytic input.** Its entire Young theory is **two
files** — `Combinatorics.Young.YoungDiagram` and `.SemistandardTableau`. Checked:
no RSK/Schensted, no Plancherel measure, no semicircle law, no free probability,
no VKLS limit shape. Every analytic ingredient this route uses would have to be
built first.

**2. The margin shrinks exactly where the error terms grow.** Measured:

| n | 100 | 200 | 400 | 800 | limit |
|---|---|---|---|---|---|
| total | 0.8799 | 0.9181 | 0.9413 | 0.9597 | 0.99953 |
| margin | 12% | 8.2% | 5.9% | 4.0% | **0.047%** |

The budget *rises* toward its limit, so the route is **tightest in the limit** —
the opposite of the usual situation. An effective limit-shape estimate would have
to be accurate to better than `5·10⁻⁴` relative, in the asymptotic regime, which
is where such estimates are weakest.

**3. The finite range is not kernel-checkable.** Exact verification reaches
n = 60; the next level has `p(61) = 1,121,505` partitions with ~40-digit
dimensions.

### What IS possible, and is now done

`sum_lt_of_weighted_bound` and `sum_lt_of_split_bound` (sorry-free, standard
axioms) formalise the **reduction**: per-edge bounds plus **one** aggregate
inequality give `N < P`, hence `M₁ > 0`. The split version has exactly the route's
shape — same-sign edges bounded by the density reading, opposite-sign by the
refined telescoping bound.

Every per-edge bound it consumes is already proved in this file
(`diagLen_sub_nonneg_le`, `diagLen_sub_transpose_le_refined`). What is **not**
proved is precisely the hypothesis `hagg`: that the bounds' own weighted average
stays below the total weight. **That is the whole remaining gap, now one named
Lean hypothesis instead of prose spread across a dozen probes.**

`M1EdgeCalculus.lean`: **26 theorems**, up from 8 at the start of this arc.

**STILL OPEN.** qou-k5r5 OPEN, and on this route it stays open until Mathlib
grows an effective limit-shape theory — or until someone finds a bound with more
than 0.047% of room.


---

## Leg A, 2026-08-30 (tenth) — the area constraint: 160× more room

**The lever was sitting unused.** Every bound so far used only `D(0)`, `λ₁` and
1-Lipschitz. The global constraint **`Σ_c D(c) = n`** was never touched, and it is
worth more than both previous refinements combined:

    monotonicity:  a·D(a) ≤ Σ_{c<a} D(c)
    1-Lipschitz:   D(a)(D(a)+1)/2 ≤ Σ_{c≥a} D(c)     (the tail triangle)
    together:      a·D(a) + D(a)²/2 ≤ A_σ
              ⟹    D(a) ≤ √(a² + 2A) − a

| bound | B_opp → | total | margin |
|---|---|---|---|
| crude `D(0)` | 0.675475 | 1.005709 | **fails** 0.57% |
| refined `min(D0, λ₁−a)` | 0.669299 | 0.999534 | 0.047% |
| **+ area** `√(a²+2A) − a` | **0.594394** | **0.924629** | **7.54%** |

**Why it works:** the near-side bound `min(D0, λ₁−a)` is nearly *vacuous* away
from the origin — it permits `D(1) = 0.637` where the truth is `φ(1) = 0.218`.
The area constraint is what closes that gap.

**HONEST CAVEAT, and it is not small.** With only the fully deterministic
`A_σ ≤ n` the margin is **0.094%** — still knife-edge. The jump to 7.54% needs
`A_σ → n/2`, i.e. the boxes splitting evenly between the two sides. That is the
conjugation symmetry of the limit shape: the same *class* of input as
`D(0)/√n → 2/π`, arguably more robust, but an input all the same.

**A control failure of mine, worth recording.** My first check of the area
inequality reported **5870 violations of a true statement**. The bookkeeping was
wrong: the `c = 0` diagonal belongs to the **positive** side's sum, so the
negative side's total is `A_- + D(0)`, not `A_-`. Corrected: **0 violations**
across 31,766 positive-side and 27,259 negative-side diagonals. Both the
inequality and the c=0 subtlety are now checks in the probe.

**LITERATURE.** Not needed for this step — area, monotonicity and 1-Lipschitz are
elementary and Lean-reachable from lemmas already proved. Literature *is* needed
for the finite-n crossover, specifically effective versions of `λ₁/√n → 2`,
`D(0)/√n → 2/π` and `A_σ/n → 1/2`. **What changes is that with 7.5% of room
instead of 0.047%, ordinary effective limit-shape bounds become plausibly usable
— they were hopeless before.**

**STILL OPEN.** qou-k5r5 OPEN.


---

## Leg A, 2026-08-31 (eleventh) — the area bound is Lean, and connected to n

**`D(a) ≤ √(a²+2A) − a` is the *solved* form of a quadratic.** The underlying
fact is division-free and far better suited to Lean, so that is what is stated:

    2·(a · D a) + D a · (D a + 1)  ≤  2 · ∑_{c < a + D a} D c        [diagLen_area_bound]
    ∑_{c < T} D c  ≤  μ.card                                          [sum_diagLen_le_card]
    2·(a · D a) + D a · (D a + 1)  ≤  2 · μ.card                      [diagLen_area_bound_card]

Two pieces, each one step from something already proved: `mul_diagLen_le_sum` is
monotonicity (`D` antitone), `triangle_le_sum_Ico` is the 1-Lipschitz tail
(`D(a+k) ≥ D a − k` is `diagLen_le_add_sub`). The ranges are disjoint and abut,
so `sum_Ico_consecutive` glues them. `sum_diagLen_le_card` injects the sigma-type
`(c,i) ↦ (i, i+c)` into `μ.cells`; the diagonals are disjoint because
`(i,i+c₁) = (j,j+c₂)` forces `c₁ = c₂`.

**What this is and is NOT.** In the rescaled variables this is the **A = 1** line
— fully deterministic, no limit-shape input — which alone takes the budget from
failing (1.0057) to a **0.094%** margin. The **7.54%** figure uses `A_σ → n/2`,
which is a limit-shape input, *not* this theorem. Both are in the docstring;
conflating them would overstate what is formalized.

**Three `omega` obstacles, all about linearity, worth recording:**
1. The obvious induction for Gauss **fails** — omega sees
   `∑ i ∈ range m, (m − i)` and its eta-reduced form as *different atoms*, so the
   inductive hypothesis never connects. Reflecting `d−i → i+1` plus
   `sum_range_id_mul_two` works instead.
2. Even then, `d(d+1)` and `d(d−1)` are unrelated atoms; omega needs the explicit
   bridge `d(d+1) = d(d−1) + 2d`, with the `d = 0` truncated-subtraction case.
3. `2 * a * D a` parses as `(2*a) * D`, a *different* atom from the `a * D` in the
   hypothesis. Parenthesising as `2 * (a * D a)` fixes it. **Nonlinear terms only
   work as literal atoms.**

**Two API frictions:** `Finset.card_le_card_of_injOn` states hypotheses over the
**Set** coercion, so memberships need `Finset.mem_coe` before `mem_sigma`; and
`mem_diagIdx` takes `μ` explicitly (section variable), so `mem_diagIdx.mp` does
not resolve — rewrite with it.

**Verified:** 40,780 instances over all partitions n ≤ 22 and a ∈ [0, λ₁+1],
**0 violations, min slack 0** — the bound is exactly attained, not slack. Controls
fire in both forms (partial-sum −2, and 2n−2).

`M1EdgeCalculus.lean`: **31 theorems**, sorry-free, up from 8 at the start of this
arc.

**STILL OPEN.** qou-k5r5 OPEN. Next is the literature step: effective versions of
`λ₁/√n → 2`, `D(0)/√n → 2/π`, `A_σ/n → 1/2`, now needing only ~7% accuracy.


---

## Leg A, 2026-08-31 (twelfth) — `A_σ → n/2` is a SYMMETRY, not a limit-shape fact

The 7.54% margin rests entirely on `A_σ → n/2` (with only `A_σ ≤ n` it is
0.094%), so it matters a great deal *which kind* of input that is.

**FINDING 1 — under Plancherel it is exact, at every n.** Plancherel is
conjugation-invariant (`dim λ = dim λᵀ`) and conjugation maps `c ↦ −c`, so with
`A₊ = #{content > 0}`, `A₋ = #{content < 0}`, `A₀ = D(0)`:

> **`E[A₊] = E[A₋] = (n − E[D(0)])/2` EXACTLY**, verified as exact rationals for
> n = 2..13.

Since `E[D(0)] ~ (2/π)√n`, that is `n/2` with a *relative* correction of order
`n^{−1/2}` — **a symmetry, not an asymptotic statement**.

**The c = 0 bookkeeping is the whole difficulty, and it beat me first.** Counting
`A₊ = #{content ≥ 0}` puts the main diagonal on the positive side and breaks the
symmetry: `E[A₊] = (n + E[D0])/2` then, off by the same amount the other way. My
first run reported "DIFFERS" at every n for exactly this reason. **The c = 0
diagonal has now caused three separate errors in this cluster** — the negative
side's area sum, this, and the earlier `A_- + D(0)` control.

**FINDING 2 — it does NOT transfer to the ω-measure.** `A_σ` is the area on the
side where the *near* corner sits, and which corner is near is selected by the
edge geometry, which correlates with the shape. Measured
`E_ω[A_σ]/(n/2)`, exact for n = 6..18: **0.303 → 0.712**. Far from 1. That was
the stated risk and it is what happened.

**But it converges to 1 FROM BELOW** — sampled 0.731, 0.859, 0.912, 0.942, 0.963
at n = 20/50/100/200/400, at roughly the `n^{−1/2}` rate the `O(√n)` diagonal
correction predicts. *From below is the favourable direction*: a smaller `A`
gives a **tighter** bound `√(a²+2A) − a`, so the 7.54% computed at `A = n/2` is
conservative at finite n.

**Not a proof.** Rigour needs either concentration of `A_σ` about its mean, or
Jensen against the **conditional** mean given the edge geometry (the bound is
concave in `A`, so Jensen points the right way). Neither is done.

**WHAT THIS CHANGES.** The remaining analytic input is no longer "effective
VKLS". It is **concentration of one smooth functional of a Plancherel diagram
around a mean fixed by an exact symmetry** — a far narrower literature question,
and the one to actually ask.

**STILL OPEN.** qou-k5r5 OPEN.


---

## Leg A, 2026-08-31 (thirteenth) — the Jensen route: viable, narrower, and not free

**The reduction.** `A ↦ min(D0, L−a, √(a²+2A) − a)` is a min of concave
functions, hence **concave in A**. So `E[bound(A_σ)|a,r] ≤ bound(E[A_σ|a,r])`,
and `E_ω[A_σ | a,r] ≤ n/2` would give the 7.54% margin with **no concentration
input at all** — one conditional-mean inequality in place of concentration of a
functional.

**MEASURED: the inequality holds everywhere.** Exact, grouping opposite-sign
edges by the integer pair `(a,r)`: **0 groups over n/2** for n = 8..18. Sampled,
binned in rescaled coordinates: **0 bins over** at n = 50/100/200.

**But it is asymptotically tight.** Max ratio 0.935, 0.945, 0.958, 0.972 at
n = 50/100/200/400 — rising toward 1 from below at about `n^{−0.4}`. Viable and
uncomfortable at once.

**TWO THINGS I GOT WRONG, both recorded rather than quietly fixed.**

1. **I predicted failure at large `a`** — a near corner far out ought to mean that
   side is long and holds more than half the area. It does not fail there. The
   maximum sits at **small** `(a,r)` — (2,3), (3,4), (4,5) — near the diagonal, in
   groups carrying under 0.4% of the weight.
2. **The natural pointwise explanation is FALSE.** If the far corner sits further
   out one expects the far side to hold more area, giving `A_near ≤ A_far` and
   hence `A_near ≤ (n−D0)/2 < n/2` deterministically — no Jensen, no probability.
   Measured: **2760 violations of 11656 (24%)**. Minimal counterexample
   `λ = (4,2,1)` with corners at `c = 1, −2`: near is `c = 1`, and
   `A_near = 3 > A_far = 2` because the diagram is **wide**. So the
   conditional-mean inequality is a genuine **averaging** statement with no
   elementary pointwise route behind it.

**WHERE THIS LEAVES THE ROUTE.** Jensen does narrow the remaining analytic input
— from *concentration of `A_σ`* to *one conditional-mean inequality*. Strictly
weaker, and precisely stated. Not free: it holds on everything measured,
approaches equality, and has no pointwise proof.

**STILL OPEN.** qou-k5r5 OPEN.


---

### 2026-08-31 (session cont.) — the `A_sigma` leg is settled as a ROUTE question

**Lean.** 8 new sorry-free theorems in `QOU.BraidKnot.M1EdgeCalculus`, all on
`[propext, Classical.choice, Quot.sound]`. The diagonal decomposition turns
`sum_diagLen_le_card` from an inequality into an **equality**:
`card_eq_sum_diagLen_add`, and the symmetric `sum_diagLen_add_transpose`
(`sum D + sum D^T = n + D0`, double-counting the main diagonal). On that:
`areaUpper` / `areaLower`, the exact split `A+ + A- + D0 = n`, the conjugation
swap `areaUpper_transpose`, and `two_mul_areaUpper_le_card_iff` — `2A+ <= n` iff
`A+ - A- <= D0`. Stated as an **iff on purpose**: `2A+ <= n` is FALSE pointwise
(the one-row diagram has `A+ = n-1`), so `A_sigma <= n/2` can only ever hold in
expectation, and the iff says what the average must control — the *imbalance*
between halves, against the Durfee side.

**Probe** `wlambda_covariance_epic_M1_area_fluctuation_scale.py`, 7/7,
float64-guard clean.

- **The margin is exactly one sigma.** `n/2 - E[A+] = E[D0]/2` and `sd(A+)` are
  BOTH `(1/pi) sqrt(n)`; `gap/sd` measured 1.002, 1.001, 1.005, 0.992, 1.002,
  1.038 over `n = 100..3200` (32x range), flat within noise.
- **Derived, not just measured.** Kerov's CLT (Ivanov–Olshanski, eq. 3.20–3.21
  of `library/arxiv-1909.06797v5`) gives `sd(A+ - A-) -> (2/pi) sqrt(n)` via
  `sum_{m even} m/(m^2-1)^2 = 1/4`, controlled by quadrature on `c_m`.
- **Consequence: concentration can NEVER close this.** It would have to cover
  one standard deviation, and a 1-sigma event has probability ~0.16. Sharpening
  the inequality does not help — the obstruction is the width of the
  distribution.
- **Pemantle–Peres Thm 3.5 is short by a growing `n^(1/4)`** (shortfall
  90 -> 2836 over `n = 1e2..1e8`), because `A+` is a linear statistic with
  UNBOUNDED coefficients. Not a weakness of the theorem: `D(c)` itself is a
  particle count, hence Lipschitz-1, so the same theorem DOES concentrate the
  per-diagonal profile the telescoping route uses, at scale `n^(1/4)`.

**Retired:** "`A_sigma -> n/2` is a literature question" (the closing line of
`..._M1_area_symmetry.py`). It is not.

**What survives:** `E_omega[A_sigma]/(n/2)` converges to 1 **from below**, and a
smaller `A` gives a TIGHTER `sqrt(a^2+2A)-a`, so the 7.54 % margin is
conservative at every finite `n`. Making that rigorous needs a **one-sided
finite-n inequality**, not concentration.

**Library:** 27 PDFs ingested across two batches (strong-Rayleigh toolchain +
Plancherel growth). Pushed `03fdcab23b`.


---

### 2026-08-31 (cont.) — `E_ω[A_σ] ≤ n/2`: pointwise REFUTED, expectation holds but margin shrinks

**Pointwise `2A_σ ≤ n` is FALSE on the ω-support.** 130/1640 violations over
n = 4..16, one named family: `Λ = (K, 3, 1)`, corners at contents `+1` and `−2`,
so the near corner is `+1` but the diagram is a long row and `A₊ = K−1`. Worst
slack `−8` at n = 16, degrading linearly. CONTROL fired (918 violations for
`A_far`), so the enumeration was live. My brief's hypothesis — that the
`D₀` slack rescues it — is refuted; `A_near ≤ A_far + D₀` survives the *old*
counterexample λ=(4,2,1) but not this family.

**In ω-expectation it holds everywhere measured, but the margin is shrinking.**
Splitting `E_ω[A_σ]/(n/2) = 1 + P − M`:

| n | ratio | P (violating excess) | M (deficit) | P/M |
|---|---|---|---|---|
| 20 | 0.734 | 0.00077 | 0.2664 | 0.003 |
| 100 | 0.912 | 0.00224 | 0.0902 | 0.025 |
| 400 | 0.962 | 0.00176 | 0.0400 | 0.044 |
| 800 | 0.975 | 0.00151 | 0.0269 | 0.056 |

`M ~ n^{−0.57}` (→ n^{−1/2}); `P` peaks at n = 100 then decays only ~n^{−0.22}.
So **P/M is still growing (~n^{0.35})** and a naive extrapolation crosses 1
around n ~ 10⁶. 18× margin at n = 800. NOT asymptotically safe on this evidence.

**But it is not load-bearing.** The Lean-proved `A_σ ≤ n` already gives a
positive margin (0.094%); `A_σ → n/2` only widens it to 7.54%. So this leg is
margin-widening, not a blocker — and the blocker is κ.

### The κ result (the downstream payoff)

`M₁ = Cov(Σ_□h, Σ_□h²)` **exactly**, via the classical `Σh² = Σc² + n²`
(914 partitions, control fires). `sd(Σc²) ~ n^{3/2}` but `sd(Σh) ~ n¹`, and the
new Lean theorem `two_mul_sum_hookLen` says why: `2Σh = Σλᵢ² + Σλ'ⱼ²`, a
conjugation-symmetric combination of two order-`n` statistics that are ~96%
anti-correlated. `σ_c = 1/√3` **derived** from Kerov (only mode m=3 survives);
`σ_h → √6/24` measured; `ρ → 1`; product = **√2/24**, and the roadmap's "trends
slightly above" is finite-n bias in `σ_c`, not evidence against it.

**`κ > 0 ⟺ ρ > 0`** (Lean: `cov_pos_iff_corr_pos`), because σ_h, σ_c are
standard deviations. So the SIGN k5r5 needs is a correlation sign — strictly
weaker than pinning κ, and weaker than Sniady's genus expansion. Measured
ρ = 0.974 → 0.9975 over n = 100..1600.

**14 sorry-free Lean theorems added today**, all on
`[propext, Classical.choice, Quot.sound]`. Pushed.


---

### 2026-08-31 (cont.) — κ leg: a falsified prediction, and where the sign now stands

**Briefed prediction, FALSIFIED.** From `Σc²` being a single Kerov mode (m=3), I
predicted each half of the `[+]/[−]` split would be single-mode too — which
would have turned the −0.62 cancellation into a comparison of two constants.
It is false: `ρ(Σ|cₖ|, Σc²)` is **flat at 0.979** across n = 100..1600 (spread
0.0016 over 16×), and `ρ(ΣDₖ, Σc²) ≈ −0.95`, while their combination `Σh`
reaches **0.9975**.

**What that buys instead.** The off-mode components of `Σ|cₖ|` and `2ΣDₖ`
**cancel each other**: `Σh` is nearly a pure m=3 statistic while *neither of its
parts is*. That is a sharper account of why `Σh` is the special combination than
"it is conjugation-symmetric", and it explains why the cancellation resists
reduction to two constants.

**The "need ratio > −1 uniformly" worry is not live.** Ratio = −0.648, −0.653,
−0.656, −0.655, −0.658 over n = 100..1600 — drifting by 0.010 per 16× in n, so
−1 is unreachable at that rate. And κ itself is **flat** (spread 0.0025 around
√2/24) while the ratio drifts, because `Cov(Σ|c|,Σc²)` drifts to compensate. A
cancellation heading for −1 would show as κ **decaying**; it does not. Weakest
point: n = 1600 uses only 1400 samples.

**New exact identity, Lean-proved.** Adding a box at `(r,s)` raises `Σ□h` by
exactly `1+r+s`, so along a standard Young tableau
`Σ□h = Σ|cₖ| + 2ΣDₖ − n` (verified on all 42400 sampled diagrams). A path sum
equal to a function of the final shape must be path-independent — and it is,
because it collapses to

> **`Σ□ h = Σ□ (i + j + 1)`**  — `sum_hookLen_eq_sum_coords`

exact on all 914 partitions of n ≤ 16 with a firing control. It implies
`two_mul_sum_hookLen`.

Also Lean-proved, closing a step previously only asserted: `cov_involution` /
`cov_eq_cov_symmetrised` — under a weight-preserving involution fixing one
argument, only the symmetric part of the other contributes. That is what makes
`Cov(Σλᵢ²,Σc²) = Cov(Σh,Σc²)`.

**File state:** 59 declarations, **0 sorries**. `ρ → 1` remains measured, not
proved — that is the whole remaining gap for the sign.


---

### 2026-08-31 (cont.) — κ DERIVED = 128/(225π²), and a correction to my own claim

**🛑 CORRECTION.** My `σ_h → √6/24` and `κ → √2/24` from earlier today are
**wrong**. Fitted to n = 400..800 while `σ_h` was still drifting *down* through
them; the z-check passed because its target sat inside the drift. Correct:

> `σ_h = 0.09987155` (not √6/24 = 0.10206207) — matches the n=1600 measurement
> 0.09982967 to 0.04%
> **`κ = 128/(225π²) = 0.05764050`** (not √2/24 = 0.05892557)

`128/(225π²)` is **exactly** the constant this bean's parent `qou-k5r5` already
records as "DERIVED (not fitted) via the Ivanov–Olshanski field" — so the new
derivation reproduces it independently, and the error was mine. Lesson: a
monotone drift over a 4× range in n is not a limit. `..._M1_kappa_structure.py`
FINDING 4 has been retargeted with the correction in its docstring.

### The derivation (new, shorter route) — and the reduction that matters

1. **Exact, Lean-proved** (`sum_hookLen_eq_diag`): a cell on diagonal `c` at
   depth `k` is `(k, k+c)`, so `i+j+1 = 2k+c+1` and summing down the diagonal
   gives `D(c)² + c·D(c)`. Hence
   **`Σ□h = Σ_c D(c)² + Σ_c |c|·D(c)`**.
2. **The `|u|` cancellation.** The two halves are `(n^{3/2}/4)∫(ν̂−|u|)²` and
   `(n^{3/2}/2)∫|u|(ν̂−|u|)`; their first-order parts are `n∫(Ω−|u|)Δ` and
   `n∫|u|Δ`, and the `|u|` **cancels**, leaving `Σh − E ≈ n∫Ω(u)Δ(u)du`. *That*
   is why `Σh` fluctuates at order `n` — an explicit cancellation, not the
   conjugation symmetry.
3. `Σc²` is mode m=3 alone.
4. So `κ = (8/3π²)·f₃` with **`f_m = 16/(m(m²−4)²)`** (odd m, 0 even; checked
   against quadrature to 3.6e-36 over m=1..25). `f₃ = 16/75 > 0`.

> **`κ > 0` is the sign of ONE Fourier coefficient.**

**Refinement that falls out:** `σ_h·σ_c ≠ κ` — κ uses mode 3 alone, σ_h sums all
odd modes. So "ρ → 1" sharpens to a *prediction* `ρ_∞ = 0.99964674 < 1`, against
measured 0.9744…0.9975 over n=100..1600 (still rising, consistent).

**k5r5's remaining claim (b), `κ_n ≥ κ` for n ≥ 13:** measured at 6 sizes,
`κ_n` sits **above** κ at every one — z = 3.14, 1.48, 2.02, 1.26, 0.61, 0.17 for
n = 50..1600, approaching from above, no significant violation.

**Not proved:** steps 2–4 assume Kerov's CLT; Mathlib has no Plancherel measure.
Lean file: 0 sorries.


---

### 2026-08-31 (cont.) — my "can't be formalized" framing was wrong; and κ_n exactly

**🛑 CORRECTION (framing).** I repeatedly wrote "Mathlib has no Plancherel
measure, so this can't be formalized" **without checking what this repo has**.
It has a lot, all sorry-free: `QOU/MathlibExt/QPlancherel.lean`,
`QOU/Observations/{QCltNonCommutative,QPlancherelAsymptoticSkeleton}.lean`,
`QOU/Mass/FreeCumulants.lean`, `QOU/BraidsAndKnots/{YoungDiagramKernel,
M1DescentDPPConvergence,ContentVarianceLeadingConstant}.lean`,
`QOU/Archimedean/QHookBound.lean`.

The accurate statement is narrower and more useful: those are typeclass
**interfaces** per `§3b-cond` — `class QCltNonCommutative`,
`class HasQPlancherelCLT`, `class DescentDPPMarginConvergence` — with **no
instances**. The CLT is *hypothesised*, not proved. Filling it means supplying
instances, which needs unconditional bricks.

**Supplied one.** `ContentVarianceLeadingConstant.lean` scoped out, in its own
header, "**not** the infinite sum (`= 1/8`, a tsum telescoping)". Now proved:

> `vaTerm_hasSum : HasSum (fun k => 1/((2k+1)((2k+1)²−4)²)) (1/8)`

sorry-free, via an exact closed form for **every** partial sum —
`Σ_{k<N} = 1/8 + (1/32)(1/(2N−1) − 1/(2N+1) − 1/(2N−1)² − 1/(2N+1)²)` — which
also holds at N=0, so no positivity side condition. Summability by AM-GM on the
same formula. **Same summand family as my `f_m = 16/(m(m²−4)²)`**, so the two
lines of work meet here.

### κ_n exactly — 13 is the crossing point

`M₁(n)` is an exact rational, so claim (b) needs no sampling.

- **`κ_n < κ` for n = 2..12, `κ_n ≥ κ` for every n ≥ 13.** The gap's threshold
  is exactly where the sequence crosses its own limit. **n = 13 is the binding
  case, margin 0.23%.**
- **My briefed expectation FALSIFIED.** I expected `κ_n` decreasing to κ, making
  (b) a corollary of monotonicity. It is not monotone: `κ_n` **rises to a peak
  at n = 32** (1.026988κ) and falls after, rejoining κ from above (sampled
  0.0590 at n=50 → 0.0577 at n=1600).

**So claim (b) is two regimes, not one:** n = 13..42 is a finite exact check
(**done, to n = 42**), and n ≥ 43 needs an **effective error bound** on
`κ_n − κ`. The remaining work is an error term, not a monotonicity.


---

### 2026-08-31 (cont.) — claim (b) is stronger than the goal needs

`M₁(n) > 0` is **equivalent** to `κ_n > 0` (since `n^{5/2} > 0`), so the tail
never needed `κ_n ≥ κ`. It needs only

> **(b′)  `|κ_n − κ| < κ`**

and the difference in what an effective error bound must deliver is large:

| claim | what the tail must do | required relative accuracy |
|---|---|---|
| (b) `κ_n ≥ κ` | resolve the **sign** of a quantity 2.6% of κ | better than 2.6% |
| **(b′)** | any crude bound | **100% — a ~38× slacker demand** |

Measured over the exactly-computed range n = 32..46: `|κ_n − κ|/κ` runs
0.0270 → 0.0255. At the binding n = 13 the (b) margin is 0.234%, but n=13 sits
**inside** the exactly-verified range, so that tightness costs nothing.

**Lean (both sorry-free):**
- `pos_of_abs_sub_lt {x k : ℚ} (h : |x - k| < k) : 0 < x` — needs **no**
  positivity hypothesis on `k`; `|x−k| < k` already forces both `0 < k` and
  `0 < x`. I first stated it with `0 < k`; the linter flagged the hypothesis as
  unused, and the weaker statement is the right one.
- `pos_of_check_and_tail` — the exact logical shape: finite exact check up to
  `N`, plus the **crude** tail bound past it. Stated over an arbitrary
  `f : ℕ → ℚ` because the content is *which regime carries which burden*, not
  the analysis.

**Exact verification extended to n = 46** (from 42): `κ_n` still above κ, ratio
1.0255, still decreasing from the n=32 peak.

This does **not** close the gap. It replaces a demanding analytic requirement
with an undemanding one. What remains: an effective Kerov error term for
n ≥ 47 — and it may now be crude.


---

### 2026-08-31 (cont.) — weighted Chebyshev proved; the route it does NOT open

**A genuine Mathlib gap, filled.** Mathlib has Chebyshev's sum inequality only
unweighted (`MonovaryOn.sum_mul_sum_le_card_mul_sum`: `(Σf)(Σg) ≤ card·Σfg`),
i.e. `Cov ≥ 0` for the **uniform** measure. Every measure here — Plancherel, the
ω-weighted edge measure — is non-uniform, so that form never applies. New file
`QOU/MathlibExt/WeightedChebyshev.lean`, 4 theorems, sorry-free:

> `weighted_chebyshev : (Σ w f)(Σ w g) ≤ (Σ w)(Σ w f g)` for `w ≥ 0`, `f,g` monovarying

via the exact symmetrisation
`Σᵢ Σⱼ wᵢwⱼ(fᵢ−fⱼ)(gᵢ−gⱼ) = 2[(Σw)(Σwfg) − (Σwf)(Σwg)]`. Setting `w ≡ 1`
recovers Mathlib's statement, so it is a **strict generalisation** and an
upstream candidate.

**🛑 My briefed expectation, FALSIFIED.** I claimed `Σ|c|` and `Σc²` monovary,
so the positive term of the M₁ split "is exactly this inequality". True **per
growth step** (there `c²` is literally a function of `|c|`); **false** for the
sums over a partition, which is what the covariance is over. Exhaustive:
`(Σ|c|, Σc²)` first violates at **n = 7**, `(Σh, Σc²)` at **n = 6**, counts
growing to 120 and 464 by n = 14. **Route as briefed is CLOSED** — recorded so
nobody retries it.

**What survives, and it is the useful part.** The inequality needs only the
*weighted sum* of pair products nonneg, not every pair. Over n = 6..16:

| | by count | by weighted mass |
|---|---|---|
| violating pairs | 0.5–1.8% | **0.05–0.12%** |

neg/pos ≈ 5e-4 — a **~2000× margin**, with `Cov(Σ|c|,Σc²) > 0` at every n. So
proving the positive term needs a **bound on the violating mass**, not a
monovary hypothesis, with three orders of magnitude of room. Same shape as the
(b′) weakening: a crude bound replaces a sharp one.

**Does NOT settle `M₁ > 0`** — the negative term is ~65% of the positive one and
that difference remains the open part.


---

### 2026-08-31 (cont.) — `M₁ > 0` as a pairwise statement: ~48× more room, and a route closed

**The reformulation.** The symmetrisation identity (Lean:
`WeightedChebyshev.two_mul_weighted_cov_eq`) applies to `M₁` **directly**, with
no growth-chain split:

> `2M₁ = Σ_{λ,μ} P(λ)P(μ)·(Σh(λ)−Σh(μ))·(Σc²(λ)−Σc²(μ))`
>
> so **`M₁ > 0` ⟺ concordant pair mass > discordant pair mass**

Finite, pairwise — **no asymptotics and no CLT in the statement**.

**FINDING 1 — ~48× more room than the recorded route.** This bean's parent
records `M₁ = Cov(Σ|c|,Σc²)[+] + 2Cov(ΣD,Σc²)[−]` with the negative term ~65% of
the positive ("need ratio > −1 uniformly") — a margin of ~2.9×. Measured
exactly over n = 6..18, the pairwise ratio discordant/concordant settles at

> **0.007235 over the last five n → a ~138× margin**

with `2M₁ > 0` at every n. Roughly **48× more room** for the same conclusion.

**FINDING 2 — ROUTE CLOSED (measured).** The obvious next step is to call
discordant pairs atypical and apply a classical Plancherel large-deviation bound
on `λ₁`. **It does not work.** Fraction of discordant product-mass from pairs
where either diagram exceeds `t·√n` in row-length or depth:

| t = 2.0 | t = 2.5 | t = 3.0 |
|---|---|---|
| 0.05–1.4% | < 1e-4 % | < 1e-10 % |

So ~100% of the discordant mass sits **inside** the VKLS window — the discordant
pairs are **typical** diagrams, and no `λ₁` tail estimate can isolate them.
Recorded so it is not retried.

**Plainly: `M₁ > 0` is not closed.** The reformulation buys ~48× of room and
removes the CLT from the *statement*, but not from the *proof* — the bound must
come from the bulk, which is where the Kerov machinery lives anyway.


---

### 2026-08-31 (cont.) — the discordant mass factorises; the margin is a CONSTANT

**🛑 My briefed hypothesis, falsified in its strong form.** I expected discordant
pairs to be **close** in `(Σh, Σc²)` — `|Δh·Δc²|` one power of `n` below the
typical `n^{5/2}` — which would have given `discordant/concordant` a free
`n^{-1/2}` decay. It does not hold: `max|Δh·Δc²|` over discordant pairs, divided
by `n^{5/2}`, runs **0.088 → 0.419** over n = 8..18 — *growing*, so that max
itself grows like ~`n^{4.4}`, well **above** the typical `n^{5/2}`. No `n²`
bound, no free decay.

**What is true, and it is the usable part.** The ratio factorises exactly:

> `discordant/concordant = [q/(1−q)] · [mean|d| over discordant / mean|d| over concordant]`

with `q` the **probability** mass of discordant pairs. Both sides are accumulated
independently and agree **exactly** (both rationals; worst relative disagreement
0). Over n = 15..18:

| | n=15 | n=16 | n=17 | n=18 | spread |
|---|---|---|---|---|---|
| `q` | 0.0631 | 0.0607 | 0.0606 | 0.0601 | 0.0031 |
| mean ratio | 0.1110 | 0.1101 | 0.1109 | 0.1124 | 0.0023 |
| product | 0.00748 | 0.00711 | 0.00715 | 0.00718 | — |

So discordant pairs are **~6% of the mass** and each contributes **~9× less**
than a typical pair. The ~138× margin is a **constant**.

That cuts both ways, and both are worth saying: it is exactly what a
*uniform-in-n* bound needs, **and** it is a warning that large `n` will not make
this easier. The factorisation splits the target into two independently
boundable pieces.

**Caveat:** "stable" here is four points of exact enumeration, not an asymptotic.


---

### 2026-08-31 (cont.) — the pairwise route is a KENDALL statement, not circular

**The outcome I set out to rule out.** For a centered bivariate normal with
correlation ρ, two iid draws give exactly `q_Gauss = 1/2 − arcsin(ρ)/π`. If
measured `q` tracked that, the pairwise route would merely **restate** `ρ > 0`
and the 138× margin would be an illusion. Checked before treating it as
progress — and it is ruled out.

**FINDING 1 — `q` is ~2.2× rarer than Gaussian.** Exact, n = 15..18, with `ρ_n`
from the same enumeration:

| | n=15 | n=16 | n=17 | n=18 |
|---|---|---|---|---|
| ρ | 0.9127 | 0.9146 | 0.9163 | 0.9184 |
| q measured | 0.0631 | 0.0607 | 0.0606 | 0.0601 |
| q Gaussian | 0.1340 | 0.1325 | 0.1311 | 0.1295 |
| **ratio** | 0.471 | 0.458 | 0.462 | **0.464** |

Settles near 0.464 (spread 0.013). Discordance is ~2.2× rarer than a Gaussian
with the **same** correlation, so the route carries structure beyond Pearson.

**FINDING 2 — the target in its natural language.** `1 − 2q` is **Kendall's τ**,
so `q < 1/2` is exactly `τ > 0`: a **rank** statement, invariant under monotone
reparametrisation, neither implied by nor implying Pearson `ρ > 0`. At n = 18,
`τ = 0.8799` against the Gaussian-implied `(2/π)arcsin(ρ) = 0.7411` — the rank
dependence is **stronger** than the linear one.

And `M₁ > 0` needs less than `τ > 0`. It needs `[q/(1−q)]·[mean ratio] < 1`, and
the mean ratio is separately ≈ 0.111, so

> **`q < 0.90` suffices, against a measured `q = 0.060` — a ~15× margin on `q`
> alone.**

Two sufficient routes: (`q < 1/2` and mean ratio ≤ 1), or (`q < 0.90` and mean
ratio ≤ 0.111).

**NOT CLOSED.** Both still need a statement about the joint law of
`(Σh, Σc²)`. What changed is the target: a rank quantity with a 15× margin,
instead of a Pearson sign with none.


---

### 2026-08-31 (cont.) — 🛑 RETRACTION: the non-Gaussian advantage erodes

The previous entry concluded, from exact n ≤ 18, that the pairwise route is
**not** a restatement of `ρ > 0` — measured `q` was ~2.2× rarer than the
Gaussian quadrant value. I flagged the risk that this was a small-n artefact
(ρ₁₈ = 0.918 vs the derived ρ_∞ = 0.99965). **It is.**

| n | 15–18 (exact) | 50 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|---|
| ρ | 0.918 | 0.9547 | 0.9759 | 0.9846 | 0.9915 | 0.9951 |
| q measured | 0.060 | 0.0564 | 0.0482 | 0.0412 | 0.0320 | 0.0249 |
| **q/q_Gauss** | 0.46 | 0.586 | 0.688 | 0.738 | 0.768 | **0.792** |

Rising steadily toward 1. At n = 800 discordance is only **1.26×** rarer than
Gaussian, not 2.2×. So the pairwise route looks **asymptotically equivalent** to
the Gaussian picture — i.e. to `ρ > 0` — which is exactly what that finding
claimed to rule out. `..._M1_kendall_route.py` FINDING 1 retitled and amended in
place with a FINDING 3 carrying the data.

**What survives:** `q` itself *decreases* with n (0.060 → 0.0249), so the margin
in "`q < 0.90` suffices" improves to **~36×** at n = 800. The reformulation
still gives a target with a margin; it does not give independence from the
correlation question.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-31 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress 2026-11-16 (PR #8187)

- [x] Added `same_sign_edge_num_bounds`, `edge_ratio_eq_slope_add_gap`, `weighted_edge_ratio_eq_slope_add_gap`, and `sum_edge_ratio_lt_of_slope_and_gap_bounds` in `QOU/BraidKnot/M1EdgeCalculus.lean` + 80-dps `mpmath` probe (`litlfred/qou#8187`, `28237151a70df9ecb11495b374e141771a7b4a76`).
- [ ] Await review and merge of `litlfred/qou#8187`.
