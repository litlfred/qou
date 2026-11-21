---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-007-32-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 3.2
pages: 19-21
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.943
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
\label{sc:41.blocks}

One happy fact of state integral model of knot $\knot{4}_1$ at level 1
is that when $\imag{\bb}\neq 0$, it can be evaluated by summing over
residues and it factorises to products of $q$- and $\tq$-series
\cite{Garoufalidis:2013rca}, i.e., the holomorphic blocks
\cite{Beem:2012mb}.  In addition, variants known as the descendants of
the state integral can be written, which also enjoys factorisation.
This fact turns out to be very useful in the resurgence analysis, as
the Stokes matrices can be written in terms of them
\cite{Garoufalidis:2020xec,Garoufalidis:2020nut}.  We find here at
generic level $k$, we can also write down descendants of the state
integral and they also factorise to holomorphic blocks.  In fact, the
holomorphic blocks are independent of $k$ (only implicitly through
$x,\tx,q,\tq$, cf.~\cite{Dimofte:2014zga}), while the factorisation
formulas are not.

We introduce the following descendant state integral for knot
$\knot{4}_1$
\begin{align}
  \chi^{(k)}_{\knot{4}_1;r,s}(\mu,n;\tau) = \frac{\eta_k}{k}
  &\sum_{m\in\IZ_k}\int_{\mc{C}}
    \rd \sigma \mc{Z}_\bb^{(k)}[\Delta](\sigma-\mu,m-n)
    \mc{Z}_{\bb}^{(k)}[\Delta](\sigma,m)\nn
  &\times(-1)^m
    \re^{\frac{\pi\ri}{k}((\sigma-c_\bb)^2-2(\mu-\sigma+c_\bb)^2-m^2+2(n-m)^2)}\nn
  &\textcolor{blue}
    {\times\re^{\frac{2\pi\ri}{k}(-\ri(r\bb+s\bb^{-1})(c_\bb-\sigma)+(r-s)m)}}.
\end{align}
The motivation for the particular form of the descendant state
integral is that both the tetrahedron partition function
$\mc{Z}_\bb^{(k)}[\Delta](\sigma,m)$ and the extra factor colored in blue
\begin{equation}
  f(\sigma,m) = \exp\left(\frac{2\pi}{k}(r\bb+s\bb^{-1})(c_\bb-\sigma)
    +\frac{2\pi\ri}{k}(r-s)m\right)
\end{equation}
in the integrand enjoys nice quasi-periodicity property under the
shift
\begin{equation}
  (\sigma,m) \rightarrow (\sigma-\ri\bb^{\pm 1},m \pm 1),\quad
  (\sigma,m) \rightarrow (\sigma+\ri\bb^{\pm 1},m \mp 1).
\end{equation}
The former is given in \eqref{eq:Db-per}, and the latter is simply
\begin{subequations}
\begin{align}
  &f(\sigma\mp\ri\bb,m \pm 1) = f(\sigma,m) q^{\pm r},\\
  &f(\sigma\pm\ri\bb^{-1},m \pm 1) = f(\sigma,m)\tq^{\pm s}.
\end{align}
\end{subequations}
In addition, the form of the descendant state integral may be related
to insertion of a light knot from the Chern-Simons theory point of
view \cite{Agarwal:2022cdm}, or to turning on FI parameters from the
3d SCFT point of view \cite{Yoshida:2014ssa}.

Note that compared to the state integral
$\chi_{\knot{4}_1}^{(k)}(\mu,n;\tau)$ defined in \eqref{eq:chi-41},
here the contour of integral $\mc{C}$ has to be modified such that it
asymptotes at both $\pm \infty$ to the horizontal line
$\imag{\sigma} = \sigma_0$ with
$\sigma_0 <\imag(c_\bb)-|\imag(\mu)|-|\real(r\bb+s\bb^{-1})|$ but is
deformed near the origin so that all the poles of the integrand are
below the contour.  The integrand only has poles coming from the two
tetrahedron partition functions
$\mc{Z}^{(k)}_\bb[\Delta](\sigma-\mu,m-n)$ and
$\mc{Z}^{(k)}_\bb[\Delta](\sigma,m)$, and they are located
respectively at
\begin{align}
  &v = \mu
    -\ri\bb\alpha-\ri\bb^{-1},\quad
    \alpha-\beta \equiv m-n \;(\text{mod}\; k),\\
  &\sigma =
    -\ri\bb \,\alpha -\ri\bb^{-1} \beta,\quad
    \alpha-\beta \equiv m \;(\text{mod}\; k).
\end{align}

On the other hand, since the integrand decays exponentially fast
towards infinity below the contour $\mc{C}$, we can evaluate the
descendant state integrand by completing the contour from below and
adding up residues from these poles.
Then we find in this way that
\begin{align}
  \chi^{(k)}_{\knot{4}_1;r,s}(\mu,n;\tau)=
  &\re^{-\frac{\pi\ri k}{4}-\frac{\pi\ri}{2k}-\frac{\pi\ri}{4k}(\tau+\tau^{-1})}
    A_r(x,q)A_{-s}(\tx,\tq^{-1}) \nn
  &+\re^{\frac{\pi\ri          k}{4}+\frac{\pi\ri}{2k}+\frac{\pi\ri}{4k}(\tau+\tau^{-1})}
    B_r(x,q)B_{-s}(\tx,\tq^{-1}).
\end{align}
Here $A_r(x,q), B_r(x,q)$ are descendant holomorphic blocks defined by
\begin{align}
  &A_r(x,q) = \theta(-q^{1/2}x;q)^{-2}x^{2r} J(q^rx^2,x;q),\\
  &B_r(x,q) = \theta(-q^{-1/2}x;q)x^r J(q^r x,x^{-1};q),
\end{align}
where $J(x,y;q^\varepsilon):= J^{\varepsilon}(x,y;q)$ for $|q|<1$ and
$\varepsilon = \pm$ is the $q$-Hahn Bessel function
\begin{subequations}
  \begin{align}
    &J^+(x,y;q) = (qy;q)_\infty \sum_{n=0}^\infty
      (-1)^n\frac{q^{\frac{1}{2}n(n+1)}x^n}{(q;q)_n(qy;q)_n}\\
    &J^-(x,y;q) = \frac{1}{(y;q)_\infty} \sum_{n=0}^\infty
      (-1)^n\frac{q^{\frac{1}{2}n(n+1)}x^ny^{-n}}{(q;q)_n(qy^{-1};q)_n}.  
  \end{align}
\end{subequations}
Note that the definition of descendant holomorphic blocks as function
of $x,q$ are independent of $k$.  They enjoy the same properties as
discussed in \cite{Garoufalidis:2020xec}.  If we define the descendant Wronskian matrix
\begin{equation}
  W_r(x;q) =
  \begin{pmatrix}
    A_r(x;q) & B_{r}(x;q)\\
    A_{r+1}(x;q) & B_{r+1}(x;q)
    \label{eq:W.41}
  \end{pmatrix},
\end{equation}
it enjoys the inversion property that
\begin{equation}
  W_m(x;q)
  \begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix}
  W_{\ell}(x;q^{-1})^T \in GL(2,\IZ[q^{\pm 1}x^{\pm 1}]).
\end{equation}
In particular
\begin{equation}
  W_{-1}(x;q)
  \begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix}
  W_{-1}(x;q^{-1})^T =
  \begin{pmatrix}
    x^{-2}+x^{-1}-1 & 1 \\ 1 & 0
  \end{pmatrix}.
  \label{eq:Wcont.41}
\end{equation}
