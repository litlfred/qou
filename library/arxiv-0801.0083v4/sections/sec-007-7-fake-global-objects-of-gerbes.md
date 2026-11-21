---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-007-7-fake-global-objects-of-gerbes
section_title: "Fake Global Objects of Gerbes"
section_number: 7
pages: 33-36
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.983
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec.fake}

In this section $X$ is some topological space. We will study a gerbe
$\gerbe{G}$ on $X$, with center $\mrm{Z}(\gerbe{G})$,
and the central extension of gerbes
\begin{equation} \label{eqn:11}
1 \to  \mrm{Z}(\gerbe{G}) \to \gerbe{G} \xar{F} 
\gerbe{G} / \mrm{Z}(\gerbe{G}) \to 1 .
\end{equation}

\begin{dfn}
An object 
$i \in \opn{Ob}\, \bigl( \gerbe{G} / \mrm{Z}(\gerbe{G}) \bigr)(X)$ 
is called a {\em fake global object of $\gerbe{G}$}.
\end{dfn}

When we need to emphasize that $i \in \opn{Ob} \gerbe{G}(X)$,
as opposed to being in \linebreak
$\opn{Ob}\, \bigl( \gerbe{G} / \mrm{Z}(\gerbe{G}) \bigr)(X)$,
we will say that $i$ is a {\em true global object of $\gerbe{G}$}.

Note that some fake global objects $i$ of $\gerbe{G}$ will lift to
true global objects of $\gerbe{G}$, whereas other won't; this is
determined by the vanishing of the obstruction class 
\[ \opn{cl}^2_F(i) \in \check{\mrm{H}}^2 \bigl( X, \mrm{Z}(\gerbe{G}) 
\bigr) \]
for the central extension of gerbes (\ref{eqn:11}), if this obstruction
class is defined. 

Here is an easy example of a fake global object that does not lift.

\begin{exa} \label{exa:11}
Suppose $X$ is an algebraic variety over a field, with 
$\mrm{H}^2(X, \mcal{O}_X) \neq 0$. 
Choose a nonzero cohomology class $c \in \mrm{H}^2(X, \mcal{O}_X)$. 
There is an abelian gerbe $\gerbe{G}$ corresponding to $c$, and it has
no global objects. (This construction is standard; cf.\ Example \ref{exa:17}
below.) Indeed, here the gerbe 
$\gerbe{G} / \mrm{Z}(\gerbe{G})$ 
is equivalent to the gerbe $\gerbe{I}$ from Example \ref{exa:15}, and
hence it has one global object (up to isomorphism), say $j$. 
We have a central extension of gerbes
\[ 1 \to  \mcal{O}_X \to \gerbe{G} \xar{F} 
\gerbe{G} / \mrm{Z}(\gerbe{G}) \to 1 , \]
and the obstruction class to lifting $j$ to an object of 
$\gerbe{G}(X)$ is $\opn{cl}^2_F(j) = c$. We see that $j$ is a fake global object
of $\gerbe{G}$, which does not lift to a true global object of
$\gerbe{G}$.
\end{exa}

\begin{rem} \label{rem.1}
The reason we are interested in fake global objects has to do
with {\em twisted deformations}. Let $\K$ be a field of
characteristic $0$, and consider the ring of formal power series
$\K[[\hbar]]$ in the variable $\hbar$. Let $(X, \mcal{O}_X)$ be a
ringed space over $\K$, as in Examples \ref{exa:12}-\ref{exa.3}. As explained in
\cite{Ye}, a twisted (Poisson or associative)
$\K[[\hbar]]$-deformation $\gerbe{A}$ of $\mcal{O}_X$ is made up
of many locally defined sheaves of (Poisson or associative)
$\K[[\hbar]]$-algebras
$\mcal{A}_i$, that are glued together by isomorphisms 
$\opn{Ad}(g) : \mcal{A}_i \iso \mcal{A}_j$,
called {\em gauge equivalences}. The indices 
$i,j, \ldots$ are local objects of the {\em gauge gerbe} $\gerbe{G}$
of $\gerbe{A}$, and the isomorphisms $g$ are local sections
of the bitorsors $\gerbe{G}(i, j)$.
The group $\gerbe{G}(i, i)$, for a local object $i$,
is by definition $\opn{exp}(\hbar \mcal{A}_i)$, where $\mcal{A}_i$ is
viewed as
a pronilpotent $\K[[\hbar]]$-linear Lie algebra, with Lie bracket
being either its
Poisson bracket or the commutator of the associative multiplication.
The deformations $\mcal{A}_i$, for $i \in \opn{Ob} \gerbe{G}(X)$,
are called {\em global deformations
belonging to $\gerbe{A}$}. In case such global deformations do
not exist (i.e.\ the gerbe $\gerbe{G}$ is nontrivial), then we say
$\gerbe{A}$ is {\em really twisted}. Note that the gerbe $\gerbe{G}$
is pronilpotent.

