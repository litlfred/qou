---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-006-constructions-of-unbounded-topological-volume
section_title: "Constructions of unbounded topological volume"
section_number: null
pages: 7-8
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.992
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{ssec:unbounded}

The main observation used in this section is that, following J\o{}rgensen--Thurston theory \cite{thurston-notes,Gro81, Mai10}, all hyperbolic 3--manifolds of volume bounded from above by a constant are obtained by Dehn surgery on a finite set of cusped hyperbolic 3--manifolds. In particular, every infinite sequence of hyperbolic manifolds of bounded volume must have a subsequence with converging volumes, and which is obtained from a sequence of Dehn fillings on a fixed cusped hyperbolic $3$--manifold. This implies bounds on a number of topological invariants of those manifolds that have bounded topological volume, such as rank of the fundamental group, rank of homology, and hence number of JSJ pieces or prime summands in a decomposition of the manifold. In more precise terms we have the following result.

\begin{proposition}\label{prop:increasing-complexity}
	Let $\mathbf{I}$ be a real valued topological invariant of $3$--manifolds with the following property: If $M$ denotes a $3$--manifold with at least one torus boundary component $T$, then $\mathbf{I}(M)\geq \mathbf{I}(M(r))$ for all but finitely many slopes $r$, where $M(r)$ denotes the Dehn-filling of $M$ with slope $r$ along the boundary component $T$.
	Let $(M_n)_{n\in\N}$ be a family of closed, orientable $3$--manifolds with $\mathbf{I}(M_n) \rightarrow \infty$ for $n\rightarrow  \infty$. Then $\volt(M_n)\rightarrow \infty$ for $n\rightarrow \infty.$
\end{proposition}

\begin{proof}
Suppose that $(\volt(N_m))_{m\in \N}$ is a bounded sequence. Then, by J\o{}rgensen--Thurston theory, as explained at the beginning of \Cref {ssec:unbounded}, the elements of some subsequence $(N_{m_n})_{n\in\N}=(M_n)_{n\in\N}$ are obtained by Dehn filling a fixed cusped hyperbolic $3$--manifold $M$. This implies that, by assumption, the values $\mathbf{I} (M_{n})$ must also be bounded. This is a contradiction.
\end{proof}

\Cref{prop:increasing-complexity} has the following immediate consequences.

\begin{corollary}\label{cor:topinv}\hfill
	\begin{enumerate}
		\item Let $(M_n)$ be a sequence of closed, orientable $3$--manifolds with unbounded Heegaard genus or surgery number. Then $(\volt(M_n))$ is unbounded.
		\item Let $(M_n)$ be a sequence of closed, orientable $3$--manifolds with unbounded rank of first homology or fundamental group. Then $(\volt(M_n))$ is unbounded.
		\item For each $i$, let $M_i$ be a closed, orientable 3--manifold which is not homeomorphic to $S^3$. Then $\volt(M_1\#\cdots \#M_n) \to \infty$ as $n\to\infty$. 
		\item Let $(M_n)$ be a sequence of closed, orientable Seifert fibered spaces such that the number of exceptional fibres is unbounded. Then $(\volt(M_n))$ is unbounded. 
	\end{enumerate}
\end{corollary}

\begin{proof}
$(1)$ and $(2)$ follow directly from~\Cref{prop:increasing-complexity} since these complexities are well-known not to increase under Dehn filling.
$(3)$ follows from $(2)$ and the fact that the rank of the fundamental group is additive under connected sum. Similarly, the rank of the first homology is unbounded if the number of exceptional fibres in a Seifert fibered space is unbounded and thus $(4)$ follows.
\end{proof}
