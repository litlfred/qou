---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-011-d-finite-generating-functions-and-diagonals
section_title: "D-finite generating functions and diagonals"
section_number: null
pages: 58-69
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
The more explicitly a generating function is described, the better the prospects
are for extracting information from it. This includes not only exact formu-
lae and asymptotic estimation, but also additional properties like bijections to
other classes and random sampling algorithms for objects in the class. Ratio-
nal generating functions (with coeﬃcients in the integers or rational numbers)
2.4 D-ﬁnite generating functions and diagonals
41
are easy to work with because they are speciﬁed by the ﬁnite data of their
numerator and denominator polynomials.
We have seen that some common and very natural combinatorial operations
take us from the class of rational functions to the larger class of algebraic gen-
erating functions. Algebraic functions also have canonical representations: if
f is algebraic then there is a minimal polynomial P for which P( f(z), z) = 0
and the series f may be speciﬁed by writing down the coeﬃcients of P, which
are themselves polynomials and therefore ﬁnitely speciﬁed, and enough initial
terms to uniquely determine f among all roots of P. In Chapter 8 we discuss
techniques in computational algebra that allow one to manipulate algebraic
quantities implicitly using symbolic methods, making the class of algebraic
generating functions reasonably nice to work with. There are, however, com-
mon combinatorial operations that take us out of the class of algebraic func-
tions, and this drives us to consider a more general class of generating functions
involving diﬀerential equations. A more complete discussion of the hierarchy
for univariate generating functions may be found in [Mel21, Chapter 2] and
[Sta99, Chapter 6].
Rational 
Algebraic
D−finite
Figure 2.4 Common classes of generating functions.
42
Generating functions
Univariate D-ﬁnite functions
Because any formal power series with a non-zero constant is invertible, the
ﬁeld of fractions of C[[z]] is the ﬁeld of formal Laurent series
C((z)) =

X
n≥κ
anzn : κ ∈Z and an ∈C for all n

