---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-016-5-the-maximal-volume-occurs-at-a-positive-angle
section_title: "The maximal volume occurs at a positive angle structure"
section_number: 5
pages: 20-23
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
---
Corollary 4.2 shows that the space of positive angle structures on each triangulationτp is nonempty,
so we have accomplished the ﬁrst step of the Casson-Rivin program described by Futer and Gu´ eritaud
in [5] and summarized in 3.3. In this section, we complete the program, proving the main result.
Theorem 5.1. Let Lp be the closure of the 3-braid C 2σp
1σ−1
2 and Xp be its complement in the
3-sphere. Then there is an ideal triangulation of Xp that is geometric.
Proof. Let τp be the triangulation deﬁned in 2.4. By Corollary 4.2, A(τp)⁄=∅, which means the
volume functionalV attains its maximum on the compact setA(τp), say at the point α. A maximal
point has two important properties. The ﬁrst was proved in Lemma 3.2.
Property 1. Ifα is maximal and assigns an angle in {0,π} to a tetrahedron, then the tetrahedron
must be ﬂat, i.e., its angles are 0, 0, π in some order.
The second important property derives from a symmetry of the coordinates of a maximal point.
Let the involution ι : τp→ τp be as in Proposition 4.3, so ι ﬁxes s and takes w′
i to wp−i. Then ι
induces a symmetry on A(τp), which rearranges the coordinates of an angle structure tetrahedron
by tetrahedron, so, just as in Observation 3, V(ια) = V(α). Thus, if α is maximal, so is ια,
but maximal points are unique by Proposition 3.1, so ια = α, and Corollary 4.4 together with
Deﬁnition 3.1 guarantee the following.
Property 2. If α is maximal, then the angles assigned by α belong to [0,π ]; sum to π within a
tetrahedron; and are determined by the angles assigned to w1,w 2,...,w p ands, which must satisfy
Equations (4)–(10).
Our goal is to use these properties to show that the maximal point, α, is in A(τp), not its
boundary. Then we can apply the Casson-Rivin Theorem from 3.3 [5, Theorem 1.2] and conclude
that α corresponds to the complete hyperbolic structure on Xp, thus proving Theorem 5.1. We
will show that α is inA(τp) by showing that points in B =A(τp)−A (τp) will never maximize the
volume. We do so by proving the following.
Proposition 5.2. Any β∈B satisfying Properties 1 and 2 must have V(β) = 0.
Proof of Proposition 5.2. Let β∈B satisfy both Property 1 and Property 2. Because β is in the
boundary of the space of positive angle structures, there is a tetrahedron in τp to which β assigns
angles from the set {0,π}. By Property 1, this tetrahedron is ﬂat (has angles 0, 0, and π). Using
Property 2, we can conclude that β must assign π to at least one of the edges of w1,w 2,...w p ors.
We now explore which edges can have such assignments and determine the resulting volume.
Observe that, because all angle assignments are nonnegative, assigning an angle measure of π to
anyR edge of aw tetrahedron violates Equation (4) of Corollary 4.4 and thus Property 2. Therefore,
noβRwi can equalπ. We will use this result often, so we record it as a lemma and follow with another
useful lemma.
Lemma 5.3. If β∈B satisﬁes both Property 1 and 2, βRwi cannot equal π for i = 1,...,p . □
Lemma 5.4. If β∈B satisﬁes both Property 1 and 2, and either wp or s is ﬂat, then all tetrahedra
are ﬂat, so V(β) = 0.
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 21
Proof of Lemma 5.4. If a tetrahedron is ﬂat, one of its edges is assigned an angle ofπ. By Lemma 5.3,
βRwp cannot equalπ. However, βRs could equalπ, and, if this is the case, Equation (4) forces βRwi
to equal 0 for all i = 1,...,p , so, by Property 1, the non- s tetrahedra are also ﬂat. Because, βDwp
also appears in Equation (4), a similar argument shows that if βDwp = π, all tetrahedra are ﬂat.
By Equation (10), βDwp =βDs, so the same holds if βDs =π. Thus, it only remains to check what
happens if the angle at a B edge of wp or s equals π.
• If βBwp = π, Equation (5) implies that βBs = 0, so, by Property 1, there is a π angle at
either the R or D edge of s, and, in either case, as observed above, all tetrahedra are ﬂat.
• IfβBs =π, thenβDs = 0, soβDwp also equals 0 (Equation (10)), and, by Property 1, either
βRwp or βBwp equals π. Because of Lemma 5.3, βBwp must be π, so, by the previous case,
all tetrahedra are ﬂat.
Therefore, if either wp or s has an assigned angle of π,V(β) = 0. □
Returning to the proof of Proposition 5.2, recall that β∈B must assign π to at least one of the
edges of w1,w 2,...w p or s. Lemmas 5.3 and 5.4 cover the R edges and the tetrahedra wp and s, so
the only edges left to consider are the B andD edges ofw1,w 2,...w p−1. We start with the B edges
and ﬁrst examine the case when βBw1 =π.
IfβBw1 =π, then βDw1 equals 0 and, by Equation (10)i=1, so does βDwp−1. Property 1 implies
that in wp−1 one of the other angles must be π, but, because of Lemma 5.3, it cannot be the angle
at the R edge. Consequently, βBwp−1 equals π and Equation (9) implies βDs must equal 0, so s is
ﬂat and, by Lemma 5.4, V(β) = 0.
Having shown that if β assigns the angle π to a B edge of w1, thenV(β) = 0, we now consider
the B edges of wj with 1 < j≤ k. By repeatedly applying Equations (10) and (7) together with
Property 1 and Lemma 5.3, we will push the ﬂatness ofwj all the way down tow1, allowing us to once
again concludeV(β) = 0. In particular, if βBwj =π, then βDwj equals 0 and, by Equation (10)i=j,
so does βDwp−j. There is a π angle in wp−j (Property 1) and it cannot occur at the R edge
(Lemma 5.3), so βBwp−j, will equal π. With both βBwj and βBwp−j equal to π, Equation (7)i=j
implies that βDwj−1 = 0, so, by Equation (10) i=j−1, βDwp−(j−1) = 0 also. Another application of
Property 1 and Lemma 5.3 shows both βBwj−1 and βBwp−(j−1) are equal to π and we can apply
Equation (7)i=j−1 to conclude βDwj−2 = 0. Continuing in this manner and eventually applying
Equation (7)i=2 when both βBw2 andβBwp−2 are equal to π, allows us to conclude that βDw1 = 0.
Thus (by Property 1 and Lemma 5.3), βBw1 =π, soV(β) = 0.
It remains to examine the B edges of wj where j > k. If βBwj equals π, then βDwj = 0,
so applying Equation (10) i=p−j, Property 1, and Lemma 5.3 shows that βBwp−j = π. Because
p−j≤ k, this case has already been covered. Therefore, if any of the B edges of w1,w 2,...w p−1
have angle equal to π, thenV(β) = 0.
The proof for the D edges is a little simpler, because there is no need to appeal to Lemma 5.3. If
βDw1 =π, then, by Equation (10)i=1,βDwp−1 =π, so bothβBw1 andβBwp−1 are equal to 0. In this
situation, applying Equation (9) yields βDs =π, so s is ﬂat and, by Lemma 5.4, V(β) = 0. If j≤k
and βDwj equals π, then, by Equation (10) i=j, so does βDwp−j, and both βB(wj) and βB(wp−j)
equal 0, so Equation (7) i implies βDwj−1 = π. Continuing in this manner shows that if βDwj
equals π, so does βDw1, and thusV(β) = 0. If j >k and βDwj =π, then, by Equation (10) i=p−j,
βDwp−j =π with p−j≤k, a previous case. □
Any point maximizing the volume functional must satisfy Properties 1 and 2. By proving Propo-
sition 5.2, we have shown that any point, β, on the boundary of A(τp) satisfying these properties
hasV(β) = 0. Therefore, the maximal point α must be on the interior ofA(τp), and, by the Casson-
Rivin Theorem (3.3 and [5, Theorem 1.2]), α corresponds to the complete hyperbolic structure
on Xp. Thus, the triangulation τp is geometric, which concludes the proof of Theorem 5.1. □
Corollary 5.5. In the braid group, C 2σp
1σ−1
2 is not conjugate to σp0
1 σq0
2 for integers p0 and q0.
22 BARBARA NIMERSHIEM
Proof. Closures of braids of the form σp0
1 σq0
2 are not hyperbolic, but Theorem 5.1 shows that the
closure of C 2σp
1σ−1
2 is. □
Corollary 5.6. The complements of the (−2, 3,n )-pretzel knots and links admit geometric triangu-
lations for n≥ 7.
Proof. Recall that the braid group has the single relation σ1σ2σ1 = σ2σ1σ2 and that C, which is
this element’s square, is central. Conjugate words in the braid group yield equivalent braid closures,
so, using the relation and the centrality of C, Lp, the closure of C 2σp
1σ−1
2 with p≥ 1, is also the
closure of
(σ2σ1σ2)(σ1σ2σ1)Cσp
1σ−1
2 ∼σ2σ1σ2Cσp+2
1
=σ1σ2Cσp+3
1
∼σ2(σ1σ2σ1)(σ1σ2σ1)σp+4
1
=σ1σ2σ1σ1σ1σ2σp+5
1
∼σ3
1σ2σp+6
1 σ2;
here∼ denotes the equivalence relation of conjugacy.
As indicated in Figure 10, the closure of σ3
1σ2σp+6
1 σ2 is a pretzel. Using our deﬁnitions, σ1 and
σ2 generate left-handed (negative) twists, so Lp is a pretzel with−(p + 6), 2, and−3 half-twists, or
equivalently — after rolling thep+6 half-twists to the right —Lp is the (2,−3,−(p+6))-pretzel, and
Xp is its complement. By Theorem 5.1, Xp admits a geometric triangulation. But the complement
of the (−2, 3,p + 6)-pretzel is homeomorphic (via a reﬂection) to Xp, so it also has a geometric
triangulation. □
p + 6
{
Figure 10. The (−(p+6), 2,−3)-pretzel is also the closure of the braidσ3
1σ2σp+6
1 σ2.
Start at the dashed line and read the braid counterclockwise (strands numbered from
the outside in).
The braid relation σ1σ2σ1 =σ2σ1σ2 and the centrality of C = (σ1σ2)3 can also be used to show
that Lp is equivalent to the braid closure of σp+1
1 (σ1σ2)5:
C 2σp
1σ−1
2 =σp
1(σ1σ2)6σ−1
2 =σp
1(σ1σ2)5σ1∼σp+1
1 (σ1σ2)5.
In this form, Lp is a T-link as deﬁned by Birman and Kofman in [2], where they show that T-links
are in one-to-one correspondence with Lorenz links.
Corollary 5.7. The complements of the T-links/Lorenz links formed as closures of the braids
σp+1
1 (σ1σ2)5 admit geometric triangulations for p> 1. □
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 23
