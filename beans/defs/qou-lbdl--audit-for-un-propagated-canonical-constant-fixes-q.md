---
# qou-lbdl
title: 'Audit for un-propagated canonical-constant fixes (qou-usft class): duplicated physical constants in computations/'
status: completed
type: task
priority: normal
created_at: 2026-08-10T17:21:44Z
updated_at: 2026-08-10T17:44:55Z
parent: qou-1nvh
---

Found while working qou-xeys: coulomb_mirror_killswitch_probe.py kept its own float64 copy of ALPHA_HBAR_C_MEV_FM=1.43996 (CODATA) and R0_FM=1.2 (empirical) AFTER bean qou-usft replaced both in coulomb_energy.py with a derived alpha_EM and the CAL-3 length. A predicted observable was consuming experimental inputs with nothing detecting it. Likely a pattern, not an incident. Suggested: grep computations/ for duplicated physical constants (hbar_c, alpha_EM, r0, m_pi, CODATA masses) defined outside their canonical module.

Drained the Coulomb slice; the rest is already-tracked 46ke scope. Findings: (1) detection ALREADY EXISTS - audits/derived_alpha_em_usage_audit.py flags 53 INPUT sites incl. the 1.43996 product form; it is simply UNDRAINED, so this is a drain problem not a tooling problem. (2) Routed mirror_isospin_coulomb_split.py AHC 1.43996 -> canonical derived (3.6 ppm, no conclusion moves). (3) gap2_borromean_triple_count.py comments asserted CODATA while importing the derived module - annotation-only, code was right. (4) NEW staleness class confirmed: gap2's committed witness predates qou-usft and its numbers move on re-run (triple/binding ratios 1.132/1.197/1.240 -> 1.148/1.210/1.250). Third dependency-stale witness this session. (5) 46ke's handoff item calling 931.49410372 'WRONG vs 931.49410242' is itself STALE - that is the CODATA-2022 value, 2018 is what AME2020 carries, and the dashboard already routes U_MEV through the registry. Remaining tail = 46ke/me3r scope, not re-opened here.
