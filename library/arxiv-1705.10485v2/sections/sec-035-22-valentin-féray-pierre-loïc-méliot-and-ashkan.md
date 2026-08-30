---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-035-22-valentin-féray-pierre-loïc-méliot-and-ashkan
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 22
pages: 22-24
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
eηc,α,β(iξ) =
{
e−|cξ|2
if α = 2,
exp
(
imξ +
∫
R(eiξx− 1− 1|x|<1iξx)πc,α,β(dx)
)
if α∈ (0, 2),
where πc,α,β(dx) is the Lévy measure deﬁned forα∈ (0, 2) by
πc,α,β(dx) = c+ 1x>0
x1+α + c− 1x<0
|x|1+α ,
with m∈ R and c+,c−∈ R+ related to (c,α,β ) byβ = c+−c−
c++c−
and
m =
{c+−c−
1−α if α⁄= 1,(∫ 1
0
sint−t
t2 dt +
∫∞
1
sint
t2 dt
)
(c+−c−) if α = 1;
c+ +c− =
{ αcα
Γ(1−α) sin(
π(1−α)
2 ) if α⁄= 1,
2c
π if α = 1.
The proof of the Lévy–Khintchine formula in the general case of an inﬁnitely divisible law involves the
following elementary fact (cf. [Sat99, Chapter 2]): ifµ is inﬁnitely divisible andµ = (ρn)∗n for n≥ 1,
then the compound Poisson lawµn of intensitynρn, which has Fourier transform
ˆµn(ξ) = exp
(∫
R
(eixξ− 1)nρn(dx)
)
,
converges in law towardsµ; thus, any inﬁnitely divisible law is a limit of compound Poisson laws. In the
case of stable laws, this approximation result can be precised in terms of Kolmogorov distances:
Proposition 23.Let Y be a random variable with stable lawφc,α,β, andYn be a random variable with
the following compound Poisson distribution: ifµn is the law ofYn, then its Fourier transform is
ˆµn(ξ) = exp
(∫
R
(eixξ− 1)nφ c
n1/α,α,β(dx)
)
.
The Kolmogorov distance betweenYn and Y is
dKol(Yn,Y )≤



C(α)n−1/α if α∈ (1, 2],
C(α)n−1 if α∈ (0, 1) or α = 1,β = 0,
C′ (logn)2n−1 if α = 1,β⁄= 0,
with constantsC(α) or C′ that depend only on the exponentα.
We thus get a phase transition between the casesα >1 and α <1, with the caseα = 1 that exhibit
distinct transition behaviors according to the value ofβ.
Proof. Let us distinguish the following cases:
• Suppose ﬁrstα /∈{ 1, 2}. The deﬁnition ofYn implies that
E[eiξYn] =ˆµn(ξ) = exp
(
n
(
e
ηc,α,β (iξ)
n − 1
))
.
Set Xn =n1/(2α)Yn, tn =√n and θn(ξ) = E[eiξXn] e−tnηc,α,ξ(iξ). We have
θn(ξ) = exp
(
n
(
e
ηc,α,β (iξ)
n1/2 − 1− ηc,α,β(iξ)
n1/2
))
.
On the zone[−K(tn)1/α,K (tn)1/α] withK = | cos(πα
2 )|
2
α
c , we can use a Taylor formula with an integral
form remainder:
Mod-φ convergence, II: Estimates on the speed of convergence 23
n
(
e
ηc,α,β (iξ)
n1/2 − 1− ηc,α,β(iξ)
n1/2
)
= (ηc,α,β(iξ))2
(∫ 1
0
(1−u) e
uηc,α,β (iξ)
n1/2 du
)
⏐⏐⏐⏐n
(
e
ηc,α,β (iξ)
n1/2 − 1− ηc,α,β(iξ)
n1/2
)⏐⏐⏐⏐≤ 1
2|ηc,α,β(iξ)|2≤ 1
2
(
cα
cos
(πα
2
)
)2
|ξ|2α.
We thus obtain a zone of control for(Xn)n∈N with v =w = 2α, γ = 1
α,
K1 =K2 = 1
2
(
cα
cos
(πα
2
)
)2
,
and one checks that ( cα
2K2
) 1
w−α
=| cos(πα
2 )|
2
α
c =K.
Since we needγ≤ min
(
1
w−α, v−1
α
)
to obtain a bound on the Kolmogorov distance (see the hypotheses
of Theorem 20), this leads to a reduction ofγ when α< 1:
γ + 1
α =
{
2
α if α> 1,
2 if α< 1.
With Theorem 20, we obtain the following upper bound fordKol(Yn,Y ):
1 +λ
απ
(
2
(
cos(πα
2 )
)2 + Γ ( 1
α)
3√π
⏐⏐cos(πα
2 )
⏐⏐2/α
(
4
3
√
1 + 1
λ + 3
3√
3
))
1
n
γ
2 + 1
2α
,
Then, any choice ofλ> 0 gives a constantC(α) that depends only onα.
• When α = 2, the result follows from the usual Berry–Esseen estimates, since√nYn has the law of a
sum ofn independent random variables with same law and ﬁnite variance and third moment.
• If α = 1 and β = 0, then the same computations as above can be performed with a constantK = 1
c,
v =w = 2, γ = 1,
K1 =K2 = c2
2,
and this leads to
dKol(Yn,Y )≤ 1 +λ
π
(
2 + 1
3√π
(
4
3
√
1 + 1
λ + 3
3√
3
))
1
n,
and a constantC = 3.04 when λ = 0.2.
• Let us ﬁnally treat the caseα = 1 , β ⁄= 0 . Recall that we then have ηc,α,β(iξ) = −|cξ| (1 +
2iβ
π sgn(ξ) log|ξ|). We choosetn such thattn logtn =√n, and set
Xn =tnYn + 2cβ
π
√n.
We then have
θn(ξ) = E[eiξXn] e−tnηc,α,β(iξ)
= exp
(2cβiξ
π tn logtn +n
(
e
ηc,α,β (itnξ)
n − 1
)
−tnηc,α,β(iξ)
)
= exp
(
n
(
e
ηc,α,β (itnξ)
n − 1− ηc,α,β(itnξ)
n
))
,
