---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-005-5-sufficient-conditions-for-existence-of-obstruc
section_title: "Sufficient Conditions for Existence of Obstruction Classes"
section_number: 5
pages: 25-29
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.985
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec.suff}

Let $\mcal{N}$ be a sheaf of abelian groups on a topological space
$X$. The operation in $\mcal{N}$ is multiplication.
We denote by $\mrm{H}^i (X, \mcal{N})$ the derived functor sheaf
cohomology. An open
set $U \subset X$ will be called {\em $\mcal{N}$-acyclic} if the sheaf
cohomology satisfies
$\mrm{H}^i (U, \mcal{N}) = 1$ for all $i > 0$. Now suppose 
$\bsym{U} = \{ U_k \}_{k \in K}$ is a collection of open sets in $X$. 
We say that the collection $\bsym{U}$ is $\mcal{N}$-acyclic if all the open 
sets $U_{k_0, \ldots, k_m}$ are $\mcal{N}$-acyclic.

\begin{dfn}
Let $\mcal{N}$ be a sheaf of abelian groups on $X$.
We say that {\em there are enough $\mcal{N}$-acyclic open coverings} if for 
any open set $U \subset X$, and any open covering $\bsym{U}$ of $U$,
there exists an $\mcal{N}$-acyclic open covering $\bsym{U}'$ of $U$ which
refines $\bsym{U}$. 
\end{dfn}

\begin{exa} \label{exa:12}
Suppose $X$ is a differentiable (i.e.\ $\mrm{C}^{\infty}$) manifold, and let
$\mcal{O}_X$ be the sheaf of $\mrm{C}^{\infty}$ $\mbb{R}$-valued functions on
it. If $\mcal{N}$ is an $\mcal{O}_X$-module, then any open covering of
$X$ is $\mcal{N}$-acyclic. If $\mcal{K}$ is a constant sheaf of
abelian groups on $X$, then any open covering $\bsym{U} = \{ U_k \}_{k
\in K}$ such that 
the finite intersections $U_{k_0, \ldots, k_m}$ are contractible, is 
$\mcal{K}$-acyclic. There are always enough coverings of this sort.
\end{exa}

\begin{exa} \label{exa.2}
Suppose $X$ is a complex analytic manifold, and let
$\mcal{O}_X$ be the sheaf of holomorphic $\mbb{C}$-valued functions on
it. If $\mcal{N}$ is a coherent $\mcal{O}_X$-module, then any open covering of
$X$ by Stein manifolds is $\mcal{N}$-acyclic. There are always enough coverings
of this sort. 
Regarding constant sheaves see the previous example. (Oddly, we do not know if 
it is possible to find an open covering 
$\bsym{U} = \{ U_k \}_{k \in K}$ such that 
the finite intersections $U_{k_0, \ldots, k_m}$ are both contractible and
Stein.)
\end{exa}

\begin{exa} \label{exa.3}
Suppose $X$ is an algebraic variety over a field $\K$ (i.e.\ a
separated integral finite type $\K$-scheme), and let
$\mcal{O}_X$ be the structure sheaf. If $\mcal{N}$ is a coherent
$\mcal{O}_X$-module, then any affine open covering of $X$ (i.e.\ a covering
$\bsym{U} = \{ U_k \}_{k \in K}$ such that the open sets $U_k$ are all affine)
is $\mcal{N}$-acyclic. There are always enough coverings of this sort.
If $\mcal{K}$ is a constant sheaf of abelian groups
on $X$, then any open covering of $X$ is
$\mcal{K}$-acyclic (since $\mcal{K}$ is a flasque sheaf in the Zariski
topology).
\end{exa}

Recall that there are canonical group homomorphisms
\[ \check{\mrm{H}}^i(X, \mcal{N}) \to \mrm{H}^i(X, \mcal{N}) , \]
which are bijective for $i = 0, 1$; see \cite[Section III.4.]{Ha}.

