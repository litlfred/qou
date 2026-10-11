---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-037-103-moderate-deviations-for-subgraph-count-stati
section_title: "Moderate deviations for subgraph count statistics"
section_number: 10.3
pages: 85-91
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
text_source: latex
latex_prose_ratio: 0.784
latex_coverage_ratio: 0.99
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




















\section{Random character values from central measures on partitions}\label{sec:central}
Our Theorem~\ref{thm:dependencygraphsrefined} can also be used to study certain models of random integer partitions. Recall that if $G$ is a finite group and if $\tau$ is a function $G \to \C$ with $\tau(e_{G})=1$ and $\tau(gh)=\tau(hg)$ (such a function is called a \emph{trace} on $G$), then $\tau$ can be expanded uniquely as a linear combination of normalized irreducible characters:
$$\tau=\sum_{\lambda \in \widehat{G}} \,\proba_{\tau}[\lambda]\,\widehat{\chi}^{\lambda},$$
where $\widehat{G}$ is the (finite) set of isomorphism classes of irreducible representations of $G$ and $\widehat{\chi}^{\lambda}$ the normalized ({\em i.e.} divided by the dimension of the space)
character of the irreducible representation associated to $\lambda$.
\begin{definition}
The map $\lambda \mapsto \proba_{\tau}[\lambda]$ is called the spectral measure of the trace $\tau$. It takes non-negative values if and only if, for every family $(g_1,\ldots,g_n)$ of elements of $G$, the matrix $(\tau(g_i(g_j)^{-1}))_{1 \leq i,j \leq n}$ is Hermitian non-negative definite. Then, the spectral measure is a probability measure on $\widehat{G}$.
\end{definition}
\bigskip

When $G=\sym(n)$ is the symmetric group of order $n$, the irreducible representations are indexed by \emph{integer partitions} of size $n$, that is non-increasing sequences of positive integers $\lambda=(\lambda_{1},\ldots,\lambda_{\ell})$ with $\sum_{i=1}^{\ell}\lambda_{i}=n$. In the following we denote $\pym(n)=\widehat{\sym}(n)$ the set of integer partitions of size $n$, and $\ell(\lambda)=\ell$ the length of a partition. We shall also consider the infinite symmetric group $\sym(\infty)=\bigcup_{n \ge 1} \sym(n)$, which is the group of permutations of the set of natural numbers that have a finite support.

\begin{definition}
A \emph{central measure} on partitions is a family $(\proba_{\tau,n})_{n \in \N}$ of spectral measures on the sets $\pym(n)$ that come from the same trace of the infinite symmetric group $\sym(\infty)$. In other words $(\proba_{\tau,n})_{n \in \N}$ is a central measure if there exists a trace $\tau : \sym(\infty) \to \C$ such that
$$\tau_{|\sym(n)}=\sum_{\lambda \in \pym(n)} \proba_{\tau,n}[\lambda]\,\widehat{\chi}^{\lambda}.$$
\end{definition}

\begin{example}
The regular trace $\tau(\sigma)=\mathbbm{1}_{\sigma=\mathrm{id}}$ corresponds to the Plancherel measures of the symmetric groups, given by the formula $\proba_{n}[\lambda]=(\dim V^\lambda)^{2}/n!$, where $V^{\lambda}$ is the $\sym(n)$-irreducible module of label $\lambda$. They have been extensively studied in connection with Ulam's problem of the longest increasing subsequence and with random matrix theory, see \emph{e.g.} \cite{BDJ99,BOO00,Oko00,IO02}.
\end{example}
\bigskip

