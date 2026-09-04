---
# qou-hnri
title: 'Three different filtrations are all called depth: transcendence n, partition depth(lambda), curvature-rank k'
status: todo
type: task
priority: normal
created_at: 2026-09-04T13:59:16Z
updated_at: 2026-09-04T14:11:44Z
---

MEASURED 2026-09-04, and it has produced repeated errors including my own. THREE distinct filtrations in this corpus are all indexed by something called 'depth':

  1. TRANSCENDENCE / iterated-integral depth n   - G^(n) adjoins Li_n^q; tau_arch(G^(n)) subset P_n. Moved ADDITIVELY by the q-shuffle. (def:hq-bi-filtration, horizontal axis)
  2. KNOT / Hecke cell K                         - refined by the partition cell lambda_K |- n_K. (same block, vertical axis)
  3. GB / CURVATURE-RANK k = depth(lambda) - 1   - stratifies A = H_n(R,q); moved by the curvature 2-cocycle F, the Hecke + Yang-Baxter obstruction, read as string tension. (observations/confinement-curvature-rank.md)

Note (3)'s formula literally reads 'depth(lambda)' where depth is PARTITION depth - a third sense inside the definition of the third filtration.

COST ALREADY PAID: I read 'strict depth-0 convolution' as an order-0 truncation and reported bowtie_K as not being on the tower (it is, in both senses); then read the grid's summary cell 'preserves n' instead of the definition's n1+n2 containment and reported that the corpus has no depth-raising law (it does). Both were corrected the same day. The Frobenius curvature 2-cocycle is a live quadratic operator on filtration (3) and it is NOT established anywhere that it moves filtration (1) - a conflation that would be easy to make and hard to catch.

PROPOSED FIX, cheap: give the three distinct names in notation/notation-register-table3-data.md and notation-collisions.md - e.g. transcendence depth n, cell lambda_K, curvature-rank k - and stop using the bare word 'depth' for (3). This is option (F) of docs/audits/2026-09-04-depth-one-is-empty.md and is worth doing regardless of which attack route is chosen.

NOT A DUPLICATE, but cite the prior work. docs/audits/2026-08-16-three-gb-filtrations-one-name.md already covers a collision UNDER THE SAME SYMBOL J^bullet - three inequivalent readings of 'the GB filtration'. Checked: grep for iterated / transcendence / Li_2 / polylog in that audit returns ZERO, so it does not touch the transcendence-depth axis and this bean is complementary rather than a re-file.

AND THE PRIOR AUDIT IS MUCH STRONGER THAN A NAMING COMPLAINT: object 2 (image of the l-th power of the rewrite ideal) is PROVABLY ZERO for every l >= 1; object 3 (Coxeter-length span) fails the dimension count at n <= 3 and is excluded for EVERY n >= 2 by the 2026-08-26 supersession (bean qou-wjbd, no re-indexing repairs it); object 1 is 'not obviously well defined'. Its conclusion: all three readings of J^bullet are excluded and 'the citation does no work'.

CONSEQUENCE BEYOND NOTATION: the curvature-rank attack route (option C of docs/audits/2026-09-04-depth-one-is-empty.md) is DEAD - the curvature 2-cocycle F has no established filtration to be a cocycle on. And conj:two-filtration-bridge, which is the corpus's own statement of the owner's 'maps and operators are related to filtration' question, flags in its OWN statement that it presupposes the unestablished word-to-partition step.

So the notation drain should be scoped as: transcendence depth n, cell lambda_K, curvature-rank k - and it should record that the third is currently attached to no well-defined filtration.
