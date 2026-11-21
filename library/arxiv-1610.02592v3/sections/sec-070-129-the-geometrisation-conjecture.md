---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-070-129-the-geometrisation-conjecture
section_title: "The geometrisation conjecture"
section_number: 12.9
pages: 409-413
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.744
latex_coverage_ratio: 0.917
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{geometrisation:section}

We can finally state the famous Geometrisation Conjecture, proposed by Thurston in 1982 and proved twenty years later by Perelman in 2002.


\subsection{Statement and main consequences}
We say that a compact 3-manifold with (possibly empty) boundary consisting of tori is \emph{geometric} if its interior has a finite-volume complete geometric structure modelled on one of the eight geometries:\index{three-manifold!geometric three-manifold} 
$$S^3,\ \matR^3,\ \matH^3,\ S^2\times \matR,\ \matH^2\times \matR,\ \Nil,\ \Sol,\ \widetilde{\SL_2}.$$
The following conjecture was formulated by Thurston in 1982:\index{geometrisation conjecture}

\begin{conj}[Geometrisation Conjecture]
Let $M$ be an irreducible orientable compact 3-manifold with (possibly empty) boundary consisting of tori. Every block of the geometric decomposition of $M$ is geometric.
\end{conj}

The conjecture has been proved by Perelman in 2002 and its proof goes very very far from the scope of this book. It is however quite easy to deduce important consequences from it.

