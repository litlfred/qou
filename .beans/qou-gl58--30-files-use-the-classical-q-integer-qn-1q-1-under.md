---
# qou-gl58
title: 30 files use the CLASSICAL q-integer (q^n-1)/(q-1) under names q_int/qint — check each consumer expects it, not the symmetric one; several are in deltalambda/ (Track A)
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T14:02:18Z
updated_at: 2026-09-13T07:21:36Z
---

WORKED 2026-09-07 (audit sec 22). 0 of 363 files carry BOTH conventions — no internal inconsistency anywhere. My 'the word hecke appears' classifier is NOISE: tw_gram_determinant_probe.py is CORRECT (its q_int is the Gaussian bracket and its docstring says the conventions match QOU/Hecke/TwMul.lean, whose rule sigma_i T_v = (q-1)T_v + q T_{v s_i} is the T_w basis, where classical IS right); deltalambda_jet_filtration_magnitude_probe.py DECLARES the convention in its docstring ('Coxeter-length / coinvariant Poincare convention, NOT the balanced'). THE REAL DISCRIMINATOR IS THE BASIS: T_w / Iwahori unnormalised -> classical; normalised / quantum-dimension -> symmetric. Defensible figures: at most 28 unclassified, 1 confirmed ambiguous (helium_four_body_cluster_probe.py, sum(q**k), undeclared, Borromean cluster context), 2 confirmed fine. term7_chi5_basis.py stays OPEN: it feeds a q-hook-length dim_q, and my attempt to settle it against y_lambda_at was the WRONG TEST — y_lambda_at is the SU(2)-restricted Markov weight (zero on height>2 partitions), term7 computes Plancherel dim_q^2/[n]_q! over all partitions.

2026-09-13 — the TEN classical definitions surfaced by qou-b8vx are all resolved.
SCOPE FIRST, because these are NOT this bean's original 30: the duplication
audit's 30 are q-PARAMETRIC (2-arg) definitions; qou-b8vx's global-resolution
audit measures the q0-PINNED (1-arg) population, which that audit skips
entirely. Different sets. This append closes the 10, and this bean's own 30
are untouched.

FIVE SELF-DECLARE IN THE FUNCTION NAME — no determination needed:
   probes/c1_kernel_door_v_residual_probe.py::qint_geo
   probes/c1_kernel_level_reading_probe.py::qint_geo
   probes/derivative_only_dq_vs_c1_kernel_probe.py::qint_geo
   probes/ramified_shift_calculus_prune_probe.py::qint_geo
   substrate/lever1_qinvolution_kernel_test.py::qint_asym
"geo" IS the geometric sum 1+q+...+q^(n-1), which IS the classical bracket;
"asym" says the same thing the other way. The name states the convention.

FIVE UNDER AMBIGUOUS NAMES, each DETERMINED BY ITS OWN BASIS — all five
CORRECT AS WRITTEN. None is a defect.

1. hecke/tw_gram_square_class_crosscheck.py::q_int — CORRECT, and decisively.
   A T_w Gram file (twGram, QOU.Hecke.TwBasis), where audit sec 22 rules the
   classical bracket correct. But the file settles it without needing that
   rule: it MEASURES det = q^22 (q+1)^48 (q^2+1)^20 (q^2+q+1)^6, and the
   published form [2]^28 [3]^6 [4]^20 reconstructs that ONLY classically,
   since [4]_clas = (1+q)(1+q^2). Ran it: exit 0, "all ranks confirm both
   predictions".

2. gs_tower_jet_degree_body_order_probe.py::q_int — CORRECT. The subject is
   the GS/jet filtration's GRADED DIMENSION. A Poincare grading is exactly
   where sec 22 puts the classical bracket. Ran it: exit 0.

3. lever1_kernel_maj_involution_identification.py::qint_u — CORRECT. The
   subject is the MAJOR INDEX (maj) over involutions in S_n -- a
   Coxeter-length statistic, whose generating function is the classical
   [n]_q!. sec 22 again. Used in a q-factorial hook ratio, num/den.

4. deltalambda/binding_weight_markov_pinning_probe.py::qint — CORRECT, and
   this is the one whose NAME most suggests otherwise. "Markov" implies the
   symmetric bracket, so I expected a defect. Ran it: the Markov weights come
   from the CANONICAL MODULE ("y_lambda source: canonical-module"), and qint
   feeds only W_lambda = d_q^2/[n]!, the Schur-Weyl/Plancherel weight this
   probe EXCLUDES. Built via the hook-length formula, which is a principal
   specialization -- classical. The file's own check that W_lambda is
   conjugation-symmetric HOLDS THROUGH n=7, and that symmetry fails for a
   wrong-convention hook formula. Its own test verifies its own bracket.

5. qbeta/qbessel_mu_lambda_vs_qlommel_zeros.py::q_int — SELF-DECLARED. Its
   docstring is literally "[n]_q = (q^n - 1)/(q - 1), valid for negative n
   too" and the body implements exactly that, so no reader is misled. Used in
   the content-Casimir sum total += q_int(c)*q_int(c+1). NOT ESTABLISHED, and
   deliberately not guessed: whether classical is the RIGHT convention for a
   q-Casimir belongs to whoever owns prop:q-heat-kernel-peter-weyl. That is a
   question about the mathematics, not about whether the file says what it
   does.

SO: 0 defects in 10. The lesson for this bean's remaining 30 is the useful
part -- the discriminator that worked was never the NAME, it was:
  (a) does the file publish a figure its bracket must reproduce? (case 1)
  (b) does the file's own internal check verify the bracket? (case 4)
  (c) does the subject name a grading/statistic sec 22 already rules on? (2,3)
  (d) does the docstring declare it? (case 5 and the five _geo/_asym)
Only when none of (a)-(d) applies is a per-file basis determination actually
needed. On this sample that was ZERO of 10, which suggests the 30 may be far
cheaper than "a per-file determination, not a sweep" implies.
