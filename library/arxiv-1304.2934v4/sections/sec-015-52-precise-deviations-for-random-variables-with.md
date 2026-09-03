---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-015-52-precise-deviations-for-random-variables-with
section_title: "Precise deviations for random variables with control on cumulants"
section_number: 5.2
pages: 39-43
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
same hypotheses as in the previous subsection, and without loss of generality, we sup-
pose that v = 3. Then, the sequence of random variables
Xn = Sn
βn (αn)1/3
converges mod-Gaussian with parameters (αn)1/3 σ2 and limiting function ψ(z) =
exp(Lz3/6) (here, we may have L = 0). So, one can apply the previous theorems
to estimate the tail of the distribution of Sn. In particular, Xn/√tn = Sn/(βnσ√αn)
satisﬁes a central limit theorem with a normality zone of size o(√tn) = o
(
α1/6
n
)
(as for
the sum of αn i.i.d. variables) and one can describe the deviation probabilties at the
edge of the normality zone — see Proposition 4.14.
We shall see now that, with stronger assumptions on the speed of convergence than
Equation (25), we can extend these results to a larger scale. More precisely, we will
assume:
κ(2)(Sn) = σ2 αn (βn)2 (1 + O((αn)−1/2));
κ(3)(Sn) = L αn (βn)3 (1 + O((αn)−1/4)). (26)
40 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
We then have the following result:
Proposition 5.2. Let (Sn)n∈N be a sequence of centered real-valued random variables. Assume
that the bound on cumulants (24) and the asymptotics of second and third cumulants given by
Equation (26) hold. If x n is a positive sequence, bounded away from 0 with x n = o
(
α1/12
n
)
,
then
P
[
Sn≥ βnσ2α2/3
n xn
]
= P[Xn≥ tnxn] = e− (xn)2(αn)1/3 σ2
2
xn(αn)1/6σ
√
2π
e
L(xn)3
6 (1 + o(1)).
P
[
Sn≥ βnσ2α2/3
n xn
]
= P[Xn≤− tnxn] = e− (xn)2(αn)1/3 σ2
2
xn(αn)1/6σ
√
2π
e
−L(xn)3
6 (1 + o(1)).
Remark 5.3. The case where xn is a constant sequence equal to x corresponds to Equa-
tions (21) and (22), which gives an equivalent for the deviation probability at the edge
of the normality zone. Hence, the proposition asserts that, with appropriate assump-
tions on cumulants, this result is valid at a larger scale. Namely, we give an equivalent
for the deviation probability of Xn of order up to o
(
t5/4
n
)
, instead of the usual O(tn).
Proof. Set Xn = ( αn)−1/3 Sn; up to a renormalization of the random variables, one can
suppose βn = 1, and also σ2 = 1. Let zn be a sequence of complex numbers with
|zn| = O((αn)1/12); we set ηn =|zn| (αn)−1/12. Then, following the computation of
Section 5.1 with v = 3, we get:
log ϕXn(zn) = κ(2)(Sn)
2 (αn)
2
3
(zn)2 + κ(3)(Sn)
6 αn
(zn)3 +
∞
∑
r=4
κ(r)(Sn)
r! (αn)
r
3
(zn)r
= 1
2 (αn)
1
3 (zn)2 + L
6 (zn)3 + O((ηn)2 + (ηn)3 + (ηn)4).
If|zn| = o((αn)1/12), then ηn→ 0, so the remainder above is o(1) and we have:
ϕXn(zn) = exp
(
(αn)
1
3
(zn)2
2 + L(zn)3
6
)(
1 + o(1)
)
. (27)
We make the change of probability measure
P[Yn∈ dy] = exny
ϕXn(xn) P[Xn∈ dy]
with xn = o((αn)1/12); the generating function of Yn is ϕYn(z) = ϕXn (xn+z)
ϕXn (xn) . So, using
the inequality
|(z + xn)r− (xn)r|≤ 2r|z| max(|z|,|xn|)r−1,
we get, setting ηz
n =|z| (αn)−1/12 and ηx,z
n = max(|xn|,|z|) (αn)−1/12,
log ϕYn(z) = ( αn)1/3 (z + xn)2− (xn)2
2 + L((z + xn)3− (xn)3)
6
+ O(ηz
n(ηx,z
n + (ηx,z
n )2 + (ηx,z
n )3))
=
(
(αn)1/3 xn + L (xn)2
2
)
z +
(
(αn)1/3 + L xn
2
)
z2 + L
6 z3
+ O(ηz
n(ηx,z
n + (ηx,z
n )2 + (ηx,z
n )3)) (28)
MOD-φ CONVERGENCE, I 41
Thus, if
Zn = Yn− (αn)1/3 xn− L (xn)2
2 ,
then the sequence (Zn)n∈N converges in the mod-Gaussian sense, with parameters
tn = ( αn)1/3 + L xn and limiting function exp ( L z3
6 ). Moreover, in Equation (28), the
approximation is valid for any z such that|z|≤ ∆(αn)1/12, for some constant ∆ de-
pending only on the constant C in the bound (24).
Besides, for xn = o((αn)1/12), one has
P
[
Sn≥ xn (αn)
2
3
]
= P
[
Xn≥ xn (αn)
1
3
]
= ϕXn(xn)
∫ ∞
y=xn (αn)1/3
e−xny P[Yn∈ dy]
= ϕXn(xn) e
−
(
(αn)1/3 (xn)2+ L (xn)3
2
)
∫ ∞
z=− L (xn)2
2
e−xnz P[Zn∈ dz]
= exp
(
− (αn)1/3 (xn)2
2 − L(xn)3
3
)
Rn (1 + o(1)),
by replacing ϕXn(xn) by its estimate (27), which holds since xn = o((αn)1/12); Rn is the
integral of the second line.
To estimate the integral Rn, we shall adapt the proof of Proposition 4.1 to the special
case of a sequence(Zn)n∈N that converges in the mod-Gaussian sense, with parameters
tn, limit function exp(Kz3), and with the approximation
log ϕZn(z) = tn z2
2 + K z3 + O
( z
(tn)1/4
)
(29)
that is valid for every |z|≤ ∆(tn)1/4 with ∆ > 0. Notice that the sequence (Zn)n∈N
previously constructed satisﬁes these hypotheses with tn = ( αn)1/3 + Lxn≃ (αn)1/3.
If one applies Proposition 4.1 to the case of mod-Gaussian convergence with a limit
exp(Kz3), then η′′′(0) = ψ′(0) = 0, so the approximation of the law dFn(w) of Zn/√tn
is simply the Gaussian lawdG(w) = ( 2π)−1/2 e−w2/2 dw, and the Kolmogorov distance
between Fn and G is a o((tn)−1/2). However, by using the validity of the approximation
(29) on a larger scale thanz = O(1), it is possible to obtain a better Berry-Esseen bound,
namely, O((tn)−3/4).
Recall that for any T > 0 and any w∈ R, the distance between cumulative distribu-
tion functions is smaller than
|Fn(w)− G(w)|≤ 1
π
∫ T
−T
⏐⏐⏐⏐
f∗
n (ζ)− g∗(ζ)
ζ
⏐⏐⏐⏐ dζ + 24m
πT .
42 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
However, for any ζ = O((tn)3/4), one has
⏐⏐⏐⏐
f∗
n (ζ)− g∗(ζ)
ζ
⏐⏐⏐⏐ = e− ζ2
2
⏐⏐⏐⏐⏐⏐
exp
(
K ζ3
(tn)3/2 + O
(
ζ
(tn)3/4
))
− 1
ζ
⏐⏐⏐⏐⏐⏐
e
ζ2
2
⏐⏐⏐⏐
f∗
n (ζ)− g∗(ζ)
ζ
⏐⏐⏐⏐≤
⏐⏐⏐⏐⏐e
K ζ3
(tn)3/2
⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐
exp
(
O
(
ζ
(tn)3/4
))
− 1
ζ
⏐⏐⏐⏐⏐⏐
+
⏐⏐⏐⏐⏐⏐
exp
(
K ζ3
(tn)3/2
)
− 1
ζ
⏐⏐⏐⏐⏐⏐
≤ e
K|ζ|3
(tn)3/2 O
( 1
(tn)3/4 + ζ2
(tn)3/2
)
.
In these inequalities, the constant hidden in the big O can be chosen uniform if ζ
(tn)3/4
stays in a bounded, sufﬁciently small interval [−∆, ∆]. As a consequence, setting T =
∆ (tn)3/4, one obtains from Feller’s lemma:
|Fn(w)− G(w)|≤ O
(∫ ∆ (tn)3/4
−∆ (tn)3/4
( 1
(tn)3/4 + ζ2
(tn)3/2
)
e
− ζ2
2 + K|ζ|3
(tn)3/2 dζ + 1
∆ (tn)3/4
)
uniformly in w. Since|ζ| stays smaller than ∆ (tn)3/4, in this integral,
− ζ2
2 + K|ζ|3
(tn)3/2≤− ζ2
2
(
1− K ∆
(tn)3/4
)
≤− ζ2
4
for tn large enough. As claimed before, it follows that
sup
w∈R
|Fn(w)− G(w)| = O
( 1
(tn)3/4
)
.
We can now compute the asymptotics of the integral Rn. Set
εn =− L(xn)2
2
√
(αn)1/3 + Lxn
=− L(xn)2
2√tn
;
since xn = o((αn)1/12), εn→ 0. Now,
Rn =
∫ ∞
w=εn
exp
(
−w xn
√
tn
)
dFn(w)
= xn
√
tn
∫ ∞
εn
exp
(
−w xn
√
tn
)
(Fn(w)− Fn(εn)) dw
= xn
√
tn
∫ ∞
εn
exp
(
−w xn
√
tn
)(
Gn(w)− Gn(εn) + O
( 1
(tn)3/4
))
dw
= 1√
2π
∫ ∞
εn
exp
(
−w xn
√
tn− w2
2
)
dw + O

 e
