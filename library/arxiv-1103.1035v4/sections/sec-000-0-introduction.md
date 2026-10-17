---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-4
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.882
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:Int}

Let $\K$ be a field of characteristic $0$.
By {\em parameter algebra} over $\K$ we mean a complete
local noetherian commutative $\K$-algebra $R$, with maximal ideal $\m$, such
that $R / \m = \K$. The important example is $R = \K[[\hbar]]$, the ring of 
formal power series in the variable $\hbar$.

Let $(R, \m)$ be a parameter algebra, and let 
$\g = \bigoplus_{i \in \Z}\, \g^i$ be a DG
(differential graded) Lie algebra over $\K$.
There is an induced pronilpotent DG Lie algebra 
\[ \m \hot \g = \bigoplus_{i \in \Z}\, \m \hot \g^i . \]
A solution $\om \in \m \hot \g^1$ of the Maurer-Cartan equation 
\[ \d(\om) + \smfrac{1}{2} [\om, \om] = 0 \]
is called an {\em MC element}. The set of MC elements is denoted by 
$\opn{MC}(\g, R)$. There is an action of the {\em gauge group} 
$\opn{exp}(\m \hot \g^0)$
on the set $\opn{MC}(\g, R)$, and we write
\begin{equation}
\ol{\opn{MC}}(\g, R) := \opn{MC}(\g, R) / \opn{exp}(\m \hot \g^0) ,
\end{equation}
the quotient set by this action.

The {\em Deligne groupoid} $\mbf{Del}(\g, R)$, introduced in \cite{GM}, is the
transformation \lb groupoid associated to the action of the group 
$\opn{exp}(\m \hot \g^0)$ on the set $\opn{MC}(\g, R)$. So the set 
$\pi_0 (\mbf{Del}(\g, R))$ of isomorphism classes of objects of this
groupoid equals $\ol{\opn{MC}}(\g, R)$. 
In \cite[Theorem 2.4]{GM} it was proved that if $R$ is artinian, $\g$ and $\h$
are DG Lie algebras concentrated in the degree range $[0, \infty)$
(we refer to this as the ``nonnegative nilpotent case''), and 
$\phi : \g \to \h$ is a DG Lie algebra quasi-isomorphism, then the induced
morphism of groupoids 
\[ \mbf{Del}(\phi, R) : \mbf{Del}(\g, R) \to \mbf{Del}(\h, R) \]
is an equivalence.

We introduce the {\em reduced Deligne groupoid} 
$\mbf{Del}^{\mrm{r}}(\g, R)$,
which is a certain quotient of the Deligne groupoid $\mbf{Del}(\g, R)$;
see Section \ref{sec:red-del} for details. 
If the {\em Deligne 2-groupoid} $\mbf{Del}^{2}(\g, R)$ is defined 
(see below), then 
\begin{equation} \label{eqn:109}
\mbf{Del}^{\mrm{r}}(\g, R) = 
\pi_1 (\mbf{Del}^{2}(\g, R)) .
\end{equation}
However the groupoid $\mbf{Del}^{\mrm{r}}(\g, R)$ always exists. 
This new groupoid also has the property that 
\[ \pi_0 (\mbf{Del}^{\mrm{r}}(\g, R)) = \ol{\opn{MC}}(\g, R) . \]

