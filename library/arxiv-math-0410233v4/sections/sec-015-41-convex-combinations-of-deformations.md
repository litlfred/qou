---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-015-41-convex-combinations-of-deformations
section_title: "Convex combinations of deformations"
section_number: 4.1
pages: 18-19
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.944
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#subsec:convex label="subsec:convex"}

Recall that corresponding to an infinitesimal deformation is the 1--form $\omega_0$. We want $\omega_0$ to have certain desired properties.

By equation ([\[eqn:omega_0-decomp\]](#eqn:omega_0-decomp){reference-type="ref" reference="eqn:omega_0-decomp"}), we can decompose $\omega_0 =
(\omega_0)_j$ in $V_j$ as $$(\omega_0)_j =u_j\, \omega_m + (x_j+iy_j)\,\omega_\ell,$$ with $u_j$, $x_j$, and $y_j$ in ${\mathbb{R}}$, and where $\omega_m$ and $\omega_\ell$ were computed in [@hk:cone-rigid].

In [@hk:univ], it was shown that if the singular locus has just one component, then the entire cone deformation can be parameterized by the square of the cone angle $t=\alpha^2$. In this case, $u=u_1$ was determined explicitly in [@hk:univ]: $u = -1/(4\alpha^2),$ where $\alpha$ is the cone angle at the core of the singular solid torus $V=V_1$.

When we have multiple components of the singular locus, we may not necessarily be able to parameterize the cone deformation in this manner. However, we do have the following information.

First, for each $j$ in $\{1, \dots, n\}$, locally we have a deformation given by changing the $j$-th cone angle only and leaving the others fixed. This is a deformation with only one component of the singular locus, so the methods of [@hk:univ] apply, and this deformation can be parameterized by $t=\alpha_j^2$. Then $$(\omega_0)_j = -\frac{1}{4\alpha_j^2}\, \omega_m +
(x_{jj}+iy_{jj})\omega_\ell.$$

Changing the angle in the $j$-th tube $V_j$ and leaving the others fixed also affects the $k$-th tube $V_k$. Since there is no change of cone angle in this tube, $(\omega_0)_k$ can be expressed as $$(\omega_0)_k = (x_{jk}+iy_{jk})\omega_\ell.$$

Any of these $j$ deformations may be scaled by a factor $s_j\geq 0$, and we may take non-negative linear combinations. These correspond to new local deformations, in which the rates of change of cone angles vary according to the choice of the $s_j$. In a neighborhood of the $j$-th component, write: $$(\omega_0)_j = -\frac{s_j}{4\alpha_j^2}\,\omega_m + \sum_{k=1}^n (s_k
x_{kj} + i\,s_k y_{kj})\,\omega_\ell.
\label{eqn:omega_0-S}$$

Given a point $\bar{s} = (s_1, s_2, \dots, s_n)$, we may use these equations for $\omega_0$ to compute the forms $\eta_0$ explicitly, and thus compute the boundary terms $b_j = b_j(\bar{s})$ explicitly. Hodgson and Kerckhoff did the calculations without the extra $\bar{s}$ (page 382 of [@hk:univ]). When the $\bar{s}$ is put in, we obtain: $$\frac{b_j(\bar{s})}{\mbox{Area}(\partial V_j)}= s_j^2\,c +
\left( (\sum_k s_k x_{kj})^2 + 
   (\sum_k s_k y_{kj})^2 \right)\,a +
  s_j(\sum_k s_k x_{kj}) \,b.
\label{eqn:b_j}$$ Here the terms $a$, $b$, and $c$ are constants in terms of $R$ which agree with those on page 383 of [@hk:univ]. However, we are not immediately concerned with their values. More important, $a$ is always negative, $b$ and $c$ always positive.

From the formula ([\[eqn:b_j\]](#eqn:b_j){reference-type="ref" reference="eqn:b_j"}) we obtain the following information.

1.  $b_j(\bar{s})$ is quadratic in $\bar{s}$.

2.  If any $s_j=0$ for some $\bar{s}$, then $b_j(\bar{s})\leq 0$.

We also know that the sum of all the $b_j$'s is strictly positive, provided $\bar{s} \neq (0, 0, \dots, 0)$, by equation ([\[eqn:b_j\>0\]](#eqn:b_j>0){reference-type="ref" reference="eqn:b_j>0"}), as well as the remark right after that equation. We will use this information in §[\[subsec:Vnonempty\]](#subsec:Vnonempty){reference-type="ref" reference="subsec:Vnonempty"}.
