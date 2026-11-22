---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-001-2-a-brief-review-of-theories-of-class-s
section_title: "A brief review of theories of class S"
section_number: 2
pages: 11-12
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.993
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:review-S}

In \cite{Witten:1997sc, Gaiotto:2009we, Gaiotto:2009hg} a large and interesting
class of $\CN=2$, $d=4$ theories was studied.
These theories, which we call ``theories of class S,''
can be constructed by compactification and twisting of
$\CN=(2,0)$, $d=6$ theories.
Here we quickly review the basic features of this construction.

Fix a compact Riemann surface $C$, with $s$ punctures at points $\fs_1, \dots, \fs_s$.  Also fix a Lie algebra
$\fg$ of $ADE$ type.  In this paper we will focus on the case $\fg = A_{K-1}$.
We consider the $\CN=(2,0)$ theory $S[\fg]$ compactified on $C$, and partially twisted as described in \cite{Gaiotto:2009hg}.  $S[\fg]$ admits half-BPS codimension-2 defects; we put one
such defect $D_n$ at each puncture $\fs_n$.

The main statements of this paper will be independent of the choice of which type of defect
we put at each puncture, but it is useful to have an example in mind to fix ideas.
There is a class of \ti{regular} defects labeled by Young diagrams with
$K$ boxes \cite{Gaiotto:2009we, Gaiotto:2009hg}.
In particular we can consider a \ti{full} regular defect,
corresponding to the Young diagram with a single row.
Each full defect admits a natural mass deformation depending
on $K$ complex parameters $m_n^{(i)}$, with
$\sum_{i=1}^K m_n^{(i)} = 0$, which we are free to fix arbitrarily.

In any case, whatever collection $D$ of defects we choose, the compactification procedure yields an $\CN=2$, $d=4$ theory $S[\fg, C, D]$.  This theory is our main object of study.

The Coulomb branch of $S[\fg, C, D]$ consists of tuples $(\phi_2, \dots, \phi_K)$, where $\phi_r$ is an $r$-differential
on $C$ (i.e. a section of $K_C^{\otimes r}$), which is holomorphic away from the punctures $\fs_n$, and has some prescribed singular behavior
at the $\fs_n$.  For example, if we choose $D_n$ to be a full defect,
then the prescription is that
for each $r$, $\phi_r$ has a pole of order $r$ at $\fs_n$, with residue determined by a combination of the parameters $m_n^{(i)}$ \cite{Gaiotto:2009we, Gaiotto:2009hg}.
Having fixed $(\phi_2, \dots, \phi_K)$, the Seiberg-Witten curve is given by
\begin{equation} \label{eq:sw-curve}
 \Sigma = \{ \lambda: \lambda^K + \sum_{r=2}^K \phi_r \lambda^{K-r} = 0 \} \subset T^* C.
\end{equation}
$\Sigma$ is a $K$-fold branched cover of $C$.
Since $\Sigma$ sits inside $T^* C$ it carries a canonical 1-form,
the restriction of the Liouville 1-form, which by slight abuse of notation
we will also call $\lambda$.

In this paper it will be crucial to introduce a half-BPS \ti{surface defect} into
$S[\fg, C, D]$.  There is a canonical such defect $\bS_z$ \cite{Alday:2009fs,Gaiotto:2009fs,Gaiotto:2011tf}, depending only on a point $z \in C$
(and on a representation of $\fg$, but since we choose $\fg = A_{K-1}$ we can just
take the fundamental representation.)  When $z$ is generic, the defect $\bS_z$
has $K$ distinct massive vacua, which correspond to the $K$ solutions of \eqref{eq:sw-curve} at $z$;
locally we may denote these by $z^{(1)}, \cdots, z^{(K)}$.
From the point of view of the
$d=6$ theory $S[\fg]$, $\bS_z$ is obtained by inserting a surface defect
at the point $z$.
