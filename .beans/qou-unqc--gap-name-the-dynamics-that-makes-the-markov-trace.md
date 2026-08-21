---
# qou-unqc
title: 'GAP: name the dynamics that makes the Markov trace a FINITE-temperature Gibbs state'
status: todo
type: task
priority: normal
created_at: 2026-08-19T17:31:15Z
updated_at: 2026-08-19T17:32:16Z
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
