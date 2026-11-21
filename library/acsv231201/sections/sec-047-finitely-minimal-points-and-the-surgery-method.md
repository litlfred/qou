---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-047-finitely-minimal-points-and-the-surgery-method
section_title: "Finitely minimal points and the surgery method"
section_number: null
pages: 271-275
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
253
Sections 9.3.1 and 9.3.2 complement the decomposition (9.9) by presenting
an algorithm to determine the integer coeﬃcients kw for bivariate series, the
only case beyond minimal points and rational functions with linear denomi-
nators where we know a general strategy for their calculation. Section 9.3.3
also gives an asymptotic formula for degenerate critical points in the bivariate
case. Finally, Section 9.4 ends this chapter with some related results, including
explicit formulae for higher-order terms and a coordinate-free formula (9.23)
in terms of geometric invariants such as the Gaussian curvature.
9.1 Finitely minimal points and the surgery method
To prove Theorem 9.5 we show that the Cauchy integral representation for se-
ries coeﬃcients is negligible outside a small neighborhood of w, reduce to a
lower-dimensional integral using a univariate residue computation, parametrize
the simpliﬁed integral to obtain a saddle point integral, and apply the theorems
of Chapter 5 to the result.
Localization and residue
We start by assuming that W( ˆr) contains a strictly minimal contributing sin-
gularity w = w( ˆr).
Deﬁnition 9.16. For simplicity, we write v◦= (v1, . . . , vd−1) for any vector
v ∈Cd.
Our hypotheses imply that ˜Qzd(w) , 0, so the implicit function theorem
states that zd is locally analytically parametrized by z◦near w on V. More
speciﬁcally, if rd > 0 and we deﬁne ρ = |wd| then there exist a suﬃciently
small real number δ > 0, a neighborhood N of w◦in T(w◦), and an analytic
function g : N →C such that for z◦∈N,
(i) Q(z◦, g(z◦)) = 0,
(ii) ρ ≤|g(z◦)| < ρ + δ with equality only if z◦= w◦, and
(iii) Q(z◦, t) , 0 if t , g(z◦) and |t −wd| < δ.
If rd < 0 then the same conditions hold except w being contributing means the
inequality in (ii) is replaced by ρ −δ < |g(z◦)| ≤ρ.
Let C1 denote the circle of radius ρ −δ centered at the origin of the complex
plane and let C2 denote the circle of radius ρ+δ. The fact that w is contributing,
254
Smooth point asymptotics
combined with the Cauchy integral formula, implies that the series coeﬃcients
of interest can be represented by an iterated integral
ar =

 1
2πi
!d Z
T(w◦)
"Z
C1
F(z◦, t)t−rd−1 dt
#
(z◦)−r◦
dz◦
z1 · · · zd−1
if rd > 0
 1
2πi
!d Z
T(w◦)
"Z
C2
F(z◦, t)t−rd−1 dt
#
(z◦)−r◦
dz◦
z1 · · · zd−1
if rd < 0
.
(9.10)
In either case, the key observation is that the inner integral is exponentially
smaller than ρ−rd away from w◦. Indeed, if rd > 0 under our assumptions then
for each ﬁxed z◦, w◦the function f(t) = F(z◦, t) has radius of convergence
greater than ρ and the inner integral is O((ρ+ε)−rd) for some ε > 0; by continu-
ity of the radius of convergence, a single ε > 0 may be chosen for all compact
subsets of T(w◦) not containing w◦. Similarly, if rd < 0 then the inner integral
is O((ρ + ε)−rd) for some ε ∈(−ρ, 0). Thus,
|wr (ar −I)| →0
(9.11)
exponentially quickly, where I is any integral in (9.10) with T(w◦) replaced by
any neighborhood of w◦in T(w◦). We now take the neighborhood deﬁning I
to be the set N on which the properties (i)–(iii) for the parametrization g hold,
and compare the inner integral in (9.10) to one pushed ‘beyond’ the singular
set. Note that in general we cannot do this without ﬁrst ‘cutting out’ the small
neighborhood N.
Assume that rd > 0 and compare
I =
 1
2πi
!d Z
N
"Z
C1
F(z◦, t)t−rd−1 dt
#
(z◦)−r◦
dz◦
z1 · · · zd−1
to the integral
I′ =
 1
2πi
!d Z
N
"Z
C2
F(z◦, t)t−rd−1 dt
#
(z◦)−r◦
dz◦
z1 · · · zd−1
with the inner contour C1 replaced by C2. Because the points on C2 have larger
modulus than ρ,

wrI′

 →0
(9.12)
exponentially quickly. Furthermore, our assumption of strict minimality im-
plies that the common inner integrand of I and I′ has a unique pole in the
annulus ρ −δ ≤|t| ≤ρ + δ, occurring at t = g(z◦). If
Ψ(z◦) = Res

