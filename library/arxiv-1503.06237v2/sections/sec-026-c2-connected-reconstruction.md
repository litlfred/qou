---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-026-c2-connected-reconstruction
section_title: "C.2 Connected reconstruction"
section_number: null
pages: 51-53
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
We’ll now compute the size of connected boundary region that we need to reconstruct
operators on the logical leg of the central ( n = 0) tensor. This is complicated by the
fact that our network is not translationally invariant; whether or not we can reconstruct
the center depends not only on the size of the boundary region we have access to but
also where it is. The “best case” situation is illustrated in ﬁgure 21.
We can compute the number of physical qubits in the best-case region by growing
the tree it bounds: we start with f1 = 3 and g1 = 0, and then proceed as before by
applying M repeatedly, being careful to remove two tensors at the ends at each layer.
– 49 –
Figure 21 . The best-case reconstruction of the center; we need to use only three “branches”
of the tree, and in the outer branches we can choose to push “inwards” every time.
Figure 22 . The worst-case reconstruction of the center; we are just barely not able to use
the second branch, so we need to use the third, fourth, and ﬁfth.
This tree thus obeys the modifed recursion relation
(fn+1
gn+1
)
=
(2 1
1 1
)(fn
gn
)
−
(0
1
)
, (C.7)
which has solution
(fn
gn
)
=
(2 1
1 1
)n−1(3
0
)
−
n−2∑
k=0
(2 1
1 1
)k(0
1
)
. (C.8)
After cutting oﬀ the tree at leveln the number of physical qubits in the best-case region
will be Nbest = 4fn + 3gn− 3, and by diagonalizing M we see that asymptotically
Nbest
Nboundary
→ 3 +
√
5
10 ≈.524. (C.9)
We can also study the “worst case” location of the region, which is shown in ﬁgure
22. To compute its size in the large n limit we only need to replace the initial condition
f1 = 3,g 1 = 0 by f1 = 4,g 1 = 0, and we ﬁnd
Nworst
Nboundary
→ 5 +
√
5
10 ≈.724, (C.10)
which reproduces (5.1).
We can connect this worst-case result to the “bad” sets of points from ﬁgure 16b
that prevent a general threshold for this code: these points are shown in ﬁgure 23.
– 50 –
Figure 23 . Locations of the “bad” points from ﬁgure 16b. If the worst-case region were
just a little smaller on the right it wouldn’t contain any of them so, it wouldn’t be able to
reconstruct the center.
Similar calculations are possible in the pentagon-hexagon code we introduced to
restore the threshold, we ﬁnd
Nbulk
Nboundary
→
{
3
√
6−4
38 ≈.088 n odd
3
√
6+4
38 ≈.299 n even
, (C.11)
with the two cases being whether the last layer is taken to be pentagons ( n even) or
hexagons (n odd). The rate is thus relatively small compared to (C.6), which suggests
that this code should be better protected against erasures, as indeed we ﬁnd. The
rate when n is odd is smaller since it throws in an extra level of hexagons without any
new logical legs. We can also compute the sizes of the best and worst case connected
reconstructions of the center, we ﬁnd
Nbest
Ntot
→ 6 +
√
6
20 ≈.422
Nworst
Ntot
→ 10 +
√
6
20 ≈.622. (C.12)
These are smaller than the pentagon results, as expected since the code is denser, and
are closer to the AdS/CFT value of 1 /2.
