---
# qou-tqfm
title: a_operator_categorical.py:512 carries the colour-blind -h/2 under an I_pn label
status: todo
type: task
created_at: 2026-08-23T22:07:20Z
updated_at: 2026-08-23T22:07:20Z
---

3dcf933c5d colour-weighted the physical p-n interface (-h/2 -> -h(1-delta/4)/2) at five sites in a_operator_gauge_align.py. Two consumer sites were missed. One (cyclic_intertwiner_verify.py:67) was a real bug and is fixed in the branch claude/cyclic-intertwiner-colour-blind-interface-2026-08-23. The other, a_operator_categorical.py:512 inside verify_operator_decomposition_exact, is MEASURED INERT: that function uses I_iface on both sides of its own comparison, so the assertion operator_interface_decomposition_exact_1e-25 passes at 1.8495342e-49 whatever shift is used. Left unedited rather than making a change with no observable effect. The label is nevertheless wrong by 3dcf933c5d's own stated criterion (it says I_pn is the physical p-n bridge and must carry the colour weighting), so it is a latent inconsistency: if that operator ever becomes load-bearing, it disagrees with every other p-n interface in the subsystem. Decide: align the constant (no numeric effect today), or relabel it as a shift-agnostic test operator.
