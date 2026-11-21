---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-007-32-distribution-of-the-smallest-eigenvalue
section_title: "Distribution of the smallest eigenvalue"
section_number: 3.2
pages: 8-9
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.979
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec32}

In lattice simulations, the performance of an algorithm is frequently
determined by the magnitude of the smallest eigenvalue.  It is
therefore of interest to compute an analytical result for the
distribution of the smallest eigenvalue, $P^{(N_f)}(\lambda_{\rm
  min},m)$, in the framework of RMT.  This is the subject of this
section.  The RMT result should be universal and identical with that
of full QCD under the same conditions as the microscopic spectral
density.  The only result that has been computed so far in the
literature applies to the quenched approximation where
$P^{(0)}(\lambda)=\lambda\exp(-\lambda^2/4)/2$ \cite{Forr93}.

A well-known quantity in RMT is the so-called ``hole probability''
$E(s_1,s_2)$ which is the probability that the interval $(s_1,s_2)$ is
free of eigenvalues.  For the smallest eigenvalue, we again move to
the microscopic scale by rescaling energies and masses by $2N\Sigma$.
For the interval $(0,s)$ at the spectrum edge, we then have
\begin{equation}
  \label{eq4.1}
  E(0,s)=\int_s^\infty dx_1\cdots dx_N \widetilde\rho_N^{(N_f)}
  (x_1,\ldots,x_N;m)\:,
\end{equation}
where the probability density function on the microscopic scale (with
$x_i=z_i^2$) is given by
\begin{equation}
  \label{eq4.2}
  \widetilde\rho_N^{(N_f)}(x_1,\ldots,x_N;m)=c_N^{(N_f)}(m)
  \Delta_N^2(x)\prod_{i=1}^Ne^{-x_i/4N} \prod_{f=1}^{N_f}(x_i+m_f^2)\:,
\end{equation}
cf.~Eqs.~(\ref{eq2.1}) and (\ref{weight}).  The factor
$c_N^{(N_f)}(m)$ ensures that $E(0,0)=1$ and should not be confused
with the normalization constant defined in Eqs.~(\ref{polnorm}) and
(\ref{CNfm}).  On the other hand, we have
\begin{equation}
  \label{eq4.3}
  E(0,s)=\int_s^\infty dx_{\rm min} P^{(N_f)}(x_{\rm min},m)\:.
\end{equation}
Hence, the distribution of the smallest eigenvalue ($x_{\rm min}
=\lambda_{\rm min}^2$) is given by
\begin{equation}
  \label{eq4.4}
  P^{(N_f)}(\lambda_{\rm min},m)=2\lambda_{\rm min}
  P^{(N_f)}(x_{\rm min},m)=
  -2\lambda_{\rm min}\left.\frac{dE(0,s)}{ds}
  \right|_{s=\lambda_{\rm min}^2} \:.
\end{equation}
Performing the derivatives, we obtain
\begin{eqnarray}
  \label{eq4.5}
  -E'(0,s)&=&c_N^{(N_f)}(m)Ne^{-s/4N}\prod_{f=1}^{N_f}(s+m_f^2)
  \nonumber\\ 
  &&\times\int_s^\infty dx_1\cdots dx_{N-1} \Delta_{N-1}^2(x)
  \prod_{i=1}^{N-1}
  e^{-x_i/4N} (x_i-s)^2 \prod_{f=1}^{N_f}(x_i+m_f^2) \:.
\end{eqnarray}
We now shift $x_i\to x_i+s$ and finally obtain from (\ref{eq4.4})
\begin{eqnarray}
  \label{eq4.7}
  P^{(N_f)}(\lambda,m)&=&2c_N^{(N_f)}(m)N\lambda e^{-\lambda^2/4}
  \prod_{f=1}^{N_f}(\lambda^2+m_f^2)\nonumber\\
  &&\times\int_0^\infty dx_1\cdots dx_{N-1} \Delta_{N-1}^2(x) 
  \prod_{i=1}^{N-1}
  e^{-x_i/4N} x_i^2 \prod_{f=1}^{N_f}(x_i+\lambda^2+m_f^2)\:,
