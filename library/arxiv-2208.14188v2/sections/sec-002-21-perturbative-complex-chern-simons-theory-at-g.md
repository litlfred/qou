---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-002-21-perturbative-complex-chern-simons-theory-at-g
section_title: "Perturbative complex Chern-Simons theory at generic level"
section_number: 2.1
pages: 4-10
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.987
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
The $sl(2,\IC)$ Chern-Simons theory on a three manifold $M$ has action
\begin{equation}
  I_{k,s} = t S_{\text{CS}}(A) + \tilde{t} S_{\text{CS}}(\overline{A})
\end{equation}
where $S_{\text{CS}}(A)$ is the three dimensional Chern-Simons action
\begin{equation}
  S_{\text{CS}}(A) = \frac{1}{4\pi}\int_M \Tr (A\wedge\rd A + \frac{2}{3}A\wedge
  A\wedge A),
\end{equation}
$A$ is a connection of the $sl(2,\IC)$ bundle over $M$, and
$\overline{A}$ its complex conjugation.

The couplings $t,\tilde{t}$ can be split as
\begin{equation}
  t = \frac{1}{2}(k+\ri s),\quad \tilde{t} =\frac{1}{2}(k-\ri s).
\end{equation}
In a consistent quantum theory, the level $k$ must be an integer so
that the partition function of the Chern-Simons theory is invariant
under large gauge transformations.  The other level $s$ is constrained
to be either real or imaginary in order for the CS theory to be
unitary, which, however, we do not impose in this work.

Suppose the 3-manifold $M$ is a knot complement $M = S^3\backslash K$
with torus boundary.  The $sl(2,\IC)$ connection on the boundary torus
is parametrised by the holonomies $x,y$ along the meridian and the
longitude.  The condition that the $sl(2,\IC)$ connection can be
extended to the interior of $M$ constrains that $x,y$ are not
independent but are related by a polynomial equation
\begin{equation}
  A(x,y) = 0
\end{equation}
called the $A$-polynomial.
Furthermore, in a quantum theory, the holonomy $x$ should be
parametrised as
\begin{equation}
  x = \exp\left(\frac{2\pi \bb\mu}{k} - \frac{2\pi\ri n}{k}\right),
\end{equation}
where $\mu\in\IC$, $n\in\IZ_k$, and the parameter $\bb$ is related to
the levels $k,s$ by
\begin{equation}
  \bb^2 = \frac{k-\ri s}{k + \ri s}.
\end{equation}

By the 3d-3d correspondence, the $sl(2,\IC)$ Chern-Simons theory at
discrete level $k\geq 1$ on $M$ is dual to a 3d $N=2$ SCFT denoted by
$T_2[M]$ put on an orbifold of the squashed 3-sphere $S^3_\bb/\IZ_k$
\cite{Dimofte:2014zga},
\begin{equation}
  S^3_\bb/\IZ_k = \left\{(z,w)\in \IC^2 \,|\, \bb^2|z|^2 +
    \bb^{-2}|w|^2 = 1\right\}/ (z,w)\sim (\re^{2\pi\ri/k}z,\re^{-2\pi\ri/k}w).
\end{equation}
Here $\bb$ has the geometric meaning of the squashing parameter.  When
$M$ is a knot complement, the $T_2[M]$ theory has a $u(1)$ flavor
symmetry.  The parameters $\mu,n$ are then respectively the flavor
mass, and the holonomy of the flavor vector field.  The latter takes
value in $\pi_1(S^3_\bb/ \IZ_k) = \IZ_k$.

When $M = S^3\backslash K$ is a hyperbolic manifold, it can be
triangulated, namely decomposed to $N$ ideal tetrahedra glued along
their faces.  In \cite{Dimofte:2011ju}, the $T_2[M]$ theory was
constructed based on the triangulation data from the $T_2[\Delta]$
associated with an ideal tetrahedron $\Delta$, which is well
understood.  Based on this construction, the partition function of
$T_2[M]$ on $S^3_\bb/\IZ_k$ was computed \cite{Dimofte:2014zga}, and
it was used to give the state integral model for the $sl(2,\IC)$
Chern-Simons theory at level $k$.

