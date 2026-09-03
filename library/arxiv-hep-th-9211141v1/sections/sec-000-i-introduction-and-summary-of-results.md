---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-000-i-introduction-and-summary-of-results
section_title: "INTRODUCTION AND SUMMARY OF RESULTS"
section_number: I
pages: 2-5
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
A. Introduction
In this paper we present new results for the level spacing distribution functions obtained
from scaling random matrix models of N ×N hermitian matrices at the edge of the support
of the (tree-level) eigenvalue densities when the parameters of the potential V are not “ﬁnely
tuned.” This universality class is already present in the Gaussian Unitary Ensemble. It is
known [3,10,20,23] that these distribution functions are expressible in terms of a Fredholm
determinant of an integral operator K whose kernel involves Airy functions.
It turns out that there are striking analogies between the properties of this Airy kernel
K(x, y) = A(x)A′(y) −A′(x)A(y)
x −y
where A(x) =
√
λ Ai(x), and the sine kernel
λ
π
sin π(x −y)
x −y
,
whose associated Fredholm determinant describes the classical level spacing distribution
functions ﬁrst studied by Wigner, Dyson, Mehta, and others [7,20,26].
To be a little more explicit about how these kernels arise we remind the reader that in
the GUE the probability density that the eigenvalues of a random N × N hermitian matrix
lie in inﬁnitesimal intervals about x1, · · ·, xN is given by [20]
PN(x1, · · ·, xN) = 1
N!det (KN(xi, xj))i,j=1,···,N
where
KN(x, y) =
N−1
X
k=0
ϕk(x)ϕk(y) .
Here {ϕk(x)} is the sequence obtained by orthonormalizing the sequence
n
xk exp(−x2)
o
2
over (−∞, ∞). More generally the n-point correlation function Rn(x1, · · ·, xn), which is
the probability density that n of the eigenvalues (irrespective of order) lie in inﬁnitesimal
intervals about x1, · · ·, xn, is given by
Rn(x1, · · · , xn) = det (KN(xi, xj))i,j=1,···,n
In particular R1(x), the density of eigenvalues at x, equals KN(x, x).
Replacing KN(x, y) by
1
R1(z)KN
 
z +
x
R1(z), z +
y
R1(z)
!
has the eﬀect of making the point z in the spectrum the new origin and rescaling so that
the eigenvalue density at this point becomes equal to 1. Now if z is ﬁxed then
R1(z) = KN(z, z) ∼1
π
√
2N
as N →∞, and
lim
N→∞
π
√
2N KN
 
z +
πx
√
2N , z +
πy
√
2N
!
= 1
π
sin π(x −y)
(x −y)
,
so we obtain the sine kernel in this way. (This limit is obtained by applying the Christoﬀel-
Darboux formula to KN(x, y) and then using the known asymptotics of ϕN(x) as N →∞.)
The “edge of the spectrum” corresponds to z ∼±
√
2N and one has there the scaling limit
[10,23]
lim
N→∞
1
21/2N1/6 KN
√
2N +
x
21/2N1/6 ,
√
2N +
y
21/2N1/6

= Ai(x)Ai′(y) −Ai′(x)Ai(y)
x −y
.
We now present some of the analogies which we have found.
(That such analogies
between properties of the sine kernel and Airy kernel exist is perhaps not suprising since
they are both scaling limits of the same family of kernels.)
The ﬁrst is the analogue of
the completely integrable system of P.D.E.’s of Jimbo, Miwa, Mˆori, and Sato [17] when the
underlying domain is a union of intervals. The second is the fact that in the case of the
semi-inﬁnite interval (s, ∞) (the analogue of a single ﬁnite interval for the sine kernel) the
3
Fredholm determinant is closely related to a Painlev´e transcendent of the second kind (the
ﬁfth transcendent arises for the sine kernel [17]). And the third is the existence of a second
order diﬀerential operator commuting with the Airy operator K. (The existence of such a
diﬀerential operator in the sine kernel case has been known for some time, see e.g. [14], page
201.) This last fact leads to an explicit asymptotic formula, as the interval (s, ∞) expands,
for the probability that it contains precisely n eigenvalues (n = 1, 2, . . .) (the analogue of
results in [2,31]). Here are our results, stated in some detail. (A short announcement appears
in [29].)
B. The System of Partial Diﬀerential Equations
We set
J =
m
[
j=1
(a2j−1, a2j)
and write D(J; λ) for the Fredholm determinant of K acting on J. We think of this as a
function of a = (a1, . . . , a2m). Then
da log D(J; λ) = −
2m
X
j=1
(−1)jR(aj, aj) daj
(1.1)
where R(x, y) is the kernel of the operator K(I−K)−1 and da denotes exterior diﬀerentiation
with respect to the aj’s. We introduce quantities
qj = (I −K)−1A(aj) ,
pj = (I −K)−1A′(aj) ,
(1.2)
(which are the analogue of the quantities r±j of [17]; see also [9,15,21,22]) as well as two
further quantities
u =

A, (I −K)−1A

,
v =

A, (I −K)−1A′
(1.3)
where the inner products refer to the domain J. Then the equations read
4
∂qj
∂ak
= (−1)k qjpk −pjqk
aj −ak
qk
(j̸ = k),
(1.4)
∂pj
∂ak
= (−1)k qjpk −pjqk
aj −ak
pk
(j̸ = k),
(1.5)
∂qj
∂aj
= −
X
k̸=j
(−1)k qjpk −pjqk
aj −ak
qk + pj −qju ,
(1.6)
∂pj
∂aj
= −
X
k̸=j
(−1)k qjpk −pjqk
aj −ak
pk + ajqj + pju −2qjv ,
(1.7)
∂u
∂aj
= (−1)jq2
j ,
(1.8)
∂v
∂aj
= (−1)jpjqj .
(1.9)
Moreover the quantities R(aj, aj) appearing in (1.1) are given by
R(aj, aj) =
X
k̸=j
(−1)k (qjpk −pjqk)2
aj −ak
+ p2
j −ajq2
j −2pjqju + 2q2
jv .
(1.10)
These equations are derived very much in the spirit of [28]; see also [9,15,21].
