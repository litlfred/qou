---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-026-62-a-precise-upper-bound
section_title: "A precise upper bound"
section_number: 6.2
pages: 46-47
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.978
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\begin{theorem}\label{thm:superellis}
Let $B$ be a Borelian subset of $\R$.\vspace{2mm}
\begin{enumerate}
\item\label{item:admissible} If $B$ is admissible, then
$$\limsup_{n \to \infty} \big(\sqrt{2\pi t_{n}}\,\exp(t_{n}F(B))\,\proba[X_{n} \in t_{n} B] \big) \leq \begin{cases}
&\sum_{a \in B_{\min}} \frac{\psi(h(a))}{(1-\E^{-|h(a)|})\,\sqrt{\eta''(h(a))}}\\
&\sum_{a \in B_{\min}} \frac{\psi(h(a))}{|h(a)|\,\sqrt{\eta''(h(a))}}
\end{cases}$$
the distinction of cases corresponding to $\phi$ lattice or non-lattice distributed. The sum on the right-hand side consists in one or two terms --- it is considered infinite if $a=\eta'(0) \in B_{\min}$. \vspace{2mm}
\item\label{item:nonadmissible} If $B$ is not admissible, then for any positive real number $M$,
$$\lim_{n \to \infty} \big( \exp(t_{n}M)\,\proba[X_{n} \in t_{n} B] \big)=0.$$
\end{enumerate}
\end{theorem}\medskip

\begin{proof}
For the second part, one knows that $\varphi_{n}(x)\,\exp(-t_{n}\eta(x))$ converges to $\psi(x)$ which does not vanish on the real line, so by taking the logarithms, 
$$\lim_{n \to \infty} \frac{\log \varphi_{n}(x)}{t_{n}}=\eta(x).$$
Then, Ellis-G\"artner theorem holds since $F$ is supposed essentially smooth. So, $$\limsup_{n \to \infty} \,\frac{\log \proba[X_{n} \in t_{n}B]}{t_{n}} \leq -F(B),$$ and if $B$ is not admissible, then the right-hand side is $-\infty$ and \eqref{item:nonadmissible} follows immediately.\bigskip

For the first part, suppose for instance $\phi$ non-lattice distributed. Take $C$ a closed admissible subset, and assume $\eta'(0) \notin C$ --- otherwise the upper bound in \eqref{item:admissible} is $+\infty$ and the inequality is trivially satisfied. Since $C^{\mathrm{c}}$ is an open set, there is an open interval $(a,b) \subset C^{\mathrm{c}}$ containing $\eta'(0)$, and which we can suppose maximal. Then $a$ and $b$ are in $C$ as soon as they are finite, and $C \subset (-\infty,a] \sqcup [b,+\infty)$. Moreover, by strict convexity of $F$, the minimal value $F(C)$ is necessarily attained at $a$ or $b$. Suppose for instance $F(a)=F(b)=F(C)$ --- the other situations are entirely similar. Then,
\begin{align*}\proba[X_{n} \in t_{n}C] &\leq \proba[X_{n} \leq t_{n}a]+\proba[X_{n}\geq t_{n}b] \\
&\lesssim \exp(-t_{n}F(C)) \left(\frac{\psi(h(a))}{-h(a)\sqrt{2\pi t_{n}\eta''(h(a))}}+\frac{\psi(h(b))}{h(b)\sqrt{2\pi t_{n}\eta''(h(b))}}\right) 
\end{align*}
by using Theorem \ref{thm:mainnonlattice} for $\proba[X_{n} \geq t_{n}b]$, and also for $\proba[X_{n}\leq t_{n}a]=\proba[-X_{n} \geq -t_{n}a]$ --- the random variables $-X_{n}$ satisfy the same hypotheses as the $X_{n}$'s with $\eta(x)$ replaced by $\eta(-x)$, $\psi(x)$ replaced by $\psi(-x)$, \emph{etc}. This proves the upper bound when $B$ is closed, and since $F(B)=F(\overline{B})$ by lower semi-continuity of $F$ and $B_{\min}=(\overline{B})_{\min}$, the result extends immediately to arbitrary admissible Borelian subsets.
\end{proof}\bigskip
