---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-014-332-the-second-resurgent-structure
section_title: "The second resurgent structure"
section_number: 3.3.2
pages: 30-34
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.995
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
We can use the conifold free energies

to construct the formal power
series $\Phi_{0;2}(g_s)$ at $N=2$. Instead we will consider the
following normalised series\footnote{The fact that the normalised
  series has no exponential factor indicates that the leading
  contribution to $\Phi_{0;2}(g_s)\sim Z_2(\hbar)$ is indeed
  $\exp(2\CV_{\IP^2}/g_s)$ as predicted by \eqref{vc-cy}.}
  
\begin{equation}
\ba
  \Phi'_{0;2}(g_s) &= 1 +
  \frac{8\pi^2g_s}{9\sqrt{3}}\frac{\Phi_{0;2}(g_s)}{\Phi_{0;1}(g_s)^2}= \sum_{n \ge 0} a_n g_s^n\\
  &
  =1+ \frac{8\pi^2g_s}{9 \sqrt{3}}
  +\frac{16\pi^4g_s^2}{81} + \frac{64\pi^6g_s^3}{729 \sqrt{3}}
  -\frac{64\pi^8g_s^4}{19683} + \ldots
  
  \label{eq:NPhi2}
  \ea
\end{equation}
Up to normalisation, this is the power series associated to the
normalised second trace
\begin{equation}
  \tr'\rho_{\IP^2}^2 :=
  \frac{\tr\rho_{\IP^2}^2}{(\tr\rho_{\IP^2})^2}
  = 1-\frac{2Z_2(\hbar)}{Z_1(\hbar)^2}.
\end{equation}

As we will see, the advantage of working with this series is that its
resurgent structure is simpler.  In the remainder of this section and
the following sections we will drop the prime and always refer to the
normalised series \eqref{eq:NPhi2} when we use the symbol
$\Phi_{0;2}(g_s)$. We will refer to $\mathfrak{B}_{ \Phi_{0;2}}$ as the second resurgent structure of local 
$\IP^2$. 

\begin{figure}
  \centering
  \includegraphics[height=6cm]{singularities_Z2P2}
  \caption{The singularities in the Borel plane for the series
    $\varphi_{0;2}(g_s)$
    
    }
  \label{fg:sings-Z2P2}
\end{figure}

The resurgent structure associated to $\Phi_{0;2}(g_s)$ is quite
interesting.  The Borel transform $\wh{\Phi}_{0;2}(\zeta)$ has one
family of infinitely many singularities in the first and the fourth
quadrants as illustrated in Fig.~\ref{fg:sings-Z2P2}, and they are
located at
\begin{equation}
  3\CV_{\IP^2}+\ri n,\quad n\in\frac{1}{2}+\IZ.
\end{equation}
This indicates that there exists a
second family of asymptotic series, which we denote by
\begin{equation}
\label{phi12P2}
  \Phi_{1,n;2}(g_s) = \Phi_{1;2}(g_s)\re^{-n\frac{\ri}{g_s}},\quad
  n\in \frac{1}{2}+\IZ.
\end{equation}
Note that here we have generalized the convention \eqref{full-bts} in
Section~\ref{sc:S-topo} in order to emphasize the reflection symmetry of
the singularities in the Borel plane. In (\ref{phi12P2}), 

\begin{equation}
  \Phi_{1;2}(g_s) =

  \re^{-\frac{3\CV_{\IP^2}}{g_s}}
  \varphi_{1;2}(g_s),
\end{equation}
and we assume $ \varphi_{1;2}(g_s)$ has the general form
\begin{equation}
  \varphi_{1;2}(g_s) = (-g_s)^{-\nu}\sum_{n=0}^\infty a_{n,1} g_s^n.
\end{equation}
To uncover the nature of the series $\varphi_{1;2}(g_s)$, we focus on
the two nearest singularities
\begin{equation}
  \zeta_1:=3\CV_{\IP^2}+\frac{\ri}{2},\quad
  \zeta_1^* = 3\CV_{\IP^2}-\frac{\ri}{2},
