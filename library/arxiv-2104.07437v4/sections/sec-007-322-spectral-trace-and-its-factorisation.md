---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-007-322-spectral-trace-and-its-factorisation
section_title: "Spectral trace and its factorisation"
section_number: 3.2.2
pages: 20-24
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.982
---
\label{sc:block-F0}

According to the TS/ST correspondence \cite{ghm,cgm}, we should
promote the mirror curve \eqref{eq:mirrorF0} to the difference
operator

\begin{equation}
  \CO_{\IF_0}(m_{\IF_0}) = \re^{\ms{x}} + m_{\IF_0} \re^{-\ms{x}} +
  \re^{\ms{y}} + \re^{-\ms{y}},
\end{equation}

where $\ms{x}$ and $\ms{y}$ are Heisenberg operators, satisfying the commutation
relation
\begin{equation}
  [\ms{x}, \ms{y}] = \ri\hbar.
\end{equation}
Then the inverse operator $\rho_{\IF_0} = \CO_{\IF_0}^{-1}$ is of
trace class \cite{kama} and its Fredholm determinant as well as
fermionic spectral traces $Z_N(\hbar)$ can be defined.  Furthermore
the latter can be computed explicitly \cite{kmz}.

The integral kernel for $\rho_{\IF_0}$ was obtained in \cite{kmz} for real $\hbar$, and it reads

\begin{equation}
  \label{f0ker}
  \rho_{\IF_0}(x_1, x_2)
  = \frac{\re^{- \mathsf{b}^2 \xi /2+\pi\bb(x_1+x_2)/2}}
  {2\bb\cosh(\pi\frac{x_1-x_2}{\bb})}
  \frac{\fad(x_1-\bb\xi/2\pi+\ri\bb/4)\fad(x_2+\bb\xi/2\pi+\ri\bb/4)}
  {\fad(x_1+\bb\xi/2\pi-\ri\bb/4)\fad(x_2-\bb\xi/2\pi-\ri\bb/4)}.
\end{equation} 







The parameter $\xi$ is related to the mass parameter $m_{\IF_0}$ by

\begin{equation}
  \label{mmu}
  m_{\IF_0}=\re^{2 \mathsf{b}^2 \xi},
\end{equation}

and $\mb$ is related to $\hbar$ by

\begin{equation}
  \hbar = \pi \bb^2. 
\end{equation}

As we mentioned above, we need to perform an analytic continuation of the spectral theory of $\rho_{\IF_0}$ to complex $\hbar$. Since we have an explicit expression (\ref{f0ker}) for its integral kernel, this is easy to do. We just note that Faddeev's quantum dilogarithm can be analytic continued to all values of $\bb$ such that $\bb^2 \notin \IR_{\le 0}$. Therefore, (\ref{f0ker}) defines the integral kernel of the operator for $\hbar \in \IC'$, as required in (\ref{h-domain}). 

The first spectral trace has the following integral representation:
\begin{equation}
  \tr\rho_{\IF_0}=
  \frac{\re^{-\bb^2\xi/2}}{2\bb} \int_{\IR}
  \re^{\pi\bb  x}
  \frac{\fad(x-\bb\xi/2\pi+\ri\bb/4)\fad(x+\bb\xi/2\pi+\ri\bb/4)}
  {\fad(x+\bb\xi/2\pi-\ri\bb/4)\fad(x-\bb\xi/2\pi-\ri\bb/4)}
  \rd x, 
  \label{eq:F0intxi}
\end{equation}
while the fermionic trace is
\begin{equation}
  Z_1(m_{\IF_0},\hbar)= \tr\rho_{\IF_0}.
\end{equation}
We will only be interested in the simple case $\xi = 0$, where the
integral reads
\begin{equation}
  \tr\rho_{\IF_0} =
  \frac{1}{2\bb} \int_{\IR}
  \re^{\pi\bb  x}
  \frac{\fad(x+\ri\bb/4)^2}
  {\fad(x-\ri\bb/4)^2}
  \rd x.\label{eq:F0intxi0}
\end{equation}
Note that the integrand mostly consists of the product of quantum
dilogarithms, and the spectral trace is therefore very similar to state integrals in complex
Chern-Simons theory.  Due to this reason, we will sometimes refer to the
integral representation of spectral traces as state integrals. 

