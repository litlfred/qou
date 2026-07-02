---
# cmiy
title: 'Integration: canonical watcher - P30 WitnessBuilder rollup'
status: todo
type: task
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-06-21T21:44:26Z
---

## Canonical bean for the P30 WitnessBuilder rollup (dedup 2026-06-28)

`1j39` ("I-infra-no-witnessbuilder-P30 batch port") is the **same work** —
both are the P30 WitnessBuilder rollup (~133 scripts that emit raw witness
JSON instead of routing through `WitnessBuilder`). Treat **this bean
(`cmiy`) as canonical**; `1j39` is its duplicate. (Owner-close `1j39` when
convenient — resolve is human-only.)

## DEFERRED — high collision with the active compute-PR storm

A big-bang witness regen across ~133 scripts conflicts with 8–12 in-flight
compute PRs (e.g. #2993 λ_A-excision, #3009 lever-1 kernel, #2985 z2bn,
#2970 canonical-derivation, #3016 dashboard, #3013/#3007 Cl3Zeta5, #2747
ct80 codata) — a repo-wide regen now would create merge churn across all of
them. Per `/coordinate` (2026-06-28): **defer the big-bang** until the
compute-PR storm settles, then do it in small per-cluster batches (or one
sweep once `main` is quiet). Prior triage also classes much of the rollup as
acceptable Class-B/C/D (`docs/audits/2026-06-25-session-bean-triage.md`).

## 2026-06-30 — re-confirmed DEFERRED (not started)
The ~133-script WitnessBuilder big-bang regen remains a high-collision sweep
to be done in small per-cluster batches once main is quiet — explicitly not a
late-session big-bang. No work taken here. Duplicate 1j39 still open (owner-close).

## 2026-06-30 — batch 1 (1 script) + migration gotchas documented
Routed meson_vol_density.py off raw json.dump onto WitnessBuilder provenance
(PROV_MISSING 280 → 279). Stays OPEN (multi-batch). Surfaced 3 non-mechanical
gotchas that gate a bigger sweep — full recipe in
docs/audits/2026-06-30-cmiy-witnessbuilder-rollup-batch1.md:
  1. wrap_legacy DROPS flat assertions/allPassed (data loss) → use
     stamp_staleness_metadata for assertion-bearing payloads.
  2. regen refreshes stale data (q0 drift) → full regen, not provenance-only;
     pyhecke_native producers need the canonical env (skip in ad-hoc env).
  3. some raw-emit scripts pre-crash (magic_A_formula mpf-format) → separate fix.

## 2026-06-30 — batch 2 (3 scripts, wrap_legacy)
3 pure-Python zero-consumer raw-emit scripts migrated via wrap_legacy (none
carries flat assertions, so wrap_legacy is safe per batch-1 gotcha #1):
rt_route_cross_particle_ratio_quantum_dim, bw_chirality_isotopes,
canonical_lepton_braid_words. Each: exit 0, PROV_OK, original keys preserved.

## 2026-06-30 — batch 3 (2 scripts, wrap_legacy)
delta_lambda_borromean_ascaling, crystal_yekutieli_probes_abcd — pure-Python,
zero content-consumers, no flat assertions. crystal lacked a sys.path entry
for substrate/ (witness_base home); added it inline before the import.
Both: exit 0, PROV_OK, original keys preserved.

## 2026-06-30 — batch 4 (1 script) + easy-tail exhausted note
q_beta_complex_q_test1_phaseA_v2 migrated via wrap_legacy (0 consumers, no
assertions, exit 0, PROV_OK). NOTE: the clean single-output / zero-consumer /
no-assertion / fast tail is now EXHAUSTED — ~1 in 12 triaged this round.
Remaining raw-emit scripts need per-script handling: multi-emit (≥3 witnesses),
flat-assertions (→ stamp), many-consumer (restructure risk), slow/Hecke regen
(canonical-env), or NOFILE (would add a witness, not fix one). Future batches
are the harder tail the bean's deferral anticipated.
## 2026-06-30 — batch 5 (3 scripts, stamp — the assertion-bearing case)
First "harder tail" batch: 3 assertion-bearing substrate/ probes migrated via
stamp_staleness_metadata (NOT wrap_legacy, which drops flat assertions):
lever1_lambda_sw_no_shortcut, lever1_color_eq_monodromy_integrality,
lever1_binding_monodromy_hyperbolicity. Each: exit 0, PROV_OK, assertions
preserved, original keys kept. (lambda_sw also: fixed a fragile cwd-relative
output path → os.path.dirname(__file__).)

## 2026-07-01 — batch 6 (3 scripts, stamp)
3 more assertion-bearing substrate/ probes via stamp_staleness_metadata:
lever1_color_eq_intrinsic_tau_rapidity, zeta4_complex_volume_moderator_probe,
lever1_color_eq_lambda_sw_rapidity. Each: exit 0, PROV_OK, assertions preserved,
keys kept. (zeta4 also: fixed cwd-relative output path → dirname(__file__).)

## 2026-07-02 — batch 7 (3 scripts, stamp)
3 more assertion-bearing substrate/ probes migrated via stamp_staleness_metadata
(preserves flat assertions per gotcha #1): lever1_lw_depth2_recurrence_test,
lever1_qinvolution_kernel_test, lever1_binding_habiro_qexponential. Each:
exit 0, PROV_OK, assertions preserved, original keys kept; all three also fix
the fragile cwd-relative output path → dirname(__file__). PROV_MISSING 276→273
pre-rebase (batch 6 #3198 merged first; post-rebase audit refresh → 270).
