---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-019-55-the-borel-resummations-of-the-asymptotic-seri
section_title: "The Borel resummations of the asymptotic series"
section_number: 5.5
pages: 39-41
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.768
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.borel41}

In this section we explain how Conjecture~\ref{conj.41M} identifies the
Borel resummations of the factorially divergent series $\Phi(x;\tau)$
with the descendant state-integrals, thus lifting the Borel resummation
to holomorphic functions on the cut-plane $\BC'$. This is
interesting theoretically, but also practically in the numerical
computation of Borel resummations.

After multiplying the inverse of $M_R(\tx,\tq)$ from the left
on both sides of \eqref{abrelx}, we can also express the Borel sums
$s_R(\Phi)(x;\tau)$ in each region in terms of holomorphic functions
of $\tau \in \IC\backslash \IR$ as follows

\begin{corollary}(of Conjecture~\ref{conj.41M})
  \label{cor.41borel}
  We have
\begin{subequations}
\begin{align}
  s_{I}(\Phi)(x;\tau) =
  &\begin{pmatrix}
    -\tx&1+\tx^{-1}\\0&1
  \end{pmatrix} W_{-1}(\tx;\tq^{-1})\Delta(\tau)B(x;q)\,,
                        \label{eq:HU1-41}\\
  s_{II}(\Phi)(x;\tau) =
  &\begin{pmatrix}
    0&-\tx\\1&-\tx-\tx^2
  \end{pmatrix} W_{-1}(\tx^{-1};\tq^{-1})
               \begin{pmatrix}
                 1&0\\0&-1
               \end{pmatrix}\Delta(\tau) B(x;q)\,,
                         \label{eq:HU2-41}\\
  s_{III}(\Phi)(x;\tau) =
  &\begin{pmatrix}
    0&-\tx\\1&1   
  \end{pmatrix} W_{-1}(\tx^{-1};\tq^{-1})
               \begin{pmatrix}
                 1&0\\0&-1
               \end{pmatrix}\Delta(\tau) B(x;q)\,,
                         \label{eq:HU3-41}\\
  s_{IV}(\Phi)(x;\tau)=
  &\begin{pmatrix}
    -\tx&-\tx\\0&1   
  \end{pmatrix}W_{-1}(\tx,\tq^{-1})\Delta(\tau) B(x;q)\,.
                  \label{eq:HU4-41}
\end{align}
\end{subequations}
where the right hand side of~\eqref{eq:HU1-41}--\eqref{eq:HU4-41} are
holomorphic functions of $\tau \in \IC'$, as they are linear
combinations of the descendants \eqref{41x-desc-fac}.
\end{corollary}

The asymptotic series of the $\knot{4}_1$ knot have the
symmetry~\eqref{Phi4112} due to the fact that it is an amphichiral
knot. This gives a symmetry of the state-integral.

\begin{proposition}
  \label{prop.Z41uu}
  (Assuming Conjecture~\ref{conj.41M}) We have:
  \begin{equation}
  \label{Z41uu}
  Z_{\knot{4}_1}(u;\tau) = e^{2\pi (\bb+\bb^{-1})u}
  Z_{\knot{4}_1}(-u;\tau) \,.
  \end{equation}
\end{proposition}

\begin{proof}
  The second line of~\eqref{eq:HU1-41} indicates that in region $I$
\begin{equation}
  Z_{\knot{4}_1}(u;\tau) = s_I(\Phi_2)(x;\tau).
\end{equation}
Recall the structure of $\Phi_2(x;\tau)$ from \eqref{Phi41}
\begin{equation}
  \Phi_2(x;\tau) = \exp\left(\frac{V(x,y_2(x))}{2\pi\ri\tau}\right)
  \frac{1}{\sqrt{\ri\delta(x,y_2(x))}}
  \sqrt{\ri\delta}\varphi(x,y_2(x);\tau).
\end{equation}
Here
$\sqrt{\ri\delta}\varphi_2(x;\tau):=\sqrt{\ri\delta}\varphi(x,y_2(x);\tau)$
is an asymptotic series in $\tau$ with
$\sqrt{\ri\delta}\varphi_2(x;0)=1$.  The coefficients of the series
$\sqrt{\ri\delta}\varphi_2(x;\tau)$ are invariant under the
transformation $x\mapsto 1/x$ (see for instance \eqref{eq:vf-41}; this
is also true for
$\sqrt{\ri\delta}\varphi_1(x;\tau) =
\sqrt{\ri\delta}\varphi(x,y_1(x);\tau)$), and thus
\begin{equation}
  s(\sqrt{\ri\delta} \varphi_2)(1/x;\tau) = s(\sqrt{\ri\delta}
  \varphi_2)(x;\tau).
  \label{eq:-xphi}
\end{equation}
On the other hand, from definition \eqref{eq:delta-41} of
$\delta_2(x):=\delta(x,y_2(x))$, it is clear that
\begin{equation}
  \delta_2(1/x) = x^2\delta_2(x).
  \label{eq:-xdelta}
\end{equation}
Finally, to study the behavior of $V_2(x):=V(x,y_2(x))$ under the
transformation $x\mapsto 1/x$, it is convenient to do the change of
variables $y = x^{-1}+\ty$, so that the Equation~\eqref{41critb}
satisfied by $y$ becomes
\begin{equation}
  1-(1-x-x^{-1})\ty+\ty^2 = 0
\end{equation}
which is manifestly invariant under this transformation, and thus
$\ty(1/x) = \ty(x)$.
Expressed in terms of this variable
\begin{align}
  V_2(x) =
  &-\Li_2(-x^{-1}\ty_2)-\Li_2(-x \ty_2) -\frac{\pi}{3}
    -\frac{1}{2}\log^2(x\ty_2^{-1})\nn
  &+\log(1+x \ty_2^{-1})\log(-x\ty_2^{-1})
    -\log(1+x\ty_2)\log(-x\ty_2)\nn
  &-\frac{1}{2}\log^2(-1-x\ty_2^{-1})
    +\frac{1}{2}\log^2(-x^{-1}-\ty_2)
    +2\log x \log(-x^{-1}-\ty_2),
\end{align}
and it has the property that
\begin{equation}
  V_2(x^{-1}) = V_2(x) - 2\pi\ri x
  \label{eq:-xV}
\end{equation}
This can be proven by differentiating both sides with respect to $x$,
and reducing it to an identity of rational functions on the curve $S$.
Combining \eqref{eq:-xphi},\eqref{eq:-xdelta},\eqref{eq:-xV}, we have
\begin{equation}
  s_I(\Phi_2)(x^{-1};\tau) = x^{-1}\tx^{-1} s_I(\Phi_2)(x;\tau)
  \label{eq:-xPhi}
\end{equation}
which implies~\eqref{Z41uu}. We comment in the passing that the
identity~\eqref{eq:-xPhi} is true for both
$s(\Phi_{1,2})(x;\tau)$ for any $\tau\in\IC$ whenever the asymptotic
series is Borel summable.

Once we have established the identity \eqref{Z41uu} in region $I$, it
can be extended to $\tau\in\IC'$ by the holomorphicity of
\eqref{41x-desc-fac}.
\end{proof}
