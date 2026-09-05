---
# qou-4a7a
title: 'RED on main: ParticleInteractions/silver_ratio_beta_decay_null.lean — 3 proof errors, real, not a port'
status: completed
type: task
priority: normal
created_at: 2026-09-04T13:16:36Z
updated_at: 2026-09-05T06:20:57Z
---

Found by the dirty-closure library rebuild (qou-n9j7, PR #6649) on main 71744b7775: the only red among 158 modules rebuilt from source (every dependency rebuilt clean first; no importers). File last touched e1fd0deed4 (2026-08-30, 'lean(silver-ratio): the β-decay null in crossing energy, and the q→∞ volume limit'). Errors, verbatim:
- :175:64 error: No goals to be solved
- :184:15 error: linarith failed to find a contradiction (case mp.inr, q : ℝ, hq : 0 < q, …)
- :227:2 error: Type mismatch: After simplification, term h has type Filter.Tendsto (fun q => 1 - q⁻¹) Filter.atTop (nhds 1) …
Classification: REAL (proof-level, not a retype/argument-order/rename the corpus made elsewhere). Not fixed on #6649 by design — a real red is repaired by its author or a session that owns the mathematics, never by weakening the statements to get green. Repro: cd content/quantum-observable-universe/lean; LEAN_PATH=<restored dirs> lean QOU/ParticleInteractions/silver_ratio_beta_decay_null.lean.



CONFIRMED 2026-09-05: still red with its ENTIRE import cone rebuilt under the sound seed-commit criterion (1,497 modules). Real.
