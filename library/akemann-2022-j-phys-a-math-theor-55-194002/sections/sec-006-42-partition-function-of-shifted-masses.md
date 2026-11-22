---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-006-42-partition-function-of-shifted-masses
section_title: "Partition function of shifted masses"
section_number: 4.2
pages: 16-20
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
In order to determine the second partition function Z( 
Nf)
2,n−k−1({#m}) with an extended number of
shifted masses (41), which are partly degenerate, we will use the following theorem from [44].
It expresses the expectation value of the product of characteristic polynomials in several equiv-
alent forms, in terms of the determinant of a matrix of kernels and orthogonal polynomials.
Adapted to our setting of the χGUE, it reads for K ⩾L
15
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
1
Z(0)
ν,n

[0,∞)n
n

j=1

dy jy2ν+1
j
e−y2
j
K

k=1
(v2
k −y2
j)
L

l=1
(u2
l −y2
j)

Δn({y2})2
=
 n+L−1
j=n
ˆh j
ΔK({v2})ΔL({u2}) det

K(χGUE)
ν,n+L (v2
a, u2
b)
++++(L(ν)
n+L(v2
a), . . . , (L(ν)
n+K−1(v2
a)

a=1,...,K
b=1,...,L
. (58)
Notice that in [44] the expression on the right-hand side is given here in terms of orthogonal
polynomials in monic normalisation and their norms (47). The point is that we may split the
K + L characteristic polynomials or masses in two groups as we like, resulting in many equiv-
alent forms of determinants of different size. In [44], valid for Hermitian and non-Hermitian
ensembles of random matrices, this split was introduced when considering the product of K
characteristic polynomials and L complex conjugated ones in the non-Hermitian case.
Considering the $
Nf new masses in (41), it is unavoidable to apply l’Hôpital’s rule to the ν-
fold degenerate mass xk + s. However, some simplification can be achieved by dividing the k
two-fold degenerate masses into the two groups of characteristic polynomials with parameters
{v2} and {u2}, thus choosing K = Nf + ν + k and L = k in (58). Before taking into account
this degeneracy,let us take one more step of preparation,in sending v2
i →−v2
i and u2
j →−u2
j in
(58), to achievethe correctsigns in the mass terms, by switching polynomialsand kernels inside
the determinant, and by moving from monic to standard generalised Laguerre polynomials
(−1)n(K+L)

[0,∞)n
n

j=1

dy jy2ν+1
j
e−y2
j
K

k=1
(v2
k + y2
j)
L

l=1
(u2
l + y2
j)

Δn({y2})2
= (−1)L(K−L)+(K−L)(n+L+(K−L−1)/2)n! n+L−1
j=0
j!( j+ν)!
2
 n+K−1
l=n+L l!
(−1)
K(K−1)
2
+ L(L−1)
2
ΔK({v2})ΔL({u2})
× det

L(ν)
n+L(−v2
a), . . . , L(ν)
n+K−1(−v2
a)
++++K(χGUE)
ν,n+L (−v2
a, −u2
b)

a=1,...,K
b=1,...,L
,
(59)
where we have multiplied by (55). Regarding the degeneracy of some of the parameters v j, it is
not difficult to see that for any set of suitably differentiable functions f1, . . . , fν, the following
limit applies:
lim
z1,...,zν→x
1
Δν({z}) det [fa(zb)]a,b=1,...,ν =
ν−1

j=0
1
j! det [f (b−1)
a
(x)]a,b=1,...,ν,
(60)
where f (b)
a (x) denotes the bth derivative with respect to the argument. The size of the deter-
minant can be trivially extended, as long as the first ν rows depend in the same way on the
arguments zb and thus become degenerate in the limit.
Let us turn to the evaluation of the partition function Z( 
Nf)
2,n−k−1({m}). In order to apply (59),
we split the #Nf = Nf + ν + 2k masses into two sets, which is born out of (41),
16
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
v1 = · · · = vν = xk + s ≡#s;
vν+ j =
"
m2
f + (xk + s)2 ≡#m f
for f = 1, . . . , Nf;
vν+Nf+ j = u j =
"
(xk + s)2 −x2
j ≡#x j
for j = 1, . . . , k.
(61)
Notice that in the last term for j = k, we obtain
vν+Nf+k = uk =

s(2xk + s) = #xk,
(62)
which is proportional to √s. These are the variables that will appear inside the polynomials
and kernels on the right-hand side of (59). In the Vandermonde determinants of parameters
{u2} and {v2}, due to their translational invariance, the following simplifications occur:
Δk({u2}) = (−1)
k(k−1)
2
Δk({x2}),
(63)
and
ΔNf+ν+k({v2}) = Δν(v2
1, . . . , v2
ν)ΔNf+k(v2
ν+1, . . . , v2
ν+Nf+k)
ν
i=1
Nf+k

j=1
(v2
ν+ j −v2
i ),
(64)
with
ΔNf+k(v2
ν+1, . . . , v2
ν+Nf+k) = (−1)
k(k−1)
2
+NfkΔNf({m2})Δk({x2})
k
j=1
Nf

f=1
(m2
f + x2
j),
ν
i=1
Nf+k

j=1
(v2
ν+ j −v2
i ) = (−1)νk
Nf

f=1
m2ν
f
k
j=1
x2ν
j .
(65)
In the last line, we have already applied the degeneracy of the first ν masses. Before taking the
degenerate limit of the first ν parameters vi, we multiply the first ν rows of the determinant
by #s4 for later convenience, and thus divide the pre-factor by #s4ν. Putting all this together, we
obtain the following expression for the partition function of #Nf shifted masses with n −k −1
eigenvalues and two zero-modes
(66)
Notice that all factors of (−1) have cancelled, and we recall the definition (61). In the same
way as we simplified (54) to (57), in order to prepare the large-n limit, we can apply here (56)
17
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
to modify the first Nf + ν column as follows:
(67)
Now, the leading order asymptoticno longerleads to degeneratecolumns.In a final step, we can
carry out the derivatives, where we employ another recurrence relation [45, equation (8.971.3)]
(∂z −1)zνL(ν)
j (z) = (j + 1)zν−1L(ν−1)
j+1 (z),
(68)
applied to z →−#s2. We would like to point out the subtlety that, to be applicable, the power in
zν and the order of the generalised Laguerrepolynomialsν have to agree. This is the reason why
we multiplied with#s4 in one of the previous steps. After differentiation the power and order are
lowered by one unit, which allows to iterate. Therefore,we recombinethe first ν rows beginning
from the highest derivative, so that we obtain shifted derivative operators, (1 + ∂˜s2)a−1 instead
of ∂a−1
˜s2 , making (68) in z →−#s2 applicable. We evaluate
(1 + ∂˜s2)a−1#s2d+2L(d+1)
n−1 (−#s2) = (n + a −2)!
(n −1)!
#s2(d−a+2)L(d−a+2)
n+a−2 (−#s2),
(69)
for the Laguerre polynomials, and for the kernel (49)

1 + ∂˜s2
a−1#s4K(χGUE)
2,n−1 (−#s2, −#xe) =
n−2
'
j=0
2(j + a −1)!
(j + 2)!
#s2(3−a)L(3−a)
j+a−1(−#s2)L(2)
j (−#x2
e)
= #s4 (n + a −2)!
(n −1)!
#K(a−1)
2,n−1(−#s2, −#x2
e).
(70)
In the last line, we have defined
#K(a−1)
2,n−1(−#s2, −#x2
e) =
(n −1)!
(n + a −2)!
n−2
'
j=0
2(j + a −1)!
(j + 2)!
#s2(1−a)L(3−a)
j+a−1(−#s2)L(2)
j (−#x2
e),
(71)
which includes the original kernel for a = 1, #K(0)
2,n−1(−#s2, −#x2
e) = K(χGUE)
2,n−1 (−#s2, −#x2
e). In such
a way, the factors #s4 and factorials in (69) and (70) can be pulled out of the first ν rows of the
determinant in (67), and we obtain as the final answer for the partition function
(72)
18
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
