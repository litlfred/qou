---
# qou-w5fw
title: 'T3f: is the Ocneanu/Markov trace parameter derived or chosen?'
status: completed
type: task
priority: critical
created_at: 2026-08-04T00:07:01Z
updated_at: 2026-08-07T14:30:00Z
parent: qou-8lxd
---

SHARPEST cheap test of 'why N=2'. HOMFLY is the gl_N invariant with a = q^N; Jones is its N=2 specialisation. The Ocneanu trace on the Hecke tower carries a free parameter whose value selects N. QOU uses Jones -- so N=2 may be a CHOICE (framing/writhe normalisation) rather than forced by the Descartes condition, which constrains Aut(tau) not the trace parameter. If chosen, N=3 is available from the SAME Hecke machinery and the eightfold way follows by Schur-Weyl. If derived, flavour SU(3) really is excluded at single-fibre. Check jones-markov-trace.lean + markov-trace-factorization.lean.


---

## RESULT (2026-08-07) — the soft constraint is HARD: N = 2 is locked in

`computations/ocneanu_N_lockin_probe.py`, exact `Fraction` arithmetic, all
checks pass; witness `computations/ocneanu-N-lockin.witness.json`.

**Mechanism.** `tr_M = sum_lambda y_lambda chi_lambda` with the `chi_lambda`
Hecke characters (N-**independent**) and the weights the **principal
specialisations** `y_lambda ~ s_lambda(1, q, ..., q^{N-1})` — hence the corpus
module name `schur_principal_mpmath`. So *all* N-dependence sits in the
weights, and the q-hook-content formula makes it explicit.

**C1 — tied to the Lean, not asserted.** At `q -> 1` the principal
specialisation reproduces `RowCapObstruction.lean` exactly, for `N = 2..5`:
`s_(3) = C(N+2,3) = weylDimSym`, `s_(2,1) = N(N^2-1)/3 = weylDimMixed`,
`s_(1^3) = C(N,3) = weylDimAlt`.

**C2 — the row cap IS the weight vanishing.** `y_(1^3) = 0` at `N = 2` for
every `q` (cell content `-2` gives the factor `[N-2]_q = [0]_q = 0`), nonzero at
`N = 3`. "The row cap kills the singlet at N = 2" and "the Ocneanu weight
vanishes at N = 2" are the **same fact**, not two.

**C3 — the two traces are NOT proportional.**
`y_(2,1)/y_(3) = q [2]_q [N-1]_q / [N+2]_q`, which is `q[2][1]/[4]` at `N = 2`
and `q[2][2]/[5]` at `N = 3`. Checked at `q = 2, 3, 5/2, 11/10, 7/5`: differ
every time (e.g. at `q = 2`: `2/5` vs `18/31`).

**Verdict.** Moving to `N = 3` does not merely add the singlet channel — it
**re-weights the surviving channels relative to one another**, so `tr_M` changes
on elements the mass pipeline already evaluates. §3c's "soft constraint, not a
theorem" is now hard, for a specific checkable reason. **scope-(b)** for the
claim "the two traces differ by an overall normalisation".

**This is the GOOD outcome.** `qou-dwsh` §2c asked whether the tower can carry
both an `N = 2` Jones trace (mass) and an `N = 3` HOMFLY trace (flavour) as two
functors on one algebra. It can — the Ocneanu trace is a family, every member is
a valid Markov trace, and `HnMarkovTrace.lean` already types the parameter as a
free class **field** (only `z_pos`), so two instances are typeable today. What
this adds is that the separation is **mandatory, not optional**: the flavour
channel cannot be reached by re-tuning the mass channel, because that moves the
mass numbers.

**NOT claimed:** that `N = 2` is *derived* from the Descartes condition — it is
not, and why the mass channel is the `N = 2` one **remains open**. Nor that the
`N = 3` trace reproduces any flavour observable (the Gavrilik test TG,
untouched). Nor anything about **colour** `SU(3)` — this is the flavour channel.


---

## T3f's "Unknown" RESOLVED for the mass channel (2026-08-07)

`computations/ocneanu_parameter_is_fibre_qdim.py`, exact arithmetic, all checks
pass.

T3f's §1 table records the Ocneanu parameter's constraint as **"Unknown"**, on
the grounds that "the Ocneanu trace is defined on `H_n(q)` **abstractly** — it
does not require a specific `V` to exist." That is right for the *abstract*
trace. **The mass pipeline does not use the abstract trace.**

`feynman-eigenbasis.md` defines the mass as the **categorical trace**, summed
"over the finitely many irreducible summands of `V^{tensor n}`", and quotes the
skein relation `q m(L+) - q^{-1} m(L-) = (q^{1/2}-q^{-1/2}) m(L0)` — HOMFLY at
`a = q`, i.e. `a = q^{N-1}` with `N = 2` already baked in.

**The identity that closes it** (dual Cauchy, at the principal specialisation):

    sum_{lambda |- n}  f^lambda * s_lambda(1, q, ..., q^{N-1})  =  [N]_q^n

verified for `n = 1..5`, `N = 2..4`, five rational `q`. The right side is the
categorical trace of the identity on `V^{tensor n}` when `dim_q V = [N]_q`. So
the total Ocneanu weight at parameter `N` **is** the categorical trace of an
`N`-dimensional fibre:

> **`N` is the quantum dimension of the fibre. Choosing `N` IS choosing `V`.**

Descartes fixes `dim V = 2`, hence `N = 2`, hence `a = q` — exactly the skein
the mass block quotes. Not a knob.

## And it collapses the board

An `N = 3` flavour channel cannot be the same trace re-tuned (excluded by
`ocneanu_N_lockin_probe.py`). By this identity it must be the categorical trace
on a **genuinely 3-dimensional object** — which is precisely the missing
3-dimensional fibre `qou-8p1x` identifies as the real gap.

**So the Ocneanu route does not avoid needing a 3-dim fibre; it restates the
need for one. The two open threads are one thread.**

NOT claimed: that the Descartes condition is derived (input here); that no
other trace could serve the mass pipeline (the claim is conditional on the
corpus's own definition of mass as a categorical trace); anything about colour.
