---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model"
section_id: sec-003-the-lagrangian-and-euler-lagrange-equations
section_title: "The Lagrangian and Euler-Lagrange equations"
section_number: null
pages: 4-7
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model — 21 sections: Compact Q-balls and Q-shells withi; Introduction; The extended Skyrme-Faddeev model"
---
The Extended Skyrme-Faddeev (ESF) model augmented by a potential, defined on a $CP^N$ target space, is conveniently formulated using the principal variable $X$ [@Ferreira:1998zx]. The Lagrangian density is expressed by derivative terms containing $L_{\mu}\equiv X^{-1}\partial_{\mu}X$, as well as a non-derivative potential term $V(X)$. We examine a model whose Lagrangian density, $\mathcal{L}$, comprises five terms: a potential term, $\mathcal{L}_0$; a standard quadratic term, $\mathcal{L}_2$; a (quartic) Skyrme term, $\mathcal{L}_4^{(S)}$; and two additional quartic terms, $\mathcal{L}_{4}^{(1)}$ and $\mathcal{L}_{4}^{(2)}$. The total Lagrangian density is given by: $${\cal L}={\cal L}_2+{\cal L}_0+{\cal L}_4^{(S)}+{\cal L}_{4}^{(1)}+ {\cal L}_{4}^{(2)}.\label{lagr1}$$ These individual Lagrangian terms are explicitly defined as: $$\begin{aligned}
{\cal L}_0&=-\mu^2V(X)\\
{\cal L}_2&=-\frac{M^2}{2}\;{\rm Tr}(L_{\mu}L^{\mu})\\
{\cal L}_4^{(S)}&=\frac{1}{e^2}\;{\rm Tr}([L_{\mu},L_\nu][L^{\mu},L^\nu])\\
{\cal L}_4^{(1)}&=\frac{\beta}{2}\;\big({\rm Tr}(L_{\mu}L^{\mu})\big)^2\\
{\cal L}_4^{(2)}&=\gamma\;{\rm Tr}(L_{\mu}L_{\nu}){\rm Tr}(L^{\mu}L^{\nu}).
\end{aligned}$$

The term $\mathcal{L}_2$ constitutes the standard $CP^N$ Lagrangian. When combined with a properly chosen potential term $\mathcal{L}_0$, these two terms collectively support compact Q-ball and Q-shell solutions [@Klimas:2017eft]. While the additional quartic terms, $\mathcal{L}_4^{(1)}$ and $\mathcal{L}_4^{(2)}$, have been investigated in other physical contexts, their application to Q-ball solutions represents a novel approach. This paper, therefore, primarily focuses on analyzing the impact of these quartic terms on the morphology of the resulting Q-balls.

It is important to note that for the $N=1$ case, the terms $\mathcal{L}_4^{(1)}$ and $\mathcal{L}_4^{(2)}$ are functionally equivalent. This $N=1$ scenario, previously discussed in [@Ferreira:2008nn], included only a single additional quartic term, which was defined using a unit complex three-component vector $\vec{n}$.

The coupling constant $M^2$ has the dimension of $L^{-2}$, where $L$ denotes the dimension of length. Similarly, $\mu^2$ has the dimension of $L^{-4}$. Conversely, the constants $e^{-2}$, $\beta$, and $\gamma$ are dimensionless. In the context of the Lagrangian, the parameters are required to satisfy the constraints $M^2>0$, $e^2<0$, and $\mu^2>0$. The specific values of the dimensionless constants $\beta$ and $\gamma$ will be discussed subsequently, with particular attention to ensuring the positive definiteness of the energy density.

