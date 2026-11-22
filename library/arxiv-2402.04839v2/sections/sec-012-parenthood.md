---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-012-parenthood
section_title: "Parenthood"
section_number: null
pages: 15-15
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.987
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Next, we describe all ways in which the fourteen $1$-cusped manifolds in $\mathcal{V}$ of volumes at most $3.07$ can arise as fillings of the two $2$-cusped manifolds of minimal volume~\cite{agol-2cusped}. These are the Whitehead link complement $m129$ and the Whitehead link sister $m125$; compare~\Cref{sec:WandP}.

\begin{proposition}
	\label{prop:isometry}
	Every manifold in $\mathcal{V}$ can be obtained by filling the first cusp of $m125$ or $m129$. The complete list of surgeries on $m125$ and $m129$ that yield a manifold in $\mathcal{V}$ is shown in~\cref{tab:parent}. Because $m125$ has a symmetry that preserves the cusps but acts as $\bigl(\begin{smallmatrix}0 & -1 \\ 1 & 0\end{smallmatrix}\bigr)$ on the geometric basis, we obtain each manifold that arises as filling of $m125$ in two ways. Both manifolds admit an isometry that interchanges the components and thus we also have the analogous result for the second cusp.
\end{proposition}

\begin{proof}
	For the proof we use a result of Futer--Kalfagianni--Purcell~\cite{FuterKalfagianniPurcell} giving a bound on the possible length of slopes yielding manifolds of volume at most $3.07$. In~\cite{data} we explicitly compute these finite sets of slopes and identify all filled manifolds. The results are summarised in~\cref{tab:parent}.
\end{proof}

\begin{table}[htbp]
	\caption{The parenthood diagram of the low volume $1$-cusped manifolds. \label{tab:whichone}}
	\label{tab:parent}
	\begin{tabular}{lll}
		Manifold & Surgery on $m129$ &Surgery on $m125$ \\
		\toprule	
		$m003$ & $m129(3, 1)  (0,0)$ & $m125(-2, 1)(0,0)$ and $m125(1, 2)(0,0)$\\ 
		
		$m004$ & $m129(-3, 1) (0,0)$ & none \\  
		
		$m006$ & $m129(1, 2) (0,0)$ & $m125(3, 1)(0,0)$ and $m125(-1, 3)(0,0)$\\  
		
		$m007$ & $m129(-1, 2) (0,0)$ & none \\ 
		
		$m009$ & $m129(-4, 1) (0,0)$ & none \\ 
		
		$m010$ & $m129(4, 1) (0,0)$ & none \\ 
		
		$m011$ & none & $m125(-3, 1) (0,0)$ and $m125(1, 3)(0,0)$\\ 
		
		$m015$ & $m129(-3, 2) (0,0)$ & none\\  
		
		$m016$ & none & $m125(3, 2)(0,0)$ and $m125(-2, 3)(0,0)$\\ 
		
		$m017$ & $m129(3, 2) (0,0)$ & none \\  
		
		$m019$ & none & $m125(-3, 2)(0,0)$ and $m125(2, 3)(0,0)$ \\ 
		
		$m022$ & $m129(5, 1)  (0,0)$ & none \\  
		
		$m023$ & $m129(-5, 1)  (0,0)$ & none \\  
		
		$m026$ &none & $m125(4, 1)(0,0)$ and $m125(-1, 4)(0,0)$\\ 
		\bottomrule
	\end{tabular}
\end{table}
