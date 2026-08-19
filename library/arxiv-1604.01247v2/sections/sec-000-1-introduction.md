---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-9
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3 generations, we develop an"
---
2 Unimodularity of SU (3) and the quark-lepton symmetry 6
2.1 SU (3)-spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 SU (3)-algebra version of octonion algebra . . . . . . . . . . . 7
2.3 The quark-lepton symmetry . . . . . . . . . . . . . . . . . . . 9
2.4 Gauge theoretical aspect . . . . . . . . . . . . . . . . . . . . . 9
3 The 3-generations, triality and the exceptional ﬁnite qua n-
tum space 11
3.1 the 3-generations . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 Finite quantum spaces . . . . . . . . . . . . . . . . . . . . . . 12
3.3 The exceptional ﬁnite quantum space . . . . . . . . . . . . . . 15
3.4 Exceptional almost classical quantum spacetime . . . . . . . . 16
4 Modules and fundamental fermions 18
4.1 Modules over Jordan algebras . . . . . . . . . . . . . . . . . . 18
4.2 J 8
3 -modules and SU (3) × SU (3)-action . . . . . . . . . . . . . 20
4.3 Modules for the two families by generation . . . . . . . . . . . 21
4.4 Problem of the U(1) × SU (2)-symmetry . . . . . . . . . . . . 22
4.5 Charge conjugation . . . . . . . . . . . . . . . . . . . . . . . . 23
5 Diﬀerential calculus over Jordan algebras 24
5.1 First order diﬀerential calculi . . . . . . . . . . . . . . . . . . 24
5.2 First order diﬀerential calculi over J 8
3 . . . . . . . . . . . . . . 25
5.3 Diﬀerential graded Jordan algebras . . . . . . . . . . . . . . . 26
5.4 Higher order derivation-based diﬀerential calculi . . . . . . . . 27
5.5 Diﬀerential calculi as A∞-algebras . . . . . . . . . . . . . . . . 28
6 Connections on Jordan modules 30
6.1 Derivation-based connections. First deﬁnition . . . . . . . . . 30
6.2 Derivation-based connections. Second deﬁnition . . . . . . . . 30
6.3 General connections . . . . . . . . . . . . . . . . . . . . . . . . 32
7 Tentative conclusion 32
2
1 Introduction
It is well known that the Standard Model of particles is very succes sful but
contains several inputs which ought to have explainations at a fund amental
level. Some of these inputs like the existence of the Higgs particles, w hich
seem to have recently acquired experimental conﬁmations, appea r naturally
for instance in the (almost commutative) noncommutative geometr ic formu-
lations [15], [16], [13], [11], [8], [9] or in the superconnection formulations
[37]. Some other structural inputs come almost directly from the ex perimen-
tal observation. For instance the quark-lepton symmetry or the existence of
3 generations belong to these latter inputs and it is one of our aims he re to
connect these 2 inputs and to suggest some theoretical explanat ions for these
facts.
By the quark-lepton symmetry, we mean the fact that to each qua rk cor-
responds one lepton and conversely. For instance to the quark u corresponds
the electronic neutrino νe, to the quark d corresponds the electron e, etc..
On the theoretical side, it is worth noticing here that the cancellatio n of
anomalies is a very strong argument for the quark-lepton symmetr y.
The classical quark ﬁeld is a spinor ﬁeld with values in a complex 3-
dimensional space acted by the color group SU (3). Thus, forgetting the
spin etc., at each point of spacetime, the internal space E for a quark is a
complex 3-dimensional Hilbert space (since SU (3) ⊂ U(3)) which is endowed
with a complex volume that is with an antisymmetric C-trilinear form (since
elements of SU (3) are of determinant 1). By using the Hilbertian scalar
product of E, one can transform the volume into an antilinear antisymmetric
product /vartimeson E. Thus E is equipped with a product
/vartimes: E × E → E
and the Hilbertian scalar product
⟨, ⟩ : E × E → C
and SU (3) is the group of the C-linear transformations which preserve these
structures. It is then natural to combine these products into an SU (3)-
invariant product on the Hilbertian direct sum A = C ⊕ E such that 1 ∈
C ⊂ A is a unit denoted by 1 l for the product of A and such that the norm of
3
the product of 2 elements of A is the product of the norms of these 2 elements.
The product on A is then not C-bilinear but is only real bilinear and the cor-
responding real algebra is isomorphic to the algebra of octonions [4]. The
group SU (3) identiﬁes then with the group of C-linear isomorphisms of A
(≃ C4) which preserve the product. Under this action the invariant subs pace
E of A = C1 l⊕ E corresponds to the fundamental representation of SU (3)
while its orthogonal corresponds to the trivial representation. T hinking of
E as the internal quark space, it is then natural to identify the comp onent
C1 l of A as the trivial internal space of the corresponding lepton. In this
way one connects the quark-lepton symmetry to the S of SU (3), i.e. to the
unimodularity condition.
It is worth noticing here that this interpretation of the quark-lept on sym-
metry leads directly to the original interpretation given in [22] of the color
group SU (3) as a subgroup of the automorphism group G2 of the octonion al-
gebra. Indeed it is classical (see e.g. in [35], [4], [41]) that the automor phism
group of the real algebra O of octonions is the ﬁrst exceptional group G2
and that SU (3) identiﬁes with the subgroup of G2 of automorphisms which
preserve a given imaginary unit of O. This is of course directly connected to
the above construction which is explained in details in Section 2; the co rre-
sponding imaginary unit of O being then the imaginary unit i of C.
Since SU (3) is a gauge group, that is the structure group of a bundle over
spacetime, this construction means that at each point of spacetim e one has
a complex 4-dimensional vector space A = C ⊕ E which is a real algebra (for
the underlying structure of real 8-dimensional vector space) iso morphic to the
octonion algebra, ( SU (3) being the automorphism group of this structure).
In other words associated to the SU (3)-bundle we have a complex vector
bundle A of rank 4 which is also a bundle in octonion algebras. A natural
question is what is the role of this local algebra structure if it is releva nt ?
Let us observe that there are 3 generations and that the principle of trial-
ity combined with octonions leads directly to the exceptional Jordan algebra
J 8
3 = H3(O) of octonionic hermitian 3 by 3 matrices, see e.g. in [1]. This
algebra was introduced in [28] where it was pointed out that it is a quan tum
version of an algebra of “real functions” on a “ﬁnite quantum spac e” (see
also [23]) as any formally real (Euclidean) ﬁnite-dimensional Jordan a lgebra.
4
The above discussion suggests to put over each spacetime point a ﬁ nite
quantum space corresponding to the exceptional Jordan algebra J 8
3 . As be-
fore this corresponds to a bundle in algebras J 8
3 which is associated to the
above (color) SU (3)-bundle. In other words this suggests to replace the real
algebra C ∞(M) of smooth functions on spacetime M by the real Jordan
algebra J 8
3 (M) of smooth sections of this bundle in algebras J 8
3 . Since in
this paper we assume that M is the usual Minkowski space R4, this algebra
J 8
3 (M) is isomorphic to the algebra C ∞(M, J 8
3 ) = J 8
3 ⊗ C ∞(M) of smooth
J 8
3 -valued functions on M. That is, we take J 8
3 (M) = J 8
3 ⊗ C ∞(M) which
is interpreted as the “algebra of real functions” on the quantum s pace which
is the product of the “ﬁnite quantum space” corresponding to J 8
3 with the
spacetime M. Since the “quantum part” is “ﬁnite”, we refer to such a quan-
tum space as an “almost classical quantum space”. Classical matte r ﬁelds are
then elements of J 8
3 (M)-modules and gluon ﬁelds are part of connections on
these modules. However none of these two items, modules and conn ections,
are straightforward for Jordan algebras.
There is a notion of (bi)module [38], [27] for Jordan algebras (see also
in [14]) which will be used here. It seems that no diﬀerential calculus ha s
been developed so far for Jordan algebras, a step which is certainly necessary
to speak of connections. We deﬁne such a diﬀerential calculus over Jordan
algebras and describe several examples and their properties. A pa rticular
attention is devoted to the case of the exceptional Jordan algebr a J 8
3 . An
appropriate associated notion of connection on Jordan modules is in troduced.
It is our aim to develop in the furure these notions in the present con text
in order to get a natural description of the ﬁeld content of the Sta ndard
Model of particles and of some possible generalizations.
The present approach is close in spirit to the approach of noncommu ta-
tive geometry. However here it is not a ﬁnite noncommutative space cor-
responding to a ﬁnite-dimensional associative algebra but a ﬁnite qu antum
space corresponding to a ﬁnite-dimensional Euclidean Jordan algeb ra which
is added to spacetime. Furthermore since the exceptional Albert a lgebra is
involved, one cannot use directly the technics of noncommutative g eometry
(i.e. of associative algebra) and some care must be taken to handle s uch
theory. Nevertheless as in the noncommutative geometric approa ches, it is
expected that the apparition of the Higgs ﬁelds is a consequence of the quan-
5
tum nature of the almost classical spacetime (i.e. components of co nnections
in the quantum directions).
Finally let us recall that occurrence in physics of octonions and exce p-
tional structures has a long history, (see e.g. [28],[21],[22], [23], [24], [12 ],
[36]). They appear very naturally in extensions of the Standard Mod el. More
recently, in [7], [19] and [20], an interesting tentative approach to in corporate
nonassociativity in the framework of the spectral action principle h as been
carried over.
Our notations are standard and we use Einstein convention of summ ation
over repeated up-down indices in the formulas.
2 Unimodularity of SU (3) and the quark-lepton
symmetry
2.1 SU (3)-spaces
In the following, an SU (3)-space will be a complex 3-dimensional Hilbert
space E equipped with an antisymmetric complex 3-linear form v : Λ 3E → C
of norm ‖ v ‖= 1, that is such that one has
|v(e1, e 2, e 3)| = 1
for any orthonormal basis ( ek) of E.
An SU (3)-basis of E will be an orthonormal basis ( e1, e 2, e 3) of E such
that one has v(e1, e 2, e 3) = 1. Given such an SU (3)-basis ( e1, e 2, e 3), one de-
ﬁnes a bijection of the group SU (3) onto the set of all SU (3)-basis
g ↦→(e(g)
1 , e (g)
2 , e (g)
3 ) by setting
e(g)
k = eℓgℓ
k (2.1)
for k ∈ {1, 2, 3} where gℓ
k are the matrix elements of g ∈ SU (3) (in the fun-
damental representation).
Given an SU (3)-basis (e1, e 2, e 3) of E one deﬁnes the components Z k ∈ C
of a vector Z ∈ E by
Z = ekZ k
6
and E can then be identiﬁed with C3 with Hilbertian scalar product given
by
⟨Z1, Z 2⟩ =
3∑
k=1
¯Z k
1 Z k
2 (2.2)
and v given by
v(Z1, Z 2, Z 3) = εkℓmZ k
1 Z ℓ
2Z m
3 (2.3)
for Z1, Z 2, Z 3 ∈ E. An element Z ∈ E is identiﬁed with the column [ Z k] ∈ C3
of its components and a change of SU (3)-basis corresponds to the left action
of an SU (3)-matrix on [Z k], (which leaves invariant the forms (2.2) and (2.3)).
2.2 SU (3)-algebra version of octonion algebra
One can combine the 3-linear form v on E with the Hilbertian scalar product
to deﬁne an antibilinear antisymmetric product ( Z1, Z 2) ↦→Z1 /vartimesZ2 on E by
v(Z1, Z 2, Z 3) = ⟨Z1 /vartimesZ2, Z 3⟩ (2.4)
for any Z1, Z 2, Z 3 ∈ E. In the SU (3)-basis ( e1, e 2, e 3) and the corresponding
identiﬁcation of E with C3 this product reads
(Z1 /vartimesZ2)k = εkℓm ¯Z ℓ
1 ¯Z m
2 (2.5)
for k ∈ { 1, 2, 3}. Notice that this product on E is nonassociative and is
invariant by the action of SU (3). Thus one has a product
/vartimes: E × E → E, (Z, Z ′) ↦→Z /vartimesZ ′
and the scalar product
⟨, ⟩ : E × E → C, (Z, Z ′) ↦→ ⟨Z, Z ′⟩
which are invariant by the action of SU (3) on E. This representation of
SU (3) is the fundamental representation and SU (3) is exactly the subgroup
of the complex linear group of E which preserves these two products; C being
equipped with the trivial representation of SU (3)
(g, z ) ↦→gz = z
7
for g ∈ SU (3), z ∈ C. It is therefore natural to combine these products into
an SU (3)-invariant product
((z, Z ), (z′, Z ′)) ↦→(z, Z )(z′, Z ′)
on C ⊕ E in such a way that
(0, Z )(0, Z ′) = ( α ⟨Z, Z ′⟩, βZ /vartimesZ ′) (2.6)
for some α, β ∈ C and that 1 l = (1, 0) is a unit, i.e. that one has in particular
(1, 0)(0, Z ) = (0 , Z )(1, 0) = (0 , Z )
for any Z ∈ E with of course (1 , 0)(1, 0) = (1 , 0) and more generally
(z, 0)(z′, 0) = ( zz ′, 0)
for z, z ′ ∈ C.
If C ⊕ E is endowed with its natural structure of 4-dimensional Hilbert
space (Hilbertian direct sum), one has
‖ (0, Z )(0, Z ′) ‖2= (|α |2 − |β |2)|⟨Z, Z ′⟩|2 + |β |2 ‖ Z ‖2‖ Z ′ ‖2
so that one has
‖ (0, Z )(0, Z ′) ‖2=‖ (0, Z ) ‖2‖ (0, Z ′) ‖2
by chosing
|α |2 = |β |2 = 1 (2.7)
as normalization. One has also of course
‖ (z, 0)(z′, 0) ‖2=‖ (z, 0) ‖2‖ (z′, 0) ‖2
so it is natural to require
‖ (z, Z )(z′, Z ′) ‖2=‖ (z, Z ) ‖2‖ (z′, Z ′) ‖2
with ‖ (z, Z ) ‖2= |z|2+ ‖ Z ‖2 and the real bilinearity of the product.
A solution is given by
(z, Z )(z′, Z ′) = ( zz ′ − ⟨Z, Z ′⟩, ¯zZ ′ + z′Z + iZ /vartimesZ ′) (2.8)
8
This product is probably essentially unique up to irrelevant normalizat ions.
Setting
(z, Z ) = (¯z, −Z) (2.9)
one obtains in particular
(z, Z )(z, Z ) = ( z, Z )(z, Z ) = ( |z|2+ ‖ Z ‖2)(1, 0)
i.e.
(z, Z )(z, Z ) = ( z, Z )(z, Z ) =‖ (z, Z ) ‖2 1 l (2.10)
which implies that as a real 8-dimensional algebra for the product (2 .8),
A = C1 l⊕ E is a normed division algebra which is (necessarily) isomorphic to
the algebra O of octonions. The group SU (3) is the group of automorphisms
of this algebra which preserves the structure of 4-dimensional co mplex vector
space of C ⊕ E or, equivalently, the group of all complex automorphisms of
C ⊕ E which preserve the product given by (2.8).
