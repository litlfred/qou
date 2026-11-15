---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-002-3-b-model-and-matrix-factorizations
section_title: "B-model and matrix factorizations"
section_number: 3
pages: 10-25
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
text_source: latex
latex_prose_ratio: 0.619
latex_coverage_ratio: 1.0
---
\label{sec:matrix}

Let us denote by $\CH^{\frak{g}, R}$ a homology theory of knots and links colored by a representation $R$ of the Lie algebra $\frak{g}$.
Many such homology theories can be constructed using categories of matrix factorizations \cite{KRa,KRfoam,KRb,Khov,KRso,MSV,Yonezawa,Wu}.
In this approach, one of the main ingredients is a polynomial function $W_{\frak{g},R}$ called the {\it potential},
associated to every segment of a link (or, more generally, of a tangle) away from crossings.
For example, for the fundamental representation of $\frak{g} = sl(N)$ the potential
is a function of a single variable,
\be
W_{sl(N), \tableau{1}} (x) \; = \; x^{N+1} \,.
\label{WslN}
\ee

In physics, matrix factorizations are known \cite{Kontsevich,Kli,Orlov,BHLS,HWalcher,BrunnerR}
to describe D-branes and topological defects
in Landau-Ginzburg models which, in the present context, are realized on the two-dimensional
part of the five-brane world-volume in \eqref{theoryA} or \eqref{theoryB}.
More precisely, it was advocated in \cite{GWalcher} that reduction of the M-theory configuration \eqref{theoryA}
on one of the directions in $D$ and a T-duality along the time direction
gives a configuration of intersecting D3-branes in type IIB string theory,
such that the effective two-dimensional theory on their common world-volume provides a physical
realization of the Landau-Ginzburg model that appears in the mathematical constructions.

In particular, this interpretation was used to deduce potentials $W_{\frak{g}, R}$ associated to
many Lie algebras and representations. Indeed, since away from crossings every segment of the knot $K$
is supposed to be described by a Landau-Ginzburg theory with potential $W_{\frak{g}, R}$,
we can approximate this local problem by taking $W = \R^3$ and $K = \R$ in \eqref{theoryA}.
Then, we also have $L_K = \R^3$ and the reduction (plus T-duality) of \eqref{theoryA} gives type IIB theory
in flat space-time with two sets of D3-branes supported on 4-dimensional hyperplanes in $\R^{10}$:
one set supported on $\R \times W$, and another supported on $\R \times L_K$.
The space of open strings between these two groups of D3-branes contains information about the potential $W_{\frak{g}, R}$.

\begin{figure}[htb]
\centering
\includegraphics[width=2in]{LLbranes}
\caption{The physics of open strings between two stacks of Lagrangian branes
is described by the Landau-Ginzburg model with potential~$W_{\frak{g}, R}$.}
\label{fig:branes}
\end{figure}

For example, in the case of the fundamental representation of $sl(N)$, the first stack consists of $N$ D3-branes
and the second only contains a single D3-brane. The open strings between these two stacks of D3-branes
transform in the bifundamental representation $({\bf N}, +1)$ under the gauge symmetry $U(N) \times U(1)$ on the D3-branes.


The Higgs branch of this two-dimensional theory
is the K\"ahler quotient of the vector space $\C^N$ parametrized by the bifundamental chiral multiplets,
modulo $U(1)$ gauge symmetry of a single D3-brane supported on $\R \times L_K$:
\be
\C^N / \! / U(1) \; \cong \; \cp^{N-1} \,.
\ee
The chiral ring of this theory on the intersection of D3-branes
is precisely the Jacobi ring of the potential \eqref{WslN}.

Following similar arguments one can find potentials associated to many other Lie algebras
and representations \cite{GWalcher}, such that
\be
\CH^{\frak{g}, R} (\unknot) \; = \; \CJ (W_{\frak{g}, R}) \,.
\ee
For example, the arguments that lead to \eqref{WslN} can be easily generalized to $R=\Lambda^r$,
the $r$-th anti-symmetric representation of $sl(N)$.
The only difference is that, in this case, the corresponding brane systems \eqref{theoryA} and \eqref{theoryB}
contain $r$ coincident M5-branes supported on $\R \times L_K \times D$.
Following the same arguments as in the case of the fundamental representation ($r=1$)
and zooming in closely on the local geometry of the brane intersection,
after all the dualities we end up with a system of intersecting D3-branes in flat ten-dimensional space-time,
\bea
N~\text{D3-branes} & : & \qquad \R \times W \label{D3branes} \\
r~\text{D3}'\text{-branes} & : &  \qquad \R \times L_K \nonumber
\eea
where, as in the previous discussion, for the purpose of deriving $W_{\frak{g},R}$
we can approximate $W \simeq \R^3$ and $L_K \simeq \R^3$, so that $W \cap L_K = \R$.
Now, the open strings between two sets of D3-branes in \eqref{D3branes}
transform in the bifundamental representation $({\bf N}, {\bf r})$ under the gauge symmetry $U(N) \times U(r)$ on the D3-branes.
Here, if we want to ``integrate out'' open strings ending on the D3$'$-branes,
only the second gauge factor should be considered dynamical,
while $U(N)$ should be treated as a global symmetry of the two-dimensional $U(r)$ gauge theory on the brane intersection.
In the infrared this theory flows to a sigma-model based on the Grassmannian manifold:
\be
{\rm Gr} (r,N) \; = \; \frac{U(N)}{U(r) \times U(N-r)} \,.
\ee
The potential of the corresponding Landau-Ginzburg model \cite{Wgrassmannian} is a homogeneous polynomial of degree $N+1$,
\be
W_{sl(N),\Lambda^r} (z_1,\ldots,z_r) \; = \; x^{N+1}_1 + \ldots + x_r^{N+1} \,,
\label{Wanti}
\ee
where the right-hand side should be viewed as a function of the variables $z_i$ of degree $\deg (z_i) = i$, $i=1, \ldots, r$,
which are the elementary symmetric polynomials in the $x_j$,
$$
z_i \; = \; \sum_{j_1<j_2<\cdots<j_i} x_{j_1}x_{j_2} \cdots x_{j_i} \,.
$$
We shall return to the discussion of the potential $W_{sl(N),\Lambda^r}$ later in this section.
In the case of more general representations,
one needs to consider various sectors of the $U(r)$ gauge theory on $\R \times L_K$
labeled by non-trivial flat connections (Wilson lines) around the codimension-2 locus
where D3$'$-branes meet D3-branes, {\it cf.}~\cite{OoguriV,Rigid}.

