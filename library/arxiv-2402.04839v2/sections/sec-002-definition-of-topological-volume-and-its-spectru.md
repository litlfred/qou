---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-002-definition-of-topological-volume-and-its-spectru
section_title: "Definition of topological volume and its spectrum"
section_number: null
pages: 4-5
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.994
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:definition}

Let $M$ be a closed, orientable 3--manifold.
A \textbf{link} in $M$ is a (possibly empty, possibly disconnected) closed 1--submanifold $L$ of $M.$ 
We consider links up to (not necessarily orientation preserving) diffeomorphisms of their complement $M\setminus L$. This is motivated by the fact that none of the invariants we consider in this article differ on non-isotopic links with diffeomorphic complement.

A link $L$ in $M$ is \textbf{hyperbolic} if its complement admits a complete hyperbolic structure of finite volume. In this case, let $\volh(M\setminus L)$ denote the hyperbolic volume of $M\setminus L.$ We often write $\volh(L) = \volh(M\setminus L).$
Following~\cite[\S 1.3.2]{BBBMP}, let
\begin{equation}
\volt(M) = \inf \big\{ \; \volh(M\setminus L) \;\mid \; L \subset M \text{ is a hyperbolic link } \; \big\}.
\end{equation}
It follows from Mostow--Prasad rigidity that $\volt(M)$ is a topological invariant of $M$, and we term it the \textbf{topological volume} of $M.$ 
The invariant $\volt(M)$ is indeed finite since every closed, orientable 3--manifold contains a hyperbolic knot~\cite{My82,My93}.\footnote{\cite{My93} in fact established that all compact $3$--manifolds, including non-orientable $3$--manifolds, contain hyperbolic knots. However we restrict ourselves to the closed and orientable case.} If $M$ admits a complete hyperbolic structure, then $\volt(M)=\volh(M)$, since volume decreases under Dehn filling.

\begin{example}\label{ex:volume-S3}
As our first example, we observe that $\volt(S^3)=2{v}_0 \approx 2.02988$, where ${v}_0$ is the volume of the ideal regular tetrahedron in hyperbolic $3$-space, and with the figure eight knot as unique minimiser. To see this, recall that \cite{cao-meyerhoff} showed that the complement of the figure eight knot, called $K4a1$ in the Hoste--Thistlethwaite--Weeks knot table \cite{HTWKnots}, and $m004$ in SnapPy's \cite{snappy} \texttt{OrientableCuspedCensus},\footnote{The naming convention throughout this paper follows that of the SnapPy census manifolds. Hence the symbol $m$ means that the corresponding manifolds can be triangulated with at most $5$ ideal tetrahedra.} is a cusped hyperbolic 3--manifold of minimum volume. Indeed, the cusped hyperbolic 3--manifolds of minimum volume are the once-punctured torus bundles $m003$ and $m004$ and they are related by a change in monodromy. However, $m003$ admits no filling to $S^3$ and thus does not represent a knot complement in $S^3$. All exceptional fillings of these two manifolds have the same topological volume.
\end{example}

According to J\o{}rgensen and Thurston (see~\cite{thurston-notes,Gro81, Mai10}), the set of volumes of complete orientable hyperbolic 3--manifolds of finite volume is a closed, non-discrete, well-ordered subset of the positive reals of order type $\omega^\omega.$ Throughout this article, we refer to this fact, as well as related results, as J\o{}rgensen--Thurston theory. In particular, there is always at least one hyperbolic link  $L \subset M$ with $\volt(M) = \volh(M\setminus L)$. We term such a link a \textbf{volume minimiser}. We say that two minimising links are equivalent if they have diffeomorphic complements. Occasionally we refer to the least volume hyperbolic link complement in $M$ as a volume minimiser of $M$ as well. 

\begin{question}
Let $M$ be a closed, orientable $3$--manifold $M$. Suppose $L_1$ and $L_2$ are links realising $\volt(M)$. Is $M \setminus L_1$ diffeomorphic with $M \setminus L_2$?
\end{question}

The manifold $m003$ appears as complement of a minimiser in $L(5,1)$ in two different ways---through the fillings $m003(-1, 1)$ and $m003(0, 1).$ However, there is a diffeomorphism of $m003$ that sends one surgery slope to the other. In particular, the minimising hyperbolic knot in $L(5,1)$ is the same. Hence this is not a counterexample to the following question, which is equivalent to the previous one if the cosmetic surgery conjecture is true.

\begin{question}
Let $M$ be a closed, orientable $3$--manifold $M$. Suppose $L_1$ and $L_2$ are links realising $\volt(M)$. Is there a diffeomorphism $M\to M$ taking  $L_1$ to $L_2$?
\end{question}

It is shown in~\cite{Adams_unbounded_volume} that the set of volumes of hyperbolic knots in any 3--manifold is unbounded. Hence not only determining the minimum but also the study of the spectrum of $\volt$ is interesting. 
Let $\mathcal{V}$ be the set of volumes of all cusped hyperbolic 3--manifolds, and $\mathcal{N}$ be the set of all closed, non-hyperbolic, orientable 3--manifolds. 
\begin{question}
Is $\volt\co \mathcal{N} \to \mathcal{V}$ surjective?
\end{question}
