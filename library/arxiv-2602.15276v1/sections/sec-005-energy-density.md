---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model"
section_id: sec-005-energy-density
section_title: "Energy density"
section_number: null
pages: 9-12
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.989
doc_brief: "Compact Q-balls and Q-shells within a $CP^N$ Skyrme-Faddeev type model — 21 sections: Compact Q-balls and Q-shells withi; Introduction; The extended Skyrme-Faddeev model"
---
A crucial prerequisite for constructing physically meaningful solutions is ensuring the positive definiteness of the energy density. Given that the Lagrangian for this model comprises multiple terms connected by various coupling constants, it is essential to guarantee a non-negative energy density across all configurations before proceeding to the derivation of solutions for specific parameter values. Consequently, the focus of the following section is a detailed analysis of the model's energy density.

The dimensionless Hamiltonian density, $\widetilde{\cal H} := r_0^4{\cal H}$, is conventionally defined via the Legendre transformation: $$\widetilde {\cal H}=\sum_{m=-l}^l\left(\frac{\delta \widetilde{\cal L}}{\delta(\partial_t u_m)}\partial_tu_m+\frac{\delta \widetilde {\cal L}}{\delta(\partial_t u^*_m)}\partial_tu^*_m\right)-\widetilde {\cal L}.$$ Given the structure of the Lagrangian density, where its variation with respect to the derivative-coupling-tensor is $\delta \widetilde{\cal L}=-\frac{1}{2}\tilde{C}_{\mu\nu}\delta \tau^{\nu\mu}$, the Hamiltonian density can be formally expressed using the components involving time derivatives as: $$\widetilde{\cal H}=-\widetilde C^{\mu t}\tau_{t\mu}-\widetilde C^{t\mu}\tau_{\mu t}-\widetilde{\cal L}.\label{H2}$$

