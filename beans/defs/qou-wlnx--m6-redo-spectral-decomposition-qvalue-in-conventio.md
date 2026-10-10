---
# qou-wlnx
title: 'M6: redo spectral-decomposition-qvalue in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-10T09:04:19Z
parent: qou-d8c7
---

predicted-spectra/spectral-decomposition-qvalue.md:23 defines z = z_C in the chain V_j = z M[0][0] + M[1][0] (12 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed; tr_M^D(tau(2,9))=1.82841 spot-checked). z -> q^3/(q^2+1); F_deg2 0.5904 -> 3.6844 (and not a suppression factor under C either: 4.581 by the stated formula); trace column recomputed. HONEST NEGATIVES: Pauli branch of (iii) gives F=0 (y_(1^3)=0) so Q=0 for every magic shell, no replacement derived; F_Pauli 0.6382 not reproducible (producer hard-coded); two old C table entries were wrong (markov_trace bug qou-ix74). OPEN: Q_bare values and 2-10% error range need a producer re-run; producer rosso-jones-qvalues.py is deprecated and float-only. Stays open.
