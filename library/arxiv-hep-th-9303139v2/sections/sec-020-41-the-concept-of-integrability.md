---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-020-41-the-concept-of-integrability
section_title: "The concept of integrability"
section_number: 4.1
pages: 70-75
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Integrable structure of dynamical system implies that all the dynamical
characteristics - solutions of equations of motion for a classical system and
functional integrals for a quantum one - can be found exactly. According to
this description the notion of integrability is not very concrete, and in fact
it evolves with time, including more and more classes of theories into the
class of integable systems. Nowadays we consider the following types of
theories as clearly belonging to this class:

- Free motion (classical or quantum) on group manifolds and homogeneous
spaces;

- 2-dimensional conformal theories and their "integrable massive deformations";

- Integrable hierarchies of the (multicomponent) KP and Toda type and their
reductions;

- Functional integrals, subjected to conditions of (generalized)
Duistermaat-Heckman theorem;

- (Eigenvalue) matrix models;

- Topological theories;

- Many supersymmetric models (at least those allowing for Nicolai
transformation and/or Duistermaat-Heckman-like description);

- Systems with (infinitely) many local integrals of motion.

This list (nothing to say about the order of items) is rather arbitrary.
Also different items are not really different and (as it should be) can be
considered as different descriptions of the same reality. Now we discuss
very briefly at least some of the most important views on the concept of
integrability.

Often the notion of integrability is related to occurence of "many enough"
integrals of motion ("many enough" means equal to the number of degrees of
freedom). This is, however, not such a rigid definition as one can think.
In fact, in classical mechanics there is usually a complete set of integrals
of motion available: just initial conditions in the phase space (or, to be more
sophisticated, angle-action variables). The problem is, however, that

a) these obvious integrals are very complicated (non-local and multi-valued)
functionals of the $current$ coordinates, and

b) in general situation they are very "unstable" under a small change of
current coordinates ("divergency of trajectories").

In order to avoid these problems one usually imposes a "locality" condition on
equations of motion. While this is a reasonable thing to do for particular
classes of theories (e.g. possessing a well defined kinetic term, which is
quadratic in momenta), this is $not$ a nice decription in general situation,
since "locality" is not invariant under arbitrary (including non-local) change
of variables. In practice, when approached from this side, integrability
implies a kind of "regular" behaviour of trajectories and some more or less
nicel defined transformation from "natural" (or, better to say, "original")
coordinates to the action-angle variables.

Situation becomes even less clear when quantum theory is considered, since
"chaotic behaviour" no longer implies anything really "chaotic" for the quantum
system. Again, very much depends on what kind of observables one wants to
consider, and any notion of "regularity" is not enough under arbitrary
change of variables.

This can be made even more transparent, if one recalls the idea of
universality classes, so important in the modern theory. The idea is
that even in the cases when behaviour of the system seems absolutely haotic
from any naive point of view (like in the cases of turbulence or quantum
gravity), one can and should introduce new variables (which can be very
complicated functions of original ones), which have smooth and well defined
correlation functions. In most cases one is not attempting to find a
$complete$ set of such variables (and thus some information is lost), but this
reflects nothing but the current state of knowledge, and in fact in studies of
$2d$ quantum gravity the $goal$ of $complete$ descrption is already clearly
fromulated.

Despite these comments, the "definition" of integrability in terms of "many
enough" $local$ integrals of motion should be put at the first place in our
discussion, because most of the systems which were so far considered as
integrable more or less naturally get into this class, allowing for some
prefered choice of dynamical variables ("more or less" appears because some
"minor" non-locality is usually present in any interesting examples, where
angle-action variables are not obvious from the very beginning).

This "definition" is so unclear because we attempted to look for a generic
description of integrability. Most interesting approaches, however, go from
another direction. One starts from some simple system and then
perform a change of variables, which makes it looking much more complicated
(being still simple in its essense). This appears to be a much more fruitfull
view on the problem and in fact all the other items of our list above are
describable in this kind of terms.

A trivial, but surprisingly representative example of this approach is
provided by a free particle, moving in flat $D$-dimensional space. The
eigenfunctions of Laplace operator are just plain waves or, equivalently,
spherical harmonics. The radial part of the $j$-th harmonic is already a
not very simple function, satisfying the equation
\be
\left( -\frac{d^2}{dr^2} + \frac{D-1}{r}\frac{d}{dr} +
\frac{C_2(j)}{r^2}\right) \psi(r) = E\psi(r).
\label{ralap}
\ee
This equation is of course less trivial than the original Laplace equation,
but their solutions are related in a simple way. In order to find a solution
of (\ref{ralap}), say, for $j=0$, one should just take an angular average of a
plane wave:
\be
\phi_k(r) = \int e^{ik\vec r\vec\nu}d^{D-1}\vec\nu; \ \ \
\mid\vec\nu\mid = 1.
\ee
This integral representation expresses the solutions of (\ref{ralap}) through
Bessel functions, and this is in fact the proper way to derive the well-known
formula:
\be
\phi_k(r) = 2^{\frac{D}{2}-1}\Gamma\left(\frac{D}{2}\right)
(kr)^{1-\frac{D}{2}} J_{\frac{D}{2}-1}(kr).
\ee
If one expands the exponent in the integral in a series, the standard
expansion for the Bessel function arises.

