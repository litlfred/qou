---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-003-mathematical-preliminaries-and-notations
section_title: "Mathematical preliminaries and notations"
section_number: null
pages: 6-9
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Here we collect, for the reader’s convenience, some mathematical expressions, terminology and notations which appear
most frequently in the text. Needless to say, we have made no attempt at being completely rigorous. We just try to facilitate
the casual reading of isolated sections.

As already mentioned, the natural mathematical habitat for most of the objects we will deal with in this report is a Lie
group, or its associated Lie algebra. Although most of the results discussed in these pages are valid in a more general setting,
we will essentially consider only matrix Lie groups and algebras.

By a Lie group § we understand a set which combines an algebraic structure with a topological one. At the algebraic level,
every two elements of § can be combined by an internal composition law to produce a third element, also in ¢. The law is
required to be associative, to have an identity element, and every element must have an inverse. The ordinary product and
the inverse of the invertible matrix, play that role in the cases we are more interested in. The topological exigence forces the
composition law and the association of an inverse to be sufficiently smooth functions.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 157

A Lie algebra g is a vector space whose elements can be combined by a second law, the Lie bracket, which we represent
by [A, B] = C, with A, B, C elements of g, in such a way that the law is bilinear, skew-symmetric and satisfies the well known
Jacobi identity,

[A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0. (8)
When dealing with matrices we take, as Lie bracket, the familiar commutator:

[A,B] =AB—BA, A€g,Beg, (9)
where AB stands for the usual matrix product. If we consider a finite-dimensional Lie algebra with dimension d and denote
by Aj, i = 1, ..., d, the vectors of one of its bases, then the fundamental brackets one has to know are

(Aj, Ail = cfAx, (10)

where sum over repeated indexes is understood. The coefficients ch are the so-called structure constants of the algebra.
Associated with any A € g we can define a linear operator ad, : g > g which acts according to

ad,B=[A,B], ad,B=[A,ad/-'B],  ad°B=B, jeEN,Beg. (11)
Also of interest, is the exponential of this ad, operator,
Ada = exp(ada), (12)
whose action on g is given by
oo
Vix
Ada(B) = exp(A)Bexp(—A) = > pas, Bes. (13)

The type of matrices we will handle more frequently are orthogonal, unitary and symplectic. Here are their
characterization and the notation we shall use for their group and algebra.

The special orthogonal group, SO(n), is the set of all n x n real matrices with unit determinant satisfying A'A = AA™ = I,
where A! is the transpose of A and I denotes the identity matrix. The corresponding algebra so(n) consists of the skew-
symmetric matrices.

An x ncomplex matrix A is called unitary if A‘'A = AAT = I, where At is the conjugate transpose or Hermitian adjoint
of A. The special unitary group, SU(n), is the set of all n x n unitary matrices with unit determinant. The corresponding
algebra su(n) consists of the skew-Hermitian traceless matrices. Special relevance in some quantum mechanical problems
we discuss will have the case n = 2. In this case a convenient basis for su(2) is made up by the Pauli matrices

o1= (! s) ; = (; rn) : o3= (; ) : (14)

They satisfy the identity

GOK = Sik + ie, (15)
and correspondingly

[oj, on] = igor, (16)
which directly give the structure constants for SU(2). The following identities will prove useful for a and b in R?:

(a-o)(b-o) =a-b!I+i(ax b)-o, [a-o,b-o] = 2i(a x b)-o, (17)
where we have denoted o = (04, 02, 03). Any U € SU(2) can be written as

sin(a)

U = exp(ia- 0) = cos(a)I +i a-o, (18)

where a = |lal| = /@e + as + a. Amore elaborate expression which we shall make use of, in later sections, is (with a = 1)

exp(ia- ot)(b- 0) exp(—ia- ot) = b-o + sin2t (bx a)-o+ sin’ t(a x (bx a))- 0. (19)
In Hamiltonian problems, the symplectic group Sp(n) plays a fundamental role. It is the group of 2n x 2n real matrices
satisfying
AYA=J, withy= (Or fn (20)
=—In On
and I, denotes the n-dimensional identity matrix. Its corresponding Lie algebra sp(n) consists of matrices verifying B'J+JB =
O2,. In fact, these can be considered particular instances of the so-called J-orthogonal group, defined as [41]

O,(n) = {A € GL(n) : AYA = J}, (21)
158 S. Blanes et al. / Physics Reports 470 (2009) 151-238

where GL(n) is the group of all n x n nonsingular real matrices and J is some constant matrix in GL(n). Thus, one recovers
the orthogonal group when J = I, the symplectic group Sp(n) when J is the basic symplectic matrix given in (20), and the
Lorentz group SO(3, 1) whenJ = diag(1, —1, —1, —1). The corresponding Lie algebra is the set

oj(n) = {B € gl,(R) : BJ + JB = 0}, (22)

where gl, (RR) is the Lie algebra of all n x n real matrices. If B € 0,(n), then its Cayley transform

A= (I —a@B)~'(I + aB) (23)

is J-orthogonal.

Another important matrix Lie group not included in the previous characterization, is the special linear group SL(n),
formed by all n x nreal matrices with unit determinant. The corresponding Lie algebra s{(n) comprises all traceless matrices.
For real 2 x 2 matrices in s{(2) one has

(24)

b
cosh(7) + 4 sinh(n) — sinh(n)
a b n n
exp |. a)=

© sinh) cosh(n) — = sinh(n)
ri 7

with n = Ja’ + be.
When dealing with convergence problems it is necessary to use some type of norm for a matrix. By such we mean a
non-negative real number ||A|| associated with each matrix A € C’*" and satisfying

(a) ||Al| = 0 for all A and ||Al| = 0 iffA = O,.
(b) ||oAl| = || ||Al], for all scalars a.
(c) ||A+ Bl] < |All + IIBI).

Quite often, one adds the sub-multiplicative property
ABI] < All IIBIl, (25)

