---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-8
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
text_source: latex
latex_prose_ratio: 0.624
latex_coverage_ratio: 1.0
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






\section{Recalling some Facts on $2$-Categories}
\label{sec.recall}

There are several sources in the literature on $2$-categories and prestacks,
e.g.\ \cite{Be}, \cite{Gi}, \cite{Ma}, \cite{Mo}, \cite{Le}, \cite{KS}
and \cite{Br}. Unfortunately
there is disagreement on terminology among the sources, and hence we
feel it is
better to start with an exposition of the conventions we adopted, and a
recollection some facts. 

First we must establish some set-theoretical background, in order to
avoid paradoxical phenomena. Recall that in set theory all
mathematical objects and operations are interpreted as sets, with
suitable additional properties. Following \cite{Ma}
we fix a {\em Grothendieck universe} $\cat{U}$, which is a set closed
under standard set-theoretical operations, and large enough such
that the objects of interest for us (e.g.\ the topological space $X$ 
in Section \ref{sec:prest}) are elements of
$\cat{U}$. We refer to elements of $\cat{U}$ as {\em small sets}.
A category $\cat{C}$ such that
$\opn{Ob}(\cat{C}) \in \cat{U}$,
and 
$\opn{Hom}_{\cat{C}}(C_0, C_1) \in \cat{U}$
for every pair $C_0, C_1 \in \opn{Ob}(\cat{C})$,
is called a {\em small category}.

By $\cat{Set}$ we refer the category of small sets; thus in effect
$\opn{Ob}(\cat{Set}) = \cat{U}$.
Likewise $\cat{Grp}$, $\cat{Mod} A$ etc.\ refer to the categories of
small groups, small $A$-modules (over a small ring $A$) etc.\ 
A category $\cat{C}$ such that 
$\opn{Ob}(\cat{C}) \subset \cat{U}$,
and $\opn{Hom}_{\cat{C}}(C_0, C_1) \in \cat{U}$
for every pair $C_0, C_1 \in \opn{Ob}(\cat{C})$,
is called a $\cat{U}$-category.
Thus $\cat{Set}$ is a $\cat{U}$-category, but it is not small. 

Next we introduce a bigger universe $\cat{V}$, such that 
$\cat{U} \in \cat{V}$. Then 
$\opn{Ob}(\cat{Set}),$ \linebreak 
$\opn{Ob}(\cat{Grp}),\ldots \in \cat{V}$.
In order to distinguish between them, we call $\cat{U}$ the small
universe, and $\cat{V}$ is the large universe. 
The set of all $\cat{U}$-categories is denoted by
$\twocat{Cat}$. Note that 
$\twocat{Cat}$ is a $\cat{V}$-category, but (this is the whole
point!) it is not a $\cat{U}$-category.

By default sets, groups etc.\ will be assumed to be small; and
categories will be assumed to be $\cat{U}$-categories. 

A {\em $2$-category} $\twocat{C}$ is a ``category enriched in
categories''. (Some authors use the term ``strict $2$-category''.)
This means the following. There is a set $\opn{Ob} (\twocat{C})$, whose
elements are called {\em objects} of $\twocat{C}$. For any pair of objects
$\cat{C}_0, \cat{C}_1 \in \opn{Ob} (\twocat{C})$
there is a category 
$\twocat{C}(\cat{C}_0, \cat{C}_1)$.
The objects of the category $\twocat{C}(\cat{C}_0, \cat{C}_1)$
are called {\em $1$-morphisms}, and the morphisms of 
$\twocat{C}(\cat{C}_0, \cat{C}_1)$ are called {\em $2$-morphisms}.
For every triple 
$\cat{C}_0, \cat{C}_1, \cat{C}_2 \in \opn{Ob} (\twocat{C})$
there is a bifunctor
\[ \twocat{C}(\cat{C}_0, \cat{C}_1) \times
\twocat{C}(\cat{C}_1, \cat{C}_2) \to
\twocat{C}(\cat{C}_0, \cat{C}_2) , \]
called {\em horizontal composition}.
Horizontal composition has to be associative (as bifunctor).
For any $\cat{C} \in \opn{Ob} (\twocat{C})$ there is a distinguished
$1$-morphism
$\bsym{1}_{\cat{C}} \in \opn{Ob} \bigl( \twocat{C}(\cat{C}, \cat{C}) \bigr)$,
called the identity $1$-morphism of $\cat{C}$. Horizontal composition with
$\bsym{1}_{\cat{C}}$, on either side, is 
required to be the identity functor. 

