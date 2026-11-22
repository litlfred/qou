---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-002-2-deformations-of-sheaves-of-rings
section_title: "Deformations of Sheaves of Rings"
section_number: 2
pages: 15-19
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.979
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:defs-alg-vars}

In this section we recall material from the companion papers
\cite{Ye7} and \cite{Ye9}.
For the rest of the paper we work over a base field $\K$ of characteristic
$0$. All algebras are by default $\K$-algebras, and all homomorphisms are by
default over $\K$. Further conventions are that associative algebras are
unital, and commutative algebras are associative (and unital). 
For $\K$-modules $M, N$ we write $M \ot N := M \ot_{\K} N$  and
$\opn{Hom}(M, N) := \opn{Hom}_{\K}(M, N)$.

\begin{dfn} \label{dfn:13}
A {\em parameter $\K$-algebra} is a 
complete local noetherian commutative
$\K$-algebra $R$, with maximal ideal $\m$ and residue field 
$R / \m = \K$.
We sometimes say that $(R, \m)$ is a parameter $\K$-algebra.
For $i \geq 0$ we let
$R_i := R / \m^{i+1}$.
The $\K$-algebra homomorphism $R \to \K$ is called the 
augmentation of $R$.

By homomorphism of parameter algebras $R \to R'$ we mean a $\K$-algebra
homomorphism (it is automatically a local homomorphism).
\end{dfn}

Note that $R$ can be recovered from $\m$, since
$R = \K \oplus \m$ as $\K$-modules, with the obvious multiplication. 

\begin{exa}
The most important parameter algebra in deformation theory is
$\K[[\hbar]]$, the ring of formal power series in the variable
$\hbar$. A $\K[[\hbar]]$-deformation (see below) is sometimes called
a ``$1$-parameter formal deformation''. 
\end{exa}

\begin{rem}
Some of the definitions and results in the paper hold for a field $\K$ of
arbitrary characteristic.
(A few of them hold even for any commutative ring $\K$ and any 
commutative $\K$-algebra $R$.) A rule of thumb is that
whenever exponential functions occur, we need characteristic $0$. For the sake
of clarity we restrict attention to a field of characteristic $0$ and parameter
algebras over it.
\end{rem}

Let $(R, \m)$ be a parameter algebra, and let $M$ be an $R$-module. 
The $\m$-adic completion of $M$ is the $R$-module
$\what{M} :=  \lim_{\leftarrow i}\, (R_i \otimes_R M)$. 
The module $M$ is called {\em $\m$-adically complete} if the
canonical homomorphism
$M \to \what{M}$ is bijective. 
Since $R$ is noetherian, the $\m$-adic completion of any $R$-module is 
$\m$-adically complete; see \cite[Corollary 3.5]{Ye5}. (This may be false when
$R$ is not noetherian.) 

Given a $\K$-module $V$ and an $R$-module $M$, we let
$M \hot V := \what{M \ot V}$, the $\m$-adic completion of the $R$-module 
$M \ot V$.  

Let $X$ be a topological space. Recall that a sheaf $\mcal{M}$ 
of $R$-modules on $X$ is called {\em flat} if for every point 
$x \in X$ the stalk $\mcal{M}_x$ is a flat $R$-module. 
The {\em $\m$-adic completion} of $\mcal{M}$ is the sheaf 
$\what{\mcal{M}} := \lim_{\leftarrow i}\, (R_i \otimes_R \mcal{M})$.
The sheaf $\mcal{M}$ is called {\em $\m$-adically complete} if the
canonical sheaf homomorphism 
$\mcal{M} \to \what{\mcal{M}}$ is an isomorphism.

We need some properties of sheaves on $X$.
Suppose $\bsym{U} = \{ U_k \}_{k \in K}$ is a collection of
open sets in $X$. For $k_0, \ldots, k_m \in K$ we write
$U_{k_0, \ldots, k_m} := U_{k_0} \cap \cdots \cap U_{k_m}$.

\begin{dfn} \label{dfn:23}
Let $\mcal{N}$ be a sheaf of abelian groups on a topological space
$X$. 
\begin{enumerate}
\item An open set $U \subset X$ will be called {\em
$\mcal{N}$-acyclic} if the derived functor sheaf cohomology satisfies
$\mrm{H}^i (U, \mcal{N}) = 0$ for all $i > 0$.

