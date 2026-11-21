---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-001-1-preliminaries-on-homological-algebra
section_title: "Preliminaries on Homological Algebra"
section_number: 1
pages: 4-7
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
toc_source: outline
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.943
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
\label{sec:prelim}

This paper relies on delicate work with derived functors. Therefore we begin
with a review of some facts on homological algebra. There are also a few
new results. By default all rings considered in the paper are commutative. 

Let $\cat{M}$ be an abelian category. 
As in \cite{RD} we denote by $\cat{C}(\cat{M})$ the category of complexes of
objects of $\cat{M}$, by $\cat{K}(\cat{M})$ its homotopy category, 
and by $\cat{D}(\cat{M})$ the derived category.
There are full subcategories  $\cat{D}^-(\cat{M})$, $\cat{D}^+(\cat{M})$ and 
$\cat{D}^{\mrm{b}}(\cat{M})$ of $\cat{D}(\cat{M})$, whose objects are
the bounded above, bounded below and bounded complexes respectively.

Our notation for distinguished triangles in $\cat{K}(\cat{M})$ or 
$\cat{D}(\cat{M})$ is either 
$L \xar{\alpha} M \xar{\beta} N \xar{\gamma} L[1]$,
or simply $L \to M \to N \distri$ 
if the names of the morphisms are not important.

A complex $P \in \cat{C}(\cat{M})$ is called {\em K-projective} if 
for any acyclic complex $N \in \cat{C}(\cat{M})$ the complex 
$\opn{Hom}_{\cat{M}}(P, N)$ is also acyclic. 
A complex $I \in \cat{C}(\cat{M})$ is called {\em K-injective} if 
for any acyclic complex $N \in \cat{C}(\cat{M})$ the complex 
$\opn{Hom}_{\cat{M}}(N, I)$ is also acyclic. 
These definitions were introduced in \cite{Sp}; in \cite[Section 3]{Ke} it is
shown that ``K-projective'' is the same as ``having property (P)'', and
``K-injective'' is the same as ``having property (I)''.

A K-projective resolution of 
$M \in \cat{C}(\cat{M})$ is a quasi-isomorphism $P \to M$ in 
$\cat{C}(\cat{M})$ with $P$ a K-projective complex. If every 
$M \in \cat{C}(\cat{M})$ admits some K-projective resolution, then we say that 
$\cat{C}(\cat{M})$ has enough K-projectives. 
Similarly for K-injectives.

Now we specialize to the case $\cat{M} := \cat{Mod} A$,
where $A$ is a ring. 
A complex $P \in \cat{C}(\cat{Mod} A)$ is called {\em K-flat} if 
for any acyclic complex $N \in \cat{C}(\cat{Mod} A)$ the complex 
$N \otimes_A P$ is also acyclic. Note that a K-projective
complex $P$ is K-flat. 

Here is a useful existence result.

\begin{prop} \label{prop:28}
Let $A$ be a ring, and let $M \in \cat{C}(\cat{Mod} A)$.
\begin{enumerate}
\item The complex $M$ admits a
quasi-isomorphism $P \to M$, where $P$ is a K-projective complex, and moreover
each component $P^i$ is a free $A$-module.

\item The complex $M$ admits a
quasi-isomorphism $P \to M$, where $P$ is a K-flat complex, and moreover
each component $P^i$ is a flat $A$-module.

\item The complex $M$ admits a quasi-isomorphism
$M \to I$, where $I$ is a K-injective complex, and moreover each component
$I^i$ is an injective \lb $A$-module. 
\end{enumerate}
\end{prop}

\begin{proof}
(1) This is proved in \cite[Subsection 3.1]{Ke}, when discussing the existence
of P-resolutions. Cf.\ \cite[Corollary 3.5]{Sp}.

\medskip \noindent
(2) This follows from (1), since any K-projective complex is also K-flat.

\medskip \noindent
(3) See \cite[Subsection 3.2]{Ke}. Cf.\ \cite[Proposition 3.11]{Sp}.
\end{proof}

