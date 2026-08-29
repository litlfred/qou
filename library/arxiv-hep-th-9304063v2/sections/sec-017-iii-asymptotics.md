---
doc_id: arxiv-hep-th-9304063v2
doc_title: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗"
section_id: sec-017-iii-asymptotics
section_title: "ASYMPTOTICS"
section_number: III
pages: 12-14
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
doc_brief: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗ — 26 sections: INTRODUCTION AND STATEMENT OF RESU; KN(; (α2 −aj + 2v)q2"
---
A. Asymptotics of the σ-equation
In the case of the ﬁnite N ensemble and α = 0, Edelman [7,8] and Forrester [11] (by a direct evaluation of the
integrals deﬁning the probability EN(0; s)) has shown that E(0; s) is exactly equal to e−s/4. From this it follows, for
α = 0 and λ = 1, that σ(s; 1) = s/4. For general α and λ = 1 it is therefore reasonable to assume an asymptotic
expansion of the form:
σ(s; 1) = c1s + c2s1/2 + c3 + c4s−1/2 + · · · ,
s →∞.
Substituting this into the diﬀerential equation (1.21) results in equations that uniquely determine the coeﬃcients cj
once a choice in the square root
√
α2 is made. Since for α = ∓1
2 our asymptotic expansion of E(0; s) must agree with
those of Dyson (recall (1.3)), we see that we must choose the square root −α −α. A calculation then gives
σ(s; 1) = s
4 −α
2 s1/2 + α2
4 + α
16s−1/2 + α2
16 s−1 + α
256(16α2 + 9)s−3/2 + α2
64 (4α2 + 9)s−2
+ α
2048(128α4 + 720α2 + 225)s−5/2 + · · ·
s →∞,
(3.1)
from which (1.24) follows.
B. Asymptotics via the commuting diﬀerential operator
Throughout this section we take λ = 1. The operator K, when rescaled to act on (0, 1) instead of (0, s), has kernel
s K(sx, sy). By (2.2) this is equal to
s
4
Z 1
0
φ(sxt) φ(syt) dt,
12
and so K (rescaled, as it will be throughout this section), is the square of the operator on (0, 1) with kernel
J(x, y) =
√s
2 φ(sxy) =
√s
2 Jα(√sxy).
This function satisﬁes the diﬀerential equation
x2Jxx + xJx + (sxy
4
−α2
4 )J = 0.
(3.2)
The operator J will commute with a diﬀerential operator
L = d
dxα(x) d
dx + β(x)
if α(0) = α(1) = 0 and if
α(y)Jyy + α′(y)Jy + β(y)J = α(x)Jxx + α′(x)Jx + β(x)J.
If we use (3.2) we see that this will be satisﬁed if
−α(x)

x−1Jx + ( sy
4x −α2
4x2 )

+ α′(x)Jx + β(x)J
= the same expression with x and y interchanged.
Equating the terms involving the ﬁrst derivatives of J gives
(α′(x) −x−1α(x))Jx = (α′(y) −y−1α(y))Jy.
But x Jx = y Jy, so the above will hold if
x−1(α′(x) −x−1α(x)) = y−1(α′(y) −y−1α(y)).
This is satisﬁed if α(x) is a quadratic without constant term and, of course, we choose
α(x) = x(1 −x).
What is required of β, then, is seen to be
β(x) −x(1 −x)( sy
4x −α2
4x2 ) = β(y) −y(1 −y)(sx
4y −α2
4y2 ),
which is satisﬁed by
β(x) = −α2
4x −sx
4 .
We write the diﬀerential equation, for which the eigenfunctions f(x) are the eigenfunctions of J, as
(x(1 −x)f ′x))′ + (µ√s −α2
4x −sx
4 )f(x) = 0.
(3.3)
The boundary conditions are that f(x) be bounded as x →1 and that f(x) be asymptotic to a constant times xα/2
as x →0. The reason we wrote the eigenvalues as we did is that for each i the µ corresponding to the i’th largest
eigenvalue is bounded as s →∞. This is easily seen by an oscillation argument. So we assume i is ﬁxed and proceed
to ﬁnd the asymptotics of the corresponding eigenfunction f(x) as s →∞. We assume it normalized so that
f(x) ∼xα/2 as x →0.
(3.4)
13
