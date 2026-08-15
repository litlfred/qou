---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-6
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
The exceptional Jordan algebraJ =J 8
3 =H3(O) – the algebra of 3×3 hermitian
matrices with octonionic entries (reviewed in [McC, J68, B, Be, BS, G, Y]) –
appears to be tailor made for the description of three families of quarks and
leptons (like
(u c t
νe νµ ντ
)
or
(d s b
e µ τ
)
of a ﬁxed chirality) – see [DV], brieﬂy
outlined in Sect. 2. There are three exceptional Lie algebras associated with J:
(a) the automorphism or derivation algebra
Der (J) = f4 (= LieF4) =so(9) ˙+S9 =so(8) ˙+S+
8 ˙+S−
8 ˙+V8, (1.1)
(we use, following [BS], the sign ˙+ for the direct sum of vector spaces,
to be distinguished from the direct sum ⊕ of (mutually commuting) alge-
bras);
(b) the (reduced) structure algebra
str (J) = e6 (= LieE6) = f4 ˙+J0 ; (1.2)
(c) the conformal algebra
co (J) = e7 (= LieE7) = e6 ˙+ 2J ˙+ C. (1.3)
Here LieG stands for the Lie algebra of the Lie groupG;S9 is the 16-dimensional
spinor representation of the rotation Lie algebra so(9); it can be viewed as the
direct sum of the two inequivalent 8-dimensional spinor representations S±
8 of
so(8);V8 is the (8-dimensional) vector representation ofso(8);J0 is the traceless
part of J (the 26 dimensional real vector space of 3 × 3 hermitian traceless
octonionic matrices, also denoted as sH3(O)). The construction of the above
exceptional Lie algebras involves the magic square of Freudenthal and Tits. It
is explained in [BS, B] – see the summary in Sect. 3.
The Borel-de Siebenthal theory (see [BdS, K]) describes the maximal closed
connected subgroups of a compact Lie group that have maximal rank. Our main
observation (Sect. 4) is that the intersection of the maximal subgroups Spin (9),
and SU (3)×SU (3)
Z3
of the (compact) automorphism group F4 of J is the gauge
group of the standard model of particle physics
GF4 =GST =S(U(2)×U(3)) = SU (2)×SU (3)×U(1)
Z6
. (1.4)
This result makes it natural to consider as possible extensions of GST the inter-
sections of appropriate maximal rank subgroups of Str (J) =E6,
GE6 =S(U(2)×U(2)×U(3)) (1.5)
and of Co(J) =E7;
GE7 =S(U(2)×U(3)×U(3)). (1.6)
2
Note that all three groups, GF4, GE6, GE7 are non-semisimple (i.e. they in-
clude U(1) factors) compact subgroups of F4,E 6,E 7, of maximal rank (4 , 6, 7,
respectively).
It would be useful to consider J as a member of the family Hn(K) where
K is an alternative composition algebra . We recall that an algebra A is said
to be a division algebra if ab = 0 for a,b ∈A implies that either a = 0 or
b = 0. It is called an alternative algebra if any two elements of A generate
an associative subalgebra. Zorn has proven (in 1933) that there are just four
alternative division algebras: the real and the complex numbers, R and C, the
quaternions, H, and the octonions, O. All four admit a multiplicative norm
x→|x|∈ R+ such that
|xy| =|x||y|, |x|2 =x ¯x = ¯xx (> 0 for x⁄= 0) (1.7)
where x→ ¯x is the (involutive) conjugation in K. Hurwitz has proven back in
1898 that the only normed division algebras are R, C, H and O. Hn(K) is the
algebra of n×n hermitian matrices (with entries in K) closed under the Jordan
multiplication
X◦Y = 1
2(XY +YX ) (=Y◦X). (1.8)
For K = O the resulting algebra only satisﬁes the Jordan condition
(X 2Y )X =X 2(YX ) (1.9)
forn = 1, 2, 3. The condition (1.9), on the other hand, characterizes an abstract
Jordan algebra for which the endomorphismZ→X(YZ )−Y (XZ ) is an (inner)
derivation.
Division algebras can be also characterized by the existence of a non-degene-
rate real trilinear form t : K×3→ R, the triality form – see Sect. 2.4 of [B]. (We
note that it looks nontrivial even for K = C. In this case, for zj = xj +iyj,
j = 1, 2, 3, the form is a multiple of t(z1,z 2,z 3) =x1x2x3−x1y2y3−x2y1y3−
x3y1y2.) In general, the presence of a hermitian inner product (cf. (1.7)) makes
the existence of t equivalent to the existence of a K-valued cross product in K.
We shall consider (in Sect. 2 and Sect. 3.3) more general alternative compo-
sition algebras which have a (not necessarily positive deﬁnite) non-degenerate
sesquilinear form⟨x,y⟩ satisfying the (square of the) factorization property (1.7):
⟨xy,xy⟩ =⟨x,x⟩⟨y,y⟩, (1.10)
and have an alternating associator (see Eq. (2.3) below).
2 Exceptional ﬁnite quantum geometry
In the approach of almost commutative geometry [DKM, D, CL, C, CC, CCS,
BF] to the standard model, space-time is viewed as the tensor product of a stan-
dard (commutative) 4-dimensional spin manifold with a ﬁnite noncommutative
3
space. In the almost classical quantum geometry approach one is led to identify
the ﬁnite quantum space with the exceptional Jordan algebra.
To begin with, it was argued in [DV] that the decomposition of the (8-
dimensional, real) vector space O of octonions 1 into a direct sum of complex
vector spaces,
O = C⊕ C3 (2.1)
naturally corresponds to the splitting of the basic fermions (in one generation)
of the standard model into quarks and leptons. Moreover, the color groupSU (3)
leaves invariant a (complex) volume form onC3 which is dual with respect to the
hermitian scalar product⟨,⟩ in C3 to a skew symmetric antilinear cross product
z× w =− w× z (× : C3⊗ C3→ C3): Vol (z1, z2, z3) =< z1× z2, z3 >. This
cross product and the (hermitian) inner product⟨z, w⟩ (⟨,⟩ : C3⊗C3→ C) can
be combined with the usual multiplication of complex numbers and extended
to a unique real bilinear multiplication xy in O that is norm preserving:
⟨xy,xy⟩ =⟨x,x⟩⟨y,y⟩,
x =z0⊕ z⇒⟨x,x⟩ = ¯z0z0 +
3∑
i=1
¯zizi (≡|x|2) (2.2)
(¯z standing for the complex conjugate of z∈ C). The resulting product is non
associative but alternative: the associator
[x,y,z ] = (xy)z−x(yz) (2.3)
is an alternating function of x,y,z ; in particular, it vanishes if any two of the
arguments x,y,z coincide. More generally, this is true for any composition
algebra – i.e. an algebra with a non-degenerate (but not necessarily positive
deﬁnite – thus including the split octonions) inner product ⟨ , ⟩ satisfying the
ﬁrst equation (2.2) (cf. [BS]).
The signiﬁcance of the notion of an alternative algebra is illustrated by the
following remark. The commutator
adax = [a,x ]
deﬁnes a derivation in an associative algebra:
ada (xy) = (adax)y +xaday.
This property fails, in general, for a non-associative algebra. If however the
algebraA is alternative, every pair of elements x,y ∈A deﬁnes a derivation
Dx,y inA in terms of the double commutator and the associator:
Dx,y(z) = [[x,y ],z ]− 3 [x,y,z ] (2.4)
1Octonios have been ﬁrst applied to the standard model by Feza G¨ ursey and his students
[G]. His work triggered an imaginative development by G. Dixon [Di] followed by C. Furey
[Fu] among others. A distinguished feature of our approach, started in [DV], is the fact that
we are dealing with an euclidean Jordan algebra suited for a (ﬁnite) observable algebra.
4
(see Eq. (14) of [B]).
The construction of the octonionic scalar product satisfying (2.2) in terms
of the cross product and the inner product in C3, indicated above (and worked
out in [DV, TD]) yields the standard multiplication in O which is conveniently
expressed in terms of the Fano plane of imaginary octonionic units recalled in
Appendix A. Choosing, say, e7 as the “i” in C we can write the decomposition
(2.1) explicitly in the basis {e0 = 1,ej,j = 1,..., 7} as:
x =x0 +x7e7 + (x1 +x3e7)e1 + (x2 +x6e7)e2 +
+ (x4 +x5e7)e4
(
=
7∑
α=0
xαeα
)
. (2.5)
The presence of three generations of quark-lepton doublets
(
u ν
d e
)
(with
u,d – 3-vectors in the color space) suggests combining the octonions into a 3×3
hermitian matrix:
X =