\item Now suppose $\bsym{U} = \{ U_k \}_{k \in K}$ is a collection of
open sets in $X$. We say that the collection $\bsym{U}$ is
{\em $\mcal{N}$-acyclic} if all the finite intersections
$U_{k_0, \ldots, k_m}$ are $\mcal{N}$-acyclic.

\item We say that {\em there are enough $\mcal{N}$-acyclic open
sets} if for any open set $U \subset X$, and any open covering
$\bsym{U}$ of $U$, there exists an $\mcal{N}$-acyclic open covering
$\bsym{U}'$ of $U$ which refines $\bsym{U}$.
\end{enumerate}
\end{dfn}

\begin{exa} \label{exa:20}
Here are a few typical examples of a topological space $X$, and a
sheaf $\mcal{N}$, such that there are enough $\mcal{N}$-acyclic 
open sets.
\begin{enumerate}
\item $X$ is an algebraic variety over the field $\K$
(i.e.\ an integral finite type separated  $\K$-scheme), with structure
sheaf $\mcal{O}_X$, and $\mcal{N}$ is a coherent $\mcal{O}_X$-module.
Then any affine open set $U$ is $\mcal{N}$-acyclic.

\item $X$ is a complex analytic manifold, with structure sheaf 
$\mcal{O}_X$, and $\mcal{N}$ is a coherent $\mcal{O}_X$-module. 
Here we take $\K = \mbb{C}$ of course. Then
any Stein open set $U$ is $\mcal{N}$-acyclic.

\item $X$ is a differentiable manifold, with structure
sheaf $\mcal{O}_X$, and $\mcal{N}$ is any $\mcal{O}_X$-module. 
The field is $\K = \mbb{R}$. Then
any open set $U$ is $\mcal{N}$-acyclic.

\item $X$ is a differentiable manifold, and $\mcal{N}$ is a locally
constant sheaf of abelian groups. Then any sufficiently small
simply connected open set $U$ is $\mcal{N}$-acyclic. 
\end{enumerate}
\end{exa}

In order to get a good behavior of $\m$-adically complete sheaves, we shall
consider deformations in the following setup:

\begin{setup} \label{setup:200}
$\K$ is a field of characteristic $0$;
$(R, \m)$ is a parameter $\K$-algebra; $X$ is a topological
space; and $\mcal{O}_X$ is a sheaf of commutative $\K$-algebras on $X$. 
Moreover $X$ has enough $\mcal{O}_X$-acyclic open sets.
\end{setup}

As Example \ref{exa:20} shows this covers many instances.
We assume Setup \ref{setup:200} for the rest of this section.

\begin{dfn} \label{dfn:230}
An {\em associative $R$-deformation of $\mcal{O}_X$} is a sheaf
$\mcal{A}$ of flat $\m$-adically complete associative
$R$-algebras on $X$, together with an isomorphism of
sheaves of $\K$-algebras
$\psi : \K \otimes_R \mcal{A} \to \mcal{O}_X$, called an {\em augmentation}.

Let $\mcal{A}$ and $\mcal{A}'$ be associative $R$-deformations of
$\mcal{O}_X$. A {\em gauge transformation}
$g : \mcal{A} \to \mcal{A}'$
is an isomorphism of sheaves of $R$-algebras that commutes with
the augmentations to $\mcal{O}_X$.
\end{dfn}

Similarly, given a commutative $\K$-algebra $C$, an {\em associative
$R$-deformation of $C$} is a flat $\m$-adically complete associative
$R$-algebra $A$, together with an isomorphism of $\K$-algebras
$\K \otimes_R A \cong C$. 

Observe that we do not impose a condition that an associative deformation $\AA$
should be ``locally differential''; see Remarks \ref{rem:defs-sh.110} and
\ref{rem:221} for a discussion. 

Recall that a Poisson bracket on a commutative $R$-algebra $A$ is 
an $R$-bilinear pairing 
$\{ -,- \} : A \times A \to A$ 
which is a Lie bracket, and is a biderivation (a derivation in each variable). 
The pair $(A, \{ -,- \} )$ is called a {\em Poisson $R$-algebra}. 
A homomorphism of Poisson $R$-algebras $A \to A'$ is an algebra homomorphism
that respects the Poisson brackets. All of this makes sense also for sheaves of
$R$-algebras. 

