---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-001-2-categories-and-connections
section_title: "Categories and Connections"
section_number: 2
pages: 3-11
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.998
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{connections}

A category consists of objects, which we draw as dots:
\[ \bullet \,\, x \]
and morphisms between objects, which we draw as arrows between dots:
\[
\xymatrix{
   x \bullet \ar@/^1pc/[rr]^{f}
&& \bullet y
}
\]
You should think of objects as `things' and morphisms as
`processes'.  The main thing you can do in a category is 
take a morphism from $x$ to $y$ and a morphism from $y$ to $z$:
\[
\xymatrix{
   x \bullet \ar@/^1pc/[rr]^{f}
&& \bullet y \ar@/^1pc/[rr]^{g}
    && \bullet z
}
\]
and `compose' them to get a morphism from $x$ to $z$:
\[
\xymatrix{
   x \bullet \ar@/^2pc/[rrrr]^{gf}
&&&& \bullet z
}
\]

The most famous example is the category $\Set$, which has sets as
objects and functions as morphisms.  Most of us know how to compose
functions, and we have a pretty good intuition of how this works.  So,
it can be helpful to think of morphisms as being like functions.  But
as we shall soon see, there are some very important categories where the
morphisms are \emph{not} functions.

Let us give the formal definition.  A \define{category} consists of:
\begin{itemize} 
\item A collection of \define{objects}, and
\item for any pair of objects $x,y$, a set of \define{morphisms}
$f \maps x \to y$.   Given a morphism $f \maps x \to y$,
we call $x$ its \define{source} and $y$ its \define{target}.
\item Given two morphisms $f \maps x \to y$ and $g \maps y \to z$, 
there is a \define{composite} morphism $gf \maps x \to z$.  Composition 
satisfies the \define{associative law}:
\[ (hg)f = h(gf). \]
\item For any object $x$, there is an \define{identity} morphism
$1_x \maps x \to x$.  These identity morphisms satisfy
the \define{left and right unit laws}:
\[ 1_y f = f = f 1_x \]
for any morphism $f \maps x \to y$.
\end{itemize}
The hardest thing about category theory is getting your arrows to
point the right way.  It is standard in mathematics to use $f g$ to
denote the result of doing first $g$ and then $f$.  In pictures, this
backwards convention can be annoying.  But rather than trying to fight it,
let us give in and draw a morphism $f \maps x \to y$ as an arrow from
right to left:
\[
\xymatrix{
   y \bullet 
&& \bullet x \ar@/_1pc/[ll]_{f}
}
\]
Then composition looks a bit better:
\[
\xymatrix{
   z \bullet 
&& \bullet y \ar@/_1pc/[ll]_{f}
    && \bullet x \ar@/_1pc/[ll]_{g}
}
\quad = \quad
\xymatrix{
   z \bullet 
&& \bullet x \ar@/_1pc/[ll]_{fg}
}
\]

An important example of a category is the `path groupoid' of a space $X$.  
We give the precise definition below, but the basic idea is to 
take the diagrams we have been drawing seriously!  The objects are 
points in $X$, and morphisms are paths: 
\[
\xymatrix{
   y \bullet 
&& \bullet x \ar@/_2pc/[ll]_{\gamma}
}
\]
We also get examples from groups.  A group is the same as
a category with one object where all the morphisms are invertible.
The morphisms of this category are the elements of the group.  
The object is there just to provide them with a source and target.
We compose the morphisms using the multiplication in the group.

In both these examples, a morphism $f \maps x \to y$ is \textit{not} a
function from $x$ to $y$.  And these two examples have something else
in common: they are important in gauge theory!  We can use a path
groupoid to describe the possible motions of a particle through
spacetime.  We can use a group to describe the symmetries of a
particle.  And when we combine these two examples, we get the concept
of \textit{connection}---the basic field in any gauge theory.

