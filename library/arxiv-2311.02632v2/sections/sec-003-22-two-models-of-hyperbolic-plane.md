---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-003-22-two-models-of-hyperbolic-plane
section_title: "Two models of hyperbolic plane"
section_number: 2.2
pages: 5-6
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.988
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In this subsection, we review the two models of the hyperbolic plane. One such model is the upper half-plane, denoted by $\uhp$. This consists of complex numbers $z$ where the imaginary part is positive: $\uhp = \{ z \in \C : \Im(z) > 0 \}$. This model of the hyperbolic plane carries a metric: $$ds^2 = \frac{dx^2 + dy^2}{y^2},$$ which yields a constant Gaussian curvature $-1$. The distance $\distH(z,z')$ between two points $z$ and $z'$ is given by $$\cosh \distH(z,z') = 1 + \frac{|z-z'|^2}{2\Im z \Im z'}.$$ Geodesics in $\uhp$ are represented as either vertical half-lines or semicircles that intersect the $x$-axis perpendicularly. For any two distinct points in $\uhp$, there is a unique geodesic connecting them. The Laplacian is given by $$-\Delta = y^2 \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} \right).$$

The group $\PSL_2(\R)=\SL_2(\R)/\{\pm 1\}$ acts isometrically on $\uhp$. The action is given by $z \mapsto gz = \frac{az+b}{cz+d}$, where $g = \pm \pmat abcd \in\PSL_2(\R)$. A non-trivial element $g$ of $\PSL_2(\R)$ is called hyperbolic if $|\Tr(g)| > 2$. This is equivalent to $g$ fixing two distinct points on the boundary $\partial \uhp$ of the upper half-plane. The *length* $\ell(g)$ of a hyperbolic element $g$ is defined as: $$\ell(g) = 2 \arcosh\left(\frac{|\Tr(g)|}{2}\right).$$

The unit disk $\disk$ provides another model for the hyperbolic plane. It is defined by $\disk = \{ z \in \mathbb{C} : |z| < 1 \}$. In this model, the metric is expressed as: $$ds^2 = \frac{4(dx^2 + dy^2)}{(1 - x^2 - y^2)^2}$$ which results in a constant Gaussian curvature $-1$. An isometry that maps $\uhp$ onto $\disk$ is given by: $$z \mapsto \frac{z-i}{z+i},$$ which is also a conformal equivalence. The distance, denoted as $\distD(z,z')$, between two points $z$ and $z'$ in the disk is $$\cosh \distD(z,z') = 1 + \frac{2|z-w|^2}{(1-|z|^2)(1-|w|^2)}.$$ The Laplacian in this setting reads $$-\Delta = \frac{(1 - x^2 - y^2)^2}{4} \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} \right).$$ The group of orientation-preserving isometries of $\disk$ is given by the group $$\PSU(1,1) = \left\{\pm \pmat{a}{\conj{b}}{b}{\conj{a}} : a, b \in \mathbb{C},\, \abs{a}^{2}-\abs{b}^{2}=1 \right\}.$$ The notion of hyperbolic elements for $\PSU(1,1)$ and their lengths can be defined in the same way.
