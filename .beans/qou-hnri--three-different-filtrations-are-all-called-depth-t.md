---
# qou-hnri
title: 'Three different filtrations are all called depth: transcendence n, partition depth(lambda), curvature-rank k'
status: todo
type: task
priority: normal
created_at: 2026-09-04T13:59:16Z
updated_at: 2026-09-04T13:59:17Z
---

MEASURED 2026-09-04, and it has produced repeated errors including my own. THREE distinct filtrations in this corpus are all indexed by something called 'depth':

  1. TRANSCENDENCE / iterated-integral depth n   - G^(n) adjoins Li_n^q; tau_arch(G^(n)) subset P_n. Moved ADDITIVELY by the q-shuffle. (def:hq-bi-filtration, horizontal axis)
  2. KNOT / Hecke cell K                         - refined by the partition cell lambda_K |- n_K. (same block, vertical axis)
  3. GB / CURVATURE-RANK k = depth(lambda) - 1   - stratifies A = H_n(R,q); moved by the curvature 2-cocycle F, the Hecke + Yang-Baxter obstruction, read as string tension. (observations/confinement-curvature-rank.md)

Note (3)'s formula literally reads 'depth(lambda)' where depth is PARTITION depth - a third sense inside the definition of the third filtration.

COST ALREADY PAID: I read 'strict depth-0 convolution' as an order-0 truncation and reported bowtie_K as not being on the tower (it is, in both senses); then read the grid's summary cell 'preserves n' instead of the definition's n1+n2 containment and reported that the corpus has no depth-raising law (it does). Both were corrected the same day. The Frobenius curvature 2-cocycle is a live quadratic operator on filtration (3) and it is NOT established anywhere that it moves filtration (1) - a conflation that would be easy to make and hard to catch.

PROPOSED FIX, cheap: give the three distinct names in notation/notation-register-table3-data.md and notation-collisions.md - e.g. transcendence depth n, cell lambda_K, curvature-rank k - and stop using the bare word 'depth' for (3). This is option (F) of docs/audits/2026-09-04-depth-one-is-empty.md and is worth doing regardless of which attack route is chosen.
