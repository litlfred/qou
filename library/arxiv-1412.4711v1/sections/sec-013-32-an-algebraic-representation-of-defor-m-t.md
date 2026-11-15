---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-013-32-an-algebraic-representation-of-defor-m-t
section_title: "An algebraic representation of Defor ( M, T )"
section_number: 3.2
pages: 12-13
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{ss:equations}

Given $M$ and $\mathcal{T}$ a triangulation of $M$ with $n$ tetrahedra, the
deformation variety $\tmop{Defor} (M, \mathcal{T} )$ is defined in
$\mathbb{C}^{16n}$ by a system of internal relations for each tetrahedron and
gluing equations for adjacent tetrahedra. Moreover, using the internal
relations, we may directly express the face parameters in terms of the edge
parameters. From now on, we consider $\tmop{Defor} (M, \mathcal{T} )$ as a
subset of $\mathbb{C}^{12n}$.

The system, more precisely, is given in terms of variables $Z= (z_{ij} (T))
\in \mathbb{C}^{12n}$, where $T$ denotes a tetrahedron in the triangulation
(containing $n$ tetrahedra) and $ij$ one of its oriented edges.
\begin{itemize}
  \item $L_{e}$ (resp. $L_{f}$) denotes the set of the $2n$ edge (resp. face)
  equations;
  
  \item $L_{c}$ denotes the polynomials defining the internal relations (also
  called cross-ratio relations), of the form $z_{ik} (T)  (1-z_{ij} (T)) -1$
  and $z_{ij} (T)  (1-z_{il} (T)) -1$ for each tetrahedron;
\end{itemize}
In this terms, $\tmop{Defor} (M, \mathcal{T} )$ is the algebraic variety:
\[ \tmop{Defor} (M, \mathcal{T} ) =V ( \langle L_{e} \cup L_{f} \cup L_{c}
   \rangle ) = \{{Z} \in \mathbb{C}^{12n} |P(Z)=0,P \in L_{e} \cup
   L_{f} \cup L_{c} \} . \]
Note that $\tmop{Defor} (M, \mathcal{T} ) \subset (\mathbb{C} \setminus
\{0,1\})^{12n}$, because of the internal relations $L_{c}$. This remark will be important later on.

We now display the equations for the figure eight knot complement. The triangulated structure (see section \ref{section:intro-eight}) associated
with the figure eight knot complement is made of two tetrahedra decorated by
the coordinates $(u_{ij} )_{i \neq j \in \{1, \ldots ,4\}}$ (resp. $(v_{ij}
)_{i \neq j \in \{1, \ldots ,4\}}$) with cross-ratio relations defined as the
roots of the system $L_{c_{1}} =0$ (resp. $L_{c_{2}} =0$) :
\begin{center}
  $L_{c_{1}} = \left\{ \begin{array}{c}
    u_{12} u_{13} -u_{13} +1\\
    u_{12} u_{14} -u_{12} +1\\
    u_{21} u_{23} -u_{21} +1\\
    u_{21} u_{24} -u_{24} +1\\
    u_{31} u_{34} -u_{31} +1\\
    u_{32} u_{34} -u_{34} +1\\
    u_{41} u_{43} -u_{43} +1\\
    u_{42} u_{43} -u_{42} +1
  \end{array} \right. \begin{array}{c}
    \\
    \\
    
  \end{array}$ , \ $L_{c_{2}} = \left\{ \begin{array}{c}
    v_{12} v_{13} -v_{13} +1\\
    v_{12} v_{14} -v_{12} +1\\
    v_{21} v_{23} -v_{21} +1\\
    v_{21} v_{24} -v_{24} +1\\
    v_{31} v_{34} -v_{31} +1\\
    v_{32} v_{34} -v_{34} +1\\
    v_{41} v_{43} -v_{43} +1\\
    v_{42} v_{43} -v_{42} +1
  \end{array} \right.$ ,
\end{center}
and gluing edge (resp. face) relations defined as the roots of the system
$L_{e} =0$ (resp. $L_{f} =0$) :
\begin{center}
  $L_{e} = \left\{ \begin{array}{c}
    u_{13} u_{14} u_{23} v_{21} v_{24} v_{31} -1\\
    u_{31} u_{32} u_{41} v_{12} v_{13} v_{42} -1\\
    u_{21} u_{24} u_{34} v_{23} v_{41} v_{43} -1\\
    u_{12} u_{42} u_{43} v_{14} v_{32} v_{34} -1
  \end{array} \right.$ , $L_{f} = \left\{ \begin{array}{c}
    u_{21} u_{31} u_{41} v_{21} v_{31} v_{41} -1_{\nosymbol}\\
    u_{12} u_{32} u_{42} v_{13} v_{23} v_{43} -1\\
    u_{13} u_{23} u_{43} v_{12} v_{32} v_{42} -1\\
    u_{14} u_{24} u_{34} v_{14} v_{24} v_{34} -1
  \end{array} \right.$ .
\end{center}
We set $Z= \{ u_{ij} ,v_{i,j} ,i \neq j \in \{ 1, \ldots ,4 \} \}$.
