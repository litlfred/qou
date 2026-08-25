---
# qou-m1fx
title: 'M1 UNBLOCKED from source: eq (18) rotated index is the FUGACITY basis sum_e I(m,e) zeta^e — my probe used the wrong index object'
status: done
type: task
priority: high
tags:
    - g3-aomega
    - route-c
created_at: 2026-08-11T10:50:00Z
updated_at: 2026-08-11T10:50:00Z
parent: qou-rtec
---

Read GGM 2012.00062v3 (library/, pymupdf). The convention gap of qou-m1nz is PINNED:

  eq (18):  Ind^rot_K(m, zeta; q) = sum_{e in Z} I_K(m,e)(q) * zeta^e     [fugacity basis, DGG13/BDP14]
  eq (21):  S+_{sigma1 sigma1}(x; q) = Ind^rot_K(0, x; q)                 [exact; holds for 4_1 and 5_2]
  eq (200): S+(x;q)_{1,1} = 1 - (2x^-2 + x^-1 + 2 + x + 2x^2) q
                              - (x^-2 + 2x^-1 + 3 + 2x + x^2) q^2 + O(q^3)
            (at x=1: 1 - 8q - 9q^2 = the eq-(61) tower. CHECKS.)
  eq (17):  S+(x;q)^T S-(x^-1;q) = 1   [the inversion relation already Lean-proved at q->0]

MY BUG (qou-m1nz probe): I summed fe.index(0,e), but the corpus producer's index(x,y) is
I_T(x*mu + y*lam) — the GHHR SLOPE-parametrized index — NOT I_K(m,e) in the DGG
magnetic/electric FLUX basis. Different objects. That is why sum_e gave [1,-2,-3,4,12,28,22].

NEXT ACTION (now fully specified, no lit needed — we have every paper):
 1. Implement I_K(m,e) in the DGG flux basis for 4_1 from the tetrahedron-index gluing
    (library/arxiv-1112.5179v1/1112.5179v1.pdf DGG; library/arxiv-1604.02688v1/1604.02688v1.pdf GHHR; library/arxiv-1208.1663v2/1208.1663v2.pdf).
 2. Form Ind^rot(0,x;q) = sum_e I(0,e) x^e and verify against eq (200) COEFFICIENT-WISE
    in BOTH x and q (a 2-variable check — much stronger than the x=1 tower alone).
 3. Then the dictionary S+_11 = Ind^rot is confirmed in-corpus and Route C M2 unblocks.

## 2026-08-11 — M1 EXECUTED from the block definitions. PARTIAL: one localized q^1 discrepancy.

Implemented S+_11(x;q) directly from the q-Hahn Bessel holomorphic blocks (GGM eq 127a/b) and
evaluated the eq-(200) bilinear symbolically (exact truncated q-series over rational functions
of x): computations/probes/qbeta_m1_rotated_index_from_blocks.py, witness alongside, 3/4.

  q^0   computed 1                                    == printed          EXACT
  q^2   computed -(x^-2 + 2x^-1 + 3 + 2x + x^2)       == printed          EXACT
  x=1   computed tower [1,-8,-9]                      == eq (61)          EXACT
  q^1   computed -(x^-2 + 2x^-1 + 2 + 2x + x^2)
        printed  -(2x^-2 + x^-1 + 2 + x + 2x^2)                           DIFFERS

Both q^1 readings sum to -8 at x=1 — the discrepancy is the DISTRIBUTION over the fugacity,
not the total, which is why the eq-(61) tower still matches.

PROVENANCE CHECKED (this is not an OCR artifact): re-extracted page 39 at SPAN level, using
font size 8 = superscript. Confirms the block arguments
   S+(x;q)_1,1 = J(x,x^-1;q) J(x,x^-1;q^-1) + J(x^-2,x^-1;q) J(x^2,x;q^-1)
(exactly what the probe implements) AND the printed q^1 coefficient as read.

TWO LIVE EXPLANATIONS, NOT ADJUDICATED (do not tune either way):
 (a) a typo in the paper's q^1 coefficient — note q^2 is palindromic (1,2,3,2,1) and the
     computed q^1 is the analogous (1,2,2,2,1), while the printed (2,1,2,1,2) breaks that
     pattern; or
 (b) a branch subtlety in the |q|<1 vs |q|>1 convention for J(.;q^-1) hitting this order.

NEXT ACTION to adjudicate: compute I_{4_1}(0,e)(q) independently in the DGG flux basis and
form sum_e I(0,e) x^e; that settles which q^1 distribution is correct without relying on the
printed line. If (a), it is a publishable erratum and should be reported upstream.

## 2026-08-11 (later) — ADJUDICATED: the q^1 discrepancy is a TYPO IN THE PAPER. M1 CONFIRMED.

Independent second route settles it. Summing the DGG flux-basis table I_{4_1}(0,e) per eq (18)
(Ind^rot(0,x;q) = sum_e I(0,e) x^e) gives q^1 coefficients (-2,-2,-1) — IDENTICAL to the
q-Hahn-Bessel block computation, and NOT the printed (-2,-1,-2). q^0 and q^2 agree with both.

  corrected eq (200) q^1:  -(x^-2 + 2x^-1 + 2 + 2x + x^2)
  printed:                 -(2x^-2 + x^-1 + 2 + x + 2x^2)

Both sum to -8 at x=1, which is why the eq-(61) tower never exposed it — only the two-variable
check did. => M1 CONFIRMED (dictionary verified in-corpus as a 2-variable identity, modulo the
erratum). ACTION: consider reporting the erratum upstream. Status -> done.