In particular, the proposition says that $\cat{C}(\cat{Mod} A)$ has enough 
K-projectives, K-flats and K-injectives.

\begin{rem}
Let $(X, \mcal{A})$ be a ringed space, and let 
$\cat{Mod} \mcal{A}$ be the
category of sheaves of $\mcal{A}$-modules. 
It is known that $\cat{C}(\cat{Mod} \mcal{A})$ has enough K-injectives and
enough K-flats; but their structure is more complicated than in the case of \lb 
$\cat{C}(\cat{Mod} A)$, and Proposition \ref{prop:28} might not hold.
\end{rem}

Here are a few facts about K-projective and K-injective resolutions,
compiled from \cite{Sp, BN, Ke}. The first are: a bounded above complex of
projectives is K-projective, a bounded above complex of
flats is K-flat, and a bounded below complex of injectives is
K-injective.

Once again $\cat{M}$ is an abelian category. 
Let $\cat{E}$ be some triangulated category, and let 
$F : \cat{K}(\cat{M}) \to \cat{E}$ be a triangulated functor.
If $\cat{C}(\cat{M})$ has enough K-projectives, then the
left derived functor 
$(\mrm{L} F, \xi) : \cat{D}(\cat{M}) \to \cat{E}$ exists, and it is calculated
by K-projective resolutions. Likewise, if 
$\cat{K}(\cat{M})$ has enough K-injectives, then the right derived
functor $(\mrm{R} F, \xi) : \cat{D}(\cat{M}) \to \cat{E}$ exists,
and it is calculated by K-injective resolutions.

Let $M = \{ M^i \}_{i \in \Z}$ be a graded object of $\cat{M}$.
We define 
\begin{equation} \label{eqn:285}
\inf (M) := \opn{inf}\, \{ i \mid M^i \neq 0 \} \in \Z \cup \{ \pm \infty\}
\end{equation}
and 
\begin{equation} \label{eqn:286}
\sup (M) := \opn{sup}\, \{ i \mid  M^i \neq 0 \} \in \Z \cup \{ \pm \infty\} .
\end{equation}
The amplitude of $M$ is
\begin{equation} \label{eqn:287}
\opn{amp} (M) := \sup (M) - \inf (M) \in \N \cup \{ \pm \infty\} .
\end{equation}
(For $M = 0$ this reads $\inf (M) = \infty$, $\sup (M) = -\infty$ 
and $\opn{amp} (M) = -\infty$.)
Thus $M$ is bounded iff $\opn{amp} (M) < \infty$. 

For $M \in \cat{D}(\cat{M})$ we write
$\mrm{H} (M) := \{ \mrm{H}^i (M) \}_{i \in \Z}$.

