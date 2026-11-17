---
# qou-jplv
title: 'V3 (hard): positive-factor branch-point Riemann sum (k<=k*) -> Li2(x)-pi^2/6 for q>1 partition u:1->1/x hitting branch point x=1; adapt DilogPartAConvergence h(u) machinery (integral_zero_one_eq_LiTwo, riemann_error_bound, tail_bound) to the u>1 side with integrable log singularity'
status: in-progress
pr: 8224
updated_at: 2026-11-17T06:27:22Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:17:08Z
updated_at: 2026-10-04T15:14:18Z
parent: qou-r9ih
---


## 2026-07-25 V3 sub-obstacle breakdown (formalize-first scoping)

W-P1: `-(1-q)Sum_{k<=k*} log(1-x q^k) -> Li2(x) - pi^2/6` for the q>1 side, where
the u=q^k partition runs u: 1 -> 1/x hitting the branch point x*u=1. Decomposition
(each a distinct Lean sub-brick):

1. **Proper target integral (interior).** `int_1^b -log(1-xu)/u du = Li2(xb)-Li2(x)`
   for `b < 1/x` (so `xb<1`, no branch point). Change of variables t=xu (pattern of
   `integral_zero_one_eq_LiTwo`) + `LiTwo_eq_integral` (DilogReflection:377) +
   `integral_add_adjacent_intervals`. **Sub-obstacle:** interval-integrability of
   `-log(1-t)/t` across the removable t=0 point on [0,x] and [x,xb] — Part A's
   DilogReflection proof establishes this internally; check if it is exposed as a
   reusable `intervalIntegrable` lemma, else port it.
2. **Improper limit b -> 1/x^-.** `Li2(xb)-Li2(x) -> Li2(1)-Li2(x) = pi^2/6-Li2(x)`
   as b->1/x (i.e. xb->1^-). Needs continuity/limit of `LiTwo` at 1 from below
   (LiTwo is a tsum; `LiTwo_one` gives the value, need left-continuity or Abel).
3. **Variable-term Riemann sum.** The positive-factor sum has k*=floor(log_q(1/x))
   terms; the count jumps with q. Adapt Part A's `riemann_error_bound` telescoping
   squeeze to the q>1 "going up" partition [q^k, q^{k+1}] with widths q^k(1-q)<0
   (sign flip) and the growing integrand near 1/x. This is the genuine analytic
   core; the survey (2026-07-25) mapped the ~8 reusable Part-A lemmas with the
   flipped positivity hypothesis `b < 1/x`.