Given a $1$-morphism 
$F \in \opn{Ob} \bigl( \twocat{C}(\cat{C}_0, \cat{C}_1) \bigr)$,
we write $F : \cat{C}_0 \to \cat{C}_1$. 
The notation for horizontal composition is $\circ$; so given
$1$-morphisms 
$F_1 : \cat{C}_0 \to \cat{C}_1$ and
$F_2 : \cat{C}_1 \to \cat{C}_2$, their composition is
$F_2 \circ F_1 : \cat{C}_0 \to \cat{C}_2$.
We sometimes denote the set 
$\opn{Ob} \bigl( \twocat{C}(\cat{C}_0, \cat{C}_1) \bigr)$
of $1$-morphisms $\cat{C}_0 \to \cat{C}_1$  by
$\opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1)$.

Let 
$F, G \in \opn{Ob} \bigl( \twocat{C}(\cat{C}_0, \cat{C}_1) \bigr)$,
and let
$\eta \in \opn{Hom}_{\twocat{C}(\cat{C}_0, \cat{C}_1)}(F, G)$;
i.e.\ $\eta$ is a $2$-morphism. We write 
$\eta: F \Rightarrow G$.
This data is usually depicted as a diagram:
\hide{ \[ \UseTips
\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[dd]_{\eta}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F}
\ar@(dr,dl)[rr]_{G}
& & \cat{C}_1
\\
& {}
} \] }
The composition rule in the category
$\twocat{C}(\cat{C}_0, \cat{C}_1)$
is called {\em vertical composition}, and we denote it by $*$.
Thus if $H \in \opn{Ob} \bigl( \twocat{C}(\cat{C}_0, \cat{C}_1) \bigr)$ 
is another $1$-morphism, and $\zeta : G \Rightarrow H$ is a
$2$-morphism, then
by vertical composition we get
$\zeta * \eta : F \Rightarrow H$.
\hide{ \[ \UseTips
\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[d]_{\eta}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F}
\ar[rr]^(0.7){G}
\ar@(dr,dl)[rr]_{H}
& \ar@{=>}[d]_{\zeta}
& \cat{C}_1
\\
& {}
} \qquad

\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[dd]_{\zeta * \eta}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F}
\ar@(dr,dl)[rr]_{H}
& & \cat{C}_1
\\
& {}
} \] }
Let us denote by $\bsym{1}_{F}$ the identity automorphism of the
object $F$ in
the category
$\twocat{C}(\cat{C}_0, \cat{C}_1)$.
Then $\bsym{1}_{F} * \eta = \eta = \eta * \bsym{1}_{G}$. 

The pictorial description of horizontal composition is this:
given a diagram 
\hide{ \[ \UseTips
\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[dd]_{\eta_1}
& & 
\ar@{=>}[dd]_{\eta_2}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F_1}
\ar@(dr,dl)[rr]_{G_1}
& & \cat{C}_1
\ar@(ur,ul)[rr]^{F_2}
\ar@(dr,dl)[rr]_{G_2}
& & \cat{C}_1
\\
& & & {}
} \] }
the horizontal composition of the $2$-morphisms $\eta_1$ and $\eta_2$ is
\hide{ \[ \UseTips
\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[dd]_{\eta_2 \circ \eta_1}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F_2 \circ F_1}
\ar@(dr,dl)[rr]_{G_2 \circ G_1}
& & \cat{C}_2
\\
& {}
} \] }

The horizontal and vertical compositions are required to satisfy the following
condition, called the {\em exchange condition}. Suppose we are
given a diagram 

