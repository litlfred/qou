---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-002-11-jet-spaces
section_title: "jet spaces"
section_number: 1.1
pages: 4-6
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.941
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
Let $n,m$ be non-negative integers, and let $P$ be a manifold of dimension $n + m$. We begin providing an intrinsic definition of \emph{derivatives} of an $n$-dimensional submanifold $N \subseteq P$. In the following, $n$ should be interpreted as the number of \emph{independent variables}, $m$ as the number of \emph{dependent variables}, and $P$ as the space parameterizing both independent and dependent variables. In other words, in this theory, dependent and independent variables can be mixed and swapped. Around every point $p \in N$ there are coordinates $(x^i, u^\alpha)$ on $P$, $i = 1, \ldots, n$, $\alpha = 1,\ldots, m$, \emph{adapted} to $N$ in the sense that, in these coordinates, $N$ looks like the \emph{graph of a map}:
\begin{equation}\label{eq:N_loc}
N :  u^\alpha = f^\alpha (x)  .
\end{equation}
We will need to take multiple partial derivatives of the $f$'s with respect to the $x$'s. We adopt the following notation. Let $h$ be a non-negative integer and let $I = i_1\cdots i_h$ be a \emph{multiindex}, i.e.{} a (possibly empty) word containing $h$ letters $i_\ell \in \{1, \ldots, n\}$, $\ell = 1, \ldots, h$. We identify two words if they only differ by a permutation of their letters. We also compose two words by concatenation. Denote $|I| := h$ and call it the \emph{lenght} of the multiindex $I$. Finally denote
\[
\frac{\partial^{|I|} f^\alpha}{\partial x^I} := \frac{\partial^h f^\alpha}{\partial x^{i_1} \ldots \partial x^{i_h}}.
\] 

If there is another $n$-dimensional submanifolds $\tilde N$ through $p$, i.e.{} $p \in N \cap \tilde N$, then around $p$ there are coordinates $(x^i, u^\alpha)$ on $P$ adapted to both $N, \tilde N$:
\[
N : u^\alpha = f^\alpha (x), \quad \text{and} \quad \tilde N : u^\alpha = \tilde f{}^\alpha (x) .
\]
In this case we say that $N$ and $\tilde N$ are \emph{tangent up to order $k = 0, 1, \ldots, \infty$ at $p$} if
\[
\frac{\partial^{|I|} f^\alpha}{\partial x^I} (p) = \frac{\partial^{|I|} \tilde f{}^\alpha}{\partial x^I} (p),\quad \text{for all multiindexes $I$ with $|I| \leq k$},
\]
and we write $N \sim_p^k \tilde N$. Tangency up to order $k$ at $p$ is a well-defined equivalence relation on submanifolds through $p$. In particular, it is independent of the choice of adapted coordinates. The equivalence class of $N$ is denoted $N^k_p$ and called the \emph{$k$-jet of $N$ at $p$}.   In other words,   $k$-jets at $p$ encode partial derivatives of $n$-dimensional submanifolds at $p$ up to order $k$. The space of tangency classes is denoted $J^k_p (P, n)$. Finally put
\[
J^k (P, n) = \coprod_{p \in P} J^k_p (P,n).
\] 
We call $J^k (P, n)$ the \emph{$k$-jet space of $n$-dimensional submanifolds of $P$}. It is clear that $J^0 (P, n)$ identifies naturally with $P$ and $J^1 (P, n)$ identify with the bundle of $n$-Grassmannians in the fibers of the tangent bundle $TP$. More precisely, the $0$-jet of $N$ at $p$ identifies with $p$ itself, while the $1$-jet of $N$ at $p$ identifies with the tangent space $T_p N$. For a general $k$, the space $J^k (P, n)$ can be coordinatized as follows. Choose coordinates $(x^i, u^\alpha)$ on $P$, and let $U \subseteq J^k (P, n)$ be the subset consisting of $k$-jets of submanifolds for which $(x^i, u^\alpha)$ are adapted coordinates. We define coordinates  $(x^i, u^\alpha_I)$ on $U$ by putting
\[
x^i \big( N^k_p \big) := x^i (p), \quad \text{and} \quad u^\alpha_I \big(N^k_p\big) = \frac{\partial^{|I|} f^\alpha}{\partial x^I} (p),
\]
for all $N$ locally given by (\ref{eq:N_loc}), $i = 1, \ldots, n$, $\alpha = 1, \ldots, m$, and $|I| \leq k$. The $(x^i, u^\alpha)$ are called \emph{jet coordinates}, they cover $J^k (P, n)$ and, for $k < \infty$, they give to $J^k (P, n)$ the structure of a smooth manifold. For all $h \leq k \leq \infty$ the are projections
\[
J^k (P, n) \to J^h (P, n), \quad N^k_p \mapsto N^h_p,
\]
and by Borel Lemma $J^\infty (P, n)$ identifies with the inverse limit of the tower of surjective submersions
\[
J^0 (P, n)  \longleftarrow \cdots \longleftarrow J^{k-1} (P, n) \longleftarrow J^k (P,n) \longleftarrow \cdots.
\]

