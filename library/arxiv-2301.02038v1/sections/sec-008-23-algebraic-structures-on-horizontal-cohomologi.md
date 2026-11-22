---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-008-23-algebraic-structures-on-horizontal-cohomologi
section_title: "algebraic structures on horizontal cohomologies"
section_number: 2.3
pages: 15-18
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.964
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly"
---
\label{Subsec:LR}
 Examples \ref{exmpl:var_prin} and \ref{exmpl:cons_law} suggest that the horizontal cohomology $\overline H{}^\bullet (\mathscr E)$ should be interpreted as ``smooth functions on the space of solutions of the PDE $\mathscr E_0$''. For this reason we also denote it
 \[
 \boldsymbol C^\infty := \overline H{}^\bullet (\mathscr E)
 \] 
 and call it \emph{secondary functions} adopting a terminology by Vinogradov. Similarly, the discussion at the end of Example \ref{exmpl:inf_sym} suggests that $\overline H{}^\bullet (\mathscr E, \mathscr V)$ should be interpreted as ``vector fields on the space of solutions of $\mathscr E_0$''. For this reason we also denote it
 \[
 \boldsymbol{\mathfrak X} := \overline H{}^\bullet (\mathscr E, \mathscr V)
 \]
 and call it \emph{secondary vector fields}. Finally, Example \ref{exmpl:ELeq} suggests that $\overline H{}^\bullet (\mathscr E, \mathscr V)$ should be interpreted as ``differential forms on the space of solutions of $\mathscr E_0$'', we denote
 \[
 \boldsymbol{\Omega}^p := \overline H{}^\bullet (\mathscr E, \wedge^p \mathscr V^\ast)
 \]
 and call it \emph{secondary differential $p$-forms}, $p = 0, 1, \ldots$. This interpretation is supported by the fact that the above cohomologies possess the appropriate algebraic structures for functions, vector fields, differential forms. For instance, $\boldsymbol C^\infty$ is naturally a (graded) commutative algebra, being the cohomology of a  commutative DG algebra. Similarly, the pair $(\boldsymbol C^\infty, \boldsymbol{\mathfrak X})$ is a (graded) Lie-Rinehart algebra. We now explain the latter claim.
 
 Choose once for all a splitting of the short exact sequence (\ref{eq:SES_C}):

 \begin{equation}\label{eq:split}
 \xymatrix{0 \ar[r] & \mathscr C \ar[r] & T\mathscr E \ar[r] & \mathscr V \ar[r] \ar@/^9pt/[l]& 0
 }.
 \end{equation}
 
\vspace{10pt}
\noindent This induces a direct sum decomposition $T\mathscr E \cong \mathscr C \oplus \mathscr V$ that allows us to interpret $\mathscr V$ as a distribution and transverse vector fields as honest vector fields on $\mathscr E$. Dually, we get a factorization
\begin{equation}\label{eq:fact}
\Omega^\bullet (\mathscr E) \cong \overline \Omega{}^{\bullet} (\mathscr E) \otimes \mathscr V \Omega^\bullet
\end{equation}
that allows us to interpret horizontal differential forms as honest differential forms on $\mathscr E$, and in the rest of this section we will do so.  Similarly, we understand the embedding $\overline \Omega{}^\bullet (\mathscr E, \mathscr V) \hookrightarrow \Omega^\bullet (\mathscr E, T\mathscr E)$ induced by the splitting (\ref{eq:split}) (and the factorization (\ref{eq:fact})) and interpret $\mathscr V$-valued horizontal differential forms as honest vector valued forms on $\mathscr E$.    Now, recall that vector valued forms are naturally equipped with a graded Lie bracket: the Fr\"olicher-Nijenhuis bracket $[-,-]^{\mathrm{fn}}$ (see, e.g., \cite[Section 16]{m08}). Moreover, the resulting graded Lie algebra acts on differential forms via the Lie derivative (along vector valued forms). 

