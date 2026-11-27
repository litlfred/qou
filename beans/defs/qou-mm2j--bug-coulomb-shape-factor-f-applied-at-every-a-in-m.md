---
# qou-mm2j
title: 'BUG: Coulomb shape factor f applied at every A in mass_table EM field; coulomb_energy.py scopes it to A <= 4'
status: todo
type: bug
created_at: 2026-11-27T21:59:36Z
updated_at: 2026-11-27T21:59:36Z
---

coulomb_isospin_channel.py:59 pastes F_QHANKEL; mass_table_comprehensive.py:611 uses it for all A (Table 3.4b m_ruled_em). coulomb_energy.shape_factor(A) uses q-Hankel only for A <= 4. Also ACCURACY.md:144 says uniform sphere at A=3 (stale since 98608fc2f); mirror-nuclei witness likely stale. Owner card open in thread 'Audit the q-Bessel special-function dictionary' (recommended: single source with the A <= 4 scope).
