---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-007-22-interpreting-horizontal-cohomologies
section_title: "interpreting horizontal cohomologies"
section_number: 2.2
pages: 12-15
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.959
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
Some of the horizontal cohomologies have nice interpretations, sometimes informal, sometimes more precise. In this subsection we illustrate some of them. We begin with horizontal cohomology with trivial coefficients.

\begin{example}[Constrained Variational Principles]\label{exmpl:var_prin}
Top horizontal cohomologies with trivial coefficients $\overline H{}^n (\mathscr E)$ can be (informally) interpreted as \emph{variational principles} constrained by the PDE $\mathscr E_0$. To see this, consider a cohomology class $[L] \in \overline H{}^n (\mathscr E)$. Locally
\[
L = \mathscr L (x, \ldots, u_I, \ldots)\, \overline{\mathrm{d}}{}^n x, \quad \text{where $\overline{\mathrm{d}}{}^n x := \overline d x^1 \wedge \cdots \wedge \overline d x^n$},
\]
for some local function $\mathscr L \in C^\infty (\mathscr E)$. Now, let $N \subseteq P$ be a compact, oriented $n$-dimensional solution of $\mathscr E$ (without boundary). We can pull-back $L$ along the embedding $j^\infty : N \to \mathscr E$. If we do so, we get a honest top form on $N$ that we can integrate using compactness and the orientation. Thus we have a well defined functional
\[
\mathbf F : N \mapsto \mathbf F [N] := \int_N j^\infty{}^\ast L.
\]
If $N$ is locally given by (\ref{eq:N_loc}) and the coordinates $x^1, \ldots, x^n$ on $N$ define the positive orientation, then $\mathbf F$ locally looks like
\begin{equation}\label{eq:F_loc}
\mathbf F [N] = \int \mathscr L \left(x, \ldots, \frac{\partial^{|I|} f}{\partial x^I}, \ldots \right) \mathrm{d}^n x.
\end{equation} 
Actually $\mathbf F$ does only depend on the cohomology class of $L$. Additionally, we see from (\ref{eq:F_loc}) that we can interpret $\mathbf F$, and hence $[L]$ as a (coordinate free version of) a variational principle with Lagrangian density $\mathscr L$, imposed on (certain) solutions of $\mathscr E_0$.
\end{example}

\begin{example}[Conservation Laws]\label{exmpl:cons_law}
Top minus $1$ horizontal cohomologies with trivial coefficients can be interpreted as \emph{conservation laws} for the PDE $\mathscr E_0$. To see this consider a cohomology class $[J] \in \overline H{}^{n-1} (\mathscr E)$. Locally
\[
J = J^i (x, \ldots, u_I, \ldots)\, \overline{\mathrm{d}}{}^{n-1} x_i,
\]
where
\[
\overline{\mathrm{d}}{}^{n-1} x_i := (-)^{i+1}\overline d x^1 \wedge \cdots \wedge \widehat{\overline d x^i} \wedge \cdots \wedge \overline d x^n,
\]
for some local functions $J^i \in C^\infty (\mathscr E)$, $i = 1, \ldots, n$. The cocycle condition $\overline d J = 0$ in local coordinates reads
\[
D_i |_{\mathscr E} J^i = 0,
\]
so $J$ can be seen as a \emph{conserved current} along solutions of $\mathscr E_0$. Now, let $N \subseteq P$ be a solution of $\mathscr E$ and let $\Sigma \subseteq N$ be a compact, oriented hypersurface (without boundary) in $N$. We can pull-back $J$ along $j^\infty : N \to \mathscr E$. If we do so, we get a honest $(n-1)$-form on $N$ that we can integrate on $\Sigma$ using compactness and the orientation. The integral
\[
\int_\Sigma j^\infty{}^\ast J
\]
does only depend on (the horizontal cohomology class $[J]$ and on) the homology class of $\Sigma$ in $N$. In this sense, it is conserved along every $N$. Summarizing, $[J]$ can be seen as the conservation law associated to the conserved current $J$. Notice that lower degree horizontal cohomologies can be similarly seen as lower degree conserved charges to be integrated on higher codimensional submanifolds. For instance the electric charge is a degree $(n-2)$ horizontal cohomology class for the Maxwell equations on a vacuous $n$-dimensional space-time.
\end{example}

