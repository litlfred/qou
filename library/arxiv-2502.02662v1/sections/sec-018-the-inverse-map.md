---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-018-the-inverse-map
section_title: "The Inverse Map"
section_number: null
pages: 23-24
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
The duality map [\[DualityMap\]](#DualityMap){reference-type="eqref" reference="DualityMap"} we have uncovered is a rather complicated one, and it would be interesting to identify new Yang-Mills variables in terms of which which this map simplifies. To that effect, we shall invert the duality map [\[DualityMap\]](#DualityMap){reference-type="eqref" reference="DualityMap"}. We consider the correlation functions of standard vertex operators on the string theory side and derive their expression in terms of Yang-Mills observables. We start by inverting the relation ([\[SchurToPower\]](#SchurToPower){reference-type="ref" reference="SchurToPower"}). This yields an expression for the symmetric group characters in terms of the unitary group characters: $$\chi_{\lambda}(\alpha)=\int dU s_{\lambda}(U) p_{\alpha}(U^{-1})\, .$$ The observables of the deformed Hurwitz theory at fixed degree thus read:

$$\langle \prod_{i=1}^k \hat{C}_{\sigma_i} \rangle_{d}^{\text{def}}= \frac{1}{\prod_{i=1}^k  z_{\sigma_i}}\int\left( \prod_{i=1}^k  dU_i\right) \, p_{\sigma_1}(U_1^{-1})\cdots p_{\sigma_k}(U_k^{-1})\cdot Z_{d}^{+}(U_1,\dots,U_k)\, .
    \label{HurwitzAsYM}$$ The equation [\[HurwitzAsYM\]](#HurwitzAsYM){reference-type="eqref" reference="HurwitzAsYM"} suggests that the basis most natural for comparing operators on both sides is that of the complex-conjugated power sum polynomials $p_{\alpha}^*$: $$\langle \prod_{i=1}^k p^*_{\alpha_i} \rangle_{+} = \int dU_1\cdots dU_k \,  p^*_{\alpha_1}(U)\cdots p^*_{\alpha_k}(U)\, Z^{+}(U_1,\dots,U_k) \, ,
    \label{UpsilonBasis}$$ as first argued in [@Gross:1993yt]. We note that the insertions must be associated with Young diagrams of the same order to get non-vanishing correlators. In particular, one may replace the full partition function of Yang-Mills in equation [\[UpsilonBasis\]](#UpsilonBasis){reference-type="eqref" reference="UpsilonBasis"} with the fixed-degree partition function, up to a factor of the chemical potential. We may then write $$q^d g_s^{2g(d)-2} \langle \prod_{i=1}^k g_s^{\ell(\sigma_i)} \hat{C}_{\sigma_i} \rangle_{d}^{\text{def}} 
    = \langle \prod_{i=1}^k \frac{p_{\sigma_i}^*}{z_{\sigma_i}} \rangle_{+}\, ,
    \label{BetterHurwitzAsYM}$$ where $g(d)$ is the covering surface genus determined by the Riemann-Hurwitz formula for the ramification profiles $\sigma_i$.

Expressing the correlators of the deformed Gromov-Witten theory in terms of Yang-Mills observables is then a basis change in the algebra of partial permutations.[^1]. We write $$\begin{aligned}
    \langle \prod_{i=1}^{k} \hat{\tau}_{k_i} \rangle^{\text{def}}= \langle \Tilde{\Omega}_{g_s u}^{-k} \prod_{i=1}^{k} \frac{\bar{A}_{k_i +1}}{k_i !} \rangle^{\text{def}} \, .
\end{aligned}$$ Writing out the completed cycles explicitly, rearranging the sum and taking out the combinatorial factors arising from the correlators of partial permutations, we obtain $$\langle \prod_{i=1}^{k} \hat{\tau}_{k_i} \rangle^{\text{def}}
    =\sum_{s_1,\dots, s_k} \sum_d  g_s^{2g(d)-2} q^d  \left(\prod_{i=1}^{k} \binom{m_1(\sigma_i)}{m_1(s_i)}\, \frac{\rho_{k_i+1,s_i}}{k_i !}\right)\langle \prod_{i=1}^{k}  \hat{C}_{\sigma_i} \rangle_{d}^{\text{def}} \, .$$ Substituting in equation [\[BetterHurwitzAsYM\]](#BetterHurwitzAsYM){reference-type="eqref" reference="BetterHurwitzAsYM"}, we find $$\langle \prod_{i=1}^{k} \hat{\tau}_{k_i} \rangle^{\text{def}} = \sum_d \sum_{s_1,\dots, s_k} \left(\prod_{i=1}^{k}  \frac{g_s^{-\ell(\sigma_i)}}{k_i! z_{\sigma_i}} \binom{m_1(\sigma_i)}{m_1(s_i)} \rho_{k_i+1,s_i}\right) \langle \prod_{i=1}^k p_{\sigma_i}^* \rangle_{+}
   \label{YMSector}\, .$$

This equation is the inverse of [\[DualityMap\]](#DualityMap){reference-type="eqref" reference="DualityMap"}: it describes the Yang-Mills observables naturally computed by standard string theory correlators. These observables are a completed version of the power sum polynomials.

It is interesting to manipulate the expression a little further to uncover the role of the trivial sheets: $$\langle \prod_{i=1}^{k} \hat{\tau}_{k_i} \rangle^{\text{def}}  = \left\langle \sum_{s_1,\dots, s_k} \left(\prod_{i=1}^{k} \frac{\rho_{k_i+1,s_i}}{k_i!} \frac{g_s^{-\ell(s_i)}}{z_{s_i}}\, p^*_{s_i}\right) \sum_d \left(\prod_{i=1}^k \frac{g_s^{-(d-\lvert d_{s_i} \rvert)}}{(d-\lvert d_{s_i} \rvert)!}\right) (p_{1}^*)^{d-\lvert d_{s_i} \rvert} \right\rangle_{+}\, .$$ They give rise both to operator insertions $p_1^\ast$ as well as combinatorial factors.

[^1]: We note that a basis of the family of Yang-Mills observables encoded by the string theory at fixed-degree is given by the correlators $\langle \prod_{i=1}^k p_{\sigma_i}^* \rangle_d$.
