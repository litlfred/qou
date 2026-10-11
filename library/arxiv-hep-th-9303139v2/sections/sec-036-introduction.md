---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-036-introduction
section_title: "Introduction"
section_number: null
pages: 4-25
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.742
---
\setcounter{equation}{0}

The purpose of these notes is to review one of the branches of modern string
theory: the theory of matrix models with the emphasize on their intrinsic
integrable structure. We begin with a brief description of the field and
its place in the closest environement within entire string theory.

The main content of the string theory
\footnote{See \cite{UFN} for a general review}
is the study of symmetries in the broadest possible sense of the word
by methods of the quantum field theory. The usual scheme is to start
from some symmetry and construct a field-theoretical model (usually
2-dimensional, for the reason that we do not discuss here),
which possesses this symmetry in some simple sense (e.g. as Noether
symmetry or as a chiral algebra). The main idea at this stage is to
find a model which is exactly solvable (if nothing but the symmetry
is given this is a nice principle to restrict dynamics). The next step
is to study the hidden symmetries of the model, which are somehow
responsible for its exact solvability and are usually much larger
than the original symmetry.

This "inverse" step: {\it model} $\longrightarrow$ {\it symmetry}
can be made at least with three different ideas in mind.

One can look for some hidden local (gauge) symmetry of the model,
which is fixed or spontaneously broken, i.e. identify it with some
other model which had more fields - $auxiliary$ from
the point of view of the smaller model and $gauge$ - from that of
the larger one. (Examples: gauged Wess-Zumi\-no-No\-vikov- Witten (WZNW)
model, topological theories in BRST formalism etc.)

One can take for a new (full) symmetry of the model just its operator
algebra (algebra of observables) (see \cite{KleP},
\cite{W(KleP)} and also \cite{Klepo} for the first results in this
direction). It deserves mentioning that $gauging$ of entire algebra
of observables gives rise to a "string field theory", associated
with original model (considered as a string model).

One can construct effective action of the theory by exact evaluation
of the functional integral.

As to direct step {\it symmetry} $\longrightarrow$ {\it model},
one can take as example the  best understood case, when
original symmetry is just a Lie algebra. Then the quantum mechanical
model can be constructed by geometrical quantization technique (see
\cite{AS} for the most important example of Kac-Moody algebra and
the WZNW model).

{}From the mathematical point of view the two elements of the above
scheme look like {\it algebra} (theory of symmetries) and
{\it Analysis} \& {\it Geometry} (field-theoretical models). The idea of
constructing models with a given symmetry (and nothing else relevant
for the dynamics) can be identified with the mathematical concept of
"universal objects".

\bigskip
\bigskip
\centerline{$|\ \ \ SYMMETRY \ \ \ | \ \ \ \ \ =
                         \ \ \ \ \ |\ \ \ {\bf ALGEBRA}\ \ \ |$}
\bigskip
\centerline{$\ \ \ \uparrow \ \ \ \downarrow\ \
                          \ \ \ \ \ \ \phantom{.................}$}
\bigskip
\centerline{$|\ \ \ \ \ \ \ \ \ MODEL \ \ \ \ \ \ \ \ \ | \ \ \ \ \ =
                   \ \ \ \ \ | \ \ \ {\bf ANALYSIS} \ \ \ \ \ \ |$}
\centerline{$|\ \ with\ this\ symmetry\ \ | \ \ \ \ \ \phantom.
                  \ \ \ \  \ \ \ \ | \ \ \ {\bf GEOMETRY} \ \ \ |$}
\bigskip
\centerline{\it Theory of everything}
\bigskip


The sequence of iterations of the two arrows in the picture leads to
a deaper understanding, enlargening and generalization of all the
notions involved: symmetry, exact solvability, field theory,
geometrical structures, quantization etc, thus stimulating considerable
progress both in physics and mathematics. If this iterative process
can somehow converge, the limit point will deserve the name of the
{\it theory of everything}, which will indeed unify all the
possible field theoretical models by embedding them into a huge, but
well structuired theory, which will be also exactly solvable in some,
yet unspecified sense of the word. We refer to \cite{UFN} for more details
about this semiphilosophical $programm$, known under the name of
(modern) $string$ $theory$, and now turn to a more narrow subject:
the theory of matrix models.

