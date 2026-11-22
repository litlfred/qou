---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-003-4-colored-homfly-homology
section_title: "Colored HOMFLY homology"
section_number: 4
pages: 15-25
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.982
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
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
