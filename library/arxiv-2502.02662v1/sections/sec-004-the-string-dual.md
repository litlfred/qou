---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-004-the-string-dual
section_title: "The String Dual"
section_number: null
pages: 6-8
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.969
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#StringDual label="StringDual"} In this subsection, we discuss the string dual to the extended Hurwitz theory [@OP1]. See also [@Benizri:2024mpx]. Firstly, we describe the string theory, which is a theory of two-dimensional gravity coupled to two-dimensional matter. The matter theory is a $\mathcal{N}=(2,2)$ supersymmetric sigma model with world-sheet $\Sigma$ and a two-dimensional, closed target space $X$ of genus $G$. The $A$-twist of the sigma model is a topological field theory whose operators are in one-to-one correspondence with the de Rham cohomology of the target space. We denote the observable associated with the volume form on $X$ by $\omega$. The topological matter model was fully solved in [@Witten:1989ig]. Consider next the topological string theory obtained by coupling the model on $X$ to topological gravity [@Witten:1989ig; @Dijkgraaf:1990qw]. Its observables are given by the gravitational descendants of the observables of the $X$ model. We will focus on the stationary sector, namely on the half infinite tower of descendants of the volume form. We denote the corresponding operators $\tau_k$ where $k \in \mathbb{N}$ labels the gravitational descendant.

Their correlation functions compute Gromov-Witten invariants, which are defined by integration of classes on the moduli space of Riemann surfaces of genus $g$ with a number of marked points equal to the number of operator insertions [@Witten:1989ig; @OP1; @Hori:2003ic].

We stress that the observables $\tau_k$ may be thought of as vertex operators. Indeed, they are defined in terms of the pullback of the volume form on the target space to the covering space, which is identified with the world-sheet of the theory.[^1] In string theory, every vertex operator comes with a factor of the string coupling $g_s$. Therefore, we can identify vertex operators in this theory as $$V_{k} = g_s \tau_k\, .$$ An insertion of an operator $V_k$ on a world-sheet generates a single string state. The correlators of the string theory may then be written as $$\langle V_{k_1} \cdots V_{k_n}\rangle = \sum_{g} g_s^{2g-2} \langle V_{k_1}\cdots V_{k_n}\rangle_{g}\, ,
    \label{VertexOp}$$ where the sum is over the genus $g$ of the world-sheet.

A backbone to our approach is that these Gromov-Witten invariants are equal to fixed-degree correlation functions of completed cycles in Hurwitz theory [@OP1]. Completed single cycles are linear combinations of orbits of partial permutations defined in [@OP1]. They form a multiplicative basis of the algebra. We write

$$\bar{A}_{k}=\sum_{r} \rho_{k,r} A_{r}\, ,
    \label{CompletedCyclesDefinition}$$ where the sum is over partitions $r$ of varying degree.[^2] The coefficients $\rho_{k,r}$ vanish when $\lvert d_r \rvert>k$ and yield a Kronecker delta for $\lvert d_r \rvert = k$.

