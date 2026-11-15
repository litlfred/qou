---
# qou-mu1h
title: At A=2 the bond constants rank nn > pn > pp, but only pn binds
status: completed
type: task
priority: normal
created_at: 2026-09-04T02:12:28Z
updated_at: 2026-09-04T02:35:18Z
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

- [x] **Worse than structural — DEFINITIONAL.** The reading I wrote when opening
      this bean was close but sloppy: it attached "delta < 2" to the wrong one of
      the two inequalities. The correct statement, now proved:

          d_pn = (1/2 + delta/4) d_pp + (1/2 - delta/4) d_nn

      exactly, weights summing to 1 — the pn letter IS the weighted average of
      the pp and nn letters, which is just what "averaged interface" means in
      `atom_braid_word_3A`. The two-strand trace is affine in the offset
      (`tr_2(sigma+d) = z+d`, qou-m3sh), an affine map sends a convex
      combination to the same convex combination, and `L = -log(z+d)` is
      strictly decreasing. So

          L_pp < L_pn < L_nn   for EVERY q > 0 and EVERY delta in (0,2),

      with `L_pn < L_nn` needing delta > -2 and `L_pp < L_pn` needing delta < 2.
      At q0, delta = 0.00138, and it would have to reach 2 — at q = 3.458 — to
      break convexity. Nothing is tunable.

      **The consequence.** Exactly one of the three two-body systems binds, so a
      binding-ranking constant must put pn at an EXTREME, and a convex
      combination never is. The model cannot rank them, for any q, by
      construction rather than by misfit.

      Lean `QOU.Mass.ChainTraceFactor` (sorry-free, standard axioms, verified
      lean-direct): `dPN_eq_convex`, `convex_weights_sum`, `dPN_strict_between`,
      `factors_strict_mono`, `L_strict_mono`, `heckeH_pos`. Probe
      `the_pn_bond_is_an_average_and_cannot_be_extremal_probe` (7/7).
- [x] **Reconciled: no contradiction, and that is the difficulty.** The corpus's
      np preference is not in the bond constants. `prop:wigner-np-pairing` puts
      it in the self-conjugate (2,2) |- 4 partition as
      `Delta_(2,2) = m_e [3]_q [2]_q^2 = 6.2894 MeV` (reproduced to check the
      reading, not re-derived). That is a level-4 object and there is no (2,2)
      partition of 2, so it supplies nothing at A = 2.
      `reeb-pn-magnitude-criticality` item 4 is pn-SIGN blindness
      (`D S(a,w) D = S(a,-w)`), a different statement again. So neither block is
      contradicted — and neither rescues the two-body ordering. Nothing does.
- [ ] Decide whether the framework wants a spin/isospin channel at all. If the
      bond constant is meant to be channel-averaged, say so and state what it
      is averaged over; the `1S0`-vs-`3S1` split is the whole content at A=2.
- [x] Checked: deuteron 2.8332 vs AME 2.22452 = **1.2736x**, recorded in the
      probe alongside the ordering. The overshoot and the inversion are two
      readings of the same object — the pn letter sits at fraction 0.500344 of
      the way from nn to pp, i.e. essentially the midpoint, and the midpoint is
      both too large in magnitude and in the wrong rank.

Not claimed: that the framework is wrong. Claimed: that at the one place where
no convention, ordering, arrangement or many-body term can be blamed, the three
bond constants come out in an order the physics does not have.

## Summary of Changes

Three of the four items are closed; the fourth is a modelling decision, not a
computation, and is left for the owner.

- `the_pn_bond_is_an_average_and_cannot_be_extremal_probe` (7/7): the convex
  combination identity symbolically and at 200 bits; the forced ordering; the
  delta bound (q = 3.458 before convexity breaks); the 1.2736x deuteron
  overshoot; the Wigner reading reproduced at 6.2894 MeV.
- Lean `QOU.Mass.ChainTraceFactor` extended with the ordering theorems, all
  sorry-free on standard axioms.
- Exposition `rem:pn-bond-cannot-be-extremal`, wired into
  `sec:canonical-closure-as-link`, with the no-spin caveat stated before the
  conclusion and the non-contradiction with the Wigner channel spelled out.

**What is left, and it is a decision rather than a calculation:** whether the
framework wants a spin/isospin channel at all. The bound/unbound split at A=2
is `3S1` versus `1S0` and a spinless bond constant cannot carry it. Either the
pn interface stops being an average over crossing sign, or the bond constant
stops being what ranks binding, or the framework declares it channel-averaged
and says what over. Whoever owns convention D should pick.
