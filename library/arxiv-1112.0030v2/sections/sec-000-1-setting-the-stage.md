---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-000-1-setting-the-stage
section_title: "Setting the stage"
section_number: 1
pages: 1-7
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.983
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
\label{sec:intro}

Quantum knot invariants were introduced in 1980's \cite{RT,Witt}:
for every representation $R$ of a Lie algebra $\g$, one can define a polynomial invariant $\bar{P}^{\g,R}(K)$ of a knot $K$.
Its {\it reduced} version is
\be
{P}^{\g,R}(K) \; = \; \frac{\bar{P}^{\g,R}(K)}{\bar{P}^{\g,R}({\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,})} \,,
\ee
where ${\,\raisebox{-.08cm}{\includegraphics[width=.4cm]{unknot}}\,}$ denotes the unknot.

A categorification of the polynomial ${P}^{\g,R}(K)$ (or its {\it unreduced} version $\bar{P}^{\g,R}(K)$)
is a doubly-graded homology theory\footnote{All homologies in this paper are defined over $\Q$.}
${\CH}^{\g,R}(K)$ whose graded Euler characteristic is equal to ${P}^{\g,R}(K)$.
In other words, if ${\CP}^{\g,R}(K)(q,t)$ denotes the Poincar\'e polynomial of ${\CH}^{\g,R}(K)$, then we have
\[
P^{\g,R}(K)(q) \; = \; \CP^{\g,R}(K)(q,t=-1) \,.
\]
Unlike ${P}^{\g,R}(K)$, the explicit combinatorial definition of ${\CH}^{\g,R}(K)$ exists for very few choices of $\g$ and $R$.
However, physics insights based on BPS state counting and Landau-Ginzburg theories predict
various properties and a very rigid structure of these homology theories.

One of the first results was obtained in \cite{DGR} for $\g=sl(N)$ and its fundamental representation $R\!=\!\tableau1$.
This work builds on a physical realization of knot homologies as spaces of BPS states \cite{GSV,GukovRTN}:
\be
\CH_{\text{knot}} \; = \; \CH_{\text{BPS}} \,.
\label{HHBPS}
\ee

Among other things, this relation predicts the existence of a polynomial knot invariant $\CP^{\tableau1}{(K)}(\a,q,t)$,
sometimes called the {\it{superpolynomial}}, such that for all sufficiently large $N$ one has
\be
{\CP}^{sl(N),\tableau1}(K)(q,t) \; = \; \CP^{\tableau1}(K)(\a=q^N,q,t) \,.
\label{maja2}
\ee
Moreover, the polynomial $\CP^{\tableau1}(K)(\a,q,t)$
has nonnegative coefficients and is equal to the Poincar\'e polynomial of a triply graded homology theory ${\CH}^{\tableau1}(K)$
that categorifies the reduced two-variable HOMFLY polynomial $P^{\tableau1}(K)(\a,q)$, and similarly for the unreduced invariants.
This triply graded theory comes equipped with a collection of differentials $\{d_N\}$,
such that the homology of ${\CH}^{\tableau1}(K)$ with respect to $d_N$ is isomorphic to ${\CH}^{sl(N),\tableau1}(K)$.

There are only two triply-graded knot homologies that have been studied in the literature up to now.
Besides the above-mentioned HOMFLY homology, the second triply-graded theory, proposed in \cite{GWalcher},
similarly unifies homological knot invariants for the $N$-dimensional vector representation $R=V$ of $\g = so(N)$ and $\g = sp(N)$.
This triply-graded theory $\CH^{\mathrm{Kauff}}(K)$ comes with a collection
of differentials $\{d_N\}$, such that the homology with respect to $d_N$ for $N>1$ is isomorphic to $\CH^{so(N),V}(K)$,
while the homology with respect to $d_N$ for even $N<0$ is isomorphic to $\CH^{sp(-N),V}(K)$.
Since the graded Euler characteristic of $\CH^{\mathrm{Kauff}}(K)$ is equal to the (reduced) Kauffman polynomial of $K$,
$\CH^{\mathrm{Kauff}}(K)$ is called the Kauffman homology of a knot $K$.

