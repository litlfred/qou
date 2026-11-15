---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-3
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.906
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
\label{sec.Int}

A {\em gerbe} $\gerbe{G}$ on a topological space $X$ is the geometric
version of a connected nonempty groupoid. Thus $\gerbe{G}$
associates a groupoid $\gerbe{G}(U)$ to any open set $U \subset X$,
and to any inclusion $V \subset U$
of open sets there is a restriction functor
$\gerbe{G}(U) \to \gerbe{G}(V)$.
These have to satisfy a lot of conditions (for the benefit of the reader we
have included a review in Section \ref{sec:prest}).
Gerbes arise in various contexts; but
for us the are mainly important as ``bookkeeping devices'' for certain
geometric data. At the end of the introduction we will outline the main
application we have in mind. 

A key question is to determine if a given gerbe $\gerbe{G}$ is
{\em trivial}, namely if $\opn{Ob} \gerbe{G}(X) \neq \emptyset$.
When $\gerbe{G}$ is {\em abelian}, with band some sheaf $\mcal{N}$
of abelian groups, there is an obstruction class in the \v{C}ech cohomology
group $\check{\mrm{H}}^2(X, \mcal{N})$ that vanishes if and only if  $\gerbe{G}$
is trivial. However for a {\em nonabelian} gerbe $\gerbe{G}$ there is no
useful obstruction theory, since the structure is too complicated.
There is Giraud's nonabelian cohomology theory \cite{Gi}, but that
does not provide an effective answer. 

We noticed during our work on deformation quantization that the
gerbes occurring there are {\em pronilpotent} (see explanation
below). Such gerbes are composed of central extensions, and for
those extensions we can construct useful obstruction classes. 

A {\em central extension of gerbes} on $X$ is a diagram
\begin{equation} \label{eqn:14}
1 \to  \mcal{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 , 
\end{equation}
in which $\gerbe{G}$ and $\gerbe{H}$ are gerbes,  
$F : \gerbe{G} \to \gerbe{H}$ is a weak epimorphism of gerbes, and
$\mcal{N} = \opn{Ker}(F)$ is a sheaf of abelian groups in the center of 
$\gerbe{G}$.
This notion is technically quite complicated (see Definition \ref{dfn:2}), but
in principle it is just a generalization of the notion of central extension of
sheaves of groups
\begin{equation} \label{eqn:26}
1 \to \mcal{N} \to \mcal{G} \to \mcal{H} \to 1 .
\end{equation}

Consider a central extension of gerbes (\ref{eqn:14}). Suppose 
$i, j$ are two objects of $\gerbe{G}(X)$, and 
$h : F(i) \to F(j)$ is an isomorphism if $\gerbe{H}(X)$. 
Then there is obstruction class
\[ \opn{cl}^1_F(h) \in \check{\mrm{H}}^1(X, \mcal{N}) . \]
The first main result of the paper, Theorem \ref{thm.3}, says that 
$\opn{cl}^1_F(h)$ vanishes if and only if $h$ can be lifted to an
isomorphism $g : i \to j$ in $\gerbe{G}(X)$.

Given an object $j$ of $\gerbe{H}(X)$, 
we define (under some hypothesis) an obstruction class
\[ \opn{cl}^2_F(j) \in \check{\mrm{H}}^2(X, \mcal{N}) . \]
The second main result of the paper, Theorem \ref{thm.2}, says that $j$
lifts to an object of $\gerbe{G}(X)$ if and only if 
$\opn{cl}^2_F(j) = 1$. 

There are three typical situations where central extensions of gerbes occur.
The first is when we are given a central extension of sheaves of groups 
(\ref{eqn:26}). This is discussed briefly in Example \ref{exa:27}.

Another situation is when we take any gerbe $\gerbe{G}$, and look at 
$\mcal{N} := \mrm{Z}(\gerbe{G})$, the center of $\gerbe{G}$, which
is a sheaf of abelian groups. We get a central extension
\[ 1 \to  \mrm{Z}(\gerbe{G}) \to \gerbe{G} \xar{F} 
\gerbe{G} / \mrm{Z}(\gerbe{G}) \to 1 . \]
Global objects of $\gerbe{G} / \mrm{Z}(\gerbe{G})$ are called
{\em fake global objects of $\gerbe{G}$}. See Section \ref{sec.fake}. 

The third situation, which is the most important for us, is when the
gerbe $\gerbe{G}$ is pronilpotent,
i.e.\ it is complete with respect to a central filtration
$\{ \gerbe{N}_p \}_{p \in \mbb{N}}$
(see Definition \ref{dfn.12}). 
Then for any $p$ there is a central extension of gerbes
\[ 1 \to \gerbe{N}_p / \gerbe{N}_{p+1}
\to \gerbe{G} / \gerbe{N}_{p+1} \to
\gerbe{G} / \gerbe{N}_p \to 1 . \]
The obstruction classes can detect whether the groupoid
$(\gerbe{G} / \gerbe{N}_p)(X)$ is nonempty or connected
for any $p$; but passing to the limit is more delicate. This is done in the
third main result of the paper, namely Theorem \ref{thm.4}. 

Presumably our results can be extended, with minor changes, to sites
other than a topological space (e.g.\ the \'etale site of a scheme).
But we did not explore this direction. 

Here is an outline of the role gerbes have in our paper \cite{Ye}. 
Suppose $X$ is a smooth algebraic variety over a
field $\K$ of characteristic $0$. We are interested in {\em twisted
deformations} of $\mcal{O}_X$. A twisted (associative or
Poisson) deformation $\gerbe{A}$ is a collection of locally defined 
(associative or Poisson) deformations $\mcal{A}_i$ of $\mcal{O}_X$, together
with a collection of locally defined gauge equivalences 
$\mcal{A}_i \iso \mcal{A}_j$ between them. The bookkeeping data of
deformations and gauge equivalences are encoded in the {\em gauge gerbe} 
$\gerbe{G}$ of $\gerbe{A}$. Here is just a hint of how this goes --
see Remark \ref{rem.1} for a few more details, or the paper \cite{Ye} for the
full story. Let $U \subset X$ be an open set. 
Then to any object $i$ in the groupoid $\gerbe{G}(U)$ we
attach a deformation 
$\mcal{A}_i$ of $\mcal{O}_{U}$; and to any morphism 
$g : i \to j$ in $\gerbe{G}(U)$ we attach a gauge equivalence
$\gerbe{A}(g) : \mcal{A}_i \iso \mcal{A}_j$.
Thus the groupoid $\gerbe{G}(X)$ carries the
information of global deformations: objects of 
$\gerbe{G}(X)$ correspond to global deformations of $\mcal{O}_X$
belonging to $\gerbe{A}$, and isomorphic objects correspond to gauge
equivalent deformations. Since the gauge gerbe $\gerbe{G}$ is 
pronilpotent, we can often use Theorems \ref{thm.3}, \ref{thm.2} and
\ref{thm.4} to figure out how many connected components the
groupoid $\gerbe{G}(X)$ has.

\medskip \noindent
\textbf{Acknowledgments.}
Work on this paper began together with Fredrick Leitner, and I wish to thank
him for his contributions, without which the paper could not have been written. 
Thanks also to Lawrence Breen for reading an early version of the
paper and offering valuable suggestions. Finally I wish to thank the referee
for his/her input, and especially for discovering a subtle error in one of the
main results, as it was stated in a previous version of the paper.
