---
# qou-ox7v
title: 'R1: is the depth axis the shuffle filtration on H_q, or the K-theory weight tower? A rank count says they cannot match as graded algebras'
status: completed
type: task
priority: high
created_at: 2026-09-04T20:45:27Z
updated_at: 2026-09-04T21:48:10Z
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

SETTLED 2026-09-04. THE ANSWER IS 'BOTH, AND THEY ARE CONSISTENT' - AND MY OWN R1 WORRY IS RETRACTED.

R1 asked whether the depth axis is the H_q shuffle filtration or the K-theory weight tower, claiming on a rank count that they 'cannot match as graded algebras'. THAT CLAIM WAS WRONG. They match. My mismatch: I compared the WHOLE weight-2 graded piece against K_3^ind, which is only ONE SUMMAND of it.

THE CORPUS STATES THE RESOLUTION ITSELF, at appendix-surreals/k-theory-period-rosetta.md:22 - a line I quoted earlier in this same session and did not act on:

  'K_*^ind denotes the indecomposable part of higher K-theory, MODULO THE IMAGE OF PRODUCTS OF LOWER K-GROUPS.'

So the weight-2 piece SPLITS: a DECOMPOSABLE part (products of weight-1 elements, log * log = Lambda^2 or Sym^2 of K_1, infinite rank) and an INDECOMPOSABLE part (K_3^ind, Bloch-Wigner, THE VOLUME, rank r_2 = 1 for an imaginary quadratic field). Both live in weight 2; they are different summands. The rank 'disagreement' I found was me comparing a summand to the whole.

THE CONSEQUENCE, AND IT IS STRONGER THAN R1'S: ROUTE B (qou-wnhk) IS DEAD. The shuffle-square of a depth-1 object lands in the DECOMPOSABLE part - which is EXACTLY what the indecomposable quotient discards. Squaring cannot reach the volume, not because the gradings disagree (they do not) but because squaring produces precisely the summand the target is DEFINED to exclude.

FORMALIZED: content/quantum-observable-universe/lean/QOU/Eightfold/IndecomposableQuotientPrune.lean, lean-direct exit 0, 4 theorems sorry-free (three need only [propext, Quot.sound]). For any bilinear mul : A_1 ->L A_1 ->L A_2, every product mul a b is zero in A_2 / decomposable(mul). Nothing about knots, periods or q is used - that is the point; the obstruction is what 'indecomposable' MEANS.

NON-VACUITY CHECKED, both directions: over Z with real multiplication, mkQ (a*b) = 0 (the prune bites); with the ZERO multiplication the decomposable part is bot and 1 SURVIVES in the quotient (so the theorem is not true by the quotient collapsing).

SCOPE. (b) structural exclusion of SQUARING as a route to an indecomposable target - NOT of route B's ingredients. Building H_q^(1,K) may still be worth doing for its own sake; what is excluded is reaching the volume FROM it by multiplication. It says NOTHING about route A (qou-jopk): the coproduct's 2=2+0 split is not a product of two degree-1 elements, so this theorem does not touch it. Route A is now the only surviving depth-crossing route on the epic.

Audit: docs/audits/2026-09-04-depth-one-is-empty.md and the roast; epic qou-2q85.
