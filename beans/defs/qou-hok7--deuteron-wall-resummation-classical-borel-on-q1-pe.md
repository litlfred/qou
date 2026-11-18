---
# qou-hok7
title: 'Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:02:55Z
updated_at: 2026-11-15T22:20:00Z
parent: qou-3e6w
---


DIAGNOSTIC DONE (2026-08-21). Confirmed the full-transseries negative resummed a_D^(n)=I(n)/n (q=1 telephone period) with classical Gamma(n/2+1) Borel; substrate object Z_n(q0) is q-Gevrey (log Z_n ~ Theta(n^2), lever1 order q0^{n^2/2}). classical Gamma-Borel coeff q0^{n^2/2}/Gamma(n/2+1) DIVERGES (1.15->7.3e17, n<=40) => wrong transform. Deuteron-wall resummation REOPENED. OPEN next step: q-Borel-Laplace resummation of Z_n(q0) (divisor ~q0^{n^2/2}); q-Borel machinery exists (qborel-ecalle-resum-barodd, qbeta_habiro_tail_util) but not pointed at the deuteron. Probe: deuteron_wall_wrong_transform_diagnostic.py; audit: 2026-08-21-deuteron-wall-resummation-wrong-transform.md


## 🛑 CORRECTION 2026-09-06 — the divisor in this bean is wrong by a square root (`qou-p6m1` session)

This bean's open step reads "q-Borel-Laplace resummation of Z_n(q0) (divisor
~q0^{n^2/2})". **Measured: the divisor is `q0^{n^2}`.** An agent building the
transform on `q0^{n^2/2}` divides away only half the growth, is left with
`q0^{n^2/2}` still undivided, fails to converge — and would likely read that
failure as a fact about the deuteron rather than about the divisor.

**Probe:** `computations/deltalambda/deuteron_qborel_kernel_level_probe.py` (7/7,
witness `deuteron-qborel-kernel-level.witness.json`).

**Method.** `log Z_n / n^2` is still falling at n=30, so it cannot decide this by
eye. Second differences can, with no fit and no tolerance on the limit:
`d2(a n^2) = 2a` (positive constant) vs `d2` of classical Gevrey-1/2
`(n/2)log n` ~ `1/2n -> 0`. The involution numbers `I(n) = Z_n(1)` are carried as
an IN-PROBE CONTROL: their d2 must fall, and does (0.0553 -> 0.0158). So the
discriminator is validated on a known-classical object, not assumed.

**R1.** `d2 log Z_n` RISES 0.1685 -> 0.1862 toward `2 ln q0 = 0.2087`. Since
`d2(a n^2) = 2a`, that gives `a = ln q0`, i.e. **`Z_n ~ q0^{n^2}`**. The
`q0^{n^2/2}` hypothesis predicts `d2 -> ln q0 = 0.1043`, which is **1.78x below**
the measured value.

**Where the error came from — the producer contradicts itself.**
`lever1_transfer_operator_spectral_qgevrey.py`'s docstring says in ONE sentence
that the multiplier slope is `2 log q0` (correct — it is what its own assertion
`S2_target_2_ln_q0` tests) and then concludes `q0^{n^2/2}`, which does not
follow: slope `2a = 2 ln q0` gives `a = ln q0`. The wrong half propagated here
and into the 2026-08-21 diagnostic.

**R2 — and level 1 is not enough anyway.** `Z_n` is DEFINED as
`S^bal(n;q) * q^{n(n-1)/2}`, and `n(n-1)/2 = C(n,2)` is exactly the exponent of
the corpus's own Lean-proved `QOU.MathlibExt.QBorelKernel.qBorelKernel`. So the
level-1 q-Borel transform of `Z_n` is not a new object — it IS `S^bal`. Stripping
it leaves `d2 log S^bal` RISING 0.0642 -> 0.0819 toward `ln q0`, **5.2x the
control**: `S^bal ~ q0^{n^2/2}`, still q-Gevrey.

Note where `q0^{n^2/2}` correctly belongs: it is the order of **`S^bal`**, the
kernel-STRIPPED object. This bean attached `S^bal`'s order to `Z_n`.

## What is now open (narrowed, NOT closed)

The resummation itself is still not done. What changed is that the target is
specified correctly:

- the divisor is `q0^{n^2}`, i.e. **two** level-1 kernels' worth, not one;
- so the open question is which q-Borel LEVEL applies — `qBorelExp d n` with the
  right `d`, or a level-1 kernel applied twice, or the ramified level-2 family
  that `QBorelKernelLevel.lean:24-27` already names as open;
- `B_D` is NOT reached here and nothing is wired. scope-(a).


## The missing object is SHARED with `qou-odh5` (2026-09-06)

The kernel this bean needs and the one `qou-odh5` is blocked on are the same object.

- **`qou-hok7` (here).** `Z_n ~ q0^{n^2}` needs exponent `n(n-1) = 2*C(n,2)` — twice
  the level-1 exponent. `qBorelExp d n ~ n^2/(2d)` is DECREASING in `d`, so no
  integer level in the corpus family supplies it; what is required is a **half
  level**. Lean: `QOU.MathlibExt.QBorelKernel.two_mul_qBorelExp_one` (sorry-free).
- **`qou-odh5`.** "C1 infinity: extract the two Stokes multipliers." Its own body
  records the lower hull at infinity as the single edge `(0,0) -> (2,-1)`,
  **slope −1/2**, and the open residue as the ramification square roots `B_1,B_2`.
- **`QBorelKernelLevel.lean:24-27`** already names the **ramified level-2 family**
  as the open item, for exactly the slope-1/2 case.

Three descriptions of one gap: a half level / slope −1/2 / the ramified level-2
family. **Constructing it once unblocks both beans.** That is a statement about
the work plan, not a new mathematical result — but it means these should not be
attacked as two separate tranches.

## `qou-odh5` is a STALLED CLAIM, not live work (measured 2026-09-06)

I reported it as "in-progress right now" earlier this session on the strength of
its `status:` field. Measured: its last commit `2ce063f238` is **2026-08-07,
30.6 days ago**, and it is **NOT on main** — the work never landed. Under the
AGENTS.md stalled-claim policy (>3h without a commit on the branch backing a live
in-progress bean) it is available for takeover, following the protocol: re-claim
with a body-append noting the takeover and the stale SHA, continue from that
branch's tip or from main, and never force-push over it.

Recording rather than taking it: reading a `status:` field as evidence of current
activity is the same error class as everything else this bean corrects — a label
quoted in place of a measurement.


## THE SLOPE IS DERIVED (2026-09-06/07, owner asked "derive the slope")

Not extrapolated. Chain, from symmetry to slope:

| step | statement | status |
|---|---|---|
| per-step | `<content> = 0` and `P(descent) = 1/2` at every k=1..21 | EXACT (rational) |
| ⟹ | `<delta_k> = 0 + 2k*(1/2) = k` ⟹ **`<w>_n = C(n,2)`** for every n=1..26 | EXACT — the MEAN |
| degree | `d2(deg Z_n) = 2 - [n triangular]`, exceptions exactly 3,6,10,15,21,28,36 | EXACT to n=41, zero exceptions |
| ⟹ | `deg_n = n^2 - (2*sqrt2/3) n^{3/2} + O(n)`, `c` from triangular density | DERIVED, confirmed 2.06% → 0.60% |
| ⟹ | max/mean → `n^2/(n^2/2) = 2` | **this is why level 1 supplies half** |
| ⟹ | **`d2 log Z_n → 2 ln q0`**, i.e. `Z_n = q0^{n^2 + o(n^2)}` | DERIVED |

**The exact divisor is `q^{deg_n}`**, computable cheaply at any n by the max-plus
recursion. `q^{n(n-1)}` is its leading term, short by `Theta(n^{3/2})`. Use `deg_n`
in the resummation, not the asymptotic form.

**The level-1 kernel now has a meaning it did not have in the corpus:** its exponent
`C(n,2)` IS the mean path weight. "Apply the level-1 kernel" and "centre on the mean"
are the same operation, and the Borel divisor centres on the max instead.

Probes: `deuteron_qborel_kernel_level_probe.py` (10/10),
`deuteron_qborel_slope_derivation_probe.py` (11/11). Lean:
`QOU/MathlibExt/QBorelKernelSquared.lean`, 4 theorems, sorry-free.

### Four routes to REV closed — REV's asymptotics remain the ONE open piece

- **Palindromicity** (would have given `<w>` for free): REFUTED. `min deg Z_n = 0`
  always, so `min+max = deg_n != n(n-1)`; no coefficient vector is palindromic.
- **Extensivity** `REV ~ n*f(q0)`: NOT confirmed. `Delta REV` drifts 0.82 → 0.61
  over n=12..30 rather than settling.
- **2nd-order cumulant expansion** about q=1: tracks at n=8 (5.374 vs 5.371),
  diverges by n=27 (20.63 vs 19.19). Distribution not Gaussian enough.
- **`Var(w)` polynomial closed form**: none. Exact finite differences never vanish
  through order 5; denominators are `I(n)`-related. `12*Var/n^3` drifts 0.70 → 1.16,
  consistent with `Var ~ n^3/10`, unpursued.

The `n^{3/2}` residual model **cannot** be REV's asymptotic form (`REV >= 0`, while
`a*n - b*n^{3/2}` goes negative at finite n), so it describes the measured range only.

**Suggested next attack, given those four:** they all failed through *moments*. Go at
the deficit distribution `N_n(E)` directly — `REV_n = log sum_E N_n(E) x^E` with
`x = 1/q0` is a free energy, and the exactness of `<w> = C(n,2)` suggests `N_n(E)`
has exact combinatorial structure rather than merely asymptotic.


## 2026-09-07 — deg Z_n DERIVED in closed form; REV is a free energy over shapes; and D5's attribution is wrong

Branch claude/zn-hook-length-closed-form-2026-09-07.

