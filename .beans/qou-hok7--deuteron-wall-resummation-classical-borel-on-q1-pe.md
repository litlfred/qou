---
# qou-hok7
title: 'Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0)'
status: in-progress
type: task
priority: high
created_at: 2026-08-21T15:02:55Z
updated_at: 2026-09-13T16:40:16Z
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
status: todo
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

`content/quantum-observable-universe/lean/QOU/BraidKnot/HookSumBetaCoordinates.lean`,
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
[`QOU.BraidKnot.HookSum.betaSide_eq_hookSum`](content/quantum-observable-universe/lean/QOU/BraidKnot/HookSumBetaCoordinates.lean)
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

[`StaircaseHookMultiset.lean`](content/quantum-observable-universe/lean/QOU/BraidKnot/StaircaseHookMultiset.lean),
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
