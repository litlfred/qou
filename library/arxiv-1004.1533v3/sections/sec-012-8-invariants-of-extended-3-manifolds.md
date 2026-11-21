---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-012-8-invariants-of-extended-3-manifolds
section_title: "Invariants of extended 3-manifolds"
section_number: 8
pages: 27-34
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.944
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:ext_mfds}
We begin by generalizing the definition of a polytope decomposition to
extended 3-manifolds as defined in \deref{d:ex_manifold}.

\begin{definition}\label{d:comb_ex_manifold}
 A combinatorial extended 3-manifold $\M$ is  an extended PL 3-manifold
  with a polytope decomposition such that

  \begin{itemize}
   \item For an open tube $T_\al$, its interior is a single 3-cell of the
    decomposition. Moreover, the interior of the  ``bottom disk''
    $B_0=\ph_\al(\{0\}\times D^2)$ is a single 2-cell of the decomposition,
    and the marked point $P$ on the boundary of the bottom disk is a
    vertex of the decomposition, and similarly for the top disk
    $B_1=\ph_\al(\{1\}\times D^2)$.

   \item For a closed tube $T_\al$, the interior of the  disk
    $B_\al=\ph_\al(\{0\}\times D^2)$ is a single 2-cell of the
    decomposition, the marked point $P_\al\in \del B_\al$ is a vertex of
    the decomposition, and the complement $\Int(T_\al)-B_\al$ is
    a single 3-cell of the decomposition.

  \end{itemize}
\end{definition}

Note that this implies that the restriction of such a polytope
decomposition to the boundary of $\del M$ satisfies the conditions of
\deref{d:comb_ex_surface} and thus defines on $\del M$ the structure of a
combinatorial extended surface. It also this implies that $\M$
contains two kinds of 3-cells: usual cells (which are not contained in any
tube) and ``tube cells'', i.e. cells contained in one of the tubes. The
boundary of a usual 3-cell is a union of usual 2-cells; the boundary of a
 3-cell corresponding to an open  tube contains usual 2-cells and two
embedded disks;
the boundary of a  3-cell corresponding to a closed tube contains usual
2-cells and two copies of the disk $B_\al$ with opposite orientation. 

Finally, note that we have imposed no restriction on the longitude of the
tube: it is allowed (and usually will) intersect the edges of the
decomposition of the boundary tubes. 


The following theorem is an analog of \thref{t:moves_rel}.

\begin{theorem}\label{t:moves_ext}
 Let $M$ be an extended 3-manifold. Then any two polytope decompositions
$\M', \M''$ of $\M$ which satisfy the conditions of
\deref{d:comb_ex_manifold} and agree on $\del M$ can be obtained  from
each other by a sequence of moves M1---M3 and their inverses such that all
intermediate decompositions also satisfy the conditions of
\deref{d:comb_ex_manifold} and agree with $\M', \M''$ on $\del M$.
\end{theorem}
\begin{proof}
Let us consider the manifold $\tilde M$ obtained by removing from $M$ the
interior of every tube and also the interior of the embedded disks on the
boundary of $M$. Then $\tilde M$ is a manifold with boundary
$$
\del \tilde M=(\del M-\cup \Int(D_\al))\cup \del \tilde M_{free}
$$
where the ``free boundary'' $\del \tilde M_{free}$ is the union of side
surfaces $I\times \del D^2$ of the tubes (for closed tubes, $S^1\times
\del D^2$).

Obviously, polytope decompositions $\M', \M''$ satisfying the conditions
of the theorem determine decomposition of $\tilde M$ which agree on the
subset $X=(\del M-\cup \Int(D_\al))\subset \del \tilde M$. Now the result
follows from \thref{t:moves_rel2}.
\end{proof}




Recall that for usual oriented  3-cell $F$ and a choice of edge labeling
$l$, we have defined the vector $Z_{TV}(F,l)\in H(\del
F,l)$ defined by \eqref{e:Z(F)}. We can now generalize it to tube
cells. Namely, let $l$ be an edge coloring of an extended
combinatorial 3-manifold $\M$ and let $T_\al\subset M$ be an open tube,
with the longitude $\ga_\al$ and color $Y_\al\in Z(\C)$. Since $T$ is
homeomorphic to $[0,1]\times D^2\simeq D^3$--- a 3-ball, the boundary
$\del T$ is homeomorphic to $S^2$; thus, the polytope
 decomposition of $T$ defines a polytope decomposition of $S^2$. 

 Let $\Ga$ be  the dual graph of this cell decomposition. We can connect
