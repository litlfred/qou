---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-005-321-strong-coupling-region
section_title: "Strong coupling region"
section_number: 3.2.1
pages: 11-15
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.931
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
We start with the region $\CW$ inside the curve of marginal
stability. The
spectrum consists of one monopole with charge
 
\begin{equation}
  \gamma_m=(0,1)
\end{equation}
 
and one dyon with charge
 
\begin{equation}
  \gamma_d=(1,1), 
\end{equation}
 
see \cite{sw,fb,selfdual} (we follow the conventions in \cite{fb}). We
also have the corresponding antiparticles, carrying opposite
charges. Then, the only nonzero coefficients in (\ref{su2tba}) are
 
\begin{equation}
  c_e(\gamma_m)=c_e(\gamma_d)=-1, \qquad c_m(\gamma_d)=1.
\end{equation}
 
Therefore, the equations (\ref{su2tba}) read
 
\begin{equation}
  \ba
  \chi_e (\zeta)&=  \chi^{\rm sf}_{e} (\zeta)\exp\left[{1\over 2 \pi
      \ri} \left( \CC_{\gamma_m}+ \CC_{\gamma_d} \right) \right],\\ 
  \chi_m (\zeta)&=  \chi^{\rm sf}_{m} (\zeta)\exp\left[-{1\over 2 \pi
      \ri} \CC_{\gamma_d} \right], 
  \ea
\end{equation}

and it is better to write them in terms of $\chi_d$, $\chi_m$,

\begin{equation}
  \ba
  \chi_d (\zeta)&=  \chi^{\rm sf}_{d} (\zeta)\exp\left[{1\over 2 \pi
      \ri}  \CC_{\gamma_m} \right],\\ 
  \chi_m (\zeta)&=  \chi^{\rm sf}_{m} (\zeta)\exp\left[-{1\over 2 \pi
      \ri} \CC_{\gamma_d} \right]. 
  \ea
\end{equation}
 
 
We now write the central charges
 
\begin{equation}
  Z_{d}=\re^{\ri \phi_d}|Z_d|, \qquad Z_m=-\ri \re^{\ri \phi_m} |Z_m|. 
\end{equation}
  
These conventions are such that, when $u \in \IR$ inside the curve of
marginal stability, we have $\phi_d=\phi_m=0$. Let us define the
functions $\epsilon_{d,m}$ and $\widetilde \epsilon_{d,m}(\theta)$ as
follows (this is similar to the notation used in \cite{amsv,ims}):
  
\begin{equation}
  \ba
  \chi_d\left( -\re^{\ri \phi_d -\theta}\right)&=
  \exp\left(-\epsilon_d (\theta-\ri \phi_d) \right)=
  \exp\left(-\widetilde \epsilon_d (\theta) \right),\\ 
  \chi_m\left( \ri \re^{\ri \phi_m -\theta}\right)&=
  \exp\left(-\epsilon_m (\theta-\ri \phi_m) \right)=
  \exp\left(-\widetilde \epsilon_m (\theta) \right).  
  \ea
\end{equation}

Then, the conformal limit of the TBA equations reads:

