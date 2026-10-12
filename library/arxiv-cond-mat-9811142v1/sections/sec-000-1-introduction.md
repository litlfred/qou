---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
Random matrix ensembles for quantum Hamiltonians are defined in terms of the constraint imposed on the general Hermitian matrix representing the Hamiltonian by time reversal symmetry and spin-rotation invariance (when relevant). This leads to ten distinct random matrix ensembles [@Zi97]. The corresponding eigenvalue probability density function (p.d.f.) can be computed exactly when the independent elements are chosen to have a Gaussian distribution. One then finds that the ten distinct random matrix ensembles belong to one of six different eigenvalue p.d.f.'s. These are $$\begin{aligned}
\label{1.1}
{1 \over C_N} \prod_{l=1}^N e^{-\beta x_l^2/2} \prod_{1 \le j < k \le N}
|x_k - x_j|^\beta
\end{aligned}$$ which defines the Gaussian random matrix ensemble, or $$\begin{aligned}
\label{1.2}
{1 \over C_N'} \prod_{l=1}^N e^{-\beta x_l^2/2} 
x_l^{\beta a + 1} \prod_{1 \le j < k \le N}
|x_k^2 - x_j^2|^\beta, \quad x_l >0
\end{aligned}$$ which defines the Laguerre random matrix ensemble, where $\beta = 1, 2$ or 4.

The study of these random matrix ensembles can be generalized to include a parameter $\tau$. This allows the situation to be studied in which the system evolves between two distinct eigenvalue p.d.f.'s as $\tau$ is varied. For the Gaussian ensemble this can be achieved by choosing the joint distribution of the elements of the random matrix to be $$\begin{aligned}
\label{1.3}
P({X}^{(0)};{X};\tau) = A_{\beta,\tau}
\exp\Big (-\beta
{\rm Tr} \Big \{ (
{X} - {\rm e}^{-\tau}{X}^{(0)})^2
\Big \}/2|1 - {\rm e}^{-2 \tau}| \Big ).
\end{aligned}$$ In this expression $X$ is a real symmetric ($\beta = 1$), Hermitian ($\beta = 2$) or self dual quaternion ($\beta = 4$) $N \times N$ matrix, and $X^{(0)}$ is a prescribed random matrix which must belong to a subspace of the symmetry class of $X$. For $\tau \rightarrow \infty$ the p.d.f. is independent of $X^{(0)}$ and is that of the standard Gaussian ensembles, with p.d.f. ([\[1.1\]](#1.1){reference-type="ref" reference="1.1"}). For general $\tau$ Dyson [@Dy63] proved that the eigenvalue p.d.f. $p = p(x_{1},  \ldots , x_{N}; \tau)$ satisfies the Fokker-Planck equation $$\begin{aligned}
\label{1.4}
{\partial p \over \partial \tau} = {\cal L}p, \quad
{\cal L} = {1 \over \beta} \sum_{j=1}^N {\partial \over \partial x_j}
e^{-\beta W} {\partial \over \partial  x_j}  e^{\beta W}
\end{aligned}$$ with $$\begin{aligned}
\label{1.5}
W = W^{(H)}   =  {1 \over 2} \sum_{j=1}^N x_j^2 - \sum_{1 \le j < k \le N}
\log |x_k - x_j|
\end{aligned}$$ (the superscript $(H)$ is used because of a connection with the Hermite polynomials), subject to the initial condition that $p$ agrees with the eigenvalue p.d.f. of $X^{(0)}$ at $\tau = 0$.

For the Laguerre ensemble, a parameter dependent theory can be developed (see e.g. [@Fo98]) by considering the non-negative matrices $A = X^{\dagger} X$, where $X$ is an $n \times m$ parameter-dependent matrix $$\begin{aligned}
\label{1.6}
P({X}^{(0)};{X};\tau) = A_{\beta,\tau}
\exp\Big (-\beta
{\rm Tr} \Big \{ (
{X} -  e^{-\tau}{X}^{(0)})^\dagger   (
{X} -  e^{-\tau}{X}^{(0)})
\Big \}/2|1 - {\rm e}^{-2 \tau}| \Big )
\end{aligned}$$ (c.f. ([\[1.3\]](#1.3){reference-type="ref" reference="1.3"})) and the elements of $X$ are real ($\beta = 1$), complex ($\beta = 2$) or quaternion real ($\beta = 4$), and $X^{(0)}$ is a prescribed random matrix which must belong to a subspace of the symmetry class of $X$. For $\tau \rightarrow \infty$ the corresponding p.d.f. for the square of the eigenvalues of $A$ is given by ([\[1.2\]](#1.2){reference-type="ref" reference="1.2"}) with $a = n - m + 1 - 2/\beta$, while for general $\tau$ the eigenvalue p.d.f. $p = p(x_{1}^{2},  \ldots , x_{N}^{2}; \tau)$ satisfies ([\[1.4\]](#1.4){reference-type="ref" reference="1.4"}) with $$\begin{aligned}
\label{1.7}
W = W^{(L)}  =  {1 \over 2} \sum_{j=1}^N x_j^2  - (a + 1/\beta) 
 \sum_{j=1}^N \log x_j - \sum_{1 \le j < k \le N}
 \log |x_k^2 - x_j^2|
\end{aligned}$$ (the superscript $(L)$ is used because of a connection with the Laguerre polynomials).

Associated with the parameter dependent eigenvalue p.d.f.'s are parameter dependent distribution functions $$\begin{aligned}
\label{1.7'}
\rho_{(n+m)}(x_1^{(1)},\dots,x_n^{(1)};\tau_1;x^{(2)}_1,\dots,x_m^{(2)};
\tau_2)
\end{aligned}$$ The distribution function $\rho_{(n+m)}$ is defined such that the ratio $$\begin{aligned}
\nonumber
\rho_{(n+m)}(x_1^{(1)},\dots,x_n^{(1)};\tau_1;x_1^{(2)},\dots,x_m^{(2)};
\tau_2)/\rho_{(n+(m-1))}(x_1^{(1)},
\dots,x_n^{(1)};\tau_1;x^{(2)},\dots,x_{m-1}^{(2)};
\tau_2)
\end{aligned}$$ gives the density of eigenvalues at $x_{m}^{(2)}$ when the parameter equals $\tau_{2}$, given that there were eigenvalues at $x_{1}^{(1)}, \ldots,  x_{n}^{(1)}$ when the parameter equalled $\tau_{1}$, and that there are also eigenvalues at $x_{1}^{(2)}, \ldots,  x_{m}^{(2)}$ with parameter $\tau_{2}$ (it is assumed $\tau_{2} > \tau_{1}$).

For the parameter dependent Gaussian and Laguerre ensembles, quaternion determinant expressions have been derived for $\rho_{(n+m)}$ in the case that $\beta = 2$ in ([\[1.4\]](#1.4){reference-type="ref" reference="1.4"}) and initial condition proportional to $e^{-\beta ' W}$ with $\beta ' = 1$ and 4 [@NF98a]. Because each $\beta$ corresponds to a different symmetry class of the Hamiltonian (orthogonal, unitary and symplectic symmetry for $\beta = 1, 2$ and 4 respectively), this describes the transition from orthogonal or symplectic symmetry to unitary symmetry as the parameter $\tau$ is varied from $0$ to $\infty$.

The determinant expressions apply for the finite system. As revised in Section 2, they involve skew orthogonal polynomials known from the study of the distribution functions for $\tau = 0$ in the $\beta = 1$ and 4 cases [@NW91; @NF95], the orthogonal polynomials related to the $\tau = 0$, $\beta = 2$ case, as well as the elements of a connection matrix which specifies the orthogonal polynomials in terms of the appropriate skew orthogonal polynomials. In the Gaussian case, this matrix can be written down from knowledge of the expression for the skew orthogonal polynomials in terms of the orthogonal polynomials (the Hermite polynomials). In the Laguerre case this step requires some calculation which is undertaken below.

Once all these quantities are specified, the general $(n + m)$-point distribution function in the finite system is known explicitly. The immediate task is to compute the scaled thermodynamic limit. This is done in Section 3 for the Laguerre ensemble in the neighbourhood of the hard edge (the smallest eigenvalues, which are constrained to be positive), and in Section 4 for the Gaussian ensemble in the neighbourhood of the soft edge (the largest eigenvalues).

In Section 5 inter-relationships between the distribution functions are discussed. This is done by analyzing certain limits in ([\[1.7\'\]](#1.7'){reference-type="ref" reference="1.7'"}): the limit $\tau_1,\tau_2 \to \infty$, $\tau_1 - \tau_2$ fixed; the $a \to \infty$ limit of the hard edge; and the bulk limit corresponding to large distances from the edge. Also considered is the asymptotic form of the dynamical density-density function $\rho_{(1+1)}^T(X,Y;t)$, which is shown to exhibit a universal non-oscillatory decay for $X,Y,t \to \infty$. A consequence of this decay is an O(1) fluctuation formula for the variance of a slowly varying linear statistic. In the final subsections a realization of the density at the soft edge for $\beta = 1$ initial conditions is given by an empirical computation based on the parameter dependent matrices ([\[1.3\]](#1.3){reference-type="ref" reference="1.3"}) with $X^{(0)}$ a real symmetric matrix, and the explicit form of the static distribution functions at the hard and soft edges for $\beta = 1$ and 4 is noted.

In the Appendix it is shown how our results for the Laguerre ensemble with $N$ finite coincide, in the static limit $\tau \to 0$, with formulas given recently by Widom [@Wi98].
