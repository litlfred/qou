---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-045-10-subgraph-count-statistics-in-erdös-rényi-rand
section_title: "Subgraph count statistics in Erdös-Rényi random graphs"
section_number: 10
pages: 80-81
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{sec:erdosrenyi}
In this section, we consider Erd\"os-R\'enyi model $\Gamma(n,p_n)$ of random graphs. A random graph $\Gamma$ with this distribution is described as follows. Its vertex set is $[n]$ and for each pair $\{i,j\} \subset [n]$  with $i \neq j$, there is an edge between $i$ and $j$ with probability $p_n$. Moreover, all these events are independent. We are then interested in the following random variables, called {\em subgraph count statistics}. If $\gamma$ is a fixed graph of size $k$, then $\SubGraph_\gamma$ is the number of copies of $\gamma$ {\em contained} in the graph $\Gamma(n,p_n)$ (a more formal definition is given in the next paragraph). This is a classical parameter in random graph theory; see, {\em e.g.}, the book of S. Janson, T. {\L}uczak and A. Ruci\'nski \cite{JLR00}. \bigskip

The first result on this parameter was obtained by P. Erd\"os and A. R\'enyi, \emph{cf.} \cite{ER60}. They proved that, if $\gamma$ belongs to some particular family of graphs (called {\em balanced}),
one has a threshold: namely,
$$\lim_{n \to \infty} \proba[\SubGraph_\gamma >0]=\begin{cases}
    0 & \text{if }p_n=o\left(n^{-1/m(\gamma)}\right); \\
1 & \text{if }n^{-1/m(\gamma)}=o(p_n), \end{cases}
$$
where $m(\gamma)=|E(\gamma)|/|V(\gamma)|$.
This result was then generalized to all graphs by B. Bollob\'as~\cite{Bol01}, but the parameter $m(\gamma)$ is in general more complicated than the quotient above. Consider the case $n^{-1/m(\gamma)}=o(p_n)$, when the graph $\Gamma(n,p_n)$ contains with high probability a copy of $\gamma$. It was then proved by A. Ruci\'nski (see \cite{Ruc88}) that, under the additional assumption $n^2 (1-p_n) \to \infty$, the fluctuations of $\SubGraph_\gamma$ are Gaussian. This result can be obtained using dependency graphs; see {\em e.g.}  \cite[pages 147-152]{JLR00}.\bigskip

Here, we consider the case where $p_n=p$ is a constant sequence ($0<p<1$). The possibility of relaxing this hypothesis is discussed in Subsection \ref{subsec:nonconstantproba}. Denote $\alphan=n^2$ and $\betan=n^{k-2}$, where $k$ is the number of vertices of $\gamma$. It is easy to check that 
$$\esper[\SubGraph_\gamma]=c \,\alphan \,\betan \quad;\quad \Var(\SubGraph_\gamma)=\sigma^2 \,\alphan \,(\betan)^2$$ 
for some positive constants $c$ and $\sigma$ --- see, {\em e.g.}, \cite[Lemma 3.5]{JLR00}. Hence, Ruci\'nski's central limit theorem asserts that,  if $T \sim x \sqrt{\alphan}$ for some fixed real $x$, then
$$ \lim_{n\to \infty} \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}
\betan \geq T \right] = \frac{1}{ \sqrt{2\pi}}
\int_{-\infty}^{x/\sigma} e^{-u^2/2} du.$$
Using Theorem \ref{thm:dependencygraphsrefined}, we shall extend this result to a framework where $x$ tends to infinity, but not to quickly: $(\alphan)^{1/2} \ll T \ll (\alphan)^{3/4}$.

\begin{theorem} \label{thm:moddevgraphs}
    Let $0<p<1$ and $\gamma$ be a graph with $k$ vertices. We consider $\SubGraph_\gamma$ the number
    of copies of $\gamma$ contained in Erd\"os-R\'enyi random graph $\Gamma(n,p)$. Let $\alphan$ and $\betan$ be defined as above.\vspace{2mm}
\begin{enumerate}
\item The renormalized variable 
    $(\SubGraph_\gamma - \esper[\SubGraph_\gamma])/(\alphan^{1/3} \betan)$
    converges mod-Gaussian with parameters $t_{n}=\sigma^{2}\,\alphan^{1/3}$
    and limiting function $\psi(z)=\exp\big(\frac{L}{6} z^{3}\big)$,
    where $\sigma$ and $L$ are computed in Section \ref{subsec:sigma_L}.
The convergence takes place on the whole complex plane with speed of convergence $o(\alphan^{-1/3})$.
\vspace{2mm}

\item Therefore, $(\SubGraph_\gamma - \esper[\SubGraph_\gamma])/(\alphan^{1/2} \betan)$ converges in distribution
towards a Gaussian law, with normality zone $o(\alphan^{1/6})$.
Moreover, the deviation probabilities at the edge of the normality zone and at a slightly larger scale 
are given as follows:
is $x_n$ is a positive sequence bounded away from $0$ with $x_n=o\big(\alphan^{1/12})$, then
\begin{align*}
        \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}    
        {\alphan^{1/2} \, \betan} \geq \sigma^2 \alphan^{1/6} x_n \right] &=
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)).\\
        \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}    
        {\alphan^{1/2} \, \betan} \leq - \sigma^2 \alphan^{1/6} x_n \right] &=
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{-L(x_n)^3}{6}}\,(1+o(1)).
\end{align*}

        




    \end{enumerate}
\end{theorem}
\smallskip

A similar result has been obtained by H. D\"{o}ring and P. Eichelsbacher in \cite[Theorem 2.3]{DE12}. However, \vspace{2mm}
\begin{itemize}
    \item their result is less precise as they only obtain the equivalence of the logarithms of the relevant quantities (in particular, when we look at the logarithm, the second factor of the right-hand side is negligible);\vspace{2mm}
    \item and they cover a smaller zone of deviation.\vspace{2mm}
\end{itemize}
Unfortunately, we cannot get deviation results when $x_n \sim t \alphan^{1/3}$ for some real number $t$;
this would amount to evaluate $\proba [\SubGraph_\gamma > (1+\varepsilon)\,\esper[\SubGraph_\gamma]]$. For large deviations equivalents of
$$ \log \, \proba [\SubGraph_\gamma >  (1+\varepsilon)\,\esper[\SubGraph_\gamma]], $$
there is a quite large literature, see \cite[Theorem 4.1]{CV11} and \cite{Cha12} for recent results in this field. As we consider deviations of a different scale, our result is neither implied by, nor implies these results. Note, however, that their large deviation results are equivalents of the logarithm of the probability, while our statement is an equivalent for the probability itself.
\bigskip