The integrand of \eqref{eq:F0intxi0} is integrable for $\real\mb>0$,
which we always assume, and the spectral trace (\ref{eq:F0intxi0}) is
an analytic function of $\hbar \in \IC'$. When $\hbar>0$, a conjecture
of \cite{ghm} states that it can be computed in terms of the so-called
modified grand potential of local $\IF_0$, which is fully specified by
BPS invariants of the CY threefold. This conjecture can be extended to
complex $\hbar$, provided ${\rm Re}(\hbar)>0$ (otherwise the large
radius expansion embodied in the grand potential does not converge).
We have explicitly verified this extended conjecture in many
cases. Therefore, our analytic continuation of the trace to complex
$\hbar$ matches the natural analytical continuation of the modified
grand potential, in such a way that the conjecture of \cite{ghm}
remains true.




We now show that the minimal resurgent structure
$\{\Phi_{0,n}(g_s), \Phi_{1,n}(g_s)\}$ can be recovered by performing
a saddle point analysis of the state integral, but we hasten to
comment that this is rather exceptional due to the particular nice
form of the integrand in (\ref{eq:F0intxi0}). In general, as we will see in
Section~\ref{sc:block-P2}, one cannot easily recover the minimal
resurgent structure from the integral representation of the spectral
traces.

In the limit $\hbar \rightarrow\infty, g_s = -1/\hbar \rightarrow 0$,
the integrand has the semiclassical expansion

\begin{equation}
  \exp \sum_{n=0}^\infty g_s^{2n-1} V_n(\tx,\bb),
  \quad \tx = 2\pi\bb^{-1}x,
\end{equation}

where

\begin{equation}
  V_0(\tx,\bb) = -\frac{1}{2\pi^2\ri}\left(\pi\ri\tx + 2\Li_2(-\ri
    \re^{\tx}) - 2\Li_2(\ri \re^{\tx})\right).
\end{equation}

The saddle point equation
\begin{equation}
  \frac{\pd V_0(\tx)}{\pd \tx} = -\frac{1}{2\pi^2\ri}
  \left(\pi\ri-2\log\frac{1+\ri \re^{\tx}}{1-\ri \re^{\tx}}\right) = 0
\end{equation}

has two sets of solutions

\begin{equation}
  \tx =
  \begin{cases}
    2\pi\ri \IZ,\\
    \pi\ri+2\pi\ri \IZ.
  \end{cases}
\end{equation}

By expanding the integrand in the semiclassical limit around these saddle
points, and performing Gaussian integration order by order in $g_s$, we obtain two
infinite sets of asymptotic series.  After proper normalisation they
are precisely $\Phi_{0,n}(g_s)$ and $\Phi_{1,n}(g_s)$, as defined in
\eqref{eq:Phi0n-F0}, \eqref{eq:Phi1n-F0}.\footnote{If we plug
  $\tx = \pi\ri +2\pi\ri\IZ$ in $V_0(\tx,\bb)$ we seem to find the
  leading contribution
  $\exp(-\frac{1}{g_s}(\CV_{\IF_0}+\frac{\ri}{2}))$ to
  $\Phi_{1}(g_s)$.  However, as the singularity structure shown in
  Fig.~\ref{fg:sings-Z1F0} illustrates the correct leading
  contribution should be instead $\exp(-\frac{\CV_{\IF_0}}{g_s})$.}
We want to point out that this in fact provides a very efficient way
to compute the series $\Phi(g_s)$, and we are able to compute 400 terms
of $\Phi(g_s)$.

Next, we demonstrate that the integral \eqref{eq:F0intxi0} can be
evaluated explicitly by closing the contour from above and summing up
residues, and show that the result factorises as a sum of products of
holomorphic and anti-holomorphic blocks given by $q$ and $\tq$-series
respectively, where

\begin{equation}
  q = \re^{2\pi\ri\bb^2},\quad \tq = \re^{-2\pi\ri \bb^{-2}}.
\end{equation}

Note the definition of $q$ here is consistent with \eqref{eq:q-gs}.
Throughout the section we will assume that $\imag\bb^2 > 0$ so that
$|q| , |\tq|<1$ and the $q$,$\tq$-series converge.

It turns out it is more convenient to first evaluate the integral
\eqref{eq:F0intxi} when $\xi \not=0$, as the integrand of
\eqref{eq:F0intxi} has only simple poles, and then to evaluate the
limit $\xi \rightarrow 0$. We assume that $\xi$ is small and since
$\real \bb >0$, the poles in the upper half plane are
\begin{equation}
  \pm\frac{\bb\xi}{2\pi} -\frac{\ri\bb}{4} + c_\bb +\ri r \bb +\ri
  s\bb^{-1},\quad r,s = 0,1,2,\ldots, 