The principal variable $X$, as introduced in [@EICHENHERR1980528; @Ferreira:1984bi], is employed to parameterize symmetric spaces, with the complex projective space $CP^N$ serving as a canonical example. We consider the $(N+1)$-dimensional defining representation wherein the $SU(N+1)$-valued element $g$ is parameterized by a set of $N$ complex fields $u_i$ according to the following matrix form: $$\begin{aligned}
g&\equiv\frac{1}{\sqrt{1+u^{\dagger} \cdot u}}\left(\begin{array}{cc}
\Delta&iu\\
iu^{\dagger}&1
\end{array}\right)\label{parametryzacja}
\end{aligned}$$ where the $N \times N$ block $\Delta$ is defined as: $$\begin{aligned}
\Delta_{ij}&\equiv \sqrt{1+u^{\dagger} \cdot u}\,\delta_{ij}-\frac{u_iu_j^*}{1+\sqrt{1+u^{\dagger} \cdot u}}.
\end{aligned}$$ The principal variable $X$ is then expressed in terms of the complex fields $u_i$ as the square of the element $g$: $$\begin{aligned}
X(g)&=g^2=
\left(\begin{array}{cc}
{\mathbb{I}}_{N\times N} & 0 \nonumber \\
0 & -1 \nonumber 
\end{array}\right)
+
\frac{2}{1+\sqrt{1+u^{\dagger} \cdot u}}\left(\begin{array}{cc}
-u\otimes u^\dagger & iu \nonumber \\
iu^\dagger & 1  
\end{array}\right).
\end{aligned}$$

