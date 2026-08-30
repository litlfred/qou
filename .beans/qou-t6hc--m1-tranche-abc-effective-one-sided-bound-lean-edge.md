---
# qou-t6hc
title: 'M1 tranche A+B+C: effective one-sided bound, Lean edge-calculus, and the kappa_n correction exponent'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T09:43:34Z
updated_at: 2026-08-30T11:09:40Z
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