Now consider a global deformation $\mcal{A}$ of the following sort: there is an
open covering $X = \bigcup_{k \in K} U_k$, objects
$i_k \in \opn{Ob} \gerbe{G}(U_k)$, and gauge equivalences
$h_k : \mcal{A}|_{U_k} \iso \mcal{A}_{i_k}$, 
such that
\[ h_{k_1} \circ h_{k_0}^{-1} = \opn{Ad}(g_{k_0, k_1})  \]
for some 
$g_{k_0, k_1} \in \gerbe{G}(U_k)(i, i)$. 
So as gauge equivalences 
$\mcal{A}_{i_{k_0}} \iso \mcal{A}_{i_{k_2}}$
we have the equality
\[ \opn{Ad}(g_{k_0, k_2}) = \opn{Ad}(g_{k_1, k_2}) \circ 
\opn{Ad}(g_{k_0, k_1})  . \]
The local isomorphisms $g$ in the center 
$\mrm{Z}(\gerbe{G}(i, i))$ are precisely those such that the 
gauge equivalences $\opn{Ad}(g)$
are trivial. Hence, going to the extension of gerbes (\ref{eqn:11}), we have
\[  F(g_{k_0, k_2}) = F(g_{k_1, k_2}) \circ 
F(g_{k_0, k_1}) \]
in the gerbe $\gerbe{G} / \mrm{Z}(\gerbe{G})$. 
This implies that the global deformation $\mcal{A}$ corresponds to an object
$j \in \opn{Ob} \, \bigl( \gerbe{G} / \mrm{Z}(\gerbe{G}) \bigr)(X)$,
i.e.\ to a fake global object of $\gerbe{G}$. Therefore we call it a 
{\em global deformation falsely belonging to $\gerbe{A}$}.
Observe that the obstruction class 
$\opn{cl}^2_F(j) \in \check{\mrm{H}}^2(X, \mrm{Z}(\gerbe{G}))$ 
is represented by the cocycle 
\[  g_{k_0, k_1, k_2}  :=  g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ
g_{k_0, k_1} . \]
If $\opn{cl}^2_F(j) \neq 1$ then the deformation $\mcal{A}$ does not truly
belong to $\gerbe{A}$.
\end{rem}

Next a result. 

\begin{prop} \label{prop:3} 
Let $\gerbe{G}$ be a gerbe on $X$, and assume there are enough
$\mrm{Z}(\gerbe{G})$-acyclic open coverings.
Let 
$\bar{\gerbe{G}} := \gerbe{G} / \mrm{Z}(\gerbe{G})$.
\begin{enumerate}
\item If $\check{\mrm{H}}^2(X, \mrm{Z}(\gerbe{G})) = 1$, then the
canonical morphism of groupoids
$\gerbe{G}(X) \to \bar{\gerbe{G}}(X)$
is essentially surjective on objects. In particular any fake global
object of $\gerbe{G}$ lifts to a true global object.
\item If moreover $\check{\mrm{H}}^1(X, \mrm{Z}(\gerbe{G})) = 1$, then 
$\gerbe{G}(X) \to \bar{\gerbe{G}}(X)$
is bijective on isomorphism classes of objects.
\end{enumerate}
\end{prop}

