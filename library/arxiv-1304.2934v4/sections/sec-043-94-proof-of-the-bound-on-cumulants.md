---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-043-94-proof-of-the-bound-on-cumulants
section_title: "Proof of the bound on cumulants"
section_number: 9.4
pages: 76-78
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.96
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
Recall that we want to find a bound for $\kappa^{(r)}(X)$. As $X$ writes $X=\sum_{\alpha \in V} Y_{\alpha}$, we may use joint cumulants and expand by multilinearity:
\begin{equation}\label{eq:expcumulant}
    \kappa^{(r)}(X) =
\sum_{\alpha_1,\dots,\alpha_r}
\kappa(Y_{\alpha_1},\dots,Y_{\alpha_r}).
\end{equation}
The sum runs over lists of $r$ elements in $V$, that is vertices of the dependency graph $G$. The proof consists in bounding each summand $\kappa(Y_{\alpha_1},\dots,Y_{\alpha_r})$, with a bound depending on the induced subgraph $G[\alpha_1,\dots,\alpha_r]$.


\subsubsection{Bringing terms together in joint cumulants.}
Recall the moment-cumulant formula \eqref{eq:moment2cumulant} which states $\kappa(Y_{\alpha_1},\dots,Y_{\alpha_r}) = \sum_\pi \mu(\pi) M_\pi$, where 
$$M_\pi = \prod_{B \in \pi} \,\esper\! \left[ \prod_{i \in B} Y_{\alpha_i} \right]. $$
We warn the reader that the notation $M_\pi$ is a little bit abusive as this quantity depends also on the list $(\alpha_1,\dots,\alpha_r)$. By hypothesis, $G$ is a dependency graph for the family $\{Y_{\alpha}\}_{\alpha \in V}$. Hence if some block $B$ of a partition $\pi$ can be split into two sub-blocks $B_1$ and $B_2$ such that the sets of vertices $\{\alpha_i\}_{i \in B_1}$ and $\{\alpha_i\}_{i \in B_2}$ are disjoint and do not share an edge, then
\begin{equation}\esper\! \left[ \prod_{i \in B} Y_{\alpha_i} \right] = 
\esper\! \left[ \prod_{i \in B_1} Y_{\alpha_i} \right] \times
\esper\! \left[ \prod_{i \in B_2} Y_{\alpha_i} \right]. \label{eq:alsoinnoncommutative}\end{equation}
Therefore, $M_\pi=M_{\phi_H(\pi)}$, where $H=G[\alpha_1,\dots,\alpha_r]$ and $\phi_H(\pi)$ is the refinement of $\pi$ obtained as follows: for each part $\pi_i$ of $\pi$, consider the induced graph $H[\pi_i]$ and replace $\pi_i$ by the collection of vertex sets of the connected components of $H[\pi_i]$. This construction is illustrated on Figure \ref{fig:phiH}.

\begin{figure}[ht]
    \hfill \begin{minipage}{.3\linewidth}
        \[H=\begin{array}{c}\begin{tikzpicture}
    \tikzstyle{vertex1}=[circle,blue!90!white,draw,inner sep=0.5pt,minimum size=1mm]
    \tikzstyle{vertex2}=[rectangle,red,draw,inner sep=1.5pt,minimum size=1mm]
    \node (v1) at (0:1) [vertex1] {\footnotesize $1$};
    \node (v2) at (60:1) [vertex1] {\footnotesize $2$};
    \node (v3) at (120:1) [vertex1] {\footnotesize $3$};
    \node (v4) at (180:1) [vertex1] {\footnotesize $4$};
    \node (v5) at (240:1) [vertex2] {\footnotesize $5$};
    \node (v6) at (300:1) [vertex2] {\footnotesize $6$};
    \draw [line width=1pt] (v1) to (v5);
    \draw [line width=1pt] (v1) to (v6);
    \draw [line width=1pt] (v2) to (v1);
    \draw [line width=1pt] (v3) to (v4);
    \draw [line width=1pt] (v3) to (v6);
    \draw [line width=1pt] (v5) to (v4);
\end{tikzpicture} \end{array}\]
    \end{minipage}\hfill \hfill
    \begin{minipage}{.6\linewidth}
For example, consider the graph $H$ here opposite and the partition $\pi=\{\pi_1,\pi_2\}$ with $\pi_1=\{1,2,3,4\}$ and $\pi_2=\{5,6\}$. Then $H[\pi_1]$ (respectively, $H[\pi_2]$) has two connected components with vertex sets $\{1,2\}$ and $\{3,4\}$ (resp. $\{5\}$ and $\{6\}$). Thus
\[\phi_H(\pi)=\{\{1,2\},\{3,4\},\{5\},\{6\}\}. \]
    \end{minipage} \hfill
    \vspace{3mm}
    \caption{Illustration of the definition of $\phi_H$.}
    \label{fig:phiH}
