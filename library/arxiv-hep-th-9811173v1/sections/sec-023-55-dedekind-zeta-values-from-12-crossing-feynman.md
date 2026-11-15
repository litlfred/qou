---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-023-55-dedekind-zeta-values-from-12-crossing-feynman
section_title: "Dedekind zeta values from 12-crossing Feynman knots"
section_number: 5.5
pages: 21-23
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.994
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
At 12 crossings, corresponding to 8 loops in QFT, Broadhurst and Kreimer [@BK15] found that 7 of the 2,176 hyperbolic knots are positive. We found that 3 of these have rational Dedekind-zeta invariants, with $$\begin{aligned}
Z_{23,3}&=&
\df13\times{\rm vol}(\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{7})
\label{1317}\\
Z_{848,4}&=&
1\times{\rm vol}(\sigma_1^{}\sigma_2^{5}\sigma_1^{}\sigma_2^{5})
\label{1515}\\
Z_{2068,4}&=&
2\times{\rm vol}(\sigma_1^{3}\sigma_2^{3}\sigma_1^{3}\sigma_2^{3})
\label{3333}
\end{aligned}$$ The first two are those identified as Feynman knots in [@BGK; @BK15]. Again, we find it uncanny that, with odds of at least $100:1$ against, both Feynman knots proved to have single-complex-place invariant trace fields. It is clear that the Dedekind single-complex-place criterion and the Feynman positivity criterion are strongly related. The origin of this association is, however, quite unclear to us.

Most notable is the result ([\[1317\]](#1317){reference-type="ref" reference="1317"}) for the 12-crossing positive knot with braid word $\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{7}$, which is associated [@BGK] with the irreducible MZV $\zeta(9,3)$ in QFT. It has a rather small, and very special, volume: $${\rm vol}(\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{7})
={\rm vol}(5_2)
=\df{3}{10}\times{\rm vol}(9_{49})
=\df37\times{\rm vol}(7^2_2)
=3Z_{23,3}
\approx2.828122\label{12A}$$ which is precisely 3 times the volume of the closed Weeks manifold, ${\rm m}003(-3,1)$, conjectured to be the smallest of all hyperbolic manifolds. The knot $\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{7}$ is the first in the sequence of hyperbolic Feynman knots [@BK15] $F_{2n}:=\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{2n-5}$, with $2n\ge12$ crossings, associated with $\zeta(2n-3,3)$ in Feynman diagrams with $n+2\ge8$ loops.

We found that the equality of the volumes of $F_{12}$ and $5_2$ generalizes to $${\rm vol}(\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{2n-5})
={\rm vol}(\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{11-2n})\label{vt}$$ where the knot on the r.h.s. is formally obtained by $n\to8-n$ and has no more than $2n-6$ crossings. For $2n\ge12$ we also found that $${\rm vol}(F_{12})\le{\rm vol}(F_{2n})
\le{\rm vol}(9^2_{60})=\df12Z_7\approx5.333489\label{bound}$$ where $Z_7$ is the pivot of ([\[d7\]](#d7){reference-type="ref" reference="d7"}), which is the first of the non-trivial Clausen relations from 1-loop box diagrams. At large $n$, the behaviour was measured to be $${\rm vol}(F_{2n})=\df12Z_7
-\frac{C}{(\frac14n-1)^2}+O(1/n^4)
\label{limits}$$ with $C\approx0.8160$, found from 12-digit SnapPea results, with up to 500 crossings.

The asymptote suggested that the manifolds complementary to the series $F_{2n}$ of Feynman knots might be isometric to a series of Dehn fillings of a manifold with volume $\frac12Z_7$. The `drill` command of Snap suggested the manifold ${\rm s}785$, which we found to be isometric to the complement of the link $9^2_{60}$. Performing the surgeries $(-2,1)\ldots(-21,1)$ on its second cusp, we obtained 20 manifolds and asked SnapPea to compare them with the manifolds complementary to the Feynman knots $F_{2n}$, with crossing numbers from 12 to 50. The result was isometry, in all 20 cases. It was then possible to compute 64 good digits of $$C={\tt
0.8160162119959694990691941006445603982758744790599736680521553757
\ldots}\label{C}$$ from 20 high-precision Snap triangulations of ${\rm s}785(,)(4-n,1)$, with $n=O(10^3)$. It would be interesting to obtain analytical results for asymptotic changes [@NZ] in volume, such as that given by ([\[C\]](#C){reference-type="ref" reference="C"}).

Now one sees the origin of the invariance ([\[vt\]](#vt){reference-type="ref" reference="vt"}) of volumes, under the transformation $n\to8-n$. This merely flips a sign of the Dehn surgery on the torus [@Adams] curve $(4-n,1)$. The fixed point, at $n=4$, is the non-hyperbolic longitudinal surgery $(0,1)$, corresponding to the $(4,3)$ torus knot, $F_8:=(\sigma_1^{}\sigma_2^{3})^2
\sim(\sigma_1\sigma_2)^4=8_{19}$, which is the first 3-braid Feynman knot, found at 6 loops [@BKP] in QFT, where it signals the appearance of the first irreducible [@Eul; @BBB] MZV, $\zeta(5,3)$, in the counterterms of $\phi^4$-theory. At 7 loops, with $n=5$, the surgery $(-1,1)$ is likewise non-hyperbolic, corresponding to the $(5,3)$ torus knot $F_{10}:=\sigma_1^{}\sigma_2^{3}\sigma_1^{}\sigma_2^{5}
\sim(\sigma_1^{}\sigma_2^{})^5=10_{124}$, associated with $\zeta(7,3)$. Only at 12 crossings, and hence 8 loops, does this series of Feynman knots start to be hyperbolic. One thus expects to find a rather special volume at 12 crossings, as is indeed seen in ([\[12A\]](#12A){reference-type="ref" reference="12A"}).
