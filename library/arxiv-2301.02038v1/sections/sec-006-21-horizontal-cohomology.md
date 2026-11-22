---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-006-21-horizontal-cohomology
section_title: "horizontal cohomology"
section_number: 2.1
pages: 10-12
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.916
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
\label{Sec:hor_cohom}
In this section we attach a cochain complex to every diffiety $(\mathscr E, \mathscr C)$. The associated cohomology is called the \emph{horizontal cohomology} of $\mathscr E$ and it contains important coordinate free information on $\mathscr E_0$.

Let $(\mathscr E, \mathscr C)$ be a diffiety.  By involutivity, the vector subbundle $\mathscr C \to \mathscr E$ of the tangent bundle $T \mathscr E$ is actually a Lie algebroid. Accordingly, there is an associated Cartan calculus. There are also associated De Rham cohomologies (with coefficients). Specifically,    denote by
\[
\overline \Omega{}^\bullet (\mathscr E) := \Gamma (\wedge^\bullet \mathscr C^\ast)
\]
the exterior algebra of the dual of $\mathscr C$. In other words, $\overline \Omega{}^\bullet (\mathscr E)$ consists of differential forms on $\mathscr E$ acting on vector fields in $\mathscr C$. Elements in $\overline \Omega{}^\bullet (\mathscr E)$ are called \emph{horizontal differential forms}. There is a canonical differential $\overline d : \overline \Omega{}^\bullet (\mathscr E) \to \overline \Omega{}^{\bullet +1} (\mathscr E)$, the \emph{horizontal De Rham differential}, defined by the usual Chevalley-Eilenberg formula: for all $\overline \omega \in \overline \Omega{}^q (\mathscr E)$,
\[
\begin{aligned}
& \overline d \overline \omega (X_1, \ldots, X_{q+1}) \\
& = \sum_{i = 1}^{q+1} (-)^{i+1}X_i \left( \overline \omega (X_1, \ldots \widehat{X_i}, \ldots, X_{q+1})\right) \\
& \quad + \sum_{i < j} (-)^{i+j}\overline \omega  \left( [X_i, X_j], \ldots, \widehat{X_i}, \ldots, \widehat{X_j}, \ldots \right), \quad X_1, \ldots, X_{q+1} \in \Gamma (\mathscr C),
\end{aligned}
\]
where a hat denotes omission. The pair $(\overline \Omega{}^\bullet (\mathscr E), \overline d)$ is a commutative differential graded (DG) algebra called the \emph{horizontal De Rham algebra} of $\mathscr E$. Its cohomology is called the \emph{horizontal De Rham cohomology} and denoted $\overline H{}^\bullet (\mathscr E)$. Locally, $\overline \Omega{}^\bullet (\mathscr E)$ is generated, as a graded algebra, by functions and by the \emph{coordinate horizontal $1$-forms}
\[
\overline d x^1, \ldots, \overline d x^n.
\]
In particular, there are no non-trivial horizontal forms of degree higher than $n$, the number of independent variables. In coordinates the horizontal De Rham differential acts as follows:
\[
\overline d \left( f_{i_1 \ldots i_q} \overline d x^{i_1} \wedge \cdots \wedge \overline d x^{i_q} \right) = \left(D_i |_{\mathscr E} f_{i_1 \ldots i_q}\right) \overline d x^i \wedge \overline d x^{i_1} \wedge \cdots \wedge \overline d x^{i_q}.
\]
Notice that the horizontal cohomology is a variant of the standard leaf-wise cohomology of a foliation in our (generically) $\infty$-dimensional setting.

