---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-003-12-the-cartan-distribution
section_title: "the Cartan distribution"
section_number: 1.2
pages: 6-10
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly non-li"
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.942
---
\label{Sec:CD}
The main geometric structure on jet spaces is the \emph{Cartan distribution}. There are several equivalent ways to define it. The one we present here will be also useful in defining the prolongation of a PDE in the next subsection. We begin noticing that a section of the fibration $J^1 (P, n) \to J^0 (P, n) \cong P$ can be interpreted as an $n$-dimensional distribution on $P$. Now, for every $1 \leq k \leq \infty$, the $k$-jet space is canonically equipped with a rank $n$ \emph{distribution along the projection $J^{k} (P, n) \to J^{k-1}(P, n)$}, i.e.{} a smooth map
\[
\mathscr C : J^k (P, n) \longrightarrow J^1 \big(J^{k-1} (P, n), n\big)
\]
such that the following diagram commutes
\[
\begin{array}{c}
\xymatrix{
 & J^1 \big(J^{k-1} (P, n), n\big) \ar[d] \\
 J^k (P, n) \ar[ur]^-{\mathscr C} \ar[r] & J^{k-1} (P, n)
}
\end{array}.
\]
The \emph{Cartan distribution} $\mathscr C$ is defined as follows. For $z = N^k_p \in J^k (P, n)$, denote by $\bar z = N^{k-1}_p \in J^{k-1}(P, n)$ its projection. Now put
\[
\mathscr C_z := \big( N^{k-1} \big){}^1_{\bar z} = T_{\bar z} \big(N^{k-1} \big) \in J^1 \big(J^{k-1} (P, n), n\big).
\]
In other words $\mathscr C_z$ is the $1$-jet at $\bar z$ of the $(k-1)$-jet prolongation of $N$. In local coordinates
\begin{equation}\label{eq:C_loc}
\mathscr C^\ast ( u^\alpha_{I, j}) = u^\alpha_{Ij}, \quad |I| \leq k-1, \quad j = 1, \ldots, n,
\end{equation}
where, in the left hand side, we denoted by $(x^i, u^\alpha_{I, j})$ the jet coordinates on the $1$-jet space $J^1 \big(J^{k-1} (P, n), n\big)$ (corresponding to the coordinates $(x^i, u^\alpha_I)$ on $J^{k-1}(P, n)$), and, in the right hand side, we are using concatenation of multiindexes.

\begin{remark}\label{rem:J^k+h}
The Cartan distribution $\mathscr C : J^k (P, n) \longrightarrow J^1 \big(J^{k-1} (P, n), n\big)$ is an embedding that we often use to interpret the $k$-jet space $J^k (P, n)$ as a submanifold in the jet space $J^1 \big(J^{k-1} (P, n), n\big)$. More generally for any two non-negative integers $h, k$, there is an embedding
\[
J^{h+k} (P, n) \hookrightarrow J^h \big(J^{k} (P, n), n\big)
\]
given by
\[
N^{h+k}_p \mapsto (N^k)^h_{\overline p}, \quad \overline p = N^k_p.
\]
In the next subsection we will use this embedding to interpret $J^{h+k} (P, n)$ as a submanifold in $J^h \big(J^{k} (P, n), n\big)$.
\end{remark}

For $k = \infty$, the Cartan distribution is a honest rank $n$ distribution on $J^\infty (P, n)$, and (\ref{eq:C_loc}) shows that it is locally spanned by the \emph{total derivatives}, i.e.{} the following vector fields
\[
D_i := \frac{\partial}{\partial x^i} + \sum_{|I| < \infty} u^\alpha_{Ii} \frac{\partial}{\partial u^\alpha_I}, \quad i = 1, \ldots, n.
\]
Dually, the annihilator $\mathscr C^0 \subseteq T^\ast J^\infty (P, n)$ is spanned by the \emph{Cartan forms}
\[
du^\alpha_I - u^\alpha_{Ii}dx^i, \quad \alpha = 1, \ldots, m, \quad |I| \leq \infty.
\]
 
Here, and in the rest of the paper, we adopt the Einstein summation convention over pairs of lowercase-uppercase indexes. We will not adopt the Einstein convention for multiindexes.
  

\begin{proposition}
The Cartan distribution on $J^\infty (P, n)$ is involutive, i.e.{} the commutator of two sections of $\mathscr C$ lays in $\mathscr C$ as well. Additionally it detects $\infty$-jet prolongations in the following sense: a submanifold $S \subseteq J^\infty (P, n)$ is locally of the form  $S = N^\infty$ for some $n$-dimensional submanifold $N \subseteq P$ if and only if it is an $n$-dimensional integral submanifold of $\mathscr C$. 
\end{proposition}


So, morally, the $\infty$-jet prolongation construction $N \mapsto N^\infty$ identifies $n$-dimensional submanifolds of $P$ with $n$-dimensional integral submanifolds of $\mathscr C$. In the following, \emph{Cartan distribution} will always mean the Cartan distribution on $J^\infty (P, n)$ (unless otherwise stated).