\begin{example}[Infinitesimal Symmetries]\label{exmpl:inf_sym}
In this example we discuss degree $0$ horizontal cohomologies with coefficients in $\mathscr V$. The $0$-th cohomology $\overline H{}^0 (\mathscr E, \mathscr V)$ is just the kernel of the operator
\[
\overline d : \Gamma (\mathscr V) \to \overline \Omega{}^1 (\mathscr E, \mathscr V)
\]
and it consists of \emph{parallel sections} with respect to the Bott connection. It is easy to see that a section $Y \operatorname{mod} \Gamma (\mathscr C)$ of $\mathscr V$, with $Y \in \mathfrak X (\mathscr E)$, is parallel with respect to the Bott connection if and only if $Y$ is an infinitesimal symmetry of the $\mathscr E_0$. We conclude that the natural inclusion
\[
\mathfrak X_\mathscr{E} / \Gamma (\mathscr C) \to \mathfrak X (\mathscr E) / \Gamma (\mathscr C) = \Gamma (\mathscr V)
\]
establishes a bijection between non-trivial infinitesimal symmetries of $\mathscr E_0$ and the $0$-th cohomolgy $\overline H{}^0 (\mathscr E, \mathscr V)$. 

Let $Y \in \mathfrak X_{\mathscr C}$.  Remember from Remark \ref{rem:infty_dim} that the vector field $Y$ might not possess a flow. However,    when $Y$ possesses a flow, then the latter maps $n$-dimensional integral submanifolds of $\mathscr C$ to $n$-dimensional integral submanifolds. So, morally, it defines a flow on the space of solutions of $\mathscr E_0$. If two infinitesimal symmetries differ by a trivial infinitesimal symmetry then their flows (if they exist) induce the same flow on the space of solutions, because the flow of a trivial symmetry fixes every $n$-dimensional integral submanifold. We conclude that nontrivial infinitesimal symmetries can be informally seen as vector fields on the space of solutions. This remark will be relevant in the next subsection.
\end{example}

\begin{example}[Euler Lagrange Equations]\label{exmpl:ELeq}
We now discuss top horizontal cohomology with coefficients in transverse $1$-forms $\mathscr V^\ast$. We begin noticing that there is a map
\[
d^{\mathrm{sec}} : \overline H{}^n (\mathscr E) \to \overline H{}^n (\mathscr E, \mathscr V^\ast)
\]
defined as follows. Let $[L] \in \overline H{}^n (\mathscr E)$, and choose any $n$-form $\omega \in \Omega^n (\mathscr E)$ projecting to $L \in \overline \Omega{}^\bullet (\mathscr E)$ under $\Omega^\bullet (\mathscr E) \to \overline \Omega{}^\bullet (\mathscr E)$. The differential $d \omega$ belongs to the ideal $\mathscr C \Omega^\bullet$. Hence, it has the following property: the contraction
\[
i_{X_n} \cdots i_{X_1} d\omega 
\]
with any $n$ vector fields $X_1, \ldots, X_n$ in $\mathscr C$ is a transverse differential $1$-form: 
\[
i_{X_n} \cdots i_{X_1} d\omega \in \mathscr V \Omega^1 = \mathscr C \Omega^1.
\]
 Hence we have a well-defined, skew-symmetric and $C^\infty (\mathscr E)$-multilinear map
