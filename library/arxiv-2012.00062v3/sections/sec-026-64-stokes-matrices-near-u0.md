---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-026-64-stokes-matrices-near-u0
section_title: "Stokes matrices near u=0"
section_number: 6.4
pages: 56-60
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.633
latex_coverage_ratio: 0.693
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.41stokes}

In this section we conjecture a formula for the Stokes matrices of the
asymptotic series $\varphi(x;\tau)$.  When we turn on the non-vanising
deformation parameter $u$, the resurgent structure discussed in
Section~\ref{sub.41x=1} undergoes significant changes.  Compared to
Figure~\ref{fig:sings-u0-41} there are many more singular points in
the Borel plane whose positions depend on $u$ in addition to $\tau$,
and the Stokes matrices also become $u$-dependent.  However, if we
focus on the case when $u$ is not far away from zero, equivalent to
$x$ not far away from 1, the resurgent data is holomorphic in $u$ and
reduces to those in Section~\ref{sub.41x=1} in the $u=0$ limit.  For
instance, each singular point in Figure~\ref{fig:sings-u0-41} splits
to a cluster of neighoring singular points separated with distance
$\log x$ as shown in Figure~\ref{fig:sings-m-41}. In particular, each
singular point $\iota_{i,j}$ on the real axis splits to a cluster of
three, in accord with the off-diagonal entries $\pm 3$ in
\eqref{eq:S0u041}, and if we choose real $x$, the split singularities
still lie on the real axis.  As in Section~\ref{sub.41x=1}, we label
the four regions separating singularities on real axis and all the
others by $I,II,III,IV$ (see Figure~\ref{fig:secs-m-41}).  In each of
the four regions, we have the following the results.

\begin{figure}
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_borelplane_s1m}\hspace{4ex}
\includegraphics[height=7cm]{fig8_borelplane_s2m}
\end{center}
\caption{The singularities in the Borel plane for the series
  $\varphi_{\sigma_{j}} (x;\tau)$ with $j=1,2$ of knot $\knot{4}_1$
  where $x$ is close to 1. The shortest vertical spacing between
  singularities is $2\pi\ri$, and the horizontal spacing between
  neighboring singularities in each cluster is $\log x$.}
\label{fig:sings-m-41}
\end{figure}

\begin{figure}
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_regions_m}
\end{center}
\caption{Four different sectors in the $\tau$-plane for $\Phi(u;\tau)$
  of knot $\knot{4}_1$ with $u$ close to zero.}
\label{fig:secs-m-41}
\end{figure} 

\begin{conjecture}
  \label{conj.41M}
  The asymptotic series and the holomorphic blocks are related
  by~\eqref{abrelx} with the diagonal matrix $\Delta(\tau)$ as
  in~\eqref{D41}, where matrices $M_R(x;q)$ are given in terms of the
  matrices $W_{-1}(x;q)$ as follows 
\begin{subequations}
\begin{align}
  M_{I}(x;q) =
  &\begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix} W_{-1}(x;q)^T
            \begin{pmatrix}
              0&1\\-x^{-1}&1
            \end{pmatrix}, & |q|<1\,,
  \label{eq:M1-41}\\
  M_{II}(x;q) =
  &W_{-1}(x^{-1};q)^T
    \begin{pmatrix}
      -x^{-1}&0\\-x^{-1}&1
    \end{pmatrix}, & |q|<1\,,
  \label{eq:M2-41}\\
  M_{III}(x;q) =
  &W_{-1}(x^{-1};q)^T
    \begin{pmatrix}
      -x^{-1}&0\\1+x&1
    \end{pmatrix}, & |q|>1\,,
  \label{eq:M3-41}\\
  M_{IV}(x;q) =
  &\begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix} W_{-1}(x;q)^T
            \begin{pmatrix}
              0&1\\-x^{-1}&-x^{-1}-x^{-2}
            \end{pmatrix}, & |q|>1\,.
                            \label{eq:M4-41}
\end{align}
\end{subequations}
\end{conjecture} 
The above conjecture completely determines the resurgent structure of
$\Phi(\tau)$. Indeed, it implies that the Stokes matrices, defined in 
Equations~\eqref{4G} and~\eqref{SG}, are explicitly given by:

