---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-020-62-period-mappings
section_title: "Period mappings."
section_number: 6.2
pages: 72-79
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.931
---
\label{sub:1.2} 

\begin{para}\label{para:1.2.1}
 In the case of curves, the construction of period mappings belongs to
 the nineteenth
 century. The idea is to study the deformations of a curve by looking at
 the variation of its periods.  Let $f:{\udl{X}}\rightarrow S$ be an
 algebraic family of projective smooth (connected) curves of genus $g$
 over $\C$. Let $\tilde S$ be the universal covering of $S$. Then the
 homology groups $\mathrm{H}_1(-,{\Z})$ of the fibers form a constant
 local system on $\tilde S$. Let us choose a symplectic basis
 $\gamma_1^+,\gamma_1^-,\ldots ,\gamma_g^+, \gamma_g^-$. Choosing,
 locally, an auxiliary $\C$-basis $\omega_1,\ldots,\omega_g$ of
 $f_\ast\Omega^1_{\udl{X} /S}$ gives rise as above to a period matrices
 $\Omega^+=(\int_{\gamma^+_j}\omega_i)$, 
 $\Omega^-=(\int_{\gamma^-_j}\omega_i)$,  
 and $\mathcal{P}=(\Omega^-)^{-1}\Omega^+$ does not depend on the
 $\omega_i$'s and is well-defined on $\tilde S$.


 We get a commutative square 

 \begin{equation*}
  \begin{CD}
   \til{S} @>\mathcal{P}>> \mathfrak{h}_g\\
   @VVV @VVV\\
   S @>\mathcal{P}>> \mathfrak{h}_g/Sp(2g,\Z)
  \end{CD}
 \end{equation*}
 Applying this construction to the universal case
 $S=\mathcal{M}_g$ ($\mathcal{T}_g=\til{\mathcal{M}}_g$ in the orbifold
 sense), the bottom line of this commutative square is nothing but an
 analytic interpretation of the Torelli map.
\end{para}

\begin{para}\label{para:1.2.2}
 An important feature of the period mapping $\mathcal{P}$ is that it is
 a {\it quotient of solutions of a fuchsian differential system}, with
 rational exponents at infinity. This comes out as follows. The vector
 bundle $f_\ast\Omega^1_{\udl{X} /S}$ is a subbundle (of rank $g$) of a
 vector bundle $\mathcal{H}$ (of rank $2g$) whose fibers are the De Rham
 cohomology spaces $\mathrm{H}^1_{\mathrm{DR}}(\udl{X}_s)$. This bundle
 $\mathcal{H}$ carries an integrable connection, the Gauss-Manin
 connection
 \begin{equation*}
  \nabla_{\mathrm{GM}}:\;\mathcal{H}\rightarrow \Omega^1_S\otimes \mathcal{H}.
 \end{equation*}
 The local system of germs of horizontal analytic sections is
 $R^1f_\ast{\C}$ (with fibers
 $\mathrm{H}^1(\udl{X}_s,{\C})$). Completing, locally, the basis
 $\omega_1,\ldots,\omega_g$ of sections of $f_\ast\Omega^1_{\udl{X}/S}$
 into a basis $\omega_1,\ldots,\omega_g,\eta_1,\ldots,\eta_{g}$ of
 sections $\mathcal{H}$ allows to write the connection in form of a
 differential system, and a full {\it solution matrix} is given by the
 ``full $2g\times 2g$-period matrix''
 \index{full 2g 2g-period matrix@full $2g\times 2g$-period matrix} 
 $\begin{pmatrix} \Omega^+ &
  \Omega^- \cr N^+ & N^-  \end{pmatrix}$, while
 $\mathcal{P}=(\Omega^-)^{-1}\Omega^+$.


 In the case of the Legendre elliptic curve over ${\P}^1\setminus
 \{0,1,\infty\}$ (\cf I.\ref{sec-tale}), one finds that $\mathcal{P}$
 is given by the 
 quotient $\tau$ of two solutions of the hypergeometric differential
 equation with parameters $\bigl(\frac{1}{2},\frac{1}{2},1\bigr)$.