It is important to note that, as first pointed out in
\cite{Chung:2014qpa}, the construction in \cite{Dimofte:2011ju} misses
an entire sector related to the Abelian flat connection, and thus the
partition function computed in \cite{Dimofte:2014zga} is also not
complete.  Rather, the state integral model should be regarded as the
reduced partition function of the $sl(2,\IC)$ Chern-Simons theory that
does not include the contribution from the Abelian flat connection.

Let us discuss in a bit detail the state integral model.  The
triangulation of $M$ in terms of $N$ tetrahedra is described by the
small Neumann-Zagier data\footnote{The complete Neumann-Zagier data
  introduced in \cite{Dimofte:2015kkp,Dimofte:2012qj} also includes a
  choice of the solution to the Neumann-Zagier equation.} that can be
encoded in a tuple $\gamma = (\pmb{A},\pmb{B},\nu)$ consisting
of 


two matrices $\pmb{A},\pmb{B}\in GL(N,\IZ)$ and a vector $\nu
\in\IZ^N$. They encode the coefficients of Thurston's gluing equations
for the triangulation including $N-1$ independent equations imposing
condition on internal edges, and one equation describing holonomy on
external edges.  We order rows of $\pmb{A},\pmb{B}$ and elements of
$\nu$ so that the first rows of $\pmb{A},\pmb{B}$ and the first element
of $\nu$ corresponds to the external edge.


It was shown in \cite{Neumann:1985vht} that $(\pmb{A}\;\pmb{B})$ forms
the top half of a symplectic matrix, so that $\pmb{A}\pmb{B}^T$ is
symmetric and $(\pmb{A}\;\pmb{B})$ is of full rank.  On the other hand,
giving a triangulation of $M$, the choice of Neumann-Zagier data is
not unique.  Following \cite{Dimofte:2015kkp,Dimofte:2012qj} we always
choose a set of Neumann-Zagier data where $\pmb{B}$ is invertible over
integers, and then $\pmb{B}^{-1}\pmb{A}$ must be symmetric.


Let us introduce in addition
$\bs{\sigma} = (\s_1,\ldots,\s_N) \in \IC^N$,
$\pmb{m} = (m_1,\ldots,m_N)\in(\IZ_k)^N$ as well as
$\bs{\mu} = (\mu,0,\ldots,0) \in \IC\times 0^{N-1}$,
$\pmb{n} = (n,0,\ldots,0) \in \IZ_k\times 0^{N-1}$.

By following the procedure in \cite{Dimofte:2014zga} and extending
slightly the formulas in \cite{Dimofte:2015kkp}, the state integral
model can be written as 
  
\begin{align}
  &\mc{Z}_\gamma^{(k)}(\mu,n;\bb)  =
  
    \frac{
    1
    }{k^N\sqrt{\det \pmb{B}}}
    \sum_{m\in (\IZ_k)^N}\int
    \rd^N \bs\sigma
    \textcolor{blue}{\re^{\frac{2\pi\ri}{k}(-\bs\sigma \pmb{B}^{-1}\bs\mu+\pmb{m} \pmb{B}^{-1}\pmb{n})}}
    \re^{\frac{\pi\ri}{k}(-\bs\sigma \pmb{B}^{-1}\pmb{A}\bs\sigma +
    \pmb{m} \pmb{B}^{-1}\pmb{A} \pmb{m} + 2 c_\bb\bs{\sigma}
    \pmb{B}^{-1}\bs{\nu})}\nn 
  &\phantom{===============}      
    (-1)^{\pmb{m} \pmb{B}^{-1}\pmb{A} \pmb{m}}
    \prod_{i=1}^N \mc{Z}_\bb^{(k)}[\Delta](\sigma_i,m_i).
      \label{eq:ZNgmMu0}
