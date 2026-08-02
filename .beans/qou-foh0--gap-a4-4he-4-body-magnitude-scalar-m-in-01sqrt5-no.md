---
# qou-foh0
title: 'GAP: A=4 (4He) >=4-body magnitude scalar m in (0,1/sqrt5) not fixed by a categorical driver'
status: todo
type: task
priority: normal
created_at: 2026-08-02T09:22:59Z
updated_at: 2026-08-02T09:23:17Z
---

Formalize-first session (branch claude/a4-interface-magnitude-2026-08-02) reduced the A=4 >=4-body magnitude to a SINGLE under-determined scalar m (per-pair bond magnitude) in (0,1/sqrt5).

DERIVED (sorry-free Lean, QOU/MassTheory/A4InterfaceMagnitude.lean):
- det(I+G)=(1-5m^2)(1-m^2) from the #3924 exchange spectrum {+-sqrt5,+-1}; b4=-ln det.
- b4 is SURJECTIVE onto (0,inf) in m (closed-form inverse m*(t)=sqrt((6-sqrt(16+20 e^-t))/10)) and strictly monotone => the AME target is reachable (NOT scope-(b)) but matching it is a FIT.
- naive uniform z~0.499 has 5z^2>1 => det<0, scope-(b) excluded (cited invariant = the spectrum). Same OVERSHOOT signature as the #4526 geometric W_geom.

WHAT IS OPEN: an independent categorical DRIVER that fixes m in (0,1/sqrt5) strictly below the naive z (equivalently a normalized color-tube weight W strictly below the geometric d_q^2/D^2). No driver identified. A tuned m is an anchor-inversion fit; do NOT wire.

NEXT HONEST STEP: derive m (or the intermediate W) from the s5-so3 fiber action / interface-operator spectral data WITHOUT inverting B(4He)/mu4/b4. Candidate: the interface operator I=c*sigma+d spectral eigenvalues on the (xi,nu) isotypic blocks (InterfaceOperatorBlockDiagonal.lean) may fix the per-pair coupling m from c,d (Hecke eigenvalues q,-q^-1) rather than a normalized character reweight. Coordinate with #4543 (BindingWeightMarkovPinning, distinct object).
