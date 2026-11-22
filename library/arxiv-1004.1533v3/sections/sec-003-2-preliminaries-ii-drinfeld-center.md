---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-003-2-preliminaries-ii-drinfeld-center
section_title: "Preliminaries II: Drinfeld Center"
section_number: 2
pages: 6-10
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.95
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:center}



We will also need the notion of Drinfeld center of a spherical fusion
category. Recall that the Drinfeld center $Z(\C)$ of a fusion category $\C$
is defined as the category whose objects are pairs $(Y,\ph_Y)$, where $Y$
is an object of $\C$ and $\ph_Y$ -- a functorial isomorphism $Y\otimes -\to
-\otimes Y$ satisfying certain compatibility conditions (see
\ocite{muger1}).

As before, we will frequently use graphical presentation of morphisms
which involve objects both of $\C$ and $Z(\C)$. In these diagrams, we
will show objects of $Z(C)$ by double green lines   and the
half-braiding isomorphism $\ph_Y\colon Y\otimes V\to V\otimes Y$  by
crossing as in \firef{f:crossing}.
\begin{figure}[ht]
\tzCrossing
\caption{Graphical presentation of the half-braiding $\ph_Y\colon Y\otimes
V\to V\otimes Y$, $Y\in \Obj Z(\C)$, $V\in \Obj \C$}\label{f:crossing}
\end{figure}


We list here main properties of $Z(\C)$, all under the assumption that $\C$
is a spherical fusion category over an algebraically closed field of
characteristic zero.

\begin{theorem}{\ocite{muger2}}
 $Z(\C)$ is a modular category; in particular, it is
    semisimple with finitely many simple objects, it is braided and has
    a pivotal structure which coincides with the pivotal structure on
    $\C$. 
\end{theorem}


We have an obvious forgetful functor $F\colon Z(\C)\to \C$. To simplify
the notation, we will frequently omit it in the formulas, writing for
example $\Hom_\C(Y,V)$ instead of $\Hom_\C(F(Y),V)$, for $Y\in \Obj
Z(\C)$, $V\in \Obj \C$. Note, however, that if $Y,Z\in \Obj Z(\C)$, then
$\Hom_{Z(\C)}(Y,Z)$ is different from $\Hom_{\C}(Y,Z)$: namely,
$\Hom_{Z(\C)}(Y,Z)$ is a subspace in $\Hom_{\C}(Y,Z)$ consisting of those
morphisms that commute the with the half-braiding. The following lemma will
be useful in the future. 


\begin{lemma}\label{l:projector}
  Let $Y,Z\in \Obj Z(\C)$. Define the operator 
  
  $P\colon \Hom_\C(Y,Z)\to
  \Hom_\C(Y,Z)$ by the following formula:
  $$
    P\psi=\frac{1}{\DD^2}\sum_{X\in \Irr(\C)} d_X\quad
    \tzProjectionI
  $$
  Then $P$ is a projector onto the subspace   
  $\Hom_{Z(\C)}(Y,Z)\subset   \Hom_\C(Y,Z)$. 
\end{lemma}
\begin{proof}It is immediate from the definition that if $\psi\in
  \Hom_{Z(\C)}(Y,Z)$, then $P\psi=\psi$. On the other hand, using
  \leref{l:pairing}, we get  that for any $\psi\in \Hom_\C(Y,Z)$, one has
  $(P\psi)\ph_Y=\ph_Z(P\psi)$:
  \begin{align*}
    (P\psi)\ph_Y &=
    \frac{1}{\DD^2}\sum_{j}d_{j}\quad\tzProjectionII=
  \frac{1}{\DD^2}\sum_{i,j}d_{i}d_{j}\quad \tzProjectionIII\\
  &=
\frac{1}{\DD^2}\sum_{i}d_i\quad \tzProjectionIV
  = \ph_Z(P\psi),
  \end{align*}
 (as before, we are using convention \eqref{e:summation_convention}). 
\end{proof}



The following theorem is a refinement of \ocite{ENO}*{Proposition 5.4}.
\begin{theorem}\label{t:I}
   Let $F\colon Z(\C)\to \C$ be the forgetful functor and $I\colon
  \C\to Z(\C)$ the (left) adjoint of $F$:
  $\Hom_{Z(\C)}(I(V),X)=\Hom_\C(V,F(X))$. Then for $V\in \Obj \C$, one
  has 
  \begin{equation}\label{e:I}
    I(V)=\bigoplus_{i\in \Irr(\C)} X_i\otimes V\otimes X_i^*
  \end{equation}
  with the half braiding given by
  \begin{figure}[ht]
    $$\bigoplus_{i,j\in \Irr (\C)} \sqrt{d_i}\sqrt{d_j} \quad
    \tzHalfBraid
    $$
    \caption{Half-braiding $I(V)\otimes
    W\to W\otimes I(V)$.}\label{f:I}
  \end{figure}
\end{theorem}
Note that instead of normalizing factor $\sqrt{d_i}\sqrt{d_j}$ we could
have used $d_i$ or $d_j$ ---  each of this would give an equivalent
definition.
\begin{proof}
Denote $Y=\bigoplus_{i\in \Irr(\C)} X_i\otimes V\otimes X_i^*$. It follows
from \leref{l:pairing} that the morphisms $Y\otimes W\to W\otimes Y$
defined by \firef{f:I} satisfy the compatibility relations required of half
braiding and thus define on $Y$ a structure of an object of $Z(\C)$. Now,
define for any $Z\in \Obj Z(\C)$, maps
\begin{align*}
\Hom_{Z(\C)}(Y,Z)&\to\Hom_\C(V,Z)\\
\Psi&\mapsto \Psi\circ P_0=\quad 
\tzFunctI
\end{align*}
where $P_0$ is the embedding $V=\one\otimes V\otimes \one\to Y=\bigoplus
X_i\otimes V\otimes X_i^*$
 and
