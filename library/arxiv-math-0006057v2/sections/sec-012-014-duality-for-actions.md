---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-012-014-duality-for-actions
section_title: "Duality for actions"
section_number: 0.14
pages: 14-16
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.956
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
An analogue of the Blattner-Montgomery duality theorem for
actions of quantum groupoids was proven in \cite{N2}.
Let $H$ be a finite quantum groupoid and
$A$ be a left $H$-module algebra. Then the smash product $A\#H$
is a left $\widehat H$-module algebra via
\begin{equation}
\label{dual action}
\phi\cdot (a\#h) = a\#(\phi\act h), \quad
\phi\in \widehat H,\,h\in H,\,a\in A.
\end{equation}
In the case when $H$ is a finite dimensional Hopf algebra,
there is an isomorphism
$(A\#H)\#\widehat H \cong M_n(A)$, where $n=\dim H$ and $M_n(A)$ is an algebra
of $n$-by-$n$ matrices over $A$ \cite{BM}.
This result extends to quantum groupoid
action in the form $(A\#H)\#\widehat H \cong \End(A\#H)_A$, 
where $A\#H$ is a right $A$-module
via multiplication (note that $A\#H$ is not necessarily a free $A$-module,
so that we have $\End(A\#H)_A\not\cong M_n(A)$ in general).

\begin{theorem}[\cite{N2}, 3.1, 3.2]
\label{BM-duality}
The map $\alpha : (A\#H)\#\widehat H \to \End(A\#H)_A$ defined by
$$
\alpha((x\#h)\#\phi)(y\#g) = (x\#h)(y\#(\phi\act g)) 
= x(h\1\cdot y) \#h\2 (\phi\act g) 
$$ 
for all $x,y\in A,\, h,g\in H,\,\phi\in \widehat H$ is an isomorphism of algebras.
\end{theorem}

\begin{proof}
A straightforward (but rather lengthly) computation shows  
that $\alpha$ is a well defined homomorphism, cf.\ (\cite{N2}, 3.1).
Let $\{ f_i\}$ be a basis of $H$ and $\{ \xi^i\}$ be the dual basis
of $\widehat H$, i.e., such that $\la f_i,\, \xi^j \ra =\delta_{ij}$ for
all $i,j$, then  the element $\sum_i\, f_i\otimes \xi^i \in H\otimes_k 
\widehat H$ does not depend on the choice of $\{ f_i\}$ and
the following map 
\begin{eqnarray*}
\beta 
&:& \End(A\# H)_A \to (A\# H)\# \widehat H \\
&:& T \mapsto \sum_i\, T(1\# {f_i}\2)(1\# S^{-1}({f_i}\1)) \# \xi^i.
\end{eqnarray*}
is the inverse of $\alpha$.
\end{proof}

\begin{corollary}
$H\# \widehat H \cong \End(H)_{H_t}$, therefore, $H\# \widehat H$ 
is a semisimple algebra.
\end{corollary}

\begin{proof} 
Theorem~\ref{BM-duality}
for $A=H_t$ shows that $H$ is a projective generating $H_t$-module
such that $\End(H)_{H_t} \cong H\# \widehat H$. Therefore, $H_t$ and
$H\# \widehat H$ are Morita equivalent. Since $H_t$ is semisimple
(as a separable algebra), $H\# \widehat H$ is semisimple.
\end{proof}

\end{section}





\begin{section}
{Representation category of a quantum groupoid}

Representation categories of quantum groupoids were studied in \cite{BSz2}
and \cite{NTV}.


\subsection{Definition of $\Rep(H)$}
For a quantum groupoid $H$
let $\Rep(H)$ be the category of  representations of $H$, whose objects are
$H$-modules of finite rank and whose morphisms are $H$-linear homomorphisms.
We show that, as in the case of Hopf algebras, $\Rep(H)$ has a natural 
structure of a monoidal category with duality.

For objects $V,W$ of $\Rep(H)$ set
\begin{equation}
V\otimes W = \{x \in V\otimes_k W \mid x= \Delta(1)\cdot x\},
\end{equation}
with the obvious action of $H$ via the comultiplication $\Delta$
(here $\otimes_k$ denotes the usual tensor product of vector spaces).

Since $\Delta(1)$ is an idempotent, 
$V\otimes W=\Delta(1)\cdot (V\otimes_k W)$.
The tensor product of morphisms is the restriction of usual
tensor product of
homomorphisms. The standard associativity isomorphisms
$\Phi_{U,V,W} : (U\otimes V)\otimes W \to U\otimes (V\otimes W)$
are functorial and satisfy the pentagon condition, since $\Delta$ is
coassociative. We will suppress these isomorphisms and write simply
$U\otimes V\otimes W$.

The target counital subalgebra $H_t\subset H$ has an $H$-module structure  
given by $h\cdot z = \eps_t(hz)$, where $h\in H,\, z\in H_t$.

\begin{lemma}
$H_t$ is the unit object of $\Rep(H)$.
\end{lemma}

\begin{proof}
Define a left unit homomorphism $l_V : H_t\otimes V \to V$ by
$$
l_V( 1\1\cdot z \otimes 1\2\cdot v) = z\cdot v, \qquad z\in H_t,\, v\in V.
$$
It is an invertible $H$-linear map  with the inverse 
$l_V^{-1}(v) = S(1\1) \otimes 1\2 \cdot v$. Moreover, the collection
$\{l_V\}_V$ gives a natural equivalence between the functor $H_t\otimes (\ )$
and the identity functor. 
Similarly, the right unit homomorphism
$r_V : V\otimes H_t \to V$ defined by
$$
r_V( 1\1\cdot v \otimes 1\2\cdot z) = S(z)\cdot v, \qquad z\in H_t,\, v\in V,
$$
has the inverse $r_V^{-1}(v) = 1\1 \cdot v \otimes 1\2$
and satisfies the necessary properties.
Finally, one can check the triangle axiom, i.e., that 
\begin{equation*}
(\id_V\otimes l_W) = (r_V\otimes id_W)
\end{equation*}
for all objects $V,W$ of $\Rep(H)$ and $v\in V,\,w\in W$ (\cite{NTV}, 4.1).
\end{proof}

Using the antipode $S$ of $H$, we can provide $\Rep(H)$ with a duality.
For any object $V$ of $\Rep(H)$ define the action of $H$ on $V^*=
\Hom_k(V,\,k)$ by $(h\cdot \phi)(v) = \phi(S(h)\cdot v)$, where $h\in H,
v\in V, \phi\in V^*$. For any morphism $f: V\to W$ let $f^* : W^*\to V^*$
be the morphism dual to $f$ (see \cite{T}, I.1.8).

For any $V$ in $\Rep(H)$ define the duality homomorphisms
\begin{equation*}
d_V : V^*\otimes V \to H_t, \qquad b_V: H_t \to V \otimes V^*
\end{equation*}
as follows. For $\sum_j\, \phi^j \otimes v_j\in V^* \otimes V$ set
\begin{equation}
d_V(\sum_j\, \phi^j \otimes v_j)= \sum_j\, \phi^j(1\1\cdot v_j)1\2.
\end{equation}
Let $\{g_i\}_i$ and $\{\gamma^i\}_i$ be bases of $V$ and $V^*$ respectively,
dual to each other. The element $\sum_i\,g_i\otimes \gamma^i$ does not
depend on choice of these bases; moreover, for all $v\in V, \phi\in V^*$
one has $\phi = \sum_i\,\phi(g_i)\gamma^i$ and $v =\sum_i\,g_i\gamma^i(v)$.
Set
\begin{equation}
b_V(z) = z\cdot \sum_i\, g_i \otimes \gamma^i.
\end{equation}
 
\begin{proposition}
\label{monoidal with duality}
The category $\Rep(H)$ is a monoidal category with duality.
\end{proposition}

\begin{proof}
We know already that $\Rep(H)$ is monoidal.
One can check (\cite{NTV}, 4.2) that $d_V$ and $b_V$ are $H$-linear.
To show that they satisfy the identities
$$
(\id_V\otimes d_V)(b_V \otimes \id_V) = \id_V, \qquad
(d_V \otimes \id_{V^*})(\id_{V^*}\otimes b_V) = \id_{V^*},
$$ 
take $\sum_j\, \phi^j \otimes v_j\in V^*\otimes V, z\in H_t$.
Using the isomorphisms $l_V$ and $r_V$ identifying $H_t\otimes V$,
$V\otimes H_t$ and $V$, for all $v\in V$ and $\phi\in V^*$ we have:
\begin{eqnarray*}
(\id_V\otimes d_V)(b_V \otimes \id_V)(v)
&=& (\id_V\otimes d_V)(b_V(1\1\cdot 1)\otimes 1\2\cdot v) \\
&=& (\id_V\otimes d_V)(b_V(1\2)\otimes S^{-1}(1\1)\cdot v) \\
&=& \sum_i\,(\id_V\otimes d_V)
            (1\2\cdot g_i \otimes 1\3\cdot \gamma^i \otimes S^{-1}(1\1)\cdot v) \\
&=& \sum_i\,1\2\cdot g_i \otimes (1\3\cdot \gamma^i)(1\1'S^{-1}(1\1)\cdot v)1\2'\\
&=& 1\2 S(1\3) 1\1' S^{-1}(1\1)\cdot v \otimes 1\2' =v, \\
(d_V \otimes \id_{V^*})(\id_{V^*}\otimes b_V)(\phi)
&=& (d_V \otimes \id_{V^*})(1\1\cdot \phi \otimes b_V(1\2)) \\
&=& \sum_i\, (d_V \otimes \id_{V^*})
             (1\1\cdot\phi \otimes 1\2\cdot g_i \otimes 1\3\cdot \gamma^i) \\
&=& \sum_i\,(1\1\cdot\phi)(1\1'1\2\cdot g_i)1\2' \otimes 1\3\cdot \gamma^i\\
&=& 1\2' \otimes 1\3 1\1 S(1\1'1\2)\cdot \phi = \phi,
\end{eqnarray*}
which completes the proof.
\end{proof}
