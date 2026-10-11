---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-005-31-the-tsst-correspondence
section_title: "The TS/ST correspondence"
section_number: 3.1
pages: 11-15
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
text_source: latex
latex_prose_ratio: 0.681
latex_coverage_ratio: 0.962
---
\label{tsst-subsec}

The simplest case of the TS/ST correspondence corresponds to the case of toric CYs $X$ with one  
single true modulus, and we will only consider this type of 
examples in this paper. In this case, the mirror curve $\Sigma_X$ has genus one. As shown in 
\cite{ghm}, there is a canonical way to obtain an operator on $L^2(\IR)$, 
$\rho_X$, by Weyl quantization of this curve. The mass parameters of $X$ become parameters of the operator $\rho_X$. 
The quantization procedure introduces a Planck constant $\hbar \in \IR_{>0}$. It can be shown that, for 
appropriate values of the mass parameters, the operator $\rho_X$ is 
self-adjoint and of trace class, therefore its spectral determinant

\begin{equation}
\label{spec-det}
\Xi_X (\kappa, \hbar)= {\rm det}(1+ \kappa \rho_X)
\end{equation}

exists and defines an entire function of $\kappa$. Its expansion around the origin

\begin{equation}
\Xi_X (\kappa, \hbar)= 1+ \sum_{N \ge 1} Z_N (\hbar) \kappa^N 
\end{equation}

defines ``fermionic spectral traces" $Z_N(\hbar)$, which depend on $\hbar$ and on the possible mass parameters of $X$. It is easy to show that these fermionic traces are polynomials in the conventional ``bosonic" traces 

\begin{equation}
\tr \, \rho_X^n. 
\end{equation}

In the more general case in which the toric CY has $r$ true moduli, one can define a generalized spectral determinant depending on $r$ variables 
$\boldsymbol{\kappa}=(\kappa_1, \cdots, \kappa_r)$, with an expansion of the form \cite{cgm,cgum}

\begin{equation}
\Xi_X (\boldsymbol{\kappa},  \hbar)= 1+ \sum_{\bN } Z_{\bN}(\hbar) \kappa_1^{N_1} \cdots \kappa_r^{N_r}. 
\end{equation}


The TS/ST correspondence postulates, among other things, that the
fermionic spectral traces $ Z_{\bN}(\hbar) $ have an asymptotic
expansion as $\hbar \rightarrow \infty$ which is essentially given by
the formal power series (\ref{phiN}) \footnote{We choose this
  convention for $g_s$ because we want to treat $\hbar$ and $g_s$ as
  modular-like parameters, and the relation $\hbar = -g_s^{-1}$ is the
  analogue of an $S$-type modular transformation.\label{fn:gs}}

\begin{equation}
\label{zn-ae}
Z_{\bN}(\hbar) \sim c_{\bN} g_s^{\nu_{\bN}} \Phi_{\bN}(g_s), \qquad \hbar = -g_s^{-1} \gg 1. 
\end{equation}

Here, $c_{\bN}$ and $\nu_{\bN}$ are constants. Since the fermionic
spectral traces are well-defined for $\hbar \in \IR_{>0}$, this
defines a rigorous non-perturbative completion of topological string
theory at the conifold point. This particular consequence of the TS/ST
correspondence has been tested in detail and extensively studied in
e.g. \cite{kama,mz,kmz,cgm,cgum,cms}. It should be noted that the
asymptotic conjecture (\ref{zn-ae}) is itself the consequence of a
stronger conjecture which provides an {\it exact} expression for the
spectral determinant and the fermionic spectral traces in terms of
topological string data (and, in particular, of BPS invariants of the
CY $X$).  One can obtain in this way exact quantization conditions for
the spectral problem of the quantum mirror curve (see also \cite{wzh,
  hm,fhm,swh} for related developments).

As we will show, the relation (\ref{zn-ae}) turns out to be very
useful to study the resurgent structure of the formal power series
$\Phi_{\bN}(g_s)$. However, to understand this structure, we have to
consider the case in which $g_s$ (or, equivalently, $\hbar$) is {\it
  complex}.  The complexification of $\hbar$ in the TS/ST