How do we combine these examples?  We do it using a map between
categories.  A map between categories is called a `functor'.  A
functor from a path groupoid to a group will send every object of the
path groupoid to the same object of our group.  After all, a group,
regarded as a category, has only one object.  But this functor will
also send any morphism in our path groupoid to a group element.  In
other words, it will assign a group element to each path in our space.
This group element \emph{describes how a particle transforms} as it
moves along that path.

But this is precisely what a connection does!  A connection lets us
compute for any path a group element describing parallel transport
along that path. So, the language of categories and functors quickly
leads us to the concept of connection---but with an emphasis on
parallel transport.

The following theorem makes these ideas precise.  Let us first
state the theorem, then define the terms involved, and then give
some idea of how it is proved:

\begin{thm} 
\label{thm:connections}
For any Lie group $G$ and any smooth manifold $M$,
there is a one-to-one correspondence between:
\begin{enumerate}
\item connections on the trivial principal $G$-bundle over $M$,
\item $\g$-valued 1-forms on $M$, where $\g$ is the Lie algebra of
$G$, and
\item smooth functors
\[ \hol \maps \P_1(M) \to G \]
where $\P_1(M)$ is the path groupoid of $M$.
\end{enumerate}
\end{thm}
\noindent
We assume you are familiar with the first two items.  
Our goal is to explain the third.  We must start by explaining
the path groupoid.

Suppose $M$ is a manifold.  Then the path groupoid $\P_1(M)$ is
roughly a category in which objects are points of $M$ and a morphism
from $x$ to $y$ is a path from $x$ to $y$.  We compose paths by gluing
them end to end.  So, given a path $\delta$ from $x$ to $y$, and a path
$\gamma$ from $y$ to $z$:
\[
\xymatrix{
   z \bullet 
&& y \bullet \ar@/_2pc/[ll]_{\gamma}
&& x \bullet \ar@/_2pc/[ll]_{\delta}
}
\]
we would like $\gamma \delta$ to be the path from $x$ to $z$ 
built from $\gamma$ and $\delta$.

However, we need to be careful about the details to make sure that the
composite path $\gamma \delta$ is well-defined, and that composition is
associative!  Since we are studying paths in a smooth manifold, we
want them to be smooth.  But the path $\gamma \delta$ may not be
smooth: there could be a `kink' at the point $y$.

