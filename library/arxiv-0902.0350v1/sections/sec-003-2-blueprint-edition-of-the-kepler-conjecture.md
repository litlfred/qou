---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-003-2-blueprint-edition-of-the-kepler-conjecture
section_title: "Blueprint edition of the Kepler conjecture"
section_number: 2
pages: 5-7
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.978
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:blueprint}

The {\it blueprint edition} of the proof of the Kepler conjecture is a second-generation proof that contains far more explicit detail than the original proof.  The blueprint edition is available at \cite{hales:2008:blueprint}, \cite{hales:2008:collection}.   Many proofs have been significantly simplified and systematized.   It has been written in a manner to permit easy formalization.  As its name might suggest, this version is intended as a blueprint for the construction of a formal proof.
This section 
compares the blueprint edition with the original.



\subsection{Lemmas in elementary geometry}


A collection of about 200 lemmas that can be expressed in elementary terms has been extracted from 
the original proof and placed in a separate collection~\cite{hales:2008:collection}.  This has
several advantages.  First of all, these lemmas, although elementary, are precisely the parts of the
original proof that put the greatest burden on the reader's geometrical intuition.  (Many of these
lemmas deal with the existence or non-existence of configurations of several points in $\ring{R}^3$ subject to
various metric constraints.)  Also, the lemmas can be stated without reference to the Kepler conjecture and all of the
machinery that has been introduced to give a proof.
Finally, the proofs of these lemmas rely on similar methods and are best considered
together~\cite{1271687}.  Section~\ref{sec:ordinary} on {\it Enhanced Automation} gives an approach to proving the lemmas in this collection.


These lemmas  can be
expressed in the first-order language of the real numbers; that is, they can be expressed in
the syntax of first-order logic with equality (allowing quantifiers $\forall x$, $\exists x$ with variables
running over the real numbers), the real constants $0$, $1$, and ring operations $(+)$, $(-)$,
$(\cdot)$ on $\ring{R}$.  In fact, L. Fejes T\'oth's statement of the Kepler conjecture as
an optimization problem in a finite number of variables can itself be expressed in the
first-order language of the real numbers~\cite{Toth:1972:Lagerungen}.  (For this, the truncation used by L. Fejes T\'oth must be modified slightly so that the truncated Voronoi cells are polyhedra.)  Thus, it should come as no surprise that many
of the intermediate lemmas in the proof can also be expressed in this manner.

For example, consider the statement asserting the existence of a circumcenter of a triangle: 
if three points in the plane are not collinear, then there exists a
point in the plane that is equidistant from all three.  This can be expressed in elementary terms
as follows:  for every $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$, if there do not exist $t_1, t_2$, and $t_3$
for which $t_1 (x_1,y_1) + t_2 (x_2,y_2)+ t_3 (x_3,y_3) = (0,0)$ and $t_1+t_2+t_3=1$, then there exists
$(x,y)$ such that 
$$
  (x-x_1)^2 + (y-y_1)^2 = (x-x_2)^2 + (y-y_2)^2 = (x-x_3)^2 + (y-y_3)^2. 
$$



 


\subsection{Background material}

There is now a close
match between what the blueprint edition assumes as background and what the proof assistant {\it HOL Light}
provides, as described in Section~\ref{sec:ordinary}.  The blueprint edition develops 
substantial background
material in trigonometry, measure and integration, hypermaps, and fans (a geometric realization of a hypermap).   It turns out
that only a small number of {\it primitive} volumes need to be computed for the proof of the Kepler
conjecture. These primitives include the volume of a ball, a tetrahedron, and right circular cone.  
No line or surface integrals are required.

A hypermap consists of  three permutations $e,n,f$ (on a finite set $D$) 
that compose to the identity $e\circ n\circ f= I$.  A hypermap is the
combinatorial structure used by Gonthier in his formal proof of the four color theorem.  In 2005,
the proof of the Kepler conjecture was rewritten in terms of hypermaps, because it is better suited
for formal proofs than planar graphs.  

The Jordan curve theorem (JCT) has been formalized as a step in the Flyspeck project~\cite{Hales:2007:jordan}.  In fact, something weaker than the JCT
suffices.  The project only uses the JCT for curves on
the surface of a unit sphere consisting of a finite number of arcs of great circles; that is, a 
spherical polygonal version of the JCT.  In the proof of the Kepler conjecture, the combinatorial structure of
a cluster of spheres is encoded as a hypermap.  An Euler characteristic calculation, based on the JCT, shows that
these hypermaps are planar.  The planarity of these hypermaps is a crucial property that is used in the enumeration
of tame graphs (Section~\ref{sec:graph}).
The background chapter in the blueprint edition contains detailed proofs of these facts.


The blueprint edition contains several introductory essays that introduce 
the main concepts in the proof, including the algorithms implemented by the computer code.

The formalization of the blueprint text started in
2008 with work of J. Rute (CMU) and the Hanoi Flyspeck group. The current members of this group are {\vn Tr\`\acircumflex n Nam Trung}, {\vn Nguy\~\ecircumflex n T\'\acircumflex t Th\'\abreve ng}, {\vn Ho\`ang L\ecircumflex\ Tr\uhorn\`\ohorn ng}, {\vn Nguy\~\ecircumflex n Quang Tr\uhorn\h\ohorn ng}, {\vn V\~u Kh\'\abreve c K\h y}, {\vn Nguy\~\ecircumflex n Anh T\acircumflex m}, {\vn Nguy\~\ecircumflex n Tuy\ecircumflex n Ho\`ang}, {\vn Nguy\~\ecircumflex n \DJ\'\uhorn c Ph\uhorn \ohorn ng}, {\vn V\uhorn \ohorn ng Anh Quy\`\ecircumflex n}, {\vn Phan Ho\`ang Ch\ohorn n}, and managed by {\vn T\d a Th\d i Ho\`ai An}.  The blueprint formalization is still at an early stage.