correspondence was addressed in different forms in
\cite{kpamir,ks1,ks2, gm-complex}. In \cite{ks1, ks2} it was shown in
some examples that the spectral problem associated to the operator
$\rho_X$ is well-defined when $\hbar$ is of the form
$\hbar = 2 \pi \re^{\ri \theta}$, where $\theta \in (0, \pi)$. The
spectrum of the operator $\rho_X$ is in this case discrete and
complex.

In this paper we will assume that TS/ST correspondence can be extended to the complex $\hbar$-plane minus the negative real axis, 

\begin{equation}
\label{h-domain}
\hbar \in \IC'=\IC\backslash \IR_{\le 0},  
\end{equation}

in such a way that the relevant operators remain of trace class, 
and the fermionic spectral traces $Z_{\bN}(\hbar)$ are {\it analytic functions} on $\IC'$. 
Although we do not know
how to establish this on general grounds, we will show that it is possible to perform the 
analytic continuation to $\IC'$ in explicit expressions for the $Z_{\bN} (\hbar)$. 
It turns out that the resulting picture shares many formal similarities with complex Chern--Simons theory 
on the complement of a hyperbolic knot $\CK$. More precisely, we have 
the following parallelisms: 

\begin{enumerate}

\item The spectral determinant $\Xi_X (\kappa, \hbar)$ and the
  fermionic spectral traces $Z_N (\hbar)$ correspond to state integral
  invariants of the knot \cite{hikami,dglz}, also known as
  Andersen--Kashaev invariants \cite{ak}. For the complement of a
  hyperbolic knot, the Andersen--Kashaev invariant is a function
  $Z_{\CK}(u, \tau)$ of the holonomy $u$ around the knot, and a
  complex coupling constant $\tau$ which plays the r\^ole of Planck's
  constant.  Therefore, we expect that the full spectral determinant
  $\Xi_X (\kappa, \hbar)$, as function of the modulus $\kappa$,
  corresponds to the state integral as a function of $u$. Note that
  both are entire functions of the moduli (for $Z_{\CK}(u, \tau)$,
  this was proved in \cite{ggm2} in the case of the first two
  non-trivial hyperbolic knots). Accordingly, the spectral traces
  $Z_N (\hbar)$ correspond to the coefficients of $Z_{\CK}(u, \tau)$
  in a Taylor expansion around $u=0$. The first non-trivial
  coefficient in this expansion, which is
  $Z_\CK(\tau)= Z_{\CK}(u=0, \tau)$, was studied in \cite{ggm1} (the
  case with more than one modulus in topological string theory would
  correspond to the case of links in complex CS theory).

\item The asymptotic expansion (\ref{zn-ae}) of $Z_{\bN}(\hbar)$,
  involving the perturbative topological string series, corresponds to
  the expansion of the Andersen--Kashaev invariant at large positive
  values of $\tau$. This is given by the asymptotic expansion of
  complex CS theory around the so-called {\it conjugate} connection
  (which is the complex conjugate to the geometric connection).

\item The {\it volume conjecture} for the Andersen--Kashaev invariant
  \cite{ak} states that its asymptotics at $\tau \rightarrow 0^+$
  involves the complexified volume\footnote{The imaginary part of the
    complexified volume is the Chern-Simons action.} $V_{\CK}$ of the
  three sphere complement of the hyperbolic knot $\CK$:

  \begin{equation}
    \label{vc-knots}
    Z_{\CK} (\tau) \sim \exp\left(-{V_{\CK} \over \tau} \right),
    \qquad \tau \rightarrow 0^+. 
  \end{equation}

  In this equation, we have set $u=0$ in $Z_{\CK} (u, \tau)$, but
  there is a generalization to arbitrary $u$ \cite{gukov,ak}.  The
  conjecture (\ref{vc-knots}), which is closely related to the
  original Kashaev conjecture \cite{kashaev}, relates a ``quantum"
  invariant of the knot in the l.h.s., to a ``classical" geometric
  invariant in the r.h.s. Interestingly, the TS/ST correspondence
  implies a {\it conifold volume conjecture for toric CYs},

\begin{equation}
\label{vc-cy}
Z_{\bN}(-g^{-1}_s) \sim \exp \left({1 \over g_s} \sum_{i=1}^r N_i \CV_i  \right), \qquad g_s \rightarrow 0^-, 
\end{equation}

