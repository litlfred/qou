---
# qou-7xt3
title: 'Orbit-size classification: the 3-cell configuration to size map (1/2/3/6) with the size-2 hook'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T02:59:25Z
updated_at: 2026-11-17T11:34:45Z
parent: qou-1oif
---


## The map (exact enumeration, 2026-08-15)

Orbit size = number of standard fillings of the 3-cell configuration holding k, k+1, k+2.
Determined by the comparability relation among the three cells (a <= b iff same row with
a left of b, or same column with a above b):

  total order on all 3 (a chain)        -> 1   e.g. 3-in-a-row, 3-in-a-column,
                                                (0,0)(0,1)(1,1)
  exactly one INCOMPARABLE pair (hook)  -> 2   e.g. (0,0)(0,1)(1,0)
  exactly one COMPARABLE pair           -> 3   e.g. any two sharing a row/column
                                                (adjacent or not) + one unrelated
  antichain (no comparable pair)        -> 6

So the orbit size is 6/|number of linear extensions|... precisely: it IS the number of
linear extensions of the induced poset on the three cells.

USE: this is the classification step (ii) needs. The identities are already proved for
every size — 1 (scalars), 2 (seminormalBlock), 3 (Orbit3Braid), 6 (Orbit6Braid).

DESIGN NOTE, and the real blocker: there is NO Lean object for "the orbit" yet. The
s_k-action (swapTableau) is partial — defined only under SwapAdmissible — so the orbit is
a connected component under partial moves, not a group orbit. Options before writing the
classification:
  (a) define the orbit as a Finset (SYT lam) closed under the available moves;
  (b) index by the linear extensions of the 3-cell poset and build the correspondence
      directly, skipping a general orbit notion;
  (c) sidestep orbits: define rho on ALL of SYT lam by the trichotomy (axialDist_trichotomy
      already gives the per-generator case split) and prove the relations globally, with the
      orbit-local identities used only as the algebraic content.

(c) is probably the shortest route to discharging hoefsmit_seminormal_rep, since the
per-orbit basis correspondence — the thing that makes Orbit3Braid/Orbit6Braid's explicit
index orderings usable — is exactly what (a) and (b) force one to build.


## ROUTE (c) TAKEN 2026-08-15 — definition lands, compiles first try

New sorry-free file QOU/SchurWeyl/SeminormalRep.lean:

  offDiag q d -- the size-2 pair's off-diagonal, carrying the orientation convention
                 (negative-distance member is "first": its column gets 1 + a(d)a(-d), the
                 other the plain 1)
  genMat q k  -- the matrix of sigma_k indexed by StandardYoungTableau mu on BOTH sides,
                 so there is no re-indexing and hence no basis correspondence to justify
  + genMat_diag / genMat_of_not_admissible / genMat_apply_of_ne / genMat_swap

The diagonal is a(axialDist T k) UNIFORMLY. That is what makes the trichotomy a case split
on block SIZE only: at distance +-1 it is the size-1 scalar q resp. -q^-1
(seminormalParam_one/_neg_one), at |d| >= 2 it is a seminormalBlock diagonal. Each column
has at most two nonzero entries.

Indexing by SYT directly is the whole point of (c): (a) and (b) both force construction of
the per-orbit basis correspondence that makes Orbit3Braid/Orbit6Braid's explicit index
orderings usable, and that correspondence is the expensive part. Here there is no
re-indexing at all.

STILL OPEN: the Hecke relations for genMat -- quadratic, far commutation, braid -- proved
GLOBALLY, with the orbit-local identities supplying the algebraic content. That is what
route (c) buys the chance to do and it is not done. hoefsmit_seminormal_rep keeps its
Ref'd sorry.

## Round 64 Progress (`lane-e667`)
- Formalized `qou-7xt3`, `qou-ck0g`, `qou-em1j`, `qou-kbjc`, `qou-w0zn` in `QOU.Foundations.ThreeCellPosetOrbitSizeBarSymEigenvalueLengthGeneratingQBinomialUpDownWeyl` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = 13e718201144523610e11912018cdb123e6155b3`, `COMMIT2 = 06940a10b90934e8a8d7233d592147be01aa5979`, `scriptHash = 01e1202f7b26`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8323 (`ready-to-merge`, `release`, `ready: 06940a10b90934e8a8d7233d592147be01aa5979`).
- Keeping bean at `status: in-progress` pending merge and verification.