\end{align}
The part in blue is due to non-vanishing boundary holonomy and thus
new compared to the results in \cite{Dimofte:2015kkp}. Here
$\mc{Z}_\bb^{(k)}[\Delta](\sigma_i,m_i)$ is the partition function of
the Chern-Simons theory on a tetrahedron, which can be expressed in
terms of Faddeev's quantum dilogarithm $\Phi_\bb(x)$
\begin{equation}
  \mc{Z}_\bb^{(k)}[\Delta](\mu,n) =
  \prod_{(r,s)\in \Gamma(k;n)}\Phi_\bb(c_\bb
  -\frac{1}{k}(\mu+\ri \bb r + \ri\bb^{-1}s))
\end{equation}
where
\begin{equation}
  \Gamma(k;n) = \{(r,s)\in\IZ^2\;|\; 0\leq r,s<k, r-s \equiv n
  (\text{mod}\;k)\}
\end{equation}
and $c_\bb = \frac{\ri}{2}(\bb+\bb^{-1})$.  This defines a meromorphic
function of $\mu\in\IC$ for each $n\in\IZ_k$, and it is defined for
all values of $\bb$ with $\bb^2$ in the cut plane
$\IC' = \IC\backslash \IR_{\leq 0}$.
When $\imag \bb >0$ or $\imag\bb <0$, it has the factorisation form
\begin{equation}
  \mc{Z}_{\bb}^{(k)}[\Delta](\mu,n) = (qx^{-1};q)_\infty (\tq^{-1}\tx^{-1};\tq^{-1})_\infty
\end{equation}
where we use the notation
\begin{equation}
  \begin{gathered}
    q = \exp \frac{2\pi\ri}{k}(\bb^2+1),\quad \tq = \exp
    -\frac{2\pi\ri}{k}(\bb^{-2}+1),\\
    x = \exp \left(\frac{2\pi\bb\mu}{k} - \frac{2\pi\ri n}{k}\right),\quad
    \tx = \exp \left(\frac{2\pi\bb^{-1}\mu}{k} + \frac{2\pi\ri n}{k}\right),
  \end{gathered}
\end{equation}
and $(a,q)_\infty$ is the $q$-Pochhammer symbol defined to be
$\prod_{j=1}^\infty(1-a q^j)$ if $|q|<1$ or
$1/(q^{-1}a;q^{-1})_\infty$ if $|q|>1$.

One can give explicitly the contour of integral to make the $N$
dimensional integral convergent \cite{Dimofte:2014zga}.  But it is a
bit complicated and we specify the contours in individual examples in
Sections~\ref{sc:41}, \ref{sc:52}.

We are interested in the double scaling limit
\begin{equation}
  \bb\rightarrow 0,\quad\mu \rightarrow\infty, \quad
  \bb\mu\;\text{fixed},
\end{equation}
where the last condition guarantees that the holonomy parameter $x$
remains finite.
Let us introduce
\begin{equation}
  \zeta = \re^{2\pi\ri/k},\quad \tau = \bb^2
\end{equation}









By scaling the variables
\begin{equation}
  Z_i = 2\pi\bb\sigma_i, \quad u_i = 2\pi\bb\mu_i =
  \begin{cases}
    2\pi\bb\mu,\quad &i=1\\
    0,\quad &i\geq 2
  \end{cases}
\end{equation}
and using the asymptotic expansion \eqref{eq:ZDasymp} of the
tetrahedron partition function, the integral \eqref{eq:ZNgmMu0} can be
written as
\begin{align}
  \mc{Z}_\gamma^{(N)}(\mu,n;\tau) =
  &
    \frac{1
    }
    {k^N\sqrt{\det \pmb{B}}(4\pi^2\tau)^{N/2}}\nn
  &\sum_{\pmb{m}\in(\IZ_k)^N}(-1)^{\pmb{m} \pmb{B}^{-1}\pmb{A}\pmb{m}}
    \zeta^{\frac{1}{2}\pmb{m}\pmb{B}^{-1}\pmb{A}\pmb{m}+\pmb{m}\pmb{B}^{-1}\pmb{n}}
    \int\rd^N \pmb{Z} \exp \sum_{\ell=0}^\infty (2\pi\ri\tau)^{\ell-1}
    U^{(\pmb{m})}_\ell(\pmb{u},\pmb{Z})
