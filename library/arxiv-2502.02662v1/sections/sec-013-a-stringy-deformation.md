---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-013-a-stringy-deformation
section_title: "A Stringy Deformation"
section_number: null
pages: 17-19
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.965
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#AStringyDeformation label="AStringyDeformation"} We start from the undeformed partition function [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"} and study the implementation of the deformation into the structure of the genus expansion of the string theory. Consider first the deformation by transpositions. The exponential can be expanded inside the correlation functions to write $$Z_{G}^{+}(U_1,\dots,U_k) = \sum_d g_{s}^{(2G-2+k)d} q^d \sum_r (-1)^r \frac{(g_s t)^r}{r!} \langle C_2^r \prod_{i=1}^{k} C_{\alpha_i}\rangle_{d}$$ The Riemann-Hurwitz equation may be leveraged to write this expression as a correlator in a string theory. The method consists again in introducing a redundant sum over all genera together with a constrained correlator $\langle \cdot \rangle_{g,d}$: $$Z_{G}^{+}(U_1,\dots,U_k) = \sum_g g_{s}^{(2G-2+k)d+r} \sum_d  q^d \sum_r (-1)^r \frac{t^r}{r!} \langle C_2^r \prod_{i=1}^{k} C_{\alpha_i}\rangle_{g,d}\, .$$ The correlator is non-vanishing when the genus $g$ takes the value determined by the Riemann-Hurwitz formula $$2g-2=(2G-2+k)d-\sum_i \ell(\alpha_i)+r\, .$$ One then identifies the power of the string coupling $g_s$ with the genus $g$ of the covering surface, up to the appropriate normalization factor for the vertex operators. We write: $$\begin{aligned}
    Z_{G}^{+}(U_1,\dots,U_k) = \sum_g g_{s}^{2g-2} \sum_d  q^d \langle e^{-tC_2} \prod_{i=1}^{k} g_s^{\ell(\alpha_i)} C_{\alpha_i}\rangle_{g,d}\, .
\end{aligned}$$ The genus expansion has absorbed the factor of the string coupling $g_s$ featured in the deformation. The deformation by transpositions thus preserves the stringy structure of the correlators. In general, a deformation by conjugacy classes $C_{\eta}$ preserves the stringy structure of the correlators if each insertion comes with a factor of the string coupling raised to the power of the charge of the conjugacy class $g_{s}^{\lvert \eta \rvert}$. For transpositions, $\lvert C_2 \rvert = 1$, and each insertion $C_2$ comes indeed with a single factor $g_s$. Importantly, this means that we interpret the power expansion of the exponential as insertions of distinct observables: $\langle C_2^r C_{\alpha} \rangle_{g,d}$ denotes the correlator $$\underbrace{\langle C_2,\dots, C_2}_{r\ \text{times}}, C_{\alpha} \rangle_{g,d}\, ,$$ as indicated in the previous section.

We move on to study the effect of $\Omega$ deformations. We recall the definition of the exponential distance operator $\Omega$: $$\Omega_{g_s u} :=\, \sum_{\eta\vdash d} (g_s u)^{\lvert \eta \rvert} C_{\eta} \, .$$ The criterion just stated is manifestly satisfied and we deduce that the $g_s$ factor in $\Omega_{g_s u}$ is absorbed by the genus expansion. Furthermore, the inverse $\Omega_{g_s u}^{-1}$ can be defined by a series expansion, in which each term $C_{\eta_1}\dots C_{\eta_s}$ is again accompanied by a factor $g_{s}^{\lvert \eta_1 \rvert+\dots+\lvert \eta_s \rvert}$. As a result, the genus expansion soaks up the factors of the string coupling contained in the operator $\Omega_{g_s u}^{-1}$ as well.

In conclusion, the observables of chiral Yang-Mills theory admit a string theoretic expansion $$Z_{G}^{+}(U_1,\dots,U_k) = \sum_g g_{s}^{2g-2} \sum_d  q^d \langle \prod_{i=1}^{k} \left(\sum_{\alpha_ik} p_{\alpha}(U) g_s^{\ell(\alpha_i)} \hat{C}_{\alpha_i}\right) \rangle_{g,d}^{\text{def}}\, ,$$ where the correlation functions of the deformed theory are defined by $$\langle \hat{C}_{\alpha_1}\cdots \hat{C}_{\alpha_k}\rangle_{g,d}^{\text{def}} =  \langle C_{\alpha_1}\cdots C_{\alpha_k}\cdot e^{-tC_2} \Omega_{u}^{2-2G-k} \rangle_{g,d} \, .$$ We stress that by the explicit criterion we laid out, generic deformations do not preserve the string theoretic structure of correlation functions.

We thus view the preservation of the structure as further new and strong evidence that chiral Yang-Mills theory in two dimensions admits a string dual.
