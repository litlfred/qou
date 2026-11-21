---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-007-7-l-morphisms-and-coalgebras
section_title: "L Morphisms and Coalgebras"
section_number: 7
pages: 24-26
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.948
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:L-infty}

We shall use the coalgebra approach to $\mrm{L}_{\infty}$ morphisms, following
\cite{Qu}, \cite[Section 4]{Ko2}, \cite{Hi2}, \cite[Section 3.7]{CKTB} and
\cite[Section 3]{Ye2}. 

Let us denote by $\cat{DGLie}(\K)$ the category of DG Lie algebras over $\K$,
and by $\cat{DGCog}(\K)$ the category of DG unital cocommutative coalgebras
over $\K$. Note that commutativity here is in the graded (or super) sense.
Recall that a unital coalgebra $C$ has a comultiplication 
$\Delta : C \to C \ot C$,
a counit $\ep : C \to \K$ and a unit $1 \in C$. The differential $\d$ has to be
a coderivation of degree $1$. The conditions on the unit are
$\Delta(1) = 1 \ot 1$, $\d(1) = 0$ and $\ep(1) = 1$ in $\K$. 
Morphisms in $\cat{DGCog}(\K)$ are $\K$-linear homomorphisms
$C \to D$ respecting
$\Delta$, $\ep$ and $1$. We write $C^+ := \opn{Ker}(\ep)$.

Let $V = \boplus_{i \in \Z} V^i$ be a graded $\K$-module. The 
symmetric algebra over $\K$ of the graded module $V$ is 
\[ \opn{Sym}(V) = \bigoplus_{i \in \N}\, \opn{Sym}^j(V) . \]
Note that we are in the super-commutative setting, so
$\opn{Sym}^j(V) = \bwedge^j(V[1])[-j]$.
We view $\opn{Sym}(V)$ as a Hopf algebra over $\K$, 
which is commutative and cocommutative. The unit is 
$1 \in \K = \opn{Sym}^0(V)$, and the counit is the projection
$\ep : \opn{Sym}(V) \to \K$.

The Hopf algebra $\opn{Sym}(V)$ is bigraded, with one grading coming from the
grading of $V$, which we call degree. The second grading is called order; by
definition the $j$-th order component of $\opn{Sym}(V)$ is $\opn{Sym}^j(V)$.
Let us write
\[ \opn{Sym}^+(V) := \bigoplus_{i \geq 1}\, \opn{Sym}^j(V) =
\opn{Ker}(\ep) . \]

The projection $\opn{Sym}(V) \to \opn{Sym}^1(V)$ is denoted by $\ln$.
So for an element $c \in \opn{Sym}(V)$, its first order term is $\ln(c)$.
Recall that giving a homomorphism of unital graded coalgebras
$\Psi : \opn{Sym}(V) \to \opn{Sym}(W)$ 
is the same as giving its sequence of Taylor coefficients 
$\{ \pa^j\Psi \}_{j \geq 1}$,
where the $j$-th Taylor coefficient of $\Psi$ is the $\K$-linear function 
\[ \partial^j \Psi := (\ln \circ \Psi)|_{\opn{Sym}^j(V)} : 
\opn{Sym}^j(V) \to W  \]
of degree $0$.

The free graded Lie algebra over the graded $\K$-module $V$ is denoted by \lb
$\opn{FrLie}(V)$. 

There is a functor 
\[ \opn{C} : \cat{DGLie}(\K) \to \cat{DGCog}(\K) \]
called the {\em bar construction}. Given a DG Lie algebra $\g$, the
corresponding DG coalgebra is 
$\opn{C}(\g) := \opn{Sym}(\g[1])$, with a coderivation that encodes both the
differential of $\g$ and its Lie bracket. 
There is another functor 
\[ \opn{L} : \cat{DGCog}(\K) \to \cat{DGLie}(\K)   \]
called the {\em cobar construction}. Given a DG coalgebra $C$, the
corresponding DG Lie algebra is $\opn{FrLie}(C^+[-1])$, with a derivation that
encodes both the differential of $C$ and its comultiplication. 
If $\g \in \cat{DGLie}(\K)$ and $C \in \cat{DGCog}(\K)$, then the set of graded
$\K$-linear homomorphisms $\opn{Hom}^{\mrm{gr}}(C, \g)$ 
is a DG Lie algebra, and there are functorial bijections
\begin{equation} \label{eqn:60}
\opn{Hom}_{\cat{DGLie}(\K)}(\opn{L}(C), \g) \cong
\opn{Hom}_{\cat{DGCog}(\K)}(C, \opn{C}(\g)) \cong
\opn{MC}(\opn{Hom}^{\mrm{gr}}(C, \g)) . 
\end{equation}
Thus the functors $\opn{C}$ and $\opn{L}$ are adjoint.
We denote the adjunction morphisms by
\[ \zeta_{\g} : (\opn{L} \circ \opn{C})(\g) \to \g \]
and 
\[ \th_C : C \to (\opn{C} \circ \opn{L})(C) .  \]