containing series with a ﬁnite number of terms with negative exponents, where
addition is still deﬁned termwise and multiplication is still deﬁned by convo-
lution. Section 6.1 gives further information on Laurent series.
Deﬁnition 2.20. A formal power series f(z) ∈C[[z]] is a D-ﬁnite series if
and only if there is an integer m and polynomials P0(z), . . . , Pm(z) ∈C[z] with
Pm(z) , 0 such that
P0(z) f(z) + P1(z) f ′(z) + · · · + Pm(z) f (m)(z) = 0 .
(2.8)
Equivalently, f is D-ﬁnite if and only if f and its derivatives span a ﬁnite
dimensional vector space in C((z)) over the ﬁeld C(z) of rational functions.
Remark. The more natural deﬁnition of a D-ﬁnite series is one whose deriva-
tives span a ﬁnite dimensional space over the polynomial ring C[z]. Vector
spaces over ﬁelds are simpler than modules over rings, so we phrase this in
terms of vector space dimension over the rational functions instead. This re-
quires that the rational functions act on C[[z]], which requires us to extend
C[[z]] to C((z)).
Remark. If f(z) is a formal power series that satisﬁes a non-homogeneous
linear equation
P0(z) f(z) + P1(z) f ′(z) + · · · + Pm(z) f (m)(z) = P(z)
with P(z), P0(z), . . . , Pm(z) ∈C[z] then repeated diﬀerentiation proves that f(z)
is D-ﬁnite.
Variants of this deﬁnition are discussed in [Sta99, Proposition 6.4.1]. The
Venn diagram in Figure 2.4 depicting the hierarchy of generating function class
is justiﬁed by the following classical proposition.
Proposition 2.21. If f(z) ∈C[[z]] is algebraic then f(z) is D-ﬁnite.
Proof
Since f(z) is algebraic there exists P(z, y) = Pm
j=0 Pj(z)yj ∈C[z, y]
such that P(z, f(z)) = 0. Assume P is selected among all such polynomials
to have minimal degree in y, so that the partial derivative Py(z, y), which has
2.4 D-ﬁnite generating functions and diagonals
43
smaller degree in y than P(z, y), is non-zero when y = f(z). Implicit diﬀerentia-
tion of the equation P(z, f(z)) = 0 shows that Pz(z, f(z)) + f ′(z)Py(z, f(z)) = 0,
so Py(z, f(z)) , 0 implies
f ′(z) = −Pz(z, f(z))
Py(z, f(z)) .
(2.9)
We have now shown that f ′(z) lies in the ﬁeld of fractions of the ring C[z][f].
The quotient rule thus implies that the derivative of any element of the ﬁeld
extension C(z, f) is again in C(z, f), so induction implies all derivatives of f
are in C(z, f). Because f is algebraic, C(z, f) is a ﬁnite extension of C(z). Thus,
f and its derivatives span a ﬁnite vector space over C(z), and f is D-ﬁnite.
□
Recall that a series f = P∞
n=0 anzn is rational if and only if the sequence
{an : n ≥0} satisﬁes a linear recurrence with constant coeﬃcients. There is no
equivalent linear characterization for the coeﬃcients of algebraic generating
functions, but there is for D-ﬁnite functions.
Deﬁnition 2.22 (P-recursiveness). A univariate sequence {an : n ≥0} is said
to be a P-recursive sequence (or polynomially recursive) if there exist polyno-
mials P0(n), . . . , Pr(n) ∈C[n] with Pm(n) , 0 such that
Pr(n)an+r + Pr−1(n)an+r−1 + · · · + P0(n)an = 0
(2.10)
for all n ≥0.
Example 2.23. If an = 1/n! then {an} is P-recursive as (n + 1)an+1 −an = 0 for
all n ≥0. Furthermore, if f(z) enumerates {an} then P
n≥0(n + 1)an+1zn = f ′(z),
so f ′(z) −f(z) = 0 and f is D-ﬁnite. We can compute f by solving this linear
diﬀerential equation with the initial condition a0 = 1, obtaining the expected
solution f(z) = ez = P
n≥0 zn/n!.
◁
The correspondence between P-recursive sequences and D-ﬁnite series is a
classical result, known at least as far back as Frobenius’s work on computing
series solutions to ordinary diﬀerential equations.
Theorem 2.24 (P-recursive corresponds to D-ﬁnite). A sequence {an : n ≥0}
is P-recursive if and only if its generating function f(z) = P∞
n=0 anzn is D-ﬁnite.
Proof
First, suppose f is D-ﬁnite and satisﬁes (2.8). Diﬀerentiating the power
series for f shows that for any n ∈N and k ∈[n] the coeﬃcient [zn−k] f (j)(z)
equals (n −k + j) jan−k+ j, where (u) j := u(u −1) · · · (u −j + 1) denotes the
falling factorial. Let bk, j = [zk]P j(z) and let D denote the maximum degree of
the coeﬃcient polynomials P0(z), . . . , Pm(z). Then for any n ≥0, extracting the
44
Generating functions
coeﬃcient of zn in (2.8) gives the linear equation
m
X
j=0
D
X
k=0
bk, j (n −k + j)j an−k+ j = 0
having polynomial coeﬃcients in n of degrees at most m. This is a non-trivial
linear recurrence for {an}, because for any k such that bk,m = [zk]Pm(z) , 0 the
coeﬃcient of an−k+m is bm,knm + O(nm−1) , 0.
Conversely, suppose that {an} is P-recursive and satisﬁes (2.10). The set of
falling-factorial polynomials {(n + j)j : j ≥0} forms a basis for C[n] which
is triangular with respect to the basis {nj : j ≥0}, hence each Pk(n) is a ﬁnite
linear combination Pk(n) = P
j ck,j(n + j) j and substitution into (2.10) yields
m
X
k=0
deg Pk
X
j=0
ck, j (n + j)jan+k = 0 .
The rules for diﬀerentiating formal power series extend to the diﬀerentiation
of Laurent series, and imply that the coeﬃcient of zn in the repeated derivative
(zj−k f(z))(j) is (n + j) j an+k. Multiplying our last equality by zn and summing
over all values of n thus gives the relation
m
X
k=0
deg Pk
X
j=0
ck,j

