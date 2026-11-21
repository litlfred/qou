---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.994
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of point particles using connections on bundles, higher gauge theory describes the parallel transport of 1-dimensional"
---
\label{section: Introduction}

Ordinary gauge theory describes how 0-dimensional particles
transform as we move them along 1-dimensional
paths.  It is natural to assign a group element to 
each path:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g}
&& \bullet
}
\]
The reason is that composition of paths then corresponds to
multiplication in the group:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g}
&& \bullet \ar@/^1pc/[rr]^{g'}
&& \bullet
}
\]
while reversing the direction of a path corresponds to taking
inverses:
\[
\xymatrix{
   \bullet
&& \bullet \ar@/_1pc/[ll]_{g^{-1}}
}
\]
and the associative law makes the holonomy along a triple
composite unambiguous:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g}
&& \bullet \ar@/^1pc/[rr]^{g'}
&& \bullet \ar@/^1pc/[rr]^{g''}
&& \bullet
}
\]
In short, the topology dictates the algebra!

Now suppose we wish to do something similar
for 1-dimensional `strings' that trace out 2-dimensional surfaces
as they move.  Naively we might wish our holonomy to assign a group 
element to each surface like this:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]_{}="0"
           \ar@/_1pc/[rr]_{}="1"
           \ar@{=>}"0";"1"^{g}
&& \bullet
}
\]
There are two obvious ways to compose surfaces of this sort, vertically:
\[
\xymatrix{
   \bullet \ar@/^2pc/[rr]_{}="0"
           \ar[rr]_{}="1"
           \ar@{=>}"0";"1"^{g}
           \ar@/_2pc/[rr]_{}="2"
           \ar@{=>}"1";"2"^{g'}
&& \bullet
}
\]
and horizontally:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]_{}="0"
           \ar@/_1pc/[rr]_{}="1"
           \ar@{=>}"0";"1"^{g}
&& \bullet \ar@/^1pc/[rr]_{}="2"
           \ar@/_1pc/[rr]_{}="3"
           \ar@{=>}"2";"3"^{g'}
&& \bullet
}
\]
Suppose that both of these correspond to multiplication
in the group $G$.  Then to obtain a well-defined holonomy for this
surface regardless of whether we do vertical or horizontal composition
first:
\[
\xymatrix{
   \bullet \ar@/^2pc/[rr]_{}="0"
           \ar[rr]_{}="1"
           \ar@{=>}"0";"1"^{g_1}
           \ar@/_2pc/[rr]_{}="2"
           \ar@{=>}"1";"2"^{g_1^\prime}
&& \bullet \ar@/^2pc/[rr]_{}="3"
           \ar[rr]_{}="4"
           \ar@{=>}"3";"4"^{g_2}
           \ar@/_2pc/[rr]_{}="5"
           \ar@{=>}"4";"5"^{g'_2}
&& \bullet
}
\]
we must have
\[      (g_1 g_2)(g_1' g_2') = (g_1 g_1')(g_2 g_2') . \]
This forces $G$ to be abelian!

In fact, this argument goes back to a classic paper by
Eckmann and Hilton \cite{EckmannHilton}.  They showed
that even if we allow $G$ to be equipped with two products,
say $gg'$ for vertical composition and $g \circ g'$ for
horizontal, so long as both products share the
same unit and satisfy this `{\bf interchange law}':
\[  
  (g_1 g_1') \circ (g_2 g_2') =
      (g_1 \circ g_2) (g_1' \circ g_2')  
\]
then in fact they must agree --- so by the previous argument,
both are abelian.  The proof is very easy:
\[  
     g \circ g' 
   = (g 1) \circ (1 g') 
   = (g \circ 1) (1 \circ g') 
   = g g' 
\]

Pursuing this approach, we would ultimately reach the theory of
connections on abelian gerbes [2-8].


If $G = \U(1)$, such a connection can be locally identified with a 
2-form --- but globally it is a subtler object, just as a connection
on a $\U(1)$ bundle can be locally identified with a 1-form, but not
globally.  In fact, connections on abelian gerbes play an important role 
in string theory [9-11].

Just as ordinary electromagnetism is described by a connection on a $\U(1)$ 
bundle, usually called the `vector potential' and denoted $A$, the 
stringy analogue of electromagnetism is described by a connection on 
a $\U(1)$ gerbe, called the $B$ field.

To go beyond this and develop a theory of \emph{nonabelian} higher gauge 
fields, we must let the topology dictate the algebra.  Readers familiar
with higher categories will already have noticed that 1-dimensional 
pictures above resemble diagrams in category theory, while the
2-dimensional pictures resemble diagrams in 2-category theory.  This 
suggests that the holonomies in higher gauge 
theory should take values in some `categorified' analogue of
a Lie group --- that is, some gadget resembling a Lie group, but 
which is a category rather than a set.  We call this `Lie 2-group'.   

In fact, Lie 2-groups and their Lie 2-algebras have already been studied 
\cite{BaezLauda:2003,BaezCrans:2003} and interesting examples have been 
constructed using the mathematics of string theory: central extensions 
of loop groups \cite{BCSS}.  
But even without knowing this, we could be led to the definition of a 
Lie 2-group by considering a kind of connection that gives holonomies 
\emph{both for paths and for surfaces}.

So, let us assume that for each path we have a holonomy taking values 
in some Lie group $G$, where composition of paths corresponds to 
multiplication in $G$.  Assume also that for each 1-parameter family of 
paths with fixed endpoints we have a holonomy taking values in some other
Lie group $H$, where vertical composition corresponds to multiplication in
$H$:
\[
\xymatrix{
   \bullet \ar@/^2pc/[rr]_{}="0"
           \ar[rr]_{}="1"
           \ar@{=>}"0";"1"^{h}
           \ar@/_2pc/[rr]_{}="2"
           \ar@{=>}"1";"2"^{h'}
&& \bullet
}
\]

Next, assume that we can parallel transport an element $g \in G$
along a 1-parameter family of paths to get a new element $g' \in G$:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g}_{}="0"
           \ar@/_1pc/[rr]_{g'}_{}="1"
           \ar@{=>}"0";"1"^{h}
&& \bullet
}
\]
This picture suggests that we should think of $h$ as a kind of
`arrow' or `morphism' going from $g$ to $g'$.  We can use categories
to formalize this.  In category theory, when a morphism
goes from an object $x$ to an object $y$, we think of the morphism as
determining both its source $x$ and its target $y$.  The group
element $h$ does not determine $g$ or $g'$.  However, the pair $(g,h)$
does.  

For this reason, it is useful to create a category $\twogroup$ where the
set of objects, say $\Ob(\twogroup)$, is just $G$, while the set of
morphisms, say $\Mor(\twogroup)$, consists of ordered pairs $f = (g,h) 
\in G \times H$.  Switching our notation to reflect this, we rewrite the 
above picture as
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g}_{}="0"
           \ar@/_1pc/[rr]_{g'}_{}="1"
           \ar@{=>}"0";"1"^{f}
&& \bullet
}
\]
and write $f \maps g \to g'$ for short.  

