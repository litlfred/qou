---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-006-31-microscopic-spectral-correlators-and-density
section_title: "Microscopic spectral correlators and density"
section_number: 3.1
pages: 6-8
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.994
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec31}

To calculate the spectral correlations, we insert the polynomials
$p_n^{(N_f)}(x,M)$ in Eq.~(\ref{kernel}) for the kernel
$K_N^{(N_f)}(x,y,M)$.  The microscopic limit is obtained according to
Eq.~(\ref{eq1.1}) by rescaling energies and quark masses by
$2N\Sigma$.  We define $\lambda=2N\Sigma \sqrt{x}$ and $m_f=2N\Sigma
M_f$.  In the limit $N\to\infty$, we want both $\lambda$ and $m_f$ to
be of order unity.  The quenched approximation then corresponds to
taking $m_f\to\infty$ (or, of course, setting $N_f=0$).  In the limit
$m_f\to 0$, our results must reduce to those obtained earlier in the
chiral limit \cite{Verb93}.  After rescaling the parameters one uses
the asymptotic relation $\lim_{N\to\infty}L_N^{(\alpha)}(z/N)/N^\alpha
= z^{-\alpha/2}J_\alpha(2\sqrt{z})$, where $J_\alpha$ denotes the
Bessel function of the first kind and order $\alpha$. To obtain the
correct large-$N$ limit one has to use the recurrence relations for
the Laguerre polynomials \cite{Grad65} in Eq.~(\ref{polcf}).  The
properties of the determinant can be used to simplify the expression.
After summing up one uses
\begin{eqnarray}
{\left(\frac{z^2}{N}\right)^\alpha}
        L_{N-1}^{(\alpha)}{\left(\frac{z^2}{N}\right)}&=&
{\frac{N}{N+\alpha}\left(\frac{z^2}{N}\right)^\alpha}
        L_N^{(\alpha)}{\left(\frac{z^2}{N}\right)}\nonumber\\
&&+{\frac{1}{N+\alpha}\left(\frac{z^2}{N}\right)^{\alpha+1}}
        L_N^{(\alpha+1)}{\left(\frac{z^2}{N}\right)}
-{\frac{1}{N+\alpha}\left(\frac{z^2}{N}\right)^{\alpha+1}}
        L_N^{(\alpha)}{\left(\frac{z^2}{N}\right)}\:.
\label{reccur}
\end{eqnarray}
Note that the first, second, and third term on the right-hand side is
of ${\cal O}(1)$, ${\cal O}(1/N)$, and ${\cal O}(1/N^2)$,
respectively.  Using the properties of the determinant and collecting
the terms of  ${\cal O}(1)$ carefully, one obtains the
microscopic limit of (\ref{kernel}).  We arrive at
\begin{eqnarray}
K^{(N_f)}(\lambda,\lambda^\prime,m) & = &\lim\limits_{N\to\infty}
 \:\frac{2\sqrt{\lambda\lambda^\prime}}{(2N\Sigma)^2}\:
  K_N^{(N_f)}\left(\left(\lambda/2N\Sigma\right)^2,
    \left(\lambda^\prime/2N\Sigma\right)^2,
    m/2N\Sigma\right)
  \nonumber \\ & & \hspace*{-35pt} = 
  \frac{\sqrt{\lambda\lambda^\prime}}{\lambda^{\prime 2}-\lambda^2}
  \frac{B^{(N_f)}(\lambda,m)\sum_{f=0}^{N_f}
  \widetilde{B}_f^{(N_f)}(\lambda^\prime,m)
  -B^{(N_f)}(\lambda^\prime,m)\sum_{f=0}^{N_f}
  \widetilde{B}_f^{(N_f)}(\lambda,m)}
  {[C^{(N_f)}(m)]^2\prod_{f=1}^{N_f}\sqrt{(\lambda^2+m_f^2)
      (\lambda^{\prime 2}+m_f^2)}}\:,
\label{microkernel}
\end{eqnarray}
where the normalization $C^{(N_f)}(m)$ is the microscopic limit
of the normalization $C_N^{(N_f)}(M)$ of Eq.~(\ref{polnorm}),
\begin{equation}
C^{(N_f)}(m) \ = \ \lim_{N\to\infty} C_N^{(N_f)}(m/2N\Sigma)
             \ = \ \det\left[m_{f^\prime}^{f-1}I_{f-1}(-m_{f^\prime})
                                 \right]_{f,f^\prime=1,\ldots,N_f} \ .
