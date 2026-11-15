---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-017-the-gromov-witten-formulation
section_title: "The Gromov-Witten Formulation"
section_number: null
pages: 21-23
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.993
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
The description of the correlation functions of chiral Yang-Mills theory in terms of a partial permutation algebra enables us to provide an explicit string dual by deforming the Gromov-Witten theory. We symbolically define this deformed Gromov-Witten theory as: $$\mathcal{L}_{GW} \to \mathcal{L}_{GW} - t\, \tau_1 + \log \Tilde{\Omega}_{u}^{2-2G} \, ,
    \label{StringDualLagrangian}$$ where the expression of the exponential distance operator at degree $d$ in terms of Gromov-Witten operators can be written using equation [\[SubRule\]](#SubRule){reference-type="eqref" reference="SubRule"} : $$\Tilde{\Omega}_{u} := \sum_{\substack{r\\ \text{minimal}}} u^{\lvert r \rvert} \left(\sum_{\substack{l\leq \lvert d_r \rvert\\ s\, \vdash \, l}} \zeta_{r,s}\, g_s^{\lvert r \rvert-\lvert s \rvert} \tau_{s-1} \right)  \, .
    \label{OmegaFromGW}$$ On the one hand, this deformation is implemented at the level of the string theory Lagrangian. Therefore, the factors of the string coupling $g_s$ that appeared in the parameters of the deformations in equation [\[ppDeformation\]](#ppDeformation){reference-type="eqref" reference="ppDeformation"} are absorbed by the string expansion. On the other hand, the definition of the operator $\Omega$ in terms of Gromov-Witten operators [\[OmegaFromGW\]](#OmegaFromGW){reference-type="eqref" reference="OmegaFromGW"} depends on the string coupling. This is a consequence of the fact that the dictionary of observables between completed cycles and Gromov-Witten invariants features $g_s$ factors once the genus expansion of the string theory is taken into account [\[SubRule\]](#SubRule){reference-type="eqref" reference="SubRule"}. We stress furthermore that the $\Omega$ operator is defined as a Taylor series in $g_s$ whose dominant term is $$\sum_{\substack{r\\ \text{minimal}}} u^{\lvert r \rvert}  \left( \prod_{i=1}^{\ell(r)} (r_i-1)! \right) \tau_{r-1}  \, .$$ Indeed, the coefficients $\zeta_{r,s}$ with $\lvert d_s \rvert < \lvert d_r \rvert$ vanish unless the condition $\lvert s \rvert < \lvert r \rvert$ is satisfied. This can be seen by decomposing the partial permutation orbit $A_r$ in single cycles and showing that the inequality is obeyed by each single cycle.

The need to deform the theory by an operator that includes subdominant corrections in the string coupling suggests that a more appropriate description of the string dual to two-dimensional Yang-Mills theory involves a new compactification of the moduli space of the string theory which is encoded by the exponential distance operator.

Moreover, this deformation imposes that the operators be renormalized by a factor of the inverse operator $\Omega^{-1}$. We denote the renormalized operators by $\hat{\tau}_r:=\Tilde{\Omega}_{u}^{-1} \prod_{i=1}^{\ell(r)} \tau_{r_i}$ and define corresponding vertex operators $\hat{V}_r := g_s^{\ell(r)} \hat{\tau}_r$. The correlation functions of the deformed Gromov-Witten theory are $$\left\langle \prod_{i=1}^n \hat{V}_{k_i} \right\rangle  ^{\text{def}} :=\left\langle \left(\prod_{i=1}^n g_s \tau_{k_i}\right) e^{-t\, \tau_1} \Tilde{\Omega}_{u}^{2-2G-n}  \right\rangle\, .$$

Restricted to fixed-degrees, they match the correlators of the renormalized conjugacy classes of the deformed Hurwitz theory [\[DeformedHurwitz\]](#DeformedHurwitz){reference-type="eqref" reference="DeformedHurwitz"}, up to a factor of the string coupling which is absorbed by the genus expansion. In terms of the Gromov-Witten vertex operators, the correlation functions of chiral Yang-Mills theory read $$Z^{+}[M_G,U_i]=\sum_{r_i} \sum_{\substack{s_i\ :\\ \lvert d_{s_i} \rvert\leq  \lvert d_{r_i} \rvert }} \prod_i \Big(a_{r_i}(U) \xi_{r_i,s_i}\Big) \langle \prod_i \hat{V}_{s_i-1} \rangle \, ,$$ where we have rescaled the coefficients $\zeta$ to make the string coupling factors associated with each vertex operator manifest: $$\xi_{r,s}=g_s^{\lvert d_r \rvert-\lvert d_s \rvert}\zeta_{r,s}\, .$$ The duality map sends a boundary holonomy $U$ in the chiral Yang-Mills theory to the following infinite linear combination of vertex operators in the string theory $$\sum_r a_r(U) \sum_{s} \xi_{r,s} \hat{V}_{s-1}\, .
    \label{DualityMap}$$ The existence of the map confirms that the string theory we have defined is indeed dual to chiral two-dimensional Yang-Mills theory.

To conclude our description of the string dual of chiral Yang-Mills theory, we stress that on the torus, no deformation of the moduli space of the string theory is required. Therefore, chiral Yang-Mills theory on the torus is exactly dual to the stationary sector of a $T^2$ matter model coupled to topological gravity and deformed by transposition interactions. The dictionary of observables is given by

$$U\leftrightarrow \sum_r a_r(U) \sum_{s} \xi_{r,s} \Tilde{\Omega}_u^{-1} V_{s-1}\, .$$