One way to discover differentials acting on all of these knot homology theories is via studying deformations of the potentials and matrix factorizations in the corresponding Landau-Ginzburg theories (see section \ref{sec:matrix} for details).
In particular, in the case of the Kauffman homology one finds a peculiar deformation that leads to a ``universal" differential $d_{\to}$
and its conjugate $d_{\leftarrow}$, such that the homology with respect to these differentials is, in both cases,
isomorphic to the triply-graded HOMFLY homology $\CH^{\tableau1}(K)$.\\

A careful reader may notice that most of the existent results reviewed here deal with the fundamental
or vector representations of classical Lie algebras (of Cartan type $A$, $B$, $C$, or $D$).
In this paper, we do roughly the opposite: we focus mainly on $\g = sl(N)$ but vary the representation $R$.
In particular, we propose infinitely many triply-graded homology theories associated with arbitrary symmetric ($S^r$)
and anti-symmetric ($\Lambda^r$) representation of $sl(N)$.
Moreover, these colored HOMFLY homology theories come equipped with differentials,
such that the homology, say, with respect to $d_N^{S^r}$ is isomorphic to $\CH^{sl(N),S^r}(K)$, and similarly for $R = \Lambda^r$.

Remarkably, in addition to the differentials labeled by $N$ (for a given $r$) we also find {\it{colored}} differentials
that allow to pass from one triply graded theory to another, thus relating homological knot invariants associated with different representations!

Specifically, for each pair of positive integers $(r,m)$ with $r>m$, we find a differential $d_{r\to m}$,
such that the homology of $\CH^{S^r}(K)$ with respect to $d_{r\to m}$ is isomorphic to $\CH^{S^m}(K)$.
Similarly, in the case of anti-symmetric representations,
we find an infinite sequence of triply-graded knot homologies $\CH^{\Lambda^r}(K)$, one for every positive integer $r$,
equipped with colored differentials that allow to pass between two triply-graded theories with different values of $r$.\\

The colored differentials are a part of a larger algebraic structure that becomes manifest
in a physical realization of knot homologies as spaces of BPS states.
As it often happens in physics, the same physical system may admit several mathematical descriptions;
a prominent example is the relation between Donaldson-Witten and Seiberg-Witten invariants of 4-manifolds
that follows from physics of supersymmetric gauge theories in four dimensions \cite{Wmonopoles}.
Similarly, the space of BPS states in \eqref{HHBPS} admits several (equivalent) descriptions
depending on how one looks at the system of five-branes in eleven-dimensional M-theory \cite{GSV} relevant to this problem.

Specifically, for knots in a 3-sphere ${\bf S}^3$
the relevant system is a certain configuration of five-branes in M-theory on $\R \times M_4 \times X$,
where $M_4 \cong \R^4$ is a 4-manifold with isometry group $U(1)_P \times U(1)_F$ and $X$ is a non-compact toric Calabi-Yau 3-fold
(both of which will be discussed below in more detail).
And, if one looks at this M-theory setup from the vantage point of the Calabi-Yau space $X$,
one finds a description of BPS states via enumerative geometry of $X$.
Furthermore, for simple knots and links that preserve toric symmetry of the Calabi-Yau 3-fold $X$
the study of enumerative invariants reduces to a combinatorial problem of counting certain 3d partitions
(= fixed points of the 3-torus action \cite{ORV}),
hence, providing a combinatorial formulation of knot homologies in terms of 3d partitions~\cite{GIKV,IK}.

On the other hand, if one looks at this M-theory setup from the vantage point of the 4-manifold $M_4$,
one can express the counting of BPS invariants in terms of equivariant instanton counting on $M_4$.
In this approach (see {\it e.g.} \cite{DGH}), the ``quantum'' $q$-grading and the homological $t$-grading
on the space \eqref{HHBPS} originate from the equivariant action of $U(1)_P \times U(1)_F$ on $M_4$.