\end{align}
where the coefficient functions are
\begin{subequations}
  \begin{align}
    &U_0(\pmb{u},\pmb{Z}) = \textcolor{blue}{\frac{1}{k}\pmb{Z}\pmb{B}^{-1}\pmb{u} +}
      \frac{1}{2k}\pmb{Z} \pmb{B}^{-1}\pmb{A}\pmb{Z}
      -\frac{\pi\ri}{k}\pmb{Z}\pmb{B}^{-1}\bs\nu
      +\frac{1}{k}\sum_{i=1}^N\Li_2(\re^{-Z_i})\label{eq:U0},\\
    
    
    
    
    &U^{(\pmb{m})}_{\ell\geq 1}(\pmb{u},\pmb{Z}) =
      -\frac{1}{2k}\pmb{Z}\pmb{B}^{-1}\bs\nu\delta_{\ell,1} + 
      \sum_{i=1}^N\sum_{s=1}^k
      \frac{B_\ell(s/k)}{\ell!}
      \Li_{2-\ell}(\re^{\frac{2\pi\ri}{k}(s+m_i)}\re^{-\frac{Z_i}{k}}).\label{eq:Ul}
  \end{align}
\end{subequations}
We drop the superscript $(\pmb{m})$ for $U_0$ since it does not depend
on the index $\pmb{m}$. We have also simplified the expression of
$U_0$ using the identity
\begin{equation}
  \sum_{s=1}^k \Li_2(\re^{2\pi \ri s/k}x) = \frac{1}{k}\Li_2(x^k),
\end{equation}
which can be easily proved by the series expansion of $\Li_2(x)$.  The
saddle point equations, i.e. the critical point equations for $U_0$
are
\begin{align}
  u_j + \sum_{i=1}^N A_{ji}Z_i + \sum_{i=1}^N B_{ji}
  \log(1-\re^{-Z_i}) = \pi\ri \nu_j,\quad j=1,\ldots,N,
  \label{eq:cr-eq-u}
\end{align}
or equivalently with
\begin{equation}
  z_i = \re^{Z_i},\quad w_i = \re^{u_i}
\end{equation}
we find
\begin{align}
  w_j \prod_{i=1}^N z_i^{A_{ji}}(1-z_i^{-1})^{B_{ji}} =
  (-1)^{\nu_j},\quad
  j=1,\ldots,N.
  \label{eq:cr-eq-w}
\end{align}
Note that at the end of the day, we must set $u_j=0$ or equivalently
$w_j = 1$ for $j=2,\ldots,N$.
Since
\begin{equation}
  x = \exp\frac{2\pi\ri}{k}\left(-\ri\bb\mu-n\right) =
  \exp \left(\frac{u}{k} - \frac{2\pi\ri n}{k}\right)
  = \zeta^{-n} w_1^{1/k},
\end{equation}
the critical equations can also be written as
\begin{subequations}
  \begin{align}
    &x^k\prod_{i=1}^N z_i^{A_{ji}}(1-z_i^{-1})^{B_{ji}} =
      (-1)^{\nu_j},\quad
      j=1,
      \label{eq:cr-eq-x1}\\
    &\prod_{i=1}^N z_i^{A_{ji}}(1-z_i^{-1})^{B_{ji}} =
      (-1)^{\nu_j},\quad
      j=2,\ldots,N.
      \label{eq:cr-eq-x2}
  \end{align}
\end{subequations}
They can be regarded as a deformation of the Neumann-Zagier
equations. Each solution $\pmb{z}^* = \exp \pmb{Z}^*$ to the critical
equations corresponds to a non-Abelian $sl(2,\IC)$ flat connection
$\sigma_*$ over $M$.

We can choose one of the critical points (saddle points)
$\pmb{Z}^* = (Z_i^*)$ and expand around the critical point by
$Z_j = Z_j^* + (2\pi\ri\tau)^{1/2} \delta Z_j$.  By an expansion first
in terms of $\tau$ and then performing Gaussian integral order by
order, we obtain a trans-series
$\Phi_{\gamma}^{(k,\s_*)}(\mu,n;\tau)$.  This was worked out in
\cite{Dimofte:2015kkp} when $\mu=0$ and $n=0$.  In the generic case
the calculation is similar, and we present the results here.