\end{equation}
which are conjugate to each other. It follows from standard resurgent analysis that 
the perturbative series $\varphi_{1;2}(g_s)$ at these two
singular points control the large order behavior of the coefficients
$a_n$ of the series $\Phi_{0,2}(g_s)$, albeit in a more complicated
form





\begin{equation}
  a_n \sim \frac{\ms{S}_{01,0;2}}{\pi}
  \sum_{k=0}^\infty
  |\zeta_1|^{k-n-\nu}\Gamma(n+\nu-k)|a_{k,1}|\sin(\theta_k -
  (n+\nu-k)\theta). 
  \label{eq:an-asymp2}
\end{equation}
Here,

\begin{equation}
  \theta = \arg \zeta_1, \quad \theta_k = \arg a_{k,1}.
\end{equation}
Therefore, it should be possible to extract the coefficients $a_{k,1}$ from the large order behavior 
of the series $a_n$. Since the asymptotics is oscillatory, one can not apply the standard Richardson transform 
which is often used in resurgent analysis. It turns out that, for this type of oscillatory behavior, there is a numerical 
algorithm due to Hunter and Guerrieri \cite{HunterGuerrieri1980} which makes it possible to extract the coefficients $a_{k,1}$ 
(see Appendix \ref{sc:hunter} for an explanation of this algorithm). By using this algorithm, we find
\begin{equation}
  \ms{S}_{01,0;2}\varphi_{1;2}(g_s) =
  -2^{1/2}3^{9/4} \pi^{-1/2} g_s^{-1/2}\exp
  \left(\frac{\pi^2g_s}{2\sqrt{3}}-\frac{4\pi^6g_s^3}{405\sqrt{3}}+\ldots\right),
\end{equation}
which turns out to be proportional to $\Phi_{0;1}(g_s)^{-3}$.  We
choose the normalisation $\ms{S}_{01,0;2} = 1$ so that the second
asymptotic series associated to the normalised second trace reads
\begin{equation}
  \Phi_{1;2}(g_s) =
  -2^{1/2}3^{9/4}\pi^{-1/2}g_s^{-1/2}
  \Phi_{0;1}(g_s)^{-3}.
\end{equation}
Since by Stokes automorphism $\Phi_{0;1}(g_s)$, and hence
$\Phi_{1;2}(g_s)$, transforms back to itself, the two families of
power series $\{\Phi_{0,n;2}(g_s)$, $\Phi_{1,n;2}(g_s)\}$ form a
minimal resurgent structure.  The complete set of Borel singularities
of this minimal resurgent structure is illustrated in
Fig.~\ref{fg:rays-Z2P2}.  Stokes rays passing through these singular
points divide the complex plane into infinitely many sectors in the
first and the fourth quadrants.  As usual we denote the sectors
bordering the positive real axis in the first and the fourth quadrants
as $I,IV$ and sometimes refer to the second and the third quadrants as
sectors $II,III$.

\begin{figure}
  \centering
  \includegraphics[height=7cm]{rays_Z2P2}
  \caption{Stokes rays and sectors in the $g_s$-plane for the series
    $\varphi_{0;2}(g_s), \varphi_{1;2}(g_s)$ in the second resurgent structure of local $\IP^2$.}
  \label{fg:rays-Z2P2}
\end{figure}

Following the pattern of Stokes rays we can collect all the Stokes
constants in the $2\times 2$ Stokes matrix
\begin{equation}
  \ms{S}_2(q) =
  \begin{pmatrix}
    0 & \ms{S}_{01;2}(q)\\
    0 & \ms{S}_{11;2}(q)
  \end{pmatrix},
\end{equation}
and then decompose it as
\begin{equation}
  \ms{S}_2(q) = \ms{S}_2^+(q) + \ms{S}_2^-(q),
\end{equation}
where $\ms{S}_2^+(q)$ and $\ms{S}_2^-(q)$ are respectively $q$- and
$q^{-1}$-series encoding Stokes constants in the upper and lower half
planes.
Here we choose for $q$ the same convention as in the previous subsection

