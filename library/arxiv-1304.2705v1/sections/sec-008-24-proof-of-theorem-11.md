---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-008-24-proof-of-theorem-11
section_title: "Proof of Theorem 1.1"
section_number: 2.4
pages: 10-10
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.808
latex_coverage_ratio: 0.952
---
\lbl{sub.thm1}
 
Fix natural numbers $A$ and $B$ with $B > A \geq 1$, and  
let
$$
t(m)=\frac{(-1)^{A m} q^{A \frac{m(m+1)}{2}}}{(q)^B_m}, \qquad
F(q,x)=\sum_{m=0}^\infty t(m)x^m 
$$
and
$$
\ti t(n)=\frac{(-1)^{(B-A) n} \tq^{(B-A) \frac{n(n+1)}{2}}}{(\tq)^B_n}, 
\qquad
\ti F(\tq,\ti x)=\sum_{n=0}^\infty \ti t(n)x^n \,.
$$
Use Equations \eqref{eq.III} and \eqref{eq.FABmn} and Proposition 
\ref{prop.phiexp} to expand $F_{A,B,m,n}(w)$ as a power series with 
coefficients polynomials in the variables $m, E^{(m)}_l(q)$ and 
$n, \ti E^{(n)}_l(\tq)$ and $b^{\pm 1}$ and $(2 \pi i)^{-1}$. Now apply Lemma
\ref{lem.dconnect} to convert the variables $m, E^{(m)}_l(q),
n, \ti E^{(n)}_l(\tq)$ in terms of the action of the operators $\d,\d_l,\ti \d,
\ti \d_l$ respectively. This concludes the proof of Theorem \ref{thm.1}.
\qed
