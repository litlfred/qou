---
doc_id: 0307092v2
doc_title: "Published: 14 February 2004"
section_id: sec-003-411-algebraic-description
section_title: "Algebraic description"
section_number: 4.1.1
pages: 14-18
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class Walter D Neumann — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
We recall a standard chain complex for homology of G = PSL(2, C), the chain
complex of “homogeneous simplices for G.” We will, however, diverge from
the standard by using only non-degenerate simplices, ie, si mplices with distinct
vertices — we may do this because G is inﬁnite.
Let Cn(G) denote the free Z–module on all ordered ( n + 1)–tuples ⟨g0, . . . , gn⟩
of distinct elements of G. Deﬁne δ : Cn → Cn−1 by
δ⟨g0, . . . , gn⟩ =
n∑
i=0
(−1)i⟨g0, . . . ,ˆgi, . . . , gn⟩.
Then each Cn is a free ZG–module under left-multiplication by G. Since G is
inﬁnite the sequence
· · · → C2 → C1 → C0 → Z → 0
is exact, so it is a ZG–free resolution of Z. Thus the chain complex
· · · → C2 ⊗ZG Z → C1 ⊗ZG Z → C0 ⊗ZG Z → 0
computes the homology of G. Note that Cn⊗ZGZ is the free Z–module on sym-
bols ⟨g0 : . . . : gn⟩, where the gi are distinct elements of G and ⟨g0 : . . . : gn⟩ =
⟨g′
0 : . . . : g′
n⟩ if and only if there is a g ∈ G with ggi = g′
i for i = 0, . . . , n (we
call these homogeneous n–simplices for G).
Thus an element of α ∈ Hn(G; Z) is represented by a sum
∑
ǫi⟨g(i)
0 : . . . : g(i)
n ⟩
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 427
of homogeneous n–simplices for G and their negatives (here each ǫi is ±1).
The fact that this is a cycle means that the ( n − 1)–faces of these homogeneous
simplices cancel in pairs. We choose some speciﬁc way of pair ing canceling faces
and form a geometric quasi-simplicial complex K by taking a n–simplex ∆ i for
each homogeneous n–simplex of the above sum and gluing together ( n − 1)–
faces of these ∆ i that correspond to ( n − 1)–faces of the homogeneous simplices
that have been paired with each other.
As already mentioned, a quasi-simplicial complex actually suﬃces for our pur-
poses. But we can obtain a simplicial complex by replacing K by its barycentric
subdivision if necessary (label the barycenter of each simp lex by an arbitrary
element of G that diﬀers from the G–labels of the barycenters of all proper
faces of that simplex). A standard argument shows that this d oes not change
the homology class represented by K . We thus get a representation of the
homology class in the promised form.
4.1.2 T opological description
Given a space X , any element α ∈ Hn(X; Z) can be represented as f∗[K]
for some map f : |K| → X of an ordered n–cycle to X . If X = BG is a
classifying space for G then this map is determined up to homotopy by the ﬂat
G–bundle f ∗EG over |K|, so this ﬂat bundle determines the homology class
α ∈ Hn(BG; Z) = Hn(G; Z)
Flat G–bundles over |K| are determined by G–valued 1–cocycles on K up to
the coboundary action of G–valued 0–cochains (the 1–cocycle is the obstruction
to extending over |K (1)| a chosen section of the ﬂat bundle over K (0) ). We recall
the basic deﬁnitions.
Let Sq(K) be the set of ordered q –simplices of K . A G–valued 1–cocyle on
K is a map σ : S1(K) → G with the cocyle property:
σ⟨v0, v2⟩ = σ⟨v0, v1⟩σ⟨v1, v2⟩ for ⟨v0, v1, v2⟩ ∈ S2(K) .
For convenience we extend the deﬁnition of σ to reverse-ordered simplices by
σ⟨v1, v0⟩ = σ⟨v0, v1⟩−1 for ⟨v0, v1⟩ ∈ S1(K) .
If τ : S0(K) → G is a 0–cochain, then its coboundary action on 1–cocycles is
to replace σ by
⟨v0, v1⟩ ↦→τ (v0)−1σ⟨v0, v1⟩τ (v1) .
A G–valued 1–cocycle σ determines a G–labeling of simplices: label a sim-
plex ⟨v0, . . . , vk⟩ by (1 , σ⟨v0, v1⟩, . . . , σ⟨v0, vk⟩). Conversely, a G–labeling of
Geometry & Topology, Volume 8 (2004)
428 Walter D Neumann
simplices determines a 1–cocycle: assign to a 1–simplex wit h label ( g1, g2) the
element g−1
1 g2 ∈ G. These correspondences are clearly mutually inverse. When
a 1–cocyle σ is changed by the coboundary action of a 0–cochain τ , the cor-
responding G–labeling ( g0, . . . , gk) of a k –simplex ⟨v0, . . . , vk⟩ is replaced by
(g0τ (v0), . . . , gkτ (vk)).
Thus, we get our desired representative as in subsection 4.1 for a homology
class α ∈ Hn(G; Z) by representing α by a ﬂat G bundle over an ordered
n–cycle K , representing that by a G–valued 1–cycle on K , and then taking
the corresponding G–labeling of K . We want labels of the vertices of any n–
simplex to be distinct, which means that the 1–cocycle shoul d never take the
value 1. Since G is inﬁnite, this can be achieved by modifying by a coboundary
if necessary.
4.2 Deﬁnition of λ : H3(G; Z) → ˆP(C)
Let K be an ordered 3–cycle. We call a closed path γ in |K| a normal path
if it meets no 0– or 1–simplices of K and crosses all 2–faces that it meets
transversally. When such a path passes through a 3–simplex ∆ i , entering and
departing at diﬀerent faces, there is a unique edge E of the 3–simplex between
these faces. We say the path passes this edge E .
(In the following it will often be necessary to distinguish b etween a 1–simplex of
K and the various edges of 3–simplices that are identiﬁed with this 1–simplex.
To avoid excess notation, we will often use the same symbol fo r a 1 simplex of
K and the edges of 3–simplices that are identiﬁed with it, but w e will refer to
“edges” or “1–simplices” to ﬂag which we mean.)
Consider a choice of combinatorial ﬂattening wi for each simplex ∆ i . Then for
each edge E of a simplex ∆ i of K we have a log-parameter lE = lE(∆ i, wi)
assigned. Recall that this log-parameter has the form log z + sπi where z is the
cross-ratio parameter associated to the edge E of simplex ∆ i and s is some
integer. We call ( s mod 2) the parity parameter at the edge E of ∆ i and
denote it δE = δE(∆ i, wi).
Deﬁnition 4.3 Suppose γ is a normal path in |K|. The parity along γ is the
sum ∑
E
δE modulo 2
of the parity parameters of all the edges E that γ passes. Moreover, if γ runs
in the star of some ﬁxed 0–simplex v of K , then the log-parameter along the
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 429
path is the sum ∑
E
±ǫi(E)lE,
summed over all edges E that γ passes, where:
• i(E) is the index i of the simplex ∆ i that the edge E belongs to and ǫi(E)
is the coeﬃcient ±1 that encodes whether the ordering of the vertices of
∆ i(E) matches the orientation of |K| or not.
• the extra sign ± is + or − according as the edge E is passed in a
counterclockwise or clockwise fashion as viewed from the ve rtex.
If γ just encircles a 1–simplex (so the extra signs are all + or all −) we speak
of the parity or log-parameter “around the 1–simplex.”
We assume we have represented an element α ∈ H3(G; Z) by a G–labeled
ordered 3–cycle K as in subsection 4.1. So to each 3–simplex ∆ i of K is
associated a 4–tuple ⟨g(i)
0 : . . . : g(i)
3 ⟩, deﬁned up to left-multiplication by ele-
ments of G, and ǫi = ±1 encodes whether the ordering of the vertices of ∆ i
matches the orientation of K or not. In the following deﬁnition we identify
G = PSL(2, C) with the isometry group Isom +(H3).
Deﬁnition 4.4 Flattening of K Choose z ∈ ∂
H
3
so g(i)
0 z , g(i)
1 z , g(i)
2 z , g(i)
3 z
are distinct points of ∂H
3
for each i (this excludes ﬁnitely many points z ∈
∂H
3
). We then have an ideal hyperbolic simplex shape for each sim plex ∆ i
of K and an associated cross ratio xi = [g(i)
0 z : g(i)
1 z : g(i)
2 z : g(i)
3 z]. A ﬂattening
of K consists of a choice of combinatorial ﬂattenings wi = ℓ(xi; pi, qi) of the
simplices of K such that the parity along any normal path in K is zero and
the log-parameter around each edge of K is zero. If log-parameter along any
normal path in the star of each 0–simplex of K is zero we call it a strong
ﬂattening of K .
Theorem 4.5 For each choice of z as in the above deﬁnition, a strong ﬂat-
tening of K exists.
Recall that our G–labelled ordered 3–cycle K was chosen to represent an ele-
ment α ∈ H3(G; Z) ( G = PSL(2 , C)). The following theorem ﬁnally gives the
deﬁnition of the map λ : H3(G; Z) → ˆB(C).
Theorem 4.6 For any ﬂattening of K the element ∑
i ǫi[xi; pi, qi] ∈ ˆP(C)
only depends on the homology class α ∈ H3(PSL(2, C); Z). We denote it λ(α).
Moreover, λ(α) ∈ ˆB(C) and λ : H3(PSL(2, C); Z) → ˆB(C) is a homomorphism.
Geometry & Topology, Volume 8 (2004)
430 Walter D Neumann
In Remark 10.5 we point out that instead of choosing a single z in the deﬁnition
of ﬂattening, we may choose a diﬀerent z for each vertex of K , and Theorem
4.6 remains true. This is useful in practice (Section 14).
We now give a brief overview of the proofs.
If the extended Bloch group ˆB(C) is to be isomorphic to H3(G; Z) then it must
ﬁt in the same Bloch–Wigner short exact sequence that was giv en for H3(G; Z)
in the Introduction. This is proved in section 7, and section 8 is a digression
describing a related group. These sections are independent of the proofs of
Theorems 4.5 and 4.6, which take up Sections 9 through 11.
First some basic tools are developed in Sections 5 and 6. Sect ion 5 describes
