---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model"
section_id: sec-004-radial-reduction
section_title: "Radial reduction"
section_number: null
pages: 7-9
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.963
doc_brief: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model — 21 sections: Compact Q-balls and Q-shells withi; Introduction; The extended Skyrme-Faddeev model"
---
Following the methodology established in [@Klimas:2017eft], we consider an odd number of scalar fields, specifically $N=2l+1$. For convenience, the field index $i=1, 2, \ldots, N$ is replaced by the corresponding angular momentum index $m=-l, \ldots, l$. We introduce spherical coordinates $(r, \theta, \phi)$ and apply the following ansatz for the field components $u_m(t, r, \theta, \phi)$: $$u_m(t,r,\theta,\phi):=\sqrt{\frac{4\pi}{2l+1}}f(r)Y_{lm}(\theta,\phi)e^{i\omega t}.\label{ansatz}$$ In this definition, $Y_{lm}(\theta, \phi)$ represents the spherical harmonics, $f(r)$ is a non-negative radial profile function ($f(r) \ge 0$), and $\omega$ is the oscillation frequency. This specific ansatz enables the reduction of both the Lagrangian and the field equations to a radial form.

The non-vanishing components of the derivative--coupling tensor, $\tau_{\mu\nu}(\xi)$, in the spherical coordinate system are found to be: $$\begin{aligned}
\tau_{tt}(\xi)&=-\frac{4\,\omega^2\,f^2}{(1+f^2)^2},
&\tau_{rr}(\xi)&=-\frac{4\,f'^2}{(1+f^2)^2},\nonumber\\
\tau_{tr}(\xi)&=-\frac{4i\,\omega\,ff'}{(1+f^2)^2},
&\tau_{rt}(\xi)&=-\tau_{tr}(\xi),\nonumber\\
\tau_{\theta\theta}(\xi)&=-4\,\frac{l(l+1)}{2}\frac{f^2}{1+f^2},
&\tau_{\phi\phi}(\xi)&=\sin^2\theta\,\tau_{\theta\theta}(\xi).\nonumber
\end{aligned}$$ Note that $f'$ denotes the derivative of the radial function with respect to $r$ ($f' = \partial f / \partial r$).

The components of the dimensionless coefficient tensor $\widetilde{C}_{\mu\nu}(\xi)$ in the spherical coordinate system are determined to be: $$\begin{aligned}
\widetilde C_{tt}&=1+\kappa F_1(r),\nonumber\\ 
\widetilde C_{rr}&=-1+\kappa F_2(r),\nonumber\\
\widetilde C_{tr}&=-\widetilde C_{rt}=-3i\omega\,\kappa  F_3(r),\nonumber\\
\widetilde C_{\theta\theta}&=r^2[-1+\kappa F_4(r)],\nonumber\\
\widetilde C_{\phi\phi}&=\sin^2\theta \,\tilde C_{\theta\theta},\nonumber
\end{aligned}$$ where the functions $F_1(r)$, $F_2(r)$, $F_3(r)$, and $F_4(r)$ encapsulate the radial dependence arising from the coupling terms. These functions are explicitly defined as: $$\begin{aligned}
F_1(r)&=(\beta e^2+2\gamma e^2)\frac{\omega^2f^2}{(1+f^2)^2}-(\beta e^2-1)\left[\frac{f'^2}{(1+f^2)^2}+\frac{l(l+1)}{r^2}\frac{f^2}{1+f^2}\right],\nonumber\\
F_2(r)&=(\beta e^2+2\gamma e^2)\frac{f'^2}{(1+f^2)^2}-(\beta e^2-1)\left[\frac{\omega^2 f^2}{(1+f^2)^2}-\frac{l(l+1)}{r^2}\frac{f^2}{1+f^2}\right],\nonumber\\
F_3(r)&=\frac{ff'}{(1+f^2)^2},\nonumber\\
F_4(r)&=(\beta e^2+\gamma e^2-{\textstyle\frac{1}{2}})\frac{l(l+1)}{r^2}\frac{f^2}{1+f^2}-(\beta e^2-1)\frac{\omega^2f^2-f'^2}{(1+f^2)^2}.\nonumber
\end{aligned}$$

The radial equation of motion (Equation [\[eom1\]](#eom1){reference-type="eqref" reference="eom1"}) can be reduced to the following ordinary differential equation for the radial profile function $f(r)$: $$\begin{aligned}
&(1-\kappa F_2)\left(f''+\frac{2}{r}f'-\frac{2ff'^2}{1+f^2}\right)-\kappa F_2'f'\nonumber\\
&-3\kappa\omega^2\left(F_3'+\frac{2}{r}F_3\right)f-(1-\kappa F_4)\frac{l(l+1)}{r^2}f\nonumber\\&+\omega^2(1+\kappa F_1)\frac{(1-f^2)f}{1+f^2}-\frac{\tilde\mu^2}{8}{\rm sgn}(f)\sqrt{1+f^2}=0\label{radialeq}
\end{aligned}$$ where the prime symbol ($\prime$) denotes the derivative with respect to the radial coordinate $r$, and the functions $F_1, F_2, F_3, F_4$ (and their derivatives $F_2', F_3'$) are defined based on the coupling constants and the profile $f(r)$.
