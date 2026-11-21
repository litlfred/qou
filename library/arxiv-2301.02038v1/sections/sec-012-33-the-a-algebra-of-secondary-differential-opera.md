---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-012-33-the-a-algebra-of-secondary-differential-opera
section_title: "the A-algebra of secondary differential operators"
section_number: 3.3
pages: 22-25
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.965
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
In this final subsection we discuss \emph{secondary scalar differential operators}. In order to define them we follow the recipe presented at the end of Section \ref{Sec:Homol}. Let $(\mathscr E, \mathscr C)$ be a diffiety. The construction $\Phi$ for which we want to find a replacement on the space of solutions of $\mathscr E_0$ is ``\emph{scalar differential operators}'', i.e.{} linear differential operators from functions to functions (just DOs, for simplicity, in what follows).

For Step (1) in our recipe, we have to define \emph{transverse DOs}. Intuitively, they should be DOs taking derivatives just in the direction transverse to $\mathscr C$. Begin with the (non-commutative) $\mathbb R$-algebra $DO (\mathscr E)$ of DOs
\[
\Delta : C^\infty (\mathscr E) \to C^\infty (\mathscr E)
\]
on $\mathscr E$. As vector fields are DOs (of order $1$), sections of $\mathscr C$ span a right ideal $\Gamma (\mathscr C) \cdot DO(\mathscr E)$ in $DO (\mathscr E)$. Denote
\[
\mathscr VDO := \frac{DO(\mathscr E)}{\Gamma (\mathscr C) \cdot DO(\mathscr E)}
\] 
the quotient left $DO(\mathscr E)$-module. By definition, $\mathscr V DO$ is the space of \emph{transverse DOs}.

For Step (2) in the recipe, we have to notice that $\mathscr V DO$ is equipped with an action of the Lie algebroid $\mathscr C$. This is indeed the case: left composition with a section of $\mathscr C$ is indeed such action. Accordingly, the $\overline \Omega{}^\bullet (\mathscr E)$-module
\[
\overline \Omega{}^\bullet (\mathscr E, \mathscr V DO) := \overline \Omega{}^\bullet (\mathscr E) \otimes \mathscr V DO
\]
is a DG $(\overline \Omega{}^\bullet (\mathscr E), \overline d)$-module, whose differential we denote again by $\overline d$.

In Step (3) we define \emph{secondary differential operators} as the cohomology of $(\Omega{}^\bullet (\mathscr E, \mathscr V DO), \overline d)$:
\[
\boldsymbol{DO} := H^\bullet \big( \overline \Omega (\mathscr E, \mathscr V DO), \overline d \big).
\]

For Step (4) we have to show that $\boldsymbol{DO}$ is equipped with the appropriate algebraic structure for DOs. Actually, we can show that $\boldsymbol{DO}$ is a graded associative algebra (notice that, on the contrary, $\overline \Omega{}^\bullet (\mathscr E, \mathscr V DO)$ is not a DG algebra in general, as it does not possess a natural associative product). To do this, it is a good idea to perform simultaneously Step (5) of the recipe (see the end of the previous subsection). The relevant homotopy algebras here are \emph{$A_\infty$-algebras}.

\begin{definition}
An \emph{$A_\infty$-algebra} \cite{ls93, lm95} is a graded vector space $U$ equipped with a sequence $\mathfrak a = \{\mathfrak a_k\}_{k \in \mathbb N}$ of degree $1$ multilinear maps:
\[
\mathfrak a_k : \big(\textstyle\bigotimes^k U\big){}^\bullet \to U^{\bullet + 1}, \quad (u_1, \ldots, u_k) \mapsto \mathfrak a_k (u_1, \ldots, u_k)
\]
satisfying the following \emph{higher associativity conditions}:
\[
\sum_{r+s = k} \sum_{j=1}^{r+s}(-)^{|u_1| + \cdots + |u_j|} \mathfrak a_{s+1}\big(u_1, \ldots, u_j, \mathfrak a_{s} (u_{j+1}, \ldots, u_{j + r}), u_{j+r+1}, \ldots, u_{r+s}\big) = 0
\]
for all $k \in \mathbb N$, and all $u_1, \ldots, u_k \in U$.
\end{definition}

