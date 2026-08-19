---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-012-2-there-is-a-constant-c13-such-that
section_title: "There is a constant C13 such that"
section_number: 2
pages: 22-24
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
√−1
2π ∂∂ϕ ≥ −C13ω g(4.29)
on M \{x}, where ω g is the K¨ ahler form ofM ;
22
3. ϕ satisﬁes
ϕ ≤C13(4.30)
on M and
ϕ ≥ 2 logd(x) − 2π
δx0
−C13(4.31)
for d(x) ≤δx0.
Proof. Letγ1, · · ·,γ s be the closed geodesics such that length(γi)< 1
1000 .
LetCγi be the corresponding collars. Let
Cγi(Ri − 4) = {x|dist(x,γ i) ≤Ri − 4} i = 1, · · ·s.
For any x0 ∈ M , if x0 ∈ Cγi(Ri − 4) for some i, then let Cδ = Cγi and
deﬁne ϕ =ϕ x0 :M → R as follows
ϕ =



2η(ρ − (R − 3))ϕ 3 ρ ≥ 0 and x ∈Cδ,
2η(−ρ − (R − 3))ϕ 3 ρ< 0 and x ∈Cδ,
0 otherwise,
(4.32)
where the function η is deﬁned in (2.10). By Lemma 4.1, Lemma 4.2 and
the fact that ϕ 3 is harmonic on Cδ\{x0}\{p0}, it is easy to check that the
functionϕ satisﬁes all the assertions in the proposition. On the other hand,
ifx0 /∈Cγi(Ri − 4) for any 1 ≤i ≤s, then by Proposition 4.1, δx0 ≥ε2. The
argument becomes quiet standard: deﬁne
ϕ = 2η(d(x)
ε2
) log(d(x)
ε2
)(4.33)
Then we can prove that ϕ satisﬁes all the requirements by using the same
method as in Lemma 2.3.
Theorem 4.1. Let M be a Riemann surface of genus g ≥ 2 and constant
curvature (−1). Then there are absolute constants m0 > 0 and D >0 such
that for any m > m0 and any x0 ∈ M , there is a section S ∈ H 0(M,K m
M )
with ||S||L2 = 1 such that
||S||(x0) ≥
√m
D(1 + 1√mδ2x0
e
π
δx0 )
.(4.34)
Proof. Letx0 ∈M and Ux0 = {x|dist(x,x 0)<δ x0}. Let z1 be the holo-
morphic function on Ux0 such that the hermitian metric can be represented
as
ds2 = 1
(1 − 1
4 |z1|2)2dz1dz1.
Form> 0 large enough, let
u1 =∂(η( 2|z1|
δx0
))(dz1)m.
23
Then ∂u 1 = 0 and
||∂u 1||2 ≤ 16
δ2x0
(1 − 1
4 |z1|2)m+1
for 1
4δx0 ≤ |z1| ≤ 1
2δx0. Thus there is a C14> 0 such that
∫
M
||∂u 1||2e−ϕ x0 ≤ 1
m
C14
δ4x0
e
2π
δx0.
Let m0 = C13 + 2. By Proposition 2.1, for m > m0, we can ﬁnd a
u ∈ Γ(M,K m
M ) such that ∂u =u1 with
∫
M
||u||2e−ϕ x0 ≤ 1
m(m −C13 − 1)
C14
δ4x0
e
2π
δx0.(4.35)
Let S = η( 2|z1|
δx0
)(dz1)m − u. Then ∂S = 0. Thus S is an element of
H 0(M,K m
M ). Furthermore, since
∫
Me−ϕ x0 = +∞, we must have u(x0) = 0.
So
||S||(x0) = 1.(4.36)
On the other hand,
||S||2
L2 ≤ 2(
∫
M
||u||2 +
∫
M
||η(dz1)m||2).
By (4.35) and (4.30), we have
∫
M
||u||2 ≤ 1
m(m −C13 − 1) · C14eC13
δ4x0
e
2π
δx0.(4.37)
We also have ∫
M
||η(dz1)m||2 ≤ π
m.(4.38)
The theorem follows from (4.36), (4.37) and (4.38).