Notice that, unless the distribution $\mathscr V \subseteq T \mathscr E$ is itself involutive, the Fr\"olicher-Nijenhuis bracket does not preserve $\mathscr V$-valued horizontal forms $\overline \Omega{}^\bullet (\mathscr E, \mathscr V) $. We can define a bracket on $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)$ by first taking the Fr\"olicher-Nijenhuis bracket, and then projecting to $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)$, but the bracket obtained in this way is not a Lie bracket (unless $\mathscr V$ is involutive). However, it gives a honest graded Lie bracket on $\boldsymbol{\mathfrak X}$. Namely, denote by
\[
\operatorname{pr} : \Omega^\bullet (\mathscr E) \to \overline \Omega{}^\bullet (\mathscr E), \quad\quad \operatorname{pr} : \Omega^\bullet (\mathscr E , T \mathscr E) \to \overline \Omega{}^\bullet (\mathscr E, \mathscr V)
\]
the (natural) projections. Define a bracket $[-,-]^{\mathrm{sec}}$ on $\boldsymbol{\mathfrak X}$, the \emph{secondary commutator}, via:

\begin{equation}\label{eq:sec_Lie_bra}
[-,-]^{\mathrm{sec}} : \boldsymbol{\mathfrak X} \times \boldsymbol{\mathfrak X} \to \boldsymbol{\mathfrak X}, \quad \left(\boldsymbol W, \boldsymbol U \right) \mapsto \left[ \boldsymbol W, \boldsymbol U \right]^{\mathrm{sec}} := \big[\operatorname{pr}[\overline W, \overline U]^{\mathrm{fn}}\big],
\end{equation}
where $\boldsymbol W = [\overline W], \boldsymbol U = [\overline U]$ are the cohomology classes of the cocycles $\overline W, \overline U \in \overline \Omega{}^\bullet (\mathscr E, \mathscr V)$ respectively.

We also define the \emph{secondary Lie derivative}:
\begin{equation}\label{eq:sec_Lie_der}
\mathcal L^{\mathrm{sec}} : \boldsymbol{\mathfrak X} \times \boldsymbol{C}^\infty \to  \boldsymbol{C}^\infty, \quad \left(\boldsymbol W, \boldsymbol f \right) \mapsto \mathcal L^{\mathrm{sec}}_{\boldsymbol W} \boldsymbol f :=\big[ \operatorname{pr} \mathcal L_{\overline W} \overline \omega \big],
\end{equation}
where $\boldsymbol f = [\overline \omega]$ is the cohomology class of the cocycle $\overline \omega \in \overline \Omega{}^\bullet (\mathscr E)$. 

\begin{theorem}\label{theor:LR}
The operations (\ref{eq:sec_Lie_bra}) and (\ref{eq:sec_Lie_der}) are well-defined and independent of the splitting (\ref{eq:split}). Together with them and the graded $\boldsymbol C^\infty$-module structure on $\boldsymbol{\mathfrak X}$ induced by the DG $(\overline \Omega{}^\bullet (\mathscr E), \overline d)$-module structure on $(\overline \Omega{}^\bullet (\mathscr E, \mathscr V), \overline d)$, the pair $(\boldsymbol{C}^\infty, \boldsymbol{\mathfrak X})$ form a graded Lie-Rinehart algebra.
\end{theorem}

As for secondary differential forms, they form a commutative DG algebra. To see this, consider the splitting (\ref{eq:split}) again and understand the induced factorization (\ref{eq:fact}). For every $p, p'$, we have a \emph{secondary wedge product}:
\begin{equation}\label{eq:wedge_sec}
\wedge^{\mathrm{sec}} : \boldsymbol \Omega^p \times \boldsymbol \Omega^{p'} \to \boldsymbol \Omega^{p+p'}, \quad (\boldsymbol \omega, \boldsymbol \omega') \mapsto \boldsymbol \omega \wedge^{\mathrm{sec}}  \boldsymbol \omega' := \big[ \omega \wedge \omega' \big],
\end{equation}
where $\boldsymbol \omega = [\omega], \boldsymbol \omega' = [\omega']$ are the cohomology classes of the cocycles $\omega \in \overline \Omega{}^\bullet (\mathscr E, \wedge^p \mathscr V^\ast)$, $\omega' \in \overline \Omega{}^\bullet (\mathscr E, \wedge^{p'} \mathscr V^\ast)$.

