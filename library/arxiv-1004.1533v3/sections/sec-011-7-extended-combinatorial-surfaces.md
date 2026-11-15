---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-011-7-extended-combinatorial-surfaces
section_title: "Extended combinatorial surfaces"
section_number: 7
pages: 24-27
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.925
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:ext_surfaces}
We begin by generalizing the definition of a polytope decomposition to
extended surfaces.

\begin{definition}\label{d:comb_ex_surface}
    A  combinatorial extended surface $\N$ is a an extended surface $N$
  together with a  polytope decomposition such that
\begin{enumerate}
  \item The interior of each embedded disk is one of the 2-cells of the
    polytope decomposition.
  \item Each marked point $P_\al$ on the boundary of an embedded disk is a
    vertex (0-cell) of the polytope decomposition. 
\end{enumerate}
\end{definition}

We can now define the state space for such a surface. Let $\N$ be
a combinatorial extended surface, and $Y_\al, \al\in D(N)$, --- a
coloring of $\N$. Let $l$ be a labeling of edges of $\N$. Then we define
the state space
$$
H(\N, \{Y_\al\},l)=\bigotimes_C  H(C,l)
$$
where the product is over all 2-cells of $\N$ (including the embedded
disks) and
$$
H(C,l)=\begin{cases}
\<Y_\al,l(e_1), l(e_2),\dots, l(e_n)\>&\quad
                  C=D_\al \text{ -- an embedded disk}\\
\<l(e_1), l(e_2),\dots, l(e_n)\>&\quad C \text{ -- an ordinary 2-cell of
$\N$}
\end{cases}
$$
where $e_1,e_2,\dots$ are edges of $C$ traveled counterclockwise;
for the embedded disks, we also require that we start with the
marked point $P_\al$; for ordinary 2-cells of $\N$ the choice of starting
point is not important.

As usual, we now define
\begin{equation}\label{e:ex_state_sum}
  H(\N, \{Y_\al\})=\bigoplus_{l}H(\N, \{Y_\al\},l)
\end{equation}
where the sum is taken over all equivalence classes of simple labellings
$l$ of edges of $\N$. 

Note that so defined state space is functorial in $Y_\al$ and functorial
under homeomorphism of extended surfaces;  it is
 also immediate from the definition that one has a canonical isomorphism
$$
H(\ov{\N},Y^*_\al)=H(\N,Y_\al)^*.
$$


\begin{example}\label{x:n-sphere}
Let $\N$ be the sphere with $n$ embedded disks and the cell decomposition
shown in \firef{f:n-sphere}. 

\begin{figure}[ht]

\fig{figures/n-sphere.eps}
\caption{$n$-punctured sphere}\label{f:n-sphere}
\end{figure}

Then
\begin{align*}
&H(\N,Y_1, \dots, Y_n)\\
&\qquad=\bigoplus_{X_1,\dots, X_n, U_1,
\dots, U_n\in \Irr(\C)}
\<X_1,U_1,X_1^*,\dots, X_n, U_n, X_n^*\>\otimes
\<U_1^*,Y_1\>\otimes\dots\otimes \<U_n^*,Y_n\>\\
&\qquad\simeq\bigoplus_{X_1,\dots, X_n\in \Irr(\C)}
\<X_1,Y_1,X_1^*,\dots, X_n, Y_n, X_n^*\>.
\end{align*}
where the last isomorphism is given by direct sum of rescaled compositions
\eqref{e:composition2}.
\end{example}



The first main result of this paper is the gluing axiom for the so defined
state space.

\begin{theorem}\label{t:gluing_surfaces}
Let $\N$ be a combinatorial extended surface and $D_a, D_b$ --- two
distinct embedded disks.  Let $\N'$ be the extended
surface obtained by removing the disks $D_a$, $D_b$ and connecting
the resulting boundary circles with a cylinder with the polytope
decomposition consisting of a single 2-cell and a single 1-cell as shown
below:

\begin{figure}[ht]
\fig{figures/gluing_surfaces-a.eps}

