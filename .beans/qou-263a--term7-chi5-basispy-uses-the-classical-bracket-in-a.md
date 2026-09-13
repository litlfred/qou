---
# qou-263a
title: term7_chi5_basis.py uses the CLASSICAL bracket in a q-hook-length dim_q — settle against its own consumer (NOT y_lambda_at, which is SU(2)-Markov not Plancherel)
status: completed
type: task
priority: normal
created_at: 2026-09-07T14:08:27Z
updated_at: 2026-09-07T16:00:28Z
---

SETTLED 2026-09-07 (audit sec 23): term7_chi5_basis.py uses the WRONG bracket. Tested against AGENTS.md's recorded sum_lambda w_lambda(q) at the proton q0 — symmetric gives 0.9874/0.9822/0.9822/0.9911 at n=3/4/5/6 against the register's 0.987/0.982/0.982/0.991 (four for four to recorded precision); classical gives 0.9150/0.8829/0.8683/0.8746, 7-13% low, matching none. The test HAD to be at q0: at q=1 both give exactly 1 by Burnside (verified), so the easy point discriminates nothing. BLAST RADIUS: the witness only. It emits wedderburn_weight per partition via WitnessBuilder.wrap_legacy, so those committed numbers are off by 7-13%, but its two apparent importers are COMMENT references not imports (partition_utils.py docstring; unified_low_isotope_predictor.py comment). No code takes its numbers. NOTE: unified_low_isotope_predictor.py already names term7_chi5_basis.dim_q as one of several conflicting dim_q conventions and guards against silent selection — the corpus had flagged the class; this adds the measurement. REMAINING: one-line bracket change + re-run, then check whether the chi_5 conclusion moves.

FIXED 2026-09-07 (audit sec 24). term7_chi5_basis.q_int now delegates to qou_substrate.constants.q_int_at (symmetric), so the file keeps no q-integer of its own — 366 local definitions became 365. The correction is LARGE and NON-UNIFORM: sum w_lambda goes 0.000611->0.001192 (1.951x) at A=2, 0.035772->0.046062 (1.288x) at A=3, 0.281684->0.264703 (0.940x) at A=4, 1.324423->0.907809 (0.685x) at A=5, 5.488341->2.730299 (0.497x) at A=6. The ratio crosses 1 between A=3 and A=4, so the SHAPE of the docstring's 'upper bound on |chi_5(T_w)|' across A changes, not just its scale; at A=6 the bound halves. Whether the downstream alpha_5 fit's conclusion moves is NOT assessed — no code imports these numbers, so nothing recomputes automatically. Verified: producer re-run, witness regenerated and parsing, raw-float64 ratchet 0 NEW. Bean COMPLETED: the bracket question is settled and fixed; the alpha_5 consequence is a separate question with no open conjecture attached to THIS file.
