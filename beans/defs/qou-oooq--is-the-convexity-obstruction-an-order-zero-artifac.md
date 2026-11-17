---
# qou-oooq
title: Is the convexity obstruction an order-zero artifact? Test the bond ordering in the phi_q tower
status: in-progress
pr: 8284
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:48:02Z
updated_at: 2026-10-04T15:20:59Z
parent: qou-v2om
---


Opened 2026-09-04 from the `qou-mu1h` post-mortem, on the owner's question
"B3 — are you in the full tower, not just order 0?" **Answer: no.** Every number
in that arc is a single Markov trace of a Hecke element at `q_0`. Nothing touched
the `phi_q` resummation or the Vassiliev filtration.

## Why that might matter

`the_pn_bond_is_an_average_and_cannot_be_extremal_probe` established an
obstruction with exactly two ingredients:

1. **the pn letter is a convex combination in the offset `d`** — a statement
   about the ALGEBRA ELEMENT, so it survives to every order;
2. **`L = -log(trace)` is convex** — this is specific to order zero.

Jensen on (1) + (2) gives `L_pn < (L_pp + L_nn)/2` strictly, hence the all-pairs
binding is convex in `Z`, hence its maximum sits at an endpoint and no valley of
stability is possible in any sum-over-bonds model. Ingredient (2) is the only one
that is order-zero-specific, so the tower is the sole escape route found so far
that does not require changing the letter.

It also closes a loop with the owner's serpenoid point: the graded piece is read
off correlations between order-zero observables, the cumulants `c_3..c_6` ARE
those correlations, and `qou-bygw` showed the bond model cannot define them.
The tower and the cumulant question may be one object seen twice.

## The honest prior

This is the least-evidenced option on the table and the one I was most drawn to,
which is itself a reason for suspicion. "Higher orders are not `-log` of a single
trace, so convexity need not apply" is a HOPE, not an argument. It is equally
possible that every graded piece inherits convexity from the element-level
convex combination, in which case the tower changes nothing and this bean closes
negative in a day.

- [x] **Formulated.** `q = exp(hbar)`; the `hbar`-expansion is the grading both
      the `phi_q` resummation and the Vassiliev filtration are built on, with
      `hbar -> 0` the classical point `q = 1`. The order-`k` observable is
      `[hbar^k] L_X(hbar)`. This does NOT distinguish the two gradings — that
      part of the question is still open and is now the only formulation item
      left.
- [x] Computed to order 15 for all three bond types, exactly (sympy Rational).
- [x] **YES — and the honest prior in this bean was wrong.**
      `the_convexity_obstruction_is_order_two_in_the_tower_probe` (7/7):

          Delta(hbar) = L_pn - (L_pp + L_nn)/2
                      = -2 hbar^2 + (4/3) hbar^5 - (59/45) hbar^6 - (5/9) hbar^7
                        + (149/126) hbar^8 - ...

      Orders 0, 1, 3, 4 vanish identically. **The obstruction is order two**,
      coefficient exactly `-2`. The first order putting `pn` ABOVE the midpoint
      is **five**, and orders 5, 8, 10, 12, 13 are all positive. So ingredient
      (2) genuinely fails higher up: there is no all-orders convexity theorem
      and the order-zero result cannot be promoted to one.

      Also worth recording: `delta = (4/3)hbar^3 - (4/3)hbar^4 + (5/3)hbar^5`
      is `O(hbar^3)`, so the pn letter is the EXACT midpoint through order
      `hbar^2`. The colour weighting is a third-order effect.

      Validation: summed at `hbar_0 = log(q_0) = 0.104340720`, the series gives
      `-0.0217592325` against the independently computed 200-bit
      `-0.021759233`, agreeing to 4.9e-10. Symbolic expansion on one side, exact
      Markov trace on the other.
- [x] Not applicable: convexity does NOT survive at every order, so there is no
      all-orders result to report.

## Where this actually leaves us — the door is unlocked, and it has an address

*(Superseded in part by the answered items above: the escape has a named home,
the LP/SDP per-type reading, and it is at type 4 in the corpus's `h` grading,
not order 5 in `hbar`.)*

## Original framing — the door is unlocked, the room is unproven

The escape is REAL and NUMERICALLY IRRELEVANT, and the second half matters as
much as the first. At `hbar_0`:

    leading NEG term  k=2 : -2.177e-02
    largest POS term  k=5 : +1.649e-05
    ratio                 :  7.6e-4

Any observable that RESUMS the tower is dominated by order two and inherits the
obstruction unchanged — which is exactly what the 200-bit measurement is, since
the measurement IS the resummation. The positive orders are reachable only by a
reading that takes a SINGLE graded piece as the physical observable, and nothing
in the probe argues for such a reading.

So this bean did not fail and it did not succeed. It converted "the bond model
is obstructed" into "the bond model is obstructed unless the physical observable
is a single graded piece at order >= 5", which is a much narrower and much more
falsifiable claim than we had.

