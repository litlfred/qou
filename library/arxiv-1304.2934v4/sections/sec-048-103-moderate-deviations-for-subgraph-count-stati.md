---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-048-103-moderate-deviations-for-subgraph-count-stati
section_title: "Moderate deviations for subgraph count statistics"
section_number: 10.3
pages: 85-88
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.98
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\subsubsection{End of the proof of Theorem \ref{thm:moddevgraphs}}
We would like to apply Proposition \ref{prop:largedeviationscumulants} to the sequence $S_n=\SubGraph_\gamma-\esper[\SubGraph_\gamma]$ with $\alphan=n^2$ and $\betan=n^{k-2}$. Let us check that $S_n$ indeed fulfills the hypothesis.\vspace{2mm}
\begin{enumerate}
\item The uniform bound $|\kappa^{(r)}(S_n)| \leq (C r)^r \alphan (\betan)^r$, where $C$ does not depend on $n$,  corresponds to Proposition~\ref{prop:boundcumulantsubgraph}; we may even choose $C=2k^4$.\vspace{2mm}
\item We also have to check the speed of convergence:
\begin{equation}\label{eq:speedconvK2K3}
    \kappa^{(2)}(S_{n})= \sigma^{2}\,\alphan\,(\betan)^2\,(1+O(\alphan^{-1/2}))
\quad;\quad
\kappa^{(3)}(S_{n}) = L \,\alphan\, (\betan)^3\,(1+O(\alphan^{-1/4})).
\end{equation}
But these estimates follow directly from the bound above for $r=2,3$ and the fact that $\kappa^{(r)}(S_{n})$ is always a polynomial in $n$ --- see Corollary \ref{cor:jointcumulantpoly}.\vspace{2mm}
\end{enumerate}
Finally, the mod-Gaussian convergence follows from the observations in Section \ref{sec:cumulantechnic}.
The normality zone result follows from Proposition \ref{prop:normalityzone} and we can apply Proposition \ref{prop:largedeviationscumulants} to get the moderate deviation statement.
 This ends the proof of Theorem \ref{thm:moddevgraphs}. \qed
\medskip

\begin{remark}
    Using Theorem \ref{thm:boundjointcumulant}, we could obtain a bound for joint cumulants of subgraph count statistics. Hence, it would be possible to derive mod-Gaussian convergence and moderate deviation results for {\em linear combinations} of subgraph count statistics. However, since we do not have a specific motivation for that and since the statement for a single subgraph count statistics is already quite technical, we have chosen not to present such a result.
\end{remark}\bigskip



\subsubsection{Computing $\sigma^2$ and $L$}
\label{subsec:sigma_L}
The proof above does not give an explicit value for $\sigma^2$ and $L$. Yet, these values can be obtained by analyzing the graphs $G$ that contribute to the highest degree term of $\kappa^{(2)}$ and $\kappa^{(3)}$.

\begin{lemma} 
Let $\gamma$ be a graph with $k$ vertices and $h$ edges. Then the positive number $\sigma$ appearing in Theorem \ref{thm:moddevgraphs} is given by $$\sigma^2 = 2 h^2 p^{2h-1} (1-p). $$
\end{lemma}

\begin{proof}
By definition, $\sigma^2$ is the coefficient of $n^{2k-2}$ in $\kappa^{(2)}(\SubGraph_\gamma)$. As seen in Equation \eqref{eq:expansioncumulantgraphs}, the quantity $\kappa^{(2)}(\SubGraph_\gamma)$ can be written as 
$$\sum_{G} \kappa(G) N_G,$$
where the sum runs over some graphs $G$ with vertex set $V \sqcup V$. However, we have seen that $\kappa(G)=0$ unless the $2$-contraction $H^2$ of $G$ is connected --- see Inequality \eqref{eq:boundkappa} --- and on the other hand, $N_G$ is a polynomial in $n$, whose degree is the number $c_G$ of connected component of $G$.
\bigskip

