---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-009-32-deviations-at-the-scale-otn
section_title: "Deviations at the scale O(tn)"
section_number: 3.2
pages: 16-21
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
Lemma 3.3. Let X be a Z-valued random variable whose generating functionϕX(z) = E[ezX ]
converges absolutely in the stripS(c,d), with c < 0 < d. For k∈ Z,
∀h∈ (c, d), P[X = k] = 1
2π
∫ π
−π
e−k(h+iu) ϕX(h + iu) du;
∀h∈ (0, d), P[X≥ k] = 1
2π
∫ π
−π
e−k(h+iu)
1− e−(h+iu) ϕX(h + iu) du.
Proof. Since
ϕX(h + iu) = ∑
k∈Z
P[X = k] ek(h+iu),
MOD-φ CONVERGENCE, I 17
P[X = k] ekh is the k-th Fourier coefﬁcient of the 2 π-periodic and smooth function
u↦→ ϕX(h + iu); this leads to the ﬁrst formula. Then, assuming also h > 0,
P[X≥ k] =
∞
∑
l=k
P[X = l] =
∞
∑
l=k
1
2π
∫ π
−π
e−l(h+iu) ϕX(h + iu) du,
and the sum of the moduli of the functions on the right-hand side is dominated by the
integrable function e−kh
1−e−h ϕX(h); so by Lebesgue’s dominated convergence theorem,
one can exchange the integral and the summation symbol, which yields the second
equation. □
We now work under the assumptions of Deﬁnition 1.1, with a lattice inﬁnitely divisi-
ble distribution φ. Furthermore, we assume that the convergence is at speedO((tn)−v),
on a stripS(c,d) containing 0. Note that necessarily η(0) = 0 and ψ(0) = 1. A simple
computation gives also the following approximation formulas:
E(Xn) = ϕ′
n(0) = tnη′(0) + ψ′(0)∼ tnη′(0) = tnη′(0) + O(1);
Var(Xn) = ϕ′′
n(0)− ϕ′
n(0)2 = tnη′′(0) + O(1).
Theorem 3.4. Let x be a real number in the interval (η′(c), η′(d)), and h deﬁned by the
implicit equation η′(h) = x. We assume t nx∈ N.
(1) The following expansion holds:
P[Xn = tnx] = exp(−tnF(x))√
2πtnη′′(h)
(
ψ(h) + a1
tn
+ a2
(tn)2 +··· + av−1
(tn)v−1 + O
( 1
(tn)v
))
= exp(−tnF(x))
√
F′′(x)
2πtn
(
ψ(F′(x)) + a1
tn
+··· + av−1
(tn)v−1 + O
( 1
(tn)v
))
,
for some numbers ak.
(2) Similarly, if x is a real number in the range of η′
|(0,d), then
P[Xn≥ tnx] = exp(−tnF(x))√
2πtnη′′(h)
1
1− e−h
(
ψ(h) + b1
tn
+··· + bv−1
(tn)v−1 + O
( 1
(tn)v
))
,
for some numbers bk.
Both a k and bk are rational fractions in the derivatives of η and ψ at h, that can be computed
explicitly — see Remark 3.7.
Proof. With the notations of Deﬁnition 1.1, the ﬁrst equation of Lemma 3.3 becomes
P[Xn = tnx] = 1
2π
∫ π
−π
e−tnx (h+iu) ϕn(h + iu) du
= 1
2π
∫ π
−π
e−tnxh etn(η(h+iu)−iux) ψn(h + iu) du
= e−tnF(x)
2π
∫ π
−π
etn(η(h+iu)−η(h)−iuη′(h)) ψn(h + iu) du. (3)
The last equality uses the facts that xh = F(x) + η(h) and x = η′(h). We perform
the Laplace method on (3), and to this purpose we split the integral in two parts. Fix
18 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
δ > 0, and denote qδ = maxu∈(−π,π)\(−δ,δ)| exp(η(h + iu)− η(h))|. This is strictly
smaller than 1, since
exp(η(h + iu)− η(h)) = E[e(h+iu)X]
E[ehX ] = EQ[eiuX ]
is the characteristic function of X under the new probability dQ(ω) = ehX(ω)
E[ehX ]dP(ω)
(and X has minimum lattice Z). Note that Lemma 3.11 hereafter is a more precise
version of this inequality.
As a consequence, if I(−δ,δ) and I(−δ,δ)c denote the two parts of (3) corresponding to∫ δ
−δ and
∫−δ
−π +∫ π
δ , then
|I(−δ,δ)c|≤ e−tnF(x)
2π
∫
(−δ,δ)c
(qδ)tn|ψn(h + iu)| du≤ 2 (e−F(x) qδ)tn max
u∈(−π,π)
|ψ(h + iu)|
for n big enough, since ψn converges uniformly towards ψ on the compact set K =
h + i[−π, π]. Since qδ < 1, for any δ > 0 ﬁxed, I(−δ,δ)c etnF(x) goes to 0 faster than
any negative power of tn, so I(−δ,δ)c is negligible in the asymptotics (recall that F(x) is
non-negative by deﬁnition, as η(0) = 0).
As for the other part, we can ﬁrst replace ψn by ψ up to a (1 + O((tn)−v)), since the
integral is taken on a compact subset ofS(c,d). We then set u = w√
tnη′′(h):
I(−δ,δ) =
e−tnF(x)
(
1 + O
(
1
(tn)v
))
2π
√
tnη′′(h)
∫ δ
√
tnη′′(h)
−δ
√
tnη′′(h)
ψ
(
h + iw√
tnη′′(h)
)
etn∆n(w)− w2
2 dw, (4)
where ∆n(w) is the Taylor expansion
η (h + iu)− η(h)− η′(h) (iu)− η′′(h)
2 (iu)2
=
2v+1
∑
k=3
η(k)(h)
k!
(
iw√
tnη′′(h)
)k
+ O
( 1
(tn)v+1
)
= 1
tn