\begin{prop} \label{prop:11}
Let $\mcal{N}$ be a sheaf of abelian groups on $X$.
\begin{enumerate}
\item If $\bsym{U}$ is an $\mcal{N}$-acyclic open covering of $X$,
then the canonical group homomorphisms
\[ \check{\mrm{H}}^i(\bsym{U}, \mcal{N}) \to \mrm{H}^i(X, \mcal{N}) \]
are bijective for all $i$. 
\item If there are enough $\mcal{N}$-acyclic open coverings, then for
any $\mcal{N}$-acyclic open covering  $\bsym{U}$ of $X$,
the canonical group homomorphisms
\[ \check{\mrm{H}}^i(\bsym{U}, \mcal{N}) \to
\check{\mrm{H}}^i(X, \mcal{N}) \to \mrm{H}^i(X, \mcal{N}) \]
are bijective for all $i$. 
\end{enumerate}
\end{prop}

\begin{proof}
Assertion (1) is \cite[Exercise III.4.11]{Ha}. Assertion (2) follows
from (1). See also the original \cite{Gr2}.
\end{proof}

 From now on in this section, the operation in the group $\mcal{N}$ is
multiplication, and the identity element is $1$. 

\begin{prop} \label{prop:9}
Suppose
\begin{equation} \label{eqn:15}
1 \to \mcal{N} \to \mcal{G} \to \mcal{H} \to 1 
\end{equation}
is an exact sequence of sheaves of groups on $X$. 
\begin{enumerate}
\item There is an exact sequence in \v{C}ech cohomology
\[ \begin{aligned}
& 1 \to \mcal{N}(X) \to \mcal{G}(X) \to \mcal{H}(X) \\
& \qquad \to \check{\mrm{H}}^1(X, \mcal{N}) \to \check{\mrm{H}}^1(X, \mcal{G}) 
\to \check{\mrm{H}}^1(X, \mcal{H}) .
\end{aligned} \]
Here $\check{\mrm{H}}^1(X, -)$ are pointed sets. 

\item Assume \tup{(\ref{eqn:15})} is a central extension, and there are enough
$\mcal{N}$-acyclic open coverings. Then the exact sequence of part \tup{(1)}
extends to an exact sequence
\[ \cdots \to \check{\mrm{H}}^1(X, \mcal{G}) 
\to \check{\mrm{H}}^1(X, \mcal{H}) \xar{\partial} \check{\mrm{H}}^2(X, \mcal{N})
. \]
\end{enumerate}
\end{prop}

\begin{proof}
(1) This is pretty easy. A readable proof can be found in \cite[Chapter V]{Gr1}.

\medskip \noindent
(2) A more general result is \cite[Corollaire to Proposition 3.4.2]{Gr2},
where there is no topological assumption of the sheaf $\mcal{N}$.
However, the precise statement and the proof rely on Godement
resolutions, and are hard to follow. Hence we
provide a relatively easy proof in the case we need. 

Recall that the pointed set $\check{\mrm{H}}^1(X, \mcal{H})$ classifies left 
$\mcal{H}$-torsors on $X$, up to isomorphism. And the function
$\check{\mrm{H}}^1(X, \mcal{G}) \to \check{\mrm{H}}^1(X, \mcal{H})$
sends a $\mcal{G}$-torsor to the induced $\mcal{H}$-torsor.

Let $\mcal{S}$ be an $\mcal{H}$-torsor. 
Choose an $\mcal{N}$-acyclic open covering 
$\bsym{U} = \{ U_k \}_{k \in K}$ of $X$ that trivializes $\mcal{S}$. 
For any index $k$ choose some
$s_k \in \mcal{S}(U_k)$. For any $k_0, k_1$ we have an element
$h_{k_0, k_1} \in \mcal{H}(U_{k_0, k_1})$ such that
$s_{k_1} = h_{k_0, k_1} \cdot s_{k_0}$.
Since 
$\check{\mrm{H}}^1(U_{k_0, k_1}, \mcal{N}) = 1$, by part (1) we have a
surjection of groups
$\mcal{G}(U_{k_0, k_1}) \to \mcal{H}(U_{k_0, k_1})$,
and thus we can lift $h_{k_0, k_1}$ to some
$g_{k_0, k_1} \in \mcal{G}(U_{k_0, k_1})$.
Define
\[ n_{k_0, k_1, k_2} := g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ
g_{k_0, k_1} \in \mcal{G}(U_{k_0, k_1, k_2}) . \]
Then 
\[ c := \{ n_{k_0, k_1, k_2} \}_{k_0, k_1, k_2 \in K} \]
is a \v{C}ech $2$-cocycle with values in $\mcal{N}$; cf.\
Lemma \ref{lem:10}. Let
\[ \partial(\mcal{S}) := [c] \in \check{\mrm{H}}^2(X, \mcal{N}) . \]
As in the proof of Lemma \ref{lem.4} we see that the cohomology class 
$\partial(\mcal{S})$ is independent of choices, and thus we get a well defined
function
\[ \partial : \check{\mrm{H}}^1(X, \mcal{H}) \to \check{\mrm{H}}^2(X, \mcal{N})
. \]
And like in the proof of Theorem \ref{thm.2} we see that
$\partial(\mcal{S}) = 1$ if and only if $\mcal{S}$ comes from a 
$\mcal{G}$-torsor. 
\end{proof}

