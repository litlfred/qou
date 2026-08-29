---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-010-33-central-limit-theorem-at-the-scales-otn-and-o
section_title: "Central limit theorem at the scales o(tn) and o(tn23)"
section_number: 3.3
pages: 21-26
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
has described in the lattice case the ﬂuctuations of (Xn)n∈N in the regime O(tn), with
a result akin to large deviations. In this section, we establish in the same setting an
extended central limit theorem, for ﬂuctuations of order up to o(tn). In particular, for
ﬂuctuations of order o((tn)2/3), we obtain the usual central limit theorem. Hence, we
describe the panorama of ﬂuctuations drawn on Figure 4.
order of ﬂuctuations
large deviations (η′(0) < x):
extended central limit
central limit theorem (y≪ (tn)1/6):
theorem ((tn)1/6≲ y≪ (tn)1/2):
P[ Xn
tn ≥ x]≃ exp(−tn F(x))√
2πtnη′(x)
1
1−e−F′(x) ψ(F′(x));
P[ Xn−tnη′(0)√
tn η′′(0) ≥ y]≃ exp(−tn F(x))
F′(x)
√
2πtnη′(x);
P[ Xn−tnη′(0)√
tn η′′(0) ≥ y]≃ P[NR(0, 1)≥ y].
O(tn)
O((tn)2/3)
O((tn)1/2)
FIGURE 4. Panorama of the ﬂuctuations of a sequence of random vari-
ables (Xn)n∈N that converges modulo a lattice distribution (with x =
η′(0) +
√
η′′(0)/tn y).
Theorem 3.9. Consider a sequence (Xn)n∈N that converges mod-φ, with a reference inﬁnitely
divisible law φ that is a lattice distribution. Assume y = o((tn)1/6). Then,
P
[
Xn≥ tnη′(0) +
√
tnη′′(0) y
]
= P[NR(0, 1)≥ y] (1 + o(1)) .
On the other hand, assuming y≫ 1 and y = o((tn)1/2), if x = η′(0) +
√
η′′(0)/tn y and h
is the solution of η′(h) = x, then
P
[
Xn≥ tnη′(0) +
√
tnη′′(0) y
]
= e−tnF(x)
h
√
2πtn η′′(h) (1 + o(1));
= e−tnF(x)
y
√
2π
(1 + o(1)). (5)
Remark 3.10. The case y = O(1), which is the classical central limit theorem, follows im-
mediately from the assumptions of Deﬁnition 1.1, since by a Taylor expansion around
0 of η the characteristic functions of the rescaled r.v.
Yn = Xn− tnη′(0)√
tnη′′(0)
22 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
converge pointwise to e− ζ2
2 , the characteristic function of the standard Gaussian dis-
tribution. In the ﬁrst statement, the improvement here is the weaker assumption
y = o((tn)1/6).
As we shall see, the ingredients of the proof are very similar to the ones in the previ-
ous paragraph. We start with a technical lemma of control of the module of the Fourier
transform of the reference law φ.
Lemma 3.11. Consider a non-constant inﬁnitely divisible law φ, of type lattice, and with
convergent moment generating function
∫
ezx φ(dx) = eη(z) on a stripS(c,d) with c < 0 < d.
We assume without loss of generality thatφ has minimal latticeZ. Then, there exists a constant
D > 0 only depending on φ, and an interval (−ε, ε)⊂ (c, d), such that for all h ∈ (−ε, ε)
and all δ small enough,
qδ = max
u∈[−π,π]\(−δ,δ)
| exp(η(h + iu)− η(h))|
is smaller than 1− D δ2.
Proof. Denote X a random variable under the inﬁnitely divisible distribution φ. We
claim that there exist two consecutive integers n and m = n− 1 with P[X = n]⁄= 0
and P[X = m]⁄= 0. Indeed, under our hypotheses, if Π is the Lévy measure of φ, then
Z = Z[supp(Π)] = N[supp(Π)]− N[supp(Π)],
so there exist a and b in N[supp(Π)] such that b− a = 1. However, supp (φ) = γ +
N[supp(Π)] for some γ∈ Z, so n = γ + b and m = γ + a satisfy the claim.
Now, we have seen that exp(η(h + iu)− η(h)) can be interpreted as the characteristic
function of X under the new probability measure dQ = ehX
E[ehX ] dP. So, for any u,
| exp(η(h + iu)− η(h))|2 =
⏐⏐⏐EQ[eiuX ]
⏐⏐⏐
2
= ∑
n,m∈Z
Q[X = n] Q[X = m] eiu(n−m)
= ∑
k∈Z
(
∑
n−m=k
Q[X = n] Q[X = m]
)
cos ku.
Fix two integers n and m = n− 1 such that P[X = n]⁄= 0 and P[X = m]⁄= 0. Then
one also has Q[X = n]⁄= 0, Q[X = m]⁄= 0, and there exists D > 0 such that
Q[X = n] Q[X = m]≥ 15 D > 0
for h small enough (Q tends to P for h→ 0). As cos u≤ 1− u2
5 for all u∈ (−π, π),
| exp(η(h + iu)− η(h))|2≤ 1 + 15 D (cos u− 1)≤ 1− 3 D u2;
qδ≤
√
1− 3 D δ2≤ 1− D δ2 for δ small enough.
This concludes the proof of the Lemma. □
Proof of Theorem 3.9. Notice that η′′(0)⁄= 0 since this is the variance of the law φ, as-
sumed to be non-trivial. Set x = η′(0) + s, and assume s = o(1). The analogue of
Equation (3) reads in our setting
P[Xn≥ tnx] = e−tnF(x)
2π
∫ π
−π
etn(η(h+iu)−η(h)−iuη′(h))
1− e−h−iu ψn(h + iu) du. (6)
MOD-φ CONVERGENCE, I 23
Since h′(x) = 1
η′′(x), one has h = s
η′′(0) + O(s2). The same argument as in the proof of
Theorem 3.4 shows that the integral over (−δ, δ)c is bounded by C δ (qδ)tn, where qδ <
1, and C δ (with C a constant independent from s and δ) comes from the computation
of
max
u∈(−δ,δ)c
⏐⏐⏐⏐
ψ(h + iu)
1− e−h−iu
⏐⏐⏐⏐ .
In the following we shall need to makeδ go to zero sufﬁciently fast, but withδ
√
tnη′′(0)
still going to inﬁnity. Thus, set δ = ( tn)−2/5, so that in particular (tn)−1/2 ≪ δ≪
(tn)−1/3. Notice that I(−δ,δ)c etnF(x) still goes to zero faster than any power oftn; indeed,
(qδ)tn≤
(
1− D
(tn)4/5
)tn
≤ e−D (tn)1/5
by Lemma 3.11. The other part of (6) is
e−tnF(x)
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
etn∆n(w) e− w2
2
1− e
−h− iw√
tnη′′ (h)
dw,
up to a factor (1 + o(1)). Let us analyze each part of the integral:
• The difference between ψ
(
h + iw√
tnη′′(h)
)
and ψ(0) is bounded by
max
z∈[−s,s]+i[−δ,δ]
|ψ(z)− ψ(0)| = o(1)
by continuity of ψ, so one can replace the term with ψ by the constant ψ(0) = 1,
up to factor (1 + o(1)).
• The term ∆n(w) has for Taylor expansion
η(3)(h)
6
(
iw√
tnη′′(h)
)3
+ O
( 1
(tn)2
)
,
so tn ∆n(w) is bounded by a O(tn δ3), which is a o(1) since δ≪ (tn)−1/3. So
again one can replace etn∆n(w) by the constant 1.
• The Taylor expansion of
(
1− e
−h− iw√
tnη′′ (h)
)−1
is 1
h+ iw√
tnη′′ (h)
(1 + o(1)). Hence,
P
[
Xn≥ tn(η′(0) + s)
]
= e−tnF(x)
2π


∫
R
e− w2
2
√
tnη′′(h) h + iw
dw

(
1 + o(1)
)
= e−tnF(x)+ h2 tn η′′ (h)
2 P
[
NR(0, 1)≥ h
√
tnη′′(h)
](
1 + o(1)
)
.
Indeed, setting β = h
√
tn η′′(h), this leads directly to the computation done in
Lemma 2.7, (4).
Hence, we have shown so far that
P
[
Xn≥ tn(η′(0) + s)
]
= e−tnF(η′(0)+s) e
β2
2 P[NR(0, 1)≥ β]
(
1 + o(1)
)
, (7)
with β = h
√
tn η′′(h).
24 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
We now set y = s
√
tn/η′′(0) = o(t1/2
n ), and we consider the following regimes.
If y≫ 1 (and a fortiori if y is of order bigger than O(tn)1/6), then s≫ (tn)−1/2, so
h≫ (tn)−1/2 and β≫ 1. We can then use Lemma 2.7, (3) to replace in Equation (7) the
function of β by the tail-estimate of the Gaussian:
P
[
Xn≥ tnη′(0) +
√
tn η′′(0)y
]
= e−tn F(x)
h
√
2πtn η′′(h) (1 + o(1)). (8)
Recall that h = s
η′′(0) (1 + O(s)), so that the denominator above can be approximated
as follows:
h
√
tn η′′(h) = s
η′′(0) (1 + O(s))
√
tn (η′′(0) + O(s)) = y (1 + O(s)) = y(1 + o(1)).
This completes the proof of the second part of the theorem.
Suppose on the opposite that y = o((tn)1/6), or, equivalently,s = o((tn)−1/3). Let us
then see how everything is transformed.
• By making a Taylor expansion aroundη′(0) of the Legendre-Fenchel transform,
we get (recall that x = η′(0) implies h = 0)
F(x) = F(η′(0)) + F′(η′(0)) s + F′′(η′(0))
2 s2 + O(s3) = y2
2tn
+ o((tn)−1), (9)
so e−tnF(η′(0)+s)≃ e− y2
2 .
• As above,
β = h
√
tn η′′(h) = y (1 + O(s)) = y (1 + o((tn)−1/3))
Consequently, β2 = y2(1 + o((tn)−1/3)) = y2 + o(1), so e
β2
2 can be replaced
safely by e
y2
2 , which compensates the previous term.
• Finally, ﬁx y, and denote Fy(λ) = P[NR(0, 1)≥ λy]. Then, for|λ| say between
1
2 and 2,
|F′
y(λ)| =
⏐⏐⏐⏐
y√
2π
e− λ2y2
2
⏐⏐⏐⏐≤ max
y∈R
⏐⏐⏐⏐
y√
2π
e− y2
8
⏐⏐⏐⏐ = C < +∞;
as a consequence,
|P[NR(0, 1)≥ β]− P[NR(0, 1)≥ y]| =
⏐⏐⏐Fy(1 + o((tn)−1/3))− Fy(1)
⏐⏐⏐
≤ C
(tn)1/3 = o(1).
This ends the proof of Theorem 3.9. □
Remark 3.12. Equation (7) is the probabilistic counterpart of the number-theoretic re-
sults of [Kub72, Rad09], see in particular Theorems 2.1 and 2.2 in [Rad09]. In Section
7.2, we shall explain how to recover the precise large deviation results of [Rad09] for
arithmetic functions whose Dirichlet series can be studied with the Selberg-Delange
method.
MOD-φ CONVERGENCE, I 25
The following corollary gives a more explicit form of Theorem 3.9, depending on the
order of magnitude of y.
Corollary 3.13. If y = o((tn)1/4), then one has
P
[
Xn≥ tnη′(0) +
√
tnη′′(0) y
]
= (1 + o(1))
y
√
2π
e− y2
2 exp
( η′′′(0)
6 (η′′(0))3/2
y3
√tn
)
. (10)
More generally, if y = o((tn)1/2−1/m), then one has
P
[
Xn≥ tnη′(0) +
√
tnη′′(0) y
]
= (1 + o(1))
y
√
2π
exp
(
−
m−1
∑
i=2
F(i)(η′(0))
i!
(η′′(0))i/2 yi
(tn)(i−2)/2
)
.
(11)
Proof. As above in Equation (9), we write s = y
√
η′′(0)/tn and x = η′(0) + s and do a
Taylor expansion of F around η′(0):
F(x) =
m−1
∑
i=0
F(i)(η′(0))
i!

y
√
η′′(0)
tn


i
+ O(sm).
Note that F(η(0)) = F′(η′(0)) = 0. Because of the hypothesis y = o((tn)1/2−1/m), we
have tnO(sm) = o(1). Therefore, plugging the equation above in Equation (5), we get
(11).
Observing that F′′(η′(0)) = 1/η′′(0) and F′′′(η′(0)) = −η′′′ (0)
η′′(0)3 , we get the ﬁrst equa-
tion. □
To summarize, in the lattice case, mod-φ convergence implies a large deviation prin-
ciple (Theorem 3.4) and a precised central limit theorem (Theorem 3.9), and these two
results cover a whole interval of possible scalings for the ﬂuctuations of the sequence
(Xn)n∈N. As we shall see in the next Section 4, the same holds for non-lattice reference
distributions.
4. F LUCTUATIONS IN THE NON -LATTICE CASE
In this section we prove the analogues of Theorems 3.4 and 3.9 when φ is not lattice-
distributed; hence, by Proposition 3.2,|eη(iu)| < 1 for any u⁄= 0. In this setting, assum-
ing φ absolutely continuous w.r.t. the Lebesgue measure, there is a formula equivalent
to the one given in Lemma 3.3, namely,
P[X≥ x] = lim
R→∞
(
1
2π
∫ R
−R
e−x(h+iu)
h + iu ϕX(h + iu) du
)
(12)
if ϕX(h) = E[ehX ] < +∞ for h > 0 (see [Fel71, Chapter XV , Section 3]). However,
in order to manipulate this formula as in Section 3, one would need strong additional
assumptions of integrability on the characteristic functions of the random variables
Xn. Thus, instead of Equation (12), our main tool will be a Berry-Esseen estimate (see
Proposition 4.1 hereafter), which we shall then combine with techniques of tilting of
measures (Lemma 4.7) similar to those used in the classical theory of large deviations
(see [DZ98, p. 32]).
26 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