\begin{dfn} \label{dfn:231}
We view $\mcal{O}_X$ as a sheaf of Poisson $\K$-algebras
with the zero bracket.
A {\em Poisson $R$-deformation of $\mcal{O}_X$} is a sheaf
$\mcal{A}$ of flat $\m$-adically complete Poisson
$R$-algebras on $X$, together with an isomorphism of
sheaves of Poisson $\K$-algebras
$\psi : \K \otimes_R \mcal{A} \to \mcal{O}_X$, called an {\em augmentation}.

 Let $\mcal{A}$ and $\mcal{A}'$ be Poisson $R$-deformations of
$\mcal{O}_X$. A {\em gauge transformation}
$g : \mcal{A} \to \mcal{A}'$
is an isomorphism of sheaves of Poisson $R$-algebras that commutes with
the augmentations to $\mcal{O}_X$.
\end{dfn}

Similarly, given a commutative $\K$-algebra $C$, a {\em Poisson $R$-deformation
of $C$} is a flat $\m$-adically complete Poisson $R$-algebra $A$, together with
an isomorphism of Poisson $\K$-algebras $\K \otimes_R \mcal{A} \cong A$.

According to \cite[Proposition 4.5]{Ye9}, if $\mcal{A}$ is an associative
(resp.\ Poisson) $R$-deformation of $\OX$, and $U \subset X$ is an $\OX$-acyclic
open set, then $A := \Gamma(U, \mcal{A})$ is an associative
(resp.\ Poisson) $R$-deformation of $C :=  \Gamma(U, \OX)$.
The important fact is that $A$ is a flat and $\m$-adically complete
$R$-module.

