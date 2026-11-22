---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-004-13-diffieties
section_title: "diffieties"
section_number: 1.3
pages: 8-10
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.96
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
We now use jets to define PDEs and present their geometric portraits: diffieties. Let $P$ be a manifold of dimension $n + m$.

\begin{definition}\label{def:PDE}
A \emph{system of $k$-th order partial differential equations imposed on $n$-dimensional submanifolds of $P$}, or simply a \emph{PDE}, is a closed submanifold $\mathscr E_0 \subseteq J^k (P, n)$ of the $k$-jet space. A \emph{solution} of a PDE $\mathscr E_0 \subseteq J^k (P, n)$ is an $n$-dimensional submanifold $N \subseteq P$ such that $N^k \subseteq \mathscr E_0$.
\end{definition}

\begin{remark}
As a minimal regularity condition on a PDE $\mathscr E_0 \subseteq J^k (P, n)$ we will always assume $\dim \mathscr E_0 \geq n$ so that the existence of solutions is not excluded a priori by trivial dimensional reasons.
\end{remark}

For a PDE $\mathscr E_0 \subseteq J^k (P, n)$, locally, in jet coordinates, we have
\begin{equation}\label{eq:PDE}
\mathscr E_0 : F_a (x, \ldots, u_I, \ldots) = 0, \quad |I| \leq k,
\end{equation}
for some local smooth functions $F_a \in C^\infty (J^k (P, n))$. If $N \subseteq P$ is an $n$-dimensional submanifold locally given by
\[
N : u^\alpha = f^\alpha (x) ,
\]
then $N$ is a solution of $\mathscr E_0$ iff
\[
F_a \left(x, \ldots, \frac{\partial^{|I|}f}{\partial x^I}, \ldots\right) = 0 .
\]
This motivates Definition \ref{def:PDE}.

In Algebraic Geometry, given a system of algebraic equations, it is natural to take all their algebraic consequences. In other words, given a subset of polynomials, it is natural to consider the ideal that they span. Similarly, given a PDE (\ref{eq:PDE}), it is natural (besides their smooth consequences) to take all their total derivatives, this can be done in a coordinate free way via a construction known as \emph{prolongation} that we now describe. Let $\mathscr E_0 \subseteq J^k (P, n)$ be a PDE, and let $q = 0, 1, \ldots, \infty$.

\begin{definition}\label{def:prolong}
The \emph{$q$-prolongation} of $\mathscr E_0$ is the subset $\mathscr E_q \subseteq J^{k+q} (P, n)$ of the $(k+q)$-jet space defined by
\begin{equation}\label{eq:prolong}
\mathscr E_q := J^q (\mathscr E_0, n) \cap J^{k+q} (P, n).
\end{equation}  
The $\infty$-prolongation will be often denoted simply $\mathscr E$.
\end{definition}

Definition \ref{def:prolong} requires some little explanations. As $\mathscr E_0$ is a submanifold in $J^k (P, n)$, its jet space $J^q (\mathscr E_0, n)$ is a submanifold in the jet space $J^q (J^k (P, n), n)$ as in Remark \ref{rem:jet_emb}. The jet space $J^{k+q} (P, n)$ can be seen as a submanifold in $J^q (J^k (P, n), n)$ as well via the embedding in Remark \ref{rem:J^k+h}. This explains the intersection in (\ref{eq:prolong}). We stress that we will always understand the prolongation $\mathscr E_q$ as a subset in $J^{k+q} (P, n)$. If $\mathscr E_0$ is locally given by (\ref{eq:PDE}), then its $q$-prolongation is locally given by
\[
\mathscr E_q : D_J F_a (x, \ldots, u_I, \ldots) = 0, \quad |J| \leq q.
\]
This shows that $\mathscr E_q$ encodes in a coordinate free way the total derivatives of $\mathscr E_0$ up to order $q$, as desired.

\begin{remark}
For a generic $\mathscr E_0 \subseteq J^k (P, n)$ its $q$-th prolongation $\mathscr E_q$ is \emph{not} a submanifold in $J^{k + h} (P, n)$. When it is a submanifold, then it is clearly a PDE with the same solutions as $\mathscr E_0$. In the following, we will always assume that the $\infty$-th prolongation $\mathscr E = \mathscr E_\infty$ is a submanifold in $J^\infty (P, n)$. This happens, e.g., when $\mathscr E_0$ is a \emph{formally integrable PDE}. Our assumptions are not a great loss of generality according to \emph{Cartan-Kuranishi Prolongation Theorem} which roughly states that, under mild regularity conditions, every PDE becomes formally integrable after finitely many $1$-prolongations.
\end{remark}

Now on we concentrate on the $\infty$-prolongation $\mathscr E \subseteq J^\infty (P, n)$.

\begin{proposition}\label{prop:diffiety}
Let $\mathscr E_0 \subseteq J^k (P, n)$ be a PDE. Assume that its $\infty$-prolongation $\mathscr{E} \subseteq J^\infty (P, n)$ is a submanifold. Then the Cartan distribution restricts to $\mathscr E$ in the sense that
\[
\mathscr C_z \subseteq T_z \mathscr E \quad \text{for all $z \in \mathscr E$}.
\]
Hence the restriction $\mathscr C : \mathscr E \to J^1 (\mathscr E, n)$ is a well-defined rank $n$ involutive distribution on $\mathscr E$. Additionally it detects solutions of $\mathscr E_0$ in the following sense: a submanifold $S \subseteq \mathscr E$ is locally of the form $S = N^\infty$ for some solution $N$ of $\mathscr E_0$ if and only if it is an $n$-dimensional integral submanifold of $\mathscr C$. 
\end{proposition}

