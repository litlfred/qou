---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-018-exact-methods
section_title: "Exact methods"
section_number: null
pages: 36-39
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
As long as we consider only systems with a few particles, we can use the Lanczos/ Arnoldi algorithm [95,
96] for sparse matrices to solve the eigenvalue problem. Afterward, we have the energy and the wave
function of the system and use this information for the calculation of binding energies and phase shifts.
The Lanczos algorithm works as the following.
A general eigenvalue problem reads
A·v =λ·v, (3.38)
where A is a n× n matrix,λ is the eigenvalue andv is the eigenvector which can be rewritten in the basis
of the power-iterated subspace, {
q, Aq, A2q, A3q,...
}
, (3.39)
where q is an arbitrary starting vector. Hence, we could use a ﬁnite number of m vectors based
on Eq. (3.39) to orthogonally transform the matrix A into a Hessenberg matrix Hm, from which the
eigenvalues and -vectors are calculated faster than for a general matrix. Admittedly, the aforementioned
arguments of Eq. (3.39) do not have to be orthogonal. After orthogonalization, the basis is given by
p1,..., pm and applied to the general matrix A, we get the m× m Hessenberg matrix, where all entries
below the ﬁrst subdiagonal are equal to zero. It is of the form
Hm =

h1,1 h1,2 ... h1,m
h2,1 h22 ... h2,m
0 h3,2 ... h3,m
0 0 ... h4,m
...
... hm,m

, (3.40)
and it is an similarity transformation of the original matrix A in the ﬁrst m arguments. In the case of a
real symmetric matrix A, Eq. (3.40) reduces to a tridiagonal matrix which can be evaluated even faster.
As we work with ﬁnite m, the eigenvectors and -values are only an approximation of the exact solution,
making it necessary to iterate the procedure until the desired precision is reached. Generally, we only
have to perform a matrix-vector multiplication and we have to store the vectors p1,..., pm as well as
the matrix Hm. This is particularly eﬃcient for very sparse matrices, where most of the entries are zero
and as such do not contribute to the calculation. Using a large enough basis and enough iterations it is
also possible to calculate more than one eigenvalue which is particularly important for the calculation of
phase shifts where one needs eigenvalues corresponding to a large range of energy.
30
3.6 The auxiliary ﬁeld partition function
3.6 The auxiliary ﬁeld partition function
Generally, we use three diﬀerent methods to extract physical observables. While we use the Hamiltonian
formalism and the transfer matrix formalism for the exact calculations, we use a Grassmann path integral
formalism with auxiliary ﬁelds in the case of Monte Carlo simulations. In the following we will show
that all formalisms are equivalent up to higher order lattice artifacts. In the current and the subsequent
section we follow [97, 98]. For the proof we consider a system of two fermions with spin↑ and↓ and a
simple contact interaction∝ C. On the one hand, the corresponding path integral reads
Z =
∫
Dc Dc∗ exp[−S (c, c∗)], (3.41)
with the action
S (c, c∗) = S free
(c, c∗) + Cαt
∑
⃗n,nt
c∗
↑
(⃗n, nt
) c↑
(⃗n, nt
) c∗
↓
(⃗n, nt
) c↓
(⃗n, nt
). (3.42)
Here,αt is the ratio of the spatial and temporal lattice spacings,αt = a/at. The free part reads
S free
(c, c∗) =
∑
⃗n,nt,i=↑,↓

[c∗
i
(⃗n, nt
) ci
(⃗n, nt + 1)− (1− 6h)c∗
i
(⃗n, nt
) ci
(⃗n, nt
)]
+
∑
ˆl=1,2,3
[
c∗
i
(⃗n, nt
) ci
(
⃗n + ˆl, nt
)
+ c∗
i
(⃗n, nt
) ci
(
⃗n− ˆl, nt
)]
,
(3.43)
with h =αt/(2m) . Eq. (3.43) represents the most simple discretization of the free action. On the other
hand, the discrete Hamiltonian reads
H =
∑
⃗n,i=↑,↓

