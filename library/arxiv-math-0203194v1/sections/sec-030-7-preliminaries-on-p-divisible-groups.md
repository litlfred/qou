---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-030-7-preliminaries-on-p-divisible-groups
section_title: "Preliminaries on $p$-divisible groups."
section_number: 7
pages: 76-76
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.969
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sec:2}

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