\end{figure}

We can thus write
$$\kappa(G)= \sum_{\pi'}\, M_{\pi'} \! \left( \sum_{\pi \in \phi_H^{-1}(\pi')} \mu(\pi) \right).$$
Fix $\pi'=(\pi'_1,\dots,\pi'_t)$ and let us have a closer look to the expression in the parentheses that we will call $\pa_{\pi'}$. To compute it, it is convenient to consider the contraction $H/\pi'$ of the graph $H$ with respect to the partition $\pi'$.
\begin{lemma} 
    Let $\pi'$ be a set partition of $[r]$. If one of the induced graph $H[\pi'_i]$ is disconnected, then $\pa_{\pi'}=0$. Otherwise, $\pa_{\pi'}=(-1)^{\ell(\pi')-1} \SF_{H/\pi'}$.
\end{lemma}
\begin{proof}
The first part is immediate, as $\phi_H^{-1}(\pi')=\emptyset$ in this case.\bigskip

\noindent If all induced graphs are connected, let us try to describe $\phi_H^{-1}(\pi')$. All set partitions $\pi$ of this set are coarser than $\pi'$, so can be seen as set partitions of the index set $[r]$ of the parts of $\pi'$. This identification does not change their M\"obius functions, which depends only on the number of parts. Then, it is easy to see that $\pi$ lies in $\phi_H^{-1}(\pi')$ if and only if $\pi$ is coarser than $\pi'$ and  two elements in the same part of $\pi$ never share an edge in $H/\pi'$ (here, $\pi$ is seen as a set partition of $[r]$). In other words, $\pi$ lies in $\phi_H^{-1}(\pi')$ if and only if $\pi \perp (H/\pi')$. This implies the Lemma.
\end{proof}
\bigskip

\noindent Consequently,
\begin{equation}\label{eq:jointcumulantgroup}
\kappa(Y_{\alpha_1},\dots, Y_{\alpha_r}) =
\sum_{\pi'} (-1)^{\ell(\pi')-1} M_{\pi'}\, \SF_{H/\pi'}\left( \prod_{i=1}^t \mathbbm{1}_{H[\pi'_i]\text{ connected}}\right),
\end{equation}
where the sum runs over all set partitions $\pi'$ of $[r]$.\medskip


\subsubsection{Bounding all the relevant quantities}
Using $|Y_{\alpha_i}| \le A$ for all $i$, we get the inequality: 
$$|M_\pi| \le A^{r-1}\, \esper[|Y_{\alpha_1}|].$$
Finally, to bound each summand $\kappa(Y_{\alpha_1},\dots,Y_{\alpha_r})$, we shall use the following bounds:
\begin{align*}
    |\SF_{H/\pi'}| &\le \ST_{H/\pi'}  \qquad \text{by Corollary \ref{cor:ineq_SFST};}\\
    \mathbbm{1}_{H[\pi'_i]\text{ connected}} &\le \ST_{H[\pi'_i]}\,.
\end{align*}
Thus, Equation \eqref{eq:jointcumulantgroup} gives
\begin{equation}\label{eq:boundkappa}
    |\kappa(Y_{\alpha_1},\dots, Y_{\alpha_r})| \le 
    A^{r-1}\, \esper [|Y_{\alpha_1}|]
    \,\sum_{\pi'} \,\ST_{H/\pi'} \left(\prod_{i=1}^t \ST_{H[\pi'_i]}\right) =
    A^{r-1}\, \esper[|Y_{\alpha_1}|]
    \, 2^{r-1}\, \ST_H,
\end{equation}
the last equality corresponding to Equation \eqref{eq:coloredpseudotree}.
Recall that $H=G[\alpha_1,\dots,\alpha_r]$.
Summing over $\alpha_1,\dots,\alpha_r$ and using Equation \eqref{eq:expcumulant}, we get 
$$
|\kappa^{(r)}(X)| \le (2A)^{r-1} \sum_{\alpha_1} \esper[|Y_{\alpha_1}|] \left[ \sum_{\alpha_2,\dots,\alpha_r} \ST_{G[\alpha_1,\dots,\alpha_r]} \right].
$$

\noindent From Corollary \ref{cor:countingcouplessequences_ST}, we know that the expression in the bracket is bounded by the quantity \hbox{$r^{r-2} (D+1)^{r-1}$} (for any fixed $\alpha_1$). This completes the proof of Theorem \ref{thm:dependencygraphs_sumY}.
\bigskip
