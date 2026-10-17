---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-007-441-bessel-model-rh-problem
section_title: "Bessel model RH problem"
section_number: 4.4.1
pages: 18-18
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 1.0
---
We will construct $P$ in terms of a model RH problem for which the solution is constructed using Bessel functions.
Consider the following model RH problem:


\subsubsection{RH problem for $\Psi$}

\begin{itemize}
\item[(a)] $\Psi : \mathbb{C} \setminus \Sigma_{\Psi} \to \mathbb{C}^{2\times 2}$ is analytic, where $\Sigma_{\Psi} = \mathbb{R}^{-} \cup \{ xe^{\pm\frac{2\pi }{3}i} : x \in \mathbb{R}^{+} \}$, with the orientation from $\infty$ towards $0$ for the three half-lines.
\item[(b)] $\Psi$ satisfies the jump conditions
\begin{equation*}
\begin{array}{l l}
\Psi_{+}(\zeta) = \Psi_{-}(\zeta) \begin{pmatrix}
0 & 1 \\ -1 & 0
\end{pmatrix}, & \zeta \in \mathbb{R}^{-}, \\

\Psi_{+}(\zeta) = \Psi_{-}(\zeta) \begin{pmatrix}
1 & 0 \\ 1 & 1
\end{pmatrix}, & \zeta \in \{ xe^{\frac{2\pi }{3}i} : x \in \mathbb{R}^{+} \}, \\

\Psi_{+}(\zeta) = \Psi_{-}(\zeta) \begin{pmatrix}
1 & 0 \\ 1 & 1
\end{pmatrix}, & \zeta \in \{ xe^{-\frac{2\pi}{3}i} : x \in \mathbb{R}^{+} \}. \\
\end{array}
\end{equation*}
\item[(c)] $\Psi(\zeta) = \left( 2\pi \zeta^{\frac{1}{2}} \right)^{-\frac{\sigma_{3}}{2}} \frac{1}{\sqrt{2}} \begin{pmatrix}1&i\\i&1\end{pmatrix}\left(
I+\bigO (\zeta^{-\frac{1}{2}})\right) e^{2\zeta^{\frac{1}{2}}\sigma_{3}}$, \quad as $\zeta \to \infty$, $\zeta \notin \Sigma_{\Psi}$.
\item[(d)] As $\zeta$ tend to 0, the behaviour of $\Psi(\zeta)$ is
\begin{equation}\label{Psi local}
\Psi(\zeta) = \bigO (\ln |\zeta| ).
\end{equation}
\end{itemize}
This model RH problem is well-known and it can be solved explicitly using Bessel functions, see e.g.\ \cite{Kuijlaars2, Krasovsky}. The unique solution to this RH problem is given by 
\begin{equation}\label{Psi explicit}
\Psi(\zeta)=\begin{cases}
\begin{pmatrix}
I_{0}(2\zeta^{\frac{1}{2}}) & \frac{i}{\pi} K_{0}(2\zeta^{\frac{1}{2}}) \\
2\pi i \zeta^{\frac{1}{2}} I_{0}^{\prime}(2\zeta^{\frac{1}{2}}) & -2\zeta^{\frac{1}{2}} K_{0}^{\prime}(2\zeta^{\frac{1}{2}})
\end{pmatrix}, & |\arg \zeta | < \frac{2\pi}{3}, \\

\begin{pmatrix}
\frac{1}{2} H_{0}^{(1)}(2(-\zeta)^{\frac{1}{2}}) & \frac{1}{2} H_{0}^{(2)}(2(-\zeta)^{\frac{1}{2}}) \\
\pi \zeta^{\frac{1}{2}} \left( H_{0}^{(1)} \right)^{\prime} (2(-\zeta)^{\frac{1}{2}}) & \pi \zeta^{\frac{1}{2}} \left( H_{0}^{(2)} \right)^{\prime} (2(-\zeta)^{\frac{1}{2}})
\end{pmatrix}, & \frac{2\pi}{3} < \arg \zeta < \pi, \\

\begin{pmatrix}
\frac{1}{2} H_{0}^{(2)}(2(-\zeta)^{\frac{1}{2}}) & -\frac{1}{2} H_{0}^{(1)}(2(-\zeta)^{\frac{1}{2}}) \\
-\pi \zeta^{\frac{1}{2}} \left( H_{0}^{(2)} \right)^{\prime} (2(-\zeta)^{\frac{1}{2}}) & \pi \zeta^{\frac{1}{2}} \left( H_{0}^{(1)} \right)^{\prime} (2(-\zeta)^{\frac{1}{2}})
\end{pmatrix}, & -\pi < \arg \zeta < -\frac{2\pi}{3},
\end{cases}
\end{equation}
where $H_0^{(1)}$ and $H_0^{(2)}$ are the Hankel functions of the first and second kind, and $I_0$ and $K_0$ are the modified Bessel functions of the first and second kind.
