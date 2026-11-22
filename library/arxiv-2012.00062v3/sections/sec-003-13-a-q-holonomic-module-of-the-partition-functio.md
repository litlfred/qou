---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-003-13-a-q-holonomic-module-of-the-partition-functio
section_title: "A q-holonomic module of the partition function and its descendants"
section_number: 1.3
pages: 4-6
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.966
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.results}

In this section we discuss a $q$-holonomic module associated to the
partition function and its descendants. This module and its
fundamental solutions are crucial to our exact computation of the
Stokes matrices in Section~\ref{sub.pert} below. One advantage of
introducing this module before we discuss resurgence of perturbative
series is that the former has been established mathematically in many
cases, whereas the latter remains a mathematical challenge.

We begin our discussion with a factorization of the state-integral
\begin{equation}
  \label{Zfacx}
  Z_M(\ub;\tau) = B(\tx,\tq^{-1})^T \Delta(\tau) B(x;q),
  \qquad (\tau \in \BC\setminus\BR)
\end{equation}
where
\begin{equation}
  \label{ub}
  \ub = \frac{u}{2\pi \bb} \,
\end{equation}
(this rescaling is dictated by the asymptotics of Faddeev's quantum
dilogarithm), $\Delta(\tau)$ is a diagonal matrix with diagonal
entries a 24-th root of unity times an integer power of
$\re^{\frac{\pi \ri}{24}(\tau+\tau^{-1})}$, 
$B(x;q)=(B^{(j)}(x;q))_{j=1}^r$ is a vector of holomorphic blocks, and
\begin{equation}
  \label{xq}
  q=\re^{2\pi \ri \tau}, \qquad \tq= \re^{-2 \pi \ri/\tau}, \qquad
  x=\re^{u}, \qquad \tx = \re^{u/\tau}, \qquad \tau=\bb^2 \,.


\end{equation}
The above notation is consistent with the literature in modular forms
and Jacobi forms~\cite{EZ} and indicates that $u \in \BC$ can be thought of
as a Jacobi variable. The
factorization~\eqref{Zfacx} was first noted in a related context in
\cite{pas} and further developed in complex Chern--Simons theory
in~\cite{Beem,dimofte-state}. We find that this factorization persists
to descendant state-integrals parametrized by a pair of (Jacobi-like)
variables $m$ and $\mu$ (see Equations \eqref{Z41x-desc} and
\eqref{Z52x-desc} for the definition of descendant state-integrals for
the knots $\knot{4}_1$, $\knot{5}_2$) 

\begin{equation}
  \label{ZM-desc}
  Z_{M,m,\mu}(\ub;\tau) 
  =
  (-1)^{m+\mu} q^{m/2}\tq^{\mu/2} B_{-\mu}(\tx;\tq^{-1})^T
  \Delta(\tau) B_m(x;q), \qquad (m, \mu \in \BZ)
\end{equation}
where $Z_{M,0,0}=Z_M$. The holomorphic blocks determine a matrix
$W_m(x;q)$ defined by
\begin{equation}
  \label{Wm}
  W_m(x;q) =
  \begin{pmatrix}
    B^{(1)}_{m}(x;q) & \ldots & B^{(r)}_{m}(x;q) \\
    \vdots & & \vdots \\
    B^{(1)}_{m+r-1}(x;q) & \ldots & B^{(r)}_{m+r-1}(x;q)
  \end{pmatrix}
\end{equation}
with the following properties

\begin{itemize}
\item[(a)] The entries of $W_m(x;q)$ are holomorphic functions of
  $|q| \neq 1$, meromorphic functions of $x \in \BC^*$ with poles in
  $x \in q^\BZ$ of order at most $r$, and have Taylor series
  expansions in $(1-x)^{-r}\BZ[x^\pm][[q^{\frac{1}{2}}]]$ whose
  monomials $x^k q^{n/2}$ satisfy $n= O(k^2)$.
