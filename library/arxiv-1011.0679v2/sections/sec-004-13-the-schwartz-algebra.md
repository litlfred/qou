---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-004-13-the-schwartz-algebra
section_title: "The Schwartz algebra"
section_number: 1.3
pages: 9-11
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.957
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
We recall how to complete an affine Hecke algebra to a topological algebra called the
Schwartz algebra. As a vector space $\mc S$ will consist of rapidly decreasing functions
on $W^e$, with respect to some length function. For this purpose it is unsatisfactory
that $\ell$ is 0 on the subgroup $Z(W^e)$, as this can be a large part
of $W$. To overcome this inconvenience, let
$L : X \otimes \mh R \to [0,\infty )$ be a function such that
\begin{itemize}
\item $L (X) \subset \mh Z$,
\item $L(x+y) = L(x) \quad \forall x \in X \otimes \mh R, y \in E$,
\item $L$ induces a norm on
$X \otimes \mh R / E \cong Z(W) \otimes \mh R$.
\end{itemize}
Now we define
\[
\mc N (w) := \ell (w) + L (w(0))  \qquad w \in W^e .
\]
Since $Z(W^e) \oplus \mh Z R_0$ is of finite index in $X$, the set
$\{ w \in W^e : \mc N (w) = 0 \}$ is finite. Moreover, because $W^e$ is
the semidirect product of a finite group and an abelian group, it is of
polynomial growth and different choices of $L$ lead to equivalent length
functions $\mc N$. For $n \in \mh N$ we define the norm
\[
p_n \big( {\ts \sum_{w \in W}} h_w N_w \big) :=
\sup_{w \in W} |h_w | (\mc N (w) + 1 )^n .
\]
The completion $\mc S = \mc S (\mc R ,q)$ of $\mc H (\mc R ,q)$ with respect to the family
of norms $\{ p_n \}_{n \in \mh N}$ is a nuclear Fr\'echet space. It consists of all possible
infinite sums $h = \sum_{w \in W} h_w N_w$ such that $p_n (h) < \infty \; \forall n \in \mh N$.
By \cite[Section 6.2]{Opd-Sp} or \cite[Appendix A]{OpSo2} $\mc S (\mc R,q)$ is a unital
locally convex *-algebra.