Let us introduce $z = \re^{Z}$, as well as
\begin{equation}
  z' = (1-z)^{-1},\quad z'' = 1-z^{-1}
\end{equation}
so that
\begin{equation}
  z z' z'' = -1.
\end{equation}

From \eqref{eq:Ul} it is necessary to choose a $k$-th
root of $Z^*$. We introduce $\theta_i$ such that
\begin{equation}
  (\theta_i)^k = z_i^*.
\end{equation}






Let us also define the Average and Vev of a function $g$
\begin{align}
  \mathop{\text{Av}}(g(\pmb{m})) =
  \frac{\sum_{\pmb{m}\in(\IZ_k)^N} a_{\pmb{m}}(x,\theta) g(\pmb{m})}
  {\sum_{\pmb{m}\in(\IZ_k)^N} a_{\pmb{m}}(x,\theta)}
\end{align}
with
\begin{align}
  a_{\pmb{m}}(x,\theta) =
  \textcolor{blue}{x^{-\pmb{m}\pmb{B}^{-1}}}
  (-1)^{\pmb{m}\pmb{B}^{-1}\pmb{A}\pmb{m}}
  \zeta^{\frac{1}{2}(\pmb{m}\pmb{B}^{-1}\pmb{A}\pmb{m}+\pmb{m}\pmb{B}^{-1}\bs\nu)}
  \theta^{-\pmb{B}^{-1}\pmb{A}\pmb{m}}
  \prod_{i=1}^N(\zeta\theta_i^{-1};\zeta)_{m_i}^{-1}.
  \label{eq:am}
\end{align}
and
\begin{align}
  \vev{g(\delta \pmb{Z})} = \frac{\int \rd^N \delta \pmb{Z}\,
  \re^{-\frac{1}{2}\delta \pmb{Z}^T \pmb{H} \delta \pmb{Z}}g(\delta \pmb{Z})}
  {\int\rd^N \delta \pmb{Z}\,
  \re^{-\frac{1}{2}\delta \pmb{Z}^T \pmb{H} \delta \pmb{Z}}}