\hide{ \[ \UseTips
\xymatrix  @C=5ex @R=1.5ex  {
& {}
\ar@{=>}[d]_{\eta_1}
& {}
& 
\ar@{=>}[d]_{\eta_2}
\\
\cat{C}_0
\ar@(ur,ul)[rr]^{F_1}
\ar[rr]^(0.7){G_1}
\ar@(dr,dl)[rr]_{H_1}
& \ar@{=>}[d]_{\zeta_1} 
& {}
\cat{C}_1
\ar@(ur,ul)[rr]^{F_2}
\ar[rr]^(0.7){G_2}
\ar@(dr,dl)[rr]_{H_2}
& \ar@{=>}[d]_{\zeta_2} 
& {}
\cat{C}_2
\\
& {}
& {}
& {}
} \] }
in $\twocat{C}$. Then 
\[ (\zeta_2 \circ \zeta_1) * (\eta_2 \circ \eta_1) = 
(\zeta_2 * \eta_2) \circ (\zeta_1 * \eta_1) \]
as $2$-morphisms 
$F_2 \circ F_1 \Rightarrow H_2 \circ H_1$.

Regarding set-theoretical issues, we require that 
$\opn{Ob}(\twocat{C}) \subset \cat{V}$,
$\opn{Ob} \bigl( \twocat{C}(\cat{C}_0, \cat{C}_1) \bigr) \in \cat{V}$,
and
$\opn{Hom}_{\twocat{C}(\cat{C}_0, \cat{C}_1)}(F, G) \in \cat{U}$.
Note that if we forget the $2$-morphisms in $\twocat{C}$, then
$\twocat{C}$ becomes a $\cat{V}$-category.

The basic example of a $2$-category is this:

\begin{exa} \label{exa.1} 
The $2$-category of $\cat{U}$-categories, denoted by $\bsym{\cat{Cat}}$.
The set $\opn{Ob} (\bsym{\cat{Cat}})$ of all $\cat{U}$-categories was already
mentioned. The $1$-morphisms in
$\bsym{\cat{Cat}}(\cat{C}_0, \cat{C}_1)$
are the functors $F : \cat{C}_0 \to \cat{C}_1$ between these categories.
And the $2$-morphisms $\eta : F \Rightarrow G$ are the natural
transformations. The composition rules are the usual ones.
\end{exa}

Here is another example, of a different flavor. 

\begin{exa}
Let $\K$ be a commutative ring. The category
$\cat{DGMod} \K$ of DG (differential graded) $\K$-modules can be made into a 
$2$-category, as follows. 
Given $M, N \in \opn{Ob} (\cat{DGMod} \K)$, the 
$1$-morphisms $F : M \to N$ are the usual morphisms in 
$\cat{DGMod} \K$, i.e.\ $\K$-linear DG module homomorphisms. 
Now such a homomorphism $F : M \to N$ can be viewed as a $0$-cocycle
in the DG module $\opn{Hom}_{\K}(M, N)$. Given another such homomorphism
$G : M \to N$, the $2$-morphisms $\eta : F \Rightarrow G$ are by definition 
the $0$-coboundaries $\eta \in \opn{Hom}_{\K}(M, N)$ such that 
$G = \eta + F$. Compositions are obvious.
\end{exa}

Suppose $F, G \in \opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1)$. We
say
that $F$ and $G$ are {\em $2$-isomorphic} if there is some
$2$-isomorphism
$\eta : F \twoiso G$ in the category 
$\opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1)$; 
we denote this by $F \twocong G$. 
A diagram (of $1$-morphisms)
\hide{ \[ \UseTips \xymatrix @C=5ex @R=5ex {
\cat{C}_0
\ar[r]^{D}
\ar[dr]_{F}
& 
\cat{C}_1
\ar[d]^{E}
\\
& 
\cat{C}_2
}  \] }
is {\em commutative up to $2$-isomorphism} if 
$E \circ D \twocong F$. 

There is an intrinsic notion of {\em equivalence} in a $2$-category
$\twocat{C}$.
A $1$-morphism $F : \cat{C} \to \cat{D}$ is an called an equivalence
if there
is a $1$-morphism $G : \cat{D} \to \cat{C}$
such that $G \circ F \twocong \bsym{1}_{\cat{C}}$ and 
$F \circ G \twocong \bsym{1}_{\cat{D}}$.
This generalizes the usual notion of equivalence (of categories) in
Example \ref{exa.1}.

