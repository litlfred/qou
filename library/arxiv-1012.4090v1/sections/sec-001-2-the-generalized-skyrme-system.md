---
doc_id: arxiv-1012.4090v1
doc_title: "Generalized Skyrme Crystals"
section_id: sec-001-2-the-generalized-skyrme-system
section_title: "The Generalized Skyrme System"
section_number: 2
pages: 1-2
source_pdf: 1012.4090v1.pdf
source_sha256: 02fe4a5eb36ff0ed
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.955
doc_brief: "Generalized Skyrme Crystals — This letter deals with triply-periodic (crystalline) solutions in a family of Skyrme systems, namely where the ﬁeld takes values in the squashed 3-sphere."
---
In this section, we give some details of the one-parameter interpolating family of Skyrme systems. The field is denoted $\Phi_{\beta}=(\Phi_1,\Phi_2,\Phi_3,\Phi_4)$, where each component $\Phi_{\beta}$ is a function of the spatial coordinates $x^j=(x^1,x^2,x^3)=(x,y,z)$, and the constraint $\Phi_{\beta}\Phi_{\beta}=1$ is imposed. The energy density for the system, parametrized by $\alpha\in[0,1]$, is

$$\label{Enden}
  {\cal E}=\lambda_2[(\partial_j\Phi_{\beta})(\partial_j\Phi_{\beta})-\alpha P_jP_j]
  +\lambda_4[2(1-\alpha)F^j_{\beta\gamma}F^j_{\beta\gamma}+\alpha Q^jQ^j],$$

where

$$\begin{aligned}
P_j &=& \Omega_{\beta\gamma}\Phi_{\beta}\partial_j\Phi_{\gamma},  \\
F^j_{\beta\gamma} &=&
    \textstyle\frac{1}{2}\varepsilon^{jkl}(\partial_k\Phi_{\beta})(\partial_l\Phi_{\gamma}),  \\
Q^j &=& \Omega_{\beta\gamma}F^j_{\beta\gamma},
\end{aligned}$$

with $\Omega_{\beta\gamma}$ being a symplectic form with non-zero components $\Omega_{12}=-\Omega_{21}=-\Omega_{34}=\Omega_{43}=1$. The coupling constants $\lambda_2$ and $\lambda_4$ can be scaled as desired, by changing the units of energy and length; in what follows, we shall use the 'geometrical' choice $\lambda_2=1/[4\pi^2(3-\alpha)]$ and $\lambda_4=1/[4\pi^2(3-2\alpha)]$ as in [@W04]. The effect of this is that the energy of a 1-skyrmion on $\mathbb R^3$ is approximately independent of $\alpha$ ($E_1\approx1.22$).

If we are thinking of the Skyrme model as a nonlinear theory of pions, then the deformation when $\alpha$ becomes positive may be viewed as putting one of the three pions on a different footing from the other two. To see this explicitly, we impose the boundary condition $\Phi_{\mu}\to(0,0,0,1)$ as $|x^j|\to \infty$, and identify $(\Phi_1,\Phi_2,\Phi_3)$ as the pion fields in the usual way. Then in the asymptotic region the energy density ([\[Enden\]](#Enden){reference-type="ref" reference="Enden"}) becomes

$$\label{Enden_asymp}
  {\cal E}\approx\lambda_2[(\partial_j\Phi_1)^2+(\partial_j\Phi_2)^2+(1-\alpha)(\partial_j\Phi_3)^2].$$

If $\alpha=1$, then one of the fields becomes non-dynamic. This amounts to passing from the original target space $S^3\cong{\rm SU(2)}$ to the quotient space $S^2\cong{\rm SU(2)/U(1)}$, by the Hopf projection

$$\begin{aligned}
\psi_1 &=& 2(\Phi_1\Phi_3-\Phi_2\Phi_4),   \nonumber \\
\psi_2 &=& 2(\Phi_2\Phi_3+\Phi_1\Phi_4),   \nonumber \\
\psi_3 &=& \Phi_3^4+\Phi_4^2-\Phi_1^2-\Phi_2^2. \label{hopfproj}
\end{aligned}$$

The relevant field is then the unit 3-vector $\vec\psi$, and the energy density ([\[Enden\]](#Enden){reference-type="ref" reference="Enden"}) becomes $$\label{Enden_Hopf}
  {\cal E} = \frac{1}{32\pi^2}\left[(\partial_j\vec\psi)^2
       + \frac{1}{4}(G_{jk})^2\right],$$

where $G_{jk}=
\vec\psi\cdot(\partial_j\vec\psi)\times(\partial_k\vec\psi)$. This is the Skyrme-Faddeev energy [@FN97].

The energy $E[\Phi]$ is the integral of ([\[Enden\]](#Enden){reference-type="ref" reference="Enden"}) over $\mathbb R^3$, or over a fundamental cell if one is dealing with periodic fields. There is a Bogomolny-type lower bound [@M87] on the energy of fields with topological charge $N$, namely $E\geq6N\sqrt{\lambda_2 \lambda_4}\mathop{\rm vol}\nolimits{(\Sigma)}$. Using the fact that the volume of the squashed 3-sphere is $2\pi^2\sqrt{1-\alpha}$, and with our choice of $\lambda_2$ and $\lambda_4$, this gives

$$\label{Bog}
    E_N \geq \frac{\sqrt{1-\alpha}}{\sqrt{(1-\alpha/3)(1-2\alpha/3)}}.$$

In the limit $\alpha=1$, the bound ([\[Bog\]](#Bog){reference-type="ref" reference="Bog"}) becomes trivial. There are various nontrivial bounds in this case. For isolated Hopf solitons on $\mathbb R^3$, we know that $E_N\geq cN^{-1/4}$, where $c$ is a constant; it is conjectured that this bound holds for $c=1$ [@W99]. This bound is not valid for triply-periodic fields $\Phi:T^3\to S^2$; but in that case there is another lower bound, which follows from the general formula given in [@Sp10]: if $\Phi$ is triply-periodic, and $L$ is the largest of its periods, then its normalized energy satisfies $E_N\geq\pi/(2L)$.

For $\alpha=0$, the expression ([\[Enden\]](#Enden){reference-type="ref" reference="Enden"}) gives the standard static Skyrme energy, and it has an obvious O(4) symmetry. For $\alpha\neq0$, the symmetry is broken to U(2), this being the subgroup of O(4) which preserves the symplectic form $\Omega$.

In this letter, we are focusing on crystalline configurations, so the fields are periodic in $(x^1,x^2,x^3)$ with periods $(L_1,L_2,L_3)$ respectively. In effect, $\Phi$ is a map from $T^3$ to $S^3$, and it is classified topologically by its degree $N\in\mathbb Z$. The topological classification of maps from $T^3$ to $S^2$, which is relevant to the $\alpha=1$ case, is more complicated. But if we restrict to fields which are algebraically inessential, meaning that the 2-form $G_{jk}$ belongs to the trivial cohomology class in $H^2(T^3,\mathbb Z)$, then the classification remains a single integer $N\in\mathbb Z$ (*cf.* [@KS06]). The Hopf charge of the Hopf projection $\vec\psi$ of $\Phi$ is equal to the degree of $\Phi$, so it is consistent to let $N$ denote either.