\begin{conj}[Poincar\'e conjecture] \label{Poincare:conj}
Every simply connected closed 3-manifold $M$ is diffeomorphic to $S^3$.
\end{conj}
\begin{proof}[Proof using geometrisation]
Via the prime decomposition we may restrict to the case $M$ is prime, hence irreducible. The group $\pi_1(M)$ is trivial and hence does not contain $\matZ \times \matZ$: every torus in $M$ is thus compressible and the geometric decomposition is trivial. By geometrisation $M$ is itself geometric. The only geometry with finite fundamental groups is $S^3$, and hence $M= S^3/_\Gamma$ is elliptic. Since $M$ is simply connected, the group $\Gamma = \pi_1(M)$ is trivial and hence $M=S^3$.
\end{proof}

\begin{conj}[Elliptisation]  \label{finite:conj}
Every closed 3-manifold $M$ with finite $\pi_1(M)$ is elliptic.
\end{conj}
\begin{proof}[Proof using geometrisation]
Same proof as above. Note that this is \emph{not} a consequence of Poincar\'e conjecture in general, for a manifold covered by $S^n$ needs not to be elliptic a priori.
\end{proof}

\begin{conj}[Hyperbolisation] \label{hyperbolisation:conj}
Every closed irreducible 3-manifold $M$ with infinite $\pi_1(M)$ not containing $\matZ \times \matZ$ is hyperbolic.
\end{conj}
\begin{proof}[Proof using geometrisation]
Since $\pi_1(M)$ does not contain $\matZ\times \matZ$ every torus is compressible and the geometric decomposition of $M$ is trivial. By geometrisation $M$ is geometric. Its geometry is not $S^3$ since $\pi_1(M)$ is infinite, and is not $S^2\times \matR$ since $M$ is irreducible. In the other Seifert geometries and in $\Sol$ the fundamental group $\pi_1(M)$ always contain a $\matZ\times \matZ$ (there is always a finite covering containing an incompressible torus).
\end{proof}

\begin{cor} 
Let $\tilde M \to M$ be a finite covering. If $\tilde M$ is geometric, then $M$ also is (with the same geometry).
\end{cor}
\begin{proof}[Proof using geometrisation]
Note that this is stronger than Conjecture \ref{finite:conj}. 
Since $\tilde M$ is geometric, it is irreducible and hence also $M$ is. Proposition \ref{JSJ:lifts:prop} implies that the geometric decomposition of $M$ is trivial, and by geometrisation $M$ is geometric.
\end{proof}

Concerning bounded manifolds, we get the following simple statement.

\begin{cor} \label{simple:bounded:hyperbolic}
Every simple compact manifold $M$ bounded by a non-empty collection of tori is hyperbolic.
\end{cor}
\begin{proof}[Proof using geometrisation]
Being simple, it is geometric. Seifert manifolds with boundary are never simple.
\end{proof}

That statement is not true for closed manifolds, because many Seifert manifolds fibering over $S^2$ with at most 3 singular fibres are simple. 


\subsection{Surface bundles}
There is a nice way to formulate geometrisation for surface bundles. 
We start with the much simpler torus case.

\begin{prop}
Let $M_A$ be a torus bundle with monodromy $A \neq \pm I$. The following holds:
\end{prop}
\begin{itemize}
\item if $|\tr A|<2$, \emph{i.e.}~$A$ has finite order, then $M_A$ is flat;
\item if $|\tr A|=2$, \emph{i.e.}~$A$ is reducible, then $M_A$ is $\Nil$;
\item if $|\tr A|>2$, \emph{i.e.}~$A$ is Anosov, then $M_A$ is $\Sol$.
\end{itemize}
\begin{proof}
Use Proposition \ref{torus:bundle:prop}.
\end{proof}

We now turn to the generic case. Let $\Sigma$ be a closed orientable surface with $\chi(\Sigma)<0$.
\begin{teo} \label{fibering:geometrisation:teo}
Let $M_\psi$ be a surface bundle with fibre $\Sigma$ and monodromy $\psi \in \MCG(\Sigma)$. The following holds:
\begin{itemize}
\item if $\psi$ has finite order, then $M_\psi$ has a $\matH^2 \times \matR$ geometry,
\item if $\psi$ is reducible, then $M_\psi$ contains an essential torus,
\item if $\psi$ is pseudo-Anosov, then $M_\psi$ is hyperbolic.
\end{itemize}
\end{teo}
\begin{proof}[Proof using geometrisation]
Use Proposition \ref{trichotomy:prop}.
\end{proof}

Theorem \ref{fibering:geometrisation:teo} was initially proved by Thurston in the 1980s. In the same years Thurston also proved the geometrisation conjecture for all Haken 3-manifolds. Before Perelman's proof the conjecture was open ``only'' in the non-Haken case, and it naturally split in three parts: the Conjectures \ref{Poincare:conj}, \ref{finite:conj}, and \ref{hyperbolisation:conj}. Perelman's proof certifies geometrisation in all cases with a unified technique.


\subsection{References}
This chapter contains many technical proofs. Most of them were taken from Scott \cite{S}, that is the standard reference on the geometrisation of Seifert manifolds, and Thurson's book \cite{Th_book}. We have also consulted a nice survey of Bonahon \cite{B3}, that contains in particular the suggestion of calculating the Ricci tensors in the non-product geometries. Thurson's geometrisation conjecture appears in \cite{Th_conj} in 1982, while Perelman's proof consists of three papers that he sent to the arXiv in 2003 \cite{Pe1, Pe2, Pe3}.



\chapter{Mostow rigidity theorem} \label{Mostow:chapter}
We have defined in Chapter \ref{Teichmuller:chapter} the
Teichm\"uller space $\Teich(S_g)$ of a genus-$g$ closed orientable surface $S_g$ as the space of all the hyperbolic metrics on $S_g$, considered up to isometries isotopic to the identity; we have then proved that $\Teich(S_g)$ is homeomorphic to $\matR^{6g-6}$ using the Fenchel--Nielsen coordinates.

This definition of $\Teich(M)$ actually applies to any closed hyperbolic manifold $M$, and we show here a striking difference between the dimensions two and three: if $\dim M = 3$ then $\Teich(M)$ is a single point. This strong result is known as the \emph{Mostow rigidity Theorem}.\index{Mostow--Prasad rigidity theorem} 

The impact of Mostow's rigidity on our understanding of three-dimensional topology cannot be overestimated. Thanks to this theorem every geometric information on a given closed hyperbolic three-manifold $M$ like its volume, geodesic spectrum, etc.~is promoted to a \emph{topological} invariant of $M$, that is it depends on the differentiable structure of $M$ only. In its strongest version, Mostow's rigidity says that the hyperbolic metric of $M$ is fully determined by the group $\pi_1(M)$ alone. 

We expose here Gromov's proof of Mostow's rigidity, which uses hyperbolic tetrahedra and introduces a nice invariant on closed manifolds of any dimension, called the \emph{simplicial volume}.\index{simplicial volume}