where $\CV_i$, $i=1, \cdots, r$ are the values of the K\"ahler parameters of the CY at the conifold point. This can be also regarded 
as a relation between the asymptotics of a ``quantum" invariant 
on the l.h.s. (a spectral trace obtained by quantizing the mirror curve), to a ``classical" geometric property of the CY. Let us note as 
well that the $\CV_i$ can be regarded as the ``minimal" values of the volumes of the CY manifold. The conifold volume conjecture (\ref{vc-cy}) for toric CY manifolds 
was checked in one and two-moduli examples in \cite{mz,kmz,cgm,cgum,kerr}. 

\item The state integral has a factorization property, namely, it can be written as a sum of products of 
holomorphic and anti-holomorphic blocks \cite{pasq,bdp,dimofte-state,GK-qseries,ggm1,ggm2}. Moreover, the blocks
are given by $q$ and $\tq$-series, where 

\begin{equation}
q= \re^{2 \pi \ri \tau}, \qquad \tq =   \re^{-2 \pi \ri /\tau}. 
\end{equation}

As we will see, the fermionic spectral traces also factorize in various examples, and can be written as a sum of products of $q$ and $\tq$ series. There is however an important 
difference between the state integral and the fermionic spectral traces. The former is symmetric under the $S$-duality transform

\begin{equation}
\tau \rightarrow -{1\over\tau} 
\end{equation}

which exchanges $q$ and $\tq$. This leads to a symmetry between the holomorphic and anti-holomorphic blocks, which involve the same functions (with different arguments). 
In contrast, the fermionic spectral traces do {\it not} have this symmetry, and sending $\hbar$ to $-1/\hbar$ exchanges the conventional topological string with the NS topological string. As a consequence, the holomorphic and anti-holomorphic blocks are given by different functions, as we will see in examples.

\item As shown in \cite{ggm1,ggm2}, the Stokes constants associated to the different asymptotic series in complex CS theory are integer invariants, and they turn out to be closely related to the DGG index of the knot \cite{dgg-index}. In the case of the topological string, the Stokes constants are precisely the new integer invariants that we define in this paper, therefore we can regard these as analogues of the DGG index. 

 \end{enumerate}


\begin{table}
\begin{center}
\begin{tabular}{|| l || l||}
\hline
 complex CS theory  & TS/ST correspondence\\ \hline\hline
state integral &  spectral determinant and traces \\ \hline
expansion around conjugate connection &  perturbative topological string \\ \hline
volume conjecture&  conifold volume conjecture\\ \hline
(symmetric) factorization & (non-symmetric) factorization  \\\hline
DGG index &new integer invariants \\ \hline
\end{tabular}
\end{center}
\caption{Similarities between structures appearing in complex CS theory and in the TS/ST correspondence.}
\label{table-sim}
\end{table}


We summarize these parallelisms in Table \ref{table-sim}.  The formal
similarities between the two theories suggest a reinterpretation of
topological string theory on toric CYs in terms of a topological gauge
theory, or perhaps of a superconformal field theory in 3d, in view of the
3d/3d correspondence \cite{DGG1,ter-yama1}\footnote{The possible relationship with a 3d superconformal field 
theory was already pointed out in \cite{ghm}, where it was also noted that the spectral traces at large $N$ and fixed $\hbar$ 
satisfy a $N^{3/2}$ scaling typical of many 3d theories.}.
We should note that, even at the formal level, the topological string story seems to be
much more involved than the complex CS counterpart.  For example, 
in complex CS, the different formal power series have a simple
semiclassical interpretation in terms of expansions around different
saddle points, and this makes their calculation a relatively easy task. We do 
not have such a physical interpretation for the topological string series (\ref{bts}). 
Another crucial difference is that the full
moduli-dependent state integral $Z_\CK (u, \tau)$ can be represented in terms of an
integral, which can be in addition calculated explicitly in many
interesting examples. In the case of the topological string, we are
not aware of integral expressions for the spectral
determinant.

