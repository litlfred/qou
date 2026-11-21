---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-030-laurent-series
section_title: "Laurent series"
section_number: null
pages: 153-159
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
135
naturally capture properties related to all convergent series expansions of the
function. Thus, even if one wishes to stay within the realm of power series, a
knowledge of Laurent expansions provides insight into the analysis that can
help in real applications.
The second section of this chapter surveys basic properties of amoebas, and
describes their use in analytic combinatorics, while the third section introduces
some basics from convex geometry and describes their connection to polyno-
mial amoebas. The fourth section studies the boundary points of amoebas and
minimal singularities, which are very important to our ACSV analysis. The
ﬁnal section collects some related topics that are needed in later chapters.
Notational remarks
To simplify notation we extend the logarithm and exponential functions coor-
dinatewise to vectors,
log(z) := (log z1, . . . , log zd)
exp(x) := (ex1, . . . , exd) ,
and deﬁne the coordinatewise log-modulus Relog map
Relog(z) := (log |z1|, . . . , log |zd|).
The inverse image of x ∈Rd under the Relog map is the exponential torus
Te(x) := Relog−1(x) = {z ∈Cd : |zj| = exj for all j} .
Note that the torus T(z) passing through z is equal to Te(Relog(z)). As we will
soon see, the image of the singular set of a multivariate meromorphic function
under the Relog map provides important information about its analytic behav-
ior.
6.1 Laurent series
A Laurent polynomial is a ﬁnite complex linear combination of monomials
zr with integer exponents r. The ring of Laurent polynomials C
h
z, z−1i
=
C
h
z1, z−1
1 , . . . , zd, z−1
d
i
consists of the set of all Laurent polynomials, with addi-
tion and multiplication deﬁned analogously to the polynomial ring C[z]. Since
a Laurent polynomial has only a ﬁnite number of terms, the algebraic structure
of C[z, z−1] is similar to the algebraic structure of C[z]. On the other hand, the
space of formal Laurent expressions in z is the complex vector space L(z) of
formal complex linear combinations of monomials zr as r ranges over all of
136
Laurent series, amoebas, and convex geometry
Zd. Although the space L(z) is a module over the ring of Laurent polynomials,
it is not itself a ring. Indeed, because a formal Laurent expression can have
indices with negative sign and arbitrarily large magnitude, there is no natural
product structure on L(z).
Example 6.2. If G(z) = P
n∈Z zn then attempting to use the usual deﬁnition
of series multiplication gives, for instance, that the constant term of G(z)2 is
P
n∈Z 1, which is not well deﬁned. We also note that (1 −z)G(z) = 0 so, as a
C[z, z−1] module, elements of L(z) can have non-trivial annihilators.
◁
One approach to giving L(z) a ring structure involves restricting the indices
that can appear, for instance requiring that all coordinates of all indices have
a ﬁxed lower bound (this is suﬃcient to develop a rich theory in one variable,
but the multivariate case is more delicate). Here we work around these formal
diﬃculties by restricting ourselves to the study of convergent Laurent series.
Let D be an open simply connected subset of Cd
∗and let LD(z) denote the
subspace of L(z) consisting of series that are absolutely convergent, uniformly
on compact subsets of D.
When discussing convergence of Laurent series, we always mean uniform
convergence on compact sets of Cd
∗(we disallow zero coordinates so that we
do not need to worry about dividing by zero in terms with negative indices).
Deﬁnition 6.3. The domain of convergence of a Laurent series P
r∈Zd arzr
is its open domain of absolute convergence, equal to the interior of the set of
z ∈Cd
∗for which P
r∈Zd |arzr| is ﬁnite.
As usual, we deﬁne a convex set to be a subset S of Rd with the property
that for each x, y ∈S , and each λ ∈[0, 1], necessarily (1 −λ)x + λy ∈S .
It follows easily by induction that each convex set is closed under taking a
convex combination of elements and the Chain Rule. That is, if x1, . . . , xn ∈S
and λ1, λn ∈[0, 1] with P
i λi = 1, then P
i λixi ∈S .
Theorem 6.4 (domains of convergence of Laurent series).
(1) Let F(z) = P
r∈Zd arzr be a Laurent series. Then the domain of conver-
gence of F has the form D = Relog−1(B) for some convex open set B ⊂Rd.
(2) The function f deﬁned by f(z) = F(z) for z ∈D is analytic in D.
(3) Conversely, if B is an open convex subset of Rd and f(z) is an analytic
function on D = Relog−1(B) then there is a unique Laurent series F(z) ∈
LD(z) converging to f(z). For each r ∈Zd, the coeﬃcient ar = [zr]F(z)
is given by the Cauchy integral
ar =
 1