\end{para}

\begin{para}\label{para:1.2.3}
 The theory of period mappings has been generalized to any projective
 smooth morphism $f:\udl{X}\rightarrow S$ by P. Griffiths
 \cite{poioam3}.  We assume that $S$ and the fibers of $f$ are connected for
 simplicity.  The idea is the following: by abstracting the structure of
 the periods of the fibers of $f$, one arrives at the notion of
 polarized Hodge structure; one then construct a map from the universal
 covering $\tilde S$ to a classifying space $\mathcal{D}$ of polarized
 Hodge structures.

 For a fixed $n$, the real cohomology spaces
 $V_s^{\R}:= \mathrm{H}^n(\udl{X}_s,{\R})$) form a local system $V^{\R}$
 on $S$. We denote by $V^{\C}$ its complexification. The vector bundle
 $\mathcal{O}_S\otimes V^{\C}$ is the analytification of an algebraic
 vector bundle $\mathcal{H}$ on $S$, and $V^{\C}$ is the local system of
 germs of analytic solutions of an algebraic fuchsian integrable
 connection $\nabla_{\mathrm{GM}}$ on $\mathcal{H}$, the Gauss-Manin
 connection.

 On the other hand, the spaces $V_s^{\R}$ carry a natural algebraic
 representation of ${\C}^\times$ (Hodge structure), which amounts to a
 decomposition $V_s^{\C}=\bigoplus_{p+q=n,\;p\geq 0}
 \;V^{p,q},\;\;\overline{V^{p,q}}=V^{q,p}$. When $s$ varies, the
 filtrations
 \begin{equation*}
  F_s^p:=\bigoplus_{p'+q=n,\;p'\geq p} V^{p',q}
 \end{equation*}
 are the fibers of a decreasing filtration $F_s^p$ of $\mathcal{H}$ by
 vector subbundles (the Hodge filtration). The Gauss-Manin connection
 fails to preserve the Hodge filtration by just one notch:
 $\nabla_{\mathrm{GM}}(F^p)\subset \Omega^1_S\otimes F^{p-1}$.


 The last piece of data is the polarization: a bilinear form $Q$ on
 $V_s^{\R}$, $Q(v,v')=(-1)^nQ(v',v)$, such that $(-i)^nQ(v,\ovl{v})$ is
 hermitian on $V_s^{\C}$, definite (of sign $(-1)^p$) on each
 $V^{p,q}=F_s^p\cap \overline F_s^q$, and such that $F_s^p$ is the
 orthogonal of $F_s^{n-p-1}$ in $V_s^{\C}$.
 
 Let $G_{\R}$ denote the real group of similitudes of $Q$. The
 space of isotropic flags of type $0\subset \ldots \subset F_s^p\subset
 F_s^{p-1}\subset \ldots \subset V_s^{\C} \;$ is a homogeneous space
 \begin{equation*}
  \mathcal{D}^\vee = P\backslash G_{\C}
 \end{equation*}
 for a suitable parabolic subgroup $P$.  
 

 The flags satisfying the above positivity condition (on each $F_s^p\cap
 \ovl{F}_s^q$) are classified by an analytic open submanifold, the
 {\it period domain},
 \begin{equation*}
  \mathcal{D}\subset \mathcal{D}^\vee ;\;\; \mathcal{D}
   \cong K\backslash G_\R^{\mathrm{ad}}({\R})^{0}
 \end{equation*}
 \index{000GRad@$G_\R^{\mathrm{ad}}$}
 for a suitable compact subgroup $K\;$ ($\mathcal{D}^\vee$ is called the
 compact dual of $\mathcal{D}$).


Over $\tilde S$, the local system $V^{\C}$ becomes constant, and the
construction which attaches to any $s\in \tilde S$ the classifying point
of the corresponding flag $0\subset \ldots \subset F_s^p\subset
F_s^{p-1}\subset \ldots \subset V_s^{\C}\;$ gives rise to a holomorphic
mapping, the {\it period mapping}

 \begin{equation*}
  \tilde{S}\xrightarrow{\mathcal{P}} \mathcal{D}.
 \end{equation*}
 Via Pl\"ucker coordinates, $\mathcal{P}$ is again
 given by quotients of solutions of the Gauss-Manin connection
 $\nabla_{\mathrm{GM}}$.  The projective monodromy group of
 $\nabla_{\mathrm{GM}}$ is a 
 subgroup $\Gamma \subset G_{\R}^{\mathrm{ad}}$ (well-defined up to
 conjugation), and we get a commutative square

\begin{equation*}
 \begin{CD}
  \tilde{S}@>\mathcal{P}>> \mathcal{D} @. \subset \;\mathcal{D}^{\vee}\\
  @VVV @VVV @.\\
  S@>\mathcal{P}>> \mathcal{D}/\Gamma.
 \end{CD}
\end{equation*}
\end{para}

\begin{para}\label{para:1.2.4} In the simple case of a
 family of elliptic curves and $n=1$, $G_{\R}=GL_{2,\R}$, the flag space
 is just $\mathcal{D}^\vee={\P}^1_{\C}$, $K=PSO(2)$ (the isotropy group
 of $i\in {\P}^1_{\C}$ in $PSL_2({\R})=G_\R^{\mathrm{ad}}({\R})^0$), and
 $\mathcal{D}\cong K\backslash G_\R^{\mathrm{ad}}({\R})^0$ is the
 Poincar\'e upper half plane $\mathfrak{h}$.

 More generally, for a polarized abelian
 scheme, $G_{\R}$ is the group of symplectic similitudes, and
 $\mathcal{D}^\vee$ is the grassmannian of lagrangian subspaces of
 ${\C}^{2g}$, and $\mathcal{D}$ is the Siegel upper half space.

 \bigskip
 When one deals with refined moduli problems for abelian schemes with PEL
 decoration as in \ref{para:1.1.4}, one should work with the group $G_{\R}$ of
 $B$-{\it linear} symplectic similitudes of $V_{\R}$ (notation as in
 \ref{para:1.1.4}). In that case, the corresponding period domain
 $\mathcal{D}$ is a symmetric domain.

 More precisely, the datum of our $B$-stable lagrangian subspace
 $F^1_0\subset V_{\C}$ (attached to our particular $A_0$ with
 $\mathrm{H}^1(A_0,{\C})=V_{\C}$) amounts to the datum of an algebraic
 $\R$-homomorphism $h_0: {\C}^\times\rightarrow G_{\R}\subset
 GL(V_{\R})$ such that $h_0$ acts by the characters $z$ and $\ovl{z}$ on
 $V_{\C}$ ($F^1$ is the subspace where $h_0$ acts through $z$), and such
 that the symmetric form $\an{v,h(i) w}$ is positive definite on
 $V_{\R}$. For any abelian variety $A$ with PEL structure of the correct
 type, together with a fixed isomorphism $\mathrm{H}^1(A,{\C})\cong
 V_{\C}$, the corresponding subspace
 $F^1\mathrm{H}^1(A,{\C})=\Omega^1(A)\subset V_{\C}$ is an eigenspace
 for some conjugate of $h_0$. The set of conjugates of $h_0$ under
 $G({\R})$ is a finite union of copies of a symmetric domain
 $\mathcal{D}$.  \par For any component $S$ of the {\it Shimura
 orbifold}, we thus get a commutative square
 
 \begin{equation*}
  \begin{CD}
   \tilde{S}@>\mathcal{P}>> \mathcal{D} @. \subset\; \mathcal{D}^{\vee}\\
   @V\mathcal{Q}VV @VV\mathcal{Q}V @.\\
   S@>\mathcal{P}>> \mathcal{D}/\Gamma
  \end{CD}
 \end{equation*}
 \par\noindent
 where the horizontal maps are {\it isomorphisms}, $\mathcal{Q}$ denotes
 the quotient maps, and $\Gamma$ is a congruence subgroup of level $N$
 in the semi-simple group $G^{\mathrm{ad}}$ (a conjugate of the standard
 one).

 \bigskip
 The complex manifold $\tilde S$ admits the following
 modular description. Let $U$ be the oriented real Lie group
 $\Hom(L,(\R/\Z)^\times)$ (with $\mathcal{B}$-action and polarization),
 and let $\hat U$ be the associated infinitesimal Lie group. The
 automorphism group $J$ of the decorated $\hat U$ coincides with
 $G(\R)^0$. Then $\tilde S$ is a moduli space for {\it marked} decorated
 abelian varieties, where the marking is an isomorphism $\rho: \hat
 A\rightarrow \hat U$ of associated infinitesimal decorated oriented
 real Lie groups (note that, by taking duals of Lie algebras, $\rho$
 amounts to an $B$-linear symplectic isomorphism
 $\mathrm{H}^1(A,\R)\cong V^{\R}$). Note that the standard right action
 of $J$ on $\tilde S$ is obtained by functoriality.

\newpage

\section{Preliminaries on $p$-divisible groups.}\label{sec:2}

\begin{abst}
 Definitions and basic theorems about $p$-divisible groups,
 quasi-isogenies, liftings and deformations.
\end{abst}
\end{para}


\subsection{$p$-divisible groups and quasi-isogenies.}\label{sub:2.1}

\begin{para}\label{para:2.1.1} We begin with four definitions. Let $S$ be a scheme. Let
$\Lambda$ and $\Lambda'$ be commutative group schemes over $S$.  

A
homomorphism $f:\Lambda \rightarrow \Lambda'$ is called an {\it isogeny}
if it is an (f.p.p.f.) epimorphism with finite locally free kernel.


Let $p$ be a prime number. $\Lambda$ is a {\it $p$-divisible group}
(or Barsotti-Tate group) if $\displaystyle
\Lambda=\underset{n}{\liminj}\Ker [p^n]$ and for all $n$, the multiplication
$[p^n]$ by $p^n$ on $\Lambda$ is an isogeny.

\par\noindent If $S$ is connected, the rank of $\Ker [p^n]$ is then of
the form $p^{hn}$, where $h$ is an integer called the height of $\Lambda$.  

From the fact that $[p]$ is an isogeny, it follows that for 
$p$-divisible groups, $\Hom_S(\Lambda,\Lambda')$ is a torsion-free 
${\Z}_p$-module. 

A {\it quasi-isogeny} of $p$-divisible groups $\Lambda, \Lambda'$ is a
global section $\rho$ of the Zariski sheaf $ \udl{\Hom}_S(\Lambda,
\Lambda')\otimes_{\Z}{\Q}$ such that there exists locally an integer $n$
for which $p^n\rho$ is an isogeny. By abuse, one writes $\rho: \Lambda
\rightarrow \Lambda'$ as for homomorphisms. We denote by
$\qisog_S(\Lambda, \Lambda')$\index{000qisog@qisog} the ${\Q}_p$-space of
quasi-isogenies.


The objects of the category of {\it $p$-divisible groups on $S$ up
to isogeny} are the $p$-divisible groups over $S$; morphisms between
$\Lambda $ and $\Lambda'$ are global sections of $ \udl{\Hom}_S(\Lambda,
\Lambda')\otimes_{\Z}{\Q}$. This is a $\Q_p$-linear category.
\end{para}

\begin{para}\label{para:2.1.2} The most important example of a
 $p$-divisible group is $\Lambda =A[p^\infty]$, the (inductive system
 of) $p$-primary torsion of an abelian scheme $A$ over $S$
 (\cite{pg}); in this case, the height 
$h$ is twice the relative dimension of $A$. 
\end{para}

\begin{para}\label{para:2.1.3}
 When $p$ is locally nilpotent on $S$, any $p$-divisible group $\Lambda$
 over $S$ is formally smooth; the completion $\hat\Lambda$ of a
 $p$-divisible group $\Lambda$ along the zero section is a formal Lie
 group \cite[VI,3.1]{grothendieck74:_group_barsot_tate_dieud}.  However
 ${\hat\Lambda}$ is not necessarily 
 itself a $p$-divisible group; it is if and only if the separable rank of
 the fibers of $\Ker[p]$ is a locally constant function on $S$ (in which
 case $\Lambda$ is an extension
 \begin{equation*}
  1\rightarrow \hat{\Lambda}\rightarrow \Lambda\rightarrow
   \Lambda^{\mathrm{et}}\rightarrow 1 
 \end{equation*} 
 of an ind-etale $p$-divisible group $\Lambda^{\mathrm{et}}$ by the
 infinitesimal $p$-divisible group $\hat\Lambda$, \cf
 \cite[III,7.4]{grothendieck74:_group_barsot_tate_dieud}).
 An example of an ind-etale (\resp infinitesimal)
 $p$-divisible group of height $h=1\;$ is
 $\displaystyle {\Q}_p/{\Z}_p=\underset{n}{\liminj} {\Z}/p^n{\Z}$ (\resp
 $\hat {\G}_m$).
\end{para}


\subsection{Two theorems on $p$-divisible groups.}\label{sub:2.2} 

\begin{para}\label{para:2.2.1}
 A considerable amount of work has been
 devoted to $p$-divisible groups and their 
 applications to the $p$-adic study of abelian varieties and their local
 moduli. Among the pioneers, let us mention: Barsotti, Tate, Serre,
 Grothendieck, Lubin, Messing...


 In the sequel, we shall outline the main concepts and results of the
 Rapoport-Zink theory of period mappings for $p$-divisible groups,
 emphasizing the analogy with the complex case. We refer to their book
 \cite{psfpg} for details and proofs. We shall also emphasize the
 relation to differential equations, which does not appear in
 \cite{psfpg}.

 The whole theory relies upon three basic theorems on $p$-divisible
 groups and their Dieudonn\'e modules, which we shall recall below:


 \begin{enumerate}
  \item the rigidity theorem for $p$-divisible groups up to isogeny,
  \item the Serre-Tate theorem, and
  \item the Grothendieck-Messing theorem,
 \end{enumerate}

 \noindent
 which deal with infinitesimal deformations of $p$-divisible groups.
\end{para}

\begin{para}\label{para:2.2.2} Let $\mathfrak{v}$ be a complete discrete
valued ring $\mathfrak{v}$ of mixed characteristic $(0,p)$. Let 
$\Nil_\mathfrak{v}$ denote the category of locally noetherian 
$\mathfrak{v}$-schemes $S$ on which $p$ is locally nilpotent.  For any
$S$ in $\Nil_\mathfrak{v}$, the ideal of definition 
$\mathcal{J}=\mathcal{J}_{S_{\mathrm{red}}}$ of the closed subscheme $S_{\mathrm{red}}$ 
(of characteristic $p$) is locally nilpotent.
\end{para}

\begin{thm}[Rigidity theorem for $p$-divisible groups up to isogeny]
 \label{thm:2.2.3}
 
 Every homomorphism
 $\;\ovl{\rho}:\;\Lambda\times_S S_{\mathrm{red}} \rightarrow \Lambda'\times_S
 S_{\mathrm{red}}$ of $p$-divisible groups up to isogeny admits a unique lifting
 $\rho: \Lambda \rightarrow \Lambda'$. Moreover, $\rho$ is a
 quasi-isogeny if $\ovl{\rho}$ is.
\end{thm}

\begin{proof}
 (following an argument of V. Drinfeld). We may assume that $S$ is
 affine, and that $\mathcal{J}$ is nilpotent. Then the connected part
 ${\hat\Lambda'}$ is a formal Lie group, hence there is a power $p^n$ of
 $p$ such that for any affine $S$-scheme $S'$, ${\hat\Lambda}'(S')$ is
 killed by $[p^n]$ (in fact if $\mathcal{J}^{r+1}=0$ on $S$, one can take
 $n=r^2$).

 We observe that $\Ker(\Lambda'(S')\rightarrow
 \Lambda'(S'_{\mathrm{red}}))= {\hat\Lambda}'(S')$. We have
 \begin{align*}
 &\Ker(\Hom(\Lambda(S') ,
 \Lambda'(S'))\rightarrow \Hom(\Lambda(
 S'_{\mathrm{red}}) , \Lambda'(S'_{\mathrm{red}}) )\\
 =&
 \Hom (\Lambda(S') ,\Ker(\Lambda'(S')
 \rightarrow \Lambda'(S'_{\mathrm{red}}))) 
 \end{align*}
 which is zero because $\Ker(\Lambda'(S')\rightarrow
 \Lambda'(S'_{\mathrm{red}})$ is killed by $[p^n]$ while $\Lambda$ is
 $p$-divisible.

 \noindent This implies the injectivity of
 $\qisog_S(\Lambda , \Lambda') \rightarrow 
 \qisog_{S_{\mathrm{red}}}(\Lambda\times_S S_{\mathrm{red}} ,
 \Lambda'\times_S S_{\mathrm{red}}) $ (taking into account the fact that 
 $\Hom(\Lambda( S'_{\mathrm{red}}), \Lambda'(S'_{\mathrm{red}}) )$ is
 torsion-free).

 \noindent For the surjectivity, let us first show that for any
 ${\ovl{f}}\in \Hom(\Lambda(S'_{\mathrm{red}}),
 \Lambda'(S'_{\mathrm{red}}))$, there is 
 a lifting $g\in \Hom(\Lambda(S'), \Lambda'(S'))$ of $p^n {\ovl{f}}$. For
 any $x\in \Lambda( S')$, let $\ovl{x}$ denote its image in $\Lambda(
 S'_{\mathrm{red}})$. Since $\Lambda'$ is formally smooth,
 ${\ovl{f}}({\ovl{x}})$ 
 admits a lifting $y\in \Lambda'(S')$.  Since
 $\Ker(\Lambda'(S')\rightarrow \Lambda'(S'_{\mathrm{red}}))) $ is killed
 by $p^n$, 
 $g(x):=[p^n] y$ is well-defined. This construction provides the desired
 lifting $g$.

 It remains to show that $g$ is an isogeny if
 $\ovl{f}$ is. Let $\ovl{f}'$ be a quasi-inverse of $\ovl{f}$
 ($\ovl{f}'\ovl{f}=[p^m]$), and $g'$ be a lifting of $p^n\ovl{f}'$. Then
 $g'g=[p^{2n+m}]$ by unicity of liftings. Thus $g$ is an epimorphism, and
 the subscheme $\Ker g$ of $\Ker [p^{2n+m}]$ is finite over $S$. On the
 other hand, $\Lambda$ is flat over $S$ and the fibers of $g'$ are flat
 (being isogenies). The criterium of flatness fiber by fiber
 \cite[11.3.10]{ega44} implies that $g'$ is flat, and we conclude that
 it is an isogeny.
\end{proof}

Let us observe that there is variant of both the statement and the
proof of \ref{thm:2.2.3} for abelian schemes, instead of $p$-divisible groups. 

 The next theorem asserts that deforming an abelian scheme of
 characteristic 
 $p$ is equivalent to deforming its $p$-divisible group. For any $S $ in
 $\Nil_\mathfrak{v}$, let $\Def_{p\text{-div}}(S)$ be the category of
 triples $(\ovl{A},\Lambda, \epsilon)$ consisting of an abelian scheme
 over $S_{\mathrm{red}}$, a $p$-divisible group $\Lambda$ over $S$ and an
 isomorphism $\epsilon: \ovl{A}[p^\infty]\cong \Lambda\times_S S_{\mathrm{red}}$.

\begin{thm}[The Serre-Tate theorem]\label{thm:2.2.4}
 The functor
 \begin{equation*}
  A\;\mapsto \;(A_{\mathrm{red}},\;\Lambda=A[p^\infty],
   \;\epsilon: A_{\mathrm{red}}[p^\infty]\cong \Lambda\times_S S_{\mathrm{red}})
 \end{equation*}
 induces an equivalence of categories between the
 category of abelian schemes over $S$ and the category
 $\Def_{p\text{-div}}(S)$.
\end{thm}


We again follow Drinfeld's argument \cite{copsr}, \cf also \cite{slm}.
We may assume that $S$ is affine and that
$\mathcal{J}^{n+1}=0$. We begin with the full faithfulness: given a
homomorphism $f^\infty: A[p^\infty]\rightarrow B[p^\infty]$ such that
$f^\infty$ $\pmod{\mathcal{J}}$ comes from a homomorphism $\ovl{f} :
A_{\mathrm{red}}\rightarrow B_{\mathrm{red}}$ of abelian schemes over $S_{\mathrm{red}}$, we have
to show that there exists a unique homomorphism $f: A\rightarrow B$
compatible with $f^\infty$ and $\ovl{f}$. The unicity follows from the
injectivity of $\Hom(A,B)\rightarrow \Hom(A_{\mathrm{red}},B_{\mathrm{red}})\;$
(\ref{thm:2.2.3}). Furthermore, \ref{thm:2.2.3} shows the existence of a
homomorphism $g$ 
compatible with $\;p^nf^\infty$ and $p^n\ovl{f}$. To show the existence
of an $f$ such that $g=p^nf=f\circ [p^n]$, the point is to show that $g$
kills $A[p^n]$, which can be seen on $g^\infty$.


For the essential surjectivity, we have to construct an abelian scheme
$A$ over $S$ compatible with a given datum $(\ovl{A},\Lambda, \epsilon)$
in $\Def_{p\text{-div}}(S)$.  By unicity of liftings, it suffices to do so
locally on $S$.  hence we may assume that $S$ is affine, and choose an
abelian scheme $A'$ over $S$ and an isogeny $A'_{\mathrm{red}}\rightarrow
\ovl{A}$. By the above argument, $p^n$ times the given isogeny
$A'_{\mathrm{red}}\rightarrow \ovl{A}$ lifts to a (unique) isogeny
$e:\;A'[p^\infty ]\rightarrow \Lambda$ of $p$-divisible groups over
$S$. Its kernel is a finite locally free subgroup scheme of $A'$, and we
can form the abelian scheme $A'':=A'/\Ker e$. The isogeny $A''[p^\infty
]\rightarrow \Lambda$ induced by $e$ is an isomorphism
$\pmod{\mathcal{J}}$, hence is an isomorphism.

\begin{para}\label{para:2.2.5} In the sequel, we shall have to deal
 occasionally with $p$-divisible groups over formal schemes rather 
than over schemes. Our formal schemes $\mathfrak{X}$ will be adic,
locally noetherian; hence there is a largest ideal of definition
$\mathcal{J}\subset \mathcal{O}_{\mathfrak{X}}$, and
$\mathfrak{X}=\liminj \;{\mathfrak{X}}_n\;,\;{\mathfrak{X}}_n =
\Spec(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})\;\;
({\mathfrak{X}}_{\mathrm{red}}={\mathfrak{X}}_0)\;$.

A $p$-divisible group $\Lambda$ over $\mathfrak{X}$ will be an inductive
system of $p$-divisible groups $\Lambda_n$ over $\mathfrak{X}_n$ such
that $\Lambda_{n+1}\times_{{\mathfrak{X}}_{n+1}}{\mathfrak{X}}_n\cong
\Lambda_n$.

\newpage
