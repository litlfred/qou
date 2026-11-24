---
# qou-9ki6
title: 'GAP: b_over_a_evaluator crashes after refresh (mpf.__format__, held with the assertion failures)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T20:49:38Z
updated_at: 2026-11-24T21:16:57Z
---

Found by the 2026-11-24 paper-compute refresh (PR #9395, branch `claude/compute-refresh-2026-11-24`, main `dd5f163edbd`). `computations/b-over-a.witness.json` was self-stale. The current producer `computations/b_over_a_evaluator.py` writes its witness ("0 assertions, all passed") and then **crashes**:

```
File "computations/b_over_a_evaluator.py", line 395, in main
    print(f"E_0 = {E_0_MEV:.6f} MeV")
TypeError: unsupported format string passed to mpf.__format__
```

The cause is mpmath 1.3.0, the version pinned by sympy 1.14 and recorded by the 80-dps swarm witnesses, which does not accept a format spec on `mpf`. The fix is display-only (`mp.nstr`), but no producer was edited in the refresh. The witness written before the crash was **NOT committed** (owner decision 2026-11-24 holds this producer). Its payload differed from main only in float repr: `alpha_EM` `0.0072973525692838015` → `0.0072973525692838`, `coulomb_correction_MeV` `0.22678020554817568` → `0.226780205548176` (and two more). So no number of substance is at stake.

The same `mpf.__format__` crash also blocks 7 more paper producers in this refresh: `alpha/alpha_5_jucys_murphy_central.py`, `delta_q_decoration.py`, `markov/markov_trace_atomic_proton_full.py`, `markov/markov_trace_canonical.py`, `nf-qvalues.py`, `probes/gg_production_bond_probe.py`, `probes/rho_k_markov_multiplicativity_probe.py`.

Note the float-repr diff: the producer emits Python floats (`0.0072973525692838`), so the raw-float64 ratchet applies when it is fixed.

Log: `/tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/logs/b_over_a_evaluator.py.log`. It is in session scratchpad and may not survive.

Next honest step: replace mpf format specs with `mp.nstr` in the 8 producers, re-run, and refresh their witnesses.

## 2026-11-24 fixed in PR https://github.com/litlfred/qou/pull/9401 (agent, session 01Eucf)
All 8 producers run (exit 0, assertions pass) after rewriting only the crashing f-string fields to mpmath.nstr (82643b15227 and 299625e1bb8). alpha_5_jucys_murphy_central also needed a fix to qou_substrate.witness._raw_float_paths, which handles int dict keys now. Witnesses were re-run on mpmath 1.4.1 + clarabel 0.11.1 (venv) so the environment record does not degrade (the guard warns on 1.3.0). Payload moves are float noise; the exception is gg-production-bond-probe E0 4.18598 -> 4.22748 MeV via the routed qbeta_e0 (#8590). Note the mechanism is version-dependent (qou-eg4l): 1.4.1 accepts the format spec, while 1.3.0 is what sympy 1.14 pins. Complete when https://github.com/litlfred/qou/pull/9401 merges.