\label{CNfm}
\end{equation}
The determinant $B^{(N_f)}(\lambda,m)$ in Eq.~(\ref{microkernel}) is
given by
\begin{equation}
B^{(N_f)}(\lambda,m)=\left|
\begin{array}{cccc}
J_0(\lambda) & I_0(-m_1) & \cdots & I_0(-m_{N_f}) \\
\lambda J_1(\lambda) & m_1I_1(-m_1) & \cdots & m_{N_f}I_1(-m_{N_f}) \\
\vdots & \vdots & & \vdots \\
\lambda^{N_f}J_{N_f}(\lambda) & m_1^{N_f}I_{N_f}(-m_1) & \cdots &
m_{N_f}^{N_f}I_{N_f}(-m_{N_f}) \end{array} \right| \ .
\label{matrixb}
\end{equation}
The determinant $\widetilde{B}_f^{(N_f)}(\lambda,m)$ is constructed
from $B^{(N_f)}(\lambda,m)$ by replacing the first column by 
$(\lambda J_1(\lambda), \ldots,\lambda^{N_f+1}J_{N_f+1}(\lambda))^T$ 
if $f=0$ and by replacing the ($f$+1)-th column by
$(m_fI_1(-m_f),\ldots,m_f^{N_f+1}I_{N_f+1}(-m_f))^T$ if
$f=1,\ldots,N_f$.  All $k$-point spectral correlations can be obtained
from the kernel (\ref{microkernel}) in analogy with
Eq.~(\ref{corrfct}).  Most importantly, the microscopic spectral
density is obtained by taking the limit $\lambda'=\lambda=z$ in
(\ref{microkernel}).  This yields
\begin{equation}
  \label{microdens}
  \rho_s^{(N_f)}(z,m)=\frac{z}{2}
  \frac{B^{(N_f)}(z,m)\sum_{f=0}^{N_f}\widetilde{D}_f^{(N_f)}(z,m)
  -D^{(N_f)}(z,m)\sum_{f=0}^{N_f}\widetilde{B}_f^{(N_f)}(z,m)}
  {[C^{(N_f)}(m)]^2\prod_{f=1}^{N_f}(z^2+m_f^2)}\:,
\end{equation}
where the determinant $D^{(N_f)}(z,m)$ is constructed from
$B^{(N_f)}(z,m)$ by replacing the first column in (\ref{matrixb}) by
$(z^{-1}J_{-1}(z),\ldots, z^{N_f-1}J_{N_f-1}(z))^T$,
$\widetilde{D}_f^{(N_f)}(z,m)$ is constructed from $D^{(N_f)}(z,m)$ by
replacing the ($f$+1)-th column by
$(m_fI_1(-m_f),\ldots,m_f^{N_f+1}I_{N_f+1}(-m_f))^T$ if
$f=1,\ldots,N_f$, and $\widetilde{D}_0^{(N_f)}(z,m)=B^{(N_f)}(z,m)$.

We have verified that our results (\ref{microkernel}) and
(\ref{microdens}) reproduce the known results for the chiral limit and
the quenched approximation if $m_f\to 0$ and $m_f\to\infty$,
respectively.  In Refs.~\cite{Guhr97a,Jack97a}, the correlations of
the Dirac operator at finite temperature were studied using the
supersymmetry method. These investigations suggest that the
expression~(\ref{microkernel}) for the kernel can be simplified
further and expressed in form of a single determinant.
Indeed, such a more compact form was very recently obtained in
Ref.~\cite{Damg97}.  We write the result in the form
\begin{eqnarray}
K^{(N_f)}(\lambda,\lambda^\prime,m) & = &  
  \frac{\sqrt{\lambda\lambda^\prime}}{\lambda^{\prime 2}-\lambda^2}
  \frac{1}{C^{(N_f)}(m)\prod_{f=1}^{N_f}\sqrt{(\lambda^2+m_f^2)
      (\lambda^{\prime 2}+m_f^2)}}
  \nonumber \\ & & \hspace*{-60pt}\times
\left|\begin{array}{ccccc}
J_0(\lambda) & J_0(\lambda^\prime) & I_0(-m_1) & \ldots & I_0(-m_{N_f}) \\
\lambda J_1(\lambda) & \lambda^\prime J_1(\lambda^\prime) & 
  m_1I_1(-m_1) & \ldots & m_{N_f}I_1(-m_{N_f}) \\
\vdots & \vdots & \vdots & & \vdots \\
\lambda^{N_f+1} J_{N_f+1}(\lambda) & 
  {\lambda^\prime}^{N_f+1} J_{N_f+1}(\lambda^\prime) & 
  m_1^{N_f+1}I_{N_f+1}(-m_1) & \ldots & 
  m_{N_f}^{N_f+1}I_{N_f+1}(-m_{N_f}) 
\end{array}\right| \ .
\label{darmnij}
\end{eqnarray}
The microscopic spectral density then reads
\begin{eqnarray}
\rho_s^{(N_f)}(z,m) & = &  
  -\frac{z}{2}
  \frac{1}{C^{(N_f)}(m)\prod_{f=1}^{N_f}(z^2+m_f^2)}\nonumber \\ 
  & & \hspace*{-22pt}\times