**Prior work, cited not claimed** (corpus-grep, six paths): the path decomposition
w(T) = [n(l')-n(l)] + 2 maj(T) is committed at lever1_descent_transfer_operator.py:18-24, and the
hook-side closed form is committed verification target V2 at :45, exact to n<=16. What follows
differs from V2 by the sorry-free substitution sum_c h(c) = n(l)+n(l')+n
(contentSum_eq_hookSum_sub) — a re-normalisation, not a new identity.

**NEW (not on any of the six paths): the degree in closed form.** Each summand of the hook-side
form has degree exactly n^2 - H(lambda), coefficients non-negative, so

    deg Z_n = n^2 - H_min(n),   H_min(n) = min_{lambda|-n} sum_c h(c)
    H_min(n) = 2n - 1 + sum_{k>=2, T_k <= n-1} (n - T_k)  = (2 sqrt2/3) n^{3/2} + O(n)

verified against brute-force minimisation n<=26, and against the exact transfer-operator
polynomial n<=11. The corpus's MEASURED D1 recursion d2 deg = 2 - [n triangular] now FOLLOWS
(exceptions {3,6,10,15,21}, zero disagreement, from partitions alone). The mechanism: H is
minimised by the staircase (k,k-1,...,1), which is an exact partition of n precisely when n is
triangular, where H_min = k(k+1)(2k+1)/6 (square pyramidal). H_min is now O(sqrt n) to compute at
any n — no partition enumeration — so the divisor q^{d_n} this bean asks for is cheap at any n.

**REV is a free energy over SHAPES.** Exactly, no approximation:

    REV_n = log sum_{lambda|-n} exp( R_lambda - (H(lambda)-H_min) ln q0 ),  0 <= R_lambda <= log f^lambda

This IDENTIFIES the deficit spectrum N_n(E) the bean asks to attack: at leading order E is the
excess total hook length, a purely combinatorial object independent of q0. Energy = excess hook
length; entropy = shape multiplicity; neither alone reproduces REV. REV extended to n=44 (p(n)
partitions, not I(n) paths).

**CORRECTION to D5 of deuteron_qborel_slope_derivation_probe.py.** D5 concludes 'the whole
-0.165 n^{3/2} signal is therefore REV's' because d2(degree part) = 0 at the sampled
non-triangular n. Premise right, inference wrong: d2 H_min = [n triangular], so the degree part's
second difference is an indicator on a sparse set and generic-n sampling returns zero BY
CONSTRUCTION. Summed twice that same indicator IS the n^{3/2}: coefficient -(2sqrt2/3) ln q0 =
-0.098373, confirmed to 2e-7 at n=10^6. REV cannot supply it — REV >= 0 while the signal is
negative, and REV is measured sub-linear (REV/n peaks at n=18, falls to 0.650 by n=44).

**Honest limits.** REV's sub-linearity is MEASURED over n<=44, not proved — that is now the open
piece, and it is a sharper one than before because the object is explicit. An earlier R5 asserted
the degree part exceeds REV in magnitude and FAILED: they cross at almost exactly n=44 (24.21 vs
28.60). 'Grows faster' != 'is already bigger'.

**Also fixed:** binding-period-involution-statistic.md claimed the polynomial has degree n(n-1) —
false for every n>=2 (degrees 1,4,8,14 vs 2,6,12,20). The block's own Lean already carried the
counterexample (statExponents_three, max exponent 4).

Probes: zn_hook_length_closed_form_probe.py (6/6), rev_free_energy_over_shapes_probe.py (3/3),
hmin_closed_form_and_rev_sublinearity_probe.py (5/5). Exact integer / 60-dps mpmath, no float64.

## 2026-09-07 — tightness attacked; the r-route MEASURED, and the data cannot yet decide

Attacked the one open piece (is the 3/4 exponent sharp?). No closure. Recording what was measured
so the next agent does not re-walk it.

### The gap has a specific cause

The upper bound composes two facts: R_lambda <= C*r (from L1) and r <= sqrt(H) (from L2, proved in
Lean as H >= r^2, PR #7018). The second is TIGHT for hook shapes — the hook (m,1^{m-1}) has
H = m^2+m-1 against r = m — but very LOOSE where it is actually used, at H = H_min, because
minimal-H shapes are staircase-like with r ~ sqrt(2n) while sqrt(H_min) ~ 0.97 n^{3/4}.

### Measured: max r as a function of the energy budget D = H - H_min

    n     sqrt(2n)   D<=0   D<=5   D<=20   D<=50   D<=inf   sqrt(H_min)
    12      4.90       5      6       6       6        6        6.32
    24      6.93       7      8      10      12       12       10.58
    36      8.49       8      9      11      14       18       14.28
    44      9.38       9     10      12      15       22       16.61

At D = 0 the maximum r tracks sqrt(2n) closely (9 vs 9.38 at n=44) — so minimal-energy shapes ARE
confined to r = O(sqrt n), as expected. r then grows with the budget, locally about sqrt(2n) + D/8
over the measured range, reaching n/2 at D = infinity (the hook shape).

**A tempting inference I checked and did NOT make.** With alpha = 1/8, C*alpha = 0.771 far exceeds
ln q0 = 0.1043, which suggests the energy can never pay for the r-growth and the route is dead. That
argument is WRONG: the linear model is a local fit at small D and does not extend. Globally r <=
sqrt(H), and at large H the energy does dominate — which is exactly why the O(n^{3/4}) bound closes
at all. Do not quote the alpha = 1/8 slope outside the measured range.

### How loose the composition is

    n     TRUE max(R-E)   max(C*r - E)   ratio
    16       8.0802          48.0148     5.94
    24      12.4052          69.2572     5.58
    32      16.2765          88.0997     5.41
    40      19.7497         104.4381     5.29
    44      21.1462         111.5639     5.28

The bound over-states by ~5.3x and the ratio decreases only slowly. So the exponent is not going to
be fixed by a constant; a sharper bound on R_lambda ITSELF is needed, not a sharper r-vs-H relation.

### 🛑 The data cannot yet distinguish sqrt(n) from n^{3/4}

    TRUE max(R-E) / sqrt(n) :  2.02  2.53  2.88  3.12  3.19   (n = 16,24,32,40,44) — still RISING
    TRUE max(R-E) / n^{3/4} :  1.01  1.15  1.21  1.24  1.24   — flattening, but not flat

Neither has converged. A rising sqrt(n) ratio is consistent BOTH with Theta(n^{3/4}) and with
Theta(sqrt n) approaching a constant slowly — and slow convergence is established for this object:
the staircase ratio is still only 4.466 at n=435 against its own limit A*sqrt2 = 5.0959. So n <= 44
is simply too small to separate the two, and no conclusion about sharpness is drawn here.

### What would decide it

Larger n on the max alone: M_n needs a full scan over p(n) partitions (p(60) = 966,467,
p(80) = 15.8M), which is feasible to n ~ 60 in this container and would extend the trend by half a
decade — probably still not enough. The structural route is a bound on R_lambda = sum_m eps_m
N_m(lambda) that uses more than N_m <= r; the two moment constraints (sum N_m = n, sum m N_m = H)
are NOT enough on their own, since the LP relaxation over those alone has supremum n*eps_1, which is
linear and useless.

Status unchanged: Omega(sqrt n) <= REV <= O(n^{3/4}) both proved (#7014, #7018); tightness open.


## 2026-09-07 — the structural handle this bean asked for: beta-coordinates (PR #7070)

The "What would decide it" section above has now been answered on both halves.

**The enumeration half is CLOSED, not merely hard** (#7065). It guessed "feasible to n ~ 60,
probably still not enough". Measured: n = 76 was reached (p = 9,289,091, 17 min) and the answer is
that the statistic itself does not discriminate there. A provably Theta(sqrt n) control — the
staircase — has an n^{3/4} ratio that RISES to a peak at n = 55 and only then falls, so over
n = 36..78 it is flat at 1.20-1.23, the same range and the same value the M_n scan shows. The
control only leaves its peak past n ~ 150, and p(150)/p(84) = 1,539, roughly 52 days of scanning
here. Do not spend more compute on this route.

**The structural half now has coordinates.** This bean asked for "a bound on R_lambda that uses
more than N_m <= r", having ruled out the two-moment LP. The answer is to change variables to the
first-column hook lengths (beta-numbers) beta_i = lambda_i + l - i:

    (I')  R_lambda = sum_i F(beta_i) - sum_{i<j} eps_(beta_i - beta_j) - F(n)
    (II)  H        = sum_i beta_i(beta_i+1)/2 - sum_{i<j}(beta_i - beta_j)
    (III) n        = sum_i beta_i - l(l-1)/2

with F(k) = sum_{m<=k} eps_m. Both R and the energy are one-body plus a PAIR interaction in the
same coordinates — a log-gas shape. Exact: verified on every partition of n <= 13 (eps-weighted,
worst residual 3.3e-49) and n <= 16 (integer arithmetic, exact).

**The pair term is not a correction — it is 41.6% of the constant.** The one-body term alone gives
R <~ l*C, i.e. L1 recovered with nothing gained. On the staircase every gap is even, so the pair
term is sum_d (k-d) eps_{2d} -> k * sum_d eps_{2d}, and

    R_{delta_k} / k  ->  C - sum_d eps_{2d}  =  sum_{m odd} eps_m  =  A = 3.6034

which is EXACTLY the constant proved in #7010. Richardson on k = 64,128 agrees with A to 1.4e-13.
So the interaction is precisely what makes the staircase A and not C. At the other extreme (single
column, all gaps 1) it takes R to exactly 0. The identity is tight at both ends.

### Two things I predicted and got wrong

Recorded because the corrections are the informative part, not as self-flagellation.

- I expected the derived bound to LOSE to C*r, since it is applied with the rows while C*r takes
  r = min(l, lambda_1) and so silently picks the better conjugate reading. It WINS at all six
  empirical argmax shapes, cutting the over-statement of R from 2.46-2.89x to 1.61-1.86x. Those
  shapes have l = r in five of six, so the prefactors tie and the pair term is pure gain.
- I expected its ratio to the truth to GROW with n once maximized with the energy (an upper bound
  with too high an exponent must eventually outrun its target). It FALLS: 4.34x at n=16 to 3.09x
  at n=40, against 5.94x -> 5.29x for C*r.

### 🛑 The inference NOT drawn

Maximized, the bound over sqrt(n) is flat to 9.8% (8.77, 9.45, 9.72, 9.64 at n=16,24,32,40) while
over n^{3/4} it falls monotonically (4.38, 4.27, 4.08, 3.83). That reads as "the bound itself is
O(sqrt n)", which would settle sharpness the OTHER way — the 3/4 not sharp, REV = Theta(sqrt n).
**Refused.** By the control above, n <= 40 sits below the peak of the very statistic being read, on
a range shorter than the one already shown not to discriminate. Recorded as an observation with its
refutation attached.

### What is next, and why it is not another scan

The bound depends on lambda only through (l, W, n), with W = beta_1 - beta_l — three small integers
instead of a partition. So maximizing it does NOT require enumerating p(n) shapes, which is exactly
the wall the enumeration route hit. The remaining work is the admissibility relation linking
(l, W) to H: large W spreads the beta's, which costs H through (II), and that trade-off is now
writable in one variable set. If that optimisation can be done in closed form the exponent follows
at every n, with no scan.

One lossy step stands in the way and should be attacked first: the bound currently applies Jensen
at the mean of each distance class, which is what leaves it ~1.8x above the truth at the argmax.

Status unchanged: Omega(sqrt n) <= REV <= O(n^{3/4}) both proved; **tightness OPEN**.


## 2026-09-07 (later) — the (l,W) reduction is TIGHT, so the beta-bound is the weak step (PR #7081)

The section above proposed the (l, W) reduction as "the route". It was tried. **The transfer does
not fire, and sharpness stays open** — but the negative locates the loss precisely, which the
previous section could not.

**The plan.** REV_n <= M_n + log p(n), and log p(n) ~ pi*sqrt(2n/3) = 2.5651*sqrt(n) is itself
Theta(sqrt n). So an O(sqrt n) rate for max_(l,W) B(l,W) - E would give REV = O(sqrt n) and settle
that the 3/4 is not sharp. The entropy cannot spoil it; the entropy IS Theta(sqrt n).

**Measured to n = 4000** (p(n) ~ 1e64, so five of six points are unreachable by enumeration):

    n            40      100      250      625     1600     4000
    relaxed max  61.1   106.9    231.7    742.9   3070.9  13337.1
    / sqrt(n)    9.67   10.69    14.66    29.72    76.77   210.88
    / n^{3/4}    3.84    3.38     3.69     5.94    12.14    26.52   <- RISES
    argmax (l,W) (22,37) (26,47) (27,62) (43,105) (78,192) (151,357)

The n^{3/4} column rises, so the relaxation's own growth exceeds n^{3/4} and nothing transfers.
REV_n stays in [Omega(sqrt n), O(n^{3/4})], unchanged. No claim either way.

### 🛑 I diagnosed this backwards; the correction is the finding

I asserted the Cauchy-Schwarz Hhat was the weak link — the maximizer runs to l = 151 at n = 4000
against sqrt(2n) = 89, which looked like an energy credit handed out by a slack H bound. The
measurement refutes it. At the maximizer's OWN (l, W), Hhat reaches the true minimum hook sum over
partitions with exactly that (l, W) to 99.3-100% — exact at n = 24 and 32 — and the whole
relaxation overshoots the ENUMERATED max(B - E) by at most 0.15 over n = 16..40.

So passing from a partition to two integers costs essentially nothing. The relaxation is a
**faithful instrument**, and what it faithfully reports is that the beta-bound of #7070 is itself
too weak. The lossy step is **Jensen on the pair term**: at the mean of each distance class it
under-counts badly for gap sequences of mostly 1s with a few large jumps — exactly what the
maximizer selects (W/l ~ 1.7 at every n).

### One sharpening kept

The H lower bound now peels the known extreme part on BOTH halves of 2H = sum lambda_i^2 +
sum lambda'_j^2:  2H >= [lambda_1^2 + (n-lambda_1)^2/(l-1)] + [l^2 + (n-l)^2/(lambda_1-1)]. The
first attempt used the crude n^2/lambda_1 on the columns, which assumes equal column lengths and is
catastrophic for one long row plus many short ones. Fixing it moved n=4000 from 17,309 to 13,337
and the argmax l from 333 to 151. There is now under 1% left in H — **do not spend more on it**.

### Anti-caveat

This is NOT the #7065 situation. There a statistic could not discriminate because the range sat
below its resolving point. Here the reading is a clear RISE across two orders of magnitude in n,
not a flat column being over-read, so the negative does not depend on where that control's peak
sits.

### What the next attempt should do

Replace the Jensen step, not the H bound. Target: a lower bound on sum_{i<j} eps_(beta_i - beta_j)
that survives gap sequences of mostly 1s with a few large jumps. Any candidate is now testable at
n = 4000 in polynomial time against an instrument calibrated to the truth at n <= 40
(rev_beta_bound_polynomial_max_probe.py, R2 dominance + R6 tightness).

Status unchanged: Omega(sqrt n) <= REV <= O(n^{3/4}) both proved; **tightness OPEN**.

---
---
# qou-hok7
title: 'Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0)'
status: in-progress
type: task
priority: high
created_at: 2026-08-21T15:02:55Z
updated_at: 2026-09-07T06:14:21Z

---
# 🛑 MAJOR CORRECTION 2026-09-07 — THE RESUMMATION WAS ALREADY RUN, AND IT IS A NEGATIVE

Everything this bean said today about "what is now open" is **wrong**, and my
"correction by a square root" restates a divisor the corpus had already measured and
used a month ago.

## The run exists, on `main`, since 2026-08-21

- audit `docs/audits/2026-08-21-deuteron-wall-qborel-resummation.md`
- probe `computations/deltalambda/deuteron_wall_qborel_resummation_probe.py`
- commit `d19014bb4f`, verified an ancestor of `origin/main`

It resummed the **right object** (`Z_n(q₀)`) with a **q-Gevrey-matched divisor**, and got:

> **best substrate value = 2.745 % of `B_D` — undershoots by ~36×**

and, decisively for the anti-fit discipline, it reaches `B_D` only at `x ≈ 1.12`, *through*
the Borel singularity — which the audit itself labels: *"Adopting that coupling would be
tuning to the singularity — a fit, forbidden."*

**So the deuteron q-Borel–Laplace resummation is a scope-(a) NEGATIVE, correctly
labelled, and has been for a month.**

## How this bean missed it — and it is the same defect twice in one day

`grep` on this bean: it cites `2026-08-21-deuteron-wall-resummation-**wrong-transform**.md`
(the **diagnostic**) **once**, and `2026-08-21-deuteron-wall-**qborel-resummation**.md`
(the **run**) **zero** times. Two audits, same day, adjacent names; I read the one that
says "this had never been run" and never checked whether it had been run *since*.

That is the second prior-art miss today, after `qou-qbg2` recorded the growth-budget
table a month before I re-derived it — **and I made this one after being burned by that
one.**

## What my #6968 R1 actually was

R1 said the divisor is `q₀^{n²}`, not the `q₀^{n²/2}` this bean specified. **True, and
already known**: the 08-21 run had measured and used it. R1 corrected *this bean's stale
text*, not the corpus's understanding. That is a much smaller claim than the PR made.

## My "use `deg_n`, not the asymptotic form" advice was WORSE, not wrong — measured

I advised using the exact `q^{deg_n}` rather than `q^{n²}`. A sibling report predicted it
would **diverge**. I checked rather than accepting; **the prediction is not confirmed**:

| divisor | `|Z_n/div|^{1/n}` at n = 10, 14, 18, 22, 25 | radius |
|---|---|---|
| `q₀^{n²}` (08-21's choice) | 1.467, 1.426, 1.364, 1.298, **1.249** ↓ toward ~1.05 | ≈ **0.95** |
| `q₀^{deg_n}` (my advice) | 2.006, 2.070, 2.083, 2.066, **2.052** — flat ≈ 2.06 | ≈ **0.49** |

Both converge. But mine gives **half the radius**, pushing the sum further from the
`x ≈ 1.12` where the run reaches `B_D`. **So: not divergent, but materially worse, and
the advice is withdrawn.** Recording the direction because the sibling's prediction and
mine were both wrong in different ways, and only the measurement settles it.

## What genuinely survives from #6968

The derivations, which are new and are untouched by any of this:

- `d²(deg Z_n) = 2 − 𝟙[n triangular]`, exceptions exactly 3,6,10,15,21,28,36, zero
  exceptions to n=41;
- `deg_n = n² − (2√2/3)n^{3/2} + O(n)`, coefficient derived from triangular density;
- `⟨w⟩ = C(n,2)` **exactly**, reducing to `⟨content⟩ = 0` and `P(descent) = ½` per step;
- the five closed `REV` routes.

**And one distinction the corpus did not have**, which the correction sharpens rather
than removes: `deg_n` is the polynomial **degree** (max weight), while the resummation
divisor must track the **value** growth `log_{q₀} Z_n(q₀) ~ n²` (mean-dominated). They
differ by `Θ(n^{3/2})`, and the root test above is exactly the measurement of that gap.
That is why `q₀^{n²}` is the right resummation divisor and `q^{deg_n}` is not — a
question this bean previously got backwards.

## Status

**This bean is NOT closed** — but its open item is no longer "run the resummation." It is
run and negative. What remains genuinely open is `REV`'s asymptotics, which is a
statement about the *object*, not about a route to `B_D`.

Taken over 2026-09-07 by claude/stalled-agents-em-linking-jilmbv; the #7093 session ended awaiting merge permission (last c0704640e2e). Child task qou-0ie7 attacks the Σβ constraint on the same branch; nothing force-pushed.

## 2026-09-07 (later still) — the Jensen step attacked; three refutations and a price (PR #7093)

The section above says: "Replace the Jensen step, not the H bound." Done. It is **not replaced**,
and the reason is now specific enough to be worth more than the attempt.

**The reformulation, which is right and is kept.** Write the beta's by their partial gap sums,
0 = S_0 < S_1 < ... < S_{l-1} = W. Then the pair term is

    P = sum_{0 <= a < b <= l-1} eps(S_b - S_a),

the energy of l points in an interval of length W under the potential eps. So P_min(l, W) is the
**ground state of a one-dimensional repulsive gas with hard walls**. That is the object to bound.

### Three conjectures of mine, all refuted

1. **"The minimiser is the most even spacing."** Misses on 44 of 105 brute-forced (l, W) pairs.
   At (4, 4) the even multiset {2,1,1} gives 6.8236 as (2,1,1) and 6.5135 as (1,2,1) — the energy
   depends on the ARRANGEMENT, not the multiset. Both hand-checks I ran before writing the probe
   had all-equal gaps, i.e. were drawn from exactly the cases where the distinction cannot appear.
   That is the methodological error, not the mathematical one.

2. **"...arranged unimodally, large gaps in the middle."** Better — 44 violations down to 12 — and
   still false. At (5, 11) the true minimiser has gaps (2,3,4,2), which is not the even multiset
   {3,3,3,2} in any order. The minimiser is not a rearrangement of the even gaps at all.

3. **"Jensen can be beaten one distance class at a time."** False and backwards. For a single class
   the differences satisfy x_i >= d and sum x_i <= d*W, and eps is CONVEX — so sum eps(x_i) is
   convex and minimised at the centroid, which IS Jensen. I reached for the opposite extreme point
   expecting an improvement (at (l,W,d) = (22,37,1) it gives 33.4 against Jensen's 24.8); for a
   convex summand that is the MAXIMUM. Verified against 280 random feasible configurations across
   7 triples drawn from the maximizer's own argmaxes: 0 beat Jensen.

### What survives, and why it probably is not enough

Jensen is optimal per class, so the whole loss is the **coupling between classes** — the same gaps
appear in every class and the per-class relaxation forgets it. Brute force prices it, in the regime
the maximizer selects (W/l ~ 1.7):

    l         4        5        6        7        8
    Jensen    3.4004   5.6678   7.5417   9.5157  11.5682
    P_min     4.0481   6.8906   9.2128  11.5733  13.9448
    ratio     1.1905   1.2157   1.2216   1.2162   1.2054

**But priced against the BOUND rather than the pair term, ~1.21x buys little.** The pair term is
one part of B = l*C - P - F(n). At #7081's own n=40 argmax (l, W) = (22, 37):

    l*C - F(n) = 129.60054      J = 50.81003
    B with Jensen               78.790513
    B with the full 1.21x       68.125789      (13.54% smaller)

Against the ~3x over-statement #7081 measured, closing the pair term COMPLETELY at this strength
moves the bound by about a tenth. So solving the 1-D gas exactly would likely still not settle
sharpness, and **the (l, W) route is close to exhausted rather than merely unfinished.**

**Caveat, and it is the thing to check first.** That projection applies a factor measured at
l = 4..8 to l = 22. The factor may grow with l, and brute force cannot say — it is C(W-1, l-2), and
the maximizer's argmax at n = 4000 is (151, 357). If the coupling factor does grow substantially
with l, this route revives; if it is flat, it is dead. That single measurement is the cheapest
decisive next step, and it needs a way to compute or bound P_min at moderate l without enumeration.

### What is left after this

- **If the coupling factor is flat in l:** abandon (l, W). The missing information is not in those
  two integers, and the remaining relaxation of any size is the dropped constraint
  sum(beta) = n + l(l-1)/2, which couples the beta's to n beyond (l, W).
- **A lower bound on the 1-D gas ground state that keeps the gaps coupled** — transfer-matrix or
  convex-duality — is the only way to improve the pair term further. No further per-class
  inequality can help; that is what refutation 3 establishes.

Status unchanged: Omega(sqrt n) <= REV <= O(n^{3/4}) both proved; **tightness OPEN**.

## 2026-09-11 — SHARPNESS SETTLED: REV_n = Θ(√n); the 3/4 exponent is NOT sharp (PR #7185)

The one open piece of this bean since 2026-09-07 — "is the 3/4 sharp?" — is closed on the
side the (ℓ,W)-route sections above refused to read off their flat columns. Not by a sharper
bound on `R_λ` (which "What would decide it" asked for) but by a sharper bound on the ENERGY
as a function of the number of rows, which every prior route threw away when it passed to
`r ≤ √H`.

**The mechanism.** `R_λ = Σ_c ε_{h(c)} − F(n) ≤ (ℓ−1)C` (hooks strictly decrease along a row,
#7018). And with the row form `2H = Σ_{i<ℓ} λ_i(λ_i + 2i + 1)`, tangent lines on the convex row
terms give, for `n = T_k + r`, the polynomial identity

    2(H(λ) − H⁺) ≥ (ℓ − k)² − r,      H⁺ = P_k + r(k+1) = H(λ⁺),   for EVERY λ ⊢ n, every ℓ.

Entropy linear in ℓ, energy quadratic in `ℓ − √(2n)`:

    M_n ≤ (C + L/2)√(2n) + C²/(2L) − C = 8.80√n + 176.3,
    REV_n ≤ M_n + log p(n) ≤ 11.37√n + 176.3.

With #7014's Ω(√n): **Θ(√n).** Lean: `QOU/BraidKnot/HookSumRowTangentBound.lean`,
`two_mul_sum_hookZ_sub_hminClosed_ge`, sorry-free, axioms `propext, Classical.choice,
Quot.sound`. Probe `rev_sqrt_n_upper_bound_probe.py` 7/7: every step exact on all partitions
n ≤ 30; every link of the chain at n = 2..44 (60 dps). Details and the flaw hunt on `qou-0ie7`.

**What this corrects in the sections above.**

- 2026-09-07 "the data cannot yet distinguish": correct at the time; the discriminator was
  never going to be data — the route is a two-line convexity argument the enumerations could
  not see because they never grouped by ℓ.
- #7070 / #7081 "the lossy step is Jensen on the pair term" and #7093 "the (ℓ,W) route is close
  to exhausted": both right about the β-bound and both beside the point. The pair term was
  never needed; `(ℓ−1)C` with the row-indexed energy suffices.
- **#7081's relaxation RISING above `n^{3/4}` to n = 4000 is an instrument artefact**, not a
  fact about REV. Its Cauchy–Schwarz `Ĥ` is **48.9 % of `H_min(4000)`** at its own argmax
  `(ℓ,W) = (151, 357)`: the column half spreads `n − ℓ` cells evenly over `λ₁ − 1` columns,
  impossible with 151 rows, so the maximiser fed on a negative energy no partition has. Its
  99–100 % calibration was at n ≤ 40 where `ℓ − k` is small. The "anti-caveat" in that section
  ("a clear RISE ... not a flat column being over-read") is therefore withdrawn: it was a rise
  in a quantity that is not an upper bound on anything at that n. Reproduced at n = 44 (R5b).
- #7081's argmax drift `ℓ = 151` vs `√(2n) = 89` is explained: the bound's maximiser sits
  `x = C/L = 59` rows above the staircase at every n.

**Still open on this bean** (unchanged, and none of it is the sharpness question): the
substrate-side reading of REV's Θ(√n) coefficient — the bound's `(C + L/2)√2 = 8.80` is an
upper constant, the true `M_n/√n` is 3.19 at n = 44 and still rising toward its limit, which
is not identified; and the q-Borel resummation negative (2026-08-21) stands. **Do not close
this bean.**


## 2026-09-13 — #7081 repaired at the source; TWO defects, not one; and an independent check of #7185

The 2026-09-11 append correctly identified #7081's rise as an instrument artefact. The probe
itself still asserted the false conclusion in its docstring, R3, R4 and R6 — a producer that
gets re-run and quoted — so it is repaired here rather than only annotated. 6/6.

**Defect 1 (as #7185 reported), reproduced independently.** `Hhat/H_min(n)` at this probe's own
argmax: 1.7051 (n=40) -> 0.7005 (250) -> 0.5658 (1600) -> **0.48947** (4000, argmax (151,357)),
matching the reported 48.9 %. The missing energy at n=4000 is 12,705.8 against the 13,337 the
probe reported — i.e. essentially the entire figure. Every partition has `H >= H_min(n)`, so a
lower bound falling below it feeds the maximiser energy no shape can have.

**Defect 2, NEW and independent — the search under-explores every row.** The heuristic
`if v < best - 50: break` is keyed on the GLOBAL best, but the value is UNIMODAL in `W`. At
n = 4000, l = 88 it runs 57 -> 126 -> 260 -> 326 -> 362 -> 438 -> 507 before collapsing, so the
break fires at W = 87 and abandons the row. `(88,174)` alone gives **326.4**, above the staircase
floor `A*sqrt(2n) = 322.3`, and the search never saw it. Caught by asserting the staircase floor
as a validity check — a first repair pass reported 169.4 at n = 4000, *below* that floor, hence
not a bound at all.

The two defects push in OPPOSITE directions, which is why neither surfaced as an absurdity: the
reported figure was neither an upper nor a lower bound on anything.

**The methodological error is the reusable part.** R6 calibrated `Hhat` against the true minimum
`H` at that exact `(l,W)` and got 99.3-100 % — at n <= 40, where brute force reaches and `l - k`
is small — then read the RATE at n = 4000. The calibration was sound; extrapolating it was not.
Same shape as #7093's even-gap conjecture, whose two hand-checks both had all-equal gaps.
Sharper still: R6 was written to test *"the weak link is Hhat"*, which was RIGHT, and inverted it
on that measurement.

### Independent confirmation of #7185, and a refinement of its constant

Swapping the row-tangent floor `2(H - H^+) >= (l-k)^2 - r` into this probe's own maximiser, with
no other change (same eps table, same entropy term, same search):

    n            40      250     1600     4000    10000    40000
    max         225.9    306.9    522.1    723.8   1047.1   1921.7
    / sqrt(n)   35.72    19.41    13.05    11.44    10.47     9.609   <- falls
    / n^{3/4}   14.20     4.882    2.064    1.439    1.047    0.679   <- falls
    argmax l-k     59       59       59       59       59       59

Richardson on the last two (the correction is `O(1/sqrt n)`) gives **8.7462**. The argmax sits
`l - k = 59` at every n against the predicted `C/L = 59.147`.

**Refinement: the coefficient is a BAND, not 8.80.** Maximising `(l-1)C - ((l-k)^2 - r)L/2`
exactly gives `(k-1)C + C^2/(2L) + rL/2`, so the ratio oscillates with `r` in
`[C*sqrt2, (C+L/2)*sqrt2] = [8.7277, 8.8015]`. The 8.80 on this bean is the `r = k` upper
envelope, attained only when `n` sits just below a triangular number; Richardson's 8.7462 is
inside the band. This bears on the open coefficient question below — it is an upper band for the
BOUND, still well above the true `M_n/sqrt n` (3.19 at n=44).

Also checked, since #7185 names it as its one honest Lean gap: `H^+ = P_k + r(k+1)` equals
`H_min_closed(n)` at all eight test n. Numerically confirmed, not proved.

**Withdrawn from this bean's 2026-09-07 sections:** "the (l,W) relaxation is faithful", "the loss
is the Jensen step", the "anti-caveat" defending the rise, and the impact arithmetic computed
against the inflated ~3x. **Surviving:** R1/R2 of #7081; #7093's three refutations about `P_min`
(brute-forced, independent of `Hhat`); and the coupling factor shrinking with `l`.

Status unchanged: **do not close.** The Theta(sqrt n) coefficient and the q-Borel negative stay open.


## 2026-09-13 — the Θ(√n) coefficient is near the STAIRCASE end; the bracket's width is bound slack

The item this bean lists as still open — "the substrate-side reading of REV's Θ(√n) coefficient …
which is not identified" — is narrowed, not closed. Bracket before:

    5.09595 = A*sqrt2         staircase limit, proved (#7010)          LOWER
      ?                       lim M_n/sqrt(n)                          OPEN
    8.72769 = C*sqrt2         row-tangent band, lower edge (#7185)     UPPER
    8.80147 = (C+L/2)*sqrt2   its r = k envelope

**Method: local search over beta-sets at fixed n, not enumeration.** `M_n` is a max over shapes, so
ANY shape's exact `R − E` is a lower bound on it; the staircase is just one shape. Moves shift one
`beta_i` by ±1 with a compensating ∓1, keeping `n` and `l` fixed. One-sided by construction: a find
RAISES the lower end and a miss proves nothing about the upper.

    n       k    stair R    best found   l   l-k   /sqrt(n)   excess
    36      8    17.63209   17.773921    9    1     2.96232   1.00804
    78     12    31.91046   32.601639   14    2     3.69141   1.02166
    136    16    46.29905   47.515487   18    2     4.07442   1.02627
    300    24    75.12050   77.075526   27    3     4.44996   1.02603
    630    35   114.75740  117.133810   38    3     4.66672   1.02071

**Two findings.**

1. **The maximiser is NOT the staircase.** It is beaten at every triangular `n` tested, by a shape
   sitting `l − k` = 1, 2, 2, 3, 3 rows above it. So the coefficient is strictly above `A*sqrt2`
   in the limit unless that excess vanishes.
2. **But the excess is only ~2.4 % and FLAT in n** (0.80 %, 2.17 %, 2.63 %, 2.60 %, 2.07 %), which
   projects a coefficient near **5.22**. Against the bound's 8.728, **the ~1.7× width of the
   bracket is mostly SLACK IN THE ROW-TANGENT BOUND, not headroom in `M_n`.** The next gain is in
   tightening the bound, not in searching harder for shapes.

**Why the excess is readable at n where the ratios are not.** The `/sqrt(n)` column is still
climbing (2.96 → 4.67) exactly as #7065 measured for the staircase alone (4.466 at n = 435 against
its proved 5.0959), so a finite-n ratio below 5.096 is expected and is NOT evidence against the
limit. The excess is a RATIO of two such sequences, in which that common slow convergence largely
cancels — which is the whole reason this measurement works at n ≤ 630.

**Limits, stated.** A projection from five points, not a limit. n = 1275 was attempted and cut: the
search recomputes the value in full (`O(l^2)`) per move rather than incrementally, so it did not
finish in ~9 min; making it incremental is the cheap way to extend the table.

**Discipline check (owner request, same day).** Verified across the whole `qou-hok7` cone —
`rev_beta_bound_polynomial_max`, `rev_pair_term_even_gap`, `rev_coupling_factor_growth`,
`rev_sharpness_discriminator_control`, `rev_max_large_n_scan`, `hmin_closed_form_…`,
`zn_hook_length_closed_form`, and the sibling's `rev_sqrt_n_upper_bound`:

- **Proton pin, by VALUE not by table**: `Q_50_DIGIT_STR = 1.1099785827513808…`; none of the eight
  stems appears in `q0_anchor_manifest.json`'s `ideal_muon` (19 entries), so all default to proton.
- **Convention C/D does not arise**: no Markov parameter `z` appears anywhere in this cone.
  `R_λ = Σ_c ε_{h(c)}` is over HOOK LENGTHS; the C/D question is about the Markov trace parameter
  and is simply not a degree of freedom here.
- **No float64**: no `float(`, `statistics.`, `math.sqrt` or numpy in any of the eight.
  `zn_hook_length_closed_form` is exact-integer polynomial arithmetic and is anchor-free by design.

Status unchanged: **do not close.** The coefficient is narrowed, not identified; the q-Borel
negative (2026-08-21) is untouched.


### 2026-09-13 — the arc's assertions are now Lean, and (I') was already in the corpus (PR #7282)

**Claim.** The three identities this arc runs on are proved sorry-free, and the
central one cost four lines because the corpus already had it in a different
register.

`folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumBetaCoordinates.lean`,
11 declarations, 0 `sorry`, axioms `[propext, Classical.choice, Quot.sound]` on all 11.

| | |
|---|---|
| **(I')** `sum_hookF_add_pairF` | `Σ_c g(h(c)) + Σ_{i<j<L} g(β_i − β_j) = Σ_{i<L} Σ_{m≤β_i} g(m)`, any `g` into an `AddCommMonoid` |
| **(III)** `two_mul_sum_betaR` | `2 Σ_{i<L} β_i = 2n + L(L−1)` |
| **(II)** `two_mul_sum_hookZ_betaForm` | `2 Σ_c h(c) = Σ_i β_i(β_i+1) − 2 Σ_{i<j}(β_i − β_j)` |
| **(II) again** `sum_hookZ_betaForm_of_hookMultiset` | same statement, **independent proof** |

all for **every** padding `L ≥ ℓ(μ)`, not only `L = ℓ(μ)`.

**The finding worth carrying forward.** `QOU.SchurWeyl.hookSide_betaR` already
states, for an arbitrary `CommMonoid`,
`∏_c f(h(c)) · ∏_{i<j<L} f(β_i − β_j) = ∏_{i<L} descFactF f β_i` — the
divisor-free hook-length formula with its Vandermonde denominator. Instantiating
`M = Multiplicative N` turns every product into a sum and **is** (I'). So the
one-body/two-body split this arc has treated as its own structural input is the
hook-length formula, and the corpus proved it months ago on the product side.
`SchurWeyl.betaR L μ i = μ.rowLen i + (L−1−i)` is likewise *already* this arc's
`β_i`; the Lean reuses it rather than redefining it.

**What the corpus did NOT have**: any identity about β-number **sums**. A grep
for a sum over `betaNum`/`betaR` returns nothing. That gap is what this file closes.

**(II) now has two proofs sharing no step** — one through `HookSumClosedForm`'s
`2Σ_h = p₂(λ) + p₂(λ')` (a reflection argument over the cells) plus a termwise
polynomial identity and the vanishing `−3Σm² + (2L−1)Σm = 0` that *is* the
padding-independence; the other through the hook multiset, needing no column
bound `M`. Agreement checks both, and checks the numerical probe (#7070, all
partitions of `n ≤ 16`) that motivated them.

**Implications for this bean.** This formalizes the **foundation**, not the open
question. The Θ(√n) coefficient is still open: #7270 brackets it from the bound
side at `[8.7277, 8.8015]` and #7279 puts the achievable side near ≈5.22, so most
of that 1.7× width is slack in the *bound*. Tightening it is an argument about
`Σ_i F(β_i) − Σ_{i<j} ε(β_i − β_j)` — and that expression is now a Lean theorem
rather than a numerical observation, so a Lean-side bound on it is a route that
did not exist yesterday.

### 2026-09-13 — the 1.71× bracket is ONE term, and it has a name (PR #7286)

**Claim.** The `[A√2, C√2] = [5.0959, 8.7277]` bracket on the Θ(√n) coefficient has
ratio **exactly `C/A = 1.71267243954`** — no `√2`, no `n` — because

    C = A + E_2,      E_2 := Σ_{d≥1} ε(2d)

(the odds and evens partition the positive integers; `A` is the odd half). And `E_2`
is **the staircase's pair term**: `δ_k` has β = (2k−1, 2k−3, …, 1), all gaps even, so
`P_stair(k) = Σ_{d<k}(k−d)ε(2d)`.

**Evidence** (`rev_coefficient_slack_is_the_pair_term_probe.py`, 8/8, mp.dps 80,
Richardson k=800→1600):

| | limit | target | rel |
|---|---|---|---|
| one-body / k | 6.1714057200791 | `C` | 7.9e-80 |
| **pair / k** | 2.5680279943593 | **`E_2`** | 5.9e-80 |
| R / k | 3.6033777257199 | `A` | 9.5e-80 |

**Implication — the open problem moves.** The row-tangent bound reaches `C√2` through
`R ≤ (ℓ−1)C`, which **discards the pair term outright**; the maximising shapes do not.
So this is not diffuse slack to be chipped at from the shape side. The task is:
**prove a pair-term LOWER bound that survives the energy trade-off.** That trade-off
is the real content — `P` is small exactly when the β's are widely separated, which is
exactly when `H` (hence `E`) is large. Any nontrivial pair floor lands the bound near
`A√2` rather than 71% above it.

**New exact fact (R4).** `H(δ_k) = H_min(T_k) = P_k` (square-pyramidal) at all 9
triangular `n` tested, exact integers. **The staircase pays zero energy**, so its value
IS its `R` — which is why `A√2` is a floor on `M_n` and not merely one shape's `R`.

**Correction to my own #7279 reading.** That PR's "achievable ≈ 5.22" invites reading
the excess over the staircase as converging to ~1.02. R5 declines it: `excess/√n` runs
0.0236, 0.0783, 0.1043, 0.1129, **0.0947** — it **peaks at n=300 and FALLS at n=630**.
#7279's own header says a failure to find a better shape does not lower the upper
bound, so a turnover at the *largest* n is more likely the heuristic search weakening
than a fact. Five points, all triangular, cannot separate a multiplicative excess from
an additive one. **Do not quote ≈5.22 as the coefficient.**

**NOT established:** that the true coefficient is `A√2`. Only that the bracket's width
is one identified term and that the bound is where it lives.

**Method note worth keeping.** R1 first FAILED at mp.dps 40 with residual 1.06e-39 —
one ulp. The identity was testing my threshold, not itself. Fixed at the *precision*
(dps 40 → 80, residual exactly 0) against a **derived** `3·N·ulp` bound, not by
widening the tolerance.

**Do not close this bean.**


### 2026-09-13 — the energy trade-off priced; a model refuted, a claim corrected (PR #7286, 2nd commit)

**Claim (the reusable one).** Mean-gap **rigidity**. With `φ(g) = g/√(g−1)`,

    H − H_min ≈ (2n)^{3/2}·[φ(ḡ) − 2]/6 ,   E = (H − H_min)·ln q₀
    φ(2) = 2, φ'(2) = 0, φ''(2) = 1/2   ⟹   E ≈ ln q₀·(2n)^{3/2}·(ḡ − 2)²/24

A **quadratic** penalty of order `n^{3/2}` against a prize of order `√n`. **The mean
β-gap of any maximiser is pinned to `2 + O(1/√n)`.** There is no room for a shape that
spreads its βs to kill the pair term — which is exactly the obstruction a pair-term
lower bound has to clear, and the corpus did not have it.

**Evidence.** `rev_energy_gap_rigidity_probe.py`, 7/7. Checked against **exact integer
H**: ratio to the formula 0.9988 → 0.99999 as ℓ 40→160 at g = 3,4,5; and `H − H_min = 0`
**exactly** at g = 2 for every ℓ (the staircase pays nothing — that is `φ'(2) = 0`).

**Three of mine that did not survive.**

1. **Model refuted.** Rigidity predicts the excess should *shrink* like `1/k`. Measured:
   `excess·k` spreads **73×**, and the model over-predicts by 10–160×. Cause — the extra
   rows sit at small β where `F(β) ≪ C`, so they do not each contribute `A`. R1 untouched.
2. **My #7286-R5 explanation WITHDRAWN.** I blamed the `excess/√n` turnover at n=630 on
   "the search weakening". This is an **independent** search (different move set:
   `β_i+=1 / β_j−=1` at fixed n AND ℓ; different seeds) and it reproduces **all five** of
   #7279's values to the 1e-5 their printed 6-dp figures resolve. Two independent searches
   agreeing is evidence the values are RIGHT. Recomputed at full precision the turnover is
   still there. **R5's numbers stand; my explanation was wrong.**
3. **Assumption falsified.** I wrote "the ℓ=k search reproduces the staircase" as a
   *calibration*. It fails at 4 of 5 k: the staircase is **beaten at its own row count** by
   +0.245/+0.492/+0.815/+0.893 at k = 12/16/24/35. So **`A√2` is the staircase's rate, not
   the optimum's**, and the coefficient is strictly above it.

**R4.** `P/(ℓ·E₂)` at the per-ℓ optimum stays in **[0.90, 1.09]** across all five n — the
maximiser keeps a pair term within ~10 % of the staircase's. Necessary for a pair floor to
be non-vacuous; not a proof that any shape must.

**Still open, and better constrained:** the pair-term lower bound. Rigidity supplies the
half that was missing (βs cannot spread); what is not proved is that a mean-gap-2
configuration must carry `P ≳ ℓ·E₂`. Note #7093 already refuted the obvious route — the
uniform/even gap multiset is NOT the pair-term minimiser at fixed (ℓ,W) — so this needs a
different argument, not a Jensen step.

**Do not close this bean.**


### 2026-09-13 — the Θ(√n) COEFFICIENT IS IDENTIFIED: `A√2`. I withdraw my own #7286 verdict (PR #7294)

**Claim.** `lim M_n/√n = A√2 = 5.09594565`, and the bracket `[A√2, C√2]` — whose whole
1.71× width #7286 showed to be the single discarded term `E₂` — **collapses to its
lower end**.

**Evidence.** Three results, two Lean and one measured:

1. **Rigidity, exact** (`HookSumCompletedSquare.lean`, #7294, 3 decls, 0 sorry).
   Completing the square in the β-coordinates:
   `8H = Σᵢ(2βᵢ − aᵢ)² − Σᵢaᵢ²`, `aᵢ = 2L−3−4i`. The hook sum is a **positive-definite
   quadratic**. `hookDev_sub_succ`: `dᵢ − dᵢ₊₁ = 2(βᵢ − βᵢ₊₁) − 4`, so the deviations
   are constant **exactly** on the staircase. Cauchy–Schwarz then gives a parameter-free
   floor `(Σdᵢ)² − L·Σaᵢ² ≤ 8L·Σ_c h(c)`, tight (zero gap vs `H_min` at `L=k`).
   ⟹ `ℓ = √(2n)(1 + o(1))`.
2. **The excess is BOUNDED** (`rev_excess_scaling_exponent_probe.py`, 11 points to
   n = 3916, 2284 s, 6/6). Excess 2.3764 → 2.4393 over n = 630 → 3916; the last step is
   **+7e-5** across 1.58× in n. Slopes collapse 0.198 → 0.045 → 0.012 → 0.0014 →
   **6.2e-5**; tail α = 0.0043, span-fit α = 0.0499, against the **0.5** a coefficient
   change requires. Converging to ≈ 2.43930.
3. ⟹ `M_n = A√(2n) + O(1)`.

**WITHDRAWN — my own verdict in #7286.** That PR said *"A√2 is the staircase's rate,
not the optimum's, and the coefficient is strictly above it"*. The staircase IS beaten
at its own row count (reconfirmed 11/11 here) — but that inference needs the excess to
be `Θ(√n)`, and **#7286 never checked it**. A bounded difference of two `Θ(√n)`
quantities is subleading and changes no coefficient.

**The maximiser's SHAPE** (`rev_optimal_gap_profile_probe.py`, 5/5): the staircase with
a **top block of 3-gaps**, a bulk of 2s, a **matching bottom block of 1-gaps**, and
**no gap above 3**. 3-count = 1-count at every n. Deviating fraction falls 0.500 →
0.216; deviation count grows with exponent **0.2422 ≈ n^{1/4}**.

**A closed-form model of mine, refuted before it reached a PR body.** Widen one gap to
`G` at fixed `(n,ℓ)`: cost `ln q₀(G−2)²/2`, saving `Σ_{j≥1}[ε(2j) − ε(2j+G−2)]`, peaking
at **G = 5, net +0.9297**. No measured optimum uses a gap above 3. It holds `ℓ` fixed,
forcing the compensating shift uniformly across rows; the real optimum moves `ℓ` and pays
with explicit 1-gaps.

**Two caveats, neither moving the conclusion.** (a) The ℓ-cap `[k, k+5]` binds at
n = 78/136/210 — those three are censored downward; every point from n = 300 up is
interior, and the exponent is set by the tail. (b) One-sidedness: a heuristic search that
under-performs at large n depresses the excess and biases α **downward, toward this very
conclusion**. `R1` guards the evaluator (5/5 vs #7286's independent search), not search
quality at n the earlier probes never reached.

**STILL OPEN — and it is now the only thing between this and a theorem:** the
**pair-term lower bound**, that a mean-gap-2 configuration must carry `P ≳ ℓ·E₂`. The
target is far smaller than it was: gaps within 1 of 2, bounded deviation per position,
sparse. #7093 refuted the Jensen route (the uniform/even multiset is not the pair
minimiser at fixed (ℓ,W)), so it needs a different argument.

**Do not close this bean.**

---

## 2026-09-13 — caveat (a) above is WITHDRAWN: ℓ is padding, not a search dimension

**The claim.** Caveat (a) three paragraphs up — *"the ℓ-cap `[k, k+5]` binds at
n = 78/136/210 — those three are censored downward"* — is **wrong, and it was mine.**
It treats ℓ as a search dimension. Above the maximiser's own row count it is not one:
ℓ is the **padding** of the β-frame, and the objective is provably blind to it.

**The theorem, which came first.**
[`QOU.BraidKnot.HookSum.betaSide_eq_hookSum`](folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumBetaCoordinates.lean)
— sorry-free, `lean`-direct exit 0 with `-DautoImplicit=false -s 65536`, shadow-verified
against current library source, axioms `[propext, Classical.choice, Quot.sound]`. For any
`g` into an additive commutative group and any padding `L ≥ ℓ(μ)`,

$$\sum_{i<L}\ \sum_{m\le\beta_i} g(m)\ -\ \sum_{i<j<L} g(\beta_i-\beta_j)\ =\ \sum_{c\in\mu} g(h(c)).$$

The right-hand side is indexed by **cells** and carries no `L` at all. At `g = ε` the
left-hand side *is* this arc's β-side; `H = Σ_c h(c)` is likewise cell-indexed; so `V` is
padding-invariant. Two lines (`rw`, `abel`) from **(I')**, which has been in that file
since #7282 — I read past it four times. Companion `betaSide_padding_invariant` states the
same over a mere monoid, subtraction-free.

**Measured, and the decisive test is the precision one** — a residual that is arithmetic
shrinks with `dps`, a real dependence sits still
([`rev_l_cap_is_padding_invariance_probe.py`](computations/deltalambda/rev_l_cap_is_padding_invariance_probe.py), 13/13):

| dps | worst residual over 14 paddings | ratio |
|---|---|---|
| 30 | 8.20e-29 | — |
| 50 | 1.15e-48 | 7.1e19 |
| 70 | 8.98e-69 | 1.3e20 |
| 90 | 2.71e-88 | 3.3e19 |

Each 20-dps step divides it by ~1e20. The exact value is **0**. `H` is invariant as an
*integer*. Tolerances elsewhere are **derived** from the summation's operation count
`(L + L(L−1)/2)·|value|·10^{−dps}`, never fitted to the observed residual.

**Consequences**, under an ℓ-scan 4× wider than #7294's window:

- the three "censored" excesses **do not move** (agree to 1e-12) — they were never
  censored, and the caveat predicted a rise the theorem forbids;
- the real threshold is **ℓ\* = k+2** at all three; `V(ℓ)` drops only at `ℓ = k, k+1`;
- **`best_l` in `rev-excess-scaling-exponent.witness.json` is NOISE** and must not be
  quoted as a row count. On a plateau the strict `v > best` comparison is decided by the
  last digit of a different climb path; it reports `k+5` where ℓ\* = `k+2`.

**A finding I was not looking for, and it is the one with teeth.** At **n = 210 the
maximiser is not a unique partition**: a 23-row shape and a 22-row shape tie, and they tie
**exactly**, because they share a **hook multiset** — which `betaSide_eq_hookSum` makes a
*structural* degeneracy, not a numerical near-tie (the objective is a function of the hook
multiset alone). So *"the maximiser's gap profile is a top block of 3s, a bulk of 2s, a
matching bottom block of 1s"* — the 2026-09-13 gap-profile result recorded above — is a
statement about a **hook-equivalence class**, and a search that reports one representative
is not evidence the others were rejected. That result is not refuted; its **scope** was
over-stated, and re-reading it as a class statement is the honest form.

**Untouched:** the `A√2 = 5.09594565` identification. No excess in #7294's table changes,
so neither the exponent slopes nor the excess/√n turnover move at all. Caveat (b) —
one-sidedness — stands exactly as written: every value in this arc remains a **lower
bound** on `M_n`. Padding invariance removes one spurious source of doubt about those
values; it says nothing about whether the climb found the optimum.

**Still open, unchanged:** the **pair-term lower bound**.

**Do not close this bean.**

---

## 2026-09-13 — the staircase leg is CLOSED FORM, and the asymptotic is an IDENTITY

**This needed no new mathematics** — only reading the padding-invariance theorem above in the
direction it already points. `betaSide_eq_hookSum` makes the objective **cell-local**:

$$V(\mu) \;=\; \sum_{c\in\mu}\varphi(h(c)) \;+\; \mathrm{const}(n),\qquad
\varphi(h) := \varepsilon(h) - h\ln q_0 .$$

On the staircase `H = H_min` kills the second term outright, leaving `Σ_c ε(h(c)) − F(n)`. The
staircase's hook multiset is elementary — **`2j−1` with multiplicity `k+1−j`, and no even hook
length at all** — so the sum telescopes:

$$V(\delta_k) \;=\; \sum_{j=1}^{k}(k+1-j)\,\varepsilon(2j-1) \;-\; F(n)
\;=\; A\,k \;-\; B \;-\; F(n) \;+\; \mathrm{rem}_k$$

with `A = Σ_j ε(2j−1) = 3.6033777` (the arc's constant) and **`B = Σ_j (j−1)ε(2j−1) =
5.1893691`**, new. The series form reproduces #7294's committed `V_staircase` column at **all 11
points to 1e-19** — computed from hooks, with no β anywhere, so it checks `betaSide_eq_hookSum`
as much as it checks the multiset.

**And it is an IDENTITY, not an asymptotic.** At triangular `n`, `k + 1/2 = √(2n + 1/4)` exactly:

$$M_n \;=\; A\sqrt{2n + \tfrac14} \;-\; \tfrac{A}{2} \;-\; B \;-\; C \;+\; e_n \;+\; \text{(i)} + \text{(ii)}$$

with `C = Σ_m ε(m)`, `e_n` the excess over the staircase, and two exponentially small remainders
— (i) the series tail `Σ_{j>k}(j−1−k)ε(2j−1)`, (ii) `C − F(n)` — **together 5.1e-16 at
n = 3916**. From `n = 990` up the residual *is* the excess gap to six figures.

$$\kappa \;=\; -A/2 - B - C + e_\infty \;=\; -10.7231689187$$

**Write the √ exactly.** Plain `A√(2n)` carries an extra `A/(8√(2n)) = 0.0051` at n = 3916 —
about **1e13×** the residual it would be explaining. The constant term is only well-defined in
the `√(2n+1/4)` form, and my first pass used the loose one.

**What this does to the open problem.** The entire gap between this and a closed asymptotic is
the single sequence `e_n`. Not the coefficient (settled, #7294). Not the staircase baseline
(exact as of here). **One number** — and it is the same number the pair-term lower bound is
about. That bound's target is now stated in its sharpest form: `e_∞ ≈ 2.43929`.

Two corroborations that do not reuse each other: the predicted multiset's total is
`Σ_j (k+1−j)(2j−1) = k(k+1)(2k+1)/6 = H_min` exactly (integers, k = 1..40), against the
independently-established square-pyramidal closed form; and the remainder is tested against its
**derived** decay rate `q₀⁴` per unit `k` rather than an absolute threshold — converging to
`1.517759` against a predicted `1.517763`.

**Does not make `M_n` a theorem**: the maximiser is still heuristic, so `M_n` is a lower bound,
and `e_∞` is measured at a single `n` rather than proved to be a limit. What is exact is the
**baseline**.

Probe: [`rev_staircase_closed_form_and_constant_term_probe.py`](computations/deltalambda/rev_staircase_closed_form_and_constant_term_probe.py), 7/7.

**Do not close this bean.**

---

## 2026-09-13 — the staircase leg is no longer an enumeration: the multiset is PROVED

The closed form recorded above, `V(δ_k) = A·k − B − F(n) + rem_k`, rested on exactly one
combinatorial fact — **hook length `2j−1` occurs `k+1−j` times, no even hook** — and that fact
was *enumerated*, checked for `k = 1..40`. It is now a theorem for every `k`.

**The presentation is what makes it short.** Present `δ_k` as the **sublevel set**
`{(i,j) : i+j < k}` rather than through `YoungDiagram.ofRowLens`. That form is visibly symmetric
in `i` and `j`, so `colLen` costs nothing — no separate transpose argument — and both lengths
fall out of the matching `mem_iff_lt_*` by the same `omega`. Then, since
`hook = (rowLen − j) + (colLen − i) − 1`:

$$h(i,j) \;=\; 2\,(k - i - j) - 1 .$$

The hook depends only on the **antidiagonal index** `s = i+j`, and antidiagonal `s` carries
`s+1` cells. That *is* the multiset statement. Telescoping it:

$$\sum_{c\in\delta_k} g(h(c)) \;=\; \sum_{s<k} (s+1)\cdot g\!\left(2(k-s)-1\right)$$

for any `g` into an additive commutative monoid — and at `g = ε`, via `betaSide_eq_hookSum`,
that **is** the staircase's β-side.

[`StaircaseHookMultiset.lean`](folio/quantum-observable-universe/lean/QOU/BraidKnot/StaircaseHookMultiset.lean),
0 `sorry`, axioms `[propext, Classical.choice, Quot.sound]`, shadow-verified against current
library source (32 modules had changed since the olean snapshot, so a bare-`lean` green would
have been a claim about the snapshot — `qou-56qy`).

**What the corpus already had, and why it did not cover this.** Checked before writing:
`QOU.StaircaseCornerHook.staircase_corner_hook_eq_two_k_sub_one` proves the **corner** hook is
`2k−1` — the `s = 0` case and nothing more; the rest of that file is the EW-residual conjecture.
And `QOU.Hecke.staircasePartition` is a `Nat.Partition`, so the arc's `YoungDiagram`-indexed
hook machinery cannot reach it at all. Hence a diagram here rather than a bridge.

**A lead for `e_∞`, and a first guess of mine it already killed.** Reading the recorded
maximiser gap profiles (`rev-optimal-gap-profile.witness.json`), `#3-gaps = #1-gaps = d` and
`ℓ = k + d − 1` at all five points, with the gap sum `2ℓ−2` — the staircase span at `ℓ` rows.
That suggested a two-parameter family `(ℓ, d)`. **It is not one.** The 1-gaps are
*interleaved*, not a contiguous bottom block (`n = 78`: `…,1,2,1,2,1`), and `Σβ` depends on gap
*positions*, so `(ℓ,d)` does not determine the shape — a family built with contiguous blocks
reproduces **none** of the measured excesses (only `d = 0` members hit `n` at all, giving
excess 0). The correct statement of the family is the constraint

$$\sum_j (j+1)\,\delta_j \;=\; \tfrac{k(k+1)}{2} - \tfrac{\ell(\ell-1)}{2}, \qquad
\delta \in \{-1,0,+1\}, \quad \textstyle\sum_j \delta_j = 0 ,$$

with the objective also position-dependent. Structured and far smaller than "all partitions",
but not two-parameter. Recorded so the next attempt does not re-make the guess.

**Do not close this bean.**


## 2026-09-13 — M_n is EXACT at small k, and the cost term is a quadratic form (PR #7305)

**The claim.** Two results, one measured and one proved.

1. **`M_n` is no longer a heuristic lower bound for `k ≤ 12`.** Every `M_n` this arc has
   published came from `rev_max_large_n_scan.py` searching a neighbourhood of the staircase.
   `rev_exact_maximiser_small_n_probe.py` enumerates **every** partition of `n = T_k` up to
   `T_12 = 78` (12.1M partitions at k=12, 64 s). At both published points it reaches —
   `n = 36` and `n = 78` — **the heuristic had in fact found the true maximum** (agreement
   4.9e-21, the published column's own printed precision). That is evidence for the rows at
   `k = 16..88`, not proof of them; those stay lower bounds.

2. **`H − H_min = ½ Σ u_i²` exactly**, where `u_i = β_i(ν) − β_i(δ_k)`. Proved, sorry-free,
   `QOU/BraidKnot/HookSumElasticity.lean` (8 declarations, axioms `[propext,
   Classical.choice, Quot.sound]`). No new combinatorial input: `two_mul_sum_hookZ_betaForm`
   and `sum_pair_betaR_sub` have both been in the corpus since #7282, and composing them
   leaves `2H = Σ_i [β_i(β_i+1) − 2(L−1−2i)β_i]` — separable, quadratic, **no pair term**.

**Why it matters for `e_∞`.** The objective is `Σ_c ε(h(c)) − ln q₀·H(μ)`. Everything but `H`
is built from `ε(m) ~ q₀^(−2m)` and is exponentially screened (range `1/(2 ln q₀) ≈ 4.8`
sites). So the problem is now stated in its physical form: **a short-range gain against a
local harmonic cost**, with no long-range term anywhere, and the cost **quantised** —
`Σ u_i²` is an even integer when `Σ u_i = 0`, so `H − H_min ∈ ℤ` and the cost moves only in
whole steps of `ln q₀`. Measured: `H − H_min` = 2, 2, 2, 5, 5, 8 at `k = 7..12`.

**Structure of the exact maximiser**, now established without a search: every gap in
`{1,2,3}`, every 3 strictly above every 1, at all `k = 4..12` (13/13). The heuristic reported
this at `k = 8..35` (`rev-optimal-gap-profile`, R1). Also `e_k = 0` for `k ≤ 6` — the
staircase IS the maximiser and the perturbation switches on at `k = 7`.

**Corollary not previously in the corpus:** the staircase is the **unique** minimiser of the
hook sum at triangular `n` (`staircase_hookSum_eq_iff`). `hmin_closed_form_and_rev_sublinearity_probe`
had the closed form `k(k+1)(2k+1)/6`, not the uniqueness.

**Two corrections to my own checks, fixed at the derivation rather than the tolerance.** X1
compared the enumerated staircase against `A·k − B`, which is the closed form for the *ε*-sum
while the enumeration accumulates the *φ*-sum; the residual was exactly `−ln q₀·H_min`. X8
read the excess back from a 24-digit rendering of itself and reported 2.7e-25 as arithmetic
noise; against the scaled integers it is 1e-40.

**And one anticipated-structure claim of mine that the data refuted.** I expected the
arithmetic-progression frame (`L = k+1`) always to be available via a transpose. At `k = 12`
**neither the maximiser nor its transpose fits `k+1` rows**. This is why the Lean is stated in
a general frame — a theorem hypothesising `ν.colLen 0 ≤ k+1` would not apply to the shapes the
arc cares about.

**What is still open — unchanged.** Nothing here bounds `e_k`. The gain side is untouched, and
`e_∞ ≈ 2.4393` remains the whole gap between this arc and a closed asymptotic. What has
changed is that the question is now a **lattice ground-state problem with an exactly known
cost**, not a β-space pair-term estimate.

**Do not close this bean.**


## 2026-09-13 (later) — the window class is REFUTED; the compensating −1 run is why (PR #7323)

**The claim.** `e_k` is not searchable by confining the displacement to two end windows. The
class reproduces the exhaustive maximum **exactly** for `k = 7..12` and is **3.16 % short** at
`k = 16` with a window already covering 18 of 23 rows; the deficit grows. So the failure is
structural.

**Why — and this is the usable part.** I reconstructed the published heuristic's own maximisers
from their committed gap profiles (`rev-optimal-gap-profile.witness.json`). They reproduce the
published excess exactly, so the reconstruction is verified rather than assumed, and they give
the arc displacement fields it did not previously have, up to `k = 35`:

```
k=16  u = [2,1,0,0,0, −1×6, 0,0,0,0, 1,1,1]
k=24  u = [3,2,1,0,0,0, −1×12, 0,0,0,0, 1,1,2,1,1]
k=35  u = [3,2,1,1,0×7, −1×14, 0×7, 1,1,1,2,1,1]
```

Between the two edges sits a **contiguous run of `−1`**, of length 2, 6, 6, 12, 14 at
`k = 8, 12, 16, 24, 35`. Two facts about it:

- **It gains only at its two interfaces.** A contiguous `−1` run shifts a block down together,
  so every distance *inside* it is unchanged — while it costs `ln q₀ · length / 2`.
- **Its length is forced**, not chosen: `Σu = 0` makes it equal the total positive displacement
  the two edges chose.

**So the two-edge reading survives and the WINDOW is what fails** — the run's *position* is
free and a window pinning the middle has nowhere to put it.

**A correction of mine, and it vindicated the previous PR's scoping decision.** The first
version framed at `L = k+1`, where the staircase β-set is an arithmetic progression and the cost
is a bare `½Σu²`. The exhaustive maximiser at `k = 12` has **fourteen** rows against the
staircase's twelve, so that frame cannot express it and the probe reported `0.5995` against the
true `0.6912`. Using the general-frame Lean identity (`staircase_two_mul_hookSum_sub`, #7305) —
`ΔH = Σ_{i>k}(i−k)uᵢ + ½Σuᵢ²` — fixes it to 1e-40. The generalisation I made in #7305 on the
strength of that same `k = 12` observation was load-bearing within a day.

**Next, and it is concrete:** search `(top edge) × (bottom edge) × (position of the −1 run)`
with the run length forced by `Σu = 0`. Small, exact, and it reaches any `k`. Recorded in the
probe docstring so the next attempt does not simply re-widen the window.

`e_∞ ≈ 2.4393` remains open. **Do not close this bean.**


## 2026-09-13 (later still) — additivity over the two edges is REFUTED (PR #7331)

**The conjecture.** #7323's shape (top block + bottom block + a `−1` run of forced length
`ℓ = S_top + S_bot`) makes the **cost exactly separable**: substituting `ℓ`,
`Σuᵢ² = (Σ_top u² + S_top) + (Σ_bot u² + S_bot)` — no cross term at any `k`. If the gain
separated too, `e_∞ = max E_top + max E_bot` would be a **closed number**.

**Measured, and false.** At `k = 40`, `E_both − E_top − E_bot ≈ 0.6` against `ε(4k) = 3.2e-15`
— fourteen orders apart. Since the cost separates exactly, the residual is wholly gain-side,
and its size names the mechanism: the joint shape has **one** run with **two** interfaces where
two single-edge shapes have **two** runs with **four**. Combining saves an interface pair — an
O(1) gain. Not constant either (0.516–0.617), because a run's own interfaces still interact at
`ε(2·length)`.

**What survives:** the joint argmax **is** the pair each edge picks alone. The edges choose
independently; only the value fails to add.

**Two corrections of mine.**

- **The extension-row count is a search dimension, not a frame choice.** Fixing it at 3 gave
  `2.3684` at `k = 40` — *below* `e_35 = 2.3764`, which monotonicity forbids. That
  impossibility is what exposed the under-search; searching it gives `2.4141`, correctly
  between `e_35` and `e_88 = 2.4393`. Padding is free only when the frame is what is being
  varied; here it bounds which partitions the class can express.
- **A tolerance tighter than the recording it compared against** — #7323's values are 22-digit
  renderings, so ~1e-22 is the floor. Derived now, not picked.

**One structural fact handed over by the search:** `max E_top = max E_bot` **exactly**, equal as
scaled integers (`0.89852649642062312021`, from two independent maximisations). The staircase is
self-conjugate and the hook multiset is a transpose invariant, so `(3,2,1,1)` at the top and
`(1,1,1,2,1,1)` at the bottom are a conjugate pair. **There is one edge energy, seen twice.**

**Where this leaves `e_∞`.** Not closed. The interface term couples the edges, so the two-search
shortcut fails; what is now known exactly is the cost side, the argmax structure, and that the
two edges are one object. Best in class at `k = 40` is `2.41409064417390445671`.

**Do not close this bean.**

---

## 2026-09-13 — `e_∞` is a sum of **three** k-free pieces, and it has a value (PR #7335)

`e_∞` was the one number left: `κ = −A/2 − B − C + e_∞` with the first three explicit convergent
series, and #7294 says so in its own words — *"e_inf is measured at a single n rather than proved
to be a limit."* That single reading was `2.4392948082722254204` at `n = 3916` (`k = 88`).

**The resolution of the previous entry's non-additivity is one sentence: the run belongs to one
edge, not to both.** The entry above stopped at "the residual is an interface count". It is, and
what that means is that the isolated single-edge shapes each carried their **own** run, so their
sum double-counts one run's interface. Put the run in neither edge and make it its **own** piece.

**The load-bearing step is #7323's "the run's position is free."** A displaced row interacts with
another only through `ε`, which decays geometrically — so a free position is a position that goes
to **infinity**. Measured, not asserted (E3b): the block-plus-run value rises monotonically with
separation, `−0.0532` adjacent → `0.4739` at separation 250, reaching `Xblock + Xrun` **exactly**.
Had the interaction been attractive the pieces would not separate and this whole decomposition
would understate the limit.

    e_∞ = max over (s_t, s_b)  [ Xblock(s_t) + Xrun(s_t + s_b) + Xbot(s_b) ]

**`e_∞ = 2.43929645512078402706542884314`**, and it collapses further, because the two block
energies are **equal as exact integers** (E7):

    e_∞  =  2 · E_edge  +  Xrun(2s)
         =  2 × 1.965444371077749996131  +  (−1.491592287034715965196)

with `E_edge` on `[3,2,1,1,1]` (top) and `[1,1,1,1,2,1,1]` (bottom), `s = 8`, run length 16,
extension `P = 2`. **One edge energy, one run.**

**🛑 Correction to the entry above, and to #7331's witness.** That entry says the two shapes
"are that [conjugate] pair" and #7331's `S5` detail says the same. **They are not conjugate
partitions.** Measured: `(3,2,1,1,1)ᵀ = (5,2,1)`, which is not `(1,1,1,1,2,1,1)`; `(3,2,1,1)ᵀ =
(4,2,1)`, which is not `(1,1,1,2,1,1)`. The **equality of the energies is measured** and holds
to the last of 40 digits, twice, by evaluators sharing no code path. The transpose invariance of
the hook multiset remains the likely *mechanism* — but the correspondence between these
particular tuples is **not identified**, and I repeated #7331's claim before checking it.
Contaminated: #7331's witness `edge_energy` detail, the bean entry above, and the first draft of
this one.

**Where the sequence stops moving is measured, not guessed.** The finite-`k` shortfall is nonzero
exactly where a pair still crosses between groups, and both switch off at the same rung — `k = 520`
with the run at the midpoint. They are **not equal**: at `k = 460` the crossing term is 1 unit and
the shortfall 6, because the shortfall also carries each piece's own AP truncation. Reading the two
columns as one number would be wrong; what is measured is that they share a support.

**The first version of this probe was a statement about its own search, and E5 is why.** Its argmax
sat on *every* cap at once — `ell = ELL_MAX`, `p = lt + PWIN`, `len(bot) = BMAX` — and it returned
`2.4392152671991969174`, **below** the `k = 88` heuristic, which `e_k` increasing forbids. That
impossibility is what exposed it, the same way the extension-row count was exposed in the entry
above. Widened (75073 → 3317656 top profiles, 29524 → 88573 bottom, run 40 → 60, `P` 8 → 12) the
value and the argmax do not move.

**Lean, sorry-free** — `QOU/BraidKnot/EdgeDecoupling.lean`, `[propext, Classical.choice,
Quot.sound]`, `lean -DautoImplicit=false -s 65536` exit 0. `sum_pairs_split` makes "restrict the
displacement to one group" an exact summand in any `AddCommMonoid`; `cross_sum_le` bounds the
cross part by `|A|·|B|·g R` for an antitone kernel at separation `R`; `cross_sum_le_geom` is the
archimedean specialisation that sends it to zero geometrically.

**What is NOT established.** That the limit **exists**. `e_k` here is exhaustive over a shape
class, so every value is a rigorous **lower** bound; the class is the shape #7305's full
enumeration independently found at every `k ≤ 12` (E1) and reaches #7331's own `k = 40` maximum
(E2), but an upper bound on `M_n` is still the arc's open item and nothing here supplies one.

**A defect this session introduced three times, now fixed.** The raw-float64 ratchet reported
three NEW dirty witnesses, all from this session's own merged PRs — `rev-excess-scaling-exponent`
(#7294 re-run), `rev-edge-relaxation-window` (#7323), `rev-exact-maximiser-small-n` (#7305). Every
one of the 30 raw floats is a wall-clock `"seconds"` field. `witness_raw_float64_audit.py` carves
out runtime durations **by field name**, and its own self-test at line 699 asserts that
`"seconds"` is *counted* — the carve-out covers only names containing `dur` or `elapsed`. So the
fix is a rename to `elapsed_sec` at the producer plus a re-run, not a baseline entry. The new
probe here emits no timing field at all and carries **zero** float64 values.

**Next:** `E_edge` and `Xrun(ℓ)` are now single k-free numbers over a semi-infinite AP with a
`ε`-kernel. Whether either has a closed form is the remaining question, and it is a much smaller
one than `e_∞` was.

**Do not close this bean.**

### 2026-09-14 — a re-run I made silently cut the exhaustive enumeration by two rungs

Caught in the post-rebase verification, not by a gate. The rename of `"seconds"` →
`"elapsed_sec"` (previous entry) required re-running `rev_exact_maximiser_small_n_probe.py`.
Its reach is an **environment variable**:

    K_MAX = int(os.environ.get("REV_EXACT_KMAX", "10"))

The witness committed on `main` was built with `REV_EXACT_KMAX=12`. My re-run used the default,
so `exact_rows` went `k = 1..12` → `k = 1..10` — the corpus's only exhaustive enumeration of
every partition of `T_k`, narrowed by two rungs, with **no diagnostic anywhere**: the producer
printed `10/10 checks pass`, and the witness is internally consistent at its smaller reach.

**What made it visible was a downstream count, not the producer.** `e_inf`'s E1 calibration reads
that witness and reported *"4 values of k"* where the previous run said 6. The check's own text
then made it worse, because the range was **hardcoded** — it printed `4 values of k (7..12,
n = 28..78)`, i.e. the right count beside the wrong range, which reads as a formatting quirk
rather than as two missing rungs.

**Fixed three ways**, in increasing order of what they buy:

1. Regenerated at `REV_EXACT_KMAX=12`, restoring `k = 1..12`.
2. E1's range is now **derived from the data** it loaded, so a count and a range can no longer
   disagree.
3. The probe reads and records `upstream_enumeration_kmax`, and prints it, so the reach of the
   enumeration this calibration rests on is a stated number rather than an assumption.

**Scope checked, not assumed:** of the four producers re-run this session, only this one reads
an environment variable at all (`grep -nE "os\.environ|getenv"` over all four). The other two
regenerated witnesses are **row-identical to `main`** — `rev-excess-scaling-exponent` 11 rows,
`rev-edge-relaxation-window` 7 rows, same sets.

`e_inf` is unaffected: `2.43929645512078402706542884314`, settled from `k = 520`. E1 is a
calibration of the shape class, not an input to the value.

**The reusable shape:** a producer whose *reach* is an env var with a modest default will
silently shrink under any re-run that does not set it — a rename, a lint fix, a provenance
refresh. The witness stays self-consistent, so nothing downstream fails; only a consumer that
counts rows can see it.

**Do not close this bean.**

---

## 2026-09-14 — both pieces of `e_∞` are CLOSED FORMS in `q₀` (PR #7349)

The previous entry left `e_∞ = 2·E_edge + Xrun(2s)` with both terms `k`-free but obtained by
**search**. Both values are now explicit convergent series; only the argmax *shape* is still a
search result.

**The run.** A run of `ℓ` consecutive `−1`s in a bi-infinite AP of gap 2 leaves every internal
gap alone and moves only the straddling pairs. Collecting by distance and re-indexing
(`Σ_{j≤ℓ} Σ_{d≥j} = Σ_d min(d,ℓ)`):

    Xrun(ℓ) = Σ_{d≥1} min(d,ℓ)·T(d) − (ln q₀/2)·ℓ ,   T(d) = 2ε(2d) − ε(2d−1) − ε(2d+1)

`T` is a **second difference** of `ε` along the progression, so where `ε` decays like `q₀^{−2d}`,
`T` decays like `q₀^{−4d}`. The intercept resums to a single Lambert-type series:

    C = Σ_d d·T(d) = −Σ_{r≥1} (1/r)·(q^r − q^{−r})²·q^{−4r}/(1 − q^{−4r})²
      = −0.657177947545899893947060755021

**The edge.** Same expansion. Every block-to-bulk tail is
`Σ_{d≥m}[ε(2d) − ε(2d+u)] = Σ_r (1/r)(1 − q^{−2ur})·q^{−4mr}/(1 − q^{−4r})`, so `E_edge` is a
finite sum of Lambert series plus finitely many `ε` values — no lattice sum at all.

**Assembled**, the two closed forms reproduce #7335's *independently searched* `e_∞` to the 30
digits its witness records. #7335 searched in scaled integers; this evaluates two series.
Nothing is shared but the argmax shape.

**The asymptote is NOT a shortcut.** At `ℓ = 16` — the length `e_∞` uses — the exact `min(d,ℓ)`
form and the linear asymptote `C − (ln q₀/2)ℓ` differ by **3.1e-4**, four orders above anything
else in this arc, falling to 9.8e-19 by `ℓ = 96`. Quoting the asymptote as `Xrun` would corrupt
`e_∞` in its fourth decimal.

**🛑 Two of my own tolerance derivations were wrong, and the probe caught both.** "Derived, not
chosen" is not the same as "right":

1. The intercept series decays like `q^{−2r}`, **not** `q^{−4r}` — `(q^r − q^{−r})²` contributes
   `q^{2r}` and cancels half the decay. I gave it half the depth it needed and the identity read
   as failing at 1e-30. The depth was short; the mathematics was fine.
2. R5 demanded the secant slope equal `−ln q₀/2` **exactly**, where the approach is asymptotic.
   The bound is now computed from the same `T`.

Both fixed at the derivation, neither by widening a tolerance.

**What is NOT closed.** The **search**: `[3,2,1,1,1]` and `ℓ = 16` are inputs from #7335 and
nothing here proves them optimal. And the **existence of the limit** — still the upper bound on
`M_n`.

**Next:** two targets, and the first is much smaller than it was. (a) Close the *search* — with
`E_edge(u)` now an explicit function of `u`, the block optimisation is an analytic question
rather than an enumeration, and `T`'s sign structure may bound which blocks can win. (b) The
upper bound on `M_n`, which is the arc's one real open problem and is untouched by any of this.

**Do not close this bean.**


---

## The search is COERCIVE, and the greedy route into it is REFUTED (2026-09-14)

Probe [`rev_e_infinity_search_reduction_probe.py`](computations/deltalambda/rev_e_infinity_search_reduction_probe.py), 7/7.
Lean [`SearchCoercivity.lean`](folio/quantum-observable-universe/lean/QOU/BraidKnot/SearchCoercivity.lean), four declarations, sorry-free.

### The negative first, because it kills the argument a reader reaches for

`Xrun` loses `ln q0/2 = 0.05217036` per unit of run length, so the obvious way to bound the
block sum `s` is: find the first `s` where the block's marginal gain drops below that, and
stop. That is a greedy / first-crossing exchange argument and it needs `Xblock` to have
decreasing increments.

**It does not.** Measured marginals:

| s | Xblock(s) | marginal | vs ln q0/2 |
|---|---|---|---|
| 8 | 1.965444371077749996131 | 0.05521818971 | above |
| 9 | 1.993985001872683715154 | 0.02854063079 | BELOW |
| 10 | 2.029360245858113610495 | 0.03537524399 | BELOW |
| 11 | 2.109192647479678445684 | **0.07983240162** | **above** |
| 12 | 2.151115432106013449567 | 0.04192278463 | BELOW |
| 13 | 2.156693167813466520995 | 0.00557773571 | BELOW |
| 14 | **2.159802376118285961604** | 0.00310920830 | BELOW |

The marginal re-crosses upward at `s = 11`. A first-crossing rule stops at `s = 9` and misses
everything above it — including `s = 14`, where `Xblock` actually peaks. So `Xblock` is **not
discretely concave** and no greedy rule closes this search. Scope (a): the greedy route does
not close it; this says nothing about whether some other argument does.

### What does work: coercivity, with no fitted constant

`eps(m) = -log(1 - q0^(-2m))` is convex decreasing, so for **every** sign of `D`

    eps(2d) - eps(2d + D)  <=  |eps'(2d)| * D  =:  g(d) * D

(`D > 0`: `int_a^(a+D)|eps'| <= D|eps'(a)|`; `D < 0`: `-int_(a+D)^a|eps'| <= -|D||eps'(a)|`;
both because `|eps'|` is decreasing). Summing over pairs **telescopes** — the distance-`d`
pairs of a block contribute `(top d entries) - (bottom d entries)` — and with `top_d <=
sqrt(d N)`, `bottom_d >= d`, and the bulk tails bounded by `sum_d d eps(2d) =: S_1`:

    Xblock(u)  <=  S_1 - G_1 + G_half * sqrt(N) - (ln q0/2) N ,   N = sum v^2

a downward parabola in `sqrt(N)`, hence **uniformly bounded in the block's length AND its
entries**:

    S_1    = 6.66246903314631884630
    G_1    = 1.72932318801322827252
    G_half = 1.08314550703034554883
    B_rig  = S_1 - G_1 + G_half^2/(2 ln q0) = 10.5551320927234643540

`B_rig` bounds every valid block. Since `Xrun` falls linearly, only finitely many `(s_t, s_b)`
can win: **unconditionally `s_t + s_b <= 345`**. Checked: 0 violations over the per-sum
maximisers of 8,346,945 enumerated blocks.

**Both signs of `D` are load-bearing.** Keeping only `D+` — dropping the negative pair terms —
makes the bound diverge: nothing then stops a long alternating profile from collecting `g(1)`
per step at merely linear cost.

### The practical cut, and it lands on the incumbent

With the **measured** `B = 2.15980237611828596160353` (at `s = 14`) the cut is `s_t + s_b <=
23`. Inside it the enumeration carries **no effective cap at all** — entries `>= 1` and sum
`<= 23` force length `<= 23` and every entry `<= 23`, so `TMAX = UMAX = SMAX = 23` is exhaustive
— and over all 696,616 blocks the join with `Xbot := Xblock` is maximised at

    (s_t, s_b) = (8, 8),   value = 2.43929645512078402706542884314

reproducing #7335's independently searched `e_inf` to `-2.4e-30`. A second run widened to
24/12 over `s <= 26` agrees at **every** `s <= 23`; its argmax profiles reach length 18 and
entry 4, both inside their caps. #7335's published caps were 8/6 and this is the check it could
not make, its enumeration being over profiles rather than incremental.

### A structural fact worth keeping

`Xblock` peaks at `s = 14` (2.15980) but the join puts the top block at `s = 8` (1.96544) —
**the block gives up 0.19435800 of its own maximum** to shorten `ell` by 12 and buy back
0.62635367 on the run. Neither edge's shape can be read off its own table; that is why the
search is over pairs. Relatedly, `Xblock` and `Xrun` share the same asymptotic slope
`-ln q0/2`, so the join is coercive in `s_t` at rate `ln q0`.

### The two gaps, now sharp enough to name

**G1.** `Xbot(s) <= Xblock(s)` for every `s`. #7335's E7 measured the two tables EQUAL for
`s <= 12` and the top higher by 0.01982 at `s = 13`; beyond that unmeasured. The join above
substitutes `Xblock` for `Xbot`, which is an upper bound **only if G1 holds**.

**G2.** `sup_s Xblock(s) = 2.15980237611828596160353`. Measured over `s <= 26` with caps
lifted and non-binding; bounded rigorously only by `B_rig`, which at 4.887x is far too crude to
substitute.

Under G1 and G2 the `(s_t, s_b)` search is **closed** and `e_inf` is exactly the value above.
Neither gap is the arc's headline open problem, which remains **the upper bound on `M_n`**.

### Lean

`SearchCoercivity.lean` carries the two halves, both `propext/Classical.choice/Quot.sound` only:

- `sub_le_mul_of_antitone_step` / `sub_le_neg_mul_of_antitone_step` — the linearisation, stated
  DISCRETELY (a sequence whose downward steps are antitone) and proved by induction. No
  derivative, no integral, no `Real.log`. The downward twin is the half an agent drops.
- `join_lt_of_lt_sum` / `le_of_le_join` — the reduction: `f, g <= B` and `h` below `V - 2B`
  past `L` confine any pair reaching `V` to `a + b <= L`. Pure order arithmetic, independent of
  what `f`, `g`, `h` are.

Also this session: `EdgeDecoupling.lean` gained the run's re-indexing (`card_filter_lt`,
`card_filter_ge`, `sum_tails_eq_sum_min`, `sum_heads_eq_sum_min`,
`run_pair_sum_eq_sum_min`), with probe check R7 tying each half separately to the two branches
`run_direct` walks — R1 checked only their sum, which a compensating error in the split would
survive. The two halves are NOT the same lemma: different conditions, different kernels, and
measured they differ by up to 3.603.

**Do not close this bean.**


### Tightened the same day: the Cauchy-Schwarz step was the loss (2.7x)

`B_rig` applied `top_d <= sqrt(d N)` once per pair distance, charging the same top rows again
at every `d`. Collecting the linearisation **by row** telescopes to one coefficient per row,
and it has a reading: row `i` from the free top edge only ever sees distances `>= i+1` on its
way to the bulk, so the most it can gain per unit of displacement is

    Ghat(m) := sum_{d>=m} |eps'(2d)| ,    coefficient of row i = Ghat(i+1)
    Xblock(u) <= sum_i [ u_i Ghat(i+1) - (ln q0/2) u_i^2 ] <= B_sharp
    B_sharp   := sum_m Ghat(m)^2 / (2 ln q0) = 3.92139923021415319458

against `B_rig = 10.5551320927234643540`. Tightest slack at the per-sum maximisers: **0.142949
vs 5.38217**, a factor 37.65. Unconditional cut **345 -> 90**.

**Still not enumerable** — 90 is far past any feasible search. What it changes is the shape of
**G2**: closing it is now the same thing as tightening `B_sharp` by a factor under two (it is
1.816x the measured maximum). That makes G2 the most tractable-looking open item here, ahead
of G1.

Probe 8/8 (S8 added: the scaled-integer tables the enumeration runs on against a direct mpmath
evaluator, worst 2.06e-40 against a 2.0e-38 floor — the enumeration uses those tables for
everything, so it cannot check them itself). Library sweep `--only QOU.BraidKnot` 337 ok 0 RED
0 TIMEOUT 0 skipped (671 s); `--only QOU.BraidKnot.SearchCoercivity` 1 ok 0 RED.

**Do not close this bean.**


### G2 shrinks 1.82x -> 1.04x: the block value is CONCAVE (2026-09-14)

Probe [`rev_e_infinity_block_sup_relaxation_probe.py`](computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py), 7/7.

**Where `B_sharp = 3.9214` lost it.** Row 0 alone is **73.79 %** of it — budget 2.8936, attained
at `u_0 = 7.447`. That is fiction: the per-row bound is the tangent at `u = 0` with no cap,
while a single row's gain saturates at `S_e(1) = 2.568` and then turns over. The true best
single-row block is `[3]` at **0.9297** — 3.11x less — and `[8]` is worth **-1.149** against a
bound of 2.878. The linear bound calls a block worth minus one worth nearly three.

**Fix 1, Jensen.** `f(x) = eps(2d) - eps(2d+x)` is concave, so the distance-`d` pair sum obeys
`sum_i f(Delta_i) <= (T-d) f(mean)`, saturating at `(T-d) eps(2d)`. Valid (0 violations),
`B_jensen = 2.6951` over `T <= 12` (2.69566 at `T = 13` in a longer run, 2.5532 by `T = 20`).
Cut `90 -> 43`. **Still not enumerable** (~1e10 blocks).

**Fix 2, and this is the one.** The same second-derivative fact applies to the whole objective:
every internal term is `-eps(2d + (u_i - u_j))` — concave composed with a linear map — every
bulk tail is `-eps(2d + u_i)`, the cost is `-(ln q0/2) sum u^2`. **`Xblock` is concave in `u`**
(verified on 200 random ordered triples, min gap `+0.00147`, not assumed). So maximising over
real `u >= 1` is a **concave program**, a relaxation of the integer problem and hence a rigorous
upper bound:

    B_relax = 2.253731338838604564088   at T = 7
    argmax  [3.9769, 2.794, 2.075, 1.5824, 1.231, 1.0, 1.0]

against the integer maximum 2.1598023761 — **1.04349x**, where `B_sharp` was **1.81563x**. The
argmax is recognisably the integer argmax `[4,3,2,2,1,1,1]` with integrality let out. The AP
ordering constraint was dropped from the program (a further relaxation) and comes out satisfied
at every `T`.

| bound | value | cut | blocks |
|---|---|---|---|
| `B_sharp` (#7349) | 3.9213992302 | 90 | ~1e10 — hopeless |
| `B_jensen` (T<=12) | 2.6951302763 | 43 | ~1e10 — hopeless |
| **`B_relax`** (T<=12) | **2.2537313388** | **27** | **6,325,874 — minutes** |
| integer sup (measured) | 2.1598023761 | 23 | 696,615 |

So the **arithmetic** of an unconditional closure now works: 27 is enumerable, and inside any
such cut the enumeration carries no effective cap (entries `>= 1`, sum `<= L` force length
`<= L` and every entry `<= L`).

**G2 is REDUCED, NOT CLOSED.** Two finite, specified computations remain — neither is an open
question:

- **(a) a certificate for the concave maximum.** Coordinate ascent on a concave function reaches
  the global max and the gradient there is tiny, but *a tiny numerical gradient is not a proof*.
  What settles it is the supergradient inequality `F(u) <= F(w) + grad F(w).(u - w)` at the
  returned `w`, with boundary coordinates (`u_i = 1`) carrying `grad <= 0` by KKT.
- **(b) block lengths `T = 13..40`.** Every row past index 5 contributes at most
  `Ghat(i+1) - ln q0/2 < 0`, so the cumulative per-row cap falls below `B_relax` at a rigorous
  **`T0 = 40`**. This probe measured `T <= 12` (peak at 7, monotone decline after). The 28
  values between are compute, not insight.

Until both are done the cut of 27 is NOT usable and the practical cut stays at 23 on the
measured `B`. Validation: `F([4,3,2,2,1,1,1])` reproduces #7349's enumerated maximum to
**3.5e-21**, and the Lambert tail resummation agrees with the direct sum to 1e-22 at 5 points —
both matter, since the relaxation is only a relaxation of the right problem if the extended
function restricts correctly.

**G1 unchanged.** Nothing here touches `Xbot <= Xblock`, nor the arc's headline open problem,
the upper bound on `M_n`.

**Do not close this bean.**


## 🟩 G2 is CLOSED — `e_inf` is now a MAXIMUM over a proved window, not a search result (2026-09-14, PR #7349)

Gap **G2** was the last conditionality on `e_inf` that came from the *search*
rather than from the mathematics: the `Xbot := Xblock` join was run over a window
chosen because `sup_s Xblock` had been *measured* at 2.1598, not because anything
forbade a larger block from beating it. Both halves of G2 are now shut.

### (a) The concave maximum is CERTIFIED — slack 6.43e-12

`Xblock(u)` is concave in the displacement vector (every internal term is
`−ε(2d + (u_i − u_j))`, concave composed with a linear map; every tail is
`−ε(2d + u_i)`; the cost is `−(ln q₀/2)Σu²`), so the supergradient inequality
holds at **every** `u`:

    F(u)  ≤  F(w) + ∇F(w)·(u − w) .

The linear term is unbounded alone, so the region is confined first: the per-row
bound gives `F(u) ≤ φ_i(u_i) + Σ_{j≠i} rowcap(j)`, so any `u` reaching the
incumbent has `φ_i(u_i) ≥ INT_SUP − Σ_{j≠i} rowcap(j)` — a one-variable quadratic
whose solution set is an interval `[L_i, U_i]`. Outside that box `F` is already
below the incumbent. Maximising the linear term over `[1, U_i]` per coordinate:

    sup F(T = 7)  ≤  2.25373556700090488296611     slack 6.4265742e-12

which is **6.84e-11 of the distance to the integer maximum** — the certificate
costs nothing. The gradient is **analytic** (`gx = −ε'` in closed form); a central
difference would make the inequality a statement about the step size.

**The trap, and it cost me a wrong result first.** At the optimum rows 5 and 6 sit
on the boundary `u = 1` with *strictly negative* gradients (−0.011552, −0.271508).
That is correct KKT behaviour, not a convergence failure. But for `g_i < 0` the
max of `g_i(u_i − w_i)` over `[1, U_i]` is at `u_i = 1`, **not** at `U_i`. Charging
every row `|g_i|(U_i − w_i)` inflates the slack to **1.447** — eleven orders of
magnitude, enough to swamp the result several times over. My first run did exactly
that and reported slack 1.467. The probe now **recomputes that inflated figure
every run** rather than quoting it, so the warning cannot go stale.

Second refinement: the ascent point is **polished** before the certificate is
taken — coordinates parked at `1.0000149` are snapped to exactly `1` (killing a
`+4e-6` boundary term outright) and interior ones get a wider ternary. `F(w)`
barely moves; slack falls 1.50e-5 → 6.43e-12. The certificate is valid at *any*
`w`, so choosing a better one is free.

### (b) Every admissible block length is covered — `T ≤ 40 = T0`

The per-row cap gives a rigorous length bound: every row past index 5 contributes
at most `Ĝ(i+1) − ln q₀/2`, which is negative there (`Ĝ(7) = 0.034051 < ln q₀/2 =
0.052170`) and tends to `−ln q₀/2`, so the cumulative cap falls below the certified
bound at **`T0 = 40`**. No block longer than 40 can reach it, unconditionally.

A `REV_BLOCK_SUP_TMAX=40` run covers the whole of `1..40` and declines
**monotonically** from the `T = 7` peak throughout:

| T | 7 | 12 | 20 | 25 | 30 | 34 | 38 | 39 | **40 = T0** |
|---|---|---|---|---|---|---|---|---|---|
| sup | **2.25373** | 2.11924 | 1.71919 | 1.45889 | 1.19810 | 0.98942 | 0.78073 | 0.72856 | **0.67639** |

Step size settles at exactly `ln q₀/2 = 0.0521704` — one unit of quadratic cost per
added row, the rows past 6 contributing no gain. At `T0` the value is **3.33× below
the peak**, so `T = 7` is the maximiser over the *whole* admissible range, not over
the range that happened to be convenient.

### The payoff: the join at the certified cut reproduces #7335 exactly

Certified `B_cert = 2.2537355670` ⇒ cut `s_t + s_b ≤ 27` (was 90 on `B_sharp`,
~1e10 blocks and hopeless). **6,325,875 blocks**, 19 s:

    e_inf  = 2.43929645512078402706542883973   at (s_t, s_b) = (8, 8), top block [3,2,1,1,1]
    #7335  = 2.43929645512078402706542884314   (independently searched)
    diff   = -3.41e-27

and `max_s Xblock` over the same window is **2.159802376118285961604 at s = 14** —
comfortably under `B_cert`, so the cut is not merely large enough by luck. Note
`s = 14`, not the `s = 9` a first-crossing/greedy rule would stop at: `Xblock`'s
marginal dips below `ln q₀/2` at `s = 9` (0.02854) and `s = 10` (0.03538), comes
back **above** at `s = 11` (0.07983), then falls for good. That refutation stands
and is why the window had to be proved rather than walked.

**So #7335's `e_inf` was a search result and is now a maximum.**

### What is left, stated precisely

- **G1 is the ONLY remaining conditionality on `e_inf`**: `Xbot(s) ≤ Xblock(s)` for
  every `s`. Measured EQUAL for `s ≤ 12`; top higher by 0.01982 at `s = 13`;
  unmeasured beyond. The `Xbot := Xblock` substitution is an upper bound only under
  it. Untouched by any of this.
- **The arc's headline problem — the upper bound on `M_n` — is untouched.** None of
  G2's closure bears on it.

Artifacts: `computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py`
(9/9, checks P8 and P9 are new), witness
`rev-e-infinity-block-sup-relaxation.witness.json`.

**Do not close this bean.**


## 🛑 CORRECTION — G1's only recorded supporting evidence is an ARTIFACT (2026-09-14, PR #7349)

The entry above says G1's evidence is *"measured EQUAL for `s ≤ 12`; top higher by 0.01982 at
`s = 13`"*, and treats that second clause as a data point in G1's favour — the one place the
inequality is strict, and strict in the right direction. **It is not a data point.**

`Xbot` is tabulated by enumerating bottom profiles with a cap of `BMAX = 9` **rows**. Its
maximisers are **flat and long** (entries 1–3, roughly one row per unit of `s`) where the top's
are **steep and short** — at `s = 8` the top winner is `[3,2,1,1,1]` (5 rows) and the bottom
winner is `[1,1,1,1,2,1,1]` (7 rows), *worth exactly the same to all 40 digits*. So the bottom
class exhausts its row budget first, and from that point `Xbot` understates its own supremum.

Vary the cap and the break point moves with it. At **every** setting the winner at the break
uses **exactly `BMAX` rows**:

| `BMAX` | `BUMAX` | equal through | breaks at | winner rows at break |
|---|---|---|---|---|
| 8 | 6 | `s = 11` | 12 | 8 = cap |
| **9** | **3** | **`s = 12`** | **13** | **9 = cap** ← the committed row, the one quoted |
| 10 | 3 | `s = 14` | 15 | 10 = cap |
| 11 | 3 | **`s = 17`** | 18 | 11 = cap |

**At `BMAX ≥ 10` the two tables are EXACTLY EQUAL at `s = 13`.** The 0.01982 does not exist.
`BUMAX` is not the constraint: raising it 3 → 6 while dropping `BMAX` 9 → 8 made the agreement
*shorter*, not longer.

### A prediction of mine that was REFUTED

From the first two rows I read off "break = `BMAX` + 4" and predicted 14 and 15 for `BMAX` 10
and 11. **Both wrong** — 15 and 18. A two-point linear fit on a cap effect, which is exactly
what this repo tells agents not to trust. What survives is only the qualitative claim, which all
four settings support: the break is governed by `BMAX`, saturates it, and recedes as `BMAX`
grows — but not by a fixed offset, because saturating the cap is **necessary and not sufficient**
to lose the maximum (at `BMAX = 11` the winner reaches 11 rows at `s = 15` and equality survives
to `s = 17`).

### What this does and does not change

- **G1 is NOT closed and NOT weakened.** Enumerating a larger class bounds `Xbot` from **below**,
  and a lower bound can only ever *refute* `Xbot ≤ Xblock`, never prove it.
- **Withdrawn**: the `s = 13` observation, as evidence in either direction.
- **Strengthened**: exact agreement now runs through `s ≤ 17` rather than `s ≤ 12` — in exact
  40-digit integer arithmetic, across two *different* evaluators (`ap_value` in the `k → ∞` AP
  for the top; `delta_excess` on a finite `k = 320` staircase frame with a `P` extension for the
  bottom) and two *unrelated* maximiser shapes. 11 of 12 maximiser pairs are not reverses of one
  another, so whatever makes `Xbot = Xblock` it is **not** "read the block backwards".
- `s ≤ 17` covers the certified join window's argmax `s_b = 8` comfortably; it does not cover the
  whole window `s_b ≤ 27`.

### Where the stale sentence still lives

The quoted figure appears in #7335's E7, in three witness `description`s, in two probe headers,
in this bean above, and in #7349's body. #7349's body is corrected. The rest are dated records of
their own analyses and are left as such — the same decision as the `4.66e6` drain (`qou-3nva`).

### Lean

`QOU/BraidKnot/SupergradientCertificate.lean`, six sorry-free declarations (`propext /
Classical.choice / Quot.sound` only):

- `sup_le_of_supergradient` — the G2 certificate as a general theorem: a supergradient inequality
  at `w` (what concavity supplies) plus confinement of any competitive `u` to a box (what the
  coercivity bound supplies) gives an explicit bound on `F` **everywhere**, including outside the
  box, where it is already below the incumbent.
- `box_mul_sub_le` — its load-bearing step, the case split on `sign g`.
- `boundary_charge_eq_zero` / `abs_charge_pos` — why that split is worth 2.25e11 rather than
  being a refinement: a coordinate pinned to `lo` with `g < 0` contributes **exactly zero**,
  where `|g|(hi − lo)` contributes strictly positively.
- `capped_lt_not_sufficient` — the G1 point as a non-implication, with an explicit witness
  (`0 ≤ 2`, `0 < 1`, `¬(2 ≤ 1)`): a capped maximum falling short of a bound implies nothing about
  the true one.
- `capped_gt_is_sufficient` — the direction that *is* valid: only **exceeding** a bound refutes.

### What would actually settle G1

An **upper** bound on `Xbot` of the kind #7349 built for `Xblock` — a per-row coercivity bound on
the bottom edge's own evaluator, then a certificate. Or **bypass it**: the join needs a certified
cut, not a pointwise inequality, so a certified bound on `Xbot` plus an honest enumeration of the
bottom class inside that cut removes G1 from the argument rather than proving it. My judgement is
that the bypass is the better target — it is the same machinery already built for the top edge,
and it retires the conditionality instead of discharging it.

Probe: `computations/deltalambda/rev_e_infinity_g1_bottom_edge_cap_probe.py` (5/5).

**Do not close this bean.**


## 🛑 CORRECTION TO MY OWN CORRECTION — the one-sided sweep was half the story, and the missing half nearly produced a false G1 REFUTATION (2026-09-14, PR #7349)

The entry above diagnoses the `s = 13` figure as the **bottom** enumeration running out of rows,
and demonstrates it by raising `BMAX` 8 → 9 → 10 → 11 against the committed `TMAX = 8`. That
diagnosis is **correct and is confirmed below**. The *method* is not sound, and pushing it one
step further shows why.

### At `BMAX = 12` the bottom OVERTAKES the top — and that is not a refutation

| s | top (`TMAX=8`) | bot (`BMAX=12`) | top − bot |
|---|---|---|---|
| 16 | 2.0802943029 | **2.1301891570** | **−0.0498949** |
| 17 | 1.9971122429 | **2.0663634247** | **−0.0692512** |
| 18 | 1.9261369638 | **1.9858139748** | **−0.0596770** |

Read at face value that **refutes G1** (`Xbot(s) ≤ Xblock(s)`). I was one edit away from writing
that down. It is an artifact of the **top's own cap**: the top maximiser saturates `TMAX = 8` from
`s = 15` on (`[4,3,2,2,1,1,1,1]`), so past there it is the *top* table that has run out of rows.
**Raising one cap against a fixed other is the same mistake the entry above is about, one level
up**, and it fails in the more dangerous direction — toward a false refutation rather than a
false confirmation.

### The symmetric comparison, which is the one G1 actually asks for

Both classes at **12 rows** (top entries ≤ 5, bottom ≤ 3; 4,054,896 and 797,161 profiles):

- **exact equality for every `s = 1..16`**, 40-digit integer, no tolerance;
- the top is strictly higher from `s = 17`;
- **the bottom exceeds the top at NO `s` in the measured range** — nothing here refutes G1.

So the `s = 13` withdrawal stands and is *strengthened*: at matched caps the two are equal there,
and the honest agreement run is `s ≤ 16` rather than the `s ≤ 17` the one-sided sweep reported.

### Why an equal cap is still not a FAIR cap

At every `s` where both winners sit strictly inside the cap, the **bottom needs more rows than the
top** — at `s = 14`, **ten against seven**; at `s = 8`, seven against five. The bottom's
maximisers are flat and long (`[1,1,1,1,2,1,1]`), the top's steep and short (`[3,2,1,1,1]`). A
numerically equal row cap therefore systematically favours the top, which is exactly how the
committed `BMAX = 9` against `TMAX = 8` came to look balanced when it is not. **A fair cap gives
the bottom more rows, not the same number.**

### Two hypotheses of mine, both refuted en route

1. **"The bottom edge pays an extra cost the top does not, so `Xbot ≤ Xblock` is structural."**
   The cost is real — `delta_excess` carries `lin = Σ_{i>k}(i−k)u_i`, absent from `ap_value`,
   worth `ln(q₀)·lin` and reaching **0.7304** at the `s ≥ 11` winners (`lin = 7`). But it does not
   give the inequality: the bottom reaches the *same* maximum while paying it, so the gain side
   must exceed the top's by exactly that handicap at every `s`. Not a relabelling, and not a
   proof. *(I first printed `lin` through the probe's `sc()` scaler, which divides by 1e40 and
   made a 0.73 handicap read as `7e-40`. The number was never wrong; the display was.)*
2. **"The agreement is a value-preserving correspondence between the two classes."** **Refuted.**
   Compared value *multisets* per `s`: identical for `s ≤ 9`, but from `s = 10` the bottom class
   **misses** top values it cannot attain (1 at `s=10`, 3 at 11, 9 at 12, 24 at 13, 61 at 14) —
   while being much *larger* in count (1,902 vs 953 at `s = 14`). So it is a coincidence of
   **maxima**, not a bijection, which makes the exact agreement over sixteen values of `s` more
   striking rather than less.

### Structural context worth recording

`staircase_beta(k, L)` is **two different environments**: rows `i ≤ k` are an AP of **gap 2** (the
top edge's world), rows `i > k` are consecutive, **gap 1** (the bottom wall). The bottom block
straddles them — at `pe = 3` its lowest three rows are in the gap-1 wall and the rest in the gap-2
AP. So the two edges are not the same problem in different coordinates, and their agreement is not
a symmetry of the frame.

### Status

**G1 is STILL OPEN, neither closed nor weakened.** Every table here is a maximum over a *capped*
class, hence a **lower** bound on its own supremum, and a lower bound can only refute the
inequality, never prove it. Past `s = 16` the bottom winner is cap-saturated, so `s ≥ 17` is
**undetermined**, not settled in the top's favour. `s ≤ 16` covers the certified join window's
argmax `s_b = 8` comfortably; it does not cover the full window `s_b ≤ 27`.

Probe `rev_e_infinity_g1_bottom_edge_cap_probe.py` gains **G1f** (the symmetric comparison) and
**G1g** (the row-count asymmetry); its docstring, summary, witness `description` and `verdict` are
corrected, and the witness field is renamed `agreement_widest_cap_ONE_SIDED` with a `_note`
saying it is not a G1 verdict — so the next agent cannot read the one-sided number as one.

**Do not close this bean.**


## 🟩 G2 CLOSED AND MERGED; the Xbot coercivity transfers but is 9.6× too loose (2026-09-15, #7349 merged / #7419 open)

**#7349 is merged** — `05eaebd6b2f`, rebase-merge, **11/11 commits replayed** (patch-id verified
with `verify-merge-replay.py`, not `git diff`, which after a rebase-merge compares a commit to
itself and can never fail). Verification on the final rebased head: Lean sweep
`--only QOU.BraidKnot` **528 ok / 0 RED / 0 TIMEOUT / 0 UNVERIFIED**, with all four changed Lean
files verified by name.

### 🛑 Two sweep runs had to be rejected as gates first, and neither failure was about Lean

- The first crashed at module **282/1710** on `OSError: [Errno 28] No space left on device`
  **while printing a clean `1 ok, 0 RED` summary line belonging to a different, tiny package.**
  Taken at face value that reads as a pass.
- The second ran clean to **1038/1710** and hit my own 57-minute timeout — 0 RED throughout, but
  672 modules unverified.

The closure was 1710 modules only because rebasing onto 163 commits of `main` marks most of the
library's sources newer than their oleans. What scoped it honestly: **all three of my changed
Lean files import only Mathlib — zero QOU imports**, so the hazard the sweep guards against (a
*QOU* signature moving under a file that calls it, #6751) cannot touch them; the only changed
file that depends on QOU is the aggregator `QOU.BraidKnot`, and `--only QOU.BraidKnot` covers it,
its subtree and all three files.

**Container hygiene, worth recording as a recurring cost.** Disk was at **305 M free** — near the
point where the Bash harness cannot write its own output capture and every command fails. Freed
**7.4 G**, all regenerable: two stale ~2.5 G `lean-*-sweep` shadow trees from earlier sessions,
the **1.7 G leaked `/tmp/tmp.*` lake-cache restore tarball** (the exact leak AGENTS.md documents —
the `trap` in the restore recipe is load-bearing and something bypassed it), and a 697 M
already-extracted toolchain zip. Passed on to #7318, whose scope makes it the next likely victim.

### The Xbot upper bound — #7419, the gate on the G1 bypass

No enumeration can settle G1 (a capped maximum is a lower bound; a lower bound can only refute).
The needed object is an **upper** bound on `Xbot`, which also **bypasses** G1 since the join needs
a certified cut, not a pointwise inequality. So: does #7349's per-row coercivity transfer?

**It was not a formality.** `staircase_beta` is **two environments glued at a wall** — rows
`i ≤ k` an AP of **gap 2**, rows `i > k` consecutive **gap 1** — and the bottom block straddles
them (measured: every gap above the wall is 2, every gap below is 1; `b0` reads `…7,5,3,2,1,0…`
at the junction). Two further terms the top edge lacks entirely:

| term | `ap_value` (top) | `delta_excess` (bottom) |
|---|---|---|
| one-body `fi(β) − fi(b0)` | **identically zero** (`β ~ 2k` saturates `F`) | up to `ε(1) = 1.6695` per unit displacement at the wall |
| `lin = Σ_{i>k}(i−k)u_i` | **no analogue** | `ln(q₀)·10 = 1.0434` over the class |

Against an `Xbot` worth ~2.16, neither is perturbative.

**Result: the bound holds, 0 violations over 17,534 (profile, pe) pairs**, tightest slack 0.4012:

```
delta_excess(u) <= sum_a u_a Ghat_bot(a) - ln(q0) lin - (ln q0/2) sum u^2

Ghat_bot(a) = eps(b0_a+1)  +  sum_{b0_j < b0_a} delta(b0_a-b0_j)  -  sum_{b0_j > b0_a} delta(b0_j-b0_a)
```

`Ghat_bot` is a **difference, not a sum** — rows below a displaced row are a gain, rows above a
loss, and deep in the staircase there are ~`k` rows above. That was the substantive question and
it comes out fine. `delta(m) = ε(m) − ε(m+1)` is the **discrete** step, i.e. exactly the object
`SearchCoercivity.sub_le_mul_of_antitone_step` is stated over, so the per-pair step is licensed by
a sorry-free lemma rather than by a derivative argument. (The *assembly* over the frame is
empirical, not formalised — say so when citing this.)

**🛑 And it is 9.62× too loose to use.** Uniform cap **20.7758** against an enumerated maximum
**2.1598**. `B_sharp` was **1.82×** for the top edge and *even that* gave an unenumerable cut of
90. So the route is **LIVE** and the bound **is not yet a tool**. The looseness has the same shape
`B_sharp`'s did — a per-row tangent with no cap while a single row's real gain saturates — so the
concave relaxation that took the top edge 1.82× → 1.04× is the next step, not a new idea.

**A bug of mine, caught before it was quoted.** X4 first summed the per-row caps across **all nine
`pe` frames** → **171.11**. A block occupies exactly **one** frame, so the uniform bound is the
**max over `pe`**: **20.78 at `pe = 6`**, an inflation of **3.9×** that would have made the route
look four times more hopeless than it is. The probe now prints both and labels the cross-frame sum
wrong in its own output; the witness carries the per-frame breakdown.

### Status

**G1 is UNTOUCHED** — neither closed nor refuted. #7419 measures whether one already-formalised
tool reaches the bottom edge, which is the gate on the bypass route, not the bypass. The arc's
headline problem, the upper bound on `M_n`, is untouched as throughout.

**Next:** the concave relaxation on `Ghat_bot`, mirroring #7349 Part 3 — the bottom edge's
objective should be concave in `u` for the same second-derivative reason, so maximising over real
`u ≥ 1` is again a relaxation, and the supergradient certificate of
`SupergradientCertificate.sup_le_of_supergradient` applies verbatim (it is stated for an arbitrary
`F`, `w`, gradient and box, and knows nothing about the `REV_n` objective).

**Do not close this bean.**


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-09-15 — the concave relaxation reaches the bottom edge, and the two edges differ in KIND

PR #7419, continued.  #7349 closed G2 by certifying the TOP edge (concave relaxation +
supergradient certificate, slack 6.4e-12, 1.04x the integer maximum).  The sibling coercivity
probe showed the per-row linearisation reaches the bottom edge but caps it 9.6x too high.  This
session carried the concave route across.  Three things are established and two bugs were caught
by invariants rather than by inspection.

**The extension to real `u` is exact, not merely valid.**  `delta_excess`'s one-body term
`fi(beta) - fi(b0)` is a partial sum with no canonical real extension.  The obvious integral
extension `int_0^u eps(b0+t)dt` is concave and is an upper bound, so it would relax — but it is
NOT exact at integers, and would carry avoidable slack at every one.  `R(b0) - R(b0+u)` with
`R(x) = sum_{j>=1} eps(x+j)` is both, because the constant `sum_m eps(m)` cancels.  Verified
against the committed `delta_excess` on 36 (pe, block) pairs to 8.7e-25.  The extended objective
is concave (min gap 0.0057 over 300 random feasible triples) and its closed-form tails and
analytic gradient agree with direct sums to 6.2e-25 / 4.2e-16.

**`Gamma_j` is exactly independent of the block length** (agrees to 1.7e-23 across T = 3, 7, 11).
The block rows above `j` and the undisplaced tail above the block are one sum split at an
arbitrary place.  So a length-T program is the restriction of ONE program to its first T
coordinates, and a certificate at a zero-padded ascent point bounds every length at once.

**#7349's block-length bound does NOT transfer, and the reason is the class, not the analysis.**
Its blocks have every entry `>= 1`, so a row whose tangent slope falls below `ln q0 / 2`
contributes a strictly NEGATIVE cap and the cumulative cap eventually drops below the certified
bound.  The bottom class permits zero entries (`bot_profiles` requires only the leading one
positive), the relaxation therefore has `u >= 0`, every row cap is `>= 0`, and the cumulative cap
never falls.  I wrote the transfer first and asserted the padded rows are charged zero; they are
not — every `Gamma_j` is strictly POSITIVE, in the pure AP exactly `sum_{i odd} gx(b0_j + i)`,
the odd gaps the one-body term reaches and the gap-2 ladder does not.  A termination test written
for `cap == 0` never fires, which is how it was caught: by a guard that refused to return a
truncated sum, not by reading the code.

**Consequence: the plain relaxation is valid and measurably NOT tight.**  A real `u` collects a
gain from an arbitrarily small displacement on arbitrarily many rows; no integer block can, since
its entries jump from 0 to 1.  Measured at `pe = 2`, the relaxed sup is still rising by `+0.2301`
at `T = 6`.  The tightening is a valid inequality rather than more compute: every integer
`u_j >= 0` has `u_j^2 >= u_j`, so `sup_integer G <= sup_{real u>=0} [G(u) + lam sum (u_j^2 - u_j)]`
for any `lam >= 0`, and `+lam sum u^2` eats into `G`'s own `-(ln q0/2) sum u^2` so the program
stays CONCAVE for `lam < ln q0/2`.  Select `lam` on the CERTIFICATE: the T-free tangent sum goes
the wrong way (14.17 -> 251 across the grid), because the cap is
`Gamma'^2/(2(ln q0 - 2 lam))` and the denominator collapses faster than the numerator shrinks on
the dominant row — selecting by that proxy returns `lam = 0` and discards the tightening.

**Two search bugs, both caught by invariants:**

1. **Cold start + value-based stopping.**  `pe = 2` returned 1.8466 at `T = 6` against 2.0310 at
   `T = 5` — impossible, since padding the T=5 optimum with a zero is feasible at T=6.  From
   `u = 0` every barrier is at its tightest and coordinates unlock one sweep at a time; and
   `|G_k - G_{k-1}| < tol` was satisfied while the largest coordinate gradient was still 1.12.
   Warm-start across T, and stop on the projected gradient, not the value.
2. **The lower barrier is not 0.**  A row BELOW `i` displaced by more than the gap forces
   `u_i > u_j - (b0_i - b0_j) > 0`.  The search maximised over `[0, hi]` and evaluated the
   derivative at an infeasible `0`, where `gx` returns a plausible NEGATIVE number rather than
   failing.  `gx` now refuses a non-positive argument, and `_lo_for` keeps it from having to.

With both fixed: 0 monotonicity violations, worst KKT residual 8.9e-14, and the per-program
certificate closes with slack 3.9e-12 at 1.23x the enumerated maximum (T <= 6 smoke range).

**Lean (sorry-free, `#print axioms` clean on all nine declarations in the file):**
`box_charge_eq_zero_of_nonpos` (a padded coordinate with `g <= 0` and `w = lo` is charged zero in
BOTH branches — the hypothesis is `<=`, not `<`, because a padded coordinate may have gradient
exactly zero and there the `if` takes the opposite branch), `sum_charge_extend` (its consequence),
and `sum_charge_extend_le` — the honest form, which bounds the padded block instead of deleting
it, because that is what a geometrically decaying tail permits and a vanishing one would not.

**G1 is untouched.**  It is neither proved nor refuted; what the arc is doing is removing it from
the argument, since the join needs a finite window and that follows from SEPARATE certified caps
on the two edges.

Probe: `computations/deltalambda/rev_e_infinity_xbot_relaxation_probe.py`.
Lean: `folio/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean`.

**Do not close this bean.**

> **Provenance of the section above.** It was written on 2026-09-15 and committed to
> `.beans/qou-hok7--….md` on branch `claude/xbot-upper-bound-2026-09-15` (`5df5d36f943`), i.e.
> to the bean store's **old path**. The store moved to `beans/defs/` in `58a1f3231c`
> (bean `qou-utbr`), so PR #7419 went un-mergeable on a path rename and the arc's latest state
> sat stranded on a dirty PR for a month. Re-applied verbatim here on 2026-10-10. **The
> corresponding hunk in #7419 should be DROPPED on rebase, not re-resolved** — see `qou-jz80`.


## Reorganisation 2026-10-10 — this bean is now the arc's LEDGER, not its work queue

Owner instruction: *"reorganize this Arc within the bean reorg."* This file is 1,967 lines and
~20 session appendices covering at least five separable problems; it was `parent: qou-v2om`
(EPIC: low-isotope binding defect) while a sibling arc task, `qou-0ie7`, hung directly off the
PROGRAM root `qou-10v9` — two parents at two different depths and no epic of its own.

**New shape.** `PROGRAM qou-10v9 (L2 at 1 ppQ)` → **`EPIC qou-3e6w` (REV_n asymptotics — the
upper bound on M_n)** → the six beans below. `qou-3e6w --blocking qou-v2om` records the gate
(the deuteron leg needs the q-Borel resummation of `Z_n`, which needs the `M_n` bound) as an
**edge** rather than as containment, so the dependency survives either bean being re-parented.

| bean | what it owns | status |
|---|---|---|
| `qou-as81` | **A1 (live)** — certify an UPPER bound on `Xbot` so the join needs no G1 | todo, high |
| `qou-o7c0` | **A2** — G1 itself (`Xbot(s) ≤ Xblock(s)`); open, and no enumeration can settle it | todo, low |
| `qou-fxym` | **A3 (headline)** — prove `REV_n = O(√n)`; the β-bound is the weak step | todo, high |
| `qou-0ie7` | **A4** — the dropped `Σβ = n + ℓ(ℓ−1)/2` constraint; the √n vs n^{3/4} discriminator | todo (pre-existing, re-parented) |
| `qou-zx9y` | **A5** — formalize the `Ghat_bot` frame assembly (17,534 pairs measured, 0 proved) | todo, normal |
| `qou-jz80` | **A6** — land PR #7419; the conflicts are two PATH migrations | todo, normal |

**What this bean keeps.** Everything above this line: the diagnostic history, the five corrections
of my own claims, the four refuted routes, the withdrawn verdicts, and the structural facts
(the two-environment staircase, the T-freeness of `Γ_j`, the integrality gap). It is the arc's
record and the first thing to read before picking up any child. **Nothing was deleted.**

**What it stops being.** The place to append new work. New findings go on the child bean whose
problem they bear on; only arc-wide reframings come back here.

**Do not close this bean** — its subject is an open conjecture (owner directive 2026-09-06).


## 🛑 CORRECTION 2026-10-10 — four figures in this bean are stale against the committed probe, and one is INVERTED

Re-ran `computations/deltalambda/rev_e_infinity_xbot_relaxation_probe.py` from the branch
`claude/xbot-upper-bound-2026-09-15` (#7419) on `main` + that branch. R1–R4 complete, R5
7 of 9 frames; **R5/R6 did not finish** — see the budget finding on `qou-as81`. Everything
below is from that run, not from memory.

**The three stale figures.** Each was written in the 2026-09-15 section *before* the
probe's final edit landed in `39329828903`, so they describe an earlier version of the
same script. The conclusions all survive; the numbers do not.

| this bean says | measured 2026-10-10 |
|---|---|
| R1 agrees over **36** `(pe, block)` pairs | **43** pairs (worst diff `8.65955e-25`, unchanged) |
| R2 min concavity gap **0.0057** | **0.0016707802**, at `pe = 4, T = 2`, 300 seeded triples |
| relaxed sup peaks at **`pe = 3` (2.742)**, declining 4: 2.672, 5: 2.414, 6: 1.978 | peaks at **`pe = 4` (3.0825)**; the whole profile is shifted **two frames** and the peak is **12.4 % higher** |

The `pe` profile in full, R4 at `T ≤ 12` (the recorded one was `T ≤ 6`, and that truncation
is the entire discrepancy — every frame optimises at the boundary `T = 12`, so even this is
a lower bound on the true profile):

    pe = 0  1.53539138607047383
    pe = 1  2.27576061362907053
    pe = 2  2.74201217067973621     <- the value this bean attributes to pe = 3
    pe = 3  2.99241794528878216
    pe = 4  3.08251683268933314     <- the actual peak
    pe = 5  3.06493014680884017
    pe = 6  2.98905604183360738
    pe = 7  2.87240361178974294
    pe = 8  2.69255850033782009

**The inference resting on it SURVIVES**: there is a single interior maximum and a monotone
decline to `pe = 8`, so `P_EXT_MAX = 8` is past the peak. That was the load-bearing part and
it is now measured over a wider window rather than inferred from a truncated one. Only the
peak's location and value were wrong.

**🛑 And the fourth is INVERTED, not merely stale.** This bean says, of the padded rows:

> *"I wrote the transfer first and asserted the padded rows are charged zero; they are not
> — every `Gamma_j` is strictly POSITIVE … Measured padded charge **2.4707** at `pe = 2`."*

The committed probe reports, on every one of the 7 frames that ran:

    padded charge 0.0, tail 0.0  [exactly zero (g <= 0, lo = w = 0, Gamma monotone)]

**Exactly zero, at all nine frames measured, for a reason that is not "Gamma vanishes".**
`Gamma_j` is indeed strictly positive — that part of the bean is right and is unchanged.
What makes the charge zero is that at the *fixed* ascent point the padded coordinates have
**gradient `g <= 0`** and sit at `lo = w = 0`, which is precisely the hypothesis of
`QOU.BraidKnot.SupergradientCertificate.box_charge_eq_zero_of_nonpos`.

So the 2.4707 was real but its scope was the **broken** ascent — it was a symptom of the
two search bugs (cold start with value-based stopping; the lower barrier assumed to be 0),
not a property of the frame. Once those were fixed the padded block contributes nothing.

**This inverts the epistemic status of two Lean lemmas, in the direction of strength.**
`sum_charge_extend` (padded rows charged zero ⇒ bound unchanged) is the lemma the
computation **uses**; `sum_charge_extend_le` (bound grows by at most the padded total) is a
safety net that is never exercised. The 2026-09-15 entry calls the latter *"the honest
form, which bounds the padded block instead of deleting it, because that is what a
geometrically decaying tail permits and a vanishing one would not"* — written on the
strength of the 2.4707. The tail does not merely decay; it is **exactly zero**, so the
all-T certificate is tight rather than tail-bounded. PR #7419's body carries the same
inverted claim and is corrected there.

**Nothing in the Lean changes.** All nine declarations are sorry-free and
`#print axioms`-clean, verified 2026-10-10 by `lean`-direct at the file's post-rename path
`folio/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean`
(exit 0; two-sided `autoImplicit` control; a negative control on the same file goes red;
counterexamples compiled showing both hypotheses of `box_charge_eq_zero_of_nonpos`
load-bearing). `sum_charge_extend_le` stays — a lemma that proves the weaker thing is not
wrong for being unneeded, and nothing yet proves the charge is zero at *every* admissible
ascent point rather than at the nine measured ones.

**One caveat on `SearchCoercivity`, also from that verification.** This bean and #7419 both
say the probe's `delta(m)` is *"precisely the object `SearchCoercivity.sub_le_mul_of_antitone_step`
is stated over, so the probe and the formalisation are testing the same thing."* The
mathematical claim stands, but `SupergradientCertificate.lean` **imports only Mathlib** and
names `SearchCoercivity` in prose alone — so that correspondence is a reading, not a
machine-checked fact.

**2026-11-15 update (Round 44, PR #8044, commit `704fca1db0eda5cb6a4a400ce4fd936a3248f86e`):**
Discharged the prose-only caveat above: `QOU/BraidKnot/SupergradientCertificate.lean` now imports `QOU.BraidKnot.SearchCoercivity` and proves `antitone_step_box_bound` (composing `SearchCoercivity.sub_le_mul_of_antitone_step` with `SupergradientCertificate.box_mul_sub_le`) and `sup_ghatBot_frame_certificate` (composing `SearchCoercivity.sum_ghatBot_frame_bound` and `SearchCoercivity.ghatBot` with `SupergradientCertificate.box_mul_sub_le`), sorry-free (`lean -DautoImplicit=false -s 65536` exit 0, 0 warnings, standard axioms `[propext, Classical.choice, Quot.sound]`).

**Do not close this bean.**

- **Round 89 (`https://github.com/litlfred/qou/pull/8408`, head `10a16c52a2f1ad211bfb233927428389e8e4dd3e`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
