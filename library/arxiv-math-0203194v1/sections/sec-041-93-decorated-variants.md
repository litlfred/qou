---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-041-93-decorated-variants
section_title: "Decorated variants."
section_number: 9.3
pages: 89-92
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.979
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:4.3} 

\begin{para}\label{para:4.3.1} Just as in the complex case
 \ref{para:1.1.4}, it is useful to consider variants or the moduli
 problem \ref{sub:4.1} for ``decorated'' $p$-divisible groups, with prescribed
 endomorphisms and/or polarization.


Instead of
the $\Q$-algebra $B$ of \ref{para:1.1.4}, we shall consider a finite-dimensional semi-simple $\Q_p$-algebra $B_p$, since
the category of $p$-divisible groups up to isogeny is
$\Q_p$-linear. Let $V_p$ be a $B_p$-module
of finite type, and let $G_{\Q_p}$ be the group of 
$B_p$-linear endomorphisms of $V_p$.
\par\noindent  Let $\mathcal{B}_p$ be a maximal order in $B_p$, and let
$L_p$ be a lattice in $V_p$, stable under $\mathcal{B}_p$. 


\end{para}

\begin{para}\label{para:4.3.2} We assume that $\mathcal{B}_p$ acts on our
 $p$-divisible group $\ovl{\Lambda}$. One then redefines $J$ to 
be the group of self-quasi-isogenies of $\ovl{\Lambda}$ which respect
the $\mathcal{B}_p$-action.


For technical reasons, one picks up a lifting $\tilde{\ovl{\Lambda}}$ of
$\ovl{\Lambda}$ with $\mathcal{B}_p$-action to some finite extension of
$W$, and looks at the $\mathcal{B}_p$-module
$F^1_0:=\omega_{\tilde{\ovl{\Lambda}}}$. We denote by $\mathfrak{v}$ the
finite extension $W[\tr(b| F^1_0)]$ of $W$.


One strengthens the moduli problem \ref{sub:4.1} by imposing to our pairs
 $(\Lambda,\rho)$ that $\Lambda$ is endowed with a
 $\mathcal{B}_p$-action $\iota:\mathcal{B}_p\rightarrow \End \Lambda$,
 $\rho$ respects the $\mathcal{B}_p$-action, and moreover a ``Shimura
 type condition'' $\det(\iota(b)| \omega(\Lambda))=\det(b|
 F^1_0)$.

 It follows easily from \ref{thm:4.1.2} \cite[3.25]{psfpg} that this
 moduli problem is {\it representable by a formal scheme, still denoted
 by $\mathfrak{M}$, over $\mathfrak{v}$. It is acted on by
 $J$. $\mathfrak{M}_{\mathrm{red}}$ is locally of finite type over ${\ovl{\F}}_p$
 and its irreducible components are projective
 ${\ovl{\F}}_p$-varieties. }
\end{para}

\begin{para}\label{para:4.3.3} Let us say a word about the polarized variant
 (here, it is safer to assume $p\neq 2$). One assumes 
 that $\mathcal{B}_p$ is endowed with an involution $\ast$, and that
 $L_p$ is autodual for an alternate $\Z_p$-bilinear form such that
 $\an{bv,w}=\an{v,b^\ast w}$. Of course, here, $G_{\Q_p}$ denotes the algebraic
 $\Q_p$-group of $B_p$-linear symplectic similitudes of $V_p$. One
 assumes that $\ovl{\Lambda}$ is endowed with a $\ast$-polarization
 \footnote{a $\ast$-polarization is a symmetric
 $\mathcal{B}_p$-linear quasi-isogeny between the $p$-divisible and its
 Serre dual, endowed with the transposed action of $\mathcal{B}_p$
 twisted by $\ast$}, and modify $J$ to respect the polarization up to a
 multiple in $\Q_p$.
 
 \bigskip
 The corresponding moduli problem is again representable by a formal
 scheme with the same properties. This formal scheme has been conjectured to be flat by Rapoport-Zink; although this has been verified in many cases (\cf \eg \cite{gortz}), there are some counter-examples  (\cf  \cite{pappas}).
\end{para}