\noindent As we are interested in the coefficient of $n^{2k-2}$, we should consider only graphs $G$ with at least $2k-2$ connected components and a connected $2$-contraction. These graphs are represented on Figure~\ref{fig:computationsigma}.
\begin{figure}[ht]
    $$\begin{array}{c} 
        \begin{tikzpicture}
    \tikzstyle{vertex}=[circle,fill=black,inner sep=0pt,minimum size=2mm]
    \begin{scope}[xscale=.5]
        \node (v1) at (36:1) [vertex] {};
        \node (v2) at (108:1) [vertex] {};
        \node (v3) at (180:1) [vertex] {};
        \node (v4) at (-108:1) [vertex] {};
        \node (v5) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \begin{scope}[xshift= 3.5cm,xscale=.5]
        \node (v1b) at (36:1) [vertex] {};
        \node (v2b) at (108:1) [vertex] {};
        \node (v3b) at (180:1) [vertex] {};
        \node (v4b) at (-108:1) [vertex] {};
        \node (v5b) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \draw [line width=1.2pt,DarkOrchid] (v1) to (v2b);
    \draw [line width=1.2pt,DarkOrchid] (v5) to (v3b);
\end{tikzpicture}\end{array}$$
\caption{Graphs involved in the computation of the main term in $\kappa^{(2)}(\SubGraph_{\gamma})$.}
\label{fig:computationsigma}
\end{figure}

\noindent Namely, we have to choose a pair of vertices on each side and connect each of these vertices to one vertex of the other pair (there are $2$ ways to make this connection, if both pairs are fixed). A quick computation shows that, for such a graph $G$,
\[\kappa(G)=\begin{cases}
    p^{2h-1} (1-p) &\text{ if both pairs correspond to an edge of }\gamma;\\
    0 & \text{ else.}
\end{cases}\]
Finally there are $2 h^2$ graphs with a non-zero contribution to the coefficient of $n^{2k-2}$ in $\kappa^{(2)}(\SubGraph_\gamma)$.
For each of these graphs, $N_G=n(n-1)\cdots(n-2k+3)=n^{2k-2}(1+o(1))$. Therefore, the coefficient of $n^{2k-2}$ in $\kappa^{(2)}(\SubGraph_\gamma)$ is $2 h^2 p^{2h-1} (1-p)$, as claimed.
\end{proof}\bigskip

The number $L$ can be computed by the same method.
\begin{lemma}
Let $\gamma$ be a graph with $k$ vertices and $h$ edges. Then the number $L$ appearing in Theorem \ref{thm:moddevgraphs} is given by
$$L =12 h^3 (h-1) p^{3h-2} (1-p)^2 + 4 h^3 p^{3h-2} (1-p) (1-2p).$$
\end{lemma}

\begin{proof}
Here, we have to consider graphs $G$ on vertex set $V \sqcup V \sqcup V$ with at least $3k-4$ connected components and with a connected $2$-contraction. These graphs are of two kinds, see Figure~\ref{fig:computationL}.
 \begin{figure}[ht]
 $$\begin{array}{c|c}
     \begin{tikzpicture}[scale=.8]
    \tikzstyle{vertex}=[circle,fill=black,inner sep=0pt,minimum size=2mm]
    \begin{scope}[xscale=.5]
        \node (v1) at (36:1) [vertex] {};
        \node (v2) at (108:1) [vertex] {};
        \node (v3) at (180:1) [vertex] {};
        \node (v4) at (-108:1) [vertex] {};
        \node (v5) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \begin{scope}[xshift= 3cm,xscale=.5]
        \node (v1b) at (36:1) [vertex] {};
        \node (v2b) at (108:1) [vertex] {};
        \node (v3b) at (180:1) [vertex] {};
        \node (v4b) at (-108:1) [vertex] {};
        \node (v5b) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \begin{scope}[xshift= 6cm,xscale=.5]
        \node (v1t) at (36:1) [vertex] {};
        \node (v2t) at (108:1) [vertex] {};
        \node (v3t) at (180:1) [vertex] {};
        \node (v4t) at (-108:1) [vertex] {};
        \node (v5t) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \draw [line width=1pt,DarkOrchid] (v1) to (v2b);
    \draw [line width=1pt,DarkOrchid] (v5) to (v3b);
    \draw [line width=1pt,DarkOrchid] (v1b) to (v3t);
    \draw [line width=1pt,DarkOrchid] (v4b) to (v5t);
