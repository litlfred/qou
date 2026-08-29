---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-029-31-sums-of-independent-random-variables
section_title: "Sums of independent random variables"
section_number: 3.1
pages: 18-20
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
As a direct application of Theorem 20, one recovers the classical Berry–Esseen estimates. Let(An)n∈N
be a sequence of centered i.i.d. random variables with a third moment. We denoteE[(Ai)2] = σ2 and
E[|Ai|3] =ρ. SetSn =∑n
i=1Ai, Xn =Sn/(σn1/3),
tn =n1/3 ; K = σ3
ρ ; v =w = 3 ; γ = 1.
Notice thatK≤ 1 as a classical application of Hölder inequality. On the zoneξ∈ [−Kn1/3,Kn 1/3], we
have:
|θn(ξ)− 1| =
⏐⏐⏐⏐
(
E
[
eiξ A1
σn1/3
]
e
ξ2
2n2/3
)n
− 1
⏐⏐⏐⏐
≤n
⏐⏐⏐⏐E
[
eiξ A1
σn1/3
]
e
ξ2
2n2/3− 1
⏐⏐⏐⏐
(
max
(⏐⏐⏐⏐E
[
eiξ A1
σn1/3
]
e
ξ2
2n2/3
⏐⏐⏐⏐, 1
))n−1
.
For anyt,|eit− 1− it + t2
2|≤ |t3|
6 , so
⏐⏐⏐⏐E
[
eiξ A1
σn1/3
]
e
ξ2
2n2/3− 1
⏐⏐⏐⏐
≤
⏐⏐⏐⏐E
[
eiξ A1
σn1/3
]
− 1 + ξ2
2n2/3
⏐⏐⏐⏐ e
ξ2
2n2/3 +
⏐⏐⏐⏐e− ξ2
2n2/3− 1 + ξ2
2n2/3
⏐⏐⏐⏐ e
ξ2
2n2/3
≤
(|ξ|3
6Kn + ξ4
8n4/3
)
e
ξ2
2n2/3≤ 7e1/2
24
|ξ|3
Kn.
For the same reasons,
Mod-φ convergence, II: Estimates on the speed of convergence 19
⏐⏐⏐⏐E
[
eiξ A1
σn1/3
]
e
ξ2
2n2/3
⏐⏐⏐⏐≤ |ξ|3
6Kn e
ξ2
2n2/3 +
(
1− ξ2
2n2/3
)
e
ξ2
2n2/3
≤ |ξ|3
6Kn e1/2 + 1≤ e
e1/2
6
|ξ|3
Kn
We conclude that
|θn(ξ)− 1|≤ 7e1/2
24
|ξ|3
K e
e1/2
6
|ξ|3
K
on the zone of control[−Kn1/3,Kn 1/3]. If we want Condition (Z2) to be satisﬁed, we need to changeK
and set
K = 3
2e1/2
σ3
ρ ,
which is a little bit smaller than before. We then have a zone of control with constantsK1 = 7e1/2ρ
24σ3 and
K2 = e1/2ρ
6σ3 , and the inequalityK≤ ( cα
2K2
)
1
w−α is an equality. By Theorem 20,
dKol(Yn,NR)≤ 1 +λ√
2π
(
7
24 23/2e1/2 + 2e1/2
3 3√π
(
4
3
√
1 + 1
λ + 3
3√
3
))
ρ
σ3√n
withYn = 1
σ√n
∑n
i=1Ai. Takingλ = 0.183, we obtain a bound with a constantC≤ 4.815, so we recover
dKol(Yn,NR(0, 1))≤ 4.815 ρ
σ3√n,
which is almost as good as the statement in the introduction, where a constantC = 3 was given (the
best constant known today is, as far as we know,C = 0.4748, see [KS10]). Of course, the advantage of
our method is its large range of applications, as we shall see in the next sections.
Our notion of zone of control allows one to deal with sums of random variables that are independent
but not identically distributed. As an example, consider forr< 1 a random series
Zr =
∞∑
k=1
B(r2k),
with Bernoulli variables of parametersr2k that are independent. The random variableZr has the same law
as the number of zeroes with module smaller thanr of a random analytic seriesS(z) =∑∞
n=0anzn, where
the an’s are independent standard complex Gaussian variables (see [FMN16, Section 7.1]). Ifh = 4πr2
1−r2
is the hyperbolic area of the disc of radiusr and center 0, then we showed inloc. cit.that ash goes to
inﬁnity andr goes to 1, denotingZr =Zh, the sequence
Xh = 1
h1/3
(
Zh− h
4π
)
is mod-Gaussian convergent with parametersth = h1/3
8π and limitθ(ξ) = exp( (iξ)3
144π ). Let us compute a
zone of control for this mod-Gaussian convergence. We change a bit the parameters of the mod-Gaussian
convergence and take
~th = Var(Xh) = 1
h2/3
∞∑
k=1
r2k(1−r2k) = h1/3(h + 4π)
4π(2h + 4π).
The precise reason for this small modiﬁcation will be given in Remark 26. Then,
