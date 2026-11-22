---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-016-42-deviations-at-scale-otn
section_title: "Deviations at scale O(tn)"
section_number: 4.2
pages: 29-30
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
4.2. Deviations at scale O(tn).
Theorem 4.3. Suppose φ non-lattice, and consider as before a sequence (Xn)n∈N that con-
verges mod-φ on a band S(c,d) with c < 0 < d. If x ∈(η′(0), η′(d)), then
P[Xn ≥tnx] = exp(−tnF(x))
h
p
2πtnη′′(h)
ψ(h) (1 + o(1))
where as usual h is deﬁned by the implicit equation η′(h) = x.
Remark 4.4. By applying the result to (−Xn)n∈N, one gets similarly
P[Xn ≤tnx] = exp(−tnF(x))
|h|
p
2πtnη′′(h)
ψ(h) (1 + o(1))
for x ∈(η′(c), η′(0)), with h deﬁned by the implicit equation η′(h) = x.
Remark 4.5. Theorem 4.3 should be compared with [Hwa96, Theorem 1], which studies
another regime of deviations in the mod-φ setting, namely, when h goes to zero (or
equivalently, x →η′(0)). We shall also look at this regime in our Theorem 4.8.
Remark 4.6. The main difference between Theorems 3.4 and 4.3 is the replacement of
the factor ψ(h)/(1 −e−h) by ψ(h)/h; the same happens with Bahadur-Rao’s estimates
when going from lattice distributions to non-lattice distributions.
Lemma 4.7. Let (Xn)n∈N be a sequence of random variables that converges mod-φ with pa-
rameters (tn)n∈N and limiting function ψ, on a strip S(c,d) that does not necessarily contain 0.
For h ∈(c, d), we make the exponential change of measure
Q[dy] =
ehy
ϕXn(h) P[Xn ∈dy],
and denote eXn a random variable following this law. The sequence ( eXn)n∈N converges mod-eφ,
where eφ is the inﬁnitely divisible distribution with characteristic function eη(z+h)−η(h). The
parameters of this new mod-convergence are again (tn)n∈N, and the limiting function is
eψ(z) = ψ(z + h)
ψ(h)
.
The new mod-eφ convergence occurs in the strip S(c−h,d−h).
Proof. Obvious since ϕ eXn(z) = ϕXn(z + h)/ϕXn(h).
□
Proof of Theorem 4.3. Fix h ∈(c, d), and consider the sequence ( eXn)n∈N of Lemma 4.7.
All the assumptions of Proposition 4.1 are satisﬁed, so, the distribution function Fn(u)
of
eXn −tnη′(h)
p
tnη′′(h)
is
Gn(u) =
Z u
−∞
 
1 +
ψ′(h)
ψ(h)
p
tnη′′(h)
y +
η′′′(h)
p
tn(η′′(h))3 (y3 −3y)
!
g(y) dy
30
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
up to a uniform o(1/√tn). Then,
P[Xn ≥tnη′(h)] =
Z ∞
y=tnη′(h) ϕXn(h) e−hy Q(dy)
= ϕXn(h)
Z ∞
u=0 e−h

tnη′(h)+√
tnη′′(h) u

dFn(u)
= ψn(h) e−tnF(x)
Z ∞
u=0 e−h√
tnη′′(h) u dFn(u), (as F(x) = hη′(h) −η(h)).
To compute the integral I, we choose the primitive Fn(u) −Fn(0) of dFn(u) that van-
ishes at u = 0, and we make an integration by parts. Notice that we now need h > 0
(hence, x > η′(0)) in order to manipulate some of the terms below:
I = h
q
tnη′′(h)
Z ∞
u=0 e−h√
tnη′′(h) u (Fn(u) −Fn(0)) du
= h
q
tnη′′(h)
Z ∞
u=0 e−h√
tnη′′(h) u

Gn(u) −Gn(0) + o
 1
√tn

du
≃h
q
tnη′′(h)
ZZ
0≤y≤u
e−h√
tnη′′(h) u
 
1 +
ψ′(h) y
ψ(h)
p
tnη′′(h) + η′′′(h) (y3 −3y)
p
tn(η′′(h))3
!
g(y) dy du
≃
Z ∞
y=0 e−h√
tnη′′(h) y
 
1 +
ψ′(h)
ψ(h)
p
tnη′′(h)
y +
η′′′(h)
p
tn(η′′(h))3 (y3 −3y)
!
g(y) dy
≃e
h2 tnη′′(h)
2
√
2π
Z ∞
y=0 e−(y+h√
tnη′′(h))2
2
 
1 +
ψ′(h)
ψ(h)
p
tnη′′(h)
y +
η′′′(h)
p
tn(η′′(h))3 (y3 −3y)
!
dy,
where on the three last lines the symbol ≃means that the remainder is a o((tn)−1/2).
By Lemma 2.7, (3), the only contribution in the integral that is not a o((tn)−1/2) is
e
h2 tnη′′(h)
2
√
2π
Z ∞
y=0 e−(y+h√
tnη′′(h))2
2
dy =
1
h
p
2πtnη′′(h) + o
 1
√tn

.
This ends the proof since ψn(h) →ψ(h) locally uniformly.
□
