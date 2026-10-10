---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-18
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.629
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
We consider Toeplitz determinants of the form
\begin{equation}\label{Toeplitz}
D_n(f) = \det(f_{j-k})_{j,k=0,\ldots, n-1},\qquad f_{j} = \frac{1}{2\pi} \int_{0}^{2\pi} f(e^{i\theta}) e^{-ij\theta} d\theta,
\end{equation}
where the symbol $f$ is given by
\begin{equation}\label{symbol}
f(e^{i\theta}) = e^{W(e^{i\theta})}\ \times\ 
\begin{cases}
1,&\mbox{ for $-\theta_0\leq \theta\leq \theta_0$,}\\
s,&\mbox{ for $\theta_0<\theta<2\pi-\theta_0$,}
\end{cases}
\end{equation}
and $f_{k}$ is the $k$-th Fourier coefficient of $f$. The symbol depends on the parameters $s\in [0,1]$ and $\theta_0 \in (0,\pi)$, and on a function $W(z)$ which we assume to be analytic in a neighbourhood of the unit circle. In the simplest case where $W(z)=0$, $f$ is piecewise constant with jump discontinuities at $e^{\pm i\theta_0}$.  


For $s\in [0,1]$ and $\theta_0\in(0,\pi)$ fixed, the large $n$ asymptotic behavior for the Toeplitz determinants $D_n(f)=D_n(s,\theta_0,W)$ is well understood.
For $s=0$, the symbol is supported on the arc $\gamma= \{e^{i\theta}:-\theta_0\leq \theta\leq \theta_0\}$. If $f$ is positive on $\gamma$ and symmetric, $f(e^{i\theta}) = f(e^{-i\theta})$, we have the following asymptotics due to Widom \cite{Widom},
\begin{multline} \label{Asymptotic_one_arc}
\ln D_n \left(s=0, \theta_{0},W \right) = n^2\ln \sin  \frac{\theta_0}{2}  + n\widetilde{W}_0 - \frac{1}{4} \ln n  \\
+\sum_{k=1}^{\infty}k\widetilde{W}_k\widetilde{W}_{-k}-\frac{1}{4}\ln\cos\frac{\theta_0}{2}+\frac{1}{12}\ln 2 +3\zeta'(-1)+ o(1), \qquad\mbox{ as $n\to\infty$},
\end{multline}
where $\widetilde{W}_k$ is the $k$-th Fourier coefficient of $\widetilde{W}$, defined by
\begin{equation}
\widetilde{W}(e^{i\theta}) = W(e^{2i\arcsin ( \sin \frac{\theta_{0}}{2}\sin \frac{\theta}{2} )}),
\end{equation}
and where $\zeta$ is the Riemann $\zeta$-function.
For $W=0$, it was shown in \cite{Krasovsky, Krasovsky2} that this result holds not only for $0<\theta_0<\pi$ fixed, but also if $\theta_0$ approaches $\pi$ slowly enough such that $n(\pi-\theta_0)$ is large. The error term in (\ref{Asymptotic_one_arc}) then becomes $\bigO(n^{-1}(\pi-\theta_0)^{-1})$. 



On the other end of the parameter range for $s$, we have $s=1$: here the symbol is smooth and we have the Szeg\H{o} asymptotics
\begin{equation} \label{Asymptotic_Szego}
\ln D_n \left(s=1, \theta_{0}, W \right) = nW_0+\sum_{k=1}^{\infty}kW_kW_{-k}+ o(1), \qquad \mbox{ as } n \to \infty.
\end{equation}
For $0 < s < 1$, $f$ has two jump discontinuities which are special cases of Fisher-Hartwig (FH) singularities. FH singularities are generally characterized by two parameters: $\alpha$, which describes a root-type singularity, and $\beta$, which describes a jump discontinuity. Our symbol $f$ has Fisher-Hartwig singularities at $e^{\pm i\theta_0}$ with parameters $\alpha=0$ (which means that there are no root-type singularities) and $\beta=\mp \frac{1}{2\pi i} \log s$.
Asymptotics for Toeplitz determinants with Fisher-Hartwig singularities have been studied by many authors \cite{FH, W, Basor, Basor2, BS, Ehr, Deift2, DeiftItsKrasovsky}. Applied to our symbol $f$, the results from, e.g., \cite{Deift2} imply that, for $s\in (0,1)$ fixed, i.e.\ independent of $n$, we have
\begin{multline} \label{Asymptotic_FH}
\ln D_n \left(s,\theta_{0},W \right) = nW_0 + \frac{(\ln s)^2}{2 \pi^{2}}  \ln n +\frac{\ln(2\sin\theta_0)}{2\pi^2} \\
\qquad\qquad +\frac{\ln s}{\pi} \sum_{k=1}^{+\infty}(W_k+W_{-k}) \sin(k\theta_0) 
+ \sum_{k=1}^{+\infty}kW_kW_{-k}\\
+2\ln\left(G\left(1+\frac{\ln s}{2\pi i}\right)G\left(1-\frac{\ln s}{2\pi i}\right)\right) + o(1),
\end{multline}
as $n\to\infty$, where $G$ is Barnes' $G$-function.



