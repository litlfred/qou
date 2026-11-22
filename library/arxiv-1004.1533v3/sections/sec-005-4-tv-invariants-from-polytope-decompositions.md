---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-005-4-tv-invariants-from-polytope-decompositions
section_title: "TV invariants from polytope decompositions"
section_number: 4
pages: 15-20
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.975
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:TV}

In this section, we recall the definition of Turaev--Viro (TV) invariants
of 3-manifolds. Our exposition essentially follows the approach of
Barrett and Westbury \ocite{barrett}; however, instead of triangulations we
use more general polytope decompositions as defined in the previous
section. 



Let $\C$ be a spherical fusion category as in \seref{s:prelim}, and $\M$
--- a combinatorial 3-manifold. We denote by $E$ the set of oriented edges
(1-cells) of $\M$. Note that each 1-cell of $\M$ gives rise to two oriented
edges, with opposite orientations. 

\begin{definition}\label{e:labeling}
 An  {\em labeling} of $\M$ is a map $l\colon E\to \Obj \C$ which assigns
  to every oriented edge $e$ of $\M$ an object $l(e)\in \Obj \C$ such that
  $l(\ov{e})=l(e)^*$. A labeling is called simple if for every edge,
  $l(e)$ is simple.  
 
  Two labelings are called equivalent if $l_1(e)\simeq l_2(e)$ for every
  $e$. 
\end{definition}

Given a combinatorial 3-manifold $\M$ and a labeling $l$, we
define, for every oriented 2-cell $C$, the state space
\begin{equation}\label{e:H(C)}
 H(C,l)=\<l(e_1), l(e_2),\dots, l(e_n)\>,\qquad 
 \del C=e_1\cup e_2\dots\cup e_n
\end{equation}
where the edges $e_1,\dots, e_n$ are taken in the counterclockwise order on
$\del C$ as shown in \firef{f:state_space1}.

  \begin{figure}[ht]
  \tzStateSpaceI
  \hspace{1.5cm} $H(C,l)=\<X_1,X_2,\dots, X_5\>$
  \caption{Defining the state space for a 2-cell}\label{f:state_space1}
  \end{figure}



Note that by \eqref{e:cyclic}, up to a canonical isomorphism, the state
space only depends  on the cyclic order of $e_1,\dots, e_n$ (which is
defined by $C$) and does not  depend on the choice of the starting point.

If $\N$ is an oriented 2-dimensional combinatorial manifold, we define the
state space
$$
H(\N,l)=\bigotimes_C H(C,l)
$$
where the product is over all 2-cells $C$, each taken with 
orientation induced from orientation of $\N$. 

Finally, we define
\begin{equation}\label{e:H(N)}
 H(\N)=\bigoplus_{l}H(\N,l),
\end{equation}
where the sum is over all simple labelings up to equivalence.

In the case when $\N$ is a triangulated surface, this definition
coincides with the one in \ocite{barrett}.


Note that it is immediate from \eqref{e:dual} that we have canonical
isomorphism
\begin{equation}\label{e:H-duality}
H(\ov{\N})=H(\N)^*.
\end{equation}

Next, we define the TV invariant of 3-manifolds. Let $\M$ be a
combinatorial 3-manifold with boundary. Fix a labeling $l$ of edges of
$\M$. Then every  3-cell $F$ defines a vector
$$
Z(F,l)\in  H(\del F,l)
$$
defined as follows. Recall that $F$ is an inclusion 
$F\colon (0,1)^3\to M$. The pullback of the polytope  decomposition of
$\M$  gives a polytope decomposition of $\del (0,1)^3\simeq S^2$. Consider
the dual  graph $\Ga$ of this decomposition and  choose an
orientation for every edge of this dual graph (arbitrarily) as shown in
\firef{f:dual_graph}.




   \begin{figure}[ht]
   $$\fig{figures/dual_graph2a.eps}\xxto{}\fig{figures/dual_graph2b.eps}$$
  \caption{The dual graph on the boundary of a 3-cell}\label{f:dual_graph}
  \end{figure}




Note that a labeling $l$ of $\M$ defines  a labeling of edges of this dual
graph as shown in \firef{f:state_space2}. Moreover, choose, for every face
$C\in \del F$, an element $\ph_C\in H(C,l)^*=\<l(e_n)^*,\dots, l(e_1)^*\>$.
Then this collection of morphisms defines a coloring of  vertices of
$\Ga$.


   \begin{figure}[ht]
   \tzStateSpaceII
  \qquad $\ph_C \in H(C,l)^*=\<X_5^*,X_4^*, \dots, X_1^*\>$
  \caption{Coloring of the dual graph}\label{f:state_space2}
  \end{figure}




By \thref{t:spherical1}, we get an invariant $Z_{RT}(\Ga)\in \kk$, which
depends on the choice of labeling of edges $l$ and on the choice of
morphisms $\ph_C$.  We define $Z(F,l)\in \otimes_{C}H(C,l)$
by 
\begin{equation}\label{e:Z(F)}
(Z(F,l), \otimes \ph_C)=Z_{RT}(\Ga, l, \{\ph_C\}).
\end{equation}

