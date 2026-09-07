---
# qou-gl58
title: 30 files use the CLASSICAL q-integer (q^n-1)/(q-1) under names q_int/qint — check each consumer expects it, not the symmetric one; several are in deltalambda/ (Track A)
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T14:02:18Z
updated_at: 2026-09-07T14:08:26Z
---

WORKED 2026-09-07 (audit sec 22). 0 of 363 files carry BOTH conventions — no internal inconsistency anywhere. My 'the word hecke appears' classifier is NOISE: tw_gram_determinant_probe.py is CORRECT (its q_int is the Gaussian bracket and its docstring says the conventions match QOU/Hecke/TwMul.lean, whose rule sigma_i T_v = (q-1)T_v + q T_{v s_i} is the T_w basis, where classical IS right); deltalambda_jet_filtration_magnitude_probe.py DECLARES the convention in its docstring ('Coxeter-length / coinvariant Poincare convention, NOT the balanced'). THE REAL DISCRIMINATOR IS THE BASIS: T_w / Iwahori unnormalised -> classical; normalised / quantum-dimension -> symmetric. Defensible figures: at most 28 unclassified, 1 confirmed ambiguous (helium_four_body_cluster_probe.py, sum(q**k), undeclared, Borromean cluster context), 2 confirmed fine. term7_chi5_basis.py stays OPEN: it feeds a q-hook-length dim_q, and my attempt to settle it against y_lambda_at was the WRONG TEST — y_lambda_at is the SU(2)-restricted Markov weight (zero on height>2 partitions), term7 computes Plancherel dim_q^2/[n]_q! over all partitions.