This gives to the $\infty$-jet space the structure of a pro-finite dimensional manifold (see, e.g., \cite{b...99,v01}, see also \cite{g17}). 

 
\begin{remark}
For the reader more familiar with jets of sections, we mention that, when $P$ is fibered over some $n$-dimensional manifold $M$, then, for all $k \leq \infty$, the space $J^k (P, M)$ of $k$-jets of sections of $P$ over $M$ can be recovered as the open and dense submanifold of $J^k (P, n)$ consisting of jets of $n$-dimensional submanifolds transverse to the projection $P \to M$. The open embedding $J^k (P, M) \hookrightarrow J^k (P, n)$ maps the $k$-jet at $x \in M$ of a (possibly local) section $s$ of $P \to M$ to the $k$-jet of its image at $s(x)$.
\end{remark}
  


Differential calculus on $J^\infty (P, n)$ can be defined algebraically. For instance, we define smooth functions $C^\infty (J^\infty (P, n))$ on $J^\infty (P,n)$ as the direct limit of the algebra filtration
\begin{equation}\label{eq:filt_C}
C^\infty \big(J^0 (P, n)\big) \hookrightarrow \cdots \hookrightarrow C^\infty \big(J^{k-1} (P, n)\big) \hookrightarrow C^\infty \big(J^k (P, n)\big) \hookrightarrow \cdots.
\end{equation}
In other words a smooth function on $J^\infty (P, n)$ is a smooth function of the independent variables $x^i$, the dependent variables $u^\alpha$, and their derivatives up to some finite order $k$, but $k$ can be arbitrarily high (sometimes they are defined as functions which are only locally of this type). Vector fields, differential forms, etc., on $J^\infty (P, n)$ are defined in a way compatible with the filtration (\ref{eq:filt_C}). We will not insist on these technicalities and we refer to \cite{b...99} for details.

\begin{remark}\label{rem:infty_dim}
We stress that, in this $\infty$-dimensional setting, some important results in finite dimensional differential geometry might fail. To mention a few: the inverse function theorem, existence and uniqueness of the flow of a vector field, the Frobenius theorem, etc.
\end{remark}

Any $n$-dimensional submanifold $N \subseteq P$ defines a new $n$-dimensional submanifold
\[
N^k :=\left\{ N^k_p : p \in N \right\}
\]
in $J^k (P, n)$, called the \emph{$k$-jet prolongation} of $N$. If $N$ locally looks like (\ref{eq:N_loc}) in coordinates, then $N^k$ locally looks like
\[
N^k :  u^\alpha_I = \frac{\partial^{|I|} f^\alpha}{\partial x^I} (x), \quad |I| \leq k,
\]
in jet coordinates.

\begin{remark}\label{rem:emb_N}
Let $N \subseteq P$ be an $n$-dimensional submanifold. For all $k \leq \infty$, the map
\[
j^k : N \to N^k, \quad p \mapsto N^k_p
\]
is a diffeomorphism. In particular $N$ embeds into $J^k (P, n)$ for all $k$.  
When $P$ is fibered over some $n$-dimensional manifold $M$, and $s : M \to P$ is a (possibly local) section of $P$ over $N$, then the usual $k$-jet prolongation $j^k s$ of $s$ can be recovered as the composition
\[
j^k s : M \overset{s}{\longrightarrow} \operatorname{im} s \overset{j^k}{\longrightarrow} (\operatorname{im} s)^k \hookrightarrow J^k (P, M).
\]
  
\end{remark}

\begin{remark}\label{rem:jet_emb}
Let $r$ be a non-negative integer and let $Q \subseteq P$ be an $(n+r)$-dimensional submanifold. Then, for all $k \geq 0$, the $k$-jet space $J^k (Q, n)$ is a submanifold in the $k$-jet space $J^k (P, n)$ in the obvious natural way.
\end{remark}