− w2
η′′(h)
2v−1
∑
k=1
η(k+2)(h)
(k + 2)!
(
iw√
tnη′′(h)
)k
+ O
( 1
(tn)v
)
 .
We also replace ψ by its Taylor expansion
ψ
(
h + iw√
tnη′′(h)
)
=
2v−1
∑
k=0
ψ(k)(h)
k!
(
iw√
tnη′′(h)
)k
+ O
( 1
(tn)v
)
.
Thus, if one deﬁnes αk by the equation
fn(w) :=


2v−1
∑
k=0
ψ(k)(h)
k!
(
iw√
tnη′′(h)
)k
 exp

− w2
η′′(h)
2v−1
∑
k=1
η(k+2)(h)
(k + 2)!
(
iw√
tnη′′(h)
)k

=
2v−1
∑
k=0
αk(w)
(tn)k/2 + O
( 1
(tn)v
)
,
MOD-φ CONVERGENCE, I 19
then one can replace ψ(h + iu) etn∆n(w) by fn(w) in Equation (4). Moreover, observe
that each coefﬁcient αk(w) writes as
αk(w) = αk,0(h)
(
w√
η′′(h)
)k
+ αk,1(h)
(
w√
η′′(h)
)k+2
+··· + αk,r(h)
(
w√
η′′(h)
)k+2r
with the αk,r(h)’s polynomials in the derivatives ofψ and η at point h. So,
I(−δ,δ) =
(
1 + O
( 1
(tn)v
)) e−tnF(x)
√
2πtnη′′(h)


2v−1
∑
k=0
∫ δ
√
tnη′′(h)
−δ
√
tnη′′(h)
αk(w)
(tn)k/2
e− w2
2
√
2π
dw

 .
For any power wm,
⏐⏐⏐⏐⏐⏐
∫ ∞
−∞
wm e− w2
2
√
2π
dw−
∫ δ
√
tnη′′(h)
−δ
√
tnη′′(h)
wm e− w2
2
√
2π
dw
⏐⏐⏐⏐⏐⏐
is smaller than any negative power of tn as n goes to inﬁnity (see Lemma 2.7, (3) for
the case m = 0): indeed, by integration by parts, one can expand the difference as
e−δ2 tnη′′(h)/2 Rm(√tn), where Rm is a rational fraction that depends on m, h, δ and on
the order of the expansion needed. Therefore, one can take the full integrals in the
previous formula. On the other hand, the odd moments of the Gaussian distribution
vanish. One concludes that
P[Xn = tnx] = e−tnF(x)
√
2πtnη′′(h)