It is known that the functor $\opn{C}$ is faithful. 
Let $\g$ and $\h$ be DG Lie algebras.
By definition, an {\em $\mrm{L}_{\infty}$ morphism} $\Phi : \g \to \h$ 
is a morphism $\opn{C}(\g) \to \opn{C}(\h)$ in $\cat{DGCog}(\K)$.
Let us define $\cat{DGLie}_{\infty}(\K)$ to be the category whose objects are
the DG Lie algebras, and the morphisms are the  $\mrm{L}_{\infty}$ morphisms
between them. Composition of  $\mrm{L}_{\infty}$ morphisms is that of
$\cat{DGCog}(\K)$. Thus we get a full and faithful functor
\[ \opn{C}_{\infty} : \cat{DGLie}_{\infty}(\K) \to \cat{DGCog}(\K) \]
whose restriction to $\cat{DGLie}(\K)$ is $\opn{C}$.

Take an $\mrm{L}_{\infty}$ morphism 
$\Phi : \g \to \h$. Its $i$-th Taylor coefficient
$\pa^i \Phi := \pa^i (\opn{C}_{\infty}(\Phi))$ is a $\K$-linear function 
\[ \pa^i \Phi : \bwedge^i \g \to \h \]
of degree $1 - i$. Writing $\phi_i := \pa^i \Phi$, the sequence of 
functions $\{ \phi_i \}_{i \geq 1}$ satisfies these equations:
\[ \begin{aligned}
& \mrm{d} \bigl( \phi_i(\gamma_1 \wedge \cdots 
\wedge \gamma_i) \bigr) - \sum_{k = 1}^i \pm 
\phi_i \bigl( \gamma_1 \wedge \cdots \wedge 
\mrm{d}(\gamma_k) \wedge \cdots \wedge \gamma_i \bigr) = \\
& \quad {\smfrac{1}{2}} \sum_{\substack{k, l \geq 1 \\ k + l = i}}
{\smfrac{1}{k! \, l!}} \sum_{\sigma \in \mfrak{S}_i} \pm
\bigl[ \phi_k (\gamma_{\sigma(1)} \wedge \cdots \wedge 
\gamma_{\sigma(k)}),
\phi_l (\gamma_{\sigma(k + 1)} \wedge \cdots \wedge 
\gamma_{\sigma(i)}) \bigr] \\
& \qquad +
\sum_{k < l} \pm
\phi_{i-1} \bigl( [\gamma_k, \gamma_l] \wedge
\gamma_{1} \wedge \cdots \gamma_k \hspace{-1em} \diagup \cdots
\gamma_l \hspace{-1em} \diagup 
\cdots \wedge \gamma_{i} \bigr) .
\end{aligned} \]
Here $\gamma_k \in \mfrak{g}$ are homogeneous elements,
$\mfrak{S}_i$ is the permutation group of $\{ 1, \ldots, i \}$,
and the signs depend only on the indices, the permutations and the 
degrees of the elements $\gamma_k$. The
signs are written explicitly in \cite[Section 3.6]{CKTB}. 
Conversely, any sequence $\{ \phi_i \}_{i \geq 1}$ of homomorphisms satisfying
these equations determines an $\mrm{L}_{\infty}$ morphism.

Let $\Phi : \g \to \h$ be  an $\mrm{L}_{\infty}$ morphism.
The first Taylor coefficient  $\pa^1 \Phi : \g \to \h$ is a homomorphism of
complexes of $\K$-modules (forgetting the Lie brackets). 
If $\pa^i \Phi = 0$ for all $i \geq 2$, then 
$\pa^1 \Phi$ is a DG Lie algebra homomorphism. 
If $\pa^1 \Phi$ is a quasi-isomorphism, then $\Phi$ is called an 
{\em $\mrm{L}_{\infty}$ quasi-isomorphism}.

\begin{lem} \label{lem:20}
Let $\g \in \cat{DGLie}(\K)$, and define
$C := \opn{C}(\g)$, $\til{\g} := \opn{L}(C)$ and $\til{C} := \opn{C}(\til{g})$.
Consider the coalgebra homomorphisms 
$\th_C : C \to \til{C}$ and $\opn{C}(\zeta_{\g}) : \til{C} \to C$. 
Then 
\[ \opn{C}(\zeta_{\g}) \circ \th_C = \bsym{1}_C , \]
the identity automorphism of $C$.
\end{lem}

\begin{proof}
This is true for any pair of adjoint functors; see 
\cite[Section IV.1 Theorem 1]{Ma}.
\end{proof}

\begin{lem} \label{lem:21}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ quasi-isomorphism. Then 
\[ (\opn{L} \circ \opn{C}_{\infty})(\Phi) : 
(\opn{L} \circ \opn{C})(\g) \to (\opn{L} \circ \opn{C})(\h) \]
is a DG Lie algebra quasi-isomorphism.
\end{lem}

\begin{proof}
Let us write
$C := \opn{C}(\g)$, $D := \opn{C}(\h)$ and $\Psi := \opn{C}_{\infty}(\Phi)$. 
Put on $C$ the ascending filtration 
$F_j C := \boplus_{k = 0}^j \opn{Sym}^k(\g[1])$; 
so that $\{ F_j C \}_{j \geq 0}$ is an admissible coalgebra filtration, in the
sense of \cite[Definition 4.4.1]{Hi2}. Likewise there is an 
admissible coalgebra filtration $\{ F_j D \}_{j \geq 0}$ on $D$.
According to step 2 of the proof of \cite[Proposition 4.4.3]{Hi2}, the
coalgebra homomorphism $\Psi$ is a filtered quasi-isomorphism. 
Hence by \cite[Proposition 4.4.4]{Hi2} the DG Lie algebra homomorphism 
$(\opn{L} \circ \opn{C}_{\infty})(\Phi) = \opn{L}(\Psi)$
is a quasi-isomorphism.
\end{proof}