\begin{subequations}
\begin{align}
    \ms{S}^+(x;q) =
    &\begin{pmatrix}
      0&-1\\
      x^{-1}&-1-x
    \end{pmatrix}
              \cdot W_{-1}(x^{-1};q^{-1})\cdot W_{-1}(x;q)^T\cdot
              \begin{pmatrix}
                0&x\\
                -1&-1-x^{-1}
              \end{pmatrix} ,\quad |q|<1\,,
  \label{eq:Sp-41}\\
  
  
  
  
  
  
    \ms{S}^-(x;q)=
    &\begin{pmatrix}
      x&x\\
      0&-1
    \end{pmatrix}
              \cdot W_{-1}(x;q)\cdot W_{-1}(x^{-1};q^{-1})^T\cdot
              \begin{pmatrix}
                x^{-1}&0\\
                x^{-1}&-1
              \end{pmatrix},\quad |q|<1\,.
                                \label{eq:Sn-41}
\end{align}
\end{subequations}
We remark that since $s(\Phi_\s)(x;\tau)$ for $\s=1,2$ transform under
the reflection $\pi: x\mapsto x^{-1}$ uniformly by \eqref{eq:-xPhi} (see
the comment below), the Stokes matrices should be invariant under
$\pi$, and we have checked that \eqref{eq:Sp-41},\eqref{eq:Sn-41}
indeed satisfy this consistency condition.

In the $q\mapsto 0$ limit,
\begin{equation}
  \ms{S}^+(x;0) =
  \begin{pmatrix}
    1&x^{-1}+1+x\\0&1
  \end{pmatrix},\quad
  \ms{S}^-(x;0) =
  \begin{pmatrix}
    1&0\\-x^{-1}-1-x&1
  \end{pmatrix}
  \label{eq:S0x41}
\end{equation}
A curious corollary of our computation is that the matrices of
integers \eqref{eq:S0u041} from~\cite{gh-res,GZ:kashaev} which relates
the asymptotics of the coefficients of $\varphi(\tau)$ to the
coefficients themselves, spreads out to the matrices \eqref{eq:S0x41}
with entries in $\IZ[x^{\pm 1}]$.

Using the unique factorization Lemma~\ref{lem.fac} and the Stokes
matrix $\sf{S}$ from above, we can compute the Stokes constants and
the corresponding matrix $\calS$ of Equation~\eqref{calS} to arbitrary
order in $q$, and we find that
\begin{align}
  \mc{S}^+_{\s_1,\s_1}(x;q) =
  &\ms{S}^+(x;q)_{1,1}-1\nn=
  &(-2 - x^{-2} - 2x^{-1} - 2 x - x^2)q
    +(-3 - x^{-2} - 2x^{-1} - 2 x - x^2)q^2+\cO(q^3),\\
  \mc{S}^+_{\s_1,\s_2}(x;q) =

  &\ms{S}^+(x;q)_{1,2}/\ms{S}^+(x;q)_{1,1}
  -(\mc{S}^{(1,0)}_{\s_1,\s_2}x+\mc{S}^{(0,0)}_{\s_1,\s_2}
  +\mc{S}^{(-1,0)}_{\s_1,\s_2}x^{-1})\nn=
  &(3 + x^{-2} + 2x^{-1} + 2 x + x^2)q\nn
  &+(17 + x^{-4} + 4x^{-3} + 9x^{-2} + 15x^{-1} + 15 x + 9 x^2 + 4 x^3 + x^4)
  q^2+\cO(q^3),\\
  \mc{S}^+_{\s_2,\s_1}(x;q) =
  &\ms{S}^+(x;q)_{2,1}/\ms{S}^+(x;q)_{1,1}\nn=
  &(-3 - x^{-2} - 2x^{-1} - 2 x - x^2)q\nn
  &+(-17 - x^{-4} - 4x^{-3} - 9x^{-2} - 15 x^{-1} - 15 x - 9 x^2 - 4 x^3 - x^4)
  q^2+\cO(q^3),\\
  \mc{S}^+_{\s_2,\s_2}(x;q) =
  &\ms{S}^+(x;q)_{2,2} -1-
    \ms{S}^+(x;q)_{1,2}\ms{S}^+(x;q)_{2,1}/\ms{S}^+(x;q)_{1,1}\nn=
  &(2 + x^{-2} + 2x^{-1} + 2 x + x^2) q \nn
  &+ (17 + x^{-4} + 4x^{-3} + 9x^{-2} + 14x^{-1} + 14 x + 9 x^2 + 4 x^3 + x^4)
  q^2+\cO(q^3).
\end{align}
They enjoy the symmetry
\begin{equation}
  \mc{S}^{+}_{\s_1,\s_2}(x;q) =
  -\mc{S}^{+}_{\s_2,\s_1}(x;q)\,,
