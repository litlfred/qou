---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-002-21-the-path-2-groupoid-of-a-smooth-manifold
section_title: "The Path 2-Groupoid of a Smooth Manifold"
section_number: 2.1
pages: 6-7
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
The basic idea of the path 2-groupoid is very simple: for a smooth man ifoldX, it is a strict 2-category
whose objects are the points of X, whose 1-morphisms are smooth paths in X, and whose 2-morphisms
are smooth homotopies between these paths. We recall some deﬁn itions from [SW09, SW11].
For points x,y ∈ X, a path γ : x /d47/d47 y is a smooth map γ : [0, 1] /d47/d47 X with γ(0) = x and
γ(1) = y. Since the composition γ2 ◦γ1 of two paths γ1 : x /d47/d47 y and γ2 : y /d47/d47 z should again
be a smooth map we require sitting instants for all paths: a number 0 < ǫ <1
2 with γ(t) = γ(0) for
0 ≤ t < ǫand γ(t) = γ(1) for 1 −ǫ < t≤ 1. The set of these paths is denoted by PX . In order to
make the composition associative and to make paths invertible, we co nsider the following equivalence
relation on PX : two paths γ,γ ′ :x /d47/d47 y are called thin homotopy equivalent if there exists a smooth
map h : [0, 1]2 /d47/d47 X such that
(1) h is a homotopy from γ to γ′ through paths x /d47/d47 y and has sitting instants at γ and γ′.
(2) the diﬀerential of h has at most rank 1.
The set of equivalence classes is denoted by P 1X. We remark that any path γ is thin homotopy
equivalent to any orientation-preserving reparameterization of γ. The composition of paths induces a
well-deﬁned associative composition on P 1X for which the constant paths id x are identities and the
reversed paths γ−1 are inverses; see [SW09, Section 2.1] for more details.
A homotopy h between two paths γ0 andγ1 like above but without condition (2) on the rank of its
diﬀerential is called a bigon in X and denoted by Σ : γ0 /d43/d51 γ1. These bigons form the 2-morphisms
of the path 2-groupoid of X. We denote the set of bigons in X by BX . Bigons can be composed in
two natural ways. For two bigons Σ : γ1 /d43/d51 γ2 and Σ ′ :γ2 /d43/d51 γ3 we have a vertical composition
Σ ′ • Σ : γ1 /d43/d51 γ3.
If two bigons Σ 1 : γ1 /d43/d51 γ′
1 and Σ 2 : γ2 /d43/d51 γ′
2 are such that γ1(1) = γ2(0), we have a horizontal
composition
Σ 2 ◦ Σ 1 :γ2 ◦γ1 /d43/d51 γ′
2 ◦γ′
1.
Like in the case of paths, we consider an equivalence relation on BX in order to make the two
compositions associative and to make bigons invertible: two bigons Σ : γ0 /d43/d51 γ1 and Σ ′ : γ′
0 /d43/d51 γ′
1
are called thin homotopy equivalent if there exists a smooth map h : [0, 1]3 /d47/d47 X such that
(1) h is a homotopy from Σ to Σ ′ through bigons and has sitting instants at Σ and Σ ′.
(2) the induced homotopies γ0 /d43/d51 γ′
0 and γ1 /d43/d51 γ′
1 are thin.
(3) the diﬀerential of h has at most rank 2.
– 6 –
Condition (1) assures that we have deﬁned an equivalence relation o n BX , and condition (2) asserts
that two thin homotopy equivalent bigons Σ : γ0 /d43/d51 γ1 and Σ ′ : γ′
0 /d43/d51 γ′
1 start and end on thin
homotopy equivalent paths γ0 ∼ γ′
0 and γ1 ∼ γ′
1. We denote the set of equivalence classes by B2X.
The two compositions ◦ and • between bigons induce a well-deﬁned composition on B2X. The path
2-groupoid P2(X) is the 2-category whose set of objects is X, whose set of 1-morphisms is P 1X and
whose set of 2-morphisms is B2X. The path 2-groupoid is strict and all 1-morphisms are strictly
invertible. We refer the reader to [SW11, Section 2.1] for a detailed d iscussion.
In this article we describe connections on gerbes by transport 2-f unctors – certain (not necessarily
strict) 2-functors
F : P2(X) /d47/d47 T ,
for some 2-category T , the target 2-category. We note that 2-functors can be pulled back along smooth
maps f :M /d47/d47 X: such a map induces a strict 2-functor f∗ : P2(M ) /d47/d47 P2(X), and we write
f ∗F :=F ◦f∗.
If we drop condition (3) from the deﬁnition of thin homotopy equivale nce between bigons we
would still get a strict 2-groupoid, which we denote by Π 2(X) and which we call the fundamental
2-groupoid ofX. The projection deﬁnes a strict 2-functor P2(X) /d47/d47 Π 2(X). We say that a 2-functor
F : P2(M ) /d47/d47 T is ﬂat if it factors through the 2-functor P2(M ) /d47/d47 Π 2(M ). We show in Section
3.4 that this abstract notion of ﬂatness is equivalent to the vanishin g of a certain curvature 3-form.
