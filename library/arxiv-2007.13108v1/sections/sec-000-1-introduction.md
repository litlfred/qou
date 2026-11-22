---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.943
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
In the Euclidean space $\RR^n$, \emph{log-concave} measures, namely measures whose density is of the form $e^{-U}$ with $U$ being a convex potential are known to satisfy several concentration inequalities. For instance, if $\gamma$ is the standard Gaussian measure on $\RR^n$ and the probability measure $\nu$ is absolutely continuous with respect to $\gamma$ with density $d \nu = e^{V} d \gamma$ where the potential $V:\RR^n \to \RR$ satisfies the condition
\begin{equation}\label{eq:Rnsemilogconcave}
\nabla^2 V \preceq (1-\delta) \Id,
\end{equation}
then for every $1$-Lipschitz test function $\varphi$, we will have $\Var_\nu[\varphi] \leq \frac{1}{\delta}$, see e.g., \cite{Saumard14}. In fact, much stronger concentration, for instance in the form of a logarithmic Sobolev inequality, is known to hold in this case.

The objective of this work is to try to generalize the notion of log-concavity to the Boolean hypercube in a way that analogous concentration inequalities are attained. Define $\DC := \{-1,1\}^n$. We say that a function $\varphi:\DC \to \RR$ is $1$-(Hamming)-Lipschitz if
$$
|\varphi(x) - \varphi(y)| \leq \|x-y\|_1, ~~ \forall x,y \in \DC.
$$
Let $\mu$ be the uniform measure on $\DC$. Suppose that $d \nu = e^V d \mu$. Given a $1$-Lipschitz function $\varphi$, it is a trivial fact that $\Var_\nu[\varphi] \leq n^2$, and this bound is sharp in general (e.g., take $\varphi(x) = \sum_i x_i$ and $\nu$ which assigns mass $1/2$ to $(-1,\cdots,-1)$ and $(1,\dots,1)$). We are interested in the question of finding sufficient conditions on the potential $V$, analogous to \eqref{eq:Rnsemilogconcave}, under which a nontrivial bound for $\Var_\nu[\varphi]$ is implied. Let us mention that in the case of the \emph{continuous} hypercube, concentration results of this nature we obtained by Klartag (\cite{Klartag-cube}).

It is clear that any potential $V: \DC \to \RR$ is the restriction of some convex function on $\RR^n$ to $\DC$, meaning that the notion of convexity has to either consider the discrete derivatives of $V$ or to consider the continuous Hessian applied to a suitably chosen interpolation. Our suggested notion of convexity is roughly based on the multi-linear interpolation, but the formal definition will first be given in terms of the logarithmic Laplace transform. Define,
$$
\mathcal{L}[\nu](x) = \log \int_{\DC} e^{\langle x, y \rangle} d \nu(y), ~~ \forall x \in \RR^n.
$$
The function $\mathcal{L}[\nu]$ is known as the log-Laplace transform of the measure $\nu$. We are now ready to define our main notion of \emph{semi-log-concavity}.
\begin{definition} (Semi log-concave measures).
Given a measure $\nu$ on $\DC$, We say that $\nu$ is $\beta$-semi-log-concave if
\begin{equation}\label{eq:semilc}
\nabla^2 \mathcal{L}[\nu](x) \preceq \beta \Id, ~~ \forall x \in \RR^n,
\end{equation}
where the inequality is in the positive-definite sense.
\end{definition}

Our main theorem gives a nontrivial concentration bound for Lipschitz functions with respect to such measures.
\begin{theorem} \label{thm:main}
	Let $\beta \geq 1$. If $\nu$ is a $\beta$-semi-log-concave probability measure on $\DC$ and $\varphi$ is $1$-Lipschitz, then
	$$
	\Var_\nu[\varphi] \leq C \beta n^{2 - c/\beta} 
	$$
	where $C,c>0$ are universal constants.
\end{theorem}
The theorem shows in particular that for any $\beta \in \RR$ there exists $n$ large enough such that $\beta$-semi-log-concave measures on $\DC$ admit nontrivial concentration. \\

Before we proceed, let us give an alternative and slightly stronger notion of semi-log-concavity which could hopefully shed some light and give better intuition regarding the relation to the usual notion of log concavity in $\RR^n$. We first need to recall the \emph{multi-linear} extension of the measure into the continuous hypercube, $[-1,1]^n$. Given a function $f:\DC \to \RR$, it is known that there is a unique function $\hat f:2^{[n]} \to \RR$ such that
\begin{equation}\label{eq:Fourier}
f(x) = \sum_{A \subset [n]} \hat f(A) \prod_{i \in A} x_i.
\end{equation}
The function $\hat f$ is known as the Walsh-Fourier transform of $f$. Observing that the above form makes sense as a function from $[-1,1]^n$ to $\RR$, we refer to this as the multi-linear (or harmonic) extension of $f$. Since the two coincide on $\DC$, below we allow ourselves to use the same notation for both the function and its multi-linear extension. The following fact is attained via a simple calculation, see Section \ref{sec:harmonic} below.
\begin{fact} \label{fact:harmonic}
Suppose that 
\begin{equation}\label{eq:lc2}
\nabla^2 \log \frac{d \nu}{d \mu}(x) \preceq \beta \Id, ~~ \forall x \in [-1,1]^n.
\end{equation}
Then $\nu$ is $(\beta+3)$-semi-log-concave.
\end{fact}
Thus, a corollary to Theorem \ref{thm:main} is that the condition \eqref{eq:lc2} implies that every $1$-Lipschitz function $\varphi$ satisfies $\Var_\nu[\varphi] \leq C(\beta+3)n^{2 - c/(\beta+3)}$.
\medskip
\begin{remark}
Let $f$ be the multi-linear extension of $\frac{d \nu}{d \mu}$. Since $f$ is harmonic and since $\nabla \log f = \frac{\nabla^2 f}{f} - \frac{\nabla f^{\otimes 2}}{f^2}$, we see that in order for $f$ to be log-concave, the Hessian of $f$ can have at most one positive eigenvalue, due to which the family of log-concave functions, or in other words functions satisfying condition \eqref{eq:lc2} with $\beta = 0$, is rather restricted. Semi-log-concave measures are a much richer family, as demonstrated below. 
\end{remark}
