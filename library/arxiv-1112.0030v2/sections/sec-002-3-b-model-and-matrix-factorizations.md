---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-002-3-b-model-and-matrix-factorizations
section_title: "B-model and matrix factorizations"
section_number: 3
pages: 10-15
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.982
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
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
