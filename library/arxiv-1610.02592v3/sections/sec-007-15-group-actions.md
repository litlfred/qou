---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-007-15-group-actions
section_title: "Group actions"
section_number: 1.5
pages: 40-42
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.984
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Groups acting of spaces are so important in geometry, that they are sometimes used as a definition of  ``geometry'' itself.


\subsection{Definitions}
The \emph{action} of a group $G$ on a topological space $X$ is a homomorphism 
$$G\to \Omeo (X)$$ 
where $\Omeo(X)$ is the group of all self-homeomorphisms of $X$. The quotient set $X/_G$ is the set of all orbits in $X$ and we give it the usual quotient topology. We denote by $g(x)$ the image of $x\in X$ along the homeomorphism determined by $g\in G$. The action is:
\begin{itemize}
\item \emph{free} if $g(x) \neq x$ for all non-trivial $g\in G$ and all $x\in X$;
\item \emph{properly discontinuous} if any two points $x,y \in X$ have neighbourhoods $U_x$ and $U_y$ such that the set
$$\big\{g \in G\ \big|\ g(U_x) \cap U_y \neq \emptyset \big\}$$
is finite.
\end{itemize}
The relevance of these definitions is due to the following.
\begin{prop} \label{equivalent:prop}
Let $G$ act on a Hausdorff connected space $X$. The following are equivalent:
\begin{enumerate}
\item $G$ acts freely and properly discontinuously;
\item the quotient $X/_G$ is Hausdorff and the map $X \to X/_G$ is a covering.
\end{enumerate}
\end{prop}

A covering of type $X \to X/_G$ is called \emph{regular}. A covering $X \to Y$ is regular if and only if the image of $\pi_1(X)$ in $\pi_1(Y)$ is normal, and in that case $G$ is the quotient of the two groups. In particular every universal cover is regular.
Summing up:

\begin{cor} \label{XG:cor}
Every path-connected locally contractible Hausdorff topological space $X$ is the quotient $\tilde X/_G$ of its universal cover by the action of some group $G$ acting freely and properly discontinuously.
\end{cor}

The group $G$ is isomorphic to $\pi_1(X)$.

\begin{ex} \label{proper:ex}
Let a discrete group $G$ act on a locally compact space $X$. The following are equivalent:
\begin{itemize}
\item the action is properly discontinuous; 
\item for every compact $K\subset X$, the set $\big\{g\ |\ g(K) \cap K \neq \emptyset\big\}$ is finite; \item the map 
$ G \times X \to X \times X$ that sends $(g,x)$ to $(g(x), x)$ is proper.
\end{itemize}
\end{ex}


\subsection{Isometry group}
We now want to consider the case where a group $G$ acts by isometries on a Riemannian manifold $M$. In this case we have a homomorphism
$$G \to \Iso(M)$$
with values in the \emph{isometry group} $\Iso(M)$ of $M$, \emph{i.e.}~the group of all isometries $f \colon M \to M$. The group $\Iso(M)$ is much smaller than $\Omeo (M)$. \index{isometry!isometry group} \index{Myers -- Steenrod theorem}

\begin{teo}[Myers -- Steenrod] \label{MS:teo}
The group $\Iso (M)$ has a natural Lie group structure compatible with the compact-open topology. The map $F\colon \Iso(M) \times M \to M \times M$ that sends
$(\varphi, p)$ to $(\varphi(p), p)$ is proper.
\end{teo}
\begin{cor} If $M$ is compact then $\Iso(M)$ is compact.
\end{cor}

\begin{prop} \label{stabilizer:compact:prop}
The stabilizer of any point $x\in M$ is a compact Lie subgroup of $\Iso(M)$.
\end{prop}
\begin{proof}
The stabilizer of $x$ is closed and hence is a Lie subgroup of $\Iso(M)$. The isometries that fix $x$ are determined by their orthogonal action on $T_xM$ and therefore form a compact Lie subgroup of $O(n)$. 
\end{proof}

The hard part of the Myers -- Steenrod Theorem is to endow $\Iso(M)$ with a Lie group structure. In fact, in all the concrete cases that we will encounter, the Lie group structure of $\Iso(M)$ will be evident from the context, so we will not need the full strength of Theorem \ref{MS:teo}. The rest of the theorem is not difficult to prove and we can leave it as an exercise.

\begin{ex} Prove that $F$ is proper.
\end{ex}

We denote by $\Iso^+(M)$ the subgroup of $\Iso(M)$ consisting of all the orientation-preserving isometries. It has index one or two in $\Iso(M)$.


\subsection{Discrete groups}
Let $M$ be a Riemannian manifold. The group $\Iso(M)$ is a Lie group, so it makes sense to consider discrete subgroups.

\begin{prop} \label{iff:discrete:prop}
A group $\Gamma<\Iso(M)$ acts properly discontinuously on $M$ if and only if it is discrete.
\end{prop}
\begin{proof}
If $\Gamma$ is discrete, Theorem \ref{MS:teo} and Exercise \ref{proper:ex} imply that it acts properly discontinuously. Conversely, if $\Gamma$ acts properly discontinuously then $e\in \Gamma$ is easily seen to be isolated, and we apply Exercise \ref{isolated:ex}.
\end{proof}

If $\Gamma < \Iso(M)$ is discrete and acts freely, the quotient map $M \to M/_\Gamma$ is a covering. Moreover, the Riemannian structure projects from $M$ to $M/_\Gamma$.

\begin{prop} \label{quotient:prop}
Let $\Gamma <\Iso(M)$ act freely and properly discontinuously on $M$. There is a unique Riemannian structure on the manifold $M/_\Gamma$ such that the covering $\pi\colon M \to M/_\Gamma$ is a local isometry.
\end{prop}
\begin{proof}
Let $U\subset M/_\Gamma$ be a well-covered set: we have $\pi^{-1}(U) = \sqcup_{i\in I} U_i$ and $\pi|_{U_i}\colon U_i \to U$ is a homeomorphism. Pick an $i\in I$ and assign to $U$ the smooth and Riemannian structure of $U_i$ transported along $\pi$. The resulting structure on $U$ does not depend on $i$ since the open sets $U_i$ are related by isometries in $\Gamma$. We get a Riemannian structure on $M/_\Gamma$, determined by the fact that $\pi$ is a local isometry.
\end{proof}


\subsection{Measures} \label{measure:descends:subsection}
The case where a group $G$ acts by preserving some measure instead of a Riemannian metric is also very interesting, although quite different. This situation will occur only in Chapter \ref{automorfismi:chapter}.

Let a group $G$ act on a manifold $M$. A Borel measure $\mu$ on $M$ is \emph{$G$-invariant} if $\mu(S) = \mu(g(S))$ for every Borel set $S\subset M$. 

If $G$ acts on $M$ freely and properly discontinuously, then $M \to M/_G$ is a covering and every $G$-invariant measure $\mu$ on $M$ descends to a natural measure on the quotient $M/_G$ which we still indicate by $\mu$. The measure on $M/_G$ is defined as follows: for every well-covered open set $U\subset M/_G$ we have $\pi^{-1}(U) = \sqcup_{i\in I}U_i$ and we assign to $U$ the measure of $U_i$ for any $i\in I$. This assignment extends to a unique Borel measure on $M/_G$ by Proposition \ref{ricoprimento2:prop}.

Note that the measure on $M/_G$ is \emph{not} the push-forward of $\mu$, namely it is not true that $\mu(U) = \mu(\pi^{-1}(U))$.