\bigskip

At the moment it is mainly associated with the theory of effective actions,
at least so far this is where the main results of the modern theory
of matrix models find their applications. This technique is especially
suited for the study of effective actions, obtained after integration
over 2-dimensional geometries (including the sum over genera) and
it produces non-perturbative (exact) partition functions of particular
string models. The main result of these studies points out that these
partition functions exhibit two remarkable (though expected \cite{GLM})
properties:

First, effective action for a given model is essentially the $same$ as for any
other model. In fact effective action is a function of coupling constants
("sources" in the old-fashioned terms), which are nothing but coordinates
in the $space\ of$ various $models$ (configuration space of entire string
theory): variation of couplings change one model for another.

Second, effective action possesses a huge additional symmetry, which is
somewhat similar to the general covariance in the space of all models
(the above mentioned configuration space) and in the simplest examples,
which have been studied so far,
can be expressed in terms of integrable hierarchies.
(This "general covariance" in the configuration space can after all turn
into the main dynamical principle of the string theory.)

Both these features seem to be very general, arising whenever the largest
possible Lagrangian with a given symmetry is considered (without restrictions
on the possible counterterms, imposed by requirements of renormalizability
or by locality-minimality "principles" - this is why this phenomenon is
not widely known to field theorists). An example of highly-nontrivial
calculations leading to similar conclusions can be found in ref.\cite{KoS}.

We hope that these remarks will become more clearer after some
specific examples will be considered below. Still they deserve being
fromulated in the full generality, not only to intrigue the reader, but also
because they can serve for better understanding of the ideas and outcomes of
generic string theory.

\bigskip

The "corner" of the string theory, associated with matrix models, can be
described by the following picture: see Fig.1.

\bigskip

The big blocks within the body of string theory, which are directly related
to matrix models are: theory of conformal models, that of the $N=2$
supersymmetry and the (loop-equation version of) the Yang-Mills theory (in any
dimension). Also the Einstein gravity should be related to the subject in a
way, similar to Yang-Mills theory, but these links are yet not clarified.

Both conformal theory and $N=2$ supersymmetry are sources of the concept of
"topological models" \cite{Wito}-\cite{BBRT}.
These arise after gauging of all continuous symmetries
of the WZNW models and/or as models with BRST-exact stress tensors, naturally
appearing in the context of $N=2$ supersymmetry. If formulated in a
self-consisted way in the "universal module space" (unification of module
spaces of all finite-genus Riemann surfaces and bundles over them)
these models turn into those of "topological gravity". Generating functionals
of topological gravity models in fact generate infinite sequences of
topological invariants of certain spaces (inverse definition is also
possible in some cases \cite{Wito}, though the universal (generic) algorithm
for the operation {\it topology of some space} $\longrightarrow$ {\it
topological gravity} is not yet formulated).

