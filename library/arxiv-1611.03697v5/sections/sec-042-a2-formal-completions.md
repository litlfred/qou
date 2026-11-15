---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-042-a2-formal-completions
section_title: "A.2. Formal completions"
section_number: null
pages: 37-38
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let $(\Gamma,Z,\Omega)$ be a BPS structure. To an acute sector   $\Delta\subset \bC^*$  we associate a Poisson subalgebra
\begin{equation}
\label{frioff}\bC_\Delta[\bT]=\bigoplus_{Z(\gamma) \in \Delta\sqcup\{0\}}  \bC\cdot x_\gamma\subset \bC[\bT].\end{equation}
We will now introduce a natural completion of this algebra.


Define the height of an element $a=\sum_\gamma  a_\gamma\cdot x_\gamma$   to be
\[\height(a)=\inf\{|Z(\gamma)|: \gamma \in \Gamma\text{ such that }a_\gamma\neq 0\}.\]
Note that since $\Delta$ is acute, we have
\[|Z(\gamma_1+\gamma_2)|\geq \min (|Z(\gamma_1)|,|Z(\gamma_2)|),\]
whenever $\gamma_i\in \Gamma$ satisfy $Z(\gamma_i)\in \Delta$. It follows that \[\height(a\cdot b)\geq \max(\height(a),\height(b)),\quad \height(\{a,b\})\geq \max(\height(a),\height(b)).\]
In particular, for any $N>0$, the subspace \[\bC_\Delta[\bT]_{\geq N}\subset \bC_\Delta[\bT]\] consisting of elements of height $\geq N$ is a Poisson ideal. We can therefore consider the inverse limit of the quotient Poisson algebras as $N\to \infty$:
\[\bC_{\Delta}[[\bT]]=\varprojlim_{N} \,\bC_{\Delta}[\bT]_{< N}, \qquad  \bC_{\Delta}[\bT]_{< N}= \bC_{\Delta}[\bT]/\bC_{\Delta}[\bT]_{\geq N}.\] 
The resulting completion $\bC_{\Delta}[[\bT]]$
can be identified with  the set of formal sums \begin{equation}\label{lon} \big.\sum_{Z(\gamma)\in \Delta} a_\gamma \cdot x_\gamma,\end{equation} such that for any $N>0$ there are only finitely many terms with $|Z(\gamma)|<N$. We define the height of such an element to be  the minimum value of $|Z(\gamma)|$ occurring.