A closely related viewpoint, that will be very useful to us in what follows,
is based on the five-brane world-volume theory \cite{fiveknots}.
Let us briefly review the basic ingredients of this approach
that will make the relation to the setup of \cite{GSV} more apparent.
In both cases, knot homology is realized as the space of BPS states and, as we shall see
momentarily, the physical realization of the triply-graded knot homology proposed in \cite{GSV}
is essentially the large-$N$ dual of the system realizing the doubly-graded knot homology in \cite{fiveknots}.
This is very typical for systems with $SU(N)$ gauge symmetry\footnote{The same is true for other classical groups.}
which often admit a dual ``holographic'' description
that comprises all $N$ in the same package and leads to useful computational techniques~\cite{holography}.

In the case of $sl(N)$ homological knot invariants,
the five-brane configuration described in \cite[sec. 6]{fiveknots} is the following:
\bea
\text{space-time} & : & \qquad \R \times T^* W \times M_4 \nonumber \\
N~\text{M5-branes} & : & \qquad \R \times W \times D \label{theoryA} \\
\text{M5-brane} & : &  \qquad \R \times L_K \times D \nonumber
\eea
Here, $W$ is a 3-manifold and $D \cong \R^2$ is the ``cigar'' in the Taub-NUT space $M_4 \cong \R^4$.
The Lagrangian submanifold $L_K \subset T^* W$ is the conormal bundle to the knot $K \subset W$; in particular,
\be
L_K \cap W = K \,.
\ee
In all our applications, we consider $W = {\bf S}^3$ (or, a closely related case of $W = \R^3$).

Similarly, the setup of \cite{GSV} can be summarized as
\bea
\text{space-time} & : & \qquad \R \times X \times M_4 \label{theoryB} \\
\text{M5-brane} & : &  \qquad \R \times L_K \times D \nonumber
\eea
where $X$ is the resolved conifold, {\it i.e.} the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$.
{}From the way we summarized \eqref{theoryA} and \eqref{theoryB}, it is clear that they
have many identical elements.

The only difference is that \eqref{theoryA} has extra M5-branes supported on $\R \times W \times D$,
whereas \eqref{theoryB} has a different space-time (with a 2-cycle in the Calabi-Yau 3-fold $X$),
which is exactly what one expects from a holographic duality or large-$N$ transition \cite{GopakumarV,OoguriV}.

Indeed, what is important for the purpose of studying the space of BPS states, $\CH_{\text{BPS}}$, is that
both \eqref{theoryA} and \eqref{theoryB} preserve the same amount of supersymmetry and have the same symmetries:

\begin{itemize}

\item {\bf time translations:} both systems have a translation symmetry along the time direction
(denoted by the $\R$ factor in \eqref{theoryA} and \eqref{theoryB}).
Therefore, in both cases, one can ask for a space of BPS-states --- on multiple M5-branes in \eqref{theoryA},
and on a single M5-brane in \eqref{theoryB} --- which is precisely what was proposed as a candidate
for the $sl(N)$ knot homology (resp. HOMFLY homology).

\item {\bf rotation symmetries:}
\be
U(1)_P \times U(1)_F
\label{uusyms}
\ee
Here, the two $U(1)$ factors correspond, respectively, to the rotation symmetry
of the tangent and normal bundle of $D \cong \R^2$ in a 4-manifold $M_4 \cong \R^4$.
In particular, in both frameworks \eqref{theoryA} and \eqref{theoryB},
the former is responsible for the $q$-grading of $\CH_{BPS}$,
which corresponds to the conserved angular momentum derived from the rotation symmetry of $D$.

\end{itemize}

