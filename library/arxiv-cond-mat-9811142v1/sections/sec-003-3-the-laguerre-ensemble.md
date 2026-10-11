---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-003-3-the-laguerre-ensemble
section_title: "The Laguerre ensemble"
section_number: 3
pages: 8-10
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.987
---
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