but not all matrix norms satisfy this condition [42].
There exist different families of matrix norms. Among the more popular ones, we have the p-norm ||Al|, and the Frobenius
norm ||All-. For a matrix A with elements aj, i,j = 1...n, they are defined as

Ally = max |AX|lp (26)

[x\|p=1

YY tail? = Vtraia), (27)

i=1 j=1

Alle =

respectively, where ||x||) = (er Ixj[P)? and tr(A) is the trace of the matrix A. Although both verify (25), the p-norms have
the important property that for every matrix A and x € R" one has ||Ax||p < ||Allp ||X/lp. The most used p-norms correspond
top=1,p=2andp=o.

Of paramount importance in numerical linear algebra is the case p = 2. The resulting 2-norm of a vector is nothing but
the Euclidean norm, whereas in the matrix case it is also called the spectral norm of A and can be characterized as the square
root of the largest eigenvalue of AtA. A frequently used inequality relating to Frobenius and spectral norms is the following:

IIAll2 < llAlle < Vn [lAll2. (28)
In fact, this last inequality can be made more stringent [43]:

|Alle < yrank(A) [[All2- (29)

Considering in a matrix Lie algebra g a norm satisfying property (25), it is clear that ||[A, B]|| < 2\|Al|||B|], and the ad
operator defined by (11) is bounded, since

lladal] < 2||Al|

for any matrix A.

A matrix norm is said to be unitarily invariant if || UAV|| = ||A|| whenever U, V are unitary matrices. Frobenius and
p-norms are both unitarily invariant [44].

In some of the most basic formulas for the Magnus expansion, there will appear the so-called Bernoulli numbers B,,
which are defined through the generating function [45]

teZ! ic2] t"
= DEBS. Itl < 2
n=0 .

et
S. Blanes et al. / Physics Reports 470 (2009) 151-238 159

as B, = B,(0). Equivalently,

°0

whereas the formula
e-1 << 1

x “= (n+ 1)!

n

x

will be also useful in the sequel. The first few nonzero Bernoulli numbers are Bp = 1, By; = — 1B= Z. Ba=— + In general
one has Bym;1 = 0 form > 1.
