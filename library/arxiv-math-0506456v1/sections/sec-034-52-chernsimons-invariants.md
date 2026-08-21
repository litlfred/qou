---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-034-52-chernsimons-invariants
section_title: "Chern–Simons invariants"
section_number: 5.2
pages: 35-37
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
We begin by recalling formulas from [18] for the Chern–Simons invarian ts of the
ﬂat SU(2)–connections on Mp/q. The basic tool will be Theorem 6 below due to P.
A. Kirk and E. P. Klassen.
Let M be a closed oriented 3–manifold with a knot K in its interior and let
X be the complement of a tubular neighborhood of K in M . Moreover, let µ be
a meridian of K and λ a longitude, both in ∂X . Let G be SU(2) or SL(2 , C). If
ρ :π1(X) →G is a representation, then ρ extends to a G–representation of π1(M )
if and only if ρ(µ) = 1. Now assume that ρt : π1(X) → G is a piecewise smooth
path of representations, t ∈I = [0, 1]. Choose a piecewise smooth path g :I →G
such that
gtρt(µ)g−1
t = diag
(
e2πiα(t),e −2πiα(t)
)
,
gtρt(λ)g−1
t = diag
(
e2πiβ(t),e −2πiβ(t)
)
(5.66)
for some piecewise smooth curves α,β . If G = SU(2) this is always possible by [18,
Lemma 3.1], and in that case α and β are real-valued. If G = SL(2, C) the above
is possible if the path ρ avoids the parabolic representations (i.e. upper triangular
with 1s or −1s on the diagonal), cf. [18, Remark p. 354]. (See the text in connec tion
to (5.63) for the case of the ﬁgure 8 knot.) In that case the curve s α and β are
complex-valued. We then have
Theorem 6 ( [18, Theorem 4.2] ). Assume that ρ0(µ) = ρ1(µ) = 1. Thinking
of ρ0 and ρ1 as ﬂat G–connections on M , we have
CS(ρ1) − CS(ρ0) = −2
∫ 1
0
β(t)α′(t)dt (mod Z),
where CS is the Chern–Simons functional associated to G.
We note that in case G = SL(2, C) the Chern–Simons functional takes values in
C/Z.
36 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Next consider a knot K in S3 and let X be the knot complement. Let p/q be
a rational number and let Np/q be the closed oriented 3–manifold obtained by p/q
surgery onS3 alongK. Let µ andλ be classes in π1(∂X ) represented by respectively
a meridian and the preferred longitude of K. Choose integers c,d ∈ Z such thatpd−
qc = 1. Let V be a tubular neighborhood of K considered as a subspace of Np/q. We
note that µ′ =pµ +qλ andλ′ =cµ +dλ are represented by respectively a meridian
of V and a longitude of V . Assume that ρt : π1(X) → G, t ∈ I, is a piecewise
smooth curve of representations from the trivial representatio n to a representation,
which extends to a representation of π1(Np/q), i.e. ρ1(µ′) = 1. Assume, moreover,
thatρt avoids the parabolic representations in case G = SL(2, C), and choose curves
α,β as in (5.66) with α(0) = β(0) = 0. By Theorem 6 we have
CS(ρ1) = −2
∫ 1
0
(cα(t) +dβ(t))(pα′(t) +qβ ′(t))dt (5.67)
= −2
∫ 1
0
β(t)α′(t)dt −cpα2(1) −dqβ 2(1) − 2cqα(1)β(1) (mod Z).
(We have corrected a sign error in [18, Formula (*) p. 361].) We note t hat this
expression is independent of the choice of c,d . The condition ρ1(µ′) = 1 is equivalent
to
pα(1) +qβ(1) ∈ Z. (5.68)
Now let K be the ﬁgure 8 knot and let ¯ ρθ,ε be a SU(2)–representation of π1(Mp/q),
i.e. (5.65) is satisﬁed. Following [18] we determine a formula for CS(¯ ρθ,ε). For later
we will here pay special attention to the branches of the logarithm. By Proposition 2
we have
Re (L−(θ)) = Re ( L+(θ)) = 2 cos 2(4πθ) − cos(4πθ) − 2,
Im (L±(θ)) = ∓2 sin(4πθ)
√
cos2(4πθ) − cos(4πθ) − 3
4 (5.69)
for all θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3]. From these identities we see that
L±(1/3) = L±(1/6) = −1, L ±(1/4) = 1, (5.70)
and that Im( L+) < 0 and Im( L−) > 0 on ]1 /6, 1/4[ with the opposite signs on
]1/4, 1/3[. We conclude that L+(θ) and L−(θ) run through S1 both beginning and
ending in −1, L+ in the anti-clockwise and L− in the clockwise direction, as θ
runs through [1/6, 1/3]. We can therefore use the principal logarithm Log to deﬁne
continuous curves β± : [1/6, 1/3] → R by
β±(θ) = 1
2πi Log(L±(θ)) +f±(θ), (5.71)
where
f+(θ) =
{
0, θ = 1
6,
1, θ ∈] 1
6, 1
3 ], (5.72)
Asymptotics of the quantum invariants for the ﬁgure 8 knot 37
and
f−(θ) =
{
0, θ ∈ [ 1
6, 1
3 [,
−1, θ = 1
3. (5.73)
By (5.65) and the deﬁnition of β± the representation ¯ρθ,ε extends to a representation
of π1(Mp/q) if and only if
pθ +qβε(θ) ∈ Z (5.74)
which is nothing but (5.68) (reparametrized). We note that β± are smooth on ] 1
6, 1
3 [
but not in the end points 1 /6 and 1 /3. The terms f± have been chosen so that
β±(1/6) = 1/2. This is needed for the proof of
Proposition 4 ( [18, p. 362] ). Let θ ∈ [1/6, 1/3] and let ¯ρθ,± be as in Proposi-
tion 2. If ¯ρθ,ε extends to a representation of π1(Mp/q) for a ε ∈ {±1} then
CS(¯ρθ,ε) = − 1
6 −cpθ2 −dqβ 2
ε (θ) − 2cqθβε(θ) − 2
∫ θ
1/6
βε(t)dt (mod Z),
where β± are the curves deﬁned by (5.71).
Kirk and Klassen prove the above result by explicitly constructing a p iecewise
smooth path ρ : [0, 1] → Hom(π, SL(2, C)) from the trivial representation to ¯ρ 1
6,+ =
¯ρ 1
6,− with piecewise smooth curves α,β : [0, 1] → C as in (5.66) satisfying α(1) = 1
6
and β(1) = 1
2 . Moreover, they use that
∫ 1
0 β(t)α′(t)dt = 1
12 and the fact that
y ↦→¯ρy,ε, [1/6,θ ] → Hom(π, SU(2)) is a path from ¯ ρ 1
6,ε to ¯ρθ,ε with associated
functions α(y) = y and β(y) = βε(y). By the choice of the functions f±, these α–
and β–functions are continuations of the ones used for the path ρ from the trivial
representation to ¯ρ 1
6,±.
Kirk and Klassen argue that
∫ 1
0 β(t)α′(t)dt = 1
12 using a comparison between a
computer calculation and the Chern–Simons invariants of ﬂat SU(2) –connection on
the Seifert manifold M−3. By following Kirk and Klassen’s argument [18, pp. 361–
362] it is actually not hard to give an explicit calculation of this integral. Let us give
some details. The path ρ from the trivial connection to ¯ρ 1
6,± consists of three parts,
whereβ is identically zero along the ﬁrst two parts. We can therefore conce ntrate on
the third part. Let a = (3+
√
5)/2, and letα : [0, 1] → C be a piecewise smooth curve
from 1
2πi Log(√a) to 1/6. Let t(s) = e4πiα(s) and choose a piecewise smooth solution
u(s) to φ(t(s),u (s)) = 0, where φ is given by (5.61). Then s ↦→ρ(e2πiα (s),u(s)) =:ηs
is the third piece of our curve ρ (reparametrized). Assuming α(s) /∈ 1
