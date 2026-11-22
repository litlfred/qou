---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-011-state-integrals
section_title: "State integrals"
section_number: null
pages: 11-12
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
10
(b) If the shadow coloring avoids the unit circle, then none of the poles of the function CE →C
deﬁned by
t 7→exp NSN(D, µ|β/N + t)
occur for t ∈RE.
⌟
Proof. (a) Equation (3.3) gives the quasi-periodicity relation
eϕN(ζ/N+1) =
eϕN(ζ/N)
(1 −e2πi(ζ+1)/N) · · · (1 −e2πi(ζ+N)/N) = eϕN(ζ/N)
1 −e2πiζ
so
exp Ω+
N

µ

β1
N + 1, β2
N , β1′
N , β2′
N

= exp Ω+
N

µ

β1
N , β2
N , β1′
N , β2′
N

(1 −b2′/b1)
m(1 −b2/mb1)
= a1 exp Ω+
N

µ

β1
N , β2
N , β1′
N , β2′
N

where a1 is the parameter assigned to the segment by equation (2.8). Similarly
exp Ω+
N

µ

β1
N , β2
N , β1′
N + 1, β2′
N

= a−1
1′ exp Ω+
N

µ

β1
N , β2
N , β1′
N , β2′
N

and more generally the incoming segment variables have quasi-periodicity constant ai and the
outgoing have a−1
i . When the crossing functions Ωϵ
N(µ) are assembled together into SN(D, µ)
these factors cancel: the ai match because the bi = e2πiβi are a solution of the gluing equations.
(b) Recall that the zeros and poles of eϕN(z) all occur when z ∈
1
N Z. The arguments of the
quantum dilogarithms ϕN in equations (3.5) and (3.6) are of the form ζ/N + ti −tj with e2πiζ the
shape parameter of the relevant tetrahedron. Because (ρ, u) avoids the unit circle Im ζ̸ = 0 for
each tetrahedron so we do not encounter any singularities when t ∈RE.
3.3. State integrals
Deﬁnition 3.5. The state integrals associated to a log-coloring β are
(3.9)
JN(D, µ, β|k) :=
Z
[0,1]E exp N (SN(D, µ|t + β/N) −2πik · t) dt
for each integer vector k ∈ZE.
Theorem 1. Under the hypotheses above Zψ
N is given by the sum
(3.10)
Zψ
N(K, ρ, µ) = N |E|/2−1/2 X
k∈ZE
JN(D, µ, β|k)
over all state integrals.
⌟
Proof. Deﬁne a function F : RE →C by F(t) := exp(NSN(D, µ|t + β/N)). It restricts to a
not-necessarily continuous, periodic function f : CE/ZE →C. By Lemma 3.4(b) F is smooth
and in particular
(3.11)
Z
[0,1]E

∂F(t)
∂ti

 dt =
Z
CE/ZE

∂f(t)
∂ti

 dt < ∞for all i ∈E.
