---
doc_id: arxiv-2002.04901v5
doc_title: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms"
section_id: sec-001-1-idealistic-derived-completion-and-torsion
section_title: "Idealistic Derived Completion and Torsion"
section_number: 1
pages: 4-6
source_pdf: 2002.04901v5.pdf
source_sha256: f1320c4b87229215
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms — We begin by recalling the role that weak proregularity of an ideal in a commu- tative ring has in derived completion and adic"
---
\label{sec:idealistic}

Throughout the paper $A$ is a commutative ring.
It is {\em not} assumed that $A$ is a noetherian ring.
We denote by $\cat{M}(A)$ the category of $A$-modules, and by 
$\cat{D}(A)$ its unbounded derived category. 
Our reference for derived categories is the book \cite{Ye3}. 

In this section, $\a$ is a finitely generated ideal of the ring $A$. 

For an $A$-module $M$, its $\a$-adic completion is
\[ \La_{\a}(M) := 
\lim_{\leftarrow k} \, (M \lsp / \lsp \a^{k} \cd M) . \]
Completion is an $A$-linear functor 
\begin{equation} \label{eqn:180}
\La_{\a} : \cat{M}(A) \to \cat{M}(A) , 
\end{equation}
which is neither left nor right exact. 
It is an idempotent functor, in the sense that the two canonical morphisms 
$\La_{\a} \to \La_{\a} \circ \La_{\a}$
are isomorphism (cf.\ \cite[Definition 2.8]{VY}, and Remark \ref{rem:180}).
There is a functorial homomorphism 
$\tau_{\a, M} : M \to \La_{\a}(M)$,
and we call $M$ an {\em $\a$-adically complete module} if $\tau_{\a, M}$ is an 
isomorphism. (Note that older texts used the adjective ``complete and 
separated'' for what we call {complete.)

For an $A$-module $M$ we also have its $\a$-torsion submodule
\[ \Ga_{\a}(M) := \lim_{k \to} \, \opn{Hom}_A(A / \a^{k}, M) . \]
Torsion is a left exact $A$-linear functor 
\begin{equation} \label{eqn:181}
\Ga_{\a} : \cat{M}(A) \to \cat{M}(A) ,
\end{equation}
and it too is idempotent. 
There is a functorial homomorphism 
$\si_{\a, M} : \Ga_{\a}(M) \to M$,
and we call $M$ an {\em $\a$-torsion module} if $\si_{\a, M}$ is an 
isomorphism. 

\begin{dfn} \label{dfn:180}
The {\em idealistic derived $\a$-adic completion functor}
is the functor 
\[ \mrm{L} \La_{\a} : \cat{D}(A) \to \cat{D}(A) , \]
the left derived functor of the functor $\La_{\a}$ from (\ref{eqn:180}).
\end{dfn}

See Remark \ref{rem:210} regarding terminology. 
The left derived functor $\mrm{L} \La_{\a}$ is calculated by K-flat 
resolutions. It's first appearance seems to have been in the paper \cite{AJL}. 
Further study of the functor $\mrm{L} \La_{\a}$ was done in the paper 
\cite{PSY}. Several earlier papers (including \cite{Ma} and \cite{GM}) had 
considered the partial derived functors 
$\mrm{L}_q \La_{\a} = \mrm{H}^{-q} \circ \mrm{L} \La_{\a}$ 
from $\cat{M}(A)$ to itself. 

There is a functorial morphism 
\begin{equation} \label{eqn:182}
\tau_{\a, M}^{\mrm{L}} : M \to \mrm{L} \La_{\a}(M)
\end{equation}
in $\cat{D}(A)$; see \cite[Proposition 3.7]{PSY}.

\begin{dfn} \label{dfn:181} 
A complex $M \in \cat{D}(A)$ is called {\em derived $\a$-adically  
complete in the idealistic sense} if the morphism  
$\tau_{\a, M}^{\mrm{L}}$ in (\ref{eqn:182}) is an isomorphism. 
\end{dfn}

Here are the analogous definitions for $\a$-torsion. 

\begin{dfn} \label{dfn:185}
The {\em idealistic derived $\a$-torsion functor}
is the functor 
\[ \mrm{R} \Ga_{\a} : \cat{D}(A) \to \cat{D}(A) , \]
the right derived functor of the functor $\Ga_{\a}$ from 
(\ref{eqn:181}).
\end{dfn}

The derived functor $\mrm{R} \Ga_{\a}$ is calculated using K-injective 
resolutions. 

The idealistic derived torsion functor $\mrm{R} \Ga_{\a}$ has a long history, 
especially when the ring $A$ is local and $\a = \m$ is its maximal ideal. Then 
the cohomology modules 
$\opn{H}^q(\mrm{R} \Ga_{\m}(M)) = \mrm{R}^q \Ga_{\m}(M)$ are called 
the {\em local cohomologies} of $M$. See \cite{RD} and \cite{LC}. 

There is a functorial morphism 
\begin{equation} \label{eqn:185} 
\si_{\a, M}^{\mrm{R}} : \mrm{R} \Ga_{\a}(M) \to M 
\end{equation}
in $\cat{D}(A)$; see \cite[Proposition 3.10]{PSY}.

\begin{dfn} \label{dfn:186} 
A complex $M \in \cat{D}(A)$ is called {\em derived $\a$-torsion  
in the idealistic sense} if the morphism  
$\si_{\a, M}^{\mrm{R}}$ in (\ref{eqn:185}) is an isomorphism. 
\end{dfn}

The next proposition says that the idealistic derived completion and 
torsion functors depend not on the ideal $\a$, but rather on the closed subset 
in $\opn{Spec}(A)$ that the ideal $\a$ defines. 

\begin{prop} \label{prop:210}
Let $\a$ and $\b$ be finitely generated ideals in $A$ such that 
$\sqrt{\a} = \sqrt{\b}$. Then there are canonical isomorphisms 
$\mrm{L} \La_{\a} \iso \mrm{L} \La_{\b}$ and 
$\mrm{R} \Ga_{\a} \iso \mrm{R} \Ga_{\b}$
of triangulated functors from $\cat{D}(A)$ to itself, such that the diagrams 
\[ \UseTips \xymatrix @C=8ex @R=6ex {
\opn{Id} 
\ar[d]_{\tau^{\mrm{L}}_{\a}}
\ar[dr]^{\tau^{\mrm{L}}_{\b}}
\\
\mrm{L} \La_{\a}
\ar[r]^{\simeq}
&
\mrm{L} \La_{\b}
} 
\qquad \qquad 
\UseTips \xymatrix @C=8ex @R=6ex {
\mrm{R} \Ga_{\a}
\ar[r]^{\simeq}
\ar[dr]_{\si^{\mrm{R}}_{\a}}
&
\mrm{R} \Ga_{\b}
\ar[d]^{\si^{\mrm{R}}_{\b}}
\\
&
\opn{Id} 
} \]
are commutative.  
\end{prop}

\begin{proof}
An easy calculation shows that the obvious morphisms of functors 
$\La_{\a} \to \La_{\a + \b}$ and 
$\La_{\b} \to \La_{\a + \b}$ 
are both isomorphisms. It follows that there are isomorphisms
$\mrm{L} \La_{\a} \iso \mrm{L} \La_{\a + \b}$ 
and
$\mrm{L} \La_{\b} \iso \mrm{L} \La_{\a + \b}$ 
between the left derived functors. Hence there is a canonical isomorphism 
$\mrm{L} \La_{\a} \iso \mrm{L} \La_{\b}$.
The construction of $\tau^{\mrm{L}}_{\a}$ in \cite[Proposition 3.7]{PSY} shows 
that the first diagram above is commutative. 

The proof for derived torsion is similar.
\end{proof}


\begin{rem} \label{rem:210}
In the paper \cite{PSY} the names ``cohomologically $\a$-adically complete 
complex'' and ``cohomologically $\a$-torsion complex'' were used for the 
complexes in Definitions \ref{dfn:181} and \ref{dfn:186} respectively.  
The word ``cohomologically'' was replaced here with ``derived'', because it 
seems to describe the mathematical situation better: the condition in both 
cases is whether a certain morphism in the derived category $\cat{D}(A)$ is an 
isomorphism -- and not about the the cohomology $\opn{H}(M)$.  

The adjective ``idealistic'' was introduced in order to create a semantic 
distinction between the the definitions in this section, and those in the 
next section, which will be called ``sequential''. 
\end{rem}

\begin{rem} \label{rem:180}
We mentioned in passing that when $\a \sub A$ is a finitely generated ideal,
and $M$ is an arbitrary $A$-module, the $\a$-adic completion 
$\what{M} = \La_{\a}(M)$ is an $\a$-adically complete $A$-module. (This is 
included in the assertion that the functor $\La_{\a}$ is idempotent.)
See \cite[Corollary 3.6]{Ye1} for a proof. 

If the ideal $\a$ is not finitely generated, then the completion functor 
$\La_{\a}$ and the torsion functor $\Ga_{\a}$ are ill-behaved. Most disturbing 
is that fact that the functor $\La_{\a}$ could fail to be idempotent -- namely 
there are examples where the completion $\La_{\a}(M)$ is not 
$\a$-adically complete; see \cite[Example 1.8]{Ye1}.
\end{rem}

\begin{rem} \label{rem:250}
If the ideal $\a$ is weakly proregular, then the functor $\mrm{L} \La_{\a}$ is 
idempotent (see \cite[Lemma 7.9 and Proposition 7.10]{PSY}). Conversely, 
Positselski \cite[Proposition 5.3]{Po} shows that 
when $\a$ is not weakly proregular, and $P$ is a free $A$-module of infinite 
rank, then  $\mrm{L} \La_{\a}(P) = \La_{\a}(P)$ is not derived 
$\a$-adically complete in the idealistic sense. This means that without weak 
proregularity the functor $\mrm{L} \La_{\a}$ is not idempotent. 
\end{rem}
