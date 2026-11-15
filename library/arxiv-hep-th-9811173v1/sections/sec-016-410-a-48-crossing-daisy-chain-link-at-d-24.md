---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-016-410-a-48-crossing-daisy-chain-link-at-d-24
section_title: "A 48-crossing daisy-chain link at $D=-24$"
section_number: 4.10
pages: 12-13
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
The attentive reader will now expect us to skip the case $D=-23$ and jump to the 8th underlining in ([\[iq\]](#iq){reference-type="ref" reference="iq"}), at $D=-24$. This is precisely what we did, though the character of the result was not what we first supposed. It seemed to us that the hallmark of past success, in finding links that link Clausen values, was to achieve the largest possible symmetry group. What, we asked ourselves, could pack a better symmetry-to-crossing ratio than the remaining 4 platonic alternating links?

Let us denote the tetrahedral link of Fig. 1 by $T:=24^{10}_{\rm tet}$. The 4 non-self-dual alternating platonic links have components that mimic the vertices and edges of the cube $C:=48^{20}_{\rm cub}$, octahedron $O:=48^{18}_{\rm oct}$, dodecahedron $D:=120^{50}_{\rm dod}$, and icosahedron $I:=120^{42}_{\rm ico}$, where, for example, the last has 120 alternating crossings of its 42-components, which mimic the 12 vertices and 30 edges of the perfect solid with 20 faces. These links are highly symmetrical, yet none of their 4 volumes yielded the sought-for rational relation to a quadratic Dedekind zeta value. Later, we show that they are quartic links.

Instead, we found an answer to our 8th question by a more child-like construction: a non-alternating daisy chain. By a daisy chain we mean a link each of whose components has 2 crossings with a neighbour on one side, and 2 crossings with a neighbour on the other, with the whole forming a circle, as in Fig. 2. By a non-alternating daisy chain, we mean one in which the 4 crossings of each component occur in an order over-over-under-under, while still linking with neighbours. A little doodling should convince the reader that non-alternating daisy-chain links must have an even number of components.

A delightful feature of Jeff Weeks' program SnapPea [@SnapPea] is that it enables one to draw such chains quickly, and then ask whether the resultant non-alternating link has quadratic shapes in its triangulation. Using A.C. Manoharan's port of SnapPea to Windows95[^1], we inferred, from instances with up to 96 crossings, that the non-alternating daisy-chain link with $2n\ge6$ components, and hence $4n\ge12$ crossings, has hyperbolic volume $$V_{2n}=8nD\left(i\tan\frac{(n-2)\pi}{4n}\right)\label{daisy}$$ The first 4 hyperbolic non-alternating daisy chains yield results with $-D\in\{3,4,8,20\}$: $$\begin{aligned}
V_6&=&4Z_4\label{dc6}\\
V_8&=&2Z_8\label{dc8}\\
V_{10}&=&\df12Z_{20}+V_6\label{dc10}\\
V_{12}&=&20Z_3\label{dc12}
\end{aligned}$$ Then nothing interesting happens until we reach 24 components, with 48 crossings, where $$V_{24}=Z_{24}+V_{8}\label{dc24}$$ hits the target, at $D=-24$.

SnapPea illustrates this nicely. Drawing daisy chains with 6, 8, 10, 12, 24 components, and inspecting the triangulations, one detects the square roots of 1, 2, 5, 3, 6. The last, illustrated in Fig. 2, delivers a result for $Z_{24}=V_{24}-V_{8}$, namely $$60{\rm Cl}_2(\theta_{3,2})-18{\rm Cl}_2(2\theta_{3,2})
-4{\rm Cl}_2(3\theta_{3,2})+3{\rm Cl}_2(4\theta_{3,2})=Z_{24}
=24\sum_{k\in\{1,5,7,11\}}{\rm Cl}_2\left(\frac{2\pi k}{24}\right)
\label{d24}$$ with $\theta_{3,2}:=2\arctan\sqrt{3/2}$. So, for the 6th time, we have a relation that is as easy to check numerically as it appears hard to derive.

[^1]: ` http://home.att.net/`$\,\widetilde{}\,$`Manoharan/SnapPea/snappea.html`