If we let $s$ tend to $0$, the jump discontinuities of $f$ turn into endpoints of the support of $f$, and $f$ transforms from a Fisher-Hartwig symbol to an arc-supported symbol on $[-\theta_0,\theta_0]$. Nevertheless, letting $s\to 0$ in \eqref{Asymptotic_FH}, we do not recover the Widom asymptotics \eqref{Asymptotic_one_arc}. This means that a non-trivial critical transition in the asymptotic behavior for $D_n(s,\theta_0,W)$ takes place as $s\to 0$. In this paper, we show that the Widom asymptotics (\ref{Asymptotic_one_arc}) extend to the case where $s\neq 0$ but $s=s(n)\to 0$ sufficiently rapidly as $n\to\infty$. 

\begin{theorem}\label{theorem: extensionWidom}
Let $\theta_0\in (0,\pi)$ and define
\begin{equation}\label{xcintro}
x_{c} = -2\ln \tan \frac{\theta_{0}}{4}.
\end{equation} Let $f$ be of the form (\ref{symbol}) with $W$ analytic in a neighbourhood of the unit circle.
As $n\to\infty$ and simultaneously $s\to 0$ in such a way that $0\leq s\leq e^{-x_cn}$, we have
\begin{equation}\label{extension Widom}
\ln D_n(s,\theta_0,W)=\ln D_n(0,\theta_0,W)+o(1).
\end{equation}
The error term $o(1)$ is uniform for $0\leq s\leq e^{-x_c n}$ and $\epsilon \leq \theta_0 \leq \pi-\epsilon$, $\epsilon>0$, and can be specified as
\begin{equation}\label{error}
o(1)=\bigO(n^{-1/2} e^{x_cn} s).
\end{equation}
In addition, the result extends to the case where
$\theta_0$ approaches $\pi$ at a sufficiently slow rate:  (\ref{extension Widom}) holds for $\epsilon<\theta_0<\pi-\frac{M}{n}$ with $M$ sufficiently large and $0\leq s\leq e^{-x_c n}$, with the error term given by
\begin{equation}\label{error large y}
o(1) = \bigO((\pi-\theta_0)^{1/2}n^{-1/2}e^{nx_c}s).
\end{equation}
\end{theorem}

\begin{figure}[t]
\begin{center}
\includegraphics[width=0.7\textwidth]{asymptotics_1.jpg}
\end{center}
\caption{\label{fig_s_n} As $n\to\infty$, $\ln D_n(s,\theta_0,W)$ follows Widom asymptotics for $s=0$, Fisher-Hartwig asymptotics for $s\in(0,1)$ fixed, and Szeg\H{o} asymptotics for $s=1$. Theorem \ref{theorem: extensionWidom} implies that the Widom asymptotics remain valid as $n\to\infty$ with $s=s(n)$ below the curve $s=e^{-x_cn}$. As $n\to\infty$ with $s=s(n)$ above the curve, a different type of asymptotic behavior is expected.}
\end{figure}

\begin{remark}\label{remark: elliptic}
We believe the bound $s\leq e^{-x_cn}$ is sharp: as $n\to\infty$, $s\to 0$ with $s>e^{-x_cn}$, the asymptotic behavior for $\ln D_n(s,\theta_0,W)$ is expected to be described in terms of elliptic $\theta$-functions. 
For a heuristic discussion, see Section \ref{section: elliptic}.
\end{remark}
\begin{remark}
If $f$ is positive on $\gamma$ and even in $\theta$, the asymptotics for $\ln D_n(0,\theta_0,W)$ in (\ref{extension Widom}) are given by (\ref{Asymptotic_one_arc}). 
The perturbative result (\ref{extension Widom}) is valid for general analytic $W$, even if the positivity and symmetry conditions needed for the Widom asymptotics do not hold. Note that the error term $o(1)=\bigO((\pi-\theta_0)^{1/2}n^{-1/2}e^{nx_c}s)$ in (\ref{extension Widom}) improves as $\theta_0$ approaches $\pi$. This is reasonable since the perturbation of the arc-supported symbol then takes place on a shrinking arc near $-1$. For our proof, it is however crucial that $n(\pi-\theta_0)$ is sufficiently large.
\end{remark}




\subsection*{Application 1: the Circular Unitary Ensemble}
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


