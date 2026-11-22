---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-017-411-quartic-platonic-links
section_title: "Quartic platonic links"
section_number: 4.11
pages: 13-15
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
Our first guess, that the 4 non-self-dual platonic links might yield quadratic number fields, failed. Nonetheless, it is interesting to determine their number fields, and hence obtain accurate volumes. This is clearly a taxing job. To prepare for it, we first tackled a problem of similar complexity, where an accurate answer could be inferred.

We found that by adding $n$ concentric components at each of the 4 "vertices" of Fig. 1, one obtains a volume $Z_{20}+2nZ_{15}$ for the link with $24+24n$ crossings and $10+4n$ components, when $n\le5$. At $n=6$, SnapPea was given the 34-component link with 168 crossings, which was triangulated to give 632 ideal tetrahedra, each having a volume $D(z_k)$ with $z_k\in\mbox{\bf Q}(\sqrt{-5})$ or $z_k\in\mbox{\bf Q}(\sqrt{-15})$. We output the 632 shapes, and computed, at 1800-digit precision, the $3\times632=1,896$ Clausen values entailed by $$\begin{aligned}
D(z)&=&V(\arg(z),-\arg(1-z))\label{arg}\\
V(\theta_1,\theta_2)&:=&\df12\left\{{\rm Cl}_2(2\theta_1)
+{\rm Cl}_2(2\theta_2)
-{\rm Cl}_2(2\theta_1+2\theta_2)\right\}
\label{3cl}
\end{aligned}$$ obtaining 1800-digit agreement with the expectation $Z_{20}+12Z_{15}=502.408032\ldots$ for the volume. This gave us confidence that we could process the 950 ideal tetrahedra entailed by the remaining 4 platonic links.

We obtained from SnapPea the low-precision volumes $$\begin{aligned}
{\rm vol}(C)\approx{\rm vol}(O)&\approx&{\tt 114.537611}\label{CO}\\
{\rm vol}(D)\approx{\rm vol}(I)&\approx&{\tt 310.913145}\label{DI}
\end{aligned}$$ from $128+130+346+346=950$ ideal tetrahedra.

The duality between cube and octahedron, and between dodecahedron and icosahedron, is gratifying. Such duality is not restricted to platonic links. More generally, suppose that we have a link, $L$, with an alternating projection in which the components may be separated into two classes: vertex (V) components and edge (E) components, with pairs of crossings only between V and E components, and every E connecting a pair of V's. Thus the crossing number is 4 times the number of E components. Now shrink the V components to true vertices (some of which may be divalent) and the E components to true edges that connect these points, to obtain a planar graph, $P$. Then construct the dual graph, $P^*$, whose vertices lie in the regions of the plane partitioned by the edges of $P$ and whose edges thus cross the edges of $P$. Now thicken $P^*$ to obtain the alternating link $L^*$ dual to $L$. The crossing numbers of $L$ and $L^*$ are equal, but the numbers of components need not be. For example $C:=48^{20}_{\rm cub}$ has more components than $C^*:=O:=48^{18}_{\rm oct}$, and $D:=120^{50}_{\rm dod}$ has more than $D^*:=I:=120^{42}_{\rm ico}$. On the basis of these and further tests, we conjecture that ${\rm vol}(L)={\rm vol}(L^*)$, for every shrinkable link $L$.

To identify the number fields of the $\{C,O\}$ and $\{D,I\}$ pairs, we first examined the cusp shapes, and found that $$K_C:=\mbox{\bf Q}\left(\sqrt{8\sqrt{2}-15}\right)\label{FC}$$ gave a simple fit to the cusp shapes of $\{C,O\}$, at the 12-digit precision provided by SnapPea, while $$K_D:=\mbox{\bf Q}\left(\sqrt{-12\sqrt{5}-31}\right)\label{FD}$$ similarly fitted the cusp shapes of $\{D,I\}$.

We then output $z$-values of the triangulations. Fitting these was not easy, since the data now consisted of numerical values, to 12 decimal places, of $1,900$ real or imaginary parts, each of which was supposed to be fittable by two powers of $\sqrt{15-8\sqrt{2}}$, in the cubical and octahedral cases, or $\sqrt{31+12\sqrt{5}}$, in the dodecahedral and icosahedral cases. In each of the $1,900$ cases we required a significant integer relation between 3 numbers: the 12-digit SnapPea datum and the two powers, namely 0 and 2 for a real part, or 1 and 3 for an imaginary part. Whether this can be done by a reliable and uniformly automated method depends upon the largest integer. If it has more than 4 digits, the matter is moot, since fitting 12-digit data with 3 integers with up to 4 digits is already a parlous business. In fact our first attempt yielded garbage in a significant fraction of the $1,900$ cases.

Fortunately, 3 features of the mathematics enable us to crack this tough nut. First, the 6-fold symmetry of the Bloch--Wigner function $$D(z)=D(1/(1-z))=D(1-1/z)=D(1/\overline{z})
=D(1-\overline{z})=D(\overline{z}/(\overline{z}-1))
\label{6fold}$$ gave us 6 bites at each cherry. Secondly, number theory suggested that we might do well to make the Ansatz $$z=\frac{1}{I_z}\sum_{p=0}^3 I_p u^p\label{ansatz}$$ with $6\times950\times5=28,500$ integers relating 6 equivalent $z$ values of 950 ideal volumes to 4 powers of $u=\frac12(1+i\sqrt{15-8\sqrt{2}})$ or $u=\frac12(1+i\sqrt{31+12\sqrt{5}})$. Finally, we were prepared for even the simplest of the 6 fits to any shape to contain the prime factor $97=15^2-2\times8^2$ of the cubical/octahedral discriminant, or $241=31^2-5\times12^2$ in the dodecahedral/icosahedral case.

These 3 features allowed us to devise a diversity of algorithms that yielded, eventually, total fits which we consider to be corporately indubitable. Our confidence came from a fourth mathematical feature, which at first sight appeared to make life difficult, namely that there was virtually no overlap between problems that were supposed to be related by duality. In fact we found only two distinct ideal volumes that contributed to both the dodecahedron and icosahedron, and each of these was unambiguous. The absence of further overlap doubled the computational load, yet made the resulting numerical agreement of volumes, to 1800 digits, a potent signal of success. It seems unlikely that a misidentification of one of the ideal volumes, for the dodecahedron, could produce the same effect as a misidentification of a quite different ideal volume, for the icosahedron.

Thus we believe that we have found exact (and also very lengthy) expressions of the form $\sum_{k=1}^{n}D(z_k)$, with $n=128$ and $z_k\in\mbox{\bf Q}(\sqrt{8\sqrt{2}-15})$, for the cubical/octahedral volume of Table 20, and with $n=346$ and $z_k\in\mbox{\bf Q}(\sqrt{-12\sqrt{5}-31})$, for the dodecahedral/icosahedral volume of Table 21. Thanks to David Bailey's evaluations of $\zeta(2n)$, described in Section 4.2, we were able to obtain $1,800$ good digits of $2,850$ Clausen values in less than 2 hours.
