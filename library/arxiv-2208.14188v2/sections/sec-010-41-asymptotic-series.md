---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-010-41-asymptotic-series
section_title: "Asymptotic series"
section_number: 4.1
pages: 24-30
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.762
latex_coverage_ratio: 0.806
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
\label{sc:41.asymp}

The state integral of figure eight knot at level $k$ is already given
as a one-dimensional integral in \cite{Andersen:2016ugz}
\begin{align}
  \chi^{(k)}_{\knot{4}_1}(\mu,n;\tau) =
  &\frac{\eta_k}{k}\sum_{m\in \IZ_k}\int_{\IR+\ri\imag(c_\bb)-\ri|\mu|-\ri 0}\rd \sigma
    \mc{Z}^{(k)}_\bb[\Delta](\sigma-\mu,m-n)
    \mc{Z}^{(k)}_\bb[\Delta](\sigma,m)\nn
  &\phantom{==}\times(-1)^m
    \re^{\frac{\pi\ri}{k}((\sigma-c_\bb)^2-2(\mu-\sigma+c_\bb)^2-m^2+2(n-m)^2)},
      \label{eq:chi-41}
\end{align}
where $\eta_k = \exp \frac{\pi\ri}{6}(k+2 c_\bb^2/k)$.
This can be derived from the generic formula \eqref{eq:ZNgmMu0}.
We can choose the Neumann-Zagier data
\begin{equation}
  \pmb{A} =
  \begin{pmatrix}
    1&0\\1&1
  \end{pmatrix},\quad
  \pmb{B} =
  \begin{pmatrix}
    0&-1\\-1&-1
  \end{pmatrix},\quad
  \bs\nu =
  \begin{pmatrix}
    0\\0
  \end{pmatrix},
\end{equation}
with which \eqref{eq:ZNgmMu0} yields
\begin{align}
  &\mc{Z}_\gamma^{(k)}(\mu,n;\bb)\nn =
  &\frac{1}{\ri k^2}\sum_{m\in (\IZ_k)^2}\int \rd^2\sigma
    \re^{\frac{2\pi\ri}{k}(-\sigma_1\mu_1+\sigma_2\mu_1+m_1n_1-m_2n_1)}
    \re^{\frac{\pi\ri}{k}(2\sigma_1\sigma_2-2m_1m_2)}
    \mc{Z}_\bb^{(k)}[\Delta](\sigma_1,m_1)
    \mc{Z}_\bb^{(k)}[\Delta](\sigma_2,m_2) \nn=
  &\frac{\re^{\frac{\pi\ri}{12}(k+\frac{8c_\bb^2}{k})}}{\ri k}
    \sum_{m\in\IZ_k}
    \int\rd \sigma
    \mc{Z}_\bb^{(k)}[\Delta](\sigma,m)
    \mc{Z}_\bb^{(k)}[\Delta](\sigma+\mu,m+n)\nn
  &\phantom{=========}
    (-1)^{m+n}
    \exp\frac{\pi\ri}{k}\left(
    -(\sigma-c_\bb)^2-4\mu\sigma-\mu^2+2c_\bb\mu+m^2+4mn+n^2
    
    \right).
\end{align}
In the last step, we have integrated over $\sigma_2$ and summed
over $m_2$ using the Fourier transformation \eqref{eq:FourierFQD}.
We then relabeled $(\sigma_1,m_1)$ to $(\sigma,m)$ as well as
$(\mu_1,n_1)$ to $(\mu,n)$.  After changing the signs of $\mu,n$ we
find the same expression as \eqref{eq:chi-41} up to an overall
irrelevant factor
\begin{equation}
  \chi^{(k)}_{\knot{4}_1}(\mu,n;\tau) = \ri
  \re^{\frac{\pi\ri}{12}(k-\frac{4c_{\bb}^2}{k})}(-1)^n
  \re^{\frac{\pi\ri}{k}(-\mu^2-2c_\bb\mu+n^2)}
  \mc{Z}_{\gamma}^{(k)}(-\mu,-n;\hbar).
\end{equation}

As a one-dimensional integral, it is much easier to perform saddle
point analysis on \eqref{eq:chi-41}.  We first introduce an
alternative representation of the tetrahedron partition
function\footnote{This version of tetrahedron partition function was
  introduced in \cite{Andersen:2016ugz}.}
\begin{equation}
  \DD_\bb^{(k)}(u,m) = \mc{Z}_\bb^{(k)}[\Delta](c_\bb-\sqrt{k}u,m),
  \label{eq:Dk}
