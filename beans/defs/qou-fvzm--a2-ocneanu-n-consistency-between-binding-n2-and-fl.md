---
# qou-fvzm
title: 'A2: Ocneanu N consistency between binding (N=2) and flavor (N=3)'
status: completed
type: task
priority: normal
created_at: 2026-08-07T08:37:46Z
updated_at: 2026-08-07T11:52:09Z
parent: qou-kemt
---

T3f audit 2026-08-04 rules a=q^(N-1) GENUINELY OPEN; binding runs Jones N=2, flavor chapter argues N=3. **ROAST (near-fatal):** the same audit 3a says if Descartes forces N=2 then the eightfold way CANNOT use N=3 from the same Hecke machinery -- and that IS the chapter's current position. Worse: the audit states changing N changes ALL mass predictions. The framework's SUCCESSES (m_mu/m_e, m_p) live at N=2. Any N=3 probe must first demonstrate it does not destroy them. Treat as regression risk, not upside.

CLOSED 2026-08-07 as PREMISE-REFUTED by PR #4640. The memo claimed the eightfold chapter independently argues N=3. #4640 shows that was a conflation of two different A_2's: the Coxeter A_2 of H_3(q) (permutes STRANDS, true by construction since B_n has type A_{n-1}) vs A_2 = sl_3 (flavour SU(3), acts on the FIBRE V, needs dim V = N = 3). Setting n=3 does not make N=3, and the framework gives N=2. Worse, #4640 section 4 PROVES sorry-free, scope-(b) with the Schur-Weyl row cap cited, that N=2 CANNOT host the decomposition: dim V_(1^3) = C(N,3) vanishes iff N<3; at N=2, 8=4+4+0, no singlet, no eta-prime, and no choice of q restores it. So there is no flavor N=3 to import into binding. The N=2 vs N=3 tension is a PROVED OPEN CONTRADICTION (bean qou-8pl3 'N=3 routes'), not a lever available to this arc.

REOPENED 2026-08-07 IN CORRECTED FORM. My 'premise-refuted' closure was right that there is no flavour N=3 to import, but the conclusion was too strong. The Schur-Weyl ROW CAP gives dim V_lambda = 0 whenever l(lambda) > N. The framework has dim V = 2 (Descartes), so N=2 FORCES the two-row restriction: N=2 <=> l(lambda)<=2 <=> pairwise-only <=> the proved rho_A <= C(A,2) cap. Read #4640's sorry-free weyl_dim_alt_eq_zero_iff (dim V_(1^3) = C(N,3) vanishes iff N<3) for BINDING rather than flavour: three-body channels exist iff N>=3. So the super-pairwise term REQUIRES N>=3 for ROW-CAP reasons, not flavour reasons. The octet's N=3 requirement and three-body binding's N>=3 requirement are THE SAME row-cap condition, reached from two independent directions -- this is the eightfold-way hint the owner originally asked for. qou-8pl3 ('N=3 routes') is therefore load-bearing for binding, not only for flavour.

CLOSED FOR GOOD 2026-08-07 by main commit f92a8b15 'N = 2 is LOCKED IN for the mass pipeline'. T3f's 'GENUINELY OPEN' is now scope-(b) resolved. Mechanism: tr_M = sum_lambda y_lambda chi_lambda with chi_lambda Hecke characters (N-INDEPENDENT), so all N-dependence sits in the weights, which are principal specialisations y_lambda ~ s_lambda(1,q,...,q^{N-1}). The row cap IS the weight vanishing -- y_(1^3) = 0 at N=2 because the content-(-2) cell contributes [N-2]_q = [0]_q = 0 -- so 'row cap kills the singlet' and 'Ocneanu weight vanishes' are ONE fact, the q->1 shadow of RowCapObstruction.lean weylDimAlt. And the traces are NOT proportional: y_(2,1)/y_(3) = q[2]_q[N-1]_q/[N+2]_q differs at every q tested, so moving to N=3 RE-WEIGHTS surviving channels and changes tr_M on elements the mass pipeline already evaluates.\n\nSO: my reopened form ('N>=3 is necessary for the >=3-body term, making the N=3-route load-bearing for binding') is closed -- the route is unavailable, not merely hard.\n\nSHARPER CONCLUSION from combining with this branch's l1 ceiling: the l1 ceiling (0.36-0.59 of target, all four isotopes) forecloses every REWEIGHTING of the N=2 partition sum, and N=2-locked forecloses escaping to larger N for the missing l(lambda)>=3 channels. Together: THE MISSING ADDITIVE TERM IS NOT A HECKE-TRACE OBJECT AT ALL. That is stronger than either result alone and explains why all six ansatze failed -- every one looked for the magnitude inside sum_lambda y_lambda chi^lambda Delta_lambda.\n\nSurviving candidates are the ones that were never trace objects: the extended-Bloch/geometric route (qou-985x) and the untested atomic-braid -> nucleus map (qou-imcd).


---

SCOPING NOTE ADDED 2026-09-03 (bean `qou-bmz8`) — THE VERDICT SURVIVES, THE
STATED GROUND DOES NOT COVER IT. This bean's closing line, "THE MISSING ADDITIVE
TERM IS NOT A HECKE-TRACE OBJECT AT ALL", is quoted by later sessions as settled;
it is added to rather than altered here, and the conclusion is NOT withdrawn.

The two inputs exclude (i) every REWEIGHTING of the partition sum, via the ell-1
ceiling, and (ii) escape to larger N. But the ceiling evaluates
`chi^lambda(beta_atom)` at ONE element and ranges over coefficients at that fixed
point; it never varies the point. `tr_M(x . w)` is a Markov trace for every `w`,
hence a Hecke-trace object inside the N = 2 carrier and not row-capped, and a
non-central `w` is neither a reweighting nor a larger-N escape. Measured: for
central `z`, Schur gives `chi^lambda(beta.z) = c_lambda . chi^lambda(beta)` to
3.6e-49, so the ceiling bounds EXACTLY the centre; the freedom it never touched
is precisely the non-central part, whose chi-vectors span the full partition
space (rank 11 at the deuteron).

**That gap has since been measured, and it is empty where it is reachable.**
Almost all non-central freedom is INERT on `Delta_bind` — `sigma_1`, the
Jucys-Murphy `L_2` and both Lagrange projectors of `sigma_1` each rescale by an
atom-independent constant, so all four share the control's spread. The mechanism
narrows the live part to the INTERFACE subalgebra, and the interface elements
(crossing, inverse, the corpus's averaged crossing, single-bond) were tested at
FOUR atoms with one shared constant: no candidate reaches 5 % spread and none
beats the control by 2x. Validation reproduced every committed `tr_M_at_q0` to
8.0e-51.

So the correction is to this bean's ARGUMENT, not its VERDICT — and the verdict
now rests on a measurement of the region the stated argument had left open,
rather than on the ell-1 ceiling alone. Not proved in general: a small,
fixed-in-advance candidate set does not exhaust the non-central part. What has
been removed is the obvious place to look.
