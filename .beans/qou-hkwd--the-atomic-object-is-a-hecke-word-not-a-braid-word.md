---
# qou-hkwd
title: 'RENAME TRANCHE: the atomic object is a Hecke word, not a braid word — 5 mathematically-false lines, not a 672-file rename'
status: in-progress
type: milestone
priority: high
created_at: 2026-09-06T12:25:33Z
updated_at: 2026-09-06T12:25:33Z
---

Owner instruction 2026-09-06: "do a separate rename tranche. coordinate with all
open PRS relevant."

ROOT (issue #6941 §10). atom_braid_word_3A returns (c, d, gen_idx) and d takes
FOUR values at the proton q0:
    d = 0                     -> sigma       positive crossing        BRAID
    d = -h  = -0.2090602988   -> sigma_inv   negative crossing        BRAID
    d = -h/2 = -0.1045301494  -> averaged    (sigma+sigma^-1)/2       NOT
    d = -0.1044582478         -> averaged_wt colour-weighted          NOT
0 of 14 atoms protium->Fe-56 is free of the last two, so the object lives in
H_n(q) and outside the image of B_n. Its closure is not defined.

WHY NOT A RENAME. "braid word" appears in 2169 files; atom_braid_word_3A in 672.
MOST ARE CORRECT -- the trefoil really is sigma_0^3 in B_2, the Borromean rings
really are (sigma_0 sigma_1^-1)^3 in B_3. A blanket rename would corrupt true
statements to fix false ones.

THE ACTUAL DEFECT is much smaller: lines asserting the ATOMIC object lives in a
BRAID GROUP. That is wrong as MATHEMATICS, not naming. Detector:
computations/audits/braid_vs_hecke_word_audit.py, 3/3.

  5 DEFECTS
    mass-theory/per-braid-mass-tower.md:1              "W in B_{3A} the atomic braid"
    mass-theory/graded-hecke-energy-truncation-bound.md:1  "the CLOSURE of B_K in B_n"  <- sharpest
    mass-theory/conj-atom-braid-exterior-algebra.md:2  "T_w(Z,N) in B_{3A}"
    mass-theory/sigma-shell-from-beta-chain-derivation.md:1
    mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md:2
  1 SIBLING-OWNED, not touched
    mass-endomorphism/atomic-mass-gb-nf.md:3  -> PR #6821
  24 lines / 7 files VERIFIED CORRECT and left alone

DETECTOR BLIND SPOT, found and fixed before shipping: v1 keyed on the word
"atom" and missed graded-hecke-energy-truncation-bound, which says
"the closure of $\mathcal{B}_K \in B_n$" and never says "atom". The symbol IS
the subject. 4 -> 5 defects after the fix.

COORDINATION: #6821 owns the strand-count question on the same object and has a
three-way decision with the owner. Braid-vs-Hecke is PRIOR to it: whichever
count wins, "in B_n" is wrong on the GROUP.