In this paper we are mostly interested in knots colored by symmetric and anti-symmetric representations of $\frak{g} = sl(N)$,
even though much of the present discussion can be easily generalized to other Lie algebras and representations.
Thus, for a symmetric representation $R=S^r$ of $\frak{g} = sl(N)$ one finds that
the corresponding potential $W_{sl(N),S^r} (z_1, \ldots, z_r)$ is a homogeneous polynomial of degree $N+r$
in variables $z_i$ of degree $i=1,\ldots,r$, much like \eqref{Wanti}.
Moreover, the explicit form of such potentials can be conveniently expressed through a generating function \cite{GWalcher}:
\be
\sum_N (-1)^{N} t^{N+r} W_{sl(N),S^r} (z_1, \ldots, z_r) \; = \; (1+ \sum_{i=1}^r t^i z_i) \log ( 1 + \sum_{i=1}^r t^i z_i) \,,
\label{Wsymgenfncn}
\ee
which in the basic case $N=r=2$ gives
\be
W_{sl(2),\tableau{2}} \; = \; z_1^4 - 6 z_1^2 z_2 + 6 z_2^2 \,.
\label{W22}
\ee
Instead of going through the derivation of this formula we can use a simple trick
based on the well known isomorphism $sl(2) \cong so(3)$
under which a vector representation of $so(3)$ is identified with the adjoint representation of $sl(2)$.
Indeed, it implies that \eqref{W22} should be identical to the well known potential
\be
W_{so(3), V} \; = \; x^2 + xy^2
\label{Wso3}
\ee
in the $so(3)$ homology theory, {\it cf.} \cite{GWalcher,KRso}.
It is easy to verify that the potentials \eqref{W22} and \eqref{Wso3} are indeed related
by a simple change of variables.\footnote{Explicitly, the change of variables that relates
\eqref{W22} and \eqref{Wso3} is given by:
\begin{eqnarray}
x & = & - \frac{1}{2} (\sqrt{2} + \sqrt{6}) \; z_1^2 + \sqrt{6} \; z_2 \nonumber \\
y & = & 2^{1/4} \; z_1 \nonumber
\end{eqnarray}
}

Moreover, the fact that the adjoint representation of $sl(2)$ is identical to the vector representation of $so(3)$
implies that
\be
\boxed{\phantom{\int}
\CH^{sl(2), \tableau{2}} (K) \; \cong \; \CH^{so(3),V} (K) \phantom{\int}}
\label{sl2so3}
\ee
should hold for every knot $K$.
In particular, it should hold for the unknot.
And, since $\CH^{so(3),V} (\unknot)$ is 3-dimensional,
it follows
\be
\dim \CH^{sl(2), \tableau{2}} (\unknot) \; = \; \dim \CH^{so(3),V} (\unknot) \; = \; 3 \,.
\label{HHunknot3dim}
\ee
This is indeed what one finds in physical realizations of knot homologies reviewed in section \ref{sec:intro}.
In the framework of \cite{GSV} the colored homology $\CH^{sl(2), \tableau{2}}$ of the unknot
was computed in \cite{GIKV} using localization with respect to the toric symmetry of the Calabi-Yau space $X$.
Similarly, in the gauge theory framework \cite{fiveknots} the moduli space of solutions on $\R^2$
with a single defect operator in the adjoint representation of the gauge group $G=SU(2)$
is the weighted projective space $\mathbb{W} \cp^2_{(1,1,2)}$ (= the space of Hecke modifications \cite{KW}, see also \cite{GWopers}).
In this approach, the colored homology $\CH^{sl(2), \tableau{2}} (\unknot)$
is given by the $L^2$ cohomology of the moduli space $\mathbb{W} \cp^2_{(1,1,2)}$
which is 3-dimensional, in agreement with \eqref{HHunknot3dim}.


\subsection{Colored differentials}

One of the reasons why we carefully reviewed the properties of the potentials $W_{\frak{g}, R}$
is that they hold a key to understanding the colored differentials.
Namely, in doubly-graded knot homologies constructed from matrix factorizations differentials
that relate different theories are in one-to-one correspondence with deformations
of the potentials \cite{Lee,BarNatan,Turner,KhovanovFr,Gornik,GWalcher}:
\be
\boxed{\phantom{\int} \text{differentials on} ~ \CH^{\frak{g}, R} \quad \Longleftrightarrow \quad \text{deformations of} ~W_{\frak{g}, R} \phantom{\int}}
\label{defdiff}
\ee
For example, deformations of the potential \eqref{WslN} of the form $\Delta W = \beta x^{M+1}$ with $M<N$,
correspond to differentials $d_M$ that relate $sl(N)$ and $sl(M)$ knot homologies (with $R = \tableau{1}$).

More generally, one can consider deformations $\Delta W$ of the potential $W_{\frak{g}, R}$
such that $\deg \Delta W < \deg W_{\frak{g}, R}$ and
\be
W_{\frak{g}, R} + \Delta W \; \simeq \; W_{\frak{g}', R'}
\label{Wdeformed}
\ee
for some Lie algebra $\frak{g}'$ and its representation $R'$.
Here, the symbol ``$\simeq$'' means that the critical point(s) of the deformed potential
is locally described by the new potential $W_{\frak{g}', R'}$.
A deformation of this form leads to a spectral sequence that relates knot
homologies $\CH^{\frak{g}, R}$ and $\CH^{\frak{g}', R'}$.
With the additional assumption that the spectral sequence converges after the first page one arrives at \eqref{defdiff}.
Moreover, the difference
\be
\deg W_{\frak{g}, R}-\deg \Delta W
\label{WWqgrading}
\ee
gives the $q$-grading of the corresponding differential.
Notice, the condition $\deg \Delta W < \deg W_{\frak{g}, R}$
implies that this $q$-grading is positive.

For example, among deformations of the degree-4 potential \eqref{W22} one finds
$\Delta W = z_1^3$, which leads to a differential of $q$-degree 1
that relates $\CH^{sl(2),\tableau{2}}$ and $\CH^{sl(2),\tableau{1}}$.
This deformation has an obvious analog for higher rank $S^2$-colored homology;
it deforms the homogeneous polynomial $W_{sl(N),\tableau{2}} (z_1,z_2)$ of degree $N+2$
in such a way that the deformed potential has a critical point described by the potential
$W_{\frak{g}', R'} = W_{sl(N),\tableau{1}} (z_1)$ of degree $N+1$.
Therefore, it leads to a colored differential of $q$-degree 1, such that
\be
\big( \CH^{sl(N),\tableau{2}} , \; d_{\text{colored}} \big) \; \cong \; \CH^{sl(N),\tableau{1}} \,.
\label{coloredHdH}
\ee
In section \ref{sec:reduced} we present further evidence for the existence of a differential
with such properties not only in the doubly-graded $sl(N)$ theory but also in the triply-graded
knot homology that categorifies the colored HOMFLY polynomial.\\

Similar colored differentials exist in other knot homologies associated with more general Lie algebras and representations.
Basically, a knot homology associated to a representation $R$ of the Lie algebra $\frak{g}$
comes equipped with a set of colored differentials that, when acting on $\CH^{\frak{g}, R}$,
lead to homological invariants associated with smaller representations (and, possibly, Lie algebras),
\be
\dim R' \; < \; \dim R \,.
\label{coloredRR}
\ee
While it would be interesting to perform a systematic classification of such colored differentials
using the general principle \eqref{defdiff},
in this paper we limit ourselves only to symmetric and anti-symmetric representations of $\frak{g} = sl(N)$.