A central measure $(\proba_{\tau,n})_{n \in \N}$ is non-negative if and only if $(\tau(\rho_{i}\rho_{j}^{-1}))_{1\leq i,j \leq n}$ is Hermitian non-negative definite for any finite family of permutations $\rho_{1},\ldots,\rho_{n}$. The set of non-negative central measures, \emph{i.e.}, coherent systems of probability measures on partitions has been identified in \cite{Tho64} and later studied in \cite{KV81}. Call extremal a non-negative trace on $\sym(\infty)$  that is not a positive linear combination of non-negative traces. Then, extremal central measures are indexed by the infinite-dimensional \emph{Thoma simplex}
$$\Omega=\bigg\{\omega=(\alpha,\beta)=\big((\alpha_{1}\geq \alpha_{2}\geq \cdots \geq 0),(\beta_{1}\geq \beta_{2}\geq \cdots \geq 0)\big)\,\,\bigg|\,\,\sum_{i=1}^{\infty}\alpha_{i}+\beta_{i}\leq 1\bigg\}.$$
The trace on the infinite symmetric group corresponding to a parameter $\omega$ is given by

\begin{equation}\label{eq:def_tau_omega}
\tau_{\omega}(\sigma)=\prod_{c \in C(\sigma)} p_{|c|}(\omega) \quad\text{with }p_{1}(\omega)=1,\,\,\,p_{k\geq 2}(\omega)=\sum_{i=1}^{\infty}(\alpha_{i})^{k}+(-1)^{k-1}(\beta_{i})^{k},
\end{equation}
$C(\sigma)$ denoting the set of cycles of $\sigma$. Kerov and Vershik have shown that if $\omega \in \Omega$ and $\rho \in \sym(\infty)$ are fixed, then the random character value $\widehat{\chi}^{\lambda}(\rho)$ with $\lambda$ chosen according to the central measure $\proba_{\omega,n}$ converges in probability towards the trace $\tau_{\omega}(\rho)$. Informally, central measures on partitions and extremal traces of $\sym(\infty)$ are {\em concentrated}. More recently, it was shown by F\'eray and M\'eliot that this concentration is Gaussian, see \cite{FM12,Mel12}. The aim of this section is to use the techniques of Sections \ref{sec:depgraph}-\ref{sec:erdosrenyi} in order to prove the following:

\begin{theorem}\label{thm:modgaussianrcv}
Fix a parameter $\omega \in \Omega$, and denote $\rho$ a $k$-cycle in $\sym(\infty)$ (for $k \ge 2$). Assume $p_{2k-1}(\omega)-(p_{k}(\omega))^{2}\neq 0$. Denote then $\RCV$ the random character value $\widehat{\chi}^{\lambda}(\rho)$, where:\vspace{2mm}
\begin{itemize}
\item $\lambda \in \pym(n)$ is picked randomly according to the central measure $\proba_{\omega,n}$, \vspace{2mm}
\item and $\widehat{\chi}^{\lambda}$ denotes the normalized irreducible character indexed by $\lambda$ of $\sym(n)$, that is 
$$\widehat{\chi}^{\lambda}(\rho)=\frac{\mathrm{tr}\, \Pi^{\lambda}(\rho)}{\dim V^{\lambda}}\qquad \text{ with }(V^{\lambda},\Pi^{\lambda}) \text{ irreducible representation of }\sym(n).$$
\end{itemize}
The rescaled random variable $n^{2/3}\,\big[\RCVk-p_{k}(\omega)\big]$ converges in the mod-Gaussian sense with parameters $t_{n}=n^{1/3}\,\sigma^{2}$ and limiting function $\psi(z)=\exp(L\,\frac{z^{3}}{6})$, where
\begin{align*}
\sigma^{2}&=k^{2}\,\big(p_{2k-1}(\omega)-p_{k}(\omega)^{2}\big);\\
L&= k^{3}\,\big((3k-2)\,p_{3k-2}(\omega)-(6k-3)\,p_{2k-1}(\omega)\,p_{k}(\omega)+(3k-1)\,p_{k}(\omega)^{3}\big).
\end{align*}
\end{theorem}