Consider a central extension of gerbes
\begin{equation} \label{eqn:9}
1 \to  \mcal{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 
\end{equation}
on $X$.

\begin{lem} \label{lem.A.1}
Suppose $U$ is an $\mcal{N}$-acyclic open set. Let
$i, j \in \opn{Ob} \gerbe{G}(U)$ be such that 
$\gerbe{G}(U)(i, j) \neq \emptyset$. Then the function
\[ F : \gerbe{G}(U)(i, j) \to 
\gerbe{H}(U) \bigl( F(i), F(j) \bigr) \]
is surjective.
\end{lem}

\begin{proof}
Here both torsors 
$\gerbe{G}(i, j)$ and $\gerbe{H} \bigl( F(i), F(j) \bigr)$
are trivial over the respective sheaves of groups 
$\gerbe{G}(i, i)$ and $\gerbe{H} \bigl( F(i), F(i) \bigr)$;
so we may assume $i = j$. Since
$\check{\mrm{H}}^1(U, \mcal{N}) = 1$ the assertion follows from the exact
sequence in Proposition \ref{prop:9}(1), applied to the short exact sequence of
sheaves of groups
\[ 1 \to \mcal{N}|_U \to \gerbe{G}(i,i) \xar{F} \gerbe{H}(i,i) \to
1 . \]
\end{proof}

\begin{lem} \label{lem.A.2}
Suppose $U$ is an $\mcal{N}$-acyclic open set. Then for any
$i, j \in \opn{Ob} \gerbe{G}(U)$ the function
\[ F(i, j) : \gerbe{G}(U)(i, j) \to 
\gerbe{H}(U) \bigl( F(i), F(j) \bigr) \]
is surjective.
\end{lem}

\begin{proof}
If $\gerbe{H}(U) \bigl( F(i), F(j) \bigr) = \emptyset$ then there is
nothing to prove. So let us assume it is nonempty. We will prove that 
$\gerbe{G}(U) \bigl( i, j \bigr) \neq \emptyset$; and then the assertion
will follow by Lemma \ref{lem.A.1}.

Choose some $h \in \gerbe{H}(U) \bigl( F(i), F(j) \bigr)$. 
Let $\bsym{U} = \{ U_k \}_{k \in K}$ be an open covering of $U$, such that 
for any $k$ there exists an isomorphism 
$g_k \in \gerbe{G}(U_k)(i, j)$ lifting $h$.
This can be done. 
Now for $k_0, k_1 \in K$ define
\[ g_{k_0, k_1} := g_{k_1}^{-1} \circ g_{k_0} \in 
\gerbe{G}(U_{k_0, k_1})(i, j) . \]
Since $F(g_{k_0, k_1}) = 1$ we see that in fact
\[ g_{k_0, k_1} \in \mcal{N}(U_{k_0, k_1}) . \]
An easy calculation shows that the \v{C}ech $1$-cochain 
$\{ g_{k_0, k_1} \}_{k_0, k_1 \in K}$ is a cocycle. 
Since $\check{\mrm{H}}^1(U, \mcal{N}) = 1$, after possibly replacing
$\bsym{U}$ with a refinement, we can find a $0$-cochain
$\{ f_k \}_{k \in K}$ such that 
$g_{k_0, k_1} = f_{k_1}^{-1} \circ f_{k_0}$. 
Define
\[ g'_{k} := g_k \circ f_k^{-1} \in \gerbe{G}(U_{k})(i, j) . \]
Then the $0$-cochain $\{ g'_{k} \}_{k \in K}$ is a cocycle with values in the
sheaf of sets $\gerbe{G}(i, j)$. 
 From the sheaf property it follows that there is an element
$g' \in \gerbe{G}(U)(i, j)$ 
such that $g'|_{U_k} = g'_k$ for all $k$. We see that
$\gerbe{G}(U) \bigl( i, j \bigr) \neq \emptyset$.
\end{proof}

\begin{thm} \label{thm:10}
Consider the central extension of gerbes \tup{(\ref{eqn:9})}. If there are
enough $\mcal{N}$-acyclic open coverings, then the obstruction class
$\opn{cl}^2_F(j)$ from Definition \tup{\ref{dfn.4}} exists, for any
$j \in \opn{Ob} \gerbe{H}(X)$.
\end{thm}

\begin{proof}
Since the morphism of gerbes $F$ is locally surjective on objects, we
can find an open covering $\bsym{U} = \{ U_k \}_{k \in K}$ of $X$,
and objects $i_k \in \opn{Ob} \gerbe{G}(U_k)$ that lift
$j|_{U_k}$. By refining it we can assume that $\bsym{U}$ is
$\mcal{N}$-acyclic. According to Lemma \ref{lem.A.2} 
there exist elements $g_{k_0, k_1}$ that lift the elements 
$h_{k_0, k_1}$, in the notation of Construction \ref{const1}.
\end{proof}

Now suppose we are given a morphism of central extensions of gerbes
\begin{equation} \label{eqn:10}
\UseTips \xymatrix @C=5ex @R=5ex {
1 
\ar[r]
&
\mcal{N}
\ar[r]
\ar[d]
&
\gerbe{G}
\ar[r]^{F}
\ar[d]_{D}
& 
\gerbe{H}
\ar[r]
\ar[d]_{E}
& 
1
\\
1 
\ar[r]
&
\mcal{N}'
\ar[r]
&
\gerbe{G}'
\ar[r]^{F'}
& 
\gerbe{H}'
\ar[r]
& 
1
} 
\end{equation}
There is a  homomorphism of sheaves of abelian groups
$D : \mcal{N} \to \mcal{N}'$, and an induced homomorphism
\[ D : \check{\mrm{H}}^2(X, \mcal{N}) \to \check{\mrm{H}}^2(X, \mcal{N}') . \]

\begin{prop} \label{prop:7}
Consider the morphism of central extension of gerbes \tup{(\ref{eqn:10})}. 
\begin{enumerate}
\item Let $j \in \opn{Ob} \gerbe{H}(X)$ be such that
the obstruction class $\opn{cl}^2_F(j)$ is defined, and let 
$j' := E(j) \in \opn{Ob} \gerbe{H}'(X)$. 
Then the obstruction class $\opn{cl}^2_{F'}(j')$ is also defined, and moreover
\[ \opn{cl}^2_{F'}(j') = D \bigl( \opn{cl}^2_{F}(j) \bigr)  \]
in $\check{\mrm{H}}^2(X, \mcal{N}')$.

\item Let $i, j \in \opn{Ob} \gerbe{G}(X)$ and let
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
We write $i' := D(i)$ and $j' := D(j)$ for the corresponding objects of
$\gerbe{G}'(X)$, and
$h' := E(h)$ for the corresponding isomorphism $i' \to j'$. Then 
\[ \opn{cl}^1_{F'}(h') = D \bigl( \opn{cl}^1_{F}(h) \bigr)  \]
in $\check{\mrm{H}}^1(X, \mcal{N}')$.
\end{enumerate}
\end{prop}

\begin{proof}
Take the choices made in constructing the class
$\opn{cl}^2_{F}(j)$ or $\opn{cl}^1_{F}(h)$, as the case may be, and use the same
open covering, and the images under $D, F$ of the elements, to construct the
class $\opn{cl}^2_{F'}(j')$ or $\opn{cl}^1_{F'}(h')$.
\end{proof}

\begin{cor}
Consider the morphism of central extension of gerbes \tup{(\ref{eqn:10})}.
Assume that $E$ is an equivalence, and that there are enough  $\mcal{N}$-acyclic
open coverings. Then the obstruction class $\opn{cl}^2_{F'}(j')$ is defined for
any $j' \in \opn{Ob} \gerbe{H}'(X)$.
\end{cor}

\begin{proof}
There is some $j \in \opn{Ob} \gerbe{H}(X)$ such that
$\gerbe{H}'(X) \bigl( j', E(j) \bigr) \neq \emptyset$.
Now use Propositions \ref{prop:7}(1) and \ref{prop:10}.
\end{proof}