\begin{equation}
  q = \re^{2\pi\ri \bb^2} = \re^{3\ri\hbar}= \re^{-\frac{3\ri}{g_s}},
\end{equation}

so that the entries of $\ms{S}_2(q)$ are

\begin{equation}
  \ms{S}_{01;2}(q) = q^{\frac{1}{6}}\sum_{n=0}^\infty
  \ms{S}_{01,n;2}q^{\frac{n}{3}},
  \quad
  \ms{S}_{11;2}(q) = \sum_{n=1}^\infty
  \ms{S}_{11,n;2}q^{\frac{n}{3}}.
\end{equation}

Since under complex conjugation

\begin{equation}
  \Phi_{-;2}(g_s)^* = \Phi_{-;2}(g_s^*),
\end{equation}
it follows that
\begin{equation}
  \ms{S}_2^-(q) = (\md{1}+\ms{S}_2^+(q^{-1}))^{-1} - \md{1},
  \label{eq:S2mp}
\end{equation}
and we only have to compute $\ms{S}_2^+(q)$.  The component
$\ms{S}^+_{11;2}(q)$ can be immediately identified
\begin{equation}
  \ms{S}^+_{11;2}(q) = (1+\ms{S}^+_{1}(q))^{-3}-1 =
  - 9q^{1/3}+45q^{2/3}-165q+486q^{4/3}-1197 q^{5/3} + 2517 q^2
  +\ldots.
\end{equation}
The first term of $\ms{S}^+_{01;2}(q)$ is $q^{1/6}$ by our
normalisation.  More terms of $\ms{S}^+_{01;2}(q)$ can again be
computed by using the TS/ST correspondence and radial asymptotic
analysis, to which we will momentarily turn.  We end this subsection
by recording the results here
\begin{align}
  \ms{S}^+_{01;2}(q) =
  &q^{1/6}(1 - 3q^{1/3} + 10q^{2/3} - 29q + 72q^{4/3}
  -155 q^{5/3} + 291 q^2 - 474 q^{7/3} + 660 q^{8/3} - 760 q^3 \nn
  &+  663q^{10/3} -309 q^{11/3}- 193 q^4 + \ldots).
    \label{eq:S01-P2}
\end{align}
Using \eqref{eq:S2mp} we can write down the following Stokes constants
in the lower half plane as well:

\begin{align}
  \ms{S}^-_{11;2}(q) =
  &(1+\ms{S}_1^+(q^{-1}))^{3}-1 = 9 q^{-1/3} + 36
    q^{-2/3} + 84 q^{-1} + 135 q^{-4/3} + 198 q^{-5/3} + 327 q^{-2} + \ldots,\nn
  \ms{S}^-_{01;2}(q) =
  &-\ms{S}^+_{01;2}(q^{-1})/(1+\ms{S}^+_{11;2}(q^{-1}))\nn  =
  &-q^{-1/6}(1 + 6 q^{-1/3} + 19 q^{-2/3} + 37 q^{-1} + 54 q^{-4/3}
    + 82 q^{-5/3} + 135 q^{-2} + 174 q^{-7/3} \nn
  &+ 171 q^{-8/3} + 234 q^{-3}
    + 399 q^{-10/3} + 406 q^{-11/3}+273q^{-4}+\ldots).
\end{align}

The diagonal Stokes constants in the series $\ms{S}_{11;2}(q)$ are
responsible for the automorphism of $\Phi_{1;2}(g_s)$ back to itself
and they are similar to Stokes constants in $\ms{S}_{00;1}(q)$ which
are illustrated in Fig.~\ref{fg:Stokes_Z1P2}.  The off-diagonal Stokes
constants in the series $\ms{S}_{01;2}(q)$ are illustrated in
Fig.~\ref{fg:Stokes_Z2P2}.

\begin{figure}
  \centering
  \includegraphics[height=6.5cm]{singularities_Stokes_Z2P2}
  \caption{Off-diagonal Stokes constants for the second resurgent structure of local $\IP^2$.}
  \label{fg:Stokes_Z2P2}
\end{figure}
