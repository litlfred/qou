---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-009-no-internal-relations
section_title: "No Internal Relations"
section_number: null
pages: 46-49
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.991
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:no internal relations}






Let $p^{\times \times} =\left[ p \setminus \operatorname{int}(D^3 \sqcup D^3) \right]  \in P$ be a prime endomorphism. We say a relation is \textit{internal }to $p^{\times \times} $ if there exists a composition of CF generators and $P$ generators such that the composition is again  $p^{\times \times} $, other than the trivial composition $p^{\times \times}  = id_{S^2} \circ p^{\times \times}  = p^{\times \times}  \circ id_{S^2}$. One might reasonably suspect that internal relations could arise: two Morse data on a representative $p$ could induce very different Morse decompositions. Even for two Morse functions that are identical except being related by a simple birth, one could ask if a new critical point is coming from that of a CF generator. But since the prime factors of a manifold is unique up to diffeomorphism, the only $P$ generator that could possibly show up is $p^{\times \times} $ itself. This places a very strong constraint on the possible form of the internal relation.

The following lemma guarantees that there are no such internal relations.

\begin{lemma}\label{sphereinp}
Let $p $ be an oriented prime 3 manifold and $f: p \setminus \operatorname{int}( D^3 \sqcup D^3 )  \to \mathbb{R}$ an admissible Morse function. If a regular level set has a component diffeomorphic to $S^2$, namely $ S \cong S^2 \subset  f^{-1}(r)  $ for some regular value $r$, then either 
\begin{enumerate}
\item $p \cong S^2 \times S^1$
\end{enumerate}
Or one of the following mutually exclusive conditions must be true
\begin{enumerate}\setcounter{enumi}{1}
\item $S$ is the gluing sphere of $p\setminus \operatorname{int}( D^3\sqcup D^3 ) \cong \Big( p\setminus \operatorname{int}(D^3 \sqcup D^3)  \Big) \cup_S S^2\times I$, namely $S$ bounds $S^2\times I$ with the other boundary being the incoming or outgoing boundary of $p\setminus \operatorname{int}(D^3 \sqcup D^3)$, or
\item $S$ is the gluing sphere of $p\setminus \operatorname{int}( D^3 \sqcup D^3  ) 
\cong \Big( p \setminus \operatorname{int}(D^3 \sqcup D^3 \sqcup D^3) \Big)  \cup_S D^3$, or
\item $S$ is the gluing sphere of $\Big( p\setminus \operatorname{int}( D^3\sqcup D^3 )  \Big) 
\cong \operatorname{int}( p\setminus D^3 )  \cup_S \left( S^2\times I \setminus \operatorname{int}( D^3) \right)  $.
\end{enumerate}
\end{lemma}

\begin{proof}
This is a fancy restatement of the fact that an oriented 3-manifold is prime if and only if it's irreducible, except for $S^2 \times S^1$. If $S$ is non-separating, one can take a tubular neighbourhood of the connecting path and show that $p$ must contain a connected sum factor of $S^2\times S^1$. Since $p$ is prime, $p$ must be $S^2\times S^1$. If $S$ is separating, then $p$ has a connected sum factor with attaching sphere $S$. Since $p$ is prime, the other prime factor must be $S^3$, namely $S$ bounds a three-ball in $p$. This three ball could contain the deleted incoming ball, the deleted outgoing ball, neither deleted balls, or both deleted balls. If the three-ball bound by $S $ contains only the incoming or the outgoing ball, then $S$ must be one of the boundary components of $S^2\times I$, the other being the boundary of the incoming/outgoing ball. If the three-ball bound by $S$ contains neither the incoming nor the outgoing three balls, then $S$ is the boundary of a simple $D^3$, glued to the rest of the manifold via $S$. If the three-ball bound by $S$ contains both the incoming and the outgoing ball, then $S$ is the gluing boundary of $\left( S^2 \times I \right)  \setminus \operatorname{int}(D^3)$ to the topologically non-trivial part, which is  $p \setminus \operatorname{int}(D^3)$. See figure \ref{fig:sphereinprimeendo} for a sketch of the latter three cases.
\end{proof}

\begin{figure}[ht]
    \centering
    \incfig{sphereinprimeendo}
    \caption[Spheres in a prime endomorphism]{Classifications of spherical regular surface in a prime endomorphism. The shaded sphere is the regular surface $S\cong S^2$. Not depicted is the case $p=S^2\times S^1$. Note that $p$ here denotes the diffeomorphism class of a connected closed oriented prime 3-manifold, but only up to some finite number of $D^3$ removed.}
    \label{fig:sphereinprimeendo}
\end{figure}





\begin{mycom}
Note that there exist separating spheres in $S^2\times S^1$, for example one could pick $S$ to be the level set near a global minimum. Therefore even though condition 2, 3, 4 are mutually exclusive, they are each compatible with condition 1. 
\end{mycom}

\begin{prop}
There are no internal relations among generators in $\mathcal{G}_2$.
\end{prop}

