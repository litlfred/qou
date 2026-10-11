---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-007-41-shifted-abelian-groups
section_title: "Shifted Abelian Groups"
section_number: 4.1
pages: 27-33
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.996
---
\label{abelian}

Any group $G$ automatically gives a 2-group where $H$ is 
trivial.  Then higher gauge theory reduces to ordinary gauge theory.  
But to see what is \emph{new} about higher gauge theory, let us
instead suppose that $G$ is the trivial group. 
Then $t$ and $\alpha$ are forced to be trivial, and $t$ is
automatically $G$-equivariant.  On the other hand, the Peiffer identity
\[
	\alpha(t(h))h'  =  hh'h^{-1} 
\]
is not automatic: it holds if and only if $H$ is abelian!  

There is also a nice picture proof that $H$ must be abelian when
$G$ is trivial.  We simply move two elements of $H$ around each other
using the interchange law:
	\begin{eqnarray*}
	\xy
	(-16,0)*+{\bullet}="4";
	(0,0)*+{\bullet}="6";
	{\ar@/^1.65pc/^1 "6";"4"};
	{\ar@/_1.65pc/_1 "6";"4"};
	{\ar@{=>}_<<<{h} (-8,3)*{};(-8,-3)*{}};
	(0,0)*+{\bullet}="4";
	(16,0)*+{\bullet}="6";
	{\ar@/^1.65pc/^1 "6";"4"};
	{\ar@/_1.65pc/_1 "6";"4"};
	{\ar@{=>}^<<<{h'} (8,3)*{};(8,-3)*{}};
	\endxy
	& = & 
	\xy
	(-16,0)*+{\bullet}="4";
	(0,0)*+{\bullet}="6";
	{\ar "6";"4"};
	{\ar@/^1.75pc/ "6";"4"};
	{\ar@/_1.75pc/ "6";"4"};
	{\ar@{=>}^<<<{h} (-8,6)*{};(-8,1)*{}};
	{\ar@{=>}^<<{1} (-8,-1)*{};(-8,-6)*{}};
	(0,0)*+{\bullet}="4";
	(16,0)*+{\bullet}="6";
	{\ar "6";"4"};
	{\ar@/^1.75pc/ "6";"4"};
	{\ar@/_1.75pc/ "6";"4"};
	{\ar@{=>}^<<<{1} (8,6)*{};(8,1)*{}} ;
	{\ar@{=>}^<<{h'} (8,-1)*{};(8,-6)*{}} ;
	\endxy
	\\
	& = &
	\xy 
	(-8,0)*+{\bullet}="4"; 
	(8,0)*+{\bullet}="6"; 
	{\ar@/^1.75pc/ "6";"4"}; 
	{\ar "6";"4"};
	{\ar@/_1.75pc/ "6";"4"};
	{\ar@{=>}^<<{h} (0,6)*{};(0,1)*{}} ;
	{\ar@{=>}^<<{h'} (0,-1)*{};(0,-6)*{}} ;
	\endxy
	\\
	& = &
	\xy
	(-16,0)*+{\bullet}="4";
	(0,0)*+{\bullet}="6";
	{\ar "6";"4"};
	{\ar@/^1.75pc/ "6";"4"};
	{\ar@/_1.75pc/ "6";"4"};
	{\ar@{=>}^<<<{1} (-8,6)*{};(-8,1)*{}};
	{\ar@{=>}^<<{h'} (-8,-1)*{};(-8,-6)*{}};
	(0,0)*+{\bullet}="4";
	(16,0)*+{\bullet}="6";
	{\ar "6";"4"};
	{\ar@/^1.75pc/ "6";"4"};
	{\ar@/_1.75pc/ "6";"4"};
	{\ar@{=>}^<<<{h} (8,6)*{};(8,1)*{}} ;
	{\ar@{=>}^<<{1} (8,-1)*{};(8,-6)*{}} ;
	\endxy
	\\
	& = & 
	\xy
	(-16,0)*+{\bullet}="4";
	(0,0)*+{\bullet}="6";
	{\ar@/^1.65pc/ "6";"4"};
	{\ar@/_1.65pc/ "6";"4"};
	{\ar@{=>}^<<<{h'} (-8,3)*{};(-8,-3)*{}};
	(0,0)*+{\bullet}="4";
	(16,0)*+{\bullet}="6";
	{\ar@/^1.65pc/ "6";"4"};
	{\ar@/_1.65pc/ "6";"4"};
	{\ar@{=>}^<<<{h} (8,3)*{};(8,-3)*{}};
	\endxy
	\end{eqnarray*}
As a side-benefit, we see that horizontal and vertical
composition must be equal when $G$ is trivial.  This proof is called
the `Eckmann--Hilton argument', since Eckmann and Hilton used it to
show that the second homotopy group of a space is abelian \cite{EH}.

So, we can build a 2-group where:
\begin{itemize}
\item $G$ is the trivial group,
\item $H$ is any abelian Lie group, 
\item $\alpha$ is trivial, and
\item $t$ is trivial.
\end{itemize}
This is called the \define{shifted} version of $H$, 
and denoted $\mathrm{b}H$.  

In applications to physics, we often see $H = \U(1)$.  A principal
$\mathrm{b}\U(1)$-2-bundle is usually called a \define{\boldmath
$\U(1)$ gerbe}, and a 2-connection on such a thing is usually just
called a connection.  By Theorem~\ref{thm:2-connections}, a
connection on a trivial $\U(1)$ gerbe is just an ordinary
real-valued 2-form $B$.  Its holonomy is given by:
\[
\begin{array}{rccl}
 \hol \maps& \xymatrix{ \bullet &
  \bullet \ar@/_0.5pc/[l]_{\gamma}  
} 
\quad &\mapsto & \quad 1 
\\ 
\\
\hol  \maps &
	{\xy
	(-16,0)*+{\bullet}="4";
	(0,0)*+{\bullet}="6";
	{\ar@/^1.65pc/ "6";"4"};
	{\ar@/_1.65pc/ "6";"4"};
	{\ar@{=>}^<<<{\scriptstyle \Sigma} (-8,3)*{};(-8,-3)*{}};
	\endxy}
\quad	&\mapsto & 
	\displaystyle{\exp\left( {i \int_\Sigma B} \right)} \in \U(1).
\end{array}
\]

The book by Brylinski \cite{Brylinski} gives a rather extensive
introduction to $\U(1)$ gerbes and their applications.  Murray's
theory of `bundle gerbes' gives a different viewpoint \cite{Murray,
Stevenson}.  Here let us discuss two places where $\U(1)$ gerbes
show up in physics.  One is `multisymplectic geometry'; the other is
`2-form electromagnetism'.  The two are closely related.

First, let us remember how 1-forms show up in symplectic geometry and
electromagnetism.  Suppose we have a point particle moving in some
manifold $M$.  At any time its position is a point $q \in M$ and its
momentum is a cotangent vector $p \in T^*_q M$.  As time passes, its
position and momentum trace out a curve
\[              \gamma \maps [0,1] \to T^* M  . \]
The action of this path is given by
\[ S(\gamma) = \int_\gamma \left( p_i \dot{q}^i - H(q, p) \right) \, dt \]
where $H \maps T^* M \to \R$ is the Hamiltonian.  But now suppose
the Hamiltonian is zero!  Then there is still a nontrivial action, 
due to the first term.  We can rewrite it as follows:
\[     S(\gamma) = \int_\gamma \alpha \]
where the 1-form
\[          \alpha = p_i dq^i  \]
is a canonical structure on the cotangent bundle.  We can think of 
$\alpha$ as connection on a trivial $\U(1)$-bundle over $T^* M$.
Physically, this connection describes how a quantum particle changes
phase even when the Hamiltonian is zero!  The change in phase is
computed by exponentiating the action.  So, we have:
\[     \hol(\gamma) = \exp \left( i \int_\gamma \alpha \right)  .\]

Next, suppose we carry our particle around a small loop $\gamma$ 
which bounds a disk $D$.  Then Stokes' theorem gives
\[
	S(\gamma) =  \int_\gamma \alpha
                  =  \int_D  d \alpha
\]
Here the 2-form 
\[        \omega = d \alpha = dp_i \wedge dq^i  \]
is the curvature of the connection $\alpha$.  It makes $T^*M$ into
a \define{symplectic manifold}, that is, a manifold with a
closed 2-form $\omega$ satisfying the nondegeneracy condition 
\[       \forall v \; \omega(u, v) = 0 \; \Longrightarrow \; u = 0  .\]
The subject of symplectic geometry is vast and deep, but sometimes
this simple point is neglected: the symplectic structure describes
the \emph{change in phase} of a quantum particle as we move it around a
loop:
\[         \hol(\gamma) =  \exp \left( i \int_D \omega \right) .\] 
Perhaps this justifies calling a symplectic manifold a `phase
space', though historically this seems to be just a coincidence.

It may seem strange to talk about a quantum particle tracing out a
loop in phase space, since in quantum mechanics we cannot
simultaneously know a particle's position and momentum.  However,
there is a long line of work, beginning with Feynman, which computes
time evolution by an integral over paths in phase space \cite{DMN}.
This idea is also implicit in geometric quantization, where the first
step is to equip the phase space with a principal $\U(1)$-bundle
having a connection whose curvature is the symplectic structure.  (Our
discussion so far is limited to \emph{trivial} bundles, but everything
we say generalizes to the nontrivial case.)

Next, consider a charged particle in an electromagnetic field.
Suppose that we can describe the electromagnetic field using a vector
potential $A$ which is a connection on trivial $\U(1)$ bundles over
$M$.  Then we can pull $A$ back via the projection $\pi \maps T^\ast M
\to M$, obtaining a 2-form $\pi^*\!A$ on phase space.  In the absence
of any other Hamiltonian, the particle's action as we move it
along a path $\gamma$ in phase space will be
\[    S(\gamma) =   \int_\gamma \alpha + e\,\pi^*\!A  \]
if the particle has charge $e$.  In short, \textit{the
electromagnetic field changes the connection on phase space}
from $\alpha$ to $\alpha + e\, \pi^*\!A$.  Similarly, when the path $\gamma$ 
is a loop bounding a disk $D$, we have
\[    S(\gamma) = \int_D \omega + e\,\pi^*\!F   \]
where $F = dA$ is the electromagnetic field strength.  So,
electromagnetism also changes the symplectic structure on phase
space from $\omega$ to $\omega + e \, \pi^*\!F$.  For more on this, see
Guillemin and Sternberg \cite{GS}, who also treat the case of
nonabelian gauge fields.

All of this has an analog where particles are replaced by strings.  It
has been known for some time that just as the electromagnetic vector
potential naturally couples to point particles, there is a 2-form $B$
called the Kalb--Ramond field which naturally couples to strings.  The
action for this coupling is obtained simply by integrating $B$ over
the string worldsheet.  In 1986, Gawedski \cite{Gawedski} showed that
the $B$ field should be seen as a connection on a $\U(1)$ gerbe.
Later Freed and Witten \cite{FreedWitten} showed this viewpoint was
crucial for understanding anomaly cancellation.  However, these
authors did not actually use the word `gerbe'.  The role of gerbes was
later made explicit by Carey, Johnson and Murray \cite{CJM}, and even
more so by Gawedski and Reis \cite{GawedskiReis}.

In short, electromagnetism has a `higher version'.  What about
symplectic geometry?  This also has a higher version, which dates back to
1935 work by DeDonder \cite{DeDonder} and Weyl \cite{Weyl}.  The idea
here is that an $n$-dimensional classical field theory has a kind of
finite-dimensional phase space equipped with a closed $(n+2)$-form
$\omega$ which is \define{nondegenerate} in the following sense:
\[       \forall v_1,\dots,v_{n+1} \; \; \omega(u, v_1, \dots, v_n) = 0 
\quad \Longrightarrow \quad u = 0  .\]
Such a $n$-form is called a \define{multisymplectic structure}, or
more specifically, an \define{$n$-plectic structure} For a nice
introduction to multisymplectic geometry, see the paper by Gotay,
Isenberg, Marsden, and Montgomery \cite{GIMM}.

The link between multisymplectic geometry and higher electromagnetism
was made in a paper by Baez, Hoffnung and Rogers
\cite{BaezHoffnungRogers}.  Everything is closely analogous to the
story for point particles.  For a classical bosonic string propagating
on Minkowski spacetime of any dimension, say $M$, there is a
finite-dimensional manifold $X$ which serves as a kind of `phase
space' for the string.  There is a projection $\pi \maps X \to M$, and
there is a god-given way to take any map from the string's worldsheet
to $M$ and lift it to an embedding of the worldsheet in $X$.  So, let
us write $\Sigma$ for the string worldsheet considered as a surface in
$X$.

The phase space $X$ is equipped with a 2-plectic structure: that is, a
closed nondegenerate 3-form, say $\omega$.  But in fact, $\omega = d
\alpha$ for some 2-form $\alpha$.  Even when the string's Hamiltonian
is zero, there is a term in the action of the string coming from the
integral of $\alpha$:
\[          S(\Sigma) = \int_{\Sigma} \alpha .\]
We may also consider a charged string coupled to a Kalb--Ramond field.
This begins life as a 2-form $B$ on $M$, but we may pull it back to a 
2-form $\pi^*\!B$ on $X$, and then
\[    S(\Sigma) =   \int_\Sigma \alpha + e\,\pi^*\!B.  \]
In particular, suppose $\Sigma$ is a 2-sphere bounding a 3-ball 
$D$ in $X$.  Then by Stokes' theorem we have
\[    S(\Sigma) =   \int_D \omega + e\,\pi^*\!Z  \]
where the 3-form
\[         Z = dB  \]
is the Kalb--Ramond analog of the electromagnetic field strength,
and $e$ is the string's charge.  (The Kalb--Ramond field strength 
is usually called `$H$' in the physics literature, but that conflicts 
with our usage of $H$ to mean a Lie group, so we shall call it `$Z$'.) 

In summary: \emph{the Kalb--Ramond field modifies the 2-plectic 
structure on the phase space of the string}.
The reader will note that we have coyly refused to describe the phase
space $X$ or its 2-form $\alpha$.  For this, see the paper by Baez,
Hoffnung and Rogers \cite{BaezHoffnungRogers}.  In this paper, we
explain how the usual dynamics of a classical bosonic string coupled
to a Kalb--Ramond field can be described using multisymplectic
geometry.  We also explain how to generalize Poisson brackets from
symplectic geometry to multisymplectic geometry.  Just as Poisson
brackets in symplectic geometry make the functions on phase space into
a Lie algebra, Poisson brackets in multisymplectic geometry give rise
to a `Lie 2-algebra'.  Lie 2-algebras are also important in higher
gauge theory in the same way that Lie algebras are important for gauge
theory.  Indeed, the `string 2-group' described in Section
\ref{string} was constructed only after its Lie 2-algebra was found
\cite{BaezCrans}.  Later, this Lie 2-algebra was seen to arise
naturally from multisymplectic geometry \cite{BaezRogers}.


\subsection{The Poincar\'e 2-Group}
\label{poincare}

Suppose we have a representation $\alpha$ of a Lie group $G$ on a
finite-dimensional vector space $H$.  We can regard $H$ as an abelian
Lie group with addition as the group operation.  This lets us
regard $\alpha$ as an action of $G$ on this abelian Lie group.
So, we can build a 2-group $\G$ where:
\begin{itemize}
\item $G$ is any Lie group,
\item $H$ is any vector space,
\item $\alpha$ is the representation of $G$ on $H$, and
\item $t$ is trivial.
\end{itemize}
In particular, note that the Peiffer identity holds.  In this way, we
see that any group representation gives a crossed module---so group
representations are secretly 2-groups!

For example, if we let $G$ be the Lorentz group and let $\alpha$ be
its obvious representation on $\R^4$:
\[ G = \SO(3,1) \]
\[ H = \R^4 \]
we obtain the so-called \define{Poincar\'e 2-group}, which has the
Lorentz group as its group of morphisms, and the Poincar\'e group as
its group of 2-morphisms \cite{BaezLauda:2groups}.

What is the Poincar\'e 2-group good for?  It is not clear, but there
are some clues.  Just as we can study representations of groups on
vector spaces, we can study representations of 2-groups on `2-vector
spaces' \cite{BBFW, BarrettMackaay,CraneYetter,Elgueta2}.  The
representations of a group are the objects of a category, and this
sort of category can be used to build `spin foam models' of
background-free quantum field theories \cite{Baez:spinfoam}.  This
endeavor has been most successful with 3d quantum gravity
\cite{FreidelLouapre}, but everyone working on this subject dreams
of doing something similar for 4d quantum gravity \cite{Rovelli}.
Going from groups to 2-groups boosts the dimension of everything:
the representations of a 2-group are the objects of a
\emph{2-category}, and Crane and Sheppeard outlined a program for
building a 4-dimensional spin foam model starting from the 2-category of
representations of the Poincar\'e 2-group \cite{CraneSheppeard}.

Crane and Sheppeard hoped their model would be related to quantum
gravity in 4 spacetime dimensions.  This has not come to pass, at least
not yet---but this spin foam model \textit{does} have interesting
connections to 4d physics.  The spin foam model of 3d quantum gravity
automatically includes point particles, and Baratin and Freidel have
shown that it reduces to the usual theory of Feynman diagrams in 3d
Minkowski spacetime in the limit where the gravitational constant
$G_{\textrm{{\tiny Newton}}}$ goes to zero \cite{BaratinFreidel:3d}.
This line of thought led Baratin and Freidel to construct a spin foam
model that is equivalent to the usual theory of Feynman diagrams in 4d
Minkowski spacetime \cite{BaratinFreidel:4d}.  At first the
mathematics underlying this model was a bit mysterious---but it now
seems clear that this model is based on the representation theory of
the Poincar\'e 2-group!  For a preliminary report on this fascinating
research, see the paper by Baratin and Wise \cite{BaratinWise}.

In short, it appears that the 2-category of representations of the
Poincar\'e 2-group gives a spin foam description of quantum field
theory on 4d Minkowski spacetime.  Unfortunately, while spin foam
models in 3 dimensions can be obtained by quantizing gauge theories,
we do not see how to obtain this 4d spin foam model by quantizing a
higher gauge theory.  Indeed, we know of no classical field theory in
4 dimensions whose solutions are 2-connections on a principal
$\G$-2-bundle where $\G$ is the Poincar\'e 2-group.

However, if we replace the Poincar\'e 2-group by a closely related
2-group, this puzzle \emph{does} have a nice solution.  Namely, if
we take 
\[ G = \SO(3,1) \]
\[ H = \so(3,1) \]
and take $\alpha$ to be the adjoint representation, we obtain the
`tangent 2-group' of the Lorentz group.  As we shall see,
2-connections for this 2-group arise naturally as solutions of a 
4d field theory called `topological gravity'.
