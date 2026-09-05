---
# qou-99rx
title: Which coordination edge set has a BULK? Both derived candidates on main are affine, and an affine bond count is provably never a surface term
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:07:13Z
updated_at: 2026-09-05T17:45:37Z
---

## Resolved 2026-09-05 — every AFFINE edge set fails, for two opposite reasons; the enumeration is empirical

Lean `QOU/Mass/CoordinationBulkCriterion.lean` (sorry-free, 10 decls axiom-clean) + probe
`computations/probes/coordination_bulk_criterion_probe.py` (17/17). Audit:
`docs/audits/2026-09-05-coordination-bulk-criterion.md`.

**Part 1.** An affine bond count M(A) = alpha*A + beta gives eps*alpha + eps*beta/A exactly — the
p = 1 member — so by #6780's perNucleonExp_exponent_inj it is never a surface term, for any p != 1.
Instantiated at the chain (1, -1) and the deltahedron (3, -6). The obstruction is NOT
one-dimensionality; affineness alone suffices and both share it.

**Part 2.** HasBulk(A_surf) := A_surf -> inf AND A_surf/A -> 0. The two candidates fail one clause
each, for OPPOSITE reasons: the chain's A_surf = 2 is constant (interior, no growing surface); a
convex deltahedron has A_surf = A (growing surface, no interior at all). The satisfying case is the
sublinear power law CoordinationSurfaceDeficit assumed.

**The corpus-grep narrowed this twice and both narrowings are in the Lean.**

1. THE ENUMERATION IS EMPIRICAL, so the conclusion is scope-(a) and covers AFFINE edge sets only.
   QOU.Hecke.BoundedDegreeCoulomb keeps the corpus's own list and it is longer than two.
   Max-contact sphere packing (binding_edge_set_selection.py) is derived-in-principle, is NOT the
   deltahedron family in general, and is NOT known to be affine — out of scope. The degree-capped
   count is piecewise (2nd difference -6 at the knee). "No derived edge set has a bulk" would
   overclaim; "no affine one does" is what was proved.
2. deltahedronSurface_not_hasBulk extrapolates a family that barely exists: convex deltahedra exist
   only for A in {4..10,12} and the corpus records them only to A = 7, so an A -> infinity criterion
   is applied to the IDEALISATION, never to the data.

**Prior art that had to be cited rather than re-derived.** AffineCountMultiplicityWindow.mu is the
same affine object in Lean already (used for cumulants; its own note says it is "instantiated at
nothing"). qbeta_chain_cannot_carry_coulomb_or_surface_probe.py §2 states boundedSurface_not_hasBulk
in prose verbatim. The deltahedron half is my own #6780 prose, here promoted to a decidable Prop.
AffineCountIsNotASurfaceTerm is a ONE-INSTANCE result (both sides hardcoded defs) whose
generalisation over invariants was already made informally in every_seifert_invariant_is_affine_probe.py.
New: arbitrary (alpha, beta) against every p != 1, the deltahedron instantiation, and HasBulk itself
— which a full grep finds nowhere in any wording.

**Not writable in any scope: "the substrate cannot emit a non-affine coordination object."** No
invariant, and the corpus already carries two scope-(a) negatives pointing that way
(every_seifert_invariant_is_affine_probe.py; nf_inter_nucleon_is_a_count_not_a_graph_probe.py,
which is STRONGER on one layer — the NF encoding carries a bond count and no graph at all).

## Next (my judgement, overrule freely)

Test max-contact sphere packing against HasBulk. It is the one derived-in-principle candidate this
tranche does not cover and the only one that could still have a bulk. Cheap: a probe over the known
contact numbers. Risk: the family is case-by-case and may not be defined far enough out to test an
asymptotic criterion — the same limit that already weakens the deltahedron row.
