---
# qou-hok7
title: 'Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0)'
status: in-progress
type: task
priority: high
created_at: 2026-08-21T15:02:55Z
updated_at: 2026-09-07T12:45:17Z
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
