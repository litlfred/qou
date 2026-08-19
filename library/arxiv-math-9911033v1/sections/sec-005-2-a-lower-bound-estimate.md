---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-005-2-a-lower-bound-estimate
section_title: "A lower bound estimate"
section_number: 2
pages: 4-7
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
Suppose that M is a Riemann surface of genus g ≥ 2. Let KM be the
canonical line bundle over M with the Hermitian metric H. We assume that
the curvature ω g of H is positive and ω g deﬁnes a K¨ ahler metric ofM .
Let K be the Gauss curvature of the metric ω g. Let K1 and K2 be two
nonnegative constants such that
−K1 ≤K ≤K2.(2.1)
Letδ′ be the injective radius of M with and
δ = min(δ′, 1
√K1 +K2
).(2.2)
Letx0 ∈M be a ﬁxed point. Let U be the open set
U = {dist(x,x 0)<δ }.
4
It is well known that at each point of U there is an isothermal coordinate. In
the ﬁrst part of this section, we prove that there is a holomor phic function z
onU which gives the isothermal coordinate of U with the required estimate.
Consider the equation
{
∆ h =K/ 2
h|∂U = 0,(2.3)
where ∆ is the (complex) Laplacian of M . The solution h exists and is
unique. Let ds2 be the Riemann metric of U . Then we have
Lemma 2.1. The metric ehds2 on U is a ﬂat metric.
Proof. A straightforward computation using (2.3).
Since U is an open set which is diﬀermorphic to an open set in the Eu-
clidean plane, we can assume that there are global frames on U . Let ω 1 and
ω 2 be 1-forms on U such that
ehds2 =ω 2
1 +ω 2
2.
Letω 12 be the connection 1-form deﬁned by
dω 1 =ω 12 ∧ω 2,
dω 2 = −ω 12 ∧ω 1.(2.4)
Then by Lemma 2.1, dω 12 = 0. It follows that there is a real smooth function
σ on U such that
ω 12 =dσ.(2.5)
Let
ξ =eiσ (ω 1 +iω 2).
Then by (2.4) and (2.5), we have
dξ = 0.
Thus there is a function z on U such that
ξ =dz,
and
ehds2 =dzd
z.(2.6)
Either z or
z will be holomorphic because it deﬁnes a conformal structure
ofU . Without losing generality, we assume that z is holomorphic and at x0,
z = 0.
We have the following lemma:
Lemma 2.2. Letρ be the distance to the point x0. ρ(x) = dist(x,x 0). Then
1
3ρ ≤ |z| ≤ 3ρ(2.7)
for ρ<δ .
5
Proof. By the Gauss Lemma [3, page 8], the Riemann metric ds2 can be
written as
ds2 =dρ2 +f 2(ρ,θ )dθ2
for the polar coordinate ( ρ,θ ) where f (ρ,θ ) is a smooth function satisfying
f (0,θ ) = 0, ∂f
∂ρ (0,θ ) = 1,
and
∂ 2f
∂ρ 2 = −Kf.
By the Hessian comparison theorem [10, page 4], we have
∆ ρ ≥
√K2
4 cot
√
K2ρ.
In particular, ∆ ρ ≥ 0 on U . Noting that ∆ is the complex Laplacian, we
have
∆ ρ2 = 1
2 |∇ρ|2 + 2ρ∆ ρ ≥ 1
2.(2.8)
By (2.8), we have
∆( h +K1ρ2) ≥K/ 2 +K1/ 2 ≥ 0,
∆( h −K2ρ2) ≤K/ 2 −K2/ 2 ≤ 0.
By the maximal principle, we have
−1 ≤ −K2δ2 ≤h|∂U −K2ρ2 ≤h ≤h|∂U +K1ρ2 ≤K1δ2 ≤ 1.(2.9)
Letds2
1 =ehds2 denotes the ﬂat metric. Then
e−1ds2 ≤ds2
1 ≤eds2.
By (2.6), |z| is the distance to the point x0 with respect to the metric ds2
1.
Thus by (2.9),
1
3ρ ≤e−1ρ ≤ |z| ≤ eρ ≤ 3ρ.
Proof of Theorem 1.1. Deﬁne a smooth function η : R+ → R such that
η(t) =
{ 0 t ≥ 1,
1 0 ≤t ≤ 1
2.(2.10)
We assume that |η′| ≤ 4 and |η′′| ≤ 4.
In the rest of this paper C1,C 2, · · ·, are absolute constants, unless other-
wise stated.
Let δ1 = 1
4δ. Deﬁne the smooth function r on M such that
r =
{
η( |z|
δ1
) log( |z|
δ1
) x ∈U,
0 x /∈U.(2.11)
6
r is well deﬁned. For if x ∈∂U , then ρ =δ. By the Lemma 2.2, |z| ≥ 4
3δ1
and thus r|∂U = 0 using either expression.
Note that if z ⁄= 0, then ∆ log( |z|) = 0. Deﬁne the function ψ such that
ψ = ∆ r for z ⁄= 0 and ψ = 0 for z = 0. We have
Lemma 2.3. There is a constant C1> 0 such that
{
|ψ | ≤ C1
δ2,∫
M |ψ | ≤ C1.(2.12)
Proof. A straightforward computation gives
ψ = ∆ r = 1
4eh( 1
δ2
1
η′′ log( |z|
δ1
) +η′ 1
δ1|z| log( |z|
δ1
) + 2η′ 1
δ1|z| )(2.13)
for δ1
2 <z <δ 1. Using (2.9), (2.10), we have the estimate
|ψ | ≤ C2
δ2
for some constant C2. To get the estimate of the
∫
M |ψ |, we ﬁrst see that
by the volume comparison theorem [10, page 11],
vol(U ) ≤ 2π ( cosh √K1δ − 1
K1
).
Since √K1δ ≤ 1, there is a constant C3 such that
vol(U ) ≤C3δ2.(2.14)
The lemma follows by setting C1 = max(C2,C 2C3).
Let G(x,y ) be the Green’s function of M . That is,
{ ∆ xG(x,y ) = 1
