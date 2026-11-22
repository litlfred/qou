---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-035-83-the-hodge-filtration
section_title: "The Hodge filtration."
section_number: 8.3
pages: 81-82
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.774
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.3}

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
