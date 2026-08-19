---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-004-6-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 6
pages: 5-7
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
contour integral expression for J ′
K(r) is the following. In the upper half plane we
approximate tan by √−1 and by −√−1 in the lower half plane. Further we ap-
proximateSγ by the above expression involving only the dilogarithm. In Appendix
B we prove the required estimates which allows us to do these approx imations and
we end up with the following formula for the leading order large r asymptotics
J ′
K(r) ∼r2
∫ 1−ǫ
ǫ
erΦ(x)dx, (1.3)
where ǫ< 1/(4r) is a small positive parameter and
Φ(x) = 1
2π√−1
(
Li2(e−2π√−1x) − Li2(e2π√−1x)
)
.
Now we simply analyze the integral on the right-hand side of (1.3) by t he saddle
point method. This consists of ﬁnding the stationary points of Φ and also the di-
rections of steepest descent, see e.g. [6]. (In this paper we use cr itical point and
stationary point interchangeably to mean a point in which the derivat ive is zero.)
This analysis leads to two interesting results. Firstly, the search fo r stationary
points leads to the hyperbolicity equation for the complement of the ﬁgure 8 knot
in the 3–sphere. Recall that this complement can be decomposed int o two ideal
hyperbolic tetrahedra each parametrized by a certain complex num ber. This de-
composition then deﬁnes a hyperbolic structure on the complement exactly when
the two parameters are equal and satisfy the hyperbolicity equat ion.
Secondly, we ﬁnd that the value of the phase function in the relevan t stationary
point (there is only one such point in this case) is equal to the hyperb olic volume
of the knot complement (divided by 2 π), hence the leading asymptotics of J ′
K(r) is
determined by this volume.
These phenomena were ﬁrst observed by Kashaev [14] and have be en conjectured
by Thurston [32] and Yokota [35] to be generally true for hyperbolic knots (see
Remark 2).
Ultimately our asymptotic analysis leads to the following
Theorem 1. The leading order large r asymptotics of the colored Jones polynomial
evaluated at the top color is given by
J ′
K(r) ∼ 3−1/4r3/2 exp
(r
2π Vol(K)
)
.
As a corollary we obtain the volume conjecture for the ﬁgure 8 knot . We note
that none of the proofs so far given in the literature for the volume conjecture for
the ﬁgure 8 knot have been able to see the ﬁner details of the asymp totic behaviour,
namely the polynomial part 3 −1/4r3/2.
After completion of this paper we have been informed that D. Zagier has com-
puted the full asymptotic expansion of J ′
K(r) by using the Euler–Maclaurin sum-
mation formula, however his techniques seem not applicable to the ca lculation of
the large r asymptotics of τr(Mp/q).
6 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Let us now return to the study of the large r asymptotics of the quantum in-
variantτr(Mp/q). We expect that an analysis of the expression (1.2) paralleling our
analysis of J ′
K(r) should be applicable. I.e. tan and cot should be approximated by
±√−1 depending on the signs of Im( y) and Im(x) and ˜fp,q,r(x,y ) by an appropriate
expression involving the dilogarithm for some deformation of the rele vant part of
Cr ×Cr. We have partial analytic results supporting this.
To be more speciﬁc we propose the following analog of (1.3) for the qu antum
invariant. Let d be the inverse of p modq and let (a,b ) ∈ {0, 1}2 andn ∈ Z. Deﬁne
Φn(x,y ) = −dn2
q − p
4qx2 + n
qx −xy + 1
4π2
(
Li2(e2πi(x+y)) − Li2(e2πi(x−y))
)
,
and
Φa,b
n (x,y ) = a(x +y) +b(x −y) + Φ n(x,y ). (1.4)
Finally, let
S = {(x,y ) ∈ R × C |e2πiy ∈] − ∞, 0[ }. (1.5)
Thus S is the union of inﬁnitely many planes, namely the ones characterized b y
x ∈ R and Re(y) ∈ 1
2 + Z.
Conjecture 2. There exist surfaces ˜Σµ,ν,n
a,b ⊂ C2 for (a,b ) ∈ { 0, 1}2, n ∈ Z/|q|Z
and (µ,ν ) ∈ {±1}2 such that the leading order large r asymptotics of the quantum
invariant is given by
¯τr(Mp/q) ∼ Cr
∑
n∈Z/|q|Z
∑
(a,b)∈{0,1}2
∑
(µ,ν)∈{±1}2
µν (1.6)
×
∫
˜Σ µ,ν,n
a,b
˜gn(x)e2πirΦ a,b
n (x,y)dxdy, (1.7)
where C is a constant only depending on p and q and ˜gn is some simple r–
independent function of x ∈ C. If p/q ⁄= 0 the surfaces ˜Σµ,ν,n
a,b ⊂ C2 can be chosen
such that any critical point of Φ a,b
n belonging to ˜Σµ,ν,n
a,b also belongs to the set S.
Please see Conjecture 3 for the more detailed version of this conje cture, including
the precise formula for ˜gn. (We have here for sign-reasons switched to the complex
conjugate invariant ¯τr(Mp/q) =
τr(Mp/q) = τr(M−p/q).) In case p/q = 0 our results
show that we have to include critical points not belonging to S in our surfaces
˜Σµ,ν,n
a,b , see Appendix C.
We now proceed by making an asymptotic analysis of the right-hand s ide of
(1.6) using the saddle point method like in our analysis of (1.3). Thus we need to
analyze integrals of the form
Iµ,ν,n
a,b =
∫
˜Σ µ,ν,n
a,b
˜gn(x)e2πirΦ a,b
n (x,y)dxdy. (1.8)
Again we have to determine the stationary points of Φ a,b
n and the values of Φ a,b
n in
the relevant stationary points. The main idea behind the saddle point method is
