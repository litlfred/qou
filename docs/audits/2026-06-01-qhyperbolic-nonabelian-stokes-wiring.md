# q-Hyperbolic geometry as the implementation of the Yekutieli non-abelian Stokes step

**Branch:** `claude/qhyperbolic-stokes-wiring-2026-06-01`
**Date:** 2026-06-01
**Status:** read-only trace + design (WIP). No fit, no fabrication.

> Companion to the Geom_full derivation trace
> (`docs/audits/2026-06-01-geom-full-derivation-trace.md`, this session,
> soon on main), which found the C-action → Yekutieli non-abelian Stokes
> → Hecke link is ASSERTED (`conj:geom-yekutieli-alignment`,
> `GeomFullFunctorial.functorial := True`), not derived. A sibling agent
> runs the Reeb/Bring geometric escape test on
> `claude/reeb-bring-geometric-escape-2026-06-01`; this doc uses the
> `-qhyp` filename suffix and does not touch that branch.

## Scope of this trace

The owner's steer: the non-abelian Stokes step should MAKE USE OF the
paper's q-hyperbolic geometry (hyperbolic knot complements, q-deformed
volume / Reeb-contact structure) to (a) implement Yekutieli's
surface-Stokes → boundary-holonomy map, (b) land the holonomy in the
Hecke algebra giving tr_M, and (c) provide the per-knot-operator
dimensional bridge to MeV. The key question: does wiring Yekutieli
through q-hyperbolic geometry yield a PER-KNOT-OPERATOR quantity that
escapes the Markov-degeneracy impossibility (per-partition character
functions cannot distinguish proton from neutron), or does it too
collapse to per-partition character data?

(Findings filled in below as the trace proceeds.)
