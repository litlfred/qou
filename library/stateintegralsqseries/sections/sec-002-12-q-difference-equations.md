---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-002-12-q-difference-equations
section_title: "q-difference equations"
section_number: 1.2
pages: 4-4
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
toc_source: outline
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
Consider the operators ˆx and ˆE which act on f(x) ∈Q(q)[[x]] by:
( ˆEf)(x) = f(qx),
(ˆxf)(x) = xf(x) .
Observe that ˆEˆx = qˆx ˆE.
Lemma 1.5. (a) We have:
(10)
FA,B(q−1, x) = eFA,B(q, x) .
(b) FA,B satisﬁes the linear q-diﬀerence equation
(11)

(1 −ˆE)B −(−1)AqAx ˆEA
FA,B(q, x) = 0 .
Corollary 1.6. (a) If we deﬁne ω(q, x) = FA,B(q, qx)/FA,B(q, x) and ω(q, x)n = Qn
j=1 ω(q, qjx),
then ω satisﬁes the nonlinear equation
B
X
j=0
(−1)j
B
j

ω(q, x)j −(−1)AqAxω(q, x)A = 0 .
(b) F is an admissible power series in the sense of Kontsevich-Soibelman [KS11, Sec.6], the
limit limq→1 ω(q, x) = ω(x) ∈Q[[x]] exists and satisﬁes the algebraic equation (also known
as the Nahm equation or the gluing equation)
(12)
(1 −ω(x))B = (−1)Axω(x)A .
The Nahm equation has been studied by several authors including [Zag07, Sec.3], [Vla,
VZ11], [RV, Sec.4].