\noindent
A well-known feature of the large-$N$ duality is that the rank of the gauge group
turns into a geometric parameter of the dual system ({\it cf.} \cite{holography} or \cite{GopakumarV}).
In the present case, it is the K\"ahler modulus of the Calabi-Yau 3-fold $X = \CO_{\cp^1} (-1) \oplus \CO_{\cp^1} (-1)$:
\be
N \; \sim \; \log (\a) \; = \; {\rm Vol} (\cp^1) \,.
\label{NvolCP1}
\ee
The reason we denote the K\"ahler parameter by $\log (\a)$ rather than $\a$
is that with this convention $\a = q^N$ is the standard variable of the HOMFLY polynomial / knot homology.

\begin{figure}[htb]
\centering
\includegraphics[width=3in]{walls2}
\caption{For the conifold $X$, the space of stability conditions is one-dimensional.
It is parametrized by the K\"ahler parameter $N \sim \log (a) = {\rm Vol} (\cp^1)$.
This space is divided by walls of marginal stability into a set of chambers,
which can be identified with the set of integers $\Z$.}
\label{fig:walls}
\end{figure}

Another feature familiar to the practitioners of the refined / motivic Donaldson-Thomas theory
is that $\CH_{\text{BPS}}$ can jump as one varies stability conditions \cite{DenefM,KS1,Refined,BBS,CecottiV,DGS}.
Thus, in a closely related type IIA superstring compactification on a Calabi-Yau 3-fold~$X$,
the stability parameters are the K\"ahler moduli of $X$,
and in the present case there is only one K\"ahler modulus \eqref{NvolCP1} given by the volume of the $\cp^1$ cycle in $X$.
Therefore, we conclude that the space \eqref{HHBPS} can jump as one changes the stability parameter $N \sim {\rm Vol} (\cp^1)$.



Luckily, in the case where $X$ is the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$ relevant to
our applications, the wall-crossing behavior of the refined BPS invariants has been studied in the literature \cite{NagaoN,JafferisM,Refined}.
The one-dimensional space of stability conditions is divided into a set of chambers illustrated in Figure~\ref{fig:walls}.
In each chamber, $\CH_{\text{BPS}}$ is constant and the jumps of closed BPS states
occur at the walls $\CW_{n}^{\pm 1}$ characterized by different types of ``fragments'':
\be
\begin{array}{ccl}
\CW_n^1 & : & \quad D2/D0 \text{ fragments} \;  \\[.1cm]
\CW_n^{-1} & : & \quad \overline{D2}/D0 \text{ fragments} \;  \\[.1cm]
\CW_n^0 & : & \quad D0 \text{ fragments}
\end{array}\label{walltypes}
\ee
Notice, the set of chambers in this model can be identified with $\Z$, the set of integer numbers.
As we explain in the next section, this is not a coincidence. Namely, as we shall see,
every fragment corresponds to a differential acting on the space \eqref{HHBPS},

so that in the present example one finds a set of differentials $\{d_N\}$ labeled by~$N \in \Z$.



The differentials $\{d_N\}$ are part of the homological algebra of knots / BPS states,
depending on whether one prefers to focus on the left or right side of the relation \eqref{HHBPS}.
For larger representations, in addition to the differentials $\{d_N\}$ one finds colored
differentials that allow to pass between homology theories associated with different $R$.
Even though a combinatorial definition of the majority of such theories, with all the differentials, is still missing,
their structure (deduced from physics) is so rigid that enables computation of
the homology groups for many knots and passes a large number of consistency checks.\\

In particular, by computing the triply-graded homologies $\CH^{S^r}(K)$ and $\CH^{\Lambda^r}(K)$ for various knots,
we find the following surprising symmetry between the two theories:
\be\label{mirsym}
\CH^{\Lambda^r}_{i,j,*}(K) \; \cong \; \CH^{S^r}_{i,-j,*}(K) \,.
\ee
One of the implication is that $\CH^{S^r}(K)$ and $\CH^{\Lambda^r}(K)$ can be combined into a single homology theory!