\begin{proof}
By Theorem \ref{thm:10} the obstruction classes 
$\opn{cl}^1_F(h)$ and $\opn{cl}^2_F(j)$ are all defined. 
Assertion (1) is a consequence of Theorem \ref{thm.2}, and assertion (2) 
is a consequence of Theorem \ref{thm.3}.
\end{proof}

\begin{exa} \label{exa.5}
Let $\K$ be a smooth algebraic variety over a field $\K$ of characteristic $0$. 
Suppose $\gerbe{A}$ is a twisted (Poisson or associative)
$\K[[\hbar]]$-deformation of $\mcal{O}_X$ which is symplectic. This means that
the first order bracket
$\{ -,- \}_{\gerbe{A}}$ on $\mcal{O}_X$ is nondegenerate 
(cf.\ \cite{Ye}). 
It follows that the center of the gauge gerbe $\gerbe{G}$ is isomorphic
(canonically) to the constant sheaf $\K[[\hbar]]$. 
Now in the Zariski topology constant sheaves have no higher cohomologies; and
hence Proposition \ref{prop:3} applies. So there are as many global
deformations falsely belonging to $\gerbe{A}$ there are global
deformations truly belonging to $\gerbe{A}$ in this case. 
\end{exa}

\begin{exa} \label{exa:17}
Let $\K$ be a smooth algebraic variety over a field $\K$ of
characteristic $0$, and assume there is a nonzero class 
$c \in \mrm{H}^2(X, \mcal{O}_X)$. Then there is a twisted
associative $\K[[\hbar]]$-deformation $\gerbe{A}$ of $\mcal{O}_X$,
which is commutative (i.e.\ each of the local deformations 
$\mcal{A}_i$ belonging to $\gerbe{A}$ is commutative). See 
\cite[Example 6.17]{Ye} for this construction. The gauge
gerbe here is abelian: 
$\gerbe{G} \cong \opn{exp}(\hbar \mcal{O}_X[[\hbar]])$.
We filter it by
$\gerbe{N}_p := 
\opn{exp}(\hbar^{p+1} \mcal{O}_X[[\hbar]])$.
For $p = 0$ we have a central extension of gerbes
\[ 1 \to \mcal{O}_X \xar{\hbar^{}} 
\gerbe{G} / \gerbe{N}_1 \to
\gerbe{G} / \gerbe{N}_0 \to 1 , \]
and for the unique (up to isomorphism) global object $j$ of the gerbe 
$\gerbe{G} / \gerbe{N}_0$, 
the obstruction class is $\opn{cl}^2(j) = c$
(same as in Example \ref{exa:11}). Hence 
$\opn{Ob} (\gerbe{G} / \gerbe{N}_1) = \emptyset$,
implying that 
$\opn{Ob} \gerbe{G}(X) = \emptyset$, so $\gerbe{A}$ is really
twisted. 
\end{exa}

One of the reasons for introducing the obstruction classes
$\opn{cl}^2_F(j)$
is to address the following question. 

\begin{que} \label{que.1}
Does there exist an algebraic variety
$X$, and a {\em symplectic} twisted
$\K[[\hbar]]$-deformation
$\gerbe{A}$ of $\mcal{O}_X$, that is really twisted? We expect
the answer to be positive. Indeed, we think this happens when
$X$ is any abelian surface, and we take any nonzero Poisson bracket
on $\mcal{O}_X$, and let $\gerbe{A}$ be its canonical
quantization (as in \cite[Theorem 0.1]{Ye}), which is a twisted associative
$\K[[\hbar]]$-deformation of $\mcal{O}_X$.
\end{que}

