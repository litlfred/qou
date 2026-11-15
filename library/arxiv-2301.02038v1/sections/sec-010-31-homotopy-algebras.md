---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-010-31-homotopy-algebras
section_title: "homotopy algebras"
section_number: 3.1
pages: 18-20
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.928
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
In this subsection, we recall the definitions of those homotopy algebras that we will need in the rest of the paper. Roughly, a homotopy algebra of a certain type (associative, Lie, etc.) is a graded vector space equipped with operations satisfying the algebra axioms only up to a coherent system of \emph{higher homotopies}. Homotopy algebras appear when cohomology and homotopy interact with algebraic structures \cite{lv12, v14}. We adopt the degree $1$ convention on the operations of a homotopy algebra, and we only work with (graded) vector spaces over a field of zero characteristic.

\begin{definition}
An \emph{$L_\infty$-algebra} \cite{ls93, lm95} is a graded vector space $V$ equipped with a sequence $\mathfrak l = \{ \mathfrak l_k \}_{k \in \mathbb N}$ of degree $1$ symmetric multilinear brackets:
\[
\mathfrak l_k : \left(S^k V\right){}^\bullet \to V^{\bullet +1}, \quad (v_1, \ldots, v_{k}) \mapsto \mathfrak l_k (v_1, \ldots, v_{k})
\]
satisfying the following \emph{higher Jacobi identities}:
\begin{equation}\label{eq:high_Jac}
\sum_{r+s = k} \sum_{\sigma \in S_{r, s}}\epsilon (\sigma , v) \mathfrak l_{s+1} \big(\mathfrak l_r (v_{\sigma(1)}, \ldots, v_{\sigma(r)}), v_{\sigma (r+1)}, \ldots, v_{\sigma (r+s)}\big) = 0,
\end{equation}
for all $k \in \mathbb N$, where $S_{r,s}$ denotes $(r,s)$-unshuffles, and $\epsilon (\sigma, v)$ is the Koszul sign associated to the permutation $\sigma$ of the homogeneous elements $v_1, \ldots, v_k \in V$.
\end{definition}

