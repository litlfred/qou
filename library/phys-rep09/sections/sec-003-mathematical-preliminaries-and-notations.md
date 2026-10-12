---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-003-mathematical-preliminaries-and-notations
section_title: "Mathematical preliminaries and notations"
section_number: null
pages: 6-9
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Here we collect, for the reader’s convenience, some mathematical expressions, terminology and notations which appear
most frequently in the text. Needless to say, we have made no attempt at being completely rigorous. We just try to facilitate
the casual reading of isolated sections.
As already mentioned, the natural mathematical habitat for most of the objects we will deal with in this report is a Lie
group, or its associated Lie algebra. Although most of the results discussed in these pages are valid in a more general setting,
we will essentially consider only matrix Lie groups and algebras.
By a Lie group G we understand a set which combines an algebraic structure with a topological one. At the algebraic level,
every two elements of G can be combined by an internal composition law to produce a third element, also in G. The law is
required to be associative, to have an identity element, and every element must have an inverse. The ordinary product and
the inverse of the invertible matrix, play that role in the cases we are more interested in. The topological exigence forces the
composition law and the association of an inverse to be sufficiently smooth functions.
S. Blanes et al. / Physics Reports 470 (2009) 151–238
157
A Lie algebra g is a vector space whose elements can be combined by a second law, the Lie bracket, which we represent
by [A, B] = C, with A, B, C elements of g, in such a way that the law is bilinear, skew-symmetric and satisfies the well known
Jacobi identity,
[A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0.
(8)
When dealing with matrices we take, as Lie bracket, the familiar commutator:
[A, B] = AB −BA,
A ∈g, B ∈g,
(9)
where AB stands for the usual matrix product. If we consider a finite-dimensional Lie algebra with dimension d and denote
by Ai, i = 1, . . . , d, the vectors of one of its bases, then the fundamental brackets one has to know are
[Ai, Aj] = ck
ijAk,
(10)
where sum over repeated indexes is understood. The coefficients ck
ij are the so-called structure constants of the algebra.
Associated with any A ∈g we can define a linear operator adA : g →g which acts according to
adA B = [A, B],
ad
j
AB = [A, ad
j−1
A
B],
ad0
AB = B,
j ∈N, B ∈g.
(11)
Also of interest, is the exponential of this adA operator,
AdA = exp(adA),
(12)
whose action on g is given by
AdA(B) = exp(A)B exp(−A) =
∞
X
k=0
1
k!
adk
AB,
B ∈g.
(13)
The type of matrices we will handle more frequently are orthogonal, unitary and symplectic. Here are their
characterization and the notation we shall use for their group and algebra.
The special orthogonal group, SO(n), is the set of all n × n real matrices with unit determinant satisfying ATA = AAT = I,
where AT is the transpose of A and I denotes the identity matrix. The corresponding algebra so(n) consists of the skew-
symmetric matrices.
A n × n complex matrix A is called unitary if AĎA = AAĎ = I, where AĎ is the conjugate transpose or Hermitian adjoint
of A. The special unitary group, SU(n), is the set of all n × n unitary matrices with unit determinant. The corresponding
algebra su(n) consists of the skew-Hermitian traceless matrices. Special relevance in some quantum mechanical problems
we discuss will have the case n = 2. In this case a convenient basis for su(2) is made up by the Pauli matrices
σ1 =

0
1
1
0

,
σ2 =

0
−i
i
0

,
σ3 =

1
0
0
−1

.
(14)
They satisfy the identity
σjσk = δjk + iϵjklσl,
(15)
and correspondingly
[σj, σk] = 2iϵjklσl,
(16)
which directly give the structure constants for SU(2). The following identities will prove useful for a and b in R3:
(a · σ)(b · σ) = a · b I + i(a × b) · σ,
[a · σ, b · σ] = 2i(a × b) · σ,
(17)
where we have denoted σ = (σ1, σ2, σ3). Any U ∈SU(2) can be written as
U = exp(ia · σ) = cos(a)I + i
sin(a)
a
a · σ,
(18)
where a = ∥a∥=
q
a2
1 + a2
2 + a2
3. A more elaborate expression which we shall make use of, in later sections, is (with a = 1)
exp(ia · σt)(b · σ) exp(−ia · σt) = b · σ + sin 2t (b × a) · σ + sin2 t(a × (b × a)) · σ.
(19)
In Hamiltonian problems, the symplectic group Sp(n) plays a fundamental role. It is the group of 2n × 2n real matrices
satisfying
ATJA = J,
with J =

On
In
−In
On

(20)
and In denotes the n-dimensional identity matrix. Its corresponding Lie algebra sp(n) consists of matrices verifying BTJ+JB =
O2n. In fact, these can be considered particular instances of the so-called J-orthogonal group, defined as [41]
OJ(n) = {A ∈GL(n) : ATJA = J},
(21)
158
S. Blanes et al. / Physics Reports 470 (2009) 151–238
where GL(n) is the group of all n × n nonsingular real matrices and J is some constant matrix in GL(n). Thus, one recovers
the orthogonal group when J = I, the symplectic group Sp(n) when J is the basic symplectic matrix given in (20), and the
Lorentz group SO(3, 1) when J = diag(1, −1, −1, −1). The corresponding Lie algebra is the set
oJ(n) = {B ∈gln(R) : BTJ + JB = O},
(22)
where gln(R) is the Lie algebra of all n × n real matrices. If B ∈oJ(n), then its Cayley transform
A = (I −αB)−1(I + αB)
(23)
is J-orthogonal.
Another important matrix Lie group not included in the previous characterization, is the special linear group SL(n),
formed by all n×n real matrices with unit determinant. The corresponding Lie algebra sl(n) comprises all traceless matrices.
For real 2 × 2 matrices in sl(2) one has
exp

a
b
c
−a

=


cosh(η) +
a
η
sinh(η)
b
η
sinh(η)
c
η
sinh(η)
cosh(η) −
a
η
sinh(η)


(24)
with η =
√
a2 + bc.
When dealing with convergence problems it is necessary to use some type of norm for a matrix. By such we mean a
non-negative real number ∥A∥associated with each matrix A ∈Cn×n and satisfying
(a) ∥A∥≥0 for all A and ∥A∥= 0 iff A = On.
(b) ∥αA∥= |α| ∥A∥, for all scalars α.
(c) ∥A + B∥≤∥A∥+ ∥B∥.
Quite often, one adds the sub-multiplicative property
∥AB∥≤∥A∥∥B∥,
(25)
but not all matrix norms satisfy this condition [42].
There exist different families of matrix norms. Among the more popular ones, we have the p-norm ∥A∥p and the Frobenius
norm ∥A∥F. For a matrix A with elements aij, i, j = 1 . . . n, they are defined as
∥A∥p = max
∥x∥p=1 ∥Ax∥p
(26)
∥A∥F =
v
u
u
t
n
X
i=1
n
X
j=1
|aij|2 =
p
tr(AĎA),
(27)
respectively, where ∥x∥p = (Pn
j=1 |xj|p)
1
p and tr(A) is the trace of the matrix A. Although both verify (25), the p-norms have
the important property that for every matrix A and x ∈Rn one has ∥Ax∥p ≤∥A∥p ∥x∥p. The most used p-norms correspond
to p = 1, p = 2 and p = ∞.
Of paramount importance in numerical linear algebra is the case p = 2. The resulting 2-norm of a vector is nothing but
the Euclidean norm, whereas in the matrix case it is also called the spectral norm of A and can be characterized as the square
root of the largest eigenvalue of AĎA. A frequently used inequality relating to Frobenius and spectral norms is the following:
∥A∥2 ≤∥A∥F ≤√
n ∥A∥2.
(28)
In fact, this last inequality can be made more stringent [43]:
∥A∥F ≤
p
rank(A) ∥A∥2.
(29)
Considering in a matrix Lie algebra g a norm satisfying property (25), it is clear that ∥[A, B]∥≤2∥A∥∥B∥, and the ad
operator defined by (11) is bounded, since
∥adA∥≤2∥A∥
for any matrix A.
A matrix norm is said to be unitarily invariant if ∥UAV∥= ∥A∥whenever U, V are unitary matrices. Frobenius and
p-norms are both unitarily invariant [44].
In some of the most basic formulas for the Magnus expansion, there will appear the so-called Bernoulli numbers Bn,
which are defined through the generating function [45]
tezt
et −1 =
∞
X
n=0
Bn(z)
tn
n!,
|t| < 2π
S. Blanes et al. / Physics Reports 470 (2009) 151–238
159
as Bn = Bn(0). Equivalently,
x
ex −1 =
∞
X
n=0
Bn
n!
xn,
whereas the formula
ex −1
x
=
∞
X
n=0
1
(n + 1)!
xn
will be also useful in the sequel. The first few nonzero Bernoulli numbers are B0 = 1, B1 = −1
2, B2 = 1
6, B4 = −1
30. In general
one has B2m+1 = 0 for m ≥1.
