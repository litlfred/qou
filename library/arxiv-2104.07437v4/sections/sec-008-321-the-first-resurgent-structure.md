---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-008-321-the-first-resurgent-structure
section_title: "The first resurgent structure"
section_number: 3.2.1
pages: 16-20
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.994
---
By using the free energies \eqref{eq:CF0-F0}--\eqref{eq:CF2-F0} we can construct the first asymptotic series for $N=1$ by

\eqref{phiN}
\begin{equation}
  \Phi_{0;1}(g_s) = \re^{\CV_{\IF_0}/g_s}\varphi_{0;1}(g_s),
\end{equation}
where
\begin{equation}
  \CV_{\IF_0} = \frac{2C}{\pi^2},
\end{equation}
and
\begin{equation}
  \varphi_{0;1}(g_s) =
  1+\frac{\pi^2}{24}g_s + \frac{73\pi^4}{1152}g_s^2 +\frac{13541 \pi ^6
   g_s^3}{414720}+\frac{855509 \pi ^8 g_s^4}{39813120}+\frac{150067879 \pi ^{10}
   g_s^5}{6688604160} +\ldots.
\end{equation}
Since we are only concerned with $N=1$, we will suppress the subscript
${}_{;1}$ in the remainder of the section.

\begin{figure}
  \centering
  \includegraphics[height=6cm]{singularities_Z1F0}
  \caption{The singularities in the Borel plane for the series
    $\varphi_{0}(g_s)$, $\varphi_{1}(g_s)$. 
    
   
   }
  \label{fg:sings-Z1F0}
\end{figure}

The series $\Phi_{0}(g_s)$ has a very rich resurgent structure.  The
Borel transform $\wh{\Phi}_{0}(\zeta)$ has two infinite towers of
singularities located at
\begin{align}
  &\ri n ,\quad n \in\IZ_{\neq 0},\\
  &\zeta_0 + \ri n', \quad n'\in \IZ,
\end{align}
with $\zeta_0 = 2\CV_{\IF_0}$, which is illustrated in the left panel
of Fig.~\ref{fg:sings-Z1F0}.  The first tower of singularities along
the imaginary axis corresponds to the following asymptotic series in
the same family
\begin{equation}
  \Phi_{0,n}(g_s) = \Phi_{0}(g_s)\re^{-n\frac{\ri}{g_s}},\quad n\in
  \IZ.
  \label{eq:Phi0n-F0}
\end{equation}
The second tower of singularities indicates the existence of a new
family of asymptotic series.  Since the singularity $\zeta_0$ on the
positive real axis is the nearest singularity, it controls the large
order behavior of the coefficients $a_n$ of $\varphi_{0}(g_s)$ by
\begin{align}
  a_n \sim
  &\frac{\ms{S}_{01,0}}{2\pi\ri}
    \sum_{k=0}^\infty b_k\zeta_0^{k-n}\Gamma(n-k)
    \nn =
  &\frac{\ms{S}_{01,0}}{2\pi\ri} \zeta_{0}^{-n}\Gamma(n)
    \left(b_{0} + \frac{b_{1}\zeta_{0}}{n-1}
    + \frac{b_{2}\zeta_0^2}{(n-1)(n-2)}+\ldots\right),
    \label{eq:an-asym}
\end{align}
where $b_k$ are the coefficients of the series that resurges at
$\zeta_0$, and $\ms{S}_{01,0}$ is the Stokes constant.  By
systematically extracting the coefficients $b_k$, we find that the
second family of series is given by

\begin{equation}
  \Phi_{1,n}(g_s) = \Phi_{1}(g_s)\re^{-n\frac{\ri}{g_s}},\quad n\in\IZ,
  \label{eq:Phi1n-F0}
\end{equation}

with

\begin{equation}
  \Phi_{1}(g_s) = \ri \Phi_{0}(-g_s).\label{eq:Phi1F0}
\end{equation}
Along the way, we also find the value of the first Stokes constant
\begin{equation}
  \ms{S}_{01,0} = 4.  \label{eq:S0-F0}
\end{equation}


Next we study the resurgent structure of the new series $\Phi_1(g_s)$.
Since it is related to $\Phi_0(g_s)$ by (\ref{eq:Phi1F0}), its Borel singularities are
mirror reflection of those of $\Phi_0(g_s)$ with respect to the
imaginary axis, as illustrated in the right panel of
Fig.~\ref{fg:sings-Z1F0}.  They are located at
\begin{align}
  &\ri n ,\quad n \in\IZ_{\neq 0},\\
  &\zeta_1 + \ri n', \quad n'\in \IZ,