\end{equation}

where $c_\bb$ is defined in (\ref{defcb}). 
The residues at these poles can be computed using \eqref{eq:fad-res}, and by summing
them up we find

\begin{equation}
  \tr\rho_{\IF_0} = -\frac{1}{2}\re^{-\bb^2\xi/2}q^{1/8}
  \frac{(q;q)_\infty^2(-\tq \re^{2\xi};\tq)_\infty
    (-\tq\re^{-2\xi};\tq)_\infty}
  {(q^{1/2};q)_\infty^2(\tq\re^{2\xi};\tq)_\infty
    (\tq\re^{-2\xi};\tq)_\infty}
  \coth(\xi)\left(\mc{I}(\xi,\bb) - \mc{I}(-\xi,\bb)\right)
  \label{eq:Z1facxi-F0}
\end{equation}
where
\begin{equation}
  \mc{I}(\xi,\bb) =
  \re^{\bb^2\xi/2}\qhg{2}{1}{q^{1/2},q^{1/2}}{q}{q}{q^{1/2}\re^{2\bb^2\xi}}
  \qhg{2}{1}{-1,-1}{\tq}{\tq}{-\tq\re^{-2\xi}}
\end{equation}

and the $q$-hypergeometric function is defined in (\ref{def-qhyper}). Note that, as we explained in section \ref{tsst-subsec}, 
the holomorphic and the anti-holomorphic factors involve 
very different functions, in contrast to what happens in complex CS theory. 

Before we turn off the mass parameter in the result, we notice that if
we perform the shift $\xi \mapsto \xi+\pi\ri$, the variable $\re^{2\bb^2\xi}$ in $\mc{I}(\xi,\bb)$ transforms by
\begin{equation}
  \re^{2\bb^2\xi} \mapsto q \re^{2\bb^2\xi}
\end{equation}
while the variable $\re^{-2\xi}$ is invariant. This suggests 
to define the ``massive" holomorphic blocks

\begin{subequations}
  \begin{align}
    A(x;q) =
    &x^{1/4}\qhg{2}{1}{q^{1/2},q^{1/2}}{q}{q}{q^{1/2}x},
    \label{eq:Axq}\\
    B(x;q) =
    &x^{-1/4}\qhg{2}{1}{q^{1/2},q^{1/2}}{q}{q}{q^{1/2}x^{-1}}\\ =
    &x^{-1/4}\frac{(q^{1/2};q)_\infty(q x^{-1};q)_\infty}
      {(q;q)_\infty(q^{1/2}x^{-1};q)_\infty}
      \qhg{2}{1}{q^{1/2},q^{1/2}x^{-1}}{qx^{-1}}{q}{q^{1/2}},
      \label{eq:Bxq}
  \end{align}
\end{subequations}
and ``massive" anti-holomorphic blocks
\begin{subequations}
  \begin{align}
    &\wt{A}(\tx;\tq) = \qhg{2}{1}{-1,-1}{\tq}{\tq}{-\tq\tx^{-1}},\\
    &\wt{B}(\tx;\tq) = \wt{A}(\tx^{-1};\tq),
  \end{align}
\end{subequations}
where
\begin{equation}
  x = \re^{2\bb^2\xi},\quad \tx = \re^{2\xi}.
\end{equation}




The second expression of $B(x;q)$ is obtained by applying Heine's
transformation (\ref{heine}). Both holomorphic blocks satisfy the difference
equation
\begin{equation}
  (-1+q^{3/2}x)f(q^2x;q) +q^{1/4}(2-qx)f(qx;q) +
  q^{1/2}(-1+q^{1/2}x)f(x;q) = 0.
\end{equation}
The Wronskian
\begin{equation}
  W(x;q) =
  \det\begin{pmatrix}
    A(x;q) & B(x;q) \\
    A(qx;q) & B(qx;q)
  \end{pmatrix}
\end{equation}
can be identified as
\begin{equation}
  W(x;q) = q^{-1/4}
  \frac{(q^{1/2};q)_\infty^2(qx;q)_\infty(x^{-1};q)_\infty}
  {(q;q)_\infty^2(q^{1/2}x;q)_\infty(q^{-1/2}x^{-1};q)_\infty}
  \label{eq:W-F0}
\end{equation}







We now take the massless limit $x\mapsto 1$.  We find that

