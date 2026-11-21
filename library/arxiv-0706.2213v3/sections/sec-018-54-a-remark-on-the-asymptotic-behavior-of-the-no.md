---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-018-54-a-remark-on-the-asymptotic-behavior-of-the-no
section_title: "A remark on the asymptotic behavior of the non–abelian Reidemeister torsion at holonomy"
section_number: 5.4
pages: 28-31
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{ExTb}





We close this paper with some remarks on the behavior of the cusp shape and of the non--abelian Reidemeister torsion at the holonomy for twist knots. 

\begin{remark}[Behavior of the cusp shape]
In {the Notes}~\cite[p.~5.63]{TN}, Thurston explains that the sequence of {exteriors of the twist knots ${J(2, -2m)}$} converges to the exterior of the Whitehead link on Fig. \ref{fig:Whitehead} (link $5^2_1$ in Rolfsen's table~\cite{Rolfsen}). 
Note that, if the number of crossings $m$ increases to infinity, then the {sequence of cusp shapes} of the twist knots $J(2, \pm 2m)$ converges to $2+2i$, which is the common value of the cusp shapes of the Whitehead link, see the graph on Fig.~\ref{graph:cusp_shapes}. This result is a consequence of Dehn's hyperbolic surgery theorem.
\end{remark}

\begin{figure}[!htbp]
\begin{center}
\scalebox{.4}{\includegraphics{GraphCuspShapes}}
\end{center}
\caption{Graph of the cusp shape of $J(2,-2m)$ (from Snappea~\cite{snappea}).}
\label{graph:cusp_shapes}
\end{figure}


\begin{figure}[!htbp]
\begin{center}
\scalebox{.4}{\includegraphics{graphCompare}}
\end{center}
\caption{Graph of $|{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0)|$ and $f(m)=C (\sharp J(2, -2m))^3$.}
\label{graph:compare}
\end{figure}












The graph on Fig.~\ref{graph:compare} gives the behavior of the sequence of the absolute value of  ${\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0)$ with respect to the number of crossings $\sharp J(2, -2m) = 2 + 2m$ of the knot. The order of growth can be deduced by a \lq\lq surgery argument\rq\rq\, using Item (5) of Remark~\ref{remarktwist} and the surgery formula for the Reidemeister torsion~\cite[Theorem 4.1]{Porti:1997}.


\begin{proposition}
The sequence $\left( {|{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0)|} \right)_{m\geqslant 1}$ has the same behavior as the sequence $\left( {C (\sharp J(2, -2m))^3} \right)_{m\geqslant 1}$, for some constant $C$. 
\end{proposition}
\begin{proof}[Ideas of the Proof]
Item (5) of Remark~\ref{remarktwist} gives us that $E_{J(2, -2m)} = \mathcal{W}(1/m)$ is obtained by a surgery of slope $1/m$ on the trivial component of the Whitehead link $\mathcal{W}$. Let $V$ denote the glued solid torus and $\gamma$ its core. Using~\cite[Theorem 4.1 (iii) and Proposition 2.25]{Porti:1997} we have, up to sign:
\begin{equation}\label{surgeryF}

{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0) = {\mathbb T}^{\mathcal{W}}_{(\lambda, \mu' {\lambda'}^{-m})}(\rho_0) \cdot \mathrm{TOR}(V; \sll_{\rho_0}, \gamma)
\end{equation}
where ${\mathbb T}^{\mathcal{W}}_{(\lambda, \mu' {\lambda'}^{-m})}(\rho_0)$ stands for the $(Ad \circ \rho_0)$-non--abelian Reidemeister torsion of the Whitehead link exterior computed with respect to the bases of the twisted homology groups determined by the two curves $\lambda$, and $\mu' {\lambda'}^{-m}$ (see~\cite[Theorem 4.1]{Porti:1997}), and $\mathrm{TOR}(V; \sll_{\rho_0}, \gamma)$ stands for the $(Ad \circ \rho_0)$-non--abelian Reidemeister torsion of the solid torus $V$ computed with respect to its core $\gamma$. Here $\rho_0$ denotes the holonomy representation of the Whitehead link exterior.

To obtain the behavior of ${\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0)$ we estimate the two terms on the right--hand side of Eq.~(\ref{surgeryF}):
\begin{enumerate}
  \item Using~\cite[Proof of Theorem 4.17]{Porti:1997}, it is easy to see that $\mathrm{TOR}(V; \sll_{\rho_0}, \gamma)$ goes as $\frac{1}{4 \pi^2} m^2$ when $m$ goes to infinity.
  \item Using~\cite[Theorem 4.1 (ii)]{Porti:1997}, one can prove that 
  \[
  {\mathbb T}^{\mathcal{W}}_{(\lambda, \mu' {\lambda'}^{-m})}(\rho_0) = {\mathbb T}^{\mathcal{W}}_{(\lambda, \lambda')}(\rho_0) \cdot \left( \frac{1}{\cusp(\lambda, \mu)} - m\right),
  \] 
  where $\cusp = \cusp(\lambda, \mu)$ denotes the cusp shape of $J(2, -2m)$ (computed with respect to the usual meridian--longitude system). Thus, ${\mathbb T}^{\mathcal{W}}_{(\lambda, \mu' {\lambda'}^{-m})}(\rho_0)$ goes as $ {\mathbb T}^{\mathcal{W}}_{(\lambda, \lambda')}(\rho_0) \cdot m$ when $m$ goes to infinity. One can also prove that, at the holonomy, we have 
  \[
  {\mathbb T}^{\mathcal{W}}_{(\lambda, \lambda')}(\rho_0)  = 8(1+i).
  \]
\end{enumerate}
As a result, ${\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_0)$ goes as $C\cdot m^3$ for some constant $C$.
\end{proof}

\clearpage