2πi
!d Z
Relog−1(x)
f(z)z−r−1 dz
(6.1)
6.1 Laurent series
137
for any x ∈B.
Proof
To be given after Exercise 6.1 below.
□
Theorem 6.4 allows us to deﬁne multiplication in LD(z) using multiplication
of analytic functions: if ι is the identiﬁcation map from LD(z) to the space of
analytic functions on D then ι is invertible, and for G, H ∈LD(z) we set
G · H := ι−1(ι(G) · ι(H)). Similarly, if Q is everywhere nonvanishing on D then
there is a unique Laurent series identiﬁed with the analytic function 1/Q(z).
We may therefore identify a quotient of Laurent polynomials P(z)/Q(z) with
a unique convergent Laurent series by specifying a point w ∈Cd
∗such that Q
does not vanish on T(w) or, equivalently, a point x ∈Rd such that Q does not
vanish on Te(x) = Relog−1(x).
Exercise 6.1. Let f(x, y, z) = 1/(1−x−y−z) and let B be a small neighborhood
of the point (0, 0, 2). Find a Laurent series for f converging on Relog−1(B).
Hint: You can make 1/z, x/z, and y/z simultaneously less than 1
3 on Relog−1(B).
Theorem 6.4 is classical, but a complete proof is diﬃcult to ﬁnd in the liter-
ature so we provide one here. The technicalities that arise are not essential to
one’s understanding of analytic combinatorics, and the proof may be skipped
on a ﬁrst reading without much worry.
Proof of Theorem 6.4
Our argument requires the development of a few well-known facts about series
of analytic functions.
Proposition 6.5. If ( fk) is a sequence of analytic functions on a domain U ⊂
Cd and fk converges uniformly to a function f then f is analytic.
Proof
Let p ∈U and let D, T ⊂Cd be a polydisk and torus around p with
radii r ∈Rd
>0 such that D ⊂U. Without loss of generality, we may assume
that p = 0. If w ∈D then the multivariate Cauchy Integral Formula for power
series (Proposition A.28 in Appendix A) implies
f(w) = lim
k→∞fk(w) = lim
k→∞
 1
2πi
!d Z
T
fk(z)
(z1 −w1) · · · (zd −wd)dz
=
 1
2πi
!d Z
T
lim
k→∞
fk(w)
(z1 −w1) · · · (zd −wd)dz
=
 1
2πi
!d Z
T
f(z)
(z1 −w1) · · · (zd −wd)dz ,
138
Laurent series, amoebas, and convex geometry
where the interchange of limit and integral is permissible because the fact that
fk(z) →f(z) uniformly for z ∈T implies
fk(z)
(z1−w1)···(zd−wd) →
f(z)
(z1−w1)···(zd−wd)
uniformly for z ∈T. Expanding the ﬁnal integrand as a series in z gives
f(z)
(z1 −w1) · · · (zd −wd) =
X
i∈Nd
f(z)
z1 · · · zd
 w1
z1
!i1
· · ·
 wd
zd
!id
,
which converges absolutely and uniformly for z ∈T since |wk| < rk = |zk| for
each k. Thus, for all w ∈D we obtain the convergent series expansion
f(w) =
 1
2πi
!d Z
T

X
i∈Nd
f(z)
z1 · · · zd
 w1
z1
!i1
· · ·
 wd
zd
!iddz
=
X
i∈Nd

 1
2πi
!d Z
T
f(z)z−i−1dz
wi.
□
Remark 6.6. If f(z) is analytic at w and T is a suﬃciently small torus around
w then induction from the univariate setting implies
 1
2πi
!d Z
T
f(z)
(z1 −w1)i1+1 · · · (zd −wd)id+1 dz
= 1
i1!
 1