Suppose $\twocat{C}$ and $\twocat{D}$ are $2$-categories. A 
{\em $2$-functor} $\twofun{F} : \twocat{C} \to \twocat{D}$
is a triple 
$\bsym{F} = (F_0, F_1, F_2)$, 
consisting of functions of the following kinds. The function $F_0$, 
called the $0$-component of $\twofun{F}$,
assigns to each object
$\cat{C} \in \opn{Ob} \twocat{C}$, an object
$F_0(\cat{C}) \in \opn{Ob} \twocat{D}$. 
The function $F_1$ assigns to each morphism
$G : \cat{C}_0 \to \cat{C}_1$ in $\twocat{C}$, a $1$-morphism
\[ F_1(G) : F_0 (\cat{C}_0) \to F_0 (\cat{C}_1)  \]
in $\twocat{D}$. And the function $F_2$  assigns to each $2$-morphism
$\eta : G \twoto G'$ in $\twocat{C}$, a $2$-morphism 
\[ F_2(\eta) : F_1(G) \twoto F_1(G') \]
in $\twocat{D}$. The condition is that the functions 
$(F_0, F_1,F_2)$ preserve compositions and units. Thus, if we forget
$2$-morphisms, the pair $(F_0, F_1)$ is a functor
\[ (F_0, F_1) : \twocat{C} \to \twocat{D} \]
between these categories. And for every 
$\cat{C}_0, \cat{C}_1 \in \opn{Ob} \twocat{C}$, 
the pair $(F_1, F_2)$ is a functor
\[ (F_1, F_2) : \opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1) \to 
\opn{Hom}_{\twocat{D}} \bigl( F_0(\cat{C}_0), F_0(\cat{C}_1) \bigr) .
\]

Let $\twocat{C}$ and $\twocat{D}$ be $2$-categories, and let
$\twofun{F}, \twofun{G} : \twocat{C} \to \twocat{D}$
be $2$-functors, with components 
\[ \twofun{F} = (F_0, F_1, F_2)\, , \, \twofun{G} = (G_0, G_1, G_2) . \]
A $1$-morphism (sometimes called a $2$-natural
transformation) 
$\twofun{p} : \twofun{F} \to \twofun{G}$ 
is a function that assigns to each $\cat{C} \in \opn{Ob} \twocat{C}$
a $1$-morphism 
\[ \twofun{p}_{\cat{C}} : F_0(\cat{C}) \to  G_0(\cat{C}) \]
in $\twocat{D}$, such that for every 
$E \in \opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1)$
one has
\[ \twofun{p}_{\cat{C}_1} \circ F_1(E) =
G_1(E) \circ \twofun{p}_{\cat{C}_0}  \]
in 
$\opn{Hom}_{\twocat{D}} \bigl( F_0(\cat{C}_0), G_0(\cat{C}_1) \bigr)$.
Given another $2$-functor $\twofun{H} : \twocat{C} \to \twocat{D}$, 
and a $1$-morphism 
$\twofun{q} : \twofun{G} \to \twofun{H}$, 
the composition 
$\twofun{q} \circ \twofun{p} : \twofun{F} \to \twofun{H}$
is defined in the obvious way.

