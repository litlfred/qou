---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-013-46-string-2-groups
section_title: "String 2-Groups"
section_number: 4.6
pages: 40-44
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.996
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{string}

The Lie 2-groups discussed so far are easy to construct.  The string
2-group is considerably more subtle.  Ultimately it forces upon us
a deeper conception of what a Lie 2-group really is, and a more
sophisticated approach to higher gauge theory.  Treated in proper
detail, these topics would carry us far beyond the limits of this
quick introduction.  But it would be a shame not to mention them at
all.

Suppose we have a central extension of a Lie group $G$ by an
abelian Lie group $A$.  In other words,
suppose we have a short exact sequence of Lie groups
\[   1 \to A \to H \stackrel{t}{\to} G \to 1 \]
where the image of $A$ lies in the center of $H$.  
Then we can construct an action $\alpha$ of $G$ on $H$ as follows.  
The map $t \maps H \to G$ describes $H$ as a fiber bundle over $G$,
so choose a \define{section} of this bundle: that is, a function 
$s \maps G \to H$ with $t(s(g)) = g$, not necessarily a homomorphism.  
Then set
\[      \alpha(g) h = s(g) h s(g)^{-1}  .\]
Since $A$ is included in the center of $H$, $\alpha$ is independent of
the choice of $s$.  Thanks to this, we do not need a global smooth
section $s$ to check that $\alpha(g)$ depends smoothly on $g$: it
suffices that there exist a local smooth section in a
neighborhood of each $g \in G$, and indeed this is always true. We can
use these local sections to define $\alpha$ globally, since they must
give the same $\alpha$ on overlapping neighborhoods.

Given all this, we can check that $t$ is $G$-equivariant and that
the Peiffer identity holds.  So, we obtain a Lie 2-group where:
\begin{itemize}
\item $G$ is any Lie group,
\item $H$ is any Lie group,
\item $t \maps H \to G$ makes $H$ into a central extension of $G$,
\item $\alpha$ is given by $\alpha(g) h = s(g) h s(g)^{-1}$ where
$s \maps G \to H$ is any section.
\end{itemize}
We call this the \define{central extension 2-group} 
$\CC(H \stackrel{t}{\to} G)$.  

To get concrete examples, we need examples of central extensions. 
For any choice of $G$ and $A$, we can always take $H = G \times A$ and
use the `trivial' central extension
\[   1 \to A \to A \times G \to G \to 1 .\]
For more interesting examples, we need nontrivial central
extensions.  These tend to arise from problems in quantization.  For
example, suppose $V$ is a finite-dimensional 
\define{symplectic vector space}: that is, a vector space
equipped with a nondegenerate antisymmetric bilinear form
\[     \omega \maps V \times V \to \R .\]
Then we can make $H = V \times \R$ into a Lie group
called the \define{Heisenberg group}, with the product
\[    (u,a)(v,b) = (u+v, a + b + \omega(u,v)) .\]
The Heisenberg group plays a fundamental role in quantum mechanics,
because we can think of $V$ as the phase space of a classical point
particle.  If we let $G$ stand for $V$ regarded as an abelian Lie group, 
then elements of $G$ describe translations in phase space: that is,
translations of both position and momentum.  The Heisenberg group $H$
describes how these translations commute only `up to a phase'
when we take quantum mechanics into account: the phase is given by
$\exp(i \omega(u,v))$.  There is a homomorphism $t \maps H \to G$
that forgets this phase information, given by
\[    t(u,a) = u .\]
This exhibits $H$ as a central extension of $G$.  We thus
obtain a central extension 2-group $\CC(H \stackto{t} G)$, called the
{\bf Heisenberg 2-group} of the symplectic vector space $V$.

The applications of Heisenberg 2-groups seem largely unexplored, and
should be worth studying.  So far, much more work has been put into
understanding 2-groups arising from central extensions of loop groups.
The reason is that central extensions of loop groups play a basic role
in string theory and conformal field theory, as nicely explained by
Pressley and Segal \cite{PressleySegal:1986}.

