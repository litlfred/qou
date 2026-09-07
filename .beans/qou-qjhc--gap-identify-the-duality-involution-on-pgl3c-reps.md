---
# qou-qjhc
title: 'GAP: identify the duality involution on PGL(3,C) reps with the sigma-transport on Ptolemy coordinates'
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:42:32Z
updated_at: 2026-09-07T08:43:08Z
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
