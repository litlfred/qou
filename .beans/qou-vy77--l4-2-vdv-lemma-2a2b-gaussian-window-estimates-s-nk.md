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
