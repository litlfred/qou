---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-002-2-the-derived-completion-and-torsion-functors
section_title: "The Derived Completion and Torsion Functors"
section_number: 2
pages: 7-10
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.769
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
\label{sec:comp}

In this section $A$ is a commutative ring, and $\a$ is an ideal in
it. We do not assume that $\a$ is finitely generated or that $A$ is 
$\a$-adically complete. 

For any $i \in \N$ let
$A_i := A / \a^{i+1}$.
The collection of rings $\{ A_i \}_{i \in \N}$ forms an inverse system. 
Following \cite{GM, AJL1}, for an $A$-module $M$ we write
\begin{equation}
\Lambda_{\a} (M) := \lim_{\leftarrow i}\, (A_i \otimes_A M) 
\end{equation}
for the $\a$-adic completion of $M$, although we sometimes use the more
conventional (yet possibly ambiguous) notation $\what{M}$. 
We get an additive functor 
$\Lambda_{\a} : \cat{Mod} A \to \cat{Mod} A$.
Recall that there is a functorial homomorphism
\begin{equation} \label{eqn:207}
\tau_M : M \to \Lambda_{\a} (M)
\end{equation}
for $M \in \cat{Mod} A$, coming from the homomorphisms
$M \to A_i \otimes_A M$. The module $M$ is called {\em $\a$-adically complete}
if $\tau_M$ is an isomorphism. (Some texts, such as \cite{Bo}, would say that
$M$ is separated and complete). As customary, when $M$ is
complete we usually identify $M$ with $\Lambda_{\a} (M)$ via $\tau_M$.

If the ideal $\a$ is finitely generated, then the functor $\Lambda_{\a}$ is
idempotent, in the sense that the homomorphism
\[ \tau_{\Lambda_{\a} (M)} : \Lambda_{\a} (M) \to 
\Lambda_{\a} (\Lambda_{\a} (M)) \]
is an isomorphism for every module $M$ (see \cite[Corollary 3.6]{Ye2}). 

Let $\what{A} :=  \Lambda_{\a} (A)$. Then $\what{A}$ is a 
ring, and $\tau_A : A \to \what{A}$ is a ring homomorphism. 
If $A$ is noetherian then $\what{A}$ is also noetherian, and flat over $A$. 
One can view the completion as a functor 
$\Lambda_{\a} : \cat{Mod} A \to \cat{Mod} \what{A}$. 
But in this paper we shall usually ignore this. 

\begin{rem}
The full subcategory of $\cat{Mod} A$ consisting of
$\a$-adically complete modules is additive, but not abelian in general. 

It is well known that when $A$ is noetherian, the completion functor
$\Lambda_{\a}$ is exact on 
$\cat{Mod}_{\mrm{f}} A$, the category of finitely generated modules. 
However, on $\cat{Mod} A$ the functor $\Lambda_{\a}$ is neither left exact nor
right exact, even in the noetherian case (see \cite[Examples 3.19 and
3.20]{Ye2}). 

When $A$ is not noetherian, we do not know if $\what{A}$ is flat over $A$.
Still, if $\a$ is finitely generated, and we let 
$\what{\a} := \what{A} \a \subset \what{A}$, then $\what{A}$ is 
$\what{\a}$-adically complete; this follows from \cite[Corollary 3.6]{Ye2}.

If the ideal $\a$ is not finitely generated, things are even worse: the 
functor $\Lambda_{\a}$ can fail to be idempotent; i.e.\ the completion
$\Lambda_{\a} (M)$ of a module $M$ could fail to be complete. See 
\cite[Example 1.8]{Ye2}.
\end{rem}

As for any additive functor, the functor $\Lambda_{\a}$ has a left derived
functor
\begin{equation} \label{eqn:51}
\mrm{L} \Lambda_{\a} : \cat{D}(\cat{Mod} A) \to \cat{D}(\cat{Mod} A) \ , \
\xi : \mrm{L} \Lambda_{\a} \to \Lambda_{\a}
\end{equation}
constructed using K-projective resolutions.