The Lagrangian given in Equation [\[lagr1\]](#lagr1){reference-type="eqref" reference="lagr1"} simplifies to the following expression: $${\cal L}=-\frac{1}{2}\left[M^2\eta_{\mu\nu}+C_{\mu\nu}\right]\tau^{\nu\mu}-\mu^2V.\label{lagr2}$$ The potential $V$ adopted for this investigation, defined in [@Klimas:2017eft], is given by: $$V=\frac{1}{2}\sqrt{{\rm Tr}(1-X)}=\sqrt{\frac{u^{\dagger}\cdot u}{1+u^{\dagger}\cdot u}}.\label{potencjal}$$ In Equation [\[lagr2\]](#lagr2){reference-type="eqref" reference="lagr2"}, $\eta_{\mu\nu}$ is the Minkowski metric, defined as $\eta_{\mu\nu}={\rm diag}(1,-1,-1,-1)$. The derivative-coupling tensor $\tau_{\nu\mu}$ represents the kinetic and gradient term and is given by: $$\tau_{\nu\mu}:=-4\frac{\partial_{\mu}u^{\dagger}\cdot\Delta^2\cdot\partial_{\nu}u}{(1+u^{\dagger}\cdot u)^2},\label{tau}$$ where the matrix $\Delta^2$ is defined as: $$\Delta^2_{ij}=(1+u^{\dagger} \cdot u)\;\delta_{ij}-u_iu^*_j.$$ The coefficients $C_{\mu\nu}$ are defined by: $$\begin{aligned}
C_{\mu\nu}:=&M^2\eta_{\mu\nu}-\frac{4}{e^2}\Big[(\beta e^2-1)\tau^{\alpha}_{\,\,\,\,\alpha}\eta_{\mu\nu}+(\gamma e^2-1)\tau_{\mu\nu}+(\gamma e^2+2)\tau_{\nu\mu}\Big].
\end{aligned}$$

Only the $M^2$--proportional term in the Lagrangian stems directly from quadratic terms. The remaining contributions, however, originate from quartic interactions. The influence of these quartic terms can be interpreted as a perturbation--provided their magnitude is sufficiently small--acting upon the principal solution determined by the combination of the quadratic term and the potential $V$.

To facilitate the analysis of this model, we will reformulate it using dimensionless coordinates. This procedure requires the introduction of a characteristic length scale, denoted as $r_0$. Although various definitions based on the coupling constants are possible, a specific choice must be made. The selection of the length scale has varied across prior studies; for instance, in our previous investigation of the $CP^N$--type model with a potential [@Klimas:2017eft], we defined the scale simply as $r_0=M^{-1}$. Conversely, in the study of vortices within the extended Skyrme-Faddeev model [@Amari:2015sva], the length scale was set as $r_0:=\frac{2}{M}\frac{1}{\sqrt{-e^{2}}}$, where $e^2<0$. The latter definition presents a formal inconvenience when considering the limit $e^{-2}\to 0$, as the length scale $r_0$ would vanish unless a corresponding adjustment is made to the parameter $M$. Given that a quadratic term proportional to $M^2$ is explicitly retained in the Lagrangian for the current analysis, we adopt the more straightforward definition: $r_0:=M^{-1}$.

We proceed by expressing the Lagrangian density of the model using the dimensionless counterparts of the Derivative-Coupling Tensor, $\tau_{\mu\nu}$, and the coefficient tensor, $C_{\mu\nu}$. Let $\{\xi^{\mu}\}_{\mu=0,\ldots,3}$ represent a set of dimensionless curvilinear coordinates, defined by the transformation $\xi^{\mu}=\xi^{\mu}(\tilde{x}^{\alpha})$, where $\tilde{x}^{\mu} = x^{\mu}/r_0$ are the dimensionless Cartesian coordinates. The partial derivatives transform according to the chain rule, incorporating the characteristic length scale $r_0$: $$\frac{\partial}{\partial x^{\mu}}=r_0^{-1}\frac{\partial}{\partial \tilde x^{\mu}}=r_0^{-1}\frac{\partial\xi^{\alpha}}{\partial \tilde x^{\mu}}\frac{\partial}{\partial  \xi^{\alpha}}.$$ The components of the physical flat metric $\eta_{\mu\nu}$ (in the original Cartesian coordinates $x$) are related to the components of the metric tensor in the curvilinear system, $g_{\alpha\beta}(\xi)$, by the standard tensor transformation rule: $$\eta_{\mu\nu}=\frac{\partial\xi^{\alpha}}{\partial \tilde x^{\mu}}\frac{\partial\xi^{\beta}}{\partial \tilde x^{\nu}}g_{\alpha\beta}(\xi).\nonumber$$ Consequently, the derivative--coupling tensor $\tau_{\mu\nu}(x)$, defined in Equation [\[tau\]](#tau){reference-type="eqref" reference="tau"}, transforms to its dimensionless counterpart, $\tau_{\alpha\beta}(\xi)$, which contains derivatives with respect to the curvilinear coordinates $\xi^{\alpha}$: $$\tau_{\mu\nu}(x)=r_0^{-2}\frac{\partial\xi^{\alpha}}{\partial \tilde x^{\mu}}\frac{\partial\xi^{\beta}}{\partial \tilde x^{\nu}}\tau_{\alpha\beta}(\xi).\nonumber$$ As a result of these transformations, the original tensor $C_{\mu\nu}(x)$ can be expressed as a linear combination of its dimensionless counterpart, $\widetilde{C}_{\alpha\beta}(\xi)$, scaled by $M^2$: $$\begin{aligned}
C_{\mu\nu}(x)=M^2\frac{\partial\xi^{\alpha}}{\partial \tilde x^{\mu}}\frac{\partial\xi^{\beta}}{\partial \tilde x^{\nu}}\tilde C_{\alpha\beta}(\xi).
\end{aligned}$$ The dimensionless coefficient tensor $\widetilde{C}_{\mu\nu}(\xi)$ is defined in terms of the curvilinear metric $g_{\mu\nu}(\xi)$ and the dimensionless tensor $\tau_{\mu\nu}(\xi)$ as: $$\begin{aligned}
\widetilde C_{\mu\nu}(\xi):=g_{\mu\nu}(\xi)&-\frac{\kappa}{4}\Big[(\beta e^2-1)\tau^{\alpha}_{\,\,\,\,\alpha}(\xi)g_{\mu\nu}(\xi)\nonumber\\&+(\gamma e^2-1)\tau_{\mu\nu}(\xi)+(\gamma e^2+2)\tau_{\nu\mu}(\xi)\Big].\label{Cxi}
\end{aligned}$$

The dimensionless combination of coupling constants and the characteristic length scale $r_0$ is defined as: $$\kappa:=\frac{16}{M^2 r_0^2e^2}.$$ The parameter $\kappa$ is crucial for indicating the decoupling of the quartic terms, which originate from the Lagrangian components proportional to $e^{-2}$, $\beta$, and $\gamma$. It should be noted that $\kappa$ is constrained to be non-positive ($\kappa\le 0$). If the Skyrme term vanishes (i.e., $e^{-2}\to 0$), the parameter $\kappa$ approaches zero, provided the length scale parameter $r_0$ remains finite. Crucially, the products $\kappa \beta e^2$ and $\kappa \gamma e^2$ tend to zero as $\kappa\to 0$ if and only if both $\beta$ and $\gamma$ simultaneously approach zero ($\beta\to 0$ and $\gamma\to 0$). Should the condition $\beta\to 0$ and $\gamma\to 0$ be satisfied concurrently, the full model simplifies considerably, reducing solely to the $\mathbb{C}P^N$ model incorporating only the potential term.

The primary objective of this paper is to investigate the effect of quartic terms on Q-ball solutions. To achieve this, it is essential to demonstrate the ability to decouple these quartic terms by performing the simultaneous limit where $e^{-2}\rightarrow 0$, $\beta\rightarrow 0$, and $\gamma\rightarrow 0$. This specific limiting procedure should effectively recover the known Q-ball solutions previously obtained in [@Klimas:2017eft].

The Lagrangian defined in Equation [\[lagr2\]](#lagr2){reference-type="eqref" reference="lagr2"} can be expressed in terms of dimensionless quantities as ${\cal L}=r_0^{-4}\widetilde{\cal L}$, where the dimensionless Lagrangian density $\widetilde{\cal L}$ takes the form: $$\widetilde{\cal L}=-\frac{1}{2}\left[g_{\mu\nu}(\xi)+\widetilde C_{\mu\nu}(\xi)\right]\tau^{\nu\mu}(\xi)-\tilde\mu^2V.$$ Here, $\tilde{\mu}^2$ is a dimensionless constant defined as $\tilde{\mu}^2:=\frac{r_0^2}{M^2}\mu^2$. The Euler-Lagrange equations of motion (EOMs) derived from this dimensionless Lagrangian are given by: $$\begin{aligned}
&\frac{1}{\sqrt{-g}}\partial_{\alpha}\Big(\sqrt{-g}g^{\mu\alpha}g^{\nu\beta}\widetilde C_{\mu\nu}\partial_{\beta}u_i\Big)-\frac{g^{\mu\alpha}g^{\nu\beta}\widetilde C_{\mu\nu}}{1+u^{\dagger}\cdot u}\Big[(u^{\dagger}\cdot \partial_{\alpha}u)\partial_{\beta}u_i+(u^{\dagger}\cdot \partial_{\beta}u)\partial_{\alpha}u_i\Big]+\nonumber\\
&+\frac{\tilde\mu^2}{4}\Gamma_i=0\label{eom1}
\end{aligned}$$ where $g$ is the determinant of the curvilinear metric tensor, $g:=\det(g_{\mu\nu})<0$. The term $\Gamma_i$ is derived from the variation of the potential $V$ with respect to the complex field $u_i^*$ and is defined as: $$\begin{aligned}
\Gamma_i&\equiv(1+u^{\dagger}\cdot u)\sum_{k=1}^N\left[(\delta_{ik}+u_iu^*_k)\frac{\delta V}{\delta u_k^*}\right]\\
&=\frac{u_i}{2}\sqrt{\frac{1+u^{\dagger}\cdot u}{u^{\dagger}\cdot u}}.
\end{aligned}$$ It should be noted that the form of the potential $V$, and consequently the expression for $\Gamma_i$, can be modified in several qualitatively equivalent ways while preserving the compact nature of the localized solutions (Q-balls).
