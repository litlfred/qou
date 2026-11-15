---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-004-5-mirror-symmetry-for-knots
section_title: "Mirror symmetry for knots"
section_number: 5
pages: 25-30
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.973
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
\label{sec:mirror}

In this section, we observe a remarkable ``mirror symmetry'' relation \eqref{mirwild}
between two completely different triply-graded homology theories associated with symmetric and anti-symmetric representations of $sl(N)$,
which will allow us to formulate even a bigger theory that will contain both.
As a first step, however, we need to extend the discussion in section \ref{sec:reduced} to the HOMFLY homology colored
by anti-symmetric representations of $sl(N)$.


\subsection{Anti-symmetric representations}

Much as for the symmetric representation $S^r$, we can repeat the analysis for the anti-symmetric representations $\Lambda^r$ of $sl(N)$.\\

In particular, for every positive integer $r$ there exists a triply-graded homology theory $\CH^{\Lambda^r}(K)$, together with the collection of differentials $\{d^{\Lambda^r}_{N}\}$, $N\in\Z$, such that the homology with respect to $d^{\Lambda^r}_{N}$ is isomorphic to $\CH^{sl(N),\Lambda^r}(K)$. Moreover, it comes equipped with the collection of ``universal" colored differentials, like in the case of the symmetric representations. The homologies $\CH^{\Lambda^r}(K)$, together with all the differentials, satisfy the same properties as $\CH^{S^r}(K)$ from Conjecture \ref{con2}. \\

Again, we have two canceling differentials, this time $d^{\Lambda^r}_{-1}$
and $d^{\Lambda^r}_r$ of $(\a,q,t)$-degrees $(-1,-1,-3)$ and $(-1,r,-1)$, respectively.
The origin of these differentials is clear, and can be inferred either from deformations of B-model potentials, as in section \ref{sec:matrix},
or from basic representation theory. For example, the fact the representation $\Lambda^r$ of $sl(r)$ is trivial
gives rise to a canceling differential $d^{\Lambda^r}_r$.

Another basic fact is $\Lambda^r \cong \Lambda$ for $\g=sl(r+1)$, which leads to the relation
\be
\CH^{sl(r+1), \Lambda^r} (K) \; \cong \; \CH^{sl(r+1), \tableau{1}} (K) \,.
\ee
For the triply-graded theory $\CH^{\Lambda^r}(K)$, this relation implies that
the $\a=q^{r+1}$ specializations of the homologies $(\CH^{\Lambda^r}(K), d^{\Lambda^r}_{r+1})$
and $(\CH^{\tableau1}(K),d^{\tableau1}_{r+1})$ should be isomorphic.\\

Like in the case of symmetric representations, all the required properties allow computation
of the anti-symmetric homology for various small knots. Below, we provide the details for the trefoil knot.

Using the isomorphism $so(6) \cong sl(4)$ under which the vector representation of $so(6)$
is identified with the anti-symmetric representation of $sl(4)$, we conclude
\be
\CH^{sl(4), \tableau{1 1}} (K) \; \cong \; \CH^{so(6),V} (K)
\ee
{}From this relation\footnote{Here, in comparing the two homology theories we take into account that $q$-gradings differ by a factor of~2.} we immediately find
\be
\CH^{sl(4), \tableau{1 1}} (3_1) =
q^4 + q^{6} t^2 + q^{7} t^2 + q^{8} t^3 + q^{9} t^3 + q^{10} t^4 + q^{11} t^5 + q^{12} t^5 + q^{13} t^6
\ee

Also, for $\frak g = sl(3)$ we have $\Lambda^2 \cong \Lambda$, which implies another useful relation
\be
\CH^{sl(3), \tableau{1 1}} (K) \; \cong \; \CH^{sl(3), \tableau{1}} (K)
\ee
For the trefoil, this gives:
\be
\CH^{sl(3), \tableau{1 1}} (3_1) = q^2 + q^4 t^2 + q^{6} t^3
\label{sl3anti}
\ee
Combining this data with the colored HOMFLY polynomial
\be
P^{\tableau{1 1}} (\a,q) \; = \;
\a^2 (q^{-4} + q^{-2} + q^{-1} + q^2)
- \a^3 (q^{-4} + q^{-3} + q^{-1} + 1)
+ \a^4 q^{-3}
\ee
we easily find the anti-symmetric version of the superpolynomial for the trefoil knot:
\be
\CP^{\tableau{1 1}} (3_1) \; = \;
\a^2 (q^{-4} + q^{-2} t^2 + q^{-1} t^2 + q^2 t^4)
+ \a^3 (q^{-4} t^3 + q^{-3} t^3 + q^{-1} t^5 + t^5)
+ \a^4 q^{-3} t^6
\ee

