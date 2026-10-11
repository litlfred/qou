---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-001-iii-schur-weyl-duality-and-quotients-of-the-heck
section_title: "SCHUR-WEYL DUALITY AND QUOTIENTS OF THE HECKE ALGEBRA"
section_number: III
pages: 29-42
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
---
IlLI.
Schur-Weyl Duality
We review the classical notion of Schur-Weyl duality between the general linear groups
and the symmetric group.
Then, we generalize this in two directions, giving a duality theorem
between the quantum group associated to the Lie superalgebra g[(mln) and the Iwahori-Hecke
algebra rid.
II!. 1. 1.
Classical Schur- vVeyl Duality
Fix the ground field C
Let Par(d) denote the set of all integer partitions of d.
To the
partition A = (AI, A2,"') with Al 2" A2 2" ... 2" 0, associate its Young diagram, that is, the left-
justified diagram with Al boxes on the first row, A2 boxes on the second row, etc. Let S(A) denote
the irreducible CSd-module, called the Specht module associated to A E Par(d).
Let A+(n, d) denote the set of all A E PaT (d) whose Young diagram has d boxes in at most
n rows.
The irreducible (polynomial) highest weight GL(n)-module of highest weight A will be
denoted V(A), where we fix the standard choice of maximal torus and Borel subalgebra consisting
of diagonal matrices and upper triangular matrices, respectively.
Let (["
= V(l, 0, ... ,0) denote the natural n-dimensional vector representation of the
group GL(n), and consider the tensor space
Cn 0 ... 0Cn
with d tensor factors. This is a left GL(n)-module via the diagonal action:
(IILl )
(III.2)
22
Also, the symmetric group acts on the right by permuting factors:
(III.3)
Theorem 111.1.1. Consider the representations of GL(n) and Sd on tensor space:
(IIIA)
1. The actions of GL(n) and Sd on cn 0···0 cn commute.
2. As a (GL(n), Sd) -bimodule, tensor space decomposes into simples
Cn 0 ... 0 Cn ~
EB
V(A) 0 S(A).
).,EA+ (n,d)
(IlL5)
3. The image of each group in End(Cn 0 ... 0 cn) generates the full centralizer algebra of the
other group.
For d ::::: n, the homomorphism trd
: CSd
----t End(Cn 0 ... 0 C n ) is injective.
In the
sequel, we will be concerned with the other extreme, where trd is far from injective, so 7rd(CSd)
is a proper quotient of the group algebra.
But, first we must generalize Schur-Weyl duality is
several ways. In ([5]), Berele and Regev use the Lie superalgebra g[(mln) and its standard (mln)-
dimensional module to establish an analogous duality theorem for (U(g[(mln)), CSd ), where the
symmetric group acts by signed permutations. The indexing set for the decomposition generalizing
(III.5) is the set A+(mln,d) consisting of all Young diagrams that are (mln)-hooks: Ai::::: n for all
i > ·ITt. This is further generalized by Mitsuhashi ([32]) to a duality statement about the quantum
deformation Uv(g[(mln)) ofU(g[(mln)) and the Iwahori-Hecke algebra 7-{d. However, we shall only
consider the cases (min) = (210) in connection to the Jones polynomial and (Ill) in connection to
the Alexander polynomial.
111.2.
Representations of the Iwahori-Hecke Algebra
We summarize some important facts about the Iwahori-Hecke algebra 7-{d and its represen-
tations, most of which are modified versions of well know facts about the symmetric group Sd and
its representations (see, e.g. [12]). Recall the standard generators HI, ... , H d-l for 7-{d, analogous
23
to the generators S1,.'" Sd-1 of Sd, where Si is the elementary transposition (i i + 1).
1. The standard basis for Hd consists of the elements H w , where w E Sd.
In terms of the
standard generators,
(IlL6)
where w = Si, ... Sin> is any reduced expression in Sd. The non-negative integer m is called
the length of wand denoted €(w).
2. Multiplication in this basis is
(III.7)
3. There is an irreducible module S(A) of Hd corresponding to each integer partition A. These
are pairwise non-isomorphic, and any finite-dimensional representation decomposes as a di-
rect sum of thse simple modules. An explicit construction of these modules using Young's
semi-normal form is given in Chapter IV.
4. Hd is semi-simple. Hence, we have the isomorphisms of algebras
Hd ~ II End S(A) ~ II Md)o,'
A
A
(III.8)
where Md)o, is the full matrix algebra of degree dA = dim S(A). In fact, generically, we have
the isomorphism Hd ~ C(V)Sd'
5. The branching rules for Hd are same as for Sd. Specifically, restriction of a simple Hd module
S(A) to Hd-1 decomposes into a multiplicity-free sum of simple modules S(p.), where p. is
obtained from A by removing a corner box.
Corresponding to each indecomposable block in the Wedderburn decomposition (IlL8),
there is a primitive, central idempotent e(A) E Hd, which can be constructed explicitly, as follows.
This is analogous to the Young symmetrizer in Sd and is originally due to Gyoja ([18]).
Corresponding to the partition A = (A1, ... ,Ar ), let SA
~ SAl
X '"
X SA r be the row
stabilizer of the Young diagram.
Let AT denote the transpose partition.
Define the elements
24
Q>., b>. E 'lid (the symmetrizeI' and the skew-symmetrizer, respectively) by
a>. = L
v€(w) H w
loES>.
and
b>. = L
(_v)-€(w) H w
WES>,T
(Ill,9)
Define the permutation w>. as follows,
Fill the boxes of the Young diagram for ,\ with
the numbers 1, ... , d across rows from left to right and top to bottom. Now, form the sequence
('11)(1), ... ,w(d)) by reading the numbers down the columns from left to right. This sequence is
the one-line notation for w>..
Theorem III.2.1 (Compare [13]). The element c>. E'lid defined by
(III.10)
satisfies c>.c>. = h>.c>. for some h>. E CC(v)x. Moreover, for any two partitions A 1= il, c>,c/1 = O.
Hence, the collection of e(A)
=
h-;lC>. for all partitions of d are mutually orthogonal,
primitive, central idempotents that sum to one, which explicitly realize the decomposition in
(III.8) .
III.3.
The Quantum Group Uv (s((2))
III. 3.1.
Definitions and Conventions
Let U be the quantum group Uv (s((2)) (see [21] or [20]). This is the unital, associative
CC(v)-algehra generated by E, F, K, subject to the relations
KF = v- 2FK,
K -K- 1
EF-FE=
1
.
v -v-
The representation theory of U is analogous to that of s((2). Specifically, certain finite-
dimensional simple modules for U are highest weight modules (the ones so-called type 1), in the
following multiplicative sense. In aU-module VV, a vector w has weight A if K.w = v>'w. For each
A E Z>o, there is a unique finite-dimensional simple U-module L(A) of highest weight A.
25
It is a standard fact that U is a Hopf algebra with comultiplication 6, counit c, and
antipode S given by
6(E) = E 129 K- 1 + 1 129 E,
6 (F) = F 129 1 + K 129 F,
c(K) = 1,
c(E) = c(F) = O.
S(K) =K- 1,
S(E) = -EK,
S(F) = _K- 1F.
Let W denote the natural module for U, represented in the basis {WI, W2} by the matrices
(III.ll)
Let P : U ----> End(W) be the corresponding representation. Using the comultiplication in
the Hopf algebra, it extends to a representation Pd :U ----> End(W®d). Set 6(l) = 6 and for i > 1,
6 (i) = (6129 Id®i-l) 06(i-I). Then, Pd = p®d 06(d-l), producing the formulae:
d
Pd(E) = L Id®i-l Q9p(E) 129 p(K- 1)®d-i
i=1
d
Pd(F) = L p(K)®'-1 129 p(F) 129 Id®d-,.
i=l
vVe make W®d into a right 7-{d-rnodule by defining a homomorphism 7fd : 7-{d ----> End(W®d)OP,
as follows. First, define the right operator H on W 129 W by:
ifi=j,
(III.12)
Wj 129 Wi
if i > j.
26
Now, set
(III.13)
III. 3. 2.
Schur- Weyl Duality for Uv (5[(2)) and {-{d
The following theorem is well-known.
Theorem III.3.1. Consider the maps
Pd
(
)
ITd
U -----+ End W ® ... ® W ~ {-{d.
1.
The actions of U and {-{d on W ® ... ® W commute.
2. As a (U, (-{d) -bimodule, tensor space decomposes into simples
W ® .. , ® W ~
EB
L(>.) ® S(>.).
AEA+ (Z,k)
(IlLl4)
(IlLl5)
3.
The map trd factors through the Temperley Lieb algebra T Ld' via 'l/J which was defined in
(II. 21).
(IlLl6)
Proof. Statements 1 and 2 follow from Mitsuhashi, [32] [Theorem 5.1]. Part 3 is a consequence of
IVIitsuhashi's result, combined with Lemma IlL2.1. We will explain a similar result in detail later
on, so we omit a full explanation here (See Remark IlL5.5 below).
III.3.S.
Jones Polynomial as a Q'uantum Invariant
The tensor square of the standard U-module W = L(l) decomposes as
o
(IlLl?)
where SZW ~ L(2) is the v-symmetrized submodule on which (-{z acts diagonally as the scalar v
and AZW ~ L(O) ~ C(v) is the v-skew-symmetrized submodule on which {-{z acts as _v-I. This
is the k = 2 example of Theorem IlL29, which we now interpret with arc diagrams.
27
We interpret the (0, 2)-tangle (a cap, reading up the page) as the linear map b : W@W ->
C(v), given by the formulas
C(v)
0
v-I
-1
0
.~ ...
r
1
1
1
1
(III.18)
W@W
WI @WI
WI @W2
W2 @WI
W2 @W2
Dually, we interpret the (2,0)-tangle (a cup) as the map c: C(v) -> W @ W, given by the
formula c(1) = WI @ W2 -
VW2 @ WI.
...~...
W@W
I
C(v)
(III.19)
The (2,2)-tangle (cup over cap) gives the composition cob: W@W -> W@W, which is a
non-zero multiple of the canonical map W
@ W
---» A2W '---' W
@ W, and is given by the formulas
~ ...
W@W
0
V-IWI @ W2 -
W2 @ WI
-WI @ W2 + VW2 @ WI
0
I
1
1
1
1
~...
W@W
WI @ WI
WI @W2
W2 @WI
W2 @W2
(IIl.20)
The map IdG•i- 1 @(c 0 b) @ Id@d-i.-l : W®d -~ W®d is precisely the image of the standard
generator Ui of T Ld in the representation 'Trd. Hence, we recover a matrix representation for the
generator Hi of 'Hd, using the relations 'Trd(Hi ) = 1fd(V -
Ui ) and 'Trd(Hi- l ) =
1fd(V-1 - Ui ), we
recover the action (III.12) of Hd.
X
W@W
v
(v - v-I )WI @ 'W2 + W2 @ WI
WI @W2
V
I
1
1
1
1
(III.21 )
............~ ...
~l@W
WI @WI
WI @W2
'W2 @WI
W2 @W2
X
W@W
v-I
W2 @WI
WI @ W2 -
(v -
v-I )W2 @ WI
v-I
I
1
1
1
1
(III.22)
/
W@W
WI @WI
WI @W2
W2 @WI
W2 @W2
28
111.4.
The Quantum Supergroup Uv(gl(111))
We introduce the general linear Lie 8uperalgebra 9
~ g[(111), as well as its universal
enveloping algebra U(g) and its quantization Uv(g). (See [40]) and [4]).
IIJ.4,l.
Lie Superalgebra g[(111)
'We work over the base ring ceo
A vector superspace of superdimension (min) is a Z2-
graded vector space W = Wo E8 WI whose even part Wo is of dimension m and whose odd part
il'l is of dimension n, For homogeneous elements w E vV:i , write Iwl = i E Z2. Let cem1n denote
the superspace cem E8 cen . The endomorphisms of cem1m form the Lie superalgebra 9 = g[(mln),
consisting of block matrices of the form
where A is an m x m matrix, B an m x n matrix, C an n x m matrix, and D an n x n matrix.
There is a Z2-grading: 9 = go E8 gl, where go consists of block diagonal matrices
(~ g) and gl
consists of matrices of the form (g ~). The Lie superbracket is defined on homogeneous elements
to be the supercommutator
[X, Y] = XY ~ (-l)ij yX,
where IXI = i, fYl = j.
(III.23)
and extended bilinearly.
This multiplication satisfies the axioms of a superbracket, namely for
homogeneous elements X, Y, Z with IXI = i, fYl = j, IZI = k,
[X, Y] + (-l)ij [y, X] = 0
(_l)ki[X, [Y, Z]] + (-l)ij [Y, [Z, X]] + (-l)jk[Z, [X, Y]] = 0
(super-skew commutativity)
(super-Jacobi),
(III.24)
III.4,2,
The Quantum Supergroup Uv(gl(111))
In the sequel, we shall only be interested in the quantum supergroup associated to the
Lie superalgebra 9 = gl(111). Following [4], let U be the quantum supergroup Uv(fj[(111)). This is
the unital, associative CC(v)-algebra generated by E, P, K a and K;;l (a E {I, 2}) subject to the
29
relations
K1F=v-1FK1,
K 2F=vFK2
K _K- 1
EF+FE=
l'
v - V-
where K = K1K;;1. Note that K 1 and K 2 are even while E and F are odd.
The weight of a vector 1)) in a U-module refers to A E Z such that K.1)) = V A1)). Let L(A)
denote the indecomposable weight module of highest weight A. Because E and F are nilpotent in U,
any indecomposable cyclic module has dimension at most four. Note that there are indecomposable
modules that are not simple, such as the the adjoint module. However, see Theorem III.4.1 below.
It is a standard fact that U is a Hopf superalgebra with comultiplication t>, counit E, and
antipode 8 given by
t>(Ka ) = K a 0 K a ,
t>(E) = E 0 K- 1+ 1 0 E,
t>(F) = F 01 + K 0 F,
E(K:;l) = 1,
c(E) = c(F) = O.
8(Ka ) = K;;l,
8(E) = -EK,
8(F) = _K- 1F.
Let Hi denote the natural module for U, represented in the basis {1))1, 1))2} (let 1))1 be even)
by the matrices
(
V 0)
K 1 f----l
0
0
'
(III.25)
Let p : U
~} End(W) be the representation.
Using the comultiplication in the Hopf
30
algebra, it extends to a representation of Pd : U
----. End(W0d ).
Set 6(1) =
6
and for i > 1,
6(i) = (6 (>9IdQ)i~l) o6(i-l). Then, Pd = p0d 0 6(d-l).
Theorem III.4.1 ([4]' Prop. 3.1). The representations Pd are completely reducible.
Make l-tr0d into a right 'Hd-module by defining the homomorphism 11'd : 'Hd ----. End(W0d)OP,
as follows. First, define the right operator H on W (>9 W by:
if i = j and IWil = 0,
(III.26)
Wj (>9 Wi
if i > j .
Now, set
and extend by linearity.
IIq.8.
SchuT- Weyl Duality for Uv(gl(111)) and 'Hd
Recall that A+(111, d) is the set of Young diagrams of hook shape with d boxes.
Theorem III.4.2 ([32], Theorem 5.1). Consider the maps
Pd
(
)
7T d
U ------0- End W (>9 ... (>9 W
~ 'Hd.
1.
The actions ofU and 'Hd on W
(>9 ... (>9 W commute.
2. As a (U, 'Hd)-bimodule, tensor space decomposes into simples
W (>9 ... (>9 W ~
EB
L(>") (>9 S(>..).
AEi\+(111.d)
(III.27)
(III.28)
(III.29)
31
III.5.
The Super Temperley-Lieb Algebra
III. 5.1
Defin·ition of STLd.
Definition III.5.1. The super Temperley-Lieb algebra STLd is the centralizer algebra
(HI.3D)
By Theorem III.4.2, this is 7rd(Hd)'
Proposition III.5.2.
d-l (
) 2
dimSTLd = L
d ~ 1
j=O
J
(
2d - 2)
d-1
(III.31)
Proof As abstract CC(v)-algebras, STLd ~ Ih EndS(A), where the product is over A whose Young
diagrams are hooks. Let AU) = (d - j, 11) be the hook partition of leg length j for 0 :s: j < d.
The irreducible representation S(A (1)) is of degree d -
1, and for each j = 0, ... ,d - 1, S(A(J)) ~
lVS(A(l)), hence has degree (djl).
The second equality follows from looking at the coefficient of t d - 1 in the expansion of
o
liVe have the presentation STLd = Hd/Id, where Id is the two sided ideal generated by
the idempotents e(A), where A is not a hook partition.
For 1 :s: d :s: 3, Id is trivial, hence the
representation trd is injective. Now, define J to be the two-sided ideal of H4 generated by
(III.32)
Lemma 111.5.3.
(III.33)
Proof The only partition of 4 that is not a hook is A = (22 ). The symmetrizer is
(IlI.34)
which is a nonzero scalar multiple of the idempotent e(A). Clearly, this generates the same two-
sided ideal as J.
o
32
For d 2: 4, define the embedding & : H4 '--7 Hd by &(Hi) = Hi, and let ':!d be the two-sided
(deal generated by &(J).
Theorem 111.5.4.
I d = Jd
JOT all d 2: 4.
Pmof. The following diagram commutes
(III.35)
(III.36)
where the bottom map sends ¢f-I c/J0Id@d-4. Since J
E ker7f4, &(J) E ker7fd, and so Jd
<;:;; Id.
Conversely, suppose that Jd # Id.
So, there exists A that is not a hook shape with
e(A)Jd = O.
Since S(A) embeds into Hde(A), Jd acts as 0 on S(A).
Since A is not a hook, its
diagram contains the diagram (2 2 ), so S(2 2 )
'--7
Res~= S(A).
Thus, Jd acts as 0 on S(2 2 ), a
contradiction.
o
Remark IlLS.S. The technique in Theorem IIL5.4 of reducing to the smallest A that is excluded
from the indexing set works generally.
In particular, the kernel of the map 1/J : Hd -» TL d is
generated by the symllletrizer c)., for A = (13), which is the smallest diagram not in A+ (2, d).
III. 5.2.
Robinson-Schenstedt-Knuth Correspondence
Recall that the Robinson-Schenstedt-Knuth (RSK) correspondence establishes a bijection
between permutations w E Sd and pairs of standard Young tableaux (P, Q) each of the same shape
A E Par(d) (see, e.g. [15]). The tableaux P is called the insertion tableaZlx and is defined by the
following algorithm.
Begin with the permutation written in one-line notation:
(w(l), ... ,w(d)).
Build the
sequence of tableaux 0 = Po, ... , Pd = P, forming Pi from Pi- 1 by inserting the number w(i)
as follows. Place w( i) as far to the left on the first row as possible. If it is placed on the end of
the row, then we are done. Otherwise, w(i) "bumps" a number out of its box, and that number
is placed on the next row, again as far to the left as possible. This algorithm terminates when a
number is placed on the end of a row (which may be a new row at the bottom of the diagram).
33
Two permutations w, Wi are in the same two-sided Kazhdan-Lusztig cell in Hd if they
produce tableaux of the same shape under the RSK correspondence. Let Cw denote the canonical
basis element (see [29] or [39]). Unlike the case TLd' which has a basis consisting of monomials
in the canonical elements - Ui = Hi - v, we do not know of such an elementary basis for STLd.
However,
Theorem 111.5.6. {Cw I shape of P(w) is a hook} is a basis fOT STLd.
PTOOf. For any .\ E Par(d) and for any T E Std(.\), the collection of Cw such that P(w) = T
is a basis for a submodule of the regular module Hd that is isomorphic to S(.\). Moreover, the
collection of all Cw such that the shape of P(w) is .\ forms the Wedderburn component in Hd
isomorphic to End S(.\). By the definition of STLd and Theorem III.4.2, we obtain a basis for the
algebra by concatenating the bases of each Wedderburn component corresponding to .\ of hook
shape.
D
34
CHAPTER IV
