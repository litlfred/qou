---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-005-21-step-1-applying-symmetric-conditions
section_title: "Step 1: Applying symmetric conditions"
section_number: 2.1
pages: 4-5
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.826
latex_coverage_ratio: 0.792
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
We first choose the leading coefficients $p_2$ and $p_{-2}$ to be the same as those of the A-polynomial squared. Namely we let
$$p_2(t,M)= \tilde{a}_2(M)=1 \hspace{4mm}\text{and}\hspace{4mm} p_{-2}(t,M)=\tilde{a}_{-2}(M)=1.$$
We see that this takes care of equation \eqref{eq: e2}. Then
$$
b_1(t,M) = \frac{1}{a_1(t,t^2 M)}  \hspace{4mm}\text{and}\hspace{4mm}
b_{-1}(t,M) = \frac{1}{a_{-1}(t,t^{-2} M)}. 
$$
This implies that 
\begin{eqnarray}
p_1(t,M) &=& a_1(t, M) b_0(t, M) + \frac{a_0(t, t^2 M)}{a_1(t, t^2 M)},  \label{eq:q1}\\
p_{-1}(t,M) &=&  a_{-1}(t, M) b_0(t, M) +  \frac{a_0(t, t^{-2} M) }{a_{-1}(t,t^{-2} M)}, \\
p_0(t,M) &=& a_0(t, M) b_0(t, M)  + \frac{a_1(t, t^{-2} M) }{a_{-1}(t,t^{-2} M)} +  \frac{a_{-1}(t, t^2 M)}{a_1(t,t^2 M)}. \label{eq:q0}
\end{eqnarray}

Since $a_1(t,M) = - a_{-1}(t,M^{-1})$ and $a_0(t,M) = - a_0(t,M^{-1})$, we see that equations $p_1(t,M)=p_{-1}(t,M^{-1})$ and $p_0(t,M)=p_0(t,M^{-1})$ are equivalent to a single equation
\be\label{eq: b0}
b_0(t,M^{-1})=-b_0(t,M).
\ee
Hence conditions \eqref{eq: e1} and \eqref{eq: e0} become equation \eqref{eq: b0}.