\begin{conjecture}\label{con0}
For every positive integer $r$, there exists a triply-graded theory $\CH^r(K)$ together with a collection of differentials $\{d^r_N\}$,
with $N\in \Z$, such that the homology of $\CH^r(K)$ with respect to $d^r_N$, for $N>0$, is isomorphic to $\CH^{sl(N),S^r}(K)$,
while the homology of $\CH^r(K)$ with respect to $d^r_N$, for $N<0$, is isomorphic (up to a simple regrading) to $\CH^{sl(-N),\Lambda^r}(K)$.
\end{conjecture}

Moreover, it is tempting to speculate that the symmetry \eqref{mirsym} extends to all representations:
\be\label{mirwild}
\text{``mirror symmetry''} ~:~ \quad
\CH^{\lambda} (K) \; \cong \; \CH^{\lambda^t} (K) \,,
\ee
where $\lambda$ and $\lambda^t$ are a pair of Young tableaux related by transposition (mirror reflection across the diagonal),
{\it e.g.}
$$
\lambda \; = \; \tableau{6 3 1} \qquad \longleftrightarrow \qquad \lambda^t \; = \; \tableau{3 2 2 1 1 1}
$$
The symmetry \eqref{mirwild} has not been discussed in physical or mathematical literature before.

While we offer its interpretation in section \ref{sec:physmir},
we believe the mirror symmetry for colored knot homology \eqref{mirwild}
deserves a more careful study, both in physics as well as in mathematics.
In particular, its deeper understanding should lead
to the ``categorification of level-rank duality'' in Chern-Simons theory,
which is the origin of the simpler, decategorified version of \eqref{mirwild}:
\be\label{mirHOMFLY}
P^{\lambda}(K)(\a,q) \; = \; P^{\lambda^t}(K)(\a,q^{-1})
\ee
for colored HOMFLY polynomials \cite{NaculichSchnitzer,Naculich,LMV,LiuPeng},
and extends the familiar symmetry $q \leftrightarrow q^{-1}$ of the ordinary HOMFLY polynomial.
We plan to pursue the categorification of level-rank duality
and to study the new, homological symmetry \eqref{mirwild} in the future work.


\subsection{Organization of the paper}
We start by explaining in section \ref{sec:algebra} that, in general, the space of open BPS states forms a representation
of the algebra of closed BPS states. Then, in section \ref{sec:matrix} we review elements of the connection between
string realizations \eqref{theoryA}--\eqref{theoryB} of knot homologies and Landau-Ginzburg models that play an important role
in mathematical formulations of certain knot homologies based on Lie algebra $\g$ and its representation $R$.
In particular, we illustrate in simple examples how the corresponding potentials $W_{\g,R}$
can be derived from the physical setup \eqref{theoryA}--\eqref{theoryB} and how deformations of these potentials
lead to various differentials acting on ${\CH}^{\g,R}(K)$. This gives another way to look at the algebra acting on \eqref{HHBPS}.
Based on these predictions, in section \ref{sec:reduced} we summarize the mathematical structure
of the triply-graded homology $\CH^{S^r}(K)$, together with its computation for small knots.
Section \ref{sec:mirror} lists the analogous properties of the homology associated with anti-symmetric representations,
and explains the explicit form of the ``mirror symmetry" \eqref{mirsym} between symmetric and anti-symmetric triply-graded theories.
Unreduced triply-graded theory for symmetric and anti-symmetric representations is briefly discussed in section \ref{sec:unreduced}.
In appendix \ref{sec:notation} we collect the list of our notations,
whereas in appendix \ref{sec:942} we present the computations of the $S^2$, $\Lambda^2$ and Kauffman triply-graded homology
for knots $8_{19}$ and $9_{42}$.
These particular examples of ``thick'' knots provide highly non-trivial tests of all the properties of the homologies presented in the paper. Appendix \ref{apb41} contains the computation of the $S^3$ and $\Lambda^3$ homology of the figure-eight knot $4_1$.
Finally, appendix \ref{compun} collects some notations and calculations relevant to the unreduced
colored HOMFLY polynomial of the unknot discussed in section \ref{sec:unreduced}.
