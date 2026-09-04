---
# qou-ox7v
title: 'R1: is the depth axis the shuffle filtration on H_q, or the K-theory weight tower? A rank count says they cannot match as graded algebras'
status: todo
type: task
priority: high
created_at: 2026-09-04T20:45:27Z
updated_at: 2026-09-04T20:45:28Z
---

THE ROAST FINDING of epic qou-2q85, and it hits the two routes I ranked first. docs/audits/2026-09-04-roast-of-the-six-attack-routes.md.

I recommended ROUTE B as 'build H_q^(1,K), then the shuffle squares it into H_q^(2,K) = volume'. That reads depth 2 as a PRODUCT of depth-1 things. The K-theory side of the corpus's own dictionary says the opposite:

  Bloch-Suslin complex:   B(F) --delta--> Lambda^2 F^x,   delta[z] = z ^ (1-z)

and K_3^ind is captured by the KERNEL of delta, not by the image of a product. Under rem:k-theory-period-rosetta's matching (depth 1 <-> K_1(F) = F^x, depth 2 <-> K_3^ind(F) tensor Q), the depth-2 object sits OVER Lambda^2(depth-1) as a kernel. The multiplication is the map it is the kernel OF, and it points the other way.

TWO FURTHER STRUCTURAL PROBLEMS WITH 'SQUARE IT':
  (i) Lambda^2 is ANTISYMMETRIC, so x ^ x = 0. Squaring a SINGLE depth-1 element gives zero on that side; what lands is z ^ (1-z), two DISTINCT units. 'Square a depth-1 object' is the one case that vanishes.
  (ii) THE RANKS DO NOT MATCH, and not marginally. Borel: for a number field F with r_1 real and r_2 complex places, rank(K_3^ind(F) tensor Q) = r_2 - FINITE, and equal to 1 for an imaginary quadratic field such as the Q(z_K) of a hyperbolic knot shape. Meanwhile F^x is infinite rank and so is Lambda^2 F^x. A graded object whose degree-2 piece is the square of its degree-1 piece cannot have a rank-1 degree-2 piece over an infinite-rank degree-1 piece.

WHAT THIS DOES AND DOES NOT ESTABLISH. It does NOT prove route B fails: the H_q shuffle filtration and the K-theory weight tower are different structures, and the rosetta matching them says of itself that it is 'an analogy that becomes a theorem at low depth and a conjecture at high depth, not a fully-established equivalence at all depths'. What it establishes is that THE TWO CANNOT BE MATCHED AS GRADED ALGEBRAS - the shuffle's n1+n2 additivity on H_q and the weight grading on K_{2n-1}^ind disagree at the first place one can check them.

SO THIS IS THE QUESTION TO SETTLE FIRST, before building anything: which structure is the depth axis actually indexed by? It is a reading question over objects that already exist, cheaper than any construction on the route list, and BOTH route A (qou-jopk) and route B (qou-wnhk) change shape depending on the answer.

CITED, NOT MEASURED HERE: Borel's rank theorem and the Bloch-Suslin complex are standard and are taken from the literature, not derived in this corpus. The corpus-side facts (the rosetta's dictionary rows, its self-described conjectural status, the shuffle's additivity) ARE measured - see the audit.
