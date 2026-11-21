---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-016-9-invariance-under-2-3-and-0-2-moves
section_title: "Invariance under 2-3 and 0-2 moves"
section_number: 9
pages: 25-27
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.937
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
The arguments of \cite{GHRS} extend easily to prove the following. 

\begin{thm} 
Let $\CT$ be an ideal triangulation of $M$ and let $\tilde \CT$ be obtained 
from $\CT$  by a 2-3 move. Then for all $a,b$ as above,
$I_{\CT}^a(b)=I_{\tilde\CT}^a(b)$ provided both sides are defined.
\end{thm} 

\begin{proof} 
We follow the argument from \cite[Theorem A.1]{GHRS}, indicating the main 
changes needed in the current setting. Consider a 2-3 move from $\CT$ to 
$\tilde \CT$; this occurs in a bipyramid consisting of $2$ tetrahedra in 
$\CT$ which are replaced by 3 tetrahedra sharing an edge of order 3 in 
$\tilde \CT$.

First note that each $Q$-normal class $S \in Q(\CT;\S)$  can be written 
as a linear combination of edge solutions, tetrahedral solutions and 
peripheral curve solutions with coefficients in $\frac{1}{2} \Z$, by the 
results of Section 6 (see Remark \ref{half-integer-coefs}).
As in section 4.4 of \cite{GHRS}, we can represent $S$ by a linear 
combination $\omega$ of oriented normal arcs in the induced triangulation 
$\T_\bd$ of $\bd M$, chosen so that each quad coordinate for $S$ is a sum 
of 4 ``turning numbers'' of normal arcs, coming from the 4 corners of the 
tetrahedron containing the quad (see figure 7 of \cite{GHRS}).

Explicitly, for each edge solution we choose a small normal linking
circle in  $\bd M$ around one end of the edge in $\T$,  we choose oriented 
normal curves representing each peripheral class, and for each tetrahedral 
solution we choose three normal arcs  oriented anticlockwise in a triangle 
coming from one corner of the tetrahedron. (If tetrahedral solutions are 
needed in the bipyramid, we choose the two triangles at the degree 3 
vertices at the top and bottom.) One difference from \cite{GHRS}  is that 
the coefficients of the normal arcs here can be {\em half-integers}; 
but each sum of turning numbers giving a quad coefficient is still an 
integer. 

To compute the index $I_\T^a(b)$, we choose a normal class $S_0$ with 
$[S_0]_2=a$ and $[\bd S_0]=b$, and have a contribution from each normal class
$$
S_{\kk} = S_0 + \sum k_i E_i,
$$ 
where $\kk=(k_i) \in \Z^{n-r}$ is a set of integer weights on a set
of $n-r$ ``basic edges''.  (The excluded edges are taken from a 
``maximal tree with 1- or 3- cycle for $\T$'' as in Theorem 4.3 
of \cite{GHRS}; this ensures that the map 
$\kk=(k_i) \mapsto \sum k_i E_i + \TT$ 
is an isomorphism from $\Z^{n-r}$ onto $(\EE+\TT)/\TT$.)
We can represent $S_0$ by a linear combination $\omega$ of oriented 
normal arcs as described above.
By adding $k_i$ small linking circles around one end of the $i$th edge 
in $\T$ we obtain a linear combination $\omega_{\kk}$ of oriented normal 
arcs which gives the 
quad coordinates of $S_{\kk} = S_0 + \sum k_i E_i$.

The construction of \cite{GHRS} shows how to replace $\omega$ by a linear 
combination $\tilde\omega$ of oriented normal arcs in $\tilde\T_\bd$ 
representing a normal class $\tilde S_0$ in $\tilde \T$ and this satisfies 
$[\tilde S_0]_2=[S_0]_2$ and $[\bd S_0] = [\bd \tilde S_0]$.   
(Essentially, $\tilde S_0$ is obtained by subdividing the normal disks of 
$S_0$, so its homology classes do not change.) 
Then the index sum for $I_{\tilde \T}^a(b)$ has a contribution for each 
normal class 
$$
\tilde S_{\tilde \kk} = \tilde S_0 + k_0 \tilde E_0 + \sum k_i \tilde E_i,
$$
where $k_0$ is the integer weight on the new edge class $\tilde E_0$ in 
$\tilde \T$, and $\kk=(k_i)\in\Z^{n-r}$ as above give the weights
on the edge classes $\tilde E_i$ coming from $\T$.
Adding small linking circles around one end of each  edge in $\T$ gives a 
linear combination of normal arcs  $\tilde\omega_{\tilde \kk}$
which gives the quad coordinates of $\tilde S_{\tilde \kk}$.

The proof of the Pentagon Equality (Lemma A.3 in \cite{GHRS}) now goes 
through verbatim; this gives the result. The only difference in the 
current setting is that coefficients of normal arcs and turning numbers 
can now be half-integers. However since the sums giving quad coefficients 
used in the tetrahedral index functions are integers,
the arguments of \cite{GHRS} go through without change.  
\end{proof}

The arguments from \cite{GHRS} also extend to give the following.

\begin{thm} 
\label{0-2invariance}
Let  $\CT$ be an ideal triangulation of $M$ and let $\tilde \CT$ be 
obtained from $\CT$  by a 0-2 move. Then for all $a,b$ as above,
$I_{\CT}^a(b)=I_{\tilde\CT}^a(b)$ provided both sides are defined.
\end{thm} 

\begin{proof}
Here the proof of Theorem 5.1 in  \cite{GHRS} applies, if we start with a 
linear combination $\omega$ of oriented normal arcs in $\T_\bd$
with $\frac{1}{2} \Z$ coefficients  giving the quad coordinates of $S_0$ 
with homology classes $[S_0]_2=a$ and $[\bd S_0]=b$.
\end{proof}
