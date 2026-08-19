---
# qou-e5jf
title: 'BLOCKING: three inconsistent deuteron knot assignments block any Bloch-group magnitude'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:41:44Z
updated_at: 2026-08-16T13:42:16Z
---

The corpus carries three live, inconsistent deuteron knot assignments:
  braid-closure (canonical for Delta_lambda): trefoil T(2,3), Vol = 0, 2 FLAT tetrahedra, shapes {1/2, 2}
      -- computations/deltalambda/deuteron-octahedral-gluing.witness.json (SnapPy 3.3.2, 70 dps)
  census-assigned: 6_2, Vol = 4.40083251612304610144
      -- knot_volumes.py:139, binding_manybody_series.py:11, 4 probes
  linear-chain: Hopf L2a1, Vol = 0
      -- volume-binding-four-point.witness.json:87, which also flags that the +0.2% deuteron
         match came from substituting Vol(B_3) for Vol(Hopf), an unjustified substitution

The candidate Bloch term differs by the WHOLE of Vol(6_2) between frames. You cannot derive a
knot invariant while the knot is undetermined. This is upstream of every flattening question
and is where the extended-Bloch route actually stops.

The owner ruling 'assume hyperbolicity is granted' (qou-985x) does not resolve this: it is a
question about WHICH manifold, not whether it is hyperbolic, and the committed SnapPy data for
the canonical braid closure says flat with Vol = 0.

Related proved result (PR #5242, QOU.MassTheory.BlochVolumeLeg): the volume leg is identically
zero on any real-shape triangulation at ANY tetrahedron count, flattening-independent. So the
trefoil frame gives 0 no matter how the triangulation is refined.