the marked points on the top and bottom disks to the vertex of the dual
graph corresponding to these disks; together with  the longitude $\ga$,
this gives an oriented arc on the surface of the sphere whose endpoints
are two distinct vertices of $\Ga$. For every 2-cell
$C\in \del F$ (including the embedded disks), choose a vector $v_C\in
H (C,l)^*$. Thus,  we get a graph $\hat\Ga$ of the type considered in
\seref{s:center}, i.e.  colored graph $\Ga$ on the surface of the sphere
together with a colored framed arc inside as shown in \firef{f:dual_tube}. 
\begin{figure}[ht]
  \fig{figures/dual_tube_a.eps}\qquad \fig{figures/dual_tube_b.eps}\qquad
\fig{figures/dual_tube_c.eps}
  \caption{Dual graph for a tube cell. The longitude is shown by double
green line. }\label{f:dual_tube}
\end{figure}
By \thref{t:spherical2} this
defines a number $Z_{RT}(\hat\Ga)$; as before, we let
\begin{equation}\label{e:Z(F)_ex}
(Z(F,l), \otimes v_C)=Z_{RT}(\hat\Ga).
\end{equation}

In a similar way we define the invariant for closed tubes. 

We can now generalize the constructions of \seref{s:TV}  to
extended 3-manifolds. 




\begin{definition}\label{d:TV_invariant_ex}
  Let $\M$ be an extended combinatorial 3-manifold with boundary and $\C$