Suppose that $G$ is a connected and simply-connected compact simple Lie 
group $G$.   Define the \define{loop group} $\Omega G$ to be
the set of all smooth paths $\gamma \maps [0,1] \to G$ that start and
end at the identity of $G$.  This becomes a group under pointwise
multiplication, and in fact it is a kind of infinite-dimensional Lie
group \cite{Milnor}. 

For each integer $k$, called the \define{level}, the loop group has a
central extension
\[           1 \to \U(1) \to
\widehat{\Omega_k G} \stackto{t} \Omega G \to 1 .  \]
These extensions are all different, and all nontrivial except for $k =
0$.  In physics, they arise because the 2d gauge theory called the
Wess--Zumino--Witten model has an `anomaly'.  The loop group $\Omega
G$ acts as gauge transformations in the classical version of this
theory.  However, when we quantize the theory, we obtain a
representation of $\Omega G$ only `up to a phase'---that is, a
projective representation.  This can be understood as an honest
representation of the central extension $\widehat{\Omega_k G}$, where
the integer $k$ appears in the Lagrangian for the Wess--Zumino--Witten
model.

Starting from this central extension we can construct a central
extension 2-group called the \define{\boldmath level-$k$ loop
2-group} of $G$, ${\cal L}_k(G)$.  This is an infinite-dimensional Lie
2-group, meaning that it comes from a crossed module where the groups
involved are infinite-dimensional Lie groups, and all the maps are
smooth.  Moreover, it fits into an exact sequence
\[           1 \to \mathcal{L}_k(G) \to \STRING_k(G) 
\stackto{} G \to 1   \]
where the middle term, the \textbf{level-\textit{k} string 2-group} of
$G$, has very interesting properties \cite{BCSS}.  

Since the string 2-group $\STRING_k(G)$ is an infinite-dimensional
Lie 2-group, it is a topological 2-group.  There is a way to take any
topological 2-group and squash it down to a topological group
\cite{BCSS,BaezStevenson}.  Applying this trick to $\STRING_k(G)$ when
$k = 1$, we obtain a topological group whose homotopy groups match
those of $G$---except for the third homotopy group, which has been
made trivial.  In the special case where $G = \mathrm{Spin}(n)$, this
topological group is called the `string group', since to consistently
define superstrings propagating on a spin manifold, we must reduce its
structure group from $\mathrm{Spin}(n)$ to this group
\cite{Witten:1988}.  The string group also plays a role in Stolz and
Teichner's work on elliptic cohomology, which involves a notion of
parallel transport over surfaces \cite{StolzTeichner}.  There is a lot
of sophisticated mathematics involved here, but ultimately much of it
should arise from the way string 2-groups are involved in the parallel
transport of strings!  The work of Sati, Schreiber and Stasheff
\cite{SSS} provides good evidence for this, as does the work of
Waldorf \cite{Waldorf}.

In fact, the string Lie 2-group had lived through many previous 
incarnations before being constructed as an infinite-dimensional 
Lie 2-group.  Brylinski and McLaughlin \cite{BrylinskiMcLaughlin}
thought of it as a $\U(1)$ gerbe over the group $G$.  The fact 
that this gerbe is `multiplicative' makes it something like a 
group in its own right \cite{Brylinski:2000}.  This viewpoint has
also been explored by Murray and Stevenson \cite{MurrayStevenson}.

Later, Baez and Crans \cite{BaezCrans} constructed a Lie 2-algebra 
$\sstring_k(\g)$ corresponding to the string Lie 2-group.  For 
pedagogical purposes, our discussion of Lie 2-groups has focused 
solely on `strict' 2-groups, where the 1-morphisms satisfy the group 
axioms strictly, as equations.  However, there is also an extensive 
theory of `weak' 2-groups, where the 1-morphisms obey the group axioms 
only up to invertible 2-morphisms \cite{BaezLauda:2groups}.  
Following this line of thought, we may also define weak Lie 2-algebras
\cite{Roytenberg}, and the Lie 2-algebra $\sstring_k(\g)$ is one of 
these where only the Jacobi identity fails to hold strictly.  

