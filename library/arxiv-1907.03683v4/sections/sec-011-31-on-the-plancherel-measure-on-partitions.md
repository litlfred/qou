---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-011-31-on-the-plancherel-measure-on-partitions
section_title: "On the Plancherel measure on partitions"
section_number: 3.1
pages: 11-13
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.992
---
The Plancherel measure is a probability measure $\text{Pl}_n$ on the set of Young diagrams of fixed size $n$, $\mathbb{Y}_n=\{\lambda \in \mathbb{Y}, \hspace{0.1cm} |\lambda|=n \}$. It is given by $$\begin{aligned}
\text{Pl}_n(\lambda)= \frac{\dim(\lambda)^2}{n!}, \quad \lambda \in \mathbb{Y}_n,
\end{aligned}$$ where $\dim(\lambda)$ is the dimension of the irreducible representation of the $n$-th symmetric group parametrized by $\lambda$, or equivalentely, the number of stantard Young tableaux of shape $\lambda$ (see [@macdonald] or [@sagan]). It is well known that the poissonization of the Plancherel measure is a determinantal point process. More precisely, let $\alpha > 0$ be a positive parameter and form the poissonized Plancherel measure $\mathbb{P}_\alpha$ on $\mathbb{Y}$ by imposing $n$ to have the Poisson distribution with parameter $\alpha$: $$\begin{aligned}
\mathbb{P}_\alpha (\lambda) =e^{-\alpha} \alpha^{|\lambda|}\left(\frac{\dim(\lambda)}{|\lambda|!}\right)^2, \quad \lambda \in \mathbb{Y}.
\end{aligned}$$ For $\lambda \in \mathbb{Y}$, we set $$\begin{aligned}
\mathfrak{S}^0(\lambda):=\{\lambda_i -i, \hspace{0.1cm} i=1,2,...\} \in \text{Conf}(\mathbb{Z}).
\end{aligned}$$Then the pushforward of $\mathbb{P}_\alpha$ under the map $\mathfrak{S}^0$, which we call the *discrete Bessel point process*, is a determinantal point process with the discrete Bessel kernel $$\label{discretebesselkernel} K_{\alpha}(x,y)=\sqrt{\alpha} \frac{J_x(2\sqrt{\alpha})J_{y+1}(2\sqrt{\alpha})-J_y(2\sqrt{\alpha})J_{x+1}(2\sqrt{\alpha})}{x-y},$$ where the Bessel functions $J_x(2\sqrt{\alpha}), \hspace{0.1cm} x \in \mathbb{Z}$ are defined via their generating Laurent series ([@andrews]): $$\label{defbessel}
e^{\sqrt{\alpha}(z-z^{-1})}=\sum_{x \in \mathbb{Z}} J_x(2\sqrt{\alpha}) z^x.$$ This definition leads to the expression $$\begin{aligned}
J_x(2\sqrt{\alpha}) = \sum_{m=0}^{+ \infty}\frac{(-1)^m}{m!\Gamma(m+x+1)} \alpha^{m + x/2}
\end{aligned}$$ that can be analytically continuated for all values of the indices $x \in \mathbb{C}$. We can thus introduce the derivatives of the Bessel functions with respect to their index $$\begin{aligned}
\frac{d}{dx}J_x(2\sqrt{\alpha})=:L_x(2\sqrt{\alpha}).
\end{aligned}$$

## Christoffel deformations of the Charlier ensemble and main result

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
