---
# qou-wdij
title: 'REGRESSION: the Borromean atom word is non-monotone, so every monotone-transfer consumer is dead on main'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T18:12:11Z
updated_at: 2026-09-05T18:15:35Z
---

## Measured, not assumed (branch claude/atom-trace-nonmonotone-regression-2026-09-05)

**The regression.** `7db032fb48` (2026-09-05 07:53 UTC, owner ruling, bean `qou-hu1f`) made `atom_braid_word_3A` emit the INTERLEAVED Borromean intra word by default. That fix is correct — the grouped assembly was a different element of H_3(q). But interleaving sigma_0 and sigma_1 makes the generator sequence non-monotone:

    grouped    (1,0)  gens [0,0,0,0,0,0,0,1,1,1,1]      monotone
    borromean  (1,0)  gens [0,1,0,1,0,1,0,0,1,0,0]  NOT monotone

and the whole fine-Bratteli transfer (`chi_monotone_transfer.chi_all_lambda` + `reduced_block_kernel.chi_all_lambda_reduced_block`) is valid ONLY for monotone words — its own module docstring states that as its KEY FACT. Both refuse.

So `tr_m_atom_via_transfer.tr_m_atom_zn` — the canonical atom trace producer — RAISES for every atom on main: (1,0), (0,1), (1,1) alike. `mass_binding_dashboard.py` dies on its first call. Live on main for 10 h.

**The refusal is correct and stays.** Composing a non-monotone word through the per-generator alpha/beta reduction would be silently wrong. What was missing is a route for the word the producer now builds.

**The route already existed** — found by corpus-grep, not built. Bean `qou-sorn` records `pyhecke_native.chi_lambda_all_partitions_mpfr` as the general-word kernel. Re-validated here rather than cited (a bean is not a primary source):

  probes/nonmonotone_atom_trace_kernel_route_probe.py — 15/15, 50 dps, no float64.
  kernel == transfer on the GROUPED word, max|d chi| = 6.1e-50 / 5.9e-50 / 1.5e-49
  (the 50-dps serialization floor) at (1,0)/(0,1)/(1,1).

**The corrected traces are large moves, not perturbations:**

  (1,0)  tr_M  1.1457596924573008697 -> 0.62932840220292191817   rel 0.451
  (0,1)  tr_M  0.98774368811580957163 -> 0.47513351715568221251  rel 0.519
  (1,1)  tr_M  0.57517224391777187083 -> 0.15196833920423160759  rel 0.736

At n=3 the discrepancy is confined ENTIRELY to the 2-dim (2,1) block
(1.8077030637786210288 -> -0.28059335090347205473); the two 1-dim blocks (3,)
and (1,1,1) are bit-identical, since sigma_0 and sigma_1 act by the same scalar
there and cannot see the ordering. That localises the owner ruling's premise.

**Next:** route non-monotone words in `tr_m_atom_via_transfer` through the general-word kernel; keep the transfer's refusal.
