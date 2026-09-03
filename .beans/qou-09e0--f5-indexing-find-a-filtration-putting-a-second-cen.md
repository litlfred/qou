---
# qou-09e0
title: 'F5 indexing: find a filtration putting a SECOND central element in F_1, or prove none exists'
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:37:39Z
updated_at: 2026-08-26T04:08:39Z
---

## RESULT (2026-08-26): (b), over a precisely-named class

**Scope-(b) exclusion.** No filtration of `H_n(R,q)` that EITHER places the unit
in degree 0 OR is MONOMIAL in the GS normal-form basis (each `F_k` spanned by a
subset of `{T_w}`) induces the `gbDepth` grading on the centre — for any
`n >= 4`, under any shift. All three corpus readings of `J^*` are both, so each
is excluded twice over. So is the Jucys–Murphy content filtration, the most
natural fourth candidate.

**Answer to the front as posed** ('put a SECOND central element in `F_1`'):
impossible for a monomial filtration. `tau(e_lambda) != 0` puts `T_e` in the
support of EVERY central primitive idempotent, so the first monomial piece
admitting any `e_lambda` admits `1`, hence admits ALL of them. There is no
`F_1` with two central elements and not all of them.

**The quantifier is deliberate.** NOT excluded: the Wedderburn-block filtration,
which is neither monomial nor unit-in-degree-0, and which realises the
identification trivially (the sibling's caveat, preserved). Those two hypotheses
are exactly what separate the classes — verified mechanically.

**Positive characterisation the negative comes with:** any realising filtration
must place the unit in the TOP occupied degree `n - c`. So any depth statistic
with `d(empty word) = 0` is dead on arrival — not a shape a rewriting-depth
notion naturally has. That is the next agent's concrete instruction.

**Bonus, independent of the bridge:** `prf:quantum-dilogarithm-stratified` Step 1
transports an anti-diagonal annihilator duality from the WHOLE ALGEBRA to the
centre's IDEMPOTENT strata. On `Z` the pairing is diag(phi(e_lambda)) — DIAGONAL
— so there is no Poincare duality of curvature-rank strata. That site is NOT
repaired by supplying the bridge; it needs its own correction.

**Artifacts**
- probe `docs/audits/scripts/central_idempotent_unit_coefficient.py` — exact,
  QQ + F_p, n=2..5; measures `tau(e_lambda) != 0` as a rank (no idempotent
  splitting needed). No float64.
- lean `QOU/BraidKnot/GSFiltrationUnitObstruction.lean` — 9 decls, sorry-free,
  `#print axioms` clean, non-vacuity PROVED (satisfiability witness) and all 12
  hypotheses shown load-bearing by a delete-a-binder sweep.
- audit `docs/audits/2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md`

**Value caveat, stated plainly:** this supplies the INDEX, not the magnitude
(a Seiberg–Witten period). Necessary, not sufficient. Six consumer sites: the
Class A / Class B split stands; Class B's conjecture should now record the route
as EXCLUDED rather than candidate-free, and quantum-dilogarithm-stratified moves
out of both classes.
