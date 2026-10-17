---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-002-application-2-sine-kernel-determinants
section_title: "Application 2: sine kernel determinants"
section_number: null
pages: 5-6
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.988
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
\label{section: Fredholm}
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