As in Section \ref{sec:erdosrenyi}, the mod-Gaussian convergence is proved by bounds on cumulants of type \eqref{eq:superbound}.
Furthermore, the hypothesis \eqref{eq:limitcumulant} on the third and second cumulant are ensured
by the polynomiality of joint cumulants --- Lemma \ref{lem:cumulantcharacterpoly}.
Therefore, we can apply Propositions \ref{prop:largedeviationscumulants} and \ref{prop:normalityzone}.
\begin{corollary}\label{cor:moderatedeviationcharacter}
Let $\SubGraph_{k}=\RCVk$ be the random character value on a $k$-cycle as defined above.
Then $n^{1/2}\, (\SubGraph_{k}-p_{k}(\omega))$ satisfies a central limit theorem with normality zone 
$o(n^{1/6})$.
Moreover, at the edge of this normality zone and at a slightly larger scale, the deviation probabilities are given by:
for any sequence $x$ of positive numbers bounded away from $0$ with $x_n=o\big( n^{1/12} \big)$,
one has
\begin{align*}
    \proba\left[n^{1/2} (\SubGraph_{k}-p_{k}(\omega))\geq n^{1/6} \sigma^2 x_n\right]&=
\frac{\E^{-\frac{(x_n)^2\, n^{1/3}\sigma^2}{2}}}{x_n\, n^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)).\\
    \proba\left[n^{1/2} (\SubGraph_{k}-p_{k}(\omega))\leq - n^{1/6} \sigma^2 x_n\right]&=
\frac{\E^{-\frac{(x_n)^2\, n^{1/3}\sigma^2}{2}}}{x_n\, n^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{-L(x_n)^3}{6}}\,(1+o(1)).
\end{align*}
where $\sigma^{2}$ and $L$ as in Theorem \ref{thm:modgaussianrcv}.
\end{corollary}\bigskip


\begin{remark}\label{rem:limitvarianceispositive}
The condition $\sigma^{2}>0$ is satisfied as soon as the sequence $\alpha \sqcup \beta$ associated to the Thoma parameter $\omega$ contains two different non-zero coordinates. Indeed, for any summable non-increasing non-negative sequence $\gamma=(\gamma_{1},\gamma_{2},\ldots)$ with $\gamma_{i}>\gamma_{i+1}$ for some $i$, one has
$$\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k-\eps} \right)\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k+\eps} \right) \geq \left(\sum_{i=1}^{\infty} (\gamma_{i})^{k} \right)^{2}$$
with equality if and only if $\eps=0$. Indeed, the derivative of the function of $\eps$ on the left-hand side is
$$\sum_{i<j} \left(\gamma_{i}\gamma_{j}\right)^{k}\,\log\!\left(\frac{\gamma_{i}}{\gamma_{j}}\right)\,\left(\left(\frac{\gamma_{i}}{\gamma_{j}}\right)^{\!\eps}-\left(\frac{\gamma_{j}}{\gamma_{i}}\right)^{\!\eps}\,\right).$$
Applying the result to $\gamma=\alpha \sqcup \beta$ and $\eps=k-1$, we obtain on the left-hand side
$$\left(\sum_{i=1}^{\infty} \gamma_{i} \right)\left(\sum_{i=1}^{\infty} (\gamma_{i})^{2k-1} \right) = \left(\sum_{i=1}^{\infty} \alpha_{i}+\beta_{i} \right)\,p_{2k-1}(\omega)\leq p_{2k-1}(\omega)$$
and on the right-hand side
$$\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k}\right)^{2} \geq \left(\sum_{i=1}^{\infty} (\alpha_{i})^{k} + (-1)^{k-1}(\beta_{i})^{k}\right)^{2}=(p_{k}(\omega))^{2}.$$
This proof shows that the condition $\sigma^{2}>0$ is also satisfied if $0<\sum_{i=1}^{\infty} \alpha_{i}+\beta_{i}<1$.
\end{remark}


This Section is organized as follows. In Section \ref{subsec:prelim_chmu}, we present the necessary material. In Section \ref{subsec:boundcumulantchmu}, we then prove bounds on these cumulants similar to those of Proposition \ref{prop:boundcumulantsubgraph}, and we compute the limits of the second and third cumulants. This will allow us to use in Section \ref{subsec:asymptoticrcv} the framework of Section \ref{subsec:deviationscumulant} in order to prove the results stated above. We shall also detail some consequences of these results for the shapes of the random partitions $\lambda \sim \proba_{n,\omega}$ viewed as Young diagrams, in the spirit of \cite{FM12,Mel12}. \bigskip




