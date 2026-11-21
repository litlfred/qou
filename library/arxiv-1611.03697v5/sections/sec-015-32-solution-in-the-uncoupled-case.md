---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-015-32-solution-in-the-uncoupled-case
section_title: "Solution in the uncoupled case"
section_number: 3.2
pages: 10-11
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
In the case of a finite, uncoupled,  integral BPS structure, and for certain choices of $\xi\in \bT$, the Riemann-Hilbert problem introduced above has a unique solution, which can be  written explicitly in terms of products of modified gamma functions. The inspiration for this comes from work of Gaiotto \cite[Section 3.1]{G}.



 Consider the multi-valued meromophic function on $\bC^*$ defined by
\begin{equation}\label{who}\Lambda(w)=\frac{e^w \cdot\Gamma(w)}{\sqrt{2\pi}\cdot w^{w-\half}}.\end{equation}
Taking the principal value of $\log$ on $\bC^*\setminus\bR_{<0}$, we consider $\Lambda(w)$ as a single-valued holomorphic function on this domain. The formula \eqref{who} is obtained by exponentiating  the initial terms in the Stirling expansion, and  it follows that $\Lambda(w)\to 1$ as $w\to \infty$ in  any closed subsector of $\bC^*\setminus\bR_{<0}$.


\begin{thm}
\label{one}
Let $(Z,\Gamma,\Omega)$ be a finite,  uncoupled, integral BPS structure. Suppose that $\xi\in \bT$ satisfies $\xi(\gamma)=1$ for all active classes $\gamma\in \Gamma$. Then Problem \ref{an}  has the unique solution
\begin{equation}\Psi_\beta(t)= \prod_{\Im Z(\gamma)/t>0} \Lambda\bigg(\frac{Z(\gamma)}{2\pi i t}\bigg)^{\Omega(\gamma)\<\beta,\gamma\>}
\end{equation}
where the product is  over the finitely many active classes $\gamma\in \Gamma$ with $\Im Z(\gamma)/t>0$.
\end{thm}


Note that there do indeed exist elements $\xi\in \bT$ satisfying the condition of Theorem \ref{one}. Indeed, the uncoupled assumption implies that the active classes $\gamma\in \Gamma$ span a subgroup $\Gamma_a\subset \Gamma$ on which the form $\<-,-\>$ vanishes. Any basis of this primitive subgroup can be combined with the pullback of a basis of the quotient $\Gamma/\Gamma_a$, to give a basis $(\gamma_1,\cdots,\gamma_n)$ for $\Gamma$, and an element $\xi\in \bT$ can be defined by making arbitrary choices $\xi(\gamma_i)\in \{\pm 1\}$. 
The proof of Theorem \ref{one} is a good  exercise in the basic  properties of the gamma function. The details are given in Section \ref{sol}.
