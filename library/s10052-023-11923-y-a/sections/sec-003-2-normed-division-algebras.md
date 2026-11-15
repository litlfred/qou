---
doc_id: s10052-023-11923-y-a
doc_title: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-003-2-normed-division-algebras
section_title: "Normed division algebras"
section_number: 2
pages: 3-4
source_pdf: s10052-023-11923-y_a.pdf
source_sha256: 73d1a03532d62ef7
toc_source: outline
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
duplicate_of: "arxiv-2306.13098v2"
---
An algebra A over a ﬁeld K is a vector space over K (where
the scalars used in scalar multiplication come from the ﬁeld
K), equipped with a bilinear product A×A →A, that allows
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
commutative and associative, C is commutative and associa-
tive (but no longer self-conjugate), H is associative but no
longer commutative, and ﬁnally O is neither commutative
nor associative (but alternative).
The quaternions H are a generalization of the complex
numbers C with three mutually anticommuting imaginary
units I, J, K, satisfying;
I 2 = J 2 = K 2 = I J K = −1,
which implies I J = K = −J I, J K = I = −K J, and
K I = J = −I K. A general quaternion q may then be
written as
q = q01 + q1I + q2J + q3K,
q0, q1, q2, q3 ∈R
With the quaternion conjugate q deﬁned as q = q0 −q1I −
q2J −q3K. The norm of a quaternion |q| is subsequently
deﬁned by |q|2 = qq = qq, and the inverse q−1 = q/|q|2.
The automorphism group of H is SU(2). Indeed, there
is an isomorphism between the quaternions H and the real
Clifford algebra Cℓ(0, 2), while the complexiﬁed quater-
nions C ⊗H (isomorphic to the Pauli algebra) are isomor-
phic to the complex Clifford algebra Cℓ(2). Note, however,
that C ⊗H is not a division algebra (but remains asso-
ciative), and manifestly contains projectors, for example:
(1 + i K)(1 −i K) = 0.
The octonions O are the largest division algebra, of dimen-
sion eight. Its orthonormal basis is comprised of seven imag-
inary units: i1, . . . i7, along with the unit 1 = i0. A general
octonion x may then be written as
x = x0i0 + x1i1 + · · · + x7i7,
x0, . . . , x7 ∈R
with the octonion conjugate x deﬁned as x = x0i0 −x1i1 −
· · · −x7i7. The norm of an octonion |x| is subsequently
deﬁned by |x|2 = xx = xx, and the inverse x−1 = x/|x|2.
Fig. 1 The Fano plane, encoding the multiplicative structure of our
octonions, where a ≡ia, a = 1, . . . , 7. Note that each line is cyclic,
representing a quaternionic triple
The multiplication of octonions1 is captured in terms of
the Fano plane, see Fig. 1. Each projective line in the Fano
plane corresponds (together with the identity i0) to a H
subalgebra; there are seven such subalgebras. Like with H,
all the imaginary units anticommute under multiplication.
Unlike with H, the multiplication of elements not belonging
to the same H subalgebra is non-associative. For example
i4(i7i6) = −i5̸ = i5 = (i4i7)i6. Octonion multiplication
however is alternative x(xy) = (xx)y and y(xx) = (yx)x,
∀x, y ∈O. The complexiﬁed octonions C ⊗O are again not
a division algebra (but remains alternative).
As vector spaces O = C4. The splitting of O as C ⊕C3
relies on choosing a preferred octonion unit ia (and hence a
preferred C subalgebra in O). For our purpose we choose i4.
The map [36]
π(x) = 1
2(x + i4x ¯i4),
x ∈O
where ¯i4 indicates the octonion conjugation, then projects O
down to this preferred C ⊂O, and we can write the octonion
x = x0i0 + · · · + x7i7 as:
x = (x0 + x4i4)i0 + (x1 −x5i4)i1
+(x2 −x6i4)i2 + (x3 −x7i4)i3.
Note that the product i4x ¯i4 is deﬁned unambiguously since
O is alternative.
The automorphism group of O is known to be the excep-
tional Lie group G2. This exceptional group contains SU(3)
as one of its maximal subgroups, corresponding to the sta-
bilizer subgroup of one of the octonion imaginary units, or
equivalently, the subgroup of Aut(O) that preserves the rep-
resentation of O as the complex space C⊕C3. This splitting
is associated with the quark-lepton symmetry [36]. The space
1 There are different multiplication rules for O used by different authors
in the literature. Here we follow the multiplication table used in [40].
123
of internal states of a quark is then the three complex dimen-
sional space C3 whereas the internal space of a lepton is C.
Since O and C⊗O are nonassociative, they are not repre-
sentable as matrix algebras (with the standard matrix prod-
uct). The algebra generated from the composition of left and
right actions of O (and C ⊗O) however is associative, since
each such left (right) action corresponds to a linear operator
(endomorphism).
Let La (Ra) denote the linear operator of left (right) mul-
tiplication by a ∈C ⊗O:
La[x] = ax,
Ra[x] = xa,
∀a, x ∈C ⊗O.
(1)
Then
LaLb[x] = a(bx)̸ = Lab[x] = (ab)x,
Ra Rb[x] = (xb)a̸ = Rab[x] = x(ab).
The mappings a →La and a →Ra do not correspond to
algebra homomorphisms as they each generate an associative
algebra called the associative multiplication algebra.2 They
do however preserve the quadratic relations ⟨x, y⟩= 1
2(x y+
yx) where x, y ∈C ⊗O
Lx L y1 + L yLx1 = 2⟨x, y⟩1 = Rx Ry1 + Ry Rx1
Since La (Ra) correspond to linear operators, they can be
represented as 8 × 8 complex matrices (acting on the vector
space C ⊗O written as a column vector).
For C ⊗O, one ﬁnds the following identities [4,5]:
Li1 Li2 Li3 Li4 Li5 Li6x = Li7x,
(2)
...Lib Lia Lia Lic....x = −...Lib Lic....x
(3)
...Lia Lib...x = −...Lib Lia...,
(4)
where a, b, c = 1, . . . , 7.
DuetothenonassociativityofO,theleft(right)associative
multiplication algebra of C⊗O contains genuinely new maps
which are not captured by C ⊗O. For example, i3(i4(i6 +
i2))̸ = y(i6 + i2) for any y ∈C ⊗O. There are a total of
64 distinct left-acting complex-linear maps from C ⊗O to
itself, and these (due to the given identities above) provide a
faithful representation of Cℓ(6).
Denoting the 64-dimensional left (right) associative multi-
plication algebra generated from left (right) actions of C⊗O
on itself by (C ⊗O)L ((C ⊗O)R), one ﬁnds that any left
(right) action can always be rewritten as a right (left) action
[4]. That is:
(C ⊗O)L ∼= (C ⊗O)R ∼= Cℓ(6).
(5)
This is in contrast to a similar construction for C⊗H, where
one ﬁnds that the left and right actions are genuinely distinct,
each generating a copy of Cℓ(2). The left and right adjoint
2 We will henceforth refer to this algebra simply as the left action alge-
bra or left multiplication algebra.
actions in this case commute, and only by considering both
does one obtain a basis for Mat(4, C) ∼= Cℓ(4).