\begin{dfn}
Let $\cat{M}$ and $\cat{M}'$ be abelian categories, and let
$F : \cat{D}(\cat{M}) \to \cat{D}(\cat{M}')$ be a triangulated functor.
Let $\cat{E} \subset \cat{D}(\cat{M})$ be a full additive subcategory (not
necessarily triangulated), and consider the restricted functor 
$F|_{\cat{E}} : \cat{E} \to \cat{D}(\cat{M}')$.
\begin{enumerate}
\item We say that $F|_{\cat{E}}$ has {\em finite cohomological dimension} if 
there exist some $n \in \N$ and $s \in \Z$ such that 
for every complex $M \in \cat{E}$ one has
\[ \opn{sup} \bigl( \mrm{H} (F (M)) \bigr) \leq 
\opn{sup} \bigl( \mrm{H} (M) \bigr)  + s \]
and
\[ \opn{inf} \bigl( \mrm{H} (F (M)) \bigr) \geq 
\opn{inf} \bigl( \mrm{H} (M) \bigr) + s - n .
\]
The smallest such number $n$ is called the {\em cohomological dimension} of 
$F|_{\cat{E}}$. 

\item If no such $n$ and $s$ exist then we say $F|_{\cat{E}}$ has {\em
infinite cohomological dimension}. 
\end{enumerate}
\end{dfn}

The number $s$ appearing in the definition represents the shift. (An easy
calculation shows that if $F|_{\cat{E}}$ is nonzero and has finite cohomological
dimension $n$, then the shift $s$ in the definition is unique.) 

If the functor $F$ has finite cohomological dimension, then it is a {\em
way-out functor in both directions}, in the sense of \cite[Section I.7]{RD}.
We will use this fact several times. 

\begin{exa}
Take a nonzero ring $A$, and let 
$P := A[1] \oplus A[2]$, a complex with zero differential concentrated in
degrees $-1$ and $-2$. The functor $F := P \otimes_A -$ 
has cohomological dimension $n = 1$, 
with shift $s = -1$.
\end{exa}

\begin{prop} \label{prop:21}
Let $\cat{M}$, $\cat{M}'$ and $\cat{M}''$ be abelian categories, and let
$F : \cat{D}(\cat{M}) \to \cat{D}(\cat{M}')$ and 
$F' : \cat{D}(\cat{M}') \to \cat{D}(\cat{M}'')$
be triangulated functors. Assume the cohomological dimensions of 
$F$ and $F'$ are $n$ and $n'$ respectively. Then the cohomological dimension
of $F' \circ F$ is at most $n + n'$.
\end{prop}

We leave out the easy proof. 

Here is a useful criterion for quasi-isomorphisms
(a variant of the way-out argument).
For $i, j \in \Z$ let 
$\cat{C}^{[i, j]}(\cat{M})$ be the full subcategory of 
$\cat{C}(\cat{M})$ whose objects are the complexes concentrated in the degree
range $[i, j] := \{ i, i+1, \ldots, j \}$.

\begin{prop} \label{prop:1.1}
Let $\cat{M}$ and $\cat{M}'$ be abelian categories, let
$F, G : \cat{M} \to \cat{C}(\cat{M}')$
be additive functors, and let $\eta : F \to G$ be a natural transformation. 
Assume $\cat{M}'$ has countable direct sums, and consider the extensions 
$F, G : \cat{C}(\cat{M}) \to \cat{C}(\cat{M}')$
by the direct sum totalization. Suppose $M \in \cat{C}(\cat{M})$ satisfies these
two conditions\tup{:}
\begin{enumerate}
\rmitem{i} There are $j_0, j_1 \in \Z$ such that 
$F(M^i), G(M^i) \in \cat{C}^{[j_0, j_1]}(\cat{M}')$
for every $i \in \Z$. 

\rmitem{ii} The homomorphism $\eta_{M^i} : F(M^i) \to G(M^i)$
is a quasi-isomorphism for every $i \in \Z$.
\end{enumerate}
Then $\eta_{M} : F(M) \to G(M)$ is a quasi-isomorphism.
\end{prop}

\begin{proof}
Step 1. Assume that $M$ is bounded. We prove that $\eta_{M}$ is a
quasi-iso\-morphism by induction on $\opn{amp}(M)$.
If $\opn{amp}(M) = 0$ then this is given. 
The inductive step is done using the stupid truncation functors 
\begin{equation}
\opn{stt}^{> i}(M), \opn{stt}^{\leq i}(M) : 
\cat{C}(\cat{M}) \to \cat{C}(\cat{M}) ,
\end{equation}
and the related short exact
sequences. See \cite[pages 69-70]{RD}, where the truncations
$\opn{stt}^{> i}(M)$ and $\opn{stt}^{\leq i}(M)$
 are denoted by 
$\tau_{> i}(M)$ and $\tau_{\leq i}(M)$ respectively.

\medskip \noindent
Step 2. Now $M$ is arbitrary. We have to prove that 
$\mrm{H}^i(\eta_{M}) : \mrm{H}^i (F(M)) \to \mrm{H}^i (G(M))$
is an isomorphism for every $i \in \Z$. 
For any $i \leq j$ there is the double truncation functor
$\opn{stt}^{[i, j]} := \opn{stt}^{\leq j} \circ \opn{stt}^{> i}$.
So let us fix $i$. 
The homomorphism $\mrm{H}^i(\eta_{M})$ in $\cat{M}'$ only depends on the
homomorphism of complexes
\[ \opn{stt}^{[i-1, i+1]}(\eta_{M}) :
\opn{stt}^{[i-1, i+1]} (F(M)) \to \opn{stt}^{[i-1, i+1]} (G(M)) . \]
Therefore we can replace $\eta_{M}$ with 
$\eta_{M'} : F(M') \to G(M')$,
where
\[ M' := \opn{stt}^{[j_0 + i - 1, j_1 + i +1]} (M) . \]
But $M'$ is bounded, so by part (1) the homomorphism $\eta_{M'}$ is a
quasi-isomorphism.  
\end{proof}

To end this section, here is a basic result we need, that we could not locate in
the
literature (but that was used implicitly in \cite{Sc}). 

\begin{prop} \label{prop:290}
Let $\cat{M}$ and
$\cat{N}$ be abelian categories, let 
$F : \cat{M} \to \cat{N}$ be an exact additive covariant functor, and let 
$G : \cat{M} \to \cat{N}$ be an exact additive contravariant functor. Then 
for any $M \in \cat{C}(\cat{M})$
there are isomorphisms 
$\mrm{H}^k(F(M)) \cong F(\mrm{H}^k(M))$ and 
$\mrm{H}^{-k}(G(M)) \cong G(\mrm{H}^k(M))$ in $\cat{N}$. Moreover, these
isomorphisms are functorial in $M$, $F$ and $G$. 
\end{prop}

\begin{proof}
These are very degenerate cases of Grothendieck spectral sequences.
Here is a direct proof. We use the notation 
$\mrm{Z}^k(M) := \opn{Ker}(\d : M^k \to M^{k+1})$,
which is the object of $k$-cocycles of $M$, and  
$\mrm{Y}^k(M) := \opn{Coker}(\d : M^{k-1} \to M^{k})$, 
which does not have a name. There are functorial isomorphisms
\[ \mrm{H}^k(M) \cong \opn{Coker} \bigl( \d : M^{k-1} \to \mrm{Z}^k(M) \bigr)
\cong \opn{Ker} \bigl( \d : \mrm{Y}^k(M) \to  M^{k+1}  \bigr) . \]

For any additive functor $F : \cat{M} \to \cat{N}$ (not necessarily exact) there
is an obvious morphism 
$\al : F(\mrm{Z}^k(M)) \to \mrm{Z}^k(F(M))$, and it induces 
a morphism 
$\bar{\al} : F(\mrm{H}^k(M)) \to \mrm{H}^k(F(M))$.
An easy calculation shows that when $F$ is exact, the morphisms $\al$ and
$\bar{\al}$ are isomorphisms.

Given a contravariant additive functor $G : \cat{M} \to \cat{N}$, 
there is a morphism (slightly less obvious than $\al$, because of the change in
direction) 
$\be : G(\mrm{Y}^k(M)) \to \lb \mrm{Z}^{-k}(G(M))$. This  induces a morphism 
$\bar{\be} : G(\mrm{H}^k(M)) \to \mrm{H}^{-k}(G(M))$.
When $G$ is exact, the morphisms $\be$ and $\bar{\be}$ are isomorphisms.
\end{proof}

\begin{cor} \label{cor:293}
Let $A$ be a ring, $M$ a complex of $A$-modules, $P$ a flat $A$-module, and
$I$ and injective $A$-module. There are isomorphisms
\[ \mrm{H}^k(M \ot_A P) \cong \mrm{H}^k(M) \ot_A P \]
and 
\[ \mrm{H}^{-k} ( \opn{Hom}_A(M, I) ) \cong  \opn{Hom}_A( \mrm{H}^k(M), I) , \]
functorial in $M, P$ and $I$.
\end{cor}

\begin{proof}
Take $F(M) := M \ot_A P$ and 
$G(M) := \opn{Hom}_A(M, I)$, and use the proposition above.
(These are degenerate cases of the K\"unneth Theorems.)
\end{proof}
