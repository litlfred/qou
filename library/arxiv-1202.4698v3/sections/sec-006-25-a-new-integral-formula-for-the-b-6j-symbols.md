---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-006-25-a-new-integral-formula-for-the-b-6j-symbols
section_title: "A new integral formula for the b-6j symbols"
section_number: 2.5
pages: 7-8
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
One of our main results will be the following formula 
for the b-$6j$ symbols:
\begin{align}\label{6j3}


\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{\al_4}\;{}^{\al_s}_{\al_t}\big\}_b^{}
&=\Delta(\al_s,\al_2,\al_1)\Delta(\al_4,\al_3,\al_s)\Delta(\al_t,\al_3,\al_2)
\Delta(\al_4,\al_t,\al_1)\\
&\qquad \times\int\limits_{\CC}du\;
S_b(u-\alpha_{12s}) S_b(u-\al_{s34}) S_b(u -\alpha_{23t}) 
S_b(u-\alpha_{1t4})
\notag \\[-1.5ex] & \hspace{2cm}\times 
S_b( \alpha_{1234}-u) S_b(\alpha_{st13}-u) 
S_b(\alpha_{st24}-u) S_b(2Q-u)\,.
\notag\end{align}
The expression involves the following ingredients:
\begin{itemize}
\item We have used the notations $\al_{ijk}=\al_i+\al_j+\al_k$,
$\al_{ijkl}=\al_i+\al_j+\al_k+\al_l$. 
\item $\Delta(\al_3,\al_2,\al_1)$ is defined as 
\begin{align}
&\Delta(\al_3,\al_2,\al_1)=\bigg(\frac{S_b(\alpha_1+\alpha_2+\alpha_s-Q)}{S_b(\alpha_1+\alpha_2-\alpha_s) 
S_b(\alpha_1+\alpha_s-\alpha_2) S_b(\alpha_2+\alpha_s-\alpha_1)} 
\bigg)^{\frac{1}{2}}\,.
\notag\end{align}
\item The integral is defined in the cases
that $\al_k\in Q/2+\textup{i}\BR$ by a contour $\CC$ which 
approaches $2Q+\textup{i}\BR$ near infinity,
and passes the real axis in the interval $(3Q/2,2Q)$.
For other values of the variables $\al_k$ it is defined by analytic 
continuation.
\end{itemize}
The reader may notice how closely the structure of the expression 
in \rf{6j3} resembles the well-known formulae for the classical 
$6j$ symbols. 

For establishing this relation, the
main step is contained in the following integral identity:
\begin{align}\label{6j2}


\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{\bar\al_4}\,|\,
{}^{\al_s}_{\al_t}\big\}_b^{\rm an}=\mathcal{C}(\underline{\alpha}) 
\int_{\CC'} du\;& 
S_b(u-\alpha_{12s}) S_b(u-\al_{s34}) S_b(u -\alpha_{23t}) 
S_b(u-\alpha_{1t4})
\\ \times & 
S_b( \alpha_{1234}-u) S_b(\alpha_{st13}-u) 
S_b(\alpha_{st24}-u) S_b(2Q-u),
\notag\end{align}
where the contour $\CC'$ in \rf{6j2} runs between $2Q-\textup{i}\infty$
and $2Q+\textup{i}\infty$,
and $\underline{\alpha}$ is shorthand notation for the tuple 
$(\al_1,\al_2,\al_3,\al_4,\al_s,\al_t)$. The prefactor 
$\CC(\underline{\alpha})$ is explicitly given by the expression
\begin{align}
\mathcal{C}(\underline{\alpha}) =& 
\,S_b(-Q+\alpha_1+\alpha_4+\alpha_t) S_b(Q-\alpha_1-\alpha_2+\alpha_s) \nonumber \\ \times & \,S_b(-Q+\alpha_2+\alpha_3+\alpha_t) S_b(Q-\alpha_2+\alpha_3-\alpha_t) S_b(Q+\alpha_2-\alpha_3-\alpha_t) \\ 
\times & \,S_b(Q-\alpha_3+\alpha_4-\alpha_s) S_b(Q-\alpha_3-\alpha_4+\alpha_s) S_b(Q+\alpha_3-\alpha_4-\alpha_s). 
\notag\end{align}
The proof of identity \rf{6j2} is nontrivial. It is described in 
Appendix \ref{idproof}, based on recent advances in the theory
of elliptic generalizations of the 
hypergeometric functions \cite{S1,S2,S3}.