For the field configuration defined by the ansatz [\[ansatz\]](#ansatz){reference-type="eqref" reference="ansatz"}, the dimensionless Hamiltonian density $\widetilde{\cal H}$ can be expressed in terms of the non-zero components of the derivative-coupling-tensor $\tau_{\mu\nu}(\xi)$ and the coefficient tensor $\widetilde{C}_{\mu\nu}(\xi)$ as: $$\widetilde{\cal H}=-2[\tilde C_{tt}\tau_{tt}+\widetilde C_{tr}\tau_{tr}]-\tilde{\cal L}$$ where the full dimensionless Lagrangian density $\widetilde{\cal L}$ is: $$\begin{aligned}
\widetilde{\cal L}=&-\frac{1}{2}\Big[\tau_{tt}-\tau_{rr}-\frac{2}{r^2}\tau_{\theta\theta}+\widetilde C_{tt}\tau_{tt}+\widetilde C_{rr}\tau_{rr}+2\widetilde C_{tr}\tau_{tr}+\frac{2}{r^4}\widetilde C_{\theta\theta}\tau_{\theta\theta}\Big].\nonumber
\end{aligned}$$ The dimensionless Hamiltonian density $\widetilde{\cal H}$ naturally decomposes into a quadratic part ($\widetilde{\cal H}_{02}$) and a quartic part ($\widetilde{\cal H}_{4}$), such that $\widetilde{\cal H}=\widetilde{\cal H}_{02}+\widetilde{\cal H}_{4}$. The part of the Hamiltonian density originating from the quadratic terms is given by: $$\begin{aligned}
\widetilde {\cal H}_{02}=\frac{4\omega^2f^2}{(1+f^2)^2}+\frac{l(l+1)}{r^2}\frac{4f^2}{1+f^2}+\frac{4f'^2}{(1+f^2)^2}+\tilde\mu^2V.\label{H0}
\end{aligned}$$ The portion of the Hamiltonian density arising from the quartic interactions is initially expressed as: $$\begin{aligned}
\widetilde {\cal H}_4&=\kappa\Bigg[\frac{6\omega^2f^2}{(1+f^2)^2}F_1(r)-\frac{2f'^2}{(1+f^2)^2}F_2(r)\nonumber\\&+\frac{12\omega^2 f'f}{(1+f^2)^2}F_3(r)-\frac{l(l+1)}{r^2}\frac{2f^2}{1+f^2}F_4(r)\Bigg].\label{H1a}
\end{aligned}$$ By substituting the explicit forms of the functions $F_n(r)$ into the above expression, the quartic Hamiltonian density $\widetilde{\cal H}_4$ is obtained in the fully expanded form: $$\begin{aligned}
\widetilde{\cal H}_4=&-\kappa\Bigg[-2\overbrace{(\beta e^2+2\gamma e^2)}^{0}\frac{3\omega^4f^2-f'^4}{(1+f^2)^4}\nonumber\\&+4(\beta e^2-4)\frac{\omega^2f^2f'^2}{(1+f^2)^4}\nonumber\\&+4(\beta e^2-1)\frac{l(l+1)}{r^2}\frac{f^2(\omega^2f^2+f'^2)}{(1+f^2)^3}\nonumber\\
&+\underbrace{(2\beta e^2+2\gamma e^2-1)}_{\beta e^2-1}\frac{l^2(l+1)^2}{r^4}\frac{f^4}{(1+f^2)^2}\Bigg].\label{H1b}
\end{aligned}$$ The total energy $E$ of the field configuration is determined by integrating the dimensionless Hamiltonian density over the volume, incorporating the $\sqrt{-g}$ factor for volume element transformation (which simplifies to $r^2 \sin\theta$ in spherical coordinates): $$\begin{aligned}
E=\int_{{\mathbb{R}}^3}d^3\xi\sqrt{-g}\,\Big(\widetilde {\cal H}_{02}+\widetilde {\cal H}_4\Big)
=4\pi\int_0^{\infty}dr\, r^2\Big(\widetilde {\cal H}_{02}+\widetilde {\cal H}_4\Big).
\end{aligned}$$

Following our previous analysis of the extended Skyrme-Faddeev model [@Ferreira:2010jb], we assume that $e^2<0$ and $M^2>0$. The Hamiltonian density of the quadratic terms, $\widetilde{\cal H}_{02}$ (Equation [\[H0\]](#H0){reference-type="eqref" reference="H0"}), is inherently positive definite due to its structure. Upon examining the full Hamiltonian density $\widetilde{\cal H}$ (Equation [\[H2\]](#H2){reference-type="eqref" reference="H2"}), specifically the quartic contribution $\widetilde{\cal H}_4$ (Equation [\[H1b\]](#H1b){reference-type="eqref" reference="H1b"}), we observe that most terms contribute positively to the energy density under the following constraints on the coupling constants: $$2 \beta e^2+2\gamma e^2-1\ge 0,\qquad\text{and}\qquad \beta e^2-4\ge 0.\label{leftbottom}$$ The only term in $\widetilde{\cal H}_4$ that is not intrinsically guaranteed to be positive definite is the one proportional to the combination of coupling constants $\beta e^2+2\gamma e^2$. To definitively ensure the overall positive definiteness of the total Hamiltonian density $\widetilde{\cal H}$, we impose the strong constraint: $$\beta e^2+2\gamma e^2=0.\label{upper}$$ This condition not only nullifies the potentially negative term but also simplifies the combination of coupling constants appearing in the last term of Equation [\[H1b\]](#H1b){reference-type="eqref" reference="H1b"} from $(2\beta e^2+2\gamma e^2-1)$ to ${\beta e^2-1}$.

The parameter space defined by the constraints [\[leftbottom\]](#leftbottom){reference-type="eqref" reference="leftbottom"} and $\beta e^2+2\gamma e^2\le 0$ is visually represented in FIG. [1](#bound){reference-type="ref" reference="bound"}. The upper boundary of this region, which is demarcated by the red line, corresponds precisely to the equality condition established in Equation [\[upper\]](#upper){reference-type="eqref" reference="upper"} ($\beta e^2+2\gamma e^2=0$). This boundary line represents the specific combination of coupling constants that guarantees a positive definite contribution of the quartic terms to the total energy density.

Notably, within the regime where ${e^2 < 0}$, the requirement for positive definiteness imposes constraints on the coupling constants such that ${\beta < 0}$ (which implies $\beta e^2 > 0$) and ${\gamma > 0}$ (which implies $\gamma e^2 < 0$). Below the upper boundary (the red line)--that is, for ${\beta e^2 + 2\gamma e^2 < 0}$?solutions with a non-negative energy density may still be permissible, provided that the additional condition ${3\omega^4 f^2 > f'^4}$ is locally satisfied.

<figure id="bound">

<figcaption>The coupling constant space delimited by the conditions <span class="math inline"><em>β</em><em>e</em><sup>2</sup> + 2<em>γ</em><em>e</em><sup>2</sup> ≤ 0</span>, <span class="math inline">2<em>β</em><em>e</em><sup>2</sup> + 2<em>γ</em><em>e</em><sup>2</sup> − 1 ≥ 0</span>, and <span class="math inline"><em>β</em><em>e</em><sup>2</sup> − 4 ≥ 0</span>, ensuring a non-negative contribution from the quartic terms.</figcaption>
</figure>

By applying these constraints ($\beta e^2+2\gamma e^2=0$, $e^2<0$, $M^2>0$), the radial equation of motion (Equation [\[eom1\]](#eom1){reference-type="eqref" reference="eom1"}) is simplified and can be expressed in the form: $$\begin{aligned}
&f''+\frac{2}{r}f'+\left(\omega^2\frac{1-f^2}{1+f^2}-\frac{l(l+1)}{r^2}\right)f-\frac{2ff'^2}{1+f^2}\nonumber\\&-\frac{\tilde\mu^2}{8}{\rm sgn}(f)\sqrt{1+f^2}+\kappa \,G(r) =0.\label{eq:radial}
\end{aligned}$$ Here, the function $G(r)$ represents the non-linear contributions resulting from the quartic terms and is defined as:

::: widetext
$$\begin{aligned}
G(r)=&-\underbrace{(\beta e^2+2\gamma e^2)}_{0}\frac{1}{(1+f^2)^2}\Bigg[3f'^2f''+\frac{2}{r}f'^3-\frac{6ff'^4}{1+f^2}-\omega^4\frac{(1-f^2)f^3}{1+f^2}\Bigg]\nonumber\\
&-(\beta e^2-1)\frac{l(l+1)}{r^2}\frac{1}{1+f^2}\Bigg[f^2f''+\frac{(1-2f^2)ff'^2}{1+f^2}+\omega^2\frac{(2-f^2)f^3}{1+f^2}\Bigg]\nonumber\\
&+(\beta e^2-4)\frac{\omega^2}{(1+f^2)^2}\left[f^2f''+\frac{2}{r}f^2f'+\frac{(1-3f^2)ff'^2}{1+f^2}\right]\nonumber\\
&+\underbrace{{\textstyle\frac{1}{2}}(2\beta e^2+2\gamma e^2-1)}_{\frac{1}{2}(\beta e^2-1)}\frac{l^2(l+1)^2}{r^4}\frac{f^3}{1+f^2},
\end{aligned}$$
:::

It is important to observe that the first term in the expression for $G(r)$ vanishes due to the imposed constraint $\beta e^2+2\gamma e^2=0$, and the coefficient of the final term simplifies to $\frac{1}{2}(\beta e^2-1)$.