The next result was proved in \cite{AJL1}. Since this is so fundamental, we
chose to reproduce the easy proof.

\begin{lem}[\cite{AJL1}] \label{lem:43}
Let $P$ be an acyclic K-flat complex of $A$-modules. Then the complex 
$\Lambda_{\a} (P)$ is also acyclic. 
\end{lem}

\begin{proof}
Since $P$ is both acyclic and K-flat, for any $i$ we have an acyclic complex 
$A_i \otimes_A P$. The collection of complexes 
$\{ A_i \otimes_A P \}_{i \in \N}$ is an inverse system, and the homomorphism
$A_{i+1} \otimes_A P^j \to A_{i} \otimes_A P^j$
is surjective for every $i$ and $j$. But
$\Lambda_{\a} (P^j) = \lim_{\leftarrow i} \, (A_{i} \otimes_A P^j)$.
By the Mittag-Leffler argument (see \cite[Proposition 1.12.4]{KS1} or
\cite[Theorem 3.5.8]{We})
the complex $\Lambda_{\a} (P)$ is acyclic.
\end{proof}

\begin{prop} \label{prop:26}
If $P$ is a K-flat complex then the morphism
$\xi_P : \mrm{L} \Lambda_{\a} (P) \to \Lambda_{\a} (P)$
in $\cat{D}(\cat{Mod} A)$
is an isomorphism. Thus we can calculate $\mrm{L} \Lambda_{\a}$ using K-flat
resolutions.
\end{prop}

\begin{proof}
This is immediate from Lemma \ref{lem:43}; cf.\ \cite[Theorem I.5.1]{RD}.
\end{proof}


\begin{prop}[\cite{AJL1}] \label{prop:comp.1}
Let $M \in \cat{D}(\cat{Mod} A)$. There is a morphism
$\tau^{\mrm{L}}_M : M \to \mrm{L} \Lambda_{\a} (M)$
in $\cat{D}(\cat{Mod} A)$, functorial in $M$, such that 
$\xi_M \circ \tau^{\mrm{L}}_M = \tau_M$
as morphisms $M \to \Lambda_{\a} (M)$. 
\end{prop}

\begin{proof}
Given $M \in \cat{D}(\cat{Mod} A)$ let us choose a K-projective resolution
$\phi : P \to M$. Since $\phi$ and $\xi_P$ are isomorphisms in
$\cat{D}(\cat{Mod} A)$, we can define 
\[ \tau^{\mrm{L}}_M := \mrm{L} \Lambda_{\a}(\phi) \circ \xi_P^{-1}
\circ \tau_P \circ \phi^{-1} : M \to \mrm{L} \Lambda_{\a} (M)  . \]
This is independent of the the chosen resolution $\phi$, and satisfies 
$\xi_M \circ \tau_M = \tau^{\mrm{L}}_M$.
\end{proof}

\begin{dfn} \label{dfn:2} 
\begin{enumerate}
\item A complex $M \in \cat{D}(\cat{Mod} A)$ is called {\em
$\a$-adically cohomologically complete}
if the morphism $\tau^{\mrm{L}}_M : M \to \mrm{L} \Lambda_{\a} (M)$ is an
isomorphism. 

\item The full subcategory of $\cat{D}(\cat{Mod} A)$ consisting of 
$\a$-adically cohomologically complete complexes is denoted by 
$\cat{D}(\cat{Mod} A)_{\a \tup{-com}}$.
\end{enumerate}
\end{dfn}

It is clear that the subcategory 
$\cat{D}(\cat{Mod} A)_{\a \text{-} \tup{com}}$ is triangulated.

The notion of cohomologically complete complex is quite illusive. See Example
\ref{exa:1} . 