The operator dictionary in fixed-degree correlation functions between the extended Hurwitz theory and its string dual reads [@OP1] $$\frac{\bar{A}_{k+1}}{k!} \leftrightarrow \tau_{k} \, .
    \label{Dictionary}$$ Plugging this duality into the string correlators [\[VertexOp\]](#VertexOp){reference-type="eqref" reference="VertexOp"}, we translate an integral over moduli space to a topological quantum field theory correlator:

$$\langle V_{k_1} \cdots V_{k_n}\rangle =  \sum_{r_1,\dots,r_n} \prod_i \Big(g_s^{k_i+1-\lvert d_{r_i}\rvert} \frac{\rho_{k_i+1,r_i}}{k_i!} \Big) \langle  A'_{r_1}\cdots A'_{r_n}\rangle\, .
     \label{HurwitzDualityMap}$$ Note that the factors of the string coupling $g_s$ that appear in equation [\[HurwitzDualityMap\]](#HurwitzDualityMap){reference-type="eqref" reference="HurwitzDualityMap"} are overall factors weighting different correlators. Therefore, they do not affect the genus expansion structure of a given correlator. Furthermore, the completed cycles appear as subdominant corrections to the lore according to which single cycles in a symmetric orbifold theory are dual to single string states [@Benizri:2024mpx].

Conversely, since the completed cycles form a basis of the algebra of partial permutations, equation [\[Dictionary\]](#Dictionary){reference-type="eqref" reference="Dictionary"} can be inverted to express the correlators of simple partial permutation in terms of vertex operators expectation values. We first define the coefficients $\zeta_{r,s}$ as the coefficients of the partial permutations in the basis of completed cycles $$A_r = \sum_s \frac{\zeta_{r,s}}{\prod_{i=1}^{\ell(s)} (s_i-1) !} \bar{A}_s\, .$$

We then write the substitution rule $$A'_{r} \leftrightarrow \sum_{\substack{s \,:\\ \lvert d_s \rvert\leq \lvert d_r \rvert}} g_s^{\lvert d_r \rvert-\lvert d_s \rvert} \zeta_{r,s}\,  V_{s-1}\, ,
    \label{SubRule}$$

where the $V_{s-1}:=\prod_{i=1}^{\ell(s)}V_{s_i-1}$ are products of single string vertex operators. Correlation functions involving such multi-vertex operators $V_s$ are evaluated on the moduli space that exhibits as many marked points as there are single insertions $V_{s_i}$.

Physically, such multi-cycle vertex operators are identified with multi-string states. Note that completed cycles also include single cycle corrections [@OP1] which should survive in the connected correlators. Therefore, the corrections from completed cycles do not trivialize when we consider connected correlators.

We stress that the identification of the extended Hurwitz correlators with the Gromov-Witten correlation functions [@OP1] is an important non-trivial step in the process of identifying a string dual to two-dimensional Yang-Mills theory. It identifies an ordinary topological field theory correlator with a well-defined integral over the moduli space of Riemann surfaces. That these highly different concepts coincide is proven through equivariant localization [@OP1; @Okounkov:2002cz]. Exploiting this non-trivial correspondence is the second new tool that distinguishes our approach from the literature.

To close this section, we explain how boundaries with prescribed boundary conditions can be incorporated in the gauge/string duality. Consider a target space $X$ with $m$ marked points. Hitherto, we have thought of marked points as sites of bulk operator insertions. The operator insertions in the gauge theory translate to vertex operators in the string theory. The requirement that a basis of bulk string vertex operators be multiplicative then imposes that single cycles be completed. However, in this simple topological setting, these operator insertions can equivalently be interpreted as boundaries (with an associated holonomy).

The marked points then correspond to boundary conditions[^3] and there is no need to complete the cycles. In other words, boundary conditions in a string theory should be treated as standard Hurwitz insertions on marked points. In Gromov-Witten theory, these insertions (in contrast to the bulk gravitational descendants of cohomology classes) are described as relative Gromov-Witten theory.

The relative theory computes Gromov-Witten invariants on surfaces with further specified ramification profiles $\eta_i$ in $m$ marked points -- see e.g. [@OP1] --: $$\langle \prod_{i=1}^{s} \tau_{k_i}, \eta_1, \dots, \eta_m \rangle_{g,d}\, .$$ To summarize, we have described two dual points of view: boundary conditions for open strings specified by ordinary partial permutations and closed string states corresponding to completed cycles.

Relative Gromov-Witten theory is particularly useful to study Wilson lines. As we shall review in section [\[WilsonLoops\]](#WilsonLoops){reference-type="ref" reference="WilsonLoops"} in the context of Yang-Mills theory, Wilson lines are computed by gluing manifolds with boundaries and specifying a character of the gauge group on that boundary. It will be more natural to think of this procedure in terms of boundaries rather than bulk operator insertions.

[^1]: We note that our identification of the world-sheet of the theory with the covering space is in accord with the description of Hurwitz theory as a symmetric orbifold and the identification of the world-sheet of the string in that context[@Pakman:2009zz].

[^2]: We use the characters $k,l,m,n$ of the latin alphabet to denote integers and the characters $r,s,t$ to denote partial permutations. Permutations are denoted by Greek letters.

[^3]: This simple string theory behaves as a finite-dimensional theory and boundary states for the closed string match the vertex operator insertions.
