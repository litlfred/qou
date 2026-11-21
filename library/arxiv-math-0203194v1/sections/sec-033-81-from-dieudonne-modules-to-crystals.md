---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-033-81-from-dieudonne-modules-to-crystals
section_title: "From Dieudonn'e modules to crystals."
section_number: 8.1
pages: 79-80
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.967
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.1}

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
