---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-001-normed-division-algebras
section_title: "Normed division algebras"
section_number: null
pages: 3-5
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
doc_brief: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU (3)C color symmetry based on the"
---
nions H and octonions O. In Section 3 we review the construction of one generation of fermions with unbroken
SU (3)c×U(1)em gauge symmetry from C⊗ O, following closely [5]. The Cayley-Dickson construction and
the algebra of sedenions are discussed in Section 4. Finally we present our three generation model based on
the algebra of sedenions in Section 5. We conclude with an outlook of how to develop the model further,
and a discussion.
2 Normed division algebras
A division algebra is an algebra over a field where division is always well-defined, except by zero. A normed
division algebra has the additional property that it is also normed vector spaces, with the norm defined in
terms of a conjugate. A well-known result by Hurwitz [39] is that there exist only four normed division
algebras (over the field of real numbers): R, C, H, O, of dimensions one, two, four and eight respectively. In
going to higher-dimensional algebras, successive algebraic properties are lost: R is self-conjugate, commuta-
tive and associative, C is commutative and associative (but no longer self-conjugate), H is associative but
no longer commutative, and finally O is neither commutative nor associative (but alternative).
The quaternions H are a generalization of the complex numbers C with three mutually anticommuting
imaginary units I,J,K , satisfying I 2 = J 2 = K 2 = IJK =−1, which implies IJ = K =−JI , JK = I =
−KJ , and KI =J =−IK . A general quaternion q may then be written as
q =q01 +q1I +q2J +q3K, q 0,q 1,q 2,q 3∈ R, (1)
With the quaternion conjugate q defined as q = q0−q1I−q2J−q3K. The norm of a quaternion |q| is
subsequently defines by|q|2 =qq =qq, and the inverse q−1 =q/|q|2.
The automorphism group of H is SU (2). Indeed, there is an isomorphism between the quaternions H
and the real Clifford algebra Cℓ(0, 2), while the complexified quaternions C⊗ H (isomorphic to the Pauli
algebra) are isomorphic to the complex Clifford algebra Cℓ(2). Note, however, that C⊗ H is not a division
algebra (but remains associative), and manifestly contains projectors, for example: (1 + iK)(1−iK) = 0.
The octonions O are the largest division algebra, of dimension eight. Its orthonormal basis comprises
seven imaginary units: i1,...i 7, along with the unit 1 = i0. A general octonion x may then be written as
x =x0i0 +x1ii +... +x7i7, x 0,...,x 7∈ R, (2)
with the octonion conjugate x defined as x = x0i0−x1i1−...−x7i7. The norm of an octonion |x| is
subsequently defines by|x|2 =xx =xx, and the inverse x−1 =x/|x|2.
The multiplication of octonions1 is captured in terms of the Fano plane Fig. 1. Each projective line in the
Fano plane corresponds (together with the identityi0) to an H subalgebra; there are seven such subalgebras.
Like with H, all the imaginary units anticommute under multiplication. Unlike with H, the multiplication
of elements not belonging to the same H subalgebra is non-associative. For example i4(i7i6) =−i5̸=i5 =
(i4i7)i6. Octonion multiplication however is alternative x(xy) = (xx)y and y(xx) = (yx)x,∀x,y ∈ O. The
complexified octonions C⊗ O are again not a division algebra (but remains alternative).
As vector spaces O = C4. The splitting of O as C⊕ C3 relies on choosing a preferred octonion unit ia
(and hence a preferred C subalgebra in O). For our purpose we choose i4. The map [36]
π(x) = 1
2(x +i4x ¯i4), x ∈ O, (3)
1There are different multiplication rules for O used by different authors in the literature. Here we follow the multiplication
table used in [40]
3
Figure 1: The Fano plane, encoding the multiplicative structure of our octonions, where a≡ia, a= 1,..., 7.
Note that each line is cyclic, representing a quaternionic triple.
where ¯i4 indicates the octonion conjugation, then projects O down to this preferred C⊂ O, and we can write
the octonion x =x0i0 +... +x7i7 as:
x = (x0 +x4i4)i0 + (x1−x5i4)i1 + (x2−x6i4)i2 + (x3−x7i4)i3. (4)
Note that the product i4x ¯i4 is defined unambiguously since O is alternative.
The automorphism group of O is the 14-dimensional exceptional Lie group G2. This exceptional group
contains SU (3) as one of its maximal subgroups, corresponding to the stabilizer subgroup of one of the
octonion imaginary units, or equivalently, the subgroup of Aut(O) that preserves the representation of O as
the complex space C⊕ C3. This splitting is associated with the quark-lepton symmetry [36]. The space of
internal states of a quark is then the three complex dimensional space C3 whereas the internal space of a
lepton is C.
Since O and C⊗ O are nonassociative, they are not representable as matrix algebras (with the standard
matrix product). The algebra generated from the composition of left and right actions of O (and C⊗ O)
however is associative, since each such left (right) action corresponds to a linear operator (endomorphism).
Let La (Ra) denote the linear operator of left (right) multiplication by a∈ C⊗ O:
La[x] =ax, R a[x] =xa, ∀a,x∈ C⊗ O. (5)
Then
LaLb[x] = a(bx) ̸= Lab[x] = (ab)x, (6)
RaRb[x] = ( xb)a ̸= Rab[x] =x(ab). (7)
The mappings a→La and a→Ra do not correspond to algebra homomorphisms as they each generate an
associative algebra called the associative multiplication algebra 2. They do however preserve the quadratic
relations⟨x,y⟩ = 1
2(xy +yx) where x,y∈ C⊗ O
LxLy1 +LyLx1 = 2⟨x,y⟩1 =RxRy1 +RyRx1. (8)
SinceLa (Ra) correspond to linear operators, they can be represented as 8 × 8 complex matrices (acting
on the vector space C⊗ O written as a column vector).
For C⊗ O, one finds the following identities [4, 5]:
Li1Li2Li3Li4Li5Li6x = Li7x, (9)
...LibLiaLiaLic....x = −...LibLic....x, (10)
...LiaLib...x = −...LibLia..., (11)
where a,b,c = 1,..., 7.
2We will henceforth refer to this algebra simply as the left action algebra or left multiplication algebra
4
Due to the nonassociativity of O, the left (right) associative multiplication algebra of C⊗ O contains
genuinely new maps which are not captured by C⊗ O. For example, i3(i4(i6 +i2))̸= y(i6 +i2) for any
y∈ C⊗ O. There are a total of 64 distinct left-acting complex-linear maps from C⊗ O to itself, and these
(due to the given identities above) provide a faithful representation of Cℓ(6).
Denoting the 64-dimensional left (right) associative multiplication algebra generated from left (right)
actions of C⊗ O on itself by ( C⊗ O)L ((C⊗ O)R), one finds that any left (right) action can always be
rewritten as a right (left) action [4]. That is:
(C⊗ O)L∼= (C⊗ O)R∼= Cℓ(6). (12)
This is in contrast to a similar construction for C⊗ H, where one finds that the left and right actions are
genuinely distinct, each generating a copy of Cℓ(2). The left and right adjoint actions in this case commute,
and only by considering both does one obtain a basis for Mat(4, C)∼= Cℓ(4).