As we already discussed earlier,
when $R=\Lambda^r$ is the $r$-th anti-symmetric representation of $sl(N)$
the corresponding Landau-Ginzburg potential \eqref{Wanti} is a homogeneous polynomial of degree $N+1$.
Equivalently, the potentials with a fixed value of $r$ can be organized into a generating function,
analogous to \eqref{Wsymgenfncn}:
\be
\sum_N (-1)^{N} t^{N+1} W_{sl(N),\Lambda^r} (z_1, \ldots, z_r) \; = \; \log ( 1 + \sum_{i=1}^r t^i z_i) \,.
\label{WWanti}
\ee
For example, in the first non-trivial case of $r=2$ there are only two variables,
$z_1 = x_1 + x_2$ and $z_2 = x_1 x_2$.
For $N=2$ one finds a ``trivial'' potential $W_{sl(2),\tableau{1 1}}$ of degree 3,
which corresponds to the fact that the anti-symmetric representation $R = \Lambda^2$ (also denoted $R = \tableau{1 1}$) is trivial in $sl(2)$.
For $N=3$, the existence of the anti-symmetric tensor $\epsilon^{ijk}$ identifies the second anti-symmetric representation $R = \tableau{1 1}$
with the fundamental representation of $sl(3)$.
The next case in this sequence, $N=4$, is the first example where the second anti-symmetric representation is not related to
any other representation of $sl(4)$.
According to \eqref{Wanti} and \eqref{WWanti}, the corresponding potential is a homogeneous polynomial of degree 5,
\be
W_{sl(4), \tableau{1 1}} \; = \; \frac{z_1^5}{5} - z_1^3 z_2 + z_1 z_2^2 \,.
\ee
Before studying deformations of this potential, we note that by a simple change of variables
it is related to the potential
\be
W_{so(6),V} \; = \; x^5 + x y^2
\ee
associated to a vector representation of $so(6)$. This is a manifestation of the well known isomorphism $sl(4) \cong so(6)$
under which the six-dimensional anti-symmetric representation $R = \tableau{1 1}$ of $sl(4)$ is identified with the vector representation of $so(6)$.
This isomorphism can help us understand deformations of the potential $W_{sl(4), \tableau{1 1}} = W_{so(6),V}$.
Indeed, the deformations of $W_{so(N),V}$ were already studied in \cite{GWalcher}; they include several deformations
which lead to {\it canceling} differentials and a deformation by $\Delta W = y^2$ that leads to a {\it universal} differential
$\CH^{so(N),V} \leadsto \CH^{sl(N-2),\tableau{1}}$.

In view of the relation $W_{sl(4), \tableau{1 1}} (z_1,z_2) = W_{so(6),V} (x,y)$, these deformations (and the corresponding differentials)
should be present in the $sl(4)$ theory as well. In particular, there are deformations of $W_{sl(4), \tableau{1 1}}$
that lead to canceling differentials and, more importantly, there is a deformation by $\Delta W = y^2$
that leads to the universal differential which relates $\CH^{so(6),V} \cong \CH^{sl(4),\tableau{1 1}}$ and $\CH^{sl(4),\tableau{1}}$.
Note, from the viewpoint of the $sl(4)$ knot homology, this is exactly the colored differential $d_{\text{colored}}$
that does not change the rank of the Lie algebra, but changes the representation.
Making use of \eqref{WWanti} it is easy to verify that, for all values of $N$,
the potential $W_{sl(N), \tableau{1 1}}$ admits a deformation by terms of degree $N$
that leads to $W_{sl(N), \tableau{1}}$ and, therefore, to the analog of \eqref{coloredHdH}:
\be
\big( \CH^{sl(N),\tableau{1 1}} , \; d_{\text{colored}} \big) \; \cong \; \CH^{sl(N),\tableau{1}} \,.
\label{coloredHdHanti}
\ee
Much like in the case of the symmetric representations, this colored differential as well as canceling
differentials come from the triply-graded theory that categorifies the $\tableau{1 1}$-colored HOMFLY polynomial
(see section \ref{sec:mirror} for details).




\section{Colored HOMFLY homology}
\label{sec:reduced}

In this section we propose structural properties of the triply-graded theory categorifying
the colored version of the reduced HOMFLY polynomial.
The central role in this intricate network of structural properties belongs to the colored differentials,
whose existence we already motivated in the previous sections.


\subsection{Structural properties}
Let $N$ and $r$  be positive integers, and
let $\CH^{sl(N),S^r}(K)$ denote a reduced doubly-graded homology theory categorifying $P^{S^r}_N(K)$,
the polynomial invariant of a knot $K$ labeled with the $r$-th symmetric representation of $sl(N)$.
$\CP^{S^r}_N$ denotes the Poincar\'e polynomial of $\CH^{sl(N),S^r}(K)$.
Motivated by physics, we expect that such theories with a given value of $r$ have a lot in common.

\begin{conjecture}\label{con1}
For a knot $K$ and a positive integer $r$, there exists a finite polynomial
$\CP^{S^r}(K)\in\Z_+[\a^{\pm 1},q^{\pm 1},t^{\pm 1}]$ such that
\begin{equation}\label{coneq1}
\CP^{S^r}_N(K)(q,t)=\CP^{S^r}(K)(\a=q^N,q,t),
\end{equation}
for all sufficiently large $N$.
\end{conjecture}

Since the left-hand side of (\ref{coneq1}) is a Poincar\'e polynomial of a homology theory,
all coefficients of $\CP^{S^r}(K)(\a,q,t)$ must be nonnegative.
This suggests that there exists a triply-graded homology theory whose Poincar\'e polynomial is equal to $\CP^{S^r}(K)(\a,q,t)$,
and whose Euler characteristic is equal to the normalized $S^r$-colored two-variable HOMFLY polynomial.

As in the case of ordinary HOMFLY homology \cite{DGR} (that, in fact, corresponds to $r=1$) and in the case of Kauffman homology \cite{GWalcher},
this triply-graded theory comes with the additional structure of differentials, that will imply Conjecture \ref{con1}.
In particular, for each positive integer $r$ we have a triply-graded homology theory of a knot $K$.
Moreover, these theories come with additional structure of differentials that, as in \eqref{coloredRR},
allow us to pass from the homology theory with $R = S^r$ to theories with $R' = S^m$ and $m<r$.\\

Thus, we arrive to our main conjecture that describes the structure of the triply-graded homology
categorifying the $S^r$-colored HOMFLY polynomials:

\begin{conjecture}\label{con2}
For every positive integer $r$ there exists a triply-graded homology theory $\CH^{S^r}_*=\CH^{S^r}_{i,j,k}(K)$
that categorifies the reduced two-variable $S^r$-colored HOMFLY polynomial of $K$.

It comes with a family of differentials $\{d^{S^r}_N\}$, with $N\in\Z$, and also with an additional collection of \textit{universal colored} differentials $d_{r\to m}$, for every $1\le m<r$, satisfying the following properties:\\