\subsection*{Application 2: sine kernel determinants}\label{section: Fredholm}
In the double scaling limit where $n\to\infty$ and $\theta_0$ approaches $\pi$ at rate $\bigO(1/n)$, the Toeplitz determinant $D_n(s,\theta_0,0)$ converges to the Fredholm determinant of the operator $1-(1-s)K_y$, where $K_y$ is the integral operator acting on $(-y,y)$ with kernel $\frac{\sin\pi(x-t)}{\pi(x-t)}$: we have \cite[formulas (236)-(241)]{DIK-hist}
\begin{equation}\label{Toeplitz Fredholm}
\lim_{n\to\infty}D_n(s,\theta_0=\pi (1-\frac{2y}{n}),0)=\det(1-(1-s)K_y),
\end{equation}
where the operator $K_y$ is defined by
\begin{equation}
(K_{y} g)(x)=\int_{-y}^{y}\frac{\sin \pi(x-t)}{\pi(x-t)}g(t)dt.
\end{equation}
Asymptotics for the right hand side of (\ref{Toeplitz Fredholm}) have been studied by Dyson \cite{Dyson}, see also \cite{DIK-hist} for a historical review; the double scaling limit where $y\to\infty$ and simultaneously $s\to 0$ appears to be subtle.
As $y\to\infty$, $s\to 0$ in such a way that $s\leq e^{-2\pi y}$, with
\begin{equation}\label{constant}
c=\frac{1}{12}\ln 2+3\zeta'(-1),
\end{equation} 
we have
\begin{equation}\label{large gap}
\ln \det(1-(1-s)K_y)=-\frac{\pi^{2}y^2}{2}-\frac{1}{4}\ln \pi y+c+o(1).
\end{equation}
Except for $s=0$, (\ref{large gap}) had not been proved rigorously until the recent paper \cite{BDIK}, where double scaling asymptotics were obtained both for $s\leq e^{-2\pi y}$ and for $s> e^{-2\pi y}$. The value of the constant (\ref{constant}) was also proved in \cite{BDIK}.


As a consequence of our Theorem \ref{theorem: extensionWidom}, we re-derive (\ref{large gap}) and (\ref{constant}).
Indeed,
by (\ref{Asymptotic_one_arc}), (\ref{extension Widom}), and (\ref{error large y}), we have 
\begin{equation}\label{large y}
\ln D_n(s,\pi(1-\frac{2y}{n}),0)=n^2\ln\cos\frac{\pi y}{n}-\frac{1}{4}\ln n-\frac{1}{4}\ln\sin\frac{\pi y}{n}+c+\bigO(\frac{y^{1/2}}{n}e^{nx_{c}}s)+ \bigO(y^{-1}),
\end{equation}
with the error term uniform for $n,y$ large, $y^{1/2}/n$ small, and 
\begin{equation}\label{condition sy}s\leq e^{-x_cn}=e^{2n\ln\tan\frac{\theta_0}{4}}=e^{2n\ln\tan\left(\frac{\pi}{4}-\frac{\pi y}{2n}\right)}.\end{equation}
The right hand side of (\ref{condition sy}) can be written as $e^{-2\pi y}\left(1+\bigO(y^2 n^{-1})\right)$ for $n,y$ large and $y^{2}/n$ small. \\
Now, let us choose an arbitrary small function $\epsilon (y) > 0$ and assume $s \leq (1-\epsilon(y))e^{-2\pi y}$. Then for $n$ sufficiently large, i.e.\ for $n>>y^2/\epsilon(y)$, (\ref{condition sy}) holds, and letting $n\to\infty$ in (\ref{large y}), we obtain  
\begin{equation}
\lim_{n\to\infty}\ln D_n(s,\pi(1-\frac{2y}{n}),0)=-\frac{\pi^{2}y^2}{2}-\frac{1}{4}\ln \pi y+c+\bigO(y^{-1}),
\end{equation}
for large $y$.
We thus re-derive (\ref{large gap}) in the double scaling limit where $y\to\infty, s\to 0$ in such a way that $s\leq (1-\epsilon(y))e^{-2\pi y}$, and we confirm the value of the constant (\ref{constant}), using different methods than in \cite{BDIK}.

In \cite{BDIK}, the double scaling asymptotics $y\to\infty, s\to 0$ such that $s\geq e^{-2\pi y}$ have also been considered, and asymptotics for $\det(1-(1-s)K_y)$ in terms of elliptic $\theta$-functions were obtained. This is consistent with Remark \ref{remark: elliptic} and the discussion in Section \ref{section: elliptic}.



\subsection*{Outline}
In Section \ref{section: diff id}, we will derive identities which express $\frac{d}{ds}\ln D_n(s,\theta_0,W)$ in terms of orthogonal polynomials on the unit circle.
In Section \ref{section: eq}, we will study an equilibrium problem which is crucial to obtain asymptotics for the orthogonal polynomials. In Section \ref{section: RH}, we will obtain asymptotics for the orthogonal polynomials as the degree tends to infinity, via the Riemann-Hilbert (RH) method. An important novel feature in the RH analysis is the construction of a {\em modified Bessel parametrix} compared to Bessel parametrices that appeared in the literature before. This modification is needed because $s\neq 0$. The asymptotics for the orthogonal polynomials will lead us towards large $n$ asymptotics for $\frac{d}{ds}\ln D_n(s,\theta_0,W)$. Integrating the differential identity will complete the proof of Theorem \ref{theorem: extensionWidom} 
in Section \ref{section: int} for $\theta_{0}$ fixed. In addition, we explain how the proof can be extended to the case where $\theta_{0} \to \pi$ at a sufficiently slow rate.
