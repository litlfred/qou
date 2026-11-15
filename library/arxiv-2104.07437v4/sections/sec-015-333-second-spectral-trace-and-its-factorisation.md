---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-015-333-second-spectral-trace-and-its-factorisation
section_title: "Second spectral trace and its factorisation"
section_number: 3.3.3
pages: 34-38
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.99
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
\label{sc:block-P2}

The TS/ST correspondence allows us to write down an integral
representation of the second trace. In principle the second bosonic
trace $\tr\rho_{\IP^2}^2$ involves a double integral of a product of
the integral kernel \eqref{eq:iker-P2}, but it was shown in
\cite{kama} that it can be converted into a
one-dimensional integral.  Using the result of the first trace
\eqref{eq:tr1-P2}, this translates into the following integral
representation of the normalised second trace

\begin{equation}
  \tr' \rho_{\IP^2}^2 =
  \sqrt{3}\bb\frac{\fad(-\frac{\ri\bb}{6}-\frac{\ri\bb^{-1}}{2})^2}
  {\fad(\frac{\ri\bb}{6}+\frac{\ri\bb^{-1}}{2})^2}
  \int_{\IR}\frac{\sinh(2\pi h x)}{\sinh(\pi\bb x)}
  \frac{\Phi_\bb(x-\frac{\ri\bb}{3}+c_\bb)^2}
  {\Phi_\bb(x+\frac{\ri\bb}{3}-c_\bb)^2}
  \re^{2\pi x(\frac{1}{3}\bb+\bb^{-1})}\rd x.
  \label{eq:tr2-P2}
\end{equation}











In order to perform the large $\bb$ expansion of the integral
\eqref{eq:tr2-P2}, one can first do the scaling
$x\rightarrow \bb^{-1}x$ and then use the formula of semi-classical
expansion of the quantum dilogarithm \eqref{as-fd2} for large $\bb$
(or equivalently \eqref{as-fd} for small $\bb_D = 1/\bb$).






After evaluating convergent integrals
\begin{equation}
  \int_{\IR} \frac{\sinh(\frac{1}{3}\pi x)}{\sinh(\pi x)} x^{2n}\rd x
  = \frac{2(-1)^{n-1}}{2n+1}B_{2n+1}(\tfrac{1}{3})3^{2n+1/2},
  \quad n=0,1,2,\ldots,
\end{equation}
one finds that






\begin{equation}
  \tr'\rho_{\IP^2}^2 \sim \Phi_{0;2}(g_s) = 1+ \frac{8\pi^2}{9\sqrt{3}}g_s +
  \frac{16\pi^4}{81}g_s^2 + \ldots,\quad
  g_s=-\frac{3}{2\pi}\bb^{-2}\rightarrow 0,
  \label{eq:tr2asymp-P2}
\end{equation}
justifying the prediction
\eqref{eq:NPhi2}

of the TS/ST correspondence.










Using the technique explained in Appendix~\ref{sc:fastZ2}, we are able to
compute 700 terms of this series, which allows us to perform in detail the resurgence
analysis.

The integral form \eqref{eq:tr2-P2} of the normalised second trace can
be evaluated explicitly by closing the contour of integral from above
and summing up residues of poles.  Following the exercise in
Section~\ref{sc:block-F0}, it is helpful to introduce artificially a
``mass'' deformation of the integral so that the integrand only has
simple poles, and then turn off the mass deformation.

We consider the following integral
\begin{equation}
  I(\xi,\bb) =  \int_\IR
  \frac{\sinh(2\pi h x)}{\sinh(\pi\bb x)}
  \frac{\Phi_\bb(x+\frac{\xi\bb}{2\pi}-2\ri a+c_\bb)
    \Phi_\bb(x-\frac{\xi\bb}{2\pi}-2\ri a + c_\bb)}
  {\Phi_\bb(x+\frac{\xi\bb}{2\pi}+2\ri a -c_\bb)
    \Phi_\bb(x-\frac{\xi\bb}{2\pi}+2\ri a-c_\bb)}
  \re^{2\pi x(\frac{1}{3}\bb+\bb^{-1})}\rd x.
\end{equation}
We only consider the case $\xi$ is small and $\imag\bb^2>0$.  Since
$\real \bb >0$, the poles in the upper half plane are
\begin{equation}
  \ri\bb^{-1}k, \quad \pm\frac{\xi\bb}{2\pi}+2\ri a+\ri r \bb +\ri s
  \bb^{-1},\quad k = 1,2,3,\ldots,\;r,s = 0,1,2,3,\ldots