\noindent$\bullet$ \textbf{Categorification: } $\CH^{S^r}_*$ categorifies $P^{S^r}:$
\[
\chi(\CH^{S^r}_*(K))=P^{S^r}(K).
\]
$\bullet$ \textbf{Anticommutativity:} The differentials $\{d^{S^r}_N\}$ anticommute\footnote{{\it cf.} comments following \eqref{frogtypes}}:
\[
d^{S^r}_Nd^{S^r}_M=-d^{S^r}_Md^{S^r}_N.
\]
$\bullet$ \textbf{Finite support:}
\[
\dim (\CH^{S^r}_*)< +\infty.
\]
$\bullet$ \textbf{Specializations:} For $N>1$, the homology of $\CH^{S^r}_*(K)$ with respect to $d^{S^r}_N$ is isomorphic to $\CH^{sl(N),S^r}(K)$:
\[
\left(\CH^{S^r}_*(K), d^{S^r}_N\right) \cong \CH^{sl(N),S^r}(K).
\]
$\bullet$ \textbf{Canceling differentials: } The differentials $d^{S^r}_1$ and $d^{S^r}_{-r}$  are \textit{canceling}:
the homology of $\CH^{S^r}_*(K)$ with respect to the differentials $d^{S^r}_1$ and $d^{S^r}_{-r}$ is one-dimensional,
with the gradings of the remaining generators being simple invariants of the knot $K$.\\

\noindent$\bullet$ \textbf{Vertical Colored differentials: } The differentials $d^{S^r}_{1-k}$, for $1 \le k \le r-1$, have $\a$-degree $-1$, and the homology of $\CH^{S^r}_*(K)$ with respect to the differential $d^{S^r}_{1-k}$ is isomorphic, after simple regrading that preserves $\a$- and $t$-gradings, to the $k$-colored homology $\CH^{S^{k}}_*(K)$.\\

\noindent$\bullet$ \textbf{Universal Colored differentials: } For any positive integer $m$, with $m<r$, the differentials $d_{r\to m}$
have $\a$-degree zero, and the homology of $\CH^{S^r}_*(K)$ with respect to the colored differential $d_{r\to m}$ is isomorphic (after regrading) to the $m$-colored homology $\CH^{S^m}_*(K)$:
\[
\left(\CH^{S^r}_*(K), d_{r\to m}\right) \cong \CH^{S^m}_*(K).
\]

\end{conjecture}
\vskip 1cm

A combinatorial definition of a triply-graded theory with the structure given in Conjecture \ref{con2},
as well as of the homologies $\CH^{sl(N),S^r}(K)$ for $r>1$ and $N>2$, still does not exist in the literature.

Even though there is no such combinatorial definition, one can use any combination of the above axioms as a definition,
and the remaining properties as consistency checks. In particular, one can obtain various consequence of the Conjecture \ref{con2}
and properties of the triply-graded homology $\CH^{S^r}$, along with the predictions for the triply-graded homology of simple knots.

In the rest of this section we give a summary of these properties, including some non-trivial checks.\\


\subsection{A word on grading conventions}
\label{sec:gradings}

So far we summarized the general structural properties of the colored knot homology.
Now we are about to make it concrete and derive explicit predictions for colored homology groups of simple knots.
This requires committing to specific grading conventions, as well as other choices that may affect the form of the answer.
It is important to realize, however, that none of these affect the very existence of the structural properties,
which are present with any choices and merely may look different.
While some of these choices will be discussed in section \ref{sec:comparison}, here we focus on

\begin{itemize}

\item
choices that associate various formulae to a Young tableaux $\lambda$ versus its transpose $\lambda^t$;

\item
choices of grading, {\it e.g.} grading conventions used in this paper (that we sometimes refer to as ``old'')
and grading conventions used in most of the existent literature \cite{DGR,AShakirov,DMMSS}
(that we sometimes call ``new'' in view of the forthcoming work \cite{inprogress} based on this choice).

\end{itemize}

The first choice here breaks the symmetry (``mirror symmetry'') between representations $S^r$ and $\Lambda^r$.
Indeed, since in view of the Conjecture \ref{con0}
the triply-graded homologies associated with these representations are essentially identical
and can be packaged in a single theory $\CH^r$, one has a choice whether $S^r$ homologies arise for $N>0$ or $N<0$.

The second choice listed here starts with different grading assignments, but turns out to be exactly the same as the first choice.
In other words, the ``old'' gradings and ``new'' gradings are related by ``mirror symmetry.''
Another way to describe this is to note, that in grading conventions of this paper the $S^r$-colored superpolynomials
are related (by a simple change of variables)
to the $\Lambda^r$-colored invariants that one would find by following
the same steps in grading conventions of {\it e.g.} \cite{DGR,AShakirov,DMMSS}:
\be
\CP^{S^r}_{\text{here}} \; = \; \CP^{\Lambda^r}_{\text{elsewhere}}
\ee
Note, that the $S^r$-colored invariant is related to the $\Lambda^r$-colored invariant, and vice versa.
The explicit change
of variables in this transformation is sensitive to even more elementary redefinitions,
such as $\a \to \a^2$ and $q \to q^2$ which is ubiquitous in knot theory literature.
For example, with one of the most popular choices of $\a$- and $q$-grading,
the transformation of variables / gradings looks like:










\bea
A & \mapsto & \a t^3 \,, \nonumber \\
q & \mapsto & \frac{1}{q t^2} \,, \label{GSvarchng} \\
t & \mapsto & \frac{1}{q} \,. \nonumber
\eea

The moral of the story is that, besides the grading conventions used in the earlier literature,
the present paper offers yet another choice of grading conventions consistent with all the structural properties.
And the relation between the two grading conventions can be viewed as a manifestation of mirror symmetry \eqref{mirsym}.
Keeping these words of caution in mind, now let us take a closer look at the structure
of the colored knot homology.


\subsection{Consequences of Conjecture \ref{con2}}\label{s42}

First of all, our main Conjecture \ref{con2} implies the Conjecture \ref{con1}.
Indeed, in order to be consistent with the specialization $\a=q^N$ from (\ref{coneq1}),
the $q$-degree of the differential $d^{S^r}_N$ must be proportional to $N$.
Since $\CH^{S^r}_*$ has finite support, this leads to the Conjecture \ref{con1},
with $\CP^{S^r}(K)$ being the Poincar\'e polynomial of $\CH^{S^r}_*(K)$.\\

More precisely, the differentials $d^{S^r}_N$, $N\ge 1$, are expected to have the following degrees:
\[
\deg (d^{S^r}_N) = (-1,N,-1),\quad N>0,
\]
which is consistent with the specialization $\a=q^N$ and the formula \eqref{WWqgrading}
that determines the $q$-grading of the corresponding differential in the doubly-graded theory.
In fact, the differential $d^{S^r}_N$ acts on the the following bi-graded chain complex:
\[
\CC^{sl(N),S^r}_{p,k}=\bigoplus_{iN+j=p} \CH^{S^r}_{i,j,k},
\]
and has $q$-degree 0, and $t$-degree $-1$.
The homology of $\CC^{sl(N),S^r}$ with respect to $d^{S^r}_N$ is isomorphic to $\CH^{sl(N),S^r}$.\\

In general, the degrees of the differentials $d^{S^r}_N$, for $N\in \Z$ are given by:

\begin{eqnarray*}
\deg(d^{S^r}_N)&=&(-1,N,-1),\quad N\ge 1-r,\\
\deg(d^{S^r}_N)&=&(-1,N,-3),\quad N \le -r.
\end{eqnarray*}
We note that for every $r\ge 1$, and every $N\in \Z$, the degree of the differential $d^{S^r}_N$ has the form $\deg(d^{S^r}_N)=(-1,N,\ast)$.


\subsubsection{Canceling differentials}

Canceling differentials appear in all conjectural triply-graded theories, including the ordinary HOMFLY homology and the Kauffman homology.
The defining property of a canceling differential is that the homology of the triply-graded theory with respect to this differential is ``trivial",
{\it i.e.} isomorphic to the homology of the unknot. In reduced theory, this means that the resulting homology is one-dimensional.
Furthermore, the degree of the remaining generator depends in a particularly simple way on the knot.\\

In the case of the colored HOMFLY homology $\CH^{S^r}$, the canceling differentials are $d^{S^r}_1$ and $d^{S^r}_{-r}$. Their degrees are:
\begin{eqnarray*}
\deg(d^{S^r}_1)&=&(-1,1,-1),\\
\deg(d^{S^r}_{-r})&=&(-1,-r,-3).
\end{eqnarray*}
Note that for $r=1$ this agrees with the gradings of the canceling differentials
in the ordinary triply-graded HOMFLY homology.
(Keep in mind, though, the conventions we are using in this paper, see Remark \ref{rem1}.)
For either of the two canceling differentials, the degree of the surviving generator depends only
on the $S$-invariant\footnote{Again, the value that we are using here is half of the value defined in \cite{DGR}.} of a knot $K$,
introduced in \cite{DGR}. In particular, the surviving generators have the following $(\a,q,t)$-degrees:
\begin{eqnarray}
\deg \left(\CH^{S^r}_*(K), d^{S^r}_1 \right) & = &(rS,-rS,0), \label{surviving} \\
\deg \left(\CH^{S^r}_*(K), d^{S^r}_{-r} \right) & = &(rS,r^2 S,2rS) \,. \nonumber
\end{eqnarray}
Note, that the remaining generator with respect to $d^{S^r}_1$ has $t$-degree equal to zero.\\


\subsubsection{Vertical Colored differentials}
Arguably, the most interesting feature of the colored triply-graded theory is the existence of colored differentials.
They allow to pass from the homology theory for a representation $R = S^r$ to the homology theory for another representation $R' = S^m$, with $m<r$.

The first group of colored differentials are ``vertical" colored differentials $d^{S^r}_{1-k}$, for $1\le k\le r-1$. As said before, the degrees of these differentials are
\be
\deg(d^{S^r}_{1-k})=(-1,1-k,-1),\quad 1\le k \le r-1.
\ee

The homology of $\CH^{S^r}$ with respect to the differential $d^{S^r}_{1-k}$, for any $k=1,\ldots,r-1$, is (up to a simple regrading) isomorphic to $\CH^{S^k}$.

In particular, up to an overall shift of the $\a$-grading, the $\a$- and $t$-gradings of the homologies match. More precisely, the Poincare polynomial of the homology $(\CH^{S^r},d^{S^r}_{1-k})$ satisfies:
\be
(\CH^{S^r},d^{S^r}_{1-k})(\a,q=1,t)=\a^{(r-k)S}\,\, \CP^{S^k} (\a,q=1,t),
\ee
where the $S$-invariant is defined by (\ref{surviving}).
The $q$-grading is controlled in the following way: the canceling differentials $d^{S^k}_1$ and $d^{S^k}_{-k}$ of $\CH^{S^k}$ correspond to two canceling differentials of $(\CH^{S^r},d^{S^r}_{1-k})$ of degrees $(-1,1+r-k,-1)$ and $(-1,-r,-3)$, respectively.

In the particular case of the differential $d^{S^r}_0$ that allows passage from $S^r$-colored homology to the uncolored $S^1$-homology, the explicit regrading is particularly simple:
\be
(\CH^{S^r},d^{S^r}_{0})(\a,q,t)=\a^{(r-1)S}\,\, \CP^{\tableau1} (\a,q^r,t).
\ee




\subsubsection{Universal Colored differentials}
The universal colored differentials in the triply-graded theory are ``universal" analogs
of the colored differentials in the doubly-graded theory \eqref{coloredHdH}:
\[
\CH^{sl(N),S^r} \; \leadsto \; \CH^{sl(N),S^{r-1}} \,.
\]

As explained in section \ref{sec:matrix}, these colored differentials come from the deformations of the Landau-Ginzburg potentials.\\

Since colored differentials are universal in the triply-graded theory --- {\it i.e.} they relate colored triply-graded homologies without even specializing to doubly-graded $sl(N)$ theories --- they should have zero $\a$-degree. This property distinguishes them clearly from the vertical colored differentials.


Furthermore, as explained in section \ref{sec:matrix},
the basic colored differential $d_{r\to (r-1)}$ should have $q$-degree equal to 1. Then, it is easy to see that consistency of the theory
also requires this differential to have zero $t$-grading. Combining all of these facts, we conclude that the $(\a,q,t)$-degree
of the differentials $d_{r\to (r-1)}$ is equal to $(0,1,0)$.\\

More generally, we expect that the degree of the differential $d_{r\to m}$ depends only on the difference $r-m$
and the homology of $\CH^{S^r}_*(K)$ with respect to the colored differential $d_{r\to m}$ is isomorphic (up to regrading) to $\CH^{S^m}_*(K)$.
The explicit form of the regrading for the colored differential $d_{2\to 1}$ is as follows: the Poincar\'e polynomial of the homology $(\CH^{\tableau2},d_{2\to 1})$ is equal to $\CP^{\tableau1}(\a^2,q^2,t^2q)$. Put differently,
\be
\left( \CH^{\tableau2} (K), d_{2\to 1} \right)_{2i,k+2j,2k} \; \cong \; \CH^{\tableau1}_{i,j,k} (K) \,.
\ee
In general, the explicit regrading is very subtle (unlike the case of the vertical colored differentials).

We point out that, for $m<m_1<r$,
the homology $((\CH^{S^r}, d_{r\to m_1}), d_{m_1\to m})$ does not need to coincide with the homology $(\CH^{S^r},d_{r\to m})$.


\subsection{Second symmetric representation}
\label{s2r}

In this subsection we focus on the case $r=2$, {\it i.e.} on the homology $\CH^{\tableau2}(K)$.
Specialization of the above mentioned properties to $r=2$ gives:

\begin{itemize}

\item
Two canceling differentials $d^{\tableau2}_1$ and $d^{\tableau2}_{-2}$ that have degrees:
\begin{eqnarray*}
\deg(d^{\tableau2}_1)&=&(-1,1,-1),\\
\deg(d^{\tableau2}_{-2})&=&(-1,-2,-3).
\end{eqnarray*}

\item
The generator that survives the differential $d^{\tableau2}_1$ has degree $(2S,-2S,0)$.

\item
The generator that survives the differential $d^{\tableau2}_{-2}$ has degree $(2S,4S,4S)$.