As a final comment on the formal similarities between CS and
topological string theory, let us point out the following.  One could
think that $Z_{\CK}(u, \tau)$, being a wavefunction, corresponds
rather to an open topological string theory. However, as noted in
\cite{mmrev}, it is likely that $\Xi(\kappa, \hbar)$ has an
interpretation as a wavefunction on the moduli space of the closed CY
moduli, in line with the suggestion of \cite{witten-bi}. One important
open problem is to find the analogue of the quantum differential
equation satisfied by $\Xi(\kappa, \hbar)$, similar to the AJ equation
satisfied by $Z_{\CK}(u, \tau)$. Inspired by results in the 4d limit
of the theory \cite{bgt}, it has been suggested that $q$-Painlev\'e
equations could play such a r\^ole \cite{bgt-qdef}, but a complete
description is still lacking. Recently, and following the same
philosophy, \cite{alim} obtained a ``wave equation" in the case of the
resolved conifold. Connections between partition functions in the
4d case and integrable equations have been also studied in
\cite{bdmt,teschner1,teschner2}.




\subsection{Local $\IF_0$}


\begin{figure}
  \centering \includegraphics[height=4cm]{toricF0}
  \caption{The toric diagram of the local $\IF_0$ geometry.}
  \label{fg:toricF0}
\end{figure}

The first example we consider is the canonical bundle over the
Hirzebruch surface $\IF_0 = \IP^1\times \IP^1$, which is also called
the local $\IF_0$ geometry,
\begin{equation}
  X = \CO(-2,-2) \rightarrow \IP^1\times \IP^1.
\end{equation}

This geometry is a toric variety and it is described by
the toric diagram in Fig.~\ref{fg:toricF0}.  The K\"{a}hler
moduli of this geometry are one true modulus $u$ corresponding
to the internal vertex of the toric diagram, and one mass parameter
$m_{\IF_0}$ corresponding to one of the four boundary vertices.  For the
topological string theory on local $\IF_0$, the full moduli space is
identified with the family of mirror curves described by the equation

\begin{equation}
  \re^x + m_{\IF_0} \re^{-x} + \re^y +\re^{-y} + \tilde{u} = 0,\quad x,y\in\IC.
  \label{eq:mirrorF0}
\end{equation}

The moduli are a ``true" modulus $u = 1/\tilde{u}^2$ and
the mass parameter $m_{\IF_0}$.  The maximal conifold point on the moduli space is in the
discriminant of \eqref{eq:mirrorF0}.  For simplicity we only consider
$m_{\IF_0} = 1$, in which case the maximal conifold point is located
at
\begin{equation}
  u = \frac{1}{16}.
\end{equation}
The free energies of the topological string at the maximal conifold
point can be computed by the holomorphic anomaly equations
\cite{bcov-pre,bcov}, and in terms of the local flat coordinate
$\lambda$ they are \cite{hkr,kmz}
\begin{subequations}
  \begin{align}
    \CF_0(\lambda,m_{\IF_0}=1) =
    &\frac{\lambda^2}{2}
      \left(\log\lambda+\log\left(\frac{\pi^2}{4}\right)-\frac{3}{2}\right)
      -\frac{2C}{\pi^2} -
      \frac{\pi^2\lambda^3}{12}+\frac{5\pi^4\lambda^4}{288}
      -\frac{7\pi^6\lambda^5}{960} + \ldots,
      \label{eq:CF0-F0}
    \\
    \CF_1(\lambda,m_{\IF_0}=1) =
    &-\frac{1}{12}\log(\lambda)
      +\frac{\pi^2\lambda}{24}+\frac{13\pi^4\lambda^2}{288} -
      \frac{29\pi^6\lambda^3}{576}+\ldots,
      \label{eq:CF1-F0}
    \\
    \CF_2(\lambda,m_{\IF_0}=1) =
    &-\frac{1}{240\lambda^2} +
      \frac{53\pi^6\lambda}{1920} + \ldots,
      \label{eq:CF2-F0}
  \end{align}
\end{subequations}
where $C = \imag(\Li_2(\ri)) = 0.915966\ldots$ is the Catalan's
constant, and we have restricted the mass parameter $m_{\IF_0}=1$.  We
can then construct the formal power series $\Phi_{0;N}(g_s)$ by
\eqref{phiN}.

In this section we are only concerned with the case of $N=1$.  We will
see that this example already has a very rich resurgent structure,
and it is very similar to the quantum invariants of the figure eight knot studied in \cite{ggm1,ggm2}. Furthermore, we will
show the power of the TS/ST correspondence, which enables us to write
down the \emph{complete} set of Stokes constants.


\subsubsection{The first resurgent structure}

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
