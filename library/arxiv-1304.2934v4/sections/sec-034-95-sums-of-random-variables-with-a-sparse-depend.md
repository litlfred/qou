---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-034-95-sums-of-random-variables-with-a-sparse-depend
section_title: "Sums of random variables with a sparse dependency graph"
section_number: 9.5
pages: 78-81
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.961
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



















\section{Subgraph count statistics in Erd\"os-R\'enyi random graphs}\label{sec:erdosrenyi}
In this section, we consider Erd\"os-R\'enyi model $\Gamma(n,p_n)$ of random graphs. A random graph $\Gamma$ with this distribution is described as follows. Its vertex set is $[n]$ and for each pair $\{i,j\} \subset [n]$  with $i \neq j$, there is an edge between $i$ and $j$ with probability $p_n$. Moreover, all these events are independent. We are then interested in the following random variables, called {\em subgraph count statistics}. If $\gamma$ is a fixed graph of size $k$, then $\SubGraph_\gamma$ is the number of copies of $\gamma$ {\em contained} in the graph $\Gamma(n,p_n)$ (a more formal definition is given in the next paragraph). This is a classical parameter in random graph theory; see, {\em e.g.}, the book of S. Janson, T. {\L}uczak and A. Ruci\'nski \cite{JLR00}. \bigskip

The first result on this parameter was obtained by P. Erd\"os and A. R\'enyi, \emph{cf.} \cite{ER60}. They proved that, if $\gamma$ belongs to some particular family of graphs (called {\em balanced}),
one has a threshold: namely,
$$\lim_{n \to \infty} \proba[\SubGraph_\gamma >0]=\begin{cases}
    0 & \text{if }p_n=o\left(n^{-1/m(\gamma)}\right); \\
1 & \text{if }n^{-1/m(\gamma)}=o(p_n), \end{cases}
$$
where $m(\gamma)=|E(\gamma)|/|V(\gamma)|$.
This result was then generalized to all graphs by B. Bollob\'as~\cite{Bol01}, but the parameter $m(\gamma)$ is in general more complicated than the quotient above. Consider the case $n^{-1/m(\gamma)}=o(p_n)$, when the graph $\Gamma(n,p_n)$ contains with high probability a copy of $\gamma$. It was then proved by A. Ruci\'nski (see \cite{Ruc88}) that, under the additional assumption $n^2 (1-p_n) \to \infty$, the fluctuations of $\SubGraph_\gamma$ are Gaussian. This result can be obtained using dependency graphs; see {\em e.g.}  \cite[pages 147-152]{JLR00}.\bigskip

Here, we consider the case where $p_n=p$ is a constant sequence ($0<p<1$). The possibility of relaxing this hypothesis is discussed in Subsection \ref{subsec:nonconstantproba}. Denote $\alphan=n^2$ and $\betan=n^{k-2}$, where $k$ is the number of vertices of $\gamma$. It is easy to check that 
$$\esper[\SubGraph_\gamma]=c \,\alphan \,\betan \quad;\quad \Var(\SubGraph_\gamma)=\sigma^2 \,\alphan \,(\betan)^2$$ 
for some positive constants $c$ and $\sigma$ --- see, {\em e.g.}, \cite[Lemma 3.5]{JLR00}. Hence, Ruci\'nski's central limit theorem asserts that,  if $T \sim x \sqrt{\alphan}$ for some fixed real $x$, then
$$ \lim_{n\to \infty} \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}
\betan \geq T \right] = \frac{1}{ \sqrt{2\pi}}
\int_{-\infty}^{x/\sigma} e^{-u^2/2} du.$$
Using Theorem \ref{thm:dependencygraphsrefined}, we shall extend this result to a framework where $x$ tends to infinity, but not to quickly: $(\alphan)^{1/2} \ll T \ll (\alphan)^{3/4}$.

\begin{theorem} \label{thm:moddevgraphs}
    Let $0<p<1$ and $\gamma$ be a graph with $k$ vertices. We consider $\SubGraph_\gamma$ the number
    of copies of $\gamma$ contained in Erd\"os-R\'enyi random graph $\Gamma(n,p)$. Let $\alphan$ and $\betan$ be defined as above.\vspace{2mm}
\begin{enumerate}
\item The renormalized variable 
    $(\SubGraph_\gamma - \esper[\SubGraph_\gamma])/(\alphan^{1/3} \betan)$
    converges mod-Gaussian with parameters $t_{n}=\sigma^{2}\,\alphan^{1/3}$
    and limiting function $\psi(z)=\exp\big(\frac{L}{6} z^{3}\big)$,
    where $\sigma$ and $L$ are computed in Section \ref{subsec:sigma_L}.
The convergence takes place on the whole complex plane with speed of convergence $o(\alphan^{-1/3})$.
\vspace{2mm}

\item Therefore, $(\SubGraph_\gamma - \esper[\SubGraph_\gamma])/(\alphan^{1/2} \betan)$ converges in distribution
towards a Gaussian law, with normality zone $o(\alphan^{1/6})$.
Moreover, the deviation probabilities at the edge of the normality zone and at a slightly larger scale 
are given as follows:
is $x_n$ is a positive sequence bounded away from $0$ with $x_n=o\big(\alphan^{1/12})$, then
\begin{align*}
        \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}    
        {\alphan^{1/2} \, \betan} \geq \sigma^2 \alphan^{1/6} x_n \right] &=
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)).\\
        \proba \left[ \frac{\SubGraph_\gamma - \esper[\SubGraph_\gamma]}    
        {\alphan^{1/2} \, \betan} \leq - \sigma^2 \alphan^{1/6} x_n \right] &=
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{-L(x_n)^3}{6}}\,(1+o(1)).
\end{align*}

        




    \end{enumerate}
\end{theorem}
\smallskip

A similar result has been obtained by H. D\"{o}ring and P. Eichelsbacher in \cite[Theorem 2.3]{DE12}. However, \vspace{2mm}
\begin{itemize}
    \item their result is less precise as they only obtain the equivalence of the logarithms of the relevant quantities (in particular, when we look at the logarithm, the second factor of the right-hand side is negligible);\vspace{2mm}
    \item and they cover a smaller zone of deviation.\vspace{2mm}
\end{itemize}
Unfortunately, we cannot get deviation results when $x_n \sim t \alphan^{1/3}$ for some real number $t$;
this would amount to evaluate $\proba [\SubGraph_\gamma > (1+\varepsilon)\,\esper[\SubGraph_\gamma]]$. For large deviations equivalents of
$$ \log \, \proba [\SubGraph_\gamma >  (1+\varepsilon)\,\esper[\SubGraph_\gamma]], $$
there is a quite large literature, see \cite[Theorem 4.1]{CV11} and \cite{Cha12} for recent results in this field. As we consider deviations of a different scale, our result is neither implied by, nor implies these results. Note, however, that their large deviation results are equivalents of the logarithm of the probability, while our statement is an equivalent for the probability itself.
\bigskip
