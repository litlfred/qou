---
# qou-6tcn
title: 'Phase-B encodings solve full-space: project the constraint rows onto the convention-D support'
status: todo
type: task
priority: normal
created_at: 2026-08-26T13:27:25Z
updated_at: 2026-08-26T18:30:33Z
---

2026-08-26 — Addendum 31: the interface IS fixed upstream, and the fix pins it to ONE crossing. alpha_shift is a Laurent valuation (pole order at q=0 of chi_lambda), not a magnitude; my Addenda 29-30 screen was aimed at the wrong invariant. The corpus already pins alpha_shift(I_atom)=alpha_shift(T_{2,1})=1, giving the verified D(u) exponent 40 = 18+21+1. Measured: all six screened candidates have alpha_shift = their letter count (1,2,3,4,8,9), so every one moves that exponent. Mechanism: the all-column channel is 1-dim with rho=-1, generator scalar -q^-1, valuation -1 per letter. Lean: InterfaceLengthPinned.lean, 6 decls, exit 0, axioms clean. Scope (b) with the invariant named, limited to POSITIVE words and conditional on T_2. Closes the interface front.

2026-08-26 — Addendum 32: the freedom IS in Delta, carrier named. Nucleon word is not positive (7 sigma^-1 of 23 letters) so Add.31 does not reach it. Column valuation is 13, NOT the writhe 9 — my prediction was wrong; per-letter breakdown shows the entire 4-unit excess is ONE letter, the p-n interface sigma - h(1/2 - delta/4), anomalous only under bring_color_weighted (colour-blind gives exactly the writhe, no anomalous letter). delta = flavor_split_leading(q) is the one separately q-dependent coefficient in the word. And the maximizer LEAVES the column channel: alpha_shift = 27 at (4,2), seven-way tie, vs column 13 — so alpha_shift is no word statistic here. Two max-pole channels have l<=2, i.e. live convention-D blocks, not TL radical. First positive lead of the arc. NOT a magnitude result: q->0 valuation only, nothing compared to B_AME, and 27 (exponent of q) must not be equated with 40 (exponent of u). Also caught and fixed a layer straddle in my own probe (word baked at q0 while varying q in the rep). 11/11.
