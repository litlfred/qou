---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-001-2-revision-of-the-formalism
section_title: "Revision of the formalism"
section_number: 2
pages: 4-7
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.98
---
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
