---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-010-27-step-7-explicit-solution
section_title: "Step 7: Explicit solution"
section_number: 2.7
pages: 9-9
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 1.0
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
The polynomial we are constructing is
$$P(t, M, L)=L^2+L^{-2}+p_1(t,M)L+p_{-1}(t,M)L^{-1}+p_{0}(t,M)$$
where
\begin{eqnarray*}
p_1(t,M) &=& a_1(t, M) b_0(t, M) + \frac{a_0(t, t^2 M)}{a_1(t, t^2 M)},  \\
p_{-1}(t,M) &=&  a_{-1}(t, M) b_0(t, M) +  \frac{a_0(t, t^{-2} M) }{a_{-1}(t,t^{-2} M)}, \\
p_0(t,M) &=& a_0(t, M) b_0(t, M)  + \frac{a_1(t, t^{-2} M) }{a_{-1}(t,t^{-2} M)} +  \frac{a_{-1}(t, t^2 M)}{a_1(t,t^2 M)}.
\end{eqnarray*}
Having now an explicit expression for $b_0$, we obtain 
\begin{eqnarray*}
p_1(t,M)&=&\frac{-1 - t^{16} + M^4 t^8 (1 + t^4)^2 + M^2 (t^4 + t^{12}) + 
 M^6 (t^{8} + t^{16}) - M^8 (t^{12} + t^{20})}{M^{4}t^{10}}, \\
 p_{-1}(t,M)&=&\frac{M^4 t^8 (1 + t^4)^2 - t^{12} (1 + t^8) + M^6 (t^4 + t^{12}) - M^8 (1 + t^{16}) + M^2 (t^8 + t^{16})}{M^4t^{10}}, \\
p_0(t,M)&=&\frac{1}{M^8t^4}\big(t^8 + M^{16} t^8 - M^4 t^8 (2 + t^4) - M^{12} t^8 (2 + t^4) - 
 M^2 (t^4 + t^8)\\
 && + \, M^6 (t^4 + t^8) + M^{10} (t^4 + t^8) - M^{14} (t^4 + t^8) + 
 2 M^8 (1 + t^4 + 2 t^8 + t^{12})\big).
\end{eqnarray*}

Then the polynomial $P \in\mathcal{R}[M^{\pm1},L^{\pm1}]$ constructed above satisfies $PJ_E\in \mathcal{R}[M^{\pm 1}]$, $\sigma(P)=P$ and $\varepsilon(P)= ( A'_E )^{2}$. We will also verify $PJ_E\in \mathcal{R}[M^{\pm 1}]$  directly in the next subsection. Hence, by Lemma \ref{Plem} we have $\sqrt{\varepsilon(\mathcal{A}^{\sigma}_E)}\subset \mathfrak{p}_E$. This completes the proof of the strong AJ conjecture for the figure eight knot.
