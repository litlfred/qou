---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-015-43-a-symmetry-of-the-space-of-angle-structures
section_title: "A symmetry of the space of angle structures"
section_number: 4.3
pages: 18-20
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
---
1σ−1
2 as shown
on the right of Figure 2. Moving the lone half-twist up so that it occurs halfway along the σ1
half-twists reveals an order 2 symmetry of Xp — rotate about a horizontal line through the lone
half-twist. This involution induces a symmetry on the triangulation τp — rotate the tetrahedra in
Figure 8 about a horizontal line and take s to itself. This symmetry will respect angle structures:
Proposition 4.3. An involution ι :τp→τp that ﬁxes s and takes w′
i to wp−i by matching up their
R, B, and D edges induces a symmetry of A(τp).
Proof. Let θ∈A (τp). According to Deﬁnition 3.4, to verify that ιθ is also in A(τp), we need to
check that the sum of the dihedral angles at each edge of of Xp is 2π, when the angle measure is
given by ιθ. Thus, it is enough to verify that ιθ satisﬁes the edge equations listed in Observation 4
where
ιθ⋆s =θ⋆s, ιθ ⋆w′
i =θ⋆wp−i, and ιθ⋆wi =θ⋆w′
p−i
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 19
for ⋆ =R,B , and D.
The ﬁrst equation describes the angle sum around the red edge of Xp, which consists of all R
edges and the red diagonals ofw′
0 andwp. The involution ι permutes these edges, thereby permuting
the terms of the sum:(p−1∑
i=0
2ιθRw′
i
)
+
( p∑
i=1
2ιθRwi
)
+ 2ιθRs +ιθDw′
0 +ιθDwp =
( p∑
i=1
2θRwi
)
+
(p−1∑
i=0
2θRw′
i
)
+ 2θRs +θDwp +θDw′
0 = 2π,
so the ﬁrst edge equation is satisﬁed by ιθ. The terms in the next two sums, those for the degree-5
edges, are also permuted by ι, so those equations are satisﬁed by ιθ as well.
Something a little diﬀerent happens with the degree-4 edges (only present when p > 1). To
conﬁrm the ﬁnal equation of Observation 4, for example, we need to examine
ιθDs +ιθBw′
p−1 +ιθBwp−1 +ιθDwp−2,
but this sum is just
θDs +θBw1 +θBw′
1 +θDw′
2,
which equals 2π by the penultimate equation in Observation 4. In this instance, the involution takes
the terms in one sum to the terms in another, eﬀectively permuting the edge equations themselves.
The same happens for the remaining degree-4 equations. □
Corollary 4.4. Let ι :τp→τp be as in Proposition 4.3 and let k be such that p = 2k if p is even
and p = 2k + 1 if p is odd. Positive angle structures θ∈A (τp) with the property that ιθ = θ have
w′
i∼=θ wp−i and thus satisfy a simpler list of edge equations:
( p∑
i=1
4θRwi
)
+ 2θRs + 2θDwp = 2π (4)
2θBwp + 2θDw1 +θBs = 2π (5)
2θBwp + 2θDwp−1 +θBs = 2π (6)
θDwi−1 +θBwi +θBwp−i +θDwp−(i+1) = 2π for i = 2,...k (7)
θDwp−(i−1) +θBwi +θBwp−i +θDwi+1 = 2π for i = 1,...k (8)
θDs +θBwp−1 +θBw1 +θDwp−2 = 2π. (9)
In addition,
θDwp =θDs and θDwi =θDwp−i for i = 1,...k. (10)
These equations hold for all p≥ 1, with one exception. When p = 1, Equation (6) reads: 2θBw1 +
2θDs +θBs = 2π.
Proof. By assumption, ιθ⋆w′
i = θ⋆w′
i for ⋆ = R,B , and D, and, by deﬁnition, ιθ⋆w′
i also equals
θ⋆wp−i, soθ⋆w′
i =θ⋆wp−i, and the tetrahedraw′
i andwp−i have the same angle assignments underθ,
so w′
i∼=θ wp−i. This isometry allows us to obtain Equations (4)–(9), by replacing w′
i with wp−i in
the edge equations of Observation 4 and eliminating redundancies.
To obtain Equation (10) for p = 1, replace w′
0 with w1 in the p = 1 equation of Observation 5,
which shows
θDs−θDw1 =θDw1−θDs,
soθDw1 =θDs. If p> 1, Equations (5) and (6) imply that θDw1 equals θDwp−1, which, because of
the isometry, equals θDw′
1, so the diﬀerence θDw1−θDw′
1 equals 0 as do all odd-index diﬀerences
listed in Observation 5. Replacing w′
i with wp−i, yields Equation (10) for odd i. The remaining
20 BARBARA NIMERSHIEM
equations are derived diﬀerently depending on the parity of p. As noted in Observation 5, when p is
odd, all diﬀerences are equal (in this case, equal to 0), so, after replacingw′
i withwp−i, Equation (10)
holds for all i whenp is odd. To see that Equation (10) also holds when p andi are even, note that
θDwp−θDs =θDw2−θDw′
2 =θDwp−2−θDw′
p−2 =θDs−θDw′
0 =θDs−θDwp
so θDs =θDwp. Thus, all diﬀerences in Observation 5 with even index are also 0 and replacing w′
i
with wp−i results in Equation (10). □