Now suppose 
$\twofun{p}, \twofun{q} : \twofun{F} \to \twofun{G}$
are $1$-morphisms between $2$-functors
$\twofun{F} , \twofun{G} : \twocat{C} \to \twocat{D}$ as above.
A $2$-morphism $\twofun{\eta} : \twofun{p} \to \twofun{q}$
(sometimes called a modification) is a function that assigns to each 
$\cat{C} \in \opn{Ob} \twocat{C}$, a $2$-morphism
$\twofun{\eta}_{\cat{C}} : \twofun{p}_{\cat{C}} \twoto
\twofun{q}_{\cat{C}}$
in 
$\opn{Hom}_{\twocat{D}} \bigl( F_0(\cat{C}), G_0(\cat{C}) \bigr)$.
The condition is that 
\[ \twofun{\eta}_{\cat{C}_1} \circ \twofun{p}_{\cat{C}_1} \circ
\twofun{F} = 
\twofun{\eta}_{\cat{C}_0} \circ \twofun{q}_{\cat{C}_0} \circ
\twofun{G} , \]
as functions
\[ \opn{Hom}_{\twocat{C}}(\cat{C}_0, \cat{C}_1)  \to 
\opn{Hom}_{\twocat{D}} \bigl( F_0(\cat{C}_0), G_0(\cat{C}_1) \bigr) .
\]
If $\twofun{r} : \twofun{F} \to \twofun{G}$
is yet another $1$-morphism, and 
$\twofun{\zeta} : \twofun{q} \to \twofun{r}$
is a $2$-morphism, then the composition 
$\twofun{\zeta} * \twofun{\eta} : \twofun{p} \to \twofun{r}$ is
defined in the obvious
way. We say that the $2$-morphism 
$\twofun{\eta} : \twofun{p} \to \twofun{q}$
is a $2$-isomorphism if each $\twofun{\eta}_{\cat{C}}$ is a
$2$-isomorphism. 

A $2$-functor $\twofun{F} : \twocat{C} \to \twocat{D}$ 
is called a {\em $2$-equivalence} if there is a $2$-functor
$\twofun{G} : \twocat{D} \to \twocat{C}$, and $2$-isomorphisms
$\twofun{G} \circ \twofun{F} \twoiso \twofun{1}_{\twocat{C}}$
and 
$\twofun{F} \circ \twofun{G} \twoiso \twofun{1}_{\twocat{D}}$.
If a $2$-equivalence $\twocat{C} \to \twocat{D}$ exists, then we say
that $\twocat{C}$ and $\twocat{D}$ are $2$-equivalent.

One could make the set of all $2$-categories, with the operations defined above,
into a $2$-category, but that would take us outside of the large universe
$\cat{V}$. Therefore we shall be careful to consider only ``small collections''
of $2$-categories in this paper.

We shall also need to recall what are {\em pseudofunctors}
(sometimes called normalized pseudofunctors, or morphisms of
bicategories) from a category 
$\cat{N}$ to a $2$-category $\twocat{C}$.
A pseudofunctor $\bsym{F} : \cat{N} \to \twocat{C}$
is a triple $\bsym{F} = (F_0, F_1, F_2)$, consisting of functions of
the following kinds. 
The function $F_0$, called the $0$-component of $\bsym{F}$, assigns to
each object 
$N \in \opn{Ob} \cat{N}$ an object $F_0 (N) \in \opn{Ob} \twocat{C}$.
The function $F_1$ assigns to each morphism
$f : N_0 \to N_1$ in $\cat{N}$ a $1$-morphism
\[ F_1(f) : F_0 (N_0) \to F_0 (N_1)  \]
in $\twocat{C}$.
And the function $F_2$  assigns to each composable pair of morphisms
\[ N_0 \xar{f_1} N_1 \xar{f_2} N_2 \] 
in $\cat{N}$, a $2$-isomorphism
\[ F_2(f_1, f_2) : F_1(f_2) \circ F_1(f_1) \twoiso F_1(f_2 \circ f_1) 
\]
in $\twocat{C}$.
Here are the conditions. First, 
\begin{equation} \label{eqn:12}
F_2(f_2 \circ f_1, f_3) * F_2(f_1, f_2)  = 
F_2(f_1, f_3 \circ f_2) * F_2(f_2 , f_3) 
\end{equation}
for any composable triple 
\[ N_0 \xar{f_1} N_1 \xar{f_2} N_2 \xar{f_3} N_3 \]
of morphisms in $\cat{N}$.
Next, for any object $N \in \cat{N}$, with identity morphism 
$\bsym{1}_N$, it is required that
$F_1(\bsym{1}_N) = \bsym{1}_{F_0(N)}$, the identity $1$-morphism of
$F_0(N)$.
And lastly, the $2$-isomorphisms 
\[ F_2( \bsym{1}_{N_0}, f_1 ) : F_1(f_1) \circ \bsym{1}_{F_0(N_0)}
\twoiso
F_1(f_1) \]
and
\[ F_2( f_1, \bsym{1}_{N_1} ) : \bsym{1}_{F_0(N_1)} \circ F_1(f_1)
\twoiso
F_1(f_1) \]
have to be the identity $2$-automorphism of the $1$-morphism
$F_1(f_1)$.