3
m a†
i
(⃗n) ai
(⃗n)− 1
2m
∑
ˆl=1,2,3
[
a†
i
(⃗n) ai
(
⃗n + ˆl
)
+ a†
i
(⃗n) ai
(
⃗n− ˆl
)]

+ C
∑
⃗n
a†
↑(⃗n )a↑(⃗n )a†
↓(⃗n )a↓(⃗n ).
(3.44)
Using the general properties of Grassman variables and anticommutation relations (see App. A.3 for
details), one can proof the following identity
Tr
[
: f
(
a†, a
)
:
]
=
∫
dc (0) dc∗ (0) exp{c∗ (0) [c (0)− c (1)]} f [c∗ (0), c (0)], (3.45)
where the antiperiodic boundary condition in time direction is realized by c(1) =−c(0).
The previous equation shows the connection only for one time slice, but it is extendable to the general
identity,
Tr
{
: FLt−1
[
a†
i′
(
⃗n′)
, ai
(⃗n)]
: ... : F0
[
a†
i′
(
⃗n′)
, ai
(⃗n)]
:
}
=
∫
Dc Dc∗ exp

Lt−1∑
nt=0
∑
⃗n,i
[c∗
i
(⃗n, nt
) ci
(⃗n, nt
)− ci
(⃗n, nt + 1)]

Lt−1∏
nt=0
Fnt
[
c∗
i′
(
⃗n′, nt
)
, ci
(⃗n, nt
)]
.
(3.46)
31
Chapter 3 Nuclear Lattice E ﬀective Field Theory
Now the antiperiodic boundary condition reads ci(⃗n, Lt) =−ci(⃗n, 0). Identifying F j[a†
i′(⃗n′), ai(⃗n )] with
the transfer matrix
M =: exp (−αtH) : , (3.47)
and the terms in the second line of Eq. (3.46) with the action of Eq. (3.42) we have shown the equality
between path integral and transfer matrix partition function,
Z = Tr
(
MLt
)
. (3.48)
Using a Gaussian quadratic and completing the square, the path integral is rewritten as
Z =
∏
⃗n,nt
[∫
dAs(⃗n, nt
)]∫
Dc Dc∗ exp[−S A
(c, c∗, s)], (3.49)
with the new action including the auxiliary ﬁeld,
S A
(c, c∗, s) = S free
(c, c∗)−
∑
⃗n,nt
A[s(⃗n, nt
)]ρ(⃗n, nt
). (3.50)
The auxiliary ﬁeld integral reads [99, 100]
∫
dAs(⃗n, nt
) = 1
2π
∫ ∞
−∞
ds(⃗n, nt
) exp
[
−1
2 s2 (⃗n, nt
)]
, (3.51)
A[s(⃗n, nt
)] =
√
−Cαt s(⃗n, nt
). (3.52)
The above written form is also known as Hubbard-Stratonovich transformation. In general, there are
plenty of alternative forms of Eqs (3.51) and (3.52) for the auxiliary ﬁeld which must fulﬁll the following
equations,
∫
dAs(⃗n, nt
) = 1, (3.53)
∫
dAs(⃗n, nt
) A[s(⃗n, nt
)] = 0, (3.54)
−Cαt =
∫
dAs(⃗n, nt
) A2 [s(⃗n, nt
)]. (3.55)
Some of them are investigated in [101]. Eqs. (3.41) and (3.49) are equivalent but the two-body interaction
is removed making the explicit calculation faster as the theory only consists of one-nucleon states which
do not interact with each other but only via an auxiliary ﬁeld. After showing the equivalence of the
Hamiltonian transfer matrix method and the path integral with and without auxiliary ﬁeld, the appropriate
method depends on the problem. For many-body problems the only feasible way is to choose the path
integral with auxiliary ﬁeld formulation.
This method is extended to all LO smeared contact interaction as well as the one-pion exchange which
we will be included in the subsequent calculations as well. As we already see, each operator requires
an extra auxiliary ﬁeld making it computationally expensive to include NLO operators in the partition
function too.
32
