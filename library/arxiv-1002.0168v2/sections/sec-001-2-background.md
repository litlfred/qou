---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder"
section_id: sec-001-2-background
section_title: "Background"
section_number: 2
pages: 3-5
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
doc_brief: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder — Etingof, Nikshych and Ostrik ask in [ 7,§2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
2.1 Fusion categories and ﬁelds of deﬁnition
Let k be a ﬁeld. An object in an additive category is called simple if it has no non-
trivial proper subobjects. An additive category is called semisimple if every object
is a direct sum of simple objects (and in particular, every indecomposable object is
simple). A category is called idempotent complete (or Karoubian or psuedoabelian)
if every idempotent has an image (that is, a subobject which the idempotent factors
3
through). It is easy to see that any idempotent complete additive semisimple
category is abelian. A split semisimple category overk is a semisimple category over
k such that every simple object X is split simple, that is End (X) =k. If k is an
algebraically closed ﬁeld, then any semisimple category over k is automatically split.
A fusion category over k is a k-linear abelian semisimple rigid monoidal category
with ﬁnitely many isomorphism classes of simple objects. A split fusion category
over k is a fusion category over k which is split semisimple. (Warning, some authors
require that all fusion categories be split.)
Example 1 Consider R[Z/3Z]-mod. This is a fusion category over R with two
objects: the trivial module and the 2-dimensional representation (where the generator
acts by 120-degree rotation). It is not split fusion because the endomorphism algebra
of the 2-dimensional representation is C.
Suppose that k <K is an inclusion of ﬁelds and that CK is a semisimple abelian
category over K possibly with some ﬁxed additional structures (e.g. it’s a monoidal
rigid category or a braided category). A rational form ofC over k is a semisimple
abelian category Ck over k (again with the same structure) together with an equiva-
lence between the idempotent completion of Ck⊗kK is andCK (this equivalence
should preserve the additional structure). A complete rational form ofC over k is a
rational formCk such thatCk⊗kK∼=CK , in other words, a complete rational form
is a rational form such that Ck⊗kK is already idempotent complete.
There are several reasons for considering incomplete rational forms. First, many
constructions do not preserve completeness. For example, the category of G-graded
rational vector spaces is a complete rational form of the category of G-graded
complex vector spaces, while the center of the former category is only an incomplete
rational form of the center of the latter. Second, any fusion category is the category
of representations of a weak Hopf algebra A [19, 8, 9, 23] and if that weak Hopf
algebra has an rational form Ak then Ak−mod is, in general, an incomplete rational
form for A− mod. Third, the notion of incomplete rational form arises naturally
in the context of planar algebras. Finally, it can be convenient to show that Ck is
a complete rational form by ﬁrst showing that it is a rational form (which is often
easy for the above reasons) and then explicitly checking completeness.
Notice that if CK is a split fusion category over K andCk is a rational form over
k<K thenCk is complete if and only if Ck is a split fusion category.
IfCK is a split fusion category then there is a more concrete description of having a
complete rational form (pointed out to us by Victor Ostrik). A split fusion category
CK can be completely described by a collection of vector spaces Hom (Va⊗Vb,Vc)
over K , and associativity maps between the appropriate tensor products of these
spaces. The fusion category CK has a complete rational form over k if and only if
there exists a basis for each of these vector spaces such that all the associativity
maps are given by matrices with entries in k.
Example 2 CC = C[Z/3Z]-mod has a complete rational form over Q. To see this
notice that Z/3Z is abelian, and hence C[Z/3Z]-mod is equivalent to the category
of Z/3Z-graded complex vector spaces. We can take CQ to be the category of
Z/3Z-graded rational vector spaces.
4
Example 3 Consider G a ﬁnite group. Notice that all of the representations of a
group G are deﬁned over a ﬁeldk if and only if k[G]-mod is split. All representations
of any ﬁnite groupG are deﬁned over Q(ζn), wheren is the exponent ofG. Therefore,
C[G]-mod has a complete rational form over a cyclotomic ﬁeld. On the other hand
as Example 2 shows, it is possible for C[G]-mod to be deﬁned over a smaller ﬁeld
than the minimal ﬁeld of deﬁnition for all its representations.
IfC is a k-linear category, and k <K is an inclusion of ﬁelds and the idempotent
additive completion ofC⊗kK is semisimple, thenC is semisimple. This follows from
the characterization of semisimplicity in terms of semisimplicity of the endomorphism
algebras, given in the next Lemma, and the equivalence of semisimplicity of artinian
rings with the absence of nilpotent ideals [ 12, p. 203]. The same is not true for split
semisimplicity as R[Z/3Z]-mod is not split semisimple while C[Z/3Z]-mod is. The
converse is also false at least when k<K is inseparable [18, Question 5.1].
Lemma 2.1 A k-linear additive idempotent complete category C is semisimple if
and only if the endomorphism algebra of every object is a semisimple algebra. The
simple objects are exactly those objects whose endomorphism algebras are division
rings.
Proof By Schur’s lemma, if C is semisimple then the endomorphism algebra of an
object is a sum of matrix algebras over division rings, which is a semisimple algebra.
In the other direction, suppose that C has all endomorphism algebras semisimple.
Since the category is idempotent complete, one may use the projections in the
endomorphism algebras to decompose any object into a direct sum of objects whose
endomorphism algebras are division rings. If X and Y are non-isomorphic objects
whose endomorphism algebras are division rings, the semisimplicity of End (X⊕Y )
shows that there are no nonzero maps between X and Y . Hence all objects
whose endomorphism algebras are division rings are simple and every object is
semisimple.
