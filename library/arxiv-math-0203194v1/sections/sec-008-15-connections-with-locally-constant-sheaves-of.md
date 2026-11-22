---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-008-15-connections-with-locally-constant-sheaves-of
section_title: "Connections with locally constant sheaves of solutions."
section_number: 1.5
pages: 21-25
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.977
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-connection}
\begin{para}
 Let us briefly recall the complex situation. Let $S$ be a complex
 connected manifold, $(\mathcal{M},\nabla)$ a vector bundle of rank $r$
 with integrable connection on $S$. The classical Cauchy theorem shows
 that for any $s \in S$, the solution space
 $(\mathcal{M}\otimes\mathcal{O}_{S,s})^{\nabla}$ at $s$ has dimension
 $r$. Analytic continuation along paths gives rise to a homomorphism
 $\pi_1^{\mathrm{top}}(S,{s}) \rightarrow
 \Aut_{\C}((\mathcal{M}\otimes\mathcal{O}_{S,s})^{\nabla})$ (the
 \emph{monodromy}). The sheaf of germs of solutions
 $\mathcal{M}^{\nabla}$ is locally constant on $S$: its pull-back over
 the universal covering $\til{S}$ of $S$ is constant. Conversely, any
 complex representation $V$ of $\pi_1^{\mathrm{top}}(S,{s})$ of dimension $r$
 gives rise naturally to a vector bundle $\mathcal{M}$ of rank $r$ with
 integrable connection $\nabla$:  $\mathcal{M}= (V \times
 \til{S})/\pi_1^{\mathrm{top}}(S,{s}), \; \nabla(V) = 0$.  This sets up an
 equivalence of categories:
 \begin{equation*}
  \left\{
  \begin{matrix}
   \text{finite dimensional}\\
   \text{representations of $\pi_1^{\mathrm{top}}(S,{s})$}
  \end{matrix}
  \right\}
  \simeq
  \left\{
  \begin{matrix}
   \text{$S$-vector bundles with}\\
   \text{integrable connection}
  \end{matrix}
  \right\}.
 \end{equation*}
\end{para}  
\begin{para}
 Let $(S,s)$ be now a pointed connected $p$-adic manifold. It is still
 true that any $\C_p$-linear representation $V$ of
 $\pi_1^{\mathrm{top}}(S,s)$ of dimension $r$ gives rise to a vector
 bundle $\mathcal{M}=\mathcal{M}_V$ a vector bundle of rank $r$ with
 integrable connection $\nabla =\nabla_V$ (same formula).
 The functor
 \begin{equation*}
  \left\{
  \begin{matrix}
   \text{finite dimensional}\\
   \text{representations of $\pi_1^{\mathrm{top}}(S,s)$}
  \end{matrix}
  \right\}
  \rightarrow
  \left\{
  \begin{matrix}
   \text{$S$-vector bundles with}\\
   \text{integrable connection}
  \end{matrix}
  \right\}
 \end{equation*}
 is still fully faithful, but \emph{no longer surjective}; its essential
 image consists of those connections whose sheaf of solutions is locally
 constant, \ie  becomes constant over $\til{S}$.  In fact, the
 classical ``\emph{Cauchy theorem}'' according to which the solution
 space $(\mathcal{M}\otimes\mathcal{O}_{S,s})^{\nabla}$ at $s$ has
 dimension $r$ holds for every classical point $s$ of $S$ --- which
 corresponds to a point of the associated rigid variety ---, but
 \emph{does not hold} for non-classical points $s$ of the Berkovich
 space $S$ in general.
\end{para}

\begin{para}\label{para-cauchy} 
 Any non-trivial connection over the projective line minus a few points
 gives an example when the $p$-adic analogue of the ``Cauchy theorem''
 does not hold: indeed, in this case, the topological fundamental group
 is trivial.  

 However, a $p$-adic variant of Cauchy's theorem in the neighborhood of a
 non-classical point $s$ may be restored as follows (Dwork's technique of
 generic points): it suffices to extend the scalars from $\C_p$
 to a complete algebraically closed extension of $\mathscr{H}(s)$.  This
 transforms $s$ into a classical point, and neighborhoods of $s$ after
 scalar extensions are ``smaller'' than before.
\end{para}

\begin{para}\label{para-cauchy-monodromy} 
 When ``Cauchy's theorem'' holds at every point of $S$, one can continue
 the local solutions along paths and get the monodromy representation
 just as in the complex situation. 

 This nice category of $p$-adic connections has not yet
 attracted much attention.
\end{para}