\end{equation}
in terms of which, the state integral \eqref{eq:chi-41} reads
\begin{align}
  \chi^{(k)}_{\knot{4}_1}(\mu,n;\tau) =
  &\frac{\eta_k}{k}\sum_{m\in \IZ_k}
    (-1)^m \re^{\frac{\pi\ri}{k}(2n^2-4nm+m^2)}
    \nn
  &\phantom{=}\times
    \int_{\IR+\ri 0}\rd \sigma
    \DD^{(k)}_\bb(\frac{1}{\sqrt{k}}(\sigma+\mu),m-n)
    \DD^{(k)}_\bb(\frac{1}{\sqrt{k}}\sigma,m)
    \re^{\frac{\pi\ri}{k}(-2\mu^2-4\mu\sigma-\sigma^2)}.
\end{align}

We scale the variables
\begin{equation}
  Z = 2\pi\bb \sigma,\quad u =2\pi\bb \mu
\end{equation}
and then perform asymptotic expansion of the tetrahedron partition
functions in the small $\bb$ limit using \eqref{eq:ZDasymp},
\begin{equation}
  \chi_{\knot{4}_1}^{(k)}(\mu,n;\bb) \sim
  \frac{\eta_k}{2\pi\bb k}\sum_{m\in\IZ_k}
  (-1)^m \re^{\frac{\pi\ri}{k}(2n^2-4nm+m^2)}
  \int \rd Z \exp\sum_{\ell\geq 0}(2\pi\ri\bb^2)^{\ell-1} U_\ell(u,Z)
\end{equation}
where the potential functions are
\begin{subequations}
  \begin{align}
    U_0(u,Z) =
    &\frac{1}{k}\left(
    u^2+2uZ +\frac{Z^2}{2} + 
    \Li_2(-\re^{Z}) + \Li_2(-\re^{u+Z})\right),\\
    U_{\ell\geq 1}(u,Z) =
    &\frac{1}{\ell!}\sum_{j\in\IZ_k}
      B_\ell(1-1/(2k)-j/k)
      \left(
      \Li_{2-\ell}(\zeta^{m-j-1/2} \re^{Z/k})
      +\Li_{2-\ell}(\zeta^{m-j-1/2}\re^{Z/k}x)
      \right).
  \end{align}
\end{subequations}
The critical equation of the leading order potential function reads
\begin{equation}
  0 = \frac{\pd}{\pd Z}U_0(u,Z) = \frac{1}{k}\left(2u+Z -\log(1+\re^{Z})
    -\log(1+\re^{u+Z})\right),
\end{equation}
which can be simplified to the algebraic equation
\begin{equation}
  -X^2 Y = (1-XY)(1-Y),
  \label{eq:alcr.41}
\end{equation}
with
\begin{equation}
  X = \re^u = x^k,\quad Y = -\re^{Z}.
\end{equation}
We also introduce the variable $\theta$ such that
\begin{equation}
  Y = -\theta^k.
\end{equation}

The critical point equation \eqref{eq:alcr.41} has two solutions in
terms of $Y$, corresponding to the geometric and conjugate flat
connections $\s_1, \s_2$ on the knot complement.

Numerically, they are the ones that in the limit $X\rightarrow 1$
reduce respectively to the solutions $\re^{\pi\ri/3}$ and
$\re^{-\pi\ri/3}$ of \eqref{eq:alcr.41}.

Near each critical point $\s_j$, the integrand is approximated by the
exponential
\begin{equation}
  \exp\left(\frac{V^{(k)}(\s_j)}{2\pi\ri\tau}\right),
  \label{eq:exp}
\end{equation}
where
\begin{align}
  V^{(k)}(\s_j) = U_0(\log(X),\log(-Y_j))+\frac{\pi^2}{6k}.
\end{align}
The extra factor $\pi^2/(6k)$ comes from the factor $\eta_k$.
Note the interesting relation $V^{(k)}(X,Y) = V^{(1)}(X,Y)/k$.

In addition, by expanding near the critical point and performing the
Gaussian integration order by order, for each critical point $\s_j$ we
can find an asymptotic power series $\varphi^{(k,\s_j)}(x;\tau)$,
which, together with the exponential factor \eqref{eq:exp}, forms the
trans-series
\begin{equation}
  \Phi_{\knot{4}_1}^{(k,\sigma_j)}(x;\tau) =
  \re^{V^{(k)}(\s_j)/(2\pi\ri\tau)}
  \varphi_{\knot{4}_1}^{(k,\s_j)}(x;\tau),\quad
  j=1,2.
