---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-029-62-period-mappings
section_title: "Period mappings."
section_number: 6.2
pages: 72-76
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.896
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
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
