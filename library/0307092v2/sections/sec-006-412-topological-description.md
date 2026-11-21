---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-006-412-topological-description
section_title: "Topological description"
section_number: 4.1.2
pages: 15-19
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
Topological description
Given a space X , any element α ∈Hn(X; Z) can be represented as f∗[K]
for some map f : |K| →X of an ordered n–cycle to X . If X = BG is a
classifying space for G then this map is determined up to homotopy by the ﬂat
G–bundle f ∗EG over |K|, so this ﬂat bundle determines the homology class
α ∈Hn(BG; Z) = Hn(G; Z)
Flat G–bundles over |K| are determined by G–valued 1–cocycles on K up to
the coboundary action of G–valued 0–cochains (the 1–cocycle is the obstruction
to extending over |K(1)| a chosen section of the ﬂat bundle over K(0)). We recall
the basic deﬁnitions.
Let Sq(K) be the set of ordered q–simplices of K. A G–valued 1–cocyle on
K is a map σ: S1(K) →G with the cocyle property:
σ⟨v0, v2⟩= σ⟨v0, v1⟩σ⟨v1, v2⟩
for ⟨v0, v1, v2⟩∈S2(K) .
For convenience we extend the deﬁnition of σ to reverse-ordered simplices by
σ⟨v1, v0⟩= σ⟨v0, v1⟩−1
for ⟨v0, v1⟩∈S1(K) .
If τ : S0(K) →G is a 0–cochain, then its coboundary action on 1–cocycles is
to replace σ by
⟨v0, v1⟩7→τ(v0)−1σ⟨v0, v1⟩τ(v1) .
A G–valued 1–cocycle σ determines a G–labeling of simplices: label a sim-
plex ⟨v0, . . . , vk⟩by (1, σ⟨v0, v1⟩, . . . , σ⟨v0, vk⟩).
Conversely, a G–labeling of
Geometry & Topology, Volume 8 (2004)
428
Walter D Neumann
simplices determines a 1–cocycle: assign to a 1–simplex with label (g1, g2) the
element g−1
1 g2 ∈G. These correspondences are clearly mutually inverse. When
a 1–cocyle σ is changed by the coboundary action of a 0–cochain τ , the cor-
responding G–labeling (g0, . . . , gk) of a k–simplex ⟨v0, . . . , vk⟩is replaced by
(g0τ(v0), . . . , gkτ(vk)).
Thus, we get our desired representative as in subsection 4.1 for a homology
class α ∈Hn(G; Z) by representing α by a ﬂat G bundle over an ordered
n–cycle K, representing that by a G–valued 1–cycle on K, and then taking
the corresponding G–labeling of K. We want labels of the vertices of any n–
simplex to be distinct, which means that the 1–cocycle should never take the
value 1. Since G is inﬁnite, this can be achieved by modifying by a coboundary
if necessary.
4.2
Deﬁnition of λ: H3(G; Z) →bP(C)
Let K be an ordered 3–cycle. We call a closed path γ in |K| a normal path
if it meets no 0– or 1–simplices of K and crosses all 2–faces that it meets
transversally. When such a path passes through a 3–simplex ∆i, entering and
departing at diﬀerent faces, there is a unique edge E of the 3–simplex between
these faces. We say the path passes this edge E.
(In the following it will often be necessary to distinguish between a 1–simplex of
K and the various edges of 3–simplices that are identiﬁed with this 1–simplex.
To avoid excess notation, we will often use the same symbol for a 1 simplex of
K and the edges of 3–simplices that are identiﬁed with it, but we will refer to
“edges” or “1–simplices” to ﬂag which we mean.)
Consider a choice of combinatorial ﬂattening wi for each simplex ∆i. Then for
each edge E of a simplex ∆i of K we have a log-parameter lE = lE(∆i, wi)
assigned. Recall that this log-parameter has the form log z +sπi where z is the
cross-ratio parameter associated to the edge E of simplex ∆i and s is some
integer. We call (s mod 2) the parity parameter at the edge E of ∆i and
denote it δE = δE(∆i, wi).
Deﬁnition 4.3 Suppose γ is a normal path in |K|. The parity along γ is the
sum
X
E
δE modulo 2
of the parity parameters of all the edges E that γ passes. Moreover, if γ runs
in the star of some ﬁxed 0–simplex v of K, then the log-parameter along the
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
429
path is the sum
X
E
±ǫi(E)lE,
summed over all edges E that γ passes, where:
•
i(E) is the index i of the simplex ∆i that the edge E belongs to and ǫi(E)
is the coeﬃcient ±1 that encodes whether the ordering of the vertices of
∆i(E) matches the orientation of |K| or not.
• the extra sign ± is + or −according as the edge E is passed in a
counterclockwise or clockwise fashion as viewed from the vertex.
If γ just encircles a 1–simplex (so the extra signs are all + or all −) we speak
of the parity or log-parameter “around the 1–simplex.”
We assume we have represented an element α ∈H3(G; Z) by a G–labeled
ordered 3–cycle K as in subsection 4.1.
So to each 3–simplex ∆i of K is
associated a 4–tuple ⟨g(i)
0 : . . . : g(i)
3 ⟩, deﬁned up to left-multiplication by ele-
ments of G, and ǫi = ±1 encodes whether the ordering of the vertices of ∆i
matches the orientation of K or not. In the following deﬁnition we identify
G = PSL(2, C) with the isometry group Isom+(H3).
Deﬁnition 4.4 Flattening of K
Choose z ∈∂H
3 so g(i)
0 z, g(i)
1 z, g(i)
2 z, g(i)
3 z
are distinct points of ∂H
3 for each i (this excludes ﬁnitely many points z ∈
∂H
3). We then have an ideal hyperbolic simplex shape for each simplex ∆i
of K and an associated cross ratio xi = [g(i)
0 z : g(i)
1 z : g(i)
2 z : g(i)
3 z]. A ﬂattening
of K consists of a choice of combinatorial ﬂattenings wi = ℓ(xi; pi, qi) of the
simplices of K such that the parity along any normal path in K is zero and
the log-parameter around each edge of K is zero. If log-parameter along any
normal path in the star of each 0–simplex of K is zero we call it a strong
ﬂattening of K.
Theorem 4.5 For each choice of z as in the above deﬁnition, a strong ﬂat-
tening of K exists.
Recall that our G–labelled ordered 3–cycle K was chosen to represent an ele-
ment α ∈H3(G; Z) (G = PSL(2, C)). The following theorem ﬁnally gives the
deﬁnition of the map λ: H3(G; Z) →bB(C).
Theorem 4.6 For any ﬂattening of K the element P
i ǫi[xi; pi, qi] ∈bP(C)
only depends on the homology class α ∈H3(PSL(2, C); Z). We denote it λ(α).
Moreover, λ(α) ∈bB(C) and λ: H3(PSL(2, C); Z) →bB(C) is a homomorphism.
Geometry & Topology, Volume 8 (2004)
430
Walter D Neumann
In Remark 10.5 we point out that instead of choosing a single z in the deﬁnition
of ﬂattening, we may choose a diﬀerent z for each vertex of K, and Theorem
4.6 remains true. This is useful in practice (Section 14).
We now give a brief overview of the proofs.
If the extended Bloch group bB(C) is to be isomorphic to H3(G; Z) then it must
ﬁt in the same Bloch–Wigner short exact sequence that was given for H3(G; Z)
in the Introduction. This is proved in section 7, and section 8 is a digression
describing a related group. These sections are independent of the proofs of
Theorems 4.5 and 4.6, which take up Sections 9 through 11.
First some basic tools are developed in Sections 5 and 6. Section 5 describes
a developing map ˜K →H
3 which is helpful for visualizing the ﬂattening con-
dition. It is used to prove some preliminary lemmas. Section 6 proves a con-
sequence of the ﬁve term relations, a general “cycle relation” which is used
frequently later.
Section 9 proves Theorem 4.5, the existence of a strong ﬂattening of K. The
argument of this section is combinatorial and depends heavily on [13].
The combinatorial argument is continued at the beginning of the next section
(Section 10) to show that the resulting element of bP(C) is independent of the
choice of strong ﬂattening and lies in bB(C). It then remains to show that the
element of bB(C) only depends on the homology class α ∈H3(G; Z) and not on
the G–labeled ordered 3–cycle K used to represent it. In the rest of Section
10 we ﬁrst show that this element of bB(C) is unchanged if the G–labeling of
K is changed by a coboundary (so it just depends on the ﬂat G–bundle and
not on the 1–cocycle used to represent it) and next that it is invariant under
alteration of the triangulation of |K| by Pachner moves. Thus, by the end of
this section we know that we have an element of bB(C) that only depends on
the space |K| and the ﬂat G–bundle over it.
This section uses a strong ﬂattening of K and, moreover, it needs to assume
that K is a simplicial rather than quasi-simplicial complex and that the vertex
orderings of its simplices are induced by a global ordering of the 0–simplices
of K. These assumptions will be removed one by one in the next section, so
Theorem 4.6 eventually applies to ﬂattenings that are not necessarily strong,
and also to quasi-simplicial complexes for which the vertex orderings of the
simplices need not be globally induced.
Section 11 completes the proof of Theorem 4.6. First it is shown that the singu-
larities of |K| can be “resolved” to make |K| into a manifold. Since H3(G; Z)
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
431
can be represented as the bordism group of 3–manifolds with ﬂat G–bundles,
the proof is completed by showing that the element of bB(C) is unchanged by ele-
mentary bordisms (ie, surgery). Flattenings and strong ﬂattenings are the same
thing when K is a manifold, so the requirement of strong ﬂattenings dissolves,
while retriangulation using Pachner moves is used to relax the requirements
on K to require only that it be a quasi-simplicial complex with vertex-ordered
simplices.
Finally, the main Theorem 2.6, stating that λ: H3(PSL(2, C); Z) →bB(C) is an
isomorphism and that Cheeger–Chern–Simons class is given by Rogers dilog-
arithm, is proved in section 12. At this point it follows easily, using work of
Dupont.
Section 13 describes the weaker conclusions obtained if orderings of simplices
are not used, conﬁrming a conjecture in [13].
The next two sections then apply the results to invariants of 3–manifolds, and
a very brief ﬁnal section describes what happens if C is replaced by a number-
ﬁeld.
