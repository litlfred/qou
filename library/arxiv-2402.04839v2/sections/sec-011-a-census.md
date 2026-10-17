---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-011-a-census
section_title: "A census"
section_number: null
pages: 12-15
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.995
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:census}

\begin{proposition}\label{prop:census}
The complete list of non-hyperbolic closed 3--manifolds of topological volumes at most $3.07$, their explicit volumes and their minimisers are given in \Cref{tab:complete}. In particular, each of these manifolds contains a unique volume minimiser. In all cases the volume minimiser is a knot.
\end{proposition}

\begin{proof}
From Theorem 1.5 of~\cite{GHMTY21}, cf.~\cite{Mi09}, we know the complete list of cusped hyperbolic 3--manifolds of volume at most $3.07$. These are:
$$\mathcal{V}=\big[m003,m004,m006,m007,m009,m010,m011,m015,m016,m017, m019, m022, m023, m026\big]$$
All of these have exactly one cusp. Hence the non-hyperbolic 3--manifolds of topological volumes at most $3.07$ are precisely the exceptional fillings on these manifolds, and thus there are finitely many.

We claim that the volumes of the manifolds in the above list satisfy:
\begin{align*}
\volh(m003) = \volh(m004) &< \volh(m006) = \volh(m007) \\
&< \volh(m009) = \volh(m010)\\
&< \volh(m011)\\
&< \volh(m015) = \volh(m016)= \volh(m017)\\
&< \volh(m019)\\
&< \volh(m022) = \volh(m023)\\
&< \volh(m026)
\end{align*}
We first note that the above equalities and inequalities are correct if one computes
the volumes with precision \emph{up to two decimal places}. Hence it remains to show that the stated equalities hold. 

We first note that $m003$ and $m004$ are once-punctured torus bundles with monodromies $-RL$ and $RL$, respectively. 
Here $R,L \in \mathrm{SL}(2,\mathbb{Z})$ denote the standard generators
\[
R=\begin{pmatrix}1&1\\0&1\end{pmatrix}, \qquad 
L=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\]
which correspond to right and left Dehn twists about the standard generators of the once-punctured torus. 
Hence they are related by volume-preserving mutation along the fibre and so $\volh(m003)=\volh(m004)$.
Similarly, $m009$ and $m010$ are once-punctured torus bundles with monodromies $RRL$ and $-RRL$, respectively; and $m022$ and $m023$ are once-punctured torus bundles with monodromies $-RRRL$ and $RRRL$, respectively. 
We can verify these homeomorphisms using SnapPy by constructing the once-punctured torus bundles with the given monodromies and checking that they are isometric to the claimed census manifolds.

For $\volh(m006) = \volh(m007)$ and $\volh(m015) = \volh(m016)= \volh(m017)$ we refer to \Cref{app:shapes}, where we use the gluing and completeness equations to show that the manifolds claimed to have the same volume are built from tetrahedra with equal shapes.

In \cite{Du20}, Dunfield provides a complete list of all exceptional fillings of SnapPy \cite{snappy} manifolds with one cusp. This algorithmic search is made feasible by the $6$-theorem of Agol and Lackenby~\cite{agol-bounds,lackenby-6}, and the fact that the low complexity non-hyperbolic closed 3--manifolds that arise can easily be identified.
 
Thus we can determine the topological volume of any exceptional filling along a manifold in $\mathcal V$ as follows. First enumerate all exceptional fillings of the two manifolds of smallest volume. Then enumerate all exceptional fillings of the manifolds with second smallest volume in the list and only keep those non-hyperbolic 3--manifolds that have not yet been found. Then continue this process iteratively. If an exceptional filling is found as fillings of multiple distinct cusped manifolds of the same volume, or by filling one manifold with different surgery coefficients, we report all instances in which it arises. We present the results in \Cref{tab:complete}, where we sort our results by volume. 
\end{proof}