There are various natural DG modules over $(\overline \Omega{}^\bullet (\mathscr E), \overline d)$ coming from standard representations of the Lie algebroid $\mathscr C$. In this subsection we present two of such representations while a third one will be discussed in Section \ref{Sec:Homot}. Denote by
\[
\mathscr V := T\mathscr E / \mathscr C
\]
the \emph{normal bundle} to $\mathscr E$. We will refer to $\mathscr V$ as the \emph{transverse tangent bundle} of $\mathscr E$, and sections of $\mathscr V$ are \emph{transverse vector fileds} (the word ``transverse'' refers to transversality with respect to $\mathscr C$). So, there is a short exact sequence of vector bundles
\begin{equation}\label{eq:SES_C}
0 \longrightarrow \mathscr C \longrightarrow T\mathscr E \longrightarrow \mathscr V \longrightarrow 0.
\end{equation}
The Lie algebroid $\mathscr C$ acts on $\mathscr V$ via the \emph{Bott connection} $\nabla$:
\[
\nabla_X \big(Y \operatorname{mod} \Gamma (\mathscr C) \big) = [X, Y] \operatorname{mod} \Gamma (\mathscr C), \quad \text{for all $X \in \Gamma (\mathscr C)$ and all $Y \in \mathfrak X (\mathscr E)$}.
\]
Accordingly, the graded vector space
\[
\overline \Omega{}^{\bullet} (\mathscr E, \mathscr V) := \Gamma \big(\wedge^\bullet \mathscr C^\ast \otimes \mathscr V\big) \cong \overline \Omega{}^{\bullet} (\mathscr E) \otimes \Gamma (\mathscr V),
\]
is a DG $(\overline \Omega{}^{\bullet} (\mathscr E), \overline d)$-module with differential, denoted 
\[
\overline d : \overline \Omega{}^{\bullet} (\mathscr E, \mathscr V) \to \overline \Omega{}^{\bullet +1 } (\mathscr E, \mathscr V)
\]
as well, given by: for all $\overline W \in \overline \Omega{}^{q} (\mathscr E, \mathscr V)$,
\[
\begin{aligned}
& \overline d\, \overline W (X_1, \ldots, X_{q+1}) \\
& = \sum_{i = 1}^{q+1} (-)^{i+1}\nabla_{X_i} \left( \overline W (X_1, \ldots \widehat{X_i}, \ldots, X_{q+1})\right) \\
& \quad + \sum_{i < j} (-)^{i+j}\overline W  \left( [X_i, X_j], \ldots, \widehat{X_i}, \ldots, \widehat{X_j}, \ldots \right), \quad X_1, \ldots, X_{q+1} \in \Gamma (\mathscr C).
\end{aligned}
\]
The cohomology of the DG module $(\overline \Omega{}^{\bullet} (\mathscr E, \mathscr V), \overline d)$ is denoted $\overline H{}^\bullet (\mathscr E, \mathscr V)$.

Dually to (\ref{eq:SES_C}) there is a short exact sequence of DG algebras
\[
0 \longleftarrow \big(\overline \Omega{}^\bullet (\mathscr E), \overline d\big) \longleftarrow \big( \Omega^\bullet (\mathscr E), d\big) \longleftarrow \big(\mathscr C \Omega^\bullet, d\big) \longleftarrow 0.
\]
Here the projection $\Omega^\bullet (\mathscr E) \to \overline \Omega{}^\bullet (\mathscr E)$ is just the restriction to vector fields in $\mathscr C$, and $\mathscr C \Omega^\bullet$ is its kernel: the $d$-closed graded ideal of forms vanishing when restricted to vector fields in $\mathscr C$. We also denote
\[
\mathscr V \Omega^\bullet = \Gamma (\wedge^\bullet \mathscr V^\ast).
\]
It is a graded subalgebra in $\Omega^\bullet (\mathscr E)$: the graded subalgebra generated by $C^\infty (\mathscr E)$ and $\mathscr C \Omega^1$. We will refer to elements in $\mathscr V \Omega^\bullet$ as \emph{transverse differential forms} on $\mathscr E$. The Lie algebroid $\mathscr C$ acts on $\wedge^\bullet \mathscr V^\ast$ via the \emph{dual Bott connection}, also denoted $\nabla$:
\[
\nabla_X \varpi := \mathcal L_X \varpi, \quad \text{for all $X \in \Gamma (\mathscr C)$ and all $\varpi \in \mathscr V \Omega^\bullet$}.
\]
Accordingly, the graded vector space
\[
\overline \Omega{}^{\bullet} (\mathscr E, \wedge^\bullet \mathscr V^\ast) := \Gamma \big(\wedge^\bullet \mathscr C^\ast \otimes \wedge^\bullet \mathscr V^\ast\big) \cong \overline \Omega{}^{\bullet} (\mathscr E) \otimes \mathscr V^\bullet \Omega,
\]
is also a DG $(\overline \Omega{}^{\bullet} (\mathscr E), \overline d)$-module with differential, denoted 
\[
\overline d : \overline \Omega{}^{\bullet} (\mathscr E, \wedge^\bullet \mathscr V^\ast) \to \overline \Omega{}^{\bullet +1 } (\mathscr E, \wedge^\bullet \mathscr V^\ast),
\]
 given by the usual Chevalley-Eilenberg formula again. The cohomology of the DG module $(\overline \Omega{}^{\bullet} (\mathscr E, \wedge^\bullet \mathscr V^\ast), \overline d)$ is denoted $\overline H{}^\bullet (\mathscr E, \wedge^\bullet \mathscr V^\ast)$.
