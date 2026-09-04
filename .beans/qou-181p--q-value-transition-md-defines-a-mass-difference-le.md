---
# qou-181p
title: 'q-value-transition: .md defines a MASS difference, .lean + title define an ACTION difference — statement-integrity defect'
status: in-progress
type: task
priority: high
created_at: 2026-09-04T02:14:49Z
updated_at: 2026-09-04T02:20:28Z
---

Owner pick 2026-09-04 (option 3 of the qou-zmuu close-out). predicted-spectra/q-value-transition.md opens 'We define the Q-value ... directly from the categorical action' and then states 'Definition (mass difference, primary): Q = M(Z,N) - M(Z+1,N-1)' with M = Z m_p + N m_n + Z m_e - B(Z,N). The .lean (QOU.Archimedean.QValueTransition) defines QqValue.value := S_parent - S_daughter - S_electron - S_antineutrino, an ACTION difference, with a header saying 'NOT by classical energy conservation'. The .ts title is 'Q_q-Value as Categorical Action Difference'. Three faces, two definitions. Decide which is primary, make the other a derived remark or proposition, and re-run proof-statement-integrity + wall-side-statement on the block.
