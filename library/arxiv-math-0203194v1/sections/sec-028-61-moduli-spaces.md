---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-028-61-moduli-spaces
section_title: "Moduli spaces."
section_number: 6.1
pages: 70-72
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.874
latex_coverage_ratio: 0.992
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:1.1}

\begin{para}\label{para:1.1.1} The term ``moduli'' was
 coined by Riemann to describe the continuous essential
 parameters of smooth complex compact curves of a given genus $g$. The use
 of this term has been extended to many classification problems in 
 analytic or algebraic
 geometry: typically, a classification problem consists of a discrete 
 part (the dimension, and other
 numerical invariants...) and a continuous part (the moduli). 

 One can distinguish between local and global moduli spaces: 

\begin{enumerate}
 \item local moduli are the parameters of the most general small (or
       infinitesimal) deformation of a given analytic manifold or
       algebraic variety. Let for instance $X$ be a compact analytic
       manifold.  Then a famous theorem of Kuranishi asserts that there
       is a local deformation $\pi: \udl{X}\rightarrow S$ with base
       point $s$ ($X={\udl{X}}_s$) such that any other deformation
       comes, locally around $s$, from $\pi$ by base change; moreover
       the tangent space of $S$ at $s$ is isomorphic to
       $\mathrm{H}^1(X,(\Omega^1_X)^\vee)$. For curves, the dimension of
       this space is $3g-3$ if $g\geq 2$ (the number of Riemann's
       complex moduli).
 \item Global moduli spaces, when they exist, provide the
       solution of the continuous part of moduli problems. For instance,
       Douady has constructed the global moduli space for closed analytic
       subspaces of a given compact complex manifold. Although global moduli
       spaces were already studied in the nineteenth century (in the case of
       curves), the concept was first put on firm foundations by Grothendieck
       in terms of representable functors.
\end{enumerate}

The existence of a global moduli space is often obstructed by the
presence of automorphisms of the objects under classification. One
possibility is to rule out these automorphisms by imposing some extra
structure (rigidification). When all automorphism groups are finite,
another possibility is to look for moduli orbifolds rather than moduli
spaces
\end{para}

\begin{para}\label{para:1.1.2}
 The most classical moduli problems concern complex elliptic
 curves. These are classified by their $j$-invariant. However the affine
 $j$-line ${\A}^1$ is not a fine moduli space: indeed, in any family of
 elliptic curves parametrized by the whole affine line, all the fibers
 are isomorphic.


 One can rigidify the problem by introducing a ``level $N$ structure''
 \index{levelNstructure@level $N$ structure} on 
 elliptic curves $E$, \ie fixing an identification $\Ker[N]_A\cong
 ({\Z}/N{\Z})^2$ such that the Weil pairing is given by
 $(\xi,\eta)\mapsto \exp(2\pi i(\xi\wedge\eta))$ (here $[N]_A$ denotes the
 multiplication by $N$ on the elliptic curve $A$).


For $N\geq 3$, this rules out automorphisms of $A$, and the
corresponding moduli functor is representable. For $N=3$, the moduli
space is ${\A}^1\setminus \{\mu^3=1\}$; the universal elliptic curve
with level $3$ structure is the Dixon elliptic curve
\begin{equation*}
 x^3+y^3+3\mu xy = 1 \text{ (in affine coordinates $x,y$)}
\end{equation*}
with $\Ker[3]_A=$ the set of flexes.


For $N=2$, the automorphism $[-1]_A$ remains; there is an elliptic curve
with level $2$ structure over ${\P}^1\setminus \{0,1,\infty\}$, namely
the Legendre elliptic curve
\begin{equation*}
 y^2=x(x-1)(x-\lambda) \text{ (in affine coordinates $x,y$)}
\end{equation*} 
with
$\Ker[2]_A=\{(0,0),(1,0),(\lambda, 0),(\infty,\infty)\}$, but it is not
universal: another one is given by $\lambda y^2=x(x-1)(x-\lambda)$.
\end{para}

\begin{para}\label{para:1.1.3}
 These moduli problems admit two natural generalizations: moduli
 problems for curves of higher genus, and moduli problems for polarized
 abelian varieties (polarizations ensure that the automorphism groups
 are finite).

 There is a moduli orbifold for smooth compact complex curves of genus
 $g>0$, denoted by $\mathcal{M}_g$, which can be described as
 follows. The set of complex structures on compact connected oriented
 surface $S_g$ of genus $g$ is in a natural way a contractible complex
 manifold of dimension $3g-3$ (\resp the Poincar\'e upper half plane
 $\mathfrak{h}$ if $g=1$), the Teichm\"uller space $\mathcal{T}_g$. The
 mapping class group $\Gamma_g$, \ie the component of connected
 components of the group of orientation-preserving self-homeomorphisms of
 $S_g$, acts on right on $\mathcal{T}_g$, and $\mathcal{M}_g$ is the
 quotient $\mathcal{T}_g/\Gamma_g$. For $g=1$, one recovers
 $\mathcal{M}_1=\mathfrak{h}/SL(2,{\Z})$.


