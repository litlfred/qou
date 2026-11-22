---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-002-1-preliminaries-i-spherical-categories
section_title: "Preliminaries I: spherical categories"
section_number: 1
pages: 2-6
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.951
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:prelim}



In this section we collect notation and some facts about spherical
categories.

We fix   an algebraically  closed field  $\kk$ of characteristic 0 and
 denote by $\Vect$ the category of finite-dimensional vector spaces over
$\kk$.

Throughout the paper, $\C$ will denote a spherical fusion category over 
 $\kk$. We refer the reader
to the paper \ocite{drinfeld} for the definitions and properties of such
categories. Note that we are not requiring a braiding on $\C$. 

In particular, $\C$ is semisimple with finitely many
isomorphism classes of simple objects. We will denote by $\Irr(\C)$ the
set of isomorphism classes of simple objects. We will also denote by $\one$
the unit object in $\C$ (which is simple).


Two main examples of spherical categories are the category $\VecG$ of
finite-dimensional $G$-graded vector spaces (where $G$ is a finite group)
and the category $\Rep(U_q\g)$ which is the semisimple part  of the
category of representations of a quantum group $U_q\g$ at a root of unity;
this last category is actually modular, but we will not be using this. 




To simplify the notation, we will assume that $\C$ is a strict pivotal
category, i.e. that $V^{**}=V$. As is well-known, this is not really a
restriction, since any pivotal category is equivalent to a strict pivotal
category.


We will denote, for an object $X$ of $\C$, by 
$$
d_X=\dim X\in \kk
$$
its categorical dimension; it is known that for simple $X$, $d_X$ is
non-zero. We will fix, for any simple object $X_i\in \C$, a choice of
square root $\sqrt{d_X}$ so that for $X=\one$, $\sqrt{d_\one}=1$ and that
for any simple $X$, $\sqrt{d_X}=\sqrt{d_{X^*}}$. 

We will also denote
\begin{equation}\label{e:DD}
\DD=\sqrt{\sum_{x\in \Irr(\C)}d_X^2}
\end{equation}
(throughout the paper, we fix a choice of the square root). Note that by
results of \ocite{ENO}, $\DD\ne 0$. 



We define the
functor $\C^{\boxtimes n}\to \Vect$ by 
\begin{equation}\label{e:vev}
 \<V_1,\dots,V_n\>=\Hom_\C(\one, V_1\otimes\dots\otimes V_n)
\end{equation}
for any collection $V_1,\dots, V_n$ of objects of $\C$. Note that pivotal
structure gives functorial isomorphisms 
\begin{equation}\label{e:cyclic}
 z\colon\<V_1,\dots,V_n\>\simeq \<V_n, V_1,\dots,V_{n-1}\>
\end{equation}
such that $z^n=\id$ (see \ocite{BK}*{Section 5.3}); thus, up to a canonical
isomorphism,
the space $\<V_1,\dots,V_n\>$ only depends on the cyclic order of
$V_1,\dots, V_n$. 

We have a natural composition map 
\begin{equation}\label{e:composition}
\begin{aligned}
 \<V_1,\dots,V_n, X\>\otimes\<X^*, W_1,\dots,
W_m\>&\to\<V_1,\dots,V_n, W_1,\dots, W_m\>\\
\ph\otimes\psi\mapsto \ph\cc{X}\psi= \ev_X\circ (\ph\otimes\psi)
\end{aligned}
\end{equation}
where $\ev_X\colon X\otimes  X^*\to \one$ is the evaluation morphism. It
follows from semisimplicity of $\C$ that direct sum of these composition
maps gives a functorial isomorphism
\begin{equation}\label{e:gluing1}
 \bigoplus_{X\in \Irr(\C)} \<V_1,\dots,V_n, X\>\otimes\<X^*, W_1,\dots,
W_m\>\simeq\<V_1,\dots,V_n, W_1,\dots, W_m\>.
\end{equation}




Note that for any objects $A,B\in \Obj \C$, we have a 
non-degenerate pairing $\Hom_\C(A,B)\otimes \Hom_\C(A^*,B^*)\to \kk$ 
defined by 
\begin{equation}\label{e:pairing}
(\ph, \ph')=(\one\xxto{\coev_A}A\otimes A^*\xxto{\ph\otimes \ph'}
  B\otimes B^*\xxto{\ev_B}\one)
\end{equation}
In particular, this gives us a non-degenerate pairing 
$\<V_1,\dots,V_n\>\otimes \<V_n^*,\dots,V_1^*\>\to \kk$ and thus,
 functorial isomorphisms 
\begin{equation}\label{e:dual}
\<V_1,\dots,V_n\>^*\simeq \<V_n^*,\dots,V_1^*\>
\end{equation}
compatible with the cyclic permutations \eqref{e:cyclic}. 






We will frequently use graphical representations of morphisms in the
category $\C$, using tangle diagrams as in \ocite{turaev} or \ocite{BK}.
However, our convention is that of \ocite{BK}: a tangle with $k$ strands
labeled $V_1,\dots,V_k$ at the bottom and $n$ strands labeled $W_1,\dots,
W_n$ at the top is considered as a morphism from $V_1\otimes\dots\otimes
V_k\to W_1\otimes \dots\otimes W_n$. As usual, by default all strands are
oriented going from the bottom to top. Note that since $\C$ is assumed to
be a spherical category and not a braided one, no crossings are allowed in
the diagrams. 