-- a  spherical category. Then for any edge coloring $l$ and a
coloring $Y_\al$ of the tubes $T_\al\subset \M$, define the vector
$$
Z_{TV}(\M, \{Y_\al\}, l)\in  H(\del \M,\{Y_\al\},l)
$$
by 
$$
Z_{TV}(\M,l)=\ev\Bigl(\bigotimes_F Z(F,l)\Bigr)
$$
where 
\begin{itemize}
    \item $F$ runs over all 3-cells in $M$ (including the tube cells),  
    each taken with the induced orientation, so that  
    $$
      \bigotimes_F Z(F,l)\in \bigotimes_F H(\del F,l)=H(\del
\M,l)\otimes
      \bigotimes_{c}  H(c',l)\otimes H(c'',l)
    $$
    (compare with \leref{l:delF})  

  \item $c$ runs over all unoriented 2-cells in
    the interior of   $M$, including the disks $B_\al$ inside the closed
     tubes, and $c', c''$ are the two orientations of such a
    cell, so that   $c'=\ov{c''}$. 
  \item $\ev$ is the tensor product over all $c$ of evaluation maps
    $H(c',l)\otimes  H(c'',l)=H(c',l)\otimes H(c',l)^*\to \kk$
\end{itemize}


Finally, we define
\begin{equation}\label{e:Z_ext}
Z_{TV}(\M,\{Y_\al\})=\DD^{-2v(\M)}\sum_{l} \Bigl(
Z_{TV}(\M,\{Y_\al\},l)\prod_{e}d^{n_e}_{l(e)}\Bigr)
\end{equation}
where 
\begin{itemize}
\item the sum is taken over all equivalence classes of 
   simple labellings of $\M$,
\item $e$ runs over the set of all (unoriented) edges of $\M$
\item $\DD$ is the dimension of the category $\C$ (see \eqref{e:DD}), and
  $$
  v(\M)=\text{number of internal vertices of } \M+
   \frac{1}{2}\text{(number of vertices on }\del \M)
$$
\item $d_{l(e)}$ is the categorical dimension of $l(e)$ and 

$$n_e=\begin{cases}1, &\quad e \text{ is an internal edge}\\
                   \tfrac{1}{2}, &\quad e \in \del \M
                   \end{cases}
$$
\end{itemize}
\end{definition}
Note that in this definition, edges and vertices on the boundary of the
tubes are considered internal unless they are also on $\del \M$. 


\begin{theorem}\label{t:main4}
\par\noindent
  \begin{enumerate} 
      \item $Z_{TV}(\M)$ satisfies the gluing axiom: if $\M$ is an
        extended combinatorial 3-manifold with boundary $\del \M=\N_0\cup
        \N\cup\ov{\N}$, and $\M'$ is the manifold obtained by identifying
        boundary components $\N,\ov{\N}$ of $\del \M$ with the obvious cell
        decomposition \textup{(}if $\N$  contains embedded disks,
          then we may need to erase them so that the interior of 
            resulting tubes have  exactly  one 3-cell\textup{)}, then we
        have
    $$
      Z_{TV}(\M')=\ev_{H(\N)}Z_{TV}(\M)=\sum_\al (Z_{TV}(\M),
          \ph_\al\otimes \ph^\al),
    $$
        where $\ev$ is the evaluation map $H(\N)\otimes H(\ov{\N})\to
        \kk$, and $\ph_\al\in H(\N)$,  $\ph^\al\in H(\ov{\N})$ are dual
        bases.
 

      \item If a $M$ is an extended  PL 3-manifold, and $\M',
          \M''$ are two polytope
        decompositions of $M$  which agree     on the boundary, then
        $Z(\M',\{Y_\al\})=Z(\M'',\{Y_\al\})$. 
        
    \item For a combinatorial 2-manifold $\N$, define $A\colon H(\N)\to
      H(\N)$ by 
      \begin{equation}\label{e:projector2}
       A=Z_{TV}(\N\times I)
      \end{equation}
       Then $A$ is a projector: $A^2=A$.
      
      
    \item For a combinatorial extended  2-manifold $\N$, define the vector
        space
     \begin{equation}\label{e:modular_functor2}
    Z_{TV}(\N)=\mathrm{Im}(A\colon H (\N)\to H (\N))
    \end{equation}
  where $A$ is the projector \eqref{e:projector2}.
  Then the space $Z_{RT}(\N)$ is an invariant of PL manifolds: if $\N',
  \N''$ are two different polytope decompositions of the same extended PL
    manifold  $N$, then one has a canonical isomorphism $Z(\N')\simeq
  Z(\N'')$.
\end{enumerate}
\end{theorem}
\begin{proof}
 The proof is parallel to the proof of \thref{t:main2}. The only
 new ingredient is in the proof of part (1), i.e. the gluing axiom for
  3-manifolds: if the component of boundary along which we are gluing
    contains embedded disks, we need to erase them so that in the
  resulting manifold, interior of each tube is exactly one 3-cell. Thus,
  we need to check that our that $Z(\M)$ is unchanged under this
  operation. The proof of this is similar to invariance under M3 move
  proved in \seref{s:proof}. Details are left to the reader. 

\end{proof}


Finally, we also note that our extended theory satisfies the gluing axiom
for extended surfaces. 
\begin{theorem}\label{t:gluing_surfaces2}
  Under the assumptions of \thref{t:gluing_surfaces}, one has a natural
  isomorphism
$$
Z(\N', \{Y_\al\}_{\al\in D'})=
\bigoplus_{Z\in \Irr(Z(\C))} Z(\N, \{Y_\al\}_{\al\in D'},
Z, Z^*)
$$
where objects $Z,Z^*$ are assigned to embedded disks $a,b$.
\end{theorem}
\begin{proof}
  Recall that by  \thref{t:gluing_surfaces}, one has an isomorphism
  $$
  G\colon \bigoplus_{Z\in \Irr(Z(\C))} H(\N, \{Y_\al\}_{\al\in D'},
Z, Z^*)\isoto H(\N', \{Y_\al\}_{\al\in D'})
  $$
   Since $Z(\N)$ is defined as the image of the projector $A\colon H(\N)\to
H(\N)$, and similarly for $Z(\N')$, it suffices to prove that the
following diagram is commutative: 
$$\begin{tikzpicture}
\matrix[column sep=1cm,row sep=20pt]
{ \node (m11)  {$H(\N, Z,Z^*)$}; &
 \node (m12)  {$H(\N')$};\\
 \node (m21)  {$H(\N, Z,Z^*)$}; &
 \node (m22)  {$H(\N')$};\\
};
\draw[->] (m11)--(m12) node[pos=0.5,above]{$G$};
\draw[->] (m21)--(m22) node[pos=0.5,above]{$G$};
\draw[->] (m11)--(m21) node[pos=0.5,left]{$A$};
\draw[->] (m12)--(m22) node[pos=0.5,right]{$A'$};
\end{tikzpicture}
$$
or equivalently, that for any $\ph\in H(\N, Z,Z^*)$, $\ph'\in H(\ov{\N},
Z,Z^*)$, we have 
$$
(Z(\N\times I,Z,Z^*), \ph\otimes \ph')=
(Z(\N'\times I), G(\ph)\otimes G(\ph')).
$$

Comparing both sides, we see that the only difference is that $\N\times I$ 
contains a pair of cylinders $D_a\times I, D_b\times I$:
$$
\tzGluingV
$$
whereas $\N'\times I$ contains instead a single  cell $C\times I$, where $C$ 
is the cylinder connecting boundary circles $\del D_a, \del D_b$:
$$
\tzGluingVI
$$

Thus, it suffices to prove that for any collection 
\begin{alignat*}{2}
&\ph_a\in H(D_a)=\<A,Z\>,\qquad && \ph_b\in H(D_b)=\<B,Z^*\>,\\
&\ph'_a\in H(D_a)^*=\<(A')^*,Z^*\>,\qquad &&\ph_b\in H(D_b)^*=\<(B')^*,Z\>,\\
&\psi_a\in H(\del D_a\times I)=\<X_k,A',X_k^*, A^*\>,\qquad &&
  \psi_b\in H(\del D_b\times I)=\<X_l,B',X_l^*, B^*\>
\end{alignat*}
we have 
\begin{align*}
&Z(D_a\times I, \ph_a\otimes\ph_a'\otimes \psi_a) 
\cdot  Z(D_b\times I, \ph_b\otimes\ph_b'\otimes \psi_b) \\
&\quad=\sum_{i,j}\sqrt{d_i}\sqrt{d_j}\ Z(C\times I, \psi_a,\psi_b, G (\ph_a\otimes \ph_b),
  G (\ph'_a\otimes \ph'_b))
\end{align*}
(the factors $\sqrt{d_i}$, $\sqrt{d_j}$ appear because $\N'\times I$ contains two 
extra edges on the boundary, labeled $i,j$.)


The left hand side is given by 
$$
LHS=\tzGluingI\cdot\qquad  \tzGluingII
$$
Combining explicit computation given in \seref{s:computations1} with the
formula for gluing in \leref{l:gluing_isom2}, we see that  the right hand
side is given by
$$
RHS=\sum_{i,j} \frac{d_i d_j d_Z}{\DD^2} \tzGluingIII
$$
Using \leref{l:pairing}, we can rewrite it as
$$
RHS=\sum_{j} \frac{d_j d_Z}{\DD^2}\tzGluingIV
$$
Since it follows from \leref{l:projector} that for any simple $Z\in \Obj Z(\C)$ and a morphism $\Ph\in \Hom_\C(Z,Z)$, we have 
$$
\frac{1}{\DD^2}\sum_j d_j \quad \tzProjectionIa = \frac{1}{d_Z} \tr (\Ph) \id_Z
$$
this easily implies that the LHS is equal to RHS. 



\end{proof}


\begin{example}\label{x:Z(S)}
  Let $\N$ be the sphere with $n$ embedded disks,
colored by objects $Y_1,\dots, Y_n\in \Obj Z(\C)$ (see
\exref{x:n-sphere}). Then 
$$
Z(\N,Y_1, \dots, Y_n)=\Hom_{Z(\C)}(\one, Y_1\otimes
Y_2\otimes\dots\otimes Y_n).
$$
Indeed, by \exref{x:n-sphere}, we have 
$$
H(\N,Y_1, \dots, Y_n)=\bigoplus_{i_1,\dots, i_n\in \Irr(\C)}
\<X_{i_1}, Y_1, X_{i_1}^*,\dots, X_{i_n}, Y_n, X_{i_n}^*\>.
$$

By a direct computation done  in \seref{s:computations}, we see that the 
operator $A=Z(\N\times I)\colon H(\N)\to H(\N)$  is given by 
\begin{align*}
\ph \mapsto &\frac{1}{\DD^{2(n+1)}}\sum_{l, j_1,\dots, j_n\in \Irr(\C)} 
d_l \prod_{a=1}^n 
         \sqrt{d_{i_a}} \sqrt{d_{j_a}} \\
&\qquad \tzNsphereV
\end{align*}

Consider now the subspace $W\subset H(\N,Y_1, \dots, Y_n)$ spanned by
elements of the form
\begin{align*}
&\bigoplus_{j_1,\dots, j_n}\prod_{a=1}^n \sqrt{d_{j_a}} \quad 
\tzNsphereVI\\[10pt] 
&\quad  \psi\in \Hom_{Z(\C)}(\one,
Y_1\otimes\dots\otimes  Y_n)
\end{align*}
Clearly, $W\simeq \Hom_{Z(\C)}(\one, Y_1\otimes\dots\otimes  Y_n)$.

Now, it follows from the previous computation and \leref{l:projector}
that for any $\ph \in H(\N, Y_1,\dots, Y_n)$, we have $A\ph\in W$; on the
other hand, it is immediate that if $\psi\in W$,
then $A\psi=\psi$. Therefore, $A$ is the projector onto $W\simeq
\Hom_{Z(\C)}(\one, Y_1\otimes\dots\otimes  Y_n)$.


\end{example}
