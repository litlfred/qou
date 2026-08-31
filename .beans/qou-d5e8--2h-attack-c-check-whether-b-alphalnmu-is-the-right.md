---
# qou-d5e8
title: '2H ATTACK C: check whether B = -alpha*ln(mu) is the right functional at all - qou-kj4v says the degeneracy argues no flavour-only mu can be'
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-08-31T03:44:17Z
parent: qou-9ot5
---

## RESOLVED 2026-08-25 — converges on the braid word. See docs/audits/2026-08-25-deuteron-attack-c-convergence.md

Three independent lines (my Hecke-element negative, qou-kj4v's exact flavour-only
degeneracy, and the 2026-08-09 chain-walk audit's alpha-is-pinned-elsewhere argument)
all eliminate the interface scalar and alpha and land on the BRAID WORD.

Also found: B = -alpha*ln|tr_M| is POSITED. Five-path corpus-grep finds no derivation
and NOTHING in Lean; the only statement of it in content/ is a row in a NOTATION TABLE.
And the dashboard's cited definition, 'Defn: standard-part-functor.md', is DEAD - that
block defines the standard-part map and functor and contains no B_sym, no alpha and no
binding at all. Same defect class as prop:hecke-spectral-sequence.

Measured: the 2H word is 23 crossings over 6 strands, of which exactly ONE carries the
interface offset (index 2, d = -0.4997h). The other 22 cancel in the free/atom ratio.
The entire deuteron binding rides on a single sigma-type crossing.


## 2026-08-31 — the "posited" verdict is WRONG; the derivation is in docs/audits/

This bean records, from the 2026-08-25 five-path grep:

  "B = -alpha*ln|tr_M| is POSITED. Five-path corpus-grep finds no derivation and
   NOTHING in Lean; the only statement of it in content/ is a row in a NOTATION
   TABLE."

**The first clause is false.**
`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
carries a section headed, verbatim:

  ## 10a. The functional is DERIVED, not chosen -- and it is the log form

dated **17 days earlier**, sitting in `docs/audits/` -- the first path the grep
table lists, and the one it reports as "files that USE the form; none derives
it". Its argument: tr_M is multiplicative over independent subsystems
(tr_atom = tr_free * PROD mu_k, measured to 1.2e-31) and energy is extensive, so
the trace-to-energy map obeys Cauchy's f(xy) = f(x) + f(y) on (R_+, x) and the
log form is forced.

`ursell_alternation_sign_identity_probe.py` had ALREADY cited 10a as a derivation
("THE BOLTZMANN IDENTIFICATION IS DERIVED, NOT ASSUMED -- and by the corpus").
So the corpus disagreed with itself in three places.

**Still true, and unretracted:** the dead-citation finding (the dashboard cites
`standard-part-functor.md`, which defines the standard-part map and functor and
contains no binding form), and the **Lean: nothing** row -- which is now fixed.

## What 10a needed, and now has

**Lean** (sorry-free, lean-direct exit 0, no sorryAx):

  logForm_extensive               -a ln(xy) = -a ln x + -a ln y
  linearForm_extensivity_defect   a(1-xy) - [a(1-x)+a(1-y)] = -a(1-x)(1-y)
  linearForm_not_extensive        nonzero whenever x != 1 and y != 1
  linearForm_ceiling              a(t_free - t_atom) < a * t_free

The closed form is new -- 10a reports the defect only as a measured number -- and
being an identity it holds at every q with no anchor.

**10a's number is convention-C frame.** That audit predates the 2026-08-09
convention-D excision by one day. At the proton pin with mu_pp = z, mu_nn = z - h:

    convention C   defect = 1.487498   <- 10a's quoted 1.4875, to 1.6e-6
    convention D   defect = 0.966887

Conclusion unaffected in both; the figure needed the scope. Both audits are
annotated in place rather than left for a third reader to rediscover.

**Paper:** `prop:binding-functional-is-the-log` (nuclear-interactions, validate
exit 0). **Compute:** `binding_functional_extensivity_probe.py` (4/4).

**NOT closed by this.** The uniqueness step -- only continuous solutions of
Cauchy's equation are c*ln x -- is classical and is NOT formalised, so "forced"
still rests on it. And this bean's own redirect stands: the three lines still
converge on the BRAID WORD, which none of this touches.