Let $\mcal{A}$ be an associative (resp.\ Poisson) $R$-deformation of $\OX$.
It has an $R$-bilinear Lie bracket $[-,-]$ on it. In the associative case let
$\star$ denote the multiplication. Given local sections $a_1,  a_2 \in
\mcal{A}$, their bracket is 
$[a_1,  a_2] := a_1 \star a_2 - a_2 \star a_1$. 
In the Poisson case we take the Poisson bracket:
$[a_1,  a_2] := \{ a_1,  a_2 \}$. 
Note that $[\mcal{A}, \mcal{A}] \subset \m \AA$.
According to \cite[Corollary 3.8]{Ye9}, for every $j \geq 0$ the sheaf 
$\m^j \mcal{A}$ is $\m$-adically complete. Thus we obtain a sheaf of
pronilpotent groups
\begin{equation} \label{eqn:350}
\opn{Exp}(\m^j \mcal{A}) := 
\lim_{\leftarrow i}\, \opn{Exp}(\m^j \mcal{A} / \m^{j+i} \mcal{A}) ,
\end{equation}
and an isomorphism of sheaves of sets
\begin{equation} \label{eqn:351}
\exp : \m^j \AA \iso \opn{Exp}(\m^j \mcal{A}) .
\end{equation}
In particular we have a sheaf of pronilpotent groups
\begin{equation} \label{eqn:230}
\opn{IG}(\mcal{A}) := \opn{Exp}(\m \mcal{A})  
\end{equation}
that we call the {\em sheaf of inner gauge groups} of $\AA$.
A gauge transformation $g : \mcal{A} \to \mcal{A}'$ induces a group isomorphism 
\begin{equation} \label{eqn:234}
\opn{IG}(g) : \opn{IG}(\mcal{A}) \to \opn{IG}(\mcal{A}') .
\end{equation}

Consider a local section $\al \in \m \mcal{A}$.
Let $\opn{ad}_{\mcal{A}}(\al) : \mcal{A} \to \mcal{A}$ be the operator
$\opn{ad}_{\mcal{A}}(\al)(a') := [\al, a']$,
where $[-,-]$ is the Lie bracket. Then to the group element 
$a := \exp(\al) \in \opn{IG}(\mcal{A})$ we can associate the operator 
\begin{equation} \label{eqn:231}
\opn{ig}(a) := \exp( \opn{ad}_{\mcal{A}}(\al) ) 
\end{equation}
on $\mcal{A}$. It turns out that $\opn{ad}_{\mcal{A}}(\al)$ is a derivation of
the algebra $\mcal{A}$, and hence $\opn{ig}(a)$ is a gauge transformation of
$\mcal{A}$. In the associative case the group $\opn{IG}(\mcal{A})$ is
canonically identified with the kernel of the augmentation homomorphism 
$\psi : \mcal{A}^{\times} \to \mcal{O}_X^{\times}$,
and then $\opn{ig}(a)$ becomes conjugation by the invertible element $a$.
In the Poisson case we call $\opn{ig}(a)$ a 
{\em formal hamiltonian flow}.
See \cite[Section 5]{Ye9} for details. 

\begin{dfn} \label{dfn:233}
We denote by $\cat{AssDef}(R, \mcal{O}_X)$ (resp.\ 
$\cat{PoisDef}(R, \mcal{O}_X)$) the crossed groupoid 
$\cat{P} = (\cat{P}_1, \cat{P}_2, 
\opn{Ad}_{\cat{P}_1 \crvar \cat{P}_{2}}, \opn{D})$
described as follows:
\begin{itemize}
\item The objects of $\cat{P}$ are the associative (resp.\ Poisson)
$R$-deformations $\mcal{A}$ of $\mcal{O}_X$.

\item The $1$-morphisms, i.e.\ the elements of the sets
$\cat{P}_1(\mcal{A}, \mcal{A}')$, are the gauge transformations 
$g : \mcal{A} \to \mcal{A}'$.

\item The groups of $2$-morphisms are
$\cat{P}_2(\mcal{A}) := \Gamma(X, \opn{IG}(\mcal{A}))$.

\item The twisting by a $1$-morphism $g$ is 
$\opn{Ad}_{\cat{P}_1 \crvar \cat{P}_{2}}(g) := \opn{IG}(g)$.

\item The feedback 
$\opn{D} : \cat{P}_2(\mcal{A}) \to \cat{P}_1(\mcal{A})$ is
$\opn{D}(a) := \opn{ig}(a)$.
\end{itemize}
\end{dfn}

According to \cite[Proposition 5.7]{Ye9} these are indeed crossed groupoids.

In the next two propositions we write $\cat{P}(R, X)$ for either 
$\cat{AssDef}(R, \mcal{O}_X)$ or $\cat{PoisDef}(R, \mcal{O}_X)$; etc.

\begin{prop} \label{prop:206}
Let $U' \subset U$ be open subsets of $X$, and $R \to R'$ a homomorphism of
parameter algebras.  There is a morphism of crossed groupoids 
$\cat{P}(R, U) \to \cat{P}(R', U')$,
sending $\mcal{A}$ to $(R' \hatotimes{R} \mcal{A})|_{U'}$. 
\end{prop}

\begin{proof}
For $R \to R'$ this is \cite[Proposition 5.8]{Ye9}. That 
$\mcal{A}|_{U'}$ is a deformation of $\mcal{O}_{U'}$ is trivial. 
\end{proof}

\begin{prop} \label{prop:210}
The assignment 
$U \mapsto \cat{P}(R, U)$
is a stack of crossed groupoids on $X$. 
\end{prop}

\begin{proof}
By Proposition \ref{prop:206} we have a morphism of crossed groupoids
\[ \opn{rest}_{V / U} : \cat{P}(R, \mcal{O}_U) \to \cat{P}(R, \mcal{O}_V) \]
for every inclusion $V \subset U$ of open sets. So the local objects and local
$1$-morphisms form a split prestack of groupoids, say $\twocat{P}_1$. Since the
property of being an $R$-deformation of $\OX$ is local, and gauge
transformations between deformations are local, it follows that $\twocat{P}_1$
is a stack.
Finally, we know that the local $2$-morphisms form sheaves of groups
(these are the sheaves $\opn{IG}(\mcal{A})$). 
\end{proof}

\begin{dfn} \label{dfn:210}
\begin{enumerate}
\item The stack of crossed groupoids
$U \mapsto \cat{AssDef}(R, \mcal{O}_U)$ 
is called the {\em stack of associative $R$-deformations of $\OX$},
and it is denoted by $\twocat{AssDef}(R, \mcal{O}_X)$.

\item The stack of crossed groupoids
$U \mapsto \cat{PoisDef}(R, \mcal{O}_U)$ 
is called the {\em stack of Poisson $R$-deformations of $\OX$},
and it is denoted by $\twocat{PoisDef}(R, \mcal{O}_X)$.
\end{enumerate}
\end{dfn}

We now discuss first order brackets.
Suppose $\mcal{A}$ is an $R$-deformation of $\mcal{O}_X$. Since
$\mcal{A}$ is flat over $R$, and we have the augmentation 
$\psi : \K \otimes_R \mcal{A} \iso \mcal{O}_X$,
there is an induced $\K$-linear isomorphism 
$\m \mcal{A} / \m^2 \mcal{A} \cong
(\m / \m^2) \ot  \mcal{O}_X$.
This gives rise to a homomorphism of sheaves
$\psi^+ : \m \mcal{A} \to (\m / \m^2) \ot  \mcal{O}_X$.

Suppose $\mcal{A}$ is an associative deformation, with multiplication
$\star$. Given local sections $a_1,  a_2 \in \mcal{A}$, the
commutator satisfies
$a_1 \star a_2 - a_2 \star a_1 \in \m \mcal{A}$.
Hence we get
\begin{equation} \label{eqn:400}
\psi^+(a_1 \star a_2 - a_2 \star a_1) \in 
(\m / \m^2) \ot  \mcal{O}_X . 
\end{equation}
Likewise if $\mcal{A}$ is a Poisson deformation, with Poisson bracket
$\{ -,- \}$, then we have
$\psi^+(\{ a_1, a_2 \}) \in (\m / \m^2) \ot  \mcal{O}_X$.

\begin{prop} 
Let $\mcal{A}$ be associative \tup{(}resp.\ Poisson\tup{)}
$R$-deformation of $\mcal{O}_X$. 
There is a unique $\K$-bilinear sheaf morphism
\[ \{ -,- \}_{\mcal{A}} : \mcal{O}_X \times \mcal{O}_X \to 
(\m / \m^2) \ot \mcal{O}_X  \]
having the following property.
Given local sections $c_1, c_2 \in \mcal{O}_X$, choose local liftings 
$a_1,  a_2 \in \mcal{A}$ relative to the augmentation
$\psi : \mcal{A} \to \mcal{O}_X$, 
i.e.\ $c_i = \psi(a_i)$. Then 
\[ \{ c_1, c_2 \}_{\mcal{A}} = \psi^+ 
\bigl( \smfrac{1}{2} (a_1 \star a_2 - a_2 \star a_1) \bigr) \]
or
\[ \{ c_1, c_2 \}_{\mcal{A}} = \psi^+(\{ a_1, a_2 \}) , \]
as the case may be.
\end{prop}

\begin{proof}
This is a variant of the usual calculation in deformation theory. The
only thing to notice is that it makes sense for sheaves.
\end{proof}

\begin{dfn} \label{dfn:20}
The {\em first order bracket} of $\mcal{A}$ is the 
$\K$-bilinear sheaf morphism
$\{ -,- \}_{\mcal{A}}$ in the proposition above. 
\end{dfn}

\begin{prop} \label{prop:20}
\begin{enumerate}
\item The first order bracket is gauge invariant. Namely if 
$\mcal{A}$ and $\mcal{B}$ are gauge equivalent
$R$-deformations of $\mcal{O}_X$, then 
$\{ -,- \}_{\mcal{A}} = \{ -,- \}_{\mcal{B}}$.

\item The bracket $\{ -,- \}_{\mcal{A}}$ is a biderivation of
$\mcal{O}_X$-modules.

\item Suppose $R = \K[[\hbar]]$. Using the isomorphism
$\hbar^{-1} : \m / \m^2 \iso \K$, we get a bilinear function
\[ \{ -,- \}_{\mcal{A}} : \mcal{O}_X \times \mcal{O}_X \to \mcal{O}_X
. \]
Then this is a Poisson bracket on $\mcal{O}_X$.
\end{enumerate}
\end{prop}

\begin{proof}
All these statements are easy local calculations. 
\end{proof}
