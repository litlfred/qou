---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-026-b2-volume-estimates-for-links
section_title: "B.2 Volume estimates for links"
section_number: null
pages: 41-44
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Volume estimates for links
The volumes of link complements can also be estimated in terms of diagrams. We
say that a link diagram D is reduced if no single crossing separates D. Its twist
number tw(D) is the number of equivalence classes of crossings, where two crossings
are considered equivalent if there is a loop in the projection plane intersecting D
transversely precisely in the two crossings. When the diagram D depicts a two-bridge
link constructed from a braid, as in Figure 13, tw(D) is precisely the number of syllables
of the word Ωdescribing the braid.
Theorem B.3 Let D be a reduced alternating diagram of a hyperbolic two-bridge link
K. Then
2v3 tw(D) −2.7066 < Vol(S3∖K) < 2v8(tw(D) −1).
The upper bound is sharp, and the lower bound is asymptotically sharp.
There are known diagrammatic volume bounds for the general class of alternating
links. On the lower side, Agol, Storm, and W Thurston proved that the volume of
an alternating link is at least v8
2 (tw(D) −2) [3], improving an earlier bound due to
Lackenby [14]. On the upper side, Agol and D Thurston proved an asymptotically sharp
bound of 10v3(tw(D) −1) [14, Appendix]. Numerically, Theorem B.3 improves the
multiplicative constant in the lower bound from 1.8312 to 2.0299 and the multiplicative
constant in the upper bound from 10.1494 to 7.3277 (in the special case of 2–bridge
links).
Compared to its predecessors, Theorem B.3 is less general, but uses only very elementary
methods. The proof in [3] relies in a fundamental way on Perelman’s results about the
Geometry & Topology 10 (2006)
1280
Franc¸ois Gu´eritaud and David Futer
monotonicity of volume under Ricci ﬂow with surgery. By contrast, the lower bound in
Theorem B.3 only relies on the explicit study of angled triangulations.
P
P
)
Figure 21: A ﬂype in a diagram of a two-bridge link. The shaded rectangle P is a pillowcase of
the braid.
Proof First, we claim that it sufﬁces to consider a diagram D like the one in Fig-
ure 13, constructed from an alternating braid with one free strand. By the Menasco–
Thistlethwaite ﬂyping theorem [16], any pair of reduced alternating diagrams of K are
related by a sequence of ﬂypes, as in Figure 21. It is easy to check that the twist number
of a diagram is invariant under ﬂypes. Thus the number of syllables of the word Ωis
the twist number of any reduced alternating diagram of K.
Lower bound Suppose that the link is deﬁned by the word Ω= Ra1La2 · · · Ran (the
parity of n = tw(D) and the letter of the ﬁrst and last syllables are unimportant). As in
the proof of Theorem B.1, we explicitly choose a point w = ( π
2 , w1, . . . , wc−1, π
2 ) of ¯P.
However, the concavity condition of (3) does not allow us to set wi = π
3 when i is too
close to 0 or c. Instead, we proceed as follows. We let wi = π
3 for all a1 ≤i ≤c −an.
For the indices of the ﬁrst and last fans, we interpolate linearly between π
2 and π
3 . As
before, it is easy to check that these values of the parameters make all tetrahedron angles
nonnegative, and give us a point of ¯P.
When i is a hinge and a1 < i < c−an, the two tetrahedra of ∆i have all dihedral angles
π
3 , and volume v3. For n ≥3, there are exactly n −3 hinge indices of this type. When
i = a1 or i = c −an, we can compute from Figure 5 that the three angles of ∆i are
π
3 + ti,
π
3 −ti
and
π
3 ,
where
ti = |wi+1 −wi−1| ≤π
6 .
By Proposition 6.6, the volume deﬁned by these angles is smallest at the extreme value
of ti = π
6 , when the three angles are π
2 , π
3 , π
6 . Still assuming n ≥3, by Formula (4) the
four tetrahedra in the two terminal hinge layers each have volume at least 0.84578...
Putting it all together gives
V(w) > 2v3 (tw(D) −3) + 4 × 0.84578 > 2v3 tw(D) −2.7066.
Geometry & Topology 10 (2006)
Canonical triangulations
1281
(As a special case, if n = 2, V(w) > 2 × 0.84578 also satisﬁes the theorem.)
To prove that this bound is asymptotically sharp, let Ω= (RL)k, for large k. Then
tw(D) = 2k, and the triangulation of K(Ω) consists of 2(tw(D) −1) tetrahedra, all
of them hinges. Since the volume of an ideal tetrahedron is bounded above by v3,
Vol(S3∖K) ≤2v3(tw(D) −1), a value whose ratio to the lower bound of the theorem
approaches 1 as tw(D) gets large.
K
J
L
Figure 22: The construction of an augmented 2–bridge link L. When tw(D) = 2, L is the
Borromean rings.
Upper bound The proof of the upper bound uses the same surgery argument that
Lackenby, Agol, and Thurston used for general alternating links [14], and the improved
estimate comes from the special structure of 2–bridge links.
Let D be a diagram as in Figure 13. Recall that each syllable of Ωcorresponds to a
twist region where two strands of the braid wrap around each other. For every twist
region, we add an extra link component (called a crossing circle) encircling the two
strands of K, obtaining a hyperbolic link J [14]. (See Figure 22.) Every crossing
circle of J bounds a crossing disk that is punctured by the two strands of K. Because
twice-punctured disks are totally geodesic [1], we can untwist all the crossings in the
twist region and obtain a new link L, called an augmented link, whose volume is equal
to that of J.
When K is a two-bridge link, L has the following alternate description. Start with
(tw(D) −1) copies of the Borromean rings, cut each one along a crossing disk, and
glue the copies together in a linear fashion. Volume is additive under this operation
[1]. Thus Vol(S3∖L) = 2v8(tw(D) −1), since the Borromean rings have volume 2v8.
Since K is obtained by Dehn ﬁlling the crossing circles of J, we have
Vol(S3∖K) < Vol(S3∖J) = Vol(S3∖L) = 2v8(tw(D) −1).
By choosing a link with many crossings in each twist region, one can get Vol(S3∖K)
arbitrarily close to this upper bound.
Geometry & Topology 10 (2006)
1282
Franc¸ois Gu´eritaud and David Futer