F(z◦, t)t−rd−1 ; t = g(z◦)

(9.13)
9.1 Finitely minimal points and the surgery method
255
then the diﬀerence of I and I′ can be computed in terms of Ψ. If rd < 0 the
argument is the same, with the roles of C1 and C2 reversed, changing the sign
in front of the residue integral. Ultimately, we obtain the following, which may
be thought of as the computational analog of the fact that one can integrate in
relative homology at the expense of an exponentially small error (see Proposi-
tion B.10 in Appendix B).
Theorem 9.17 (reduction to residue integral). Let
χ = I −I′ = −sgn(rd)
(2πi)d−1
Z
N
Ψ(z◦)(z◦)−r◦
dz◦
z1 · · · zd−1
,
(9.14)
with Ψ given by (9.13). Assuming the hypotheses of Theorem 9.5 when W(r) =
{w( ˆr)},
|wr (ar −χ)| →0
exponentially in |r|, uniformly as r →∞with ˆr varying over M.
The fact that we can obtain explicit asymptotic expansions is a consequence
of the following result.
Lemma 9.18. Under the hypotheses of Theorem 9.5, the residue Ψ has the
form Ψ(z◦) = −g(z◦)−rdΨp(z◦) where
Ψp(z◦) =
p−1
X
k=0
(rd + 1)(p−k−1)
k!(p −k −1)!Rk(z◦).
(9.15)
Here (a)(b) = a(a −1) · · · (a −b + 1) and
Rk(z◦) = (−g(z◦))−p+k
lim
zd→g(z◦) ∂k
d ((zd −g(z◦))pF(z)) .
In particular, Ψp is a polynomial of degree p −1 in rd with leading coeﬃcient
(−1)pg(z◦)−p p
P(z◦, g(z◦))
(∂p
dQ)(z◦, g(z◦)).
Proof
Our assumptions imply that F(z◦, t) has a pole of order p at t = g(z◦),
and (9.15) comes from the classic residue formula
Res

F(z◦, t)t−rd−1 ; t = g(z◦)

=
1
(p −1)!
lim
zd→g(z◦) ∂p−1
d

(zd −g(z◦))pF(z)z−rd−1
d

together with Leibniz’s rule for derivatives. The leading term in rd comes from
the summand where k = 0.
□
Remark 9.19. The results of this section only require that F be meromorphic
in a neighborhood of the domain of convergence D. If F is locally the ratio of
analytic functions P and Q in a neighborhood of w then all formulae are still
256
Smooth point asymptotics
valid, provided ˜Q is interpreted to be a square-free factorization in the local
ring of germs of analytic functions (see Deﬁnition 10.42 below).
Exercise 9.5. Let F(x, y) = 1/(ex + ey −1). What can you deduce from Theo-
rem 9.5 about the power series coeﬃcients of F?
Proof of Theorem 9.5
Making the change of variables zj = w jeiθj for 1 ≤j ≤d −1 turns χ into a
saddle point integral
χ = sgn(rd)
(2π)d−1 w−r
Z
N′ A(θ)e−|rd| φ(θ)dθ
(9.16)
with amplitude A(θ) = Ψp

w◦eiθ
for Ψp deﬁned in (9.15) and phase
φ(θ) = rd
|rd| log

g

w◦eiθ
wd
+ i(r◦· θ)
|rd|
= sgn(rd)
log

g

w◦eiθ
wd
+ i(r◦· θ)
rd

in the variables θ = (θ1, . . . , θd−1), where

w◦eiθ
=

w1eiθ1, . . . , wd−1eiθd−1
and
N′ is a neighborhood of the origin in Rd. Lemma 8.21 implies that this integral
satisﬁes the conditions necessary to apply Theorem 5.2 in Chapter 5 (note that
the real part of φ has a strict minimum at the origin by our conditions on g).
Lemma 8.22 applied to sgn(rd)φ simpliﬁes the Hessian and ﬁnishes the proof.
Modiﬁcation for ﬁnitely minimal points
When w( ˆr) is ﬁnitely minimal then the Cauchy integral decays exponentially
away from any element of W( ˆr). We can thus restrict the domain of integration
to a disjoint union of neighborhoods Nk around the elements of W( ˆr). The
residue computation in Theorem 9.17 results in a sum as k varies of integrals
over neighborhoods Nwk. The asymptotic contributions of each of the integrals
in the sum can be computed in the same way as the strictly minimal case.
Modiﬁcation under strong torality hypothesis
Because our residue computations are so explicit, they also hold under the fol-
lowing strong torality hypothesis. This hypothesis is important when studying
generating functions whose singularities have many symmetries, for instance
in the case of quantum random walks (see Exercise 9.12).
