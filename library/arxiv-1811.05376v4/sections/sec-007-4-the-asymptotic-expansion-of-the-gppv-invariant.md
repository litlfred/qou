---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-007-4-the-asymptotic-expansion-of-the-gppv-invariant
section_title: "The asymptotic expansion of the GPPV invariant"
section_number: 4
pages: 26-27
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
The invention of ˆZ was party motivated by an attempt to generalize the following discovery of
Lawrence and Zagier. Setqk = exp(2πi/k). Forn = 3 they proved in [40] the identity (for some
σ∈ Q)
τk (Σ(p1,p 2,p 3)) (qk− 1)qσ
k =−1
2 lim
q→qk
∞∑
m=m0
χmq
m2
4P .
For a closed oriented3-manifold Y consider the normalized WRT invariant
ZCS(Y ;k) = τk(Y )
τk(S2× S1).
We now state the radial limit conjecture.
Conjecture 2([28]). LetY be a closed oriented3-manifold withb1(Y ) = 0. Set
T = Spinc(Y )/Z2.
For everya∈T, there exists invariants
∆a∈ Q, c∈ Z+, ˆZa(q)∈ 2−cq∆a Z[[q]],
with the following properties. The seriesˆZa(q) is convergent inside the unit disc{q| |q|< 1}, and
for inﬁnitely manyk∈ N the radial limitslimq↑exp(2πi/k) ˆZa(q) exists and we have that
ZCS(Y ;k) = (i
√
2k)−1 ∑
a,b∈T
e2πiklk(a,a)|Wb|−1Sa,b lim
q↑exp(2πi/k)
ˆZb(q).
Here
Sa,b = e2πikl(a,b) +e−2πikl(a,b)
|Wa|
√
|H1(Y ;Z)|
,
andWx is the Z2-stabilizer ofx.
Resurgence Analysis of Quantum Invariants 27
Remark 3. Conjecture 2 appeared in slighly diﬀerent form in [12, 29, 27].
The levelk WRT invariantτk(M) of a closed oriented3-manifoldM can be seen as a function of
thek-root of unityqk = exp(2πi/k), and as such it is a function of a certain subset of the boundary
of the unit discD ={q :|q|< 1}. Assume b1(M) = 0 and deﬁne thek-dependent q-series
ˆZk(M;q) = (i
√
2k)−1 ∑
a,b∈T
e2πik lk(a,a)|Wb|−1Sa,bˆZb(q).
Then ˆZk(M;q) is convergent forq∈ D and the radial limit conjecture states
lim
q↑qk
ˆZk(M;q) =τk(M).
Thus ˆZk(M;q) can be seen as an analytic extension ofτk(M) to the interior of the unit disc as
illustrated in Figure 6 below
1
q 24
q 12
q 6
q k = exp
(
2 πi
k
)
WR T invariant : τ ( M ) : N → C
GPPV invariant : ˆZ k ( M ) : D → C
D = { q : | q | < 1 }
Radial limit : ˆZ k ( M ; q k ) = τ k ( M )
Figure 6: Analytic extension ofτk(M).