\begin{exa} 
Let $X$ be a complex analytic manifold, and denote by $\mcal{O}_X$ the sheaf
of holomorphic functions. Let
$\gerbe{A}$ be a symplectic (Poisson or associative) twisted
$\mbb{C}[[\hbar]]$-deformation of
$\mcal{O}_X$. Then the gauge gerbe $\gerbe{G}$ has a
central filtration, with
$\gerbe{N}_p(i) = \opn{exp}(\hbar^{p+1} \mcal{A}_i)$
for a local object $i$. 
And the center of $\gerbe{G}$ is
\[ \opn{exp}( \hbar \mbb{C}[[\hbar]] ) =
\opn{exp} \bigl( \prod\nolimits_{m = 1}^{\infty} \mbb{C} \hbar^m \bigr) 
\subset \gerbe{G} . \]
We put on 
$\bar{\gerbe{G}} := \gerbe{G} / \mrm{Z}(\gerbe{G})$
the induced filtration  $\{ \bar{\gerbe{N}}_p \}_{p \in \N}$.
Define a normal subgroupoid
\[ \gerbe{M}_p := \gerbe{N}_{p+1} \cdot
\opn{exp} \bigl( \prod\nolimits_{m = 1}^p \mbb{C} \hbar^m \bigr) \subset 
\gerbe{G} . \]
Then for every $p \geq 0$ there is a 
morphism of central extensions of gerbes
\[ \UseTips \xymatrix @C=5ex @R=5ex {
1 
\ar[r]
&
\mcal{O}_X
\ar[r]
\ar[d]
&
\gerbe{G} / \gerbe{M}_p
\ar[r]
\ar[d]
& 
\bar{\gerbe{G}} / \bar{\gerbe{M}}_p
\ar[r]
\ar[d]^{=}
& 
1
\\
1 
\ar[r]
&
\mcal{O}_X / \mbb{C}
\ar[r]
&
\bar{\gerbe{G}} / \bar{\gerbe{N}}_{p+1}
\ar[r]^{E_p}
& 
\bar{\gerbe{G}} / \bar{\gerbe{N}}_p
\ar[r]
& 
1 .
} \]
We do not know if there are enough acyclic open coverings for the
sheaf $\mcal{O}_X / \mbb{C}$; but according to Proposition
\ref{prop:7},
for any 
$j \in \opn{Ob} (\bar{\gerbe{G}} / \bar{\gerbe{N}}_p)(X)$ 
the obstruction class 
$\opn{cl}^2_{E_n}(j) \in 
\check{\mrm{H}}^2(X, \mcal{O}_X / \mbb{C})$
exists, and moreover it comes from 
$\check{\mrm{H}}^2(X, \mcal{O}_X)$.

Now assume that the homomorphism 
\begin{equation} \label{eqn:13}
\mrm{H}^2(X, \mbb{C}) \to \mrm{H}^2(X, \mcal{O}_X)
\end{equation}
is surjective. This happens when $X$ is the analytification of 
a projective algebraic variety (cf.\ \cite[Section 5]{NT}). 
Then 
$\opn{cl}^2_{E_n}(j) = 1$ for all $p$.
Presumably Theorem \ref{thm.4} can be refined to work with vanishing of
obstruction classes (rather than vanishing of the whole cohomology groups). This
would imply that fake global deformations exist here. 
\end{exa}

\begin{exa}
Suppose $X$ is a smooth projective algebraic variety over $\mbb{C}$ (with the
Zariski topology), and let $X_{\mrm{an}}$ be the corresponding complex
analytic
manifold. Let $\gerbe{A}$ be a symplectic (Poisson or associative)
twisted $\mbb{C}[[\hbar]]$-deformation of $\mcal{O}_X$. There is an induced
deformation $\gerbe{A}_{\mrm{an}}$ of $\mcal{O}_{X_{\mrm{an}}}$.
As in Example \ref{exa.5}, there are as many global deformations truly
belonging to $\gerbe{A}$ as there are global deformations falsely
belonging to it. By the
GAGA principle we have 
$\mrm{H}^p(X, \mcal{O}_X) =  
\mrm{H}^p(X_{\mrm{an}}, \mcal{O}_{X_{\mrm{an}}})$
for all $p$, and therefore there as many global deformations truly belonging to 
$\gerbe{A}$ as there are global deformations truly belonging to
$\gerbe{A}_{\mrm{an}}$. In particular, there might be none
(see Question \ref{que.1}). On the other hand, by Hodge Theory the homomorphism
(\ref{eqn:13}) is surjective here (cf.\ \cite[Section 1.2]{BK}), and therefore
(under the caveat of refining Theorem \ref{thm.4}) there is always some global
deformation falsely belonging to 
$\gerbe{A}_{\mrm{an}}$.
\end{exa}
