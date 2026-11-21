---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-044-95-sums-of-random-variables-with-a-sparse-depend
section_title: "Sums of random variables with a sparse dependency graph"
section_number: 9.5
pages: 78-80
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.942
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
An immediate application of Theorem \ref{thm:dependencygraphsrefined} is the following general result on sums of weakly dependent random variables, to be compared with \cite[\S2.3]{Pen02}. Let $X_n=\sum_{i=1}^{N_n} Y_i$ be a sum of random variables, where the $Y_i$'s have a dependency graph of degree $D_n-1$, and satisfy $\|Y_i\|_\infty \leq A$ for some $A \geq 0$ (independent of $i$). We also assume that $X_n$ is not deterministic, so that its variance is non-zero.

\begin{theorem}\label{thm:modgaussiangeneralsparsegraph}
We assume that the dependency graph of $(Y_i)_{1\leq i \leq N_n}$ is sparse, in the sense that $\lim_{n \to \infty} \frac{D_n}{N_n} = 0 $.\vspace{2mm}
\begin{enumerate}
	\item There exists a positive constant $C$ such that, for all $r \geq 2$, 
$ \left|\kappa^{(r)}\!\left(\frac{X_n}{D_n}\right)\right| \leq (Cr)^r\,\frac{N_n}{D_n}.$\vspace{2mm}
	\item Consider the bounded sequences 
	$$\sigma^2_n=\frac{D_n}{N_n}\,\,\kappa^{(2)}\!\left(\frac{X_n}{D_n}\right)\qquad;\qquad L_n=\sigma_n^3\,\frac{D_n}{N_n}\,\,\kappa^{(3)}\!\left(\frac{X_n}{D_n}\right).$$
	If they have limits $\sigma^2>0$ and $L$, then $$\frac{X_n-\esper[X_n]}{D_n\,\sigma_n}\,\left(\frac{D_n}{N_n}\right)^{1/3}$$ converges in the mod-Gaussian sense with parameters $t_n=(N_n/D_n)^{1/3}$ and limiting function $\psi(z)=\exp(Lz^3/6)$.\vspace{2mm}
\item If furthermore,
    \[ \sigma^2_n = \sigma^2 \left(1 + o\!\left( (D_n/N_n)^{1/3}\right) \right), \]
    then the variable
    \[\frac{X_n-\esper[X_n]}{D_n\,\sigma}\,\left(\frac{D_n}{N_n}\right)^{1/3}\]
    converges in the mod-Gaussian sense with parameters $(N_n/D_n)^{1/3}$ and limiting function $\psi(z)=\exp(Lz^3/6)$
    (the difference with the previous item is that $\sigma_n$ has been replaced by $\sigma$).
\end{enumerate}
\end{theorem}


Of course, if $(2)$ holds, then the results of this paper imply that 
\begin{itemize}
\item $X_n/(\sigma_n \sqrt{N_n D_n})$ satisfies a central limit
theorem, with a normality zone of size $o\!\left(\left(\frac{D_n}{N_n}\right)^{1/6}\right)$;
\item furthermore, for $x>0$,
\begin{equation}
    \label{EqDevProbAtTheEdgeInDepGraphs}
    \proba[X_n-\esper[X_n] \geq (N_n)^{2/3}\,(D_n)^{1/3}\,\sigma_n\,x]=\frac{\E^{-\left(\frac{N_n}{D_n}\right)^{1/3}\frac{x^2}{2}}}{x\sqrt{2\pi (N_n/D_n)^{1/3} }}\,\exp\left(\frac{Lx^3}{6}\right)\,(1+o(1))
\end{equation}
and a similar result holds for negative deviations.
\end{itemize}
The same holds replacing $\sigma_n$ by $\sigma$ if one has the assumption on the speed of convergence of $\sigma_n$ towards $\sigma$, given in the third item of Theorem \ref{thm:modgaussiangeneralsparsegraph}.
If, moreover, the cumulants of $X_n$ satisfy \eqref{eq:limitcumulant},
then \eqref{EqDevProbAtTheEdgeInDepGraphs} still holds when we replace $x$ by a positive sequence $x_n$
tending to infinity with $x_n=o(N_n/D_n)^{1/12}$ --- see Proposition \ref{prop:largedeviationscumulants}.

\begin{center}
\begin{figure}[ht]
\begin{tikzpicture}
\draw (-1,1.5) node {order of fluctuations};
\draw (5,-0) node {moderate deviations ($0<x$):};
\draw (7,-1) node {$\proba\!\left[\frac{X_n-\esper[X_n]}{\sigma \,(N_n)^{2/3}(D_n)^{1/3}} \geq x\right] \simeq \frac{\exp(-(\frac{N_n}{D_n})^{1/3}\frac{x^2}{2})}{x\sqrt{2\pi(\frac{N_n}{D_n})^{1/3}}}\,\exp\left(\frac{Lx^3}{6}\right);$};
\draw (5.7,-2.5) node {central limit theorem ($y \ll (\frac{N_n}{D_n})^{1/6}$):};
\draw (5.6,-3.5) node {$\proba\!\left[\frac{X_n-\esper[X_n]}{\sigma \sqrt{N_n\,D_n}} \geq y\right] \simeq \proba[\mathcal{N}_{\R}(0,1)\geq y].$};
\draw[->,thick] (-2,-4.5) -- (-2,1) ;
\draw[thick] (-2.1,0) -- (-1.9,0);
\draw (0,0) node {$O((N_n)^{2/3}(D_n)^{1/3})$} ;
\draw[->,thick] (-2.1,-2.5) -- (-1.9,-2.5) -- (-1.9,-0.1) ;
\draw (0,-2.5) node {$O((N_n)^{1/2}(D_n)^{1/2})$} ;
\end{tikzpicture}
\caption{Panorama of the fluctuations of a sum of $N_n$ random variables that have a sparse dependency graph, of degree $D_n-1$ with $\lim_{n \to \infty}\frac{D_n}{N_n}=0$.}
\label{FigPanoramaSparseDepGraphs}
\end{figure}
\end{center}
Notice that in the case of independent random variables, $D_n=1$
and we recover the mod-Gaussian convergence of Example \ref{ex:sumiid}.
\bigskip

















































In the next Sections, we shall study some particular cases of Theorem \ref{thm:modgaussiangeneralsparsegraph}. 
We will see that most computations are related to the asymptotic analysis of the first cumulants of $X_n$.

\bigskip
\bigskip
