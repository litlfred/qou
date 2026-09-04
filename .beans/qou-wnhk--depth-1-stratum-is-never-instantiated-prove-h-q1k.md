---
# qou-wnhk
title: 'Depth-1 stratum is never instantiated: prove H_q^(1,K) is empty via the K-theory rosetta, or find it'
status: todo
type: task
priority: high
created_at: 2026-09-04T13:59:16Z
updated_at: 2026-09-04T14:11:44Z
---

MEASURED 2026-09-04. The +2 mechanism EXISTS - def:hq-bi-filtration's compatibility table states the q-shuffle is depth-ADDITIVE: H_q^(n1,K1) *_q H_q^(n2,K2) subset of + H_q^(n1+n2,K'). Exactly one of its five listed operations moves depth and it is the product (coproduct splits; bar involution, Markov trace and braid action all preserve). I had reported the opposite and it was wrong.

SO A QUADRATIC TERM MAPS n -> 2n, i.e. <= +2 from a depth-1 level. That is the owner's reading and it is correct.

BUT IT CANNOT FIRE FROM THE INTERFACE LAYER: bowtie_K and the whole convolution layer are depth 0, and 0+0 = 0. Squaring depth-0 objects stays at depth 0. Reaching depth 2 by squaring needs a DEPTH-1 input.

MEASURED: THE DEPTH-1 STRATUM IS NEVER INSTANTIATED. def:hq-bi-filtration's own low-(n,K) examples grid has columns for H^(0,K), H^(2,K), H^(3,K) and SKIPS n=1. grep for 'mathcal{H}_q^{(1' across every .md and .lean in content/ returns ZERO hits. So the additive law has nothing to add. THE MISSING OBJECT IS A DEPTH-1 STRATUM, NOT A DEPTH-RAISING LAW.

AND THERE MAY BE A STRUCTURAL REASON. The same block's rem:k-theory-period-rosetta matches depth n to the Beilinson regulator on K_{2n-1}^ind(Qbar). Under that dictionary depth 1 is K_1^ind - and K_1(F) = F^x is entirely DECOMPOSABLE, so its indecomposable part is trivial. If the rosetta holds, depth 1 is empty BY CONSTRUCTION and the missing n=1 column is correct rather than an oversight.

THIS IS A HYPOTHESIS ABOUT THE CORPUS'S OWN DICTIONARY, NOT A THEOREM. Proving it is the formalize-first move: it converts today's gap into a scope-(b) exclusion and prunes every route that hoped to square a depth-1 object. REFUTING it is better - it hands over the missing input and opens the 1+1=2 route.

Depth 2 is already populated and real: figure-eight 4_1 at H_q^(2,K) is 2*Cl_2(pi/3) = Vol(4_1), marked confirmed in the grid.

Audit: docs/audits/2026-09-04-depth-one-is-empty.md, option (B), recommended first.

REFUTED MY OWN HYPOTHESIS, same hour, by the rosetta's own table. I inferred 'K_1^ind is trivial so depth 1 is empty by construction'. rem:k-theory-period-rosetta's dictionary row reads: 1 | log_q | K_1(F) via Bloch logs | Dirichlet regulator. That is PLAIN K_1(F) = F^x, NOT the indecomposable part. 'ind' means 'modulo the image of products of lower K-groups' and at n=1 there are no lower K-groups, so the qualifier is vacuous there. I applied the general K_{2n-1}^ind formula past the point where its qualifier means anything.

WORSE FOR THE HYPOTHESIS: the rosetta's STATUS column marks depth 1 'theorem' - Dirichlet regulator + Baker-Wuestholz on log-linear independence - making it the MOST established row in the table, better than depth 2 ('theorem (essentially)') and far better than depth 3 ('mostly conjectural').

SO DEPTH 1 IS POPULATED IN PRINCIPLE AND EMPTY ONLY IN PRACTICE. Grouplike log_q, K-group F^x, field of definition Q(z_K) for a Bring-embeddable knot with shape z_K - all supplied. What has never been built is the KNOT-INDEXED stratum H_q^(1,K).

THIS UPGRADES THE BEAN FROM 'PROVE THE EXCLUSION' TO 'BUILD THE OBJECT'. Construct H_q^(1,K): a log_q-level object indexed by the cell lambda_K over Q(z_K). Then the shuffle squares it into H_q^(2,K) = volume, which is exactly the owner's <= +2.

THE MECHANISM IS VISIBLE IN THE TARGET FUNCTION. Bloch-Wigner is D(z) = Im Li_2(z) + arg(1-z) log|z|; the SECOND TERM is literally a product of two depth-1 objects landing in depth 2 - the shuffle-square, already formalised in the corpus as QOU.Knot.KummerRadial.kummer (and stated at mass-theory/kummer-bloch-wigner-identity.md).

INDEPENDENT CORROBORATION that depth 1 is thin on the knot axis: conj:two-filtration-bridge's d_II(lambda) is 2 (self-conjugate) / 3 (chiral pair) / min(depth_GB, 2*ceil(n/2)) otherwise - never 1 except at the trivial cell lambda=(1).