\end{equation}
and experimentally, it appears that the entries of the matrix
$\mc{S}^+(x;q) = (\mc{S}^+_{\s_i,\s_j}(x;q))$ (except the upper-left
one) are (up to a sign) in $\BN[x^{\pm 1}][[q]]$. 
Similarly we can extract the Stokes constants
$\mc{S}^{(\ell,-k)}_{\s_i,\s_j}$ associated to the singularities in
the lower half plane, and assemble into $q^{-1}$-series
$\mc{S}^{-}_{\s_i,\s_j}(x;q^{-1})$.  We find they are related to
$\mc{S}^+_{\s_i,\s_j}(x;q)$ by
\begin{gather}
  \mc{S}^{-}_{\s_i,\s_j}(x;q) = -\mc{S}^{+}_{\s_j,\s_i}(x;q),\;\;i\neq j\,
  \nn
  \mc{S}^{-}_{\s_1,\s_1}(x;q) = \mc{S}^{+}_{\s_2,\s_2}(x;q),\;\;
  \mc{S}^{-}_{\s_2,\s_2}(x;q) = \mc{S}^{+}_{\s_1,\s_1}(x;q)\,.
\end{gather}

Let us now verify Conjecture~\ref{conj.S3D}.
From \eqref{eq:Sp-41} we find that indeed
\begin{equation}
  \ms{S}^+(x;q) \stackrel{\cdot}{=} W_{-1}(x^{-1};q^{-1})\cdot W_{-1}(x;q)^T.
\end{equation}
Using the recursion relation \eqref{eq:W41rec} and the relation
between two Wronskians \eqref{W41xm}, we further find 
\begin{equation}
  \ms{S}^+(x;q) \stackrel{\cdot\cdot}{=} \cW_{0}(x^{-1};q^{-1})\cdot
  \cW_{0}(x;q)^T.
  \label{eq:SW41}
\end{equation}
If we use the uniform notation for all holomorphic blocks
\begin{equation}
  (B_{K}^\alpha(x;q))_{\alpha=1,2} = (A_0(x;q),B_0(x;q)),
\end{equation}
the right hand side of \eqref{eq:SW41} reads 
\begin{equation}
  \cW_{0}(x^{-1};q^{-1})\cdot \cW_{0}(x;q)^T =
  \left(
    \sum_{\alpha}B^{\alpha}_{\knot{4}_1}(q^jx;q)
    B^{\alpha}_{\knot{4}_1}(q^{-i}x^{-1};q^{-1})
  \right)_{i,j=0,1}.
  \label{eq:WW41}
\end{equation}
which is precisely the right hand side of \eqref{eq:SInd} in
Conjecture~\ref{conj.S3D} following \eqref{eq:IndB}.\footnote{Note
  that because the form of the state integral in \cite{Beem} is
  slightly different from that in \cite{AK}, which we adopt, our
  convention for holomorphic blocks is also different from
  \cite{Beem}.  As a result, the entries of $\eqref{eq:WW41}$ equate
  the DGG indices computed in \cite{Beem} up to a prefactor
  \begin{equation}
    \left(\cW_{0}(x^{-1};q^{-1})\cdot \cW_{0}(x;q)^T\right)_{i+1,j+1} =
    (-q^{1/2})^{j-i}\text{Ind}_{\knot{4}_1}^{\text{rot}}
    (j-i,q^{\frac{j+i}{2}}x;q),\quad i,j=0,1.
  \end{equation}
  If we take this into account, Conjecture~\ref{conj.S3D} should be
  modified slightly by stating the accompanying matrices on the left
  and on the right are in $GL(2,\IZ(x,q^{1/2}))$.}
In addition, the forms of the accompanying matrices on the left and on the
right are such that the $(1,1)$ entry of $\ms{S}^+(x;q)$ equates
exactly the DGG index with no magnetic flux.
By explicit calculation,

\begin{equation}
\label{S11v}
\begin{aligned}
  \ms{S}^+(x;q)_{1,1}& =
  J(x, x^{-1};q) J(x, x^{-1}; q^{-1}) + J(x^{-2}, x^{-1};q) J(x^2, x; q^{-1}) \\
  &=1 -(2x^{-2}+ x^{-1}+2+x + 2x^2)q - (x^{-2}+2x^{-1} +3+ 2x + 
  x^2) q^2 + O(q^3),
  \end{aligned}
\end{equation}

which is the $\text{Ind}^{\text{rot}}_{\knot{4}_1}(0,x;q)$ given in
\cite{Beem}.
