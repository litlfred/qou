---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-018-35-tau-function-in-the-uncoupled-case
section_title: "Tau function in the uncoupled case"
section_number: 3.5
pages: 13-14
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Suppose given a miniversal variation of finite, uncoupled, integral BPS structures over a complex manifold $M$. We  will show that the family of  solutions given by Theorem \ref{one} has a corresponding $\tau$-function. To describe this function  we first introduce the expression
\begin{equation}\Upsilon(w)=\frac{e^{-\zeta'(-1)}\, e^{\frac{3}{4}w^2} \,G(w+1)}{(2\pi)^{\frac{w}{2}}\,w^{\frac{w^2}{2}}},\end{equation}
where $G(x)$ is the Barnes $G$-function, and $\zeta(s)$ the Riemann zeta function. 

\begin{thm}
\label{doss}
Let $(\Gamma,Z_p,\Omega_p)$ be a framed, miniversal variation of finite, uncoupled, integral BPS structures over a complex manifold $M$. Then the function  
\begin{equation}\tau(Z,t)=\prod_{\Im Z(\gamma)/t>0} \Upsilon\bigg(\frac{Z(\gamma)}{2\pi i t}\bigg)^{\Omega(\gamma)}\end{equation}
is a $\tau$-function for the family of solutions given by Theorem \ref{one}.\end{thm}

The known asymptotics  of the $G$-function imply  that $\tau(Z,t)$  has  an  asymptotic expansion involving the Bernoulli numbers
\begin{equation}\log \tau(Z,t)\sim \frac{1}{24} \sum_{\gamma\in \Gamma} \Omega(\gamma)\log \bigg(\frac{2\pi i t}{Z(\gamma)}\bigg) +\sum_{g\geq 2} \sum_{\gamma\in \Gamma}   \frac{\Omega(\gamma)\cdot B_{2g}}{4g\, (2g-2)} \bigg(\frac{2\pi i t}{Z(\gamma)}\bigg)^{2g-2}\end{equation}
valid as $t\to 0$ in any  half-plane whose boundary rays are not active.
