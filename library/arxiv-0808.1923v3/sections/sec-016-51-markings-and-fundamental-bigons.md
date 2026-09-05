---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-016-51-markings-and-fundamental-bigons
section_title: "Markings and Fundamental Bigons"
section_number: 5.1
pages: 46-49
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
Surface holonomy of gerbes has so far only be studied in the abelian c ase, i.e. for gerbes with structure
2-group G = BS1; see e.g. [Mur96]. It is understood that an abelian gerbe with connec tion over M
provides an S1-valued surface holonomy for smooth maps φ : S /d47/d47 M deﬁned on closed oriented
surfacesS. Various extensions have been studied for oriented surfaces with boundary [CJM02, GR02],
closed unoriented (in particular unorientable) surfaces [SSW07], an d unoriented surfaces with boundary
[GSW11].
Let us try to explain why the step from abelian to non-abelian surfac e holonomy is so diﬃcult,
by looking at the analogous but easier situation of ordinary holonomy of a connection on a principal
bundle P over M . In the abelian case, say with structure group S1, holonomy is deﬁned for closed
oriented curves inM . Passing to a non-abelian structure group G, we have two possibilities. The ﬁrst
is to choose additional structure on the closed oriented curve, na mely a point x ∈M , in which case the
holonomy is a well-deﬁned automorphism of the ﬁbre Px of the bundle P over the point x. The second
possibility is to project the value of the holonomy into an appropriate quotient, for example along the
map Aut(Px) /d47/d47 Gred into the set Gred of conjugacy classes of G. This quotient is designed such
– 46 –
that a diﬀerent choice of x yields the same element in Gred, and so P has a well-deﬁned Gred-valued
holonomy for closed oriented curves.
Choosing a point in a closed oriented curve means to represent it as a path (up to thin homotopy).
The objective of this section is to describe how to represent a close d oriented surface φ : S /d47/d47 M
as a bigon in M . It will be convenient to adapt the following standard terminology fr om the theory
of Riemann surfaces to our setting. Suppose S is a closed oriented surface of genus g. A marking of
S is a point x ∈ S together with a set M = {αi,βi}g
i=1 of paths αi :x /d47/d47 x and βi :x /d47/d47 x such
that the homotopy classes [ αi] and [βi] of the paths form a presentation of the fundamental group of
S based at x with the relation that [ τM] = 1, where
τM :=β−1
g ◦α−1
g ◦βg ◦αg ◦... ◦β−1
1 ◦α−1
1 ◦β1 ◦α1.
In other words,
π1(S,x ) = ⟨[αi], [βi] | [τM] = 1 ⟩.
Next we formulate — in the language of bigons — the statement that t he path τM can be collapsed
to the point x in such a way that the collapsing homotopy parameterizes the surfa ceS. The challenge
is that such a homotopy cannot simultaneously be a bigon and a good p arameterization. We propose
the following notion.
Deﬁnition 5.1.1. A fundamental bigon with respect to the marking (x, M) is a bigon Σ : τM /d43/d51 idx
such that there exist:
(a) a polygon P ⊆ R2 and a surjective smooth map π : P /d47/d47 S that is an embedding when restricted
to the interior of P and preserves the orientations.
(b) a surjective continuous map k : [0 , 1]2 /d47/d47 P that restricts to a diﬀeomorphism between the
interiors and preserves the orientations, such that there e xists a vertex v0 of P with v0 =k(s, 0) =
k(s, 1) = k(1,t ) for all 0 ≤s,t ≤ 1.
(c) a smooth map h : [0, 1] × P /d47/d47 S with h0 =π and h1 ◦k = Σ , such that for each edge e of P the
restrictionh|[0,1] ×e has rank one, and h(−,v ) = x for each vertex v.
In this deﬁnition the polygon P serves as the standard parameter domain of the surface, and th e
mapπ : P /d47/d47 S is such a parameterization. The map k : [0, 1]2 /d47/d47 P is responsible for the transition
between the standard parameter domain P and the parameter domain [0 , 1]2 for bigons. The map h
ensures that the fundamental bigon Σ is homotopic to the “bigonize d” standard parameterization,
π ◦k. The various conditions on k and h ensure that the homotopy h ◦k is constantly equal to x
over the boundary parts of [0 , 1]2 that are parameterized by ( s, 0), (s, 1), and (1,t ), and ensure that it
restricts to a thin homotopy between the path ( π ◦k)(0, −) and τM over the remaining boundary part
(0,t ).
A marking will be called good, if it admits a fundamental bigon. The following three lemmata
elaborate some properties of good markings and fundamental bigo ns.
Lemma 5.1.2. Every closed oriented surface S has a good marking.
Proof. It is well-known that every surface S of positive genus g > 0 has a “fundamental polygon”
P ⊆ C with 4g edges, together with a map π : P /d47/d47 S that has all required properties. It can be
– 47 –
arranged such that all vertices go to a single point x ∈S, and — if the 4 g edges are parameterized by
A1,B 1,A ′
1,B ′
1,A 2,... : [0, 1] /d47/d47 P in counter-clockwise order starting at a vertex v0 — then
π(Ai(1 −t)) = π(A′
i(t)) and π(Bi(1 −t)) = π(B′
i(t)). (5.1.1)
Let D ⊆ C denote the disc centered at −1 ∈ C. It is obvious that P and D are homeomorphic. The
homeomorphism can be arranged such that (i) it preserves orienta tions, (ii) it is a smooth embedding
when restricted to the complement of the vertices of P, and (iii) the vertices map to points equidistantly
distributed over the boundary of D, with v0 at 0 ∈ C. We deﬁne
k′ : [0, 1]2 /d47/d47 D : (s,t ) ✤ /d47/d47 (1 −s)(e2πit − 1).
Under the homeomorphism between P and D, this gives the map k with all required properties.
The map h : [0, 1] × P /d47/d47 S is chosen such that h1 : P /d47/d47 S is constantly equal to x in
neighborhoods of all vertices, and such that (5.1.1) remains true w ithh1 instead of π. Then we deﬁne
Σ := h1 ◦k
This is smooth because h1 is locally constant at all points where k is not smooth. We consider for
0 ≤k ≤ 4g − 1 the map pk : [0, 1] /d47/d47 [0, 1] : t ✤ /d47/d47 k+t
4g that squeezes the interval into the k-th of 4g
many pieces. Then, we deﬁne for i = 1,..,g
αi :=π ◦ Σ(0, −) ◦p4i−4 and βi :=π ◦ Σ(0, −) ◦p4i−3,
which give smooth maps with sitting instants, each going from x tox, Thus, (x, M) with M := {αi,βi}
is a marking, and (5.1.1) imply that Σ is a bigon Σ : τM /d43/d51 idx.
The case of genus g = 0 can be treated in a similar way using the disc D1 with one marked point;
this is left as an exercise. □
The main idea behind the deﬁnition of a fundamental bigon is that the in tegral of a 2-formω ∈ Ω 2(S)
overS can be computed over a fundamental bigon.
Lemma 5.1.3. SupposeS is a closed oriented surface with a good marking (x, M). Let Σ be a funda-
mental bigon with respect to (x, M). Then,
∫
S
ω =
∫
[0,1]2
Σ ∗ω
for all 2-forms ω ∈ Ω 2(S).
Proof. We choose the structure ( P,k,π,h ) of Deﬁnition 5.1.1. Then,
∫
S
ω =
∫
P
π∗ω =
∫
P
h∗
1ω =
∫
int(P)
h∗
1ω =
∫
(0,1)2
Σ ∗ω =
∫
[0,1]2
Σ ∗ω.
The second equality holds because the homotopy h between h0 = π and h1 has rank one on the
boundary. The other equalities hold immediately due to the assumptio ns on all the involved maps. □
Finally, we show that the choice of a fundamental bigon is essentially u nique.
Lemma 5.1.4. LetS be a closed oriented surface and (x, M) be a marking. Suppose Σ : τM /d43/d51 idx
and Σ ′ :τM /d43/d51 idx are two fundamental bigons with respect to the marking (x, M). Then, Σ and Σ ′
are thin homotopy equivalent in the sense of Section 2.1.
– 48 –
Proof. We choose for both fundamental bigons the structures ( P,k,π,h ) and ( P ′,k ′,π ′,h ′) of De-
ﬁnition 5.1.1. We can assume that P = P ′, since any two polygons are diﬀeomorphic, and such
diﬀeomorphism can be absorbed into π′ and k′. We can assume that P is convex; in that case it is
easy to see that k and k′ are homotopic, with the homotopy ﬁxing the three boundary compo nents
that map to v0, and restricting to a homotopy with values in ∂P over the forth boundary component.
The homotopies h and h′ restrict on the boundary to thin homotopies π|∂P ≃ τM and π′|∂P ≃ τM.
By a version of Alexander’s trick, we obtain a smooth homotopy π ≃π′ that ﬁxes all vertices and has
rank one over the edges. Then we have chains of homotopies
Σ ≃h1 ◦k ≃h0 ◦k ≃π ◦k ≃π ◦k′ ≃π′ ◦k′ ≃h′
0 ◦k′ ≃h′
1 ◦k′ ≃ Σ ′
which are all smooth and have rank one restricted over the bounda ry. By dimensional reasons, this
homotopy can at most have rank two everywhere. This means that it is a thin homotopy between Σ
and Σ ′. □
Next we come to the deﬁnition of surface holonomy. Since the gener ic transport 2-functor is not
strict, we have to deal with the diﬀerence between the 1-morphism tra(φ∗τM) and the 1-morphism
traφ,M :=
g∏
i=1
tra(αi) ◦ tra(βi) ◦ tra(α−1
i ) ◦ tra(β−1
i ),
for which we may agree for an arbitrary convention how to put pare ntheses in case T has a non-trivial
associator. The relation between these two 1-morphisms is given by a 2-morphism
cφ,tra : traφ,M /d43/d51 tra(φ∗τM)
made up from the compositors of tra in a unique way, due to the cohe rence axiom for compositors
(this is axiom (F3) in [SW, Appendix A]).
Deﬁnition 5.1.5. Let tra : P2(M ) /d47/d47 T be a transport 2-functor. Suppose S is a closed oriented
surface equipped with a good marking (x, M) and a smooth map φ :S /d47/d47 M . Let Σ be a fundamental
bigon for (x, M). The 2-morphism
Holtra(φ,x, M) := tra(φ∗Σ) •cφ,tra : traφ,M /d43/d51 tra(idφ(x))
in T is called the surface holonomy of tra.
Note that the surface holonomy is independent of the choice of the fundamental bigon due to
Lemma 5.1.4. On the other hand, the surface holonomy does depend on the choice of the marking
(x, M). Even worse, it is not invariant under isomorphisms between trans port 2-functors. It is the
purpose of the following discussion to improve these dependence iss ues.