It follows from the above definition that $\mathfrak a_1$ is a differential, and it is a derivation with respect to $\mathfrak a_2$. Moreover $\mathfrak a_2$ is associative up to a homotopy encoded by $\mathfrak a_3$. In particular $\mathfrak a_2$ induces a honest associative product in cohomology $H^\bullet (U, \mathfrak a_1)$ (up to d\'ecalage).

\begin{theorem}\label{theor:DO_sec}
The graded vector space $\Omega{}^\bullet (\mathscr E, \mathscr V DO)[1]$ can be equipped with an $A_\infty$-algebra structure $\mathfrak a$ such that $\mathfrak a_1 = \overline d$. Moreover, the induced associative product in the cohomology $\boldsymbol{DO}$ is canonical.
\end{theorem}

The above theorem supports the interpretation of $\boldsymbol{DO}$ as \emph{secondary DOs}, i.e.{} (an appropriate replacement for) DOs on the space of solutions of $\mathscr E_0$.

We conclude the paper by sketching the proof of Theorem \ref{theor:DO_sec}. As we will see, the proof will also suggest an alternative \emph{Secondarization Recipe}. From now on we assume some familiarity with graded geometry (see, e.g., \cite{M2006}). We begin recalling a standard technique in homotopical algebra, namely the \emph{Homotopy Transfer} (see \cite{lv12, v14}). The idea is that homotopy algebras can be transferred along contraction data. A \emph{set of contraction data} is a diagram
\begin{equation}\label{eq:contr}
\xymatrix{     *{ \quad \quad \quad(A, \delta_A)\ }
\ar@(dl,ul)[]^-{h}\
\ar@<0.5ex>[r]^-{p} & *{\
(B,\delta_B)\quad\ \  \ \quad}  \ar@<0.5ex>[l]^-{j}}
\end{equation}
where 
\begin{enumerate}
\item $(A, \delta_A)$ and $(B, \delta_B)$ are cochain complexes,
\item $p, j$ are cochain maps,
\item $h : A^\bullet \to A^{\bullet -1}$ is a homotopy,
\end{enumerate}
such that
\[
pj = \operatorname{id}_B \quad \text{and} \quad jp = [\delta_A, h]
\]
and, moreover, the following \emph{side conditions} are satisfied:
\[
ph = hj = h^2 = 0.
\]
In particular $p, j$ are mutually homotopy inverse homotopy equivalences and
\[
H^\bullet(A, \delta_A) \cong H^\bullet (B, \delta_B).
\]

\begin{theorem}[Homotopy Transfer]
Let $(A, \delta_A)$ be an associative DG algebra and let (\ref{eq:contr}) be a set of contraction data over a cochain complex $(B, \delta_B)$. Then $B[1]$ can be equipped with an $A_\infty$-algebra structure $\mathfrak a$, uniquely determined by the associative product in $A$ and the contraction data, such that $\mathfrak a_1 = \delta_B$. Moreover $(A, \delta_A)$ and $(B, \mathfrak a)$ induce the same graded associative algebra structure in cohomology $H^\bullet(A, \delta_A) \cong H^\bullet (B, \delta_B)$.
\end{theorem}

There is a version of the Homotopy Transfer Theorem for $L_\infty$-algebras \cite{h10, v14} and one, slightly more involved, for $LR_\infty$-algebras (see \cite{v12} for details). Actually the $LR_\infty$-algebra of Theorem \ref{theor:LR} can be obtained via Homotopy Transfer. Namely, let $(\mathscr E, \mathscr C)$ be a diffiety. Consider the DG manifold $\mathscr C [1]$ obtained by the Lie algebroid $\mathscr C \to \mathscr E$ by shifting by one the fiber degree. Clearly $C^\infty (\mathscr C [1]) = \overline \Omega{}^\bullet (\mathscr E)$ and the cohomological vector field on $\mathscr C[1]$ is the horizontal De Rham differential $\overline d$. The pair $\big(C^\infty (\mathscr C[1]), \mathfrak X (\mathscr C[1])\big)$ is a DG Lie-Rinehart algebra. The differential in $\mathfrak X (\mathscr C[1])$ is the graded commutator of graded vector fields with the horizontal De Rham differential. Moreover, a splitting (\ref{eq:split}) uniquely determines contraction data
\begin{equation}
\xymatrix{     *{ \quad \quad \quad \mathfrak X (\mathscr C[1]) \ }
\ar@(dl,ul)[]^-{h}\
\ar@<0.5ex>[r]^-{p} & *{\ \,
\overline \Omega{}^\bullet (\mathscr E, \mathscr V) \quad\ \  \ \quad}  \ar@<0.5ex>[l]^-{j}}
\end{equation}
that we can use to construct an $LR_\infty$-algebra structure on $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)[1]$ from the DG Lie-Rinehart algebra structure on $(C^\infty (\mathscr C[1]), \mathfrak X (\mathscr C[1]))$ (see \cite{v12} for details). This means that the Lie-Rinehart algebra structure on secondary vector fields $(\boldsymbol{C}^\infty, \boldsymbol{\mathfrak X})$ is, equivalently, the one induced in cohomology by the DG Lie-Rinehart algebra $(C^\infty (\mathscr C[1]), \mathfrak X (\mathscr C[1]))$. A similar result holds for secondary DOs. Namely, consider the space $DO(\mathscr C[1])$ of graded DOs over the DG manifold $\mathscr C[1]$. It is an associative DG algebra whose differential is the graded commutator of graded DOs with the horizontal De Rham differential. Now, a splitting (\ref{eq:split}), together with certain additional data that we will not describe, uniquely determine contraction data
\begin{equation}
\xymatrix{     *{ \quad \quad \quad \quad DO \big(\mathscr C[1]\big) \ }
\ar@(dl,ul)[]^-{h}\
\ar@<0.5ex>[r]^-{p} & *{\ \,
\overline \Omega{}^\bullet (\mathscr E, \mathscr V DO) \quad\ \  \ \quad}  \ar@<0.5ex>[l]^-{j}}
\end{equation}
that we can use to construct an $A_\infty$-algebra structure on  $\overline \Omega{}^\bullet (\mathscr E, \mathscr V DO)[1]$ from the associative DG algebra structure on $DO(\mathscr C[1])$. In particular there is a graded associative algebra structure on secondary differential operators
\[
\boldsymbol{DO} = H^\bullet \big(\overline \Omega (\mathscr E, \mathscr V DO), \overline d\big) \cong H^\bullet \big( DO (\mathscr C[1]) \big)
\]
induced by either the associative DG algebra structure on $DO (\mathscr C[1])$ or the $A_\infty$-algebra structure on $\overline \Omega{}^\bullet (\mathscr E, \mathscr V DO)$.

