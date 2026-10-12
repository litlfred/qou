---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-006-441-bessel-model-rh-problem
section_title: "Bessel model RH problem"
section_number: 4.4.1
pages: 18-20
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.906
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




\subsubsection{Modification of the model RH problem}

We will use a conformal map which maps the curves $\gamma_-, \gamma, \gamma_+$ in the vicinity of $z_0$ to (part of) the jump contour for $\Psi$. This is similar to the construction in \cite{Krasovsky}, which corresponds to the case $s=0$. If $s=0$, $P$ has no jump on $\gamma_c$ (see Figure \ref{figure: contour P}), and the model RH problem fits perfectly to construct the local parametrix $P$. In our situation however, $P$ does have a jump on $\gamma_c$, and for this reason we need to modify the model RH problem. A different but similar construction was done in \cite{BDIK}.






Define $\widehat{\Psi}$ by
\begin{equation}\label{def hatPsi}
\widehat{\Psi}(\zeta) = \left( I + A(\zeta) \right) \Psi(\zeta), 
\end{equation}
where $A$ is given by 
\begin{equation}\label{def A}
A(\zeta) = e^{-nx} F(\zeta) \begin{pmatrix}
0 & - \frac{1}{2\pi i} \ln(-\zeta) \\ 0 & 0 \\
\end{pmatrix} F^{-1}(z),
\end{equation}
with $F$ defined by
\begin{equation}\label{F}
F(\zeta) = \left\{ \begin{array}{l l}
\Psi(\zeta) \begin{pmatrix}
1 & -\frac{1}{2\pi i} \ln \zeta \\
0 & 1
\end{pmatrix} & | \arg \zeta | < \frac{2\pi}{3}, \\

\Psi(\zeta) \begin{pmatrix}
1 & 0 \\
1 & 1
\end{pmatrix} \begin{pmatrix}
1 & -\frac{1}{2\pi i} \ln \zeta \\
0 & 1
\end{pmatrix} & \frac{2\pi}{3} < \arg \zeta < \pi, \\

\Psi(z) \begin{pmatrix}
1 & 0 \\
-1 & 1
\end{pmatrix} \begin{pmatrix}
1 & -\frac{1}{2\pi i} \ln \zeta \\
0 & 1
\end{pmatrix} & -\pi < \arg \zeta < -\frac{2\pi}{3}, \\

\end{array} \right. 
\end{equation}
where in both \eqref{def A} and \eqref{F} $\ln$ has its branch cut on $\mathbb{R}^{-}$ with imaginary part between $-\pi$ and $\pi$. It is easy to check that $F$ is an entire function.
$\widehat{\Psi}$ is analytic in  $\mathbb{C} \setminus \Sigma_{\widehat{\Psi}}$, with $\Sigma_{\widehat{\Psi}}$ as shown in Figure \ref{figPsiHat}. On $\Sigma_{\widehat{\Psi}}$, it has the jump relations
\begin{equation}\label{jumps hatPsi}
\begin{array}{l l}
\widehat{\Psi}_{+}(\zeta) = \widehat{\Psi}_{-}(\zeta) \begin{pmatrix}
0 & 1 \\ -1 & 0
\end{pmatrix}, & \mbox{ on } \mathbb{R}^{-}, \\

\widehat{\Psi}_{+}(\zeta) = \widehat{\Psi}_{-}(\zeta) \begin{pmatrix}
1 & e^{-nx} \\ 0 & 1
\end{pmatrix}, & \mbox{ on } \mathbb{R}^{+}, \\

\widehat{\Psi}_{+}(\zeta) = \widehat{\Psi}_{-}(\zeta) \begin{pmatrix}
 1 & 0  \\ 1 & 1
\end{pmatrix}, & \mbox{ on } \left\{ xe^{\frac{2\pi}{3}i} : x \in \mathbb{R}^{+} \right\}, \\

\widehat{\Psi}_{+}(\zeta) = \widehat{\Psi}_{-}(\zeta) \begin{pmatrix}
 1 & 0 \\ 1 & 1
\end{pmatrix}, & \mbox{ on } \left\{ xe^{-\frac{2\pi}{3}i} : x \in \mathbb{R}^{+} \right\}.
\end{array}
\end{equation}









\begin{figure}[t]
    \begin{center}
    \setlength{\unitlength}{1truemm}
    \begin{picture}(100,55)(-5,10)
        \put(50,40){\line(1,0){30}}
        \put(50,40){\line(-1,0){30}}
        \put(50,39.8){\thicklines\circle*{1.2}}
        \put(50,40){\line(-0.5,0.866){18}}
        \put(50,40){\line(-0.5,-0.866){18}}
        \qbezier(53,40)(52,43)(48.5,42.598)
        \put(53,43){$\frac{2\pi}{3}$}
        \put(50.3,36.8){$0$}
        \put(65,39.9){\thicklines\vector(1,0){.0001}}
        \put(35,39.9){\thicklines\vector(1,0){.0001}}
        \put(41,55.588){\thicklines\vector(0.5,-0.866){.0001}}
        \put(41,24.412){\thicklines\vector(0.5,0.866){.0001}}
        \put(60,60){$\Sigma_{\widehat{\Psi}}$}
    \end{picture}
    \caption{The jump contour for $\widehat{\Psi}$.}
    \label{figPsiHat}
\end{center}
\end{figure}
