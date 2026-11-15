---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-021-voslamber-iterative-method
section_title: "Voslamber iterative method"
section_number: null
pages: 27-30
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Let us consider Eq. (30) when there is a perturbation parameter ε in the (in general, complex) matrix A, i.e., Eq. (105).
Theorem 9 guarantees that, for sufficiently small values of t, Y(t; ε) = exp Ω(t; ε), where
Ω(t; ε) =
∞
X
n=1
εn Ωn(t).
(115)
The advantages of this representation and the approximations obtained when the series is truncated have been sufficiently
recognized in the treatment done in previous sections. There is, however, a property of the exact solution not shared by any
truncation of the series (115) which could be relevant in certain physical applications: (1/ε) Pm
n=1 εnΩn(t) with m > 1 is
unbounded for ε →∞even when Ω(t, ε)/ε is bounded uniformly with respect to ε under rather general assumptions on
the matrix A(t) [92]. Notice that this is the case, in particular, for the adiabatic problem (93).
When Schur’s unitary triangularization theorem [44] is applied to the exact solution Y(t; ε) one has
Tε = UĎ Y U,
(116)
where Tε is an upper triangular matrix and U is unitary. In other words, Y is unitarily equivalent to an upper triangular
matrix Tε. Differentiating (116) and using (105), one arrives at
T ′
ε = εUĎAUTε +

Tε, UĎU′
.
Since the second term on the right hand side is not upper triangular, it follows at once that
Tε(t) = exp

ε
Z t
0
(UĎAU)△ds

,
where the subscript △denotes the upper triangular part (including terms on the main diagonal) of the corresponding matrix.
Taking into account (116) one gets
Ω(t, ε) = εU
Z t
0
(UĎAU)△ds

UĎ.
(117)
Considering now the Frobenius norm (which is unitarily invariant, Section 1.2) of both sides of this equation, one has
∥Ω∥F = |ε|

Z t
0
(UĎAU)△ds

