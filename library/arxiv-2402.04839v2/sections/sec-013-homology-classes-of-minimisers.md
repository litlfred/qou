---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-013-homology-classes-of-minimisers
section_title: "Homology classes of minimisers"
section_number: null
pages: 15-16
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.991
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:Homology classes of minimisers}

\begin{example}
A minimiser does not need to be nullhomologous. Indeed, the unique minimiser for $L(10,3)$ is given by $m003$; see \Cref{tab:complete}. Since $m003(1,0)$ is diffeomorphic to $L(10,3)$, the minimiser $m003$ represents the complement of a knot $K$ in $L(10,3)$. We claim that $K$ is not nullhomologous. For that we observe that the first homology of $m003$ is isomorphic to $\Z\oplus\Z_5$ and thus $K$ must represent an element of order two in $H^1(L(10,3))$. More concretely, we can describe $K$ as the blue knot in the surgery diagram of $L(10,3)$ along the red unknot $U$ shown in \Cref{fig:m003}. From that diagram we compute the linking number of $K$ and $U$ to be $\pm5$ and thus $K$ represents $5$ in $\Z_{10}\cong H_1(L(10,3))$.
\end{example}

\begin{figure}[htb]
	\centering
	\includegraphics[width=5cm]{m003_new}
	\caption{The surgery on the red unknot yields $L(10,3)$. We can use SnapPy to verify that the complement of the blue knot is isometric to $m003$ and thus represents the minimiser of $L(10,3)$.}
	\label{fig:m003}
\end{figure}

In the proof of \Cref{prop:census} we have listed only those knots that minimise the volume. However, among the $1$-cusped manifolds with volume at most $3.07$ there are more exceptional fillings (that do not realise) $\volt$. These are printed in \Cref{tab:non_minimizers}. Since the homologies of some of these knot complements differ from the homologies of the exteriors of the minimisers from \Cref{tab:complete}, we also obtain examples of minimisers in different homology classes.

\begin{table}[htbp]
	\caption{All other hyperbolic knots in non-hyperbolic manifolds that have volume less than $3.07$. None of these knots is a minimiser since a knot of smaller volume is already presented in \Cref{tab:complete}.}
	\label{tab:non_minimizers}
	\begin{tabular}{lll}
		knot & ambient manifold  & realisation\\
		\toprule	
		$m015$ & $S3$  & $m015(1, 0)$ \\
		$m016$ & $S3$  & $m016(1, 0)$ \\
        $m023$ & $L(3,1)$  & $m023(1, 0)$ \\
        $m019$ & $L(6,1)$  & $m019(1, 0)$ \\
		$m022$ & $L(7,2)$  & $m022(1, 1)$ \\		
		$m007$ & $SFS [S2: (2,1) (3,2) (3,-1)]$ &  $m007(2, 1)$ \\
        $m016$ & $SFS [S2: (2,1) (3,2) (5,-3)]$ &  $m016(1, 1)$ \\
		$m009$ & $SFS [S2: (2,1) (4,1) (5,-4)]$  & $m009(2, 1)$ \\
		$m023$ & $SFS [S2: (3,1) (3,1) (4,-3)]$  & $m023(-2, 1)$ \\
		$m026$ & $SFS [S2: (2,1) (3,1) (9,-7)]$  & $m026(-2, 1)$ \\
        $m016$ & $SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,2)]$  & $m016(-2, 1)$ \\
        $m017$ & $SFS [D: (2,1) (3,1)] \cup_{(-1,1 | 0,1)} SFS [D: (2,1) (3,1)]$  & $m017(-1, 2)$ \\
        $m019$ & $SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,1)]$  & $m019(1, 2)$ \\
		\bottomrule
	\end{tabular}
\end{table}

\begin{example}
In \Cref{tab:hom} we display the isomorphism types of the homologies of the knot exteriors from \Cref{tab:non_minimizers} whenever the homology differs from the homology of the minimiser. For example, the minimiser $m010$ of $L(6,1)$ is nullhomologous in $L(6,1)$, while the hyperbolic knot with second smallest volume $m019$ represents a generator in the homology of $L(6,1)$. 
\end{example}

\begin{example}
We also have examples of manifolds where the knot with smallest and the knot with second smallest hyperbolic volumes represent different non-trivial torsion elements in homology. For example, let $M$ be $SFS [S2: (2,1) (3,2) (3,-1)]$. Then the volume of $M$ is realised by $m003$ and the hyperbolic knot with second smallest volume is given by $m007$. Since their homologies are different they represent different non-trivial torsion elements in $H_1(M)\cong\Z_{15}$.
\end{example}

\begin{table}[htbp]
	\caption{Homologies of the minimisers compared with the homologies of the knots from \Cref{tab:non_minimizers}.}
	\label{tab:hom}
	\begin{tabular}{llllll}
		 ambient manifold  & homology & minimiser & homology & knot & homology \\
		\toprule
		$L(6,1)$  & $\Z_6$ & $m010$ & $\Z_6 + \Z$& $m019$ & $\Z$  \\
		$SFS [S2: (2,1) (3,2) (3,-1)]$  & $\Z_{15}$ & $m003$ & $\Z_5 + \Z$ & $m007$ & $\Z_3 + \Z$  \\
		$SFS [S2: (2,1) (4,1) (5,-4)]$  & $\Z_2$ & $m004$ & $\Z$ & $m009$ & $ \Z_2+ \Z$  \\
		$SFS [S2: (3,1) (3,1) (4,-3)]$  & $\Z_3$ & $m004$ & $\Z$ & $m023$ & $\Z_3 + \Z$  \\
		$SFS [S2: (2,1) (3,1) (9,-7)]$  & $\Z_3$ & $m007$ & $\Z_3 + Z$ & $m026$ & $\Z$  \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,2)]$  & $\Z_{20}$ & $m003$ & $\Z_5 + \Z$ & $m016$ & $\Z$  \\
		$SFS [D: (2,1) (3,1)] \cup_{(-1,1 | 0,1)} SFS [D: (2,1) (3,1)]$  & $\Z_{35}$ & $m006$ & $\Z_5 + \Z$ & $m017$ & $\Z_7 + \Z$  \\
		$SFS [D: (2,1) (2,1)] \cup_{(0,1 | 1,1)} SFS [D: (2,1) (3,1)]$  & $\Z_{28}$ & $m017$ & $\Z_7 + \Z$ & $m019$ & $\Z$  \\
		\bottomrule
	\end{tabular}
\end{table}