There is a moduli orbifold for principally polarized abelian varieties of
dimension
$g>0$, denoted by $\mathcal{A}_g$, which can be described as follows. For any
abelian variety $A$, one has an exact sequence 
\begin{equation*}
 0\rightarrow L\rightarrow \Lie A\rightarrow A\rightarrow 0
\end{equation*}
and a principal polarization corresponds to a positive
definite hermitian form $H$ on $\Lie A$ whose imaginary part induces a
perfect alternate form on $L$. Choosing a $\C$-basis
$\omega_1,\ldots,\omega_g$ of $\Omega^1(A)\cong (\Lie A)^\vee$ and a
symplectic $\Z$-basis $\gamma_1^+,\gamma_1^-,\ldots,\gamma_g^+,
\gamma_g^-$ of $L$ gives rise to a period matrices 
$\Omega^+=(\int_{\gamma^+_j}\omega_i)$, $\Omega^-=(\int_{\gamma^-_j}\omega_i)$,
and $\tau=(\Omega^-)^{-1}\Omega^+$ does not depend on the
$\omega_i$'s.  By the properties of $H$, $\tau$ belongs to the Siegel
upper half space $\mathfrak{h}_g$ of symmetric matrices with positive
definite imaginary part (Riemann relations); it is well-defined up to
right multiplication by a matrix in $Sp(2g,{\Z})$ (which is the same as
the standard left action on $\mathfrak{h}_g$ of the transposed
matrix). This construction identifies $\mathcal{A}_g$ with
$\mathfrak{h}_g/Sp(2g,{\Z})$.


The construction which associates to a curve its jacobian variety with
the principal polarization given by the theta divisor gives rise to an
immersion $\mathcal{M}_g\hookrightarrow\mathcal{A}_g$, the Torelli map.
\end{para}

\begin{para}\label{para:1.1.4}
 Following G.~Shimura, one also studies refined moduli problems for
 ``decorated'' (principally polarized) abelian varieties, by prescribing
 in addition that the endomorphism algebra contains a given simple
 $\Q$-algebra, and imposing a level $N$ structure. This gives rise to
 moduli orbifolds (\resp moduli spaces if $N\geq 3$) of ``PEL type''.

 More precisely, let $B$ be a simple finite-dimensional $\Q$-algebra,
 with a positive involution $\ast$. Let $V$ be a $B$-module of finite
 type, endowed with an alternate $\Q$-bilinear form such that
 $\an{bv,w}=\an{v,b^\ast w}$.  One denotes by $G$ the algebraic $\Q$-group of
 $B$-linear symplectic similitudes of $V$.

 Let $\mathcal{B}$ be a maximal order in $B$ stable under $\ast$, and
let $L$ be a lattice in $V$, stable under $\mathcal{B}$ and autodual for
$\an{\;,\;}$ (this will represent the structure of $\mathrm{H}^1(A,{\Z})$ for
the abelian varieties $A$ under consideration). We choose in addition a
lagrangian subspace $F^1_0\subset V_{\C}$ stable under $B$ (which
will be $\Omega^1(A_0)\cong (\Lie A_0)^\vee$ for one particular abelian
variety $A_0$ under consideration).

There is a moduli orbifold (\resp moduli space if $N\geq 3$)
for principally $\ast$-polarized\footnote{a principal
$\ast$-polarization is a symmetric $\mathcal{B}$-linear isomorphism
between the abelian variety and its dual, endowed with the transposed
action of $\mathcal{B}$ twisted by $\ast$} abelian varieties $A$,
together with a given action $\iota: \mathcal{B}\rightarrow \End A$
such that $\det(\iota(b)| \Omega^1(A))=\det(b| F^1_0)$ for all
$b\in \mathcal{B}$ (Shimura type condition), and a given
$\mathcal{B}/N\mathcal{B}$-linear symplectic similitude
$A[N]=\Ker[N]_A\rightarrow \Hom(L,{\Z}/N {\Z})$.


It amounts to the same to consider abelian varieties $A$ up to isogeny,
with $B$-action (with Shimura type condition), together with a
$\Q$-homogeneous principal $\ast$-polarization and a class of $B$-linear
symplectic similitudes $\mathrm{H}^1(A,{\hat {\Z}}\otimes
\Q)\rightarrow {\hat {\Z}}\otimes V$ modulo the group $\{g \in
G({\hat {\Z}}\otimes {\Q}) \mid (g-1)({\hat {\Z}}\otimes L)\subset {\hat
{\Z}}\otimes L\}$.

These moduli orbifolds are called Shimura orbifolds of ``PEL
type''. \index{PELtype@PEL type} They are algebraic, and defined over
 the number field 
$E={\Q}[\tr(b| F^1_0)]$ (the so-called reflex field). Their
connected components are defined over finite abelian extensions of $E$,
\cf \cite{tds}.
\end{para}