\begin{figure}[htb]
\centering
\includegraphics[width=4.5in]{colored31A2}
\caption{The reduced $\Lambda^2$-colored homology of the trefoil}
\label{fig:colored31A2}
\end{figure}

The homology $\CH^{\tableau{1 1}} (3_1)$ is shown on the Figure \ref{fig:colored31A2} below. It has the following differentials:

\begin{itemize}

\item canceling differential $d^{\tableau{1 1}}_{-1}$ of $(\a,q,t)$-degree $(-1,-1,-3)$

\item canceling differential $d^{\tableau{1 1}}_2$ of $(\a,q,t)$-degree $(-1,2,-1)$ reflects the fact that $\Lambda^2$ is trivial in $sl(2)$ theory

\item differential $d^{\tableau{1 1}}_3$ of $(\a,q,t)$-degree $(-1,3,-1)$ reflects the fact that $\Lambda^2 \cong \Lambda$ in $sl(3)$ theory
and gives, {\it cf.} \eqref{sl3anti}:
\be
\a^2 q^{-4} t^0 + \a^2 q^{-2} t^2 +\a^3 q^{-3} t^3
\; \overset{\underset{\a=q^3}{}}{=} \;
\CH^{sl(3), \tableau{1 1}} (3_1)

\ee

\item differential $d^{\tableau{1 1}}_0$ of $(\a,q,t)$-degree $(-1,0,-3)$ gives:
\be
\a^2 q^{-2} t^2 + \a^2 q^2 t^4 + \a^3 q^0 t^5 = \a t^2 \CP^{\tableau1}(3_1)(\a,q^2,t).
\ee

\item universal differential $d^{\tableau{1 1}}_{2 \rightarrow 1}$ of $(\a,q,t)$-degree $(0,1,0)$ gives:
\be
\a^2 q^{-4} t^0 + \a^2 q^2 t^4 + \a^4 q^{-3} t^6 \; = \; \CP^{\tableau{1}} (\a^2,q^4,q^{-1} t^2)
\ee

\end{itemize}


\subsection{Mirror symmetry for knot homology}

By computing the triply-graded homologies $\CH^{S^r}(K)$ and $\CH^{\Lambda^r}(K)$ for various small knots,
we discover the following remarkable symmetry between these two classes of theories, labeled by $R = S^r$ and $R = \Lambda^r$:
\be\label{mirsym2}
\CH^{\Lambda^r}_{i,j,*}(K) \cong \CH^{S^r}_{i,-j,*}(K).
\ee
Furthermore, this symmetry extends to the differentials as well. More precisely, let
\be
\phi:\CH^{S^r}(K)\to \CH^{\Lambda^r}(K),
\ee
be the isomorphisms  from (\ref{mirsym2}). Then
\be\label{difsym}
\phi\, d^{S^r}_N = d^{\Lambda^r}_{-N}\, \phi,\quad N\in\Z.
\ee

As the first illustration of the mirror symmetry, let us compare the second symmetric and anti-symmetric homology for the trefoil knot.
{}From Figures \ref{fig:colored31} and \ref{fig:colored31A2} it is clear that ``mirror symmetry" is manifest both
for the homology (\ref{mirsym2}) and for the differentials (\ref{difsym}).
The explicit $t$-grading change in (\ref{mirsym2}) in this case is given~by:
\be\label{mirsym231}
\CH^{\tableau{1 1}}_{i,j,k}(3_1) \cong \CH^{\tableau2}_{i,-j,4i-k-4}(3_1)
\ee
for the trefoil knot.\\

