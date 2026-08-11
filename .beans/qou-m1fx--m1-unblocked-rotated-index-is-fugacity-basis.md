---
# qou-m1fx
title: 'M1 UNBLOCKED from source: eq (18) rotated index is the FUGACITY basis sum_e I(m,e) zeta^e — my probe used the wrong index object'
status: todo
type: task
priority: high
tags:
    - g3-aomega
    - route-c
created_at: 2026-08-11T10:50:00Z
updated_at: 2026-08-11T10:50:00Z
parent: qou-rtec
---

Read GGM 2012.00062v3 (uploads/, pymupdf). The convention gap of qou-m1nz is PINNED:

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
    (uploads/1112.5179v1.pdf DGG; uploads/1604.02688v1.pdf GHHR; uploads/1208.1663v2.pdf).
 2. Form Ind^rot(0,x;q) = sum_e I(0,e) x^e and verify against eq (200) COEFFICIENT-WISE
    in BOTH x and q (a 2-variable check — much stronger than the x=1 tower alone).
 3. Then the dictionary S+_11 = Ind^rot is confirmed in-corpus and Route C M2 unblocks.
