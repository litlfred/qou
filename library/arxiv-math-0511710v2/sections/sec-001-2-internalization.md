---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-001-2-internalization
section_title: "Internalization"
section_number: 2
pages: 8-13
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.985
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of point particles using connections on bundles, higher gauge theory describes the parallel transport of 1-dimensional"
---
\label{section: Internalization}

The idea of internalization is simple: given a mathematical concept $X$ 
defined solely in terms of sets, functions and commutative diagrams 
involving these, and given some category $K$, one obtains the concept of 
an `$X$ in $K$' by replacing all these sets, functions and commutative
diagrams by corresponding objects, morphisms, and commutative diagrams
in $K$.  

The case we need here is when $X$ is the concept of `category':

\begin{definition} \et 
Let $K$ be a category.  
An {\bf internal category in} $K$, or simply
{\bf category in} $K$, say $C$, consists of: 
\begin{itemize}
\item an object $\Ob(C) \in K$,
\item an object $\Mor(C) \in K$,
\item {\bf source} and {\bf target} morphisms
$s,t \maps \Mor(C) \to \Ob(C)$,
\item an {\bf identity-assigning} morphism
$\id \maps \Ob(C) \to \Mor(C)$,
\item a {\bf composition} morphism
$\circ \maps \Mor(C) {{}_{s}\times_{t}} 
\Mor(C) \to \Mor(C)$
\end{itemize}
satisfying the usual rules of a category expressed in terms of commutative
diagrams.
\end{definition}

\noindent Here $\Mor(C) {{}_{s}\times_{t}} \Mor(C)$ is defined using a
pullback: if $K$ is the category of sets, it is the set of composable
pairs of morphisms in $C$.  Inherent in the definition is the
assumption that this pullback exist, along with the other pullbacks
needed to write the rules of a category as commutative diagrams.

We can similarly define a {\bf functor in} $K$ and a {\bf natural
transformation in} $K$; details can be found in Borceux's handbook
\cite{Borceux}.  There is a 2-category $K\Cat$ whose objects,
morphisms and 2-morphisms are categories, functors and natural
transformations in $K$.  To study \emph{symmetries} in higher
gauge theory, we need these examples:

\begin{definition} \et
\label{Lie 2-group}
Let $\Lie\Grp$ be the category whose objects are Lie groups and whose 
morphisms are Lie group homomorphisms.   Then the objects, morphisms
and 2-morphisms of $\Lie\Grp\Cat$ are called {\bf Lie 2-groups}, 
{\bf Lie 2-group homomorphisms}, and {\bf Lie 2-group 
2-homomorphisms}, respectively.
\end{definition}

\begin{definition} \et
\label{Lie 2-algebra}
Let $\Lie\Alg$ be the category whose objects are Lie algebras and whose 
morphisms are Lie algebra homomorphisms.   Then the objects, morphisms
and 2-morphisms of $\Lie\Alg\Cat$ are called {\bf Lie 2-algebras}, 
{\bf Lie 2-algebra homomorphisms}, and {\bf Lie 2-algebra 
2-homomorphisms}, respectively.
\end{definition}

\noindent
For the benefit of experts, we should admit that we are only
defining `strict' Lie 2-groups and Lie 2-algebras, where all the usual
laws hold as equations.  We rarely need any other kind in this paper, 
but there are more general Lie 2-groups and Lie 2-algebras
where the usual laws hold only up to isomorphism 
\cite{BaezLauda:2003,BaezCrans:2003}.

We could also consider categories in $\Diff$, the category whose objects 
are finite-dimensional smooth manifolds and whose morphisms are smooth maps.  
Ehresmann \cite{Ehresmann:1959} introduced these in the late 1950's
under the name of `differentiable categories'.  However, these 
are not quite what we want here, for two reasons.  First, unlike $\Lie\Grp$ 
and $\Lie\Alg$, $\Diff$ does not have pullbacks in general.   This means
that when we try to define a category in $\Diff$, the set 
of composable pairs of morphisms is not automatically a smooth manifold.
Second, the space of smooth paths in a smooth manifold is not again a 
smooth manifold.  This is an annoyance when studying connections on
bundles.  