The beauty of weak Lie 2-algebras is that $\sstring_k(\g)$ is
very easy to describe in these terms.  In particular, it is
finite-dimensional.  The hard part is constructing
a weak Lie 2-group corresponding to this weak Lie 2-algebra.  It is
easy to check that any strict Lie 2-algebra has a corresponding strict
Lie 2-group.  Weak Lie 2-algebras are more tricky
\cite{BaezLauda:2groups}.  Baez, Crans, Schreiber and Stevenson
\cite{BCSS} dodged this problem by showing that the string Lie 
2-algebra is \emph{equivalent} (in some precise sense) to a strict 
Lie 2-algebra, which however is infinite-dimensional.  They then 
constructed the infinite-dimensional strict Lie 2-group corresponding 
to this strict Lie 2-algebra.   This is just $\STRING_k(G)$ as described 
above.

On the other hand, a finite-dimensional model of the string 2-group 
was recently introduced by Schommer-Pries \cite{Schommer-Pries}.  
This uses an improved definition of `weak Lie 2-group', based on
an important realization: the correct maps between smooth groupoids 
are not the smooth functors, but something more general \cite{Lerman}.  
We have already mentioned this in our discussion of connection:
a smooth functor $\hol \maps \P_1(M) \to G$ is a connection on the
trivial principal $G$-bundle over $M$, while one of these more general 
maps is a connection on an \emph{arbitrary} principal $G$-bundle over
$M$.  If we take this lesson to heart, we are led into the world of 
`stacks'---and in that world, we can find a finite-dimensional version 
of the string 2-group.

There has also been progress on constructing weak Lie $n$-groups from
weak Lie $n$-algebras for $n > 2$.  Getzler \cite{Getzler} and
Henriques \cite{Henriques} have developed an approach that works for
all $n$, even $n = \infty$.  Their approach is able to handle weak Lie
$\infty$-algebras of a sort known as `$L_\infty$-algebras'.  Quite
roughly, the idea is that in an $L_\infty$-algebra, the Jacobi
identity holds only weakly, while the antisymmetry of the bracket
still holds strictly.

In fact, $L_\infty$-algebras were developed by Stasheff and
collaborators \cite{MSS,SS} before higher gauge theory became
recognized as a subject of study.  But more recently, Sati, Schreiber,
Stasheff \cite{Sati,SSS} have developed a lot of higher gauge theory
with the help of $L_\infty$-algebras. Thanks to their work, it is
becoming clear that superstring theory, supergravity and even the
mysterious `$M$-theory' have strong ties to higher gauge theory.  For
example, they argue that 11-dimensional supergravity can be seen as a
higher gauge theory governed by a certain `Lie 3-superalgebra' which
they call $\sugra(10,1)$.  The number 3 here relates to the 2-brane
solutions of 11-dimensional supergravity: just as parallel transport
of strings is described by 2-connections, the parallel transport of
2-branes is described by 3-connections, which in the supersymmetric
case involve Lie 3-superalgebras.

In fact, $\sugra(10,1)$ is one of a family of four Lie 3-superalgebras
that extend the Poincar\'e Lie superalgebra in dimensions 4, 5, 7 and
11.  These can be built via a systematic construction starting from
the four normed division algebras: the real numbers, the complex
numbers, the quaternions and the octonions \cite{BaezHuerta:susy2}.
These four algebras also give rise to Lie 2-superalgebras extending
the Poincar\'e Lie superalgebra in dimensions 3, 4, 6, and 10.  The
Lie 2-superalgebras are related to superstring theories in dimensions
3, 4, 6, and 10, while the Lie 3-superalgebras are related to
super-2-brane theories in dimensions 4, 5, 7 and 11.  All these
theories, and even their relation to division algebras, have been
known since the late 1980s \cite{Duff}.  Higher gauge theory provides
new insights into the geometry of these theories.  In particular, the
work of D'Auria, Castellani and Fr\'e \cite{TheCube} can be seen as
\emph{implicitly} making extensive use of Lie $n$-superalgebras---but
this only became clear later, through the work of Sati, Schreiber 
and Stasheff \cite{SSS}.

Alas, explaining these fascinating issues in detail would vastly
expand the scope of this paper.  We should instead return to simpler
things: gauge transformations, curvature, and nontrivial 2-bundles.
