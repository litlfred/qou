---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-025-63-holomorphic-and-tropical-triangles
section_title: "Holomorphic and tropical triangles"
section_number: 6.3
pages: 62-63
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.826
latex_coverage_ratio: 0.928
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:other-triangles label="sec:other-triangles"}

Having chosen a family of Lagrangians $\{L(d)\}_{d\in\Z}$ corresponding to the powers of an ample line bundle, we find that after positively perturbation, $HF^*(L(d_1),L(d_2))$ is concentrated in degree $0$ when $d_1 \leq d_2$. The techniques of section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"} allow us to compute the holomorphic triangles contributing to the multiplication $$HF^*(L(d_2),L(d_3))\otimes HF^*(L(d_1),L(d_2))\to HF^*(L(d_1),L(d_3))$$ Looking at the winding numbers of the Lagrangians in the base once again yields an auxiliary $\Z$-grading. For fixed values of this $\Z$-grading on the input, one can determine the number of times that triangles contributing to the product cover the critical values $w_1,
\dots, w_n$; call these numbers $k_1,\dots,k_n$. Then the degeneration process breaks the triangle into $k = \sum_{i=1}^n k_i$ copies of the fibration over a disk with single critical value, as well a trivial fibration over a $(k+3)$-gon. Over the disks the count of sections is $1$, while the analysis of sections over the $(k+3)$-gon still goes through because, in the fiber, the Lagrangian boundary condition is still a sequence of curves on the cylinder whose slope changes monotonically. Hence the matrix coefficients of this product are binomial coefficients of the form $\binom{k}{s}$.

In this degeneration argument, the Lefschetz singularities that come from different focus-focus singularities are not distinguished, while in the case of tropical triangles, different singularities of the affine structure contribute differently to the tropical curves. We find that this family of triangles, with total count $\binom{k}{s}$, corresponds to several tropical triangles $T_{s_1,\dots,s_n}$ with $s_1+\cdots+s_n = s$, indexed by ordered partitions of $s$, with $0$ allowed as a part (of which there are $\binom{s+n}{s}$). The triangle $T_{s_1,\dots,s_n}$ uses the tropical disk emanating from the $i$-th singularity either $s_i$ or $k_i-s_i$ times, and the multiplicity of $T_{s_1,\dots,s_n}$ is $\binom{k_1}{s_1}\binom{k_2}{s_2}\cdots\binom{k_n}{s_n}$. The equality of the total counts $$\binom{k}{s} = \sum_{\{s_1,\dots,s_n \mid s_i \geq 0,
    \sum_{i=1}^n s_i = s\}} \prod_{i=1}^n \binom{k_i}{s_i}$$ follows from comparing the coefficients of $x^s$ in the equation $$(1+x)^k = \prod_{i=1}^n (1+x)^{k_i}$$