\item
The vertical colored differential $d^{\tableau2}_0$ has degree $(-1,0,-1)$.

\item
The Poincar\'e polynomial of the homology $(\CH^{\tableau2}(K),d^{\tableau2}_0)$ is equal to $\a^S\CP^{\tableau1}(K)(\a,q^2,t)$.

\item
The colored differential $d_{2\to 1}$ has degree $(0,1,0)$.

\item
The Poincar\'e polynomial of the homology $(\CH^{\tableau2}(K),d_{2\to 1})$ is equal to $\CP^{\tableau1}(K)(\a^2,q^2,t^2q)$.\\

\end{itemize}

In addition, the homology of $\CH^{\tableau2}(K)$ with respect to the differential $d_2^{\tableau2}$
should be isomorphic (after specialization $\a=q^2$) to $\CH^{sl(2),\tableau2}(K)$.
To find the latter homology one can use the isomorphism \eqref{sl2so3} with $\CH^{so(3),V} (K)$ which, in turn,
can be obtained from the triply-graded Kauffman homology $\CH^{\mathrm{Kauff}}(K)$ studied in \cite{GWalcher}.
Indeed, the doubly-graded homology $\CH^{so(3),V}(K)$ is isomorphic to the homology of $\CH^{\mathrm{Kauff}}(K)$
with respect to the corresponding differential $d_3$ from \cite{GWalcher}, after the specialization $\lambda=q^2$.
Usually, that differential $d_3$ acts trivially; in particular, this is the case for all knots that we analyze below.\\

The structure of the homology $\CH^{\tableau2}(K)$ with the above differentials allows us to compute it for various small knots,
as we shall illustrate next.\\


\subsubsection{$\CH^{S^2}$ and $\CP^{S^2}$ for small knots}

The homology $\CH^{\tableau2}(K)$ and the superpolynomial $\CP^{\tableau2}(K)(\a,q,t)$
(= the Poincar\'e polynomial of $\CH^{\tableau2}(K)$)
must satisfy the following properties:

\begin{itemize}

\item
specialization to $t=-1$ gives the reduced $\tableau2$-colored HOMFLY polynomial $P^{\tableau2}(K)$.\footnote{In order to find the colored HOMFLY polynomial $P^{\tableau2}(K)$ one can use {\it e.g.} equation (3.25) in \cite{LMV} and the values for the BPS invariants $\hat{N}_{\tableau2,g,Q}$ tabulated in section 6 of that paper. The result gives the unreduced two-variable colored HOMFLY polynomial. In order to find the reduced polynomial, one should divide the unreduced polynomial by:
\[
\frac{(\a -\a^{-1}) (\a q -\a^{-1}q^{-1}) }{(q-q^{-1})(q^2-q^{-2})} \,.
\]
The results from \cite{LMV} enable us to compute the reduced $\tableau2$-colored HOMFLY polynomial for the knots $3_1$, $4_1$, $5_1$ and $6_1$.
Another useful source of the colored HOMFLY polynomials and their specializations to $\a=q^2$ and $\a=q^3$ is the KnotAtlas \cite{KAt}, which the reader may want to consult for many other knots.}

\item
specialization to $\a=q^2$ gives the Poincar\'e polynomial $\CP^{\tableau2}_2(K)$ of the homology $\CH^{sl(2),\tableau2}(K)$. This homology is isomorphic to $\CH^{so(3),V}(K)$. To find the latter one, we use the results from Table 3 of \cite{GWalcher}, if available.\footnote{In all examples we have computed, the values $i+j$ for all nontrivial Kauffman homology groups $\CH^{\mathrm{Kauff}}_{i,j,k}(K)$ have the same parity. Thus the differential $d_3$ on the Kauffman homology, which is of degree $(-1,2,-1)$, is trivial. Consequently, the Poincar\'e polynomial $\CP^{so(3),V}(K)(q,t)$ is equal to the $\lambda=q^2$ specialization of the Poincar\'e superpolynomial of the Kauffman homology $\CP^{\mathrm{Kauff}}(K)(\lambda=q^2,q,t)$ in all our examples.}

\item
$\CH^{\tableau2}(K)$ comes equipped with the differentials described in section \ref{s2r}.

\end{itemize}

\noindent
These requirements are more than sufficient to determine the colored superpolynomial for many small knots.
As the first example, we consider the trefoil knot:
\begin{example}{The trefoil knot $3_1$}
The reduced $\tableau2$-colored HOMFLY polynomial of the trefoil knot is equal to (see {\it e.g.} \cite{LMV,LZ}):
\[
P^{\tableau2}(3_1) = \a^{2}q^{-2} + \a^2q + \a^2q^2 + \a^2q^4 - \a^3 - \a^3q - \a^3 q^3 - \a^3 q^4 + \a^4q^3 \,.
\]
The homology $\CH^{so(3),V}(3_1)$ is computed in \cite{GWalcher} (see eq. (6.14) and Table 3). Hence we have:
\[
\CP^{\tableau2}_2(3_1)=q^2+q^5t^2+q^6t^2+q^6t^3+q^7t^3+q^8t^4+q^9t^5+q^{10}t^5+q^{11}t^6
\]
{}From these two expressions we immediately deduce the colored superpolynomial of the trefoil\footnote{As discussed in
section \ref{sec:gradings}, there are two different possibilities for grading conventions.
Besides the grading conventions discussed in most of this paper, there are also ``new'' grading conventions
where the $\a$ and $q$ degrees are both twice the value of the corresponding degrees in the conventions that we are using in 
this paper, while the $t$-degree change is more subtle.
The value of the colored superpolynomial of the trefoil in the ``new'' gradings is given by
\[
\CP^{\tableau2}_{\text{new grad.}}(3_1)= \a^4(q^{-4} +q^2t^4+q^4t^6 +q^8t^8) + \a^6 (t^5+q^2t^7 + q^6t^9+q^8t^{11}) +\a^8q^6t^{12}.
\]
We note that in these gradings, the answer coincides with \cite{AShakirov,DMMSS}.}:
\begin{equation}
\CP^{\tableau2}(3_1)= \a^2(q^{-2} +qt^2+q^2t^2 +q^4t^4) + \a^3 (t^3+qt^3 + q^3t^5+q^4t^5) +\a^4q^3t^6.
\end{equation}
Note that its specializations to $t=-1$ and $\a=q^2$ give $P^{\tableau2}(3_1)$ and $\CP^{\tableau2}_2(3_1)$, respectively.
Moreover, the corresponding homology $\CH^{\tableau2}(3_1)$ also enjoys the action of two canceling differentials
and one colored differential.
In order to visualize this homology, we represent each generator by a dot in the $(\a,q)$-plane, with a label denoting its $t$-grading.
In Figure \ref{fig:colored31}, the canceling differential $d^{\tableau2}_1$ is represented by a blue arrow,
the canceling differential $d^{\tableau2}_{-2}$ is represented by a red arrow,
the colored differential $d_{2\to 1}$ is represented by a magenta arrow, while the vertical colored differential $d^{\tableau2}_0$
is represented by dashed light blue arrow.

\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored31}
\caption{The reduced $S^2$-colored homology of the trefoil knot.}
\label{fig:colored31}
\end{figure}