Again, if $F$ is a tetrahedron, then this coincides with the definition in
\ocite{barrett}; if $\C$ is the category of representations of
quantum $\mathfrak{sl}_2$, these numbers are the $6j$-symbols. 

We can now give a definition of the TV invariants of combinatorial
3-manifolds.

\begin{definition}\label{d:TV_invariant}
  Let $\M$ be a combinatorial 3-manifold with boundary and $\C$ -- a
  spherical category. Then for any coloring $l$, define a vector 
$$
Z_{TV}(\M,l)\in  H(\del \M,l)
$$
by 
$$
Z_{TV}(\M,l)=\ev\Bigl(\bigotimes_F Z(F,l)\Bigr)
$$
where 
\begin{itemize}
  \item $F$ runs over all 3-cells in $M$,   each taken with the induced
    orientation, so that  
    $$
      \bigotimes_F Z(F,l)\in \bigotimes_F H(\del F,l)=H(\del \M,l)\otimes
      \bigotimes_{c}  H(c',l)\otimes H(c'',l)
    $$
    (compare with \leref{l:delF})  

  \item $c$ runs over all unoriented 2-cells in
    the interior of   $M$, $c', c''$ are the two orientations of such a
    cell, so that   $c'=\ov{c''}$. 
  \item $\ev$ is the tensor product over all $c$ of evaluation maps
    $H(c',l)\otimes  H(c'',l)=H(c',l)\otimes H(c',l)^*\to \kk$
\end{itemize}

Finally, we define
$$
Z_{TV}(\M)=\DD^{-2v(\M)}\sum_{l} \Bigl(
Z_{TV}(\M,l)\prod_{e}d^{n_e}_{l(e)}\Bigr)
$$
where 
\begin{itemize}
\item the sum is taken over all equivalence classes of simple labelings
  of $\M$,
\item $e$ runs over the set of all (unoriented) edges of $\M$
\item $\DD$ is the dimension of the category $\C$ (see \eqref{e:DD}), and
$$
v(\M)=\text{number of internal vertices of } \M+\frac{1}{2}\text{(number of
vertices on }\del \M)
$$
\item $d_{l(e)}$ is the categorical dimension of $l(e)$ and 

$$n_e=\begin{cases}1, &\quad e \text{ is an internal edge}\\
                   \tfrac{1}{2}, &\quad e \in \del \M
                   \end{cases}
$$
\end{itemize}
\end{definition}

It is easy to see that in the special case of triangulated manifold, this
coincides with the construction in \ocite{barrett}.

\begin{theorem}\label{t:main1}
  If $M$ is a PL manifold without boundary, then the
  number $Z_{TV}(M)\in \kk$ defined in \deref{d:TV_invariant} does not
  depend on the choice of polytope decomposition of $M$: for any two
  choices of polytope decomposition, the resulting 
  invariants are equal.
\end{theorem}
The proof of this theorem will be given in \seref{s:proof}.

These invariants can be extended to a TQFT. Namely, let $\M$ be a
combinatorial 3-cobordism between two 2-dimensional combinatorial
manifolds $\N_1,\N_2$, i.e a combinatorial manifold $\M$ with boundary such
that $\del \M=\ov{\N_1}\sqcup \N_2$ (note that the combinatorial structure
on $M$ automatically defines a combinatorial structure on $\del M$). Then
$H(\del \M)=H(\N_1)^*\otimes H(\N_2)=\Hom_\kk(H(\N_1),H(\N_2))$, so
\deref{d:TV_invariant} defines an element $Z(\M)\in
\Hom_\kk(H(\N_1),H(\N_2))$, i.e. a linear operator 
$$
Z(\M)\colon H(\N_1)\to H(\N_2).
$$


\begin{theorem}\label{t:main2}
\par\noindent
  \begin{enumerate}
      \item So defined invariant satisfies the gluing axiom: if $\M$ is a
        combinatorial 3-manifold with boundary $\del \M=\N_0\cup
        \N\cup\ov{\N}$, and $\M'$ is the manifold obtained by identifying
        boundary components $\N,\ov{\N}$ of $\del\M$ with the obvious cell
        decomposition, then  we have
    $$
      Z_{TV}(\M')=\ev_{H(\N)}Z_{TV}(\M)=\sum_\al (Z_{TV}(\M),
          \ph_\al\otimes \ph^\al),
    $$
        where $\ev$ is the evaluation map $H(\N)\otimes H(\ov{\N})\to
        \kk$, and $\ph_\al\in H(\N)$,  $\ph^\al\in H(\ov{\N})$ are dual
        bases. 
 
      \item If a $M$ is a 3-manifold with boundary, and $\M', \M''$ are two
        polytope decompositions of $M$  which agree     on the
        boundary, then
        $Z(\M')=Z(\M'')\in H(\del \M')=H(\del \M'')$. 
        
    \item For a combinatorial 2-manifold $\N$, define $A_{\N}\colon H(\N)\to
      H(\N)$ by 
      \begin{equation}\label{e:projector}
       A_{\N}=Z_{TV}(\N\times I)
      \end{equation}
       Then $A_{\N}$ is a projector: $A_{\N}^2=A_{\N}$.
      
      
    \item For a combinatorial 2-manifold $\N$, define the vector space
    \begin{equation}\label{e:modular_functor}
    Z_{TV}(\N)=\mathrm{Im}(A_{\N}\colon H(\N)\to H(\N))
    \end{equation}
  where $A$ is the projector \eqref{e:projector}.
  Then the space $Z_{RT}(N)$ is an invariant of PL manifolds: if $\N',
  \N''$ are two different polytope decompositions of the same PL manifold
  $N$, then one has a canonical isomorphism $Z(\N')\simeq Z(\N'')$.
   
  \item The assignments $N\mapsto Z_{TV}(N)$, $M\mapsto Z_{TV}(M)$ give a
  functor from the category of PL 3-cobordisms to the category of
  finite-dimensional vector spaces and thus define a $2+1$-dimensional
  TQFT.
\end{enumerate}

\end{theorem}
\begin{proof}
   Part (1) is immediate from the definition. 

   Part (2) will be proved in \seref{s:proof}.

    To prove part (3), note that
    gluing of two cylinders again gives a cylinder, so (3) follows from
    (1) and (2). 
  
  To prove (4), let $\N', \N''$ be two different polytope decompositions of
  $N$. Consider the cylinder $C=N\times I$ and choose a polytope
    decomposition of $C$ which agrees with $\N'$ on $N\times\{0\}$ and
    agrees with $\N''$ on $N\times\{1\}$ (existence of such a
      decomposition follows from \thref{t:moves_rel}).  Consider the
    corresponding operator 
    $F_1=Z(C)\colon  H(\N')\to H(\N'')$. In a similar way, define an
    operator $F_2\colon 
    H(\N'')\to H(\N')$. Then it follows from (2) that $F_1F_2=A_{\N''}$,
    and $F_2F_1=A_{\N'}$. Thus, $F_1, F_2$ give rise to mutually
    inverse isomorphisms $Z_{TV}(\N')\to Z_{TV}(\N'')$. 
    
    
   Part (5) follows immediately from (1)--(4).
    
\end{proof}

Note that in the PL category, gluing along a boundary component is well
defined: gluing together PL manifolds results canonically in a PL
manifodl (unlike the smooth category). 

\begin{example}\label{x:H(S)}
  Let $G$ be a finite group and $\C=\VecG$ --- the category of $G$-graded
  vector spaces, with obvious  tensor structure. Then a simple labeling is
  just labeling of edges of $\M$ with elements of the group $G$, and for a
  2-cell $C$, we have
  $$
  H(C,l)=\begin{cases} \kk, &\prod_{\del C} l(e)=1\\
                      0, & \text{otherwise}
          \end{cases}
  $$
  Thus, we see that in this case the state space $H(\N)$ is the space of
  flat $G$---connections (which depends on the choice of polytope
  decomposition!). It is well-known that in this case the projector
  $A=Z_{TV}(\Si\times I)$  is the operator of averaging over the action of
  the gauge group $G^{v(\N)}$, where $v(\N)$  is the set of vertices of $\N$. 
  Thus the space $Z(N)$ is the space of gauge equivalence classes of $G$--connections.
\end{example}
\begin{example}\label{x:2sphere}
We verify $Z_{TV}(S^2) =\kk$ as is required by the definition of a TQFT.
We pick the polytope decomposition of $S^2$ consisting of one vertex, one
edge and two faces as shown in \firef{f:2sphere}.

   \begin{figure}[ht]
   \fig{figures/S2.eps}
  \caption{The polytope decomposition of $S^2$}\label{f:2sphere}
  \end{figure}

Using the fact that for $X_i$, $X_j$
simple $\Hom(X_i,X_j) = \delta_{ij}\kk$, it is easy to see that $H(S^2)
=\bigoplus_i \<X_i\>\otimes \<X_i^*\>= \kk$. It remains to show that
$A\colon  H(S^2) \rightarrow H(S^2)$ is the identity map or equivalently,
the induced map $H(S^2) \otimes H(S^2)^* \rightarrow \kk$ equals the
canonical pairing defined in \seref{s:prelim}. Consider the cylinder
$S^2\times I$ with cell decomposition as in \firef{f:saturn}. Note that
both boundary edges must be labeled by $\one$.

   \begin{figure}[ht]
   \fig{figures/sat.eps}
  \caption{The cylinder over  $S^2$}\label{f:saturn}
  \end{figure}

The computation is then
straightforward: 
\begin{align*}
&\frac{1}{\DD^2}\sum_{X\in \Irr(\C)}d_X
\tzSphereProofI \cdot \tzSphereProofII 
=\frac{1}{\DD^2}\sum_{X\in \Irr(\C)}
\tzSphereProofIII \cdot \tzSphereProofIV \\
&\quad =\frac{1}{\DD^2}\sum_{X\in \Irr(\C)}d^2_X
 =1.
\end{align*}
The first equality follows from the
normalization of the pairing. The other two equalities are obvious. 

\end{example}
