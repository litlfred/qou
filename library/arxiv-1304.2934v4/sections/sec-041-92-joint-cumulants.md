---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-041-92-joint-cumulants
section_title: "Joint cumulants"
section_number: 9.2
pages: 72-73
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.988
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
There exists a multivariate version of cumulants, called joint cumulants, that we shall use to prove Theorem~\ref{thm:dependencygraphsrefined}. We present in this paragraph its definition and basic properties. Most of this material can be found in Leonov's and Shiryaev's paper~\cite{LS59} (see also \cite[Proposition 6.16]{JLR00}).
\medskip


\subsubsection{Preliminaries: set-partitions}
We denote by $[n]$ the set $\{1,\dots,n\}$. Recall from Section \ref{subsec:twoexamples} that a {\em set partition} of $[n]$ is a (non-ordered) family of non-empty disjoint subsets of $S$ (called parts of the partition), whose union is $[n]$. For instance,
$$\{\{1,3,8\},\{4,6,7\},\{2,5\}\}$$
is a set partition of $[8]$. Denote $\qym(n)$ the set of set partitions of $[n]$. Then $\qym(n)$ may be endowed with a natural partial order: the {\em refinement} order. We say that $\pi$ is {\em finer} than $\pi'$ or $\pi'$ {\em coarser} than $\pi$ (and denote $\pi \leq \pi'$) if every part of $\pi$ is included in a part of $\pi'$.\medskip

Lastly, denote $\mu$ the M\"obius function of the poset $\qym(n)$. In this paper, we only use evaluations of $\mu$ at pairs $(\pi,\{[n]\})$ (the second argument is the partition of $[n]$ in only one part, which is the maximum element of $\qym(n)$), so we shall use abusively the notation $\mu(\pi)$ for $\mu(\pi,\{[n]\})$.  In this case, the value of the M\"obius function is given by:
\begin{equation}\label{eq:valuemobius}
    \mu(\pi) = \mu(\pi, \{[n]\})=(-1)^{\#(\pi)-1} (\# (\pi)-1)!\,.
\end{equation}
\medskip


\subsubsection{Definition and properties of joint cumulants}
If $X_1, \ldots, X_r$ are random variables with finite moments on the same probability space (denote $\esper$ the expectation on this space), we define their joint cumulant by
\begin{equation}
    \kappa (X_1,\dots,X_r) = [t_1 \cdots t_r] \,\,\log 
    \bigg( \esper\!\left[ \E^{t_1 X_1 + \cdots + t_r X_r} \right] \bigg).
    \label{eq:defcumulant}
\end{equation}
As usual, $[t_1 \dots t_r] F$ stands for the coefficient of $t_1 \cdots t_r$  in the series expansion of $F$ in positive powers of $t_1, \dots, t_r$. Note that joint cumulants are multilinear functions. In the case where all the $X_i$'s are equal, we recover the $r$-th cumulant $\kappa^{(r)}(X)$ of a single variable. Using set-partitions, joint cumulants can be expressed in terms of joint moments, and {\em vice-versa}:

\begin{align}
    \esper [X_1 \cdots X_r] &= \sum_{\pi \in \qym(r)} \prod_{C \in \pi}
    \kappa(X_i\,;\, i \in C);
    \label{eq:cumulant2moment} \\
    \kappa (X_1,\dots,X_r) &= \sum_{\pi \in \qym(r)} \mu(\pi)
    \prod_{C \in \pi} \esper\!\left[ \prod_{i \in C} X_i \right].
    \label{eq:moment2cumulant}
\end{align}
In these equations, $C \in \pi$ shall be understood as ``$C$ is a part of the set partition $\pi$''. Recall that $\mu(\pi)$ has an explicit expression given by Equation~\eqref{eq:valuemobius}. For example the joint cumulants of one or two variables are simply the mean of a single random variable and the covariance of a couple of random variables:
$$\kappa(X_1)=\esper[X_1]\qquad;\qquad \kappa(X_1,X_2)=\esper[X_1 X_2] - \esper[X_1]\, \esper[X_2].$$
For three variables, one has
\begin{align*}
\kappa(X_1,X_2,X_3) &= \esper[X_1 X_2 X_3] - \esper[X_1 X_2]\, \esper[X_3] - \esper[X_1 X_3]\, \esper[X_2] \\
&\quad- \esper[X_2 X_3]\, \esper[X_1] +2\, \esper[X_1] \,\esper[X_2] \,\esper[X_3].
\end{align*}

\begin{remark}
    The most important property of cumulants is their relation with independence: if the variables $X_1,\dots,X_r$ can be split in two non-empty sets of variables which are independent with each other, then $\kappa (X_1,\dots,X_r)$ vanishes \cite[Proposition 6.16 (v)]{JLR00}. We will not need this property here. In fact, we will prove a more precise version of it, see Equation~\eqref{eq:boundkappa}.
\end{remark}\medskip



\subsubsection{Statement with joint cumulants}
Theorems~\ref{thm:dependencygraphs} and \ref{thm:dependencygraphsrefined} have some analog with joint cumulants. Let $\{Y_\alpha\}_{\alpha \in V}$ be a family of random variables with dependency graph $G$. As in Theorem \ref{thm:dependencygraphs}, we assume that the variables $Y_\alpha$ are uniformly bounded by a constant $A$: {\em i.e.}, for all $\alpha \in V$, 
$$ \|Y_\alpha\|_\infty \leq A.$$
Consider $r$ subsets $V_1, V_2,\ldots, V_r$ of $V$, non necessarily distinct and set $X_i=\sum_{\alpha \in V_i} Y_{\alpha}$ (for $i \in [r]$). We denote $D_i$ the maximal number of vertices in $V_i$ adjacent to a given vertex (not necessarily in $V_i$). Then one has the following result.

\begin{theorem} \label{thm:boundjointcumulant}
With the notation above,
$$ |\kappa(X_1,\dots,X_r)| \le 2^{r-1}\, r^{r-2} \,|V_1|\,(D_2 +1) \cdots (D_r +1)\, A^r .$$
\end{theorem}

\noindent The proof of this theorem is very similar to the one of Theorem \ref{thm:dependencygraphsrefined}.
However, to simplify notation, we only prove the latter here.\bigskip
