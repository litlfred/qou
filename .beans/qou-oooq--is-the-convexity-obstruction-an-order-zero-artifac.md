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

- [ ] State precisely which tower: `phi_q` resummation
      (`phi-q-resums-trace-series`) or the Vassiliev filtration
      (`vassiliev-filtration-mass-tower`). They are different gradings and the
      answer may differ.
- [ ] Compute the order-1 graded observable for the three bond types.
- [ ] Test whether `pn` can sit ABOVE the midpoint of `pp` and `nn` at any order.
      That is the whole question; everything else is scaffolding.
- [ ] If convexity survives at every order, close negative and say so loudly —
      it would upgrade the obstruction from order-zero to all-orders, which is a
      stronger result than the escape would have been.