The generator that survives $d_1^{\tableau2}$ has degree $(2,-2,0)$, while the one that survives $d_{-2}^{\tableau2}$ has degree $(2,4,4)$.
Both are consistent with the $S$-invariant of the trefoil $S(3_1)=1$ and the general discussion in section~\ref{s2r}.
The Poincar\'e polynomial of the homology with respect to the colored differential $d_{2\to 1}$ is equal to:
\[
\a^2q^{-2} + \a^2q^4t^4 + \a^4q^3t^6 \,,
\]
while the Poincar\'e polynomial of the homology with respect to the vertical colored differential $d^{\tableau2}_{0}$ is equal to:
\[
\a^2 q^{-2} + \a^2 q^2 t^4 + \a^3 t^3 \,.
\]
A careful reader will notice that the last two expressions are equal to $\CP^{\tableau1}(3_1)(\a^2,q^2,t^2 q)$ and $\a \CP^{\tableau1}(3_1)(\a,q^2,t)$, respectively,
where $\CP^{\tableau1}(3_1)(\a,q,t)$ is the ordinary superpolynomial, whose explicit form is written in \eqref{p31}.
\end{example}

This computation can be easily extended to many other small knots.
We list the results for all prime knots with up to 6 crossings in Tables \ref{tablica} and \ref{tablica2}.
The fact that the structure described in this section works beautifully for all knots with up to 6 crossings is already
an impressive test of our main Conjecture \ref{con2}.
However, to convince even hard-boiled skeptics, in appendix \ref{sec:942} we carry out a much more challenging
computation of the colored HOMFLY homology for ``thick'' knots $8_{19}$ and $9_{42}$.

We notice that all computations of colored homologies in this paper are done by hand, only by using the existence and properties of the
differentials described in this section. Moreover, in majority of the cases only a few of the differentials  are used to obtain the result, which than matched perfectly all the remaining properties.  \\

\begin{table}\begin{center}
\begin{tabular}{|c|l|}
\hline
\rule{0pt}{5mm}
Knot & $\CP^{\tableau{2}}$ \\[3pt]
\hline
\hline
\rule{0pt}{5mm}
$3_1$ & $\a^2 (q^2 t^2 + q^{-2} + q t^2 + q^4 t^4) + \a^3 (q^4 t^5 + q^3 t^5 + t^3 + q t^3) + \a^4 q^3 t^6$ \\[3pt]
\hline
\rule{0pt}{5mm}
$4_1$ & $\a^{-2}q^{-2}t^{-4} + (\a^{-1}q^{-3}+\a^{-1}q^{-2})t^{-3} + (q^{-3}+\a^{-1}q^{-1}+\a^{-1})t^{-2}  +$\\[3pt]
\rule{0pt}{5mm}
& $+(q^{-2}+q^{-1}+\a^{-1}+\a^{-1}q)t^{-1} + (q^{-1}+3+q) + (q^2+q+\a+\a q^{-1})t +$\\[3pt]
\rule{0pt}{5mm}
& $+ (q^3 + \a q+\a)t^2 + (\a q^3+\a q^2)t^3 + \a^2q^2t^4$ \\[3pt]
\hline
\rule{0pt}{5mm}
$5_1$ & $\a^4q^{-4}+(\a^4q^{-1}+\a^4)t^2 + (\a^5q^{-2}+\a^5q^{-1})t^3 +$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^4q^2+\a^4q^3+\a^4q^4)t^4 +(\a^5q+2\a^5q^2+\a^5q^3)t^5+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^4q^5+\a^4q^6+\a^6q)t^6 + (\a^5q^4+2\a^5q^5+\a^5q^6)t^7+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^4q^8+\a^6q^4+\a^6q^5)t^8+(\a^5q^7+\a^5q^8)t^9+\a^6q^7t^{10}.$ \\[3pt]
\hline
\rule{0pt}{5mm}
$5_2$ & $\a^2q^{-2}+(\a^2q^{-1}+\a^2)t+(2\a^2q+\a^2q^2+\a^3q^{-2}+\a^3q^{-1})t^2+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^2q^2+\a^2q^3+2\a^3+2\a^3q)t^3+(\a^2q^4+2\a^3q+3\a^3q^2+\a^3q^3+\a^4)t^4+$\\[3pt]
\rule{0pt}{5mm}
& $+(2\a^3q^3+2\a^3q^4+\a^4+2\a^4q+\a^4q^2)t^5+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^3q^4+\a^3q^5+\a^4q^2+3\a^4q^3+\a^4q^4)t^6+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^4q^3+2\a^4q^4+\a^4q^5+\a^5q^2+\a^5q^3)t^7+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^4q^6+\a^5q^3+\a^5q^4)t^8+(\a^5q^5+\a^5q^6)t^9+\a^6q^5t^{10}.$ \\[3pt]
\hline
\end{tabular}\end{center}
\caption{Colored superpolynomial for prime knots with up to 5 crossings.}
\label{tablica}
\end{table}


\begin{table}\begin{center}
\begin{tabular}{|c|l|}
\hline
\rule{0pt}{5mm}
Knot & $\CP^{\tableau{2}}$ \\[3pt]
\hline
\hline
\rule{0pt}{5mm}
$6_1$ &$\textstyle{ \a^{-2}q^{-2}t^{-4}+(\a^{-1}q^{-3}+\a^{-1}q^{-2})t^{-3}+(\a^{-1}q^{-2}+2\a^{-1}q^{-1}+q^{-3}+\a^{-1})t^{-2}+}$\\[3pt]
\rule{0pt}{5mm}
& $+(q^{-3}+\a^{-1}+3q^{-2}+2q^{-1}+\a^{-1}q)t^{-1}+(\a q^{-3}+2q^{-2}+\a q^{-2}+5+q)+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a q^{-2}+1+3q+3\a q^{-1}+2q^2+2\a)t+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a q^{-1}+4\a+4\a q+q^3+\a^2q^{-1}+\a q^2)t^2+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^2q^{-1}+\a q+2\a^2+3\a q^2+2\a q^3+\a^2q)t^3+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^2+2\a^2q+\a q^3+3\a^2q^2+\a q^4+\a^2q^3)t^4+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^2q^2+2\a^2q^3+\a^3q+\a^3q^2+\a^2q^4)t^5+$\\[3pt]
\rule{0pt}{5mm}
& $+(\a^3q^2+\a^3q^3+\a^2q^5)t^6+(\a^3q^4+\a^3q^5)t^7+\a^4q^4t^8.$ \\[3pt]
\hline
\rule{0pt}{5mm}
$6_2$ & $\a^4q^6t^8+ (\a^3q^6+\a^3q^7)t^7+(\a^4q^3+\a^2q^7)t^6+(2\a^3q^3+2\a^3q^4)t^5+$\\[3pt]
\rule{0pt}{2mm}
& $+(\a^4+\a^2q^3+3\a^2q^4+\a^2q^5)t^4+(2\a^3+2\a^3q+\a q^4+\a q^5)t^3+(3\a^2q+\a^2q^2)t^2+$\\[3pt]
\rule{0pt}{2mm}
& $+(\a^3q^{-3}+\a^3q^{-2}+\a q+\a q^2)t+(\a^2q^{-3}+3\a^2q^{-2}+\a^{2}q^{-1}+q^2)+$\\[3pt]
\rule{0pt}{3mm}
& $+(\a q^{-2}+\a q^{-1})t^{-1}+ \a^2q^{-5}t^{-2}+(\a q^{-5}+\a q^{-4})t^{-3}+q^{-4}t^{-4}+$\\[3pt]
\rule{0pt}{2mm}