A slightly more involved example is the quantum mechanical model of a particle
in the potential $e^{-q}$, i.e. the theory of equation
\be
\left(-\frac{d^2}{dq^2} + e^{-q}\right)\psi(q) = 0
\label{exppot}
\ee
(one of course recognizes a simplified version of Toda models).
It can be solved by projection of the simple Sshr\"odinger equation for a
particle, moving on the upper part of the hyperboloid
$x_0^2-x_1^2-x_2^2 = 1;\ \ x_0 > 0$ \cite{OlPe}. If
\be
x_0 = \cosh\frac{q}{2} + \frac{1}{2}z^2e^{q/2}; \ \
x_1 = \sinh \frac{q}{2} - \frac{1}{2}z^2e^{q/2}; \ \
x_2 = ze^{q/2},
\nn
\ee
then $q = \log(x_0+x_1)$, Laplace operator on hyperboloid is
\be
L = \frac{\partial^2}{\partial q^2} - \frac{1}{2}\frac{\partial}{\partial q}
+\frac{1}{4}e^{-q}\frac{\partial^2}{\partial z^2}
\ee
and average of the wave function $\psi_ \lambda(q,z)$
provides the following expression for solutions of (\ref{exppot}):
\be
\psi_ \lambda (q) = e^{i \lambda q}\int_0^{\infty}
t^{2i \lambda -1}e^{-(t+e^q/t)}dt.
\ee

This idea, which is sometimes refered to as "projection method" (see
\cite{OlPe} for a broad review), reveals hidden symmetries of some complicated
systems (which do not possess any symmetry at all in the usual, Noether-like,
sence of the word), by considering them as embedded into wider theories with
more degrees of freedom. Quantum mechanical examples of applicability of the
method are by no means exhausted by the two systems above, one can consider
various projections, starting from (exactly solvable problem of) the free
motion on any group manifold, and in general this gives rise to a very
important
theory of "zonal spherical functions", which nowadays is increasingly
attracting attention because of its obvious links to integrability theory and
quantum geometry (see \cite{Zab} for discussion of the latter relation and
\cite{ZabFKe}, where  also relations with orthogonal polinomials and
Generalized Kontsevich model are partly revealed). An extremely important
example of free motion on a group manifold (in the infinite-dimensional -
Kac-Moody - case) is provided by 2-dimensional WZNW
(Wess-\-Zumino-\-Novikov-\-Witten) model and the corresponding version of
projection method is known as  Hamiltonian reductions in conformal
field theory. Again the resulting theories (like minimal conformal models) do
not possess any kind of symmetry in the usual sense of the word, but still
they are very simple and exactly solvable, remembering their origin in the
theory of free fields.

In principle the theory which is reduced, i.e. complemented by constraints
(initial conditions), does not need to be absolutely symmetric, i.e. to have
Casimir operator or even zero (as in the WZNW case) as its Hamiltonian. It can
be in fact possible to use the projection method to gain a lot of information
about reductions of theories with more sophisticated Hamiltonians, which are
non-trivial functions of group generators. The simplest example is provided by
the theory of quantum-mechanical "quasi-exactly-solvable models"
\cite{QES},\cite{Turb1} and its CFT-generalizations \cite{Turb1},\cite{Halp}.
A more elaborated technique has the name of "localization theory",\footnote{
For various views and approaches to this theory see \cite{KhCh},\cite{STS},
\cite{AFS},\cite{AS},
\cite{DH}.\cite{NiDH},\cite{Wit2YM}, \cite{NT},\cite{NP}.
(So far there are no connections with Andersson localization in the solid state
physics.)
}
(known also as geometrical quantization, Fourier analysis on group manifolds
and Duistermaat-Heckman theory), it provides a very wide generalization of the
above averaging procedure, which maped plain waves into Bessel functions. The
classical sample system to illustrate all the aspects of integrability,
starting from free motion and ending with anyonic statistics,
$W_\infty$-algebras and $2d$ Yang-Mills theory, is the Calogero-Sutherland
system, which can be associated in a uniform way with any simple Lie algebras
and in an "intermediately involved" form looks like a multiparticle theory
in 1+1 dimension with interaction potential
$g^2\sin^{-2}\epsilon (x_i-x_j)$. (See \cite{OlPe} for the introduction to the
theory of Calogero-type models and \cite{Vas},\cite{GoNe} for the new
developements.)

All this discussion was necessary just to illustrate a very simple idea: the
theory of free particles, though trivial, is in fact unexhaustively deep. It is
enough to impose sophisticated initial conditions or perform a sophisticated
change of variables in order to obtain very complicated dynamical systems,
which after they are studied $per\ se$ appear to be surprisingly system, the
reason for this simplicity being that the real underlying dynamics is just
trivial - that of the free particles,- though it may be very hard probelm to
reveal this simplicity when the system is given.
It is advantage of the $general$ theory, that one can begin from the proper
side: just from the theory of free particles and just start making it more and
more complicated, by introducing different kind of variables, considering
correlators of sophisticated operators and so on. Everything what can be
obtained in this way is by definition trivially integrable, though it may be
not so simple to guess for somebody who did not know where the particular
system at the end of this procedure appeared from.

We now proceed to discussion of particularly important realization of this
idea: the theory of $\bar\partial$-operators in $1_C$ dimension (i.e. the
theory of free holomorphic fields in 2 real dimensions). When considered as
functions of moduli of the bundles over Riemann surfaces (i.e. of boundary
conditions, imposed on $2d$ free fields), these simple objects (known as
"$\tau$=functions") start looking a little involved and after all appear
related to sophisticated non-linear equations (but of course integrable)
in 2 and 3 dimensions (like KdV or Kadomtsev-Petvishvili (KP) equation).
We do not attempt to present an exhaustive theory of $\tau$-functions and
integrable hierarchies (besides being still uncompleted, this is a very big
field), but instead concentrate on the very core of it, which is just simple
determinant formulas for the simplest $\tau$-functions (namely, associated
with free-fermion theory and level $k=1$ Kac-Moody algebras). This issue will
be discussed in some details, because besides being the basis of integrable
hierarchies theory, it is also exactly the place, where the links with the
matrix models are found.
