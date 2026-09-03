---
# qou-1xne
title: Is w_3 closeable? four routes measured — none closes; it is a rank-2 boundary condition
status: completed
type: task
priority: normal
created_at: 2026-08-29T07:00:24Z
updated_at: 2026-08-29T07:01:08Z
---

## Result 2026-08-29 — NOT CLOSEABLE by anything now in the corpus

Probe: computations/w3_closeability_audit.py (exit 0)
Audit: docs/audits/2026-08-29-w3-closeability.md
PR: #5967 (claude/w3-closeability-2026-08-29)
Parent finding verified, not re-derived: qou-hh9q / binding_n3_forcing_probe.py
still reproduces exit 0 on main -- A=3 defines the n=3 term.

VERDICT: w_3 is not a gap awaiting a longer computation. It is a REQUIRED
BOUNDARY CONDITION of a rank-2 problem, and the corpus supplies exactly one
(n=2). Already proved on main and scope-(b) with its invariant cited:
BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier (sorry-free) --
non-integral Newton slope 1/2, so no scalar R(q,x) acts on the carrier at any
depth; a rank-2 recursion needs TWO base cases. The conjecture's own stated
mechanism cannot produce the weights. Companion kernel_coeff_existsUnique:
an unconstrained ansatz reparametrises the unknown rather than removing it.

Four further routes measured, none closes:

R1 a_D^(3) is DETERMINED (S(3)/3 = 1.3369656 at the proton pin; closed form in
   q and n, no anchor input, no knot argument; q=1 limit is I(n)/n, the corpus's
   classical binding period with Lean involutionNumber_pos). It is a DIFFERENT
   object from w_3. The weightless reading B_n = m_e*a_D^(n) -- which is what
   the conjecture DISPLAYS -- is refuted at the deuteron by -77.03%. So
   "w_3 free" does NOT restate "a_D^(3) unknown"; counting them as one gap
   undercounts the open work by one.

R2 prop:sl2-prolongation-recurrence is CIRCULAR at n=3. Its
   tau = (a_D^(2)+a_D^(4))/a_D^(3) is the n=2 instance of its own recurrence
   rearranged, so it consumes a_D^(3). Measured: the a_D^(4) residual is 0 to
   full precision for EVERY substituted a_D^(3), including 0.001. Independently
   the depth-2 geometric form misses the closed form by -14.31% at n=6 and
   -52.21% at n=8. Spun out as qou-vkm6 (the block does not record this).

R3 NO THIRD ANCHOR. Full tower: each isotope supplies one datum and one new
   unknown w_A, so predictions = 0 at every order -- saturated, never
   predictive -- while the deficit against the two stated anchors grows with A.
   Few-body truncation: +1 equation, +2 unknowns per isotope, strictly worse;
   helps only with a DERIVED M_n(K), blocked upstream by the undetermined
   deuteron knot (2026-08-21 adjudication). A=3 mirror pair: one equation plus
   a K-independence TEST; under K-independence the model splitting is
   identically 0, so the splitting measures the Coulomb model, not w_3.

R4 the only reading that would supply a third equation -- the magic form as
   the n=4 TERM rather than the 4He total -- determines w_3 without touching
   A=3, and gives w_3 = -6.576 (positivity NO, monotone NO), predicting
   B(3H) = -1.660 MeV, i.e. UNBOUND TRITIUM. Reduces to
   B_total(4He) - B_magic, so it is independent of the w_2 convention: forced
   by B_magic exceeding the measured total by 5.87%. Scope (a) against the
   READING, not the magic formula, whose block reads it as the total.

WHAT WOULD CLOSE IT (a new input, not a rearrangement):
 (i)   a per-knot period a_D^(n)(K) -- no such object exists; all ten a_D
       definitions in computations/ take body order alone.
 (ii)  a derived multiplicity M_n(K) -- blocked on the deuteron knot.
 (iii) the ramified double cover named in the exclusion's own scope note --
       qou-v8qx, the one route nothing measured here excludes.

A w_3 obtained by inverting AME at A=3 is a FIT, must be labelled one, and may
not be wired to production as canonical. No seventh ansatz proposed.

SIDE FINDING: PR #5961 (QOU.Knot.BodyOrderExpansion / esymm_eq_compl_sum) is
OPEN, not on main -- neither symbol exists in the tree at main@e9efee94b7. Read
from the PR head, its content is the elementary-symmetric expansion of the bond
product: combinatorial structure only, no magnitude and no weight, so it does
NOT bear on w_3.
