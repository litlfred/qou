---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-049-122-the-uniformization-theorem
section_title: "The uniformization theorem."
section_number: 12.2
pages: 101-103
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.952
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:7.2}

\begin{para}\label{para:7.2.1}
 One fixes a point of $\Sh(\ovl{\F}_p)$, hence a
 $\ovl{\F}_p$-abelian variety $\ovl{A}$ up to prime to $p$ isogeny with
 $\mathcal{B}$-action, principal $\ast$-polarization, and level
 structure. We consider the $p$-divisible group
 $\ovl{\Lambda}={\ovl{A}}[p^\infty]$ (with $\mathcal{B}_p$-action,
 principal 
 $\ast$-polarization, level structure). We denote by $\ovl{G}$ the
 $\Q$-group of self-quasi-isogenies of ${\ovl{A}}$ respecting the
 additional structure. It is clear that $\ovl{G}(\Q_p)\subset J$; on the
 other hand $\ovl{G}(\A_f^p)\subset G(\A_f^p)$.

 We also consider an auxiliary lifting $\tilde{\ovl{A}}$ of $\ovl{A}$ (with
 $\mathcal{B}$-action) over some finite extension $\mathcal{O}_{E'}$ of
 $\mathcal{O}_E$ in $\mathfrak{v}$, and set
 $\tilde{\ovl{\Lambda}}=\tilde{\ovl{A}}_\mathfrak{v}[p^\infty]$.  We can
 then identify $\D(\ovl{\Lambda})\otimes_W K$ with
 $\mathrm{H}^1_{\mathrm{DR}}(\tilde{\ovl{A}})\otimes_{\mathcal{O}_{E'}}
 K$, and the submodule $\omega_{\tilde{\ovl{\Lambda}}}$ with
 $F^1\mathrm{H}^1_{\mathrm{DR}}(\tilde{\ovl{A}})\otimes_{\mathcal{O}_{E'}}
 K$.  Thus if the complex lagrangian space 
 $F^1_0$ of \ref{para:1.1.4} is taken to be
 $F^1\mathrm{H}^1_{\mathrm{DR}}(\tilde{\ovl{A}})\otimes_{\mathcal{O}_{E'}}
 \C$ (for some complex embedding of $E'$ 
 extending the natural complex embedding of $E$), the complex and
 $p$-adic Shimura type conditions ``agree'' (\ref{para:1.1.4}, \ref{para:4.3.2}). We can
 consider the corresponding decorated moduli problem for $p$-divisible
 groups, and the formal moduli scheme $\mathfrak{M}$ over $\mathfrak{v}$
 as in \ref{sub:4.3}.
 

 \noindent Moreover, the flags spaces $\mathcal{D}^\vee$ considered in 
 the complex and $p$-adic situations agree, \ie come from the same flag 
 space defined over the reflex field $E$.


\end{para}

\begin{para}\label{para:7.2.2}
 One defines a morphism of functors on $\Nil_\mathfrak{v}$: 
 \begin{equation*}
  {\mathfrak{M}} \rightarrow \Sh
 \end{equation*}
 as follows \cite[6.14]{psfpg}.
 Let $S$ be in $\Nil_\mathfrak{v}$ and let us consider a pair
 $(\Lambda,\rho)\in \mathfrak{M}(S)$. By rigidity of $p$-divisible
 groups up to isogeny (\ref{thm:2.2.3}), the
 $\mathcal{B}_p$-quasi-isogeny $\rho 
 \in \qisog(\Lambda\times_S S_{\mathrm{red}},
 \ovl{\Lambda}\times_{{\ovl{\F}}_p}S_{\mathrm{red}})$ lifts to a unique 
 $\mathcal{B}_p$-quasi-isogeny $\tilde{\rho}\in \qisog(\Lambda,
 \tilde{\ovl{\Lambda}}\times_\mathfrak{v}S)$. This can be algebraized in
 a weak sense: there is an $S$-abelian scheme $A_{(\Lambda,\rho)}$ up to
 prime to $p$ isogeny, with $\mathcal{B}$-action and with $p$-divisible
 group $\Lambda $, and a quasi-isogeny $A_{(\Lambda,\rho)}\rightarrow
 \tilde{\ovl{A}}\times_{\mathcal{O}_{E'}}S$ which induces $\tilde{\rho}$
 at the level of $p$-divisible groups. Moreover $A_{(\Lambda,\rho)}$ is
 unique in the category of $S$-abelian schemes up to prime to $p$ isogeny
 with $\mathcal{B}$-action (\ref{lem:7.1.4}), and its formation is
 functorial in 
 $(\Lambda,\rho)$. One then defines the required morphism of functors on
 $\mathfrak{M}(S)$ by setting $(\Lambda,\rho)\mapsto A_{(\Lambda,\rho)}$
 (endowed with the polarization and level structure inherited from $\ovl{A}$).

 This defines a morphism of formal schemes, hence a morphism
 of associated analytic spaces over $\C_p$:
 \begin{equation*}
  \mathcal{Q}:\;\mathcal{M}\;\rightarrow\; \Sh_{\C_p}^{\mathrm{an}}.
 \end{equation*}
\end{para}

\begin{para}\label{para:7.2.3}
 It turns out that the decorated abelian varieties (up to prime to $p$
 isogeny) which are {\it isogenous} to $\ovl{A}$ form in a natural way a
 {\it countable union $Z=\bigcup Z_n$ of projective irreducible
 subvarieties $Z_n$ of $\;\Sh_{\ovl{\F}_p}$}, each of them
 meeting only finitely many members of the family (\cite[6.23, 6.34]{psfpg}).
 One can slightly generalize the notion of tubes (\ref{sub:3.5}) and
 define the tube $]Z[\subset \Sh_{\C_p}^{\mathrm{an}}$. We denote by $S$ the
 connected component of $]Z[$ which contains the modular point $s$ of our
 chosen lifting $\tilde{\ovl{A}}$.
\end{para}

\begin{thm}\label{thm:7.2.4}
 For sufficiently small $C^p$, there is a connected component
 $\mathcal{M}^0$ of $\mathcal{M}$ such that the restriction
 $\mathcal{Q}:\;\mathcal{M}^0\rightarrow S$ is a topological covering of
 $S$. More precisely, $S$ is the (right) quotient of $\mathcal{M}^0$ by
 some torsion-free discrete subgroup of $J$.
\end{thm}

\cf \cite[6.23, 6.31]{psfpg}. Roughly speaking, the proof of \ref{thm:7.2.4}
involves two steps: using the Serre-Tate theorem \ref{thm:2.2.4}, one
shows that 
the morphism of $\mathfrak{v}$-formal schemes $\mathfrak{M}$
$\rightarrow \widehat{\Sh}$ defined above is
formally etale. One concludes by a careful study of this morphism on
geometric points.

In our examples \ref{sub:4.2}, $S$ is an open unit
disc, and the map $\mathcal{Q}$ is an isomorphism (in \ref{para:4.2.1}, it is
induced by $q\mapsto z=\lambda$).

\begin{para}\label{para:7.2.5} Let us consider the universal decorated
 abelian scheme $\udl{A}$ over $\Sh$, and the vector bundle
 $\mathcal{H}=\mathrm{H}^1_{\mathrm{DR}}(\udl{A}/\Sh)$ with its
 Gauss-Manin connection 
 $\nabla_{\mathrm{GM}}:\mathcal{H}\rightarrow \Omega^1_{\Sh}\otimes
 \mathcal{H}$. 
\end{para}

\begin{cor}\label{cor:7.2.6}  Viewed as a $p$-adic connection and
 restricted to $S$, the Gauss-Manin connection 
 ${\nabla_{\mathrm{GM}}}_{| S}$ comes from a representation of
 $\pi_1^{\mathrm{top}}(S,s)$ on $V^{\C_p}\;$ (hence it satisfies
 Cauchy's theorem, \cf I.\ref{sub-connection}).
\end{cor}

\begin{proof}
 Let $\tilde{S}$ be the universal covering of $S$. According to
 I.\ref{sub-connection}), we have to show that the pull-back of 
 $\nabla_{\mathrm{GM}}$ on $\tilde{S}$ is trivial ($\cong V^{\C_p}\otimes
 \mathcal{O}_{\tilde{S}})$. By \ref{thm:7.2.4} and \ref{lem:6.2.5}, this
 already holds on the quotient $\mathcal{M}^0$ of $\tilde{S}$.
\end{proof}

 \noindent {\it Remark.} Using the Weil descent data of \cite[6.21]{psfpg},
 one can show that the representation is defined over a
 finite unramified extension $E'_v$ of $E_v$, \ie comes from a
 representation of $\pi_1^{\mathrm{top}}(S,s)$ on $V\otimes E'_v$.

\begin{para}\label{para:7.2.7}
 The assumption $C=C^pC_p$ is necessary to define the morphism
 $\mathcal{Q}: \mathcal{M}^0\rightarrow S$. The assumption ``$C^p$ small
 enough'' is much less important. Theorem \ref{thm:7.2.4}. holds without it,
 except that the discrete subgroup of $J$ is then no longer torsion-free
 [the point is that there is always a normal subgroup ${C'}^p$ of finite
 index which is small enough, one applies the theorem to ${C'}^p$, and one
 passes to the quotient by ${C'}^p/C^p$]. However, to give a modular
 interpretation of the (ramified) quotient of $\mathcal{M}^0$ in this
 case, one needs the notion of $p$-adic orbifold (to be discussed in
 III); moreover the Gauss-Manin connection may acquire logarithmic
 singularities along the branched locus.