F
≤|ε|
Z t
0
∥(UĎAU)△∥Fds
≤|ε|
Z t
0
∥UĎAU∥Fds = |ε|
Z t
0
∥A∥Fds.
(118)
If the spectral norm is considered instead, from inequalities (28), (29) and (118), one concludes that
∥Ω∥2 ≤
p
rank(A) |ε|
Z t
0
∥A∥2ds.
In any case, what is important to stress here is that for the exact solution Ω(t; ε)/ε is bounded uniformly with respect
to the ε parameter. Voslamber proceeds by deriving an algorithm for generating successive approximations of Y(t; ε) =
exp(Ω(t; ε)) which, contrarily to the direct series expansion (115), preserve this property. His point of departure is to get a
series expansion for the so-called dressed derivative of Ω[93]
Γ ≡eΩ/2 Ω′ e−Ω/2.
(119)
178
S. Blanes et al. / Physics Reports 470 (2009) 151–238
This is accomplished by inserting (39) in (119). Specifically, one has
Γ = eadΩ/2 Ω′ = eadΩ/2d exp−1
Ω(εA) = eadΩ/2
adΩ
eadΩ−1(εA)
=
adΩ/2
sinh Ω/2(εA) =
∞
X
n=0
Bn(1/2)
n!
adn
Ω(εA)
and finally [92,93]
Γ =
∞
X
n=0
21−n −1
n!
Bn adn
Ω(εA),
(120)
where, as usual, Bn denote Bernoulli numbers. In order to express Γ as a power series of ε one has to insert the Magnus
series (115) into Eq. (120). Then we get
Γ (t; ε) =
∞
X
n=1
εn Γn(t),
(121)
where the terms Γn can be expressed as a function of Ωk with k ≤n −2 through the recursive procedure [93]
Γ1 = A,
Γ2 = 0,
(122)
Γn =
n−1
X
j=2
cj
X
k1+···+kj=n−1
k1≥1,...,kj≥1
adΩk1 adΩk2 · · · adΩkj A,
n ≥3.
Here
cj ≡
21−j −1
j!
Bj,
with c2j+1 = 0, c2 = −1/24, c4 = 7/5760, etc. In particular,
Γ3 = −
1
24[Ω1, [Ω1, A]]
Γ4 = −
1
24([Ω1, [Ω2, A]] + [Ω2, [Ω1, A]]).
Now, from the definition of Γ , Eq. (119), we write
Ω′ = e−Ω/2 Γ eΩ/2,
which, after integration over t, can be used for constructing successive approximations to Ωonce the terms Γn are known
in terms of Ωk, k ≤n −2. Thus, the nth approximant Ω(n) is defined by
Ω(n)(t) =
Z t
0
e−1
2 Ω(n−1)(s)Γ (n)(s)e
1
2 Ω(n−1)(s)ds,
n = 1, 2, . . .
(123)
where the ε dependence has been omitted by simplicity and Γ (n) = Pn
k=1 εkΓk, Ω(0) = O. The first two approximants
explicitly read
Ω(1)(t, ε) = ε Ω1(t) = ε
Z t
0
A(s)ds
Ω(2)(t, ε) = ε
Z t
0
e−1
2 Ω(1)(s,ε)A(s)e
1
2 Ω(1)(s,ε)ds.
(124)
In this approach, the solution is approximated by Y(t) ≃exp(Ω(n)). Observe that Ω(n) contains contributions from an
infinity of orders in ε, whereas the nth term in the Magnus series (115) is proportional to εn. Furthermore, Ω(n) contains
Pn
k=1 εkΩk and also higher powers εm (m > n). In particular, one easily gets
Ω(2)(t; ε) = ε Ω1(t) + ε2 Ω2(t) +
∞
X
k=3
(−1)k−1
2k−1(k −1)!εk
Z t
0
adk−1
Ω1(s)A(s)ds.
From the structure of the expression (123) it is also possible to find the asymptotic behavior of Ω(n)/ε (n ≥3) for ε →∞
and prove that it remains bounded [92], just as the exact solution does. This property of the Voslamber iterative algorithm
may lead to better approximations of Y(t) when the parameter ε is not very small, since in that case Ω(n)/ε is expected to
remain close to Ω/ε, as shown in [93].
S. Blanes et al. / Physics Reports 470 (2009) 151–238
179
3.2. Floquet–Magnus expansion
We now turn our attention to a specific case of Eq. (30) with important physical and mathematical applications, namely
when the (complex) n × n matrix-valued function A(t) is periodic with period T. Then further information is available on
the structure of the exact solution, as is given by the celebrated Floquet theorem, which ensures the factorization of the
solution in a periodic part and a purely exponential factor. More specifically,
Y(t) = P(t) exp(tF),
(125)
where F and P are n × n matrices, P(t) = P(t + T) for all t and F is constant. Thus, albeit a solution of (30) is not, in general,
periodic, the departure from periodicity is determined by (125). This result, when applied in quantum mechanics, is referred
to as Bloch wave theory [94,95]. It is widely used in problems of solid state physics where space-periodic potentials are quite
common. In Nuclear Magnetic Resonance, this structure is exploited as far as either time-dependent periodic magnetic fields
or sample spinning are involved [24]. Asymptotic stability of the solution Y(t) is dictated by the nature of the eigenvalues
of F, the so-called characteristic exponents of the original periodic system [96].
An alternative manner of interpreting Eq. (125) is to consider the piece P(t), provided it is invertible, to perform a
transformation of the solution in such a way that the coefficient matrix corresponding to the new representation has all
its matrix entries given by constants. Thus the piece exp(tF) in (125) may be considered as an exact solution of the system
(30) previously moved to a representation where the coefficient matrix is the constant matrix F [76]. The t-dependent
change of representation is carried out by P(t). Connecting with Section 2.9, P(t) is the appropriate preliminary linear
transformation for periodic systems. Of course, Floquet theorem by itself gives no practical information about this procedure.
It just states that such a representation does exist. In fact, a serious difficulty in the study of differential equations with
periodic coefficients is that no general method to compute either the matrix P(t) or the eigenvalues of F is known.
Mainly, two ways of exploiting the above structure of Y(t) are found in the literature [97]. The first one consists in
performing a Fourier expansion of the formal solution, leading to an infinite system of linear differential equations with
constant coefficients. Thus, the t-dependent finite system is replaced with a constant one at the price of handling infinite
dimension. Resolution of the truncated system furnishes an approximate solution. The second approach is of perturbative
nature. It deals directly with the form (125) by expanding
P(t) =
∞
X
n=1
Pn(t),
F =
∞
X
n=1
Fn.
(126)
Every term Fn in (126) is fixed so as to ensure Pn(t) = Pn(t + T), which in turn guarantees the Floquet structure (125) at any
order of approximation.
Although the Magnus expansion, such as it has been formulated in this work, does not explicitly provide the structure of
the solution ensured by Floquet theorem, it can be adapted, without special difficulty, to also cope with this situation. The
starting point is to introduce the Floquet form (125) into the differential equation Y ′ = A(t)Y. In that way, the evolution
equation for P is obtained:
P′(t) = A(t)P(t) −P(t)F,
P(0) = I.
(127)
The constant matrix F is also unknown and we will determine it so as to ensure P(t + T) = P(t). Now we replace the usual
perturbative scheme in Eq. (126) with the exponential ansatz
P(t) = exp(Λ(t)),
Λ(0) = O.
(128)
Obviously, Λ(t + T) = Λ(t) so as to preserve periodicity. Now Eq. (127) conveys
d
dt
exp(Λ) = A exp(Λ) −exp(Λ)F,
(129)
from which, as with the conventional Magnus expansion, it follows readily that
Λ′ =
∞
X
k=0
Bk
k!
adk
Λ (A + (−1)k+1F).
(130)
This equation is now, in the Floquet context, the analogue of Magnus equation (39). Notice that if we put F = O then (39) is
recovered. The next move is to consider the series expansions for Λ and F
Λ(t) =
∞
X
k=1
Λk(t),
F =
∞
X
k=1
Fk,
(131)
with Λk(0) = O, for all k. Equating terms of the same order in (130) one gets the successive contributions to the series (131).
Therefore, the explicit ansatz we are propounding reads
Y(t) = exp
 ∞
