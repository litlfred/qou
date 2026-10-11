---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-021-8-a-stroll-in-the-crystalline-world
section_title: "A stroll in the crystalline world."
section_number: 8
pages: 79-82
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.97
---
\label{sec:3}

\begin{abst}
 Review of Dieudonn\'e modules, crystals, Grothendieck-Messing theory,
 convergent isocrystals.
\end{abst}
\end{para}


\subsection{From Dieudonn\'e modules to crystals.}\label{sub:3.1}

\begin{para}\label{para:3.1.1}
 At first, Dieudonn\'e theory presents itself as an analogue of Lie
 theory for formal Lie groups over a perfect field $k$ of characteristic
 $p>0$. In practice, its scope is limited to the case of {\it
 commutative} formal Lie groups (in which case the classical counterpart
 is not very substantial). The theory extends to the case of
 $p$-divisible groups over $k$.


 Let $W$ be the Witt ring of $k$, with its Frobenius automorphism
 $\sigma$. The theory associates to any 
 $p$-divisible group $\Lambda$ over $k$ a {\it Dieudonn\'e module}, \ie a
 finitely generated free module over $W$ 
 endowed with a $\sigma$-linear Frobenius $F$ and a $\sigma^{-1}$-linear
 Verschiebung 
 $V$ satisfying $FV=VF=p.\id$ (we work with the contravariant theory: 
 ${\D}(\Lambda)=\Hom(\Lambda , \mathcal{W}_k)$, 
 \index{000D@$\D$}
 where $\mathcal{W}_k\;$
 is the Witt scheme of $k$). This provides an 
 {\it anti-equivalence of categories between $p$-divisible groups over
 $k$ and Dieudonn\'e modules}. The rank of 
 ${\D}(\Lambda)$ is the height $h$ of $\Lambda$. 
\end{para}

\begin{exs}
  $\bullet \;\;{\D}(\Q_p/\Z_p)=W,$ with $F=\sigma,
 \;V=p\sigma^{-1}$. 
 \par\noindent $\bullet\;\; {\D}(\hat\G_m)=W(-1)$, \ie $W$ as an
 underlying module, with $F=p\sigma, 
 \;V=\sigma^{-1}$.
 \par\noindent $\bullet$ When
 $\Lambda=A[p^\infty]$ for an abelian variety $A$ over $k$,
 ${\D}(\Lambda)$ may be identified with 
 $\mathrm{H}^1_{\mathrm{cris}}(A/W)$. 
\end{exs}

 However, the structure of Dieudonn\'e modules is rather complicated in
 general unless one inverts $p$. 

\begin{para}\label{para:3.1.2}
 When $k$ is algebraically closed, Dieudonn\'e modules $\otimes \Q$ were
 completely classified by Dieudonn\'e (this provides a classification of
 $p$-divisible groups over $k$ up to isogeny). They are classified by
 their {\it slopes} $\lambda\in [0,1]\cap \Q$ and multiplicities
 $m_\lambda\in \Z_{>0}$ (these data are better recorded in the form of a
 Newton polygon). This comes as follows: each Dieudonn\'e module $\D$
 has a canonical increasing finite filtration by Dieudonn\'e submodules
 $\D_\lambda$, such that the associated graded $W$-module is free, and
 with the following property: if $\lambda=a/b$ in irreducible form,
 $\Gr_\lambda\otimes \Q$ admits a basis of $m_\lambda$ vectors $x$
 satisfying $F^bx=p^ax$.


 For instance, the slope of $W(-1)$ is $1$; the slope of the Dieudonn\'e
 module attached to 
 (the $p$-divisible group of) a supersingular elliptic curve over $k$ is
 $1/2$, with multiplicity $2$.
\end{para}

\begin{para}\label{para:3.1.3} The problem of generalizing Dieudonn\'e
 theory to $p$-divisible groups over more general bases $S$ (over which
$p$ is nilpotent) has been tackled and advertised by Grothendieck
 \cite{grothendieck74:_group_barsot_tate_dieud}, and further studied by many geometers.


 What should be the right substitutes for the $W$-modules ${\D}(\Lambda)$
 (\resp for the $W[\frac{1}{p}]$-spaces ${\D}(\Lambda)_{\Q}$)?


 Grothendieck's proposal was to define ${\D}(\Lambda)$ as a {\it
 $F$-crystal} on the crystalline site of $S$. 

 The right substitute for $W[\frac{1}{p}]$-spaces was proposed later by
 P. Berthelot and A. Ogus under the name of {\it convergent
 $F$-isocrystal}. Let us describe these notions.
\end{para}



\subsection{The Dieudonn\'e crystal of a $p$-divisible group.}\label{sub:3.2}

\begin{para}\label{para:3.2.1} Let $\mathfrak{v}$ be a finite extension of
 $W$ of degree $e$. We assume that $e<p$, and that $\varpi$ is a 
 uniformizing parameter of $\mathfrak{v}$ such that $\sigma$ extends to 
 $\mathfrak{v}$ by setting $\sigma(\varpi)=\varpi$.


Let $S$ be in $\Nil_\mathfrak{v}$. An
$S$-divided power thickening
$T_0\hookrightarrow T$ is given by
\begin{enumerate}
 \item an $S$-scheme $T_0$,
 \item a $\mathfrak{v}$-scheme $T$ on which $p$ is locally nilpotent,
 \item a closed immersion $T_0\hookrightarrow T$ over $\mathfrak{v}$,
 \item a collection of maps ``$\frac{x^n}{n!}$'' from the ideal of
 definition of $T_0$ in $T$ to $\mathcal{O}_T$, which 
 satisfy the formal properties of the divided powers. 
\end{enumerate}

 $S$-divided power thickenings form a category
 $(S/\mathfrak{v})_{\mathrm{cris}}$ (a fppf site). A sheaf on
 $(S/\mathfrak{v})_{\mathrm{cris}}$ is the data, for every
 $T_0\hookrightarrow T$, of a fppf sheaf $\mathcal{E}_{T_0,T}$ on $T$,
 and for every morphism $f: (T_0\hookrightarrow T)\rightarrow
 (T_0'\hookrightarrow T')$ in $(S/\mathfrak{v})_{\mathrm{cris}}$, of a
 homomorphism $f^\ast\mathcal{E}_{T_0,T}\rightarrow
 \mathcal{E}_{T_0',T'}$ satisfying the obvious transitivity
 condition. Example: $\mathcal{O}_{S_0/\mathfrak{v}}$, defined by
 $(\mathcal{O}_{S/\mathfrak{v}})_{T_0,T}=\mathcal{O}_T$. Another example:
 any fppf sheaf $\mathcal{F}$ on $S_0$ gives rise to a sheaf
 $\mathcal{F}_{\mathrm{cris}}$ on $(S/\mathfrak{v})_{\mathrm{cris}}$ by
 $(\mathcal{F}_{\mathrm{cris}})_{T_0,T}=\mathcal{F}_{T_0}$.

 A {\it crystal} on $(S/\mathfrak{v})_{\mathrm{cris}}$ (or,
 abusively, on $S$) is a sheaf $\mathcal{E}$ of
 $\mathcal{O}_{S/\mathfrak{v}}$-modules on
 $(S/\mathfrak{v})_{\mathrm{cris}}$ such that the homomorphisms
 $f^\ast\mathcal{F}_{T_0,T}\rightarrow \mathcal{F}_{T_0',T'}$ are
 isomorphisms (in Grothendieck's terms: ``crystals grow and are
 rigid''). One denotes by $\mathcal{E}_T$ the $\mathcal{O}_T$-module
 obtained by evaluating the crystal on $(\id: T\hookrightarrow T) \in
 (S/\mathfrak{v})_{\mathrm{cris}}$.

 Because of this rigidity, and using the canonical divided powers on the
 ideal $\varpi\mathcal{O}_S$ (since $e<p,\;\frac{\varpi^n}{n!}\in
 \mathfrak{v}$ for any $n$), one gets an equivalence of categories
 between crystals on $S$ and crystals on the scheme $S_0=S/\varpi$ of
 characteristic $p$.
\end{para}

\begin{para}\label{para:3.2.2}
 The Dieudonn\'e crystal attached to a $p$-divisible group $\Lambda$
 over $S$ is the crystalline $\mathcal{E}xt$-sheaf
 $\mathcal{E}xt^1(\Lambda_{\mathrm{cris}},
 \mathcal{O}_{S/\mathfrak{v}})$. It can be shown that ${\D}(\Lambda)$ is
 a finite locally free crystal on $S$, of rank the height of
 $\Lambda$. It depends functorially in $\Lambda$ (in a contravariant
 way).

 An important, though formal, consequence of the crystalline local
 character of this definition is that {\it the formation of
 ${\D}(\Lambda)$ commutes with base change in}
 $(S/\mathfrak{v})_{\mathrm{cris}}$, and for any $S$-divided power
 thickening $(T_0\hookrightarrow T)$, there is a canonical isomorphism
 of $\mathcal{O}_T$-modules ${\D}(\Lambda)_{T_0,T}\cong
 {\D}(\Lambda_{T_0})_{T_0,T}.$

 It follows that the datum of ${\D}(\Lambda)$ amounts to the datum of
 ${\D}(\Lambda\times_S S_0)$: the Dieudonn\'e crystal depends only on the
 $p$-divisible group modulo $\varpi$.
\end{para}

\begin{para}\label{para:3.2.3}
 The pull-back of a crystal $\mathcal{E}$ on $S_0$ via the absolute
 Frobenius $F_{S_0}$ is denoted by $\mathcal{E}^{(p)}$. An $F$-crystal
 structure on $\mathcal{E}$ is the datum of a morphism of crystals
 $F:\;\mathcal{E}^{(p)}\rightarrow \mathcal{E}$ which admits an inverse
 up to a power of $p$.

 If $\Lambda$ is a $p$-divisible group over $S_0$, ${\D}(\Lambda)$ is
 endowed by functoriality with a structure of $F$-crystal. The classical
 Dieudonn\'e module is obtained for
 $S_0=T_0=\Spec(k),\;T=\Spf(W)=\liminj\;\Spec(W/p^n)$.


 Although we shall not use this fact, let us mention that the
 ``Dieudonn\'e functor'' ${\D}$ from $p$-divisible groups on $S_0$ to
 $F$-crystals is fully faithful under further mild assumptions on $S_0$
 (and even an equivalence with values in the category of ``Dieudonn\'e
 crystals'', \ie finite locally free $F$-crystals for which $F$ admits an
 inverse up to $p$ --- the Verschiebung); without any further assumption on
 $S_0$, it induces an equivalence of categories between ind-etale
 $p$-divisible groups on $S_0$ and unit-root $F$-crystals (\ie finite
 locally free $F$-crystals for which $F$ is an isomorphism), 
 \cf \cite{tddc1}, \cite{jong95:_cryst_dieud}.
\end{para}



\subsection{The Hodge filtration.}\label{sub:3.3}

\begin{para}\label{para:3.3.1}
 Let $\Lambda^\vee$ be the (Serre) dual of $\Lambda$ (the $\liminj$ of
 the Cartier duals of the $\Lambda[p^n]$'s). There is a canonical,
 locally split, exact sequence of $\mathcal{O}_S$-modules
 \begin{equation*}
  0\rightarrow F^1\rightarrow {\D}(\Lambda)_S\rightarrow
   \Lie \Lambda^\vee\rightarrow 0
 \end{equation*}
 where $F^1=\CoLie \Lambda=\omega_\Lambda$ may be identified with the
 module of invariant differentials on the formal Lie group
 $\hat\Lambda$. In case $\Lambda$ is the $p$-divisible group attached to
 an abelian $S$-scheme $\udl{A}$, this exact sequence reduces to the
 Hodge exact sequence
 \begin{equation*}
  0\rightarrow F^1\rightarrow \mathrm{H}^1_{\mathrm{DR}}(\udl{A}/S)\rightarrow
   \Lie \udl{A}^\vee\rightarrow 0.
 \end{equation*}
\end{para}

\begin{para}\label{para:3.3.2}
 Now let $S_0\hookrightarrow S$ be a {\it nilpotent} divided power
 thickening (this means that the products
 ``$\frac{x_1^{n_1}}{{n_1}!}$''$\ldots$``$\frac{x_1^{n_m}}{{n_m}!}$'' vanish
 for $n_1+\ldots+n_m\gg 0$); this is for instance the case if
 $S_0=S/\varpi$ as before and $e<p-1$.


 The next theorem asserts that deformations of $p$-divisible
 groups are controlled by the variation of the Hodge filtration in the
 Dieudonn\'e module \cite{messing72:_barsot_tate}. For any $p$-divisible group
 $\ovl{\Lambda}$ on $S_0$, and any lifting $\Lambda$ over $S$, we have
 seen that ${\D}(\Lambda)_S$ identifies with ${\D}(\ovl{\Lambda})_S$,
 which is a lifting of ${\D}(\ovl{\Lambda})_{S_0}$ to $S$.
\end{para}

\begin{thm}[The Grothendieck-Messing theorem]\label{thm:3.3.3}
 The functor
 \begin{equation*}
  \Lambda\;\mapsto (\Lambda\times_S S_0,\;\omega_\Lambda)
 \end{equation*}
 induces an equivalence of categories between the category of
 $p$-divisible groups on $S$, and the category of pairs consisting of a
 $p$-divisible group $\ovl{\Lambda}$ over $S_0$ (Zariski-locally liftable
 to $S$) and a locally direct factor vector subbundle of
 ${\D}(\ovl{\Lambda})_S$ which lifts $\;\omega_{\ovl{\Lambda}}\subset
{\D}(\ovl{\Lambda})_{S_0}$.
\end{thm}


 We have already seen the faithfulness in \ref{thm:2.2.3}.  We just
 indicate here 
 the principle of proof of essential surjectivity and fullness. Working
 with nilpotent divided power thickenings allows one to construct, by
 the exponential method, a formally smooth group scheme
 $\;\E(\ovl{\Lambda})\;$ over $\;S\;$ together with a canonical
 isomorphism
 ${\D}(\ovl{\Lambda})_{S_0}=\Lie (\E(\ovl{\Lambda})\times_S{S_0})$, in
 such a way that the canonical exact sequence

 \begin{equation*}
  0\rightarrow \omega_{\ovl{\Lambda}}\rightarrow
   {\D}(\ovl{\Lambda})_{S_0}\rightarrow 
   \Lie \ovl{\Lambda}^\vee\rightarrow 0
 \end{equation*}
 lifts to an exact sequence of formally smooth group schemes
 \begin{equation*}
  0\rightarrow \omega_{\ovl{\Lambda}}\rightarrow
   \E(\ovl{\Lambda})\times_S{S_0}\rightarrow \ovl{\Lambda}^\vee\rightarrow 0
 \end{equation*}
 Via the exponential, it is equivalent to give a local summand $F^1$ of
 ${\D}(\ovl{\Lambda})_S$ which lifts
 $\;\omega_{\ovl{\Lambda}}$, or to give a vector sub-group scheme $V$ of
 $\E(\ovl{\Lambda})$ which lifts $\;\omega_{\ovl{\Lambda}}$. It then
 turns out that $\E(\ovl{\Lambda})/V$ is a 
 $p$-divisible group $\Lambda^\vee$, whose Serre dual is the looked for 
 $p$-divisible group $\Lambda$ over $S$: 
 $\Lambda\times_S S_0=\ovl{\Lambda}$ by duality, and $\omega_{\Lambda}=F^1$.
 

 The formation of $\E(\ovl{\Lambda})$ is functorial (contravariant in 
 $\ovl{\Lambda}$). If we have two $p$-divisible groups $\ovl{\Lambda}, 
 \ovl{\Lambda}'$ and a morphism $\ovl{f}:\;\ovl{\Lambda}=\Lambda\times_S 
 S_0\rightarrow \ovl{\Lambda}'=\Lambda'\times_S S_0$ such that 
 $\D(f)$ respects the $F^1$'s, then the homomorphism 
 $\E(\ovl{f}): \E(\ovl{\Lambda})\rightarrow \E(\ovl{\Lambda}')$ 
 preserves the vector subgroup schemes, hence induces a homomorphism 
 $f: \E(\ovl{\Lambda})/V\cong \Lambda\rightarrow 
 \E(\ovl{\Lambda}')/V'\cong\Lambda'$ which lifts $\ovl{f}$.


 The exponential construction becomes simpler when the ideal of $S_0$ in
 $S$ is of square zero (and endowed with the trivial divided
 powers). This is the case which will be used in the sequel.
