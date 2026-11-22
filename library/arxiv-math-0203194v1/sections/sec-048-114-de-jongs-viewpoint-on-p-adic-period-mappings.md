---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-048-114-de-jongs-viewpoint-on-p-adic-period-mappings
section_title: "De Jong's viewpoint on $p$-adic period mappings."
section_number: 11.4
pages: 99-101
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.849
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:6.4}

 J. de Jong \cite{efgonas} has proposed an interpretation of the
 period mapping which clarifies a lot the nature of its fibers. We
 briefly present this interpretation under the following mild simplifying
 assumption:

\begin{itemize}
 \item[$\ast$] that there is a family of 
 affinoid domains $(X_i)$ of $\mathcal{M}^0$ such that the
 $\mathcal{P}(X_i)$ (which are finite unions of affinoid domains in
 $\mathcal{D}$ since
 $\mathcal{P}$ is etale) form an admissible covering of $\mathcal{D}$. 
\end{itemize}

This assumption is fulfilled in our three basic examples (but not
always, \cf \cite[5.53]{psfpg}).

 Under $(\ast)$, De Jong shows (\loccit\footnote{of course
 $p=\ell$ throughout \S\S  6 and 7 of \loccit }, intr. and \ref{sub:7.2}) that
 there is an etale local system of 
 $\Q_p$-spaces $\mathcal{V}$ on $\mathcal{D}$ such that
 $\mathcal{M}^0$ is a component of the space of
 $\Z_p$-lattices in $\mathcal{V}$. Here, an ``etale local system
 of $\Q_p$-spaces'' is given by the data
 \begin{equation*}
  \mathcal{V}=(\{U_i\hookrightarrow \mathcal{D}\}, \mathcal{V}_i, \phi_{ij})
 \end{equation*}
 where $U_i\hookrightarrow \mathcal{D}$ are open immersions,
 $\mathcal{V}_i=\underset{n}{\limproj}
 \;\mathcal{V}_i/p^n\mathcal{V}_i$ are etale local systems of
 $\Z_p$-lattices (each $\mathcal{V}_i/p^n\mathcal{V}_i$ being a finite
 locally free sheaf of $\Z/p^n\Z$-modules on the etale site of $U_i$),
 and $ \phi_{ij}: (\mathcal{V}_i\otimes \Q_p)_{|
 U_i\times_\mathcal{D}U_j} \rightarrow (\mathcal{V}_j\otimes \Q_p)_{|
 U_i\times_\mathcal{D}U_j} $ are isomorphisms satisfying the usual
 cocycle condition (\cf \cite[4]{efgonas}).


 Of course, in the ``decorated case'', $\mathcal{V}$ inherits the
 relevant decoration.

 It follows from this interpretation that in example \ref{thm:4.1.2}, the
 fibers of the period mapping are in natural bijection with the set of
 vertices of the Bruhat-Tits tree $\mathcal{T}$.

 Similarly, in example \ref{exa:4.3.4}, one can see that the fibers of
 $\mathcal{P}$ are in bijection with the 
 one-point set $SL_1(B_p)/SL_1(\mathcal{B}_p)$, \cf \ref{para:7.4.4}.
\end{para}

\newpage

\section{$p$-adic uniformization of Shimura varieties.}\label{sec:7}

\begin{abst}
 Application of the theory of $p$-adic period mappings: Rapoport-Zink's
 $p$-adic uniformization theorem. The case of global uniformization.
 \v{C}erednik-Drinfeld uniformization of Shimura curves and
 other examples.
\end{abst}


\subsection{$p$-integral models of Shimura varieties.}\label{sub:7.1}