The final abstract $2$-categorical fact that we need is that given a small
category $\cat{N}$ and a $2$-category $\twocat{C}$, the set
of all pseudofunctors $\bsym{F} : \cat{N} \to \twocat{C}$
is itself a $2$-category. The $1$-morphisms are defined as follows. 
Suppose $\bsym{F}, \bsym{G} : \cat{N} \to \twocat{C}$ are
pseudofunctors, with
components $\bsym{F} = (F_0, F_1, F_2)$ and $\bsym{G} = (G_0, G_1,
G_2)$. 
A $1$-morphism 
$\bsym{p} : \bsym{F} \to \bsym{G}$ is a pair 
$\bsym{p} = (p_1, p_2)$, whose $1$-component $p_1$ is a function
assigning
to any object $N \in \opn{Ob} \cat{N}$ a $1$-morphism 
\[ p_1(N) : F_0(N) \to G_0(N) \]
in $\twocat{C}$; and the $2$-component $p_2$ is a function assigning
to any
morphism $f : N_0 \to N_1$ in $\cat{N}$ a $2$-isomorphism
\[ p_2(f) : p_1(N_1) \circ F_1(f) \twoiso G_1(f) \circ p_1(N_0) \]
in $\twocat{C}$.
These are required to satisfy
the condition
\begin{equation} \label{eqn:8}
p_2(f_2 * f_1) * F_2(f_1, f_2) = 
G_2(f_1, f_2) * p_2(f_1) * p_2(f_2) 
\end{equation}
in $\opn{Hom}_{\twocat{C}} \bigl( F_0(N_0), G_0(N_1) \bigr)$,
for any composable pair of morphisms
$N_0 \xar{f_1} N_1 \xar{f_2} N_2$ in $\cat{N}$.

Horizontal composition of $1$-morphisms is defined as follows. Suppose
$\bsym{H} : \cat{N} \to \twocat{C}$ is another pseudofunctor, and
$\bsym{q} : \bsym{G} \to \bsym{H}$ is a $1$-morphism.
Their components are $\bsym{H} = (H_0, H_1, H_2)$ and
$\bsym{q}=  (q_1, q_2)$. 
Let
\[ r_1(N) : F_0(N) \to H_0(N) \]
be the $1$-morphism
\[ r_1(N) := q_1(N) \circ p_1(N) , \]
and let 
\[ r_2(f) : r_1(N_1) \circ F_1(f) \twoto
H_1(f) \circ r_1(N_0) \]
be the $2$-morphism
\[ r_2(f) := q_2(f) * p_2(f) . \]
Then we define the $1$-morphism
\[ \bsym{q} \circ \bsym{p} : \bsym{F} \to \bsym{H} \]
to be
\[ \bsym{q} \circ \bsym{p} := (r_1, r_2) . \]

Next consider $1$-morphisms 
$\bsym{p}, \bsym{q} : \bsym{F} \to \bsym{G}$.
A $2$-morphism $\bsym{\eta} : \bsym{p} \twoto \bsym{q}$ 
has only a $2$-component $\eta_2$, which is a function that
assigns to
each object $N \in \opn{Ob} \cat{N}$ a $2$-morphism
\[ \eta_2(N) : p_1(N) \twoto q_1(N) \]
in $\twocat{C}$. The condition is that
\[ q_2(f) * \eta_2(N_0) = \eta_2(N_1) * p_2(f) \]
for any $f : N_0 \to N_1$ in $\cat{N}$.
Given yet another $1$-morphism $\bsym{r} : \bsym{F} \to \bsym{G}$,
and a $2$-morphism $\bsym{\zeta} = (\zeta_2) : \bsym{q} \twoto \bsym{r}$, the
vertical composition 
$\bsym{\theta} := \bsym{\zeta} * \bsym{\eta} : \bsym{p} \twoto \bsym{r}$ 
has $2$-component
\[ \theta_2(N) := \zeta_2(N) * \eta_2(N) . \]
