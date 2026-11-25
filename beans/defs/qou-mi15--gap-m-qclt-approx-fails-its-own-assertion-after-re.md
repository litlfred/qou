---
# qou-mi15
title: 'GAP: m_qclt_approx fails its own assertion after refresh'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T20:49:37Z
updated_at: 2026-11-25T01:31:20Z
---

Found by the 2026-11-24 paper-compute refresh (PR #9395, branch `claude/compute-refresh-2026-11-24`, main `dd5f163edbd`). The witness `computations/m-qclt-approx.witness.json` was self-stale (scriptHash drift). Re-running the current producer `computations/m_qclt_approx.py` (exit 0, Python 3.13.18, mpmath 1.3.0, sympy 1.14.0) writes `allPassed: false`. The refreshed witness was **NOT committed** (owner decision 2026-11-24, "D2 commit all 42": hold the producers that fail their own assertion). The committed witness on main still says `allPassed: true` and is stale.

Before (committed) → after (fresh run):

- assertion 5 `factorized_binding_within_1p25x_T_3He` (tolerance 0.25 around 1.0): computed `1.08333` → `1.5002`, **passed True → False**
- assertion 1 `err_full_production_equals_nucleon_gap`: computed `0.00815851` → `-0.00811061` (sign flip; still within its 0.1 tolerance)
- `data/factorized_qclt/B_fac_T_MeV`: `8.6382358` → `6.3094054`
- `data/factorized_qclt/B_fac_3He_MeV`: `7.1243868` → `5.1446899`
- `data/factorized_qclt/worst_miss_factor_T_3He`: `1.08333` → `1.5002`
- `data/err_full_production_cross_isotope_spread_pct`: `0.00945162` → `0.0239516`
- assertion 4 source text: `L_nn=1.237` → `L_nn=0.9073`
- the upstream factorized-qCLT source moved: `source_computedAt` 2026-06-15 → 2026-11-21, `source_scriptCommitSha` `32f3f731` → `453b2a86`

So the miss comes from an upstream input (the factorized q-CLT source witness was regenerated on 2026-11-21 and its `L_nn` bond trace moved 1.237 → 0.9073). It does not come from this producer's own code. 55 payload fields moved in all. Not established: whether the new upstream value is correct.

Log: `/tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/logs/m_qclt_approx.py.log`. It is in session scratchpad and may not survive; re-run with `PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python python3 -u computations/m_qclt_approx.py`.

Next honest step: find which producer regenerated the factorized-qCLT source on 2026-11-21 and why `L_nn` moved. Then decide whether the 1.25x bound or the new input is wrong. Do not widen the tolerance to the new miss.

## 2026-11-24 root cause (agent, session 01Eucf, claimed)
The upstream bond witness binding-single-pipeline-comparison was regenerated in ca6b5d6dd94 (2026-11-21) on the convention-D + beta_Bor word regime (owner ruling 7db032fb482, qou-hu1f). L_pp/pn/nn went from 0.6945/0.9292/1.2370 to 0.4899/0.6768/0.9073. The new input is correct per the corpus, so the 1.25x claim honestly fails (1.5002x). This is an honest negative; do not widen the tolerance. WARNING: the same commit widened the sibling assertion B_sym_E0_within_1p25x_T_3He from 0.25 to 0.60 so that it passes at 1.58x, which is a tolerance sized to its own miss. Flagged to the owner on #9395 (https://github.com/litlfred/qou/pull/9395#issuecomment-7144386562).

## 2026-11-24 owner ruling 3 applied in PR https://github.com/litlfred/qou/pull/9401 (f35683512a2)
Owner card 'A: revert, fail honestly'. B_sym_E0_within_1p25x_T_3He tolerance restored 0.60 -> 0.25; it now FAILS at 1.5803. m_qclt_approx's factorized_binding_within_1p25x_T_3He fails the same way (1.5002). OPEN GAP: the beta_Bor + convention-D bond traces put the A=3 log-trace binding at 1.28-1.58x of AME, outside the 1.25x claim. Not fixable by tolerance. The sibling B_qCLT_fac_chain_within_1p25x_T_3He (widened the same way, passes at 1.5002 vs 0.60) is put back to the owner. Stays open; do not close while the 1.25x claim is unmet.

## 2026-11-25 owner ruling: second revert (https://github.com/litlfred/qou/pull/9404, 64e78785035)
B_qCLT_fac_chain_within_1p25x_T_3He restored to 0.25 and now FAILS (1.5002). Both A=3 1.25x claims in binding-single-pipeline-comparison fail honestly: B_sym 1.5803, B_qCLT_fac 1.5002 (and m_qclt_approx 1.5002). witness_failed_assertion_audit keeps flagging them, with no baseline entry (owner, 2026-11-25). OPEN GAP remains.