\fig{figures/gluing_surfaces-b.eps}

\caption{Gluing of extended surfaces. To help
visualize the cylinder, it is colored light gray.}\label{f:gluing_surfaces}
\end{figure}


Thus, the set $D'$ of embedded disks of $\N'$ is
$D'=D(\N)\setminus\{a,b\}$


Then one has a natural isomorphism
$$
H(\N', \{Y_\al\}_{\al\in D'})=
\bigoplus_{Z\in \Irr(Z(\C))} H(\N, \{Y_\al\}_{\al\in D'},
Z, Z^*)
$$
where objects $Z,Z^*$ are assigned to embedded disks $D_a,D_b$.
\end{theorem}
\begin{proof}
For a given labeling $l$ of edges of $\N$, let
$$
H_0(l)=\bigotimes_C H (C,l)
$$
where the product is taken over all 2-cells of $\N$ (including the
embedded disks) except $D_a$, $D_b$. 
Then
$$
H(\N,\{Y_\al\}, Z, Z^*, l)=H_0(l)\otimes 
 \<Z, A\>\otimes \<Z^*, B\>
$$
where $A=l(e_1)\otimes l(e_2)\dots\otimes  l(e_n)$, 
where $e_1,e_2,\dots$ are edges of $D_a$ traveled counterclockwise
starting with the marked point $P_a$, and similarly for $B$.

On the other hand, for a given labeling $l'$ of edges of $\N'$, we have
$$
H(\N', \{Y_\al\}, l')=H_0(l)\otimes \<A\otimes l(e) \otimes B\otimes
l(e)^*\>
$$
where $l$ is the restriction of labeling $l'$ to edges of $\N$, and $e$ is
the added  edge connecting marked points $P_a$, $P_b$.

Thus, the theorem immediately follows from the following lemma.


\begin{lemma}\label{l:gluing_isom2} 
For any $A,B\in \Obj \C$, the map
\begin{equation}\label{e:gluing_isom2}
\begin{aligned}
\bigoplus_{Z\in \Irr(Z(\C))} \<Z, A\>\otimes \<Z^*, B\>&\to
  \bigoplus_{X\in \Irr(\C)}\<A, X , B, X^*\>\\
\ph\otimes \psi&\mapsto\bigoplus_{X\in \Irr(\C)}
\frac{\sqrt{d_X}\sqrt{d_Z}}{\DD} \quad \tzGluingAxiomI
\end{aligned}
\end{equation}
is an an isomorphism.
\end{lemma}
(The factor $\sqrt{d_X}\sqrt{d_Z}/\DD$ is introduced to make this isomorphism
agree with pairing \eqref{e:pairing}.)
\begin{proof}
By \thref{t:I}, we have
\begin{align*}
&\bigoplus_{X\in \Irr(\C)}\<A\otimes X \otimes B\otimes X^*\>
=\bigoplus_{X}\Hom_\C(A^*, X \otimes B\otimes X^*)
\\
&\quad=\Hom_\C(A^*, FI(B))=\Hom_{Z(\C)}(I(A^*), I(B))
\end{align*}
On the other hand, 
\begin{align*}
&\bigoplus_{Z\in \Irr(Z(\C))}
 \<Z, A\>\otimes \<Z^*, B\>=
\bigoplus_Z\Hom_\C(Z^*,A)\otimes \Hom_\C(Z,B)\\
&\quad
=\bigoplus_Z\Hom_{Z(\C)}(Z^*,I(A))\otimes \Hom_{Z(\C)}(Z,I(B))\\
&\quad=\bigoplus_Z\Hom_{Z(\C)}(I(A)^*, Z)\otimes
\Hom_{Z(\C)}(Z,I(B))\\
&\quad =\Hom_{Z(\C)}(I(A)^*,I(B))
\end{align*}
(using semisimplicity of $Z(\C)$). 
\end{proof}
This completes the proof of the lemma
and thus the theorem.
\end{proof}
