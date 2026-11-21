---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-093-g-drinfeld-symmetric-space
section_title: "Drinfeld symmetric space."
section_number: G
pages: 226-230
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
To each lattice M in V we associate an R-scheme
P(M): = Proj(SymRM).
Obviously the scheme P(M) depends only on the similarity class; so we
should write as P(Λ), where Λ = [M]. The scheme P(M) is isomorphic to
Pn
R; but the isomorphism cannot be taken canonically, while there exists the
2. DRINFELD SYMMETRIC SPACE.
223
canonical isomorphism V ∼= P(M) ⊗R K due to the canonical isomorphism
M ⊗R K ∼= V . So we get a bijection:
∆0
∼
−→

(P, φ)
P ∼
→Pn
R,
φ: P ⊗R K ∼
→P(V )

/ ∼,
where (P1, φ1) ∼(P2, φ2) if and only if there exists an R-isomorphism
Φ: P1
∼
→P2 which makes the diagram
P1 ⊗R K
Φ⊗RK
−→
P2 ⊗R K
φ1 ↓
↓φ2
P(V )
=
P(V )
commutative.
Next we consider two vertices Λ1 and Λ2 which are adjacent with each
other. The canonical isomorphism between the generic ﬁbers induce a nat-
ural birational map between P(Λ1) and P(Λ2). More explicitly, taking rep-
resentatives Mi ∈Λi (i = 1, 2) so that M1 ⊋M2 ⊋πM1, we have the
birational map from P(Λ1) to P(Λ2) induced by M2֒ →M1. We deﬁne the
join P(Λ1) ∨P(Λ2) to be the closure of the graph in P(Λ1) ×R P(Λ2) of this
rational map. It is easily seen that the join P(Λ1) ∨P(Λ2) is R-isomorphic
to the blow-up of P(Λ1) at the closed subscheme Proj(SymkM1/M2). In
particular, the closed ﬁber of P(Λ1)∨P(Λ2) consists of two rational varieties
intersecting transversally.
Lemma 2.1. The operation ∨is associative and commutative.
The proof is straightforward, and left to the reader. By the lemma, we
can extend the construction to any ﬁnite subcomplex of ∆. More precisely,
for a ﬁnite subcomplex S, we take the joins of all vertices in S; the resulting
R-scheme is denoted by P(S). The scheme P(S) is a regular projective scheme
over R having the following properties:
(i) The generic ﬁber is canonically isomorphic to P(V ).
(ii) The closed ﬁber is a reduced normal crossing of non-singular rational
varieties of which the dual graph coincides with S.
We want to do this for a general convex subcomplex of ∆; this cannot
be done in terms of schemes because we have to consider a limit of blow-up’s
of Pn
R centered in the closed ﬁber. But we can do this in terms of formal
schemes, or rigid analytic spaces. Let ∆∗be a convex subcomplex of ∆. For
any ﬁnite subcomplex S of ∆∗we deﬁne bΩ(S) to be the completion of P(S)
along the closed ﬁber. Consider the maximal Zariski open subset bΩ(S)′ of
bΩ(S) such that, for any ﬁnite subcomplex T of ∆∗containing S, the induced
morphism ρT
S: bΩ(T) →bΩ(S) gives an isomorphism restricted to the pull-back
of bΩ(S)′.
Deﬁnition 2.2. For a convex subcomplex ∆∗of ∆we deﬁne
bΩ(∆∗): =
[
S: ﬁnite
bΩ(S)′,
224
B. OVERVIEW OF THEORY OF p-ADIC UNIFORMIZATION.
where S runs through all ﬁnite subcomplex of ∆∗. The corresponding rigid
analytic space (Raynaud generic ﬁber) is denoted by Ω(∆∗). In case ∆∗= ∆
we simply write bΩ= bΩ(∆) and Ω= Ω(∆). The rigid analytic space Ωis
called the Drinfeld symmetric space.
The formal scheme bΩ(∆∗) is formally locally of ﬁnite type, of which the
closed ﬁber is the normal crossings of non-singular rational varieties having
the dual graph isomorphic to ∆∗. By deﬁnition, the group PGL(n + 1, K)
naturally acts on bΩ, and hence Ω.
Example 2.3. Let us consider bΩin n = 2. The closed ﬁber bΩ0 consists
of countably many components which are all isomorphic to the surface B
considered in 1.3. In each component every k-rational line is a double curve
in bΩ0, and every k-rational point is a triple point.
Structure of Ω. First we note that, as a point set, we have an equality
Ω= Pn,an
K
\
[
H∈H
H,
where H is the set of all K-rational hyperplanes.
Here we do not attempt to give a proof of this fact, but rather give a
sketchy explanation in order to get a feeling. We limit ourselves to n = 1
case just for simplicity. The formal scheme bΩis, roughly speaking, the limit
of successive blow-up’s
· · · −→Ui
ρi
−→Ui−1 −→· · · −→U0
with U0 = P1
R and ρi the blow-up centered at all the k-rational points in
the closed ﬁber of Ui−1. Let z be a point in the generic ﬁber P1
K of each
Ui. We consider the closure z of z in each Ui. Since Ui is a regular scheme,
the section z intersects the closed ﬁber at a smooth point transversally. If
z is not a K-rational point, then for suﬃciently large N, z intersects the
closed ﬁber of Ui at a non-k-rational smooth point for i > N. But, if z is
K-rational, z intersects the closed ﬁber always at a k-rational point which is
in the next blow-up center. So if we consider the limit, such formal sections
determined by K-rational points does not exist any more, while those by
non-K-rational points certainly exist. This explains the above equality in
n = 1. For higher n we can apply the similar argument.
Next we discuss the analytic structure of Ω; viz. we show how to in-
troduce an admissible covering to Ω; since we have constructed the rigid
analytic space Ωfrom the formal model, we must have one such covering
such that the associated formal model recovers bΩ.
This can be actually
described in an elegent way in terms of norms: A non-negative real valued
function α: V →R≥0 is said to be a norm over K if it satisﬁes:
(i) α(x) > 0 whenever x̸ = 0.
(ii) For a ∈K, α(ax) = |a|α(x).
(iii) α(x + y) ≤max{α(x), α(y)}.
2. DRINFELD SYMMETRIC SPACE.
225
Two norms α and α′ over K is said to be similar if α′ = λα for some λ ∈R>0.
The set of all similarity classes of norms on V over K forms in an obvious
way a topological space. The following fact is well-known ([GI63]):
Proposition 2.4. The topological space of similarlity classes of norms on V
over K is PGL(n + 1, K)-equivaliantly homeomorphic to the topological
realization |∆| of the Bruhat-Tits building ∆.
The homeomorphism is given as follows: To any lattice M we need to
associate a norm αM. For a non-zero x ∈V , the set {a ∈K | ax ∈M} is a
fractional ideal of R, and hence is of form (πm). We then deﬁne αM(x) = qm
for non-zero x ∈V , and αM(0) = 0. It is easily veriﬁed that αM is a norm.
The similarity class of αM depends only on the similarity class of M. Thus
we get a mapping from ∆0 to the set of similarity classes of norms. Let
Λ0 and Λ1 be vertices adjacent with each other.
We can choose a basis
e0, . . . , en of V such that M0 = Ln
i=0 Rei and M1 = Ln−1
i=0 Rei ⊕Rπen give
representatives of Λ0 and Λ1, respectively. Then the norms αM0 and αM1
are given by
αM0(
n
X
i=0
aiei)
=
max{|a0|, . . . , |an|},
αM1(
n
X
i=0
aiei)
=
max{|a0|, . . . , |an−1|, |π|−1|an|},
respectively. For 0 < t < 1, the class of the norm
αt(
n
X
i=0
aiei) = max{|a0|, . . . , |an−1|, |π|−t|an|}
corresponds to the point tΛ0 + (1 −t)Λ1 on the edge connecting Λ0 and Λ1.
Now, to any point z = (z0 : · · · : zn) ∈P(V ) (subject to some K-basis
{e0, . . . , en}of V ) we associate, up to invertible factor, a non-negative real
valued function
αz(
n
X
i=0
aiei) =

n
X
i=0
aizi

on V . Note that this determines a class of norm if and only if z is not lying
in any K-rational hyperplane. Thus we get a mapping
ρ: Ω−→|∆|.
The admissible covering in question is actually given by the collection of
subsets of Ωconsisting of pull-backs of each simplices of |∆| by ρ.
For
example, notation being as above,
ρ−1(Λ0) = {|z0| = · · · = |zn| = 1} \
[
H
{(z0 : · · · : zn) mod π ∈H},
where H runs through all hyperplanes in Pn
k, and
ρ−1(tΛ0 + (1 −t)Λ1) = {|z0| = · · · = |zn−1| = 1, |zn| = |π|−t}