\begin{equation}\label{eq:cTBA-1}
  \ba
  \widetilde \epsilon_d(\theta)&=\pi |Z_d| \re^{\theta}-2 \int_\IR
  {\widetilde L_m(\theta') \over \cosh(\theta-\theta'+ \ri \phi_m-\ri
    \phi_d)} {\rd \theta' \over 2 \pi}, \\ 
  \widetilde \epsilon_m(\theta)&=\pi |Z_m| \re^{\theta}-2 \int_\IR
  {\widetilde L_d(\theta') \over \cosh(\theta-\theta'+ \ri \phi_d-\ri
    \phi_m)} {\rd \theta' \over 2 \pi},  
  \ea
\end{equation}

where we have shifted $\theta \to \theta -\log R$, and

\begin{equation}
  \widetilde L_{m,d}(\theta) = \log\left(1+\re^{-\widetilde
      \epsilon_{m,d}(\theta)} \right).  
\end{equation}

We have used here the fact that the BPS spectrum consists of
hypermultiplets, therefore $\sigma(\gamma)=-1$.

The equations simplify further when $u$ is real, i.e.
$u \in \IR \cap \CW=[-1, 1]$. Then one has $\phi_d=\phi_m=0$, i.e.
 
\begin{equation}
  Z_{\gamma_d}>0, \qquad Z_{\gamma_m}=-\ri |Z_{\gamma_m}|, 
\end{equation}
 
and we obtain, 

\begin{equation}\label{eq:cTBA-1R}
  \ba
  \epsilon_d(\theta)&=\pi |Z_d| \re^{\theta}-2 \int_\IR { L_m(\theta')
    \over \cosh(\theta-\theta')} {\rd \theta' \over 2 \pi}, \\ 
  \epsilon_m(\theta)&=\pi |Z_m| \re^{\theta}-2 \int_\IR { L_d(\theta')
    \over \cosh(\theta-\theta')} {\rd \theta' \over 2 \pi}.
  \ea
\end{equation}

We also note that, before taking the conformal limit, we find the more
conventional TBA equations


\begin{equation}
  \ba
  \epsilon_d(\theta)&= \pi r Z_d \cosh(\theta)-2 \int_\IR
  {L_m(\theta') \over \cosh(\theta-\theta')} {\rd \theta' \over 2
    \pi}, \\ 
  \epsilon_m(\theta)&= \pi r |Z_m| \cosh(\theta)-2 \int_\IR
  {L_d(\theta') \over \cosh(\theta-\theta')} {\rd \theta' \over 2
    \pi},  
  \ea
\end{equation}

where 

\begin{equation}
  r=2 R. 
\end{equation}

The definition of $r$ is such that we have the same conventions as in
\cite{kl-mel-1}.

The TBA equations simplify greatly when $u=0$. In this case, we have
that

\begin{equation}
  |Z_d|= |Z_m|=\xi, 
\end{equation}

and that\footnote{Anticipating the identification
  with quantum periods, this equation does not mean that the dyonic
  and magnetic quamtum periods $\Pi_D(u,\hbar), \Pi_B(u,\hbar)$ are
  identical at $u=0$, as $\hbar$ is identified with $\theta$
  differently, c.f.~\eqref{eq:TBA-dict-1}.}

\begin{equation}
  \epsilon_d(\theta)= \epsilon_m(\theta)=\epsilon(\theta). 
\end{equation}

The two TBA equations collapse to one, 

\begin{equation}
  \label{u0TBA}
  \epsilon(\theta)=\pi \xi \re^{\theta}-2 \int_\IR {L(\theta') \over
    \cosh(\theta-\theta')} {\rd \theta' \over 2 \pi}, 
\end{equation}

which coincides with the integral equation (\ref{zmathieu})
associated to the modified Mathieu equation and the Sinh-Gordon model
and studied by Zamolodchikov (the factor $\xi$ can be absorbed in a
redefinition of the angle $\theta$). The equation (\ref{u0TBA}) was
written down in \cite{oper} as governing the quantum periods at $u=0$.

We claim that the functions $\widetilde \epsilon_{d,m}(\theta)$ are
identified with quantum periods as follows

\begin{equation}\label{eq:TBA-dict-1}
  \begin{aligned}
    \widetilde \epsilon_d(x+\ri\phi_d)
    &= \frac{1}{\hbar}s(\Pi_D)(\hbar),\\
    \widetilde \epsilon_m\left(x+\ri\phi_m-\frac{\ri\pi}{2}\right)
    &= \frac{1}{\hbar} s(\Pi_B)(\hbar),
  \end{aligned}
\end{equation}

with 

\begin{equation}
  \hbar = \pi^{-1}\re^{-x}, \quad \Pi_D=\Pi_A+\Pi_B \ ,
\end{equation}

where $\Pi_D$ denotes the dyonic quantum period. Then the TBA
equations \eqref{eq:cTBA-1} are consistent with the leading order
contribution by the classical periods in the small $\hbar$ expansion

\begin{equation}
  s(\Pi_{D,B})(\hbar) = Z_{d,m} + \mc O(\hbar^2) \ .
\end{equation}

Furthermore, the TBA equations \eqref{eq:cTBA-1} clearly indicate that
for some argument angles of $\hbar$ the quantum periods have
discontinuities. These discontinuities are determined by the BPS
spectrum of SW theory and give the singularity structure of the Borel
transform of the quantum periods. These Stokes discontinuities can
also be deduced from \eqref{eq:cTBA-1}. The location of the
singularities in the Borel plane, as well as the precise
discontinuities, can be checked against the asymptotic series of the
quantum periods, by inspecting the Borel plane and by performing
lateral Borel resummations, respectively.

For instance, from the TBA equations \eqref{eq:cTBA-1}, we conclude
that $s(\Pi_B)$ are discontinuous across the rays
$\arg(\hbar) = \phi_d, \phi_d+\pi$, with 

\begin{align}
  \text{disc}_{\phi_d(+\pi)} (\Pi_B)(\hbar)
  =
  & +2\hbar\log\left(1+\re^{-\tfrac{1}{\hbar} s(\Pi_D)(\hbar)}\right) \nn
    =
  & 2\hbar\(\re^{-\tfrac{1}{\hbar} s(\Pi_D)(\hbar)} -
    \frac{1}{2}\re^{-2\tfrac{1}{\hbar} s(\Pi_D)(\hbar)} + \ldots\) \ .
    \label{eq:disc-B1}
\end{align}

When $u=0$, we have $\phi_d=0$, and the discontinuities are located at
$\arg(\hbar) = 0,\pi$. 


The discontinuity across the ray $\arg(\hbar) = 0$ can be computed by
a lateral Borel resummation of the quantum $B$ period. We check it
against the right hand side of \eqref{eq:disc-B1}, and find good
agreement. See Table~\ref{tb:disc-Bu0}. Similarly, $s(\Pi_D)$ is
discontinuous across the rays $\arg(\hbar) = \phi_m\pm\frac{\pi}{2}$,
and one has

\begin{equation}
  \text{disc}_{\phi_m\pm\frac{\pi}{2}} (\Pi_D)(\hbar)
  = -2\hbar
  \log\left(1+\re^{-\tfrac{1}{\hbar} s(\Pi_B)(\hbar)}\right) \ .
\end{equation}

 Numerical checks for this discontinuity formula are
completely analogous.

\begin{table}
  \centering
  \begin{tabular}{cll}\toprule
    terms & lateral Borel sum & r.h.s.\ of \eqref{eq:disc-B1}\\\midrule
    181   & 0.17499253901611 & 0.1749925390148815032360 \\
    185   & 0.17499253901578 & 0.1749925390148815032482 \\
    189   & 0.17499253901545 & 0.1749925390148815032553 \\
    193   & \underline{0.174992539015}19
                              & \underline{0.17499253901488150325}95 \\\bottomrule
  \end{tabular}
  \caption{Discontinuity across the ray $\arg(\hbar) = 0$
    for $\Pi_B(u=0,\hbar=1)$ computed by lateral Borel resummation and
    by using \eqref{eq:disc-B1} with increasing number of terms in the
    asymptotic series. Underlined are stabilised digits.}
  \label{tb:disc-Bu0}
\end{table}













From the discontinuity formula \eqref{eq:disc-B1} we can deduce in the
standard way a formula for the large order behavior of $\Pi_B^{(n)}$,
of the form (see e.g. \cite{msw})

\begin{align}
&  \ri \Pi_B^{(n)}  \sim
  \frac{2 A^{-2n+b}}{\pi} \Gamma(2n+b) \nn
  &\cdot\(
    1-\frac{\mu_2 A}{2n+b-1}+ \frac{\mu_3
    A^2}{(2n+b-1)(2n+b-2)} - \frac{\mu_4
    A^3}{(2n+b-1)(2n+b-2)(2n+b-3)}\cdots\). \label{eq:aD-asymp}
\end{align}

If we write the dyonic quantum period as

\begin{equation}
  \Pi_D= \sum_{n \ge 0} \Pi_D^{(n)}\hbar^{2n},
\end{equation}

we can identify

\begin{equation}
  A= \Pi_D^{(0)}, \quad b=-1,\quad \mu_2= \Pi_D^{(1)}, \quad \mu_3 =
  (\Pi_D^{(1)})^2/2 
  ,\quad \mu_4 = (\Pi_D^{(1)})^3/6+\Pi_D^{(2)}  ,\quad\ldots
\end{equation}

These identities are numerically checked at $u=0$ up to
all stabilised digits (more than 40) with the help of Richardson
transforms.

The large order behavior of $\Pi_B^{(n)}$ also indicates that the
Borel transform $\widehat \Pi_B(\zeta)$ has branch points at
$\zeta = \pm \Pi_D^{(0)}$, which is the central charge of the BPS
state (dyon) whose electromagnetic charge has non-vanishing Dirac
pairing with the charge of the monopole. Similarly, the Borel
transform of $\Pi_A(u,\hbar)$ should have branch points at the central
charges of monopoles and dyons with electromagnetic charges
$\pm(0,1), \pm(1,1)$, while the Borel transform of $\Pi_B(u,\hbar)$
have branch points only at the central charges of dyons. This explains
the Borel plane plots in Figure~\ref{fg:u0-bc}, where we also
superimpose the central charges of the contributing BPS states as red
spots.
