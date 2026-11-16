---
# qou-018h
title: Star-Gram tr_M(a b*) is POSITIVE -- the Lorentzian reading was a wrong-pairing artifact; metric arc unblocked
status: in-progress
pr: 8193
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T13:34:15Z
updated_at: 2026-11-16T20:41:00Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08. Owner's hypothesis ("wrong
eigenbasis? needs q-deformation?") was RIGHT, and the fix is exact.

## THE FINDING

I built the Gram matrix as the BILINEAR form G_ij = tr_M(b_i b_j) and got
signature (5,1) under C and (4,1)+null under D -- and concluded the framework's
natural object is a spacetime/causal structure. WRONG PAIRING.

The Hecke *-structure is T_w* = T_{w^-1}: the basis element of the INVERSE WORD.
On the NF basis {gamma, s0, s1, L+, L-, e-} that simply swaps L+ <-> L- and
fixes the rest (gamma, s0, s1 are involutions; e- = s0 s1 s0 is a palindrome).

    S_ij = tr_M(b_i . b_j*)
      convention C:  all six eigenvalues POSITIVE       signature (6,0,0)
      convention D:  one zero, five positive            signature (5,0,1)
      symmetry defect 0.0 in both

SAME EIGENVALUE MAGNITUDES: +/-0.855067 becomes +0.855067 fourfold under C;
+/-0.752702 becomes +0.752702 fourfold under D. The star flips exactly the sign
of the antisymmetric direction, which is what a *-structure is FOR.

NOTE the earlier failed attempt and why: I first tried tr_M(b_i b_j^{-1}) using
the ALGEBRA inverse (sigma^-1 = sigma - h). That is a DIFFERENT element from
T_{w^-1}, and it gave a non-symmetric form (defect 0.3216) with signature (5,1)
and a tiny negative -0.008144. The 92x shrink of the negative eigenvalue was the
clue that the star was nearly right; the missing piece was using the inverse
WORD, not the inverse ELEMENT.

## RETRACTION

GramSignature.lean's headline "the framework's natural object is a causal
structure, not a metric space" is WITHDRAWN, in-file. The block analysis is
retained because it explains BOTH signatures from one decomposition: the M_2 of
the (2,1) block contributes (3,1) under the bilinear form and (4,0) under the
star form.

## WHAT IT UNBLOCKS

qou-5uj7 step 3 was blocked on the signature. It no longer is:
  * Under D the star form is positive SEMIdefinite, and the ONLY defect is the
    row-cap null direction (the (1^3) q-antisymmetrizer, y_(1^3) = 0). Quotient
    by the radical -> genuine POSITIVE-DEFINITE inner product, which is exactly
    what a Rieffel Lip-norm requires.
  * Under C it is positive DEFINITE outright, because y_(1^3) = 0.0227 != 0
    keeps that direction alive. Clean consistency check: D's degeneracy is
    PURELY the row cap and nothing else.

## LEAN (added, build clean, 0 warnings)

  starform_M2_sum_of_squares   tr(A A^T) = a^2+b^2+c^2+d^2 on M_2
  starform_M2_nonneg           >= 0
  starform_M2_pos_of_ne        > 0 unless A = 0
  markov_star_nonneg           positivity of the whole form reduces to y_lambda >= 0,
                               degenerate exactly where y_lambda = 0

So the general statement is: the Markov star form is positive semidefinite iff
all Markov weights are nonnegative, and its radical is the span of the zero-weight
blocks. Under D that is the single block (1^3).

## WHAT IT DOES **NOT** DO

It does NOT move the colour-weight blocker. The bond family reaches only the
DIAGONAL of the V_(2,1) block; the projectors are the OFF-DIAGONAL. That
confinement is what traps t in [z-h, z], and it is a statement about which
matrix entries a bond WORD can reach -- unchanged by the choice of pairing.

OPEN, and now well-posed (the owner's q-deformation instinct may still bite
here): the (2,1) symmetric/antisymmetric split above was taken CLASSICALLY. The
Hecke eigenvalues are q and -q^-1, an ASYMMETRIC pair, not +/-1. Whether the
q-deformed grading changes which matrix entries the bond family can reach is a
real and unanswered question.

## NEXT
  [ ] quotient by the radical, build the Rieffel Lip-norm L(a) = ||D_grad a||
      on the resulting positive-definite space
  [ ] check the Lip-norm axioms (Leibniz; kernel = scalars)
  [ ] then compute d and compare to step counts -- remembering the target
      "d = Reeb step count" only holds as q -> infinity, since D_grad mixes
      gradient and Reeb at 9:1

## Round 53 Progress (PR #8193)
- [x] Added `starform_M2_sym_antisym`, `starform_sub_traceform_M2`, `invword_swap_flips_antisym_mode`, `invword_swap_restores_positivity`, and `markov_star_quotient_pos_of_radical` to `folio/quantum-observable-universe/lean/QOU/QBeta/GramSignature.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified 80-dps `M_2` involution sign flip and convention-D quotient positivity in `computations/probes/route89_staircase_wpdb_stargram_probe.py` (`computations/probes/route89-staircase-wpdb-stargram.witness.json`).
- [ ] Await CI verification and Merge Manager merge of PR #8193 (`9d88b10b75877699bcfe0134c2f9a3d95a32edf4`).
