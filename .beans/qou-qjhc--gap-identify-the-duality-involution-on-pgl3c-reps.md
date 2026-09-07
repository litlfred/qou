---
# qou-qjhc
title: 'GAP: identify the duality involution on PGL(3,C) reps with the sigma-transport on Ptolemy coordinates'
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:42:32Z
updated_at: 2026-09-07T09:08:15Z
---

OPENED 2026-09-07 on branch `claude/8-fold-way-qou-derivation-qj9uzv` (PR #6898), as the
honest exit from formalising the Ptolemy variety. `PtolemyTwist.lean` is sorry-free and
EXIT 0; this is what it deliberately does NOT prove.

## THE GAP, precisely

The Sym-squared gate for the 13 nontrivial L6a4 obstruction classes runs on two legs.

- **Absolute leg (derived, and now in Lean).** Duality on representations,
  `rho -> rho^{-T}`, inverts the obstruction cocycle: `c* = c^{-1}`, i.e.
  `[rho*] = -[rho]` in `H^2(Gamma; mu_3)`. Concrete cocycle side:
  `ObstructionClassForcesComplexType.lean` section `CocycleModel`
  (`cocycle_dual`, `cocycle_conj`, `obs_neg_of_inv`). Class side:
  `ObstructionH2.cls_eq_zero_of_cohomologous_neg`.
- **Relative leg (measured, and now in Lean).** Negating the obstruction cocycle acts on
  snappy's Ptolemy equations as `u -> u^2`, the nontrivial automorphism of `mu_3`.
  Measured on L6a4 classes 1/2/3 in
  `computations/ptolemy/ptolemy_duality_galois_check.py`; formalised as
  `PtolemyTwist.isSolution_negSystem` / `isSolution_negSystem_iff` /
  `exists_isSolution_negSystem_iff`.

**What joins them has NOT been established: that the duality involution on
representations equals the sigma-transport on Ptolemy coordinates.** Both legs conclude
"negation of the obstruction class", so the two ends meet AT THE LEVEL OF CLASSES — which
is enough for the gate as argued. But the two MAPS have not been identified, and
`PtolemyTwist.sigmaFixed_isSolution_neg` carries the identification as a hypothesis
(`forall v, sigma (x v) = x v`) rather than deriving it. Its docstring says so; do not
read it as the gate.

## WHY THIS IS NOT MERELY BOOKKEEPING

Without the identification, a self-dual representation is not known to give a
sigma-FIXED Ptolemy point. The argument as it stands routes around this: it works on the
class, where both legs deliver `-c`, and never needs the point-level statement. So the
gap does not weaken the Sym-squared verdict. What it blocks is the stronger, more useful
claim -- that `P^c` and `P^{-c}` are exchanged BY DUALITY rather than merely by SOME
automorphism that happens to negate the class.

## WHAT WOULD CLOSE IT

The Ptolemy coordinate `c_t` of a decorated representation is a determinant of lifted
decoration vectors (GGZ arXiv:1207.6711 sections 8-9, "the natural cocycle of a generic
decoration"). Under `rho -> rho^{-T}` those vectors transform by the inverse transpose,
so the determinants should transform by an explicit rule. Working that rule out and
checking it is the sigma-transport is the concrete task. It needs the decoration
machinery formalised, which `PtolemyTwist.lean` deliberately does not build -- the file
formalises the SHAPE of the equations, not the geometry that produces them.

Cheap intermediate step, worth doing first: check the claim NUMERICALLY on class 1, whose
four points are known exactly in `K = Q[T]/(f)` (see PR #6898 section A). Apply the
duality involution to the recovered representation, recompute its Ptolemy coordinates,
and compare against `sigma` applied to the original coordinates. That is a measurement,
not a proof, but it would say whether the identification is even true before anyone
spends a tranche formalising it.

## SCOPE NOTE

This is scope-(a) in the repo's refutation taxonomy on nothing at all -- it is an OPEN
item, not a negative. Nothing here is refuted; a step is unproved.


---

## UPDATE 2026-09-07 — the cheap measurement RAN, and the variety-level half is CLOSED

The bean proposed, as the cheap first step, checking the identification numerically on
class 1 before anyone formalises it. It ran, exactly rather than numerically, and it
turned out to need no representation at all.

**Two structural facts made it cheap.** `K = Q[T]/(f)`, the class-1 field, is **Galois of
degree 4 over Q** (`f` splits over `K`) and **contains `zeta_3`** (`x^2+x+1` splits over
`K`). So both primitive cube roots of unity are IN the field the point is defined over,
and the crossing can be tested by pure substitution -- hold the equations fixed, vary
which cube root is plugged in.

**Result** (`computations/ptolemy/ptolemy_galois_point_transport.py`, exact, no floats):

```
            u = u_1     u = u_2
  P^c         9/34        0/34
  P^-c        0/34        9/34
```

Perfectly antisymmetric, and the SAME nine equations fail in the mirrored cells -- the
nine carrying a nontrivial power of `u`. The point solves `P^c` at `u_2` (the root the
producer used, which is why its recorded roundtrip is clean) and `P^-c` at `u_1 = u_2^2`.

**What this closes.** The relative leg was an *equation-set* identity: `u -> u^2` maps
`P^c` to `P^-c` as polynomial sets. That does not by itself say a genuine solution
crosses -- it would not, if the point were defined over a field missing `zeta_3`. It is
not, and it does. This is `QOU.Eightfold.Ptolemy.TwistedEq.eval_negTwist` instantiated on
corpus data.

**What this does NOT close -- the bean stays OPEN.** Nothing here involves a
representation. The crossing is a fact about the VARIETY and the Galois action on its
coefficient field. That the duality involution `rho -> rho^{-T}` INDUCES this crossing is
still unestablished, and remains this bean's subject. What has changed is the prior: the
crossing that duality would have to induce is now known to exist, on real data, rather
than merely predicted.

## A BUG WORTH KEEPING, because the guard was blind in the informative direction

The first run of this measurement gave

```
            u = u_1     u = u_2
  P^c         0/34        0/34      <- WRONG
  P^-c        9/34        9/34      <- WRONG
```

and would have been reported as CONTRADICTING the equation-level measurement.

Cause: the coordinate file records the cube root of unity it used under the key `u`,
alongside the 27 Ptolemy coordinates. Substituting the dict wholesale pinned `u` to the
recorded root before the script's own `u_1`/`u_2` was applied, so both columns evaluated
at the same root.

What caught it was not a guard but an IMPOSSIBILITY: `A*u^2 = B` at two distinct cube
roots forces `A = 0`, and `A` is not `0`. A table that cannot be true is a stronger
detector than a table that merely looks surprising.

The guard that was in place asserted no symbol was left UNsubstituted. It passed --
because the bug was OVER-substitution. **A guard against a missing substitution is
structurally blind to an extra one.** Both directions are asserted now. This is the same
detector-blindness class the tranche has hit repeatedly, in a new spelling: the check was
correct about the question it asked and the question was the wrong half.