We also have a \emph{secondary differential}.  In order to define it we first notice that the De Rham differential does not map $\wedge^p \mathscr V^\ast$-valued horizontal form to $\wedge^{p+1} \mathscr V^\ast$-valued horizontal form (unless $\mathscr V$ is involutive). We can define a map
\[
\overline \Omega{}^\bullet (\mathscr E, \wedge^p \mathscr V^\ast ) \to \overline \Omega{}^\bullet (\mathscr E, \wedge^{p+1} \mathscr V^\ast )
\]
by first taking the De Rham differential, and then projecting to $\Omega{}^\bullet (\mathscr E, \wedge^{p+1} \mathscr V^\ast )$, but the maps obtained in this way do not square to zero (unless $\mathscr V$ is involutive). However, they give a honest differential on $\boldsymbol{\Omega}^\bullet$. Namely, denote by
\[
\operatorname{pr} : \Omega^\bullet (\mathscr E) \to \Omega{}^\bullet (\mathscr E, \wedge^{p+1} \mathscr V^\ast)
\]
the projection. Define a map $d^{\mathrm{sec}}$ on $\boldsymbol{\Omega}^\bullet$ via:
\begin{equation}\label{eq:d_sec}
d^{\mathrm{sec}} : \boldsymbol \Omega^p \to \boldsymbol \Omega^{p+1}, \quad \boldsymbol \omega \mapsto d^{\mathrm{sec}} \boldsymbol \omega := \big[\operatorname{pr} d \omega \big].
\end{equation}

\begin{theorem}\label{theor:DGA}
The operations (\ref{eq:wedge_sec}) and (\ref{eq:d_sec}) are well-defined and independent of the splitting (\ref{eq:split}). Together with them $\boldsymbol{\Omega}^\bullet$ form a commutative DG algebra (with respect to the \emph{total grading}, i.e.{} the grading on $\overline H{}^q (\mathscr E, \wedge^p \mathscr V^\ast)$ given by $p+q$).
\end{theorem}

\begin{remark}
The secondary differential (\ref{eq:d_sec}) agrees with that introduced in Example \ref{exmpl:ELeq}.
\end{remark}

