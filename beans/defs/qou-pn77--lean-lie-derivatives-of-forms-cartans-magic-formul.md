---
# qou-pn77
title: 'Lean: Lie derivatives of forms + Cartan''s magic formula L_x = d i_x + i_x d (Chevalley-Eilenberg, proved)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T17:48:59Z
updated_at: 2026-11-27T19:34:46Z
parent: qou-rtxm
---

Owner 2026-11-27: 'Dispatch sibling to do lie derivatives on manifolds'. Route picked on card: Algebraic Chevalley-Eilenberg (generic CommRing R, Lie ring L, L-module M; forms = alternating R-multilinear maps). File QOU/Core/LieDerivative.lean: ceD (Koszul differential), lieDeriv, iota = curryLeft; cartan_formula proved sorry-free all degrees; discharges the 'cartan' hypothesis of CartanContraction (qou-fita) in this model; Derivation R A A instance for algebraic forms. Follow-ups: dω alternating + d²=0; L_x as AlternatingMap; [L_x, i_y] = i_[x,y]; bridge to Mathlib extDeriv / VectorField.mlieBracket.

2026-11-27: PR #9532 opened, head 50a2727ad5c7. cartan_formula + corollaries + derivation instance sorry-free. Handed to merge manager. Follow-ups remain open (dω alternating, d²=0, L_x as AlternatingMap, [L_x,i_y]=i_[x,y], analytic bridge).

2026-11-27: PR #9540 (head 26fef9cf7bbc): LieDerivativeComplex.lean — ceDAlt (d on forms), bracketPart_isAltMulti, lieDerivAlt, i_y L_x = L_x i_y - i_[x,y], [L_x,L_y]=L_[x,y], [L_x,d]=0, d∘d=0. All sorry-free, any CommRing. Remaining: analytic bridge to Mathlib extDeriv inside QOU/Transcendental boundary (#9533).

2026-11-27: analytic bridge done in PR #9576 (QOU/Transcendental/Calculus/LieDerivativeExtDeriv.lean): ceDAlt_toCE (Koszul d = Mathlib extDeriv), lieDerivAlt_toCE, cartan_constField. Sorry-free. Scope: constant vector fields only; non-constant fields (VectorField.lieBracket, C^inf(E)-linear cochains) not covered. Classical.choice from Mathlib analysis, not yet on Coev.

2026-11-27: PR #9576 merged. All four items landed (#9532, #9540, #9576). Possible follow-up, not started: non-constant vector fields (C^inf(E)-linear cochains) and moving Classical.choice onto Coev.

2026-11-27 (coordinator follow-up): non-constant vector fields. PR #9589: IsLieRinehart, FunLinear; d, i_X, L_X preserve tensors. Next: smooth vector fields instance + extDeriv bridge, then Coev routing.


2026-11-27 (PR #9589, head c6d95ea4c5b): non-constant fields done. Core: FunLinear.eq_of_span. Transcendental/Calculus/SmoothVectorFields.lean: SFun/SVF Lie-Rinehart instance, toCEv, span_const, ceDAlt_toCEv (d toCEv phi = toCEv (extDeriv phi), finite-dim E, arbitrary smooth fields), cartan_smoothField. lean-direct exit 0, 0 sorry, axioms propext/Classical.choice/Quot.sound. Coev routing: nothing to route; the choice is Mathlib's (already in the merged algebraic cartan_formula), and the bridge has no Archimedean hypothesis. Awaiting merge.


2026-11-27 choice trace (Lean BFS over used constants, listing direct Classical.* users): cartan_formula reaches 6500 consts, 89 direct users: 86 theorems (by_cases/byContradiction/decEq on Fin equalities, Equiv.swap proofs), 3 defs used only in proofs: Trunc.out/Quot.out via Equiv.Perm.swap_induction_on <- AlternatingMap.map_perm <- map_update_eq; Fintype.equivFin via Finite instance in map_perm; Exists.choose inside Lean core List.nodup_range <- Fin.fintype (every Finset sum over Fin). ceDAlt_toCEv reaches 31451, 819 direct users, 77 defs (Real, fderiv, lim, tsum, Finsupp). Routing around: impossible for the analytic bridge; for Core only by a list-based rewrite avoiding Fin.fintype. Put to Carl as a card (record / audit script / rewrite).
