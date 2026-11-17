---
# qou-8ms1
title: 'LEAD: m_e*Vol(6_2) gives 2H binding to 1.09% vs production B_sym''s 27.34% - knot-ID route, gated on open conj:canonical-knot-id-sdp'
status: in-progress
pr: 8251
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T19:18:14Z
updated_at: 2026-10-04T15:21:08Z
parent: qou-v2om
---

## REFUTED AS A LEAD 2026-08-25 — it is an admitted fit. Do not quote +1.09%.

Production source says it outright (mass_table_ppb.py L11-22, verified by reading):
'The atom->knot assignments for D, T, 3He were obtained by census search in
jsj_verification.py -- that IS a form of AME-driven fitting (we picked the knot whose
volume is closest to B_AME/rho).' The selection criterion IS proximity to the
experimental binding energy. The corpus was honest throughout; I did not read far
enough before calling it a lead.

Also: the SDP is a FEASIBILITY check on a presupposed element, not a selection - so
uniqueness cannot be a property of it. The closure-identifies-as-6_2 check is CIRCULAR
(the registry words ARE snappy's stored braid words for those knots, verified). Census
degeneracy: 796 manifolds closer than 6_2 for 2H, 1101 for 3H, 26671 for 3He. Two of
three assignments FAIL their own criterion (10_9 beats 8_11; 8^2_4 beats L6a4).

Scope-(b): 6_2 CANNOT be the closure of the canonical deuteron word. Component count =
cycle count of the permutation, and sigma/sigma^-1 project to the same transposition, so
every branch has 3 components (verified 32/32). 6_2 is a knot.

The one thing worth doing: derive a braid-index/crossing-number bound for K(2H) from the
substrate with NO reference to B_AME, then ask if the match is unique in that class.
0 better matches inside the tabulated census, 796 without it - all the discriminating
power is in the restriction, and nothing derives it. Registry asserts n_braid: 3, n_0: 6;
CHECK whether that is derived or handed over. See docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md

## ANSWERED 2026-08-31 — the derived restriction exists, and the class is empty (bean `t7qv`, Gap #2)

This bean's "one thing worth doing" was: *derive a braid-index/crossing-number
bound for `K(²H)` from the substrate with NO reference to `B_AME`, then ask if
the match is unique in that class.*

Done, with a different invariant than either suggested — the closure's
**component count**, which the substrate fixes outright. `σ_g` and `σ_g⁻¹` are
the same transposition, so the permutation, and hence the cycle count, is
branch- and convention-independent. Measured exact:

    c_free = 2A                                  23/23
    c_atom = 2A − #(odd-multiplicity bonds)     414/414   ⇒ A+1 at unit mult.

Corroborates `QOU.MassTheory.ClassicalTraceFloor` (`qou-zrx2`) by an independent
route. **Answer to the question posed: the match is not unique in that class —
the class is EMPTY.** 0 of 799 census manifolds at ²H and 0 of 1,102 at ³H have
both the derived arity and a volume matching as well as the named knot; 29 of
26,843 at ³He. The named knot is not in its own class either.

Extends this bean's scope-(b) result from `A = 2` to `A = 3`: `8_11` is a knot
where 4 components are required, `L6a4` has 3 where 4 are required. So `n_braid:
3, n_0: 6` in the registry is **handed over, not derived** — the substrate says
the ²H closure is a 3-component link on 6 strands, which `6_2` (a knot) is not.

Probe `computations/probes/link_assignment_census_selectivity_probe.py`;
the census-degeneracy half of it is this bean's prior work, re-measured as a
guard (A5) and cited, not claimed.


## Round 53 Formalization Update (2026-11-17)
- Formalized in `QOU.MassTheory` (`ConventionDErrorShiftAndBrunnianShortfall.lean`, `IntensiveVsExtensiveBindingAndClosureArity.lean`, `CrossingEnergyQuadraticAndBoxDiscrepancy.lean`) with 50-dps probe `computations/probes/convention_d_brunnian_intensive_arity_silver_probe.py` and witness on PR #8251.