\begin{proof}
Suppose there is a composition sequence of a prime endomorphism $p^{\times \times} $. Then there exists a Morse function on $p\setminus\operatorname{int}(D^3\sqcup D^3)$ which induces a Morse decomposition containing a factor $\widehat{p}$ diffeomorphic to $p\setminus \operatorname{int}(D^3\sqcup D^3)$ itself. Since $p$ is connected, one of the bounding spheres of the Morse factor $\widehat{p}$ must be the gluing sphere. By lemma \ref{sphereinp}, since $p$ is not $S^2\times S^1$, condition 2 must be true. Hence by naturality of the coherence data (unitors, associators and braiding), the composition can be brought to the form \[
p^{\times \times}  = p^{\times \times}  \circ (\left[ b_1  \right] \circ \left[ b_2  \right] \circ \dots ) 
\]
if the gluing sphere is incoming, or of the form \[
p^{\times \times}  = (\left[ b_1  \right] \circ \left[ b_2  \right] \circ \dots )\circ p^{\times \times}   
\]
if the gluing sphere is outgoing. Here the morphisms $[b_i]$ are generated by CF generators.

Lemma \ref{sphereinp} forces both parentheses to compose to the identity $id_{S^2} = [S^2 \times I]$. And by proposition \ref{prop:keyprop}, they can do so using commutative Frobenius relations. We end up getting the trivial identity relations $p^{\times \times} = p^{\times \times} \circ id_{S^2} = id_{S^2} \circ p^{\times \times} $, and neither case constitutes an internal relation by definition.
\end{proof}

\begin{rmk}
Cerf-theoretically, we have shown that given two Morse functions on $p\setminus \operatorname{int}(D^3 \sqcup D^3)$ and a path connecting them, new critical points coming from CF generators must together cancel to an identity cylinder, attached to the incoming or the outgoing part of $p\setminus \operatorname{int}(D^3 \sqcup D^3)$. They can do so with commutative Frobenius relations. They cannot cancel to a ball like in condition 3 since the only way such ball would attach to the remainder of the manifold is if the remainder has three boundary components, but our prime endomorphisms $p^{\times \times} $ all only have two boundary components. They cannot cancel to a pair of pants like in condition 4 since the only way such pants would attach to the remainder of the manifold is if the remainder has one boundary components. 

While it is true that the Morse data for the prime part might change drastically, it does not concern us-- over the prime part we care only about the diffeomorphism type. 
\end{rmk}

The analogous version for $G_1 $ generators is as follows: 

\begin{lemma}
Let $p $ be an oriented prime 3 manifold and $f: p \setminus  \operatorname{int}(D^3)   \to \mathbb{R}$ an admissible Morse function. If a regular level set has a component diffeomorphic to $S^2$, namely $ S \cong S^2 \subset  f^{-1}(r)  $ for some regular value $r$, then either 
\begin{enumerate}
\item $p \cong S^2 \times S^1$
\end{enumerate}
Or one of the two following mutually exclusive conditions must be true
\begin{enumerate}\setcounter{enumi}{1}
\item $S$ is the gluing sphere of $p\setminus \operatorname{int}(D^3)  \cong \left( p\setminus \operatorname{int}(D^3) \right)  \cup_S S^2\times I$, namely $S$ bounds $S^2\times I$ with the other boundary being the boundary of $p\setminus \operatorname{int}(D^3)$, or
\item $S$ is the gluing sphere of $p\setminus  \operatorname{int}(D^3) \cong p \setminus \operatorname{int}(D^3 \sqcup D^3 ) \cup_S D^3$.
\end{enumerate}
\end{lemma}

\begin{proof}
The proof is identical to the proof of \ref{sphereinp}, except the three ball bound by $S$ may now contain the only boundary ball or not at all. The former gives condition 2 while the later gives condition 3. See figure \ref{fig:sphereinprimeunit} for an illustration of the two cases.
\end{proof}
\begin{figure}[ht]
    \centering
    \incfig{sphereinprimeunit}
    \caption[Spheres in a prime unit]{Classifications of spherical regular surface in a prime unit. The shaded sphere is the regular surface $S\cong S^2$. Not depicted is the case $p=S^2 \times S^1$. Note that $p$ here denotes the diffeomorphism class of a connected closed oriented prime 3-manifold, but only up to some finite number of $D^3$ removed.}
    \label{fig:sphereinprimeunit}
\end{figure}

\begin{prop}
There are no internal relations among generators in $G_1 $.
\end{prop}

\begin{proof}
Suppose there is a composition of a prime unit $p^\times$. Then there exists a Morse function on $p\setminus \operatorname{int}(D^3)$ which induces a Morse decomposition containing a factor $\widehat{p}$ diffeomorphic to $p\setminus \operatorname{int}(D^3)$. Since $p$ is connected, the bounding sphere of $\widehat{p}$ must be a gluing sphere. By the previous lemma, since $p$ is not $S^2\times S^1$, condition 2 must be true. Hence by naturality of the unitors, associators, and braiding, the composition can be brought to the form \[
p^\times = ([b_1 ]\circ [b_2 ] \circ \dots ) \circ p^\times
.\]
where the parenthesis must compose to $[S^2 \times I]$ and the morphisms $[b_i]$ are generated by CF generators.  By proposition \ref{prop:keyprop} can do so with commutative Frobenius relations. We end up with the identity relation $p^\times = id_{S^2} \circ p^\times$, which by definition is not an internal relation.
\end{proof}

\begin{rmk}
While this may be an obvious statement, the lack of internal relations means that under no circumstance can a CF generator exist ``inside'' a prime unit/endomorphism. Therefore intuitively we can think of the prime units/endomorphisms as belonging to a different ``species'' of bordisms, even when studying the underlying Cerf theory.
\end{rmk}