The first implication of the mirror symmetry is that one can combine $\CH^{S^r}(K)$ and $\CH^{\Lambda^r}(K)$ into a single homology theory.
By setting $\CH^r(K)$ to be $\CH^{S^r}(K)$, we obtain the Conjecture \ref{con0}. More precisely, we conjecture the following:

\begin{conjecture}\label{mirrorcon}
For every positive integer $r$ there exists a triply-graded homology theory $\CH^{r}_*(K)=\CH^{S^r}_{i,j,k}(K)$,
that comes with a family of differentials $\{d^{r}_N\}$, with $N\in\Z$, and also with an additional collection of \textit{universal colored} differentials $d_{r\to m}$, for every $1\le m<r$, satisfying the following properties:\\

\noindent$\bullet$ \textbf{Mirror Symmetry}
\[
\CH^{r}_{i,j,*}(K)\cong\CH^{S^r}_{i,j,*}(K)\cong\CH^{\Lambda^r}_{i,-j,*}(K).
\]
\noindent$\bullet$ \textbf{Categorification: } $\CH^{r}_*$ categorifies $P^{S^r}$ and $P^{\Lambda^r}:$
\[
\chi(\CH^{r}_*(K))=P^{S^r}(K)(a,q)=P^{\Lambda^r}(K)(a,q^{-1}).
\]
$\bullet$ \textbf{Anticommutativity:} The differentials $\{d^{S^r}_N\}$ anticommute\footnote{{\it cf.} comments following \eqref{frogtypes}}:
\[
d^{r}_Nd^{r}_M=-d^{r}_Md^{r}_N.
\]
$\bullet$ \textbf{Finite support:}
\[
\dim (\CH^{r}_*)< +\infty.
\]
$\bullet$ \textbf{Specializations:} For $N>1$, the homology of $\CH^{r}_*(K)$ with respect to $d^{r}_N$ is isomorphic to $\CH^{sl(N),S^r}(K)$:
\[
\left(\CH^{r}_*(K), d^{r}_N\right) \cong \CH^{sl(N),S^r}(K).
\]
For $N \le -2r$, the homology of $\CH^{r}_*(K)$ with respect to $d^{r}_N$ is isomorphic to $\CH^{sl(-N),\Lambda^r}(K)$:
\[
\left(\CH^{r}_*(K), d^{r}_N\right) \cong \CH^{sl(-N),\Lambda^r}(K).
\]
$\bullet$ \textbf{Canceling differentials: } The differentials $d^{r}_1$ and $d^{r}_{-r}$  are \textit{canceling}:
the homology of $\CH^{r}_*(K)$ with respect to the differentials $d^{r}_1$ and $d^{r}_{-r}$ is one-dimensional. This
reflects the fact that $S^r$ representation of $sl(1)$ and $\Lambda^r$ representation of $sl(r)$ are trivial.\\

\noindent$\bullet$ \textbf{$sl(N)$ Colored differentials: } For every $1\le k \le r-1$, the homology of  $\CH^{r}_*(K)$ with respect to the differential $d^{r}_{-r-k}$ is isomorphic to $\CH^{k}(K)$:
\[
\left(\CH^{r}_*(K), d^{r}_{-r-k}\right) \cong \CH^{k}(K),\quad 1\le k\le r-1,
\]
reflecting the fact that $\Lambda^{r}\cong \Lambda^k$ for $sl(r+k)$, where $1\le k\le r-1$.\\


\noindent$\bullet$ \textbf{Vertical Colored differentials: } The differentials $d^{r}_{1-k}$, for $1 \le k \le r-1$, have $\a$-degree $-1$, and the homology of $\CH^{r}_*(K)$ with respect to the differential $d^{r}_{1-k}$ is isomorphic (after simple regrading that preserves $\a$- and $t$-gradings), to $\CH^{{k}}_*(K)$:
\[
\left(\CH^{r}_*(K), d^{r}_{1-k}\right) \cong \CH^{k}(K),\quad 1\le k\le r-1.
\]

