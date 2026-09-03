---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-013-41-puncturedtorus-bundles
section_title: "Punctured–torus bundles"
section_number: 4.1
pages: 21-25
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
Theorem 4.1. LetM be a punctured–torus bundle with monodromy
Ω = ±Rp1Lq1 · · ·RpsLqs.
LetC be a maximal horoball neighborhood about the cusp of M . Then
0.1885s ≈ 16
√
3
147 s ≤ area(∂C ) < 2
√
3v8
v3
s ≈ 12.505s.
Furthermore, if γ is any simple closed curve on ∂C that is transverse to the ﬁbers, then its
length ℓ(γ) satisﬁes
ℓ(γ) ≥ 4
√
6
147 s.
Remark. Extensive numerical experiments support the conjecture th at area(∂C )/s is mono-
tonic under the operation of adding more letters to existing syllables of the monodromy word
Ω. (It is not hard to show using the method of angled triangula tions [31] that the volume of
M behaves in a similarly monotonic fashion.) This conjecture would imply that the quantity
area(∂C )/s is lowest when all syllables have length 1 and M is a cover of the ﬁgure–8 knot
complement, while area(∂C )/s approaches its upper bound as the syllable lengths approach
∞ and the geometry of M converges to a cover of the Borromean rings. The cusp area of
the ﬁgure–8 knot complement is 2
√
3, and the cusp area of one component of the Borromean
rings is 8. Thus, if the monotonicity conjecture is correct, it would follow that
2
√
3s ≤ area(∂C ) < 8s.
Compared to the values in Theorem 4.1, this represents a mode st improvement of the upper
bound but a dramatic improvement of the lower bound.
The main idea of the proof of Theorem 4.1 is to pack the horosph erical torus ∂C with
disjoint disks that are shadows of large horospheres. Recal l from Deﬁnition 2.3 that we
denote the length of a meridian in the maximal cusp of a punctu red–torus bundle by 2µ. By
Proposition 3.6, every zigzag on ∂C will contain two horospheres of diameter at least µ2/7,
corresponding to the two endpoints of the same edge of the zig zag. When we project one of
these horospheres to ∂C , we obtain a disk whose radius is at least µ2/14.
To turn this into an eﬀective estimate on the area of ∂C , we need to employ a somewhat
subtle procedure for choosing which horospheres to count an d which ones to discard. We
choose the horospheres in the following manner:
(1) Let E be the set of all edges of M whose length outside the maximal cusp is at most
ln(7/µ2). These are exactly the edges that lead to horospheres of dia meter ≥µ2/7.
Thus, by Proposition 3.6, every pleated surface in M contains an edge in E.
(2) Order the letters of the monodromy word Ω: α1,...,α m. Recall, from Section 2.2,
that each αi corresponds to a pleated surface Tα i.
(3) Find the smallest index i such that all three edges in the pleating of Tα i belong to
E. (It is possible that such an i does not exist.) If such a Tα i occurs, remove the
longest of the those three edges from E, breaking ties at random.
(4) Repeat step (3) inductively. In the end, the set E will contain at most two edges
from each pleated surface.
At the end of step (4), if a pleated surface T contains one edge of E, that edge is the
shortest in T . If T contains two edges of E, they are the two shortest edges in T .
Lemma 4.2. The set E, constructed as above, contains at least 2s/3 distinct edges.
22 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
F L
L
L
LS
Figure 9. The only possible words between two triangles that share a ve rtex
areSRR · · ·RF andSLL · · ·LF , where S andF (start and ﬁnish) can both
be either L or R.
Proof. By Proposition 3.6, every pleated surface in M contains an edge whose length is at
most ln(7/µ2). Thus, at the end of step (1) in the selection procedure abov e, the set E
contained at least one edge from every pleated surface. Now, observe that two diﬀerent
pleated surfaces Tα and Tβ , corresponding to letters α and β in Ω, will share an edge if and
only if the corresponding triangles in the Farey graph share a vertex. As Figure 9 illustrates,
this can only happen if the letters α andβ come from the same syllable, neighboring syllables,
or syllables that share a neighbor. Therefore, at the end of s tep (1), the set E contained
at least one edge for every consecutive string of three sylla bles, hence at least 2 s/3 distinct
edges in total.
Now, consider what happens when we begin removing edges in st ep (3). Suppose that
all three edges in a pleated surface Tα belong to E. Then, just as above, for any pleated
surface Tβ that shares an edge with Tα , the letters α and β must come from the same
syllable, neighboring syllables, or syllables that share a neighbor. There are at most ﬁve
such syllables altogether (the syllable containing α, plus two on each side). Thus, after we
remove the longest edge of Tα fromE, the set E still contains two edges from a string of ﬁve
consecutive syllables.
At the end of the selection procedure, every pleated surface inM belongs either to a string
of 3 syllables containing at least one edge of E, or to a string of 5 syllables containing at
least two edges of E. In either scenario, there are at least 2 s/3 edges belonging to E. □
Lemma 4.3. LetM be a punctured–torus bundle with monodromy
Ω = ±Rp1Lq1 · · ·RpsLqs,
Then the maximal cusp boundary ∂C contains 4s/3 disjoint disks, each of radius at least
min
{
1
4,
√
2µ2
14
}
.
Proof. Consider the edge set E, as above. By Lemma 4.2, E contains at least 2 s/3 edges of
length at most ln(7 /µ2). Now, lift everything to the universal cover H3, in such a way that
∂C lifts to the horizontal plane at height 1. In a single fundame ntal domain for ∂C , each
edge e ∈ E corresponds to two horospheres: one horosphere for each end point of e. Hence
∂C contains 4s/3 shadows of disjoint horospheres, each of which has radius a t least µ2/14. If
two disjoint horospheres have the same size, then they also h ave disjoint projections. Thus,
CUSP AREAS OF F AREY MANIFOLDS 23
by shrinking each horosphere to radius µ2/14, we conclude that ∂C contains 4s/3 disjoint
disks of radius µ2/14.
Next, we claim that the disks on ∂C can be enlarged considerably while staying disjoint.
Letx andy be the centers of two of these disks. In other words, x ∈∂C ∩ei andy ∈∂C ∩ej
for some ei,e j ∈ E. The two edges ei,e j lead to horospheres Hi and Hj. Let f be the
geodesic that connects Hi directly to Hj. Consider the length of f outsideHi andHj. There
are two cases:
Case 1: the length of f is at least ln(2). In this case, the midpoint of f lies at distance
at least ln(2) /2 from both Hi and Hj. If we apply an isometry I that sends ∂Hi to the
horosphere at Euclidean height 1, the midpoint of I(f ) will lie at height at most 1 /
√
2. In
other words, the horosphere I(Hi) can be expanded by a factor of
√
2 without hitting the
midpoint of I(f ), and similarly for Hj. Of course, this still holds true before applying the
isometryI: each of Hi andHj can be expanded by a factor of
√
2 while staying disjoint from
each other. Since each of Hi and Hj has radius at least µ2/14, the disks of radius
√
2µ2/14
centered at x and y in ∂C are disjoint from each other.
Case 2: f is shorter than ln(2). Then, by Lemma 3.3, f must be an edge of the canonical
triangulation. Since ei andej are also edges of the canonical triangulation, these three e dges
bound an ideal triangle contained in some pleated surface Tα . Now, recall that at the end of
our selection procedure for the set E, if two distinct edges of Tα belong to E, then they are
the shortest edges in Tα . Thus both ei and ej are shorter than ln(2). Since the edges ei and
ej are already vertical in H3 and meet the cusp at Euclidean height 1, the horospheres Hi
and Hj must have diameter at least 1 /2. Thus Hi andHj project to disjoint disks of radius
at least 1/4 centered at x and y on ∂C .
In every case, the points x,y ∈∂C are the centers of disjoint disks of radius at least
min
{
1
4,
√
2µ2
14
}
.
There are 4s/3 such disks, completing the proof. □
We may now estimate the area of ∂C .
Lemma 4.4. LetM be a punctured–torus bundle with monodromy
Ω = ±Rp1Lq1 · · ·RpsLqs.
LetC be a maximal horoball neighborhood about the cusp of M . Then
16
√
3
147 s ≤
√
3s min
{ 1
6, 4µ4
147
}
≤ area(∂C ) < 2
√
3 v8
v3
s.
Proof. There are three inequalities in the statement, and we consid er them in turn.
First inequality. This follows immediately from Lemma 3.7, which gives µ ≥
√
2. Note
that with our deﬁnition of µ (see Deﬁnition 2.3), the conclusion of Lemma 3.7 transfers
perfectly from 4–punctured sphere bundles to punctured tor us bundles.
Second inequality. By Lemma 4.3, ∂C contains 4s/3 disjoint disks of equal radius, whose
total area is at least
4s
3 ·π min
{ 1
16, µ4
98
}
.
Now, a classical result (see e.g. [14, Theorem 1]) states tha t a packing of the plane by circles
of equal size has density at most π/(2
√
3). This gives the desired inequality.
24 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Third inequality. A result of Agol gives that vol( M )< 2v8s (see [31, Theorem B.1] for a
direct proof). Also, a horosphere packing theorem of B¨ or¨ oczky [14, Theorem 4] states that
a maximal cusp in a hyperbolic 3–manifold contains at most
√
3/(2v3) of the volume of M .
Putting these results together gives
vol(C) <
√
3 v8
v3
s, hence area( ∂C ) < 2
√
3 v8
v3
s. □
Remark. In the proof of Lemma 4.3, we also showed that ∂C contains 4s/3 disjoint disks
of radius µ2/14. Plugging this estimate into the proof of Lemma 4.4 gives
area(∂C ) ≥ 2
√
3µ4
147 s.
This statement, although apparently weaker than Lemma 4.4, will prove useful for estimating
the lengths of slopes on ∂C .
Lemma 4.5. LetM be a punctured–torus bundle with monodromy
Ω = ±Rp1Lq1 · · ·RpsLqs.
Let C be a maximal horoball neighborhood about the cusp of M . If γ is any simple closed
curve on ∂C that is transverse to the ﬁbers, ℓ(γ) ≥ 4
√
6s/147.
Proof. Deﬁne the height of the cusp to be h := area(∂C )/2µ. Then ℓ(γ) ≥h. Note that by
Lemma 3.7, µ ≥
√
2. Also, since a maximal horocycle in a punctured torus has le ngth at
most 6, it follows that µ ≤ 3. We consider three possibilities for the values of µ in the range
[
√
2, 3].
If
√
2 ≤µ ≤
√
7/23/ 4, then 4µ4/147 ≤ 1/6. Thus, by Lemma 4.4,
area(∂C ) ≥ 4
√
3µ4
147 s, hence ℓ(γ) ≥ 2
√
3µ3
147 s ≥ 4
√
6s
147 ≈ 0.066652s.
If
√
7/23/ 4 ≤µ ≤ 2, then 1/6 ≤ 4µ4/147. Thus, by Lemma 4.4,
area(∂C ) ≥
√
3s
6 , hence ℓ(γ) ≥
√
3s
12µ ≥
√
3s
24 ≈ 0.072168s.
If 2 ≤µ ≤ 3, then by the remark following Lemma 4.4,
area(∂C ) ≥ 2
√
3µ4
147 s, hence ℓ(γ) ≥
√
3µ3
147 s ≥ 8
√
3s
147 ≈ 0.094261s.
Therefore, for all possible values of µ, we have ℓ(γ) ≥ 4
√
6s/147. □
Lemmas 4.4 and 4.5 complete the proof of Theorem 4.1.
Combining the results of Theorem 4.1 with our work in [25, The orem 1.1], we obtain the
following immediate corollary for volumes of Dehn ﬁllings o f punctured torus bundles.
Corollary 4.6. Let M be a punctured–torus bundle with monodromy of length s> 94. Let
C be a maximal horoball neighborhood about the cusp of M . For any simple closed curve
γ on ∂C that is transverse to the ﬁbers, let Mγ denote the 3–manifold obtained from M by
Dehn ﬁlling ∂C along γ. Then Mγ is hyperbolic, and
(
1 − 7203π2
8s2
)3/ 2
2v3s ≤ vol(Mγ ) < 2v8s,
where v3 = 1.0149... is the volume of a regular ideal tetrahedron and v8 = 3.6638... is the
volume of a regular ideal octahedron.
CUSP AREAS OF F AREY MANIFOLDS 25
Proof. By Theorem 4.1, the slope length of γ will be at least 2 π when s ≥ 95. For such
slopes, by [25, Theorem 1.1] we know the volume of the manifol d obtained by Dehn ﬁlling
along the slope of length ℓ(γ) is at least
vol(Mγ ) ≥
(
1 −
( 2π
ℓ(γ)
)2)3/ 2
vol(M ).
Hence, using the volume bound for such manifolds given by [31 , Theorem B.1], and the
estimate on slope length of Theorem 4.1, we have
vol(Mγ ) ≥
(
1 − 7203π2
8s2
)3/ 2
2v3s.
For the upper bound, recall that volume only decreases under Dehn ﬁlling [56], and so the
result follows immediately from [31, Theorem B.1]. □