\end{equation}

After summing up the residues at these poles, by using \eqref{eq:fad-res}, we
arrive at

\begin{align}
  I(\xi,\bb) =
  &\ri\bb^{-1}h_0(x,q)\tilde{h}_0(\tx,\tq) \nn+
  &\ri\bb \,w_a^{-1}\Big(h^+_1(x,q)\tilde{h}^+_1(\tx,\tq)
    -h^+_2(x,q)\tilde{h}^+_2(\tx,\tq)\nn
  &\phantom{=====}+h^-_1(x,q)\tilde{h}^-_1(\tx,\tq)
    -h^-_2(x,q)\tilde{h}^-_2(\tx,\tq)
    \Big),
    \label{eq:mass-fac}
\end{align}
where we defined

\begin{equation}
  x := \re^{\xi\bb^2},\quad \tx:= \re^{\xi}.
\end{equation}
The holomorphic blocks are
\begin{subequations}
\begin{align}
  h_0(x,q) =
  &\frac{(q^{2/3}x;q)_\infty(q^{2/3}x^{-1};q)_\infty}
    {(q^{1/3}x;q)_\infty(q^{1/3}x^{-1};q)_\infty},\\
  h^+_1(x,q) =
  &q^{1/3}x\frac{(q;q)_\infty}{(q^{2/3};q)_\infty}
    \frac{(qx^2;q)_\infty(q^{4/3}x;q)_\infty}
    {(q^{2/3}x^2;q)_\infty(q^{1/3}x;q)_\infty}
    \qhg{3}{2}{q^{2/3},q^{2/3}x^2,q^{1/3}x}{qx^2,q^{4/3}x}{q}{q},\\
  h^+_2(x,q) =
  &q^{2/9}x^{2/3}\frac{(q;q)_\infty}{(q^{2/3};q)_\infty}
    \frac{(qx^2;q)_\infty(q^{4/3}x;q)_\infty}
    {(q^{2/3}x^2;q)_\infty(q^{1/3}x;q)_\infty}
    \qhg{3}{2}{q^{2/3},q^{2/3}x^2,q^{1/3}x}{qx^2,q^{4/3}x}{q}{q^{2/3}},
    \end{align}
    \end{subequations}
  
  as well as
  
  \be h^-_1(x,q) = h^+_1(x^{-1},q),\qquad 
  h^-_2(x,q) = h^+_2(x^{-1},q).
\ee

The anti-holomorphic blocks are

\begin{subequations}
\begin{align}
  \tilde{h}_0(\tx,\tq) =
  &\frac{(\tq w_a^{-1} \tx;\tq)_\infty
    (\tq w_a^{-1}\tx^{-1};\tq)_\infty}
    {(w_a \tx;\tq)_\infty(w_a \tx^{-1};\tq)_\infty} \nn
    &\times 
    \left(
    \qhg{3}{2}{\tq,w_a\tx,w_a\tx^{-1}}
    {\tq w_a^{-1}\tx,\tq  w_a^{-1}\tx^{-1}}{\tq}{\tq w_a^{-1}} -
    \qhg{3}{2}{\tq,w_a\tx,w_a\tx^{-1}}
    {\tq w_a^{-1}\tx,\tq w_a^{-1}\tx^{-1}}{\tq}{\tq} 
    \right),\\
  \tilde{h}^+_1(\tx,\tq) =
  &\tx\frac{(\tq w_a;\tq)_\infty}{(\tq;\tq)_\infty}
    \frac{(\tq w_a\tx^2;\tq)_\infty}{(\tx^2;\tq)_\infty}
    \qhg{2}{1}{w_a^{-1},w_a^{-1}\tx^{-2}}{\tq\tx^{-2}}{\tq}{\tq w_a^{-1}},
  \\
  \tilde{h}^+_2(\tx,\tq) =
  &\tx\frac{(\tq w_a;\tq)_\infty}{(\tq;\tq)_\infty}
    \frac{(\tq w_a\tx^2;\tq)_\infty}{(\tx^2;\tq)_\infty}
    \qhg{2}{1}{w_a^{-1},w_a^{-1}\tx^{-2}}{\tq\tx^{-2}}{\tq}{\tq},
 \end{align}
\end{subequations}

as well as 
  
  \be
  \tilde{h}^-_1(\tx,\tq) =
  \tilde{h}^+_1(\tx^{-1},\tq),\qquad
    \tilde{h}^-_2(\tx,\tq) = \tilde{h}^+_2(\tx^{-1},\tq). 
    \ee
    
