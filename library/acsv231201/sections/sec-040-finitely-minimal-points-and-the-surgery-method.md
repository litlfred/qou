---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-040-finitely-minimal-points-and-the-surgery-method
section_title: "Finitely minimal points and the surgery method"
section_number: null
pages: 271-275
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Sections 9.3.1 and 9.3.2 complement the decomposition (9.9) by presenting
an algorithm to determine the integer coe ﬃcients kw for bivariate series, the
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
gularityw =w( ˆr).
Deﬁnition 9.16. For simplicity, we write v◦ = (v1,..., vd−1) for any vector
v∈Cd.
Our hypotheses imply that ˜Qzd(w) , 0, so the implicit function theorem
states that zd is locally analytically parametrized by z◦ nearw onV. More
speciﬁcally, if rd > 0 and we deﬁne ρ =|wd| then there exist a su ﬃciently
small real number δ >0, a neighborhoodN ofw◦ in T(w◦), and an analytic
function g :N→ C such that forz◦∈N ,
(i) Q(z◦, g(z◦)) = 0,
(ii) ρ≤| g(z◦)|<ρ +δ with equality only ifz◦ =w◦, and
(iii) Q(z◦, t), 0 if t, g(z◦) and|t− wd|<δ .
If rd < 0 then the same conditions hold exceptw being contributing means the
inequality in (ii) is replaced byρ−δ< |g(z◦)|≤ ρ.
Let C1 denote the circle of radiusρ−δ centered at the origin of the complex
plane and letC2 denote the circle of radiusρ+δ. The fact thatw is contributing,
254 Smooth point asymptotics
combined with the Cauchy integral formula, implies that the series coeﬃcients
of interest can be represented by an iterated integral
ar =

