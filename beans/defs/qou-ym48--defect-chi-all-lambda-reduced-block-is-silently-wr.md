---
# qou-ym48
title: 'DEFECT: chi_all_lambda_reduced_block is silently WRONG for n not divisible by 3 (chi != dim, tr_M(1)=0)'
status: completed
type: task
priority: normal
created_at: 2026-08-23T13:57:24Z
updated_at: 2026-08-23T15:33:08Z
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

FIXED 2026-08-19. chi_all_lambda_reduced_block now DELEGATES to chi_monotone_transfer.chi_all_lambda when n % 3 != 0, instead of silently returning zeros.

ROOT CAUSE, exactly: the composition covers gens 0,1 for nucleon 0 and then 3k-1, 3k, 3k+1 for k in 1..A-1 with A = n//3 -- that is 2 + 3(A-1) generators, which equals n-1 ONLY when n == 3A. For any other n the trailing generators are skipped and the sweep ends holding shapes of size 3*(n//3) instead of n, so every lambda |- n lookup by the caller misses and the whole result reads as zero. No exception, no warning.

Chose delegation over raising: a caller passing such an n is currently getting zeros, i.e. already broken, so delegation strictly improves it and adds no new failure mode. The fast path at n = 3A is untouched.

VERIFIED:
 * reduced == general EXACTLY (max |diff| = 0.0) for every n in 2..9 on the empty word
 * tr_M(1) = 1 at every n now (was 0 at n = 2,4,5,7,8); residual 1e-30 is y_lambda carried at 30 digits, not a kernel error -- my first check used a 1e-40 threshold and wrongly flagged it
 * module self-test at 6Li (n=18): reduced vs original max |diff| = 4.1e-48, timings unchanged (warm 0.12 s)
 * production values BIT-IDENTICAL: deuteron atom at q0 and at 1/q0 to 30 digits, 6Li atom at q0 to 20 digits

Docstring now carries the root cause, the measured before-table, and why the silence mattered (it turned a correct H_4 Markov-step check into an apparent 0/0 degeneracy).