To solve these problems, we want a category of `smooth spaces' that has
pullbacks and includes path spaces.  Various categories of this sort 
have been proposed.  It is unclear which one is best, but we shall 
use the last of several variants proposed by Chen \cite{Chen:1977,Chen:1982}.  
In what follows, we use {\bf convex set} to mean a convex subset of 
$\R^n$, where $n$ is arbitrary (not fixed).  Any convex set inherits
a topology from its inclusion in $\R^n$.  We say a map $f$ 
between convex sets is {\bf smooth} if arbitrarily high derivatives 
of $f$ exist and are continuous, using the usual definition
of derivative as a limit of a quotient.   

\begin{definition} \et
\label{smooth_space} 
A {\bf smooth space} is a set $X$ equipped with, for 
each convex set $C$, a collection of functions 
$\phi \maps C \to X$ called {\bf plots} in $X$, such that:
\begin{enumerate} 
\item 
If $\phi \maps C \to X$ is a plot in $X$, 
and $f \maps C' \to C$ is a smooth map between convex sets, 
then $\phi \circ f$ is a plot in $X$,
\item
If $i_\alpha \maps C_\alpha \to C$ is an open cover of a convex
set $C$ by convex subsets $C_\alpha$,
and $\phi \maps C \to X$ has the property that $\phi \circ i_\alpha$ 
is a plot in $X$ for all $\alpha$, then $\phi$ is a plot in $X$.
\item 
Every map from a point to $X$ is a plot in $X$.
\end{enumerate}
\end{definition}

\begin{definition} \et
\label{smooth_map} 
A {\bf smooth map} from the smooth space $X$ to the smooth
space $Y$ is a map $f \maps X \to Y$ such that for every
plot $\phi$ in $X$, $\phi \circ f$ is a plot in $Y$.
\end{definition}

\noindent
In highbrow lingo, this says that smooth spaces are sheaves
on the category whose objects are convex sets and whose morphisms are
smooth maps, equipped with the Grothendieck topology where a cover
is an open cover in the usual sense.  However, smooth spaces are
not arbitrary sheaves of this sort, but precisely those 
for which two plots with domain $C$ agree whenever they agree
when pulled back along every smooth map from a point to $C$.

Using this, it is straightforward to check that there is a category 
${\rm C}^\infty$ whose objects are smooth spaces and whose morphisms
are smooth maps.  Moreover this category is cartesian closed, and 
it has arbitrary limits and colimits.  It also has other nice properties:

\begin{itemize}
\item  Every finite-dimensional smooth manifold (possibly with
boundary) is a smooth space;
smooth maps between these are precisely those
that are smooth in the usual sense.
\item  Every smooth space can be given the strongest topology in which
all plots are continuous; smooth maps
are then automatically continuous.
\item  Every subset of a smooth space is a smooth space.
\item  We can form a quotient of a smooth space $X$ by any
equivalence relation, and the result is again a smooth space.  
\item  We can define vector fields and differential forms on smooth 
spaces, with many of the usual properties.
\end{itemize}

With the notion of smooth space in hand, we can make the following
definitions:

\begin{definition} \et
\label{smooth 2-space}
Let ${\rm C}^\infty$ be the category whose objects are 
smooth spaces and whose morphisms are smooth maps.   Then the objects, 
morphisms and 2-morphisms of ${\rm C}^\infty\Cat$ are called 
{\bf smooth 2-spaces}, {\bf smooth maps}, and {\bf smooth 2-maps}, 
respectively.
\end{definition}

Writing down the above definitions is quick and easy.  It takes 
longer to understand them and apply them to higher gauge theory.
For this we must unpack them and look at examples.   

To get examples of Lie 2-groups, we can use `Lie crossed modules'.  
A {\bf Lie crossed module} is a quadruple $(G,H,t,\alpha)$ 
where $G$ and $H$ are Lie 
groups, $t \maps H \to G$ is a Lie group homomorphism and 
$\alpha$ is a smooth action of $G$ as automorphisms of $H$ such
that $t$ is equivariant:
\[   t(\alpha(g)(h)) = g \, t(h)\, g^{-1} \]
and satisfies the so-called `Peiffer identity':
\[    \alpha(t(h))(h') = hh'h^{-1} . \]
We obtain a Lie crossed module from a Lie 2-group $\twogroup$ as
follows:
\begin{itemize}
\item $G$ is the Lie group of objects of $\G$, $\Ob(\twogroup)$,
\item $H$ is the subgroup of $\Mor(\twogroup)$ consisting
of morphisms with source equal to $1 \in G$:
\item $t \maps H \to G$ is the homomorphism sending each 
morphism in $H$ to its target,
\item $\alpha$ is the action of $G$ as automorphisms of $H$ 
defined using conjugation in $\Mor(\twogroup)$ as follows: 
$\alpha(g) h = 1_g h {1_g}^{-1}$. 
\end{itemize}
Conversely, we can reconstruct any Lie 2-group from its Lie 
crossed module.  In fact, the 2-category of Lie 2-groups is 
biequivalent to that of Lie crossed modules \cite{BaezLauda:2003}.
This gives various examples:

\begin{example} \et
\label{crossed.1} 
{\rm 
Given any abelian group $H$, there is a Lie crossed module
where $G$ is the trivial group and $t, \alpha$ are trivial.  
This gives a Lie 2-group $\twogroup$ with one object
and $H$ as the group of morphisms.  Lie 2-groups of this
sort are important in the theory of \emph{abelian} gerbes.
}\end{example}

\begin{example} \et
\label{crossed.2} 
{\rm
Given any Lie group $H$, there is a Lie
crossed module with $G = \Aut(H)$, $t \maps H \to G$ the homomorphism
assigning to each element of $H$ the corresponding inner automorphism,
and the obvious action of $G$ as automorphisms of $H$.  We call the
corresponding Lie 2-group the {\bf automorphism 2-group} of $H$, and
denote it by $\AUT(H)$.   This sort of 2-group is important in the theory 
of \emph{nonabelian} gerbes.  

We use the term `automorphism 2-group' because $\AUT(H)$ really is the
2-group of symmetries of $H$.  Lie groups form a 2-category, any object
in a 2-category has a 2-group of symmetries, and the 2-group of 
symmetries of $H$ is naturally a Lie 2-group, which is none other than
$\AUT(H)$.  See \cite{BaezLauda:2003} for details.
}\end{example}

