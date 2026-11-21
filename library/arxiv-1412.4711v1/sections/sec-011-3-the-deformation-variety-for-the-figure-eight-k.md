---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-011-3-the-deformation-variety-for-the-figure-eight-k
section_title: "The deformation variety for the figure eight knot complement"
section_number: 3
pages: 10-11
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{computations}

We fix the usual ideal $2$-tetrahedra triangulation of the figure eight knot
complement (which we refer as the standard triangulation). In this section we
prove the following theorem.

\begin{theorem}\label{3components}
  Given the standard triangulation of the figure eight knot complement, the
  deformation variety $\tmop{Defor} ( M, \mathcal{T} )$ is the union of 3
  distinct smooth affine (irreducible algebraic) varieties of dimension 2 and
  is connected.
\end{theorem}

As said in the introduction, we strongly believe that the character variety of the figure 
eight knot complement does not contain any other irreducible component with irreducible 
representations. A proof should appear elsewhere.

In order to prove the theorem, we will compute 3 affine varieties $D_{1}
,D_{2} ,D_{3}$, 3 birational maps $\pi_{1} , \pi_{2} , \pi_{3}$ defined
everywhere on the $D_{i}$'s and $3$ polynomials $H_{1} ,H_{2} ,H_{3}$ in
$\mathbb{Q} [ X_{1} ,X_{2} ,X_{3} ]$ such that :
\begin{itemize}
  \item (a) $\tmop{Defor} ( M, \mathcal{T} ) = \cup_{i=1 \ldots 3} D_{i}$.
  
  \item (b) $V ( H_{i} ) = \overline{\pi_{i} ( D_{i} )} ,i=1 \ldots 3$.
  
  \item (c) $\pi_{i} ( D_{i} ) \subset V ( H_{i} )$ is smooth and $\pi_1$ realizes a homemorphism on its image.  
  \item (d) $V ( H_{i} )$ is irreducible in $\mathbb{C}^{3}$  or equivalently $H_{i}$ is
  irreducible in $\mathbb{C} [ X_{1} ,X_{2} ,X_{3} ]$.
  
  \item (e) $D_{i} \neq D_{j}$ \ for $i \neq j$ and $i,j=1 \ldots 3$.
    \item (f) $\cap_{i=1 \ldots 3} D_{i} \neq \emptyset$.
\end{itemize}
Under assumptions (a) to (f), $\pi_{i} ( D_{i} )$ is a  smooth Zariski-open subset
in the affine irreducible algebraic variety $V ( H_{i} )$, it is thus
connected -- see \cite[4.16]{Mumford}. As $\pi_{i}$ is  is a homeomorphism on its image, $D_{i}$ is also smooth and
connected. As $\cap_{i=1 \ldots 3} D_{i} \neq \emptyset$, then $\tmop{Defor}(M,\mathcal T)$
is also connected. So the theorem follows from those properties.

Let us describe how to compute $D_{i} , \pi_{i} ,H_{i} ,i=1 \ldots 3$.