\end{eqnarray}
where we have written $\lambda$ instead of $\lambda_{\rm min}$ for
brevity.  The integrals in Eq.~(\ref{eq4.7}) can be done by comparison
with the case of the microscopic spectral density.  In terms of the
probability density function on the microscopic scale, $\rho_s$ is
given by
\begin{eqnarray}
  \rho_s^{(N_f)}(z,m)&=& 2z\cdot N\int_0^\infty dx_1\cdots dx_{N-1} 
  \widetilde\rho_N^{(N_f)}(x_1,\ldots,x_{N-1},z^2;m)\nonumber\\
  &=&2c_N^{(N_f)}(m)Nz\prod_{f=1}^{N_f}(z^2+m_f^2) \nonumber\\
  &&\times\int_0^\infty dx_1\cdots dx_{N-1}\Delta_{N-1}^2(x)
  \prod_{i=1}^{N-1}
  e^{-x_i/4N} (x_i-z^2)^2 \prod_{f=1}^{N_f}(x_i+m_f^2)
  \label{eq4.8}
\end{eqnarray}
in the large-$N$ limit.  Apart from prefactors in front of the
integrals, we note that $P^{(N_f)}(\lambda,m)$ can be obtained by
setting $z=0$ in the integrand of Eq.~(\ref{eq4.8}) and by replacing
$m_f$ by $(\lambda^2+m_f^2)^{1/2}$ in the result for $\rho_s$ (but not
in the normalization factors).  Setting $z=0$ in the numerator
determinant of Eq.~(\ref{mdDN}) makes the first two columns trivial,
and the dimension of the matrix can be reduced to $N_f$ by expanding
the determinant.  Including the prefactors and the proper
normalization, we obtain
\begin{equation}
  \label{eq4.9}
  P^{(N_f)}(\lambda,m)=\frac{\lambda}{2}e^{-\lambda^2/4}
  \frac{\det\left[\left(\lambda^2+m_{f^\prime}^2\right)^{(f+1)/2}
        I_{f+1}\left(-(\lambda^2+m_{f^\prime}^2)^{1/2}\right)
        \right]_{f,f^\prime=1,\ldots,N_f}}
  {C^{(N_f)}(m)\prod_{f=1}^{N_f}(\lambda^2+m_f^2)}
\end{equation}
with $C^{(N_f)}(m)$ given in Eq.~(\ref{CNfm}).  For $N_f=0$,
Eq.~(\ref{eq4.9}) reduces to the quenched result trivially.  We also
reproduce the quenched result by taking the limit $m_f\to\infty$.  The
simplest nontrivial case is $N_f=1, \nu=0$ where
\begin{equation}
  \label{eq4.10}
  P^{(1)}(\lambda,m)=\frac{\lambda}{2}e^{-\lambda^2/4}
  \frac{I_2\left(\sqrt{\lambda^2+m^2}\right)}{I_0(m)}\:.
\end{equation}
For two degenerate flavors of mass $m$ and $\nu=0$, we obtain
\begin{equation}
  \label{eq4.11}
  P^{(2)}(\lambda,m)=
  \frac{\lambda}{2}e^{-\lambda^2/4}
  \frac{1}{I_0^2(m)-I_1^2(m)}
  \left[I_2^2(t)-I_1(t)I_3(t)\right]_{t=\sqrt{\lambda^2+m^2}}\:.

\end{equation}
In Fig.~\ref{fig2}, we plot the distribution of the smallest
eigenvalue for the same parameters as in Fig.~\ref{fig1}. We observe
the same suppression of small eigenvalues in the presence of light
dynamical quarks.
Other cases can readily be derived from (\ref{eq4.9}).  The most
general case where $\nu>0$ can again be obtained by introducing $\nu$
additional massless flavors and expanding the determinants in
(\ref{eq4.9}).  As an example, we state the result for one massive
flavor and $\nu=1$,
\begin{equation}
  P^{(N_f=1,\nu=1)}(\lambda,m)=\frac{\lambda}{2}
  e^{-\lambda^2/4}\frac{1}{mI_1(m)}
  \left[tI_2(\lambda)I_3(t)-\lambda I_2(t)I_3(\lambda)
  \right]_{t=\sqrt{\lambda^2+m^2}}\:.
\end{equation}