\begin{exa}[fake elliptic curves at a critical prime $p$]\label{exa:4.3.4}
 Let us fix a indefinite quaternion algebra $B$
 over $\Q$ and a maximal order $\mathcal{B}$ in $B$ (after Eichler, they
 are all conjugate). A prime $p$ is called {\it critical} if it divides
 the discriminant of $B$, \ie if $B_p=B\otimes_\Q \Q_p$ is the
 (non-split) quaternion algebra over $\Q_p$. Note that $B_p$ then
 contains copies of the unramified quadratic extension on $\Q_p$; we
 denote by $\Q_{p^2}$ one of them. The maximal order (unique up to
 conjugation) can be written $\mathcal{B}_p=\mathcal{B}\otimes
 \Z_p=\Z_{p^2}[\Pi],\;\Pi^2=p,\;\Pi.a=a^\sigma\Pi$ for $a\in
 \Z_{p^2}$. We fix a critical prime $p$.


 We consider abelian surfaces with quaternionic multiplication by
 $\mathcal{B}$. They are sometimes called ``{\it fake elliptic curves}''
 \index{fake elliptic curves@fake elliptic curves}
 because they share many features with elliptic curves, 
 \cf \cite[III, 1]{updcds}.

 We fix a fake elliptic curve $\ovl{A}$ over $\ovl{\F}_p$, and set
 $\Lambda=\ovl{A}[p^\infty]$. This is a special formal
 $\mathcal{B}_p$-modules of height $4$ in the following sense.

 Let $S$ be in $\Nil_\mathfrak{v}$ (or else an inductive limit of such
 schemes --- as a formal scheme), and let $\Lambda$ be a $p$-divisible
 group over $S$. After Drinfeld, one says that $\Lambda$ is a {\it
 special formal $\mathcal{B}_p$-modules of height $4$} if

\begin{enumerate}
 \item $\Lambda$ is infinitesimal ($\Lambda=\hat\Lambda$) of height
       $h=4$,
 \item $\mathcal{B}_p$ acts on $\Lambda$,
 \item via this action, $\omega_\Lambda$ is a locally free
       $(\Z_{p^2}\otimes_{\Z_p}\mathcal{O}_S)$-module of rank $1$.
\end{enumerate}

\noindent We take $V_p=B_p$ where $B_p$ acts by left
multiplication. In this situation, $G_{\Q_p}\cong B_p^\times $. When
$S=\Spec(\ovl{\F}_p)$, there is a unique class of
$\mathcal{B}_p$-isogeny of special formal $\mathcal{B}_p$-modules of
height $4$. The group $J$ of self-quasi-isogenies of a special formal
$\mathcal{B}_p$-module of height $4$ is $J=GL_2(\Q_p)$. This can be
easily read off the Dieudonn\'e module $\otimes\Q$.


In this example, there is again a discrete invariant: the ``height'' of 
the quasi-isogeny $\rho$, which amounts to the 
$p$-adic valuation of the determinant of its image in $J$.
Therefore 
 \begin{equation*}
 \mathfrak{M}=\coprod_{\Z}\;\mathfrak{M}^0
\end{equation*}
 is a disjoint sum of copies of a formal scheme $\mathfrak{M}^0$
 which parametrizes deformations of the special formal module
 $\hat{\ovl{\Lambda}}$. This formal scheme has been described by
 Drinfeld, \cf \ref{para:6.3.4}.
\end{exa}

\begin{para}\label{para:4.3.5} This example and examples \ref{sub:4.2}
 were the sources of the general theory. 

\noindent Let us at once suggest a vague analogy with the
archimedean situation --- especially \ref{para:1.1.4}, \ref{para:1.2.4} ---
 which will become more 
and more precise in the next sections: one can see the $p$-divisible
group $\ovl{\Lambda}$ in characteristic $p$ (\resp $J$) as an analogue
of the infinitesimal oriented real Lie group $\hat U$ (\resp $G(\R)^0$).
    
\newpage

\section{$p$-adic period domains.}\label{sec:5}

\begin{abst}
 Review of $p$-adic symmetric domains and period domains via stability theory.
\end{abst}
\end{para}



\subsection{$p$-adic flag spaces.}\label{sub:5.1}