z j−k f(z)
(j) = 0 .
Using the product rule, this becomes a non-trivial linear ODE in f(z) with
coeﬃcients in C[z, z−1], and multiplying through by a suﬃciently high power
of z proves that f(z) is D-ﬁnite.
□
Multivariate D-ﬁnite functions
Generalizing the univariate deﬁnition, a multivariate formal power series f(z) ∈
C[[z]] is called a D-ﬁnite sequence when f and all its iterated partial deriva-
tives generate a ﬁnite dimensional vector space over C(z). The correct ana-
logue of P-recursiveness in the multivariate case is not as obvious: the fol-
lowing deﬁnition, recursive in the dimension d, comes from [Lip89, Deﬁni-
tion 3.2].
Deﬁnition 2.25 (P-recursiveness in arbitrary dimension). Suppose d > 1 and
P-recursiveness has been deﬁned for arrays of dimension d −1. Then the mul-
tivariate sequence {ar : r ∈Nd} is said to be a P-recursive sequence if there is
some positive integer k such that the following two conditions hold.
2.4 D-ﬁnite generating functions and diagonals
45
(i) For each j ∈[d] there are polynomials
n
P j
τ(n) : τ ∈{0, . . . , k}do
, not all
zero, such that
X
τ∈{0,...,k}d
P j
τ(rj)ar−τ = 0
for all r1, . . . , rd ≥k.
(ii) All the (d −1)-variate arrays obtained from {ar} by holding one of the d
indices ﬁxed at a value less than k are P-recursive.
The following result, proved in [Lip89, Theorem 31], shows that this deﬁni-
tion of P-recursiveness is the correct one.
Theorem 2.26. The array {ar : r ∈Nd} is P-recursive if and only if its gener-
ating function f(z) = P
r arzr is D-ﬁnite.
□
2.4.1 Diagonals
D-ﬁnite generating functions are ﬁnitely speciﬁable, the arrays they enumerate
satisfy nice recursions, and they appear often in combinatorics. In addition,
D-ﬁnite functions form an interesting family to study because they satisfy nice
closure properties. First, we note that D-ﬁnite functions are closed under addi-
tion and multiplication, just like rational and algebraic functions.
Theorem 2.27. If f(z) and g(z) are D-ﬁnite then so are f(z) + g(z) and
f(z)g(z).
Proof
Let V be the C(z)-subspace of C((z)) spanned by f(z)+g(z) and all its
derivatives. Then V is contained in the sum of subspaces Vf +Vg spanned by the
derivatives of f and g. Hence, V is a ﬁnite-dimensional space with dimension
at most dim(Vf ) + dim(Vg) and f(z) + g(z) is D-ﬁnite.
Similarly, the products f (r)(z)g(s)(z) of the partial derivatives of f and g
span a ﬁnite dimensional space W of dimension at most dim(Vf ) · dim(Vg).
By the product rule, every derivative of f(z)g(z) lies in W, so f(z)g(z) is
D-ﬁnite.
□
A more interesting closure property has to do with diagonals of multivariate
series.
Deﬁnition 2.28 (diagonal of a formal power series). Let F(z) = P
r∈Nd arzr
be a formal power series and s ∈Rd be a ﬁxed vector. The s-diagonal of F is
the univariate series
(∆sF)(z1) :=
X
n≥0
anszn
1
consisting of the series coeﬃcients of F whose indices are multiples of s,
46
Generating functions
where ans = 0 if ns < Nd (so the s-diagonal is only non-trivial when s has
nonnegative rational coordinates). When s = 1 the s-diagonal of F is called
the main diagonal and denoted diag F or ∆F. For 1 ≤i < j ≤d the (zi, zj)-
elementary diagonal of F is the formal power series
(∆zi=zjF)(z1, . . . , z j−1, z j+1, . . . , zd)
obtained by taking the terms of F where the exponent of zi equals the exponent
of zj and setting z j = 1. Note that the main diagonal of F can be computed by
taking d −1 elementary diagonals.
Exercise 2.7. Show that if f(x) is the diagonal of F(x, y) then it is also the
diagonal of F(−x, −y).
Example 2.29. Consider the generating function
F(x, y, z) =
1
1 −x −y −z =
X
r,s,t≥0
(r + s + t)!
r!s!t!
xryszt
enumerating the trinomial coeﬃcients. Then the (x, y)-elementary diagonal of
F is the series
(∆x=yF)(x, z) =
X
r,t≥0
(2r + t)!
(r!)2 t! xrzt ,
while the main diagonal is
(∆F)(x) =
X
n≥0
(3n)!
(n!)3 xn = 1 + 6x + 90x2 + · · · .
◁
Exercise 2.8. Let F(x, y) = P
r,s≥0 arsxrys be a bivariate formal power series.
What is the diﬀerence between diag F and F(x, x)?
It is interesting to note that even though the generating function in Exam-
ple 2.29 is rational, the main diagonal ∆F is transcendental (i.e., not algebraic).
Perhaps the easiest way to see this is to compute asymptotics of the diagonal
coeﬃcients using the methods of Chapter 9 and verify that they do not have
asymptotic growth compatible with being an algebraic series [Mel21, Corol-
lary 2.1].
Although the classes of rational and algebraic series are not closed under
taking diagonals, the class of D-ﬁnite series is.
Theorem 2.30 (Lipshitz [Lip88]). Any elementary diagonal of a D-ﬁnite series
in d variables is a D-ﬁnite series in d −1 variables. In particular, the main
diagonal of a D-ﬁnite series is a univariate D-ﬁnite function.
□
2.4 D-ﬁnite generating functions and diagonals
47
Because many other operations on power series can be phrased as diagonals,
Theorem 2.30 ﬁnds a wide variety of applications.
Example 2.31. The Hadamard product of two formal power series F(z) =
P
r∈Nd arzr and G(z) = P
r∈Nd brzr is the series (F ⊙G)(z) = P
r∈Nd arbrzr.
The repeated diagonal expression
(F ⊙G)(z) = ∆z1=y1 · · · ∆zd=ydF(z)G(y)
implies that F ⊙G is D-ﬁnite whenever F and G are D-ﬁnite. See [CS98]
for an algorithm to compute an annihilating D-ﬁnite equation for F ⊙G from
annihilating D-ﬁnite equations for F and G.
◁
Exercise 2.9. The z-constant term of an analytic series F(z, t) ∈C[[z, t]]
is the series F(0, t) ∈C[[t]]. Prove that the z-constant term of F is the main
diagonal of F(z, z1 · · · zdt).
Finally, we note that the class of D-ﬁnite series is not closed under compo-
sition or division.
Exercise 2.10. Let f(x) = sin x and g(x) = 1/x. Prove that f and g are D-ﬁnite
but g( f(x)) is not.
Algebraic series and diagonals
The family of series obtained as main diagonals of rational functions appears
in many combinatorial applications, and sits naturally between the classes of
algebraic and D-ﬁnite series. Indeed, it turns out that the diagonals of bivariate
rational series form precisely the set of algebraic series. This means that com-
putation of asymptotics for the main diagonal of a bivariate rational series can
be reduced to computing asymptotics of a univariate algebraic series (see the
discussion in Section 13.1) or vice versa (see Section 9.3.1).
The proof that the diagonal of a bivariate rational series is algebraic was
sketched by Furstenberg [Fur67] and given in more detail by Hautus and Klarner
[HK71]. Because we work with series over the complex numbers, we give a
straightforward analytic proof that helps compute an annihilating polynomial
for the diagonal. Stanley [Sta99, Theorem 6.3.3] gives an algebraic proof hold-
ing over arbitrary ﬁelds.
Theorem 2.32 (bivariate diagonal extraction). If F(x, y) is a rational power
series in two variables then ∆F is algebraic.
Proof
Write F(x, y) = P(x, y)/Q(x, y) for coprime polynomials P and Q with
Q(0, 0) , 0, and let h(y) = (∆F)(y). Since F converges in a neighborhood of
48
Generating functions
the origin, when |y| is suﬃciently small the function F(z, y/z) is absolutely con-
vergent for z in some annulus A(y). Treating y as a constant, we view F(z, y/z)
as a convergent Laurent series in z inside the annulus A(y) with constant term
h(y). The Cauchy Integral Formula then gives the integral expression
h(y) = 1
2πi
Z
C
P(z, y/z)
zQ(z, y/z) dz ,
where C is any positively oriented circle in the annulus of convergence A(y).
By the Residue Theorem,
h(y) =
X
α
Res
z=α(y)
 P(z, y/z)
