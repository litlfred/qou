---
# qou-rj44
title: 'Retype BlochWignerD to UpperHalfPlane: the alg-geom class shape parameter was real, forcing volume=0'
status: completed
type: task
priority: normal
created_at: 2026-09-04T09:05:59Z
updated_at: 2026-09-04T09:06:45Z
---

DONE 2026-09-04, branch claude/lean-prove-assertions-2026-09-04.

WHAT WAS WRONG. content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.lean declared `opaque BlochWignerD : R -> R` and the class field `pole_cusp_matched : volume = BlochWignerD x`, applying Bloch-Wigner to the q-Pochhammer STATE variable x on the stated grounds that the narrative's matching map z(x) had been 'composed away'.

WHY THAT IS NOT A SIMPLIFICATION. Bloch-Wigner is conj-antisymmetric, so it vanishes identically on R. The corpus proves this TWICE and the second one is unconditional: QOU.Knot.FlatTet.BlochWigner_lob_ofReal (FlatTetrahedra.lean:76) gives BlochWigner_lob (x : C) = 0 for every real x with NO hypothesis, against the concrete BlochWigner_lob : C -> R (BlochWignerLobachevsky.lean:478, a real definition, not opaque). So wiring the two would have collapsed the conjecture to volume = 0 outright. It was latent only because neither file imported the other.

THE FIX. opaque BlochWignerD : UpperHalfPlane -> R; the class gained a field shape : H; pole_cusp_matched now reads volume = BlochWignerD shape. This UN-COMPOSES z(x): an instance must exhibit the matching map's value and cannot exhibit a flat one. x : R keeps its role in vc_asymptotic. Three theorems record why (eq_zero_of_conjAntisymm_ofReal, flat_shape_has_no_volume, shape_ne_real) plus shape_ne_zero_ne_one bridging to the sibling's GeometricShape.

VERIFIED. lean-direct exit 0; 11 declarations, all [propext, Classical.choice, Quot.sound]. Mathlib's UpperHalfPlane olean was absent from the restored cache and was compiled into it (16 s, lean-direct, no lake).

BLAST RADIUS NIL. No instance of the class exists anywhere; nothing outside the file consumes BlochWignerD. Only the .md sibling's Discussion (updated) and a docstring mention at shared-denominator-cusp-holonomy.lean:17 that explicitly notes there is no type-level binder.

TWO SIDE FINDINGS. (1) The .md ALREADY stated item 2 as D(z(x)) with 'z(x) is the shape parameter' (line 39) - so this was a narrative-vs-Lean divergence, not a shared simplification. (2) This is the third site of one defect class: QOU/Machinery/QDilogarithm.lean:78 (blochWignerD := 0, bean qou-ir1l, fixed 2026-08-07), shared-denominator-cusp-holonomy.lean (bean qou-z9ws, fixed 2026-08-31), and this one.