L (xn)3
2
(tn)3/4

 .
The last Gaussian integral is given by Lemma 2.7, (3):
MOD-φ CONVERGENCE, I 43
∫ ∞
εn
exp
(
−w xn
√
tn− w2
2
)
dw = e
tn(xn)2
2
∫ ∞
0
exp
(
− (y + εn + xn
√tn)2
2
)
dy
= e
L(xn)3
2
εn + xn
√tn
(1 + o(1)) = e
L(xn)3
2
xn
√tn
(1 + o(1))
since εn→ 0. Since xn = o((αn)1/12) = o((tn)1/4), 1
xn
√tn
becomes much larger than
O( 1
(tn)3/4 ) as tn goes to inﬁnity, so ﬁnally:
Rn = 1√
2π
e
L(xn)3
2
xn(αn)1/6 (1 + o(1))
as tn≃ (αn)1/3. Gathering everything, we get
P
[
Sn≥ xn (αn)
2
3
]
= e− (xn)2(αn)1/3
2
xn(αn)1/6√
2π
e
L(xn)3
6 (1 + o(1)),
and this ends the proof if βn = σ2 = 1 (set T = xn (αn)2/3 in the statement of the
Proposition). In the general case, it sufﬁces to replace Sn by Sn
σβ n , which changes L into
L
σ3 in the previous computations. □
Remark 5.4. The argument which allows one to get a better Berry-Esseen estimate than
in Proposition 4.1 can be used in a very general setting of mod-stable convergence, in
order to get optimal bounds on the Kolmogorov distance. This will be the main topic
of the forthcoming paper [FMN15a].
