---
# qou-e5jf
title: 'BLOCKING: three inconsistent deuteron knot assignments block any Bloch-group magnitude'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:41:44Z
updated_at: 2026-08-21T15:41:59Z
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



FORMALIZE-FIRST PRUNE LANDED (2026-08-21, PR #5363, commit a32906af4a).

The scope-(b) arity exclusion in the adjudication (§2/§3 Ground 1) no longer rests on enumerating the 32 resolutions of the mass word. It is now a sorry-free theorem:

  content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ClosureComponentsSignInvariant.lean

Content: wordPerm_eq_of_indices_eq -- the permutation a signed braid word induces depends only on its index sequence, never on the crossing signs. Specialises through resolve (position-indexed, so distinct averaged crossings may resolve differently) to closureComponents_resolve, and to the exclusion form closureComponents_ne_of_perm_ne. Braid words are List (i x Bool), which is QOU.Archimedean.BraidWord n definitionally.

This is §5 step 2's formalize-first note discharged: the knot-valued hypothesis class is pruned by theorem before any census search, and the exclusion holds without fixing a crossing convention first.

NOT proved (cited to Birman §1.2/§2.2, stated in the docstring): that wordPerm adjacentPerm is the image under B_n -> S_n, and that closure components are its orbits. Deriving those needs a formalisation of B_n with its relations, which the file does not build.

Verified: lean-direct exit 0 against the main checkout's oleans (read-only LEAN_PATH, no lake build); #print axioms clean on all 11 declarations (propext / Classical.choice / Quot.sound, no sorryAx); zero sorry / native_decide / axiom; check-sidecars clean.

The UNDETERMINED verdict is unchanged. What changed is that one of its two structural legs is now machine-checked.
