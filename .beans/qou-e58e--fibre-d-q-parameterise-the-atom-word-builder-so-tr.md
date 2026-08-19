---
# qou-e58e
title: 'FIBRE-D: q-parameterise the atom word builder so tr_M(q0^-1) is computable -- unblocks every bar-parity claim'
status: todo
type: task
priority: normal
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-08-19T14:21:54Z
---

THE BLOCKER IS TOOLING, NOT MATHEMATICS. complex_volume_witness.py already attempts the bar-norm ||tr_M||^2 = tr_M(q0)*tr_M(q0^-1) and guards it, with its own comment: "The canonical color-weighted atom word BAKES q0 into its crossing values, so it cannot re-lift at q^-1 (a q-parameterised word builder is required)". Same comment records the fact the whole route turns on: bar-norm and |tr_M|^2 "coincide on the unit circle (where conjugation = bar-involution) and DIFFER at the real anchor q0". So every bar-parity claim about a trace-derived quantity currently rests on a quantity the corpus CANNOT EVALUATE. Task: parameterise tr_m_atom_via_transfer over q, then un-guard the bar-norm. Prerequisite for options B/C/E being more than prose. Cost UNMEASURED -- q0 may be baked in at more than one site. Doc: docs/audits/2026-08-19-frakv-fibre-workplan-options.md option D.