\begin{subequations}
\label{ABdescendants}
\begin{align}
  A(q^m\re^{u};q) =
  &g_m(q)+\frac{1}{4}G_m(q) u + \CO(u^2),\\
  B(q^m\re^{u};q) =
  &h_m(q)-\frac{1}{4}H_m(q) u + \CO(u^2),
\end{align}
\end{subequations}

where

\begin{subequations}
\begin{align}
  g_m(q) =
  &q^{m/4}\sum_{n=0}^\infty
    \frac{(q^{1/2};q)_n^2}{(q;q)_n^2}q^{n/2+nm},\quad m\geq 0,\\
  G_m(q) =
  &q^{m/4}\sum_{n=0}^\infty
    \frac{(q^{1/2};q)_n^2}{(q;q)_n^2}q^{n/2+nm}(1+4n),\quad m\geq 0,
\end{align}
\end{subequations}

as well as

\begin{subequations}
\begin{align}
  h_m(q) =
  &q^{m/4}\sum_{n=0}^\infty
    \frac{(q^{1/2};q)_{n+m}(q^{1/2};q)_n}{(q;q)_{n+m}(q;q)_n}q^{n/2},
  \qquad\qquad m\geq 0,\\
  H_m(q) =
  &-4q^{-m/4}\sum_{n=0}^{m-1}
    \frac{(q^{1/2};q)_n(q^{-1};q^{-1})_{m-n-1}}
    {(q;q)_n(q^{-1/2};q^{-1})_{m-n}}q^{n/2}\qquad\qquad m \geq 0\nn
  &+q^{m/4}\sum_{n=0}^\infty
    \frac{(q^{1/2};q)_{n+m}(q^{1/2};q)_n}{(q;q)_{n+m}(q;q)_n}
    q^{n/2}\left(1-4\sum_{j=1}^\infty\left(
    \frac{q^{j+n}}{1-q^{j+n}} - \frac{q^{j-1/2+n}}{1-q^{j-1/2+n}}
    \right)\right).
\end{align}
\end{subequations}
We comment that when expanding $B(q^m\re^u;q)$ we need to use the
second expression of $B(x;q)$ in \eqref{eq:Bxq}, since in the first expression of $B(q^m\re^u;q)$ with
$m\geq 1$, the power of $q$ is not bounded from below. In addition, we find by explicit $q$-expansion that

\begin{equation}
  h_m(q) = g_m(q),\quad G_0(q) = H_0(q).
\end{equation}

The series $g_m(q)$, $G_m(q)$, $h_m(q)$ and $H_m(q)$ in (\ref{ABdescendants}) with $m>0$ are the analogues of the ``descendants" 
introduced in \cite{ggm1,ggm2}. As we will see, although they do not appear in the expression for the spectral trace, they are necessary to 
reconstruct the Stokes data. 




For the anti-holomorphic block we find the expansion 
\begin{equation}
  \wt{A}(\re^{\tilde{u}};\tq) = 2\tilde{g}_0(\tq) + 4\tilde{u}\,
  \tilde{G}_0(\tq) + \CO(\tilde{u}^2),
\end{equation}
where
\begin{subequations}
  \begin{align}
    \tilde{g}_0(\tq) =
    &\frac{1}{2}
      \sum_{n=0}^\infty\frac{(-1;\tq)_n^2}{(\tq;\tq)_n^2}(-\tq)^n,\\
    \tilde{G}_0(\tq) =
    &-\frac{1}{4}\sum_{n=0}^\infty\frac{(-1;\tq)_n^2}{(\tq;\tq)_n^2}(-\tq)^nn.
  \end{align}
\end{subequations}

As an application of these results, we can take the massless limit of
the factorisation formula \eqref{eq:Z1facxi-F0} and find
\begin{equation}
  \tr\rho_{\IF_0} = -\frac{\ri}{2}
  \left(G_0(q) \wt{g}_0(\tq) +8\bb^{-2} g_0(q) \wt{G}_0(\tq) \right).
  \label{eq:Z1fac0-F0}
\end{equation}

Note that this is very similar to the factorization in holomorphic blocks of the state integral invariant 
of the figure-eight knot in \cite{GK-qseries}. However, as noted above, the factorization is not 
symmetric, and the holomorphic and anti-holomorphic blocks are given by different series. 
Another important result is that in the massless limit the Wronskian
identity \eqref{eq:W-F0} implies that
\begin{equation}
  g_0(G_1+H_1) - 2g_1 G_0 = \frac{4q^{1/4}}{1-q^{1/2}}.
  \label{eq:W-id}
\end{equation}
