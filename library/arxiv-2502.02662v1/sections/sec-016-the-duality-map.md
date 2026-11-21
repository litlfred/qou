---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-016-the-duality-map
section_title: "The Duality Map"
section_number: null
pages: 20-21
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.992
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#TheDualityMap label="TheDualityMap"} In order to extend this picture to the correlation functions, we need to establish a dictionary between the observables of chiral Yang-Mills theory and those of the deformed extended Hurwitz theory. Given an insertion $U$, we need to identify the unique element $\sum_{s} a_s(U) \hat{\mathsf{A}}_s$ in the algebra of partial permutations which behaves as $$\sum_{\alpha\vdash d} p_{\alpha}(U) g_s^{\ell(\alpha)} \hat{C}_{\alpha}$$ inside genus-$g$, degree-$d$ correlation functions, for all values of the genus and degree. Our strategy is the following. Firstly, we isolate permutations with a given non-trivial structure. That is, we look for permutations $\sigma$ obtained by completing the minimal partial permutation $\bar{s}$ to all possible degrees. For each such permutation $\sigma$, we have the equation $$\sum_{s} g_s^{\ell(s)}  a_s(U) \langle \hat{A}_s \, (\dots) \rangle_{g,d} = g_s^{\ell(\sigma)} p_{\sigma}(U) \langle \hat{C}_{\sigma} \, (\dots) \rangle_{g,d}\, ,
    \label{DictionaryCoeffEqs}$$ where the only partial permutations $s$ relevant to the sum are the partial permutations of the form $\bar{s}\cup 1^k$, with $0\leq k\leq d-\lvert d_{\bar{s}} \rvert$. Thus, we obtain the following equations for the coefficient $a_{\bar{s}\cup 1^k}$ $$\sum_{k=0}^{d-\lvert d_{\bar{s}} \rvert} g_{s}^{\ell(\bar{s})+k} a_{\bar{s}\cup 1^k}(U) \binom{d-\lvert d_{\bar{s}} \rvert}{k} = g_{s}^{\ell(\sigma)}\, p_{\sigma}(U) \, .$$ There is an equation for each degree $d\geq \lvert d_{\bar{s}} \rvert$, and the coefficients $a_s$ thus obey an infinite system of linear equations.

Its matrix form is lower triangular and is a version of the Pascal triangle weighted by factors of the string coupling. It can be solved recursively, as explained in appendix [\[Solving the Dictionary\]](#Solving the Dictionary){reference-type="ref" reference="Solving the Dictionary"}. The coefficients of the partial permutation dual to an insertion $U$ are given by $$a_s(U):= p_{\bar{s}}(U) \sum_{l=0}^{m_{1}(s)} (-1)^{m_{1}(s)-l} g_{s}^{l-m_{1}(s)} \binom{m_{1}(s)}{l}  p_{1^l}(U) \, .
    \label{DictionarySolution}$$ We conclude that the insertion of a boundary holonomy $U$ in the chiral Yang-Mills theory translates to the insertion of the observable $\sum_s a_s(U) \hat{\mathsf{A}}_s$ in the deformed extended Hurwitz theory. The role of trivial sheets in the string theory is played by the power-sum polynomials in the Yang-Mills theory. Each trivial sheet corresponds to a factor $\tr U$.

An interesting consequence of this dictionary is that in the large $N$ limit, a hole operator algebra can be defined for the Yang-Mills theory. The elements of this algebra are the holonomies in the unitary group $U(\infty)$. The product is defined such that, in any given correlation function, holonomies $U_1$ and $U_2$ may be replaced by a holonomy $U_3$. We write $$Z(U_1,U_2,\dots) = \int dU_3\,  c(U_1,U_2;U_3) Z(U_3,\dots)\, .$$ The $c(U_1,U_2;U_3)$ are structure constants for the algebra and they can be written as: $$c(U_1,U_2;U_3):=\sum_{r,s,t} \hat{g}_{rs}^{\ \ t} g_s^{\lvert d_r \rvert+\lvert d_s \rvert-\lvert d_t \rvert} a_{r}(U_1) a_{s}(U_2) a^{\perp}_{t}(U_3)\, .$$ In this expression, the coefficients $\hat{g}_{rs}^{t}$ are the structure constants of the partial permutation algebra $\mathcal{A}_{\infty}$ in the renormalized basis and the $a^{\perp}_{t}$ form the basis of vectors dual to the vectors $a_s$ which means that the inner product between the two bases is a Kronecker delta: $$\int dU a_s(U) a_t^{\perp}(U) = \delta_{s,t}\, .$$ These vectors $a^{\perp}_{t}$ are explicitly given by linear combinations of the power sum polynomials $$a_s^{\perp}(U)=\sum_{k\geq m_{1}(s)} \binom{k}{m_{1}(s)} g_s^{m_{1}(s)-k}  p^*_{\bar{s}\cup 1^k}(U)\, .$$
