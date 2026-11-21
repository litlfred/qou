---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-008-25-the-andersenkashaev-state-integral
section_title: "The Andersen–Kashaev state-integral"
section_number: 2.5
pages: 18-19
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.938
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.AK41 label="sub.AK41"}

In this section we briefly recall the properties of the state-integral of Andersen--Kashaev for the $\mathbf{4}_1$ knot [@AK Sec.11.4], defined by $$\label{Z410}
  Z_{\mathbf{4}_1}(\tau) = 
  \int_{\mathbbm R+{\rm i}0} \Phi_\mathsf{b}(v)^2 \, {\rm e}^{-\pi {\rm i}v^2} {\rm d}v, \qquad (\tau=\sqrt{\mathsf{b}}) \,.$$ Here, $\operatorname{\Phi}_{\mathsf{b}}(z)$ is Faddeev's quantum dilogarithm [@Faddeev], in the conventions of e.g. [@AK Appendix A]. With this choice of contour, the integrand is exponentially decaying at $\pm \infty$ hence the integral is absolutely convergent. State-integrals have several key features:

-   They are analytic functions in $\mathbbm C'$.

-   Their restriction to $\mathbbm C\setminus\mathbbm R$ factorises bilinearly as finite sum of a product of a $q$-series and a $\tilde q$-series, where $q=\bold e(\tau)$ and $\tilde q=\bold e(-1/\tau)$; see [@Beem; @GK:qseries].

-   Their evaluation at positive rational numbers also factorises bilinearly as a finite sum of a product of a periodic function of $\tau$ and a periodic function of $-1/\tau$; see [@GK:evaluation].

-   State-integrals are equal to linear combinations of the median Borel summation of asymptotic series.

-   State-integrals come with a descendant version which satisfies a linear $q$-difference equation.

Let us explain these properties for the state-integral [\[Z410\]](#Z410){reference-type="eqref" reference="Z410"}. The integrand is a quasi-periodic meromorphic function with explicit poles and residues. Moving the contour of integration above, summing up the residue contributions, and using the fact that there are no contributions from infinity, one finds that [@GK:qseries Cor.1.7] $$\label{zlmuv0}
 Z(\tau)    =
    -{\rm i}
    \left(\frac{q}{\tilde{q}}\right)^{\frac{1}{24}}
    \left(\tau^{1/2}G^{(1)}(q)G^{(0)}(\tilde{q}) -
     \tau^{-1/2} G^{(0)}(q)G^{(1)}(\tilde{q})\right), \qquad (\tau \in \mathbbm C\setminus\mathbbm R).$$ When $\tau$ is a positive rational number, the quasi-periodicity of the integrand, together with a residue calculation leads to a formula for $Z(\tau)$ given in [@GK:evaluation]. More generally, in [@GGM:resurgent] we considered the descendant integral

$$\label{eq.statelm}
 Z_{\lambda,\mu}(\tau) =
    \int_{\mathcal D} \Phi_{\mathsf{b}}(v)^2 {\rm e}^{-\pi{\rm i}v^2 +
      2\pi(\lambda \mathsf{b}- \mu \mathsf{b}^{-1})v}{\rm d}v,$$

where $\lambda, \mu \in \mathbbm Z$ and the contour $\mathcal D$ is asymptotic at infinity to the horizontal line $\mathrm{Im}(v)=v_0$ where $v_0 > |\mathop{\mathrm{Re}}(\lambda\mathsf{b}-\mu\mathsf{b}^{-1})|$ but is deformed near the origin so that all the poles of the quantum dilogarithm located at $$c_\mathsf{b}+ {\rm i}\mathsf{b}m +{\rm i}\mathsf{b}^{-1}n,\quad m,n\in\mathbb{Z}_{\geq 0},$$ are above the contour.

These integrals factorise as follows:

$$\label{zlmu}
 Z_{\lambda,\mu}(\tau)    =
    (-1)^{\lambda-\mu+1}{\rm i}q^{\frac{\lambda}{2}}\tilde{q}^{\frac{\mu}{2}}
    \left(\frac{q}{\tilde{q}}\right)^{\frac{1}{24}}
    \left(\tau^{1/2}G^{(1)}_\lambda(q)G^{(0)}_\mu(\tilde{q}) -
     \tau^{-1/2} G^{(0)}_\lambda(q)G^{(1)}_\mu(\tilde{q})\right).$$ The above factorisation can be expressed neatly in matrix form. Indeed, let us define $$\label{Wgtred}
W^\mathrm{red}_{S,\lambda,\mu}(\tau) = \mathbf J^\mathrm{red}_\lambda(\tilde{q})^{-1}
\mathrm{diag}(\tau^{3/2}, \tau^{1/2}, \tau^{-1/2}) \, \mathbf J^\mathrm{red}_\mu(q) \,.$$ Using the $q$-difference equation [\[41Jqrec\]](#41Jqrec){reference-type="eqref" reference="41Jqrec"}, it is easy to see that $W^\mathrm{red}_{S,\lambda+1,\mu}(\tau)=A^{-1}(-1/\tau) W^\mathrm{red}_{S,\lambda,\mu}(\tau)$ and $W^\mathrm{red}_{S,\lambda,\mu+1}(\tau)=W^\mathrm{red}_{S,\lambda,\mu}(\tau) A(\tau)$ hence the domain of $W^\mathrm{red}_{S,\lambda,\mu}$ is independent of the integers $\lambda$ and $\mu$. Equation [\[zlmu\]](#zlmu){reference-type="eqref" reference="zlmu"} implies that $W^\mathrm{red}_{S,\lambda,\mu}(\tau)$ are given by the matrix $(Z_{\lambda+i,\mu+j}(\tau))$ (for $i,j =0,1$), up to left-multiplication by a matrix of automorphy factors.

Finally we discuss the relation between the Borel summation of the two asymptotic series $\Phi^{(\sigma_j)}(h)$ for $j=1,2$ and the descendant state-integrals. Since the Borel transform of those series may have singularities at the positive real axis, we denote by $s_{\rm med}$ their *median resummation* given by the average of the two Laplace transforms to the left and to the right of the positive real axis. Then, we have $$\label{smed12}
  \begin{aligned}
    s_{\rm med} ( \Phi^{(\sigma_1)} ) (\tau) = &{\rm i}(\tilde{q}/q)^{1/24}
    \left(-\frac{1}{2}Z_{0,0}(\tau)-\tilde{q}^{1/2}
      Z_{0,-1}(\tau)\right), \\
    s_{\rm med} ( \Phi^{(\sigma_2)} ) (\tau) = &{\rm i}(\tilde{q}/q)^{1/24}
    Z_{0,0}(\tau) \,.
  \end{aligned}$$
