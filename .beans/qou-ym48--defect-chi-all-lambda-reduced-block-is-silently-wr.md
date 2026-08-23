---
# qou-ym48
title: 'DEFECT: chi_all_lambda_reduced_block is silently WRONG for n not divisible by 3 (chi != dim, tr_M(1)=0)'
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:57:24Z
updated_at: 2026-08-23T13:58:09Z
---

computations/reduced_block_kernel.py::chi_all_lambda_reduced_block returns SILENTLY WRONG results when n is not divisible by 3. It composes cached H_3 blocks (that is the whole point of the optimisation) and its loop is hard-wired to nucleon-sized groups of 3 generators; a caller passing any other n gets zeros with NO error.

MEASURED on the EMPTY word, where chi^lambda must equal dim lambda = f^lambda:

   n     reduced kernel                 general chi_all_lambda
   3     tr(1)=1.0   chi==dim TRUE      tr(1)=1.0  chi==dim TRUE
   4     tr(1)=0.0   chi==dim FALSE     tr(1)=1.0  chi==dim TRUE
   5     tr(1)=0.0   chi==dim FALSE     tr(1)=1.0  chi==dim TRUE
   6     tr(1)=1.0   chi==dim TRUE      tr(1)=1.0  chi==dim TRUE

tr_M(1) = Sum_lambda y_lambda * dim lambda = 1 by the y-normalisation (Sum y f = 1), at EVERY n. The reduced kernel gives 0 at n = 2,4,5,7,8 -- i.e. it is non-degenerate only at n divisible by 3. chi_monotone_transfer.chi_all_lambda is correct at every n.

PRODUCTION IS NOT AFFECTED: tr_m_atom_via_transfer only ever calls it at n = 3(Z+N), always divisible by 3. This is a TRAP, not a live wrong number.

BUT IT NEARLY COST A FALSE RETRACTION. Testing the qou-g8i1 no-spectator Markov step needs H_4 (W_< on gens 0,1 lives in H_3; sigma_2 is the last generator of H_4). Through the reduced kernel that came back 0/0 and read as "the literal Markov instance is degenerate here", which would have retracted a correct claim. Through the general kernel it is EXACT: tr(W_< sigma_2)_{H4} / tr(W_<)_{H3} = 0.612688037146465252 = z. Section 4g stands.

FIX OPTIONS: (a) raise on n % 3 != 0 -- cheapest, honest, and matches the intended contract; (b) fall back to chi_all_lambda for such n; (c) generalise the block composition. (a) or (b). Do NOT leave it returning zeros.

Found 2026-08-19 while working qou-g8i1.