4. **Assembly -> W-P1** then **V4** (combine W-P1 + W-P2 (#4191, DONE) + #4173
   per-factor split into reg_n -> Li2(x)-pi^2/3).

Unlike W-P2 (closed via Tannery, no improper integral), V3's improper branch-point
integral + variable term count is irreducible analytic work — a focused session.

## 2026-07-25 — W-P1 fully assembled; reduced to ONE non-uniform scalar limit

All W-P1 machinery is landed sorry-free (DilogPartBBranchPointSum.lean): interior
+ improper target integral (#4210), going-up convexity/monotonicity (#4215),
per-cell squeeze (#4219), the going-up telescoping bound riemann_error_bound_up
(#4241), log-sum identity partialSum_up_eq (#4247), change of variables
integral_one_to_c_eq_LiTwo_sub (#4257), and the assembly wp1_riemann_bound +
error_up_eq (#4262).

wp1_riemann_bound sandwiches (1-q)Sum_{k<n} log(1-xq^k) against Li2(xq^n)-Li2(x)
with an explicit boundary-decomposition error. As q->1+ with xq^n->1-,
Li2(xq^n)->pi^2/6, so W-P1 -> Li2(x)-pi^2/6 IFF the single scalar limit
(q-1)*log(1-xq^n) -> 0.

RESIDUAL (do not fabricate): that scalar limit is NON-UNIFORM. With n=k*=
floor(log_q(1/x)), delta=1-xq^{k*} in (0,(q-1)/q] -- only an upper bound on delta,
never the lower bound needed. delta is governed by frac(log_q(1/x)), which
oscillates; the limit holds only under the Faddeev scaling / a Diophantine
no-resonance condition on x -- genuine analytic number theory, not a brick.
Trivial bulk sub-case: xq^n <= rho < 1 gives delta >= 1-rho and the limit for
free. Full proof needs sequence-indexed joint (n_j, q_j) scaling + t*log t -> 0.
Coordination: docs/coordination/dilog-part-b-cusp-attack.md.

## 2026-07-25 — honest bricks landed (PR #4277), general limit STILL OPEN

New module DilogPartBBranchPointLimit.lean (sorry-free, lean-direct exit 0),
registered in QOU.lean (de-orphans the whole Part B chain into CI):

- wp1_tendsto_of_boundary — full W-P1 -> pi^2/6 - Li2(x) CONDITIONAL on the named
  boundary hypothesis (q-1)*log(1-xq^n) -> 0 (§3b-cond; open input threaded as an
  explicit hypothesis, NOT fabricated). Error squeezed via wp1_riemann_bound; the
  always-vanishing bulk term (q-1)q^n log(1-x) -> 0 discharged unconditionally.
- boundary_tendsto_zero_of_bounded — the trivial bulk sub-case (xq^n <= rho < 1)
  discharges the hypothesis for free (non-vacuity witness).

DID NOT close the general non-uniform limit: still Faddeev/Diophantine, still open.
This is the honest reduction of W-P1 to exactly one named open scalar limit.

## 2026-07-25 — no-resonance capstone landed (PR #4277, commit d5537da0)

DilogPartBBranchPointLimit.lean now has 5 sorry-free theorems (lean-direct exit 0):
- wp1_bulkTerm_tendsto_zero, wp1_tendsto_of_boundary (opaque-hbdry conditional),
  boundary_tendsto_zero_of_bounded (bulk),
- boundary_tendsto_zero_of_noResonance: (q-1)log(1-xq^n) -> 0 GIVEN the geometric
  lower bound c(q-1) <= 1-xq^n (Faddeev/Diophantine no-resonance), via t log t -> 0.
- wp1_tendsto_of_noResonance: W-P1 -> pi^2/6 - Li2(x) from the two branch-point
  controls alone (automatic upper 1-xq^n <= (q-1)/q forcing xq^n->1- / Abel, +
  no-resonance lower). The opaque Tendsto hypothesis is GONE — replaced by a
  checkable INEQUALITY. The open Diophantine content is now a geometric bound.

REMAINING open (honest frontier):
1. General limit (no hypothesis): still open — Diophantine/equidistribution of
   {log_q(1/x)}; resonances where the branch point falls ~e^{-c/delta} from a node.
2. Explicit non-vacuity witness AT the branch point (turn-key recipe):
   n_j = j, target x q_j^j = 1 - 1/j  => q_j = ((1-1/j)/x)^(1/j).
   Then 1-xq^n = 1/j -> 0 (habel), and no-resonance holds with c = x/ln(1/x):
     q_j - 1 <= (1/x)^(1/j) - 1 <= (ln(1/x)/x)(1/j)  [from e^t-1 <= t e^t,
     t=ln(1/x)/j, via Real.add_one_le_exp], so c(q_j-1) <= 1/j = 1-xq^n.
   Needs only standard rpow asymptotics: a^(1/j)->1 (rpow continuity at 0) and
   (a^(1/j))^j = a (rpow_natCast/rpow_mul, a>0). Offset the index so base>1 for all j
   (N0 > 1/(1-x)). Feeds wp1_tendsto_of_boundary via habel + the noResonance term
   => a concrete scaling with W-P1 -> pi^2/6 - Li2(x). ~50-80 lines rpow bookkeeping.

## 2026-07-25 — explicit branch-point WITNESS landed (commit 2640b69f)

exists_noResonance_branchPoint_scaling: sorry-free. Constructs q_j=((1-1/m)/x)^(1/m),
n_j=m (m=j+N₀, N₀>1/(1-x)) with x q_j^n = 1-1/m → 1⁻ AND no-resonance (c=x/log(1/x)),
=> W-P1 → π²/6 - Li₂(x) along an EXPLICIT branch-point sequence. The dilog Part B
limit is now ATTAINED (not just conditional/bulk). Non-vacuity at the branch point:
CLOSED. Remaining open = the general-x UNIFORM statement only (Diophantine
equidistribution of {log_q(1/x)} over ALL scalings). 6 theorems total, all sorry-free.

## 2026-07-25 — polynomial no-resonance (Diophantine-x regime) landed (7dabfb05)

+3 theorems (9 total, all sorry-free):
- boundary_tendsto_zero_of_rate — sharp general form (gap ≥ g_j, (q-1)log g_j → 0).
- boundary_tendsto_zero_of_powerBound — c(q-1)^K ≤ 1-xq^n ⇒ term → 0 (t log t). K=2 is
  the badly-approximable regime (q_j=e^{1/j}: gap ≈ {j log(1/x)}(q-1) ≥ (c/j)(q-1)
  ≈ c(q-1)²).
- wp1_tendsto_of_powerBound — W-P1 → π²/6 - Li₂(x) from the polynomial gap bound.

OPEN FRONTIER now isolated to ONE inequality: badly-approximable x ⇒
{j·log(1/x)} ≥ c/j (three-distance / bounded continued-fraction partial quotients).
Mathlib likely lacks this; formalizing it is a separate number-theory task. Everything
in the dilog Part B W-P1 chain downstream of that inequality is now PROVED.

## 2026-07-25 — Mathlib-gap Diophantine infra LANDED (4e935b4f)

QOU/MathlibExt/QuadraticIrrationalBadlyApproximable.lean (sorry-free, mathlib-only):
  sqrt_badlyApproximable : Irrational √D → ∃ c>0, ∀ j≥1, c/j ≤ ‖j√D‖
Elementary proof (no continued fractions) via |Dj²-p²| ≥ 1. Registered in QOU.lean.

This is THE missing infra for the K=2 branch of wp1_tendsto_of_powerBound. Remaining
to make the dilog limit UNCONDITIONAL for x=e^{−√D} is the WIRING theorem (heavy
exp/floor/fract grind, ~150-250 lines):
  q_j=e^{1/j}, n_j=⌊j√D⌋ ⇒ x q_j^{n_j}=e^{−{j√D}/j};
  1−xq^n ≥ ({j√D}/j)e^{−1} ≥ (c/j²)e^{−1} ≥ (c/e³)(q_j−1)²  [K=2, needs {j√D}≥‖j√D‖≥c/j];
  hub 1−xq^n ≤ (q−1)/q  [since {j√D}≤1]; hbelow xq^n<1  [since {j√D}>0, j√D∉ℤ].
  Then wp1_tendsto_of_powerBound(K=2) ⇒ W-P1 → π²/6−Li₂(x). NOT yet wired (offered).

## 2026-07-25 — WIRED: unconditional for x=e^{−√D} (cfe45dc6)

wp1_tendsto_expNegSqrt (dilog module, sorry-free): for any irrational √D, the
maximal-cell scaling q_j=e^{1/(j+1)}, n_j=⌊(j+1)√D⌋ gives W-P1 → π²/6−Li₂(e^{−√D})
UNCONDITIONALLY. Chain: sqrt_fract_badlyApproximable ({k√D}≥c₀/k) ⇒ quadratic gap
1−xq^n ≥ (c₀/e³)(q_j−1)² ⇒ wp1_tendsto_of_powerBound(K=2). Support: two exp bounds
(one_sub_exp_neg_ge, exp_sub_one_le) + fract-form badapx lemma.

STATUS: quadratic-surd sub-class of Subgoal is CLOSED unconditionally in Lean.
The general-x UNIFORM Diophantine statement (all x, all scalings) remains open.
10 dilog theorems + 2 MathlibExt, all sorry-free.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8224)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8224` at `9725d15463b70fb5b273b6c495db79723640032c`).
- **Lean Formalization**: `QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope.branch_point_scaling_gap_and_quadratic_power_bound` (Branch-point scaling gap identity 1 - x*q^n = 1/m, linear bound, and quadratic power-law lower bound in badly-approximable regime.)
- **80-dps Witness**: `computations/probes/faddeev-halves-selection-and-q-gevrey-cauchy-envelope.witness.json` (`scriptHash: cea527e5468d`, `scriptCommitSha: 9d85aecf9640ed04a9fa33fe94c3662500eae503`).