Alternative models of $2d$ quantum gravity arise straightforwardly from
conformal models through a procedure of "summation over geometries". There are
two essen\-tially different approaches to the problem. One ("Polyakov
approach") is to make use of the complex structure, intrinsic for conformal
theory \cite{BPZ} and sum over $Riemann$ $surfaces$, what involves integration
over module spaces and sum over genera. The main technique used in this
approach is the theory of free fields on Riemann surfaces \cite{KnUFN},
\cite{MP} and bosonization formalism for conformal field theories \cite{BosF},
\cite{GMMOS}.
This approach requires solution of Liouville theory, which still remains a
problem under intensive investigation (in turn related to conformal field
theory). Further progress in this direction should be related (or can be
expressed in terms of) the adequate theory of the {\it universal module
space}, {\it handle-gluing operators} etc. Similar objects arise in the
field-theoretical approach to the topological gravity (see \cite{LP} for a
recent review).

Alternative approach to summation over geometries does not refer at all to the
complex structure and instead involves a sum over random $equilateral$
triangulations \cite{Migrev}-\cite{mamo}.
\footnote{Its relation to the Polyakov approach is a separate
very interesting, important and badly understood problem, which allows a
non-trivial reformulation in terms of number theory (see \cite{LM}). The main
puzzle here is that equilateral triangulations are in fact $arithmetic$
Riemann surfaces - a dense discrete subset in the entire module space, with
interesting and deap algebraic properties. Equivalence of the two approaches
to $2d$ quantum gravity should imply the existence of some number-theoretical
background behind the scene, which would be very nice to discover in full
purity.}
This is the place where matrix models first appear in the context of string
theory. The random triangulation approach is by no means specific for
conformal models (since it ignores the complex structure) and can be applied
in many other situations - for example, to Yang-Mills (YM) theories in any
dimensions (where instead of summation over geometries one needs "simply" to
sum over ordinary Feynman diagramms).

Applications of the matrix-model method usually involve two steps: formulation
and the study of "discrete" model and then taking its "continuum limit",
giving rise to a new  - "continuous matrix model", which
sometimes can again be represented in a form of some  matrix integral.

One of the main dis\-coveries in the field of mat\-rix models is that
$continuous$
models arising finally from the random-equilateral-triangulation
description of the simplest (minimal with $c<1$) string models coincide with
the simplest ($CP^1$ Landau-Ginzburg)  models of topological gravity
\cite{WitTG},\cite{Ko}-\cite{MMM}: two
(classes of) theories are identical (this is not yet proved in full detail,
but is more than plausible).

So far $continuous$ models are actually found and somehow understood only for
string models, based on the $c<1$ minimal conformal theories (moreover, only
for $q=1$ in the $(p,q)$-seria). Conformal models with $c \geq 1$, which
are relevant for description of gauge theories in space-time dimension
$d \geq 2$ (which possess particles, rather than only topological degrees
of freedom), should give rise to the discrete matrix models with
"non-factorizable" integration over "angular variables", of which the
simplest (solvable) example is Kazakov-Migdal model \cite{KazMi}.
The issue of continuum limit for such models is yet not understood
(at least in terms of integrable structures, which should probably
generalize the familiar theory of Toda hierarchies).

The goal of the study of matrix models is three-fold. First of all, one can
look for the non-perturbative (exact) answers for the physical amplitudes in
the given model. This is the subject which attracts most attention in the
literature (for several obvious reasons). However, it is equally (and, perhaps,
even more) important to understand the mathematical structure behind the
matrix models (which involves topics like general theory of integrable
hierarchies, geometrical quanization, Duistermaat-Heckman theorem
("localization theory") etc). Also important for the purposes of string theory
is to use the results of the study of matrix models in order to unify $a\
priori$ different models (according to the above mentioned principle:
non-perturbative partition functions for different models differ by a change
of variables in the space of coupling constants). Matrix models already played
an important role in making this principle more clear and acceptable for many
string theorists.

\bigskip

Let us make the next step and look even closer at the field of matrix models,
especially, at its mostly studied domain, associated with the $d<2$
string models. Then the following structure will be seen: Fig.2.

\bigskip

The sample example of matrix model is that of 1-matrix integral
\be
Z_N\{t\} \equiv c_N\int_{N\times N}
dH e^{\sum_{k=0}^{\infty} t_k {\rm Tr} H^k},
\label{1mamo}
\ee
where the integral is over $N\times N$ Hermitian matrix $H$ and
$dH = \prod_{i,j} dH_{ij}$.
There are three directions in which one can proceed starting from
(\ref{1mamo}).

The first one \cite{GMMMO}
is to look for an invariant formulation of properties of the
functional $Z_N\{t\}$. It appears to satisfy the infinite set of differential
equations (in fact these are just Ward identities for the functional integral
(\ref{1mamo}) \cite{MM}):
\be
&L_n Z_N\{t\} = 0, \ \ \ n\geq -1, \nn \\
&L_n \equiv \sum_{k=0}^{\infty} kt_k\frac{\partial}{\partial t_{k+n}} +
    \sum_{k=0}^n \frac{\partial^2}{\partial t_k\partial t_{n-k}},
\label{vird} \\
&\frac{\partial}{\partial t_0}Z_N = NZ_N, \nn
\ee
which is known under the name of "discrete Virasoro constraints".
$Z_N\{t\}$ can be represented as a correlator of screening operators in
some auxiliary conformal model (of one free field on the "spectral surface"),
and Virasoro constraints (\ref{vird}) are of course related to the Virasoro
algebra in that conformal model.
Also $Z_N\{t\}$ is some $\tau$-function of integrable "Toda-chain" hierarchy
(in fact this statement should be a corollary of the Virasoro constraints,
but this relation is still not very well understood).

The most straightforward further developement \cite{GMMMO},\cite{MMMM}
is to take the continuum limit
of the Toda-\-chain hierarchy.
In the specially adjusted ("double-scaling") limit
\cite{mamo}) it gives rise to the KdV-hierarchy, and the corresponding
$\tau$-function appears subjected to the slightly different constraints
\cite{FKN},\cite{MMMM}
(which again form a Borel subalgebra of some other "continuous
Virasoro algebra"):
\be
&{\cal L}_{2n} {\cal Z}^{cont}\{T\} = 0, \ \ \ n\geq -1, \nn \\
&{\cal L}_{2n} \equiv \frac{1}{2}\sum_{{\rm odd}\ k=1}^{\infty}
       k(T_k + r_k)\frac{\partial}{\partial T_{k+2n}} +
 \frac{1}{4} \sum_{{\rm odd}\ k = 1}^{2n-1}
\frac{\partial^2}{\partial T_k\partial T_{2n-k}} + \nn \\
&\quad +   \frac{1}{16}\delta_{n,0} + \frac{1}{4} (T_1+r_1)^2\delta_{n,-1},
\label{virc}
\ee
where $r_k = -\frac{2}{3}\delta_{k,3}$.
In fact
\be
{\cal Z}^{cont}\{T\} \sim \left.\lim_{d.s.\{N \rightarrow\infty\}}
\sqrt{Z_N\{t\}} \right|_{t_{2k+1}=0},
\label{coverdi}
\ee
and $T$ are related to $t$ by linear transformation \cite{Kmamo},\cite{MMMM}:
\be


 T_k = \frac{1}{2}\sum_{m\geq \frac{k-1}{2}} \frac{g_m}{(m -\frac{k-1}{2})!}
      \frac{\Gamma(m+\frac{1}{2})}{\Gamma(\frac{k}{2}+1)},  \ \ \ k\ {\rm
odd}; \nn \\
   g_m = mt_{2m},\ m\geq 1;\ \ g_0 = 2N.
\label{Tt1mamo}
\ee
This ${\cal Z}^{cont}\{T\}$ can be again represented in the form of a matrix
integral (over $n\times n$ Hermitian matrix) \cite{Ko},\cite{GKM}-\cite{AvM}:
\be
{\cal Z}^{cont}\{T\} = {\cal Z}_V\{T\}
\label{T=Q}
\ee
with $V(X) = \frac{X^3}{3}$, where
\be
{\cal Z}_V\{T\} \sim {\cal F}_{V,n}\{ L\} \equiv
\int_{n\times n} dX e^{- {\rm tr} V(X) + {\rm tr} L X}
\label{GKM}
\ee
and
\be
T_k = \frac{1}{k} {\rm tr} L^{-k/2},\ \ \  k\ {\rm odd}.
\label{TtK}
\ee
The function ${\cal Z}_V\{T\}$ (but not ${\cal F}_{V,n}\{ L\}$)
is in fact independent of $n$: the only
thing that happens for finite values of $n$ is that the r.h.s. of (\ref{GKM})
can not describe ${\cal Z}_V\{T\}$ at $arbitrary$ points in the $T$-space,
in accordance with (\ref{TtK}). Continuous Virasoro constraints (\ref{virc})
are in fact equivalent to the trivial matrix-valued Ward identity
\be
\left( V'\left(\frac{\partial}{\partial L_{\rm tr}}
\right) -  L\right) {\cal F}_{V,n}\{ L\} = 0.
\label{WiK}
\ee

