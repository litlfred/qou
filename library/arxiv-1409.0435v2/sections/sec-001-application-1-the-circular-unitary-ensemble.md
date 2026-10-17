---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-001-application-1-the-circular-unitary-ensemble
section_title: "Application 1: the Circular Unitary Ensemble"
section_number: null
pages: 3-5
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
Consider the Circular Unitary Ensemble (CUE) which is the set of unitary $n\times n$ matrices with the Haar measure.
The eigenvalues $e^{i\theta_1},\ldots, e^{i\theta_n}$ in this ensemble have the joint probability distribution
\begin{equation}\label{jpdf}
\frac{1}{(2\pi)^n n!}\prod_{1\leq j<k\leq n}|e^{i\theta_j}-e^{i\theta_k}|^2 \prod_{j=1}^nd\theta_j,\qquad \theta_1,\ldots, \theta_n\in [0,2\pi).
\end{equation}
Define the random variable $X=X_{\theta_0}$ as the number of eigenvalues of a CUE matrix on the arc $\gamma=\{e^{i\theta}:-\theta_0\leq \theta\leq \theta_0\}$. The average value of $X_{\theta_0}$ is given by
\begin{equation}
\mathbb E_n(X_{\theta_0})=\frac{\theta_0}{\pi}n.
\end{equation}
Define the moment generating function
\begin{equation}
F_n(\lambda)=\mathbb E_n(e^{\lambda X_{\theta_0}}).
\end{equation}
By (\ref{jpdf}), we can write this as
\begin{eqnarray}
F_n(\lambda)&=&\frac{1}{(2\pi)^n n!}\int_{[0,2\pi]^n}\prod_{1\leq j<k\leq n}|e^{i\theta_j}-e^{i\theta_k}|^2 e^{\lambda X_{\theta_0}}\prod_{j=1}^nd\theta_j\\
&=&
\frac{1}{(2\pi)^n n!}\int_{[0,2\pi]^n}\prod_{1\leq j<k\leq n}|e^{i\theta_j}-e^{i\theta_k}|^2 \prod_{j=1}^ne^{\lambda\chi_\gamma(e^{i\theta_j})}d\theta_j,\label{F integral}
\end{eqnarray}
with $\chi_\gamma$ the characteristic function of the arc $\gamma$.
But using the standard multiple integral representation for Toeplitz determinants, we obtain
\begin{equation}
F_n(\lambda)=e^{n\lambda}D_n(s=e^{-\lambda},\theta_0, W=0).
\end{equation}
This is an identity for any $\lambda\geq 0$.
The moment generating function $F_n(\lambda)$ at large positive values of $\lambda$ contains statistical information about large deviations where $X_{\theta_0}$ is much bigger than its average value. As an illustration, a rough estimate of the integral in (\ref{F integral}) gives us the inequality
\begin{equation}\label{est1}
{\rm Prob}_n\left[X_{\theta_0}\geq p\right]\leq e^{-p\lambda}F(\lambda)=e^{(n-p)\lambda}D_n(e^{-\lambda},\theta_0, 0),
\end{equation}
which holds for any $\lambda\geq 0$ and $p\in\{0,1,\ldots, n\}$. Theorem \ref{theorem: extensionWidom} gives asymptotics for $D_n(e^{-\lambda},\theta_0,0)$ for $\lambda\geq nx_c$. For large $n$, the minimum of the right hand side of (\ref{est1}) in the range $\lambda\geq nx_c$ is attained near
\begin{equation}\lambda=nx_c=-2n\ln\tan\frac{\theta_0}{4}.
\end{equation}
Substituting this value for $\lambda$ and the asymptotic behavior for $D_n(e^{-nx_c},\theta_0,0)$, we obtain
\begin{multline}
{\rm Prob}_n\left[X_{\theta_0}\geq p\right]\leq 
\left(\tan\frac{\theta_0}{4}\right)^{-2n^2+2pn}
\left(\sin\frac{\theta_0}{2}\right)^{n^2}
\\
\times\quad n^{-1/4}\left( \cos \frac{\theta_{0}}{2} \right)^{-1/4} 2^{1/12}e^{3\zeta'(-1)}(1+o(1)),\qquad n\to\infty.
\end{multline}
For typical values of $p\sim \frac{\theta_0}{\pi}n$, and even more generally for $p < (1-c)n$ with 
\begin{equation}
c=\frac{\ln\sin\frac{\theta_0}{2}}{2\ln\tan\frac{\theta_0}{4}},
\end{equation} this estimate does not give any useful information since the right hand side is large for large $n$.
We do get non-trivial information for large deviations from the typical value. If we let $p=n-\omega(n)$, we have
\begin{multline}
{\rm Prob_n}\left[X_{\theta_0}\geq p\right]\leq 
\left(\tan\frac{\theta_0}{4}\right)^{-2n\omega(n)}
\left(\sin\frac{\theta_0}{2}\right)^{n^2}
\\
\times \quad n^{-1/4}\left( \cos \frac{\theta_{0}}{2} \right)^{-1/4}2^{1/12}e^{3\zeta'(-1)}(1+o(1)),
\end{multline}
as $n\to\infty$,
and the right hand side decays whenever $\omega(n)<cn$.
If $\omega(n)=o(n)$ as $n\to\infty$, we observe that the probability to have at least $n-\omega(n)$ eigenvalues on $\gamma$ can be estimated by
\begin{equation}
{\rm Prob_n}\left[X_{\theta_0}\geq n-\omega(n)\right]=\bigO(n^{-1/4}e^{n^2\phi(\theta_0)-2n\omega(n)\ln\tan\frac{\theta_0}{4}}), \qquad \mbox{ as $n\to\infty$,}\label{LDP}
\end{equation}
where the rate function $\phi$ is given by $\phi(\theta_0)=\ln\sin\frac{\theta_0}{2}$.
Note that this is not a large deviation principle since we only have an asymptotic upper bound for the left hand side of (\ref{LDP}). A more detailed analysis of the moment generating function $F(\lambda)$ may lead to better estimates, but it is not our aim to proceed in this direction.
