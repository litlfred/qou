---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-015-43-2bridge-links
section_title: "2–bridge links"
section_number: 4.3
pages: 26-27
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
Theorem 4.8. LetK be a 2–bridge link in S3, whose reduced alternating diagram has twist
number t. Let C be a maximal neighborhood about the cusps of S3/integerdivideK, in which the two
cusps have equal volume if K has two components. Then
8
√
3
147 (t − 1) ≤ area(∂C ) < 2
√
3 v8
v3
(t − 1).
Furthermore, ifK is a knot, let γ be any non-trivial arc that starts on a meridian and comes
back to the same meridian (for example, a non-meridional sim ple closed curve). Then its
length satisﬁes
ℓ(γ) ≥ 4
√
6
√
2
147 (t − 1).
Proof. Letµ denote the length of a meridian of K on∂C . By Proposition 3.6, every pleated
surface Si in S3/integerdivideK contains at least one edge of length at most ln( µ2/7). Furthermore,
opposite edges in Si have the same length, because the geometry of each pleated su rface is
preserved by the full symmetry group of its triangulation. T hus, if Si is embedded in S3/integerdivideK,
it contains two edges of length at most ln( µ2/7). The only pleated surfaces that are not
embedded are the folded surfaces S1 or Sc at the ends of the product region of K; each of
these surfaces will contain at least one short edge. (See [31 , Figure 19] for a description of
how surfaces are folded in the construction of a 2–bridge lin k.)
Now, we retrace the proof of Theorem 4.1. We construct the set of short edges E exactly
as above, except that we are now counting pairs of edges. Thus, if all three pairs of edges in
a pleated surface are initially part of E, we remove the longest pair.
By the same argument as in Lemma 4.2, E contains at least t/3 distinct edge pairs. The
two paired edges on a pleated surface S will be distinct unless S isS1 orSc. Thus, if both S1
andSc contribute edges to E, the minimum possible number of edges (not pairs) is 2( t−1)/3.
The proof of Lemma 4.3 goes through without modiﬁcation. As a result, ∂C contains
4(t − 1)/3 disjoint disks, of radius at least
r ≥ min
{
1
4,
√
2µ2
14
}
, hence total area ≥ 4(t − 1)
3 ·π min
{ 1
16, µ4
98
}
.
Dividing by the maximal density π/2
√
3 of a circle packing in the plane gives
(5) area( ∂C ) ≥ 8(t − 1)
√
3
3 min
{ 1
16, µ4
98
}
.
To complete the proof of the lower bound, we note that for all 2 –bridge links except the
ﬁgure–8 knot and 5 2 knot, the meridian µ is at least
4√
2, by work of Adams [1]. Thus the
area is at least 8
√
3 (t − 1)/147. Meanwhile, the ﬁgure–8 and 5 2 knots have twist number
t = 2, hence the estimate 8
√
3/147 is vastly lower than their true cusp area (note a standard
horosphere packing argument implies the area of any cusp is a t least
√
3).
For the upper bound, Futer and Gu´ eritaud [31, Theorem B.3] f ound that the volume of a
hyperbolic 2–bridge knot satisﬁes vol( S3/integerdivideK)< 2v8(t − 1). Again, combining this with the
CUSP AREAS OF F AREY MANIFOLDS 27
theorem of B¨ or¨ oczky [14, Theorem 4], that a maximal cusp co ntains at most
√
3/(2v3) of
the volume of M , we ﬁnd
vol(C) <
√
3 v8
v3
(t − 1), hence area( ∂C ) < 2
√
3 v8
v3
(t − 1).
Finally, for the result on arc length, note that the shortest non-trivial arc γ that starts
and ends on the same meridian has length equal to area( ∂C )/µ. Again using the estimate of
Adams [1, 2], the length of a meridian of K satisﬁes
4√
2 ≤µ ≤ 2, except if K is the ﬁgure–8
or 5 2 knot. Combining Adams’s estimates with inequality (5) and a rguing as in Lemma 4.5
gives the desired lower bound on ℓ(γ). (As above, the ﬁgure–8 and 5 2 knots need to be
checked separately.) □