\begin{para}\label{para:7.1.1} Let $\Sh$ be a Shimura variety of PEL type as
 in \ref{para:1.1.4}. We recall the setting of \ref{para:1.1.4}: $B$ is
 a simple finite-dimensional $\Q$-algebra, with a positive involution
 $\ast$, $V$ is a $B$-module 
 of finite type, endowed with an alternate $\Q$-bilinear form such that
 $\an{bv,w}=\an{v,b^\ast w}$; 
 $G$ denotes the $\Q$-group of
 $B$-linear symplectic similitudes of $V$; $\mathcal{B}$ is a maximal
 order in $B$ stable under $\ast$, and 
 $L$ is a lattice in $V$, stable under $\mathcal{B}$ and autodual for
 $\an{\;,\;}$.

 The (non-connected) Shimura variety $\Sh$ is defined over the reflex
 field $E$ (which is a number field in $\C$).  There are variants of
 $\Sh$ in which the principal congruence subgroup of level $N$ of
 $G(\hat\Z)$ is replaced by any open compact subgroup $C$ of $G(\A_f)$,
 where $\A_f=\hat\Z\otimes \Q$ is the ring of finite adeles of $\Q$. The
 complex points of $\Sh$ admit the following adelic description
\begin{equation*}
\Sh(\C)=C\backslash \bigl((G(\R)^{\mathrm{ad}}.h_0) \times G(\A_f)\bigr) /G(\Q)
\end{equation*}
(\cf \ref{para:1.2.4} about the one-parameter group $h_0$). 
\end{para}

\begin{para}\label{para:7.1.2} We set $B_p=B\otimes_{\Q}
 \Q_p,\;\mathcal{B}_p=\mathcal{B}\otimes_\Z \Z_p,$ and so on. We denote
 by $C_p$ the stabilizer of $L_p$ in $G(\Q_p)$

 {\it We assume that $C$ is of the form $C^pC_p$} for some open compact
 subgroup $C^p$ of $G(\A_f^p)$, where $\A_f^p=(\prod_{\ell\neq
 p} \Z_\ell)\otimes \Q$. 


 In the case of a congruence subgroup of level $N$, this condition means
 that {\it the level is prime to $p$}. 

 We fix an embedding $v: E\hookrightarrow
 \C_p$, denote by $E_v$ the $v$-completion of $E$, by $\mathfrak{v}$ the
 discrete valuation ring
 $\widehat{\Z^{\mathrm{ur}}}.\mathcal{O}_{E_v}=
 \widehat{\Z^{\mathrm{ur}}}.\mathcal{O}_E$ 
 (compositum in $\C_p$), and by $K$ the fraction field of $\mathfrak{v}$.
\end{para}

\begin{para}\label{para:7.1.3} Let $S$ be a scheme. The objects of the the
 category of $S$-abelian schemes {\it up to prime to $p$ 
isogeny} are the abelian schemes over $S$; morphisms between $A $ and
$A'$ are global sections of $ \udl{\Hom}_S(A, A')\otimes_{\Z}\Z_{(p)}$,
where $\Z_{(p)}$ is the ring of rational numbers with denominator prime
to $p$. This is a $\Z_{(p)}$-linear category. Its relation to
$p$-divisible groups is given by the following elementary lemma:
\end{para}

\begin{lem}\label{lem:7.1.4} The faithful functor $A\mapsto A[p^\infty]$
\begin{equation*}
 \{\text{$S$-abelian schemes up to prime to $p$
  isogeny}\}\rightarrow \{\text{$p$-divisible groups over $S$}\}
\end{equation*}
is conservative, \ie reflects isomorphisms.
 


\end{lem}
The following result (which we state in a rather vague manner) is due to
R. Kottwitz \cite{possvoff} (Compare with \ref{para:1.2.4}.).

\begin{pro}\label{pro:7.1.5}
 For sufficiently small $C^p$, there is a moduli scheme $\Sh$ over
 $\mathcal{O}_{E_v}$ for isomorphism classes of abelian 
 varieties $A$ up to prime to $p$ isogeny, with $\mathcal{B}$-action 
 (with Shimura type condition), together with a $\Q$-homogeneous
 principal $\ast$-polarization and a class of $B$-linear symplectic
 similitudes $\mathrm{H}^1_{\mathrm{et}}(A,\A_f^p)\rightarrow \A_f^p\otimes V$
 modulo the group $C^p$. The generic fiber $\Sh
 \otimes_{\mathcal{O}_{E_v}}E_v$ is a finite sum of copies of
 $\Sh\otimes_E {E_v}$.
\end{pro}

In the case of a congruence subgroup of level $N$, this condition that
$C^p$ is sufficiently small means that $N$ is sufficiently large (and
kept prime to $p$).
