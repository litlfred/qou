---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-001-2-multivariable-little-q-jacobi-polynomials
section_title: "Multivariable little q-Jacobi polynomials"
section_number: 2
pages: 4-6
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
Important in our approach is the fact that (quantum) dimensions o f irreducible spher-
ical representations associated to quantum, real/complex and p-adic Grassmannians are
degenerations of a generalized dimension formula involving multivariab le little q-Jacobi
polynomials, which we now introduce. We work over the ﬁeld E (see (1.4)), although in
the present situation c andd are dummy parameters and could just as well be omitted (in
contrast to the Macdonald-Koornwinder and multivariable big q-Jacobi case as treated in
Section 6).
The symmetric group Sn in n letters acts on Zn
+ by permuting the coordinates. The
corresponding fundamental domain is the cone Λ n of partitions with at most n parts. The
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 5
symmetric group Sn acts on E[z] = E[z1,...,z n] by permuting the independent variables
z1,...,z n. We denote E[z]S for the subalgebra of Sn-invariant polynomials in E[z]. An
E-basis of E[z]S is formed by the symmetric monomials ~mλ(z) =∑
µ∈Snλzµ (λ ∈ Λ n). The
monic multivariable little q-Jacobi polynomial P L
λ (z) = P L
λ (z;a,b ;q,t ) ∈ E[z]S of degree
λ ∈ Λ n from [26] is of the form
(2.1) P L
λ (z) = ~mλ(z) +
∑
µ∈Λ n:µ<λ
cL
λ,µ~mµ(z)
for certain coeﬃcients cL
λ,µ = cL
λ,µ(a,b ;q,t ) ∈ E. The multivariable little q-Jacobi polyno-
mials can be characterized as solution of a second-order diﬀerence equation, or in terms
of orthogonality relations deﬁned with respect to an explicit discret e probability orthogo-
nality measure. The characterization in terms of the diﬀerence equ ation is as follows. For
j = 1,...,n we write Tj for the multiplicative q-shift in zj,
(Tjf )(z) = f (z1,...,z j−1,qz j,z j+1,...,z n), f ∈ E[z±1].
The characterizing diﬀerence equation then reads DLP L
λ =EqJ
λ P L
λ where
DL =
n∑
j=1
(
φ+
L,j(z)(Tj − Id) +φ−
L,j(z)(T−1
j − Id)
)
,
φ+
L,j(z) = qtn−1a
(
b − 1
qzj
) ∏
l⁄=j
zl −tzj
zl −zj
, φ −
L,j(z) =
(
1 − 1
zj
) ∏
l⁄=j
zj −tzl
zj −zl
and with eigenvalue
EqJ
λ =
n∑
j=1
(
qabt2n−j−1(qλj − 1) +tj−1(q−λj − 1)
)
.
An algebraic formulation of the orthogonality relations of the multiva riable little q-Jacobi
polynomials is as follows. Deﬁne an E-linear functional
hL =ha,b;q,t
L : E[z]S → E
by requiring
hL
(
P L
λ
)
=
{
1, if λ = 0,
0, if λ ⁄= 0.
Deﬁne a form ⟨·, ·⟩L = ⟨·, ·⟩a,b;q,t
L on E[z]S by
(2.2) ⟨p1,p 2⟩L =hL
(
p1(z)p2(z)
)
, p 1,p 2 ∈ E[z]S,
where p(z) ↦→p(z) stands for the anti-linear algebra involution on E[z] which extends
complex conjugation on C by requiring that the parameters a,b,c,d,q,t and the variables
zj to be formally real, e.g. a = a and zj = zj. The orthogonality relations now take the
form
(2.3) ⟨P L
λ,P L
µ ⟩L =NL(λ)δλ,µ, λ,µ ∈ Λ n
6 URI ONN AND JASPER V. STOKMAN
for suitable explicit quadratic norms NL(λ) = NL(λ;a,b ;q,t ) ∈ E, which are recalled in
Subsection 6.2.
The expressions
(2.4) Dq(λ;a,b ;t) =
(
P L
λ (0;q−1a,q−1b;q,t )
) 2
NL(λ;q−1a,q−1b;q,t ) ∈ E, λ ∈ Λ n
play a crucial role in the sequel. Note that Dq(λ;a,b ;t) is the generalized dimension d(λ)
from the introduction (see (1.3)), up to a slight reparametrization of the four auxiliary
parameters a,b,q and t (which we justify in a moment).
We show that specializations of the parameters ( a,b,t ) in Dq(λ) give the quantum di-
mensions of spherical irreducible representations associated to q uantum complex Grass-
mannians. In addition we show that suitable degenerations in ( a,b,q,t ) lead to the dimen-
sions of spherical irreducible representations associated to comp lex/real Grassmannians
(in which case the four parameters degenerate to one, but with diﬀ erent exponents), and
to dimensions of spherical irreducible representations associated to Grassmannians over
non-Archimedean local ﬁelds (in which case q degenerates to zero while the remaining
three parameters (a,b,t ) are specialized to q-independent values which are explicitly given
in terms of the cardinality of the residue ﬁeld). The latter case thus does not involve
degenerating the parameters ( a,b,t ), which is the reason to use the multivariable little q-
Jacobi polynomials with parameters ( q−1a,q−1b,t ) in the deﬁnition (2.4) of the generalized
dimensions.
We derive evaluation formulas forP L
λ in Section 6, which thus lead to explicit evaluations
of Dq(λ) = Dq(λ;a,b ;t) and to explicit evaluations of the (quantum) dimensions for the
irreducible spherical irreducible representations associated to diﬀ erent types of (quantum)
Grassmannians.