For their importance in the next section, we now discuss \emph{infinitesimal symmetries of the Cartan distribution $\mathscr C$}, i.e.{} vector fields $Y$ on $J^\infty (P, n)$ such that $[Y, \Gamma (\mathscr C)] \subseteq \Gamma (\mathscr C)$. Denote by $\mathfrak X_{\mathscr C}$ the Lie algebra of infinitesimal symmetries of $\mathscr C$ and notice that, by involutivity, $\Gamma (\mathscr C) \subseteq \mathfrak X_{\mathscr C}$ is an ideal. We want to show that the quotient Lie algebra $\mathfrak X_{\mathscr C} / \Gamma (\mathscr C)$ identifies with sections of an appropriate vector bundle $V \to J^\infty (P, n)$. We first define $V$. So let $z = N^\infty_p \in J^\infty (P, n)$. The fiber of $V$ over $z$ is then the $m$-dimensional vector space
\[
V_z := T_p P / T_p N.
\]
In the following, we denote by $\pi : J^\infty (P, n) \to P$ the projection. Now, let $Y \in \mathfrak X_{\mathscr C}$. We define a section $\overline Y$ of $V$ as follows. For $z = N^\infty_p \in J^\infty (P, n)$ put
\[
\overline Y_z := d\pi (Y_z) \operatorname{mod} T_p N \in T_p P / T_p N = V_z.
\]

\begin{proposition}
The assignment $Y \mapsto \overline Y$ defines an $\mathbb R$-linear surjection $\mathfrak X_{\mathscr{C}} \to \Gamma (V)$ with kernel given by $\Gamma (\mathscr C)$. Hence there is a canonical short exact sequence of vector spaces
\[
0 \longrightarrow \Gamma (\mathscr C) \longrightarrow \mathfrak X_{\mathscr C} \longrightarrow \Gamma (V) \longrightarrow 0.
\]
In particular, $\Gamma (V)$ inherits from $\mathfrak X_{\mathscr C}$ a Lie bracket.
\end{proposition}


The Lie bracket on $\Gamma (V)$ is sometimes called the \emph{higher Jacobi bracket} and denoted by $\{-,-\}$. We conclude this section describing it in local coordinates. First notice that $\Gamma (V)$ is locally spanned by the sections $v_\alpha$ defined as follows. For $z = N^\infty_p \in J^\infty (P, n)$ put
\[
v_\alpha |_z := \frac{\partial}{\partial u^\alpha}|_p \operatorname{mod} T_p N \in T_p P / T_p N = V_z.
\]
The isomorphism $\Gamma (V) \cong \mathfrak X_{\mathscr{C}} / \Gamma (\mathscr C)$ is now locally given by
\[
\chi \mapsto \rE_\chi \operatorname{mod} \Gamma (\mathscr C)
\]
where, for $\chi = \chi^\alpha v_\alpha \in \Gamma (V)$, we denoted by $\rE_\chi$ the (local) infinitesimal symmetry of $\mathscr C$ locally given by
\begin{equation}\label{eq:ev_vf}
\rE_\chi = \sum_{|I| < \infty} D_I \chi^\alpha \frac{\partial}{\partial u^\alpha_I},
\end{equation}
and, for any multiindex $i_1\cdots i_h$,
\[
D_{i_1 \cdots i_h} := D_{i_1} \circ \cdots \circ D_{i_h}.
\]
 
We mention for the reader unfamiliar with the cyrillic alphabet, that the script $\rE$ appearing in (\ref{eq:ev_vf}) is pronounced [e], like in s\underline{e}t.
  
A vector field of the form $\rE_\chi$ is sometimes called an \emph{evolutionary vector field}. Notice that evolutionary vector fields are only locally defined on $\infty$-jets of submanifolds (while one can give a coordinate free meaning to (\ref{eq:ev_vf}) on $\infty$-jets of sections of a fibration,  see e.g.{} \cite[Chapter 4, Section 2.4]{b...99} or \cite[Section 3.9]{kv98}  ). It easily follows from (\ref{eq:ev_vf}) that, if $\chi$ and $\psi$ are sections of $V$ locally given by $\chi = \chi^\alpha v_\alpha$ and $\psi = \psi^\beta v_\beta$, then their higher Jacobi bracket $\{ \chi, \psi\}$ is the section locally given by
\[
\{ \chi, \psi \} = \big(\rE_\chi \psi^\alpha - \rE_\psi \chi^\alpha\big) v_\alpha = \sum_{|I|< \infty}\left(D_I \chi^\beta \frac{\partial \psi^\alpha}{\partial u^\beta_I} - D_I \psi^\beta \frac{\partial \chi^\alpha}{\partial u^\beta_I}\right) v_\alpha.
\]


\subsection{diffieties} We now use jets to define PDEs and present their geometric portraits: diffieties. Let $P$ be a manifold of dimension $n + m$.

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
