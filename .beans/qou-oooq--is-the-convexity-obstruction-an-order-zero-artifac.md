---
# qou-oooq
title: Is the convexity obstruction an order-zero artifact? Test the bond ordering in the phi_q tower
status: todo
type: task
created_at: 2026-09-04T06:48:02Z
updated_at: 2026-09-04T06:48:02Z
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

## Where this actually leaves us — the door is unlocked, the room is unproven

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

- [ ] **The one question that now matters:** does the framework read binding off
      a single graded piece, or off the resummation? `phi-q-resums-trace-series`
      and `vassiliev-filtration-mass-tower` should settle it, and they are the
      two blocks the formulation item above could not distinguish. If it is the
      resummation, this whole direction closes negative and `qou-qnqf` (retire
      `L`) becomes the live option.
- [ ] If a single graded piece: check whether order 5 also survives
      `qou-bygw`'s ordering ambiguity, which is untouched by any of this.
