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

## CRITICAL finding (2026-06-20) — class 4 is mostly UNSAFE, not just precision

Checked registry vs tower literals before routing the "precision-bump" class:
- p/n: registry == literal to 8 digits but witness carries MORE digits ⇒ true
  precision-bump (marginal).
- **D/T/³He/⁴He: registry masses are NUCLEAR; the in-script literals are ATOMIC
  (with electrons). They differ by ≈ m_e per electron (D: reg 1875.613 vs lit
  1876.124). Routing these is an ≈0.5 MeV SEMANTIC ERROR, not a precision bump.**
  So the compound-mass literals must NOT be routed to `M_*_MEV_VALIDATION`
  (different quantity). tower_isotope_absolute etc. left as-is.

⇒ The genuine value-preserving routable set is the exact-match hardcoded-mpf
registry constants (M_π / M_K / M_μ) used as validation comparisons — largely
exhausted by #2349 + #2510 + #2546. The remaining "~57" are classes 1–4 (mostly
non-routable). Recommend re-scoping fvxq: the easy mechanical tail is done;
class-4 needs an atomic↔nuclear registry decision (add atomic-mass exports?) and
class-3 needs the 3-cal input-discipline fix — both are NOT mechanical.

## RECONCILIATION (PR #2540 ↔ #2546, 2026-06-20)

PR #2540 (branch intelligent-pasteur) routed ~57 probe/phase5/ocneanu files
in parallel with #2546's triage. #2546's class-1–4 analysis above SUPERSEDES
#2540's simpler "just route the probes" framing. #2540 matched only the EXACT
hardcoded literals (e.g. nuclear 1875.61294257, NOT atomic 1876.124), so it
did NOT hit the class-4 atomic↔nuclear semantic trap, and each route was
verified `mpf(M_X_MEV_VALIDATION) == mpf("<literal>")` True in its container.
Open risk per #2546 class-4: witness-loaded M_P/M_N_MEV_VALIDATION may carry
more digits than the 938.27208816/939.56542052 literals on main/CI ⇒ #2540's
p/n probe routes could be a precision-BUMP, not strictly value-preserving.
ACTION (post-rebase): re-verify every #2540-routed literal against main's
witness state; revert any p/n route where registry != literal.
