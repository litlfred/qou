---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-018-b3-asymptotics-of-faddeevs-dilogarithm-for-imtau
section_title: "B.3. Asymptotics of Faddeev's dilogarithm for Im(tau) near 0"
section_number: null
pages: 40-43
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
asymptotics as we cross the real numbers we use the following equality for Im(z + τ) > 0
and Im(z/τ) > 0 along with Re(−√τ −1/√τ) < Re(z/√τ) < 0
Φ(z; τ) =
(qe(z); q)∞
(e(z/τ); eq)∞
= exp

∞
X
k=1
e(kz)
k(q−k −1) −e(kz/τ)
k(eqk −1)

= exp
 Z
i√τR+ε√τ
e((z + 1 + τ)w/τ)
(e(w) −1)(e(w/τ) −1)
dw
w

,
(122)
for some small ε > 0. The various regions where the expression for Φ(τz; τ) as τ tends to
inﬁnity are depicted in Figure 32.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS
41
The asymptotics of Faddeev’s quantum dilogarithm in the lower half plane can be carried out
by a completely similar analysis as in the upper half plane using the formula for Im(τ) < 0
given by
Φ(z; τ) = (eq−1e(z/τ); eq−1)∞
(e(z); q−1)∞
.
(123)
In the upper and lower half planes there is one technicality that when τ is very close to the
reals or argument comparable with ε (the bound for z from the branch cuts) we ﬁnd that for z
in a neighbourhood of the interval [−1+2ε, −2ε] the methods we have previously mentioned
fail to produce the asymptotics. We also have the issue that the previous methods do not
work when τ ∈R>0. These two problems can be dealt with by using Faddeev’s original
formula given in Equation (122).
Lemma B.5. Suppose that τ ∈C\R≤0 and ε ∈R>0. Then as τ →∞with ﬁxed argument
bounded by ε and z bounded away from Cθ by ε with θ = arg(−1/τ) ∈(π −ε, π + ε) there
exists a constant C ∈R>0 such that

Φ(zτ; τ) −e

Dθ(z)τ + 1
2D′
θ(z) +
K
X
k=2
Bk
k!
(2πi)k−2
τ k−1
Li2−k(e(z))


 < C K! ε−K |τ|−K . (124)
Proof. By deforming the contour to inﬁnity for Im(z) > 0 we have
Z
i√τR+ε1
√τ
e(zw)
(e(−w) −1)
dw
w2−k =
∞
X
ℓ=1
e(ℓz)
ℓ2−k
= Li2−k(e(z)) ,
(125)
while for Im(z) < 0 we can deform in the other direction and ﬁnd that for k > 1 we have
Z
i√τR+ε1
√τ
e(zw)
(e(−w) −1)
dw
w2−k = −δk,2 −
∞
X
ℓ=1
e(−ℓz)
(−ℓ)2−k
= Li2−k(e(z)) ,
(126)
While for k = 0 we have
Z
i√τR+ε1
√τ
e(zw)
(e(−w) −1)
dw
w2−k = −(2πi)2(1
2z(z + 1) + 1
12) −
∞
X
ℓ=1
e(−ℓz)
(−ℓ)2
= Dθ(z) , (127)
and k = 1 we have
Z
i√τR+ε1
√τ
e(zw)
(e(−w) −1)
dw
w2−k = −(2πi)(z + 1
2) +
∞
X
ℓ=1
e(−ℓz)
ℓ
= D′
θ(z) .
(128)
Therefore, these equations hold for all z in our region. We can use these equations to deduce
our desired asymptotics. We want to compute the asymptotics of the integral
Z
C
e(zw)
(e(−w) −1)(e(−w/τ) −1)
dw
w ,
(129)
where for z with Re((ε1 −1)√τ −1/√τ) < Re(z√τ) < −ε1Re(√τ) we can take C =
i√τR + ε1
√τ. We can deform the contour of this integral so that for z bounded away from
Cθ by ε the integral converges. This is given up to exponentially small terms by the same
42
VERONICA FANTINI AND CAMPBELL WHEELER
integral cut oﬀwith |w| < |√τ|. Then by Taylor’s theorem there exists a constant C1 such
that for |w| < |√τ| we have

1
e(−w/τ) −1 −
K
X
k=0
Bk
k!
−2πiw
τ
k−1

 ≤C1

2πw
τ

K
(130)
Therefore, we ﬁnd that

Z
C

e(zw)
(e(−w) −1)(e(−w/τ) −1) −
e(zw)
(e(−w) −1)
K
X
k=0
Bk
k!
−2πiw
τ
k−1dw
w

< C1 (2π)K|τ|−K
Z
C

e(zw)
w1−K(e(−w) −1)

dw .
(131)
This ﬁnal integral can be split into two parts depending on which dominates max{e(−w), 1}.
The size of one of these integrals is then approximated by a constant times an integral of
the form
Z ∞
0
exp(−2πεw)wK−1dw = (2πε)−K(k −1)!
(132)
The other integral has a similar bound. Therefore, we see that there is a constant C such
that

Z
i√τR+ε1
√τ

e(zw)
(e(−w) −1)(e(−w/τ) −1) −
e(zw)
(e(−w) −1)
K
X
k=0
Bk
k!
−2πiw
τ
k−1dw
w

< C K! ε−K |τ|−K.
(133)
□
Theorem B.6. Suppose that τ ∈C\R≤0 and ε ∈R>0.
Then as |τ| →∞with ﬁxed
argument and z bounded away from Cθ by ε with θ = arg(−1/τ) ∈(0, 2π) there exists a
constant C ∈R>0 such that

Φ(zτ; τ) −e

Dθ(z)τ + 1
2D′
θ(z) +
K
X
k=2
Bk
k!
(2πi)k−2
τ k−1
Li2−k(e(z))


 < C ε−K K! |τ|−K . (134)
Proof. The proof follows by combining the results of Lemma B.1, Lemma B.3 and Lemma B.5.
□
Corollary B.7. If Im(z) > 0 and −arg(z) + π/2 < arg(τ) < arg(z + 1) + π/2, Im(z) < 0
and −π/2 −arg(z + 1) < arg(τ) < −arg(z) −π/2, or z ∈(−1, 0) and τ ∈C\R≤0, then
Φ(zτ; τ) is the Borel–Laplace resummation of its asymptotics.
Proof. As τ →∞we have

Φ(zτ; τ) −e

Dθ(z)τ + 1
2D′
θ(z) +
K
X
k=2
Bk
k!
(2πi)k−2
τ k−1
Li2−k(e(z))


 < C ε−K K! |τ|−K . (135)
Therefore, we see that Φ(zτ, τ) is the Borel–Laplace resummation of its asymptotics for τ in
these cones.
□
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS
