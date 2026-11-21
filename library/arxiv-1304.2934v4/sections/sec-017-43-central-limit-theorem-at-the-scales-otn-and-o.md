---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-017-43-central-limit-theorem-at-the-scales-otn-and-o
section_title: "Central limit theorem at the scales o(tn) and o(tn23)"
section_number: 4.3
pages: 30-35
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
one can also prove from the hypotheses of mod-convergence an extended central limit
theorem:
Theorem 4.8. Consider a sequence (Xn)n∈N that converges mod-φ with limiting distribu-
tion ψ and parameters tn, where φ is a non-lattice inﬁnitely divisible law that is absolutely
continuous w.r.t. Lebesgue measure. Let y = o((tn)1/6). Then,
P

Xn ≥tnη′(0) +
q
tnη′′(0) y

= P[NR(0, 1) ≥y] (1 + o(1)) .
On the other hand, assume y ≫1 and y = o((tn)1/2). If x = η′(0) +
p
η′′(0)/tn y and h is
the solution of η′(h) = x, then
P

Xn ≥tnη′(0) +
q
tnη′′(0) y

=
e−tn F(x)
h
p
2πtn η′′(h) (1 + o(1)) = e−tn F(x)
y
√
2π
(1 + o(1)) .
MOD-φ CONVERGENCE, I
31
As in the proof of Theorem 3.9, we need to control the modulus of the Fourier trans-
form of the reference law φ. Thus, let us state the non-lattice analogue of Lemma 3.11:
Lemma 4.9. Consider a non-constant inﬁnitely divisible law φ, of type non-lattice, with a
convergent moment generating function in a strip S(c,d) with c < 0 < d. We also assume that
φ is absolutely continuous w.r.t. the Lebesgue measure. Then, there exists a constant D > 0
only depending on φ, and an interval (−ε, ε) ⊂(c, d), such that for all h ∈(−ε, ε), and all δ
small enough,
qδ =
max
u∈R\(−δ,δ) | exp(η(h + iu) −η(h))| ≤1 −D δ2.
Remark 4.10. One can give a sufﬁcient condition on the Lévy-Khintchine representation
of φ to ensure the absolute continuity with respect to the Lebesgue measure; cf. [SH04,
Chapter 4, Theorem 4.23]. Hence, it is the case if σ2 > 0, or if σ2 = 0 and if the
absolutely continuous part of the Lévy measure Π has inﬁnite mass.
Remark 4.11. Let us explain why we need to add the assumption of absolute continuity
with respect to Lebesgue measure, which is a strictly stronger hypothesis than being
non-lattice. The hypotheses on the inﬁnitely divisible law φ imply that it has ﬁnite vari-
ance, and therefore, that the Lévy-Khintchine representation of the Fourier transform
given by Equation (2) can be replaced by a Kolmogorov representation. This represen-
tation actually holds for the complex moment generating function (see [SH04, Chapter
4, Theorem 7.7]):
η(z) = mz + σ2
Z
R
ezx −1 −zx
x2
K(dx)
where K is a probability measure on R, and where the fraction in the integral is ex-
tended by continuity at x = 0 by the value −z2
2 . As a consequence,
| exp(η(h + iu) −η(h))| = exp
 
σ2
Z
R
ehx (cos ux −1)
x2
K(dx)
!
≤1.
This expression can be expanded in series of u as
1 −σ2u2
2
Z
R ehx K(dx) + Oh(u3).
Therefore, Lemma 4.9 holds as soon as one can show that
sup
h∈(−ε,ε)
lim sup
|u|→∞
| exp(η(h + iu) −η(h))| < 1,
because one has a bound of type 1 −D u2 in a neighborhood of zero. Unfortunately,
for general probability measures, the Riemann-Lebesgue lemma does not apply, and
even for h = 0, it is unclear whether for a general exponent η the Cramér condition (C)
lim sup
|u|→∞
| exp(η(iu))| < 1
is satisﬁed (see [Pet95] for more discussion and references on condition (C)). We refer
to [Wol83, Theorem 2], where it is shown that decomposable probability measures enjoy
this property. This difﬁculty explains why one has to restrict oneself to absolutely
continuous measures in the non-lattice case, in order to use the Riemann-Lebesgue
lemma. In the following we provide an ad hoc proof of Lemma 4.9 in the absolutely
continuous cases, that does not rely on the Kolmogorov representation.
32
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Proof of Lemma 4.9. We shall adapt the arguments of Lemma 3.11 from the discrete to
the continuous case. Though the density f cannot be supported on a compact segment
(cf. Lemma 3.1 and the classiﬁcation of the possible supports of an inﬁnitely divisible
law), one can work as if it were the case, thanks to the following calculation:
| exp(η(h + iu) −η(h))| =

φ(e(h+iu)x)
φ(ehx)

= |φ<a(e(h+iu)x) + R b
a e(h+iu)x f (x) dx + φ>b(e(h+iu)x)|
φ<a(ehx) + R b
a ehx f (x) dx + φ>b(ehx)
≤φ<a(ehx) + φ>b(ehx) + | R b
a e(h+iu)x f (x) dx|
φ<a(ehx) + φ>b(ehx) + R b
a ehx f (x) dx
where φ<a (respectively, φ>b) is the measure 1x<a φ(dx) (resp., 1x>b φ(dx)). Therefore,
it sufﬁces to show:
max
u∈(−δ,δ)c
| R b
a e(h+iu)x f (x) dx|
R b
a ehx f (x) dx
≤1 −D δ2
for δ and h small enough. This reduction to a compact support will be convenient later
in the computations.
Set gh(x) =
ehx f (x)
R b
a ehx f (x) dx and
F(h, u) =

Z b
a gh(x) eiux dx

2
=
ZZ
[a,b]2 gh(x)gh(y) eiu(x−y) dx dy
=
ZZ
[a,b]2 gh(x)gh(y) cos(u(x −y)) dx dy
=
Z b−a
t=−(b−a)
Z min(b,t+b)
x=max(a,t+a) gh(x)gh(x −t) dx

cos ut dt.
The problem is to show that
sup
h∈(−ε,ε)
sup
u∈(−δ,δ)c
F(h, u) ≤1 −D δ2
for some constant D. With h ﬁxed, by the Riemann-Lebesgue lemma applied to the
integrable function
m(t) =
Z min(b,t+b)
x=max(a,t+a) gh(x)gh(x −t) dx,
the limit as |u| goes to inﬁnity of F(h, u) is 0. On the other hand, if u̸ = 0, then
F(h, u) < F(h, 0) = 1. Indeed, suppose the opposite: then cos ut = 1 almost surely
w.r.t. the measure m(t) dt. This means that this measure m(t) dt is concentrated on the
lattice 2π
|u| Z, which is impossible for a measure continuous with respect to the Lebesgue
measure. Combining these two observations, one sees that for any δ > 0,
sup
u∈(−δ,δ)c
F(h, u) ≤C(h,δ) < 1
MOD-φ CONVERGENCE, I
33
for some constant C(h,δ). Since all the terms considered depend smoothly on h, for h
small enough, one can even take a uniform constant Cδ:
∀δ > 0, ∃Cδ < 1 such that
sup
h∈(−ε,ε)
sup
u∈(−δ,δ)c
F(h, u) ≤Cδ.
(16)
On the other hand, notice that
∂F(h, u)
∂u
= −
ZZ
[a,b]2 gh(x)gh(y) (x −y) sin(u(x −y)) dx dy.
However, if u(b −a) ≤π
2 , then (x −y) sin(u(x −y)) ≥2u
π (x −y)2 over the whole
domain of integration, so,
∂F(h, u)
∂u
≤−2Bh
π u
where Bh = RR
[a,b]2 gh(x)gh(y) (x −y)2 dx dy. By integration,
F(h, u) ≤1 −Bh
π u2
for all u ≤
π
2(b −a).
Again, by continuity of the constant Bh w.r.t. h, one can take a uniform constant :
∃B > 0 such that for all u ≤
π
2(b −a),
sup
h∈(−ε,ε)
F(h, u) ≤1 −B u2.
(17)
The two assertions (16) (with δ =
π
2(b−a)) and (17) enable one to conclude, with
D = inf

B, 1 −Cδ
δ2

,
where δ =
π
2(b −a).
□
We also refer to [Ess45, Theorem 6] for a general result on the Lebesgue measure of the
set of points such that the characteristic function of a distribution is larger in absolute
value than 1 −δ2.
Proof of Theorem 4.8. The proof is now exactly the same as in the lattice case (Theorem
3.9). Indeed, the conclusions of the technical Lemma 4.9 hold, and on the other hand,
the equivalents for P[Xn ≥tnx] in the lattice and non-lattice cases (Theorems 3.4 and
4.3) differ only by the fact that 1 −e−h is replaced by h. But in the proof of Theorem
3.9, the quantity 1 −e−h is approximated by h, so everything works the same way as
in the non-lattice case.
□
As in the non-lattice case, we have the following corollary (with the exact same state-
ment and proof):
Corollary 4.12. If y = o((tn)1/4), then one has
P

Xn ≥tnη′(0) +
q
tnη′′(0) y
 = (1 + o(1))
y
√
2π
e−y2
2 exp

η′′′(0)
6 (η′′(0))3/2
y3
√tn

.
(18)
More generally, if y = o((tn)1/2−1/m), then one has
P

Xn ≥tnη′(0) +
q
tnη′′(0) y
 = (1 + o(1))
y
√
2π
exp
 
−
m−1
∑
i=2
F(i)(η′(0))
i!
(η′′(0))i/2 yi
(tn)(i−2)/2
!
.
(19)
34
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Hence, one can again describe all the ﬂuctuations of Xn from order O(√tn) up to
order O(tn), see Figure 5.
order of ﬂuctuations
large deviations (η′(0) < x):
extended central limit
central limit theorem (y ≪(tn)1/6):
theorem ((tn)1/6 ≲y ≪(tn)1/2):
P[ Xn
tn ≥x] ≃
exp(−tn F(x))
F′(x)√
2πtnη′(x) ψ(F′(x));
P[ Xn−tnη′(0)
√
tn η′′(0) ≥y] ≃
exp(−tn F(x))
F′(x)√
2πtnη′(x);
P[ Xn−tnη′(0)
√
tn η′′(0) ≥y] ≃P[NR(0, 1) ≥y].
O(tn)
O((tn)2/3)
O((tn)1/2)
FIGURE 5. Panorama of the ﬂuctuations of a sequence of random vari-
ables (Xn)n∈N that converges modulo an absolutely continuous distribu-
tion (with x = η′(0) +
p
η′′(0)/tn y).
To conclude this paragraph, let us mention an application that looks similar to the
law of the iterated logarithm, and that also works in the lattice case. Consider a se-
quence (Xn)n∈N converging mod-φ with parameters tn such that tn ≫(log n)3. We
also assume that the random variables Xn are deﬁned on the same probability space,
and we look for sequences γn such that almost surely,
lim sup
n→∞
Xn −tnη′(0)
γn

≤1.
Unlike in the usual law of the iterated logarithm, we do not make any assumption of
independence. Such assumptions are common in this setting, or at least some con-
ditional independence (for instance, a law of the iterated logarithm can be stated for
martingales); see the survey [Bin86] or [Pet75, Chapter X].
On the one hand we have a less precise result: we only obtain an upper bound, which
is not tight in the case of sums of i.i.d. variable since we have a
p
log(n) factor instead
the usual
p
log(log(n)) factor. On the other hand, our result does not depend at all
on the way one realizes the random variables Xn. In other words, for every possible
coupling of the variables Xn, the following holds:
Proposition 4.13. Let (Xn)n∈N be a sequence that converges mod-φ with parameters tn, where
φ is either a non-constant lattice distribution, or a non-lattice distribution that is absolutely
continuous with respect to the Lebesgue measure. We assume
lim
n→∞
tn
(log n)3 = +∞.
Then,
lim sup
n→∞
Xn −tnη′(0)
p
2η′′(0) tn log n ≤1
almost surely.
MOD-φ CONVERGENCE, I
35
Proof. Notice the term log n instead of log log n for the usual law of iterated logarithm.
One computes
P

Xn −tnη′(0) ≥
q
2(1 + ε) η′′(0) tn log n

.
Set y =
p
2(1 + ε) log n. Due to the hypotheses on tn, one has y = o
 (tn)1/6
and one
can apply Theorem 4.8: using the classical equivalent
P[NR(0, 1) ≥y] ∼e−y2/2
y
√
2π
,
we get
P

Xn −tnη′(0) ≥
q
2(1 + ε)η′′(0)tn log n

≃
e−(1+ε) log n
p
4π(1 + ε) log n ≤
1
n1+ε .
for n large enough. For any ε > 0, this is summable, so by the Borel-Cantelli lemma,
one has almost surely
Xn −tnη′(0) <
q
2(1 + ε) η′′(0) tn log n
for n large enough.
Since this is true for every ε, one has (almost surely):
lim sup
n→∞
Xn −tnη′(0)
p
2η′′(0) tn log n ≤1.
□
