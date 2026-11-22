---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-001-11-the-wrt-invariant-for-integral-homology-spher
section_title: "The WRT invariant for integral homology spheres"
section_number: 1.1
pages: 1-2
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.904
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:witt-resh-tura-1 label="sec:witt-resh-tura-1"}

Witten [@Witten] introduced the notion of Chern-Simons path integral which gives a quantum field theory interpretation of the Jones polynomial [@Jones1; @Jones2] and predicts the existence of $3$-manifold invariants. Using the quantum group $U_q(sl_2)$ at roots of unity, Reshetikhin and Turaev [@Reshetikhin-Turaev:invariants] gave a rigorous construction of $3$-manifold invariants, which are believed to coincide with the Chern-Simons path integrals. These invariants are called the Witten-Reshetikhin-Turaev (WRT) invariants.

In the present paper, we focus on the WRT invariant for integral homology spheres, i.e., closed $3$-manifolds $M$ with trivial first homology groups. If we fix such $M$, the WRT invariant $\tau _\zeta (M)\in \C$ is defined for each root of unity $\zeta$. (Unlike the case of general closed $3$-manifolds, one does not have to specify a fourth root of $\zeta$.) For an integer $r\ge 1$, $\tau _{\zeta _r}(M)$ for $\zeta _r=\exp\frac{2\pi \sqrt{-1}}{r}$ is also denoted by $\tau _r(M)$. In the literature, usually $\tau _1(M)$ is not defined, but for our purpose it is convenient to defined it as $1$. For integral homology spheres, the version $\tau '_r(M)$ introduced by Kirby and Melvin [@Kirby-Melvin] defined for odd $r\ge 3$ is equal to $\tau _r(M)$.

Let $\calZ\subset \C$ denote the set of all roots of unity. Define the *WRT function* of $M$ $$\tau (M)\zzzcolon \calZ\rightarrow \C,$$ by $\tau (M)(\zeta )=\tau _\zeta (M)$. The behavior of the function $\tau (M)$ is of interest here.

For $\tau _\zeta (M)$ with $\zeta$ roots of unity of *odd prime (power) orders*, there have been more extensive studies than for the other cases. Murakami [@Murakami1] proved that if $\zeta \in \calZ$ is of odd prime order, then $\tau _\zeta (M)\in \modZ [\zeta ]$, hence it is an algebraic integer. Ohtsuki [@Ohtsuki1] extracted from the $\tau _\zeta (M)$ for $\zeta$ of odd prime orders a power series invariant, known as the *Ohtsuki series* of $M$ $$\tau ^O(M)=1+\sum_{n=1}^\infty \lambda _n(M)(q-1)^n\in \modQ [[q-1]].$$ Lawrence [@Lawrence:integrality] conjectured, and Rozansky [@Rozansky] later proved, that $\tau ^O(M)\in \modZ [[q-1]]$ and that, for each $\zeta \in \calZ$ of odd prime power order $p^e$, $\tau ^O(M)|_{q=\zeta }$ converges $p$-adically to $\tau _\zeta (M)$. In this sense, the Ohtsuki series *unifies* the WRT invariants at roots of unity of odd prime power orders. (For generalizations of the above-mentioned results to rational homology spheres and to invariants associated to other Lie groups, see [@Le1; @Le2; @Masbaum-Roberts; @Masbaum-Wenzl; @Murakami2; @Ohtsuki2; @Takata-Yokota].)

The proofs of the above-mentioned results depends heavily on the fact that if $\zeta \in \calZ$ is of prime power order, then $\zeta -1$ is not a unit in the ring $\modZ [\zeta ]$. Otherwise, $\zeta -1$ is a unit in $\modZ [\zeta ]$, and expansions in powers of $\zeta -1$ do not work.
