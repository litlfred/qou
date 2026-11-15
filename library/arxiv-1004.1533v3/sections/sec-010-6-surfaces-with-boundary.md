---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-010-6-surfaces-with-boundary
section_title: "Surfaces with boundary"
section_number: 6
pages: 22-24
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.973
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:boundary}

In this section we extend the definition of TV TQFT to surfaces with
boundary (and 3-manifolds with corners). Recall that according to general
ideas of extended field theory (see \ocite{lurie}), an extended 3d 
TQFT should assign to a closed 1-manifold a 2-vector space, or an abelian
category, and to a 2-cobordism between two 1-manifolds, a functor between
corresponding categories (which in the special case of cobordism between
two empty 1-manifolds gives a functor $\Vect\to \Vect$, i.e. a  vector
space). In this section we show that the extension of the  TV TQFT to
1-manifolds assigns to a circle $S^1$ the category $Z(\C)$---the Drinfeld
center of the original spherical category $\C$. This result was
proved by Turaev in the special case when the original category $\C$ is
ribbon (see \ocite{turaev}); the general case has remained a
conjecture.


For technical reasons, it is more convenient to replace surfaces with
boundaries by surfaces with embedded disks. These two notions give
equivalent theories: given a surface with boundary, we can glue a disk to
every boundary circle and get a surface with embedded disks; conversely,
given a surface with embedded disks, one can remove the disks to get  a
surface with boundary. Moreover, in order to accommodate real-life
examples, we need to consider framing. This leads to the following
definition.

We denote
$$
D^2=[0,1]\times[0,1]
$$
and will call it {\em the standard disk} (it is, of course, a square, but
this is what a disk looks like in PL setting). We will also the marked
point $P_0$ on the boundary of $D^2$
$$
P_0=(0,1)\in \del D^2
$$











\begin{definition}\label{d:ex_surface}
A framed embedded disk  $D$ in a PL surface $N$ is the image of a PL
map
$$
\ph\colon D^2\to N
$$
which is a homeomorphism with the image, together with the point
$P=\ph(P_0)\subset \del D$.

An {\em extended surface} is a PL surface $N$ together with a finite
collection of disjoint framed embedded disks (see \firef{f:ex_surface}).
We will denote the set of embedded disks by $D(N)$.

A {\em coloring} of an extended surface is a choice of an object $Y_\al\in
\Obj Z(\C)$ for every embedded disk $D_\al$.
\end{definition}

\begin{figure}[ht]
\fig{figures/ex_surface.eps}
\caption{Extended surface}\label{f:ex_surface}
\end{figure}






Next, we can define cobordisms between such surfaces. As usual, such a
cobordism will be a 3-manifold with boundary together with some ``tubes''
inside which connect the embedded disks on the boundary of $M$. The
following gives a precise definition in the PL category.

\begin{definition}\label{d:tube}
Let $M$ be a PL 3-manifold with boundary.

An open {\em embedded tube} $T\subset M$ is the image of a PL map
$$
\ph\colon [0,1]\times D^2\to M
$$
which is satisfies the conditions below, together with the oriented arc
$\ga=\ph([0,1]\times \{P_0\})$ (which we will call the {\em longitude}).

The map $\ph$ should satisfy:
\begin{enumerate}
  \item $\ph$ is a homeomorphism onto its image
  \item $T\cap \del M=\ph(\{0\}\times D^2) \cup \ph(\{1\} \times D^2)$
\end{enumerate}

We will call the disks $B_0=\ph(\{0\}\times D^2)$ and $B_1=\ph(\{1\}\times
D^2)$ the {\em bottom } and {\em top}  disks of the tube.


A closed embedded tube $T\subset M$ is the image of a PL map
$$
\ph\colon S^1\times D^2\to M
$$
which is satisfies the conditions below, together with the oriented arc
$\ga=\ph([0,1]\times \{P_0\})$ (the {\em longitude}) and the disk
$B=\ph(\{0\}\times D^2)\subset T$.


The map $\ph$ should satisfy:
\begin{enumerate}
  \item $\ph$ is a homeomorphism onto its image
  \item $T\cap \del M=\varnothing$
\end{enumerate}

\end{definition}


The longitude  $\ga$ determines the framing of the tube; the disk $B$ is
convenient for technical reasons; later we will get rid of it. 



\begin{definition}\label{d:ex_manifold}
  An extended 3-manifold $M$ is an oriented  PL 3-manifold with boundary
  together with a finite collection of disjoint framed tubes $T_i\subset
  M$. We denote the set of tubes of $M$ by $T(M)$.

  A coloring of an extended 3-manifold $M$ is a choice of an object
    $Y_\al\in \Obj Z(\C)$ for every tube $T_\al$.
\end{definition}


\begin{figure}[ht]

\fig{figures/ex_mfd.eps}
\caption{Extended 3-manifold}\label{f:ex_manifold}
\end{figure}




Note that if $M$ is an extended 3-manifold, then its boundary $\del M$ has
a natural structure of an extended surface: the embedded disks are the
bottom and top disks  of the open tubes, and the marked points on the
boundary of embedded disks are the endpoints of the longitude arcs
$\ga_\al$, where $\al$ runs over the set of all open tubes in $M$.
Moreover, a coloring of $M$ defines a coloring of $\del M$: if an open
tube $T_\al$ is colored with $Y_\al\in \Obj Z(\C)$, we color the embedded
disk $\ph_\al(\{1\} \times D^2)$ with $Y_\al$ and the embedded
disk $\ph_\al(\{0\} \times D^2)$ with $Y_\al^*$.


Our main goal will be extending the TV invariants to such extended
surfaces and cobordisms. Namely, we will
\begin{enumerate}
  \item Define, for every colored extended surface $N$, the space
  $Z_{TV}(N, \{Y_\al\})$ which
  \begin{itemize}
   \item functorially  depends on colors $Y_\al$
  \item is functorial under homeomorphisms of extended surfaces
  \item has natural isomorphisms $Z_{TV}(\ov{N}, \{Y_\al^*\})=Z_{TV}(N,
\{Y_\al\})^*$
  \item satisfies the gluing axiom for surfaces
  \end{itemize}
 \item Define, for every colored extended 3-manifold $M$, a vector
    $Z_{TV}(M)\in Z_{TV}(\del M)$ (or, equivalently, for any
  colored extended 3-cobordism $M$ between colored extended surfaces $N_1,
  N_2$, a linear map $Z_{TV}(M)\colon Z_{TV}(N_1)\to Z_{TV}(N_2)$) so that
  this satisfies the gluing axiom for extended 3-manifolds.
\end{enumerate}


In the subsequent papers we will show that this  extended theory
actually coincides with the Reshetikhin--Turaev theory for the
modular category $Z(\C)$:
$$
Z_{RT, Z(\C)}=Z_{TV, \C}.
$$

The construction of the theory proceeds similar to the construction of TV
invariants. Namely, we will first define $Z_{TV}(N)$, $Z_{TV}(M)$ for
manifolds with a polytope decomposition and then show that the so defined
objects are independent of the choice of a polytope decomposition and
thus define an invariant of extended manifolds.
