---
# qou-t8qh
title: 'SW-JM: q-Jucys-Murphy eigenvalue (Ram 4.1) — the last SchurWeyl sorry'
status: completed
type: task
priority: normal
created_at: 2026-08-19T07:41:30Z
updated_at: 2026-08-19T12:31:23Z
parent: qou-59vq
---

Target: discharge the LAST sorry in the SchurWeyl tree — QJucysMurphy.barSymJMSum_block_eigenvalue (QJucysMurphy.lean:1105), which asserts rho_lambda(Theta) = cellContentCoshSum lambda q .1 for Theta = barSymJMSum.

## Prerequisite 1 is now CLEARED
The GAP note names two blockers. The first, hoefsmit_seminormal_rep, is PROVED and on main (PR #5279, HoefsmitRepGeneral.lean). Only the second remains.

## The remaining content: q-JM eigenvalue (Ram 1997, Thm 4.1)
Needed: rho(qJM k) is DIAGONAL with entry at tableau T equal to q^(2*cellContent(cellOf T (k+1))).
Given that, the target follows immediately: rho(Theta)(T) = sum_k (q^(2c_k) + q^(-2c_k)), and as k ranges over 0..n the cells of T range over ALL cells of lambda, so the sum is cellContentCoshSum lambda q — independent of T, i.e. a scalar matrix.

## CORPUS FINDING — do NOT mis-cite JucysMurphyOV
QOU/BraidKnot/JucysMurphyOV.lean proves a JM diagonalisation theorem, but it is the CLASSICAL Okounkov-Vershik case: the symmetric-group algebra, eigenvalue = cellContent (NOT q^(2*content)), resting on the cited core seminormalVector_data_exists. It does NOT supply this statement. Same for JucysMurphy.lean and SnWedderburnPartitionBridge. The q-deformed Hecke statement is genuinely separate and must be proved against SeminormalRep.genMat directly.

## Index bookkeeping (checked)
- qJM recursion: L_0 = 1, L_{k+1} = sigma_k * L_k * sigma_k (pure conjugation, QJucysMurphy.lean:101).
- seminormalGen n hN i = genMat q ((i:N)+1), so rho(sigma_k) = genMat q (k+1).
- L_k corresponds to VALUE k+1 (L_0 = 1 <-> value 1 at (0,0), content 0, q^0 = 1).

## Base case: AVAILABLE
SytAdmissible.cellOf_one : cellOf T 1 = (0,0) (needs 0 < cells.card). Content 0 ⇒ q^0 = 1 = rho(L_0). Do not re-prove it.

## THE CRUX IS DERIVED — the off-diagonal provably vanishes
The inductive step conjugates D_k (diagonal) by S = genMat(k+1). Two branches:

(a) INADMISSIBLE at k+1 (orbit size 1): S is diagonal with entry a(d), d = +-1. Then (S D S) = diag(a(d)^2 * q^(2c)). Since a(1) = q and a(-1) = -q^(-1) (seminormalParam_one/_neg_one), a(d)^2 = q^(2d), and c(k+2) = c(k+1) + d exactly. So the entry becomes q^(2c(k+2)). CONFIRMED arithmetically.

(b) ADMISSIBLE (orbit size 2): S = [[a(d), offDiag(-d)],[offDiag(d), a(-d)]], D = diag(x,y) with x = q^(2c), y = q^(2c'), c' = c + d. The off-diagonal of S*D*S is
    offDiag(-d) * (a(d)*x + a(-d)*y).
With a(d) = (q - q^-1)/(1 - q^(-2d)):
    a(d)*q^(2c) + a(-d)*q^(2c+2d)
  = (q-q^-1)*q^(2c) * [ 1/(1-q^(-2d)) + q^(2d)/(1-q^(2d)) ]
  = (q-q^-1)*q^(2c) * [ -q^(2d)/(1-q^(2d)) + q^(2d)/(1-q^(2d)) ]
  = 0.
So the conjugate IS diagonal. This is the identity to formalise first — it is a one-line field computation given q != 0 and q^(2d) != 1, and it de-risks the whole theorem.

## Remaining work (realistic)
Define the diagonal target, induct on k with the two branches above, then read off the target. ~200 lines, many verify cycles; the mathematics is settled by the derivation above, so this is formalisation rather than research.

## Hypothesis note (from the existing GAP docstring, verified)
The stated theorem carries (0 < q) (q != 1), which is SOUND but NARROWER than the construction needs: seminormalRep/hoefsmit_seminormal_rep take (q != 0) (q^2 != 1), admitting negative q. Once discharged, relax to the latter.



## PROGRESS 2026-08-19 (PR #5290) — the entire inductive step is formalised sorry-free
Landed in QJucysMurphyEigen.lean, all axiom-clean:
- seminormalParam_weighted_cancel — a(d)q^{2c} + a(-d)q^{2(c+d)} = 0 (the crux; via 1/(1-x⁻¹) = -x/(1-x)).
- seminormalParam_sq_of_one / _neg_one / _sq_mul — the inadmissible branch: a(d)^2 q^{2c} = q^{2(c+d)} for d = ±1.
- jmStep_offDiag — the off-diagonal entry of S·D·S is offDiag(d)·(cancel bracket) = 0.
- jmStep_diag — the diagonal entry is a(d)^2 q^{2c} + offDiag(-d)offDiag(d) q^{2(c+d)} = q^{2(c+d)}, using SeminormalRep.offDiag_mul_neg (offDiag(d)offDiag(-d) = 1 + a(d)a(-d)) to collapse it onto the SAME cancel identity.

### NEW FINDING: one identity governs the whole step
Both entries — not just the off-diagonal — reduce to seminormalParam_weighted_cancel. The diagonal case works because offDiag(d)offDiag(-d) = 1 + a(d)a(-d), so
  a(d)^2 q^{2c} + (1 + a(d)a(-d)) q^{2(c+d)} = a(d)·[cancel bracket] + q^{2(c+d)} = q^{2(c+d)}.
That is why the induction closes, and it means the remaining work needs NO further algebra.

## What remains: plumbing only
1. jmDiag q lam k := Matrix.diagonal (fun T => q^(2*cellContent (cellOf T (k+1)))).
2. Base: rho(L_0) = 1 = jmDiag 0, from SytAdmissible.cellOf_one (cellOf T 1 = (0,0), content 0). Already on main.
3. Step: rho(L_{k+1}) = genMat(k+1) * jmDiag k * genMat(k+1) = jmDiag (k+1). Expand Matrix.mul_apply; each column of genMat has ≤2 nonzero entries (genMat_apply_of_ne / _of_not_admissible / genMat_swap), so the sum collapses to the two terms handled by jmStep_diag and jmStep_offDiag.
4. Index bookkeeping: L_k ↔ value k+1; rho(sigma_k) = genMat q (k+1); axialDist T (k+1) = content(cell of k+2) - content(cell of k+1); the swap sends cell of k+1 to cell of k+2 (cellOf_swapTableau_self/_succ), which is why d_k(sT) = q^{2(c+d)}.
5. Then barSymJMSum: sum_k (q^{2c_k} + q^{-2c_k}) over k = 0..n runs over ALL cells of lambda, giving cellContentCoshSum — independent of T, i.e. a scalar matrix. Discharges barSymJMSum_block_eigenvalue.
The theorem must live DOWNSTREAM (QJucysMurphy does not import SeminormalRep), same pattern as HoefsmitRepGeneral: prove it in QJucysMurphyEigen and retire the stub.


## CLOSED 2026-08-19 — PR #5290

`barSymJMSum_block_eigenvalue_of_pos` proved sorry-free + axiom-clean in
`QOU/SchurWeyl/QJucysMurphyEigen.lean`. `QJucysMurphy.lean` sorries 1 -> 0.

Chain, all sorry-free:
- `seminormalRep_qJM` — Ram (1997) Thm 4.1: L_k is diagonal with q^{2.content}
  at the cell holding k+1. Induction on k; step is genMat_conj_jmDiagVal.
- `seminormalRep_qJMInv` — by inverse-uniqueness from qJMInv_mul_qJM, no
  second induction.
- `sum_cellOf_range` — k |-> cellOf T (k+1) is a bijection range(n+1) -> cells.
  This is what makes the sum SCALAR: the per-k diagonals depend on T, the total
  does not.
- `seminormalRep_barSymJMSum` — Theta acts by sum over cells of (q^{2c}+q^{-2c}).
- packaging on Fin (dLambda lam) via seminormalRepFin + card_shape.

### Two corrections to the statement, both recorded rather than absorbed

1. **The stub was FALSE at N = 0**, and no amount of proof would have closed it.
   N - 1 = 0 in ℕ, so Theta = L_0 + L_0^{-1} = 1 + 1 |-> 2.1, while the empty
   partition's cellContentCoshSum is the empty sum 0; d_lambda >= 1 always
   (instNonemptyStandardYoungTableau) so the target algebra is nontrivial.
   Lean-checked as `barSymJMSum_block_eigenvalue_zero_false` — the refutation
   sits next to the theorem, not hidden behind the new `0 < N`.
   This is a DIFFERENT defect from the one qou-gjg6 recorded (`q != 0` vs the
   rep's genericity); that one was already fixed.
2. **The q hypothesis was too strong, not too weak.** `0 < q ∧ q != 1` excluded
   negative q for no reason; the proved version takes `q != 0 ∧ q^2 != 1`,
   which over ℝ says exactly *not a root of unity* — what seminormalRep takes.