This discussion suggests the following alternative recipe to find the secondary analogue of a given construction $\Phi$ in differential geometry.

\begin{recipe}\quad
\begin{enumerate}
\item Apply the construction $\Phi$ to the DG manifold $\mathscr C[1]$ (when $\Phi$ is ``vector fields'', resp.{} ``DO'' we get $\mathfrak X (\mathscr C[1])$, resp.{} $DO (\mathscr C[1])$).
\item Notice that $\Phi (\mathscr C[1])$ is canonically equipped with a differential induced by the cohomological vector field $\overline d$ on $\mathscr C[1]$ (when $\Phi$ is ``vector fields'', resp.{} ``DOs'', such differential is the graded commutator of vector fields, resp.{} DOs, with $\overline d$).
\item Define $\boldsymbol{\Phi}$ as the cohomology of $\Phi (\mathscr C[1])$ (when $\Phi$ is ``vector fields'', resp. ``DOs'', then $\boldsymbol \Phi$ is $\boldsymbol{\mathfrak X}$, resp.{} $\boldsymbol{DO}$).
\item Notice that, being compatible with the differential, the algebraic structure on $\Phi (\mathscr C[1])$ induces the same algebraic structure on $\boldsymbol{\Phi}$ (when $\Phi$ is ``vector fields'', resp.{} ``DOs'', then $\boldsymbol \Phi = \boldsymbol{\mathfrak X}$, resp.{} $\boldsymbol \Phi = \boldsymbol{DO}$, is a graded Lie-Rinehart algebra, resp.{} a graded associative algebra).
\end{enumerate}
\end{recipe}

 
\begin{remark}
Notice that, in the alternative Secondarization Recipe just above there is no analogue of the Addendum (5) at p.~\pageref{addendum}. The reason is that the cochain complex $\Phi (\mathscr C[1])$ does possess the same (honest) algebraic structure as $\Phi$ by definition, and there is no need to work with algebraic structures up to homotopy at the level of cochains in this case. Nonetheless, by the Homotopy Transfer Theorem, cohomologies possess algebraic structures of the same type but only up to homotopy. Moreover, cohomologies with their algebraic structures up to homotopy are quasi-isomorphic to cochains with their algebraic structures. In other words, one can either choose to work with a larger space (cochains) and a simpler algebraic structure, or with a smaller space (cohomologies) and a more complicated algebraic structure (algebraic structure up to homotopy).
\end{remark}