Here is the first main result of our paper. It is a generalization to the
unbounded pronilpotent case (i.e.\ the DG Lie algebras $\g$ and $\h$ can be
unbounded, and the parameter algebra $R$ doesn't have to be artinian) of
\cite[Theorem 2.4]{GM}. Our proof is similar to that of \cite[Theorem 2.4]{GM}:
we also use obstruction classes. 

\begin{thm} \label{thm:4}
Let $R$ be a parameter algebra over $\K$, and let $\phi : \g \to \h$ be a
DG Lie algebra quasi-isomorphism over $\K$. Then the morphism of groupoids
\[ \mbf{Del}^{\mrm{r}}(\phi, R) : \mbf{Del}^{\mrm{r}}(\g, R) 
\to \mbf{Del}^{\mrm{r}}(\h, R)  \]
is an equivalence. 
\end{thm}

This is Theorem \ref{thm:2} in the body of the paper. 

A DG Lie algebra $\g =  \bigoplus_{i \in \Z}\, \g^i$ is said to be 
of {\em quantum type} if $\g^i = 0$ for all $i < -1$. A DG Lie algebra 
$\til{\g}$ is said to be of {\em quasi quantum type} if 
there exists a DG Lie quasi-isomorphism $\til{\g} \to \g$, for some 
quantum type DG Lie algebra $\g$. 
Important examples of such DG Lie algebras are given in Example \ref{exa:102}.
In Section \ref{sec:del-2-grpd} we prove that if $R$ is artinian, or if
$\g$ is of quasi quantum type, then the {\em Deligne $2$-groupoid} 
$\mbf{Del}^2(\g, R)$ exists. The original construction (see \cite{Ge}) applied
only to the case when $R$ is artinian and $\g$ is of quantum type. 

Here is the second main result of this paper (repeated as Theorem
\ref{thm:105}):

\begin{thm} \label{thm:107}
Let $R$ be a parameter algebra, let $\g$ and $\h$ be
DG Lie algebras, and let $\phi : \g \to \h$ be a DG Lie algebra
quasi-isomorphism. Assume either of these two conditions holds\tup{:}
\begin{itemize}
\rmitem{i} $R$ is artinian.  
\rmitem{ii} $\g$ and $\h$ are of quasi quantum type.
\end{itemize}  
Then the morphism of $2$-groupoids
\[ \mbf{Del}^2(\phi, R) : \mbf{Del}^2(\g, R) \to \mbf{Del}^2(\h, R) \]
is a weak equivalence.
\end{thm}

The proof of Theorem \ref{thm:107} relies on Theorem \ref{thm:4}, via formula 
(\ref{eqn:109}).
Theorem \ref{thm:107} plays a crucial role in our new proof of {\em twisted
deformation quantization}, in the revised version of \cite{Ye4}.

An {\em  $\mrm{L}_{\infty}$ morphism} $\Phi : \g \to \h$ is a sequence 
$\Phi = \{ \phi_j \}_{j \geq 1}$ of $\K$-linear functions 
\[ \phi_j : \bwedge^j \g \to \h \]
that generalizes the notion of DG Lie algebra homomorphism 
$\phi : \g \to \h$. Thus $\phi_1 : \g \to \h$ is a 
DG Lie algebra homomorphism, up to a homotopy given by $\phi_2$; and so on. 
See Section \ref{sec:L-infty} for details. 
The morphism $\Phi$ is called an {\em $\mrm{L}_{\infty}$ quasi-isomorphism}
if $\phi_1 : \g \to \h$ is a quasi-isomorphism. 
The concept of $\mrm{L}_{\infty}$ morphism gained
prominence after the Kontsevich Formality Theorem from 1997 (see
\cite{Ko2}). 

An $\mrm{L}_{\infty}$ morphism $\Phi : \g \to \h$ induces an $R$-multilinear 
$\mrm{L}_{\infty}$ morphism 
\[ \Phi_R = \{ \phi_{R, j} \}_{j \geq 1} : \m \hot \g \to \m \hot \h . \]
Given an element $\om \in \m \hot \g^1$ we write
\begin{equation}
\opn{MC}(\Phi, R) (\om) :=
\sum_{j \geq 1} \, \smfrac{1}{j!} \phi_{R, j}
(\underset{j}{\underbrace{\om, \ldots, \om}}) \in \m \hot \h^1 .
\end{equation}
This sum converges in the $\m$-adic topology of $\m \hot \h^1$. 
It is known that the function $\opn{MC}(\Phi, R)$ sends MC elements to MC
elements, and it respects gauge equivalence (see Propositions \ref{prop:4}
and \ref{prop:5}).
So there is an induced function
$\ol{\opn{MC}}(\Phi, R)$ from 
$\ol{\opn{MC}}(\g, R)$ to $\ol{\opn{MC}}(\h, R).$

Here is the third main result of our paper.

\begin{thm} \label{thm:1}
Let $\g$ and $\h$ be DG Lie algebras, let $R$ be a parameter algebra, and let 
$\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ quasi-isomorphism, all over the
field $\K$. Then the function 
\[ \ol{\opn{MC}}(\Phi, R) : \ol{\opn{MC}}(\g, R) \to \ol{\opn{MC}}(\h, R)  \]
is bijective.
\end{thm}

This is Theorem \ref{thm:3} in the body of the paper. We emphasize
that this result is in the unbounded pronilpotent case. 
The proof of Theorem \ref{thm:1} goes like this: we use the bar-cobar
construction to reduce to the case of a DG Lie algebra quasi-isomorphism
$\til{\Phi} : \til{\g} \to \til{\h}$; and
then we use Theorem \ref{thm:4}.

Theorem \ref{thm:1} was known in the nilpotent case; see 
\cite[Theorem  4.6]{Ko2}, and  \cite[Theorem 3.6.2]{CKTB}. 
The proof sketched in \cite[Section 4.5]{Ko2} relies on the structure 
of $\mrm{L}_{\infty}$ algebras. The proof in
\cite[Section 3.7]{CKTB} relies on the work of Hinich on the Quillen model
structure of coalgebras. It is not clear whether these methods work also in the
pronilpotent case. 

In this paper we only consider pronilpotent DG Lie algebras of the form 
$\m \hot \g$. 
Presumably Theorems \ref{thm:4}, \ref{thm:107} and \ref{thm:1} can be extended
to a more general setup -- see Remark \ref{rem:11}.

\medskip \noindent
{\bf Acknowledgments.} 
I wish to thank James Stasheff, Vladimir Hinich, Michel Van den Bergh,
William Goldman, Oren Ben Bassat, Marco Manetti and Ronald Brown
for useful conversations.
Thanks also to the referee for reading the paper carefully and providing
several constructive remarks.
