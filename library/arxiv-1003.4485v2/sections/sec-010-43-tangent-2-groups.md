---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-010-43-tangent-2-groups
section_title: "Tangent 2-Groups"
section_number: 4.3
pages: 33-37
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.997
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{tangent}

We have seen that any group representation gives a 2-group.  But any
Lie group $G$ has a representation on its own Lie algebra: the adjoint
representation.  This lets us build a 2-group from the crossed module
where:
\begin{itemize}
\item $G$ is any Lie group,
\item $H$ is $\g$ regarded as a vector space and thus an abelian
Lie group, 
\item $\alpha$ is the adjoint representation, and
\item $t$ is trivial.
\end{itemize}
We call this the \define{tangent 2-group} $\T G$ of the Lie group $G$.
Why?  We have already seen that for any Lie 2-group, the group of all
2-morphisms is the semidirect product $G \ltimes H$.  In the case at
hand, this semidirect product is just $G \ltimes \g$, with $G$ acting
on $\g$ via the adjoint representation.  But as a manifold, this
semidirect product is nothing other than the tangent bundle $TG$ of
the Lie group $G$.  So, the tangent bundle $TG$ becomes a group, and
this is the group of 2-morphisms of $\T G$.

By Theorem~\ref{thm:2-connections}, a 2-connection on a trivial $\T
G$-2-bundle consists of a $\g$-valued 1-form $A$ and a $\g$-valued 
2-form $B$ such that the curvature $F = dA + A \wedge A$ satisfies
\[   F = 0, \]
since $\dt(B) = 0$ in this case.  Where can we find such 2-connections?
We can find them as solutions of a field theory called 4-dimensional
$BF$ theory!

$BF$ theory is a classical field theory that works in any dimension.
So, take an $n$-dimensional oriented manifold $M$ as our spacetime.
The fields in $BF$ theory are a connection $A$ on the trivial
principal $G$-bundle over $M$, together with a $\g$-valued
$(n-2)$-form $B$.  The action is given by
\[  S(A,B) = \int_M \tr(B \wedge F) .\]
Setting the variation of this action equal to zero, we obtain the
following field equations:
\[ dB + [A,B] = 0, \quad F = 0. \]
In dimension 4, $B$ is a $\g$-valued 2-form---and thanks to the
second equation, $A$ and $B$ fit together to define a 
2-connection on the trivial $\T G$-2-bundle over $M$.  

It may seem dull to study a gauge theory where the equations of motion
imply the connection is flat.  But there is still room for some fun.
We see this already in 3-dimensional $BF$ theory, where $B$ is a
$\g$-valued 1-form rather than a 2-form.  This lets us package $A$ 
and $B$ into a connection on the trivial $TG$-bundle over $M$.  The 
field equations
\[ dB + [A,B] = 0, \quad F = 0 \]
then say precisely that this connection is flat.

When the group $G$ is the Lorentz group $\SO(2,1)$, $TG$ is the
corresponding Poincar\'e group.  With this choice of $G$, 3d $BF$
theory is a version of 3d general relativity.  In 3 dimensions, unlike
the more physical 4d case, the equations of general relativity say
that spacetime is \emph{flat} in the absence of matter.  And at first
glance, 3d $BF$ theory only describes general relativity without
matter.  After all, its solutions are flat connections.

Nonetheless, we can consider 3d $BF$ theory on a manifold from which
the worldline of a point particle has been removed.  In the Bohm--Aharonov
effect, if we carry a charged object around a solenoid, we obtain a
nontrivial phase even though the $\U(1)$ connection $A$ is flat outside
the solenoid.  Similarly, in 3d $BF$ theory, the connection $(A,B)$ will 
be flat away from the particle's worldline, but it can have a nontrivial 
holonomy around a loop $\gamma$ that encircles the worldline:
\[
\xy
(0,0)*\ellipse(6,2){-};
(8,-3)*{\gamma};
(0,-15)*{};(0,-3)*{} **\dir{-};
(0,-1)*{};(0,15)*{} **\dir{-};
\endxy
\]
This holonomy says what happens when we parallel transport an object
around our point particle.   The holonomy is an element of the Poincar\'e
group.  Its conjugacy class describes the \emph{mass} and \emph{spin} 
of our particle.  So, massive spinning point particles are lurking 
in the formalism of 3d $BF$ theory!

