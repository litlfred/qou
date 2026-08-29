---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-037-34-convergence-of-ornsteinuhlenbeck-processes-to
section_title: "Convergence of Ornstein–Uhlenbeck processes to stable laws"
section_number: 3.4
pages: 24-26
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
Another way to approximate a stable lawφc,α,β is by using the marginales of a random process of
Ornstein–Uhlenbeck type. Consider more generally a self-decomposable lawφ on R, that is an inﬁnitely
divisible distribution such that for anyb∈ (0, 1), there exists a probability measurepb on R such that
ˆφ(ξ) =ˆφ(bξ)ˆpb(ξ); (6)
see [Sat99, Chapter 3, Deﬁnition 15.1]. In Equation (6), the lawspb are the marginale laws of certain
Markov processes. Fix a Lévy–Khintchine triplet(l∈ R, ν2∈ R+, ρ) with ρ probability measure on
R\{ 0} that integrates min(1,|x|2), and consider the Lévy process(Zt)t∈R+ associated to this triplet:
E[eiξZt] = exp(tψ(iξ))
= exp
(
t
(
ilξ− ν2ξ2
2 +
∫
R
(eiξx− 1− 1|x|<1iξx)ρ(dx)
))
.
The Ornstein–Uhlenbeck process with triplet(l,ν 2,ρ ), speedv and starting pointx is the solution(Ut)t≥0
of the stochastic diﬀerential equation
Ut = e−vtx +
∫ t
0
e−v(t−s)dZs.
The Ornstein–Uhlenbeck process(Ut)t≥0 can be shown to be a Markov process whose transition kernel
(Pt(x,dy))t≥0 satisﬁes:
ˆPt(x,·)(ξ) =
∫
R
eiξyPt(x,dy) = exp
(
iξe−vtx +
∫ t
0
ψ(iξe−vs)ds
)
see [Sat99, Lemma 17.1]. The connection with self-decomposable laws is provided by:
Theorem 24 (Sato–Yamazato, 1983).For any self-decomposable lawφ and any ﬁxed speedv, there
exists a unique Lévy–Khintchine triplet(l,ν 2,ρ ) with
∫
|x|≥1 log|x|ρ(dx)< +∞, such that the associated
Ornstein–Uhlenbeck process(Ut)t≥0 with speedv satisﬁes:
Mod-φ convergence, II: Estimates on the speed of convergence 25
∀x∈ R, Pt(x,·)⇀φ.
If ψ(iξ) is the exponent associated to(l,ν 2,ρ ), then
ˆφ(ξ) = exp
(∫ ∞
s=0
ψ(iξe−vs)ds
)
.
We refer to [SY83] and [Sat99, Theorem 17.5]. In the setting of Theorem 24, one has the relation
ˆφ(ξ) =ˆφ(e−vtξ)
(
ˆPt(x,·)(ξ) ˆδ−e−vtx(ξ)
)
,
so ifb∈ (0, 1), settingb = e−vt, one recoverspb as the law ofUt− e−vtx, where(Ut)t∈R+ is the Ornstein–
Uhlenbeck process that converges in distribution toφ and that has speedv and starting pointx.
Suppose thatφ =φc,α,β is a stable law. Then, the previous computations can be reinterpreted in the
framework of mod-φ convergence. We set
θ(ξ) =
ˆδx(ξ)
ˆφ(ξ)
= exp(iξx−η(iξ)),
and
Xt =
{
evtUt if α⁄= 1,
evt
(
Ut− 2cβvt
π
)
if α = 1.
Then,
E[eiξXt] =
{
ˆµ(evtξ)θ(ξ) if α⁄= 1,
ˆµ(evtξ) e−iξevt 2cβvt
π θ(ξ) if α = 1,
= eeαvtη(iξ)θ(ξ),
so (Xt)t≥0 converges mod-φ with parameters eαvt, and with limit equal to the residueθ(ξ). Note that
θt =θ for anyt≥ 0, so we are in a special situation where the residues are constant (time-independent).
Assuming thatx⁄= 0, one has for anyξ∈ R
|θ(ξ)− 1|≤



K1|ξ| exp(K2|ξ|α) if α∈ (1, 2],
K1|ξ|α exp(K2|ξ|α) if α∈ (0, 1) or α = 1,β = 0,
K1|ξ| log|ξ| exp(K2|ξ|) if α = 1,β⁄= 0.
For the two ﬁrst cases, the conditionγ≤ min( 1
w−α, v−1
α ) in Theorem 20 imposes the following choices of
γ when computing Berry–Esseen estimates:γ = α−1
α whenα≤ 1, andγ = 0 whenα≥ 1. In these cases,
one obtains:
dKol(Ut,φc,α,β) =
{
O(e−vt) if α∈ (1, 2],
O(e−αvt) if α∈ (0, 1) or α = 1,β = 0.
Because of the termlog|ξ|, the last case does not exactly ﬁt the framework of zones of control, but it is
easy to adapt the proofs and one gets an estimateO(vt e−vt). On the other hand, whenx = 0, the only
diﬀerence with the previous discussion is the caseα∈ (1, 2], where we obtain
|θ(ξ)− 1|≤ K1|ξ|α exp(K2|ξ|α)
and by Theorem 20,dKol(Ut,φc,α,β) =O(e−αvt), choosingγ = α−1
α . So, to summarise:
Proposition 25.Let Y be a random variable with stable lawφc,α,β, and (Ut)t≥0 be the corresponding
Ornstein–Uhlenbeck process with starting pointx and speedv. We have:
