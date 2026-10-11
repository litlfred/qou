---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-016-53-link-with-the-cramér-petrov-expansion
section_title: "Link with the Cramér-Petrov expansion"
section_number: 5.3
pages: 43-45
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.947
---
Proposition \ref{prop:largedeviationscumulants} hints at a possible expansion of the fluctuations up to any order $T=o((\alphan)^{1-\eps})$, and indeed, it is a particular case of the results given by Rudzkis, Saulis and Statulevi\v{c}ius in \cite{RSS78,SS91}, see in particular \cite[Lemma 2.3]{SS91}. Suppose that
$$|\kappa^{(r)}(S_{n})|\leq (Cr)^{r}\,\alphan\,(\betan)^{r}\quad;\quad \kappa^{(r)}(S_{n})=K(r)\,\alphan\,(\betan)^{r}\,(1+O((\alphan)^{-1}))$$
the second estimate holding for any $r \leq v$; we denote $\sigma^{2}=K(2)$. In this setting, one can push the expansion up to order $o((\alphan)^{1-1/v})$. Indeed, define recursively for a sequence of cumulants $(\kappa^{(r)})_{r \geq 2}$ the coefficients of the Cram\'er-Petrov series $\lambda^{(r)}=-b_{r-1}/r$, with
$$\sum_{r=1}^{j} \frac{\kappa^{(r+1)}}{r!}\left(\sum_{\substack{j_{1}+\cdots+j_{r}=j\\ j_{i} \geq 1}} b_{j_{1}}b_{j_{2}}\cdots b_{j_{r}}\right)=\mathbbm{1}_{j=1}.$$
For instance, $\lambda^{(2)}=-\frac{1}{2}$, $\lambda^{(3)}=\frac{\kappa^{(3)}}{6}$, $\lambda^{(4)}=\frac{\kappa^{(4)}-3(\kappa^{(3)})^{2}}{24}$, \emph{etc.} The appearance of these coefficients can be guessed by trying to push the previous technique to higher order; in particular, the simple form of $\lambda^{(3)}$ is related to the fact that the only term in $z^{3}$ in the expansion \eqref{eq:push} is $\frac{\kappa^{(3)}}{6}$. If for the cumulants $\kappa^{(r)}$'s one has estimates of order $(\alphan)^{1-r/2}(1+O((\alphan)^{-1}))$, then one has the same estimates for the $\lambda^{(r)}$'s, so there exists coefficients $L(r)$ such that
$$\lambda^{(r)}\left(\frac{S_{n}}{\sigma\,\betan\,(\alphan)^{\frac{1}{2}}}\right)=L(r)\,(\alphan)^{1-r/2}\,(1+O((\alphan)^{-1})).$$ 
Take then $T=x_n\,(\alphan)^{\frac{v-1}{v}}$ with $x_n=O(1)$; Lemma 2.3 of \cite{SS91} ensures that 
\begin{align*}\proba\left[\frac{S_{n}}{\sigma\betan}\geq T\right]&=\frac{\E^{-\frac{T^{2}}{2\alphan}}}{\sqrt{2\pi\frac{T^{2}}{\alphan}}}\,\exp\left(\sum_{r=3}^{v} \lambda^{(r)}\,\left(\frac{T}{\sigma (\alphan)^{1/2}}\right)^{r}\right) \big(1+o(1)\big)\\
&=\frac{\E^{-\frac{T^{2}}{2\alphan}}}{\sqrt{2\pi\frac{T^{2}}{\alphan}}}\,\exp\left(\sum_{r=3}^{v} \,\frac{L(r)\,T^{r}}{\sigma^{r}\,(\alphan)^{r-1}}\right) \big(1+o(1)\big).
\end{align*}
Thus, the method of cumulants of Rudzkis, Saulis and Statulevi\v{c}ius can be thought of as a particular case (and refinement in this setting) of the notion of mod-$\phi$ convergence. However, their works do not yield a bound
$$|\kappa^{(r)}(S_{n})|\leq (Cr)^{r}\,\alphan\,(\betan)^{r}$$
but for simple cases, such as sums of i.i.d.~random variables. 
In Section \ref{sec:depgraph}, we show that dependency graphs
are an adequate framework to provide such bounds.\bigskip
\bigskip





















\section{A precise version of the Ellis-G\"artner theorem}\label{sec:precisellis}

In the classical theory of large deviations, asymptotic results are formulated not only for the probabilities of tails $\proba[X_{n}\geq t_{n}x]$, but more generally for probabilities
$$\proba[X_{n} \in t_{n}B]\quad \text{with $B$ arbitrary Borelian subset of $\R$}.$$
In particular, under some technical assumptions on the generating series (that look like, but are somehow weaker than mod-convergence),  Ellis-G\"artner theorem provides some asymptotic upper and lower bounds for $\log(\proba[X_{n} \in t_{n}B])$, these bounds relying on a limiting condition on $(t_n)^{-1} \log\varphi_n(\cdot)$. When the topology of $B$ is {\em nice} enough, these bounds coincide  (see \emph{e.g.} \cite[Theorem 2.3.6]{DZ98}). This generalizes Cram\'er's large deviations for sums of i.i.d.~random variables. \bigskip

Our Theorems~\ref{thm:mainlattice} and \ref{thm:mainnonlattice} give estimates for the probabilities $\proba[X_{n} \geq t_{n}x]$ themselves, instead of their logarithm). Therefore, it is  natural to establish in the framework of mod-convergence a precise version of Ellis-G\"artner theorem. In this section, we shall give some asymptotic upper and lower bounds for the probabilities $\proba[X_{n} \in t_{n}B]$ itself instead of their logarithms. Once again, the upper and lower bounds coincide for {\em nice} borelian sets $B$.\medskip

\begin{remark}
In \cite{Multidim}, we shall prove similar estimates of $\proba[\mathbf{X}_n \in t_n B]$ in the setting of sequences of random \emph{vectors} that converge in the multi-dimensional mod-Gaussian sense.
 \end{remark} \bigskip