ξ1 x3 ¯x2
¯x3 ξ2 x1
x2 ¯x1 ξ3

, x i∈ O, ξ i =ξi∈ R (2.6)
where the bar over an octonion x stands for octonionic conjugation (changing
simultaneously the sign of all imaginary units ej, j = 1,..., 7).
The matrices (2.6) span a 27-dimensional real vector space which can be
given the structure of the exceptional Jordan algebra J = J 8
3 (= H3(O)) with
multiplication deﬁned as the symmetrized matrix multiplication (1.8):
X◦Y = 1
2 (XY +YX ). (2.7)
As emphasized in [DV] the (axiomatic) properties of the (commutative) Jordan
product◦ are dictated by the requirement to have a spectral decomposition for
(hermitian) observables. In fact, the requirement of formal reality (∑
i
x2
i = 0⇒
xi = 0 for all i) implies that the Jordan condition (1.9)
(x2◦y)◦x =x2◦ (y◦x) (2.8)
is equivalent to power associativity
xrxs =xr+s (x∈J, r,s ∈ N) (2.9)
as proven in [JvNW] (see Theorem 1 of [DV]). It is clearly necessary for the
standard theory of spectral decomposition.
We recall the remark after Eq. (1.9) according to which the Jordan condition
(2.8) ensures that the commutator of two left multiplications is a derivation:
[Lx,Ly]∈ DerJ for Lx(y) :=x◦y, x,y ∈J (2.10)
5
(i.e. [Lx,Ly] (z◦w) = [Lx,Ly] (z)◦w +z◦ [Lx,Ly] (w)).
One also deﬁnes a real linear function tr X, a bilinear inner product ⟨X,Y⟩
and a symmetric trilinear form tr (X,Y,Z ) on J setting
trX =ξ1 +ξ2 +ξ3 (=⟨X, 1 I⟩),
⟨X,Y⟩ = tr (X◦Y ),
tr (X,Y,Z ) =⟨X,Y ◦Z⟩ =⟨X◦Y,Z⟩. (2.11)
3 The Lie algebra of derivations of J and its
extensions: the structure and the conformal
algebras
There are excellent detailed expositions of the material of this section. We
share the opinion of John Baez [B] that to survey the early developments of
this subject “one still cannot do better than to read Freudenthal’s classic 1964
paper [F] on Lie groups and foundations of geometry”. Later work including
the 1966 Vinberg’s and the 1976 Ramond’s (triality) constructions is given a
self contained treatment in [BS] (appearing about the same time as Baez’s tem-
peramental survey). The less emotional 2009 review by Yokota [Y] provides
a systematic treatment of exceptional Lie groups (with all formulas needed to
follow the details). The present short survey aims to ﬁx our notation and to
formulate the results that will be used in Sect. 4.