\begin{para}\label{para:5.1.1} We begin with the $p$-adic analogue of
 the flag space $\mathcal{D}^\vee$ of \ref{para:1.2.3},
 \ref{para:1.2.4}. In \ref{para:1.2.4}, this flag space parametrized the
 lagrangian subspaces $F^1$ in the $\mathrm{H}_{\mathrm{DR}}^1$ of abelian
 varieties of a certain type, marked by a fixed isomorphism
 $\mathrm{H}_{\mathrm{DR}}^1\cong V^\C$.


In the $p$-adic case, $\mathcal{D}^\vee$ will parametrize the Hodge
filtration $F^1$ of Dieudonn\'e modules of $p$-divisible groups of a
certain type (\ref{para:3.3.1}).
\end{para}

\begin{para}\label{para:5.1.2} More precisely, let us consider a moduli
 problem for $p$-divisible groups as in \ref{sub:4.1}, possibly
 decorated as in \ref{sub:4.3} (from which we follow the notation). The
 decoration reflects on the 
 Dieudonn\'e module $\D(\ovl{\Lambda})_\Q=\D(\ovl{\Lambda})\otimes \Q$:
 one has an isomorphism of $B_p$-module (with symplectic structure, in
 the polarized case):
 \begin{equation*}
  \D(\ovl{\Lambda})_\Q\cong
   V_p\otimes_{\Q_p}\widehat{\Q_p^{\mathrm{ur}}}.
 \end{equation*}
 We fix such an isomorphism, and consider that
 $G_{\Q_p}\otimes_{\Q_p}\widehat{\Q_p^{\mathrm{ur}}}$ acts on
 $\D(\ovl{\Lambda})_\Q$. But $\D(\ovl{\Lambda})_\Q$ has an extra
 structure: the $\sigma$-linear Frobenius automorphism. The group $J$ is
 nothing but the {\it subgroup} of $G_{\Q_p}(\widehat{\Q_p^{\mathrm{ur}}})$ of
 elements commuting with Frobenius.
\end{para}

\begin{para}\label{para:5.1.3} Let $\mathfrak{v}$ be the finite extension of
 $W={\Z_p^{\mathrm{ur}}}$ considered in \ref{para:4.3.2} and let $K$ be its 
 fraction field. We denote here by $F^1_0\subset V_p^{\C_p}=V_p\otimes
 \C_p$ the $\C_p$-span of the space
 $\omega_{\tilde{\ovl{\Lambda}}}\subset V_p\otimes_{\Q_p}K$ introduced in
 \ref{para:4.3.2}. We set $G_{\C_p}=G_{\Q_p}\otimes_{\Q_p}\C_p$.

 \noindent The flag variety $\mathcal{D}^\vee$ of all
 $G_{\C_p}$-conjugates of $F^1_0$ in $V_p^{\C_p}=\D(\ovl{\Lambda})
 \otimes_W\C_p$ is a homogeneous space 
 \begin{equation*}
  \mathcal{D}^\vee = P\backslash G_{\C_p}
 \end{equation*}
 for a suitable parabolic subgroup $P$. There is an
 ample line bundle $\mathcal{L}$ on $\mathcal{D}^\vee$
 which is homogeneous under the derived group $G_{\C_p}^{\mathrm{der}}$;
 \index{000GCpder@$G_{\C_p}^{\mathrm{der}}$}
 we denote by $\mathcal{D}^\vee \subset \P(W)$ an 
 associated $G_{\C_p}^{\mathrm{der}}$-equivariant projective embedding (if
 $G_{\C_p}=GL_{2g},\;\mathcal{D}^{\vee} = \Grass(g,2g)$, one 
 can just take the $SL_{2g}$-equivariant Pl\"ucker embedding).

 Note that, there is an obvious right action of $J$ on
 $\mathcal{D}^{\vee}$, which factors through the adjoint group
 $J^{\mathrm{ad}}:=\Im\bigl(J\rightarrow G_{\C_p}^{\mathrm{ad}}\bigr)$. 
\end{para}

\begin{para}\label{para:5.1.4} In our three basic examples (\ref{para:4.2.1}, \ref{para:4.2.2}, \ref{exa:4.3.4}), we
have $G_{\C_p}=GL_2$, hence $\mathcal{D}^\vee=\P^1_{\C_p}$.    
\end{para}
