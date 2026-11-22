---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-053-b5-birational-transformations
section_title: "B.5. Birational transformations"
section_number: null
pages: 48-50
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{birat}


The following example was first observed by Kontsevich and Soibelman \cite[Section 2.5]{KS1}.
Suppose that a ray $\ell$ contains a single active class $\gamma$, and that moreover $\Omega(\gamma)=1$.  The series $\DT(\ell)$ is then the dilogarithm
\[\DT(\ell)=-\sum_{n\geq 1} \frac{x_{n\gamma}}{n^2}=-\sum_{n\geq 1} \frac{x_{\gamma}^n}{n^2}.\]
This converges absolutely for $|x_\gamma|<1$ and hence defines a holomorphic function on the open subset \[U(R)=\{f\in \bT: |f(\gamma)|<e^{-R}\}\subset \bT,\]
for any $R>0$. The argument of Proposition \ref{prop} shows that the associated time 1 Hamiltonian flow $\bS(\ell)$ is well-defined on $U(R)$, and indeed we can directly compute
\[\bS(\ell)^*(x_\beta)=\exp \Big\{-\sum_{n\geq 1} \frac{x_{\gamma}^n}{n^2}, -\Big\} (x_\beta)=x_\beta\cdot  \exp\Big(  -\sum_{n\geq 1} \frac{x_{\gamma}^n}{n^2}\cdot \<n\gamma,\beta\>\Big)\]\[
= x_\beta\cdot \exp\Big( \<\gamma,\beta\>  \log(1-x_\gamma)\Big)=x_\beta\cdot (1-x_\gamma)^{\<\gamma,\beta\>}.\]
Thus the map $\bS(\ell)$  extends holomorphically to the Zariski open subset of $\bT$ which is the complement of the divisor $x_\gamma=1$. It therefore defines a birational automorphism of $\bT$.

\begin{prop}
\label{barney}
Suppose that $(\Gamma,Z,\Omega)$ is a  generic, integral and ray-finite BPS structure. Then for any ray $\ell\subset \bC^*$ the   BPS automorphism $\bS(\ell)$ extends to a birational automorphism of $\bT$, whose action on twisted characters is given by 
\begin{equation}\bS(\ell)^*(x_\beta)=x_\beta\cdot \prod_{Z(\gamma)\in \ell}(1-x_\gamma)^{\,\Omega(\gamma)\cdot\<\gamma,\beta\>}.\end{equation}
\end{prop}

\begin{proof}
The argument of Proposition \ref{prop} shows that the automorphism $\bS(\ell)$ is well-defined on a suitable open subset of $\bT$. Under the generic assumption  
 the Hamiltonian flows of the characters appearing in the function $\DT(\ell)$ commute, so we can compute as before
\[\bS(\ell)^*(x_\beta)=\exp \Big\{-\sum_{Z(\gamma)\in \ell} \sum_{n\geq 1} \Omega(\gamma)\cdot \frac{x_{\gamma}^n}{n^2}, -\Big\} (x_\beta)=x_\beta\cdot  \exp\Big( - \sum_{n\geq 1}\sum_{Z(\gamma)\in \ell}  \Omega(\gamma)\cdot \frac{x_{\gamma}^n}{n^2}\cdot \<n\gamma,\beta\>\Big)\]\[
= x_\beta\cdot \exp\Big(\sum_{Z(\gamma)\in \ell}  \<\gamma,\beta\>  \Omega(\gamma) \log(1-x_\gamma)\Big)=x_\beta\cdot \prod_{Z(\gamma)\in \ell}(1-x_\gamma)^{\,\Omega(\gamma)\cdot\<\gamma,\beta\>}.\]
When the invariants $\Omega(\gamma)$ are integers  this is clearly a birational automorphism of $\bT$. \end{proof}

\end{appendix}
