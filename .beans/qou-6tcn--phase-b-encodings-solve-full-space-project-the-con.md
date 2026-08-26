---
# qou-6tcn
title: 'Phase-B encodings solve full-space: project the constraint rows onto the convention-D support'
status: todo
type: task
priority: normal
created_at: 2026-08-26T13:27:25Z
updated_at: 2026-08-26T18:12:54Z
---

2026-08-26 — Addendum 31: the interface IS fixed upstream, and the fix pins it to ONE crossing. alpha_shift is a Laurent valuation (pole order at q=0 of chi_lambda), not a magnitude; my Addenda 29-30 screen was aimed at the wrong invariant. The corpus already pins alpha_shift(I_atom)=alpha_shift(T_{2,1})=1, giving the verified D(u) exponent 40 = 18+21+1. Measured: all six screened candidates have alpha_shift = their letter count (1,2,3,4,8,9), so every one moves that exponent. Mechanism: the all-column channel is 1-dim with rho=-1, generator scalar -q^-1, valuation -1 per letter. Lean: InterfaceLengthPinned.lean, 6 decls, exit 0, axioms clean. Scope (b) with the invariant named, limited to POSITIVE words and conditional on T_2. Closes the interface front.
