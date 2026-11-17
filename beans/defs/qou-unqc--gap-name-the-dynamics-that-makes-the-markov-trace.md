---
# qou-unqc
title: 'GAP: name the dynamics that makes the Markov trace a FINITE-temperature Gibbs state'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T17:31:15Z
updated_at: 2026-11-17T06:22:00Z
parent: qou-rtxm
---

Opened from the literature check on qou-y0mc.

The binding law's block asserted the trace IS a temperature state, citing
jones1987. That citation does not support it, and the claim is now scoped in
the block (this branch). What remains is the actual mathematics.

WHAT THE LIBRARY HOLDS (all five corpus-grep paths run):
  arxiv-0911.4494v2       Webster-Williamson, geometry of the Jones-Ocneanu trace
  arxiv-math-9806163v1    Orellana, weights of Markov traces at minimal idempotents
                          -- these ARE the y_lambda
  arxiv-math-0405508v1    Geck-Lambropoulou, Markov traces type B
None frames the Markov trace as a Gibbs or temperature state. Full-text search
over the whole 24.7M-char library returns Gibbs/KMS/temperature-state hits in
exactly ONE document, on superconducting black holes -- unrelated.
jones1987 is NOT ingested; it is 'Hecke algebra representations of braid groups
and link polynomials' (Annals 126), a knot-polynomial paper. jones1985 is also a
knot paper ('A polynomial invariant for knots via von Neumann algebras').

THE MATHEMATICAL GAP: a faithful normal tracial state has TRIVIAL modular
dynamics, i.e. it is KMS at beta = 0 (infinite temperature). Reading E_0 as a
FINITE temperature requires naming the dynamics whose equilibrium state this is.
The scale match beta ~ ln q identifies a parameter, not a dynamics.

This is prior to the S-vs-H question and survives its resolution: it would apply
to whichever functional won.

Not a refutation. The free-energy FORM may still be the right organising idea --
but as of now it is an analogy with a parameter match, not a derivation.


## Candidate tested and EXCLUDED: the Coxeter-length scaling (PR #6395, 2026-08-31)

This bean had run all five corpus-grep paths and the library full-text search
but had not TESTED a candidate dynamics. One is now tested.

CANDIDATE: sigma_t(T_w) = q^{i t l(w)}, l = Coxeter length (= the GS/jet-prefix
filtration degree). Obvious because the block's own scale match is beta ~ ln q,
so q^l is exactly the Gibbs weight this grading produces, and because it is the
same filtration the binding-residual work uses as its reference.

EXCLUDED. sigma_t is an algebra map only if it respects
sigma_i^2 = (q - q^-1) sigma_i + 1, whose LHS has length 2 while the RHS is a
length-1 plus a length-0 term. Rewrite-then-scale vs scale-then-rewrite gives two
conditions, both solved symbolically and both independently forcing t = 0:
  length 0:  q^(2it) = 1      => t in [0]
  length 1:  q^(2it) = q^(it) => t in [0]
Not marginal: phase gap at the proton pin is t*ln q0 = 0.1043*t rad.

Scope (b), invariant named: THE HECKE QUADRATIC RELATION IS INHOMOGENEOUS IN
COXETER LENGTH -- the same fact that makes the GS/jet structure a FILTRATION
rather than a grading (#6393 measured it from the other side).

WHAT SURVIVES: the obstruction is on H_n(q), NOT on gr H_n(q), which is
length-graded by construction and on which the scaling IS an automorphism group.
So this bean's question sharpens from 'name the dynamics' (unbounded) to
'does the Markov trace DESCEND to gr H_n(q), and is the descended state KMS at
beta = ln q there?' (bounded, yes/no). NOT answered here, and the descended state
is NOT claimed to exist -- a trace need not descend to the associated graded.

Still untouched: a Connes cocycle against a non-tracial weight; the
Radon-Nikodym derivative of the y_lambda reweighting.


### CORRECTION to the entry above (same session, PR #6395)

The 'what survives' line above -- descend to gr H_n(q) and ask whether the
descended state is KMS there -- is RETRACTED. It is answered NO.

For a state phi and a dynamics acting by a character of a grading,
sigma_t(y) = q^{i t l(y)} y, KMS_beta reads q^{-beta l(y)} phi(xy) = phi(yx). If
phi is TRACIAL the phi factors cancel, so q^{-beta l(y)} = 1 whenever
phi(xy) != 0; take y = sigma_i, x = sigma_i^-1 (so phi(1) != 0) and beta = 0.
Solved over beta > 0 as a gate: solution set EMPTY.

Holds for ANY grading, ANY algebra, on H_n(q) or gr alike. The problem was never
the grading -- it is TRACIALITY, exactly what Tomita-Takesaki says.

NET, and it is sharper than what it replaces: no character-of-a-grading flow
gives finite beta against a tracial state, so BOTH obvious escapes (a different
grading; passing to gr) are closed. The requirement is structural --
THE FINITE-TEMPERATURE STATE CANNOT BE tr_M ITSELF; IT MUST BE NON-TRACIAL.
So no amount of grading-hunting will license B_sym.

LIVE ROUTE, not attempted: phi(x) = tr_M(h x) for positive h, modular flow
sigma_t(x) = h^{it} x h^{-it}. TRAP for whoever takes it: the y_lambda weighting
does NOT supply h. A positive combination of characters is again a trace, so
tr_M = sum y_lambda chi^lambda is tracial and reweighting blocks cannot escape
the argument. The h must come from OUTSIDE THE CENTRE.

## 2026-11-17 — Markov Trace as a Finite-Temperature Central Gibbs State (`QOU.Foundations.CalibrationJMGibbsBarPoincare`, PR #8223)
- Formalized `gibbsWeightedBlockTrace` and `markov_trace_as_central_gibbs_state` in `folio/quantum-observable-universe/lean/QOU/Foundations/CalibrationJMGibbsBarPoincare.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `71263060fde5e0d5c09fecd66cf05ada5b6cd208` | PR: `https://github.com/litlfred/qou/pull/8223`
- Kept at `status: in-progress` per merge-manager protocol.
