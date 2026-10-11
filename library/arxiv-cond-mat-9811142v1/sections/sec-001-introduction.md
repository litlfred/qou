---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
doc_brief: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges — For the orthogonal-unitary and symplectic-unitary transitions in random matrix the- ory, the"
text_source: latex
latex_prose_ratio: 0.64
latex_coverage_ratio: 0.993
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

# Revision of the formalism

At the special coupling $\beta = 2$, the Fokker-Planck equation ([\[1.4\]](#1.4){reference-type="ref" reference="1.4"}) with $W$ given by ([\[1.5\]](#1.5){reference-type="ref" reference="1.5"}) or ([\[1.7\]](#1.7){reference-type="ref" reference="1.7"}) can be transformed into an imaginary-time Schrödinger equation for $N$ independent fermions (see e.g. [@Fo98]). As such the exact $N$-body Green function $G(\{x_{j}^{(0)}\}, \{x_{j}\}; \tau)$ can be written as a determinant involving the corresponding single particle Green functions. In terms of the new variable $y_{j} = x_{j}$ in ([\[1.1\]](#1.1){reference-type="ref" reference="1.1"}) and $y_{j} = x_{j}^{2}$ in ([\[1.2\]](#1.2){reference-type="ref" reference="1.2"}) we have previously shown [@NF98] that $$\begin{aligned}
\label{2.1}
G(x_1^{(0)},\cdots,x_N^{(0)};x_1,\cdots,x_N;\tau)  dx_1 \cdots
 dx_N
= G(y_1^{(0)},\cdots,y_N^{(0)};y_1,\cdots,y_N;\tau)  dy_1\cdots 
dy_N
\end{aligned}$$ where $$\begin{aligned}
\label{2.2}
& & G(y_1^{(0)},\cdots,y_N^{(0)};y_1,\cdots ,y_N;\tau) \nonumber \\ 
& = & {\rm e}^{E_0\tau/2} 
\prod_{j=1}^N \sqrt{w(y_j) \over w(y_j^{(0)})} \prod_{1 \le j < k \le N} 
{(y_k - y_j) \over (y_k^{(0)}-y_j^{(0)})} \det[
g(y_j^{(0)},y_k;\tau)]_{j,k=1,
\cdots,N}
\end{aligned}$$ Here $$\begin{aligned}
\label{2.3}
g(y^{(0)},y;\tau) = \sqrt{w(y^{(0)})w(y)} \sum_{j=0}^\infty
p_j(y^{(0)})p_j(y) {\rm e}^{-\gamma_j\tau}
\end{aligned}$$ and $\{p_{j}(x)\}$ are the orthonormal polynomials associated with the weight function $w(x)$. In the Gaussian case $$\begin{aligned}
\label{2.4}
w(y)={\rm e}^{-y^2}, p_n(y) = 2^{-n/2} \pi^{-1/4} (n!)^{-1/2} H_n(y), \quad
\gamma_n = n + {1
\over 2},
\end{aligned}$$ where $H_n(y)$ denotes the Hermite polynomial, while for the Laguerre ensemble $$\begin{aligned}
\label{2.5}
w(y) = y^{a} {\rm e}^{-y}, \quad
p_n(y) = (-1)^n \Big ( {\Gamma(n+1) \over
\Gamma(a+n+1)} \Big )^{1/2} L_n^a(y), \quad \gamma_n = 2(n + {a + 1 \over
2})
\end{aligned}$$ where $L_n^a(y)$ denotes the Laguerre polynomial. The factor $e^{E_{0}\tau/2}$ cancels out the formula for the distribution function, so the explicit value of $E_{0}$ is not needed.

Knowledge of the Green function allows the p.d.f. $$\begin{aligned}
\nonumber 
 p(y_1^{(1)},\cdots,y_N^{(2)};\tau_1;y_1^{(2)},\cdots ,y_N^{(2)};\tau_2)
\end{aligned}$$ for the event that there are eigenvalues at $y_{1}^{(1)}, \ldots , y_{N}^{(1)}$ when the parameter equals $\tau_{1}$, and at $y_{1}^{(2)}, \ldots , y_{N}^{(2)}$ when the parameter is increased to $\tau_{2}$ to be calculated. Explicitly $$\begin{aligned}
\label{2.a}
\lefteqn{ p(y_1^{(1)},\cdots,y_N^{(2)};\tau_1;y_1^{(2)},\cdots
,y_N^{(2)};\tau_2)} \nonumber
\\ && 
= {1 \over N!}
\int_{I'} dy_1^{(0)} \cdots \int_{I'} dy_N^{(0)}
\,p_0(y_1^{(0)},\cdots
,y_N^{(0)})
G(y_1^{(0)},\cdots,y_N^{(0)};y_1^{(1)},\cdots,y_N^{(1)};\tau_1) \nonumber
\\ \quad && \times
G(y_1^{(1)},\cdots,y_N^{(1)};y_1^{(2)},\cdots,y_N^{(2)};\tau_2 - \tau_1).
\end{aligned}$$ Here $p_{0}$ denotes the prescribed initial p.d.f. (in the $y$ variables) and $I'$ denotes the transformed domain (for convenience this will be omitted from subsequent formulas). Initial p.d.f.'s with orthogonal ($\beta = 1$) and symplectic ($\beta = 4$) symmetry are given by the functional forms $$\begin{aligned}
\label{2.b}
p_0(y_1,\cdots,y_N) \propto \left\{
\begin{array}{ll} \prod_{j=1}^N \sqrt{w(y_j)} \prod_{j < l}^N |y_j - y_l|,
& \beta = 1 \\[.2cm]
 \prod_{j=1}^{N/2} w(y_j) \delta(y_j - y_{j+N/2}) \prod_{j < l}^{N/2}
 |y_j - y_l|^4,
& \beta = 4 \quad  (N\: {\rm even}), 
\end{array}
\right.
\end{aligned}$$

The parameter dependent distribution function $\rho_{(n+m)}$ is calculated from the p.d.f. ([\[2.a\]](#2.a){reference-type="ref" reference="2.a"}) according to the formula $$\begin{aligned}
\label{2.c}
\lefteqn{
\rho_{(n+m)}(y_1^{(1)},\cdots,y_N^{(1)};\tau_1;
y_1^{(2)},\cdots,y_N^{(2)};\tau_2) =
   \frac{N!}{(N-n)!}{N! \over (N - m)!}} \nonumber \\&&
\times \int dy_{n+1}^{(1)} \cdots \int dy_N^{(1)}
\int dy_{m+1}^{(2)} \cdots \int dy_N^{(2)} 
 p(y_1^{(1)},\cdots,y_N^{(2)};\tau_1;y_1^{(2)},\cdots ,y_N^{(2)};\tau_2)
\end{aligned}$$ In a recent work [@NF98a] we have shown that for initial conditions ([\[2.b\]](#2.b){reference-type="ref" reference="2.b"}), and $G$ specified by ([\[2.2\]](#2.2){reference-type="ref" reference="2.2"}) with general weight function $w(y)$ and corresponding orthogonal polynomials $\{p_{k}(y)\}_{k = 0, 1, \ldots}\,$, the quantity ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}) can be expressed as a $(n+m)$-dimensional quaternion determinant Tdet (this quantity, which was introduced into random matrix theory by Dyson [@Dy70], is explicitly defined in e.g. [@NF98]).

The entries of the quaternion determinant depend on the functions $$\begin{aligned}
\nonumber
S(x,y;\tau_x,\tau_y), \quad \tilde{I}(x,y;\tau_x,\tau_y), \quad
D(x,y;\tau_x,\tau_y).
\end{aligned}$$ These functions in turn depend on the quantity $F(x, y; \tau)$, which is defined for the $\beta = 1$ initial conditions in ([\[2.b\]](#2.b){reference-type="ref" reference="2.b"}) by $$\begin{aligned}
\label{2.d}
F(x,y;\tau)  =  \int  dz^{\prime} \int^{z^{\prime}} dz
\Big ( g(x,z;\tau) g(y,z^{\prime};\tau) -
g(y,z;\tau) g(x,z^{\prime};\tau) \Big ), \label{tu.1}
\end{aligned}$$ while for the $\beta = 4$ initial conditions in ([\[2.b\]](#2.b){reference-type="ref" reference="2.b"}) it is specified by $$\begin{aligned}
\label{2.e}
F(x,y;\tau)  =  \int  dz  \{ g(x,z;\tau)
\frac{\partial}{\partial z} g(y,z;\tau) - g(y,z;\tau)
\frac{\partial}{\partial z}  g(x,z;\tau) \}. \label{tu.2}
\end{aligned}$$

They also depend on a family of skew-orthogonal monic polynomials $R_{k}(x; \tau)$ of degree $k$. The terminology skew-orthogonal means that they satisfy the skew orthogonality relations $$\begin{aligned}
\label{2.f}
 < R_{2m}(\cdot;\tau), R_{2n+1}(\cdot;\tau) > =
 - < R_{2n+1}(\cdot;\tau), R_{2m}(\cdot;\tau)> = r_m(\tau) \delta_{m,n},
\nonumber
\\
 < R_{2m}(\cdot;\tau), R_{2n}(\cdot;\tau) > = 0, \quad
  < R_{2m+1}(\cdot;\tau), R_{2n+1}(\cdot;\tau) > = 0
\end{aligned}$$ where $$\begin{aligned}
\label{2.g}
 < f(x), g(y) > = \frac{1}{2} \int  dx \int  dy
 \sqrt{w(x) w(y)} F(y,x;\tau)  \Big ( f(y) g(x) - f(x) g(y)\Big ). 
\end{aligned}$$ The polynomials $R_{k}(x; \tau)$ can be deduced from their static counterparts [@FP95; @NF98]. Suppose at $\tau = 0$ we write $$\begin{aligned}
\label{2.h}
R_n(x;0) = \sum_{j=0}^n \alpha_{nj}C_j(x)
, \quad \alpha_{nn}=1,
\end{aligned}$$ where the $C_{j}(x)$ are the monic version of the orthogonal polynomials $p_{j}(x)$ in ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}). Then it is straightforward to verify that $$\begin{aligned}
\label{2.i}
R_n(x;\tau)  e^{\gamma_n \tau} = \sum_{j=0}^n \alpha_{nj} C_j(x)
e^{\gamma_j \tau}
\end{aligned}$$ and $$\begin{aligned}
\label{2.j}
r_k(\tau) = r_k(0) e^{-(\gamma_{2k} + \gamma_{2k+1})\tau}
\end{aligned}$$

Still another function involved is $$\begin{aligned}
\Phi_k(x;\tau) := \int F(y,x;\tau) \sqrt{w(y)} R_k(y;\tau) \,
 dy.
\label{2.k}
\end{aligned}$$ Now, if we invert ([\[2.h\]](#2.h){reference-type="ref" reference="2.h"}) by writing $$\begin{aligned}
\label{2.l}
C_n(x)  e^{\gamma_n \tau} = \sum_{j=0}^n \beta_{nj}
e^{\gamma_j \tau} R_j(x;\tau), \ \ \beta_{nn} = 1.
\end{aligned}$$ then $\Phi_{k}(x; \tau)$ can be expanded according to [@NF98] $$\begin{aligned}
\label{2.m}
\Phi_{2k-1}(x;\tau) {\rm e}^{\gamma_{2k-1} \tau} & = &
- \sqrt{w(x)}  r_{k-1}(0) \sum_{\nu = 2 k - 2}^{\infty} \frac{C_{\nu}(x)
e^{- \gamma_{\nu} \tau}}{h_{\nu}} \beta_{\nu \ 2 k - 2},
\nonumber
\\
\Phi_{2k-2}(x;\tau)  e^{\gamma_{2k-2} \tau}& = & \sqrt{w(x)}  r_{k-1}(0)
\sum_{\nu
= 2
k - 1}^{\infty} \frac{C_{\nu}(x)
e^{- \gamma_{\nu} \tau}}{h_{\nu}} \beta_{\nu \ 2 k - 1} .
\end{aligned}$$ where $h_{\nu}$ is the normalization $$\begin{aligned}
\label{2.n}
\int w(x) C_j(x) C_k(x) \, dx = h_j \delta_{j,k}.
\end{aligned}$$

With this notation, we can now define the functions $S, \tilde{I}$ and $D$. We have, assuming $N$ even, $$\begin{aligned}
\label{2.o} 
\lefteqn{
S(x,y;\tau_x,\tau_y)  :=   \sqrt{w(y)}} \nonumber \\
& & \times 
\sum_{l=0}^{N/2-1} \frac{e^{\gamma_{2l}\tau_x + \gamma_{2l+1}\tau_y}}
{r_{l}(0)}
\{ \Phi_{2 l }(x;\tau_x)  R_{2 l + 1}(y;\tau_y) -
\Phi_{2 l + 1}(x;\tau_x)  R_{2 l}(y;\tau_y) \}, 
\end{aligned}$$ $$\begin{aligned}
\label{2.p} \lefteqn{
\tilde{I}(x,y;\tau_x,\tau_y)} \nonumber \\
  &  & :=
\sum_{l=N/2}^\infty  \frac{e^{\gamma_{2l}\tau_x + \gamma_{2l+1}\tau_y}}
{r_{l}(0)}
\{ \Phi_{2 l}(x;\tau) \Phi_{2 l + 1}(y;\tau) -
\Phi_{2 l + 1}(x;\tau) \Phi_{2 l}(y;\tau) \}
\end{aligned}$$ $$\begin{aligned}
\label{2.q}\lefteqn{ 
D(x,y;\tau_x,\tau_y)  :=   \sqrt{w(x)w(y)} } \nonumber \\ && \times
\sum_{l=0}^{N/2-1} \frac{e^{\gamma_{2l}\tau_x + \gamma_{2l+1}\tau_y}}
{r_{l}(0)}
\{ R_{2 l }(x;\tau) R_{2 l + 1}(y;\tau) -
R_{2 l + 1}(x;\tau) R_{2 l }(y;\tau) \} 
\end{aligned}$$ and in terms of $S$ we define $$\begin{aligned}
\label{2.r}
\tilde{S}(x,y;\tau_x,\tau_y) := S(x,y;\tau_x,\tau_y) - g(x,y;\tau_x-\tau_y),
\quad \tau_x > \tau_y.
\end{aligned}$$ The formula for $\rho_{(n+m)}$ can now be stated. It reads [@NF98a] $$\begin{aligned}
\lefteqn{\rho_{(n+m)}(x_1^{(1)},\cdots,x_N^{(1)};\tau_1;
x_1^{(2)},\cdots,x_N^{(2)};\tau_2)} \nonumber \\ && = {\rm Tdet}
\left [ \begin{array}{cc} [f_1(x_j^{(1)},x_k^{(1)};\tau_1,\tau_1)
]_{n \times n}
& [f_2(x_j^{(1)},x_k^{(2)};\tau_1,\tau_2)]_{n \times m} \\{}
 [f_2^D(x_j^{(1)},x_k^{(2)};\tau_1,\tau_2)]_{n \times m}^T & 
 [f_1(x_j^{(2)},x_k^{(2)};\tau_2,\tau_2)
 ]_{m \times m} \end{array} \right ]
\label{2.s}
\end{aligned}$$ where $$f_1(x,y;\tau,\tau) := \left [ \begin{array}{cc}
S(x,y;\tau,\tau) & \tilde{I}(x,y;\tau,\tau) \\
D(x,y;\tau,\tau) & S(y,x;\tau,\tau) \end{array} \right ],$$ $$f_2(x,y;\tau_x,\tau_y) := \left [ \begin{array}{cc}
S(x,y;\tau_x,\tau_y) & \tilde{I}(x,y;\tau_x,\tau_y) \\
D(x,y;\tau_x,\tau_y) & \tilde{S}(y,x;\tau_y,\tau_x) \end{array} \right ]$$ and $$f_2^D(x,y;\tau_x,\tau_y) := \left [ \begin{array}{cc}
\tilde{S}(y,x;\tau_y,\tau_x) & - \tilde{I}(x,y;\tau_x,\tau_y) \\
-D(x,y;\tau_x,\tau_y) & S(x,y;\tau_x,\tau_y) \end{array} \right ].$$

If we denote the matrix in ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) by $X$, and note from the definitions ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) and ([\[2.q\]](#2.q){reference-type="ref" reference="2.q"}) that $$\begin{aligned}
\label{2.1a}
 \tilde{I}(x,y;\tau_x,\tau_y) = -   \tilde{I}(y,x;\tau_y,\tau_x), \quad
 D(x,y;\tau_x,\tau_y) = - D(y,x;\tau_y,\tau_x)
\end{aligned}$$ then we see that $ZX$ where $$\begin{aligned}
\nonumber
Z = {\bf 1}_{(n+m)} \otimes \left ( \begin{array}{cc}
0 & -1 \\ 1 & 0 \end{array} \right )
\end{aligned}$$ is an even dimensional antisymmetric matrix. Its Pfaffian is thus well defined, and in fact [@Dy70] $$\begin{aligned}
\label{2.1b}
{\rm Tdet} X = {\rm Pf}(ZX).
\end{aligned}$$ This formula can be used to compute the formula ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}).

## Alternative formulas and inter-relationships

As first noted in [@NF98], substitution of ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) in ([\[2.o\]](#2.o){reference-type="ref" reference="2.o"}) and use of ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) implies the decomposition $$\begin{aligned}
\label{2.1c}
S(x,y;\tau_x,\tau_y) = S_1(x,y;\tau_x,\tau_y) +  S_2(x,y;\tau_x,\tau_y)
\end{aligned}$$ where $$\begin{aligned}
\label{2.1d} 
 S_1(x,y;\tau_x,\tau_y) & = &
 \sqrt{w(x) w(y)} \sum_{\nu = 0}^{N-1}
  \frac{C_{\nu}(x) C_{\nu}(y)e^{-\gamma_\nu(\tau_x-\tau_y)}}{h_{\nu}}
\\
\label{2.1e}
S_2(x,y;\tau_x,\tau_y) & = &  \sqrt{w(x) w(y)}
\sum_{\nu = N}^{\infty} \sum_{k=0}^{N-1}
\frac{C_{\nu}(x)  e^{-\gamma_{\nu} \tau_x}}{h_{\nu}} 
\beta_{\nu k}
R_k(y;\tau_y
)
{\rm e}^{\gamma_k \tau_y}
\end{aligned}$$

Since $0 \leq \gamma_{1} < \gamma_{2} < \cdots$ (recall ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) and ([\[2.5\]](#2.5){reference-type="ref" reference="2.5"})) we see that for $N \rightarrow \infty$ and with all other parameters fixed, $S_{2} \rightarrow 0$ while $$\begin{aligned}
S_{1}\left(x, y; \tau_{x}, \tau_{y}\right) \rightarrow 
g\left(x, y; \tau_{x}-\tau_{y}\right) \, ,
\nonumber
\end{aligned}$$ assuming $\tau_{x} - \tau_{y} > 0$. The use of this result is that it shows $$\begin{aligned}
\label{2.1f}
\tilde{I}(x,y;\tau_x,\tau_y) = \int F(y',y;\tau_y) \Big (
g(x,y';\tau_x - \tau_y) - S(x,y';\tau_x,\tau_y) \Big ) \, dy'
\end{aligned}$$ valid for $\tau_{x} - \tau_{y} > 0$ (for $\tau_{x} - \tau_{y} < 0$ we can first use the first equation in ([\[2.1a\]](#2.1a){reference-type="ref" reference="2.1a"}), then apply ([\[2.1f\]](#2.1f){reference-type="ref" reference="2.1f"})).

We would also like to relate $D$ to $S$. Apparently this can be done naturally only when $\tau_{x} = 0$. Using the fact that $g(x, y; 0) = \delta(x - y)$ we see from ([\[2.d\]](#2.d){reference-type="ref" reference="2.d"}) and ([\[2.e\]](#2.e){reference-type="ref" reference="2.e"}) that $$\begin{aligned}
\label{2.1g}
F(x,y;0) = \left \{ \begin{array}{ll} {\rm sgn}(y-x), & \beta = 1 \\
2 {\partial \over \partial x} \delta (y-x), & \beta = 4. \end{array}
\right.
\end{aligned}$$ Recalling ([\[2.k\]](#2.k){reference-type="ref" reference="2.k"}), these formulas show $$\begin{aligned}
\nonumber
{d \over dx} \Phi_l(x;0) & = & 2 \sqrt{w(x)} R_k(x;0) \\
 \Phi_l(x;0) & = & - 2 {d \over dx} \Big (
\sqrt{w(x)} R_k(x;0) \Big ) \label{2.1g'}
\end{aligned}$$ in the two cases respectively. Thus for $\beta = 1$ initial conditions $$\begin{aligned}
\label{2.1h}
{d \over dx} S(x,y;0,\tau_y) = -2 D(x,y;0,\tau_y)
\end{aligned}$$ while for $\beta = 4$ initial conditions $$\begin{aligned}
\label{2.1i}
\int_y^x S(x',y;0,\tau_y) \, dx' = 2 D(x,y;0,\tau_y).
\end{aligned}$$

# The Laguerre ensemble

For the Laguerre ensemble the weight function $w(x)$ and constants $\gamma_{k}$ are given by ([\[2.5\]](#2.5){reference-type="ref" reference="2.5"}), while the monic orthogonal polynomials and corresponding normalization have the explicit form $$\begin{aligned}
\label{3.1}
C_n(x) = n! (-1)^n L_n^a(x), \quad h_n = \Gamma(n+1) \Gamma(n+a+1).
\end{aligned}$$ This applies independent of the particular initial condition (orthogonal symmetry ($\beta = 1$) or symplectic symmetry ($\beta = 4$)). However, the skew orthogonal polynomials $R_{k}(x;\tau)$ and the quantities $\beta_{jk}$ depend on the initial condition.

## $\beta = 1$ initial conditions

In this case the monic skew orthogonal polynomials for $\tau = 0$ are known to be [@NW91] $$\begin{aligned}
\label{3.2}
R_{2m}(x) & = & - (2m)! {d \over dx} L_{2m+1}^a (x) \: = \: (2m)!
\sum_{j=0}^{2m} {(-1)^j \over j!} C_j(x)  \nonumber \\
R_{2m+1}(x) & = & - (2m+1)!  L_{2m+1}^a (x)- (2m)! (a + 2m +1)
{d \over dx} L_{2m}^a(x) \nonumber \\
& = & C_{2m+1}(x) + (2m)!(a+2m+1) \sum_{j=0}^{2m-1}
{(-1)^j \over j!} C_j(x).
\end{aligned}$$ with corresponding normalization $$\begin{aligned}
\label{3.3}
r_n(0) = 4 \Gamma(2n+1) \Gamma(a + 2n+2).
\end{aligned}$$ These equations can readily be inverted. We find $$\begin{aligned}
\label{3.4}
C_{2m}(x) & = & R_{2m}(x) + (2m+a)! {m! \over (m+ a/2)!}
\sum_{j=0}^{m-1} {(j+a/2 + 1)! (2j + 2)! \over (j+1)! (2j+a+2)!} 
\nonumber \\
&& \times \Big ( {1 \over (2j+1)!} R_{2j+1}(x) -
{1 \over (2j)!} R_{2j}(x) \Big ) \nonumber \\
C_{2m+1}(x) & = & R_{2m+1}(x) + (2m+a+1)! {m! \over (m + a/2)!}
\sum_{j=0}^{m-1} {(j + a/2 + 1)! (2j + 2)! \over (j+1)! (2j + a + 2)!}
\nonumber \\
&& \times  \Big ( {1 \over (2j+1)!} R_{2j+1}(x) -
{1 \over (2j)!} R_{2j}(x) \Big )
\end{aligned}$$ (direct sustitution of ([\[3.2\]](#3.2){reference-type="ref" reference="3.2"}) into the right hand sides verifies the validity of these formulas).

According to the definition ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) with $\tau = 0$, we read off from ([\[3.4\]](#3.4){reference-type="ref" reference="3.4"}) that $$\begin{aligned}
\label{3.5}
\beta_{2m \, 2m} & = & \beta_{2m+1 \, 2m+1} = 1, \qquad
\beta_{2m+1 \, 2m} = 0 \nonumber \\
\beta_{\nu \, 2j} & = & - (\nu + a)! {1 \over (2j)!}
{[(\nu/2)]! \over ([\nu/2] + a/2)!}
{(j + a/2 + 1)! \over (j+1)!} {(2j+2)! \over (2j+a+2)!} \\
\beta_{\nu \, 2j+1} & = & - {1 \over 2j + 1} \beta_{\nu \, 2j},
\end{aligned}$$ where $\nu > 2j + 1$. A most significant feature of these formulas is that the dependence on $p$ and $l$ in $\beta_{pl}$ separates. In particular, for $n > N - 1$ and $N$ even we have $$\begin{aligned}
\label{3.6}
\beta_{p l} = \beta_{p \, N-1} \beta_{N-1 \, l}, \quad
0 \le l \le N-1, \: l \ne N-2.
\end{aligned}$$ Substituting this in the formula ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) for $S_{2}$, and making use of the final formula in ([\[3.5\]](#3.5){reference-type="ref" reference="3.5"}) in the case $(\nu, 2j + 1) = (p, N - 1)$ gives $$\begin{aligned}
\label{3.7}
S_2(x,y;\tau_x,\tau_y) & = & \sqrt{w(x) w(y)} \sum_{p=N}^\infty
{C_p(x) \over h_p} e^{-\gamma_p \tau_x} \beta_{p \, N-1}
\nonumber
\\ && \times \Big ( \sum_{l=0}^{N-1} \beta_{N-1 \, l} R_l(y;\tau_y)
e^{\gamma_l \tau_y} - (N-1) R_{N-2}(y;\tau_y) e^{\gamma_{N-2} \tau_y}
\Big ).
\end{aligned}$$ Now the sum over $l$ can be computed using ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}), while the sum over $p$ is given by ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}). Thus we have the explicit evaluation $$\begin{aligned}
\label{3.8}
S_2(x,y;\tau_x,\tau_y) & = & \sqrt{w(x)}
\Big ( {\Phi_{N-2}(x;\tau_x) e^{\gamma_{N-2} \tau_x} \over
r_{N/2 - 1}(0)}  - \sqrt{w(x)}
{C_{N-1}(x) e^{-\gamma_{N-1} \tau_x} \over h_{N-1}} \Big )
\nonumber \\
&& \times \Big ( C_{N-1}(y) e^{\gamma_{N-1} \tau_y} -
(N - 1) R_{N-2}(y;\tau_y) e^{\gamma_{N-2} \tau_y} \Big ).
\end{aligned}$$ In Appendix A we will show that in the limit $\tau_{x}, \tau_{y} \rightarrow 0$ this expression reduces down to the form of $S_{2}$ recently derived by Widom [@Wi98].

### The thermodynamic limit

In the neighbourhood of the spectrum edge at the origin, we will show that after introducing the scaled coordinates and parameters $X$ and $t$ according to $$\begin{aligned}
x  = \frac{X}{4N} \, \quad \quad \tau = \frac{t}{2N} 
\label{3.9}
\end{aligned}$$ (the numerical factors $1/4$ and $1/2$ are chosen for convenience), the distribution functions have a well defined large $N$ limit. In particular, the scaled distribution function ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}), to be denoted $\rho_{(n+m)}^{\rm hard}$, is given by $$\begin{aligned}
\label{n.1}
\lefteqn{\rho_{(n+m)}^{\rm hard}(X_1^{(1)},\dots,X_n^{(1)};t^{(1)};
X_1^{(2)},\dots,X_m^{(2)};t^{(2)})} \nonumber \\ &&
= \lim_{N \to \infty} \Big ( {1 \over 4N} \Big )^{n+m}
\rho_{(n+m)}\Big ( {X_1^{(1)}\over 4N},\dots,{X_n^{(1)}\over 4N};
{t^{(1)} \over 4N};
{X_1^{(2)} \over 4N},\dots,{X_m^{(2)}\over 4N};{t^{(2)}\over 2N}\Big )
\end{aligned}$$ From the formula ([\[2.1b\]](#2.1b){reference-type="ref" reference="2.1b"}) for Tdet it follows that $\rho_{(n+m)}^{\rm hard}$ is given by the formula ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) with the functions $S, \tilde{S}, \tilde{I}, D$ replaced by their scaled counterparts $$\begin{aligned}
S_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} {1 \over 4N}
S \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.2} \\
\tilde{S}_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} {1 \over 4N}
\tilde{S} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.3} \\
\tilde{I}_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty}
\tilde{I} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.4} \\
D_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} \Big (
{1 \over 4N} \Big )^2
D \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.5}
\end{aligned}$$ where the subscripts 1 indicate $\beta = 1$ initial conditions.

Note that it was permissable to multiply ${1 \over 4N} \tilde{I}$ by $4N$ and divide ${1 \over 4N} D$ by $4N$ in the above definitions because of an invariance property of the Tdet formula ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}). Thus in general each $2 \times 2$ block $Q_{jk}$ can be replaced by the $2 \times 2$ block $$A^{-1} Q_{jk} A. \label{n.6'}$$ Choosing $$A = \left ( \begin{array}{cc} 1/\sqrt{4N} & 0 \\ 0 & \sqrt{4N} \end{array}
\right )$$ then transforms ${1 \over 4N} \tilde{I}$ and ${1 \over 4N} D$ as required.

### Asymptotics of $S(x, y; \tau_{x}, \tau_{y})$

Let us first compute the asymptotic behaviour of $\Phi_{2k-2}(x; \tau)$. This is required in the computation of $S_{2}$ (with $2k = N$), and also $\tilde{I}$. From the expansion ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.5\]](#3.5){reference-type="ref" reference="3.5"}) for the quantities $C_{\nu}(x)$, $h_{\nu}$ and $\beta_{\nu 2k-2}$ therein we have $$\begin{aligned}
\label{3.10}
\lefteqn{
\Phi_{2k - 2}(x;\tau) e^{\gamma_{2k-2} \tau} = \sqrt{w(x)}
r_{k-1}(0) \bigg ( - {L_{2k-1}^a (x) \over (2k - 1 + a)!} e^{-\gamma_{2k-1}
\tau}} \nonumber \\ &&
+ {(k + a/2)! (2k)! \over (2k - 1)! (2k + a)! k!}
\sum_{\nu = k}^\infty {\nu! \over (\nu + a/2)!}
\Big ( L_{2 \nu}^a(x) e^{-\gamma_{2 \nu} \tau} -
L_{2 \nu + 1}^a (x) e^{- \gamma_{2 \nu + 1} \tau} \Big ) \bigg ).
\end{aligned}$$ We now proceed to estimate the summand for large $\nu$.

From Stirling's formula $$\begin{aligned}
\frac{\nu !}{(\nu + a/2)!} \mathop{\sim}\limits_{\nu \to \infty}
\frac{1}{\nu^{a/2}} \,  .
\nonumber
\end{aligned}$$ For the second factor in the summand we write $$\begin{aligned}
\lefteqn{
L^{a}_{2\nu}(x) e^{-\gamma_{2\nu}\tau}  - 
L^{a}_{2\nu + 1}(x) e^{-\gamma_{2\nu + 1}\tau}} \nonumber \\
&& =  
 - e^{-\gamma_{2\nu + 1}\tau} \left( 
L^{a}_{2\nu + 1}(x) - L^{a}_{2\nu}(x) - L^{a}_{2\nu}(x)
(e^{-\tau(\gamma_{2\nu} - \gamma_{2\nu + 1})} - 1) \right) \,  .
\end{aligned}$$ Using the facts that $$\begin{aligned}
e^{\tau(\gamma_{2\nu} - \gamma_{2\nu + 1})} = e^{-2\tau}\, ,   \quad  \quad  
L^{a}_{2\nu + 1}(x) - L^{a}_{2\nu}(x) = L^{a-1}_{2\nu + 1}(x) \,  ,
\label{3.11}
\end{aligned}$$ and the asymptotic formula $$\begin{aligned}
\sqrt{w(x)}\,  L_{n}^{a}(x) 
\mathop{\sim}\limits_{n \to \infty}  n^{a/2} 
J_{a}\left(2\sqrt{nx}\right) 
\label{3.12}
\end{aligned}$$ where $J_{a}(z)$ denotes the Bessel function, we see that $$\begin{aligned}
\lefteqn{\left. \sqrt{w(x)}\, \frac{\nu !}{(\nu + a/2)!} 
 \left(L_{2\nu}^{a}(x) e^{-\gamma_{2\nu}\tau}  - 
L^{a}_{2\nu + 1}(x) e^{-\gamma_{2\nu + 1} \tau} \right)
\right|_{x = X/4N \atop \tau = t/2N}} \nonumber \\
 & \sim  &  -\nu^{-a/2} e^{-(2\nu /N)t} 
\bigg( \sqrt{\frac{X}{4N}}(2\nu)^{(a-1)/2} 
J_{a-1}\Big(\sqrt{\frac{2jX}{N}}\Big) + \frac{t}{N} (2\nu)^{a/2} 
J_{a}\Big(\sqrt{\frac{2jX}{N}}\Big)\bigg) 
\nonumber \\
& =  & -\frac{2^{a/2}}{N}u^{-a/2}\frac{d}{du}
\left(e^{-ut} u^{a/2} J_{a}\left(\sqrt{uX}\right) \right), \quad \quad 
u := 2\nu /N \,  .
\label{3.13}
\end{aligned}$$ (The equality is obtained by making use of a suitable differentiation formula for the Bessel function).

Substituting ([\[3.13\]](#3.13){reference-type="ref" reference="3.13"}) in ([\[3.10\]](#3.10){reference-type="ref" reference="3.10"}) gives the leading order behaviour of the sum over $\nu$ as a Riemann integral. Furthermore, use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) gives $$\begin{aligned}
\left. \sqrt{w(x)} \, \frac{L^{a}_{2k - 1}(x)}{(2k - 1 + a)!}\,
 e^{-\gamma_{2k-1}\tau}\right|_{x = X/4N \atop \tau = t/2N}
\sim  
\frac{N^{-a/2}}{(2k - 1)!} \, s^{-a/2} J_{a}\left(\sqrt{sX}\right)\, e^{-st},
\label{3.14} 
\end{aligned}$$ $s := 2k/N$, so in total we have $$\begin{aligned}
\Phi_{2k-2}\left(\frac{X}{4N}; \frac{t}{2N}\right) e^{\gamma_{2k-2}t/2N} & \sim &
r_{k-1}(0) \frac{N^{-a/2}}{(2k - 1)!} 
\bigg ( \frac{1}{2}\left( 1 - 2s^{-a/2}\right) J_{a}\left(\sqrt{sX}\right) 
e^{-st}  \nonumber \\
&  &   -  
\frac{a}{4} \int_{s}^{\infty} \frac{e^{-ut}}{u} J_{a}\left(\sqrt{uX}\right) 
du \bigg )  \,  .
\label{3.15}
\end{aligned}$$ The expansions ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) and ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}) with $2k = N$ and thus $s = 1$ suffice to specify the $x$-dependent factor in ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}). Thus we have $$\begin{aligned}
\lefteqn{\left. 
\left(\frac{\Phi_{N-2}(x; \tau_{x})}{r_{N/2 - 1}(0)}  -  \sqrt{w(x)}\, 
\frac{C_{N-1}(x)e^{-\gamma_{N-1} \tau_{x}}}{h_{N-1}}\right) 
\right|_{x = X/4N \atop \tau_{x} = t_{X}/2N}}
\nonumber \\ 
& & \sim  \frac{N^{-a/2}}{2(N-1)!} \left( 
J_{a}\left(\sqrt{X}\right) e^{-t_{X}} - \frac{a}{2} \int_{1}^{\infty} 
\frac{e^{-ut_{X}}}{u} J_{a} \left( \sqrt{uX}\right) \, du \right)  \,  . 
\label{3.16}
\end{aligned}$$

Next we will compute the asymptotic form of $R_{2j}(y; \tau_{y})$. In the case $2j = N - 2$ this is required for the $y$-dependent factor in ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}). From ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.2\]](#3.2){reference-type="ref" reference="3.2"}) and ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) we see that $$\begin{aligned}
R_{2j}(y; \tau )\, e^{\gamma_{2j} \tau} = (2j)! \sum_{l=0}^{2j}L_{l}^{a}(y)\, 
e^{\gamma_{l}\tau} \,  . 
\label{3.16'}
\end{aligned}$$ The asymptotic form of this expression is deduced by using ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) to approximate the summand, which leads to the result $$\begin{aligned}
\left. \sqrt{w(y)} R_{2j}(y; \tau_{y}) e^{\gamma_{2j} \tau_{y}}
\right|_{y = Y/4N \atop \tau_{y} = t_{Y}/2N}
\sim (2j)! \, 
N^{1+a/2} \int_{0}^{s}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, dv 
\,  , 
\label{3.17}
\end{aligned}$$ where here $s = 2j/N$. Setting $s = 1$ and making further use of ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) we see that $$\begin{aligned}
\lefteqn{\sqrt{w(y)} \left(C_{N-1}(y)e^{\gamma_{N-1}\tau_{y}} - 
(N-1) R_{N-2}(y; \tau_{y}) e^{\gamma_{N-2} \tau_{y}}\right)}
\nonumber \\ & & \hspace*{2cm} \sim  -(N-1)! N^{1+a/2} 
\int_{0}^{1}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, dv \,   .
\label{3.18}
\end{aligned}$$ Combining ([\[3.16\]](#3.16){reference-type="ref" reference="3.16"}) and ([\[3.18\]](#3.18){reference-type="ref" reference="3.18"}) in the formula ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}) for $S_{2}$ gives $$\begin{aligned}
S_{2}\left(\frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} 
\right) 
& \sim  & 
\frac{N}{2}\left( - e^{-t_{X}} J_{a}\left(\sqrt{X}\right) + \frac{a}{2} 
\int_{1}^{\infty} \frac{e^{-ut_{X}}}{u}J_{a}\left(\sqrt{uX}\right)\, du\right) 
\nonumber \\  &  &  \times 
\left( \int_{0}^{1}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, 
dv \right)\,  .
\label{3.19}
\end{aligned}$$

The asymptotics of $S_{1}$ can be determined by using ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula to approximate the integrand. This gives $$\begin{aligned}
S_{1}\left(\frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} 
\right) 
\sim  N \int_{0}^{1} J_{a}\left(\sqrt{uX}\right)\,J_{a}\left(\sqrt{uY}\right)\, 
e^{-u(t_{X} - t_{Y})}\, du \,  . 
\label{3.20}
\end{aligned}$$ Since $S$ is defined as the sum of $S_{1}$ and $S_{2}$, its asymptotic form is given by the sum of ([\[3.19\]](#3.19){reference-type="ref" reference="3.19"}) and ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}). Substituting into ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"}) gives $$\begin{aligned}
\label{3.20'} \lefteqn{
S_1^{\rm hard}(X,Y;t_X,t_Y) = {1 \over 4} \int_0^1 J_a(\sqrt{uX})
J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du} \nonumber \\ &&
+ {1 \over 8} \Big ( - e^{-t_X} J_a(\sqrt{X}) + {a \over 2}
\int_1^\infty {e^{-u t_X} \over u} J_a(\sqrt{uX}) \, du \Big )
\int_0^1 dv \, J_a(\sqrt{vY}) e^{t_Y v} v^{a/2}.
\end{aligned}$$

### Asymptotics of $\tilde{I} (x, y; \tau_{x}, \tau_{y})$

So as to induce a cancellation at leading order, we first perform some minor manipulation to the definition ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}), by way of subtracting and adding $(2l + 1) e^{\gamma_{2l} (\tau_{x} + \tau_{y})} \Phi_{2l}(x; \tau_{x}) 
\Phi_{2l}(y; \tau_{y})$ to the summand, so that it reads $$\begin{aligned}
\tilde{I} (x, y; \tau_{x}, \tau_{y}) & = & \sum_{l = N/2}^{\infty} 
\frac{1}{r_{l}(0)} \left\{ e^{\gamma_{2l}\tau_{x}} \Phi_{2l}(x; \tau_{x})
\left( e^{\gamma_{2l+1}\tau_{y}} \Phi_{2l+1}(y; \tau_{y}) \right. \right. 
\nonumber \\
&  &  \left. \left. - (2l + 1) e^{\gamma_{2l}\tau_{y}} \Phi_{2l}(y; \tau_{y}) \right) - 
(x \leftrightarrow y) \right\} \,  . 
\label{3.21}
\end{aligned}$$ The asymptotics of $e^{\gamma_{2l} \tau_{x}} \Phi_{2l}(x; \tau_{x})$ can be read off from ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}). For the $y$-dependent factor of the first term of the summand we note from the definitions ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.5\]](#3.5){reference-type="ref" reference="3.5"}) that $$\begin{aligned}
\lefteqn{e^{\gamma_{2l+1}\tau} \Phi_{2l+1}(y; \tau) 
- (2l + 1) e^{\gamma_{2l}\tau} \Phi_{2l}(y; \tau)} \nonumber \\ 
& & = \sqrt{w(y)}\,  r_{l}(0) \left( (2l+1)
\frac{L_{2l+1}^{a}(y)e^{-\gamma_{2l+1}\tau}}{(2l+1+a)!} - 
\frac{L_{2l}^{a}(y)e^{-\gamma_{2l}\tau}}{(2l+a)!}\right) \,  . 
\nonumber
\end{aligned}$$ Thus, using ([\[3.3\]](#3.3){reference-type="ref" reference="3.3"}) and the asymptotic formula ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) we have $$\begin{aligned}
 \lefteqn{\Big( e^{\gamma_{2l+1}\tau} \Phi_{2l+1}(y; \tau) 
- (2l + 1) e^{\gamma_{2l}\tau} \Phi_{2l}(y; \tau) \Big)
\bigg|_{y = Y/4N \atop \tau = t/2N}} \nonumber \\
&  &  \sim 4(2l+1)! N^{-1 + a/2} \left\{ 
\frac{d}{ds}\left(e^{-st}J_{a}\left(\sqrt{sY}\right)\right) - 
as^{-1+a/2}J_{a}\left(\sqrt{sY}\right)e^{-st}\right\}\,  , \quad  s = 2l/N \,  . 
\nonumber
\end{aligned}$$ Substituting this result, together with ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}) (after replacing $k$ by $l + 1$) in ([\[3.21\]](#3.21){reference-type="ref" reference="3.21"}) shows that $$\begin{aligned}
\tilde{I}_1^{\rm hard}(X,Y;t_X,t_Y) =
 \int_{1}^{\infty}  ds \left\{ \left(1- \frac{2}{s^{a/2}}\right)
J_{a}\left(\sqrt{sX}\right) e^{-st_{X}} - \frac{a}{4}\int_{s}^{\infty} 
\frac{e^{-ut_{X}}}{u} J_{a}\left(\sqrt{uX}\right)\,du \right\} 
\nonumber \\   \times
\left\{ \frac{d}{ds}\left(e^{-st_{y}}J_{a}\left(\sqrt{sY}\right)\right) - 
as^{-1+a/2}J_{a}\left(\sqrt{sY}\right)
e^{-st_{Y}}\right\} - (X \leftrightarrow Y) \, .
\label{3.22}
\end{aligned}$$

### Asymptotics of $g(x, y; \tau)$

According to ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) and ([\[2.5\]](#2.5){reference-type="ref" reference="2.5"}) $$\begin{aligned}
g(x, y; \tau) = (xy)^{a/2}e^{-(x+y)/2} \sum_{j=0}^{\infty} \frac{j!}{(j+a)!} 
L_{j}^{a}(x)L_{j}^{a}(y) e^{-2(j+(a+1)/2)\tau} \, . 
\label{3.22a}
\end{aligned}$$ This summation can be evaluated in closed form [@Er], giving $$\begin{aligned}
g(x, y; \tau) = e^{-(x+y)/2}e^{-(2a+1)\tau}\left(1 - e^{-2\tau}\right)^{-1} 
\exp \left( -\frac{e^{-2\tau}}{1 - e^{-2\tau}}(x+y) \right) 
I_{a}\left(2\frac{\sqrt{xy}\, e^{-\tau}}{1 - e^{-2\tau}}\right)\, ,
\nonumber
\end{aligned}$$ where $I_a$ denotes the Bessel function of pure imaginary argument. Consequently $$\begin{aligned}
g\left( \frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X} - t_{Y}}{2N}\right) \sim 
\frac{N}{t_{X}-t_{Y}} 
\exp \left( -\frac{X+Y}{t_{X} - t_{Y}} \right) 
I_{a}\left(\frac{\sqrt{XY}}{2(t_{X} - t_{Y})}\right) \,  .
\label{3.22'}
\end{aligned}$$

Alternatively, proceeding as in the derivation of ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) we can deduce from ([\[3.22a\]](#3.22a){reference-type="ref" reference="3.22a"}) that $$\label{m.1}
g\Big ({X \over 4N}, {Y \over 4N}; {t_X - t_Y \over 2N} \Big ) \sim
N \int_0^\infty J_a(\sqrt{uX})  J_a(\sqrt{uY}) e^{-u (t_X - t_Y)} \, du.$$ The immediate merit of this representation is that when substituted in ([\[2.r\]](#2.r){reference-type="ref" reference="2.r"}), partial cancellation occurs with ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}). Adding the result to ([\[3.19\]](#3.19){reference-type="ref" reference="3.19"}) and substituting in ([\[n.3\]](#n.3){reference-type="ref" reference="n.3"}) gives $$\begin{aligned}
\label{m.2} \lefteqn{
\tilde{S}_1^{\rm hard}(X,Y;t_X,t_Y) = - {1 \over 4} \int_1^\infty J_a(\sqrt{uX})
J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du} \nonumber \\ &&
+ {1 \over 8} \Big ( - e^{-t_X} J_a(\sqrt{X}) + {a \over 2}
\int_1^\infty {e^{-u t_X} \over u} J_a(\sqrt{uX}) \, du \Big )
+ \int_0^1 dv \, J_a(\sqrt{vY}) e^{t_Y v} v^{a/2}.
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

According to ([\[2.q\]](#2.q){reference-type="ref" reference="2.q"}) $D$ is defined in terms of $\{R_{j}(x; \tau)\}$. Now $R_{2j}(y; \tau)$ is specified by ([\[3.16\'\]](#3.16'){reference-type="ref" reference="3.16'"}). Deriving the analogous formula for $R_{2j+1}(x; \tau)$, which follows from ([\[3.2\]](#3.2){reference-type="ref" reference="3.2"}), ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) and ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}), we see that $$\begin{aligned}
R_{2j+1}(x; \tau) e^{\gamma_{2j+1}\tau}
& =  &  -(2j+1)! L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau} \nonumber \\  & & 
\quad \quad + (2j+a + 1) R_{2j}(x; \tau) e^{\gamma_{2j}\tau} \,  .
\nonumber
\end{aligned}$$ Hence $$\begin{aligned}
\lefteqn{\left( e^{\gamma_{2j+1}\tau_{x}} R_{2j+1}(x; \tau_{x}) 
e^{\gamma_{2j}\tau_{y}} R_{2j}(y; \tau_{y}) - (x \leftrightarrow y) \right) =} 
\nonumber \\ 
& & \left(-(2j+1)!  L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau_{x}} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau_{x}}\right) 
R_{2j}(y; \tau_{y}) e^{\gamma_{2j}\tau_{y}}  - (x \leftrightarrow y)  \,  .
\nonumber
\end{aligned}$$ Now the asymptotic form of $R_{2j}(y; \tau_{y})$ is specified by ([\[3.17\]](#3.17){reference-type="ref" reference="3.17"}) while we see from ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) that $$\begin{aligned}
\lefteqn{\sqrt{w(x)} \left(-(2j+1)!  
L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau_{x}} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau_{x}}\right)  
\bigg|_{x = X/4N \atop \tau_{x} = t_{X}/2N}} \nonumber \\ & & \quad \quad \quad 
\sim -2 (2j+1)! e^{st_{X}} (Ns)^{a/2} J_{a}\left( \sqrt{sX}\right) \, , \quad s = 2j/N \,  .
\nonumber
\end{aligned}$$ Making use also of the explicit form ([\[3.3\]](#3.3){reference-type="ref" reference="3.3"}) of $r_{n}(0)$ and using the definition ([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) we thus find $$\begin{aligned}
\lefteqn{
D_1^{\rm hard}(X,Y;t_X,t_Y) = - 4^{-3}  } \nonumber \\ && \times
\left\{ \int_{0}^{1}ds\, e^{st_{X}} s^{-a/2}  
J_{a}\left( \sqrt{sX}\right)  
\int_{0}^{s}dv \, e^{vt_{Y}}v^{a/2}J_{a}\left( \sqrt{vY}\right) 
- (X \leftrightarrow Y) \right\} \,  .
\label{3.23}
\end{aligned}$$

## $\beta = 4$ initial conditions

The method of evaluation of the quantities $S, \, \tilde{I}$, and $D$ for the Laguerre ensemble in the case of initial conditions with symplectic symmetry ($\beta = 4$) closely parallels that just given for $\beta = 1$ initial conditions. First, we note from previous work [@NW91] that the monic skew orthogonal polynomials at $\tau = 0$ have the explicit form $$\begin{aligned}
R_{2j}(x) &=& 2^{2j}j!\left(j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{(2l)!}{l! \, 2^{2l}} \frac{1}{\left(l + (a-1)/2\right)!} L_{2l}^{a-1}(x) 
\nonumber \\
& = &  2^{2j}j!\left(j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{1}{l! \, 2^{2l} \left(l + (a-1)/2\right)!} \left(C_{2l}(x) + 2lC_{2l-1}(x) \right) \,  , 
\nonumber \\
R_{2j+1}(x) &=& -(2j+1)! \,   L_{2j+1}^{a-1}(x) 
\nonumber \\
& = &  C_{2j+1}(x) + (2j+1)C_{2j}(x)  \,   , 
\label{3.24}
\end{aligned}$$ with corresponding normalization $$\begin{aligned}
r_{n}(0) = \Gamma(2n+2)\, \Gamma(a + 2n + 1) \,   . 
\label{3.25}
\end{aligned}$$

The inversion of these equations gives that the quantities $\beta_{n\, j}$ in ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) have the explicit values $$\begin{aligned}
\beta_{2m\, 2m} &=& \beta_{2m+1\, 2m+1} = 1 \, , \quad \quad  
\beta_{2m+1\, 2m} = - (2m+1) \,   ,   \nonumber \\ 
\beta_{\nu\, 2j+1} &=& (-1)^{\nu + 1} \frac{\nu !}{(2j+1)!} \,  ,  \quad \quad 
\beta_{\nu\, 2j} = a \,  \beta_{\nu\, 2j+1} \,   , 
\label{3.26}
\end{aligned}$$ for $\nu > 2j + 1$. Thus the factorization formula ([\[3.6\]](#3.6){reference-type="ref" reference="3.6"}) again holds, which when substituted in ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) and after making use of the explicit value of $\beta_{N-1\, N-2}$ and $\beta_{p\, N-1}$, and ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}), implies $$\begin{aligned}
S_{2}(x, y; \tau_{x}, \tau_{y}) & = & \sqrt{w(x)w(y)} \sum_{p = N}^{\infty} 
\frac{C_{p}(x)}{h_{p}}\, e^{-\gamma_{p}\tau_{x}}\, \beta_{p\, N-1} 
\left\{ C_{N-1}(y) e^{\gamma_{N-1}\tau_{y}} \right. \nonumber \\
& & \quad \left. + (a + N-1) R_{N-2}(y; \tau_{y}) 
e^{\gamma_{N-2}\tau_{y}} \right\} \,  . 
\nonumber
\end{aligned}$$ The sum over $p$ is, after minor manipulation, formally identical to the sum over $p$ in ([\[3.7\]](#3.7){reference-type="ref" reference="3.7"}), so it can be summed using ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}). Thus $S_{2}$ has the explicit form $$\begin{aligned}
S_{2}(x, y; \tau_{x}, \tau_{y}) & = & \sqrt{w(y)} \left( 
\frac{\Phi_{N-2}(x; \tau_{x})}{r_{N/2 -1}(0)} e^{\gamma_{N-2}\tau_{x}} - 
\sqrt{w(x)} \frac{C_{N-1}(x)}{h_{N-1}} e^{-\gamma_{N-1}\tau_{x}} \right) 
\nonumber \\
& & \times 
\left(C_{N-1}(y) e^{\gamma_{N-1}\tau_{y}} + (a + N-1) R_{N-2}(y; \tau_{y}) 
e^{\gamma_{N-2}\tau_{y}} \right) \,  . 
\label{3.27}
\end{aligned}$$ As with ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}), in the limit $\tau_{x}, \tau_{y} \rightarrow 0$ this reduces down to the form of $S_{2}$ derived by Widom [@Wi98] in the static $\beta = 4$ theory. The details of the verification are given in Appendix A.

### The thermodynamic limit

Although the scaled distribution function is still given by ([\[n.1\]](#n.1){reference-type="ref" reference="n.1"}), the required scaling of the elements of the quaternion determinant ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) differs slightly from the formulas ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"})--([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) appropriate with $\beta = 1$ initial conditions. In particular ([\[n.4\]](#n.4){reference-type="ref" reference="n.4"}) and ([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) should now read $$\begin{aligned}
\tilde{I}_4^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty}
\Big ( {1 \over 4N} \Big )^2
\tilde{I} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.6} \\
D_4^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} 
D \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.7}
\end{aligned}$$ while ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"}) and ([\[n.3\]](#n.3){reference-type="ref" reference="n.3"}) remain the same, except that the subscripts 1 on the right hand sides should be replaced by 4.

### Asymptotics of $S(x, y; \tau_{x}, \tau_{y})$

From the expansion ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.26\]](#3.26){reference-type="ref" reference="3.26"}) we have $$\begin{aligned}
\Phi_{2k-2}(x; \tau)e^{\gamma_{2k-2}\tau} 
= -\frac{r_{k-1}(0) \sqrt{w(x)}}{(2k-1)!} 
\sum_{\nu = 2k-1}^{\infty} \frac{L_{\nu}^{a}(x)\, \nu !}{(\nu + a)!} 
\, e^{-\gamma_{\nu}\tau}\, . 
\nonumber
\end{aligned}$$ Applying the asymptotic expansion ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula shows that $$\begin{aligned}
\Phi_{2k-2}\left(\frac{X}{4N}; \frac{t}{2N}\right)
e^{\gamma_{2k-2} t/2N}  \sim -\frac{r_{k-1}(0)}{(2k-1)!} N^{1 - a/2} 
\int_{u}^{\infty} dr \, r^{-a/2} e^{-rt} J_{a}\left(\sqrt{rX}\right)  \, , 
\label{3.28}
\end{aligned}$$ where $u := 2k/N$. Setting $u = 1$ gives the asymptotic form of $\Phi_{N-2}(x; \tau_{x})/r_{N/2 -1}(0)$ as required in ([\[3.27\]](#3.27){reference-type="ref" reference="3.27"}), and comparison with ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) shows that this term dominates the one involving $C_{N-1}(x)$. Thus here the formula ([\[3.16\]](#3.16){reference-type="ref" reference="3.16"}) applies with the right hand side replaced by $$\begin{aligned}
- \frac{N^{1 - a/2}}{(N-1)!}  
\int_{u}^{\infty} dr \, r^{-a/2} e^{-rt} J_{a}\left(\sqrt{rX}\right) \,   .
\label{3.29}
\end{aligned}$$ For the $y$-dependent factor in ([\[3.27\]](#3.27){reference-type="ref" reference="3.27"}), we note from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}), and ([\[3.16\'\]](#3.16'){reference-type="ref" reference="3.16'"}) that $$\begin{aligned}
\lefteqn{R_{2j}(y; \tau)  e^{\gamma_{2j}\tau} 
=} \nonumber \\
& &  2^{2j}j!  \left( j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{(2l)!}{l!\, 2^{2l}} \frac{1}{(l + (a-1)/2)!} 
\left( L_{2l}^{a}(y) e^{\gamma_{2l}\tau} - L_{2l-1}^{a}(y) e^{\gamma_{2l-1}\tau}\right)  .
\nonumber 
\end{aligned}$$ Use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula gives for the corresponding asymptotic form $$\begin{aligned}
\lefteqn{\left. \frac{1}{(2j+1)!}\sqrt{w(y)} R_{2j}(y; \tau) e^{\gamma_{2j}\tau}
\right|_{y = Y/4N \atop \tau = t/2N}} \nonumber \\
& \sim & \frac{N^{a/2-1}}{2} s^{-1 + a/2} \int_{0}^{s} 
u^{-a/2} \frac{d}{du} \left( e^{ut} u^{a/2} J_{a}\left(\sqrt{uY}\right) \right) du \, , 
\quad s := 2j/N\,  . 
\label{3.30}
\end{aligned}$$ Adding this with $s = 1$ to the asymptotic form of $\sqrt{w(y)} 
C_{N-1}(y) e^{\gamma_{N-1} \tau_{y}}/(N-1)!$ deduced from ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}), and multiplying the result by ([\[3.29\]](#3.29){reference-type="ref" reference="3.29"}) gives that $$\begin{aligned}
\lefteqn{S_{2}\left(\frac{X}{4N}, 
\frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} \right) 
\sim  -N\int_{1}^{\infty} dr \, r^{-a/2} e^{-rt_{X}}J_{a}\left(\sqrt{rX}\right)}
\nonumber \\ &  & \times
\left( - J_{a}\left(\sqrt{Y}\right) e^{t_{Y}} + 
\frac{1}{2} \int_{0}^{1}u^{-a/2} \frac{d}{du}\left( e^{u t_{Y}} u^{a/2} 
J_{a}\left(\sqrt{uY}\right)\right) \,du \right)\,  .
\label{3.31}
\end{aligned}$$

The asymptotic form of $S_{1}$ can be read off from ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) since according to its definition ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}), its value is the same for $\beta = 1$ and 4. The asymptotic form of $S$ itself is thus given by the sum of ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) and ([\[3.31\]](#3.31){reference-type="ref" reference="3.31"}). Thus we have $$\begin{aligned}
\lefteqn{
S_4^{\rm hard}(X,Y;t_X,t_Y) = } \nonumber \\ &  & {1 \over 4} \int_0^1
J_a(\sqrt{uX}) J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du
- {1 \over 4} \int_1^\infty dr \, r^{-a/2} e^{-r t_X}
J_a(\sqrt{rX}) \nonumber \\ &&
\times \bigg ( - J_a(\sqrt{Y}) e^{t_Y} + {1 \over 2}
\int_0^1 u^{-a/2} {d \over du} \Big ( e^{ut_Y} u^{a/2}
J_a(\sqrt{uY}) \Big ) du \bigg ) \label{m.3}
\end{aligned}$$

### Asymptotics of $\tilde{S}(x, y; \tau_{x}, \tau_{y})$

The single particle Green function $g$ as specified by ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) is independent of the initial condition, so me can use the formula ([\[m.1\]](#m.1){reference-type="ref" reference="m.1"}). Dividing by $4N$ and subtracting from ([\[m.3\]](#m.3){reference-type="ref" reference="m.3"}) shows $$\begin{aligned}
\lefteqn{
\tilde{S}_4^{\rm hard}(X,Y;t_X,t_Y)} 
\nonumber \\ && =  - {1 \over 4} \int_1^\infty
J_a(\sqrt{uX}) J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du
- {1 \over 4} \int_1^\infty dr \, r^{-a/2} e^{-r t_X}
J_a(\sqrt{rX}) \nonumber \\ &&
\times \bigg ( - J_a(\sqrt{Y}) e^{t_Y} + {1 \over 2}
\int_0^1 u^{-a/2} {d \over du} \Big ( e^{ut_Y} u^{a/2}
J_a(\sqrt{uY}) \Big ) du \bigg ) \label{m.4}
\end{aligned}$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

The definition ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) gives that $\tilde{I}$ is defined in terms of $\{\Phi_{l}(x; \tau)\}$. The asymptotic form of $\Phi_{2k-2}(x; \tau)$ is given by ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}). Instead of deriving an analogous expression for $\Phi_{2k-1}(y; \tau)$, we note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[3.26\]](#3.26){reference-type="ref" reference="3.26"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and the formula ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}) for $\Phi_{2k-2}$ that $$\begin{aligned}
\lefteqn{\Phi_{2k-1}(y; \tau)e^{\gamma_{2k-1}\tau} =} \nonumber \\ 
& - & \frac{\sqrt{w(y)}\, r_{k-1}(0)}{(2k-2 + a)!} 
\left( L_{2k-2}^{a}(y) 
e^{-\gamma_{2k-2}\tau} + L_{2k-1}^{a}(y) e^{-\gamma_{2k-1}\tau}
\right) - a \Phi_{2k-2}(y; \tau) \,  . 
\label{3.32}
\end{aligned}$$ Thus $$\begin{aligned}
\lefteqn{e^{\gamma_{2l}\tau_{x}}\Phi_{2l}(x; \tau_{x})
e^{\gamma_{2l+1}\tau_{y}}\Phi_{2l+1}(y; \tau_{y}) - (x \leftrightarrow y) 
=}  \nonumber \\ 
&  &  e^{\gamma_{2l}\tau_{x}}\Phi_{2l}(x; \tau_{x})
\left(-\frac{\sqrt{w(y)}\, r_{l}(0)}{(2l + a)!} \right)
\left( L_{2l}^{a}(y) 
e^{-\gamma_{2l}\tau_{y}} + L_{2l+1}^{a}(y) e^{-\gamma_{2l+1}\tau_{y}}
\right) - ( x \leftrightarrow y)   .  \nonumber \\
\label{3.33}
\end{aligned}$$ According to ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and ([\[3.25\]](#3.25){reference-type="ref" reference="3.25"}), the product of the second and third factors in the first term have the same leading asymptotic behaviour $$\begin{aligned}
-(2l+1)! \, 
4(vN)^{a/2} J_{a}\left(\sqrt{vY}\right)\, 
e^{-v\tau} \,  , \quad  v = 2l/N \, .  
\label{3.34}
\end{aligned}$$ Multiplying this by ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}) (with $k \mapsto l + 1$) and substituting in ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) gives that the desired asymptotic form is $$\begin{aligned}
\lefteqn{I_4^{\rm hard}(X,Y;t_X,t_Y)} \nonumber  \\
&& = 
{1 \over 4} \int_{1}^{\infty}\left\{
\int_{v}^{\infty}dr \, 
r^{-a/2}  e^{-r t_{X}} J_{a}\left(\sqrt{rX}\right)\right\}
v^{a/2} J_{a}\left(\sqrt{vY}\right) e^{-vt_{Y}} \, dv - (X \leftrightarrow Y)  .
\label{3.35}
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here we require the asymptotic form of $\{R_{l}(x; \tau)\}$. For $l$ even this is given by ([\[3.30\]](#3.30){reference-type="ref" reference="3.30"}). On the other hand, for $l$ odd we see from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.24\]](#3.24){reference-type="ref" reference="3.24"}) that $$\begin{aligned}
R_{2j+1}(y; \tau)e^{\gamma_{2j+1}\tau} = -(2j+1)! 
\left( L_{2j+1}^{a}(y) 
e^{\gamma_{2j+1}\tau} - L_{2j}^{a}(y) e^{\gamma_{2j}\tau}
\right)  \,  . 
\label{3.36}
\end{aligned}$$ Use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) shows $$\begin{aligned}
\left. \sqrt{w(y)} \,  R_{2j+1}(y; \tau) e^{\gamma_{2j+1}\tau}
\right|_{y = Y/4N \atop \tau = t/2N} 
\sim -(2j+1)! N^{a/2 - 1} \frac{d}{ds}\left( 
e^{st} s^{a/2} J_{a}\left(\sqrt{sY}\right) \right)  \, , 
\label{3.37}
\end{aligned}$$ $s := 2j/N$. Multiplying this by $(2j + 1)!$ times ([\[3.30\]](#3.30){reference-type="ref" reference="3.30"}) (with $Y$ replaced by $X$) and dividing by ([\[3.25\]](#3.25){reference-type="ref" reference="3.25"}) we thus have $$\begin{aligned}
D_4^{\rm hard}(X,Y;t_X,t_Y)
& \sim  &  -\frac{1}{4} \int_{0}^{1}ds\, s^{-a/2} \left\{
\int_{0}^{s} u^{-a/2}  \frac{d}{du}\left( 
e^{u t_{X}} u^{a/2} J_{a}\left(\sqrt{uX}\right) \right) du \right\} 
\nonumber \\  &  & \quad \times 
\frac{d}{ds}\left( e^{st_{Y}} s^{a/2} J_{a}\left(\sqrt{sY}\right) \right) 
 - (X \leftrightarrow Y) \,  .
\label{3.38}
\end{aligned}$$

# Gaussian ensemble

For the Gaussian ensemble, we see from ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) that the corresponding monic orthogonal polynomials and normalization are $$\begin{aligned}
C_{n}(x) = 2^{-n}\, H_{n}(y), \quad \quad h_{n} = 2^{-n}\, \pi^{1/4}\, n! \, .
\label{4.1}
\end{aligned}$$ The skew orthogonal polynomials for both $\beta = 1$ and $\beta = 4$ initial conditions at $\tau = 0$ are known in terms of the $C_{n}(x)$ (see e.g. [@MM91]). Using these expansions, the general formula ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) then gives $$\begin{aligned}
R_{2m}(x;\tau) e^{\gamma_{2m} \tau} & = & C_{2m}(x) e^{\gamma_{2m} \tau} 
\noindent \\
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = & 
C_{2m+1}(x) e^{\gamma_{2m+1} \tau} - m C_{2m-1}(x)  e^{\gamma_{2m-1} \tau}
\noindent\\
r_{m}(0) & = & 2^{-2m+1} \sqrt{\pi} \Gamma(2m+1)
\label{4.2}
\end{aligned}$$ for $\beta = 1$ initial conditions, and $$\begin{aligned}
R_{2m}(x;\tau) e^{\gamma_{2m} \tau} & = & m! 
\sum_{l=0}^m e^{\gamma_{2l} \tau} {C_{2l}(x) \over l!} \nonumber \\
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = & C_{2m+1}(x) e^{\gamma_{2m+1}
\tau} \\
r_m(0) & =  & 2^{-2m} \sqrt{\pi} \Gamma(2m+2)
\label{4.3}
\end{aligned}$$ for $\beta = 4$ initial conditions. Inverting these formulas for $\{R_{j}(x)\}$ in terms of $\{C_{l}(x)\}$ according to ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) gives $$\begin{aligned}
\label{4.4}
\beta_{2m \, j} = \delta_{2m,j}, \qquad
\beta_{2m+1 \, j} = \left \{
\begin{array}{ll}m!/l!, & j=2l+1, \: l=0,1,\dots,m \\
0, & j=2l, \: l=0,1,\dots,m \end{array} \right.
\end{aligned}$$ for $\beta = 1$, while for $\beta =4$ we find $$\begin{aligned}
\label{4.5}
\beta_{2m \, j} = \left \{ \begin{array}{lll}1, & j=2m \\
-m, & j=2m-2 \\ 0, & {\rm otherwise} \end{array} \right. \qquad
\beta_{2m+1 \, j} = \delta_{2m+1, j}.
\end{aligned}$$

Here we will use these explicit values in the general formulas of Section 2 to compute the matrix elements in ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}). In particular, we will give their asymptotic form in the neighbourhood of the soft edge, which is specified by introducing the scaled variables $X$ and $t$ according to $$\begin{aligned}
x = \sqrt{2N} + 
\frac{X}{2^{1/2}N^{1/6}}\, , \quad \quad \tau = \frac{t}{N^{1/3}}\,   .
\label{4.6}
\end{aligned}$$ The corresponding scaled distribution function ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}), to be denoted $\rho_{(n+m)}^{\rm soft}$, is given by $$\begin{aligned}
\lefteqn{\rho_{(n+m)}^{\rm soft}(X_1^{(1)},\dots,X_n^{(1)};
t^{(1)};X_1^{(2)},\dots,X_m^{(2)};t^{(2)})} \nonumber \\ &&
= \lim_{N \to \infty}
\Big ( {1 \over 2^{1/2} N^{1/6}} \Big )^{n+m} \rho_{(n+m)}\Big ( \sqrt{2N} +
 {X_1^{(1)} \over 2^{1/2} N^{1/6}}, \dots,
\label{r.1}\nonumber \\ &&
\sqrt{2N} + {X_n^{(1)} \over 2^{1/2}N^{1/6}}; {t^{(1)} \over N^{1/3}};
\sqrt{2N} + {X_1^{(2)} \over 2^{1/2} N^{1/6}}, \dots,
\sqrt{2N} + {X_m^{(2)} \over 2^{1/2} N^{1/6}}; {t^{(2)} \over N^{1/3}} \Big )
\end{aligned}$$ Analogous to ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"})--([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}), the matrix elements of $\rho_{(n+m)}^{\rm soft}$ are computed from the formulas $$\begin{aligned}
\lefteqn{
S_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ && =  \lim_{N \to \infty}
{e^{-N^{2/3}(t_Y - t_X)} \over 2^{1/2} N^{1/6}}
S \Big ( \sqrt{2N} + {X \over 2^{1/2} N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
 {t_Y \over N^{1/3}} \Big ) \label{r.2}
\end{aligned}$$ $$\begin{aligned}
\lefteqn{ 
\tilde{S}_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  =  \lim_{N \to \infty}
{e^{-N^{2/3}(t_Y - t_X)} \over 2^{1/2} N^{1/6}}
\tilde{S} \Big ( \sqrt{2N} + {X \over 2^{1/2} N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
  {t_Y \over N^{1/3}} \Big ) \label{r.3}
\end{aligned}$$ $$\begin{aligned}
\lefteqn{ 
\tilde{I}_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  =  \lim_{N \to \infty}
e^{N^{2/3}(t_Y + t_X)} \tilde{I} \Big ( \sqrt{2N} + {X \over 2^{1/2}
N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
   {t_Y \over N^{1/3}} \Big ) \label{r.4} 
\end{aligned}$$ $$\begin{aligned}
\lefteqn{
D_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ & & = \lim_{N \to \infty}  
{e^{-N^{2/3}(t_Y + t_X)} 
 \over 2 N^{1/3}}
D \Big ( \sqrt{2N} + {X \over 2^{1/2}
N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
{t_Y \over N^{1/3}} \Big ). \label{r.5}
\end{aligned}$$ Here the scale factors in addition to $1/2^{1/2} N^{1/6}$ do not effect the value of ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) because they result from a transformation of the form ([\[n.6\'\]](#n.6'){reference-type="ref" reference="n.6'"}).

## $\beta = 1$ initial conditions

We see from ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) that for $N$ even and $p \geq N$ $$\begin{aligned}
\beta_{p l} = \beta_{p N-1}\, \beta_{N-1 l} \,  .
\label{4.7}
\end{aligned}$$ Substituting in the formula ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) for $S_{2}$ and using ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) and ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) we thus have $$\begin{aligned}
S_2(x,y;\tau_x,\tau_y) & = & \sqrt{w(y)} \Big (
{\Phi_{N-2}(x;\tau_x) \over r_{N/2 - 1}(0)} e^{\gamma_{N-2} \tau_x} -
\sqrt{w(x)} {C_{N-1}(x) e^{-\gamma_{N-1} \tau_x} \over h_{N-1}} \Big )
\nonumber \\
&& \times C_{N-1}(y) e^{\gamma_{N-1} \tau_y}.
\label{4.8}
\end{aligned}$$

To compute the scaled limit we make use of the asymptotic expansion [@Sz] $$\begin{aligned}
\label{4.9}
e^{-x^2/2} H_n(x) = \pi^{-3/4} 2^{n/2 + 1/4} (n!)^{1/2} n^{-1/12}
\Big ( \pi {\rm Ai}(-u) + {\rm O}(n^{-2/3}) \Big )
\end{aligned}$$ where $x = (2n)^{1/2} - u/2^{1/2}n^{1/6}$. This gives $$\begin{aligned}
\label{4.10}
\sqrt{w(y)} C_{N-1}(y) \Big |_{y = (2N)^{1/2} + Y/2^{1/2} N^{1/6}} 
\sim \pi^{1/4} 2^{-(N-1)/2 + 1/4}(N-1)!^{1/2} N^{-1/12}
{\rm Ai}(Y).
\end{aligned}$$ Also, from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) and ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) $$\begin{aligned}
f(x;\tau_x) & := & {\Phi_{N-2}(x;\tau_x) \over r_{N/2 - 1}(0)}
e^{\gamma_{N-2} \tau_x} - \sqrt{w(x)} {C_{N-1}(x) e^{-\gamma_{N-1} \tau_x}
\over h_{N-1}} \\
& = & {e^{-x^2/2} \over (N/2 - 1)!} e^{-N \tau_x}
\sum_{p=0}^\infty {(N/2 + p)! \over \sqrt{\pi} (N + 2p + 1)!}
H_{N + 2p + 1}(x) e^{-(2p + 3/2) \tau_x}.
\nonumber
\end{aligned}$$ Noting that for large $N$ $$\begin{aligned}
\nonumber 
{(N/2 + p)! \over ((N + 2p + 1)!)^{1/2}}
{((N-1)!)^{1/2} \over (N/2 - 1)!} \sim 2^{-(p+1)}
\end{aligned}$$ and making use of ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}) with $n = N + 2p + 1$, $-u \sim X - 2p/N^{1/3}$ shows $$\begin{aligned}
\label{4.11}
\lefteqn{((N-1)!)^{1/2} f \Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}} \Big ) } \nonumber
\\ && \sim e^{-N^{2/3} t} 2^{(N-1)/2} 2^{1/4} \pi^{-1/4} N^{-1/12}
{N^{1/3} \over 2} \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.
\end{aligned}$$ Hence $$\begin{aligned}
 \lefteqn{
S_2 \Big (  (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
 (2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
 {t_Y \over N^{1/3}} \Big )} \nonumber \\ && \sim
 e^{N^{2/3}(t_Y - t_X)} 2^{-1/2} N^{1/6} {\rm Ai}(Y)
 \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.
\label{4.12}
\end{aligned}$$

Now consider $S_{1}$ as defined by ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}). Substituting ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) we see that the asymptotics can be determined by writing the sum so that the sum index $p$ is replaced by $N-p$, and then using Stirling's formula and ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}). We thus find $$\begin{aligned}
 \lefteqn{
S_1 \Big (  (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
(2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
{t_Y \over N^{1/3}} \Big )} \nonumber \\ && \sim
e^{N^{2/3}(t_Y - t_X)} 2^{1/2} N^{1/6} 
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \, dv.
\label{4.13}
\end{aligned}$$ Adding together ([\[4.12\]](#4.12){reference-type="ref" reference="4.12"}) and ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}) and substituting for $S$ in ([\[r.2\]](#r.2){reference-type="ref" reference="r.2"}) we thus have $$\label{4.13'}
S_1^{\rm soft}(X,Y;t_X,t_Y) = 
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \, dv
 + {1 \over 2}
 {\rm Ai}(Y)
  \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

We know from ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) that $\tilde{I}$ is defined in terms of $\{\Phi_{l}(\cdot ; \tau)\}$. The asymptotics of $\Phi_{2k-2}$ is calculated in an analogous fashion to the expansion ([\[4.11\]](#4.11){reference-type="ref" reference="4.11"}). Thus after noting $$\begin{aligned}
\lefteqn{\Phi_{N+2k-2}(x;\tau) e^{\gamma_{N+2k-2} \tau} } \\ &&
=
{r_{N/2 + k - 1}(0) \over (N/2 + k -1)!} e^{-N \tau}
\sum_{m=k-1}^\infty {H_{2m+N + 1}(x) (N/2 + m)! \over
\pi^{1/2} (N + 2m + 1)!} e^{-(2m+3/2) \tau}
\end{aligned}$$ we find $$\begin{aligned}
\Phi_{N+2k-2}\Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}} \Big ) e^{\gamma_{N+2k-2} t_X/N^{1/3}} \sim
{r_{N/2 + k -1}(0) \over ((N-1)!)^{1/2}}
{(N/2 - 1)! \over (N/2 + k - 1)!}
 \nonumber \\
\times  e^{-N^{2/3} t_X}
2^{(N-1)/2} 2^{1/4} \pi^{-1/4} N^{-1/12} {N^{1/3} \over 2}
\int_{2k/N^{1/3}}^\infty {\rm Ai}(X - v) e^{-v t_X} \, dv.
\label{4.14}
\end{aligned}$$

Consider now $\Phi _{2k-1}$. We note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) and ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) that $$\begin{aligned}
\Phi_{N+2k-1}(y;\tau) e^{\gamma_{N+2k-1} \tau} = - \sqrt{w(y)}
r_{N/2 + k -1}(0) {H_{N + 2k - 2}(y) \over \pi^{1/2}
(N + 2k - 2)!} e^{-N \tau} e^{- (2k - 3/2) \tau}
\nonumber
\end{aligned}$$ so use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives $$\begin{aligned}
\label{4.15}
\Phi_{N+2k-1}\Big ( (2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t_Y \over N^{1/3}} \Big ) e^{\gamma_{N+2k-1} \tau_Y/N^{1/3}} \sim
- r_{N/2 + k -1}(0) e^{-N^{2/3} t_Y} \nonumber \\
\times e^{-2k t_Y/N^{1/3}} 
\pi^{-1/4} 2^{(N + 2k - 2)/2 + 1/4} ((N + 2k - 2)!)^{1/2} N^{-1/12}
{\rm Ai} (Y - {2k \over N^{1/3}}).
\end{aligned}$$ Multiplying ([\[4.14\]](#4.14){reference-type="ref" reference="4.14"}) and ([\[4.15\]](#4.15){reference-type="ref" reference="4.15"}) together, substituting in ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) and making use of the explicit value of $r_{m}(0)$ from ([\[4.2\]](#4.2){reference-type="ref" reference="4.2"}), we then find $$\begin{aligned}
\label{4.16}
\tilde{I}_1^{\rm soft}(X,Y;t_X,t_Y) =
\int_0^\infty ds \, {\rm Ai}(Y - s) e^{-s t_Y}
\int_s^\infty {\rm Ai}(X - v) e^{-vt_x} dv - ( X \leftrightarrow Y )
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here the asymptotics of $\{R_{m}(\cdot ; \tau)\}$ are required. Now, from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) and ([\[4.2\]](#4.2){reference-type="ref" reference="4.2"}) we have $$\begin{aligned}
\nonumber 
R_{N - 2l - 2}(x;\tau) e^{\gamma_{N - 2l - 2} \tau} = 2^{-(N - 2l - 2)}
H_{N - 2l - 2}(x) e^{\gamma_{N - 2l - 2} \tau}.
\end{aligned}$$ Use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) then gives $$\begin{aligned}
\label{4.17}
\lefteqn{
\sqrt{w(x)} R_{N - 2l - 2}(x;\tau) e^{\gamma_{N - 2l - 2} \tau}
\bigg |_{\begin{array}{l} \scriptstyle x = (2N)^{1/2} + X/2^{1/2} N^{1/6}  \\ 
 \scriptstyle \tau = t_X / N^{1/3}\end{array}} \sim e^{N^{2/3} t_X}} \nonumber\\
&& \times  e^{-2l t_X /N^{1/3}} \pi^{1/4}
2^{-(N - 2l - 2)/2} 2^{1/4} ((N - 2l - 2)! )^{1/2} N^{-1/12}
{\rm Ai} \Big ( X + {2l \over N^{1/3}} \Big ).
\end{aligned}$$ Furthermore $$\begin{aligned}
\label{4.17'}
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = &
2^{-(2m+1)} H_{2m+1}(x) e^{\gamma_{2m+1} \tau} - m
2^{-(2m-1)} H_{2m - 1}(x) e^{\gamma_{2m - 1} \tau} \nonumber
\\ & = &
- e^{\gamma_{2m + 1} \tau} e^{x^2 / 2}
{d \over dx} \Big ( e^{-x^2 / 2} 2^{-2m} H_{2m}(x) \Big ) \nonumber \\
&&
- m 2^{-(2m - 1)} H_{2m - 1}(x) e^{\gamma_{2m - 1} \tau}
( 1 - e^{2 \tau} ),
\end{aligned}$$ and use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives for the asymptotics $$\begin{aligned}
\label{4.18}
\lefteqn{
\sqrt{w(x)} R_{N - 2l - 1}(y;\tau) e^{\gamma_{N - 2l - 1} \tau}
\bigg |_{\begin{array}{l} \scriptstyle
y = (2N)^{1/2} + Y/2^{1/2} N^{1/6}  \\ 
 \scriptstyle
\tau = t_Y / N^{1/3}\end{array}} \sim e^{N^{2/3}t_Y}} \nonumber \\
&& \times \pi^{1/4} 2^{-(N - 2l - 2)/2} 
2^{3/4} ((N - 2l - 2)!)^{1/2} N^{1/12}
{d \over ds} \Big ( e^{-s t_Y} {\rm Ai} (Y + s) \Big ), 
\end{aligned}$$ $s:= 2l / N$. Multiplying together ([\[4.17\]](#4.17){reference-type="ref" reference="4.17"}) and ([\[4.18\]](#4.18){reference-type="ref" reference="4.18"}), dividing by $r_{(N-2l-2)/2}$ and summing over $l$ (which is of the form of a Riemann integral) we thus obtain $$\begin{aligned}
\label{4.19}
D_1^{\rm soft}(X,Y;t_X,t_Y) = {1 \over 4} \int_0^\infty ds \,
e^{-st_X} {\rm Ai}(X + s) {d \over ds} \Big ( e^{-st_Y}
{\rm Ai}(Y + s) \Big ) - (X \leftrightarrow Y)
\end{aligned}$$

### Asymptotics of $g(x, y; \tau_{y} - \tau_{x})$

According to ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) and ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) $$\begin{aligned}
\label{4.19'}
g(x,y;\tau) = e^{-(x^2 + y^2)/2}
\sum_{j=0}^\infty {H_j(x) H_j(y) e^{ - (j + 1/2) \tau} \over 
\pi^{1/2} 2^j j!}
\end{aligned}$$ This summation can be evaluated in closed form [@Er] giving $$\begin{aligned}
\nonumber
g(x,y;\tau) = e^{-(x^2 + y^2)/2}
{e^{-\tau/2} \over (1 - e^{-2\tau})^{1/2}}
\exp \Big ( - {e^{-2 \tau} \over 1 - e^{-2 \tau} } (x - y)^2 \Big )
\exp \Big ( {2 e^{-\tau} \over 1 - e^{-2\tau} } xy \Big )
\end{aligned}$$ Hence $$\begin{aligned}
\nonumber
g \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )
\sim {N^{1/6} \over (2t)^{1/2}}
e^{- t N^{2/3}} e^{-(X-Y)^2/4t - t(X+Y)/2}.
\end{aligned}$$ Alternatively, proceeding as in the derivation of ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}), we can deduce from ([\[4.19\'\]](#4.19'){reference-type="ref" reference="4.19'"}) that $$\begin{aligned}
\label{4.19''}\lefteqn{
g \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )}
\nonumber \\ &&
\sim e^{- N^{2/3} t} 2^{1/2} N^{1/6} \int_{-\infty}^\infty
{\rm Ai}(X + v) {\rm Ai}(Y + v) e^{vt} \, dv
\end{aligned}$$ Dividing by $e^{- N^{2/3} t}
2^{1/2} N^{1/6}$, replacing $t$ by $t_X - t_Y$ and subtracting from ([\[4.13\'\]](#4.13'){reference-type="ref" reference="4.13'"}) shows $$\begin{aligned}
\tilde{S}_1^{\rm soft}(X,Y;t_X,t_Y) & = & -
 \int_{-\infty}^0 
 {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X) } \, dv \nonumber \\
&& +
 {1 \over 2} {\rm Ai}(Y) \int_0^\infty {\rm Ai} (X - v) e^{-vt_X} \, dv.
\end{aligned}$$

## $\beta = 4$ initial conditions

Here we want to again compute the scaled distribution ([\[r.1\]](#r.1){reference-type="ref" reference="r.1"}). As for $\beta = 4$ initial conditions in the Laguerre ensemble, we must modify the scale factor in ([\[r.4\]](#r.4){reference-type="ref" reference="r.4"}) and ([\[r.5\]](#r.5){reference-type="ref" reference="r.5"}) so that $$\begin{aligned}
\label{a.1}\lefteqn{
\tilde{I}_4^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\
&&
 = \lim_{N \to \infty}
{e^{N^{2/3}(t_X + t_Y)} \over 2 N^{1/3}}
\tilde{I} \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big ) 
\end{aligned}$$ $$\begin{aligned}
\lefteqn{
{D}_4^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  = \lim_{N \to \infty}
e^{-N^{2/3}(t_X + t_Y)} 
D \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )
\label{a.2}
\end{aligned}$$

Substituting ([\[4.5\]](#4.5){reference-type="ref" reference="4.5"}) in ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) shows that in terms of $\{C_{l}(x)\}$, $S_{2}$ only consists of a single term, which reads explicitly $$\begin{aligned}
\label{4.2a}
S_2(x,y;\tau_x,\tau_y) = \sqrt{w(x) w(y)}
{C_N(x) e^{-\gamma_N \tau_x} \over h_N}
\Big ( - {N \over 2} \Big ) R_{N-2}(y;\tau_y) e^{\gamma_{N-2} \tau_y}.
\end{aligned}$$ The explicit form of $R_{N-2}(y; \tau_{y}) e^{\gamma_{N-2} \tau_{y}}$ is given by ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}). This expression however does not give a Riemann sum after substituting the asymptotic form of the integrand. Instead, we make use of the identity $$\begin{aligned}
\label{4.3a}
\sum_{l=0}^m {m! \over l!} 2^{-2l} H_{2l}(x) c^{-l} = - \alpha
(4c)^{-m} e^{\alpha x^2} \int_{-\infty}^x e^{-\alpha s^2}
H_{2m+1}(s) \, ds,
\end{aligned}$$ $c = (1 - \alpha)/\alpha$. This can be verified by multiplying both sides by $e^{-\alpha x^{2}}$ and differentiating (we also verify that both sides have the same $x \rightarrow \infty$ behaviour). Choosing $c = e^{-2\tau}$ and comparing with ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) we see that $$\begin{aligned}
R_{2m}(y;\tau) e^{\gamma_{2m} \tau} & = &
- {e^{\tau/2} \over 1 + e^{-2 \tau} } (2 e^{-\tau})^{-2m}
e^{y^2/ (1 + e^{-2 \tau})} \int_{-\infty}^y
e^{-s^2/ (1 + e^{-2 \tau})} H_{2m+1}(s) \, ds \nonumber \\
& = &
 {e^{\tau/2} \over 1 + e^{-2 \tau} } (2 e^{-\tau})^{-2m}
 e^{y^2/ (1 + e^{-2 \tau})} \int_{y}^\infty
 e^{-s^2/ (1 + e^{-2 \tau})} H_{2m+1}(s) \, ds
\label{4.3b}
\end{aligned}$$ where to obtain the second equality the fact that the integrand is odd has been used.

With $x = (2N)^{1/2} + X/2^{1/2}N^{1/6}$, making the change of variables $s \mapsto (2N)^{1/2} + s$ and using the asymptotic expansion ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) we see that $$\begin{aligned}
\sqrt{w(y)} R_{N - 2m}\Big ((2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N - 2m} t / N^{1/3}} \sim
2^{-3/4} N^{-1/4} \pi^{1/4} 2^{-(N - 2m)/2}  \nonumber
\\  
\times ((N - 2m + 1)!)^{1/2}
e^{N^{2/3} t} e^{Yt} \int_{Y+u}^\infty e^{-st} {\rm Ai}(s) \, ds,
\quad u := 2m/N^{1/3}
\label{4.3c}
\end{aligned}$$ For the $x$-dependent factor in ([\[4.2a\]](#4.2a){reference-type="ref" reference="4.2a"}), the asymptotic form of $\sqrt{w(x)} C_{N}(x)$ is given by ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}) with $N - 1$ replaced by $N$. Making use of the explicit value of $h_{N}$, we thus find $$\begin{aligned}
\label{4.3d}
\lefteqn{S_2 \Big ((2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
(2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}}, {t_Y \over N^{1/3}} \Big )} \nonumber \\ &&
 \sim
- {N^{1/6} \over 2^{1/2}} e^{-N^{2/3} (t_X - t_Y)}
{\rm Ai}(X) e^{Y t} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds.
\end{aligned}$$

The asymptotic form of the quantity $S_{1}$ as defined by ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}) is given by ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}), since $S_{1}$ is the same for $\beta = 1$ and $\beta = 4$ initial conditions. Hence $$\begin{aligned}
\label{ls4}
S_4^{\rm soft}(X,Y;t_X,t_Y) & = &
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \,
dv \\ &&
- {1 \over 2} {\rm Ai}(X) e^{Yt} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds
\end{aligned}$$ Also, subtracting ([\[4.19\'\'\]](#4.19''){reference-type="ref" reference="4.19''"}) divided by $e^{-N^{2/3} t}2^{1/2}N^{1/6}$ (and with $t \mapsto t_X - t_Y$) gives $$\begin{aligned}
\tilde{S}_4^{\rm soft}(X,Y;t_X,t_Y) & = &
- \int_{-\infty}^0 {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \,
dv \nonumber \\
&&- {1 \over 2} {\rm Ai}(X) e^{Yt} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds
\end{aligned}$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

First note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}), ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) and ([\[4.5\]](#4.5){reference-type="ref" reference="4.5"}) that $$\begin{aligned}
\lefteqn{
\Phi_{2k-1}(x;\tau) e^{\gamma_{2k-1}\tau}} \\
 &  &
 = \sqrt{w(x)} e^{-\gamma_{2k-2} \tau} 2^{-2(k-1)} \Big (
{1 \over 2} H_{2k}(x) e^{-2\tau} - (2k-1) H_{2k-2}(x) \Big ) 
\\ &  & = -  e^{-\gamma_{2k-2} \tau} 2^{-2(k-1)} \bigg (
{d \over dx} \Big ( e^{-x^2/2} H_{2k-1}(x) \Big ) - {\sqrt{w(x)} \over 2}
H_{2k}(x) (e^{-2\tau} - 1) \Big )
\end{aligned}$$ (c.f. ([\[4.17\'\]](#4.17'){reference-type="ref" reference="4.17'"})). Use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives for the asymptotics $$\begin{aligned}
\label{4.3e}
\lefteqn{ \Phi_{N - 2k - 1} \Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N-2k-1}t/N^{1/3}} \sim} \nonumber \\&&
- e^{-N^{2/3} t_X} \pi^{1/4} 2^{7/4} 2^{-(N-2k-1)/2} (N - 2k - 1)!^{1/2}
N^{1/12} {d \over ds} \Big ( e^{st_X} {\rm Ai}(X + s) \Big ),
\end{aligned}$$ $s : = 2 k/N$. Similarly $$\begin{aligned}
\nonumber
{1 \over r_{k-1}(0)} \Phi_{2k-2}(y;\tau) e^{\gamma_{2k-2}\tau} =
\sqrt{w(y)}  {H_{2k-1}(y) e^{-\gamma_{2k-1}\tau} \over \pi^{1/2}(2k-1)!}
\end{aligned}$$ and so $$\begin{aligned}
\label{4.3f}\lefteqn{
{1 \over r_{N/2 -k - 1}(0)} \Phi_{N-2k-2}\Big (
(2N)^{1/2} +  {Y \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N-2k-2}t/N^{1/3}} \sim} \nonumber \\&&
e^{-N^{2/3} t_Y} e^{st_Y} \pi^{-1/4}
2^{(N-2k-1)/2 + 1/4} (N - 2k - 1)!^{-1/2} N^{-1/12}
{\rm Ai}(Y + s).
\end{aligned}$$ Multiplying together ([\[4.3e\]](#4.3e){reference-type="ref" reference="4.3e"}) and ([\[4.3f\]](#4.3f){reference-type="ref" reference="4.3f"}) and summing according to ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) we see that $$\begin{aligned}
\label{4.3g}
\tilde{I}_4^{\rm soft}(X,Y;t_X,t_Y) =
\int_0^\infty ds \, e^{st_Y} {\rm Ai}(Y + s)
{d \over ds} \Big ( e^{st_X} {\rm Ai}(X + s) 
\Big ) - (X \leftrightarrow Y )
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here we require the asymptotics of $R_{2m}(\cdot ; \tau)$ and $R_{2m+1}(\cdot ; \tau)$. The former is given by ([\[4.3c\]](#4.3c){reference-type="ref" reference="4.3c"}). For the latter, we note from ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) that $$\begin{aligned}
\nonumber
{1 \over r_m(0)} R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} =
{H_{2m+1}(y) \over 2 \sqrt{\pi} \Gamma(2m+2) } e^{\gamma_{2m+2}
\tau}
\end{aligned}$$ and thus according to ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) $$\begin{aligned}
\label{4.4a}
\lefteqn{
{\sqrt{w(x)} \over r_{N/2 - m}(0)} R_{N - 2m+1} (x;\tau)
e^{\gamma_{N - 2m + 1} \tau} \bigg |_{\begin{array}{l}
\scriptstyle
x = (2N)^{1/2} + X/2^{1/2} N^{1/6} \\ 
\scriptstyle \tau = t/N^{1/3} \end{array}} }
\\ && \sim {e^{N \tau_x} \over 2 \sqrt{\pi} }
{e^{-u t_X} \over (\Gamma ( N - 2m + 2))^{1/2}} \pi^{1/4}
2^{(N - 2m + 1)/2 + 1/4} N^{-1/12} {\rm Ai}(X + u).
\end{aligned}$$ Multiplying ([\[4.4a\]](#4.4a){reference-type="ref" reference="4.4a"}) and ([\[4.3c\]](#4.3c){reference-type="ref" reference="4.3c"}) according to ([\[2.q\]](#2.q){reference-type="ref" reference="2.q"}) we see that $$\label{4.4b}
D(X,Y;t_X,t_Y) = {1 \over 4} e^{N^{2/3}(t_X + t_Y)}
\int_0^\infty e^{-u t_Y} {\rm Ai}(Y + u) e^{X t_X}
\int_{X + u}^\infty e^{-st} {\rm Ai}(s) \, ds - (X \leftrightarrow Y).$$
