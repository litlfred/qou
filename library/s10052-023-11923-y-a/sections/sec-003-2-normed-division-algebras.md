---
doc_id: s10052-023-11923-y-a
doc_title: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-003-2-normed-division-algebras
section_title: "Normed division algebras"
section_number: 2
pages: 2-5
source_pdf: s10052-023-11923-y_a.pdf
source_sha256: 73d1a03532d62ef7
doc_brief: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU (3)C color symmetry based on the"
duplicate_of: "arxiv-2306.13098v2"
---
and octonions O. In Sect. 3 we review the construction of
one generation of fermions with unbrokenSU(3)c ×U(1)em
gauge symmetry from C⊗ O, following closely [5]. The CD
construction and the algebra of sedenions are discussed in
Sect. 4. Finally we present our three generation model based
on the algebra of sedenions in Sect. 5. We conclude with an
outlook of how to develop the model further, and a discussion.
123
Eur. Phys. J. C (2023) 83 :747 Page 3 of 13 747
2 Normed division algebras
An algebra A over a ﬁeld K is a vector space over K (where
the scalars used in scalar multiplication come from the ﬁeld
K), equipped with a bilinear productA×A → A, that allows
for multiplication of algebra elements.
A division algebra is an algebra over a ﬁeld where division
is always well-deﬁned, except by zero. A normed division
algebra has the additional property that it is also a normed
vector space, with the norm deﬁned in terms of a conju-
gate. A well-known result by Hurwitz [39] is that there exist
only four normed division algebras (over the ﬁeld of real
numbers): R, C, H, O, of dimensions one, two, four and
eight respectively. In going to higher-dimensional algebras,
successive algebraic properties are lost: R is self-conjugate,
commutative and associative,C is commutative and associa-
tive (but no longer self-conjugate), H is associative but no
longer commutative, and ﬁnally O is neither commutative
nor associative (but alternative).
The quaternions H are a generalization of the complex
numbers C with three mutually anticommuting imaginary
units I, J, K , satisfying;
I 2 = J2 = K 2 = IJK =− 1,
which implies IJ = K =− JI , JK = I =− KJ , and
KI = J =− IK . A general quaternion q may then be
written as
q = q01 + q1 I + q2 J + q3 K, q0, q1, q2, q3 ∈ R
With the quaternion conjugate q deﬁned as q = q0 − q1 I −
q2 J − q3 K . The norm of a quaternion |q| is subsequently
deﬁned by |q|2 = qq = qq , and the inverse q−1 = q/|q|2.
The automorphism group of H is SU(2). Indeed, there
is an isomorphism between the quaternions H and the real
Clifford algebra C𝓁(0, 2), while the complexiﬁed quater-
nions C ⊗ H (isomorphic to the Pauli algebra) are isomor-
phic to the complex Clifford algebra C𝓁(2). Note, however,
that C ⊗ H is not a division algebra (but remains asso-
ciative), and manifestly contains projectors, for example:
(1 + iK )(1 − iK ) = 0.
The octonionsO are the largest division algebra, of dimen-
sion eight. Its orthonormal basis is comprised of seven imag-
inary units: i1,... i7, along with the unit 1 = i0. A general
octonion x may then be written as
x = x0i0 + x1i1 +···+ x7i7, x0,..., x7 ∈ R
with the octonion conjugate x deﬁned as x = x0i0 − x1i1 −
··· − x7i7. The norm of an octonion |x| is subsequently
deﬁned by |x|2 = x x = xx , and the inverse x−1 = x/|x|2.
Fig. 1 The Fano plane, encoding the multiplicative structure of our
octonions, where a ≡ ia, a = 1,..., 7. Note that each line is cyclic,
representing a quaternionic triple
The multiplication of octonions 1 is captured in terms of
the Fano plane, see Fig. 1. Each projective line in the Fano
plane corresponds (together with the identity i0)t oa H
subalgebra; there are seven such subalgebras. Like with H,
all the imaginary units anticommute under multiplication.
Unlike with H, the multiplication of elements not belonging
to the same H subalgebra is non-associative. For example
i4(i7i6) =− i5 ⁄= i5 = (i4i7)i6. Octonion multiplication
however is alternative x(xy) = (xx )y and y(xx ) = (yx)x,
∀x, y ∈ O. The complexiﬁed octonions C ⊗ O are again not
a division algebra (but remains alternative).
As vector spaces O = C4. The splitting of O as C ⊕ C3
relies on choosing a preferred octonion unit ia (and hence a
preferred C subalgebra in O). For our purpose we choosei4.
The map [36]
π(x) = 1
2(x + i4 x ¯i4), x ∈ O
where ¯i4 indicates the octonion conjugation, then projects O
down to this preferredC ⊂ O, and we can write the octonion
x = x0i0 +···+ x7i7 as:
x = (x0 + x4i4)i0 + (x1 − x5i4)i1
+(x2 − x6i4)i2 + (x3 − x7i4)i3.
Note that the product i4 x ¯i4 is deﬁned unambiguously since
O is alternative.
The automorphism group of O is known to be the excep-
tional Lie group G2. This exceptional group contains SU(3)
as one of its maximal subgroups, corresponding to the sta-
bilizer subgroup of one of the octonion imaginary units, or
equivalently, the subgroup of Aut(O) that preserves the rep-
resentation of O as the complex spaceC⊕ C3. This splitting
is associated with the quark-lepton symmetry [36]. The space
1 There are different multiplication rules forO used by different authors
in the literature. Here we follow the multiplication table used in [40].
123
747 Page 4 of 13 Eur. Phys. J. C (2023) 83 :747
of internal states of a quark is then the three complex dimen-
sional space C3 whereas the internal space of a lepton is C.
Since O and C⊗ O are nonassociative, they are not repre-
sentable as matrix algebras (with the standard matrix prod-
uct). The algebra generated from the composition of left and
right actions of O (and C ⊗ O) however is associative, since
each such left (right) action corresponds to a linear operator
(endomorphism).
Let La (Ra) denote the linear operator of left (right) mul-
tiplication by a ∈ C ⊗ O:
La[x]= ax, Ra[x]= xa, ∀a, x ∈ C ⊗ O. (1)
Then
La Lb[x]= a(bx) ⁄= Lab[x]= (ab)x,
Ra Rb[x]= (xb)a ⁄= Rab[x]= x(ab).
The mappings a → La and a → Ra do not correspond to
algebra homomorphisms as they each generate an associative
algebra called the associative multiplication algebra.2 They
do however preserve the quadratic relations⟨x, y⟩= 1
2(x y+
yx) where x, y ∈ C ⊗ O
Lx L y1 + L y Lx 1 = 2⟨x, y⟩1 = Rx Ry1 + Ry Rx 1
Since La (Ra) correspond to linear operators, they can be
represented as 8 × 8 complex matrices (acting on the vector
space C ⊗ O written as a column vector).
For C ⊗ O, one ﬁnds the following identities [4,5]:
Li1 Li2 Li3 Li4 Li5 Li6 x = Li7 x, (2)
...Lib Lia Lia Lic ....x =− ...Lib Lic ....x (3)
...Lia Lib ...x =− ...Lib Lia ..., (4)
where a, b, c = 1,..., 7.
Due to the nonassociativity ofO, the left (right) associative
multiplication algebra ofC⊗O contains genuinely new maps
which are not captured by C ⊗ O. For example, i3(i4(i6 +
i2)) ⁄= y(i6 + i2) for any y ∈ C ⊗ O. There are a total of
64 distinct left-acting complex-linear maps from C ⊗ O to
itself, and these (due to the given identities above) provide a
faithful representation of C𝓁(6).
Denoting the 64-dimensional left (right) associative multi-
plication algebra generated from left (right) actions ofC⊗ O
on itself by (C ⊗ O)L ((C ⊗ O)R), one ﬁnds that any left
(right) action can always be rewritten as a right (left) action
[4]. That is:
(C ⊗ O)L ∼= (C ⊗ O)R ∼= C𝓁(6). (5)
This is in contrast to a similar construction forC⊗ H, where
one ﬁnds that the left and right actions are genuinely distinct,
each generating a copy of C𝓁(2). The left and right adjoint
2 We will henceforth refer to this algebra simply as the left action alge-
bra or left multiplication algebra.
actions in this case commute, and only by considering both
does one obtain a basis for Mat (4, C) ∼= C𝓁(4).
3 One generation of electrocolor states from C ⊗ O
Let e1 := Li1,..., e6 := Li6 be a generating basis (overC6)
for C𝓁(6) associated with the left multiplication algebra of
the complex octonions, satisfying e2
i =− 1, ei e j =− e j ei .
Deﬁne the Witt basis
α†
1 = 1
2(e1 + ie5), α 1 = 1
2(−e1 + ie5),
α†
2 = 1
2(e2 + ie6), α 2 = 1
2(−e2 + ie6),
α†
3 = 1
2(e3 + ie7), α 3 = 1
2(−e3 + ie7).
Here † corresponds to the composition of complex and octo-
nion conjugation. This new basis satisﬁes the anticommuta-
tion relations3
{αi,α j}={ α†
i ,α †
j }= 0, {αi,α †
j }= δij . (6)
Each pair of ladder operators in isolation generatesC𝓁(2),
and is associated with one of the three H subalgebras of
O that contain the privileged complex subalgebra generated
by e4. Subsequently, we obtain three anticommuting copies
of C𝓁(2), which when considered together generate the full
C𝓁(6) left multiplication algebra of C ⊗ O.
From the Witt basis, it is possible to construct two minimal
left ideals of the algebra C𝓁(6), following the procedure in
[41] (see [5] for a detailed construction):
C𝓁(6)ωω†, C𝓁(6)ω†ω,
where ω = α1α2α3 and ω† = α†
3α†
2α†
1 are nilpotents, but
ωω† and ω†ω are primitive idempotents. Each ideal is eight
complex dimensional. Explicitly,
Su = νωω†
+dr α†
1ωω† + dgα†
2ωω† + dbα†
3ωω†
+ur α†
3α†
2ωω† + ugα†
1α†
3ωω† + ubα†
2α†
1ωω†
+e+α†
3α†
2α†
1ωω†,
Sd = νω†ω
+dr α1ω†ω + dgα2ω†ω + dbα3ω†ω
+ur α3α2ω†ω + ugα1α3ω†ω + ubα2α1ω†ω
+e−α3α2α1ω†ω,
where the suggestively labelled coefﬁcients are elements of
C.
The unitary symmetries that preserve the Witt basis, and
hence the minimal left ideals is U(3) = SU(3) × U(1).
3 Note that as left actions we have{Lαi , Lα j }x = 0e t cf o rx ∈ C⊗ O.
123
Eur. Phys. J. C (2023) 83 :747 Page 5 of 13 747
The generators of this symmetry, written in terms of the Witt
basis, are:
Λ1 =− α†
2α1 − α†
1α2,Λ 2 = iα†
2α1 − iα†
1α2,
Λ3 = α†
2α2 − α†
1α1,Λ 4 =− α†
1α3 − α†
3α1,
Λ5 =− iα†
1α3 + iα†
3α1,Λ 6 =− α†
3α2 − α†
2α3,
Λ7 = iα†
3α2 − iα†
2α3,
Λ8 =− 1√
3
(α†
1α1 + α†
2α2 − 2α†
3α3),
and
Q = 1
3(α†
1α1 + α†
2α2 + α†
3α3). (7)
The basis states of the C𝓁(6) minimal ideals transform as
1⊕ 3⊕ 3⊕ 1 under SU(3), and this symmetry can therefore
be associated with the color symmetry SU(3)C , justifying
the choice of coefﬁcients. The U(1) generator Q (together
with −Q∗), related to the number operatorQ = N/3, on the
other hand gives correct electric charge for each state. The
ideal Su contains the isospin up states, whereas the ideal Sd
contains the isospin down states.
One generation of leptons and quarks with correct unbro-
ken SU(3)C × U(1)em symmetry can therefore be elegantly
represented in terms of two minimal left ideals ofC𝓁(6) gen-
erated from C ⊗ O. The dimension of the minimal ideals
dictates the number of distinct physical states, whereas the
gauge symmetries are those unitary symmetries that preserve
the ideals (or equivalently, the Witt basis).
