---
# qou-eptr
title: 'EP/canonical decomposition as the non-pair-local extensive carrier for b_3 — aim, and the hard blocker at the light end'
status: in-progress
type: task
priority: high
created_at: 2026-09-06T10:56:11Z
updated_at: 2026-09-06T11:27:53Z
---

WHY IT IS WELL-AIMED at the ONE open piece of the binding gap
(qou-brng; audit 2026-09-05-binding-gap-groupoids-derived-categories-full-tower
§1.2 row 4: measured b_3 = +1.4262 MeV, model exactly 0):
  * EXTENSIVE by construction — a sum over cells, not a per-block lambda weight,
    so it is not blocked by exchangeDet_pow_two_le_four (intensive -/-> extensive).
  * NOT PAIR-LOCAL — a tetrahedron couples FOUR vertices, and
    CrossingModelPairLocality.b3_eq_zero_of_pairLocal says pair-locality is
    exactly what forces the model's zero. A 2-3 Pachner move is literally a
    body-order-changing move.
  * CANONICAL, so no selection-against-the-target: EP is unique, no census
    search, no fitted cutoff. Satisfies the NO-FITTING directive.
  * BOUNDED DEGREE is the regime CoordinationSaturation forces, and a
    triangulation supplies a bond graph rather than assuming one.

CANDIDATE OBSERVABLE (proposal, NOT a result): Pachner distance between the
layered triangulation derived from the braid word (2026-09-06 audit: #tetrahedra
= #letters of the LR word) and the CANONICAL EP triangulation. Both the log law
(B = E_0 x #Markov reduction steps) and the layered functor are word-length
counts; their difference is a Pachner-graph distance, which is global, not
pair-local.

HARD BLOCKER, stated up front: EP requires a COMPLETE FINITE-VOLUME HYPERBOLIC
structure. The owner's 2026-08-29 deuteron ruling puts the deuteron on the
canonical braid closure (trefoil / Hopf) with Vol = 0 — Seifert-fibred and
T^2 x I respectively, neither hyperbolic — so NO EP decomposition exists for
^2H. The route cannot reach the light end where the data is best. Whether it
reaches B_3 (hyperbolic, Vol 7.3277) and the A>=3 chain is the first thing to
measure. Do NOT read "Pachner count" as "volume": the 2026-08-29 Bloch-volume
leg proved 0 kills a VOLUME term, not a combinatorial count.

## MEASURED 2026-09-06 — the route reaches the atoms and cannot separate them

STAYS OPEN. The subject is the binding gap's irreducibly many-body term, which
is open (qou-brng). Per AGENTS.md 13a this bean is not closeable by having
measured something about it.

ep_decomposition_reachability_probe (9/9), commit 43d6ddd46:
  * 15 of 16 atoms with non-zero binding ARE hyperbolic -- the route is not
    blocked by hyperbolicity above the deuteron. My earlier framing that "the
    light end is unreachable" over-generalised from the deuteron; A>=3 is fine.
  * BUT the dictionary uses only 2 distinct manifolds, and 13 atoms share L6a4
    with binding spanning 1.667e9. An EP invariant is a function of the
    manifold, so it is constant on that class. Scope-(b).
  * deuteron excluded twice over: labelled SATELLITE, and Thurston's trichotomy
    makes a satellite complement non-hyperbolic. Agrees with the 2026-08-29
    ruling without depending on it.
  * classify_nuclear_knot factors through A (30x34 grid), discards the braid
    word, one consumer, in hecke_core_legacy.py.

canonical_cell_structure_probe (7/7):
  * the Pachner-distance candidate is 0 on 4_1 -- the derived Floyd-Hatcher
    layering IS the canonical decomposition (both 2 regular ideal tetrahedra).
  * Vol(L6a4)/V_oct = 2.0 exactly, Vol(L6a4)/V_tet = 7.2198 not an integer, so
    the principal manifold's canonical decomposition is not a triangulation.

WHAT IS STILL LIVE. The exclusion is of EP-of-the-DICTIONARY-knot. EP of the
actual per-atom braid closure is untested and needs that closure identified
first -- the same modelling decision qou-imkb records as blocked for Model B.
Attacking a better invariant of a collapsed knot cannot help.