A crucial role in the harmonic analysis on affine Hecke algebra is played by a particular
Fourier transform, which is based on the induction data space $\Xi$. Let $\mc V_\Xi$
be the vector bundle over $\Xi$, whose fiber at $(P,\delta,t) \in \Xi$ is the representation
space $\C [W^P] \otimes V_\delta$ of $\pi (P,\delta,t)$. Let $\mr{End} (\mc V_\Xi)$ be the
algebra bundle with fibers $\mr{End}_\C (\C [W^P] \otimes V_\delta)$. Of course these
vector bundles are trivial on every connected component of $\Xi$, but globally not even the
dimensions need be constant. Since $\Xi$ has the structure of a complex algebraic variety,
we can construct the algebra of polynomial sections of $\mr{End} (\mc V_\Xi)$:
\[
\mc O \big( \Xi ; \mr{End} (\mc V_\Xi) \big) := \bigoplus_{P,\delta} \mc O (T^P) \otimes
\mr{End}_\C (\C [W^P] \otimes V_\delta) .
\]
For a submanifold $\Xi' \subset \Xi$ we define the algebra $C^\infty \big( \Xi' ;
\mr{End} (\mc V_\Xi) \big)$ in similar fashion.
The intertwining operators from Theorem \ref{thm:intOp} give rise to an action of the
groupoid $\mc W$ on the algebra of rational sections of $\mr{End} (\mc V_\Xi)$, by
\begin{equation}\label{eq:actSections}
(w \cdot f) (\xi) = \pi (w,w^{-1} \xi ) f (w^{-1} \xi) \pi (w, w^{-1} \xi )^{-1} ,
\end{equation}
whenever $w^{-1} \xi \in \Xi$ is defined. This formula also defines groupoid actions of
$\mc W$ on $C^\infty \big( \Xi' ; \mr{End} (\mc V_\Xi) \big)$, provided that $\Xi'$ is a
$\mc W$-stable submanifold of $\Xi$ on which all the intertwining operators are regular.
Given a suitable collection $\Sigma$ of sections of $(\Xi', \mr{End} (\mc V_\Xi) )$,
we write
\[
\Sigma^{\mc W} = \{ f \in \Sigma : (w \cdot f) (\xi) = f(\xi) \text{ for all } w \in \mc W,\
\xi \in \Xi' \text{ such that } w^{-1} \xi \text{ is defined} \} .
\]
The Fourier transform for $\mc H$ is the algebra homomorphism
\begin{align*}
& \mc F : \mc H \to \mc O \big( \Xi ; \mr{End} (\mc V_\Xi) \big) , \\
& \mc F (h) (\xi) = \pi (\xi) (h) .
\end{align*}
The very definition of intertwining operators shows that the image of $\mc F$ is contained
in the algebra $\mc O \big( \Xi ; \mr{End} (\mc V_\Xi) \big)^{\mc W}$.
By \cite[Theorem 5.3]{DeOp1} the Fourier transform extends to an isomorphism of
Fr\'echet *-algebras
\begin{equation}\label{eq:FourierIso}
\mc F : \mc S (\mc R,q) \to C^\infty \big( \Xi_{un} ; \mr{End} (\mc V_\Xi ) \big)^{\mc W} .
\end{equation}
Let $(P_1,\delta_1), \ldots, (P_N, \delta_N)$ be representatives for the action of $\mc W$ on
pairs $(P,\delta)$. Then the right hand side of \eqref{eq:FourierIso} can be rewritten as
\begin{equation}\label{eq:25}
\bigoplus\nolimits_{i=1}^N \big( C^\infty (T^P_{un}) \otimes
\mr{End} (\C [W^P] \otimes V_\delta) \big)^{\mc W_{P_i ,\delta_i}} ,
\end{equation}
where $\mc W_{P,\delta} = \{ w \in \mc W : w (P) = P, \delta \circ \psi_w^{-1} \cong \delta \}$
is the isotropy group of $(P,\delta)$.

\begin{rem}\label{rem:Plancherel}
Suppose that $L$ is a reductive $p$-adic group and that $K \subset L$ is a compact open
subgroup. Clearly \eqref{eq:FourierIso} is similar to the Plancherel isomorphism for the
Harish-Chandra--Schwartz algebra $\mc S (L)$ \cite{Wal}. One can easily deduce from \cite{Wal}
that the subalgebra $\mc S (L,K) \subset \mc S (L)$ of $K$-biinvariant functions has exactly the
same shape as \eqref{eq:25}, see \cite[Theorem 10]{Sol-Chern}.

Let $\mc H (L)$ be the Hecke algebra of $L$ and let Mod$(\mc H (L))$ be the category of smooth
$L$-representations. Consider the subalgebra $\mc H (L,K) = \mc S (L,K) \cap \mc H (L)$, for any
compact open subgroup $K \subset L$. According to \cite[Section 3]{BeDe} there exist arbitrarily
small $K$ such that Mod$(\mc H (L,K))$ is equivalent to the category consisting of those smooth
$L$-representations that are generated by their $K$-invariant vectors, and such that the latter
is a Serre subcategory of Mod$(\mc H (L))$. Moreover these subcategories exhaust Mod$(\mc H(L))$,
so all extensions of tempered smooth $L$-representations can be
described with representations of algebras $\mc S (L,K)$ of the form \eqref{eq:25}.
\end{rem}

It was shown in \cite[Corollary 5.5]{DeOp1} that \eqref{eq:FourierIso} implies
\begin{equation}
Z (\mc S) \cong C^\infty (\Xi_{un})^{\mc W},
\end{equation}
so the space of central characters of $\mc S$ is $\Xi_{un} / \mc W$.
We let $\mr{Mod}_f (\mc S)$ be the category of finite dimensional $\mc S$-modules
and $\mr{Mod}_{f,\mc W \xi} (\mc S)$ the full subcategory of modules which admit the
central character $\mc W \xi$. The collection $\mr{Irr}_{\mc W \xi} (\mc S)$ of
(equivalence classes of) irreducible objects in $\mr{Mod}_{f,\mc W \xi} (\mc S)$ equals
$\mr{Irr}_{\mc W \xi} (\mc H)$, in the notation of \eqref{eq:packetReps}.

For $\ep \in \mh R$ let $q^\ep$ be the parameter function $q^\ep (w) = q(w)^\ep$.
For every $\ep$ we have the affine Hecke algebra $\mc H (\mc R ,q^\ep )$ and its Schwartz
completion $\mc S (\mc R ,q^\ep )$. We note that $\mc H (\mc R ,q^0 ) = \mh C [W^e]$
is the group algebra of $W^e$ and that $\mc S (\mc R ,q^0 ) = \mc S (W^e)$ is the
Schwartz algebra of rapidly decreasing functions on $W^e$.

The intuitive idea is that these algebras depend continuously on $\ep$.
We will use this in the form of the following rather technical result.

\begin{thm}\label{thm:scalingReps}
\textup{\cite[Corollary 4.2.2]{Sol-Irr}} \\
For $\ep \in [-1,1]$ there exists a family of additive functors
\begin{align*}
& \tilde \sigma_\ep : \mr{Mod}_f (\mc H (\mc R ,q)) \to
\mr{Mod}_f (\mc H (\mc R ,q^\ep )) , \\
& \tilde \sigma_\ep (\pi ,V) = (\pi_\ep ,V) .
\end{align*}
with the properties
\begin{itemize}
\item[(1)] the map
\[
[-1,1] \to \mr{End}\, V : \ep \mapsto \pi_\ep (N_w)
\]
is analytic for any $w \in W^e$,
\item[(2)] $\tilde \sigma_\ep$ is a bijection if $\ep \neq 0$,
\item[(3)] $\tilde \sigma_\ep$ preserves unitarity,
\item[(4)] $\tilde \sigma_\ep$ preserves temperedness if $\ep \geq 0$,
\item[(5)] $\tilde \sigma_\ep$ preserves the discrete series if $\ep > 0$.
\end{itemize}
\end{thm}