\begin{example} \et 
\label{crossed.3} 
{\rm 
Suppose that $1 \to A \hookrightarrow H \stackto{t} G \to 1$ is a central
extension of the Lie group $G$ by the Lie group $H$.  Then there is
a Lie crossed module with this choice of $t \maps H \to G$.  To construct
$\alpha$ we pick any section $s$, that is, any function
$s \maps G \to H$ with $t(s(g)) = g$, and define 
\[      \alpha(g) h = s(g) h s(g)^{-1}  .\]
Since $A$ lies in the center of $H$, $\alpha$ independent of the choice of
$s$.  We do not need a global smooth section $s$ to show $\alpha(g)$ depends 
smoothly on $g$; it suffices that there exist a local smooth section in a
neighborhood of each $g \in G$.

It is easy to generalize this idea to infinite-dimensional cases
if we work not with Lie groups
but {\bf smooth groups}: that is, groups in the category of smooth spaces.  
The basic theory of smooth groups, smooth 2-groups and smooth crossed 
modules works just like the finite-dimensional case, but with the category 
of smooth spaces replacing $\Diff$.  In particular, every smooth group 
$G$ has a Lie algebra $\g$.  

Given a connected and simply-connected compact simple Lie 
group $G$, the loop group $\Omega G$ is a smooth group. 
For each `level' $k \in \Z$, this group has a central extension
\[           1 \to \U(1) \hookrightarrow 
\widehat{\Omega_k G} \stackto{t} \Omega G \to 1   \]
as explained by Pressley and Segal \cite{PressleySegal:1986}.  The above 
diagram lives in the category of smooth groups, and there 
exist local smooth sections for $t \maps \widehat{\Omega_k G} \to \Omega G$, 
so we obtain a smooth crossed module $(\Omega G, \widehat{\Omega_k G}, 
t,\alpha)$ with $\alpha$ given as above.  This in turn gives an
smooth 2-group which we call the \textbf{level-\textit{k} 
loop 2-group} of $G$, ${\cal L}_k G$.

It has recently been shown \cite{BCSS}
that ${\cal L}_k G$ fits into an exact sequence of smooth 2-groups:
\[           1 \to {\cal L}_k G \hookrightarrow 
{\cal P}_k G \stackto{} G \to 1   \]
where the middle term, the \textbf{level-\textit{k} path 2-group} 
of $G$, has very interesting properties.  In particular, when $k = \pm 1$,
the geometric realization of the nerve of ${\cal P}_k G$ is a topological 
group that can also be obtained by killing the 3rd homotopy group of $G$.
When $G = {\rm Spin}(n)$, this topological group goes by the name of
${\rm String}(n)$, since it plays a role in defining spinors on loop
space \cite{Witten:1988}.  The group ${\rm String}(n)$ also shows up in 
Stolz and Teichner's work on elliptic cohomology, which involves a 
notion of parallel transport over surfaces \cite{StolzTeichner}.  
So, we expect that ${\cal P}_k G$ will be an especially interesting 
structure 2-group for applications of 2-bundles to string theory.

To define the holonomy of a connection, we need smooth groups with 
an extra property: namely, that for every smooth function 
$f \maps [0,1] \to \g$ there is a unique smooth function 
$g \maps [0,1] \to G$ solving the differential equation
\[       {d\over dt}g(t) = f(t)g(t)  \]
with $g(0) = 1$.  We call such smooth groups {\bf exponentiable}.
Similarly, we call a smooth 2-group $\twogroup$ {\bf exponentiable} 
if its crossed module $(G,H,t,\alpha)$ has both $G$ and $H$ 
exponentiable.  In particular, every Lie group and thus every
Lie 2-group is exponentiable.  The smooth groups $\Omega G$
and $\widehat{\Omega_k G}$ are also exponentiable, as are the 
2-groups ${\cal L}_k G$ and ${\cal P}_k G$.  So, for the convenience
of stating theorems in a simple way, {\it we henceforth implicitly
assume all smooth groups and 2-groups under discussion are exponentiable}.
We only really need this in Theorems \ref{central proposition concerning
connections} and \ref{central proposition concerning 2-connections}.
}\end{example}

Finally, here are some easy examples of smooth 2-spaces:

\begin{example} \et 
\label{2space.1}
{\rm 
Any smooth space can be seen as a 
smooth 2-space with only identity morphisms.
}
\end{example}

\begin{example} \et 
\label{2space.2} 
{\rm 
Any smooth group (for example a Lie group) can be seen as
a smooth 2-space with only one object.
}
\end{example}

\begin{example} \et \label{2space.3}
{\rm 
Given a smooth space $M$, there is a smooth 2-space $\P_1(M)$,
the {\bf path groupoid of $M$}, such that:
\begin{itemize}
\item the objects of $\P_1(M)$ are points of $M$,
\item the morphisms of $\P_1(M)$ are thin homotopy classes of smooth paths
$\gamma \maps [0,1] \to M$ such that $\gamma(s)$ is constant near $s = 0$
and $s = 1$.
\end{itemize}
Here a {\bf thin homotopy} between smooth paths $\gamma_1, \gamma_2
\maps [0,1] \to M$ is a smooth map $H \maps [0,1]^2 \to M$ such that:
\begin{itemize}
\item 
$H(s,0) = \gamma_1(s)$ and 
$H(s,1) = \gamma_2(s)$, 
\item
$H(s,t)$ is independent of $t$ near $t = 0$ and near $t = 1$, 
\item
$H(s,t)$ is constant near $s = 0$ and near $s = 1$,
\item
the rank of the differential $dH(s,t)$ is $< 2$ for all $s,t \in
[0,1]$. 
\end{itemize}
The last condition is what makes the homotopy `thin': it guarantees
that the homotopy sweeps out a surface of vanishing area.  

To see how $\P_1(M)$ becomes a 2-space, first note that
the space of smooth maps $\gamma \maps [0,1] \to M$ becomes a
smooth space in a natural way, as does the subspace satisfying
the constancy conditions near $t = 0,1$, and finally the quotient
of this subspace by the thin homotopy relation.  
This guarantees that $\Mor(\P_1(M))$ is a smooth space.  Clearly
$\Ob(\P_1(M)) = M$ is a smooth space as well.  One can check that
$\P_1(M)$ becomes a smooth 2-space with usual composition of paths
giving the composition of morphisms.

In fact, $\P_1(M)$ is not just a smooth 2-space: it is also a groupoid.
The inverse of $[\gamma]$ is just $[\overline{\gamma}]$, 
where $\overline{\gamma}$ is obtained by reversing the orientation 
of the path $\gamma$:
\[        \overline{\gamma}(s) = \gamma(1 - s)  .\]
Moreover, the map sending any morphism to its inverse is 
smooth.  Thus $\P_1(M)$ is a {\bf smooth groupoid}: a 2-space
where every morphism is invertible and the map sending every morphism
to its inverse is smooth.  
}\end{example}
