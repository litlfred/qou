---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-046-1-mwf-l-4
section_title: "MWF (L) = 4"
section_number: 1
pages: 39-42
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
2. b(L) = 4
3. L is one of the links, whose reduced alternating diagrams are described (up to mirror images) as follows
(a) The Murasugi (or connected) sum of three (2,ni)-torus links (with |ni| > 1),
(b) The Murasugi (or connected) sum of a (2,n)-torus link with a (p,q,r,s)-pretzel link, with one of p,q,r,s
equal to 1, or its mirror image, or
(c) a special diagram whose Seifert graph (see §2.1) is as shown in ﬁgure 6.
Proof. 2 =⇒ 1. This follows from corollary 6.3.
3 =⇒ 2. That the links in 3 have braid index at least 4 follows from t he description of the links with b(L) ≤ 3 in
[St2] (which also comes out of the proof of corollary (6.3)). It is also not too hard to check that for all these links
b = 4 by exhibiting a diagram D with s(D) = 4. The most systematic way seems to apply the graph index ineq uality
of Murasugi-Przytycki [MP2] (see also [Oh]).
1 =⇒ 3. By applying theorem 6.1, we need to deal with non-special d iagrams of at most 5 and special diagrams of at
most 6 Seifert circles.
First consider the non-special diagrams.
For the ﬁbered links (the reduced Seifert graph is a tree), Mu rasugi’s result [Mu] leads directly to case 3a. For non-
ﬁbered links, the Seifert graph must have a cycle, which must be of length at least 4 (the Seifert graph is bipartite).
Then the only option that remains is case 3b. We must still arg ue why one of p,q,r,s must be ±1. This can be done
using Murasugi-Przytycki’s work, but one easily sees it also by a direct skein theoretic argument, which we explain.
40 6 Studying alternating links by braid index
(all multiplicities ≥ 2)
1
1
1 11
1
1
Figure 6: The reduced Seifert graphs of the alternating diagrams of sp ecial alternating
links of braid index 4. Simple edges have their multiplicity (1) attached, and the other
edges (of multiplicity one or more) are unlabelled. In the ﬁr st graph, exceptionally, all
edges have multiplicity at least 2.
Let L(p,q,r,s) be the corresponding link and P(p,q,r,s) its skein polynomial. Look ﬁrst at p = 0, q,r,s ≥ 2. Then
L(p,q,r,s) a connected sum of two (2,n)-torus links, and a closed alternating 3-braid. So MW F(L(p,q,r,s)) = 5.
Now since the case p = 1, q,r,s ≥ 2 has MW F(L(1,q,r,s)) ≤ b(L(1,q,r,s)) = 4, the skein relation (3) easily shows
that the maximal degree coefﬁcient maxcfvP(p,q,r,s) of v in P (which is a polynomial inz) for p = 2 is inherited from
p = 0. Then further applications of (3) show that the z-degree of maxcf vP(p,q,r,s) increases with p, so in particular
this term never vanishes, and so MW F(L(p,q,r,s)) = 5.
Now consider the special diagrams. For them one considers th e Seifert graph, and needs to write down all bipartite
planar graphs on at most 6 vertices, which have no cut vertex. Since the diagram D is special, the placement of
multiple copies of an edge give diagrams equivalent up to ﬂyp es, so it is enough to consider simple graphs (the
reduced Seifert graph), and have the multiplicities of an ed ge written as its label. The graphs can be easily compiled
using the observation that they must contain a cycle of lengt h 4 or 6; see ﬁgure 6. By direct inspection we see that
the edge multiplicities must be as speciﬁed in the ﬁgure. (In fact if an edge is multiple it turns out irrelevant what its
multiplicity is, so in this case we just omit the label.) We ru le out the remaining multiplicities by a skein theoretic
calculation, similar to the one explained for case 3b.
Let w.l.o.g. (up to mirroring) D be positive. For each edge e in Γ(D) of variable multiplicity ≥ i (where i = 1,2)
we calculate the skein polynomial of the diagram that corres ponds to Γ for multiplicities i and i + 1 of e. That is, if
Γ(D) has l edges of variable multiplicity, we have 2l polynomials to calculate. Then we check for each such set of 2 l
polynomials that Q = Pv9−χ(D) is non-zero, and maxdegz P − maxdegz Q as well as maxcf zQ is constant within this set
of 2l polynomials. Then by (3) this property is inherited to diagrams D whose Γ(D) have edges of higher multiplicity,
and in particular MW F ≥ 5.
There is one more graph,
not included in ﬁgure 6. In that case (by the method we just explained we verify that) MWF ≥ 5 for all non-zero edge
multiplicities. ✷
In [MP2], Murasugi-Przytycki deﬁne a certain quantity ind (D), assigned to a link diagram D, called index. (We omit
here the detailed discussion; one can consult also [Oh] or [St5].) Their motivation was to give an upper estimate
b(L) ≤ s(D) − ind(D)(43)
for the braid index of the underlying link L. Their origin of (43) consists in an appropriate move (see ﬁg ure 8.2
in [MP]) which reduces the number of Seifert circles of the di agram. Murasugi-Przytycki conjectured that for an
alternating diagram D, the inequality (43) is exact. This conjecture is also conﬁr med for alternating links up to braid
index 4.
Based on the Murasugi-Przytycki procedure, we can re-enter the Bennequin surface topic.
Corollary 6.4 Alternating links of braid index at most 4 carry a Bennequin surface on a minimal string braid.
41
Proof. In [St5] it was explained how to apply restrictedly the Seife rt circle reduction move of Murasugi-Przytycki
(and then those of Yamada [Y]) so as to obtain a braided surface. This modiﬁed reduction is easily checked to lead to
the minimal number of strings for the links in question. ✷
Corollary 6.5 Let L be an alternating link of braid index 4. Then |maxcf ∆(L)| ≤ 5, and if |maxcf ∆(L)| > 2, then L
is special alternating.
Proof. It is well known, that |maxcf ∆(L)| is multiplicative under Murasugi sum and for a special diagr am depends
only on the reduced Seifert graph. The result follows by calculation for the speciﬁc types. ✷
The proof of this corollary, and the extension of the multiplicativity of maxcf∆ to maxcf zP for diagrammatic Murasugi
sum [MP] demonstrates also the following more general principle:
Corollary 6.6 For any given braid index, there are only ﬁnitely many valuesof maxcf ∆ and maxcf zP among Alexan-
der and skein polynomials of alternating links of that braid index. ✷
We saw that for ∆ this statement is wrong for non-alternating links even among 3-braids. On the other hand, by [St2],
it is true for P, and we do not know if it remains true for (closed) braids on mo re strings. (One could also ask if
inﬁnitely many leading coefﬁcients of ∆ occur if maxdeg ∆ = 1 − χ, but we se no deeper meaning in this question, so
will not dwell further upon it here.)
The following is also worth observing. Call a subclass C ′ of a class C of links generic in C if
lim
n→∞
# {L ∈ C ′ : c(L) = n }
# {L ∈ C : c(L) = n } = 1 .
Corollary 6.7 The number of special alternating links of given braid index grows polynomially in the crossing num-
ber. In particular, a generic alternating link of given braid index is not special alternating.
Proof. A special alternating link is determined by the Seifert (= checkerboard) graph of its alternating diagram. The
number of such graphs with a ﬁxed number of vertices grows polynomially in the number of edges. The second claim
in the corollary follows because it is easy to see that in cont rast the number of non-special alternating links grows
exponentially (due to exponentially many, in the crossing number, ways to perform the Murasugi sum at a separating
Seifert circle of the alternating diagram). ✷
Remark 6.2 Note that in contrast we showed in [SV] that a generic alternating knot (and the case of links is analogous)
of given genus is special alternating. This shows from yet another point of vi ew the opposition between genus and
braid index.
Another immediate and useful consequence of theorem 6.2 and the preceding remarks is
Corollary 6.8 If an alternating link L has MW F(L) ≤ 4 (in particular if b(L) ≤ 4), then the MWF inequality is exact
(i.e. an equality) for L. ✷
This gives a nice complement to the MWF exactness results in [Mu, MP2]. (As another such ampliﬁcation, we proved
the case of knots and genus ≤ 4 in [St5].)
Note that at MWF bound 5 we hit already at the Murasugi-Przytycki examples [MP2] of non-exact MWF (withb = 6).
So corollary 6.8 is not true for MW F ≥ 5 or b ≥ 6. We do not know about the case b = 5. However, ruling out braid
index 5 for the Murasugi-Przytycki family is a serious computational problem (only two speciﬁc members were dealt
with, a 4-component 15 crossing link and an 18 crossing knot; see [MP2, §19]). Already with this circumstance in
mind, one cannot expect to easily extend the corollary (or theorem 6.2) for b = 5 either, even if it may be true.
On the other hand, leaving these troublesome exceptions aside, the above discussion should fairly clearly explain how
the general picture continues for alternating links with MWF bound 5 and more.
