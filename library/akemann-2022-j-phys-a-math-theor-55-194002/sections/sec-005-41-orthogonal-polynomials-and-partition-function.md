---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-005-41-orthogonal-polynomials-and-partition-function
section_title: "Orthogonal polynomials and partition function"
section_number: 4.1
pages: 14-16
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
To compute the partition functions Z(Nf)
ν,n ({m}) and Z( 
Nf)
2,n−k−1({#m}) of the χGUE with a given
number of flavours, we begin with the χGUE at Nf = 0, where the partition function and all k-
point correlation functions can be expressed in terms of the generalised Laguerre polynomials
and their kernel. Their orthogonality relation with squared norms h j reads [40, table 18.3.1]
 ∞
0
dz L(ν)
l (z2)L(ν)
j (z2)z2ν+1e−z2 = h jδl j,
h j = (j + ν)!
j! 2
,
(45)
13
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
valid for ν > −1 for convergence. Here [40, equation (8.5.12)]
L(ν)
j (z) =
j
'
l=0
(j + ν)!
j!(j −l)!Γ(ν + l + 1)(−z)l,
(46)
is the definition of the generalised Laguerrepolynomialsin their standard normalisation.Notice
that in this definition the parameter ν can be continued to negative integer values, meaning that
the sum will be cut off from below, to start at l > −ν only. For later convenience we also
introduce generalised Laguerre polynomials in monic normalisation, (L(ν)
n (z) = zn + O(zn−1),
with its corresponding norms
ˆL(ν)
n (z) = (−1)n n! L(ν)
n (z),
ˆhj = j!(j + ν)!/2.
(47)
The corresponding kernel determines all k-point correlation functions of the χGUE with
Nf = 0 through (2) at finite-n,
Rk,n(x1, . . . , xk) =
k
c=1
x2ν+1
c
e−x2c det [K(χGUE)
ν,n
(x2
a, x2
b)]a,b=1,...,k.
(48)
In contrast to section 2, we use here squared variables for the (pre-)kernel K(χGUE)
ν,n
(x2
a, x2
b), as
we later have to differentiate with respect to these. Also note that we have not included the
weight function into the kernel. It only contains the orthogonal polynomials and is given by
K(χGUE)
ν,n
(x2
1, x2
2) =
n−1
'
j=0
2
j!
(j + ν)!L(ν)
j (x2
1)L(ν)
j (x2
2)
= 2
n!
(n + ν −1)!
L(ν)
n−1(x2
1)L(ν)
n (x2
2) −L(ν)
n (x2
1)L(ν)
n−1(x2
2)
x2
1 −x2
2
,
(49)
where in the second equality we have used the Christoffel–Darboux identity for x1̸ = x2, see
[40, equation 18.2.12]. Note that the determinant (48) is invariant under a rescaling of the
kernel K(x2
a, x2
b) →g(x2
a)/g(x2
b) K(x2
a, x2
b) for any non-zero function g(x). Two kernels related
in this way are called equivalent kernels, leading to the same k-point correlation functions and,
thence, the same spectral statistics.
When x1 = x2 = x we need to apply l’Hôpital’s rule to (49), cf [40, equation 18.2.13],
K(χGUE)
ν,n
(x2, x2) = 2
n!
(n + ν −1)!

L(ν+1)
n−1 (x2)L(ν)
n−1(x2) −L(ν+1)
n−2 (x2)L(ν)
n (x2)

,
(50)
upon using [40, equation (18.9.23)]
∂zL(ν)
j (z) = −L(ν+1)
j−1 (z),
(51)
in terms of squared variables. The recurrence relation [40, equation (18.9.13)],
L(ν)
j (z) = L(ν+1)
j
(z) −L(ν+1)
j−1 (z),
(52)
14
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
is employed to bring (50) into the form
K(χGUE)
ν,n
(x2, x2) =
n!
(n + ν −1)!2

L(ν)
n (x2)L(ν)
n−1(x2) −L(ν+1)
n−1 (x2)L(ν−1)
n
(x2)

.
(53)
In this form, compared to (50), the leading order asymptotic of the Laguerre polynomials
for large-n is no longer cancelling and thus non-vanishing. Equation (53) implies in partic-
ular the following expression for the spectral density at finite matrix dimension n, R1,n(x) =
x2ν+1e−x2K(χGUE)
ν,n
(x2, x2) from (48). It is normalised to the number of points n.
When interpreting the Nf flavours added to the χGUE in (33) as expectation values of char-
acteristic polynomial in the χGUE at Nf = 0, the following expression is well known, see e.g.
[18] for a derivation,
Z(Nf)
ν,n ({m}) = n!
⎛
⎝
Nf−1

j=0
(n + j)!
⎞
⎠
⎛
⎝
n−1

j=0
j!(j + ν)!
2
⎞
⎠
det
)
L(ν)
n+b−1(−m2
a)
*
a,b=1,...,Nf
ΔNf({m2})
.
(54)
The factor n! in front reflects that the eigenvalues have not been ordered. For Nf = 0 the first
product and last ratio are absent, and we recover
Z(Nf=0)
ν,n
= n!
n−1

j=0
ˆhj.
(55)
The preparation of (54) for the large n-analysis to be done in section 5 is based on the relation
[40, equation (18.9.14)]
L(ν)
j (z) = −z
jL(ν+1)
j−1 (z) + j + ν
j
L(ν)
j−1(z)
for j > 0,
(56)
applied recursively. Taking linear combinations of columns in the determinant of (54) allows
us to rewrite (54) as
Z(Nf)
ν,n ({m}) = (n!)Nf+1
⎛
⎝
n−1

j=0
j!(j + ν)!
2
⎞
⎠det

m2b−2
a
L(ν+b−1)
n
(−m2
a)

a,b=1,...,Nf
ΔNf({m2})
.
(57)
Now, the columns no longer become degenerate to leading order in the large-n asymptotic, as
they would have done in (54). The normalisation of (57) can be readily checked in the quenched
limit m1, . . . , mNf →∞.
