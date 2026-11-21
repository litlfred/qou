---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-005-semidefinite-program-for-binary-codes
section_title: "Semidefinite program for binary codes"
section_number: null
pages: 10-10
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
Collecting all the mentioned linear and semidefinite constraints, we have the following SDP on $A(n,d)$ with variables $x_{i, j,i',j'}^{t,t'} \in\mathbb{C}$: $$\begin{aligned}
    {\rm maximize\ } &\sum_{a = 0}^{n} \sum_{i+i' = a} \binom{n_{1}}{i}\binom{n_{2}}{i'} x_{i, 0, i', 0}^{0, 0}.  \notag\\
    {\rm subject\ to\ }       &  \mbox{ positive semidefiniteness of }(\ref{sdp_1}), (\ref{sdp_2}),(\ref{sem1}), (\ref{sem2}) \label{eq:main_SDP} 
    \\ & (\ref{sdp_3}),(\ref{eqn:id_1}), (\ref{eqn:id_2}), (\ref{eq:split_cons})  \notag \\
    & (\ref{le3}), (\ref{le4}), (\ref{le5}), (\ref{le6}), (\ref{le7}), (\ref{le14}).    \notag 
\end{aligned}$$

As mentioned in the previous section, the generalized Delsarte's inequalities ([\[eq:split_del\]](#eq:split_del){reference-type="ref" reference="eq:split_del"}) are implicitly included in the SDP.
