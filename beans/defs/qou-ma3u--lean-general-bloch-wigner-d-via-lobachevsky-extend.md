---
# qou-ma3u
title: 'Lean: general Bloch-Wigner D via Lobachevsky — extends the unit-circle filler, reaches 5_2'
status: completed
type: task
priority: high
created_at: 2026-08-07T08:44:25Z
updated_at: 2026-08-07T09:22:56Z
---

MEASURED THIS SESSION (60 dps, mpmath):

  y^3 - 2y^2 + 3y - 1 has roots y_real = 0.4301597090019467340886 and a
  conjugate pair y_± = 0.7849201454990266329557 ± 1.307141278682045480492i.

  D(y_+) = 0.9427073627769277209212996   (Bloch-Wigner)
  Vol(5_2)/3 = 0.9427073627769277215667

  agreement to 20 digits, limited by the precision of my Vol(5_2)
  literal, NOT by the computation. So 3*D(y_+) = Vol(5_2). CONFIRMED.

WHY THIS IS NOT ALREADY IN THE CORPUS. BlochWignerMathlibFiller.lean
covers 4_1 (shape e^{i pi/3}) and Borromean (shape i) — both on the UNIT
CIRCLE, where the log|z|*arg(1-z) correction vanishes and D collapses to
Cl_2. That file names the general non-unit-circle D as an open gap.
5_2 has |y_+| = 1.52, so it is the first member needing the general D.

THE ROUTE, AND WHY IT BYPASSES THE COMPLEX-Li2 BLOCKER (qou-ph1k):
For z in the upper half plane set
    alpha = arg z, beta = arg(1/(1-z)), gamma = arg(1 - 1/z).
Then alpha + beta + gamma = pi (ideal-tetrahedron dihedral angles), and
    D(z) = Lob(alpha) + Lob(beta) + Lob(gamma),  Lob(t) = Cl_2(2t)/2.
VERIFIED at the 5_2 shape to 51 digits (residual 1.3e-51 at 50 dps).
This expresses the general D purely in Cl_2, which the corpus ALREADY
has. No complex Li_2 needed for D.

Lean-provable targets:
   - angles_sum_eq_pi for Im z > 0  (genuine theorem, real content)
   - BlochWigner_lob as the general-D definition
   - consistency: on the unit circle it reproduces Cl_2 (via the Clausen
     duplication formula; at theta = pi/3 this is 3*Cl_2(2pi/3)/2 =
     Cl_2(pi/3), NOT rfl — a real check against the two cases the corpus
     already trusts)

HONEST SCOPE. Vol(5_2) = 3*D(y_+) needs the GEOMETRIC input that the
5_2 complement's ideal triangulation is 3 tetrahedra ALL of shape y_+.
That is Thurston/SnapPea, nowhere near Mathlib, and is NOT proved here —
it enters as a definition exactly as Vol_figure_8 and Vol_Borromean
already do. The division by 3 is bookkeeping; the geometry is the
theorem. Do not dress this up as a proof of the volume.
