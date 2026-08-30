---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-008-3-fusion-categories-over-c
section_title: "Fusion categories over C"
section_number: 3
pages: 10-12
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
The goal of this subsection is to prove Theorem 2.3, Proposition 2.9, Proposition
2.12, and discuss their consequences.
Let C denote a fusion category over C. We will denote representatives of iso-
morphism classes of simple objects of C by Xi, i ∈ I, with 0 ∈ I labeling the
neutral object 1. Denote by ∗ :I →I the dualization map. (We note that at the
level of labels, there is no distinction between right and left dualizatio n, since by
Proposition 2.1, V is isomorphic to V ∗∗ for any simple object V ).
3.1. Proof of Theorem 2.3. By Theorem 2.6, there exists an isomorphism of
tensor functors g : Id → ∗ ∗ ∗∗. Let us ﬁx such an isomorphism. So for each simple
V ∈ C we have a morphism gV :V →V ∗∗∗∗ such thatgV ⊗W =gV ⊗gW , and gV ∗ =
(g−1
V )∗. For all simple V , let us ﬁx an isomorphism aV :V →V ∗∗ such thata2
V =gV
(a2
V makes sense as Hom( V,V ∗∗) is canonically isomorphic to Hom( V ∗∗,V ∗∗∗∗),
and so aV can also be regarded as an element of Hom( V ∗∗,V ∗∗∗∗)). Then aV ∗ =
ǫV (a−1
V )∗, where ǫV = ±1, and ǫVǫV ∗ = 1. Deﬁne d(V ) = TrV (aV ), in particular
di =d(Xi). These numbers are not at all canonical – they depend on the cho ices we
made. Nevertheless, it is easy to see from the deﬁnition that |V |2 =ǫVd(V )d(V ∗).
Now let us take any simple objects V,W ∈ C and consider the tensor product
aV ⊗aW :V ⊗W → (V ⊗W )∗∗. We have V ⊗W = ⊕U Hom(U,V ⊗W ) ⊗U , so we
haveaV ⊗aW = ⊕bVW
U ⊗aU , wherebVW
U : Hom(U,V ⊗W ) → Hom(U ∗∗,V ∗∗⊗W ∗∗).
ON FUSION CATEGORIES 11
The source and target of this map are actually canonically isomorphic , so we can
treat bVW
U as an automorphism of Hom( U,V ⊗W ). Also, since a2
V = gV and
gV ⊗W =gV ⊗gW , we get ( bVW
U )2 = 1.
Let bik
j := bXiXk
Xj . Let Tik
j = tr(bik
j ). Since ( bik
j )2 = 1, its eigenvalues are ±1,
hence Tik
j are integers.
By the deﬁnition of bik
j , we have
didk =
∑
j∈I
Tik
j dj
Let Ti be the matrix such that ( Ti)kj =Tik
j , and let d be the vector with compo-
nentsdi. This vector is clearly nonzero (e.g., d0 ⁄= 0), and we have
Tid =did.
Thus, d is a common eigenvector of Ti with eigenvalue di.
Letǫi =ǫXi. Then we have: d is an eigenvector of the matrix Ai =ǫiTiTi∗ with
eigenvalue |Xi|2.
We claim that Ti∗ =ǫiTt
i . This implies the theorem, as in this case Ai =TiTt
i ,
which is nonnegative deﬁnite (since the entries of Ti are integer, hence real), so its
eigenvalues, including |Xi|2, have to be nonnegative.
To prove that Ti∗ =ǫiTt
i , we need to show that Ti∗k
j =ǫiTij
k . But this, in turn,
follows from the equality bi∗k
j =ǫi(bij
k )∗ (which makes sense since we have canonical
isomorphisms Hom(U,V ⊗W ) → Hom(V ∗ ⊗U,W ) → Hom(W,V ∗ ⊗U )∗, the latter
by semisimplicity).
It remains to prove the last equality. Let f :Xj →Xi ⊗Xk be a morphism. By
the deﬁnition, bik
j f = (ai ⊗ak)fa −1
j . On the other hand, f gives rise to an element
f ′ :Xi∗ ⊗Xj →Xk, given by f ′ = (evi ⊗ 1)(1 ⊗f ), and hence to a linear function
on Hom(Xk,Xi∗ ⊗Xj) given by f ′′(h) = (evi ⊗ 1)(1i∗ ⊗f )h ∈ End(Xk) = C (for
brevity we omit associativity maps and use the same notation for a mo rphism and
its double dual). Now, we have
(bik
j f )′′(h) = (ev i ⊗ 1)(1i∗ ⊗ (ai ⊗ak)fa −1
j )h
= ǫiak(evi ⊗ 1)(a−1
i∗ ⊗fa −1
j )h
= ǫi(evi ⊗ 1)(1 ⊗f )(a−1
i∗ ⊗a−1
j )hak
= ǫi(evi ⊗ 1)(1 ⊗f )(ai∗ ⊗aj)ha−1
k ,
where the last equality due to the facts that gV ⊗W =gV ⊗gW , and aV =gVa−1
V .
Thus,
(bik
j f )′′(h) = f ′′(bi∗j
k h),
as desired. Theorem 2.3 is proved.
Remark 3.1. Here is a modiﬁcation of the above proof, which is simpler but
requires an extension of the category C.
The ﬁrst step is to prove the result in the case of pivotal categorie s. This is a
substantially simpliﬁed version of the above proof, since in the pivota l case ǫi and
bik
j are 1, so Tik
j are equal to Nik
j , the multiplicity of Xj in Xi ⊗Xk.
The second step is reduction to the pivotal case. To do this, take t he isomorphism
g :Id → ∗ ∗ ∗∗ as tensor functors constructed in the proof of Theorem 2.6. Deﬁ ne
the fusion category ˜C, whose simple objects are pairs ( X,f ), where X is a simple
12 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
object of C, and f :X →X ∗∗ is an isomorphism, such that f ∗∗f =g. It is easy to
see that this fusion category has a canonical pivotal structure. Thus, |X|2> 0 in ˜C.
However, we have the forgetful functor F : ˜C → C , F (X,f ) = X, which obviously
preserves squared norms. Hence, |V |2 > 0 for simple objects V in C (since for any
V there exists f :V →V ∗∗ such that f ∗∗f =g), which completes the proof.