For technical reasons, it is convenient to extend the graphical calculus by
allowing, in addition to rectangular coupons, also circular coupons
labeled with morphisms $\ph\in \<V_,1\dots, V_n\>$. This is easily seen to
be equivalent to the original formalism: every such circular coupon can be
replaced by the usual rectangular one as shown in \firef{f:round_coupon}.
\begin{figure}[ht]
\tzRoundCouponI
=
\tzRoundCouponII
\caption{Round coupons}\label{f:round_coupon}
\end{figure}

We will also use the following convention: if a figure contains a pair of
circular coupons, one with outgoing edges labeled $V_1,\dots, V_n$ and
the other with edges labeled $V_n^*,\dots, V_1^*$ , and the coupons are 
labeled by pair of letters $\ph,\ph^*$ (or $\psi, \psi^*$, or \dots)
it will stand for summation over the dual bases:
\begin{equation}\label{e:summation_convention}
\tzSummationConventionI
\quad = \sum_\al\quad
\tzSummationConventionII
\end{equation}
where $\ph_\al\in \<V_1,\dots, V_n\>$, $\ph^\al\in \<V_n^*,\dots, V_1^*\>$
are dual bases with respect to pairing \eqref{e:pairing}. 








The following lemma, proof of which is left to the reader,  lists some
properties of this pairing and its relation with the composition maps
\eqref{e:composition}. 

\begin{lemma}\label{l:pairing}
\par\noindent
\begin{enumerate}
 \item 
 If $X$ is simple and $\ph\in \<X,A\>$, $\ph'\in\<A^*,X^*\>$ then 
$$
\fig{figures/pair1.eps}=\frac{(\ph,\ph')}{d_X}\quad \fig{figures/pair2.eps}
$$
\item 
  $$
  \sum_{i\in\Irr(\C)} d_i 
  \tzPairingIII=\tzPairingIV
  $$
  \textup{(}we use here convention \eqref{e:summation_convention}\textup{)}. 
\item If $X$ is simple, $\ph\in \<A,
  X\>$, $\ph'\in \<X^*, A^*\>$,  $\psi\in \<X^*,B\>$, $\psi'\in
\<B^*,X\>$, then 
\begin{equation}\label{e:compatibility}
(\ph\cc{X} \psi,\psi'\cc{X^*}\ph')
=\frac{1}{d_X} (\ph,\ph')(\psi',\psi)
\end{equation}
\textup{(}see \firef{f:compatibility}\textup{)}.
\begin{figure}[ht]
$$\fig{figures/compL.eps}=\frac{(\ph,\ph')}{d_X}\fig{figures/compR.eps}=\frac{(\ph,
\ph')(\psi',\psi)}{d_X}$$

\caption{Compatibility of pairing with composition.}
  \label{f:compatibility}
\end{figure}
\end{enumerate} 
\end{lemma}





\begin{corollary}\label{c:composition2}
Let $X$ be a simple object. Define the rescaled composition map
\begin{equation}\label{e:composition2}
\begin{aligned}
 \<V_1,\dots,V_n, X\>\otimes\<X^*, W_1,\dots,
W_m\>&\to\<V_1,\dots,V_n, W_1,\dots, W_m\>\\
\ph\otimes\psi&\mapsto \ph\ccc{X}\psi= \sqrt{d_X}\ \ev_X\circ
(\ph\otimes\psi)
\end{aligned}
\end{equation}
Then the rescaled composition map agrees with the pairing: 
$$(\ph\ccc{X} \psi,\psi'\ccc{X^*}\ph')= (\ph,\ph')(\psi',\psi)
$$ 
\textup{(}same notation as in \eqref{e:compatibility}\textup{)}. 
\end{corollary}


The following result, which easily follows from  \leref{l:pairing}, will
also be very useful.
\begin{lemma}\label{l:pairing2}
 If the subgraphs $A$, $B$ are not connected, then 
 $$
 \tzPairingV=\tzPairingVI
 $$
\end{lemma}




Finally, we will need the following result, which is the motivation for
the name ``spherical category''.


Let $\Ga$ be an oriented graph embedded in the sphere $S^2$, where each
edge $e$ is colored by  an object $V(e)\in \C$, and each vertex $v$ is
colored by a morphism $\ph_v\in \<V(e_1)^{\pm },\dots V(e_n)^{\pm} \>$,
where $e_1,\dots,e_n$ are the edges adjacent to vertex $v$, taken in
clockwise order, and $V(e_i)^{\pm}=V(e_i)$ if $e_i$ is outgoing
edge, and $V^*(e_i)$ if $e_i$ is the incoming edge.

By removing a point from $S^2$ and identifying $S^2\setminus{pt}\simeq
\R^2$, we can consider $\Ga$ as a planar graph. Replacing each vertex $v$
by a circular coupon labeled by morphism $\ph_v$ as shown in
\firef{f:sphere_diagram}, we get a graph of the type discussed above and
which therefore defines a number $Z_{RT}(\Ga)\in \kk$ (see, e.g.,
\ocite{BK} or \ocite{turaev}).

\begin{figure}[ht]
 \fig{figures/dual_graph2b}\qquad\qquad
 \tzSphereDiagram

\caption{Graph on a sphere and its ``flattening''
to the plane}\label{f:sphere_diagram}
\end{figure}


 
\begin{theorem}\ocite{barrett}\label{t:spherical1}
  The number $Z_{RT}(\Ga)\in \kk$ does not depend on the choice of a point 
  to remove from $S^2$ or on the choice of  order of edges at
  vertices compatible with the given cyclic order and thus defines an
  invariant of colored graphs on the sphere.
\end{theorem}
