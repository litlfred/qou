---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-005-23-hyperbolic-orthogonal-coordinate-system
section_title: "Hyperbolic orthogonal coordinate system"
section_number: 2.3
pages: 4-5
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.919
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
Put an orthogonal system of axes to paracycle coordinate system such that, the new half-axes let the tangent half-lines at the origin of the old one. (We can see it on Fig.3.) To determine the new coordinates of the point $P$ we project $P$ orthogonally to the hyperplane spanned by the axes $x_1,x_2,\cdots, x_{n-2},x_n$. The getting point is $P_{n-1}$. Then we project orthogonally $P_{n-1}$ onto the $(n-2)$-space spanned by $x_1,x_2,\cdots, x_{n-3},x_n$. The new point is $P_{n-2}$. Now the $(n-1)^{th}$ coordinate is the distance of $P$ and $P_{n-1}$, the $(n-2)^{th}$ is the distance of $P_{n-1}$ and $P_{n-2}$ and so on \... In the last step we get the $n^{th}$ coordinate which is the distance of the point $P_1$ from the origin $O$.

![Coordinate system based on orthogonal axes.](vol3.eps)

Since the connection between the distance $2d$ of two points of a paracycle and the arclength of the connecting paracycle arc $2s$ is $$s=k\sinh\frac{d}{k}$$ thus the distance $z$ of the respective halving points can be calculated as: $$z=k\ln\cosh\frac{d}{k}.$$ Now elementary calculation shows that the connection between the coordinates with respect to the two system of coordinates is:

$$\begin{aligned}
\xi_{n-1} & = & e^{\frac{\xi_n}{k}}k\sinh  \frac{x_{n-1}}{k}\\
\xi_{n-2} & = & e^{\frac{\xi_n}{k}+\ln \cosh\frac{x_{n-1}}{k}}k\sinh \frac{ x_{n-2}}{k}\\
& \vdots & \\
\xi_1 & = & e^{\frac{\xi_n}{k}+\ln \cosh\frac{x_{n-1}}{k} +\cdots + \ln \cosh\frac{x_2}{k}}k\sinh \frac{ x_{1}}{k}\\
x_n & = & \xi_n+k\ln \cosh\frac{x_{n-1}}{k}+\cdots + k\ln \cosh\frac{x_2}{k} + k\ln \cosh\frac{x_{1}}{k}.
\end{aligned}$$

From this we get a new one, corresponding point $(\xi_1,\xi_2,\cdots, \xi_n)^T\in\mathbb{H}^n$ to point $(u_1,\cdots u_n)^T\in \mathbb{R}^n$ as in our first calculation. The corresponding system of equation is:

$$\begin{aligned}
u_1& = &k\cosh \frac{ x_{2}}{k} \cdots  \cosh \frac{ x_{n-1}}{k}\sinh \frac { x_1}{k}\\
& \vdots & \\
u_{n-1} & = & k\sinh \frac{ x_{n-1}}{k}\\
u_n & = &  x_n-k\ln \cosh \frac{ x_{1}}{k}-\cdots - k\ln \cosh \frac{ x_{n-1}}{k}
\end{aligned}$$ The Jacobian of this transformation is $$\left(\cosh \frac{ x_{1}}{k}\right)\left(\cosh  \frac{x_{2}}{k}\right)^2\cdots \left(\cosh \frac{ x_{n-1}}{k}\right)^{n-1},$$ and we get our third formula on the volume: $$v(D)=\int\limits_{D} \left(\cosh \frac{ x_{n-1}}{k}\right)^{n-1}\cdots \left(\cosh  \frac{x_{2}}{k}\right)^2\left(\cosh \frac{ x_{1}}{k}\right)\mathrm{d}x_1\cdots \mathrm{d}x_n.$$ Here we use hyperbolic orthogonal coordinates.