2πi
!d−1 Z
T ′
(∂i1z1 f)(w1, z2, . . . , zd)
(z2 −w2)i2+1 · · · (zd −wd)id+1 dz
...
= (∂i1z1 · · · ∂idzd f)(w)
i1! · · · id!
,
where T ′ is the projection of T onto its last d −1 coordinates and (as usual) ∂zk
denotes the partial derivative ∂/∂zk.
Proposition 6.7 (identity theorem). If f and g are analytic functions on a
connected domain D ⊂Cd which agree on an open subset of D then they agree
on all of D.
Proof
Let K ⊂D be the interior of the set where f and g agree. It is suﬃcient
to show J = K ∩D equals K, since then K is open and closed in the connected
set D, meaning K = D. To that end, pick z0 ∈J and ε > 0 suﬃciently small
so that the polydisk of radius (ε, . . . , ε) is contained in D. Since z0 ∈K there
exists a point z ∈K contained in the polydisk of radius (ε/2, . . . , ε/2) centered
at z0. Then f and g are analytic and agree in a neighborhood of z, so partial
derivatives of all orders exist for each function at z0 and each function is equal
6.1 Laurent series
139
to its power series expansion at z. Because the domains of convergence for
these power series contain z0, the functions f and g agree at z0 so z0 ∈K.
Since z0 ∈J was arbitrary, J equals K as desired.
□
Proposition 6.8 (logarithmic convexity of domains of convergence). Let F(z) =
P
r∈Zd arzr be a Laurent series with domain of convergence D. Then D =
Relog−1(B) for some open convex set B ⊂Rd.
Proof
Convergence depends on z only through the moduli of the compo-
nents, hence D is invariant under any rotation map zj 7→eiθzj. The domain of
convergence is thus the union of tori T(w) = Te(Relog w) and therefore equal
to Relog−1(B) for some B ⊂Rd. We claim that the open set B is the interior of
S =
(
x ∈Rd : sup
r∈Zd |ar|er·x is ﬁnite
)
.
First, if z ∈Relog−1(x) and P
r∈Zd |arzr| = P
r∈Zd |ar|er·x converges then
supr∈Zd |arer·x| is ﬁnite, so x ∈B implies x ∈S and (since it is open) B is
contained in the interior of S .
Now, suppose that x lies in the interior of S . Because we are considering ab-
solute convergence, we may split our series into 2d subseries depending on the
signs of its indices. In particular, using the notation v ⊙w = (v1w1, . . . , vdwd)
for coordinatewise vector product, we have
X
r∈Zd
|ar|er·x ≤
X
σ∈{±1}d
X
s∈Nd
|aσ⊙s| e(σ⊙s)·x ,
where the inequality reﬂects the fact that we have duplicated terms with indices
equal to zero (this simpliﬁes notation and does not aﬀect our argument as we
only need an upper bound). Because x lies in the interior of S , for ﬁxed σ ∈
{±1} and ε = (ε, . . . , ε) for suﬃciently small ε > 0 there exists some C > 0
such that
X
s∈Nd
|aσ⊙s| e(σ⊙s)·x =
X
s∈Nd
|aσ⊙s|e(σ⊙s)·(x+σ⊙ε) e−s·ε
≤sup
r∈Zd |ar|er·(x+σ⊙ε) ·
X
s∈Nd
e−s·ε
<
C
(1 −e−ε)d .
In particular, if x lies in the interior of S then P
r∈Zd |ar|er·x is ﬁnite, so x ∈B
and we have proven that B equals the interior of S . Furthermore, if x, y ∈S
140
Laurent series, amoebas, and convex geometry
then for any λ ∈[0, 1]
sup
r∈Zd |ar|er·(λx+(1−λ)y) ≤sup
r∈Zd |ar|λeλ(r·x) · sup
r∈Zd |ar|1−λe(1−λ)(r·y)
is ﬁnite, so λx + (1 −λ)y ∈S and S is convex. Since B is the interior of S , it
is also convex.
□
Proposition 6.9 (uniqueness of expansion). Let P
r∈Zd arzr be a Laurent se-
ries converging uniformly to zero on the torus Relog−1(x). Then ar = 0 for all
r ∈Zd.
Proof
Assume without loss of generality that x = 0, so that P
r∈Zd areir·y →
0 uniformly for y ∈[−π, π)d. For any ﬁxed r ∈Zd, uniform convergence
implies
ar =
X
s∈Zd
1
(2πi)d
Z
Te(x)
asei(s−r)·y dy
=
1
(2πi)d
Z
Te(x)
e−ir·y ·
X
s∈Zd
aseis·y dy
→
1
(2πi)d
Z
Te(x)
0 dy
= 0 ,
as desired.
□
We have now proven most of Theorem 6.4: part (1) is Proposition 6.8, while
part (2) follows from Proposition 6.5 because ι(F) is the uniform limit of the
series of partial sums. Uniqueness in part (3) is given by Proposition 6.9, so it
remains only to prove that (6.1) deﬁnes a Laurent series F(z) = P
r∈Zd arzr
converging uniformly to f.
By analyticity, the integral (6.1) deﬁning ar is independent of the value of
x ∈B deﬁning the chain of integration Te(x). Following an argument anal-
ogous to the proof of Proposition 6.8 above, for ε > 0 suﬃciently small
there exists a neighborhood N(x) of x in Rd and constant C > 0 such that
|arzr| ≤C exp(−ε|r|) for any z ∈Te(x′) with x′ ∈N(x). If K ⊂B is any
compact set, covering it with ﬁnitely many neighborhoods N(x) shows that
such a bound holds for all z ∈Relog−1(K). In particular, the series F converges
uniformly on compact subsets of D, so it is suﬃcient to prove that ι(F) = f on
a collection of sets with nonempty interior covering D.
Let B′ = Qd
j=1[log aj, log bj] be a product of closed rectangles with nonempty
interior strictly contained in B. Proposition A.29 in Appendix A gives a repre-
