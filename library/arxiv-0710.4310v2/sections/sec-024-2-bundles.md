---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-024-2-bundles
section_title: "2-Bundles"
section_number: null
pages: 37-39
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let G = (∂ : E →G,⊲ ) be a Lie crossed module. Let the associated diﬀerential
crossed module be G = (∂ : e → g,⊲ ). Fix a smooth manifold M and a smooth
principal G-bundle π : P →M .
A natural weakening of the notion of a categorical connection ( ω,m ) in P is
to consider m to be only locally deﬁned on P , but so that ∂(mi) = Ω, for any
i. Here mi ∈ A2(Pi, e), where Pi = π−1(Ui) and {Ui} is an open cover of P .
This can be done by using the general theory of 2-bundles [BS], or no n-abelian
gerbes [BrMe], which correspond to 2-bundles with structure cros sed modules
of the form G = Aut(E) of example 11.
To this end, let {Ui} be an open cover of M . We can suppose that, for any
i1,...,i n, the n-fold intersection Ui1,...,in
.=Ui1 ∩... ∩Uin is contractible. A G-
2-bundle can be described by using smooth maps gij :Uij →G andhijk : Uijk →
E. These have to satisfy the cocycle conditions: ∂(h−1
ijk )gijgjk =gik andhijkhikl =
(gij⊲hjkl )hijl for any i,j,k,l . Therefore a G-2-bundle does not necessarily de-
ﬁne a G-principal bundle, unless ∂(hijk ) = 1 for each i,j,k . If this condition is
satisﬁed, a G-2-bundle will be called a special G-2-bundle.
The main purpose of this article was the construction of categorica l holonomies,
in other words of smooth categorical group maps P2(M, ∗) → C (G), or, equiva-
lently of smooth crossed module maps Π 2,1
2 (M, ∗) → G ; see 1.3 for this notation.
From the point of view of 2-dimensional holonomy, G-2-bundles are natural ob-
jects; see [BS]. However, our notion of categorical holonomy requ ires the exis-
tence of a smooth group morphism π1
1(M, ∗) →G, and therefore of a principal
G-bundle with connection; see [CP]. This makes it natural to work with special
G-2-bundles.
A special G-2-bundle with connection can be speciﬁed by the following data:
(Here A = ker(∂) ⊂E, and a is its Lie algebra; note that A is central in E).
1. A principal G-bundle π : P →M with a connection ω.
37
2. An open cover {Ui} ofM such that for anyi1,...,i n then-fold intersection
Ui1,...,in is contractible. Let Pi1,...,in =π−1(Ui1,...,in ).
3. G-equivariantA-valued functions eijk : Pijk → A. These are required to
satisfy: eijkeikl =ejkleijl.
4. G-equivariant horizontal 2-forms mi ∈ A2(Pi, e). These are required to
satisfy ∂(mi) = Ω, the curvature 2-form of ω.
5. G-equivariant horizontal 1-forms ηij ∈ A1(Pij, a). These are required to
satisfy:
mi −mj =Dηij and
(
De−1
ijk
)
eijk =ηij +ηjk −ηik,
where D denotes the exterior covariant derivative with respect to ω, in
other words, by using lemma 30,
mi−mj =dηij +ω∧⊲ηij and
(
de−1
ijk +ω ∧⊲e−1
ijk
)
eijk =ηij +ηjk −ηik.
One passes from this setting to the setting in [BS] by choosing local sections fi
ofPi, and deﬁning the functions gij : Uij →G in the usual way: figij =fj. Next
deﬁne hijk = f ∗
i (eijk ), Ai = f ∗
i (ω), Bi = f ∗
i (mi) and aij = f ∗
i (ηij). Then this
data deﬁnes the local diﬀerential forms of Baez and Schreiber [BS ], satisfying
equations corresponding to our special G-2-bundles with connection, in partic-
ular with the transition functions gij satisfying the usual cocycle condition for
a principal G-bundle. Note that the Baez-Schreiber local diﬀerential forms ca n
be seen as a generalisation to arbitrary G of the local description of non-abelian
gerbes, with G = Aut(E), of Breen and Messing [BrMe].
Special G-2-bundles with connection deﬁne group morphisms π1
1(M, ∗) →G.
However, the deﬁnition of the categorical holonomy on a 2-track [Γ ] ∈ P2(M, ∗)
is tricky if one is to deal with the fact that m is not globally deﬁned. This can be
done (and will appear in a future work), however, it will only be, a prio ri, deﬁned
up to multiplication by central elements of E, and thus it should not deﬁne
holonomies P2(M, ∗) → C (G), unless we restrict to elements of π2
2(M, ∗), as in
[MP]. For instance, it is easy to see that given two categorical G-connections
(ω,m ) and (ω,m ′) in P then given a 2-path Γ ∈ P 2(M, ∗) we have
e′
Γ = exp
(∫ 1
0
η
(
~d
dtγ1(t)
)
Hω (γ1,t,u)
dt
)
exp
(
−
∫ 1
0
η
(
~d
dtγ2(t)
)
Hω (γ2,t,u)
dt
)
eΓ
wherem −m′ =Dη =dη +ω ∧⊲η, moreover η ∈ A1(P, a) is G-equivariant and
horizontal. We have put γ1 = ∂u(Γ) and γ2 = ∂d(Γ). Also eΓ and e′
Γ denote
2-dimensional holonomy with respect to ( ω,m ) and (ω,m ′), respectively.
For this reason we feel that it is likely that the construction in this ar ticle,
with a globally deﬁned m, will describe all categorical holonomies P2(M, ∗) →
C(G), especially if we consider a generalised unbased setting. We will inves tigate
this issue in a future publication.
38
