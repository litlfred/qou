---
# qou-263a
title: term7_chi5_basis.py uses the CLASSICAL bracket in a q-hook-length dim_q — settle against its own consumer (NOT y_lambda_at, which is SU(2)-Markov not Plancherel)
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T14:08:27Z
updated_at: 2026-09-07T14:51:32Z
---

SETTLED 2026-09-07 (audit sec 23): term7_chi5_basis.py uses the WRONG bracket. Tested against AGENTS.md's recorded sum_lambda w_lambda(q) at the proton q0 — symmetric gives 0.9874/0.9822/0.9822/0.9911 at n=3/4/5/6 against the register's 0.987/0.982/0.982/0.991 (four for four to recorded precision); classical gives 0.9150/0.8829/0.8683/0.8746, 7-13% low, matching none. The test HAD to be at q0: at q=1 both give exactly 1 by Burnside (verified), so the easy point discriminates nothing. BLAST RADIUS: the witness only. It emits wedderburn_weight per partition via WitnessBuilder.wrap_legacy, so those committed numbers are off by 7-13%, but its two apparent importers are COMMENT references not imports (partition_utils.py docstring; unified_low_isotope_predictor.py comment). No code takes its numbers. NOTE: unified_low_isotope_predictor.py already names term7_chi5_basis.dim_q as one of several conflicting dim_q conventions and guards against silent selection — the corpus had flagged the class; this adds the measurement. REMAINING: one-line bracket change + re-run, then check whether the chi_5 conclusion moves.
