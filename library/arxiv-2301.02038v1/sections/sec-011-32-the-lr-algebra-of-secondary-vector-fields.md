---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-011-32-the-lr-algebra-of-secondary-vector-fields
section_title: "the LR-algebra of secondary vector fields"
section_number: 3.2
pages: 20-22
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.932
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
Let $(\mathscr E, \mathscr C)$ be a diffiety. According to Theorem \ref{theor:LR} the pair $(\boldsymbol C^\infty, \boldsymbol{\mathfrak X})$ is a graded Lie-Rinehart algebra. Recall that $\boldsymbol C^\infty = \overline H{}^\bullet (\mathscr E) = H^\bullet (\overline \Omega (\mathscr E), \overline d)$ and $\boldsymbol{\mathfrak X} = \overline H{}^\bullet (\mathscr E, \mathscr V) = H^\bullet(\overline \Omega(\mathscr E, \mathscr V), \overline d)$. Moreover, the cochains $\overline \Omega{}^\bullet(\mathscr E, \mathscr V)$ are naturally a graded module over the cochains $\overline \Omega{}^\bullet (\mathscr E)$. It is then natural to look for an $LR_\infty$-algebra structure on cochains $(\overline \Omega{}^\bullet (\mathscr E), \overline \Omega{}^\bullet(\mathscr E, \mathscr V))$ responsible for the Lie-Rinehart algebra structure on $(\boldsymbol C^\infty, \boldsymbol{\mathfrak X})$. Such $LR_\infty$-algebra structure exists indeed as we now show. 

Choose again a splitting (\ref{eq:split}) and use it to see transverse vector fields and horizontal forms as honest vector fields and differential forms on $\mathscr E$, as we did in Subsection \ref{Subsec:LR}. We will also interpret horizontal forms with values in transverse forms as ordinary vector valued forms.

The normal bundle $\mathscr V$ is now a (non-necessarily involutive) distribution on $\mathscr E$. Its curvature is 
\[
R : \wedge^2 \mathscr V \to \mathscr C, \quad (Y, Z) \mapsto R(Y, Z) := [Y, Z] - \operatorname{pr} [Y, Z],
\]  
where we denote by $\operatorname{pr} : T\mathscr E \to \mathscr V$ the projection, and can be seen as a vector valued $2$-form on $\mathscr E$:
\[
R \in \mathscr V\Omega^2 ( \mathscr E) \otimes \Gamma (\mathscr C) \subseteq \Omega^2 (\mathscr E, T\mathscr E).
\]
In the following we will need to shift by $1$ the degree in the graded module $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)$. Accordingly, we will denote by $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)[1]$ the new graded module whose degree $k$ component is $\overline \Omega{}^{k+1} (\mathscr E, \mathscr V)$. We will also need the \emph{Nijenhuis-Richardson bracket} of vector valued forms \cite[Section 16]{m08} that we denote $[-,-]^{\mathrm{nr}}$. We recall that $[-,-]^{\mathrm{nr}}$ maps an $r$-form and an $s$-form into an $(r+s-1)$-form.

\begin{theorem}\label{theor:LR_infty}
A splitting (\ref{eq:split}) induces an $LR_\infty$-algebra structure on 
\[
\big(\overline \Omega{}^\bullet (\mathscr E), \overline \Omega{}^\bullet(\mathscr E, \mathscr V)[1]\big)
\]
whose structure maps are given by
\[
\begin{aligned}
\mathfrak l_1 \overline W & = \overline d\, \overline W \\
\mathfrak l_2 \big(\overline W, \overline U\big) & = - (-)^{|W|} [\overline W, \overline U]^{\mathrm{fn}} + [[R, \overline W]^{\mathrm{nr}}, \overline U]^{\mathrm{nr}} \\
\mathfrak l_3 \big(\overline W, \overline U, \overline Z\big) & = - [[[R, \overline W]^{\mathrm{nr}}, \overline U]^{\mathrm{nr}}, \overline Z]^{\mathrm{nr}}
\end{aligned}
\]
and
\[
\begin{aligned}
\mathfrak m_1 \overline \omega & = \overline d\, \overline \omega \\
\mathfrak m_2 \big(\overline W | \overline \omega\big) & = - (-)^{|W|} \mathcal L_{\overline W} \overline \omega + \iota_{[R, \overline W]^{\mathrm{nr}}} \overline \omega \\
\mathfrak m_3 \big(\overline W, \overline U| \overline \omega\big) & = - \iota_{[[R, \overline W]^{\mathrm{nr}}, \overline U]^{\mathrm{nr}}} \overline \omega
\end{aligned}
\]
for all $\overline W, \overline U, \overline Z \in \overline \Omega{}^\bullet(\mathscr E, \mathscr V)[1]$, and all $\overline \omega \in \overline \Omega{}^\bullet(\mathscr E)$, while $\mathfrak l_k = \mathfrak m_k = 0$ for $k > 3$. 
The graded Lie-Rinehart algebra structure induced in cohomology (Remark \ref{rem:LR_cohom}) agrees with that of Theorem \ref{theor:LR}.
\end{theorem}

