---
# qou-et5f
title: 'GAP: colour-tube branch-point monodromy commutes with the Jimbo colour braiding (conj:colour-tube-monodromy-braided)'
status: todo
type: task
priority: normal
created_at: 2026-11-22T21:50:06Z
updated_at: 2026-11-23T00:57:15Z
---

Owner card 2026-11-22: prove the singlet is kept by any braid-commuting map (done, ColourRelabel.braid_commuting_fixes_singlet, PR #9130) and state the monodromy link as a conjecture. OPEN: show the colour cubic of def:color-tube-fibers carries a flat connection whose branch-point monodromy on (K^3)^{⊗3} commutes with R12, R23 (expected: quantum Weyl group corrected swap, Lusztig 1993; Drinfeld-Kohno). Known: the bare swap does NOT commute at q^2 != 1 (swap_braid_commuting_imp). Next honest step: write the explicit quantum Weyl element T_s on V^{⊗3} for gl3 and check it commutes with R12, R23 (27x27, finite check) before attempting the geometric link.



2026-11-23 (PR #9163, a091ea296): colour ⊗ flavour monodromy splits (BridgeAColourSplit), and Drinfeld–Kohno for C^d is proved (KohnoAssemblyGL). colourC3_flavour_monodromy_conj discharges the colour step for C^3 with no hypothesis. Still open, so this bean stays open: the vanishing of the mixed P_c·P_f term in the Lagrangian pair residue (both couplings generic).