\end{tikzpicture}
\qquad & \qquad
     \begin{tikzpicture}[scale=.8]
    \tikzstyle{vertex}=[circle,fill=black,inner sep=0pt,minimum size=2mm]
    \begin{scope}[xscale=.5]
        \node (v1) at (36:1) [vertex] {};
        \node (v2) at (108:1) [vertex] {};
        \node (v3) at (180:1) [vertex] {};
        \node (v4) at (-108:1) [vertex] {};
        \node (v5) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \begin{scope}[xshift= 3cm,xscale=.5]
        \node (v1b) at (36:1) [vertex] {};
        \node (v2b) at (108:1) [vertex] {};
        \node (v3b) at (180:1) [vertex] {};
        \node (v4b) at (-108:1) [vertex] {};
        \node (v5b) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \begin{scope}[xshift= 6cm,xscale=.5]
        \node (v1t) at (36:1) [vertex] {};
        \node (v2t) at (108:1) [vertex] {};
        \node (v3t) at (180:1) [vertex] {};
        \node (v4t) at (-108:1) [vertex] {};
        \node (v5t) at (-36:1) [vertex] {};
        \draw [line width=0.8pt] (0,0) circle (1.7);
    \end{scope}
    \draw [line width=1pt,DarkOrchid] (v1) to (v2b);
    \draw [line width=1pt,DarkOrchid] (v5) to (v3b);
    \draw [line width=1pt,DarkOrchid] (v2b) to (v3t);
    \draw [line width=1pt,DarkOrchid] (v3b) to (v4t);
    \draw [line width=1pt,DarkOrchid] (v1) to (v3t);
    \draw [line width=1pt,DarkOrchid] (v5) to (v4t);
\end{tikzpicture}
 \end{array}$$
 \caption{Graphs involved in the computation of the main term in $\kappa^{(3)}(\SubGraph_{\gamma})$.\label{fig:computationL}}
\end{figure}\bigskip

In the first case (left-hand side picture),  an edge on the left can possibly have an extremity in common with an edge on the right. In this case, one has to add an edge to complete the triangle (indeed, all graphs $G$ are disjoint unions of cliques).  But this cannot happen for both edges on the left simultaneously, otherwise the graph belong to the second family.\bigskip
 
The following is now easy to check. There are $12 h^3 (h-1)$ graphs of the first kind with a non-zero cumulant $\kappa(G)$ --- 3 choices for which copy of $V$ plays the central role, $h^3 (h-1)$ for pairs of vertices and $4$ ways to link the chosen vertices --- and, for these graphs, the corresponding cumulant is always $\kappa(G) = p^{3h-2} (1-p)^2$. Similarly, there are $4 h^3$ graphs of the second kind with a non-zero cumulant $\kappa(G)$. For these graphs, $\kappa(G)=p^{3h-2}(1-p)(1-2p)$.
In both cases, $N_G=n^{3k-4}(1+o(1))$. This completes the proof.
\end{proof}
\bigskip

\begin{example}
Denote $T_{n}$ the number of triangles in a random Erd\"os-R\'enyi graph $\Gamma(n,p)$ (each triangle being counted $6$ times). According to the previous Lemmas, the parameters $\sigma^{2}$ and $L$ are respectively
$$\sigma^{2}=18\,p^{5}\,(1-p)\quad \text{and}\quad L=108\,p^{7}\,(1-p)(7 -8 p).$$
Moreover, $\esper[T_{n}]=n\fall{3}\,p^{3}=n^{3}\,p^{3}-3\,n^{2}\,p^{3}+O(n)$. So,
$$
\proba \!\left[ T_{n} \geq n^{3}p^{3}+n^{2}(v-3p^{3}) \right] \simeq \sqrt{\frac{ 9p^{5}(1-p)}{\pi\, v^{2}}}\, \exp\!\left(-\frac{v^{2}}{36\,p^{5}(1-p) }+\frac{(7-8p)\,v^{3}}{324 \,n \,p^8(1-p)^2 } \right) 
$$
for $1 \ll v\ll n^{1/2}$.
\end{example}
\medskip