- [x] **ANSWERED — both, in different places, and that is the whole answer.**
      * `phi-q-resums-trace-series`: "the `Phi_q` resummation strictly factors
        through Markov traces ... the entire tower generates from symbolic
        differentiation of the descended trace." RESUMS.
      * `vassiliev-filtration-mass-tower`, first half: "higher-order terms
        supply precision refinements, converging rapidly due to the suppression
        factor `|h|^k ~ (0.209)^k`." The mass formula RESUMS.
      * `vassiliev-filtration-mass-tower`, second half: "for the LP/SDP
        operator-selection framework, the Vassiliev filtration provides a
        canonical cost-vector basis at each type: `t_k^(type m) = c_m(b_k)`.
        This decomposes the mass-formula optimisation into a graded hierarchy of
        **independent linear programs**." SINGLE GRADED PIECE.

      So the escape is real, specific, and confined: it lives in the LP/SDP
      cost-vector channel, in machinery the corpus already has, and it is
      unavailable to the resummed mass formula — which is where every number in
      `qou-mu1h` and `qou-bygw` came from.

- [x] **Two corrections to my own first pass, both material.**

      **(a) Wrong variable.** `vassiliev-filtration-mass-tower` grades in
      `h = q - q^-1`, not `hbar = log q`. Since `h = 2 hbar + hbar^3/3 + ...`,
      a reparametrisation mixes orders — and it moves the answer. In `h` the
      obstruction is type 2 with coefficient `-1/2` and the first escape is
      **type 4** (`+1/24`), with positives at types 4, 5, 8, 9, 12, 13. My
      committed first pass said order 5, which is the `hbar` answer. "Which
      order" is not grading-independent, and quoting one while the corpus uses
      the other is how a tower result becomes unfalsifiable.

      **(b) The obstruction is created by the `-log`.** The filtration grades
      `tr_M`, not `-log tr_M`. At the TRACE level,

          (z + d_pn) - (z - h/2) = h*delta/4
                                 = h^4 (-h^4 - 4h^3 + 24h^2 - 64h + 128)/3072,

      leading behaviour `+h^4/24` — **positive**. So at the level the Vassiliev
      coefficients actually live on, `pn` sits ABOVE the midpoint from `h^4` on
      and there is no obstruction at all. Jensen on the convex `-log` is what
      flips it: the convexity gap is `O(h^2)` and the colour term is `O(h^4)`,
      so `-log` wins in the resummation and loses type by type.

- [x] **Answered, and better than expected — but at type TWO, not four.**
      `the_asymmetry_term_lives_at_vassiliev_type_two_probe` (5/5).

      **The closed form.** For the chain trace as a product of bond factors,
      verified symbolically for every `A = 3..10` and every `Z`:

          c_2 / c_0  =  (N - Z)^2 / 2  +  (5 - A)/8

      Read as `-alpha c_2/c_0` this is `-alpha(N-Z)^2/2 + alpha A/8 - 5alpha/8`:
      a **volume-like term linear in A** and an **asymmetry term quadratic in
      N-Z**, both with the SEMF's sign and functional form, out of one Vassiliev
      coefficient, with no fitting.

      **The mechanism, which explains the whole arc.** For `P = prod_i f_i` with
      all `f_i(0) = z0`,

          c_2 = z0^(A-2) sum_i f_i''  +  z0^(A-3) sum_{i<j} f_i' f_j'

      The second term is a sum over PAIRS of bonds — a convolution — hence
      quadratic in the bond counts, hence quadratic in `N - Z`. **`-log` is
      exactly the operation that destroys it**: it turns the product into a sum
      so the cross term never appears. Verified directly: the additive `L`'s
      type-2 piece is LINEAR in `Z` (all second differences vanish).

      So the standing verdict — "no valley of stability for any q" — was right
      AND is now explained. The quadratic a valley needs is a pair-convolution
      term, and the logarithm removes it. The term was never absent from the
      algebra; it was absent from the logarithm. Type 2 is also what
      `vassiliev-filtration-mass-tower` itself calls "the first mass-
      discriminating framing correction".

      **What is wrong with it, plainly.** Magnitudes: volume-like `alpha/8 =
      0.5232` MeV/nucleon against SEMF `a_V ~ 15.8`, off by 30x. The asymmetry
      is `alpha/2 = 2.093` MeV per `(N-Z)^2` with **no `1/A`**, where SEMF needs
      `-a_A(N-Z)^2/A`; it crosses SEMF's coefficient near `A ~ 11`, which is a
      crossing and not an agreement. All-pairs is worse, not better: its
      quadratic coefficient is `C(A/2,2) ~ A^2/8`. And the sign convention
      (binding as `-c_2`) is assumed, not derived — `c_2/c_0` is MINIMISED at
      `N = Z`.

      Compare `qou-xwur`, where the isospin/partition route gave only
      `-alpha log[2T+1]_q`, logarithmic in `T`, collapsing at `A = 20` for that
      reason. This is the quadratic that route could not reach.