Even better, this theory predicts an upper bound on the particle's
mass, roughly the Planck mass.  This is true even classically.  This
may seem strange, but unlike in 4 dimensions, where we need $c$,
$G_{\textrm{{\tiny Newton}}}$ and $\hbar$ to build a quantity with
dimensions of length, in 3-dimensional spacetime we can do this using
only $c$ and $G_{\textrm{{\tiny Newton}}}$.  So, ironically, the
`Planck mass' does not depend on Planck's constant.

Furthermore, in this theory, particles have `exotic statistics',
meaning that the interchange of identical particles is 
governed by the braid group instead of the symmetric group.  
Particles with exotic statistics are also known as `anyons'.  
In the simplest examples, the anyons in 3d gravity reduce to 
bosons or fermions in the $G_{\textrm{{\tiny Newton}}} \to 0$ 
limit.

There is thus a wealth of interesting phenomena to be studied
in 3d $BF$ theory.  See the paper by Baez, Crans and Wise
\cite{BaezCransWise} for a quick overview, and the work of 
Freidel, Louapre and Baratin for a deep treatment of the details
\cite{BaratinFreidel:3d,FreidelLouapre}.

The case of 4d $BF$ theory is just as interesting, and not as fully
explored.  In this case the field equations imply that $A$
and $B$ define a 2-connection on the trivial $\T G$-2-bundle over $M$.
But in fact they say more: they say precisely that this 2-connection
is \define{flat}.  By this we mean two things.  First, the holonomy
$\hol(\gamma)$ along a path $\gamma$ does not change when we change
this path by a homotopy.  Second, the holonomy $\hol(\Sigma)$ along a
surface $\Sigma$ does not change when we change this surface by a
homotopy.  The first fact here is equivalent to the equation $F = 0$.
The second is equivalent to the equation $dB + [A,B] = 0$.

When the group $G$ is the Lorentz group $\SO(3,1)$, 4d $BF$ theory is
sometimes called `topological gravity'.  We can think of it as a
simplified version of general relativity that acts more like gravity
in 3 dimensions.  In particular, we can copy what we did in 3
dimensions, and consider 4d $BF$ theory on a manifold from which the
worldlines of particles \emph{and the worldsheets of strings} have
been removed.  Some of what we will do here works for more general
groups $G$, but let us take $G = \SO(3,1)$ just to be specific.

First consider strings.  Take a 2-dimensional manifold $X$ embedded
in a 4-dimensional manifold $M$, and think of $X$ as the
worldsheet of a string.  Suppose we can find a small loop $\gamma$ that 
encircles $X$ in such a way that $\gamma$ is contractible in $M$ 
but not in $M - X$.  If we do 4d $BF$ theory on the spacetime $M - X$, the
holonomy
\[    \hol(\gamma) \in \SO(3,1)  \] 
will not change when we apply a homotopy to $\gamma$.  This holonomy
describes the `mass density' of our string \cite{BaezCransWise,
Balachandran2}.

Next, consider particles.  Take a curve $C$ embedded in $M$, and think
of $C$ as the worldline of a particle.  Suppose we can find a small 2-sphere
$\Sigma$ in $M - C$ that is contractible in $M$ but not $M - C$.  We
can think of this 2-sphere as a 2-morphism $\Sigma \maps 1_x \To 1_x$
in the path 2-groupoid of $M$.  If we do 4d $BF$ theory on the
spacetime $M - C$, the holonomy
\[     \hol(\Sigma) \in \so(3,1) \] 
will not change when we apply a homotopy to $\Sigma$.  So, this
holonomy describes some information about the particle---but so
far as we know, the physical meaning of this information has not been
worked out.  

What if we had a field theory whose solutions were flat 2-connections
for the Poincar\'e 2-group?  Then we would have 
\[     \hol(\Sigma) \in \R^4 \] 
and there would be a tempting interpretation of this quantity: namely,
as the energy-momentum of our point particle.  So, the puzzle posed at
the end of the previous section is a tantalizing one.

One may rightly ask if the `strings' described above bear any relation
to those of string theory.  If they are merely surfaces cut out of
spacetime, they lack the dynamical degrees of freedom normally
associated to a string. Certainly they do not have an action
proportional to their surface area, as for the Polyakov string.
Indeed, one may ask if `area' even makes sense in 4d $BF$ theory.
After all, there is no metric on spacetime: the closest substitute is
the $\so(3,1)$-valued 2-form $B$.

Some of these problems may have solutions.  For starters, when
we remove a surface $X$ from our 4-manifold $M$, the action 
\[ S(A,B) = \int_{M-X} \tr(B \wedge F) \]
is no longer gauge-invariant: a gauge transformation changes the
action by a boundary term which is an integral over $X$.  We can
remedy this by introducing fields that live on $X$, and adding a term
to the action which is an integral over $X$ involving these fields.
There are a number of ways to do this \cite{BaezPerez, Fairbairn,
GirelliPfeifferPopescu, FNS, MP}.  For some, the integral over $X$ is
proportional to the area of the string worldsheet in the special case
where the $B$ field arises from a cotetrad (that is, an $\R^4$-valued
1-form) as follows:
\[           B = e \wedge e  \]
where we use the isomorphism $\Lambda^2 \R^4 \iso \so(3,1)$.  
In this case there is close relation to the Nambu--Goto string,
which has been carefully examined by Fairbairn, Noui and Sardelli
\cite{FNS}.  

This is especially intriguing because when $B$ takes
the above form, the $BF$ action becomes the usual Palatini action
for general relativity:
\[  S(A,e) = \int_M \tr(e \wedge e \wedge F) \]
where `$\tr$' is a suitable nondegenerate bilinear form on $\so(3,1)$.
Unfortunately, solutions of Palatini gravity typically \emph{fail} to
obey the condition $\dt(B) = F$ when we take $B = e \wedge e$.  So, we
cannot construct 2-connections in the sense of Theorem
\ref{thm:2-connections} from these solutions!  If we want to treat
general relativity in 4 dimensions as a higher gauge theory, we need
other ideas.  We describe two possibilities at the end of Section
\ref{automorphism}.