\[
\varpi : \Gamma (\mathscr C) \times \cdots \times \Gamma (\mathscr C) \to \mathscr V \Omega^1, \quad (X_1, \ldots, X_n) \mapsto i_{X_n} \cdots i_{X_1} d\omega 
\]
which we can interpret as an element in $\overline \Omega{}^n (\mathscr C, \mathscr V^\ast)$, also denoted  $\varpi$. As $dd\omega = 0$, we get $\overline d \varpi = 0$. The cohomology class $[\varpi ] \in \overline H{}^n (\mathscr E, \mathscr V^\ast)$ does only depend on the cohomology class $[L]$, and we put
\[
d^{\mathrm{sec}} [L] = [ \varpi]. 
\]
We now provide a more concrete description of the map $d^{\mathrm{sec}} : \overline H{}^n (\mathscr E) \to \overline H{}^n (\mathscr E, \mathscr V^\ast)$. For simplicity, from now on, in this example, we will only consider the case when $\mathscr E_0$ is the empty PDE $0 = 0$, hence $\mathscr E = J^\infty (P, n)$. For the sake of brevity, we denote $J^\infty = J^\infty (P, n)$. When $\mathscr E = J^\infty$, there is a simple description of $\overline H{}^n (\mathscr E, \mathscr V^\ast)$. Namely, there is a vector space isomorphism
\[
\Gamma \big(V^\ast \otimes \wedge^n \mathscr C^\ast \big) \cong \overline H{}^n (J^\infty, \mathscr V^\ast)
\]
defined as follows. First notice that there is a vector bundle projection
\[
\mathscr V \to V
\]
mapping a transverse vector $v \operatorname{mod} \mathscr C$ at the point $z = N_p^\infty \in J^\infty$ to 
\[
d\pi (v) \operatorname{mod} T_p N \in T_p P / T_p N = V_z.
\]
Dually, there is a vector bundle inclusion
\[
V^\ast \hookrightarrow \mathscr V^\ast.
\]
Accordingly, there is an inclusion
\begin{equation}\label{eq:incl_V*}
\Gamma \big(V^\ast \otimes \wedge^n \mathscr C^\ast \big) \hookrightarrow \overline \Omega{}^n (J^\infty, \mathscr V^\ast).
\end{equation}
that can be described in local coordinates as follows. Let $v^1, \ldots, v^m \in \Gamma (V^\ast)$ be the dual basis of the local basis $v_1, \ldots, v_m \in \Gamma (V)$ described in Subsection \ref{Sec:CD}. Then the inclusion (\ref{eq:incl_V*}) maps
\[
v^\alpha \otimes \overline{\mathrm d}{}^n x \mapsto \overline{\mathrm d}{}^n x \otimes (du^\alpha - u^\alpha_i dx^i), \quad \alpha = 1, \ldots, m.
\]

\begin{proposition}
The composition
\begin{equation}\label{eq:isom_top_V*}
\Gamma \big(V^\ast \otimes \wedge^n \mathscr C^\ast \big) \hookrightarrow \overline \Omega{}^n (J^\infty, \mathscr V^\ast) \longrightarrow \overline H{}^n (J^\infty, \mathscr V^\ast)
\end{equation}
is a vector space isomorphism. Moreover, for $L \in \overline \Omega{}^n (J^\infty)$ locally given by 
\[
L = \mathscr L (x, \ldots, u_I, \ldots)\, \overline{\mathrm d}{}^n x
\]
the section $\mathbf E [L]$ of $V^\ast \otimes \wedge^n \mathscr C^\ast$ corresponding to $d^{\mathrm{sec}} [L]$ via (\ref{eq:isom_top_V*}) is locally given by
\[
\mathbf E [L] = \sum_{|I| < \infty} (-)^{|I|} D_I \left( \frac{\partial \mathscr L}{\partial u^\alpha_I}\right) v^\alpha \otimes \overline{\mathrm d}{}^n x.
\]
\end{proposition}

In view of the first part of the above proposition, the top cohomology $\overline H{}^n (J^\infty, \mathscr V^\ast)$ is in bijection with the $C^\infty (J^\infty)$-module of sections of a vector bundle over $J^\infty$. Hence it makes sense to speak about the \emph{zero locus} in $J^\infty$ of a cohomology class in $\overline H{}^n (J^\infty, \mathscr V^\ast)$. From the second part of the proposition, the zero locus of $d^{\mathrm{sec}} [L]$, equivalently the zero locus of $\mathbf E [L]$, is the \emph{Euler-Lagrange equations} corresponding to the variational principle $[L]$ (see Example \ref{exmpl:var_prin}):
\[
\sum_{|I| < \infty} (-)^{|I|} D_I \left( \frac{\partial \mathscr L}{\partial u^\alpha_I}\right)  = 0. 
\]
Similarly, one can show that there is a map
\[
d^{\mathrm{sec}} : \overline H{}^n (J^\infty, \mathscr V^\ast) \to \overline H{}^n (J^\infty, \wedge^2 \mathscr V^\ast)
\]
(see the next subsection) mapping a system of $m$ PDEs
\[
 E_\alpha (x, \ldots, u_I, \ldots) = 0 
\]
to the associated \emph{Helmoltz conditions} for variationality.
\end{example}
