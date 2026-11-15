---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-003-12-the-cartan-distribution
section_title: "the Cartan distribution"
section_number: 1.2
pages: 6-8
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.941
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
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
