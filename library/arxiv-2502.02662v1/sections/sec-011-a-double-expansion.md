---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-011-a-double-expansion
section_title: "A Double Expansion"
section_number: null
pages: 15-16
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.906
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
If we neglect the $\Omega$ points and deformation by transpositions[^1] the partition function of chiral Yang-Mills theory on a surface with $k$ boundaries becomes:

$$Z_{G}^{+}(U_1,\dots,U_k)=\sum_d (q\, g_s^{2G-2+k})^d\, \langle \prod_{i=1}^k \left(\sum_{\alpha\vdash d} p_{\alpha}(U_i) C_{\alpha}\right) \rangle_d\, .
    \label{dSumDictionary}$$ We wish to make the string theory structure of these correlators manifest. In string theory, two expansions must be distinguished. On the one hand, there is the perturbative expansion in the string coupling $g_s$. On the other hand, there is an expansion over world-sheet instantons, with expansion parameter $e^{-\frac{A}{2\pi \alpha'}}$, where $\frac{1}{2\pi \alpha'}$ is the string tension and $A$ is the area of the embedding of the world-sheet in the target space. In our two-dimensional context, the world-sheet covers the target space and $A$ equals the area of the target space. In order to bring out the structure of the double expansion, we reshape the expression [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"} using the Riemann-Hurwitz formula[@CavalieriMiles]: $$2g-2=d(2G-2)+kd-\sum_i \ell(\alpha_i)\, ,$$ where $g$ denotes the genus of the covering surface and $\ell(\alpha_i)$ is the length of a conjugacy class, i.e. the number of disjoint cycles of any element in this class. We write

$$Z_{G}^{+}(U_1,\dots,U_k) =\sum_d q^d \sum_{\alpha_i\in Y^d} g_s^{2g-2} \left(\prod_{i=1}^{k} p_{\alpha_i}(U_i)\right)\left \langle g_s^{l(\alpha_1)}  C_{\alpha_1} \cdots  g_s^{l(\alpha_k)} C_{\alpha_k}\right \rangle_d\, .
    \label{StringyHurwitz}$$ Let us analyze the content of equation [\[StringyHurwitz\]](#StringyHurwitz){reference-type="eqref" reference="StringyHurwitz"}. Firstly, we recall that, as explained in section [\[StringDual\]](#StringDual){reference-type="ref" reference="StringDual"}, the covering space of Hurwitz theory is naturally interpreted as the world-sheet of a string theory. Therefore, the factor $g_s^{2g-2}$ can be interpreted as the usual weighting factor for the different world-sheet topologies. However, unlike the standard case, there is no explicit sum over all possible topologies of the world-sheet in the above expression. This a distinctive feature of the string theory at hand. Indeed, for each correlator of a Gromov-Witten theory, there is only one contributing world-sheet at fixed instanton degree $d$. Nevertheless, an insertion in the Yang-Mills theory is represented by a sum over all possible conjugacy classes in the Hurwitz theory, which implies that many genera come into play.

One can make this sum over the genus of the world-sheet manifest by introducing the constrained correlators $$\langle \cdot \rangle_{g,d}:=\langle \cdot \rangle_{d} \cdot \delta(g=g(d))\, ,
    \label{FieldToString}$$ where $g(d)$ in the argument of the $\delta$ function is the genus of the covering surface determined by the Riemann-Hurwitz formula. It is a standard fact in topological string theory that there exist topological constraints on correlators.

In terms of the constrained correlators, the partition function [\[StringyHurwitz\]](#StringyHurwitz){reference-type="eqref" reference="StringyHurwitz"} reads $$Z_{G}^{+}(U_i) =\sum_g g_s^{2g-2} \sum_d q^d \left \langle \left(\sum_{\alpha\vdash d} p_{\alpha}(U_1) g_s^{l(\alpha)}  C_{\alpha}\right) \cdots \left(\sum_{\alpha\vdash d} p_{\alpha}(U_k) g_s^{l(\alpha)} C_{\alpha}\right)\right \rangle_{g,d}\, . 
    \label{LooksLikeAString}$$ This is manifestly the genus expansion of a string theory and we interpret the sum over $d$ as the sum over world-sheet instanton degrees. This allows us to identify the string tension as -- see also [@Gross:1993yt; @Horava:1993aq] --: $$\alpha'=\frac{1}{\pi g_{YM}^2}\, . \label{StringTension}$$

[^1]: Note that, formally, we have defined a deformed Hurwitz theory for arbitrary values of the parameters $t$ and $u$. Therefore, equation [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"} may be thought of as the corresponding string theory correlation functions for $t=u=0$. We discuss this aspect further in appendix [\[PhaseTransitions\]](#PhaseTransitions){reference-type="ref" reference="PhaseTransitions"}.