\subsection{Preliminaries}\label{subsec:prelim_chmu}

\subsubsection{Non-commutative probability theory}
The originality of this section is that, although the problem is formulated in a classical probability space,
it is natural to work in the setting of non-commutative probability theory.
\begin{definition}
    A {\em non-commutative probability space} is a complex unital $\star$-algebra $\mathscr{A}$ 
    with some linear functional $\varphi:\mathscr{A} \to \C$ such that $\varphi(1)=1$ and,
    for any $a \in \mathscr{A}$, $\varphi(a^\star a) \ge 0$.
\end{definition}
This generalizes the notion of probability space: elements of $\mathscr{A}$ should be thought as random variables, while $\varphi$ should be thought as the expectation. The difference is that, unlike random variables in usual probability theory, elements of $\mathscr{A}$ are not assumed to commute. Usually one also assumes that $\varphi$ is tracial, \emph{i.e.}, $\varphi(ab)=\varphi(ba)$ for any $a,b\in\mathscr{A}$.\bigskip

There are five natural analogues of the notion of independence in non-commutative probability theory, see~\cite{Muraki03}. In our context, the relevant one is the following one, sometimes called {\em tensor independence} \cite[Definition 1.1]{HS10}.
\begin{definition}
    Two subalgebras $\mathscr{A}_1$ and $\mathscr{A}_2$ of $\mathscr{A}$ are {\em tensor independent} if and only if, for any sequence $a_1,\dots,a_r$ with, for each $i$, $a_i \in \mathscr{A}_1$ or $a_i \in \mathscr{A}_2$, one has
    \[\varphi(a_1 \dots a_r) = 
    \varphi \left(\prod_{\substack{1\le i \le r \\ a_i \in \mathscr{A}_1}}^{\rightarrow} a_i\right)
    \varphi \left(\prod_{\substack{1\le i \le r \\ a_i \in \mathscr{A}_2}}^{\rightarrow} a_i\right)
    .\]
    The arrow on the product sign means that the $a_i$ in the product appear in the same order as in $a_1,\dots,a_r$.
\end{definition}

With this definition of independence, the notion of dependency graph presented in Section \ref{subsec:dependencygraphs} is immediately extended to the non-commutative framework. One can also define joint cumulants as follows: if $a_1,\dots,a_r$ are elements in $\mathscr{A}$, we set
$$\kappa(a_1,\dots,a_r) = \sum_{\pi} \,\mu(\pi) \,\prod_{B \in \pi} \varphi \!\left( 
\prod^{\rightarrow}_{i \in B} a_i \right).$$
Note that, in the proof of Theorem~\ref{thm:dependencygraphsrefined}, independence is only used in equation~\eqref{eq:alsoinnoncommutative}. By definition of tensor independence, equation~\eqref{eq:alsoinnoncommutative} also holds in the non-commutative setting and hence, so does Theorem~\ref{thm:dependencygraphsrefined}.
\bigskip



\subsubsection{Two probability spaces}
From now on, we fix an element $\omega$ in the Thomas simplex $\Omega$. Denote $\C\sym(n)$  the group algebra of $\sym(n)$. The function $\tau_\omega$, defined by Equation \eqref{eq:def_tau_omega}, can be linearly extended to $\C\sym(n)$. Then $(\C\sym(n),\tau_{\omega})$ is a non-commutative probability space.
\bigskip