In the equations above, 

\begin{equation}
  w_a = \re^{-4\pi\ri a/\bb} = \re^{-2\pi\ri/3}.
\end{equation}


The factorisation formula \eqref{eq:mass-fac} can be further
simplified.  The holomorphic blocks $h_1^+(x,q)$ and $h_2^+(x,q)$ can
also be expressed in terms of $q$-Appell functions, defined in (\ref{def-qappell}), 
\begin{subequations}
  \begin{align}
    h_1^+(x,q) =
    &q^{1/3}x\frac{(q^{5/3};q)_\infty}{(q^{2/3};q)_\infty}
      \Phi^{(1)}(q;q^{1/3},q;q^{5/3};q;q^{2/3}x^2,q^{1/3}x),  \\
    h_2^+(x,q) =
    &q^{2/9}x^{2/3}\frac{(q;q)_\infty(q^{4/3};q)_\infty}
      {(q^{2/3};q)_\infty^2}
      \Phi^{(1)}(q^{2/3};q^{1/3},q;q^{4/3};q;q^{2/3}x^2,q^{1/3}x).
  \end{align}
\end{subequations}
The summand of a $q$-Appell function $\Phi^{(1)}(a;b,b';c;q;x,y)$ is
$q$-holonomic. By using Takayama's algorithm
\cite{Takayama1990:grobner,Takayama1990:algo} of creative telescoping,
implemented in the \texttt{HolonomicFunctions} package of Koutschan
\cite{Koutschan:holofunctions,Koutschan}, we find that
$h_1^+(x,q)$, $h_2^+(x,q)$, together with the remaining three holomorphic
blocks, satisfy a third order linear difference equation
\begin{equation}
  C_3(x;q) h(q^3x;q) + C_2(x;q) h(q^2x;q)+C_1(x;q) h(q x;q)+C_0(x;q)
  h(x;q) = 0,
\end{equation}
where
\begin{align}
  C_3(x;q) =
  &(1- q x) (1+q x) (1-q^{5/3} x)
    (1-q^{8/3} x)^2 (1+q^{8/3} x) (1-q x^2) (1-q^{13/3} x^2),\nn
    C_2(x;q) =
  &-q^{1/3} (1-q^{5/3} x) (1-q^2 x)
    (1+q^2 x) (1-q x^2)\nn
  &\Big(1 + q^{1/3} + q^{2/3} -
    q^{4/3} (1 - q^{1/3} + q^{2/3} + 2 q) x\nn
  &- (1 + q^{1/3}) q^2
    (1 + q -  q^{4/3} + 2 q^2 - 3 q^{7/3} + 2 q^{8/3} + q^{10/3}) x^2\nn
  &+ (1 + q^{1/3}) q^4 (1 + 2 q^{2/3} - 3 q + 2 q^{4/3}
    - q^2 + q^{7/3} + q^{10/3}) x^3\nn
  &+ q^{22/3} (2 + q^{1/3} - q^{2/3} + q) x^4
    - (1 + q^{1/3} + q^{2/3}) q^9 x^5\Big),\nn
    C_1(x;q) =
  &q (1 - q x) (1 + q x) (1 - q^{4/3} x) (1 - q^5 x^2) \nn
  &\Big(
    1 + q^{1/3} + q^{2/3} - 
    q^{4/3} (2 + q^{1/3} - q^{2/3} + q) x \nn
  &- (1 + q^{1/3}) q
    (1 + 2 q^{2/3} - 3 q + 2 q^{4/3} - q^2 + q^{7/3} + q^{10/3})x^2\nn
  &+ (1 + q^{1/3}) q^2 (1 + q - q^{4/3} + 2 q^2 - 3 q^{7/3} + 2 q^{8/3} + 
    q^{10/3}) x^3 \nn
  &+ q^{13/3} (1 - q^{1/3} + q^{2/3} + 2 q) x^4
    - (1 + q^{1/3} + q^{2/3}) q^6 x^5
    \Big),\nn
    C_0(x;q) =
  &-q^2 (1 - q^{1/3} x)^2 (1 + q^{1/3} x) (1 - q^{4/3} x)
    (1 - q^2 x) (1 + q^2 x) (1 - q^{5/3} x^2) (1 - q^5 x^2).
\end{align}
Therefore there are only three linearly independent holomorphic blocks.
By making the ansatz that
\begin{equation}
  h_{i_0}(x,q) =
  f_1(x,q)h_{i_1}(x,q)+f_2(x,q)h_{i_2}(x,q)+f_3(x,q)h_{i_3}(x,q),
\end{equation}
where $h_{i_0}(x,q),h_{i_1}(x,q),h_{i_2}(x,q),h_{i_3}(x,q)$ are any
four holomorphic blocks and the coefficients $f_j(x,q)$ are elliptic
functions satsifying $f_j(qx,q) = f_j(x,q)$, we find
\begin{subequations}
  \begin{align}
    h_2^+(x,q) =
    &-\frac{q^{2/9}(q;q)_\infty^2\theta(-q^{-1/2}x;q)}
      {x^{1/3}\theta(-q^{-1/6};q)_\infty\theta(-q^{-1/6}x;q)}h_0(x,q)\nn
    & -\frac{x^{2/3}\theta(-q^{-1/6}x^2;q)}
      {q^{1/9}\theta(-q^{-1/2}x^2;q)}(h_1^+(x,q)-h_1^-(x,q)),
      \label{eq:h2p-h0h1}\\
    h_2^-(x,q) =
    &-\frac{q^{2/9}x^{1/3}(q;q)_\infty^2\theta(-q^{-1/2}/x;q)}
      {\theta(-q^{-1/6};q)\theta(-q^{-1/6}/x;q)}h_0(x,q)
      \nn
    &+\frac{\theta(-q^{-1/6}/x^2;q)}
      {q^{1/9}x^{2/3}\theta(-q^{-1/2}/x^2;q)}(h_1^+(x,q)-h_1^-(x,q)),
      \label{eq:h2n-h0h1}
  \end{align}
\end{subequations}
where we have used the notation
\begin{equation}
  \theta(x;q) = (-q^{1/2}x;q)_\infty(-q^{1/2}/x;q)_\infty.
\end{equation}
Notice that $h^+_1(x,q)$ and $h^-_1(x,q)$ always appear in these
relations by the combination $h^+_1(x,q) -h^-_1(x,q) $, which is also
true in the factorisation \eqref{eq:mass-fac} once we take into
account the fact that
$\tilde{h}^-_1(\tx,\tq) = -\tilde{h}^+_1(\tx,\tq)$.  We can therefore
write down a simplified factorisation of $I(\xi,\bb)$ by using only two
reduced (anti-)holomorphic blocks

\begin{equation}
  I(\xi,\bb) = \ri\bb^{-1} h_0(x,q) \wt{h}_0^{\text{red}}(\tx,\tq)
  +\ri\bb w_a^{-1} h_1^{\text{red}}(x,q)
  \wt{h}_1^{\text{red}}(\tx,\tq),
\end{equation}

where

\begin{equation}
  h_1^{\text{red}}(x,q) = h_1^+(x,q) - h_1^-(x,q),
\end{equation}

and

\begin{subequations}
  \begin{align}
    \wt{h}_0^{\text{red}}(\tx,\tq) =
    \wt{h}_0(\tx,\tq)
    &+w_a^{-1}\frac{(\tq;\tq)_\infty^2\theta(-\tq^{1/2}\tx;\tq)}
      {\theta(-\tq^{1/2}w_a;\tq)\theta(-\tq^{1/2}w_a^{-1}\tx;\tq)}
      \wt{h}_2^+(\tx,\tq)\nn
    &+w_a^{-1}\frac{(\tq;\tq)_\infty^2\theta(-\tq^{1/2}\tx^{-1};\tq)}
      {\theta(-\tq^{1/2}w_a;\tq)\theta(-\tq^{1/2}w_a^{-1}\tx^{-1};\tq)}
      \wt{h}_2^-(\tx,\tq),\\
    \wt{h}_1^{\text{red}}(\tx,\tq) =
    \wt{h}_1^+(\tx,\tq)
    &-w_a\frac{\theta(-\tq^{1/2}w_a^{-1}\tx^2;\tq)}
      {\theta(-\tq^{1/2}\tx^2;tq)}\wt{h}_2^+(\tx,\tq)\nn
    &+w_a\frac{\theta(-\tq^{1/2}w_a^{-1}\tx^{-2};\tq)}
      {\theta(-\tq^{1/2}\tx^{-2};tq)}\wt{h}_2^-(\tx,\tq).
  \end{align}
\end{subequations}

Finally, taking the massless limit $\xi\rightarrow 0$  and using the relation

\begin{equation}
  \tr' \rho_{\IP^2}^2 =
  \sqrt{3}\bb\frac{\fad(-\frac{\ri\bb}{6}-\frac{\ri\bb^{-1}}{2})^2}
  {\fad(\frac{\ri\bb}{6}+\frac{\ri\bb^{-1}}{2})^2} I(0,\bb),
\end{equation}
we find the following elegant factorisation formula for the normalised
second trace

\begin{align}
  \tr'\rho_{\IP^2}^2=
  \ri\sqrt{3}\left( \wt{H}_0(\tq)
  +3\bb^4  H_1(q)\wt{H}_1(\tq)\right),
  \label{eq:redfac}
\end{align}
where the only non-trivial massless holomorphic block is
\begin{align}
  H_1(q) =
  
  
  
  &q^{1/3}\frac{(q;q)_\infty^4(q^{1/3};q)_\infty^2}
    {(q^{2/3};q)_\infty^5(q^{4/3};q)_\infty}
    \qhg{3}{2}{q^{1/3},q^{2/3},q^{2/3}}{q,q^{4/3}}{q}{q^{2/3}},
    \label{eq:Hred1}
\end{align}
and the massless anti-holomorphic blocks are
\begin{subequations}
  \begin{align}
    \wt{H}_0(\tq) =
    
    
    
    &\qhg{3}{2}{w_a,w_a,\tq}{w_a^{-1}\tq,w_a^{-1}\tq}{\tq}{w_a^{-1}\tq}
      -\qhg{3}{2}{w_a,w_a,\tq}{w_a^{-1}\tq,w_a^{-1}\tq}{\tq}{\tq}\nn
    &+\frac{(\tq;\tq)_\infty^2(\tq w_a;\tq)_\infty^2}
      {(\tq w_a^{-1};\tq)_\infty^4}
      \qhg{2}{1}{w_a^{-1},w_a^{-1}}{\tq}{\tq}{\tq},
      \label{eq:tHred0}\\
    \wt{H}_1(\tq)
    
    
    
    
    
    
    
    
    
    
        =
      &\frac{2(\tq w_a;\tq)^6}{(\tq;\tq)^3(\tq w_a^{-1};\tq)^3}.\qquad
      
      \label{eq:tHred1}
  \end{align}
\end{subequations}

The simple factorisation formula \eqref{eq:redfac} enables us to
rapidly and accurately calculate the value of the normalised second
trace for $g_s$ in the upper half plane. Through a high precision
numerical calculation we find the following relationship between the
normalised second trace and the Borel resummation of
$\Phi_{0;2}(g_s), \Phi_{1;2}(g_s)$.
\begin{itemize}
\item For $g_s$ in sector $II$
  \begin{equation}
    \tr'\rho_{\IP^2}^2 = s_{II}(\Phi_{0;2})(g_s),
    \label{eq:hlift-P2}
  \end{equation}
  thus $\tr'\rho_{\IP^2}^2(\bb)$ furnishes a holomorphic lift of
  $s_{II}(\Phi_{0;2})(g_s)$.
\item For $g_s$ in sector $I$
  \begin{equation}
    \tr'\rho_{\IP^2}^2 = s_{I}(\Phi_{0;2})(g_s) +
    s_{I}(\Phi_{1;2})(g_s) K_2(q),
    \label{eq:hlift2-P2}
  \end{equation}
  where
  \begin{equation}
    K_2(q) = q^{1/6}(1-3q^{1/3}+10q^{2/3} + \ldots).
  \end{equation}
\end{itemize}
By comparing these two identities we conclude immediately
\begin{equation}
  \ms{S}^+_{01;2}(q) =K_2(q).
\end{equation}
We comment that the two relations
\eqref{eq:hlift-P2}, \eqref{eq:hlift2-P2} also justify the claim
\eqref{eq:tr2asymp-P2}.
When $g_s$ is in the second quadrant, \eqref{eq:hlift-P2} clearly
implies \eqref{eq:tr2asymp-P2}.
When $g_s$ is in the first quadrant, \eqref{eq:hlift2-P2} indicates
that in the leading order
\begin{equation}
  \tr'\rho_{\IP^2}^2(\bb) \sim \Phi_{0;2}(g_s) +
  \re^{-(3\CV_{\IP^2}+\frac{\ri}{2})/g_s} (\ldots)
\end{equation}
and the series $\Phi_{0;2}(g_s)$ clearly dominates.

In the next subsection we consider the radial asymptotic analysis of
the anti-holomorphic blocks, which is a more efficient way to compute
the $q$-series $\ms{S}_{01;2}^+$.
