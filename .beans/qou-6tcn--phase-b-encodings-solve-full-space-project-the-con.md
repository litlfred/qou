---
# qou-6tcn
title: 'Phase-B encodings solve full-space: project the constraint rows onto the convention-D support'
status: todo
type: task
priority: normal
created_at: 2026-08-26T13:27:25Z
updated_at: 2026-08-26T18:43:15Z
---

2026-08-26 — Addendum 31: the interface IS fixed upstream, and the fix pins it to ONE crossing. alpha_shift is a Laurent valuation (pole order at q=0 of chi_lambda), not a magnitude; my Addenda 29-30 screen was aimed at the wrong invariant. The corpus already pins alpha_shift(I_atom)=alpha_shift(T_{2,1})=1, giving the verified D(u) exponent 40 = 18+21+1. Measured: all six screened candidates have alpha_shift = their letter count (1,2,3,4,8,9), so every one moves that exponent. Mechanism: the all-column channel is 1-dim with rho=-1, generator scalar -q^-1, valuation -1 per letter. Lean: InterfaceLengthPinned.lean, 6 decls, exit 0, axioms clean. Scope (b) with the invariant named, limited to POSITIVE words and conditional on T_2. Closes the interface front.

2026-08-26 — Addendum 32: the freedom IS in Delta, carrier named. Nucleon word is not positive (7 sigma^-1 of 23 letters) so Add.31 does not reach it. Column valuation is 13, NOT the writhe 9 — my prediction was wrong; per-letter breakdown shows the entire 4-unit excess is ONE letter, the p-n interface sigma - h(1/2 - delta/4), anomalous only under bring_color_weighted (colour-blind gives exactly the writhe, no anomalous letter). delta = flavor_split_leading(q) is the one separately q-dependent coefficient in the word. And the maximizer LEAVES the column channel: alpha_shift = 27 at (4,2), seven-way tie, vs column 13 — so alpha_shift is no word statistic here. Two max-pole channels have l<=2, i.e. live convention-D blocks, not TL radical. First positive lead of the arc. NOT a magnitude result: q->0 valuation only, nothing compared to B_AME, and 27 (exponent of q) must not be equated with 40 (exponent of u). Also caught and fixed a layer straddle in my own probe (word baked at q0 while varying q in the rep). 11/11.

2026-08-26 — Addendum 33: the Delta freedom buys NO magnitude, and I am withdrawing my own 'first positive lead' billing of A32. The p-n letter is (1/2+delta/4)sigma + (1/2-delta/4)sigma^-1; at q0 delta = 0.001376 so weights are 0.50034/0.49966, INSIDE the convex hull, and convex_comb_le_bound applies verbatim. Colour weighting moves tr_M by 0.0141% (0.575091 -> 0.575172, reproducing Sec C's committed value to 2.4e-7). Reaching sqrt(B_AME) needs delta = 15.493, i.e. 11262x the substrate value and far past the |delta|=2 hull threshold. Reconciliation: delta = (q-1)^2(1-q^-4)/3 is -1.41e28 at q=3^-15 and 0.00138 at q0 — A32's valuation freedom and Sec C's magnitude bound are both right, in different regimes. A32 stands as a scope note on A31, not as a lead. Scope (b), premise measured not assumed. Satellite/cable route untouched — larger index set, outside the hypotheses. 9/9.