\begin{remark}
The degree $1$ shift in the statement of Theorem \ref{theor:LR_infty} is due to our convention on $LR_\infty$-algebra structure and can be removed choosing a different convention (see \cite{vi12} for more details). 
\end{remark}

The graded $\overline \Omega{}^\bullet (\mathscr E)$-module $\Omega{}^\bullet(\mathscr E, \mathscr V)[1]$ is projective and finitely generated. Accordingly, the $LR_\infty$-algebra structure of Theorem \ref{theor:LR_infty} can be also encoded into the associated Chevalley-Eilenberg algebra. The Chevalley-Eilenberg algebra of $\big(\overline \Omega{}^\bullet (\mathscr E), \overline \Omega{}^\bullet(\mathscr E, \mathscr V)[1]\big)$ is described in the next theorem.

\begin{theorem}\label{theor:CE}
The Chevalley-Eilenberg algebra of the $LR_\infty$-algebra of Theorem \ref{theor:LR_infty} is
\[
\overline \Omega{}^\bullet (\mathscr E, \wedge^\bullet \mathscr V^\ast)
\]
with structure derivations given by
\[
\begin{aligned}
\mathfrak d_1 & = \overline d\\
\mathfrak d_2 & = d- \overline d + \iota_R \\
\mathfrak d_3 & = - \iota_R
\end{aligned}
\]
while $\mathfrak d_k = 0$ for $k > 3$. In particular the total derivation $\mathfrak D = \mathfrak d_1 + \mathfrak d_2 + \mathfrak d_3$ is just the De Rham differential $d$. The DG algebra structure induced in cohomology (Remark \ref{rem:DGA_cohom}) agrees with that of Theorem \ref{theor:DGA}.
\end{theorem}

\begin{remark}
The $LR_\infty$-algebra of Theorem \ref{theor:LR_infty} is independent of the choice of the splitting \ref{eq:split} up to \emph{$LR_\infty$-isomorphisms}. We will not provide here a notion of $LR_\infty$-morphism. We just mention that the independence of the $LR_\infty$-algebra $\big(\overline \Omega{}^\bullet (\mathscr E), \overline \Omega{}^\bullet(\mathscr E, \mathscr V)[1]\big)$ of the splitting is rigorously expressed by the fact that the total derivation $\mathfrak D = \mathfrak d_1 + \mathfrak d_2 + \cdots$ in the Chevalley-Eilenberg algebra of Theorem \ref{theor:CE} is always the same, i.e.{} the De Rham differential, regardless of the splitting we have chosen. See \cite{vi12} for more details.
\end{remark}

Theorems \ref{theor:LR_infty} and \ref{theor:CE} provide indications towards \emph{Vinogradov's conjecture} that the correct category where differential calculus on the space of solutions of a PDE $\mathscr E_0$ should be developed is the homotopy category of $DG$-modules over the horizontal De Rham algebra $(\overline \Omega{}^\bullet (\mathscr E), \overline d)$. They also suggest to add one further step to the recipe presented at the end of Section \ref{Sec:Homol}. Namely

\begin{recipe}[Addendum]\label{addendum}\quad
\begin{enumerate}
\item[(5)] Show that the cochains $\overline \Omega{}^\bullet (\mathscr E) \otimes \mathscr V \Phi$ support a homotopy algebra structure responsible for the algebraic structure on $\boldsymbol{\Phi}$.
\end{enumerate}
\end{recipe}
