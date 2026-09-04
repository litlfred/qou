---
# qou-mu1h
title: At A=2 the bond constants rank nn > pn > pp, but only pn binds
status: todo
type: task
created_at: 2026-09-04T02:12:28Z
updated_at: 2026-09-04T02:12:28Z
---


Split out of `qou-bygw` (2026-09-04), where it turned up while testing whether
the all-pairs closure is well defined. It is not about closures, orderings or
cumulants — it sits **upstream of all of them**, at `A = 2`, where there is one
bond, one word, and no convention to choose.

Measured exactly at 200 bits (`the_all_pairs_closure_is_not_one_link_probe`
§5, checks 12 and 13), with `alpha = m_e/(q0(q0-1)) = 4.185981 MeV`:

| system | bond | L | B_model (MeV) | reality |
|---|---|---|---|---|
| ²He | pp | 0.489899384 | 2.0507 | UNBOUND — no bound diproton |
| ²H  | pn | 0.676821592 | 2.8332 | BOUND, B = 2.22452 MeV |
| 2n  | nn | 0.907262266 | 3.7978 | UNBOUND — no bound dineutron |

**The model ranks `nn > pn > pp`. Reality binds only `pn`.** The one system
with a bound state gets the middle bond constant, and the strongest bond is
assigned to a system that does not bind at all.

The sibling's charge term does not repair it: `-(e/2) log(1-h) = +0.117267`
per unit charge, so it raises `pp` by 0.2345 and `pn` by 0.1173 and leaves
`nn` untouched — deepening the inversion. Checked.

## The honest caveat, stated first

This arc's `L` carries no spin, and the real distinction is a spin one: the
deuteron binds in the `3S1` triplet channel, and every `1S0` two-body system
— `pp`, `pn`, `nn` alike — is unbound. So a spinless bond constant cannot be
expected to separate bound from unbound here, and "the model gets ²He wrong"
is not by itself a finding.

What is a finding is the ORDER. Nothing about the absence of spin requires
the unbound `nn` system to be ranked above the bound `pn` one. The corpus's
own `wigner-np-pairing` block asserts a `pn` preference; `L_nn > L_pn` is the
opposite, in the constants every binding number is built from.

## What to actually do

- [ ] Establish whether `L_nn > L_pn` is forced by the convention or is an
      artifact of it. `L_nn = -log(z - h)` and `L_pn = -log(z + d_pn)` with
      `d_pn = -h(1 - delta/2)/2`, so `L_nn > L_pn` iff `d_pn > -h`, i.e. iff
      `delta < 2` — true for any `q` near 1. So the inversion is STRUCTURAL in
      convention D, not a numerical accident. Confirm that reading.
- [ ] Reconcile with `wigner-np-pairing` and `reeb-pn-magnitude-criticality`,
      which assert a `pn` preference. If those are right, the bond constants
      contradict them and one of the two has to give.
- [ ] Decide whether the framework wants a spin/isospin channel at all. If the
      bond constant is meant to be channel-averaged, say so and state what it
      is averaged over; the `1S0`-vs-`3S1` split is the whole content at A=2.
- [ ] Check A=2 against the `2H` chain number already in the arc: the model
      gives the deuteron 2.8332 against AME 2.22452, i.e. 1.274x. That
      overshoot and this inversion are probably the same defect seen twice.

Not claimed: that the framework is wrong. Claimed: that at the one place where
no convention, ordering, arrangement or many-body term can be blamed, the three
bond constants come out in an order the physics does not have.
