---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-034-82-the-dieudonne-crystal-of-a-p-divisible-group
section_title: "The Dieudonn'e crystal of a $p$-divisible group."
section_number: 8.2
pages: 80-81
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.759
latex_coverage_ratio: 0.963
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.2}

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
