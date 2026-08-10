---
# qou-lbdl
title: 'Audit for un-propagated canonical-constant fixes (qou-usft class): duplicated physical constants in computations/'
status: todo
type: task
priority: normal
created_at: 2026-08-10T17:21:44Z
updated_at: 2026-08-10T17:21:45Z
parent: qou-1nvh
---

Found while working qou-xeys: coulomb_mirror_killswitch_probe.py kept its own float64 copy of ALPHA_HBAR_C_MEV_FM=1.43996 (CODATA) and R0_FM=1.2 (empirical) AFTER bean qou-usft replaced both in coulomb_energy.py with a derived alpha_EM and the CAL-3 length. A predicted observable was consuming experimental inputs with nothing detecting it. Likely a pattern, not an incident. Suggested: grep computations/ for duplicated physical constants (hbar_c, alpha_EM, r0, m_pi, CODATA masses) defined outside their canonical module.
