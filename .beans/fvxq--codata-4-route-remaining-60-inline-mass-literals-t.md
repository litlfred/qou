---
# fvxq
title: 'CODATA #4: route remaining ~60 inline mass literals through codata_constants registry'
status: in-progress
type: task
priority: normal
created_at: 2026-06-20T00:58:14Z
updated_at: 2026-06-20T01:04:35Z
parent: qfzy
---

PR #2510 / branch lucid-curie. 7 files routed in #2349 (merged). ~60 live offenders remain (/tmp/codata_offenders.txt). Registry: computations/substrate/codata_constants.py (M_*_MEV_VALIDATION).

Progress (PR #2510): +3 files routed (compound_binding_via_differences, mass_table_l1_full_crosscheck, m_p_borromean_verification_50dps). Total 10/~67 (7 in #2349 merged + 3 here). ~57 live offenders remain — long mechanical tail.

## Progress (PR #2546, 2026-06-20) — +3 value-preserving routes + tail triage

Routed (value-preserving; each runs exit 0, witness refreshed):
- `proton_mu_mass_ratio_substrate_identity.py`: m_μ → M_MU_MEV_VALIDATION
- `m_p_substrate_identity_50dps.py`: m_μ → M_MU_MEV_VALIDATION
- `m_pi_hecke_prediction_probe.py`: m_π → M_PI_PM_MEV_VALIDATION

**Triage of the remaining tail — the literal-count is NOT the offender-count.**
The 128 files matching the mass regex split into classes, most NOT cleanly routable:
1. **Documentary** (literal in comment/docstring/f-string: per_observable_100x_status,
   canonical_tower, neutron_error_diagnostic) — leave.
2. **Standalone-by-design** (meson_mass_from_hecke.py: Decimal fallback, no cluster
   infra) — routing breaks the design; leave.
3. **Mass-as-INPUT** (crt_markov.py `(Z+N)*938.272`) — routing a _VALIDATION mass into
   a prediction input violates the 3-cal discipline; leave / separate concern.
4. **Precision-BUMP** (tower_isotope_absolute p/n, etc.): M_P/M_N_MEV_VALIDATION are
   witness-loaded at HIGHER precision than the 938.27208816/939.56542052 literals
   (`!=`), so routing is a value CHANGE, not value-preserving. **DECISION NEEDED**
   (owner): bump these to canonical witness precision (changes output, refreshes
   witnesses) or leave the truncated literals? Hardcoded-mpf registry constants
   (M_PI/M_K/M_MU) match exactly and route cleanly; witness-loaded m_p/m_n/m_D…
   do not.
5. **Cleanly routable** (hardcoded-match validation literal on cluster infra) — the
   genuine remaining subset; this is the slow per-file grind.

Total now 13/~67 routed. The "value-preserving + cleanly-routable" subset is much
smaller than ~57; the bulk is classes 1–4 above.