\end{equation}
The one-loop contribution
$\varphi_{\knot{4}_1}^{(k,\s_j)}(x;0) =
\omega^{(k,\s_j)}_{\knot{4}_1}(x)$ has a universal
expression
\begin{align}
  \omega^{(k,\s_j)}_{\knot{4}_1}(x)=
  &\frac{\re^{\frac{\pi\ri}{4}+\frac{\pi\ri  k}{6}+\frac{2\pi\ri}{k}(n^2-1/12)}}
    {\sqrt{k(x^k\theta^{2k}-1)}}\theta^{1/2}x
    D_k^{*}(\zeta^{-1/2}\theta)^{1/k}
    D_k^{*}(\zeta^{-1/2}\theta x)^{1/k}\nn
  &\times\sum_{m\in\IZ_k}
    (-1)^m\zeta^{m^2/2}\theta^m x^{2m}
    (\zeta^{1/2}\theta;\zeta)_m^{-1}(\zeta^{1/2}\theta x;\zeta)_m^{-1}.
\end{align}
The power series
$\varphi_{\knot{4}_1}^{(k,\s_j)}(x;\tau)/\omega^{(k,\s_j)}_{\knot{4}_1}(x)$
on the other hand, depends in a very complicated way on the level $k$.


The case of $k=1$ is particularly simple. The dependence on
$n\in\IZ_1$ is trivial, and the state integral reduces to
\cite{Garoufalidis:2020xec}

\begin{align}
  \chi_{\knot{4}_1}(\mu;\tau) =
  \chi_{\knot{4}_1}^{(1)}(\mu;\tau) =
  \Phi_\bb(0)^{-2}\int_{\IR+\ri 0} \rd v \Phi_\bb(\mu+v)\Phi_\bb(v)
  \re^{\pi\ri(v^2-2(\mu+v)^2)}.
\end{align}
where we have used $\eta_1 = \Phi_\bb(0)^{-2}$.  The power series
$\varphi_{\knot{4}_1}^{(\s_i)}(x;\tau) =
\varphi_{\knot{4}_1}^{(k=1,\s_i)}(x;\tau)$ are given by
\cite{Garoufalidis:2020xec}
\begin{align}
  (\omega_{\knot{4}_1}^{(\s_1)})^{-1}
  \varphi_{\knot{4}_1}^{(\s_1)}(x;\frac{\tau}{2\pi\ri}) =
  &1-
    \frac{1}{24\gamma(x)^3}\left(
    x^{-3}-x^{-2}-2x^{-1}+15-2x-x^2+x^3\right)\tau\nn  +
  &\frac{1}{1152\gamma^6(x)}\left(
    x^{-6}-2x^{-5}-3x^{-4}+610x^{-3}-606x^{-2}-1210x^{-1}\right.\nn+
  &\left.3117 -1210x-606x^2+610x^3-3x^4-2x^5+x^6
    \right)\tau^2+\cO(\tau^3).
    \label{eq:vphi1.k1}
\end{align}
with
\begin{equation}
  \gamma(x) = \sqrt{x^{-2}-2x^{-1}-1-2x+x^2}.
\end{equation}
while $\varphi_2^{(\s_2)}(x;\tau) = \ri \varphi_1^{(\s_2)}(x;-\tau)$.
At level $k=2$, the power series are
\begin{align}
  &(\omega_{\knot{4}_1}^{(k=2,\s_j)})^{-1}\varphi_{\knot{4}_1}^{(k=2,\s_j)}(x;\tau)\nn
    =
  &1 -((1 + 6 x + 5 x^2 - 30 x^3 + 10 x^4 + 30 x^5 - 3 x^6 + 30 x^7 + 
    10 x^8 - 30 x^9 + 5 x^{10} + 6 x^{11} + x^{12}) \nn
  &(-1 - x^2 + x^4 + 2 x^2 Y_j))/(48 (-1 - x + x^2)^2 (1 - x + x^2)^2 (-1 + x + 
    x^2)^2 (1 + x + x^2)^2)\tau + \cO(\tau^2).
    \label{eq:phi41k2}
\end{align}


Additional terms as well as first few terms of the power series at
level $k=3$ can be found in Appendix~\ref{sc:phi.41}.

Several conclusions can be drawn from these data.  It is clear that
the coefficients of the power series depend only on the solution $Y_j$
to the NZ equation, but not on a $k$-th root of $Y_j$.  Furthermore,
they depend on the deformation parameters $u,n$ only through the
holonomy parameter $x$.  Finally, it is evident that the power series
become increasingly more complicated at higher levels $k$.