Note that we are now working with two probability spaces: the non-commutative probability space $(\C\sym(n),\tau_{\omega})$ and the usual probability space that we want to study (the set of Young diagrams of size $n$ with the probability measure $\proba_{\omega,n}$). They are related as follows. Consider an element $y$ in $\C\sym(n)$ and define the random variable (for the usual probability space) $X_y$ by $X_y(\lambda)=\widehat{\chi}(y)$.
Then one has
\[\esper_{\proba_{\omega,n}}(X_y) = \sum_{\lambda \vdash n} \proba_{\omega,n}(\lambda)
\widehat{\chi}(y) = \tau_\omega(y).\]
In other words, the {\em expectations} of $y$ (in the non-commutative probability space) and of $X_y$ (in the usual probability space) coincide (recall that the trace of a non-commutative probability space, here $\tau_\omega$, is considered as an expectation).
\bigskip

Besides, if we restrict to the {\em center} of $(\C\sym(n),\tau_{\omega})$, then the map $y \mapsto X_y$ is an {\em algebra morphism}, called {\em discrete Fourier transform}. As a consequence, if $y_1,\dots,y_r$ lie in the center of $(\C\sym(n),\tau_{\omega})$, their joint moments (and joint cumulants) are the same as those of $X_{y_1},\dots,X_{y_r}$.



\subsubsection{Renormalized conjugacy classes and polynomiality of cumulants}
Given a partition $\mu=(\mu_{1},\ldots,\mu_{\ell})$ of size $|\mu|=\sum_{i=1}^{\ell}\mu_{i}=k$, we denote 
$$\varSigma_{\mu,n}=\sum_{A} \rho_\mu(A) \text{ where } \rho_\mu(A)=(a_1,\ldots,a_{\mu_{1}})(a_{\mu_1+1},\ldots,a_{\mu_1+\mu_{2}})\cdots.$$
In the equation above, the formal sum is taken over arrangements in $\arr(n,k)$ and is considered as an element of the group algebra $\C\sym(n)$. It clearly lies in its center. Besides, $\varSigma_{\mu,n}$ is the sum of $n\fall{k}$ elements of cycle-type $\mu$, hence, if $\rho$ is a fixed permutation of type $\mu$, one has:
\[X_{\varSigma_{\mu,n}} = n\fall{k} X_\rho.\]
Note that considering these elements $\varSigma_{\mu,n}$ and their normalized characters is a classical trick in the study of central measures on Young diagrams; see \cite{IO02,Sni06b,FM12}.
\bigskip

Fix some permutations $\rho_1,\dots,\rho_r$ of respective size $k_1,\dots,k_r$. Denote $\mu^{1},\ldots,\mu^{r}$ their cycle-types.
\begin{align}
n\fall{k_{1}}\cdots n\fall{k_{r}}\,\,\kappa\!\left(\SubGraph_{\rho_{\mu^{1}}},\ldots,\SubGraph_{\rho_{\mu^{r}}}\right)&=\kappa(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}})\nonumber\\
&=\sum_{\substack{A^{1}\in \arr(n,k_{1}) \vspace{-1mm} \\ \vdots  \vspace{1mm}\\ A^{r} \in \arr(n,k_{r})}}
\kappa\left(\rho_{\mu^{1}}(A^{1}),\ldots,\rho_{\mu^{r}}(A^{r})\right).\label{eq:listequality}
\end{align}
As in the framework of subgraph count statistics,
the invariance of $\tau_\omega$ by conjugacy of its argument
implies that the joint cumulant $\kappa\left(\rho_{\mu^{1}}(A^{1}),\ldots,\rho_{\mu^{r}}(A^{r})\right)$
depends only on the graph $G_{\mathbb{A}}$ associated to the family of arrangement
$\mathbb{A}=(A^{1},\dots,A^{r})$.
Copying the proof of Corollary~\ref{cor:jointcumulantpoly},
we get:
\begin{lemma}\label{lem:cumulantcharacterpoly}
Fix some integer partitions  $\mu^1,\dots,\mu^r$. Then the rescaled joint cumulant 
$$\kappa(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}})=n\fall{k_{1}}\cdots n\fall{k_{r}}\,\,\kappa\!\left(\SubGraph_{\rho_{\mu^{1}}},\ldots,\SubGraph_{\rho_{\mu^{r}}}\right)
$$ 
is a polynomial in $n$.
\end{lemma}\bigskip