For an $A$-module $M$ and $i \in \N$ we identify 
$\opn{Hom}_A(A_i, M)$ with the submodule 
\[ \{ m \in M \mid \a^{i+1} m = 0 \} \subset M .  \]
The {\em $\a$-torsion submodule} of $M$ is
\[ \Gamma_{\a} (M) := \bigcup_{i \in \N} \, \opn{Hom}_A(A_i, M) 
\subset M . \]
The module $M$ is called an {\em $\a$-torsion module} if
$\Gamma_{\a} (M) = M$. We denote by 
$\cat{Mod}_{\a \tup{-tor}} A$ the full subcategory of $\cat{Mod} A$ consisting
of $\a$-torsion modules.

We get an additive functor 
$\Gamma_{\a} : \cat{Mod} A \to \cat{Mod} A$.
In fact this is a left exact functor. 
There is a functorial homomorphism 
$\sigma_M : \Gamma_{\a} (M) \to M$
which is just the inclusion. The functor $\Gamma_{\a}$ is idempotent, in the
sense that  
$\sigma_{\Gamma_{\a} (M)} : \Gamma_{\a} (\Gamma_{\a} (M)) \to  \Gamma_{\a} (M)$
is bijective. 

Like every additive functor, the functor $\Gamma_{\a}$ has a right derived
functor 
\begin{equation} \label{eqn:53}
\mrm{R} \Gamma_{\a} : \cat{D}(\cat{Mod} A) \to \cat{D}(\cat{Mod} A) \ , \
\xi : \Gamma_{\a} \to \mrm{R} \Gamma_{\a}
\end{equation}
constructed using K-injective resolutions. 

\begin{prop}
There is a functorial morphism
$\sigma^{\mrm{R}}_M : \mrm{R} \Gamma_{\a} (M) \to M $,
such that 
$\sigma_M = \sigma^{\mrm{R}}_M \circ \xi_M$
as morphisms $\Gamma_{\a} (M) \to M$ in $\cat{D}(\cat{Mod} A)$. 
\end{prop}

\begin{proof}
Choose a K-injective resolution $\phi : M \to I$, and define 
\[ \sigma^{\mrm{R}}_M := \phi^{-1} \circ \sigma_I \circ 
\xi_I^{-1} \circ \mrm{R} \Gamma_{\a}(\phi) . \]
This is independent of the resolution. 
\end{proof}

\begin{dfn} \label{dfn:8} 
\begin{enumerate}
\item A complex $M \in \cat{D}(\cat{Mod} A)$ is called {\em
cohomologically $\a$-torsion}
if the morphism $\sigma^{\mrm{R}}_M : \mrm{R} \Gamma_{\a} (M) \to M$ is an
isomorphism. 

\item The full subcategory of $\cat{D}(\cat{Mod} A)$ consisting of 
cohomologically $\a$-torsion complexes is denoted by 
$\cat{D}(\cat{Mod} A)_{\a \text{-tor}}$.

\item 
We denote by 
$\cat{D}_{\a \tup{-tor}}(\cat{Mod} A)$ the full subcategory of
$\cat{D}(\cat{Mod} A)$ consisting of the complexes whose cohomology modules are
in $\cat{Mod}_{\a \tup{-tor}} A$.
\end{enumerate}
\end{dfn}

It is clear that the subcategory $\cat{D}(\cat{Mod} A)_{\a \text{-} \mrm{tor}}$
is triangulated.

Since $\cat{Mod}_{\a \tup{-tor}} A$ is a thick abelian subcategory of 
$\cat{Mod} A$,  it follows
that \lb $\cat{D}_{\a \tup{-tor}}(\cat{Mod} A)$ is a triangulated category.
Note that 
$\Gamma_{\a} (I) \in \cat{D}_{\a \tup{-tor}}(\cat{Mod} A)$
for any K-injective complex $I$. Therefore  
\begin{equation} \label{eqn:54}
\cat{D}(\cat{Mod} A)_{\a \text{-} \mrm{tors}} \subset 
\cat{D}_{\a \tup{-tor}}(\cat{Mod} A) . 
\end{equation}
Later (in Corollary \ref{cor:17}) we shall see that there is equality in 
(\ref{eqn:54}) under some extra assumption.