\left|\begin{array}{ccccc}
  z^{-1}J_{-1}(z) & J_0(z) & I_0(-m_1) & \ldots & I_0(-m_{N_f}) \\
  J_0(z) & z J_1(z) & 
  m_1I_1(-m_1) & \ldots & m_{N_f}I_1(-m_{N_f}) \\
  \vdots & \vdots & \vdots & & \vdots \\
  z^{N_f} J_{N_f}(z) & 
  z^{N_f+1} J_{N_f+1}(z) & 
  m_1^{N_f+1}I_{N_f+1}(-m_1) & \ldots & 
  m_{N_f}^{N_f+1}I_{N_f+1}(-m_{N_f}) 
\end{array}\right|\:.
\label{mdDN}
\end{eqnarray}
We have verified by direct calculation that the expressions
(\ref{microkernel}), (\ref{darmnij}) and (\ref{microdens}),
(\ref{mdDN}) are identical, respectively.  A number of interesting
special cases can be derived from (\ref{microdens}) or (\ref{mdDN}).
(For $N_f=1$ and $\nu=0$, $\rho_s$ was first computed in
Ref.~\cite{Jurk96}.  However, like the authors of \cite{Damg97}, we
fail to agree with the result given in Eq.~(80) of Ref.~\cite{Jurk96}
which does not reproduce the quenched result in the limit
$m\to\infty$.)  As an example, we give the result for $\rho_s$ for two
degenerate flavors of mass $m$ and $\nu=0$,
\begin{equation}
  \rho_s^{(2)}(z,m)=\frac{z}{2}\left(J_0^2(z)+J_1^2(z)\right)
  -\frac{2z}{(z^2+m^2)^2}\frac{[zJ_1(z)I_0(m)+mJ_0(z)I_1(m)]^2}
  {I_0^2(m)-I_1^2(m)}\:.
\end{equation}
This expression is plotted in Fig.~\ref{fig1} compared with the
results obtained in the chiral limit and in the quenched
approximation.  
Clearly, the presence of light flavors leads to a suppression of small
eigenvalues as expected.  We emphasize again that while we have worked
with $\nu=0$, the general case $\nu>0$ can easily be obtained by
introducing $\nu$ additional massless flavors. For completeness, we
state the result for the microscopic spectral density for general
$\nu$ which is obtained by expanding the determinants in (\ref{mdDN}),
\begin{eqnarray}
\rho_s^{(N_f,\nu)}(z,m) & = &  
  -\frac{z}{2}
  \frac{1}{\widetilde{C}^{(N_f,\nu)}(m)z^{2\nu}
    \prod_{f=1}^{N_f}(z^2+m_f^2)}  \nonumber \\ 
  & & \hspace*{-80pt} \times
\left|\begin{array}{ccccc}
  z^{\nu-1}J_{\nu-1}(z) & z^\nu J_\nu(z) & m_1^\nu I_\nu(-m_1) & 
  \ldots & m_{N_f}^\nu I_\nu(-m_{N_f}) \\
  z^\nu J_\nu(z) & z^{\nu+1} J_{\nu+1}(z) & 
  m_1^{\nu+1}I_{\nu+1}(-m_1) & \ldots & 
  m_{N_f}^{\nu+1}I_{\nu+1}(-m_{N_f}) \\
  \vdots & \vdots & \vdots & & \vdots \\
  z^{N_f+\nu} J_{N_f+\nu}(z) & 
  z^{N_f+\nu+1} J_{N_f+\nu+1}(z) & 
  m_1^{N_f+\nu+1}I_{N_f+\nu+1}(-m_1) & \ldots & 
  m_{N_f}^{N_f+\nu+1}I_{N_f+\nu+1}(-m_{N_f}) 
\end{array}\right|
\label{rhosnu}
\end{eqnarray}
with
\begin{equation}
  \widetilde{C}^{(N_f,\nu)}(m)=
  \det\left[m_{f^\prime}^{\nu+f-1}I_{\nu+f-1}(-m_{f^\prime}) 
        \right]_{f,f^\prime=1,\ldots,N_f}\:.
\end{equation}
Note that the chiral limit follows immediately from (\ref{rhosnu}) by
the replacements $N_f=0$ and $\nu\to N_f+\nu$.   We then obtain
\begin{equation}
  \rho_s^{(N_f,\nu)}(z,0)=\frac{z}{2}\left(J_{N_f+\nu}^2(z)
    -J_{N_f+\nu+1}(z)J_{N_f+\nu-1}(z)\right)
\end{equation}
as required \cite{Verb93}.
