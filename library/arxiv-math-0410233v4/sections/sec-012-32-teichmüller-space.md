---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-012-32-teichmüller-space
section_title: "Teichmüller Space"
section_number: 3.2
pages: 12-15
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.986
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
We now turn our attention to the term $(a^2+b^2)$ in Lemma [\[lemma:b_U=area\]](#lemma:b_U=area){reference-type="ref" reference="lemma:b_U=area"}. This term is closely related to the change in metric of the torus $\partial U$.

Under the hyperbolic metric on $X=M-\Sigma$, the boundary $\partial U$ inherits a Euclidean structure. This gives a point in the Teichmüller space of the torus, $\mathcal{T}(T^2)$.

::: remark
We view $\mathcal{T}(T^2)$ as the space of flat structures on the torus. To each flat structure $\zeta$ is associated a unit area Euclidean metric $g_{\zeta}$, and vice versa. However, in the following discussion we will refer to both the flat structure and its associated metric, and so we will continue to distinguish between the two. We use Greek letters $\gamma$, $\zeta$ to denote points in $\mathcal{T}(T^2)$, and $g$ with appropriate subscripts to denote the induced metric on the torus.
:::

As the metric on $X$ changes under the cone deformation, the point in $\mathcal{T}(T^2)$ will also change, tracing out a smooth path $\gamma(t)$, with tangent vector $\gamma'(t)$. The tangent vector $\gamma'(t)$ is an infinitesimal change of the flat structure on the torus. Our 1--form $\omega$ encodes the infinitesimal deformation of the hyperbolic cone structure $X_t$ on $X=M-\Sigma$. So we may relate $\gamma'(t)$ to $\omega$, or more particularly, to $a^2+b^2$. We will do so using the Teichmüller metric on $\mathcal{T}(T^2)$.

Definitions of the Teichmüller distance vary by constant factors in the literature. We will use the convention that the Teichmüller distance between two points, $\sigma$ and $\tau$ in $\mathcal{T}(T^2)$, is defined to be $$d(\sigma, \tau) = \frac{1}{2}\inf_{f}\;\log K_f,$$ where $f\colon\thinspace
\sigma \to \tau$ is a $K_f$--quasiconformal map, with $K_f$ the smallest such constant. (See for example [@lehto].)

::: lemma
Let $\gamma(t)$ denote the path of $\partial U$ through $\mathcal{T}(T^2)$. Let $\gamma'(t)$ denote its tangent vector. Then $$\sqrt{a^2+b^2} = \left\| \gamma'(t) \right\|,$$ where the metric is the Teichmüller metric. []{#lemma:a+b-gamma label="lemma:a+b-gamma"}
:::

::: proof
*Proof.* Fix $t=t_0$, and consider the flat structure on the torus given by $\partial U_{t_0} = \gamma(t_0)$. We may assume it has unit area. Recall that any Teichmüller geodesic through $\gamma(t_0)$ is given as follows. Select two orthogonal geodesic foliations $F_1$ and $F_2$ on the torus. Select $\lambda>0$. For any $u \in {\mathbb{R}}$, obtain a new metric by multiplying vectors along $F_1$ by $\exp(-\lambda\,u)$ and multiplying vectors along $F_2$ by $\exp(\lambda\,u)$. This is a "stretch--squeeze" map, which preserves the area of the torus. It gives a one--parameter family of flat structures on the torus, which we denote by $\zeta(u)$.

Teichmüller's theorem says that in the case of the torus, this stretch--squeeze map has the minimal quasiconformal distortion, so is a Teichmüller geodesic. For each $u$, the derivative of the map $\zeta(u)$ takes an infinitesimal circle to an infinitesimal ellipse, the ratio of whose axes is $\exp(2u\lambda)$. Thus for any $u$, the distance between the structure $\zeta(0) = \gamma(t_0)$ at time $0$ and $\zeta(u)$ at time $u$ is $$d(\zeta(0), \zeta(u)) = \frac{1}{2}\inf_f\log K_f =
\frac{1}{2}\log(e^{2u\lambda}) = \lambda\,u.$$ Therefore, $\lambda = \| \zeta'(u) \|$, where the norm is given with respect to the Teichmüller metric. In particular, $\lambda =
\|\zeta'(0)\|$.

On the other hand, for any point on the torus, let $u_1$ and $u_2$ be orthonormal vectors in the directions of $F_1$ and $F_2$ respectively. Then when we write the infinitesimal change of metric induced by $\zeta'(0)$ in coordinates given by $u_1$ and $u_2$, we obtain at every point a diagonal matrix $\Lambda$ with $-\lambda$, $\lambda$ on the diagonal, since at each time $u$ those vectors are just multiplied by $e^{-\lambda\,u}$, $e^{\lambda\,u}$, respectively. Thus if we let $g_u$ be the metric on the torus induced by $\zeta(u)$, we have $$\left.\frac{d}{du}\right|_{u=0} g_u(x,y) = 2 g_0(\Lambda\,x, y).$$

Now we relate this discussion to the term $a^2+b^2$.

Recall the infinitesimal deformation of the hyperbolic cone structure of $X$ is encoded by the one--form $\omega$. In particular, the infinitesimal change in metric is given by the real part $\eta$. That is, if we let $g_t$ be the metric on $X$ at time $t$, then $$\left.\frac{d}{dt}\right|_{t_0}\, g_t(x,y) \;=\; 2 g_{t_0}(\eta(t_0) x, y).
\label{eqn:dotg}$$ (See the displayed equation on page 374 of [@hk:univ].)

We are interested in the infinitesimal change in the metric on $\partial U_{t_0}$. Since $\eta$ decomposes into $\eta_0 + \eta_c$, and only $\eta_0$ changes the holonomy of $\partial U$, we know the infinitesimal change in metric on $\partial U_{t_0}$ is given by $\eta_0$.

We have an explicit formula for $\eta_0$, written in orthonormal coordinates with respect to the metric $g_{t_0}$, given by $e_1$, $e_2$, $e_3$, where $e_1$ is radial and $e_2$ points in the direction of the meridian. Consider again equation ([\[eqn:eta0mat\]](#eqn:eta0mat){reference-type="ref" reference="eqn:eta0mat"}). Since the first row and column for the matrix of $\eta_0$ are zero, we see that $\eta_0$ actually has no effect on or contribution to the change of metric in the radial direction of $U$. Hence $\eta_0$ itself gives the infinitesimal change of metric on the torus $\partial U_{t_0}$, or $\gamma'(t_0) = \eta_0(t_0)$.

When we write $\eta_0$ in orthonormal coordinates $e_2$, $e_3$ on the torus, we discard the first row and column of the matrix of equation ([\[eqn:eta0mat\]](#eqn:eta0mat){reference-type="ref" reference="eqn:eta0mat"}), and obtain the $2\times 2$ matrix $$A = \left[\begin{array}{cc}-a&b\\b&a\end{array}\right].
\label{eqn:define-A}$$ Here the first column of $A$ gives the infinitesimal change in the meridional direction, the second the change in the direction orthogonal to the meridian. That is, if we restrict the metric $g_t$ to $\partial U_t$, we may rewrite equation ([\[eqn:dotg\]](#eqn:dotg){reference-type="ref" reference="eqn:dotg"}) as $$\left.\frac{d}{dt}\right|_{t=t_0}\, g_t(x,y) =
2g_{t_0}(\eta_0(t_0)\,x, y) = 2\left<Ax, y\right>.$$

Hence $A$ is a matrix representation of $\gamma'(t_0)$, the infinitesimal change of metric of the torus $\partial U_{t_0}$.

We can diagonalize $A$. For any point on the torus, there exist orthonormal vectors $u_1$ and $u_2$ such that when we put $A$ into coordinates given by $u_1$ and $u_2$, $A$ is diagonal with $-\sqrt{a^2+b^2}$ and $\sqrt{a^2+b^2}$ on the diagonal. Moreover, since $A$ does not depend on the point on the torus (that is, for any point on the torus we obtain the same matrix $A$), $u_1$ and $u_2$ determine orthogonal geodesic foliations $F_1$ and $F_2$. These, in turn, determine a Teichmüller geodesic $\zeta(u)$ with $\zeta(0) =
\gamma(t_0)$, whose initial tangent vector $\zeta'(0)$ agrees with $A$ at every point, and has Teichmüller norm $\|\zeta'(0\| =
\sqrt{a^2+b^2}$. Thus infinitesimally, $\gamma(t)$ and $\zeta(u)$ agree near $t=t_0$ and $u=0$, respectively. Hence $\|\gamma'(t_0)\| =
\|\zeta'(0)\| = \sqrt{a^2+b^2}$. ◻
:::

::: remark
In the proof of Lemma [\[lemma:a+b-gamma\]](#lemma:a+b-gamma){reference-type="ref" reference="lemma:a+b-gamma"}, we showed that for any time $t$, $\gamma(t)$ agrees infinitesimally with an explicit Teichmüller geodesic which is completely determined by the matrix $A$. We will use this again below.
:::

Finally, putting Lemmas [\[lemma:b_U=area\]](#lemma:b_U=area){reference-type="ref" reference="lemma:b_U=area"}, and [\[lemma:a+b-gamma\]](#lemma:a+b-gamma){reference-type="ref" reference="lemma:a+b-gamma"} together with equation ([\[eqn:eta-bound\]](#eqn:eta-bound){reference-type="ref" reference="eqn:eta-bound"}), we have completed the proof of the following theorem.

::: theorem
Let $X_t$ be a hyperbolic cone deformation with a cusp. That is, for each time $t$, the hyperbolic cone manifold $X_t$ has a cusp which remains a cusp throughout the deformation. Let $U_t$ be a horoball neighborhood of the cusp. Let $\gamma(t)$ denote the path $\partial U_t$ travels through the Teichmüller space of the torus. Then the change in $\partial U_t$ is bounded by the following inequality. $$2\,\|\gamma'(t)\|^2 \mbox{Area}(\partial U_t) \leq \sum b_j(t)$$ The sum on the right hand side is over all components of the singular locus. []{#thm:cusp-1 label="thm:cusp-1"}
:::

Note Theorem [\[thm:cusp-1\]](#thm:cusp-1){reference-type="ref" reference="thm:cusp-1"} gives an inequality identical to that of Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}, except for the boundary terms $b_j$ on the right hand side. We will bound these, and complete the proof of Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}, in Section [\[sec:bdrybound\]](#sec:bdrybound){reference-type="ref" reference="sec:bdrybound"}. First, we set up a similar theorem to Theorem [\[thm:main-norm-length\]](#thm:main-norm-length){reference-type="ref" reference="thm:main-norm-length"}.