zQ(z, y/z)
!
,
(2.11)
where the sum is over all poles α(y) inside the circle C. These residues are
all rational expressions of the poles, which are roots of Q(z, y/z), so we have
represented the diagonal as a sum of algebraic functions, which is also alge-
braic.
□
Remark. Taking |y| suﬃciently small in the proof of Theorem 2.32 allows one
to pick a circle C such that the poles of the Cauchy integrand inside the circle
are precisely the roots z = α(y) of Q(z, y/z) that approach zero as y →0. An
annihilating polynomial for the diagonal can be computed from (2.11) using
algebraic tools like the resultant, although in low-degree cases it can usually
be computed directly.
Example 2.33 (Delannoy numbers, continued). Recall from above that the
generating function of the Delannoy numbers is F(x, y) = 1/(1 −x −y −xy),
so
x−1F(x, y/x) =
1
x −x2 −y −xy
has poles at
x±(y) = 1 −y ±
p
1 −6y + y2
2
with only x−(y) →0 as y →0. Since x−1F(x, y/x) = −1/[(x−x−(y))(x−x+(y))],
the sequence of Delannoy numbers where both indices are equal has generating
function
(∆F)(y) = Res
x=x−(y) x−1F(x, y/x) =
−1
x−(y) −x+(y) =
1
p
1 −6y + y2 .
◁
The converse of Theorem 2.32 also holds. First, we give an explicit formula
of Furstenberg [Fur67] that holds in a special case.
2.4 D-ﬁnite generating functions and diagonals
49
Proposition 2.34. Let f(x) be an algebraic univariate power series satisfying
P(x, f(x)) = 0 for some P(x, y) ∈C[x, y]. Suppose further that f(0) = 0 and
Py(0, 0) , 0. Then
f(x) = ∆
 y2Py(xy, y)
