---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-037-83-two-examples-uniform-permutations-and-uniform
section_title: "Two examples: uniform permutations and uniform set-partitions"
section_number: 8.3
pages: 67-68
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.947
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:twoexamples}
The first example that fills in this framework is the number of disjoint cycles $X_n$ of a uniform random permutation in $\mathfrak{S}(n)$. As mod-convergence of $X_n$ has already been discussed in this article (Example \ref{ex:cycle}), we will skip details. Using Feller's coupling, it is easily seen that
\[P_n(t)= \prod_{i=1}^{n} \frac{t+i-1}{1+i-1}.\]
Moreover, a straight-forward computation yields $\mu_n=H_n+O(1)$, $\sigma^2_n=H_n+O(1)$ and $L^3_n=H_n+O(1)$, where $H_n$ is the $n$-th harmonic number as in Example \ref{ex:cycle}. Theorem \ref{thm:modgaussianfromzeros} implies that $(X_n-H_n)/(H_n)^{1/3}$ converges in the mod-Gaussian sense, as established at the end of Example \ref{ex:cycle}. Note however that Theorem \ref{thm:modgaussianfromzeros} does not give the stronger mod-Poisson convergence of $(X_n)_{n \in \N}$ without renormalization.
\bigskip

The second and more interesting example is the number of blocks in a random uniform set-partition of $[n]$.
By definition, a \emph{set-partition} of $[n]$ is a set of disjoint non-empty subsets of $[n]$, whose union is $[n]$.
These subsets are called \emph{blocks} or \emph{parts} of the set-partition. For instance, $\{\{2,4\},\{1\},\{3\}\}$ is a set-partition of $[4]$ with $3$ blocks. We denote $\qym(n)$ the set of all set-partitions of $[n]$. For each integer $n \ge 0$, we then consider a random uniform set-partition in $\qym(n)$, and denote $X_n$ its number of blocks.\bigskip

It was proved by Harper \cite[Lemma 1]{HarperCLTBlocks} that the probability generating function of $X_n$ has only real non-negative roots. Moreover, the asymptotic behaviour of $\mu_n=\esper[X_n]$ and $\sigma_n^2=\Var(X_n)$ are known  --- see {\it e.g.} \cite[Theorem 2.1]{DiaconisEtAlCLTSetPartitions} ---
\[ \mu_n = \frac{n}{\log n}\, (1+o(1)), \quad \sigma_n^2=\frac{n}{(\log n)^2}\,(1+o(1)).\]
We will prove in next subsection that
\[ L_n^3= \frac{2n}{(\log n)^3}\,(1+o(1)). \]
Since $M_n=1$ and
$$\sqrt{\sigma_n} = O\!\left(\frac{n^{1/4}}{(\log n)^{1/2}}\right) \ll L_n = O\!\left(\frac{n^{1/3}}{\log n}\right) \ll \sigma_n =  O\!\left(\frac{n^{1/2}}{\log n}\right),$$ 
we can apply Theorem \ref{thm:modgaussianfromzeros}: the variables $(X_n-\mu_n)/L_n$ converge in the mod-Gaussian sense with parameter $t_n=\sigma_n^2/L_n^2=(\frac{n}{4})^{1/3}\,(1+o(1))$ and limiting function $\psi(z)=\exp(z^3/6)$.
As a corollary, applying Theorem \ref{thm:mainnonlattice} and Proposition \ref{prop:normalityzone} yields the following precise deviation result.
\begin{proposition}
Let $X_n$ be the number of blocks in a uniform set-partition of $[n]$. Define $\mu_n$, $\sigma_n$, $L_n$ and $t_n$ as above. Then the random variable $\frac{X_n - \mu_n}{\sigma_n}$ converges towards a Gaussian law, with a normality zone of size $o(n^{1/6})$. Moreover, at the edge of this normality zone,
the deviation probabilities are given by: for any fixed $x>0$, 
\begin{align*}
\proba\!\left[\frac{X_n-\mu_n}{L_n} \ge t_n x\right] &= \frac{\exp(-t_n \frac{x^2}{2})}{x\sqrt{2\pi t_n}} \,\exp\left(\frac{x^3}{6}\right)\, (1+o(1)); \\
\proba\!\left[\frac{X_n-\mu_n}{L_n} \le -t_n x\right] &= \frac{\exp(-t_n \frac{x^2}{2})}{x\sqrt{2\pi t_n}} \,\exp\left(-\frac{x^3}{6}\right)\, (1+o(1)). 
\end{align*}
\end{proposition}
\bigskip