There is a more conceptual way to introduce the operations (\ref{eq:wedge_sec}) and (\ref{eq:d_sec}), based on the \emph{Vinogradov's $\mathscr C$-spectral sequence}, that we now explain. Namely, recall the $d$-closed graded ideal $\mathscr C \Omega^\bullet \subseteq \Omega^\bullet (\mathscr E)$ from Subsection \ref{Sec:hor_cohom} (it consists of differential forms vanishing when restricted to vector fields in $\mathscr C$).  The powers 
\[
\mathscr C^p \Omega^\bullet := \underset{\text{$p$ times}}{\underbrace{\mathscr C \Omega^\bullet \wedge \cdots \wedge \mathscr C \Omega^\bullet}},\quad p = 0, 1, \ldots
\]
define a filtration
\begin{equation}\label{eq:filtr}
\Omega^\bullet (\mathscr E) = \mathscr C^0 \Omega^\bullet \supseteq \mathscr C \Omega^\bullet \supseteq \cdots \supseteq \mathscr C^p \Omega^\bullet \supseteq \cdots, 
\end{equation}
by graded $d$-closed ideals, which in turn determines a spectral sequence $\mathscr C E$, called the \emph{$\mathscr{C}$-spectral sequence}, computing the ordinary De Rham cohomologies of $\mathscr E$.

\begin{proposition}
For all $p, q$, the map
\[
\overline \Omega{}^\bullet (\mathscr E, \wedge^p \mathscr V^\ast) \to \mathscr E_0^{p,\bullet} = \mathscr C^p \Omega^{p+\bullet} / \mathscr C^{p+1} \Omega^{p+\bullet}, \quad \overline \omega \otimes \varpi \mapsto \omega \wedge \varpi \operatorname{mod} \mathscr C^{p+1} \Omega^{p+\bullet}
\]
is a well-defined cochain isomorphism, where $\overline \omega \in \overline \Omega{}^\bullet (\mathscr E)$, $\varpi \in \mathscr V \Omega^p$, and $\omega \in \Omega^\bullet (\mathscr E)$ is any $q$-form projecting to $\overline \omega$ under $\Omega^\bullet (\mathscr E) \to \overline \Omega{}^\bullet (\mathscr E)$. The induced isomorphism
\[
\boldsymbol \Omega^p = \overline H{}^\bullet (\mathscr E, \wedge^p \mathscr V^\ast) \to \mathscr C E^{p, \bullet}_1 = H^\bullet (\mathscr C E^{p, \bullet}_0, d_0^{p, \bullet})
\]
identifies $d^{sec}$ with the differential $d_1$ in the first page of the $\mathscr C$-spectral sequence, and $\wedge^{sec}$ with the product structure on $\mathscr C E_1$ given by the fact that (\ref{eq:filtr}) is a filtration by DG ideals.
\end{proposition}

Hence $\wedge^{\mathrm{sec}}, d^{\mathrm{sec}}$ could have been defined via the $\mathscr C$-spectral sequence without using the splitting (\ref{eq:split}). One can even show that there is an analogue of the whole Cartan Calculus on secondary differential forms and secondary vector fields. All these operations together form the fundamentals of \emph{Vinogradov's Secondary Calculus}. Most of Vinogradov's work on PDEs has been based on the following principle: \emph{Secondary Calculus is an appropriate replacement for Differential Calculus on the space of solutions of a PDE}.

We conclude this sections presenting an informal \emph{secondarization recipe}. Namely, let $\Phi$ be any natural construction in differential geometry (e.g.{} functions on manifolds, vector fields, the De Rham complex, etc.). The discussion in this subsection suggests the following recipe to find the \emph{secondary version of $\Phi$}, i.e.{} an appropriate replacement $\boldsymbol \Phi$ for the construction $\Phi$ on the space of solutions of a PDE $\mathscr E_0$.

\begin{recipe} \quad
\begin{enumerate}
\item Define the \emph{transverse version} $\mathscr V \Phi$ of $\Phi$ (when $\Phi$ is ``vector fields'', then its transverse version is $\Gamma (\mathscr V)$).
\item Notice that $\mathscr V \Phi$ is canonically equipped with an action of the Lie algebroid $\mathscr C$ giving a DG $(\overline \Omega{}^\bullet(\mathscr E) , \overline d)$-module structure to $\overline \Omega{}^\bullet(\mathscr E) \otimes \mathscr V \Phi$ (when $\Phi$ is ``vector fields'', then $\overline \Omega{}^\bullet(\mathscr E) \otimes \mathscr V \Phi$ is $\overline \Omega{}^\bullet (\mathscr E, \mathscr V)$).
\item Define $\boldsymbol \Phi$ as the horizontal cohomology with coefficients in $\mathscr V \Phi$: $\boldsymbol \Phi := H^\bullet (\overline \Omega(\mathscr E) \otimes \mathscr V \Phi, \overline d)$ (when $\Phi$ is ``vector fields'', then $\boldsymbol \Phi$ is $\boldsymbol{\mathfrak X}$).
\item Find the appropriate algebraic structures on $\boldsymbol \Phi$ (when $\Phi$ is ``vector fields'', then $\boldsymbol \Phi = \boldsymbol{\mathfrak X}$ is a graded Lie-Rinehart algebra over $\boldsymbol C^\infty$).
\end{enumerate}
\end{recipe}

In the next section we will use this recipe to define \emph{secondary scalar differential operators}, i.e.{} an appropriate replacement for scalar differential operators on the space of solutions of a PDE.