P(xy, y)
!
.
The proof of Proposition 2.34 follows directly from factoring P(x, y) = (y −
f(x))u(x, y) for some u ∈C[[x]][y] with u(0, 0) , 0 and then examining which
terms lie on the diagonal of y2Py(xy, y)/P(xy, y).
Example 2.35. The generating function for binary trees counted by external
nodes is the shifted Catalan generating function f(x) = (1 −
√
1 −4x)/2 with
minimal polynomial P(x, y) = y2 −y + x. Proposition 2.34 yields the rational
function F(y, z) = y(1 −2y)/(1 −x −y) whose diagonal is f(x).
◁
The hypothesis that Py(0, 0) , 0 in Proposition 2.34 restricts it to the case
where P(x, y) has a single root that passes through the origin. One natural
generalization to the multivariate setting is the following, which can be found
in [Saf00, Lemma 2].
Proposition 2.36. Let f(z) be an algebraic power series with P(z, f(z)) = 0
for some P(z, y) ∈C[z, y]. Suppose further that f is divisible by zd and that in
some neighborhood of 0 there is a positive integer k and factorization P(z, y) =
(y −f(z))ku(z, y) such that u(0, 0) , 0. Then f(z) is the elementary diagonal
∆zd=yF(z, y) of the rational function
F(z, y) = y2Py(z1, . . . , zd−1, yzd, y)
kP(z1, . . . , zd−1, yzd, y) .
Example 2.37. The Narayana numbers [FS09, Example III.13], deﬁned by
the explicit formula
ars = 1
r
 r
s
! 
r
s −1
!
,
are a reﬁnement of the Catalan numbers which enumerate, for example, rooted
ordered trees by edges and leaves. The Narayana generating function
f(x, y) = 1 + x(y −1) −
p
1 −2x(y + 1) + x2(y −1)2
2
is a root of the polynomial
P(x, y, w) = w2 −w 1 + x(y −1) + xy = w −f(x, y) h
w −f(x, y)
i
,
50
Generating functions
where f denotes the algebraic conjugate of f, obtained by changing the sign
in front of the square root in f. Proposition 2.36 gives the diagonal expression
f(x, y) = ∆x=w
 w(1 −2w −wx(1 −y))
1 −w −xy −wx(1 −y)
!
.
Note that we cannot use Proposition 2.36 with respect to the variable y.
◁
The following example from [Saf00] shows that the hypotheses of Proposi-
tion 2.36 are necessary for its conclusion.
Example 2.38. Let f(x, y) = y
p
1 −x −y. If f(x, y) could be expressed as the
(y, w)-elementary diagonal of a trivariate rational series F(x, y, w) then
Fyw(x, 0, 0) = [yw]F(x, y, w) = [y] f(x, y) = fy(x, 0) =
√
1 −x,
contradicting the fact that
√
1 −x is irrational while Fyw(x, 0, 0) is rational.
◁
To extend Proposition 2.36 to larger classes of algebraic series we can ei-
ther increase the dimension of the rational function in question, or relax our
deﬁnition of a diagonal. In the ﬁrst direction, Denef and Lipshitz proved that
every algebraic function has a rational diagonal expression in at most double
the number of variables.
Proposition 2.39 (Denef and Lipshitz [DL87, Theorem 6.2]). If f(z) is an
algebraic power series in d variables then there exists a rational series R(z, y)
in 2d variables such that f(z) = ∆z1=y1 · · · ∆zd=ydR(z, y).
□
In the second direction, Safonov gave an algorithm to express any algebraic
function in d variables as a generalized diagonal of a rational function in d + 1
variables.
Deﬁnition 2.40. A unimodular matrix is a matrix having integer entries and
determinant ±1. Let F(z, y) = P
(r,s)∈Nd+1 ar,szrys be a formal power series
in d + 1 variables and let M be a unimodular d × d matrix with nonnegative
entries. The M-diagonal or generalized diagonal (with respect to M) of F is
the formal power series in d variables given by P
r∈Nd brzr with br = as,sd,
where s = Mr.
Exercise 2.11. Let M =

1 0
1 1

and suppose that F(x, y) is the M-diagonal of
H(x, y, z). Express ∆F in terms of the coeﬃcients ar,s,t of H.
Theorem 2.41 (Safonov [Saf00]). Let f(z) be an algebraic function in d vari-
ables. Then there is a unimodular matrix M ∈Nd×d and a rational function
F(z, y) in d + 1 variables such that f is the M-diagonal of F.