\begin{center}
\begin{longtable}{llll}
\caption{The complete list of non-hyperbolic manifolds of volume less than $3.07$ ordered by their volumes. Here the column \textit{Manifold} contains the Regina name~\cite{Regina} as used by Dunfield \cite{Du20}, where $S2$ $T$, $A$, and $D$ describe the case that the base surface is the $2$-sphere, the $2$-torus, the annulus, and the $2$-disk, respectively. Note that the notation of the Seifert fibered space agrees with the one used in \Cref{cor:SFS_bound} as for example shown in Section 7 of \cite{QA}. The column \textit{Volume} contains a verified approximation of the volume (i.e. at most the last digit is wrong), and the column \textit{Realisations} describes different ways to get the manifold by Dehn filling a SnapPy census manifold. Here and in the rest of this article the slopes in a cusp of a census manifold are measured with respect to the
	\textit{geometric basis} of the cusp given by the two shortest curves. This might in general differ from the Seifert basis if the census manifold is the complement of a knot in $S^3$.
	 \label{tab:complete}} \\
  
    \hline
    Manifold & Volume & Realisations &\\
    \hline
    \hline
    \endfirsthead

    \multicolumn{4}{l}
    { \tablename\ \thetable{} -- continued from previous page} \\
    \hline
    Manifold & Volume & Realisations &\\
    \endhead

    \hline \multicolumn{4}{r}{{continued on next page --}} \\
    \endfoot

    \hline
    \endlastfoot

		$S^3$ & $2.02988321281931$ & $m004(1, 0)$ & \\
		$L(5,1)$ & $2.02988321281931$ & $m003(-1, 1)$ & $m003(0, 1)$\\
		$L(10,3)$ & $2.02988321281931$ & $m003(1, 0)$ &  \\
		$SFS [S2: (2,1) (3,2) (3,-1)]$& $$2.02988321281931$$ & $m003(-2, 1)$ & $m003(1, 1)$   \\
		$SFS [S2: (2,1) (3,1) (7,-6)]$& $2.02988321281931$ & $m004(-1, 1)$ & $m004(1, 1)$    \\
		$SFS [S2: (2,1) (4,1) (5,-4)]$& $2.02988321281931$ & $m004(-2, 1)$ &  $m004(2, 1)$  \\
		$SFS [S2: (3,1) (3,1) (4,-3)]$& $2.02988321281931$ & $m004(-3, 1)$ & $m004(3, 1)$   \\
		$T \times I / [ -2,-1 | -1,-1 ]$ & $2.02988321281931$ & $m003(-1, 2)$ & \\
		$T \times I / [ 2,1 | 1,1 ]$ & $2.02988321281931$ & $m004(0, 1)$ &  \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,2)]$ & $2.02988321281931$ & $m003(1, 2)$ & $m003(-3, 2)$\\
		$SFS [D: (2,1) (2,1)] \cup_{( 0,1 | 1,0)} SFS [D: (2,1) (3,1)]$ & $2.02988321281931$ & $m004(-4, 1)$ & $m004(4, 1)$ \\
		\midrule
		$L(15,4)$ & $2.56897060093671$ & $m006(0, 1)$ & \\
		$L(5,2)$ & $2.56897060093671$ & $m006(1, 0)$ & \\
		$L(3,1)$ & $2.56897060093671$ & $m007(1, 0)$ & \\
		$SFS [S2: (2,1) (3,2) (4,-3)]$ & $2.56897060093671$ & $m006(-1, 1)$ &  \\
		$SFS [S2: (2,1) (2,1) (3,2)]$ & $2.56897060093671$ & $m006(1, 1)$ &  \\
		$SFS [S2: (2,1) (2,1) (5,-2)]$ & $2.56897060093671$ & $m007(1, 1)$ &  \\
		$SFS [S2: (2,1) (3,1) (7,-5)]$& $2.56897060093671$ & $m006(-2, 1)$ &    \\
		$SFS [S2: (3,1) (3,1) (3,-1)]$& $2.56897060093671$ & $m007(0, 1)$ &    \\
		$SFS [S2: (2,1) (4,1) (5,-3)]$& $2.56897060093671$ & $m007(-1, 1)$ &    \\
		$SFS [S2: (2,1) (3,1) (9,-7)]$& $2.56897060093671$ & $m007(-2, 1)$ &    \\
		$SFS [A: (2,1)] / [ 0,-1 | -1,0 ]$ & $2.56897060093671$ & $m006(-3, 1)$ & \\
		$SFS [D: (2,1) (3,1)] \cup_{(-1,1 | 0,1)} SFS [D: (2,1) (3,1)]$ & $2.56897060093671$ & $m006(1, 2)$ & \\
		$SFS [A: (2,1)] / [ 0,1 | 1,0 ]$ & $2.56897060093671$ & $m007(-3, 1)$ & \\
		\midrule
		$L(2,1)$ & $2.66674478344906$ & $m009(1, 0)$ & \\
		$L(6,1)$ & $2.66674478344906$ & $m010(1, 0)$ & \\
		$SFS [S2: (2,1) (2,1) (4,-1)]$ & $2.66674478344906$ & $m010(0, 1)$ &  \\
		$SFS [S2: (2,1) (3,1) (8,-7)]$& $2.66674478344906$ & $m009(0, 1)$ &    \\
		$SFS [S2: (2,1) (4,1) (6,-5)]$& $2.66674478344906$ & $m009(-1, 1)$ &    \\
		$SFS [S2: (3,1) (3,1) (5,-4)]$& $2.66674478344906$ & $m009(-2, 1)$ &    \\
		$SFS [S2: (3,1) (3,2) (3,-1)]$& $2.66674478344906$ & $m010(1, 1)$ &    \\
		$T \times I / [ 3,2 | 1,1 ]$ & $2.66674478344906$ & $m009(1, 1)$ & \\
		$T \times I / [ -3,-2 | -1,-1 ]$ & $2.66674478344906$ & $m010(-2, 1)$ & \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,0)} SFS [D: (2,1) (4,1)]$ & $2.66674478344906$ & $m009(-3, 1)$ & \\
		$SFS [D: (2,1) (2,1)] \cup_{(-1,2 | 0,1)} SFS [D: (2,1) (3,1)]$ & $2.66674478344906$ & $m009(3, 1)$ & \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (4,3)]$ & $2.66674478344906$ & $m010(2, 1)$ & \\
		$L(2,1) \# L(3,1)$ & $2.66674478344906$ &  $m010(-1, 1)$&\\
				\midrule
		$L(9,2)$ & $2.78183391239608$ & $m011(0, 1)$ & \\
		$L(13,3)$ & $2.78183391239608$ & $m011(1, 0)$ & \\
		$SFS [S2: (2,1) (3,2) (4,-1)]$ & $2.78183391239608$ & $m011(-1, 1)$ &  \\
		$SFS [S2: (2,1) (2,1) (3,-2)]$ & $2.78183391239608$ & $m011(1, 1)$ &  \\
		$SFS [S2: (2,1) (3,2) (5,-3)]$ & $2.78183391239608$ & $m011(2, 1)$ &  \\
		$SFS [D: (2,1) (3,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,2)]$ & $2.78183391239608$ & $m011(-1, 2)$ & \\
		\midrule
		$L(19,7)$ & $2.82812208833078$ & $m016(-1, 1)$ & \\
		$L(18,5)$ & $2.82812208833078$ & $m016(0, 1)$ & \\
		$L(21,8)$ & $2.82812208833078$ & $m017(-1, 1)$ & \\
		$L(14,3)$ & $2.82812208833078$ & $m017(0, 1)$ & \\
		$L(7,2)$ & $2.82812208833078$ & $m017(1, 0)$ & \\
		$SFS [S2: (2,1) (4,1) (7,-5)]$& $2.82812208833078$ & $m015(0, 1)$ &    \\
		$SFS [S2: (3,1) (3,1) (5,-3)]$& $2.82812208833078$ & $m015(1, 1)$ &    \\
		$SFS [S2: (2,1) (3,1) (11,-9)]$& $2.82812208833078$ & $m015(-1, 1)$ &    \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,0)} SFS [D: (2,1) (3,2)]$ & $2.82812208833078$ & $m015(2, 1)$ & \\
		$SFS [A: (2,1)] / [ 0,1 | 1,-1 ]$ & $2.82812208833078$& $m015(-2, 1)$ & \\
		$SFS [D: (2,1) (2,1)] \cup_{(1,1 | 0,1)} SFS [D: (2,1) (3,1)]$ & $2.82812208833078$ & $m016(2, 1)$ & \\
		$SFS [D: (2,1) (3,1)] \cup_{(-1,1 | 0,1)} SFS [D: (2,1) (3,2)]$ & $2.82812208833078$ & $m016(-1, 2)$ & \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,1)]$ & $2.82812208833078$ & $m017(-2, 1)$ & \\
		$SFS [A: (2,1)] / ( 0,-1 | -1,1 )$ & $2.82812208833078$ & $m017(2, 1)$ & \\
		\midrule
		$L(17,5)$ & $ 2.944106486676$ & $m019(0, 1)$ & \\
		$L(11,3)$ & $ 2.944106486676$ & $m019(1, 1)$ & \\
		$SFS [S2: (2,1) (3,2) (5,-2)]	$ & $2.944106486676$ & $m019(-1, 1)$ &  \\
		$SFS [D: (2,1) (3,2)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,2)] ]	$ & $2.944106486676$ & $m019(-2, 1)$ &  \\
			\midrule
		$L(7,1)$ & $2.98912028293$ & $m022(1, 0)$ & \\
		$SFS [S2: (2,1) (3,1) (4,-1)]	$ & $2.98912028293$ & $m022(0, 1)$ &  \\
		$SFS [S2: (3,2) (3,2) (4,-3)]	$ & $2.98912028293$ & $m022(-1, 1)$ &  \\
		$SFS [S2: (2,1) (3,1) (9,-8)]	$ & $2.98912028293$ & $m023(0, 1)$ &  \\
		$SFS [S2: (2,1) (4,1) (7,-6)]	$ & $2.98912028293$ & $m023(1, 1)$ &  \\
		$SFS [S2: (3,1) (3,1) (6,-5)]	$ & $2.98912028293$ & $m023(2, 1)$ &  \\
		$T x I / [ -4,-3 | -1,-1 ]	$ & $2.98912028293$ & $m022(2, 1)$ &  \\
		$T x I / [ 4,3 | 1,1 ]	$ & $2.98912028293$ & $m023(-1, 1)$ &  \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (5,4)] ]	$ & $2.98912028293$ & $m022(-2, 1)	$ &  \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,0)} SFS [D: (2,1) (5,1)]$ & $2.98912028293$ & $m023(3, 1)$ &  \\
			\midrule
		$L(19,4)$ & $3.059338057779$ & $m026(0, 1)$ & \\
		$L(8,3)$ & $3.059338057779$ & $m026(1, 0)$ & \\
		$SFS [S2: (2,1) (3,2) (5,-4)]	$ & $3.059338057779$ & $m026(-1, 1)	$ &  \\
		$SFS [S2: (2,1) (3,1) (3,2)]	$ & $3.059338057779$ & $m026(1, 1)$ &  \\
		$SFS [D: (2,1) (3,1)] \cup_{(-1,1 | 0,1)} SFS [D: (2,1) (4,1)]$ & $3.059338057779$ & $m026(1, 2)$ &  \\
		\bottomrule
\end{longtable}
\end{center}

\begin{remark}
Upper bounds on the volume of non-hyperbolic manifolds not appearing in our census can be computed from Dunfield's data~\cite{Du20}. The sharpness on these bounds depends on determining further terms in the volume spectrum of one-cusped hyperbolic 3--manifolds. The data ordered for our setting can be accessed at~\cite{data}.
\end{remark}
