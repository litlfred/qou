# I9 CODATA de-float follow-on (PR #2277 tranche-4)

**Branch:** `claude/i9-defloat-followon-2026-06-14`
**Parent tranche:** [#2277](https://github.com/litlfred/qou/pull/2277) (`claude/dazzling-mayer-gfuhik`) — scanner repair + 50 production scripts routed.
**Coordination:** intent posted on #2277; this branch picks up #2277's declared "remaining follow-on" so the two sessions don't double-route the same scripts.

## Owner rule (the discipline this enforces)

Production compute must not carry bare floats / hardcoded CODATA-AME
literals. Each hardcoded `mp.mpf("…")` CODATA/AME value in a **production**
script routes to a `substrate/codata_constants.py` registry symbol (via
the `_path_bridge` import); float tables become `mpf`; witnesses are
regenerated and each script is run-verified (exit 0). **Probes are out of
scope** — exploratory / fitting / `*search*` scripts are float-tolerant
scratch and must be *excluded*, not routed (a probe promoted to production
must be de-floated first).

## Scope

### A. The "2 codemod-incompatible" scripts (#2277 listed these for manual routing)

| Script | #2277 reason | This branch's verdict |
|---|---|---|
| `delta_lambda_full_variance_phase5e_1.py` | local `M_E_MEV` shadow | **ROUTE.** Genuine production (Δ_λ binding variance). Local `M_E_MEV = mp.mpf("0.51099894999999995")` shadow in `alpha_k()` (old/truncated m_e) → import registry `M_E_MEV`. Also route the D/T/³He/⁴He AME binding literals (`mp.mpf("2.22456607")` …) to the AME validation witness. Value shifts → **re-run + witness regen + mass-binding appendix sync (STRICT)**. |
| `qbeta/gap_a4_numeric_search.py` | no `_path_bridge` | **DO NOT ROUTE — reclassify as probe.** Body searches for a multiplicative factor `F` s.t. `m_mu_pred · F = m_mu_codata` (a fitting search); witness not consumed anywhere. This is an exploratory numerology probe, out of I9 scope. Action: move to a `probes/` dir or add the probe banner so the scanner excludes it. |

### B. 75 float-table production scripts

Enumerate via `audits/hardcoded_literal_audit.py` (the #2277 scanner).
Bare floats in dict/tuple mass/binding tables, some serialized to witness
JSON. De-float float→mpf + JSON-serialization fixes + per-script run-verify.

**Deferred-verification flag:** `mass_table_ppb.py` is ~26h compute — de-float
the source but verification must run under the long-compute logging discipline
(`-u … 2>&1 | tee`), not inline. Do not block the batch on it.

## Status

- [x] Branch created off fixed `main` (`32b6c2d0`, includes the molecular #2278 repair).
- [ ] Intent posted on #2277.
- [ ] `delta_lambda_full_variance_phase5e_1.py` routed + re-run + witness + appendix sync.
- [ ] `gap_a4_numeric_search.py` reclassified as probe (excluded, not routed).
- [ ] 75 float-tables enumerated + de-floated in run-verified batches.
- [ ] `mass_table_ppb.py` source de-floated; long-compute verification deferred/logged.