For $k = 1$ the identity (\ref{eq:high_Jac}) says that $\mathfrak l_1 : V^\bullet \to V^{\bullet +1}$ is a differential. In particular there is a cohomology $H^\bullet (V, \mathfrak l_1)$ for every $L_\infty$-algebra $(V , \mathfrak l)$. For $k = 2$ the identity (\ref{eq:high_Jac}) says that $\mathfrak l_1$ is a derivation with respect to the binary bracket $\mathfrak l_2 : (S^2 V)^\bullet \to V^{\bullet +1}$. For $k = 3$ the identity (\ref{eq:high_Jac}) says that $\mathfrak l_2$ is a graded Lie bracket only up to a homotopy encoded by $\mathfrak l_3$. In particular $\mathfrak l_2$ induces a honest graded Lie bracket in cohomology $H^\bullet (V, \mathfrak l_1)$ (up to a d\'ecalage isomorphism that we will ignore, for simplicity). So, whenever the cohomology of a cochain complex supports a graded Lie bracket, it is natural to wonder whether or not it comes from an $L_\infty$-algebra structure on cochains.

There is also a notion of $L_\infty$-module over an $L_\infty$-algebra.

\begin{definition}
An \emph{$L_\infty$-module} \cite{lm95} over an $L_\infty$-algebra $(V, \mathfrak l)$ is a graded vector space $W$ equipped with a sequence $\mathfrak m = \{ \mathfrak m_k \}_{k \in \mathbb N}$ of degree $1$ multilinear brackets:
\[
\mathfrak m_k : \left(S^{k-1} V \otimes W \right){}^\bullet \to W^{\bullet + 1}, \quad (v_1, \ldots, v_{k-1}, w) \mapsto \mathfrak m_k (v_1, \ldots, v_{k-1}| w)
\]
satisfying:
\[
\begin{aligned}
& \sum_{r+s = k-1} \sum_{\sigma \in S_{r, s}}\epsilon (\sigma , v) \Big[\mathfrak m_{s+1} \big(\mathfrak l_r (v_{\sigma(1)}, \ldots, v_{\sigma(r)}), v_{\sigma (r+1)}, \ldots, v_{\sigma (r+s)}| w \big)  \\
& + (-)^{|v_{\sigma(1)}| + \cdots +|v_{\sigma(r)}|} \mathfrak m_{r+1} \big( v_{\sigma (1)}, \ldots, v_{\sigma (r)}| \mathfrak m_s (v_{\sigma(r+1)}, \ldots, v_{\sigma(r+s)}|w)\big) \Big]= 0
\end{aligned}
\]
for all $k \in \mathbb N$, $v_1, \ldots, v_{k-1} \in V$, $w \in W$.
\end{definition}

In particular $\mathfrak m_1 : W^\bullet \to W^{\bullet +1}$ is a differential and $\mathfrak m_2$ induces a honest graded $H^\bullet (V, \mathfrak l_1)$-module structure on $H^\bullet (W, \mathfrak m_1)$.

The next definition is a homotopy version of the notion of Lie-Rinehart algebra (see \cite{k01, k01b, h05, h13, vi12, v15}).

\begin{definition}
An \emph{$LR_\infty$-algebra} \cite{vi12} (\emph{LR} for Lie-Rinehart) is a pair $(A, L)$ consisting of two graded vector spaces equipped with the following additional structures:
\begin{enumerate}
\item $L$ is an $L_\infty$-algebra with structure maps $\mathfrak l$;
\item $A$ is a commutative DG algebra with differential denoted $\mathfrak m_1$;
\item $(L, \mathfrak l_1)$ is a DG $(A^\bullet, \mathfrak m_1)$-module;
\item $A$ is an $L_\infty$-module over $(L^\bullet, \mathfrak l)$ with structure maps $\mathfrak m$ (this means that the $1$-ary bracket is precisely $\mathfrak m_1$).
\end{enumerate} 
Additionally, the maps
\[
\mathfrak m_k : \left(S^{k-1} L \otimes A \right){}^\bullet \to A^{\bullet + 1}
\]
are graded $A$-multilinear in the first $(k-1)$-arguments and they are a derivation in the last argument. Finally the $L_\infty$-algebra brackets $\mathfrak l$ satisfy the following \emph{Leibniz rule}:
\[
\begin{aligned}
&\mathfrak l_k (v_1, \ldots, v_{k-1}, a v_k) \\
& = \mathfrak m_{k} (v_1, \ldots, v_{k-1}|a) v_k + (-)^{|a| \left(|v_1| + \cdots + |v_{k-1}| + 1 \right)}a \mathfrak l_k (v_1, \ldots, v_{k-1}, v_k),
\end{aligned}
\]
for all $v_1, \ldots, v_k \in L$, and $a \in A$.
\end{definition}

\begin{remark}\label{rem:LR_cohom}
Let $(A, L)$ be an $LR_\infty$-algebra with structure maps $(\mathfrak m, \mathfrak l)$. Similarly as for $L_\infty$-algebras and $L_\infty$-modules, the cohomology $(H^\bullet (A, \mathfrak m_1), H^\bullet (L, \mathfrak l_1))$ is then a graded Lie-Rinehart algebra.
\end{remark}

As for Lie algebroids, there is a \emph{Chevalley-Eilenberg construction} for $LR_\infty$-algebras. Namely, let $(A, L)$ be an $LR_\infty$-algebra. Consider the graded commutative algebra $\operatorname{Sym}^\bullet(A, L)$ consisting of graded symmetric $A$-multilinear maps
\[
S^\bullet L \to A.
\]
The structure maps $(\mathfrak l, \mathfrak m)$ of $(A, L)$ induce on $\operatorname{Sym}^\bullet (A, L)$ a sequence $\mathfrak d = \{ \mathfrak d_k\}$ of degree $1$ derivations:
\begin{equation}\label{eq:d_Sym}
\mathfrak d_k : \operatorname{Sym}^h (A, L) \to \operatorname{Sym}^{k+h-1} (A, L)
\end{equation}
given by
\[
\begin{aligned}
&\mathfrak d_k \omega (v_1, \ldots, v_{h}) \\
& = \sum_{\sigma \in S_{k-1,h}} \epsilon(\sigma, v) (-)^{|\omega| \sum_{i = 1}^{k-1}|v_{\sigma(i)}|}
\mathfrak m_k \big(v_{\sigma(1)}, \ldots, v_{\sigma(k-1)}|\omega (v_{\sigma (k)}, \ldots, v_{\sigma (k+h-1)})\big) \\
& \quad + \sum_{\sigma \in S_{k, h-1}} \epsilon(\sigma, v) \omega \big(\mathfrak l_k (v_{\sigma(1)}, \ldots, v_{\sigma (k)}), v_{\sigma (k+1)}, \ldots, v_{\sigma (k+h-1)}\big).
\end{aligned}
\]

\begin{proposition}
The maps $\mathfrak d_k$ are well-defined degree $1$ derivations of the graded algebra $\operatorname{Sym}^\bullet(A, L)$. Additionally they satisfy
\begin{equation}\label{eq:d_d}
\sum_{r+s = k} \big[\mathfrak d_r, \mathfrak d_s \big] = 0
\end{equation}
for all $k \in \mathbb N$. In particular the total derivation
\[
\mathfrak D := \mathfrak d_1 + \mathfrak d_2 + \cdots
\]
squares to zero, whenever defined. 
\end{proposition}

The pair $(\operatorname{Sym}^\bullet(A, L), \mathfrak d)$ is called the \emph{Chevalley-Eilenberg} algebra of $(A, L)$.

\begin{remark}\label{rem:DGA_cohom}
The derivation $\mathfrak d_2$ does not square to $0$ in general (it does only up to a homotopy encoded by $\mathfrak d_3$), however it induces a derivation which squares to zero in the cohomology of $\mathfrak d_1$. Hence 
$
H^\bullet \left( \operatorname{Sym}(A, L), \frak d_1\right)
$, with the derivation induced by $\mathfrak d_2$, is a commutative DG algebra.
\end{remark}

\begin{remark}
Let $(A, L)$ be an $LR_\infty$-algebra. If $L$ is projective and finitely generated as an $A$-module, then the Chevalley-Eilenberg algebra knows everything about $(A, L)$. More precisely, let $A$ be a commutative graded algebra and let $L$ be a projective and finitely generated graded $A$-module. Then the Chevalley-Eilenberg construction establishes a bijection between $LR_\infty$-algebra structures on $(A, L)$ extending the preexisting structures on one side, and sequences $\mathfrak d = \{ \mathfrak d_k\}$ of degree $1$ derivations of $\operatorname{Sym}^\bullet(A, L)$ satisfying both (\ref{eq:d_Sym}) and (\ref{eq:d_d}) on the other side.
\end{remark}
