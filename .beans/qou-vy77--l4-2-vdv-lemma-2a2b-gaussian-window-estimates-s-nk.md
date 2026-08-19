---
# qou-vy77
title: 'L4-2: vdV Lemma 2a/2b — Gaussian window estimates S_nk/S~N'
status: todo
type: task
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-08-11T00:36:11Z
---

RE-SCOPED 2026-08-19 -- BUILD becomes ASSEMBLE.  Do NOT write a Gaussian tail
or window-sum bound; main already carries generic ones in QOU/MathlibExt/:
  GaussianWindowSum   sum_Icc_tilted_eq, abs_sum_Icc_tilted_sub_le
  GaussianTailBound   tsum_gaussian_sub_sum_Icc_le, hasSum_int_geometric
  GaussianSumBound    sum_exp_neg_mul_sq_le, integral_exp_neg_mul_sq_le,
                      antitoneOn_exp_neg_mul_sq, sum_exp_neg_mul_mul_pred_le
  GaussianTiltedSum / GaussianThetaBound / GaussianThetaSum / GaussianShearIntegral
All generic (MathlibExt namespace), so they apply to the Whitehead Gaussian --
the Kashaev lane that built them is 4_1, but these lemmas are not.
Audit: docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md

🛑 SPEC CORRECTION 2026-08-19 -- FORMALIZE THE SIGNED FORM, NOT THE PUBLISHED ONE.

vdV's Lemma 2a as PUBLISHED is wrong, and transcribing it faithfully -- which is
what this repo's anchor-verified transcription discipline would otherwise tell
you to do -- would formalize the error.  He defines n' = |n - floor(N/2)| and
k' = |k - floor(N/4)| as DISTANCES and states

    S_{n,k} * S~_N^{-1} = exp(-(pi/N)(n'^2 + 2 n' k' + 2 k'^2)) + O(N^{3 delta - 2}).

The Taylor expansion it comes from is SIGNED:

    f(pi/2 + x, pi/4 + y) = f(pi/2, pi/4) - (x^2 + 2 x y + 2 y^2) + O(|x|^3+|y|^3)

and the cross term 2xy is NEGATIVE on the opposite-sign corner.  Measured
directly on log(S_{n,k}/S~_N) (docs/audits/2026-08-08-vdv-constant-closed-form-
and-the-open-bridge.md, Sec 'Three slips'):

     n'    k'        true    signed     absolute
     10   -10   -0.070920  -0.078540   -0.392699
     20   -20   -0.300637  -0.314159   -1.570796
     30   -15   -0.353311  -0.353429   -1.767146
     15   -30   -0.857281  -0.883573   -2.297290
     40   -25   -0.660549  -0.667588   -3.809181

The signed form tracks; the absolute form is off by factors of 3 to 5.  So the
Lean statement must keep the SIGNS -- x = n - floor(N/2), y = k - floor(N/4) as
signed offsets, never absolute values.

RELATED SLIP, same source, also to carry: the Gaussian coefficient is
A = (c+d) - (4a-c+d) i, NOT (c+d) - (4a+c-d) i.  Six of twenty swept chains
discriminate and all six land on 4a-c+d.

Consequence already banked: with signs restored the Step-4 integral runs over
all of R^{n+1} and is elementary for every n -- no orthant, no erfc (see
qou-9r2q, and QOU.MathlibExt.integral_vdv_step4, sorry-free).

