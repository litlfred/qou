---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-008-b-consistency-checks-of-the-partition-function-a
section_title: "B Consistency checks of the partition function and factorisation"
section_number: null
pages: 20-22
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Consistency checks of the partition function and factorisation
In this appendix we perform a few consistency checks of the eigenvalue representation of the partition
function eq. (3.15). For simplicity we will set m = 0 and Nf = 0 here. The antisymmetric weight eq.
(3.16) thus reduces to
F(x)|m=0 = 2 e
x2(1−a2)
8a2
erf
x
√
1 −a2
2
√
2a2

.
(B.1)
B.1
The GUE limit a →1 for ν = 0
On the level of the distribution eq. (2.2) it is clear that the matrix W gets suppressed for a →1.
After reducing to eigenvalues the same result should come out. Here we will look at the simplest case
only, that is ν = 0. We can insert the simpliﬁcation eq. (B.1) into eq. (3.17) at ν = 0. Noting that in
the limit a →1 the exponential factor in eq. (B.1) reduces to unity, we can use the following result of
[28] (see end of section 3 in the ﬁrst paper) for the limit of a Pfaﬃan of an error-function,
lim
a→1 Pf1≤i,j≤2n
"
erf
 
(di −dj)
r
(1 −a2)
8a2
!#
∼∆2n({d}) .
(B.2)
This provides the second Vandermonde determinant in eq. (3.17) to constitute the GUE, and we
arrive at
lim
a→1 Z(Nf =0)
ν=0
|m=0 ∼
Z ∞
−∞
N
Y
j=1
ddj dNf
j
exp
h
−
d2
j
4
i
∆N({d})2 .
(B.3)
20
B.2
The chGUE limit a →0 and factorisation
Here we would like to perform a more detailed check. As it was shown in [21] in the large-N limit
the spectral density of the Hermitian Wilson Dirac operator behaves like the density of a ﬁnite GUE-
matrix of size ν×ν plus the microscopic chGUE density. We therefore expect that our general partition
function will factorise in the limit a →0 into a ﬁnite GUE times a second chGUE partition function
of the remaining 2n eigenvalues.
In order to show that we will ﬁrst simplify Z(0)
ν
further before using the de Bruijn integration
theorem. Taking eq. (3.13) as a starting point we can use the fact that the jpdf integrated over all
variables is totally symmetric under exchange or relabeling of the dj 4. We can split the variables
into two sets, denoted by tj=1,...,ν ≡dj=1,...,ν, and sj=1,...,2n ≡dj=ν+1,...,2n+ν. If we do a Laplace
expansion of the determinant into blocks of sizes 2n × 2n and ν × ν, we can split oﬀa Vandermonde
type determinant in the variables tj, after appropriately relabeling all other permutations:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
νY
i=1
(sj −ti) ∆2n({s})
(B.4)
×
Z ∞
0
n
Y
b=1
dube
−u2
b
2a2(1−a2)

e
s1u1
2a2 . . . e
s1un
2a2
e−s1u1
2a2 . . . e−s1un
2a2
· · ·
· · ·
e
s2nu1
2a2 . . . e
s2nun
2a2
e−s2nu1
2a2 . . . e−s2nun
2a2

1
t1
· · ·
tν−1
1
· · ·
· · ·
· · ·
· · ·
1
tν
· · ·
tν−1
ν

.
We can now perform the integrations over u1, . . . , un with the help of the standard de Bruijn inte-
gral formula eq. (3.14). To make it applicable we can simply multiply the weight factors into the
determinant, and we obtain the following result:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})2
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
ν
Y
i=1
(sj −ti)∆2n({s})Pf1≤i,j≤2n [F(si −sj)].(B.5)
In eq. (B.5) we can make further use of the symmetry under relabeling of the variables sj and the
anti-symmetry of the Vandermonde determinant to write the Pfaﬃan as the following product:
Z(0)
ν
∼
Z ∞
−∞
ν
Y
j=1
dtj e−
t2
j
4a2 ∆ν({t})2
Z ∞
−∞
2n
Y
j=1
dsj e−
s2
j
4a2
ν
Y
i=1
(sj −ti) ∆2n({s})
n
Y
k=1
F(s2k −s2k−1). (B.6)
Now consider the exponents of two consecutive variables, say s1 and s2, from the Gaussian and the
exponential part of F:
exp
h
−s2
1 + s2
2
4a2
+ (s2 −s1)2(1 −a2)
8a2
i
= exp
h
−(s1 + s2)2
8a2
−(s1 −s2)2
8
i
.
(B.7)
In the limit a →0 the ﬁrst term on the right hand side will give a delta-function, whereas the second
Gaussian term remains:
lim
a→0
√
8a2π exp
h
−(s1 + s2)2
8a2
−(s1 −s2)2
8
i
= δ(s1 + s2) e−s2
1/2 .
(B.8)
In the same limit the error-function in eq. (B.1) becomes the sign function (see e.g. [28]),
lim
a→0 erf
h
(s2 −s1)
r
(1 −a2)
8a2
i
= sign[s2 −s1] .
(B.9)
4Using this symmetry our manipulations from now on will not be valid in general for correlation functions.
21
We are now ready to take the limit a →0 of the partition function eq. (B.6). We ﬁrst formally
change variables rj = tj/a to isolate the a-dependence, and then take the limit only on the remaining
a-dependence, that is the variables rj,
lim
a→0 Z(0)
ν
∼
Z ∞
−∞
νY
j=1
drj e−
r2
j
4 ∆ν({r})2
Z ∞
−∞
n
Y
j=1
dsj sjsign[sj] exp
h
−
s2
j
2
i νY
i=1
(s2
j −a2r2
i ) ∆n({s2})2.
(B.10)
We have used the fact that for s2k →−s2k−1 we obtain ∆2n({s}) →Qn
i=1 2si ∆n({s2})2. The variables
rj thus act as mass terms to the s-variables, but to leading order these masses can be neglected, leading
to a complete decoupling of variables. Our ﬁnal result is thus reading
Z ∞
−∞
νY
j=1
drj exp
h
−
r2
j
4
i
∆ν({r})2
Z ∞
−∞
n
Y
j=1
dsj |sj|2ν+1 exp
h
−
s2
j
2
i
∆n({s2})2,
(B.11)
where the ν would-be zero-eigenvalues at a = 0 have decoupled into a GUE of size ν, times the
standard massless chGUE with exactly ν zero eigenvalues. However, we should remember that due to
rescaling the original variables tj are all of the order O(a).
It is clear how to this order of approximation the microscopic spectral density would look like:
it is the superposition of a ﬁnite-ν semi-circle from the GUE and the Bessel spectral density with
ν zero-eigenvalues from the chGUE. This conﬁrms the analysis of [21] on the level of the partition
function, to that order.
