---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-030-25-horizontality-and-relative-invariants
section_title: "Horizontality and relative invariants"
section_number: 2.5
pages: 45-48
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
The aim of this section is to extend the methods of Section 2.2 to surfaces with
strip-like ends. Throughout, (E,π ) will be an exact Lefschetz ﬁbration over such
a surface S, trivial on the ends, together with a Lagrangian boundary co ndition
Q modelled over the ends on pairs L0,e,L 1,e⊂ M of transversally intersecting
exact Lagrangian submanifolds. For {xe}e∈I −∪I + with xe∈L0,e∩L1,e write
χ({xe}) =
∑
e∈I −
aL0,e ,L1,e (xe)−
∑
e∈I +
aL0,e ,L1,e (xe).
By (2.23) A(u) = χ({xe}) +
∫
∂SκQ for all u∈ B({xe}). After ﬁxing a complex
structurej onS which is standard on the ends, and a Je∈ J(M ) for each e, we
45
consider the space
Jh(E,π,j, {Je}) = Jh(E,π,j )∩ J(E,π,j, {Je})
of almost complex structures J, compatible relative to j, which are horizontal
and have prescribed behaviour on the ends. The two condition s do not con-
tradict each other, since the model on each end, the almost co mplex structure
j±×Je on the trivial ﬁbration R±× [0; 1]×M → R±× [0; 1], is obviously
horizontal. A little more thought shows that Jh(E,π,j, {Je}) is contractible.
Choosing J in that space, one ﬁnds that for all u∈ B({xe}),
1
2
∫
S
||(Du)v||2 +
∫
S
f (u)β =A(u) +
∫
S
|| ¯∂Ju||2. (2.31)
Here||·|| is the metric on TEv associated to Ω and J; β∈ Ω 2(S) is a positive
two-form; and f is the function deﬁned by Ω |TEh = f (π∗β|TEh). Because
the symplectic connection is trivial on the ends, f (u) is compactly supported.
(2.31) is obviously the analogue of (2.10), and can be proved in the same way.
Recall that (E,π ) has nonnegative curvature iﬀ f≥ 0. From this we draw two
conclusions:
Lemma 2.23. Assume that (E,π ) has nonnegative curvature, and choose J∈
Jh(E,π,j, {Je}). Then MJ({xe}) =∅ for all{xe} withχ({xe})<− ∫
∂SκQ.
Lemma 2.24. In the same situation, let α be the minimum of aL0,e ,L1,e (x−)−
aL0,e ,L1,e (x+), taken over all e and all x±∈ L0,e∩L1,e for which this is > 0.
Then the spaces MJ ({xe}) is compact, in the Gromov-Floer topology, for all
{xe} such that χ({xe})<−
∫
∂SκQ +α.
Proof. Consider a sequence ( ui) in MJ ({xe}) which converges to ( u,{σe,m})∈
MJ ({xe}). The deﬁnition of γ implies that in (2.24), each aLe, 0,Le, 1(ˆxe,m−1)−
aLe, 0,Le, 1(ˆxe,m)≥α; therefore
A(u)≤A(ui)−
(∑
ele
)
α.
By assumption A(ui) = χ({xe}) +∫
∂SκQ <α , while on the other hand, A(u)≥
0 by nonnegative curvature and (2.31). This is only possible if le = 0 for all e,
so that the limit actually lies in MJ ({xe}).
As before, denote by Mh the space of horizontal sections with boundary
values in Q. The presence of strip-like ends makes this space somewhat s impler
than in the case which we have encountered before. Take an arb itraryu∈ B and
considerue(s,t ) = Γ −1
e ◦u◦γe(s,t ) = (s,t,σ e(s,t ));u is horizontal over the end
e iﬀ σe≡x∈M is constant, in which case the boundary conditions σe(s, 0)∈
Le,0, σe(s, 1)∈ Le,1 imply that x∈ Le,0∩Le,1. Since a horizontal section is
determined by its value at any one point, for any e and any x∈Le,0∩Le,1 there
can be at most one u∈ Mh such that σe≡x. Thus Mh is a ﬁnite disjoint union
of the subsets Mh({xe}) = Mh∩ B({xe}), each of which consists of at most one
element. One easily proves the following limiting case of Le mma 2.23:
46
Lemma 2.25. For (E,π ) and J as in Lemma 2.23, suppose that {xe} satisfy
χ({xe}) =−
∫
∂SκQ; then MJ ({xe}) = Mh({xe}).
To translate these elementary observations into results ab out relative invari-
ants, one needs to address again the question of regularity o f horizontal almost
complex structures; in other words, what is required are ana logues of Lemmas
2.9 and 2.11. For the ﬁrst of these, both the statement and pro of as essentially
the same as in the original situation; the second needs to be a dapted a little.
Lemma 2.26. Let U⊂ S be a nonempty open subset disjoint from the ends,
such that any partial section w : U → E|U which is horizontal and satisﬁes
w(∂S∩ U ) ⊂ Q is the restriction of a u ∈ Mh. Then, given some J ∈
Jh(E,π,j, {Je}), there are J ′∈ Jh(E,π,j, {Je}) arbitrarily close to it and which
agree with it outside π−1(U ), such that for all {xe}, any u∈ MJ ({xe})\ Mh is
regular.
Lemma 2.27. Let (E,π ) andJ be as in Lemma 2.23. If u∈ Mh is a horizontal
section with A(u) = 0 , then kerDu,J = 0.
Proof. Formally, taking the second derivative of (2.31) at u yields the same
formula (2.15) as in the case of a compact S, but a little care needs to be
exercised about its validity. It certainly holds for those e lements ofT Bu ={X∈
C∞(u∗TEv) : Xz∈ T (Qz) for z∈ ∂S} which are compactly supported, and
by continuity, for allX in theW 1,2-completion; to be precise, this Sobolev space
is with respect to the metric ||·|| and the connection∇u onu∗TEv. We actually
want to use the formula with X∈ W1
u and this is a space of W 1,p-sections with
p> 2, hence not contained in W 1,2. However, if one assumes additionally that
Du,JX = 0 there is no problem, because any such X is smooth and decays
exponentially on the ends, as do its derivatives.
From A(u) = 0 and (2.31) it follows that f (u)≡ 0, so that the Hessians
Hess(f|Ez)u(z) are nonnegative. One then sees from (2.15) that any X∈ W1
u
with Du,JX = 0 satisﬁes ∇uX = 0. Choose some end e and write x = xe.
The trivialization Γ e induces a trivialization of the vector bundle γ∗
e (u∗TEv)→
R±× [0; 1], which identiﬁes it with the trivial bundle with ﬁbre TMx. In this
way,Y =γ∗
eX becomes a map R±× [0; 1]→TMx. Since the connection ∇u is
compatible with the trivialization, ∇uX = 0 implies that Y must be constant.
On the other hand, the boundary conditions which are part of t he deﬁnition
of T Bu and of W1
u tell us that Ys,k∈ T (Le,k)x for k = 0, 1. Because the Le,k
intersect transversally, it follows that Y = 0, hence that X|im(γe) = 0. Since
X is covariantly constant, it must be zero everywhere.
The next result summarizes what progress we have made so far, as well as
the implications for the coeﬃcients νJ ({xe}) of the relative invariant.
47
Proposition 2.28. Assume that (E,π ) has nonnegative curvature, and that
any u∈ Mh satisﬁes A(u) = 0 and indDu,J = 0. Set κ =
∫
∂SκQ.
(i) Let U⊂S be a nonempty open subset, disjoint from the ends, such that a ny
partial horizontal section w :U→ E|U with w(∂S∩U )⊂ Q extends to a u∈
Mh. Then for any J∈ Jh(E,π,j, {Je}) there are J ′∈ Jreg,h(E,π,Q,j, {Je}) =
Jh(E,π,j, {Je})∩ Jreg (E,π,Q,j, {Je}) arbitrarily close to J, and which agree
with it outside π−1(U ).
(ii) If Je∈ Jreg(M,L 0,e,L 1,e) for all e, and J∈ Jreg,h (E,π,Q,j, {Je}), then
νJ ({xe}) =
{
0 if χ({xe})<−κ,
#Mh({xe}) if χ({xe}) =−κ.
Proof. (i) Take aJ ′ as given by Lemma 2.26. Then all u∈ MJ ′({xe}) are regular
except possibly for the horizontal ones. These satisfy A(u) = 0, so we can apply
Lemma 2.27 to them, showing that ker Du,J ′ = 0, and by assumption on the
index, that coker Du,J ′ = 0; which means that they are regular as well. (ii)
This follows immediately from Lemmas 2.23 and 2.25, in view o f the deﬁnition
of νJ ({xe}).
An algebraic language suitable for encoding results of this kind is that of
R-graded vector spaces, that is to say vector spaces C equipped with a splitting
C = ⨁
r∈RCr. All vector spaces occurring here will be over Z/2 and ﬁnite-
dimensional; in particular, their support supp(C) = {r ∈ R : Cr ⁄= 0} is
always a ﬁnite set. Let I⊂ R be an interval. We say that C has gap I if there
are no r,s ∈ supp(C) with r−s∈ I. A map f : C → D between graded
R-vector spaces is said to be of order I if f (Cr)⊂ ⨁
s∈r+IDs for all r.
Floer cochain groups are obvious examples: C = CF (L0,L 1) is canonically
R-graded, with Cr the subspace spanned by those ⟨x⟩with aL0,L1(x) = r.
Because of its gradient ﬂow interpretation, the Floer diﬀer entialdJ is of order
(0;∞). In a rather trivial way, this can always be strengthened sl ightly; namely,
there is an α >0 such that C has gap (0; α), and then dJ is of order [ α;∞).
One can reformulate Proposition 2.28(ii) in this language a s follows:
Lemma 2.29. Take (E,π ), Q and κ as in Proposition 2.28, with Je,J as in
part (ii). Then the map CΦ 0
rel(E,π,Q,J ) is of order [−κ;∞). For a more
precise statement, take α> 0 to be the minimum of χ({xe})+κ, ranging over all
{xe} where this is positive. Then CΦ rel