( 1
2πi
)d ∫
T(w◦)
[∫
C1
F(z◦, t)t−rd−1 dt
]
(z◦)−r◦ dz◦
z1··· zd−1
if rd > 0
( 1
2πi
)d ∫
T(w◦)
[∫
C2
F(z◦, t)t−rd−1 dt
]
(z◦)−r◦ dz◦
z1··· zd−1
if rd < 0
.
(9.10)
In either case, the key observation is that the inner integral is exponentially
smaller thanρ−rd away fromw◦. Indeed, if rd > 0 under our assumptions then
for each ﬁxedz◦ ,w◦ the function f (t) = F(z◦, t) has radius of convergence
greater thanρ and the inner integral isO((ρ+ε)−rd) for someε> 0; by continu-
ity of the radius of convergence, a singleε> 0 may be chosen for all compact
subsets of T(w◦) not containingw◦. Similarly, if rd < 0 then the inner integral
is O((ρ +ε)−rd) for someε∈ (−ρ, 0). Thus,
|wr (ar− I)|→ 0 (9.11)
exponentially quickly, whereI is any integral in (9.10) withT(w◦) replaced by
any neighborhood ofw◦ in T(w◦). We now take the neighborhood deﬁning I
to be the setN on which the properties (i)–(iii) for the parametrization g hold,
and compare the inner integral in (9.10) to one pushed ‘beyond’ the singular
set. Note that in general we cannot do this without ﬁrst ‘cutting out’ the small
neighborhoodN.
Assume that rd > 0 and compare
I =
( 1
2πi
)d ∫
N
[∫
C1
F(z◦, t)t−rd−1 dt
]
(z◦)−r◦ dz◦
z1··· zd−1
to the integral
I′ =
( 1
2πi
)d ∫
N
[∫
C2
F(z◦, t)t−rd−1 dt
]
(z◦)−r◦ dz◦
z1··· zd−1
with the inner contourC1 replaced by C2. Because the points onC2 have larger
modulus thanρ,
⏐⏐⏐wrI′⏐⏐⏐→ 0 (9.12)
exponentially quickly. Furthermore, our assumption of strict minimality im-
plies that the common inner integrand of I and I′ has a unique pole in the
annulusρ−δ≤| t|≤ ρ +δ, occurring at t = g(z◦). If
Ψ(z◦) = Res
(
F(z◦, t)t−rd−1 ; t = g(z◦)
)
(9.13)
9.1 Finitely minimal points and the surgery method 255
then the di ﬀerence of I and I′ can be computed in terms of Ψ. If rd < 0 the
argument is the same, with the roles of C1 and C2 reversed, changing the sign
in front of the residue integral. Ultimately, we obtain the following, which may
be thought of as the computational analog of the fact that one can integrate in
relative homology at the expense of an exponentially small error (see Proposi-
tion B.10 in Appendix B).
Theorem 9.17 (reduction to residue integral). Let
χ = I− I′ =− sgn(rd)
(2πi)d−1
∫
N
Ψ(z◦)(z◦)−r◦ dz◦
z1··· zd−1
, (9.14)
with Ψ given by (9.13). Assuming the hypotheses of Theorem 9.5 whenW(r) =
{w( ˆr)},
|wr (ar−χ)|→ 0
exponentially in|r|, uniformly asr→∞ with ˆr varying overM.
The fact that we can obtain explicit asymptotic expansions is a consequence
of the following result.
Lemma 9.18. Under the hypotheses of Theorem 9.5, the residue Ψ has the
form Ψ(z◦) =−g(z◦)−rdΨp(z◦) where
Ψp(z◦) =
p−1∑
k=0
(rd + 1)(p−k−1)
k!(p− k− 1)! Rk(z◦). (9.15)
Here (a)(b) = a(a− 1)··· (a− b + 1) and
Rk(z◦) = (−g(z◦))−p+k lim
zd→g(z◦)
∂k
d ((zd− g(z◦))pF(z)).
In particular, Ψp is a polynomial of degree p− 1 in rd with leading coeﬃcient
(−1)pg(z◦)−p p P(z◦, g(z◦))
(∂p
d Q)(z◦, g(z◦)).
Proof Our assumptions imply that F(z◦, t) has a pole of order p at t = g(z◦),
and (9.15) comes from the classic residue formula
Res
(
F(z◦, t)t−rd−1 ; t = g(z◦)
)
= 1
(p− 1)! lim
zd→g(z◦)
∂p−1
d
(
(zd− g(z◦))pF(z)z−rd−1
d
)
together with Leibniz’s rule for derivatives. The leading term inrd comes from
the summand where k = 0. □
Remark 9.19. The results of this section only require that F be meromorphic
in a neighborhood of the domain of convergenceD. If F is locally the ratio of
analytic functions P and Q in a neighborhood of w then all formulae are still
256 Smooth point asymptotics
valid, provided ˜Q is interpreted to be a square-free factorization in the local
ring of germs of analytic functions (see Deﬁnition 10.42 below).
Exercise 9.5. Let F(x, y) = 1/(ex + ey− 1). What can you deduce from Theo-
rem 9.5 about the power series coeﬃcients of F?
Proof of Theorem 9.5
Making the change of variables z j = w jeiθ j for 1≤ j≤ d− 1 turns χ into a
saddle point integral
χ = sgn(rd)
(2π)d−1w−r
∫
N′
A(θ)e−|rd|φ(θ)dθ (9.16)
with amplitude A(θ) = Ψp
(
w◦eiθ
)
for Ψp deﬁned in (9.15) and phase
φ(θ) = rd
|rd| log

g
(
w◦eiθ
)
wd
 + i(r◦·θ)
|rd|
= sgn(rd)
log

g
(
w◦eiθ
)
wd
 + i(r◦·θ)
rd

in the variablesθ = (θ1,...,θ d−1), where
(
w◦eiθ
)
=
(
w1eiθ1,..., wd−1eiθd−1
)
and
N′ is a neighborhood of the origin inRd. Lemma 8.21 implies that this integral
satisﬁes the conditions necessary to apply Theorem 5.2 in Chapter 5 (note that
the real part of φ has a strict minimum at the origin by our conditions on g).
Lemma 8.22 applied to sgn(rd)φ simpliﬁes the Hessian and ﬁnishes the proof.
Modiﬁcation for ﬁnitely minimal points
Whenw( ˆr) is ﬁnitely minimal then the Cauchy integral decays exponentially
away from any element ofW( ˆr). We can thus restrict the domain of integration
to a disjoint union of neighborhoods Nk around the elements of W( ˆr). The
residue computation in Theorem 9.17 results in a sum as k varies of integrals
over neighborhoodsNwk. The asymptotic contributions of each of the integrals
in the sum can be computed in the same way as the strictly minimal case.
Modiﬁcation under strong torality hypothesis
Because our residue computations are so explicit, they also hold under the fol-
lowing strong torality hypothesis. This hypothesis is important when studying
generating functions whose singularities have many symmetries, for instance
in the case of quantum random walks (see Exercise 9.12).