\end{align}
with
\begin{align}
  \pmb{H} = \frac{1}{k}\left(-\pmb{B}^{-1}\pmb{A} + \Delta_{{z^*}'}\right),
\end{align}
and
\begin{equation}
  \Delta_z = \diag(z_1,\ldots,z_N).
\end{equation}

The perturbative expansion of the state integral \eqref{eq:ZNgmMu0}
near the critical point $\pmb{Z}^*$ then reads
\begin{align}
  \Phi_\gamma^{(k,\sigma_*)}(u,n;\tau) = 
  \re^{U^{(k)}_{0,0}(\sigma_*)/(2\pi\ri\tau)}
  \omega_{\gamma}^{(k,\sigma_*)}\varphi_{\gamma}^{(k,\sigma_*)}(u,n;\tau).
  \label{eq:Zpert}
\end{align}
The 1-loop contribution is
\begin{align}
  \omega_{\gamma}^{(k,\sigma_*)} = \frac{1}
  {(\ri k)^{N/2}\sqrt{\det(A\Delta_{{z^*}''}+B\Delta_{z^*}^{-1})
  {\pmb{z}^*}^{\pmb{B}^{-1}\pmb{\nu}/k}
 
  }}
  \prod_{i=1}^N D_k^*(\theta_i^{-1})^{1/k} \sum_{\pmb{m}\in(\IZ_k)^N}
  a_{\pmb{m}}(x,\theta).
  \label{eq:omega}
\end{align}
Here recall the \emph{cyclic quantum dilogarithms} are defined by
\begin{equation}
  D_k(z) = \prod_{s=1}^{k-1}(1-\zeta^s z)^s,\quad
  D_{k}^*(z) = \prod_{s=1}^{k-1}(1-\zeta^{-s}z)^s.
\end{equation}
Higher loop contributions are given in
\begin{align}
  \varphi_{\gamma}^{(k,\sigma_*)}(u,n;\tau) =
  \mathop{\text{Av}}\left(
  \vev{
  g(\delta \pmb{Z},\pmb{m};x,\theta)
  }
  \right) = 1 + \tau \,\IC[[\tau]]
  \label{eq:varphi}
\end{align}
and
\begin{align}
  g(\delta \pmb{Z},\pmb{m};x,\theta) =
  \exp\left(
  \sum_{\ell\geq 0}(2\pi\ri\tau)^{\ell+d/2-1}
  {\sum_{d\geq  0}}'U_{k,(i^d)}^{(\ell,\pmb{m})}\delta Z_i^d\right),
\end{align}
where ${\sum_{d\geq 0}}'$ means $d\geq 3$ for $\ell=0$, $d\geq 1$ for
$\ell =1$, and $d\geq 0$ for $\ell\geq 2$.  Besides, in each sum a
summation over $i=1,\ldots,N$ is implicit.  The coefficients are
\begin{subequations}
  \begin{align}
    U^{(k)}_{0,0} =
    &\frac{1}{k}\pmb{Z}^*\pmb{B}^{-1}\pmb{u}
      -\frac{\pi\ri}{k}\pmb{Z}^*\pmb{B}^{-1}\bs\nu
      +\frac{1}{2k}\pmb{Z}^*\pmb{B}^{-1}\pmb{A}\pmb{Z}^*+
      \frac{1}{k}\sum_{j=1}^N\Li_2(\re^{-Z_j^*}),
      \label{eq:U00}
    \\
    U^{(k)}_{0,(i^d)} =
    &\frac{(-1)^d}{k d!}\Li_{2-d}(\re^{-Z_i^*}),\quad d\geq 3,\\
    U^{(k,\pmb{m})}_{\ell\geq 1,(i^d)} =
    &\delta_{\ell,1}\delta_{d,0}
      \left(-\frac{1}{2k}\pmb{Z}^*\pmb{B}^{-1}\bs\nu\right)
      +\delta_{\ell,1}\delta_{d,1}
      \left(-\frac{1}{2k}(\pmb{B}^{-1}\bs\nu)_i\right)\nn+
    &\frac{(-1)^d}{k^d d!\ell!}\sum_{j=1}^N\sum_{s=1}^k
      B_\ell(s/k)
      \Li_{2-\ell-d}(\re^{\frac{2\pi\ri}{k}(s+m_j)}\re^{-\frac{Z_j^*}{k}})
      (\delta_{ij})^d.
  \end{align}
\end{subequations}


The trans-series $\Phi_\gamma^{(k,\sigma_*)}(u,n;\tau)$ has some very
important properties.

First of all, unlike the other coefficients, $U_{0,0}(\sigma_*)$ in
\eqref{eq:U00} depends on the level $k$ only as an overall factor
$1/k$,
\begin{equation}
  U^{(k)}_{0,0}(\sigma_*) = \frac{1}{k} U_{0,0}(\sigma_*).
  \label{eq:U00k}
\end{equation}
And $U_{0,0}(\sigma_*)$ only depends on the Neumann-Zagier data
$\gamma$, the choice of solution $\sigma_*$, and the holonomy
parameter $u = \log(x^k)$ (but not on the other holonomy parameter
$n$).  When $|u|\ll 1$, $U_{0,0}(\sigma_*)$ is the deformed
complexified hyperbolic volume of the knot complement
$S^3\backslash K$ \cite{Gukov:2003na}.

Next, even though the expression of the trans-series
$\Phi_\gamma^{(k,\s_*)}(u,n;\tau)$ depends explicitly on
$\theta_i^*$, a choice of the $k$-th root of $z_i^*$, one can show
that a different choice of $\theta_i^*$ merely amounts to an overall
constant factor.

The exponential $\exp U_{0,0}/(2\pi\ri \tau)$ manifestly
depends on $z_i^*$ instead of $\theta_i^*$.

Besides, one can prove that \emph{both
  $(\omega_{\gamma}^{(k,\sigma_*)})^{2k}$ and
  $\varphi_{\gamma}^{(k,\sigma_*)}(\tau)$ are invariant under the
  transformation $\theta_i\rightarrow \zeta\theta_i$}.  This has
already been proved when the holonomy $x$ is turned off in
\cite{Dimofte:2015kkp}, and the coefficients of the power series
$\varphi_{\gamma}^{(k,\sigma_*)}(\tau)$ are said to live in the trace
field of the knot.

When the holonomy $x$ is turned on, a similar proof following closely
\cite{Dimofte:2015kkp} can be written down with all the necessary
ingredients provided in \eqref{eq:omega},\eqref{eq:varphi}, and we do
not repeat the proof here.

In addition, the dependence on the holonomy of the trans-series
$\Phi_\gamma^{(k,\s_*)}(u,n;\tau)$ is quite elegant.  \emph{Both
  $(\omega_{\gamma}^{(k,\sigma_*)})^{2k}$ and
  $\varphi_{\gamma}^{(k,\sigma_*)}(\tau)$ depend on the combination
  $x = \exp(u/k - 2\pi\ri n/k)$ but not on $u$ and $n$ individually}.
This is because the NZ solution $z^*$ depends on $u$ and $n$
implicitly through the modified NZ equations \eqref{eq:cr-eq-x1},
\eqref{eq:cr-eq-x2}, which only depend on $x^k$.  On top of that,
$(\omega_{\gamma}^{(k,\s_*)})^{2k}$ and
$\varphi_{\gamma}^{(k,\s_*)}(\tau)$ depend on $u,n$ through the NZ
solution $z^*$ as well as $a_{\pmb{m}}(x,\theta)$, which is also a
function of $x$.

Combining the discussion of these two paragraphs, we thus claim that
the coefficients of the power series
$\varphi_\gamma^{(k,\s_*)}(u,n;\tau)$ are understood to live in
$F_{k,x}$, the trace field of the knot extended by holonomy $x$,
defined by
\begin{equation}
  F_{k,x} = F_k(x),\quad F_k = F(\zeta), \quad F = \IQ(z_1,\ldots,z_N).
\end{equation}

Finally, although a universal expression \eqref{eq:omega} of the
one-loop contribution $\omega_\gamma^{(k,\s_*)}$ at any level is
possible, the power series $\varphi_\gamma^{(k,\s_*)}$ depend on the
level in a very complicated way, as we will see in example
sections~\ref{sc:41.asymp},\ref{sc:52.asymp}.

We also comment that the trans-series \eqref{eq:Zpert} can be computed
from radial asymptotics of $q$-series that come from the evaluation of
the state integral model for $q$ at complex roots of unity, similar to
the discussion in \cite{Garoufalidis:2018qds}.

Examples of the $q$-series, also known as holomorphic blocks, are
shown in Sections~\ref{sc:41.blocks} and \ref{sc:52.blocks}.

They can be regarded as $x$-feformation of the Nahm sums.

Even though the form of trans-series \eqref{eq:Zpert} is elegant and
it allows us to infer the above universal properties, it is
computationally inefficient as it involves an $N$-dimensional
integral.  Often the state integral \eqref{eq:ZNgmMu0} can be
simplified.

For example in the case of complements of knots $\knot{4}_1$ and
$\knot{5}_2$, in Thurston's scheme of triangulation the number $N$ of
ideal tetrahedra is respectively $2$ and $3$, and their state integral
models involve a two- and a three-dimensional integral respectively.
However using integral identities of the tetrahedron partition
function $\mc{Z}_\bb^{(k)}[\Delta](\sigma,m)$, both of them can be
reduced to one-dimensional integrals
\cite{Dimofte:2014zga,Andersen:2016ugz}, and their perturbative
expansion in terms of Gaussian integral is much simpler.  This will be
demonstrated in Sections~\ref{sc:41}, \ref{sc:52}.

Nevertheless the universal properties of the asymptotic series
discussed in this section still hold.