\begin{align*}
\Hom_\C(V,Z)&\to\Hom_{Z(\C)}(Y,Z)\\
\Phi&\mapsto \bigoplus_{i\in\Irr(\C)}\sqrt{d_i} \tzFunctII
\end{align*}

It follows from \leref{l:projector} that these two maps are inverse to
each other. Composition in one direction is easy. First suppose 
$\Phi\in\Hom_\C(V,Z)$. The computation is shown below. 
$$
\Phi\to\bigoplus_{i}\sqrt{d_i}\quad \tzFunctII \to \Phi.
$$


The composition in opposite order is  as follows:
$$\Psi \to \tzFunctI
 \to
\bigoplus_{i}\sqrt{d_{i}} \tzFunctIII=
\bigoplus_{i} \sqrt{d_{i}} \sqrt{d_{j}} \tzFunctIV=\tzFunctV
$$

The first equality holds by functoriality of the half-braiding and
\firef{f:I}. The second equality is obvious. 
Therefore, the two maps are inverses to one another and we have
$\Hom_{Z(\C)}(Y,Z)=\Hom_\C(V,Z)$; thus, $Y=I(V)$. 
\end{proof}



An easy generalization of \thref{t:spherical1} allows us to consider
graphs in which some of the edges are labeled by objects of $Z(\C)$.


Let $\hat\Ga$ be a graph which consists of a usual graph $\Ga$ embedded in
$S^2$ as in \thref{t:spherical1} and a finite collection of
non-intersecting oriented  arcs  $\ga_i$ such that endpoints of each arc
$\ga$  are vertices of graph $\Ga$, and each vertex has a neighborhood in
which arcs $\ga_i$ do not intersect edges  of $\Ga$; however, arcs $\ga_i$
are allowed to intersect edges of $\Ga$ away from vertices. Note that this
implies that for each vertex $v$, we have a natural cyclic
order on the set of all edges of $\hat\Ga$ (including arcs  $\ga_i$)
adjacent to $v$. 


Let us color such diagram, labeling each edge of $\Ga$ by an object of
$\C$, each arc $\ga$  by an object of $Z(\C)$, and each vertex $v$ by a
vector $\ph_v\in \<V^\pm (e_1), \dots, V^{\pm}(e_n)\>$ where $e_1,\dots,
e_n$ are edges of $\hat\Ga$ adjacent to $v$ (including the arcs
$\ga_i$), and the signs are chosen as in \thref{t:spherical1}.

\begin{figure}[ht]
 \fig{figures/dual_graph3b}\qquad
\tzSphereDiagramII

\caption{Diagram $\hat\Ga$ on the sphere and its
flattening to the plane. Arc $\ga$ is shown
by a double line.}\label{f:sphere_diagram2}
\end{figure}



As before, by removing a point from $S^2$ and choosing a linear order of
edges (including the arcs) at every vertex, we get a diagram in the plane;
however, now the projections of  arcs $\ga_i$ can intersect edges of $\Ga$
as shown in \firef{f:sphere_diagram2}. Let us turn this into a tangle
diagram by replacing each intersection by a picture where the arch $\ga_i$
goes under the edges of $\Ga$, as shown in \firef{f:sphere_diagram2}. 
 
 
Such a diagram defines a number $Z_{RT}(\hat\Ga)$ defined in the usual way,
with the extra convention shown in \firef{f:crossing}.

 
\begin{theorem}\label{t:spherical2}
  The number $Z_{RT}(\hat\Ga)\in \kk$ does not depend on the choice of a
  point to remove from $S^2$ orand thus defines an
  invariant of colored graphs on the sphere. Moreover, this number is
  invariant under homotopy of arcs $\ga_i$. 
\end{theorem}
\begin{proof}
The fact that it is independent of the choice of point to remove and thus
is an invariant of a graph on the sphere immediately follows from
\thref{t:spherical1}: replacing every crossing by a coupon colored by
half-braiding $\ph_Y$ gives a graph as in \thref{t:spherical1}. Invariance
under homotopy of arcs $\ga$ follows from compatibility conditions on
half-braiding shown in \firef{f:homotopy}.
\begin{figure}[ht]
\qquad \tzHomotopyI\qquad =\qquad \tzHomotopyII
\caption{Invariance under homotopy}\label{f:homotopy}
\end{figure}


\end{proof}


Finally, we will need one more useful construction.

For any  $Y\in \Obj Z(\C)$, we define a functor
functor $\C^{\boxtimes n}\to \Vect$ by
\begin{equation}\label{e:vev-Z}
 \<V_1,\dots,V_n\>_Y=\Hom_\C(\one,Y\otimes  V_1\otimes\dots\otimes V_n)
\end{equation}
for any collection $V_1,\dots, V_n$ of objects of $\C$. As before, we have
functorial isomorphisms 
\begin{equation}\label{e:cyclic-Z}
 z_Y\colon\<V_1,\dots,V_n\>_Y\simeq \<V_n, V_1,\dots,V_{n-1}\>_Y
\end{equation}
obtained as composition 
$$
\<Y,V_1,\dots,V_n\>\to \<V_n, Y, V_1,\dots,V_{n-1}\>\to 
\<Y, V_n, V_1,\dots,V_{n-1}\>
$$
(the first isomorphism is the cyclic isomorphism \eqref{e:cyclic}, the
second one is the inverse of half-braiding $\ph_Y$). Note however that
in general  we do not have $z_Y^n=\id$.
