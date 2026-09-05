---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-007-5-relationship-with-topological-chiral-homology
section_title: "Relationship with topological chiral homology"
section_number: 5
pages: 40-43
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
5.1. Review of topological chiral homology ` a la Lurie. Let A be an En-
algebra and M a manifold of dimension m which is (stably) n-framed, that is a
manifold of dimension m equipped with a framing of M×Dn−m. The topological
chiral homology of M with coeﬃcients in A was deﬁned in [26, 25] and [11] and
will be denoted
∫
MA. Note that the above deﬁnition does depend on the framing
in general, even though it is not explicit in the notation 5. Further
∫
MA is an
En−m-algebra in general, see [26, 25]. We refer to the aforementioned re ferences as
well as to[11, 1, 2] for a precise deﬁnition. If X is a manifold, let N (Disj(X)) be the
∞-category associated to the poset given by ﬁnite disjoint union of o pen sets in X
homeomorphic to an euclidean disk, ordered by inclusion. According t o Lurie [25,
Remark 5.3.2.7] we have, roughly, that
Deﬁnition 4. Let M be an n-framed manifold of dimension m and A an En-
algebra. The topological chiral homology
∫
MA is the colimit lim−→ψM with ψM :
N (Disj(M×Dn−m))→k-Mod ∞ the diagram given by the formula
(17) ψM (V1∪···∪ Vn) =
∫
V1
A⊗···⊗
∫
Vn
A∼=A⊗···⊗ A
where V1,...,V n are disjoint open sets homeomorphic to a ball (the latter equiva-
lence follows from [25, Example 5.3.2.8]).
5note that we also do not write the factor Dn−m in the notation
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 41
For our purpose, among the properties satisﬁed by
∫
MA, we will mainly need
the gluing property given in Proposition 11 below and the fact that
∫
ptA∼= A.
Indeed, the gluing property of topological chiral homology comes f rom the fact
that topological chiral homology deﬁnes an (extended) topologica l ﬁeld theory in
some appropriate monoidal ( ∞,n )-category. In view of the cobordism hypothe-
sis, the latter property can actually be used as a deﬁnition of topolo gical chiral
homology [26, Theorem 4.1.24].
Remark 12. The models for En-algebras that we are considering are given by En-
(∞-)operads as introduced in [25, Section 5.1] in the symmetric monoid al ((∞, 1)-
)category (k-Mod ∞,⊗). The category of En-algebras is symmetric monoidal ([25,
Section 5.1.5], [23, Section 1.8]) and, furthermore, there is a commut ative diagram
of operads
(18) E1
/d31 /d127 /d47/d47
j1
/d40/d40❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘ E2
/d31 /d127 /d47/d47
j2
/d35/d35❋❋❋❋❋❋❋❋ ...... /d31 /d127 /d47/d47En
/d31 /d127 /d47/d47
jn/d123/d123①①①①①①①① ...
Com
where Com is the operad of commutative (diﬀerential graded) algebras such t hat
all maps are monoidals. Note that most models for En-algebras come with such
monoidal properties and also as nested sequences (for instance, this is the case for
the models based on the Barratt-Eccles operad [4]). In particular, a commutative
diﬀerential graded algebra A is naturally an Ed-algebra for any integer d. We
write j∗
d (A) for the Ed-algebra structure on A induced by the map of operads
jd :Ed→Com whenever we want to put emphasis on this Ed-algebra structure.
Likewise, any En-algebra A is naturally an Ed algebra for d≤n. Furthermore,
we say that an A-module M has a compatible structure of Ed-algebras (d≤ n) if
the structure maps of the module structure are maps of Ed-algebras, where A is
equipped with its natural Ed-algebra induced by the diagram of operads (18).
Remark 13. With the exception of section 5.4.2, this paper only deals with a
ﬁxed En-algebra A, which, when M is framed, is an example of a locally constant
N (Disk(M ))-algebra in the sense of Lurie [25], and for which topological chiral
homology can be deﬁned, too. In particular, we will show that A also deﬁnes
canonically a locally constant factorization algebra on M in the sense of Costello
and Gwilliam [8, 9]. This also means, that ∫
MA computes the global sections of a
natural cosheaf deﬁned on the Ran space of M (see [25, Section 5.3.2]).
One of the main consequence of the interpretation [26] of topologic al chiral ho-
mology as an invariant produced by an (extended) topological ﬁeld t heory in some
appropriate monoidal (∞,n )-category is the following excision property.
Proposition 11 (Gluing for topological chiral homology) . LetM be an n-framed
manifold (possibly with corners) of dimension m, ( i.e. M×Dn−m is framed).
Assume that there is a codimension 1 submanifold (possibly with corners) of M of
the form N×Im−1−j (for some 0≤ j≤ m− 1) with a trivialization N×Im−j
of its neighborhood and that M is decomposable as M =X∪N ×I m−jY whereX,Y
are submanifolds (with corners) of M glued along N×Im−j. We endow X,Y and
N with the n-framing induced from M . Let A be an En-algebra. Then
•
∫
NA is an En−j-algebra.
42 G. GINOT, T. TRADLER, AND M. ZEINALIAN
•
∫
MA,
∫
XA, and
∫
Y A areEn−m-algebras. Further
∫
XA and
∫
Y A are also
modules over the En−j-algebra
∫
NA.
• The above module and algebra structures are compatible. Not e that this uses
the once and for all ﬁxed telescopic sequence (18) of models for En-operads.
• There is a natural equivalence of En−m-algebras∫
X
A
L
⊗∫
NA
∫
Y
A
≃
−→
∫
M
A.
Proof. This is explained in [25, Section 5.3.4] and [26, Section 4.1], also see the
proof of [11, 2]. It is also an immediate consequence of Lemma 8 below, in the case
where the manifolds are framed since, for a n-framed manifold X, an En-algebra
yields canonically an E[X]-algebra. □
Let us explain roughly, how the above Proposition can be seen in term s of
extended topological ﬁeld theory and the cobordism hypothesis. C onsider the
monoidal (∞,n )-category E≤n-Alg which is fully dualizable [26]. Each object A is
an En-algebra and deﬁnes a (unique up to equivalence) extended topological ﬁeld
theory ψA : Bordfr
n → E≤n-Alg according to [26, Theorem 2.4.6] and [26, Sec-
tion 4.1]. The objects of the ( ∞,n− 1)-categoryHomE≤n-Alg(A,B )) of morphisms
between two En-algebras A, B are (A,B )-bimodules equipped with a compatible
En−1-algebra structure (in the sense of the telescopic sequence of Ek-operads (18)).
Note that the claims made in Section 4.1 in [26] actually essentially follows from [25,
Theorem 1.2.2] and Sections 2 of [25].
The relationship between topological chiral homology with coeﬃcient s in A and
the ﬁeld theory ψA is as follows. Let Z be an n-framed manifold of dimension d
(framing of Z×Dn−d). Then Z deﬁnes a d-morphism in Bordfr
n , thus ψA(Z) is an
En−d-algebra and there is a natural equivalence
ψA(Z)∼=
∫
Z
A
see [26, Theorem 4.1.24].
Now assume M is a manifold following the assumption of Proposition 11. Thus
M×Dn−m is framed and we have a decomposition M = X∪N ×I m−j Y of M
where X,Y are submanifolds of M glued along a submanifold N× Im−1−j of
codimension 1 in M . Then N is a j-arrow inBordfr
n andX,Y arem-arrows. Hence
ψA(N )∼=
∫
NA is a j-arrow in E≤n-Alg, hence an En−j-algebra. Similarly, ψA(X)
andψA(Y ) are En−m-algebras. Since N×Im−1−j is in the boundary of X andY ,
ψA(X) and ψA(Y ) inherits ψA(N )-modules structures. Further M is equivalent to
the composition of X,Y along N in the (∞,n )-category Bordfr
n . Thus it follows
that there is a natural equivalence ψA(X)⊗L
ψA(N ) ψA(Y ) in E≤n-Alg since the
composition in the (∞,n )-category is induced by derived tensor products.
We ﬁnish this Section with the following Lemma.
Lemma 6. LetA be an En-algebra and (Mi)i∈I a family of n-framed manifolds of
dimension m. There is a natural equivalence of En−m-algebras
lim−→
F ⊂ J
F ﬁnite

⨂
f ∈F
∫
Mf
A

 ≃
−→
∫
∐
i∈IMi
A.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 43
Proof. We set M = ∐
i∈IMi and, for any ﬁnite subset F of I, we denote MF :=∐
f ∈FMf . The inclusion MF⊂M yields a canonical map N (Disj(MF×Dn−m))→
N (Disj(M×Dn−m)). Since an object in N (Disj(M×Dn−m)) is a ﬁnite disjoint
union of connected open sets in M , every object in N (Disj(M×Dn−m)) lies in some
N (Disj(MF×Dn−m)) for a ﬁnite F . Hence we have an equivalence N (Disj(M×
Dn−m))∼= lim−→
F ﬁnite
N (Disj(MF×Dn−m)) of ∞-categories and, by Deﬁnition 4, an
natural equivalence
∫
M
A∼= lim−→ψM∼= lim−→
F ﬁnite
ψMF
∼= lim−→
F ﬁnite
∫
MF
A.
Now the lemma follows from [25, Theorem 5.3.3.1] which gives a natural e quivalence( ⨂
f ∈F
∫
Mf
A
) ≃
→
∫
MF
A for all ﬁnite F . □
