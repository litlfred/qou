---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-015-31-on-the-plancherel-measure-on-partitions
section_title: "On the Plancherel measure on partitions"
section_number: 3.1
pages: 11-12
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.985
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
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
