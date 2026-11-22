---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-018-42-where-are-some-already-known-representations
section_title: "Where are some already known representations ?"
section_number: 4.2
pages: 20-22
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.976
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{section:example-unipotent}Some representations are already known, more
precisely the boundary-unipotent ones, i.e. those for which the images of $l$
and $m$ are unipotent. These representations were found in {\cite{FKR14}}.
Algebraically, we add the conditions $L=L^{\ast} =M=M^{\ast} =1$. Once a point in $\mathrm{Defor}(M,\mathcal T)$ is known, it is an easy task to decide whether it belongs to $D_1$, $D_2$ or $D_3$: just plug the coordinates in the polynomials defining these three components and check which one vanishes.

Here are the representations found in \cite{FKR14} and where they live:
\begin{itemize}
  \item The monodromy of the complete hyperbolic structure on the complement of the figure-eight knot and its complex conjugate representation correspond to points of $D_1$. Indeed, if
  $\omega^{\pm} = \frac{1 \pm i \sqrt{3}}{2}$ is one root of $f_{1}$, then
  \[ u_{12} =u_{21} =u_{34} =u_{43} =v_{12} =v_{21} =v_{34} =v_{43} =
     \omega^{\pm} \]
  is a point of $\mathrm{Defor}(M,\mathcal T)$, corresponding to this monodromy or its complex conjugate. In other terms, $D_1$ is the geometric component of $\mathrm{Defor}(M,\mathcal T)$.
  
  \item Setting:
  \[ u_{1,2} =u_{3,4} =v_{3,4} =v_{4,3} = \bar{u}_{2,1} = \bar{u}_{4,3} =
     \bar{v}_{1,2} = \bar{v}_{2,1} = \omega^{\pm} , \]
     one gets two other points in $\mathrm{Defor}(M,\mathcal T)$.
  They correspond to a discrete representation of the fundamental
  group of the complement of knot in $\tmop{PU} (2,1)$ with faithful boundary
  holonomy. Moreover, its action on complex hyperbolic space has limit set the
  full boundary sphere {\cite{falbeleight}}. Both these point also belong to the geometric component $D_1$.
  
  
  
  \item Let $\gamma^{\pm} =-
  \frac{1}{2} \pm i \frac{1}{2}  \sqrt{7}$. Define
  \begin{center}
    $\begin{array}{c}
      u_{2,1} =v_{2,1} = \bar{u}_{4,3} = \bar{v}_{1,2} = \frac{5\pm i
      \sqrt{7}}{4} ,\\
      u_{1,2} =v_{2,1} = \frac{3\pm i \sqrt{7}}{8} ,v_{4,3} = \bar{v}_{3,4} =-
      \frac{1\pm i \sqrt{7}}{2}
    \end{array}$
  \end{center}
  These two points belong to $\mathrm{Defor}(M,\mathcal T)$ and correspond to representation in $\tmop{PU} (2,1)$. It turns out that they belong to $D_3$.
  \item Consider now the inverse of $\gamma^{\pm}$: $1/ \gamma^{\pm} =-
  \frac{1}{4} \pm i \frac{1}{4}  \sqrt{7}$,nd define:
  \begin{center}
    $\begin{array}{c}
      u_{1,2} = \bar{u}_{3,4} = \frac{3\pm i \sqrt{7}}{2} ,v_{4,3} =
      \bar{v}_{3,4} = \frac{5\pm i \sqrt{7}}{8} ,\\
      u_{2,1} =v_{2,1} = \bar{u}_{4,3} = \bar{v}_{1,2} = \frac{-1\pm i
      \sqrt{7}}{4}
    \end{array}$
  \end{center}  
  These two points belong to $\mathrm{Defor}(M,\mathcal T)$ and correspond to representation in $\tmop{PU} (2,1)$. It turns out that they belong to $D_2$.
  
  
\end{itemize}
All solutions were already obtained in {\cite{falbeleight}}. Moreover the solutions that belong to $D_2$ or $D_3$ correspond to spherical CR structures with
unipotent boundary holonomy of rank one {\cite{DF}}.

Moreover, in {\cite{DF}}, it was shown that there exists a non-inner
automorphism $\tau$ of the group $\Gamma_{8}$ that sends a representation
appearing in the third point above to a representation appearing in the fourth point.
It is known that, on the hyperbolic structure, this automorphism
correspond to a change of orientation, that is it acts as complex conjugation. It proves that the action of $\tau$
on the representation variety exchange the last two components and preserves
the first one. This fact is presented in a more concrete way in the following section
\ref{deformation}.


\subsubsection{Hyperbolic solutions - $A$-polynomial}

We may now look after the representations coming from $\mathrm{PGL}
(2,\mathbb{C})$, which we call hyperbolic solutions. Indeed, the hyperbolic
conditions : $u_{12} =u_{21} =u_{34} =u_{43}$, $v_{12} =v_{21} =v_{34}
=v_{43}$ on the parameters is equivalent to the fact that the holonomy
representation associated to these parameters has its image lying in
$\mathrm{Ad} ( \mathrm{PGL} (2,\mathbb{C}))$. These conditions simplify a lot
the equations and give the 1-dimensional complex variety
\[ z= \frac{1}{1-y} , \hspace{1em} x^{2} y^{2} = (1-x)  (1-y) . \]
We then obtain
\[ \begin{array}{l}
     u_{12} =u_{34} =u_{21} =u_{43} =x,\\
     u_{23} =u_{41} =u_{14} =u_{32} =1- \frac{1}{x} ,\\
     u_{13} =u_{31} =u_{24} =u_{42} = \frac{1}{1-x} ,\\
     v_{12} =v_{21} =v_{34} =v_{43} = \frac{1}{1-y} ,\\
     v_{13} =v_{24} =v_{31} =v_{42} =1- \frac{1}{y}\\
     v_{23} =v_{14} =v_{32} =v_{41} =y.
   \end{array} \]
Furthermore, we get
\[ L= \frac{1}{L^{\ast}} = \frac{xy}{x-1} ,M= \frac{1}{M^{\ast}} =
   \frac{(1-y)^{2}}{y^{4}} . \]
It appears that all hyperbolic solutions lie in the first component.

Eliminating $x$ and $y$ between $L$ and $M$ with the condition $x^{2} y^{2} =
(1-x)  (1-y)$ gives the condition (called $A$-polynomial):

{\small{$-L^{8} M+2 \hspace{0.17em} L^{7} M+3 \hspace{0.17em} L^{6} M-2
\hspace{0.17em} L^{5} M+L^{4} M^{2} -6 \hspace{0.17em} L^{4} M+L^{4} -2
\hspace{0.17em} L^{3} M+3 \hspace{0.17em} L^{2} M+2 \hspace{0.17em} LM-M=0$}}

Note that this $A$-polynomial is not the classical one for the group
$\tmop{SL} (2,\mathbb{C})$ but is the same as the one independently found by
C. Zickert {\cite{Zickert-A-pol}}.

Note that hyperbolic and CR-solutions in the first component intersect in a
1-dimensional variety, namely the real part of the hyperbolic solutions. Those
are, from a geometric point of view, degenerate as the group $\tmop{PGL}
(2,\mathbb{R})$ is not linked to a 3-dimensional geometry.