Another direction to proceed from the discrete 1-matrix model is to rewrite it
identically in the form of Kontsevich model: this time with
$V(X) = X^2$ and additional factor of $(det\ X)^N$ aunder the integral in
${\cal F}_{V,n}\{ L\}$
\cite{ChMa}. Then the double scaling limit can be
studied in internal terms of Kontsevich models \cite{Toda}.

The third direction is towards multimatrix models. In $continuous$
version they should provide $\tau$-functions of reduced KP-hierarchies
\cite{Doug} (KdV is the $p=2$ reduction), which are subjected to
"continuous $W$-constraints" \cite{FKN}. Matrix models of such
$\tau$-functions are Kontsevich models with $V(X) \sim X^{p+1}$
\cite{GKM}-\cite{AvM}. At $discrete$ level, however, things are not so
simple. The most popular discrete multimatrix models  \cite{mumamo}
are defined as the multiple matrix integrals of the form:
\be
\new
\begin{array}{c}
Z_N\{t^{(\alpha)}\} \equiv
 \\
c_N^{p-1}\int_{N\times N} dH^{(1)}...dH^{(p-1)}
\prod_{\alpha = 1}^{p-1} e^{\sum_{k=0}^{\infty}t_k^{(\alpha)}{\rm Tr}
H_{(\alpha)}^k} \prod_{\alpha = 1}^{p-2} e^{{\rm Tr}H^{(\alpha)}H^{(\alpha+1)}}
\label{mumamo}
\end{array}
\ee
(the form of the "interaction term" ${\rm Tr}H^{(\alpha)}H^{(\alpha+1)}$ is
restricted by the "solvability" principle, but not unambiguously).
In fact these models are particular examples of the "scalar-product
eigenvalue models"
and are not really distinguished except for the 1-matrix ($p=2$) and 2-matrix
($p=3$) cases. This is reflected in the absense of any reasonable Ward
identites and integrable structures for these models, which would somehow
involve their dependence on the variables $t^{(\alpha)}$ with $2\leq \alpha
\leq p-2$. Therefore the "multi-scaling continuum limit" of these models can
hardly be
investigated at any degree of rigourousness. (It is not so much important
for "physical" applications to have any discrete models associated with the
continuum ones, but this is an interesting problem for the "science for
science".)
For the 2-matrix ($p=3$) case the Ward identities can be
expressed in the form of "$\tilde W$-constraints" \cite{tildeW} and look like
\cite{GKM}
\be
\tilde W_{n-m}^{(m+1)}\{t\} Z_N\{t,\bar t\} = (-)^{m+n}
\tilde W_{m-n}^{(n+1)}\{\bar t\} Z_N\{t,\bar t\}
\label{Wtilde}
\ee
(here $t$ and $\bar t$ stand for $t^{(1)}$ and $t^{(2)}$, and $m,n$ are any
non-negative integers).

The really interesting set of discrete multimatrix models does exist, but it
is somewhat different from (\ref{mumamo}). These theories will be refered
to as "conformal matrix models", since they arise straightforwardly as
generalization of the "CFT-formulation" of the 1-matrix model \cite{comamo}: it
is enough to substitute discrete Virasoro constraints in the theory of one free
field by the $W_p$-constraints in the theory of $p-1$ free fields. Matrix
integral formulation then involves an "interaction term"
$Det \left(H^{(\alpha)}\otimes I - I \otimes H^{(\alpha+1)}\right)$ instead of
$e^{{\rm Tr}H^{(\alpha)}H^{(\alpha+1)}}$, which is not very easy to guess
$a\ priori$, but so defined models and their continuum limits can be examined
in a manner, quite parallel to the one-matrix case (though not all is already
done in this direction). Also this approach opens a possibility to formulate
discrete models for any set of constraints, e.g. assosiated with the more
exotic
$W$-algebras and with quantum groups (i.e.can help to solve the inverse
problem: $constraints\ \longrightarrow\ discrete\ matrix\ model$). This is an
option which also deserves further investigation. Another natural name for
this set of theoris is "multi-component eigenvalue models".

Kontsevich models should be also related to topological models of
Landau-\-Ginzburg gravity (LGG), though this relation is not yet clarified in
full detail (see, however \cite{Krich},\cite{LP}) .

Among the main unresolved puzzles in this whole field is the description of
generic $(p,q)$-models. Formally, Generalized Kontsevich model (\ref{GKM})
provides this description, but in fact the partition function
($\tau$-function) gets singular when the "phase transition" point where the
$q$ changes is approached, and Kontsevich model with $V(X) = polinomial\ of
\ degree\ p+1$ provides a nice description only of $(p,1)$-models.
Generically, Kontsevich integral describes a duality transformation between
$(p,q)$ and $(q,p)$ models: $(p,q) \longrightarrow (q,p)$ \cite{KhMa}, but not
any of these models separately. (The only exclusion are $(p,1)$-models because
they are related by Kontsevich transformation to the $(1,p)$ models which are
completely trivial.)

In fact continuous models have two $different$ sets of "time-variables".
Thus far we introduced $T$, which are  essentially expansion parameters
of the generating functional for correlation functions. More exact, these
parameters $\hat T$ depend on the particular model (vacuum), around which the
perturbation expansion is performed, and they differ slightly from the
model-independent $T$. Another set of "times",
$r_k = \frac{p}{k(p-k)}{\rm Res}\left(V'(\mu)\right)^{1-\frac{k}{p}}d\mu$,
parametrizes the shape of the polinomial "potential" $V_p(X)$ (of degree
$p+1$) and it describes the coordinates in the space of (matrix)
models. These two types of variables - parameters of the generating
functional and those labeling the shape of the Lagrangian -
are almost the same (in fact they would be
$just$ the same, if there were no loop (quantum) effects). This similarity
between $T$'s and $r$'s is reflected in the remarkable property of partition
function of the $(p,1)$ model  - it essentially
depends only on the {\it sum}  of  "times" $\hat T$ and $r$ \cite{Krich}:
\be
{\cal Z}_{V_p}\{T\} = f_p(r\mid \hat T_k + r_k)\tau_p\{\hat T_k + r_k\}
\label{Krich}
\ee
with some simple (and explicitly known) function $f_p$. (In eq.(\ref{TtK})
above for {\it monomial} cubic potential $V_3(x) = \frac{x^3}{3}$,
$\ \hat T_k = T_k = \frac{1}{k}{\rm tr}L^{-k/2}$, while $r_k =
-\frac{2}{3}\delta_{k,3}$.)

The last thing to be  mentioned in this general description of the field of
the matrix model theory is their relation to group theory. Generalized
Kontsevich model (\ref{GKM}) is intimately connected to the "integrable
nature" of group chracters and the coadjoint orbit integrals (characters of
all the irreducible representations of $U(N)$ are
usually KP $\tau$-functions \cite{chartau}). In fact some "discrete
(or quantum) version"
of Kontsevich integral is a sum over all unitary irreps of $U(n)$ ("integral"
over a $model$ of $U(n)$, or over the set of all coadjoint orbits):
\be
{\cal F}_V^{qu}\{G\} \equiv \sum_R d_R\chi_R(G) e^{-\sum_{k=0}^{\infty}
v_kC_k(R)},
\label{quGKM}
\ee
where $d_R$, $\chi_R$ and $C_k(R)$ stand for dimension, character and the
$k$-th Casimir of irreducible representation $R$ of $U(n)$.
Time variables $T_k \sim
\frac{1}{k}{\rm tr}G^k$, while potential $V(X) = \sum_{k=0}^{\infty}s_kX^k$.
This expression can be further generalized to
\be
{\cal F}_V^{qu}\{G\} \equiv \sum_R \chi_R(\bar G)\chi_R(G)
e^{-\sum_{k=0}^{\infty}v_kC_k(R)}.
\label{quGKM'}
\ee
Properties of these "quantum" Kontsevich models deserve further investigation
(objects like (\ref{quGKM}) are also known to arise in the localization theory,
in particular, in the study of the $d=2$ YM theory, see, for example,
\cite{Wit2YM} and \cite{NT}).

\bigskip

These notes are essentially a review of the views and results of the group,
working at Moscow (and Kiev). Since references will not be given every time,
I present here the list of people involved into these investigations:

L.Chekhov,
A.Gerasimov,
A.Losev,
S.Kharchev,
Yu.Makeenko,
A.Mar\-sha\-kov,
A.Mikhailov,
A.Mironov,
A.Orlov,
S.Pa\-kuliak,
I.Polyubin,
A.Zab\-rodin.

I also apologize for the somewhat sporadic references to the works of other
groups.


\












\bigskip