\noindent$\bullet$ \textbf{Universal Colored differentials: } For any positive integer $m$, with $m<r$, the differentials $d_{r\to m}$have $\a$-degree zero, and the homology of $\CH^{r}_*(K)$ with respect to the colored differential $d_{r\to m}$ is isomorphic (after regrading) to $\CH^{m}_*(K)$:
\[
\left(\CH^{r}_*(K), d_{r\to m}\right) \cong \CH^{m}_*(K).
\]

\end{conjecture}

\begin{example}{$\CH^3$ for the trefoil knot}
As another example of the symmetry \eqref{mirsym2}, and this time for degree higher than $2$, let us consider $\CH^3(3_1)$.
Besides the two canceling differentials $d^3_1$ and $d^3_{-3}$, we also have the differential $d^3_{-4}$ of degree $(-1,-4,-3)$.
The homology with respect to this differential is equal to
\be\label{form331}
(\CH^3(3_1),d^3_{-4}) = \a^3q^7t^4+\a^3q^9t^6+\a^4q^8t^7.
\ee
The explicit $t$-grading change in (\ref{mirsym2}) for the trefoil and $r=3$ is given by:
\be\label{mirsym331}
\CH^{\tableau{1 1 1}}_{i,j,k}(3_1) \cong \CH^{\tableau3}_{i,-j,4i-k-6}(3_1).
\ee
With this change of gradings, the ``mirror image" of (\ref{form331}) is equal to $\a^3q^{-9}t^0+\a^3q^{-7}t^{2}+\a^4q^{-8}t^3$ which,
according to the Conjecture \ref{con0}, should be equal to the homology $(\CH^{\tableau{1 1 1}}(3_1),d^{\tableau{1 1 1}}_{4})$.
In particular, for $\a=q^4$ it implies that the Poincar\'e polynomial of
$(\CH^{\tableau{1 1 1}}(3_1),d^{\tableau{1 1 1}}_{4})$ is equal to $q^3 + q^5 t^2 + q^8 t^3$.
The latter, in turn, is equal to $\CP^{\tableau1}(3_1)(\a=q^4,q,t)$ (see (\ref{p31})),
in agreement with the isomorphism $\Lambda^3\cong \Lambda$ for $sl(4)$.
\end{example}

In Appendix \ref{apb41} we compute $\CH^3$ of the figure-eight knot and show that it satisfies all of the properties from conjecture \ref{mirrorcon}.

It is straightforward to check that the triply-graded colored HOMFLY homologies of other knots
that we computed in Section \ref{sec:reduced} satisfy all the required properties of $\CH^2$.\\