\end{itemize}
In other words, the support of the monomials in $x$ and $q$
in $(1-x)^r W_m(x;q)$ is similar to the one of Jacobi forms (in their
holomorphic version of Eichler-Zagier~\cite[Eqn.(3)]{EZ} or the
meromorphic version from Zweger's thesis~\cite[Chpt.3]{Zwegers:thesis})
and of the admissible functions of Kontsevich-Soibelman~\cite{KS}.

\begin{itemize}
\item[(b)] The matrix 
  \begin{equation}
    \label{Zfacx-desc}
    W_{m,\mu}(u;\tau) =
    W_{-\mu}(\tx;\tq^{-1}) \Delta(\tau) W_{m}(x;q)^T
  \end{equation}
  defined for $\tau=\BC\setminus\BR$, extends to a holomorphic
  function of $\tau \in \BC'$ and $u \in \BC$ for
  all integers $m$ and $\mu$.
\end{itemize}
More precisely, if we define the normalized descendant integral
\begin{equation}
  \label{Zr}
  z_{M,m,\mu}(u;\tau) =
  (-1)^{m+\mu}q^{-m/2}\tq^{-\mu/2}
  Z_{M,m,\mu}(u;\tau) \,,
\end{equation}
then $W_{m,\mu}(u;\tau) =(z_{m+i,\mu+j}(\ub;\tau))_{i,j=0}^{r-1}$.
The above statement is remarkable in two ways: (i) $W_m(x;q)$ is a
holomorphic function of $\tau \in \BC\setminus\BR$ that cannot be
extended holomorphically over the positive reals, yet
$W_{m,\mu}(u;\tau)$ holomorphically extends over the positive reals
and (ii) $W_m(x;q)$ is a meromorphic function of $u$ with
singularities, yet $W_{m,\mu}(u;\tau)$ is an entire function of $u$.
Property (ii) is common in quantum mechanics, where the wave-function
is often entire whereas its WKB expansion is singular at the turning
points. The same behavior is also observed in the case of open topological
strings in~\cite{Marino:exact}.












\begin{itemize}
\item[(c)] We have an orthogonality relation
  \begin{equation}
    \label{Wortho}
    W_{-1}(x;q) \, W_{-1}(x;q^{-1})^T \in \GL(r,\BZ[x^\pm]) \,.
  \end{equation}
\item[(d)] The columns of $W_m(x;q)$, as functions of $(x,m)$, form a
  $q$-holonomic module of rank $r$.
\end{itemize}
The factorization~\eqref{ZM-desc} and (d) implies that the
annihilator $\calI_M$ of $z_{M,m,\mu}(\ub;\tau)$ as a function of
$(x,m)$ coincides with the annihilator of $W_m(x;q)$.  The latter is a
left ideal in the Weyl algebra $\calW$ over $\BQ[q^\pm]$ generated by
the pairs $(S_x,x)$ and $(S_m,q^m)$ of $q$-commuting operators which
act on a function $f(x,m;q)$ by
\begin{align}
  (S_x f)(x,m;q) &= f(qx,m;q) & (x f)(x,m;q) &= xf(x,m;q) \\
  (S_m f)(x,m;q) &= f(x,m+1;q) & (q^m f)(x,m;q) &= q^m f(x,m;q) \,.
\end{align}
Properties (a)-(d) above define meromoprhic quantum Jacobi forms, a
concept which is further studied in~\cite{GMZ}.  Although the above
statements are largely conjectural for the partition function of
complex Chern--Simons theory, we have the following result (see
Theorems~\ref{thm.41a}, \ref{thm.41b}, \ref{thm.52a}, \ref{thm.52b}
below).
  
\begin{theorem}
  \label{thm.4152W}
  The above statements hold for the $\knot{4}_1$ and $\knot{5}_2$
  knots.
\end{theorem}

We also study the Taylor series expansion of
Equations~\eqref{ZM-desc}, \eqref{Zfacx-desc} and~\eqref{Wortho} at
$u=0$ noting that the left hand side of the above equations are entire
functions of $u$ whereas the right hand side are a priori meromorphic
functions of $u$ with a pole of order $r$ at zero.  More precisely, in
Sections~\ref{sub.41x=1} and~\ref{sub.52x=1} we prove the following.
    
\begin{theorem}
  \label{thm.Zu=0}
  For the $\knot{4}_1$ and $\knot{5}_2$ knots,
  Equations~\eqref{ZM-desc}, \eqref{Zfacx-desc} and~\eqref{Wortho} can
  be expanded in Taylor series at $u=0$ whose constant terms are
  expressed in terms of the $q$-series of~\cite{GGM:resurgent}.
\end{theorem}
