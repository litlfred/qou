---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-003-finite-semisimple-bimodule-categories-over-pivot
section_title: "Finite semisimple (bi)module categories over pivotal fusion categories"
section_number: null
pages: 9-9
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.982
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
\label{subsec:semisimple}
We focus on {\em finite semisimple} $(\mac,\mad)$-bimodule categories  over {\em fusion categories} $\mac$, $\mad$ and on $(\mac,\mad)$-bimodule functors and  natural transformations between them. In this case
all categories $\Fun_{(\mac,\mad)}(\mam,\man)$ are finite $\C$-linear abelian categories  \cite[Prop.~7.11.6]{EGNO} and  semisimple, see \cite[Th.~2.16]{ENO} by Etingof et al. 

Moreover, the  2-category  $\Bimod(\mac,\mad)$  of finite semisimple $(\mac,\mad)$-bimodule categories $(\mac,\mad)$-bimodule functors and $(\mac,\mad)$-bimodule natural transformations  is equipped with duals. Any $(\mac,\mad)$-bimodule functor $F:\mam\to\man$ between finite semisimple $(\mac,\mad)$-bimodule categories
has a left adjoint $F^l:\man\to\mam$ and a right adjoint $F^r:\man\to\mam$, and  these adjoints are also $(\mac,\mad)$-bimodule functors.  The left and right  duals of $F$  are  given by its left and right adjoint and  the units and counits of the adjunction.

This follows, because module functors between finite semisimple module categories are always exact, as finite semisimple module categories are exact and module functors between exact module categories are exact \cite[Prop.~7.6.9]{EGNO}. Any finite abelian $\C$-linear  category is equivalent to the category  of modules over some finite-dimensional semisimple $\C$-algebra \cite[Def.~1.8.5]{EGNO}. Any right exact $\C$-linear functor between such categories  is $\otimes$-representable \cite[Prop.~1.8.10]{EGNO}  and hence has a left adjoint, namely the corresponding Hom-functor. Analogously,  left exactness implies the existence of a right adjoint. 

 
 It follows that category $\End_\mac(\mam)$ is a finite multifusion category. It is a fusion category if and only if $\mam$ is {\em indecomposable}, that is, not the direct sum of non-trivial module categories,  see \cite[Sec.~7.3.6]{EGNO} and  the remark after \cite[Def.~7.2.12]{EGNO}. 
 The category $\mam$ is an $\End_\mac(\mam)$-module category with the action functor that applies endofunctors and natural transformations to objects and morphisms in $\mam$.
 


We also require  that the fusion categories $\mac$ and $\mad$ are {\em pivotal}. This has implications for the opposite bimodule category from Example  \ref{ex:dualcat}. 
 A $(\mad,\mac)$-bimodule structure on $\mam^{op}$ can be defined analogously to Example  \ref{ex:dualcat} for any fusion category $\mam$. However,  the category $\mam^{\#\#}$ is  in general not equivalent to the bimodule category $\mam$, and one needs to distinguish the $(\mad,\mac)$-bimodule category structures on $\mam^{op}$ that are induced by left and right duals, see the results by Douglas et al.~in \cite[Sec.~2.4]{DSS}. As shown in \cite{G14}, the pivotal structures of $\mac$ and $\mad$ relate their left and right duals and  eliminate this ambiguity. This justifies the name {\em opposite bimodule category}.
 

\begin{proposition}\label{ex:oppositebimod} \cite{G14, DSS}

 Let $\mac,\mad$ be pivotal fusion categories  and $\mam,\man$ finite semisimple $(\mac,\mad)$-bimodule categories.
\begin{compactenum}

\item  There are equivalences  $\Omega: \mam^{\#\#}\to \mam$ of $(\mac,\mad)$-bimodule categories with $F\Omega=\Omega F^{\#\#}$ for all $(\mac,\mad)$-bimodule functors $F:\mam\to\man$.

\item There are equivalences of  $(\mac,\mad)$-bimodule categories $\mam^\#\to \Fun_\mac(\mam,\mac)$ and $\mam^\#\to \Fun_{\mad^{rev}}(\mam,\mad)$.
\end{compactenum}
\end{proposition}

\begin{proof}
Claim 1.~is shown in \cite{G14}. As a functor $\Omega=\id_\mam$,  and its coherence isomorphisms are given by the pivots $\omega:**\Rightarrow \id$   as $s_{c,m}=\omega_c\rhd 1_m: c^{**}\rhd m \to c\rhd m$ and $t_{m,d}=1_m\lhd \omega^{\inv}_d: m\lhd d\to m\lhd d^{**}$.  The identity  $F\Omega=\Omega F^{\#\#}$ follows directly from the definition of $F^\#$ in Example \ref{ex:modulefuncs}, 7.~and formula \eqref{eq:bimodcomp} for the coherence data of a composite bimodule functor. 

Claim 2.~is essentially \cite[Prop.~2.4.9]{DSS} for  module categories over pivotal fusion categories. It follows by combining \cite[Prop.~2.4.9]{DSS} with 1.  The  $(\mad,\mac)$-bimodule structure on $\Fun_\mac(\mam,\mac)$  is given by  $(d\rhd F)(m)=F(m\lhd d)$ and $(F\lhd c)(m)=F(m)\oo c$ and  the one on $\Fun_{\mad^{rev}}(\mam,\mad)$ by   $(d\rhd F)(m)=d\oo F(m)$ and $(F\lhd c)(m)=F(c\rhd m)$ for all $c\in\Ob\mac$, $m\in\Ob\mam$ and $d\in\Ob\mad$. The equivalences are given by the left adjoints of the functors $-\rhd m: \mac\to\mam$  and $m\lhd-:\mad\to\mam$ from Example \ref{ex:modulefuncs}, 5.~and 6. 
\end{proof}
