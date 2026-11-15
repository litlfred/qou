---
doc_id: arxiv-math-0603444v2
doc_title: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY"
section_id: sec-001-2-relation-to-the-logarithmic-comparison-theorem
section_title: "Relation to the logarithmic comparison theorem"
section_number: 2
pages: 2-2
source_pdf: 0603444v2.pdf
source_sha256: 46edfcddca963d08
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.979
doc_brief: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY — We characterize quasihomogeneity of isolated hypersurface singu- larities by the injectivity of the map induced by"
---
The map $d_1$ is well-known in the context of the logarithmic comparison theorem: By Grothendieck's comparison theorem [@Gro66], the cohomology of the complement $U=\mathbb{C}^n\smallsetminus D$ of a germ of a reduced divisor $D\subseteq\mathbb{C}^n$ is computed by the complex $\Omega^\bullet(\star D)$. If the inclusion $\Omega^\bullet(\log D)\subseteq\Omega^\bullet(\star D)$ is a quasi--isomorphism then $\Omega^\bullet(\log D)$ computes the cohomology of $U$ and one says that the logarithmic comparison theorem, or briefly LCT, holds for $D$. The characterization of LCT is an open problem and the subject of active current research [@Tor05]. Mainly the two extremal cases of isolated singularities and free divisors have been studied. By definition, $D$ is free if $\mathop{\mathrm{Der}}(-\log D)$ is $\mathcal{O}$-free of rank necessarily equal to $n$. Freeness of $D$ means that it is either smooth or its singular locus $\mathop{\mathrm{Sing}}(D)$ is of pure codimension $1$ in $D$. Thus the two cases coincide for singularities in dimension $n=2$ and are disjoint if $n\ge3$.

By [@CNM96; @CMNC02 Sect. 2], the map $d_1$ occurs as the differential $d_1^{0,n-1}$ in the $1$-page $$E_1^{p,q}=H^q(\mathbb{C}^n\smallsetminus\{0\},\Omega^p(\log D))$$ of a spectral sequence $E$ which converges to the cohomology of $U$ under the assumption that LCT holds for $D\smallsetminus\{0\}\subseteq\mathbb{C}^n\smallsetminus\{0\}$. In particular, this assumption is fulfilled in the case of isolated singularities. Since sections of $\Omega^\bullet(\log D)$ defined outside $\mathop{\mathrm{Sing}}(D)$ extend uniquely to $\mathbb{C}^n$, the $q=0$ row of $E_1$ equals $\Omega^\bullet(\log D)$. Thus, if LCT holds also at the origin, the spectral sequence $\bar E$ with $1$-page $\bar E_1$ obtained from $E_1$ by removing the $q=0$ row converges to zero.

In the case of a free divisor $D$, $\Omega^\bullet(\log D)$ consists of free $\mathcal{O}$-modules and hence $E_1^{p,q}=0$ for $q\ne0,n-1$. This implies that the injectivity of $d_1$ is a necessary condition for LCT [@CMNC02 Sect. 3]. In dimension $n=2$, injectivity of $d_1$ is even equivalent to LCT and to quasihomogeneity [@CMNC02 Thm. 3.5].

If $f\in\mathfrak{m}_xJ_f$ at any point $x\in D$ for a reduced defining equation $f\in\mathfrak{m}$ of $D$ then $D$ is called strongly Euler homogeneous. In the case of free divisors, the main conjecture on LCT states that LCT implies strong Euler homogeneity [@CMNC02 Conj. 1.4]. We have proved this conjecture in dimension $n=3$ [@GS06].

For isolated singularities, strong Euler homogeneity reduces to quasihomogeneity by [@Sai71]. M. Holland and D. Mond [@HM98] have given an explicit characterization of LCT for quasihomogeneous isolated singularities $D$: Let $f\in\mathfrak{m}^2$ be a reduced defining equation of $D$ which is quasihomogeneous with respect to the necessarily strictly positive weights $w_1,\dots,w_n\in\mathbb{Q}$. Then LCT holds for $D$ if and only if $$(\mathcal{O}/\langle f_1,\dots,f_n\rangle)_{k-\sum_{i=1}^nw_i}=0\text{ for }k=1,\dots,n-2.$$ In particular, quasihomogeneity does not imply LCT for isolated singularities. On the other hand, we do not know a counter--example to the opposite implication. Our result possibly reduces the complete characterization of LCT for isolated singularities to the statement: LCT implies injectivity of $d_1$ for isolated singularities. But it is not clear if the injectivity of $d_1$ contradicts to $\bar E$ converging to zero.
