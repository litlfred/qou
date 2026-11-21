---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-002-21-formulation-of-the-model
section_title: "Formulation of the model"
section_number: 2.1
pages: 2-4
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec21}

The statistical properties of the random-matrix model for the massive
Dirac operator with $N_f$ flavors and dynamical quark masses $M_f$
($f=1,\ldots,N_f$) which was introduced above are given by the
probability density function
\begin{equation}
P_N^{(N_f)}(W,M) \ = \ \frac{1}{\widetilde{Z}_N^{(N_f)}(M)} \, 
                \prod_{f=1}^{N_f}\det(WW^\dagger+M_f^2)
                \exp(-N\Sigma^2{{\rm tr}\,} WW^\dagger)
\label{pdf}
\end{equation}
with $M=(M_1,\ldots,M_{N_f}$). Here, $W$ is a complex matrix of
dimension $N$.  Apart from a Gaussian, this distribution contains
$N_f$ fermionic determinants. Eventually, we are mainly interested in
the microscopic limit. Hence, it suffices to take into account a
Gaussian in the total distribution (\ref{pdf}) since various authors
\cite{Brez96,Nish96} have given proofs of universality in related
problems.  Note that even for nonzero topological charge $\nu$ it is
sufficient to consider only square matrices $W$ in the calculation
because of the duality between topology and flavor
\cite{Verb93,Verb94a}.  A nonzero $\nu$ is obtained by introducing
$\nu$ additional massless flavors at the end of the calculation.  The
normalization constant
\begin{equation}
\widetilde{Z}_N^{(N_f)}(M) \ = \ 
               \int d[W] \prod_{f=1}^{N_f}\det(WW^\dagger+M_f^2)
                \exp(-N\Sigma^2{{\rm tr}\,} WW^\dagger)
\label{partf}
\end{equation}
depends on the quark masses and plays the role of a partition
function.  Since both of the above expressions depend on the matrices
$W$ only through invariant functions of $WW^\dagger$, they can be
reduced to integrals over radial coordinates. We write $W=U \Lambda
\bar{V}$ with $U\in{\rm U}(N)$, $\bar{V}\in{\rm U}(N)/ {\rm U}^N(1)$,
and $\Lambda={\rm diag}(\lambda_1,\ldots,\lambda_N)$, where the radial
coordinates $\lambda_i$ are restricted to the positive real axis.
Thus, we have $WW^\dagger=U\Lambda^2U^\dagger$ suggesting the
introduction of new variables $x_i=\lambda_i^2$. The measure
transforms as $d[W]=\Delta_N^2(X)d[X]d\mu(U)d\mu(\bar{V})$, where
$X={\rm diag} (x_1,\ldots,x_N)$, $\Delta_N(X)=\prod_{i<j}(x_i-x_j)$ is
the Vandermonde determinant, and $d\mu$ is the Haar measure.  After
integrating over the unitary groups, we obtain
\begin{equation}
\label{eq2.1}
P_N^{(N_f)}(X,M) = \frac{1}{Z_N^{(N_f)}(M)} \, \Delta_N^2(X) \, 
                 \prod_{i=1}^N w^{(N_f)}(x_i,M) 
\end{equation}
for the probability density and 
\begin{equation}
Z_N^{(N_f)}(M) = \int d[X] \, \Delta_N^2(X) \,
                 \prod_{i=1}^N w^{(N_f)}(x_i,M) 
\label{pdpfx}
\end{equation}
for the partition function $Z_N^{(N_f)}(M)$ which differs from
$\widetilde{Z}_N^{(N_f)}(M)$ by the group volumes. The expression
\begin{equation}
w^{(N_f)}(x,M) \ = \ \exp(-N\Sigma^2x) \prod_{f=1}^{N_f}(x+M_f^2) 
\label{weight}
\end{equation}
will be referred to as the weight function.

Because of a main result of RMT \cite{Meht91}, all spectral
correlation functions $R_k^{(N_f)}(x_1,\ldots,x_k,M)$ of our model can
readily be written in terms of the polynomials $p_n^{(N_f)}(x,M)$
which are orthogonal with respect to the weight function
$w^{(N_f)}(x,M)$,
\begin{equation}
  \int_0^\infty dx \, w^{(N_f)}(x,M) p_n^{(N_f)}(x,M) p_m^{(N_f)}(x,M)
  \ = \ 
  \frac{Z_{n+1}^{(N_f)}(M)}{(n+1)\,Z_n^{(N_f)}(M)} \, \delta_{nm} \ .
\label{ortho}
\end{equation} 
The correlation functions are given as the determinant
\begin{equation}
R_k^{(N_f)}(x_1,\ldots,x_k,M) \ = \ 
  \det\left[K_N^{(N_f)}(x_i,x_j,M)\right]_{i,j=1,\ldots,k}
\label{corrfct}
\end{equation}
with a kernel given by
\begin{equation}
K_N^{(N_f)}(x,y,M) \ = \ \sqrt{w^{(N_f)}(x,M)w^{(N_f)}(y,M)} \,
                 \sum_{n=0}^{N-1}   
                \frac{(n+1)\,Z_n^{(N_f)}(M)}{Z_{n+1}^{(N_f)}(M)}
                p_n^{(N_f)}(x,M) p_n^{(N_f)}(y,M) \ .
\label{summe}
\end{equation}
With the help of the Christoffel-Darboux formula the kernel
can be expressed as
\begin{eqnarray}
K_N^{(N_f)}(x,y,M) & = & N \, \frac{Z_{N-1}^{(N_f)}}{Z_N^{(N_f)}} \,
                 \sqrt{w^{(N_f)}(x,M)w^{(N_f)}(y,M)} \nonumber\\
  &&\times \frac{p_N^{(N_f)}(x,M)p_{N-1}^{(N_f)}(y,M)
    -p_{N-1}^{(N_f)}(x,M)p_N^{(N_f)}(y,M)}{x-y} \ ,
\label{kernel}
\end{eqnarray}
provided that the coefficient of the power $x^n$ in $p_n^{(N_f)}(x,M)$
is unity.  Eventually, we will take the microscopic limit as discussed
in the Introduction.