v−1
∑
k=0
1
(tn)k


∫
R
α2k(w) e− w2
2
√
2π
dw

 + O
( 1
(tn)v
)
 ,
and each integral
∫
R α2k(w) e− w2
2√
2π dw is equal to
α2k,0(h) (2k− 1)!!
(η′′(h))k +··· + α2k,r(h) (2k + 2r− 1)!!
(η′′(h))k+r
where (2m− 1)!! is the 2m-th moment of the Gaussian distribution (cf. Lemma 2.7, (1)).
This ends the proof of the ﬁrst part of our Theorem, the second formula coming from
the identities h = F′(x) and η′′(h) = 1
F′′(x). The second part is exactly the same, up to
the factor
1
1− e−h−iu = 1
1− e−h

 1− e−h
1− e
−h− iw√
tnη′′ (h)


in the integrals. □
Remark 3.5. For x > η′(0), the ﬁrst term of the expansion
exp(−tnF(x))√
2πtnη′′(h)
is the leading term in the asymptotics of P[Ytn = tnx], where (Yt)t∈R+ is the Lévy
process associated to the analytic function η(z). Thus, the residue ψ measures the
difference between the distribution of Xn and the distribution of Ytn in the interval
(tnη′(0), tnη′(d)).
20 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Remark 3.6. If the convergence is faster than any negative power of tn, then one can
simplify the statement of the theorem as follows: as formal power series in tn,
√
2πtnη′′(h) exp(tnF(x)) P[Xn = tnx] =
∫
R
fn(w) e− w2
2 dw,
i.e., the expansions of both sides up to any given power O
(
1
(tn)v
)
agree.
Remark 3.7. As mentioned in the statement of the theorem, the proof also gives an
algorithm to obtain formulas for ak and bk. More precisely, denote
∆n(w) = tn
(
η
(
h + iw√
tnη′′(h)
)
− η(h)− η′(h) iw√
tnη′′(h) + w2
2tn
)
fn(w) = ψ
(
h + iw√
tnη′′(h)
)
exp(tn∆n(w)) =
∞
∑
k=0
αk(w)
(tn)k/2 ,
the last expansion holding in a neighborhood of zero. The coefﬁcient α2k(w) is an
even polynomial in w with valuation 2k and coefﬁcients which are polynomials in the
derivatives of ψ and η at h, and in 1
η′′(h). Then,
ak =
∫
R
α2k(w) e− w2
2
√
2π
dw,
and in particular,
a0 = ψ(h);
a1 =−1
2
ψ′′(h)
η′′(h) + 1
24
ψ(h) η(4)(h) + 4 ψ′(h) η(3)(h)
(η′′(h))2 − 15
72
ψ(h) (η(3)(h))2
(η′′(h))3 .
the bk’s are obtained by the same recipe as theak’s, but starting from the power series
gn(w) = 1− exp(−h)
1− exp
(
−h− iw√
tnη′′(h)
) fn(w).
Example 3.8. Suppose that (Xn)n∈N is mod-Poisson convergent, that is to say that
η(z) = ez− 1. The expansion of Theorem 3.4 reads then as follows:
P[Xn = tnx] = etn(x−1−x log x)
√2πxtn
(
ψ(h) + ψ′(h)− 3ψ′′(h)− ψ(h)
6xtn
+ O
( 1
(tn)2
))
with h = log x. For instance, if Xn is the number of cycles of a random permutation in
S(n), then the discussion of Example 2.3 shows that for x > 0 such that x log n∈ N,
P[Xn = x(log n)] = n−(x log x−x+1)
√
2πx log n
1
Γ(x)
(
1 + O(1/ logn)
)
.
Similarly, for x > 1 such that x log n∈ N, one has
P[Xn≥ x(log n)] = n−(x log x−x+1)
√
2πx log n
x
x− 1
1
Γ(x)
(
1 + O(1/ logn)
)
.
As the speed of convergence is very good in this case, precise expansions in 1/ logn to
any order could also be given.
MOD-φ CONVERGENCE, I 21