As for the $t$-grading change in (\ref{mirsym2}) for an arbitrary knot,
$\phi$ sends a generator $x$ of $(a,q,t)$-degree $(i,j,k)$ to a generator of degree $(i,-j,4i-k+2r\delta'(x))$.
Here $\delta'(x)$ is a certain grading of the generator $x$, generalizing the $\delta$-grading of the ordinary HOMFLY homology $\CH^{\tableau1}$.
In the case of thin knots, $\delta'$-grading of all generators is equal to the $S$-invariant of knots.\\

Now, since the $t$-gradings of $x$ and $\phi(x)$ have the same parity, by decategorifying (\ref{mirsym2})
we get the following simple and beautiful relation between the colored HOMFLY polynomials:
\be\label{mirsymp}
P^{S^r}(K)(\a,q)=P^{\Lambda^r}(K)(\a,q^{-1}).
\ee
To the best of our knowledge, this relation has not been observed before.
It generalizes the symmetry $q \leftrightarrow q^{-1}$ of the (ordinary) HOMFLY polynomial.\\

Based on the above observations about the mirror symmetry for symmetric and anti-symmetric representations,
we speculate that this symmetry extends to arbitrary representations: for a representation $R$ of $sl(N)$
that corresponds to a partition $\lambda$, we conjecture:
\be\label{mirgeneral}
\CH^{\lambda} (K) \; {\cong}\; \CH^{\lambda^t} (K) \,,
\ee
where $\lambda^t$ is the dual (transpose) partition of $\lambda$.
Here, we also tacitly assume that for every partition $\lambda$ there exists
a triply-graded homology theory $\CH^{\lambda}(K)$ categorifying the $\lambda$-colored HOMFLY polynomial.

Furthermore, decategorifying the isomorphism (\ref{mirgeneral}) we obtain
the following symmetry of the colored HOMFLY polynomials (see appendix \ref{sec:notation} for conventions):
\be\label{mirsympgen}
P^{\lambda}(K)(\a,q) \; = \; P^{\lambda^t}(K)(\a,q^{-1}) \,.
\ee



\subsection{Physical interpretation}
\label{sec:physmir}

The only evidence for the mirror symmetry \eqref{mirgeneral} and for its polynomial version \eqref{mirsympgen}
comes from the physical interpretation of knot homologies / polynomials in terms of BPS invariants.
Indeed, the symmetry \eqref{mirsympgen} of the reduced colored HOMFLY polynomial is a direct consequence
of the corresponding symmetry for the unreduced colored HOMFLY polynomial:
\be
\bar P^{\lambda^t}(K)(\a,q) \; = \; (-1)^{|\lambda|} \; \bar P^{\lambda}(K)(\a,q^{-1}) \,,
\label{mirunnorm}
\ee
where $|\lambda|$ is the total number of boxes in the partition $\lambda$.
This symmetry, in turn, follows\footnote{Another way to derive \eqref{mirunnorm}
is to use the properties of the Clebsch-Gordon coefficients for the symmetric group
$C_{\lambda \mu^t \nu^t} = C_{\lambda \mu \nu}$
and the characters $S_{\lambda^t} (q) = (-1)^{|\lambda|-1} S_{\lambda} (q^{-1})$ in eq.(2.6) of \cite{MV},
which describes the geometric origin of the $q$-dependence
in the colored HOMFLY polynomail.} from the explicit form of the colored HOMFLY polynomial \cite{OoguriV}:
\be
\bar P^{\lambda}(K)(\a,q) \; = \; \sum_{i,j} \frac{\a^i q^j}{q-q^{-1}} N^{\lambda}_{i,j} (K)
\label{HOMFLYBPS}
\ee
written in terms of the ordinary (that is, unrefined) BPS invariants $N^{\lambda}_{i,j} (K)$
and from the property of the integer BPS invariants \cite[eq. (2.17)]{LMV}:
\be
N^{\lambda^t}_{i,j} (K) \; = \; (-1)^{|\lambda|+1} \; N^{\lambda}_{i,-j} (K) \,.
\label{BPSmir}
\ee
Indeed, when combined, \eqref{HOMFLYBPS} and \eqref{BPSmir} imply that
under $q \leftrightarrow q^{-1}$ the unreduced colored HOMFLY polynomial of every knot has parity $(-1)^{|\lambda|}$.
In particular, this is true for the unknot. Hence, the normalized colored HOMFLY polynomial,
defined as the ratio of $\bar P^{\lambda}(K)$ and $\bar P^{\lambda}(\unknot)$,
enjoys the symmetry \eqref{mirsympgen}.

There is a refined / homological version of \eqref{mirunnorm} and \eqref{BPSmir} that leads to \eqref{mirgeneral}.
Much as the colored HOMFLY polynomial can be written in terms of the unrefined BPS invariants $N^{\lambda}_{i,j} (K)$,
the unnormalized superpolynomial of every knot $K$ can be expressed in terms of the refined integer BPS invariants \cite{GSV}:
\be
\bar \CP^{\lambda}(K)(\a,q,t) \; = \; \sum_{i,j,k} \frac{\a^i q^j t^k}{q-q^{-1}} D^{\lambda}_{i,j,k} (K) \,.
\label{superBPS}
\ee
The refined BPS invariants $D^{\lambda}_{i,j,k} (K)$ enjoy a symmetry that generalizes \eqref{BPSmir},
\be
D^{\lambda^t}_{i,j,*} (K) \; = \; D^{\lambda}_{i,-j,*} (K) \,,
\label{refBPSmir}
\ee
and follows from the CPT symmetry of the five-brane theory in \eqref{theoryA} or \eqref{theoryB}.
The normalized / reduced version of the symmetry \eqref{refBPSmir} is precisely \eqref{mirgeneral}.

Further details and interpretation of the mirror symmetry \eqref{mirgeneral} for the triply-graded
knot homology will appear elsewhere.
