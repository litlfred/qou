---
# qou-t8qh
title: 'SW-JM: q-Jucys-Murphy eigenvalue (Ram 4.1) — the last SchurWeyl sorry'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T07:41:30Z
updated_at: 2026-08-19T08:03:10Z
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