\begin{exa}\label{exa-tate-ell-curve}
 Let us consider the case when $S$ is a Tate elliptic curve:
 $S=\C_p^{\times}/q^{\Z}$, with $s =$ its origin. Then
 $\pi_1^{\mathrm{top}}(S,s)=q^{\Z}$, and the connections on $S$ which arise
 from representations of $q^{\Z}$ are those which become trivial over
 $\til{S}=\C_p^{\times}$.
 In this correspondence, the multivalued solutions $\vec y$ (\ie 
 horizontal sections) of such a connection are the solutions of the
 associated linear $q$-difference equation $\vec y(qt)=M(q) \vec y(t)$,
 where $t$ is the standard coordinate on $\C_p^{\times}$ and the
 matrix $M(q)$ is the image of $q$ in the monodromy representation.

 The simplest example is given by the obvious one-dimensional 
 representation $M(q)=q$. It corresponds to
 $\mathcal{M}=\mathcal{O}_S,\;\nabla(1)=\omega_{\mathrm{can}}$ (the canonical
 differential on $S$ induced by $dt/t$); here the $q$-difference
 equation is $t.dy=y.dt$ with obvious solution $y=t$. 

 Let us now look at the representation $M(q)=\sqrt{q}$.  The associated
 $q$-difference equation is $t.dy=\frac{1}{2}y.dt$. There is the 
 obvious solution $\sqrt t$, which leads to
 $\mathcal{M}=\mathcal{O}_S,\;\nabla(1)=\frac{1}{2}\omega_{\mathrm{can}}$. 
 Here we encounter an interesting paradox: $\sqrt{t}$ is not a multivalued
 analytic function on $S$ (\ie it is not an analytic function on the
 universal covering $\C_p^{\times}\;$.  In the complex situation, a
 similar paradox arose in the work of G. Birkhoff in his theory of
 $q$-difference equations, which was pointed out
 and analyzed by M.~van der Put and M.~Singer in the last chapter of
 their book \cite{gtode}.  The solution of the paradox is that the vector
 bundle $\mathcal{M}$ associated to the representation $q \rightarrow
 \sqrt{q}$ of $q^{\Z}$ (or to the $q$-difference equation
 $y(qt)=\sqrt{q}.t$) is in fact a non-trivial vector bundle of rank one,
 and the basic solution is not $\sqrt{t}$, but
 $\frac{\theta(t/\sqrt{q})}{\theta(t)}$, where
 $\theta(t)=\prod_{n>0}(1-q^nt)\prod_{n\leq 0}(1-q^n/t)$.

\end{exa}

\begin{para}\label{para-Simpson} 
 In the previous example, it is easily seen that rank-one vector bundles
 with connection on $S$ which arise from a representation of
 $\pi_1^{\mathrm{top}}(S,s)$ form a space of dimension one, while the
 space of all rank-one vector bundles with connection on $S$ has
 dimension two. 

 We next consider the case of a $p$-adic manifold $S$ which ``is'' a
 geometrically irreducible algebraic ${\C}_p$-curve. Let $\ovl{S}$ be
 its projective completion. It follows from the Van Kampen theorem,
 together with the fact that punctured disks are simply-connected, that
 $\pi_1^{\mathrm{top}}(S,s) \to \pi_1^{\mathrm{top}}(\ovl{S},s)$ is
 an isomorphism. It 
 follows that the vector bundles with connection attached to
 representations of $\pi_1^{\mathrm{top}}(S,s)$ automatically extend
 to $\ovl{S}$. Hence we may assume without loss of generality that $S$ is
 compact.

 Vector bundles with connection on $S$ are algebrizable, and one can
 use C.~Simpson's construction (\cite{morotfgoaspv1}) to define the {\it
 moduli space of connections} of rank $r$ over $S$, denoted by
 $M_{\mathrm{dR}}(S,r)$. On the other hand, we have seen that the topological
 fundamental group $\pi_1^{\mathrm{top}}(S,s)$ is free on $b_1(\Delta)$
generators, being isomorphic to the fundamental group of the dual graph
$\Delta$ of the semistable reduction of $S$. Simpson has also studied
the {\it moduli space of representations of dimension $r$} of such a
group. We denote it by $M_{\mathrm{B}}(S,r)$; in fact, it depends only on the
couple of integers $(b_1(\Delta),r)$.

 Let us assume that $S$ is of genus $g\geq 2$. Simpson shows that 
 $M_{\mathrm{dR}}(S,r)$ is algebraic irreducible of dimension
 $2(r^2(g-1)+1)$.   On the other hand, $M_{\mathrm{B}}(S,r)$ is an algebraic
 irreducible affine variety of dimension $(r^2(b_1(\Delta)-1)+1)$.  We
 note that this dimension is maximal when the Betti number $b_1(\Delta
 )$ takes its maximal value, namely $g$. This corresponds to the case 
 where $S$ is a Mumford curve (a curve with totally degenerate reduction).  

 It turns out that the functor which associates a vector
 bundle with connection to any finite-dimensional representation of the
 topological fundamental group induces an {\rm injective analytic map}
 of moduli spaces $\iota : M_{\mathrm{B}}(S,r)\to M_{\mathrm{dR}}(S,r)$.

[The map is induced by the functor $V \to (\mathcal{M}_V,{\nabla}_V)$,
and its injectivity follows from the faithfulness of this functor. The
difficulty in showing that $\iota$ is analytic is that
$M_{\mathrm{dR}}(S,r)$ is 
a priori a moduli space for algebraic connections, not for all analytic
connections; we shall not pursue here in this direction].

In the complex situation, the corresponding map $\iota$ would always be
an analytic isomorphism (Riemann-Hilbert-Simpson). In the $p$-adic
cases, we see that the connections which satisfy Cauchy's theorem at
every point (classical or not) form a stratum of maximal dimension half
of the dimension of the total moduli space.
\end{para}


\vspace{10pt}\par
We shall leave the closer analysis of this kind of $p$-adic 
differential equations with global monodromy until later chapters, where
we show how they arise in the context of period mappings. In the next 
section, we shall deal with a very different kind of differential 
equations, which play a distinguished role in $p$-adic analysis under 
the name of {\it unit-root F-crystals}.



\newpage
