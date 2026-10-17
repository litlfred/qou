---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-006-43-global-parametrix
section_title: "Global parametrix"
section_number: 4.3
pages: 16-18
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.933
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
Ignoring the exponentially small jumps for $S$ and small neighborhoods of $z_0, \overline{z_0}$, $-1$, we are led to the following RH problem:

\subsubsection{RH problem for $P^{(\infty)}$}
\begin{itemize}
\item[(a)] $P^{(\infty)} : \mathbb{C}\setminus \gamma \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] $P^{(\infty)}$ has the jump
\begin{equation}\label{jump Pinfty}
P^{(\infty)}_+(z)=P^{(\infty)}_-(z)\begin{pmatrix} 0&e^{W(z)}\\-e^{-W(z)}&0
\end{pmatrix},\qquad z\in\gamma\setminus\{z_{0},\overline{z_{0}}\}.
\end{equation}
\item[(c)] $P^{(\infty)}(z) = I + \bigO(z^{-1})$ as $z \to \infty$.
\item[(d)] As $z\to z_0$ or $z\to \overline{z_0}$, we have
\begin{equation}
P^{(\infty)}(z)=\bigO(|z-z_0|^{-1/4}),\qquad P^{(\infty)}(z)=\bigO(|z-\overline{z_0}|^{-1/4}).
\end{equation}
\end{itemize}

The solution of this RHP is explicitly given by
\begin{equation}
P^{(\infty)}(z)= e^{h_\infty\sigma_3}\begin{pmatrix}
\frac{1}{2} \left( \beta(z) + \beta^{-1}(z) \right) & -\frac{1}{2i} \left( \beta(z) - \beta^{-1}(z) \right) \\
\frac{1}{2i} \left( \beta(z) - \beta^{-1}(z) \right) & \frac{1}{2} \left( \beta(z) + \beta^{-1}(z) \right)
\end{pmatrix}e^{-h(z)\sigma_3} ,
\end{equation}
where $\beta(z) = \left(\frac{z-\overline{z_{0}}}{z-z_{0}}\right)^{1/4}$ is analytic in $\mathbb{C}\setminus \gamma$ and $\beta(z) \to 1$ as $z\to\infty$, 
where $h_\infty=\lim_{z\to\infty}h(z)$, and
\begin{equation}\label{h}
h(z)=\frac{\left((z-z_0)(z-\overline{z_0})\right)^{1/2}}{2\pi i}\int_{\gamma}\frac{W(\xi)}{\left((\xi-z_0)(\xi-\overline{z_0})\right)_+^{1/2}}\frac{1}{\xi-z}d\xi,
\end{equation}
with $\left((z-z_0)(z-\overline{z_0})\right)^{1/2}$ analytic off $\gamma$. Note that $h$ is analytic in $\mathbb C\setminus \gamma$, bounded near $z_0$, $\overline{z_0}$, and $\infty$, and that it satisfies the jump relation 
\[h_+(z)+h_-(z)=W(z),\qquad z\in\gamma\setminus \{z_{0},\overline{z_{0}}\}.\] Using these properties, it is straightforward to verify that $P^{(\infty)}$ solves the above RH problem.



\subsection{Local parametrix near $z_{0}$}\label{section: Bessel}
We want to construct a function $P$ defined in $D(z_0,r)$ satisfying the following RH conditions.

\subsubsection{RH problem for $P$}








\begin{figure}[t]
    \begin{center}
    \setlength{\unitlength}{1truemm}
    \begin{picture}(100,55)(-5,10)
        \cCircle(50,40){25}[f]
        \qbezier(50,40)(40,46)(27,50)
        \qbezier(50,40)(60,30)(62,18)
        \qbezier(50,40)(60,35)(70,24.8)
        \qbezier(50,40)(62,39)(74.7,35)
        
        \put(40,45.2){\thicklines\vector(-2,1){.0001}}
        \put(58.2,29){\thicklines\vector(-1,2){.0001}}
        \put(62,32.2){\thicklines\vector(-1,1){.0001}}
        \put(62.5,38.35){\thicklines\vector(-3,1){.0001}}
        
        \put(40,46){$\gamma^{c}$}
        \put(54,27){$\gamma_{+}$}
        \put(59.8,29.2){$\gamma$}
        \put(62.5,39){$\gamma_{-}$}
        
        \put(50,40){\thicklines\circle*{1.2}}
        \put(50,42){$z_{0}$}
        \put(44,67){$\partial D(z_{0},r)$}
    \end{picture}
    \caption{The jump contour for $P$.}
    \label{figure: contour P}
\end{center}
\end{figure}

\begin{itemize}
\item[(a)] $P : D(z_{0},r) \setminus (S_{1} \cup \gamma_{+} \cup \gamma_{-}) \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] For $z$ on the contour shown in Figure \ref{figure: contour P}, $P$ satisfies the jump conditions
\begin{equation}\label{jumps P}
\begin{array}{l l}
P_{+}(z) = P_{-}(z) \begin{pmatrix}
0 & e^{W(z)} \\ -e^{-W(z)} & 0
\end{pmatrix}, & \mbox{ on } \gamma\setminus \{z_{0},\overline{z_{0}}\}, \\

P_{+}(z) = P_{-}(z) \begin{pmatrix}
 1 & e^{n(\phi(z)-x)}e^{W(z)} \\
 0 & 1
\end{pmatrix}, & \mbox{ on } \gamma^{c}, \\

P_{+}(z) = P_{-}(z) \begin{pmatrix}
 1 & 0  \\ e^{-n\phi(z)}e^{-W(z)} & 1
\end{pmatrix}, & \mbox{ on } \gamma_{-} \cup \gamma_{+}. \\
\end{array}
\end{equation}
\item[(c)] For $z \in \partial D (z_{0},r)$, we have
\begin{equation}\label{matching P z0} P(z) = \left(I + \bigO(n^{-1})\right) P^{(\infty)}(z),\qquad \mbox{ as $n \to \infty$.}
\end{equation}
\item[(d)] As $z$ tend to $z_{0}$, the behaviour of $P$ is
\begin{equation}\label{P local}
\begin{array}{l l}
P(z) = \bigO(\ln|z-z_0|).
\end{array}
\end{equation}
\end{itemize}