- [ ] Check whether the type-2 result survives `qou-bygw`'s ordering ambiguity.
      The chain is safe (it is a genuine connected sum, so the factor product IS
      the trace), but the all-pairs number here uses the NAIVE factor product,
      and the true all-pairs trace is not well defined until a bond ordering is
      fixed. So the all-pairs half of this finding is provisional.
- [x] Decide the sign convention: does the framework read binding as `-c_2` or
      `+c_2`? Everything above hangs on it and nothing in the corpus settles it.
      **ANSWERED in `qou-zlra` (2026-09-12, PR #7223): the framework reads binding as a
      LOG of the trace, and for any log-type functional the question is empty — the
      pair term is absent for both signs (Lean `QOU.Mass.GradedBindingFunctionalPairTerm`).**
- [x] **The `1/A` is not the obstacle; the SCALE COUNT is.** Split to
      `qou-eqwg`. One overall `alpha` cannot fit both terms: scaling by the
      `30.2x` that fixes the volume overshoots the asymmetry by 22x at `A = 8`,
      55x at `A = 20`, 154x at `A = 56`, worsening with `A` because the model's
      asymmetry is `A`-independent. There is no `alpha` making this a SEMF.
- [ ] Sign convention split to `qou-zlra`. The probe reads binding as
      `-alpha c_2/c_0`; the corpus's `tr_M = c_0 + c_1 h + c_2 h^2 + ...` with
      higher terms "added" as refinements suggests `+`, under which symmetric
      nuclei become LEAST bound. That is a falsification, not a caveat.

## Roast of the type-two result (2026-09-04, same session that produced it)

**The `(N-Z)^2` symmetry is the criticised convention wearing a new hat.**
Measured: `z(-h) = z(h) - h` exactly, so `f_nn(h) = f_pp(-h)` — the pp and nn
factors are `h`-mirrors, which IS the `sigma <-> sigma^-1` exchange. And
`f_pn - midpoint(f_pp, f_nn) = h^4(2-h)/48`, so pn is the midpoint to third
order. Together those two facts FORCE `c_2` to be symmetric under `Z <-> N`. So
the vertex sitting at `N = Z` is not evidence for the model — it is the p/n
labelling convention plus the averaging convention of `qou-mu1h`, reappearing as
a symmetry. The same convention criticised for making pn non-extremal is what
makes the type-two term look SEMF-shaped.

**"Right functional form" is one bit.** Any symmetric quadratic in `Z` is
`(N-Z)^2` plus a constant, and `c_2` of a product of `A-1` factors is
generically quadratic in the counts. The only real content is that the vertex
sits at `N = Z`, and the previous paragraph says where that came from.

**The volume claim is weaker still.** `+A/8` is a term linear in `A`, and every
extensive quantity is linear in `A`. Calling it "the volume term with the right
sign and form" is close to vacuous.

**Pattern.** This session proposed M1 block-resolve, M4 partition channel, R1
saturation, the tower, and now type two. Each was announced with some enthusiasm
and each has been walked back or heavily caveated. Consistently finding "the
right shape" and never a number is itself a finding about the method.


## Update 2026-09-12 (PR #7223, bean `qou-zlra`) — the sign-dependent half is retracted as a statement about the framework

The corpus reads binding as a logarithm (live law `E_0 log(tr_free/tr_atom)`,
owner-ruled 2026-09-04/05; UIC's `ln|tr M_lambda|`), never as a bare Vassiliev
coefficient. `QOU.Mass.GradedBindingFunctionalPairTerm` (sorry-free): the
type-two pair convolution is in the bare product for EITHER sign and in NO
product-additive functional (log, -log, any scale). Measured on the chain
letters: second differences in Z of `[h^2] prod` = 4, of `[h^2] (+/-log)` = 0,
A = 3..12. So "read as `-alpha c_2/c_0`" describes the product, not the
framework's binding, and the valley it gives (interior max at N = Z, A = 4..12)
inverts to a hill under `+` and vanishes under the log. The closed form
`c_2/c_0 = (N-Z)^2/2 + (5-A)/8` stands exactly (reproduced A = 3..12).
Audit: `docs/audits/2026-09-12-graded-binding-sign-convention.md`.

## Progress Update (PR #8284 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/PhiQTowerConvexityAndGramRankFive.lean`, `QOU/MassTheory/ChainOrderingSpreadAndOneRowUrsellIdentity.lean`, `QOU/MassTheory/CoordinationChannelAritySeparation.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/phi_q_convexity_gram_rank_chain_ursell_arity_probe.py` and 2-commit stamped witness `computations/probes/phi-q-convexity-gram-rank-chain-ursell-arity-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8284](https://github.com/litlfred/qou/pull/8284) (`ready: d9d87101718b841adc62a2d83ad74df6ff4798e4`).