\subsubsection{Case of a non-constant sequence $p_n$}
\label{subsec:nonconstantproba}
Proposition \ref{prop:boundcumulantsubgraph} still holds when $p_n$ is a non-constant sequence (the particularly interesting case is $p_n \to 0$). Applying Theorem \ref{thm:dependencygraphs_sumY} instead of Theorem \ref{thm:dependencygraphsrefined}, one gets a slightly sharper bound 
$$\left| \kappa^{(r)} (\SubGraph_\gamma) \right| \le C^{r} \,r^{r-2} \,n^{r(k-2)+2}\, (p_n)^h.$$
But, unlike in the case $p_n=p$ constant, this bound is not always optimal for a fixed $r$ (even up to a multiplicative constant) . Indeed, \cite[Lemma 6.17]{JLR00} gives stronger bounds than ours (see also Example 6.19 in \cite{JLR00}). Finding a uniform bound for cumulants, whose dependence in $r$ is of order $(Cr)^r$  (so that we have mod-Gaussian convergence), and which is optimal for fixed $r$ is an open problem.\bigskip

Yet, we can still give a lower bound on the normality zone. Let $\alphan$ and $\betan$ be defined as follows:
\begin{align*}
    \alphan &= n^2 \,(p_n)^{4h-3} \,(1-p_n)^3;\\
    \betan &=n^{k-2}\, (p_n)^{1-h}\, (1-p_{n})^{-1}.
\end{align*}
With these choices, one has
$$\left| \kappa^{(r)} (\SubGraph_\gamma) \right| \le (Cr)^r\, \alphan (\betan)^r.$$
Notice that $\kappa^{(2)}(\SubGraph_\gamma)$ and $\kappa^{(3)}(\SubGraph_\gamma)$ are polynomials in $n$ and $p_n$, of degree $2h$ and $3h$ in $p_n$. Thanks to this observation, if $p_n \to 0$, then
\begin{align*}
\kappa^{(2)}(\SubGraph_\gamma) &= 2h^2\,n^{2k-2}\,(p_n)^{2h-1}(1-p_n) + O(n^{2k-3}) \\
&= 2h^2\,\alphan\,(\betan)^2 \left(1+O\!\left(\frac{1}{n\,(p_n)^{2h-1}}\right)\right) ;\\
\kappa^{(3)}(\SubGraph_\gamma) &= h^3\,n^{3k-4}\,(p_n)^{3h-2}(1-p_n)\,(12 (h-1) (1-p_n) + 4 (1-2p_n)) + O(n^{3k-5})\\
&=\alphan\,(\betan)^3\,\left(O((p_n)^{2h-2})+O\!\left(\frac{1}{n\,(p_n)^{h}}\right)\right).
\end{align*}
From the discussion of Section \ref{subsec:modgaussfromcumulants}, we conclude that we have mod-Gaussian convergence 
if $(\alphan)^{1/3}=o(n\,(p_n)^{2h-1})$ and $n\,(p_n)^h \to +\infty$. The first condition is equivalent to $n\,(p_n)^{2h} \to +\infty$, so, if
$$ n^{-\frac{1}{2h}} \ll p_n \ll 1 ,$$
then Conditions \eqref{eq:cv_sndthrd_cumulants} are met, and one has a mod-Gaussian convergence of 
$$\frac{\SubGraph_\gamma-\esper[\SubGraph_\gamma]}{n^{k-\frac{4}{3}}\,(p_n)^{\frac{h}{3}}}$$
with parameters $t_n = 2h^2\,n^{\frac{2}{3}}\,(p_n)^{\frac{4h}{3}-1}\,(1-p_n)$ and limit $\psi(z)=1$. Therefore, in this setting, 
$$\frac{\SubGraph_\gamma-\esper[\SubGraph_\gamma]}{h\,n^{k-1}\,\sqrt{2(p_n)^{2h-1}(1-p_n)}}$$
has normality zone at least $O(n^{\frac{1}{3}}\,(p_n)^{\frac{2h}{3}-\frac{1}{2}})$.
Note that we only have a lower bound on the normality zone,
since the limit in the mod-Gaussian convergence is trivial.

\begin{remark}
Unfortunately the convergence speed hypotheses \eqref{eq:speedconvK2K3} are not satisfied, so one cannot apply Proposition \ref{prop:largedeviationscumulants}.
\end{remark}
\bigskip
\bigskip
