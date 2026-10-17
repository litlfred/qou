---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.9
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
