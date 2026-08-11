---
# qou-ftmf
title: 'WIRE: discharge StandardYoungTableau.numSYT_mul_hookProduct via GNW numSYTenum_mul_prodHooks + numSYT=numSYTenum∘rowLens (numSYTenum_eq_numStandardYoungTableaux + ofRowLens_to_rowLens_eq_self, numSYT=numStandardYoungTableaux rfl) + the hookProduct=prodHooks core + sz(rowLens)=card'
status: completed
type: task
priority: normal
created_at: 2026-08-01T23:34:16Z
updated_at: 2026-08-10T04:18:37Z
---

STALE - target already discharged on main. numSYT_mul_hookProduct is proved sorry-free at QOU/BraidKnot/HookProductHLF.lean:99 (rw [SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux, hookProduct_eq_hookLengthProduct]; exact QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct). The original site QOU/BraidKnot/StandardYoungTableau.lean:159 now itself records it as 'proved (sorry-free)'. NOTE the route differs from this bean's plan: the landed proof goes via SYTEncodingBridge + Mathlib's HLF, not via GNW numSYTenum_mul_prodHooks. Target met, plan superseded. Caveat: all 4 'sorry' greps in HookProductHLF.lean and both in StandardYoungTableau.lean are DOCSTRING prose, not tactic positions - checked.
