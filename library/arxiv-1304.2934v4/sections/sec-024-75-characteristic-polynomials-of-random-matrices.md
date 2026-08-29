---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-024-75-characteristic-polynomials-of-random-matrices
section_title: "Characteristic polynomials of random matrices in a compact Lie group"
section_number: 7.5
pages: 61-64
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
duce the classical compact Lie groups of type A, C, D:
U(n) ={g∈ GL(n, C)| gg† = g†g = In} (unitary group)
USp(n) ={g∈ GL(n, H)| gg⋆ = g⋆g = In} (compact symplectic group)
SO(2n) ={g∈ GL(2n, R)| ggt = gtg = I2n ; det g = 1} (special orthogonal group)
where for compact symplectic groups g⋆ denotes the transpose conjugate of a quater-
nionic matrix, the conjugate of a quaternionic number q = a + ib + jc + kd being
q⋆ = a− ib− jb− kd. In the following we shall consider quaternionic matrices as
complex matrices of size 2n× 2n by using the map
a + ib + jc + kd↦→
(
a + ib c + id
−c + id a − ib
)
.
The eigenvalues of a matrix g∈ G = SO(2n) or U(n) or USp(n) are on the unit circle
S1, and the value of the characteristic polynomial det(1− g) factorizes as
det(1− g) =
n
∏
i=1
(1− eiθi )
if G = U(n) and Sp(g) = ( eiθ1, . . . , eiθn), and
det(1− g) =
n
∏
i=1
(1− eiθi )(1− e−iθi ) =
n
∏
i=1
|1− eiθi|2
if G = SO(2n) or USp(n) and Sp(g) = ( eiθ1, e−iθ1, . . . , eiθn, e−iθn). We deﬁne
YA,C,D
n =
{
Re
[
log det(1− g)
]
in type A;
log det(1− g) in types C and D.
An exact formula for the Laplace transform of log det (1− g), and the corresponding
asymptotics have been given in [KS00a, KS00b, HKO01], see also [KN12, Sections 3
and 4]. Hence, in type A,
E
[
ez1 Re(log det(1−g))+z2 Im(log det(1−g))
]
=
n
∏
j=1
Γ(j) Γ(j + z1)
Γ(j + z1+iz2
2 ) Γ(j + z1−iz2
2 )
62 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
for every z1 with Re(z1) >−1, and every z2∈ C (see e.g. [KS00b, Formula (71)]. In
particular, if Re(z) >−1, then
E
[
ezYAn
]
=
n
∏
j=1
Γ(j) Γ(j + z)
Γ(j + z
2 )2
= G(1 + z
2 )2
G(1 + z) n
z2
4 (1 + o(1)).
Here G denotes Barnes’G-function, which is the entire solution of the functional equa-
tion G(z + 1) = Γ(z) G(z) with G(1) = 1. To go from the exact formula with ratios
of Gamma functions, to the asymptotic formula with Barnes’ functions, one has to in-
terpret the formula as a Toeplitz determinant with one Fisher-Hartwig singularity, see
the details in the aforementioned paper [KN12] (the arguments therein apply mutatis
mutandi to the case of a complex random variable in the Laplace transform z, since the
exact formula holds as long as Re (z) >−1, and the theory of Toeplitz determinants
works from the outset with complex functions). Therefore, (YA
n )n∈N converges in the
mod-Gaussian sense with parameters tn = log n
2 , limiting function
ψA(z) = G(1 + z
2 )2
G(1 + z) ,
and on the bandS(−1,+∞).
Similarly, in type C and D, one has the exacts formulas
E
[
ezYCn
]
= 22n z
n
∏
j=1
Γ(j + n + 1) Γ(z + j + 1
2 )
Γ(j + 1
2 ) Γ(z + j + n + 1)
for Re(z) >−3
2;
E
[
ezYDn
]
= 22n z
n
∏
j=1
Γ(j + n− 1) Γ(z + j− 1
2 )
Γ(j− 1
2 ) Γ(z + j + n− 1)
for Re(z) >−1
2
as well as the asymptotic formulas
E
[
ezYCn
]
=
( πn
2
) z
2
( n
2
) z2
2 G( 3
2 )
G( 3
2 + z) (1 + o(1));
E
[
ezYDn
]
=
(8π
n
) z
2 ( n
2
) z2
2 G( 1
2 )
G( 1
2 + z) (1 + o(1))
which hold in the same range for z, locally uniformly. Therefore, setting
XC
n = YC
n− 1
2 log πn
2
XD
n = YD
n− 1
2 log 8π
n
then (XC
n )n∈N and (XD
n )n∈N converges in the mod-Gaussian sense, with parameters
tn = log n
2 , limiting functions
ψC(z) = G( 3
2 )
G( 3
2 + z) and ψD(z) = G( 1
2 )
G( 1
2 + z)
,
and respectively onS(− 3
2 ,+∞) and onS(− 1
2 ,+∞).
MOD-φ CONVERGENCE, I 63
Now, our large deviation theorems apply and one obtains:
Theorem 7.24. Over U(n), one has:
∀x > 0, Pn
[
| det(1− g)|≥ n
x
2
]
= G(1 + x
2 )2
G(1 + x)
1
x n
x2
4
√
π log n
(1 + o(1));
∀x∈ (0, 1), Pn
[
| det(1− g)|≤ n− x
2
]
= G(1− x
2 )2
G(1− x)
1
x n
x2
4
√
π log n
(1 + o(1)).
Over USp(n), one has:
∀x > 0, Pn

det(1− g)√
π
2
≥ n
1
2 +x

 = G( 3
2 )
G( 3
2 + x)
1
x n
x2
2 2
x2+x
2
√
2π log n
(1 + o(1));
∀x∈
(
0 , 3
2
)
, Pn

det(1− g)√
π
2
≥ n
1
2−x

 = G( 3
2 )
G( 3
2− x)
1
x n
x2
2 2
x2−x
2
√
2π log n
(1 + o(1)).
Finally, over SO(2n), one has:
∀x > 0, Pn
[det(1− g)√
8π
≥ n− 1
2 +x
]
= G( 1
2 )
G( 1
2 + x)
1
x n
x2
2 2
x2−x
2
√
2π log n
(1 + o(1));
∀x∈
(
0 , 1
2
)
, Pn
[det(1− g)√
8π
≤ n− 1
2−x
]
= G( 1
2 )
G( 1
2− x)
1
x n
x2
2 2
x2+x
2
√
2π log n
(1 + o(1)).
Proof. These are immediate computations by using Theorem 4.3. □
Remark 7.25. From Proposition 4.14, one also gets normality zones for the random vari-
ables Xn/√tn. On the other hand, the computations performed in the unitary case hint
at a phenomenon of 2-dimensional mod-Gaussian convergence for the complex num-
bers log det(1− g), with g∈ U(n). In [FMN15b], we shall prove this rigorously, and
compute various probabilistic consequences, for instance, estimates of large deviations
for the random vectors log det(1− g).
Remark 7.26. The analogue of Theorem 7.24 in the setting of random matrices in the
β-ensembles, or of general Wigner matrices, has been studied in the recent paper
[DE13a]. They can be easily restated in the mod-Gaussian language, since their proofs
rely on the computation of the asymptotics of the cumulants of the random variables
Xn = log| det Mn|, with for instance (Mn)n∈N random matrices of the Gaussian uni-
tary ensembles.
64 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
8. M OD-GAUSSIAN CONVERGENCE FROM A FACTORIZATION
OF THE PROBABILITY GENERATING FUNCTION
Let (Xn)n∈N be a sequence of bounded random variables with nonnegative integer
values such that σ2
n := Var(Xn) tends to inﬁnity. Denote Pn(t) = E[tXn] the probability
generating function of Xn. Each Pn(t) is a polynomial in t. Then, it is known that a
sufﬁcient condition so that Xn is asymptotically Gaussian is that Pn(t) has negative
real roots (see references below). In this section, we prove that if the third cumulant
L3
n := κ(3)(Xn) also tends to inﬁnity such that Ln = o(σn), then a suitable renormalized
version of Xn converges in the mod-Gaussian sense. We then give an application for
the number of blocks in a uniform set-partition of [n].
