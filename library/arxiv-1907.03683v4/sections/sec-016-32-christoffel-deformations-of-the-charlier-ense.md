---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-016-32-christoffel-deformations-of-the-charlier-ense
section_title: "Christoffel deformations of the Charlier ensemble and main result"
section_number: 3.2
pages: 12-13
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 1.0
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
We now define the Christoffel deformation of the Charlier ensemble. We know from [@johanssonplancherel] that this ensemble approximates the poissonized Plancherel measure, and the aim of this section is to generalize this fact by proving that Christoffel deformations of this ensemble admit a limit that is expressed through Bessel functions. Our discrete measure is $$\begin{aligned}
\omega(x)=\omega_a(x)=e^{-a}\frac{a^x}{x!}, \quad x \in \mathbb{N},
\end{aligned}$$ where $a>0$ is a parameter, and the $N$-th orthogonal polynomial ensemble that this measure defines is denoted by $\mathbb{P}_{N,a}$. The corresponding orthonormal polynomials are the Charlier polynomials ([@ismail], [@andrews]): $$\begin{aligned}
C_n(x)=C_n(x;a)=\frac{a^{\frac{n}{2}}}{\sqrt{n!}}\left._2F_0\right.(-n,-x; ;-1/a) \hspace{0,1cm} , \quad n \in \mathbb{N}.
\end{aligned}$$ As in the previous section, we define the Christoffel deformations of the Charlier ensemble. Let $k \in \mathbb{N}$ be a non-negative integer, and $\tilde{u}_i \in \mathbb{R}$ be distinct numbers. Let $\alpha >0$ be a positive real number, and for each $N \in \mathbb{N}$, consider the Christoffel deformation of the $N$-th Charlier ensemble at points $u_1=\tilde{u}_1+N,...,u_k=\tilde{u}_k+N$, with parameter $a=\alpha/N$, according to definition [\[maindef\]](#maindef){reference-type="ref" reference="maindef"}. This determinantal point process is denoted by $\mathbb{P}_{N,\alpha/N}^k$, and its correlation kernel is denoted by $K_N^{\alpha/N,k}$. For an integer $p \in \mathbb{Z}$, we form the determinants: $$\begin{aligned}
A_{k,p}(x) &= \begin{vmatrix}
J_{\tilde{u}_1+p}(2\sqrt{\alpha}) &\dots & J_{\tilde{u}_1-2k+p}(2\sqrt{\alpha}) \\
\vdots& \ddots & \vdots \\
J_{\tilde{u}_k+p}(2\sqrt{\alpha}) & \dots& J_{\tilde{u}_k-2k+p}(2\sqrt{\alpha}) \\
L_{\tilde{u}_1+p}(2\sqrt{\alpha}) &\dots & L_{\tilde{u}_1-2k+p}(2\sqrt{\alpha}) \\
\vdots & \ddots & \vdots \\
L_{\tilde{u}_k+p}(2\sqrt{\alpha}) & \dots & L_{\tilde{u}_k-2k+p}(2\sqrt{\alpha}) \\
J_{x+p}(2\sqrt{\alpha}) & \dots & J_{x-2k+p}(2\sqrt{\alpha})
\end{vmatrix}, \quad x \in \mathbb{Z},\\
C_{k,p} &=\begin{vmatrix}
J_{\tilde{u}_1+p}(2\sqrt{\alpha}) & \dots & J_{\tilde{u}_1-2k+1+p}(2\sqrt{\alpha}) \\
\vdots & \ddots & \vdots \\
J_{\tilde{u}_k+p}(2\sqrt{\alpha}) &\dots& J_{\tilde{u}_k-2k+1+p}(2\sqrt{\alpha}) \\
L_{\tilde{u}_1+p}(2\sqrt{\alpha}) & \dots & L_{\tilde{u}_1-2k+1+p}(2\sqrt{\alpha}) \\
\vdots & \ddots & \vdots \\
L_{\tilde{u}_k+p}(2\sqrt{\alpha}) & \dots & L_{\tilde{u}_k-2k+1+p}(2\sqrt{\alpha})
\end{vmatrix}.
\end{aligned}$$ The main result of this section is the following Theorem.

::: thm
[]{#thm1 label="thm1"} In the regime described above, we have that, for all $x,y \in \mathbb{Z}$, $x \neq y$, $$\begin{aligned}
\lim_{N \rightarrow \infty} K_N^{\alpha/N,k}(x+N,y+N)&=\frac{\alpha^{\frac{2k+1}{2}}}{C_{k,0}^2 \prod_{i=1}^k|(x-\tilde{u}_i)(y-\tilde{u}_i)|} \frac{A_{k,0}(x)A_{k,1}(y)-A_{k,0}(y)A_{k,1}(x)}{x-y}.
\end{aligned}$$ When $x=y$, L'Hospital rule entails: $$\begin{aligned}
\lim_{N \rightarrow \infty} K_N^{\alpha/N,k}(x+N,x+N)&=\frac{\alpha^{\frac{2k+1}{2}}}{C_{k,0}^2 \prod_{i=1}^k(x-\tilde{u}_i)^2}\left( A_{k,0}'(x)A_{k,1}(x)-A_{k,0}(x)A_{k,1}'(x)\right).
\end{aligned}$$
:::

This implies that the Christoffel deformation of the Charlier ensemble $\mathbb{P}_{N,\alpha/N}^k$, shifted by $-N$, weakly converges, as a probability measure on $\text{Conf}(\mathbb{Z})$, to a determinantal point process governed by the limit correlation kernel of the Theorem. In particular, if we take $k=0$, one recovers Johansson's result ([@johanssonplancherel], Theorem 1.2).
