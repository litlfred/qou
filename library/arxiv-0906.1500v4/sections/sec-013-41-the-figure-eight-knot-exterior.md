---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-013-41-the-figure-eight-knot-exterior
section_title: "The figure eight knot exterior"
section_number: 4.1
pages: 12-13
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
We consider the figure eight knot $K$ as in Figure~\ref{fig:figure8_knot}.
The knot group $\pi_1(E_K)$ is expressed as 
$$
E_K = \langle x, y \,|\, [x^{-1}, y]x = y[x^{-1}, y] \rangle 
$$
where $E_K$ is the complement an open tubular neighbourhood $N(K)$ of $K$ in $S^3$. 
\begin{figure}[!h]
  \begin{center}
    \includegraphics[scale=.6]{figure8_knot}
  \end{center}
  \caption{The figure eight knot}
  \label{fig:figure8_knot}
\end{figure}
The following correspondences give an $\SL$-representation $\rho_{\sqrt{s}, u}$ of $\pi_1(E_K)$
\begin{equation}
x \mapsto 
\begin{pmatrix}
  \sqrt{s} & 1/\sqrt{s} \\
  0 & 1/\sqrt{s}
\end{pmatrix},
\quad 
y \mapsto 
\begin{pmatrix}
  \sqrt{s} & 0 \\
  -u\sqrt{s} & 1/\sqrt{s}
\end{pmatrix}
\end{equation}
when the pair $(s, u)$ is a root of $\phi(s, u) = u^2 + (3 - (s+1/s))(u+1)$.

By using formula in~\cite{Milnor:1968,Kitano, KL},
the polynomial torsion is expressed as 
\[
\PolyTors{E_K}{\otAd{\varphi}{\rho_{\sqrt{s}, u}}}(t)
= \tau_0 \cdot 
\frac{
  \det \Phi \left(
    \frac{\partial}{\partial y}\,
    [x^{-1}, y]x[y, x^{-1}]y^{-1}
  \right)
}{
  \det \Phi(x-1)
}
\]
where $\Phi$ is the linear extension of $\otAd{\varphi}{\rho_{\sqrt{s}, u}}$ on $\ZZ[\pi_1(E_L)]$.
The Fox differential turns into 
\[
\frac{\partial}{\partial b}
\left(
  [x^{-1}, y]x[y, x^{-1}]y^{-1}
\right)
= x^{-1} - x^{-1}yxy^{-1} + x^{-1}yxy^{-1}x - yx^{-1} -1.
\]
Therefore the numerator of $\PolyTors{E_K}{\otAd{\varphi}{\rho_{\sqrt{s}, u}}}(t)$
turns out
$$ \tau_0 \cdot \det \Phi(x^{-1} - x^{-1}yxy^{-1} + x^{-1}yxy^{-1}x - yx^{-1} -1).$$ 

When we choose the basis $\{E, H, F\}$ in $\sll$, the adjoint actions
$Ad_{\rho(x)^{-1}}$ and $Ad_{\rho(y)^{-1}}$ are represented by the following 
upper and lower triangular matrices:
\[
Ad_{\rho(x)^{-1}}=
  \begin{pmatrix}
    1/s & 2/s & -1/s \\
    0 & 1 & -1 \\
    0 & 0 & s
  \end{pmatrix}
\quad
Ad_{\rho(y)^{-1}}=
  \begin{pmatrix}
    1/s & 0 & 0 \\
    -u & 1 & 0 \\
    -su^2 & 2su & s
  \end{pmatrix}.
\]

Calculating the determinant and reducing with the equation $\phi(s, u)=0$, we can obtain the polynomial as
\begin{align}\label{eqn:PolyTorsion_figure8}
  \PolyTors{E_K}{\otAd{\varphi}{\rho_{\sqrt{s}, u}}}(t)
  &=
  \frac{
    \tau_0 \cdot \frac{1}{t^3} \cdot (t-1)^2(t-s)(t-1/s)(t^2 - (2 s + 2/s +1)t +1)
  }{
    (t-s)(t-1)(t-1/s)
  } \nonumber \\
  &= \tau_0 \cdot 
    \frac{1}{t^3} 
    (t-1)\left( t^2 - (2I_x^2 -3)t +1\right)
\end{align}
where $I_x = \sqrt{s} + 1/\sqrt{s}$ is the trace function of the meridian $x$.
Note that we can use $I_y$ instead of $I_x$ since all generators in a Wirtinger presentation are conjugate.
