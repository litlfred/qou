---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-027-82-the-principal-series-representation
section_title: "The principal series representation"
section_number: 8.2
pages: 77-79
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
By taking the pairing above with the fundamental corepresentatio n deﬁned in Sec-
tion 7.2, we obtain:
Theorem 8.6. The fundamental corepresentation T λ,t corresponds to the repre-
sentationPλ,t, called the principal series representation , given on L2(R,ds ) by:
K0 = eπbt,
K = e−πbs,
E = [ Q
2b− i
b (s−λ)]qe−2πbps,
F = [ Q
2b + i
b (s +λ)]qe2πbps,
where [n]q = qn−q−n
q−q−1 . The operators are all positive essentially self-adjoint.
77
Proof. Recall that we choose c =−iq1/2 in the pairing. Recall also that we have to
multiply the expressions by Gb(Q+iα)Gb(Q+iτ )
(1−q2)ib−1 (α +τ ) . From the expression (7.31) we obtain
for K0 and K that τ = α = 0. The factor becomes lim
α− →0
Gb(−iα)Gb(Q +iα) = 1
and the rest becomes
K0 :f (s) ↦→ f (s)· (q−1/2)ib−1(t−s)(q−1/2)ib−1(t+s)
= eπbtf (s),
K :f (s) ↦→ f (s)· (q−1/2)ib−1(t−s)(q1/2)ib−1(t+s)
= e−πbsf (s).
ForE, we have τ =−ib,α = 0 so that the factor lim
α− →0
Gb(−iα)Gb(Q +iα) = 1 as
well, and we obtain
E :f (s) ↦→ −iq1/2f (s +ib)
1−q2
Gb( Q
2−is +iλ +b)
Gb( Q
2−is +iλ)
eπλb−2πbs+πbt· (qib−1(t−s))
= iq−1/2
q−q−1 (1−e2πib( Q
2 −is+iλ))eπb(λ−s)f (s +ib)
= i
q−q−1 (q1/2eπb(s−λ) +q−1/2e−πb(s−λ))f (s +ib)
= [ Q
2b− i
b (s−λ)]qf (s +ib).
Finally, forF we haveα =−ib,τ = 0, the factor lim
α− →−ib
Gb(−iα)Gb(Q +iα) =−q2,
and we obtain
F :f (s) ↦→ iq−1/2(−q2)f (s−ib)
1−q2
Gb( Q
2−is−iλ)
Gb( Q
2−is−iλ−b)
e−πλb+πbt· (qib−1(t+s))
= iq1/2
q−q−1 (1−e2πib( Q
2 −is−iλ−b))e−πb(λ+s)f (s−ib)
= i
q−q−1 (q−1/2eπb(s+λ) +q1/2e−πb(s+λ))f (s−ib)
= [ Q
2b + i
b (s +λ)]qf (s−ib).
Since i
q−q−1 = 1
2 sin(πb2) > 0, we immediately see that the operators are positive.
We note that the expression for E can be rewritten as
E = i
q−q−1 (eπb(s−λ−ps) +eπb(λ−s−ps)), (8.6)
where the summand q2-commutes. Hence using Proposition 4.1, it is unitary equiv-
alent to eπb(s−λ−ps) which in turn is equivalent to e−πb(ps+λ) by multiplication by
78
e−πis2
. Hence it is essentially self-adjoint. Similar analysis applies to F , hence all
operators are positive essentially self-adjoint.
Remark 8.7. We note that by restricting to Uq(sl(2, R)), this is precisely (the
Fourier transform of ) the continuous series representatio nPs obtained in [2] given
by
Kδ k = e−πbkδk,
Esδk = [ Q
2b− i
b (k−s)]qδk+ib,
Fsδk = [ Q
2b + i
b (k +s)]qδk−ib
under the correspondences s←→k,λ←→s.
