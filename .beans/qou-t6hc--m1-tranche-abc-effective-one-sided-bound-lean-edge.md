---
# qou-t6hc
title: 'M1 tranche A+B+C: effective one-sided bound, Lean edge-calculus, and the kappa_n correction exponent'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T09:43:34Z
updated_at: 2026-08-30T15:10:03Z
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