& $+(1+q)(1+\a^{-1}qt^{-1})(1+\a^{-1}q^{-2}t^{-3}) \times [\a^4q^4t^7+(\a^4q^3+\a^3q^4)t^6+$\\[3pt]
\rule{0pt}{3mm}
& $+(\a^4q+\a^3q^3)t^5+(\a^3q^2+\a^3q)t^4+\a^3t^3+(\a^3q^{-2}+\a^2)t^2].$\\[3pt]
\hline
\rule{0pt}{5mm}
$6_3$ & $ \a^2q^5t^6+(\a q^5+\a q^6)t^5+(\a^2q^2+q^6)t^4+(2\a q^2+2\a q^3)t^3+$\\[3pt]
\rule{0pt}{3mm}
& $+(\a^2q^{-1}+q+3q^2+q^3)t^2+(2\a q^{-1}+2\a+\a^{-1}q^3+\a^{-1}q^4)t$\\[3pt]
\rule{0pt}{3mm}
&$+(q^{-1}+5+q)+(\a q^{-4}+\a q^{-3}+2\a^{-1}+2\a^{-1}q)t^{-1}+(q^{-3}+3q^{-2}+q^{-1}+\a^{-2}q)t^{-2}+$\\[3pt]
\rule{0pt}{3mm}
&$+(2\a^{-1}q^{-3}+2\a^{-1}q^{-2})t^{-3}+(q^{-6}+\a^{-2}q^{-2})t^{-4}+(\a^{-1}q^{-6}+\a^{-1}q^{-5})t^{-5}+\a^{-2}q^{-5}t^{-6}+$\\[3pt]
\rule{0pt}{3mm}
&$+ (1+q)(1+\a^{-1}qt^{-1})(1+\a^{-1}q^{-2}t^{-3}) \times[\a^2q^3t^5+(\a^2q+\a q^3)t^4+   $\\[3pt]
\rule{0pt}{3mm}
& $+ (\a^2+\a q^2+\a q)t^3+3\a t^2+(\a q^{-1}+\a q^{-2}+1)t+(\a q^{-3}+q^{-1}) +q^{-3}t^{-1}].$\\[3pt]
\hline
\end{tabular}\end{center}
\caption{Colored superpolynomial for prime knots with 6 crossings.}
\label{tablica2}
\end{table}



\subsection{Differentials for higher symmetric representations}

Now let us consider the triply graded homology $\CH^{S^r}$ of knots and links colored by the representation $R = S^r$ with more general $r \ge 1$.
Much as in the case $r=2$ considered in the previous subsection, we expect that $\CH^{S^r}$ comes equipped with the following differentials:

\begin{itemize}

\item
canceling differential $d^{S^r}_1$ of  degree $(-1,1,-1)$, whose homology is one-dimensional and consists of a degree $(rS,-rS,0)$ generator;

\item
canceling differential $d^{S^r}_{-r}$ of degree $(-1,-r,-3)$, which leaves behind a one-dimensional homology with a generator of degree $(rS,r^2S,2rS)$;

\item
for every $1 \le k <r$, there exists a vertical colored differential $d^{S^r}_{1-k}$ of degree $(-1,1-k,-1)$, such that the homology of $\CH^{S^r}$ with respect to $d^{S^r}_{1-k}$ is isomorphic to $\CH^{S^k}$;

\item
for every $1 \le m < r$, there exists a universal colored differential $d_{r \to m}$ which, when acting on $\CH^{S^r}$, leaves behind the homology $\CH^{S^{m}}$. In particular, the colored differential $d_{r\to (r-1)}$ has degree $(0,1,0)$.

\end{itemize}


\subsubsection{Colored superpolynomial $\CP^{S^3}$ for the trefoil}
It can be computed by requiring that its specialization to $t=-1$ equals the reduced $S^3$-colored HOMFLY polynomial and that it enjoys the action of the canceling and the first colored differentials of appropriate degrees. In particular, according to the general rules \eqref{surviving}, we require that the remaining generator with respect to the $d^{\tableau3}_1$ action has degree $(3,-3,0)$, while the remaining generator with respect to the action of $d^{\tableau3}_{-3}$ has degree $(3,9,6)$. For the colored differential $d_{3\to 2}$ we require that the remaining homology should have rank 9, just like $\CH^{\tableau2}(3_1)$. From these, we obtain the following result:
\begin{eqnarray*}
\CP^{S^3}(3_1)&=&\a^3q^{-3}+(\a^3q+\a^3q^2+\a^3q^3)t^2+(\a^4+\a^4q+\a^4q^2)t^3+\\
&&+(\a^3q^5+\a^3q^6+\a^3q^7)t^4+(\a^4q^4+2\a^4q^5+2\a^4q^6+\a^4q^7)t^5+\\
&&+(\a^5q^4+\a^5q^5+\a^5q^6+\a^3q^9)t^6+(\a^4q^8+\a^4q^9+\a^4q^{10})t^7+\\
&&+(\a^5q^8+\a^5q^9+\a^5q^{10})t^8+\a^6q^9t^9.
\end{eqnarray*}
Note, there exists a differential $d_{3\to 1}$ on $\CH^{S^3}(3_1)$ of degree $(0,4,2)$,
such that the homology with respect to this differential is of rank 3, as $\CH^{\tableau1}(3_1)$.

Also, there exists a differential $d^{\tableau3}_0$ of degree $(-1,0,-1)$ such that the Poincare polynomial of $(\CH^{\tableau3}(3_1),d^{\tableau3}_0)$ is equal to $\a^2\,\,\CP^{\tableau1}(3_1) (\a,q^3,t)$.

Finally, there exists a differential $d^{\tableau3}_{-1}$ of degree $(-1,-1,-1)$ such that the homology$(\CH^{\tableau3}(3_1),d^{\tableau3}_{-1})$ is isomorphic to $\CH^{\tableau2}(3_1)$.\\

In Appendix \ref{apb41} we compute also the $S^3$-colored homology of the figure-eight knot $4_1$.



\subsubsection{Size of the homology}
Computations show that for a knot $K$, the rank of the homology $\CH^{S^r}$ grows exponentially with $r$.
In particular, this makes the computation of the homologies $\CH^{S^r}(K)$ difficult for large $r$.
(In fact, even for $r>2$ the size of the homology is too big to make computations practical.)
To be more precise, for all thin and torus knots studied here we find:
\be
\rank \CH^{S^r} (K) \; = \; \left( \rank \CH^S (K) \right)^r \,.
\ee
