---
doc_id: arxiv-2607.03827v1
doc_title: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
doc_brief: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS — The theory of affine cellular algebrasAis extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between classical"
---
2. Determinants for affine Cellular Algebras 5
3. Homomorphisms between affine cell ideals. 7
4. The asymptotic algebra of an affine cellular algebra 13
5. Properties of the embedding into the asymptotic algebra 17
6. Examples and methods 22
6.1. An explicit example 22
6.2. Extended affine Hecke algebra of typeA26
6.3. Gram determinants and Jucys Murphy elements 29
References 31
1.Introduction
The aim of this article is to clarify new and sometimes unexpected structures of affine cellular algebras
and properties of embeddings into asymptotic algebras, to illustrate these structures and properties by
examples and to put them into the context of algebraic Lie theory. This continues and builds upon [18]
and [5].
Plenty of finite dimensional algebras arising in algebraic Lie theory have been shown to be cellular
algebras. For instance, group algebras of symmetric groups and their Hecke algebras as well as classical
Date: July 7, 2026.
1
arXiv:2607.03827v1  [math.RT]  4 Jul 2026
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 2
Schur algebras, blocks of the Bernstein-Gelfand-Gelfand categoryOof semisimple complex Lie algebras,
Temperley Lieb algebras and Brauer algebras are widely studied examples of cellular algebras, as defined
by Graham and Lehrer [7]. The definition in [7] is using combinatorial properties of a cellular basis
that allows to define and investigate cell modules, which generalise Specht modules, Weyl modules and
Verma modules. A cellular structure allows to parametrise simple modules in terms of a finite partially
ordered set, and to describe them in terms of linear algebra over a field that has been fixed from the
beginning.
Subsequently, an equivalent definition of cellularity has been given [16] in terms of a finite chain of
two-sided ideals – indexed by the same finite partially ordered set – with subquotients being direct sums
of cell modules. This led to further ring theoretical and homological properties. The easiest cellular
algebras are split semisimple, more general quasi-hereditary ones still have finite global dimension and
going beyond these, one arrives at infinite global dimension [17]. In the semisimple or quasi-hereditary
case, subquotients of the cell chain all are idempotent ideals, while in the non-quasi-hereditary situation
some subquotients necessarily have square zero.
To extend cellularity to not necessarily finite dimensional algebras, in [18] affine cellular algebras have
been introduced, and then plenty of algebras have been shown to be affine cellular, for instance affine
Hecke algebras, KLR algebras, affine Schur algebras and affine Temperley-Lieb algebras. Here, there is
a common affine ground ring and the cell chain still is finite, indexed by a finite partially ordered set as
before. However, each subquotient comes with its own affine commutative ring and the subquotient is,
as a non-unital algebra, a generalised matrix ring (introduced by Brown [4]) over this affine commutative
algebra, with matrix multiplication deformed by adding a fixed matrix as an intermediate third factor
into ordinary matrix multiplication; this matrix is called swich matrix. Simple modules still are finite
dimensional (now over quotients of the affine rings modulo maximal ideals) and they are classified by
a spectrum, depending on the entries of the swich matrices. Finite products of matrix rings over affine
commutative rings can be seen as the analogues of semisimple cellular algebras, and subquotients of
cell ideals that are idempotent produce an analogue of a quasi-hereditary situation; this motivated
Kleshchev to define graded affine quasi-hereditary algebras [12]. In the general situation there are many
other cases than idempotent subquotients or those squaring to zero. As we will show, the situation is
controlled by determinants of swich matrices (not) being a zero-divisor in the affine commutative rings
of the subquotients.
Our main focus is on a new ingredient of affine cell theory: Given an affine cellular algebra A,
there exists [18] an algebra called asymptotic algebraˆA, that is a direct sum of matrix algebras over
the affine rings associated with the subquotients in the cell chain of A, and by [18] there is an algebra
homomorphismfromAto ˆA. ThesubquotientsofthecellchainofAcoincideassetswiththecomponents
of ˆA. If A is finite dimensional cellular in the sense of [7], the homomorphism can be injective only
when A is semisimple and coincides withˆA, which has the same dimension. In a different way, Lusztig
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 3
had defined in [19] asymptotic algebras for Hecke algebras of finite or affine type over ground rings
that are not fields, but for instance Laurent polynomial rings over the integers. In Lusztig’s work and
its applications, asymptotic algebras and embeddings of Hecke algebras into their asymptotic algebras
turned out to be very useful in various respects. The general theory of asymptotic algebras of affine
cellular algebras has been started in [18] and continued in [5]. The current article aims at extending
and deepening this theory, at clarifying the situation in various applications and at identifying Lusztig’s
asymptotic ˆAwith those defined in [18] in relevant situations.
The main results of the theory being developed can be stated informally as follows: LetAbe an
affine cellular algebra as defined in [18], with a fixed affine cell chain0 =J0⊂J 1⊂J 2⊂...J n =A
and subquotientsJ j/Jj−1 being generalised matrix algebras, where the multiplication inJj/Jj−1 is
deformed by adding a fixed middle factorψ(j) called swich matrix. Let ˆAbe the asymptotic algebra of
Aandι:A→ ˆA.
Finite dimensional cellular algebras are either quasi-hereditary (the desirable case with the best
properties), equivalently of finite global dimension (see [17]), or not quasi-hereditary and equivalently
of infinite global dimension. Being quasi-hereditary means that all swich matrices are invertible, which
meanstheirdeterminantsareinvertible. Otherwise, atleastsomeswichmatriceshavezerodeterminants.
As we will see, for affine cellular algebras, the desirable case is that the swich matrices are not zero-
divisors.
Under this frequently satisfied assumption, the connection between the affine cellular algebraAand
its asymptotic algebra ˆAis particularly close, as shown by Theorems A, B and C.
Theorem A(special case of Theorem 10).Suppose that no determinant of a swich matrixψ (j) (for
j= 1,...,n) is a zero-divisor. Then there is an embeddingθ:A→ ˆA, which is explicitly given by
the isomorphisms between the endomorphism rings of the subquotients(Jj/Jj−1)A and the generalised
matrix rings.
Theorem B(Theorem 15).Suppose that no determinant of a swich matrixψ (j) (forj= 1,...,n)
is a zero-divisor and all cell subquotients are idempotent ideals in the quotient algebras ofAmodulo
lower affine cell ideals. Then the embeddingθ:A→ ˆAinduces a fully faithful functor from torsionless
ˆA-modules to A-modules.
Usingθyields a K-theoretic consequence.
Theorem C(Theorem 20).Suppose that no determinant of a swich matrixψ (j) (forj= 1,...,n) is
a zero-divisor and all cell subquotients are idempotent ideals in the quotient algebras ofAmodulo lower
affine cell ideals. Then the embeddingθ:A→ ˆAis a weakly spectrum preserving morphism in the sense
of Baum and Nistor[2].
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 4
As a consequence, Baum and Nistor’s results allow in particular to identify periodic cyclic homology
of the two algebras.
The cell modules of the affine cellular algebraAare direct summands of the regularˆA-module. This
is related with another feature of the asymptotic algebra, and also of smaller analogues ofˆA.
Theorem D(Theorem 12).Suppose that no determinant of a swich matrixψ(j) (forj= 1,...,n) is
a zero-divisor and all cell subquotients are idempotent ideals in the quotient algebras ofAmodulo lower
affine cell ideals.
(a) The asymptotic algebra ˆAofAcan be constructed as centraliser algebra of endomorphism rings
of direct sums of a full set of cell modules ofA. In particular, there is a double centraliser property
betweenAand its asymptotic algebra ˆA.
(b) The same properties are satisfied for all members of a family of algebras also includingˆAand
constructed as centraliser algebras of endomorphism rings of certain direct sums of cell modules ofA.
This construction of ˆAis quite different from the definition of asymptotic algebras in [18].
In the finite dimensional cellular case, homomorphisms between cell modules rarely are injective,
there are no non-zero injective endomorphisms apart from automorphisms, and if there are no non-
zero homomorphisms between different cell modules at all, the cellular algebra must be semisimple. In
stark contrast to that, for KLR algebras of Dynkin type (shown to be graded affine quasi-hereditary
by Kleshchev, Loubert and Miemietz [13]), Kleshchev and Steinberg [15] have shown that non-zero
endomorphisms of cell modules exist and always are injective, but there are no non-zero homomorphisms
between different cell modules. It turns out that from the affine cellular perspective this is not at all
surprising.
Theorem E(special cases of Theorem 5 and Corollary 6).Suppose that subquotients in the affine cell
chain are idempotent, their affine commutative rings are integral domains and the determinants of the
swich matrices are non-zero. Then non-zero endomorphisms of cell modules always are injective and
there are no non-zero homomorphisms between non-isomorphic cell modules.
In the final section of this article, we will be turning to Lie theoretic examples, illustrating the
situations occurring in the new theory and also identifying our asymptotic algebras and the embedding
θin various situations, including classical and affine Hecke algebras studied by Lusztig [19], (see also
the book [6]). We also give a worked out small example and describe in detail the situation of extended
affine Hecke algebras of typeA, which had been shown to be affine cellular in [18]. Moreover we refer to
various useful methods to verify the assumptions (in particular on the determinants of swich matrices)
of our results above, for instance a method developed by Mathas in [20] and using the existence of Jucys-
Murphy elements, which can be used to compute Gram determinants (in our situation aka determinants
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 5
of swich matrices), as well asAandˆAbecoming isomorphic after extension of scalars (sometimes known
as Lusztig’s isomorphism), and using properties of Kazhdan-Lusztig bases.
