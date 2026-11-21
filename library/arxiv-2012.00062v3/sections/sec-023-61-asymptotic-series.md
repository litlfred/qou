---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-023-61-asymptotic-series
section_title: "Asymptotic series"
section_number: 6.1
pages: 45-47
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.713
latex_coverage_ratio: 0.714
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.41asy}

Our starting point will be the state-integral for the $\knot{4}_1$
knot~\cite[Eqn.38]{AK} (after removing a prefactor that depends on $u$
alone)
\begin{equation}
  \label{Z41x}
  Z_{\knot{4}_1}(u;\tau) =
  \re^{-2 \pi \ri u^2} \int_{\BR+\ri 0}  \Phi_\bb(v) \, \Phi_\bb(u+v)
  \, \re^{-\pi \ri (v^2+4uv)} \rd v \,.
\end{equation}
The above state-integral (and all the subsequent ones) is a
holomorphic function of $\tau \in \BC'$ and $u$ when
$|\Im(u)| < |\bb+\bb^{-1}|/2$ and extends to an entire function of
$u$ (see Theorem~\ref{thm.41a} below).

After a change of variables $u \mapsto u/(2\pi \bb)$ (see
Equation~\eqref{ub}) and $v \mapsto v/(2\pi\bb)$ 
the asymptotic expansion of the quantum dilogarithm (see for
instance~\cite[Prop.6]{AK}) implies that the
integrand of $Z_{\knot{4}_1}(\ub;\tau)$ has a leading term given by
$\re^{V(u,v)/(2 \pi \ri \tau)}$ where
\begin{equation}
  \label{V41}
  V(u,v) = \Li_2(-\re^{v}) + \Li_2(-\re^{u+v})
  + \frac{1}{2} (v)^2 + 2 u v \,.
\end{equation}
Taking derivative with respect to $v$ gives the equation for the
critical point
\begin{equation}
  \label{41crit}
  2 u + v - \log(1+\re^{v}) -\log(1+\re^{u+v})=0
\end{equation}
which implies that $(x,y)=(e^u,-e^v)$ is a complex point 
points of the affine curve $S$ given by
\begin{equation}
  \label{41critb}
  S : -x^2 y = (1-y)(1- x y) 
\end{equation}
and $(u, v)$ is a point of the exponentiated curve $S^*$ given by
the above equation where $(x,y)=(\re^{u},-\re^{v})$.  Moreover, we
have
\begin{equation}
  \label{V41b}
  V(u,v) = \Li_2(y)+\Li_2(xy) +\frac{1}{2} (\log (-y))^2 + 2 \log x \log(-y) \,.
\end{equation}
Note that~\eqref{41crit} has more information than~\eqref{41critb}
since it chooses the logarithms of $1+\re^{v}$ and $1+\re^{u+v}$
such that~\eqref{41crit} holds. This ultimately implies that $V$ is a
holomorphic $\BC/2\pi^2\BZ$-valued function on the exponentiated curve
$S^*$. Note that when $u=0$, Equation~\eqref{41critb}
becomes~\eqref{41xi}.

The constant term of the asymptotic expansion is given by the Hessian
of $V(u,v)$ at a critical point $(u,v)$, and it is a rational
function of $x$ and $y$ is given by
\begin{equation}
  \label{41delta}
  \delta(x,y) = -\frac{1-xy^2}{x^2y} \,.
\end{equation}
Note that $\delta(x,y)=0$ on $S$ if and only if $x$ is a root of the
discriminant of $S$ with respect to $y$, i.e.,
\begin{equation}
  (1 - 3 x + x^2) (1 + x + x^2)=0.
  \label{disc41y}
\end{equation}
In other words, $\delta$ vanishes precisely when two branches of
$y=y(x)$ coincide.

Beyond the leading asymptotic expansion and its constant term, the
asymptotic series has the form $\Phi(x,y;\tau)$ where 
\begin{equation}
  \label{Phi41}
  \Phi(x,y;\tau)=\exp\left( { V(u,v) \over 2\pi\ri \tau} \right)
  \varphi(x,y;\tau),
  \qquad 
  \varphi(x,y;\tau) \in \frac{1}{\sqrt{\ri\delta}}
  \BQ[x^\pm,y^\pm,\delta^{-1}] [[2 \pi \ri \tau]]
\end{equation}
where $\delta$ is given in~\eqref{41delta} and
$\sqrt{\ri \delta} \, \varphi(x,y;0)=1$.  In other words, the
coefficient of every power of $2\pi \ri \tau$ in
$\sqrt{\delta} \, \varphi(x,y;\tau)$ is a rational function on
$S$. There is a natural projection $S \to \BC^*$ given by
$(x,y) \rightarrow x$ and we denote by $y_\s(x)$ the choice of a local
section (an algebraic function of $x$), for
$\s \in \calP=\{\s_1,\s_2\}$.  We denote the corresponding series
$\Phi(x,y_\s(x);\tau)$ simply by $\Phi_\s(x;\tau)$.
Note that
\begin{equation}
  \delta(x,y_{1,2}(x)) = \pm\frac{\sqrt{(1-x-x^{-1})^2-4}}{x}
  \label{eq:delta-41}
\end{equation}
and that the two series are related by
\begin{equation}
\label{Phi4112}
\Phi_2(x;\tau) = \ri \Phi_1(x;-\tau) \,.
\end{equation}
The power series $\sqrt{\ri\delta}\varphi_\s(x;\tau)$ can be computed
by applying Gaussian expansion to the state-integral \eqref{Z41x}. One
can compute up to 20 terms in a few minutes, and
the first few terms agree with an independent computation using the
WKB method (see \cite[Eqn.(4.39)]{DGLZ} as well as
\cite{GG:asymptotics}), and given by $\sqrt{\ri\delta}\varphi_\s(x;\tau)$

\begin{align}
  &\sqrt{\ri\delta}\varphi_{1,2}\left(x;\frac{\tau}{2\pi\ri}\right)\nn =
  &1 - \frac{1}{24\gamma_{1,2}^3(x)}\big(x^{-3} - x^{-2} - 2 x^{-1} + 15 -
    2 x - x^2 + x^3\big) \tau\nn+
  &\frac{1}{1152\gamma_{1,2}^6(x)}
    \big(x^{-6} - 2 x^{-5} - 3 x^{-4} + 610 x^{-3} - 
    606 x^{-2} - 1210 x^{-1} + 3117\nn
  &\phantom{=====}- 1210 x - 606 x^2 + 610 x^3 - 
    3 x^4 - 2 x^5 + x^6\big) \tau^2 +\cO(\tau^3),
    \label{eq:vf-41}
\end{align}
where
\begin{equation}
  \gamma_{1,2}(x) = x\delta(x,y_{1,2}(x)) = \pm\sqrt{x^{-2}-2x^{-1}-1-2x+x^2}.
\end{equation}
On the other hand, if one sets $x$ to numerical values, one can
compute 300 terms of this power series.
