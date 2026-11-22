---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-039-72-voros-symbols
section_title: "Voros symbols"
section_number: 7.2
pages: 35-36
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.804
latex_coverage_ratio: 0.994
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
The weak Riemann-Hilbert problem (see Remark \ref{oh}(iii)) defined by the above BPS structures  can be solved using exact WKB analysis of an associated Schr{\"o}dinger equation.  This was  essentially proved by Iwaki and Nakanishi \cite{IN} following Gaiotto, Moore and Neitzke \cite{GMN2}.


Suppose given a quadratic differential $(S,q)$ as above. Let us also choose 
 a projective structure  on the Riemann surface $S$.\footnote{ If the quadratic differential $q$ has a double pole at a point $p\in S$ one should assume that this projective structure (represented in \cite{IN} by the term $Q_2(z)$) also has a pole of a particular form \cite[Assumption 2.5]{IN}.}
We can then invariantly consider the holomorphic Schr{\"o}dinger equation
\[\hbar^2 \frac{d^2}{dz^2} y(z,\hbar) = q(z)\cdot y(z,\hbar),\]
where $z$ is a co-ordinate in the chosen projective structure.
The WKB method involves substituting
\[y(z_1,\hbar)=\exp\Big( \int_{z_0}^{z_1} T(z)\,dz \Big), \qquad T(z)=\sum_{k\geq 0} T_k(z) \cdot \hbar^{k-1},\]
and then solving for $T_j(z)$ order by order. This gives rise to a recursion
\[\frac{dT_{k-1}}{dz}+\sum_{i+j=k} T_i(z) T_j(z)=0,\quad k>0,\]
together with the initial condition $T_{0}(z)^2 =q(z)$. Depending on the choice of square-root taken to define $T_0(z)$ one then obtains two systems of solutions $T_k^{\pm}(z)$. The differences
\[\omega_k(z)=\frac{1}{2} \big(T^+_k(z) -T^-_k(z)\big) dz\]
are single-valued meromorphic one-forms on the spectral cover $\hS$, which vanish unless $k$ is even. One has $\omega_0=\sqrt{q(z)} \, dz$.

The formal cycle Voros symbol associated to a class $\gamma\in \Gamma$ is the formal sum
\begin{equation}\exp(V_\gamma)= \exp\Big(\frac{1}{\hbar} \int_\gamma \omega_0\Big)\cdot \exp\Big(\sum_{g\geq 1} \hbar^{2g-1} \int_\gamma \omega_{2g} \Big).\end{equation}



Iwaki and Nakanishi, relying on analytic results of \cite{KoSc},  show that if $\rr\subset \bC^*$ is a non-active ray for the BPS structure defined by $(S,q)$, then the sum over $g\geq 1$ in the above formal expressions can be Borel summed in the direction $\rr$. This results in Voros symbols which are holomorphic functions of $t=\hbar$ defined in a neighbourhood of $0$ in the half-plane $\bH_\rr$. They also compute the wall-crossing behaviour for these Borel sums as one varies the active ray $\rr\subset \bC^*$.
 


\begin{claim}
Given a quadratic differential $(S,q)$ as above,  the Borel sums of the cycle Voros symbols  give a solution to the corresponding weak Riemann-Hilbert problem  with $t=\hbar$.
\end{claim}
\smallskip

\noindent{\it Sketch proof.}
For the definition of the weak Riemann-Hilbert problem see Remark \ref{oh}(iii). The claim should follow from  the work of Iwaki and Nakanishi \cite{IN}, although a careful proof would require additional continuity arguments to take care of differentials with multiple saddle connections. See particularly Theorem 2.18, Theorem 3.4 and formula (2.21). \qed
\smallskip

It is interesting to ask whether given a suitable choice of base projective structure, the Voros symbols in fact give solutions to the full Riemann-Hilbert problem as stated in Section \ref{real}.  Another interesting topic for further research is the connection with topological recursion \cite{ey}, which is known to be closely related to exact WKB analysis. In particular, it is interesting to ask whether the $\tau$-function computed by topological recursion gives a $\tau$-function in the sense of this paper.








\begin{appendix}







\section{Variations of BPS structure}
\label{two}




For BPS structures satisfying the conditions of Proposition \ref{barneyy}, the BPS automorphisms $\bS(\ell)$ can be realised   as birational automorphisms of the twisted torus $\bT$. In general however, even for BPS structures coming from quivers with potential, this is not the case.  Thus we need some other approach to defining a variation of BPS structures. If we want to avoid making unnecessary assumptions, the only way to proceed is via formal completions of the ring $\bC[\bT]$. In this section we give a rigorous definition along these lines following Kontsevich and Soibelman \cite[Section 2]{KS1}.