The restriction of the Cartan distribution to the $\infty$-prolongation of a PDE will be denoted by $\mathscr C$ as well and called the \emph{Cartan distribution}.

\begin{definition}
A \emph{diffiety} (from the words \emph{differential equation} and \emph{variety}) is a pair $(\mathscr E, \mathscr C)$ where $\mathscr E$ is the $\infty$-prolongation of some PDE and $\mathscr C$ is the Cartan distribution on $\mathscr E$.
\end{definition}

Proposition \ref{prop:diffiety} now shows that a diffiety $(\mathscr E, \mathscr C)$ contains most of the relevant information about the PDE $\mathscr E_0$ defining it.

We conclude this section briefly discussing \emph{infinitesimal symmetries} of a PDE. Let $(\mathscr E, \mathscr C)$ be the diffiety corresponding to a PDE $\mathscr E_0$.

\begin{definition}\label{def:inf_symm_E}
An \emph{infinitesimal symmetry} of $\mathscr E_0$ is a vector field $Y \in \mathfrak X (\mathscr E)$ such that $[Y, \Gamma (\mathscr C)] \subseteq \Gamma (\mathscr C)$. A \emph{non-trivial infinitesimal symmetry} is an infinitesimal symmetry modulo \emph{trivial ones}, i.e.{} sections of $\mathscr C$.
\end{definition}

\begin{remark}
The terminology ``trivial, non-trivial symmetries'' in Definition \ref{def:inf_symm_E} is motivated by the following facts. Let $X$ be a section of the Cartan distribution on $J^\infty (P, n)$ and let $(\mathscr E, \mathscr C)$ be any diffiety, then $X$ is tangent to $\mathscr E$ and $X|_{\mathscr E}$ is an infinitesimal symmetry of $\mathscr E_0$. In other words, sections of the Cartan distribution are infinitesimal symmetries of \emph{all} PDEs (regardless what is the PDE we are considering). 
\end{remark}

There is an efficient description of (non-trivial) infinitesimal symmetries in local coordinates. Consider the vector bundle $V \to J^\infty (P, n)$ from the previous subsection. Its sections are sometimes called \emph{generating sections of symmetries} for the following reasons. Take the restriction $V_{\mathscr E} \to \mathscr E$ of $V$ to $\mathscr E$. Sections of $V_{\mathscr E}$ are locally spanned by the restrictions $v_\alpha|_{\mathscr E}$, $\alpha = 1, \ldots, m$. Take a section $\chi \in \Gamma (V_{\mathscr E})$ and let it be locally given by $\chi = \chi^\alpha v_\alpha|_{\mathscr E}$ for some local functions $\chi^\alpha \in C^\infty (\mathscr E)$. Moreover, let $\tilde \chi \in \Gamma (V)$ be an extension of $\chi$, i.e.{} $\chi = \tilde \chi|_{\mathscr E}$. Finally, let $Y \in \mathfrak X_{\mathscr C}$ be any infinitesimal symmetry of the Cartan distribution on $J^\infty (P, n)$ mapping to $\tilde \chi$ under the projection $X_{\mathscr C} \to \Gamma (V)$ (if we are working locally, we can take, e.g., the evolutionary vector field $\rE_{\tilde \chi}$). If $\mathscr E_0$ is locally given by (\ref{eq:PDE}), one can show that $Y$ is tangent to $\mathscr E$ if and only if locally $\chi$ is a solution of the following \emph{universal linearization} of $\mathscr E_0$:
\[
\ell_{\mathscr E} (\chi) = 0 
\]
 
where 
\[
\ell_{\mathscr E} : \Gamma (V_\mathcal E) \to C^\infty (J^\infty (P,n))^r, \quad r = \operatorname{codim} \mathscr E_0 = \text{number of PDEs}
\]
is the locally defined operator given by
\[
\ell_{\mathscr E}(\chi) = \big( \ell_{\mathscr E}(\chi)_1, \ldots, \ell_{\mathscr E}(\chi)_r \big), \quad \ell_{\mathscr E}(\chi)_a := \left(\rE_{\tilde \chi} F_a\right)|_{\mathscr E} = \frac{\partial F_a}{\partial u^\alpha_I}|_{\mathscr E} D_I|_{\mathscr E} \chi^\alpha.
\]
and    we used that all the total derivatives are tangent to $\mathscr E$  (a more intrinsic and global interpretation of the universal linearization can be provided for PDEs imposed on sections of a fibration, particularly when $\mathcal E_0$ is specified as the zero locus of a \emph{nonlinear differential operator}, see e.g.{} \cite[Chapter 4, Section 2.7]{b...99} or \cite[Section 3.9]{kv98})  . In this case, the restriction $Y|_{\mathscr E}$ is a infinitesimal symmetry of $\mathscr E_0$  

\begin{proposition}
The assignment $\chi \mapsto Y|_{\mathscr E} \operatorname{mod} \Gamma (\mathscr C)$ establishes a bijection between solutions of the universal linearization
\[
\ell_{\mathscr E} (\chi) = 0
\]
of $\mathscr E_0$ and infinitesimal symmetries of $\mathscr E_0$.
\end{proposition}

\begin{remark}
The universal linearization is a linear PDE imposed on sections of the vector bundle $V_{\mathscr E} \to \mathscr E$. As it only involves total derivatives, for any solution $N$ of $\mathscr E_0$, it can be pulled-back along the embedding $j^\infty : N \to \mathscr E$ of Remark \ref{rem:emb_N}. If we do so we get a new linear PDE for sections of the pull-back bundle $j^\infty{}^\ast V$. The latter PDE is just the linearization of $\mathscr E_0$ around the solution $N$. This explain the terminology ``universal linearization''.
\end{remark}