There are different ways to get around this problem.  One is to work
with piecewise smooth paths.  But here is another approach: say that a
path
\[  \gamma \maps [0,1] \to M  \]
is {\bf lazy} if it is smooth and also constant in a neighborhood of
$t = 0$ and $t = 1$.  The idea is that a lazy hiker takes a rest
before starting a hike, and also after completing it.  Suppose
$\gamma$ and $\delta$ are smooth paths and $\gamma$ starts where
$\delta$ ends. Then we define their
{\bf composite}
\[   \gamma \delta \maps [0,1] \to M  \]
in the usual way:
\[   (\gamma \delta)(t) = \left\{ \begin{array}{cl}
                           \delta(2t) &\textrm{if } 0 \le t \le \half \\
                           \gamma(2t-1) &\textrm{if } \half \le t \le 1 
\end{array} \right.
\]
In other words, $\gamma \delta$ spends the first half of its time 
moving along $\delta$, and the second half moving along $\gamma$.
In general the path $\gamma \delta$ may not be smooth at $t = \half$.  
However, if $\gamma$ and $\delta$ are lazy, then their composite is
smooth---and it, too, is lazy!  

So, lazy paths are closed under composition.  Unfortunately, 
composition of lazy paths is not associative.  The paths $(\alpha \beta)
\gamma$ and $\alpha (\beta \gamma)$ differ by a smooth
reparametrization, but they are not equal.  To solve this problem, we
can take certain \textit{equivalence classes} of lazy paths as
morphisms in the path groupoid.

We might try `homotopy classes' of paths.  Remember, a homotopy is a
way of interpolating between paths:
\[
  \xymatrix{
y \bullet 
&& \bullet x
\ar@/^2.5ex/[ll]^{\delta}="g1"\ar@/_2.5ex/[ll]_{\gamma}="g2"
\ar@{=>}^{\Sigma} "g2"+<0ex,-2.5ex>;"g1"+<0ex,2.5ex>
}
\]
More precisely, a \define{homotopy} from the path $\gamma \maps [0,1] \to M$ 
to the path $\delta \maps [0,1] \to M$ is a smooth map
\[ \Sigma \maps [0,1]^2 \to M \]
such that $\Sigma(0,t) = \gamma(t)$ and $\Sigma(1,t) = \delta(t)$.  We
say two paths are \define{homotopic}, or lie in the same
\define{homotopy class}, if there is a homotopy between them.  

There is a well-defined category where the morphisms are homotopy
classes of lazy paths.  Unfortunately this is not right for gauge
theory, since for most connections, parallel transport along homotopic
paths gives different results.  In fact, parallel transport gives the
same result for all homotopic paths if and only if the connection is
\emph{flat}.

So, unless we are willing to settle for flat connections, we need 
a more delicate equivalence relation between paths.  Here the
concept of `thin' homotopy comes to our rescue.  A homotopy is {\bf thin} if
it sweeps out a surface that has zero area.  In other words, it is a
homotopy $\Sigma$ such that the rank of the differential $d\Sigma$ is
less than $2$ at every point.  If two paths differ by a smooth
reparametrization, they are thinly homotopic.  But there are other
examples, too.  For example, suppose we have a path $\gamma \maps x
\to y$, and let $\gamma^{-1} \maps y \to x$ be the \define{reverse}
path, defined as follows:
\[   \gamma^{-1}(t) = \gamma(1-t)  .\]
Then the composite path $\gamma^{-1} \gamma$, which goes from $x$ to
itself:
\[  \xymatrix{
y \bullet &&
\bullet x
\ar@/_2pc/@{<->}[ll]^{\gamma^{-1}}_{\gamma} 
}
\]
is thinly homotopic to the constant path that sits at $x$.  
The reason is that we can shrink $\gamma^{-1} \gamma$ down to the 
constant path without sweeping out any area.

We define the \define{path groupoid} $\P_1(M)$ to be the category where:
\begin{itemize}
\item Objects are points of $M$.
\item Morphisms are thin homotopy classes of lazy paths in $M$.
\item If we write $[\gamma]$ to denote the thin homotopy class of the
path $\gamma$, composition is defined by
\[      [\gamma][\delta] = [\gamma \delta] . \]
\item For any point $x \in M$, the identity $1_x$ is the thin homotopy
class of the constant path at $x$. 
\end{itemize}
With these rules, it is easy to check that $\P_1(M)$ is a category.
The most important point is that since the composite paths $(\alpha
\beta) \gamma$ and $\alpha (\beta \gamma)$ differ by a smooth
reparametrization, they are thinly homotopic.  This gives the associative
law when we work with thin homotopy classes.

But as its name suggests, $\P_1(M)$ is better than a mere category.
It is a \define{groupoid}: that is, a category where every morphism
$\gamma \maps x \to y$ has an \define{inverse} $\gamma^{-1} \maps y
\to x$ satisfying
\[  \gamma^{-1} \gamma = 1_x \quad \textrm{and} \quad
 \gamma \gamma^{-1} = 1_y \]
In $\P_1(M)$, the inverse is defined using the concept of a reverse
path:
\[         [\gamma]^{-1} = [\gamma^{-1}]  .\]
The rules for an inverse only hold in $\P_1(M)$ \emph{after} we take
thin homotopy classes.  After all, the composites $\gamma \gamma^{-1}$
and $\gamma^{-1} \gamma$ are \emph{not} constant paths, but they are
thinly homotopic to constant paths.  But henceforth, we will relax and
write simply $\gamma$ for the morphism in the path groupoid
corresponding to a path $\gamma$, instead of $[\gamma]$.

As the name suggests, groupoids are a bit like groups. Indeed, a
\define{group} is secretly the same as a groupoid with one object!
In other words, suppose we have group $G$.  Then there is a category
where:
\begin{itemize}
\item There is only one object, $\bullet$.
\item Morphisms from $\bullet$ to $\bullet$ are elements of $G$.
\item Composition of morphisms is multiplication in the group $G$.
\item The identity morphism $1_\bullet$ is the identity element
of $G$.
\end{itemize}
This category is a groupoid, since every group element has an inverse.
Conversely, any groupoid with one object gives a group.  Henceforth
we will freely switch back and forth between thinking of a group 
in the traditional way, and thinking of it as a one-object groupoid.

How can we use groupoids to describe connections? It should not be
surprising that we can do this, now that we have our path groupoid
$\P_1(M)$ and our one-object groupoid $G$ in hand.  A connection
gives a map from $\P_1(M)$ to $G$, which says how to transform 
a particle when we move it along a path.  More precisely: if $G$ is
a Lie group, any connection on the trivial $G$-bundle over $M$
yields a map, called the parallel transport map or
\define{holonomy}, that assigns an element of $G$
to each path: 
\[ \hol \maps \xymatrix{ \bullet 
 & \bullet \ar@/_0.5pc/[l]_{\gamma}  
} 
\quad \mapsto \quad \hol(\gamma) \in G \] 
In physics notation, the holonomy is defined as the 
path-ordered exponential of some $\g$-valued 1-form $A$,
where $\g$ is the Lie algebra of $G$:
\[ \hol(\gamma) = \poexp \left( \int_\gamma A \right) \in G. \]

The holonomy map satisfies certain rules, most of which are summarized
in the word `functor'.  What is a functor?  It is a map between
categories that preserves all the structure in sight!

More precisely: given categories $C$ and $D$, a \define{functor} $F
\maps C \to D$ consists of:
\begin{itemize} 
\item a map $F$ sending objects in $C$ to objects in $D$, and
\item another map, also called $F$, sending morphisms in $C$ to 
morphisms in $D$,
\end{itemize}
such that:
\begin{itemize}
\item given a morphism $f \maps x \to y$ in $C$, we have
$F(f) \maps F(x) \to F(y)$, 
\item $F$ preserves composition:
\[ F(fg) = F(f)F(g) \]
when either side is well-defined, and
\item $F$ preserves identities:
\[ F(1_x) = 1_{F(x)} \]
for every object $x$ of $C$.
\end{itemize}
The last property actually follows from the rest.  The second to 
last---preserving composition---is the most important property
of functors.  As a test of your understanding, check that if $C$ and
$D$ are just \emph{groups} (that is, one-object groupoids) then
a functor $F \maps C \to D$ is just a \emph{homomorphism}.

Let us see what this definition says about a functor
\[       \hol \maps \P_1(M) \to G \]
where $G$ is some Lie group.
This functor $\hol$ must send all the points of $M$ to
the one object of $G$.  More interestingly, it must send
thin homotopy classes of paths in $M$ to elements of $G$:
\[ \hol \maps \xymatrix{ \bullet 
 & \bullet \ar@/_0.5pc/[l]_{\gamma}  
} 
\quad \mapsto \quad \hol(\gamma) \in G \] 
It must preserve composition:
\[ \hol(\gamma \delta) = \hol(\gamma) \, \hol(\delta) \]
and identities:
\[ \hol(1_x) = 1 \in G. \]

While they may be stated in unfamiliar language, these are actually
well-known properties of connections!  First, the holonomy of a
connection along a path
\[ \hol(\gamma) = \poexp \left( \int_\gamma A \right) \in G \]
only depends on the thin homotopy class of $\gamma$.  To 
see this, compute the variation of $\hol(\gamma)$ as we vary the path
$\gamma$, and show the variation is zero if the homotopy is thin.
Second, to compute the group element for a composite of paths, we just
multiply the group elements for each one:
\[ \poexp \left( \int_{\gamma \delta} A \right) = 
\poexp \left( \int_\gamma A \right) \poexp \left( \int_\delta A \right) \]
And third, the path-ordered exponential along a constant path is just the
identity:
\[ \poexp \left( \int_{1_x} A \right) = 1 \in G. \]

All this information is neatly captured by saying $\hol$ is a
functor. And Theorem~\ref{thm:connections} says this is almost all
there is to being a connection. The only additional condition required
is that $\hol$ be \emph{smooth}. This means, roughly, that
$\hol(\gamma)$ depends smoothly on the path $\gamma$---more on that
later.  But if we drop this condition, we can generalize the concept
of connection, and define a \define{generalized connection} on a smooth
manifold $M$ to be a functor $\hol \maps \P_1(M) \to G$. 

Generalized connections have long played an important role in loop
quantum gravity, first in the context of real-analytic manifolds
\cite{AshtekarLewandowski:1994}, and later for smooth manifolds
\cite{BaezSawin:1995,LewandowskiThiemann:1999}.  The reason is that if
$M$ is any manifold and $G$ is a connected compact Lie group, there is
a natural measure on the space of generalized connections.  This means
that you can define a Hilbert space of complex-valued
square-integrable functions on the space of generalized connections.
In loop quantum gravity these are used to describe quantum states
before any constraints have been imposed.  The switch from connections
to generalized connections is crucial here---and the lack of
smoothness gives loop quantum gravity its `discrete' flavor.

But suppose we are interested in ordinary connections.  Then we
really want $\hol(\gamma)$ to depend smoothly on the path $\gamma$.
How can we make this precise?  

One way is to use the theory of `smooth groupoids'
\cite{BaezSchreiber}.  Any Lie group is a smooth groupoid, and so is
the path groupoid of any smooth manifold.  We can define smooth
functors between smooth groupoids, and then smooth functors $\hol
\maps \P_1(M) \to G$ are in one-to-one correspondence with connections
on the trivial principal $G$-bundle over $M$.  We can go even further:
there are more general maps between smooth groupoids, and maps $\hol
\maps \P_1(M) \to G$ of this more general sort correspond to
connections on \textit{not necessarily trivial} principal $G$-bundles
over $M$.  For details, see the work of Bartels \cite{Bartels:2004},
Schreiber and Waldorf \cite{SchreiberWaldorf:functors}.

But if this sounds like too much work, we can take the following
shortcut.  Suppose we have a smooth function $F \maps [0,1]^n \times
[0,1] \to M$, which we think of as a parametrized family of paths.
And suppose that for each fixed value of the parameter $s \in
[0,1]^n$, the path $\gamma_s$ given by
\[               \gamma_s(t) = F(s,t)  \]
is lazy.  Then our functor $\hol \maps \P_1(M) \to G$ gives a function
\[              
\begin{array}{ccl}
[0,1]^n &\to& G  \\
s       &\mapsto& \hol(\gamma_s)  .
\end{array}
\]
If this function is smooth whenever $F$ has the above properties,
then the functor $\hol \maps \P_1(M) \to G$ is {\bf smooth}.

Starting from this definition one can prove the following lemma, 
which lies at the heart of Theorem~\ref{thm:connections}:

\begin{lem}
There is a one-to-one correspondence between smooth functors  
\hfill \break

$\hol \maps \P_1(M) \to G$  and $\Lie(G)$-valued 1-forms $A$ on $M$.
\end{lem}

The idea is that given a $\Lie(G)$-valued 1-form $A$ on $M$, we can 
define a holonomy for any smooth path as follows:
\[ \hol(\gamma) = \poexp\left( \int_\gamma A \right) , \]
and then check that this defines a smooth functor $\hol \maps \P_1(M)
\to G$.  Conversely, suppose we have a smooth functor $\hol$ of this
sort.  Then we can define $\hol(\gamma)$ for smooth paths $\gamma$
that are not lazy, using the fact that every smooth path is thinly
homotopic to a lazy one.  We can even do this for paths $\gamma \maps
[0,s] \to M$ where $s \ne 1$, since any such path can be
reparametrized to give a path of the usual sort.  Given a smooth path
\[ \gamma \maps [0,1] \to M \]
we can truncate it to
obtain a path $\gamma_s$ that goes along $\gamma$ until time $s$:
\[ \gamma_s \maps [0,s] \to M .\]
By what we have said, $\hol(\gamma_s)$ is well-defined.  Using the
fact that $\hol \maps \P_1(M) \to G$ is a smooth functor, one can
check that $\hol(\gamma_s)$ varies smoothly with $s$.  So, we can
differentiate it and define a $\Lie(G)$-valued 1-form $A$ as follows:
\[ A(v) = \frac{d}{ds} \hol(\gamma_s) \big|_{s=0} \]
where $v$ is any tangent vector at a point $x \in M$, and 
$\gamma$ is any smooth path with 
\[        \gamma(0) = x, \qquad \gamma'(0) = v  .\]
Of course, we need to check that $A$ is well-defined and smooth.  We
also need to check that if we start with a smooth functor $\hol$,
construct a 1-form $A$ in this way, and then turn $A$ back into a
smooth functor, we wind up back where we started.