In this new notation, we can vertically compose $f \maps g \to g'$ 
and $f' \maps g' \to g''$ to get $f f' \maps g \to g''$, as follows:
\[
\xymatrix{
   \bullet \ar@/^2pc/[rr]^{g}_{}="0"
           \ar[rr]^<<<<<<{g'}_{}="1"
           \ar@{=>}"0";"1"^{f}
           \ar@/_2pc/[rr]_{g''}_{}="2"
           \ar@{=>}"1";"2"^{f'}
&& \bullet
}
\]
This is just composition of morphisms in the category $\twogroup$.  However, 
we can also horizontally compose $f_1 \maps g_1 \to g_1'$ and $f_2 \maps
g_2 \to g_2'$ to get $f_1 \circ f_2 \maps g_1g_2 \to g_1'g_2'$, as follows:
\[
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{g_1}_{}="0"
           \ar@/_1pc/[rr]_{g_1'}_{}="1"
           \ar@{=>}"0";"1"_{f_1}
&& \bullet \ar@/^1pc/[rr]^{g_2}_{}="2"
           \ar@/_1pc/[rr]_{g_2'}_{}="3"
           \ar@{=>}"2";"3"_{f_2}
&& \bullet
}
\]
We assume this operation makes $\Mor(\twogroup)$ into a 
group with the pair $(1,1) \in G \times H$ as its multiplicative unit.

The good news is that now we can assume an interchange law saying this
holonomy is well-defined:
\[
\xymatrix{
   \bullet \ar@/^2pc/[rr]^{g_1}_{}="0"
           \ar[rr]^<<<<<<{g_2}_{}="1"
           \ar@{=>}"0";"1"^{f_1}
           \ar@/_2pc/[rr]_{g_3}_{}="2"
           \ar@{=>}"1";"2"^{f_1'}
&& \bullet \ar@/^2pc/[rr]^{g_1'}_{}="3"
           \ar[rr]^<<<<<<{g_2'}_{}="4"
           \ar@{=>}"3";"4"^{f_2}
           \ar@/_2pc/[rr]_{g_3'}_{}="5"
           \ar@{=>}"4";"5"^{f_2'}
&& \bullet
}
\]
namely:
\[
  (f_1 f_1') \circ (f_2 f_2') =  (f_1 \circ f_2) (f_1' \circ f_2')
\]
without forcing either $G$ or $H$ to be abelian!   Instead, the group
$\Mor(\twogroup)$ is forced to be a semidirect product of $G$ and $H$.

The structure we are rather roughly describing here turns out to be
none other than a `Lie 2-group'.  This is an `internal category' in the
category of Lie groups.  In other words, it is a category where the set of 
objects is a Lie group, the set of morphisms is a Lie group, and all the 
usual category operations are Lie group homomorphisms. 

This audacious process --- taking a familiar 
mathematical concept defined using sets and function 
and transplanting it to live within some other category --- is far from new.  
For example, a Lie group is a group in $\Diff$, the category of smooth 
manifolds and smooth maps.  The general idea of an `internal category'
living within some other category was described by Charles Ehresmann 
\cite{Ehresmann:1963} in the early 1960's.  In the next section we begin 
by reviewing this idea.  In the rest of the paper, we use it to categorify 
the theory of Lie groups, Lie algebras, bundles and connections.  
Before we proceed, let us sketch our overall plan.

The starting point is the ordinary concept of a 
principal fiber bundle.  Such a bundle can be specified using the 
following `gluing data': 
\begin{itemize}
  \item
    a base manifold $M$,
  \item
    a cover of $M$ by open sets $\{U_i\}_{i\in I}$,
  \item
    a Lie group $G$ (the `gauge group' or `structure group'), 
  \item
    on each double overlap $U_{ij} = U_i \cap U_j$ a 
    $G$-valued function $g_{ij}$, 
  \item
    such that on triple overlaps
    the following transition law holds:
    \begin{eqnarray}
       g_{ij} g_{jk} = g_{ik}.
       \nonumber
    \end{eqnarray}
\end{itemize}
Such a bundle is augmented with a connection by specifying:
\begin{itemize}
  \item
    in each open set $U_i$ a smooth functor $\mathrm{hol}_i \maps
    \P_1(U_i) \to G$ from the path groupoid of $U_i$ to the gauge group, 
  \item
   such that for all paths $\gamma$ in double overlaps $U_{ij}$
   the following transition law holds:
   \begin{eqnarray}
     \mathrm{hol}_i\of{\gamma} &=& 
      g_{ij} \, \mathrm{hol}_j\of{\gamma} \,  g_{ij}^{-1}.
     \nonumber
   \end{eqnarray}
\end{itemize}
Here the `path groupoid' $\P_1(\manifold)$ of a manifold $\manifold$ 
has points of $\manifold$ as objects and certain equivalence classes 
of smooth paths in $\manifold$ as morphisms.  There are various ways 
to work out the technical details and make $\P_1(\manifold)$ into a 
`smooth groupoid'; here we follow the approach of Barrett \cite{Barrett:1991}, 
who uses `thin homotopy classes' of paths.  Technical details aside, 
the basic idea is that a connection on a trivial $G$-bundle gives a 
well-behaved map assigning to each path $\gamma$ in the base space the 
holonomy $\hol(\gamma) \in G$ of the connection along that path.   
Saying this map is a `smooth functor' means that these holonomies 
compose when we compose paths, and that the holonomy $\hol(\gamma)$ 
depends smoothly on the path $\gamma$.

A basic goal of higher gauge theory is to categorify all of this and to work 
out the consequences.  As mentioned, the key tool is internalization.  
This leads us immediately to the concept of a Lie 2-group, and also 
to that of a `smooth 2-space': a category in $\Diff$, or more generally 
in some category of smooth spaces that allows for infinite-dimensional 
examples.  

Using these concepts, Bartels \cite{Bartels:2004} has defined 
a `principal 2-bundle $E$ over $M$ with structure 
2-group $\twogroup$'.  To arrive at this definition, the 
key steps are to replace the total space $E$ and base space $M$ of
a principal bundle by smooth 2-spaces, and to replace the structure 
group by a Lie 2-group.  In this paper we only consider the case where 
$M$ is an ordinary space, which can be regarded as a 2-space with only 
identity morphisms.  We show that for a suitable choice of structure 
2-group, principal 2-bundles give abelian gerbes over $M$.  For another
choice, they give nonabelian gerbes.  This sets the stage for a result 
relating the 2-bundle approach to higher gauge theory to Breen and 
Messing's approach based on nonabelian gerbes \cite{BreenMessing:2001}.

Just as a connection on a trivial principal bundle over $M$ gives a 
functor from the path groupoid of $M$ to the structure group, one 
might hope that a `2-connection' on a trivial principal 2-bundle would 
define a 2-functor from some sort of `path 2-groupoid' to the structure 
2-group.  This has already been confirmed in the context of higher lattice 
gauge theory [19-21].

Thus, the main issues not yet addressed are those involving differentiability. 

To address these issues, we define for any smooth space $M$ a smooth 
2-groupoid $\P_2(M)$ such that:
\begin{itemize}
\item
the objects of $\P_2(M)$ are points of $M$: 
$ \quad   \bullet \, {\textstyle{\small{\textit{x}}}}   $
\item 
the morphisms of $\P_2(M)$ are thin homotopy classes of
smooth paths $\gamma \maps [0,1] \to M$ such that $\gamma(s)$ 
is constant in a neighborhood of $s = 0$ and $s = 1$:
$
\xymatrix{
 {\textstyle{\small{\textit{x}}}}  \,
   \bullet \ar@/^1pc/[rr]^{\gamma}
&& \bullet \, {\textstyle{\small{\textit{y}}}}   
}
$
\item 
the 2-morphisms of $\P_2(M)$ are `bigons': that is,
thin homotopy classes of smooth maps 
$\Sigma \maps [0,1]^2 \to M$ such that $\Sigma(s,t)$ is 
constant near $s = 0$ and $s = 1$, and 
independent of $t$ near $t = 0$ and $t = 1$:
$
\xymatrix{
 {\textstyle{\small{\textit{x}}}} \, 
   \bullet \ar@/^1pc/[rr]^{\gamma_1}_{}="0"
           \ar@/_1pc/[rr]_{\gamma_2}^{}="1"
&& \bullet \, {\textstyle{\small{\textit{y}}}}   
\ar@{=>}"0";"1"^{\Sigma}
}
$
\end{itemize}
The `thin homotopy' equivalence relation, borrowed from the work
of Mackaay and Picken \cite{MackaayPicken:2000,Mackaay:2001}, 
guarantees that two maps differing only by a reparametrization 
define the same bigon.  This is important because we seek a 
{\it reparametrization-invariant notion of surface holonomy}.

We define a `2-connection' on a trivial principal 2-bundle 
over $M$ to be a smooth 2-functor $\hol \maps \P_2(M) 
\to \twogroup$, where $\twogroup$ is the structure 2-group.   
This means that the 2-connection assigns holonomies both
to paths and bigons, independent of their parametrization, compatible 
with the standard operations of composing paths and bigons, and 
depending smoothly on the path or surface in question.  

We also define 2-connections for nontrivial principal 2-bundles,
and state a theorem obtaining these from Lie-algebra-valued
differential forms.   We then show that for a certain class of
structure 2-groups, such differential forms reduce to Breen and 
Messing's `connections on nonabelian gerbes' \cite{BreenMessing:2001}.  
The surprise is that we only obtain connections satisfying a 
certain constraint: the `fake curvature' must vanish!

To understand this, one must recall \cite{BaezLauda:2003}
that a Lie 2-group $\twogroup$ amounts to the same thing as 
a `crossed module' of Lie groups $(G,H,t,\alpha)$, where:
\begin{itemize}
\item $G$ is the group of objects of $\G$, $\Ob(\twogroup)$:
\item $H$ is the subgroup of $\Mor(\twogroup)$ consisting
of morphisms with source equal to $1 \in G$:
\item $t \maps H \to G$ is the homomorphism sending each morphism
in $H$ to its target,
\item $\alpha$ is the action of $G$ as automorphisms of $H$ defined
using conjugation in $\Mor(\twogroup)$ as follows: 
$\alpha(g) h = 1_g h {1_g}^{-1}$. 
\end{itemize}
Differentiating all this data one obtains a `differential crossed 
module' $(\g,\h,dt,d\alpha)$, which is just another way of talking
about a Lie 2-algebra \cite{BaezSchreiber:2004}.

In these terms, a 2-connection on a trivial principal 2-bundle over
$M$ with structure 2-group $\twogroup$ consists of a $\g$-valued
1-form $A$ together with an $\h$-valued 2-form $B$ on $M$. Translated
into this framework, Breen and Messing's `fake curvature' is the
$\g$-valued 2-form
\[
dt\of{B} + F_A, 
\]
where $F_A = \extd A + A \wedge A$ is the usual curvature of $A$.
We show that {\it if and only if the fake curvature vanishes}, 
one obtains a well-defined 2-connection $\hol \maps \P_2(M) \to \twogroup$.  

The importance of vanishing fake curvature in the framework of lattice 
gauge theory was already emphasized by Girelli and Pfeiffer
\cite{GirelliPfeiffer:2004}.  The special case where also $F_A = 0$ 
was studied by Alvarez, Ferreira, Sanchez and Guillen
\cite{AlvarezFerreiraSanchezGuillen:1998}.   The case where 
$G = H$ has been studied already by the second author of this
paper \cite{Schreiber:2004e}.  Our result subsumes these 
cases in a common framework.  

This paper is an introduction to work in progress \cite{BaezSchreiber:2004},
which began in rudimentary form as an article by the first author
\cite{Baez:2002}, and overlaps to some extent with theses by 
Bartels \cite{Bartels:2004} and the second author
\cite{Schreiber:2005}.  Bartels' thesis develops the general
theory of 2-bundles.  The second author's thesis investigates the
relationship between nonabelian higher gauge theory and the physics 
of strings.  Aschieri, Cantini and Jur{\v c}o 
\cite{AschieriCantiniJurco:2003,AschieriJurco:2004} have
also studied this subject, using connections on nonabelian gerbes.
Other physicists, including Chepelev \cite{Chepelev:2002} and Hofman 
\cite{Hofman:2002}, have also studied nonabelian higher gauge fields.
