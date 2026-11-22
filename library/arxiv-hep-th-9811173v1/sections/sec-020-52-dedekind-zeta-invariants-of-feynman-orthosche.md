---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-020-52-dedekind-zeta-invariants-of-feynman-orthosche
section_title: "Dedekind-zeta invariants of Feynman orthoschemes"
section_number: 5.2
pages: 16-18
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.854
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
Let us try to disentangle this remarkable circumstance from its physical origin. What is the common characteristic of the Davydychev--Delbourgo (DD) hyperbolic tetrahedron at those values of the physical quantities which gave the volumes of links?

In terms of ([\[3cl\]](#3cl){reference-type="ref" reference="3cl"}), we define the 3-argument dilogarithm $$\begin{aligned}
S(\psi_1,\psi_2,\psi_3)
&:=&V(\delta+\psi_1,\delta-\psi_1)+V(\delta+\psi_3,\delta-\psi_3)\nonumber\\
&+&V(\df12\pi+\psi_2-\delta,\df12\pi-\psi_2-\delta)
+V(\df12\pi-\delta,\df12\pi-\delta)\label{Schl}
\end{aligned}$$ with an auxiliary angle $\delta\in[0,\pi/2]$ satisfying [@DD] $$\tan^2\delta
=\frac{\cos^2\psi_2}{\cos^2\psi_1\cos^2\psi_3}
-\tan^2\psi_1\tan^2\psi_3\label{delta}$$ Then the Schläfli/Lobachevsky [@Lob; @Schl; @Coxeter; @Vinberg] function ([\[Schl\]](#Schl){reference-type="ref" reference="Schl"}) is 4 times the volume of a bi-rectangular hyperbolic tetrahedron, with essential dihedral angles $\psi_1,\psi_2,\psi_3$. The edges with angles $\psi_1$ and $\psi_3$ are opposite, while that with $\psi_2$ is adjacent to each. The remaining 3 dihedral angles are right angles. With 3 essential angles, a bi-rectangular tetrahedron is an example of an orthoscheme [@AMS:RK]. With a common internal mass, and a common external mass, the DD tetrahedron comprises 4 identical orthoschemes, with ([\[Schl\]](#Schl){reference-type="ref" reference="Schl"}) giving its volume.

The next step was to calculate the essential angles $\psi_k$ that had given a rational relation to the volume of a link. In all cases we found that $\psi_k\in\{0,\pi/6,\pi/4,\pi/3\}$. The final step was clear: to compute all such instances of ([\[Schl\]](#Schl){reference-type="ref" reference="Schl"}), in the hope of finding more Feynman orthoschemes that are rationally related to Dedekind zeta values. Taking account of the positivity of ([\[delta\]](#delta){reference-type="ref" reference="delta"}), and the symmetry $S(\psi_1,\psi_2,\psi_3)=S(\psi_3,\psi_2,\psi_1)$, there are 36 possibilities to consider, of which the physics in [@9806174] had already shown 5 to be fruitful. We had a lively expectation of further rational relations to $Z_{|D|}$. We were thus totally delighted by the following, totally rational, finding.

> All real instances of ([\[Schl\]](#Schl){reference-type="ref" reference="Schl"}) with $\psi_k\in\{0,\pi/6,\pi/4,\pi/3\}$ are rational multiples of $Z_{|D|}$ with $|D|\in\{3,4,7,8,11,15,20,24,39,84\}$. Table 22 gives the 36 empirical relations. All the relations are realized by Feynman diagrams; in the cases with $\psi_2\ne0$, one has merely to give the external particles a suitable common mass.

It was trivial to decide which value of $Z_{|D|}$ to try in each of the 36 cases: one has only to examine the square root of ([\[delta\]](#delta){reference-type="ref" reference="delta"}) to determine $D$. Had we been less result-oriented we might have taken time out to recast[^1] each of the 36 searches in terms of 4 complex arguments of Bloch--Wigner dilogarithms for the 4 ideal parts of ([\[Schl\]](#Schl){reference-type="ref" reference="Schl"}), and then used algebra [@AMS:SB; @AMS:DZ] to determine, in advance, whether a rational (but unspecified!) number would result from dividing the volume by $Z_{|D|}$. We were content with the faster process of division, which gives the concrete result. Throughout this work, the issue is not the existence of rationals, but their values. The rational numbers of Table 22 in the cases with $-D\ge7$ are at least as hard to derive as those in ([\[d7\]](#d7){reference-type="ref" reference="d7"}--[\[d20\]](#d20){reference-type="ref" reference="d20"},[\[d24\]](#d24){reference-type="ref" reference="d24"}). For $D=-39$, we found that $$24{\rm Cl}_2(\theta_{13,3})-15{\rm Cl}_2(2\theta_{13,3})
+{\rm Cl}_2(6\theta_{13,3})
=\df16Z_{39}\label{d39}$$ with $\theta_{13,3}:=2\arctan\sqrt{13/3}$. For $D=-84$, we found that $$60{\rm Cl}_2(\theta_{7,3})-36{\rm Cl}_2(2\theta_{7,3})
-4{\rm Cl}_2(3\theta_{7,3})+3{\rm Cl}_2(4\theta_{7,3})
+2{\rm Cl}_2(6\theta_{7,3})=\df16Z_{84}\label{d84}$$ with $\theta_{7,3}:=2\arctan\sqrt{7/3}$. These are our 7th and 8th unprovens, courtesy of Feynman.

[^1]: There is nothing complex, or ideal, in the physical problem that led to our discoveries: integration over real Feynman parameters yields the volume of a tetrahedron, none of whose vertices are at infinity.
