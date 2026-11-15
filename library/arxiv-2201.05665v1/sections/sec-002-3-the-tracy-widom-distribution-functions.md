---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-002-3-the-tracy-widom-distribution-functions
section_title: "The Tracy-Widom distribution functions"
section_number: 3
pages: 3-6
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.963
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
The joint probability densities of the eigenvalues of random matrices from the GOE, GUE and GSE ensembles are given by $$\label{eigenprob}
P_{N\beta}(\lambda_1, ..., \lambda_N) =
Z^{-1}_{N\beta}\,e^{-\frac{1}{2}\beta\sum_{j=1}^{N}\lambda^{2}_j}
\prod_{j<k}|\lambda_j - \lambda_k|^{\beta},$$ where $Z_{N\beta}$ is a normalization constant (or partition function) and $$\beta := \begin{cases}
1 & \textrm{for GOE},\cr
2 & \textrm{for GUE},\cr
4 & \textrm{for GSE}.
\end{cases}$$ The famous Tracy-Widom distribution functions, commonly denoted as $F_{\beta}(t)$, describe the edge fluctuation of the eigenvalues in the large $N$ limit. They are defined via the scaling limits $$\label{Airy1}
F_{\beta}(t) = \lim_{N\to \infty}\textrm{Prob}\,\bigl((\lambda_{\max} -\sqrt{2N})2^{1/2}N^{1/6}
\leq t\bigl),$$ where $\lambda_{\max}$ is the largest eigenvalue drawn from the ensembles with density ([\[eigenprob\]](#eigenprob){reference-type="ref" reference="eigenprob"}). The central theme of the series of papers [@74; @75; @80; @84; @96] is the following analytical description of these distributions, which links them to the theory of integrable systems.

Let $K_{\textrm{Airy}}$ be the trace-class operator in $L_2\bigl((t, \infty); dz\bigr)$ with kernel $$\label{Airy0}
K_{\textrm{Airy}}(z, z') = \frac{\textrm{Ai}(z)\textrm{Ai}'(z') - \textrm{Ai}'(z)\textrm{Ai}(z')}{z - z'},$$ where $\textrm{Ai}(z)$ is the Airy function, $$\textrm{Ai}(z) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-\frac{i}{3}s^3 - izs}ds.$$ Then, the $\beta =2$ Tracy-Widom distribution, $F_{2}(t)$, is given by the *Airy-kernel* Fredholm determinant (see [@For]) $$\label{Airy2}
F_{2}(t) = \det \left(1 - K_{\textrm{Airy}}\right).$$

Moreover, as shown in [@75], the following formula is valid for the Fredholm determinant on the right hand side of ([\[Airy2\]](#Airy2){reference-type="ref" reference="Airy2"}): $$\label{TW1}
 \det(1 - K_{\textrm{Airy}}) = \exp\left\{ - \int_{t}^{\infty}(s-t)u^2(s)ds\right\},$$ where $u(x)$ is the Hastings-McLeod solution of the *second Painlevé equation*, i.e. the solution of the ODE $$\label{painleve}
u_{tt} = tu +2u^3,$$ uniquely determined by the boundary condition, $$\label{painleve2}
u(t) = \frac{1}{2\sqrt{\pi}}t^{-1/4}e^{-\frac{2}{3}t^{3/2}}(1 + o(1)), \quad t \to +\infty.$$ Similar Painlevé representations for the other two Tracy-Widom distribution functions have the form [@84] $$\label{TW14}
F_{1}(t) = F_{2}^{1/2}(t)E(t), \quad F_{4}(t) = \frac{1}{2}\left\{E(t) + \frac{1}{E(t)}\right\}F_{2}^{1/2}(t),$$ where $$E(t) = \exp\left\{ - \frac{1}{2}\int_{t}^{\infty}u(s)ds\right\},$$ and $u(x)$ is the same Hastings-McLeod solution to the second Painlevé transcendent[^1]. Painlevé equations are integrable in the sense of Lax pairs, which, in particular, implies that their solutions admit a Riemann-Hilbert (RH) representation. A Riemann-Hilbert representation can be viewed as the non-abelian analog of the familiar integral representations of the classical special functions such as the Bessel functions, the Airy function, etc. A key consequence of the RH representation is that the Painlevé functions possess one of the principal features of a classical special function---a mechanism, viz. the nonlinear steepest descent method, to evaluate explicitly relevant asymptotic connection formulae (see e.g. [@FIKN]). Specifically, in the case of the Hastings-McLeod solution the integrability of the second Painlevé equation underlies the fact that, in addition to the asymptotic behavior ([\[painleve2\]](#painleve2){reference-type="ref" reference="painleve2"}) at $t = +\infty$, one also knows the asymptotic behavior of $u(t)$ at $t = -\infty$, which is described [@hast_mcleod] as follows[^2] $$\label{painleve3}
u(t) = \sqrt{-\frac{t}{2}} + O\Bigl((-t)^{-5/2}\Bigr), \quad t \to -\infty.$$ Herein lies the importance of the Tracy-Widom formulae ([\[TW1\]](#TW1){reference-type="ref" reference="TW1"}) and ([\[TW14\]](#TW14){reference-type="ref" reference="TW14"})---they provide the key distribution functions of random matrix theory with *explicit* representations that are amenable to detailed asymptotic analysis.

An immediate corollary of formula ([\[TW1\]](#TW1){reference-type="ref" reference="TW1"}) (and the known asymptotics ([\[painleve3\]](#painleve3){reference-type="ref" reference="painleve3"}) of the Painlevé function) is an explicit formula for the large negative $t$ behavior of the distribution function $F_{2}(t)$: $$\label{asympairy1}
\ln F_2(t) = \frac{t^3}{12} - \frac{1}{8}\ln(- t )+ c_0 + o(1), \quad t \to -\infty.$$ The value of the constant $c_0$ was conjectured by Tracy and Widom in paper [@75] to be the same as for the sine-kernel determinant, which is given by $$\label{Airyc0}
c_0 = \frac{1}{24}\ln 2 + \zeta'(-1),$$ where $\zeta(s)$ is the Riemann zeta-function[^3].

Another important advantage of the Tracy-Widom formula ([\[TW14\]](#TW14){reference-type="ref" reference="TW14"}) is that it makes it possible to design, using the exact connection formula ([\[painleve2\]](#painleve2){reference-type="ref" reference="painleve2"})-([\[painleve3\]](#painleve3){reference-type="ref" reference="painleve3"}), a very efficient scheme [@Dieng], [@Dris] for the numerical evaluation[^4] of the distribution functions $F_{\beta}$.

The appearance of the Painlevé equations in the Tracy-Widom formulae is not accidental. As follows from results in [@80], the connection to integrable systems is already encoded in the determinant formula ([\[Airy2\]](#Airy2){reference-type="ref" reference="Airy2"}). Indeed, the Airy-kernel integral operator belongs to a class of integral operators with kernels of the form $$\label{intker0}
K(z,z') = \frac{\phi(z)\psi(z') - \psi(z)\phi(z') }{z-z'},$$ acting in $L_{2}(J)$, where $J$ is a union of intervals, $$J = \bigcup_{k=1}^{l}[a_{2k-1}, a_{2k}],$$ and $\phi(z)$, $\psi(z)$ are $C^{1}$-functions. This class of integral operators has appeared frequently in many applications related to random matrices and statistical mechanics[^5]. In [@80], it is shown that if the functions $\phi(z)$ and $\psi(z)$ satisfy a linear differential equation, $$\frac{d}{dz}\begin{pmatrix}\phi(z)\\ \psi(z)\end{pmatrix}
=\Omega(z)\begin{pmatrix}\phi(z)\\ \psi(z)\end{pmatrix},$$ where $$\Omega(z) = \frac{1}{m(z)}\begin{pmatrix}A(z)&B(z)\\C(z)&-A(z)\end{pmatrix},$$ and $m(z)$, $A(z)$, $B(z)$ and $C(z)$ are polynomials, then the Fredholm determinant, $\det(1 - K)$, can be expressed in terms of the solution to a certain system of nonlinear partial differential equations with the end points $a_j$ as independent variables. This system is integrable in the sense of Lax[^6], and in the case of the Airy kernel it reduces to a single ODE---the second Painlevé equation.

In [@82], the results of [@80] were extended to the general $m\times m$ case, that is, to the kernels of the form $$\label{intker}
K(z,z') = \frac{\sum_{j,i=1}^{m}c_{ij}\phi_j(z)\phi_{i}(z')}{z-z'},$$ acting in $L_{2}(J)$. Here, $J$ is, as before, a union of intervals, the constant matrix $C \equiv \{c_{ij}\}$ is antisymmetric and $\phi_j(z)$ are $C^{1}$-functions satisfying the linear differential equation $$m(z)\frac{d\phi(z)}{dz} = \Omega(z)\phi(z), \quad
\phi(z) := \begin{pmatrix}\phi_1(z)\\\phi_2(z)\\.\\.\\.\\ \phi_m(z)\end{pmatrix},$$ where $m(z)$ is a scalar polynomial while $\Omega(z)$ is a matrix with polynomial entries connected to the matrix $C$ by $$\Omega^{T}(z)C + C\Omega(z) =0.$$ The main result of [@82] is the derivation, for such operators $K$, of a system of partial differential equations, with the $a_j$ as independent variables, whose solution determines the logarithmic derivatives of $\det (1-K)$ with respect to $a_j$.

<figure id="fig:sine">

<figcaption>Harold and his wife, Linda Larkin, at Lake Sonoma in 2013. Photo courtesy of Craig Tracy.</figcaption>
</figure>

[^1]: A similar representation for the sine-kernel determinant (involving, this time, a special solution of the fifth Painlevé equation) was given earlier in [@JMMS].

[^2]: Hastings and McLeod derived ([\[painleve3\]](#painleve3){reference-type="ref" reference="painleve3"}) using the inverse scattering transform which was a precursor of the Riemann-Hilbert method.

[^3]: This conjecture was independently proved in [@DIK] and [@Baik:2007]. Also, in [@Baik:2007] similar asymptotic results were established for the other two Tracy-Widom distributions.

[^4]: It should be noted that the Hastings-McLeod solution is very unstable; indeed, a small change in the pre-exponential numerical factor in the normalization condition ([\[painleve2\]](#painleve2){reference-type="ref" reference="painleve2"}) yields a completely different type of behavior of $u(x)$ for negative $x$, including the appearance of singularities (e.g. see again [@FIKN] ). Herein lies the importance of the knowledge of the behavior ([\[painleve3\]](#painleve3){reference-type="ref" reference="painleve3"}) in order to adjust the numerical procedure appropriately. Said differently, knowledge of the connection formulae makes it possible to transform an unstable ODE initial value problem into a stable ODE boundary value problem.

[^5]: An integral operator with kernel ([\[intker0\]](#intker0){reference-type="ref" reference="intker0"}) is a special case of a so-called "integrable Fredholm operator", i.e. an integral operator whose kernel is of the form $$\label{intker2}
    K(z,z') = \frac{\sum_{j=1}^{m}f_j(z)h_{j}(z')}{z-z'}, \quad z, z' \in C,$$ with some functions $f_{j}(z)$ and $h_{j}(z)$ defined on a contour $C$. This type of integral operators was singled out as a distinguished class in [@iiks] (see also [@deift]; in a different context, unrelated to integrable systems, these operators were also studied in the earlier work [@Sakh]). A crucial property of a kernel ([\[intker\]](#intker){reference-type="ref" reference="intker"}) is that the associated resolvent kernel is again an integrable kernel. Moreover, the functions $``f"$ and $``h"$ corresponding to the resolvent are determined via an auxiliary matrix Riemann-Hilbert problem whose jump-matrix is explicitly constructed in terms of the original $f, h$-functions.

[^6]: The Lax-integrability of the Tracy-Widom system associated with the kernel ([\[intker0\]](#intker0){reference-type="ref" reference="intker0"}) was proven in [@P], where this system was identified as a special case of isomonodromy deformation equations and the Fredholm determinant $\det(1-K)$ was identified as the corresponding $\tau$-function.