\end{align}
with $\zeta_1 = -4C/\pi^2$, associated with $\Phi_{1,n}(g_s)$ and
$\Phi_{0,n'}(g_s)$ respectively.
In addition, using the same large order analysis we find that the Stokes
constant at the singularity $\zeta_1$ on the negative real axis is

\begin{equation}
  \ms{S}_{10,0} = -4. \label{eq:S1-F0}
\end{equation}

Therefore we conclude that $\{\Phi_{0,n}(g_s),\Phi_{1,n}(g_s)\}$ form
a minimal resurgent structure. We denote by $\Phi(g_s)$ the
2-vector of asymptotic series
\begin{equation}
  \Phi(g_s) =
  \begin{pmatrix}
    \Phi_{0}(g_s) \\ \Phi_{1}(g_s)
  \end{pmatrix}.
\end{equation}

As shown in Fig.~\ref{fg:rays-Z1F0}, the Stokes rays passing through the Borel singularities of both series arrange into a peacock
pattern, very similar to the one found for the asymptotic series of the figure
eight knot in \cite{ggm1,ggm2}. The Stokes rays divide the
complex plane into infinitely many sectors, and only inside a sector can
the Borel resummation of $\Phi(g_s)$ be defined. We denote by
$s_R(\Phi)(g_s)$ the Borel resummation along a ray in the sector $R$
of the asymptotic series.  As in \cite{ggm1,ggm2} we denote the four
sectors bordering the real axis by $I,II,III,IV$ in the anti-clockwise
order.


\begin{figure}
  \centering
  \includegraphics[height=7cm]{rays_Z1F0}
  \caption{Stokes rays and sectors in the $g_s$-plane for
    $\Phi(g_s)$.}
  \label{fg:rays-Z1F0}
\end{figure}

Following the structure of Borel singularities, we can collect all the
Stokes constants into the matrix
\begin{equation}
  \ms{S}(q) = (\ms{S}_{\sigma\sigma'}(q))_{\sigma,\sigma'=0,1}.
\end{equation}
In this section we will 











scale powers of $q$ by $1/2$ in the generating series of Stokes
constants for the reason that will become clear in the next
subsection, in other words
\begin{equation}
  \ms{S}_{\sigma,\sigma'}(q) = \sum_{n\in\IZ} \ms{S}_{\sigma\sigma',n}q^{n/2}.
\end{equation}
We also decompose the matrix $\ms{S}(q)$ as
\begin{equation}
  \ms{S}(q) = \ms{S}^{(0)}+\ms{S}^+(q) + \ms{S}^-(q),
\end{equation}

where $\ms{S}^{(0)}$ is an off-diagonal constant matrix containing
Stokes constants on the real axis, the entries of $\ms{S}^+(q)$
are $q$-series encoding Stokes constants in the upper half plane,
while the entries of $\ms{S}^-(q)$ are $q^{-1}$-series encoding
Stokes constants in the lower half plane.

The constant matrix $\ms{S}^{(0)}$ has only two non-vanishing off-diagonal
entries

\begin{equation}
  \ms{S}^{(0)} =
  \begin{pmatrix}
    0 & \ms{S}_{01,0}\\
    \ms{S}_{10,0} & 0
  \end{pmatrix},
\end{equation}

and they were already obtained in \eqref{eq:S0-F0}, \eqref{eq:S1-F0}.
One finds that the matrix $\ms{S}^{(0)}$ is skew-symmetric.  To
compute the Stokes matrices $\ms{S}^+(q)$ and $\ms{S}^-(q)$ it is
beneficial to use the TS/ST correspondence as well as more advanced
machinery of radial asymptotic analysis, which we will explain in
detail in the following two subsections. We quote the results here for
completeness. The Stokes automorphism $\mf{S}_{I\mapsto II}(q)$ from
sector $I$ to $II$ is defined by

\begin{equation}
  s_{II}(\Phi)(g_s) = \mf{S}_{I\mapsto II}(q) s_{I}(\Phi)(g_s),
  \label{eq:Sauto12}
\end{equation}
and its explicit expression is 

\begin{equation}
  \mf{S}_{I\mapsto II}(q) = \frac{1}{2}
  \begin{pmatrix}
    2g(q)G(q) & G'(q)g(q) - g'(q)G(q)\\
    G(q)g'(q) - g(q)G'(q) & 2g'(q)G'(q), 
  \end{pmatrix},
  \label{eq:Sp-F0}
\end{equation}

where the $q$-series $g(q),G(q),g'(q),G'(q)$ are defined in
\eqref{eq:gG}, \eqref{eq:gprime}, \eqref{eq:Gprime}.  We note that
$\mf{S}_{I\mapsto II}(q)$ is also skew-symmetric. The Stokes constants in the upper half plane
can be read off from $\mf{S}_{I\mapsto II}(q)$. In particular,

\begin{subequations}
  \begin{align}
    \ms{S}^+_{00}(q) =
    &\mf{S}_{I\mapsto II}(q)_{1,1}-1\nn =
    &6q^{1/2}+3q+6q^{3/2}+17q^2-26 q^{5/2} + 52 q^3+\ldots,\\
    \ms{S}^+_{01}(q) =
    &\mf{S}_{I\mapsto II}(q)_{1,2}/\mf{S}_{I\mapsto II}(q)_{1,1}\nn =
    &-8q^{1/2}+36q-192q^{3/2}+1048q^2-5752 q^{5/2} + 31656 q^3+\ldots,\\
    \ms{S}^+_{10}(q) =
    &\mf{S}_{I\mapsto II}(q)_{2,1}/\mf{S}_{I\mapsto II}(q)_{1,1}\nn =
    &8q^{1/2}-36q+192q^{3/2}-1048q^2+5752 q^{5/2} - 31656 q^3+\ldots,\\
    \ms{S}^+_{11}(q) =
    &\mf{S}_{I\mapsto II}(q)_{2,2} -
      \mf{S}_{I\mapsto II}(q)_{1,2}
      \mf{S}_{I\mapsto  II}(q)_{1,1}\mf{S}_{I\mapsto II}(q)_{2,1}-1\nn =
    &-6q^{1/2}+33q+582q^{3/2}+1420q^2+2528 q^{5/2} + 7383 q^3+\ldots.
  \end{align}
\end{subequations}
Note that the definition of the Stokes automorphism \eqref{eq:Sauto12}, 
together with the difference between neighboring series in the same
family \eqref{eq:Phi0n-F0}, \eqref{eq:Phi1n-F0} implies that $q$ is identified naturally with 

\begin{equation}
  q = \re^{-\frac{2\ri}{g_s}}.
  \label{eq:q-gs}
\end{equation}

\begin{figure}
  \centering
  \includegraphics[height=6.3cm]{singularities_Stokes_Z1F0}
  \caption{Stokes constants for the minimal resurgent structure $\{\Phi_{0,n}(g_s),\Phi_{1,n}(g_s)\}$
    of local $\IF_0$.}
  \label{fg:Stokes_Z1F0}
\end{figure}

To compute the Stokes constants in the lower half plane, we notice
that
\begin{equation}
  \Phi(g_s)^* =
  \begin{pmatrix}
    1 & 0 \\ 0 & -1
  \end{pmatrix}
  \Phi(g_s^*),\quad q(g_s)^* = q(g_s^*)^{-1}.
\end{equation}
Therefore by complex conjugating both sides of \eqref{eq:Sauto12} we
find
\begin{equation}
  s_{IV}(\Phi)(g_s) = \mf{S}_{III\mapsto IV}(q) s_{III}(\Phi)(g_s),
  \label{eq:Sauto23}
\end{equation}
with
\begin{equation}
  \mf{S}_{III\mapsto IV}(q) =
  \begin{pmatrix}
    1 & 0 \\ 0 & -1
  \end{pmatrix}\mf{S}_{I\mapsto II}(q^{-1})^{-1}
  \begin{pmatrix}
    1 & 0 \\ 0 & -1
  \end{pmatrix}.
\end{equation}
The Stokes constants in the lower half plane can also be read off and
we find
\begin{subequations}
  \begin{align}
    \ms{S}^{-}_{00}(q) =
    &-6q^{-1/2}+33q^{-1}+582q^{-3/2}+1420q^{-2}+\ldots,\\
    \ms{S}^{-}_{01}(q) =
    &-8q^{-1/2}+36q^{-1}-192q^{-3/2}+1048q^{-2}+\ldots,\\
    \ms{S}^{-}_{10}(q) =
    &8q^{-1/2}-36q^{-1}+192q^{-3/2}-1048q^{-2}+\ldots,\\
    \ms{S}^{-}_{11}(q) =
    &6q^{-1/2}+3q^{-1}+6q^{-3/2}+17q^{-2}+\ldots.
  \end{align}
\end{subequations}
We illustrate the Stokes constants in Fig.~\ref{fg:Stokes_Z1F0}.