X
k=1
Λk(t)
!
exp
 
t
∞
X
k=1
Fk
!
.
(132)
This can be properly referred as the Floquet–Magnus expansion.
180
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Substituting the expansions of Eq. (131) into (130) and equating terms of the same order, one can write
Λ′
n =
n−1
X
j=0
Bj
j!
 W (j)
n (t) + (−1)j+1T (j)
n (t)

(n ≥1).
(133)
The terms W (j)
n (t) may be obtained by a similar recurrence to that given in Eq. (49)
W (j)
n =
n−j
X
m=1
h
Λm, W (j−1)
n−m
i
(1 ≤j ≤n −1),
W (0)
1
= A,
W (0)
n
= O
(n > 1),
(134)
whereas the terms T (j)
n (t) obey the recurrence relation
T (j)
n =
n−j
X
m=1
h
Λm, T (j−1)
n−m
i
(1 ≤j ≤n −1),
T (0)
n
= Fn
(n > 0).
(135)
Every Fn is fixed by the condition Λn(t + T) = Λn(t). An outstanding feature is that Fn can be determined independently
of Λn(t) as the solution Y(t) = P(t) exp(tF) shrinks to Y(T) = exp(TF). Consequently, the conventional Magnus expansion
Y(t) = exp(Ω(t)) computed at t = T must furnish
Fn = Ωn(T)
T
,
for all n.
(136)
The first contributions to the Floquet–Magnus expansion read, explicitly,
Λ1(t) =
Z t
0
A(x)dx −tF1,
F1 =
1
T
Z T
0
A(x)dx,
Λ2(t) =
1
2
Z t
0
[A(x) + F1, Λ1(x)] dx −tF2,
(137)
F2 =
1
2T
Z T
0
[A(x) + F1, Λ1(x)] dx.
Moreover, from the recurrence relations (134) and (135) it is possible to obtain a sufficient condition such that convergence
of the series P Λn is guaranteed in the whole interval t ∈[0, T] [34]. In fact, one can show that absolute convergence of
the Floquet–Magnus series is ensured at least if
Z T
0
∥A(t)∥dt < ξF ≡0.20925.
(138)
Notice that convergence of the series P
Fn is already guaranteed by (136) and the discussion concerning the conventional
Magnus expansion in Sections 2.7.2 and 2.7.3. The bound ξF in the periodic Floquet case turns out to be smaller than
the corresponding bound rc = π in the conventional Magnus expansion. At first sight this could be understood as an
impoverishment of the result. However, it has to be recalled that, due precisely to Floquet theorem, once the condition
is fulfilled in one period, convergence is assured for any value of time. On the contrary, in the general Magnus case, the
bound always gives a running condition.
