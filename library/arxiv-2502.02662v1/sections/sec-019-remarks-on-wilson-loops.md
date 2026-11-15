---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-019-remarks-on-wilson-loops
section_title: "Remarks on Wilson Loops"
section_number: null
pages: 24-25
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.992
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#WilsonLoops label="WilsonLoops"} In the previous subsections, we have studied partition functions of the chiral Yang-Mills theory. We have shown that in the absence of boundaries, the partition functions are reproduced by a deformed Gromov-Witten theory of the target space. Furthermore, we have argued that boundaries with prescribed holonomies may be thought of as operator insertions, and that their correlation functions match the corresponding Gromov-Witten correlators. In this subsection, we study correlators of Wilson lines in chiral Yang-Mills theory. As an opening remark, we observe that the expectation value of a Wilson loop depends on the area it encloses. Therefore, the area deformation of the Gromov-Witten theory of the target space must be patch-dependent: we view the parameter $t$ as an operator which associates its area to the patch under consideration.

Wilson lines on a manifold of genus $G$ and area $t$ are computed by gluing manifolds of genus $G$ and zero, with respective area $t_1$ and $t_2=t-t_1$, along a boundary with an extra character insertion: $$\langle s_{\mu} \rangle_G = \int dU Z^{+}_{G,t_1} (U) s_{\mu}(U) Z^{+}_{0,t_2} (U^{-1})\, .$$ As we explained in section [\[StringDual\]](#StringDual){reference-type="ref" reference="StringDual"}, one should think of the functions $Z^{+}_{G,t_1} (U)$ and $Z^{+}_{0,t_2}(U^{-1})$ as Gromov-Witten invariants relative to the boundary with prescribed holonomy $U$.

If we rewrite such Wilson line expectation values in terms of symmetric group quantities, we find: $$\begin{gathered}
    \langle s_{\mu} \rangle_G =  \frac{d_{\mu}}{d !}\, \sum_{d_1,d_2} g_s^{d_1 (2G-1)} g_s^{-d_2} e^{-\frac{t_1 d_1+t_2  d_2}{2}}  \sum_{\substack{\lambda\, \vdash d_1\\ \rho\, \vdash d_2}} \left(\frac{d_{\lambda}}{d_1!}\right)^{2-2G} \left(\frac{d_{\rho}}{d_2 !}\right)^2 \Omega_{g_s}(\lambda)^{1-2G}
    \\
    \Omega_{g_s}(\rho)\  e^{-g_s (t_1 f_{2}(\lambda)+t_2 f_{2}(\rho))}
    \sum_{\substack{\alpha\, \vdash d_1\\ \beta\, \vdash d \ }} z_{\alpha\cup \beta} f_{\alpha}(\lambda) f_{\beta}(\mu)  f_{\alpha\cup \beta}(\rho) \delta_{d_1+d,d_2}\, ,
\end{gathered}$$

where $\mu$ is a partition of $d$ and $\alpha\cup\beta$ denotes the concatenation of the conjugacy classes $\alpha$ and $\beta$. This expression may be simplified to render the gluing method more manifest on the symmetric group side of the equation: $$\langle s_{\mu} \rangle_G = \left(\frac{e^{-\frac{t_2}{2}}}{g_s}\right)^d \, \sum_{\beta\, \vdash d} \chi_{\mu}(\beta) \Bigg( \sum_{d_1} g_s^{d_1(2G-2)}  e^{-\frac{t d_1}{2}} \sum_{\alpha\, \vdash d_1} \frac{z_{\alpha\cup \beta}}{z_{\beta}}  \langle C_{\alpha} \rangle_{d_1, G}^{t_1,u}  \langle C_{\alpha \cup \beta} \rangle_{d+d_1, 0}^{t_2,u}\Bigg) \, .
    \label{WilsonLineGluing}$$

Equation ([\[WilsonLineGluing\]](#WilsonLineGluing){reference-type="ref" reference="WilsonLineGluing"}) provides a generic gluing prescription for how to incorporate a Wilson line in the Hurwitz formulation of the Yang-Mills theory. This prescription involves a sum over a basis of intermediate states corresponding to conjugacy classes.

A direct string theoretic interpretation of the gluing procedure would be interesting. In particular, it would be neat to interpret the Wilson lines as an extended object in the dual string theory.
