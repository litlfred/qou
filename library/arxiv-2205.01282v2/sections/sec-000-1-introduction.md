---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.934
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#sec:intro label="sec:intro"}

In this paper, we study Witten--Reshetikhin--Turaev (WRT) invariants. They are quantum invariants of $3$-manifolds constructed by Witten [@Witten] from a physical viewpoint and constructed by Reshetikhin--Turaev [@Reshetikhin-Turaev Theorem 3.3.2] from a mathematical viewpoint. The Witten's asymptotic expansion conjecture plays a central role in studying WRT invariants. It claims that the Chern-Simons invariants and the Reidemeister torsions appear in the asymptotic expansion of WRT invariants. This conjecture is proved by Lawrence--Zagier [@LZ] for the Poincaré homology sphere, Hikami [@H_Bries] for Brieskorn homology spheres, Hikami [@H_Seifert] and Matsusaka--Terashima [@Matsusaka-Terashima] independently for Seifert homology spheres. Many other authors have studied this conjecture [@Andersen-Himpel; @Andersen-Mistegard; @Andersen; @Beasley-Witten; @Charles; @Chun; @Charles-Marche_II; @FIMT; @Freed-Gompf; @GMP; @H_Lattice; @H_Lattice2; @Hansen-Takata; @Jeffrey; @Rozansky1; @Rozansky2; @Wu].

Recently, Gukov--Pei--Putrov--Vafa [@GPPV] introduced $q$-series invariants called homological blocks or GPPV invariants for plumbed manifolds. They conjectured that homological blocks have good modular transformations and their radial limits yield WRT invariants. These conjectures show a roadmap to prove the Witten's asymptotic expansion conjecture. The first conjecture, modular transformations of homological blocks, are related to quantum modular forms introduced by Zagier [@Zagier_quantum]. This conjecture is proved by Matsusaka--Terashima [@Matsusaka-Terashima] for Seifert homology spheres and Bringmann--Mahlburg--Milas [@BMM_high_depth] for non-Seifert homology spheres whose surgery diagrams are the H-graphs. Bringmann--Nazaroglu [@Bringmann-Nazaroglu] and Bringmann--Kaszian--Milas--Nazaroglu [@BKMN_False_modular] clarified and proved the modular transformation formulas of false theta functions, which are main tools to study modular transformations of homological blocks.

The second conjecture, which asks the relation between WRT invariants and radial limits of homological blocks, is proved by Fuji--Iwaki--Murakami--Terashima [@FIMT] with a result in Andersen--Mistegård [@Andersen-Mistegard] for Seifert homology spheres and Mori--Murakami [@MM] for non-Seifert homology spheres whose surgery diagrams are the H-graphs. In this paper, we prove this conjecture for a large class of plumbed manifolds by developing some new techniques.

Let us explain our setting. Let $\Gamma = (V, E, (w_v)_{v \in V})$ be a plumbing graph, that is, a finite tree with the vertex set $V$, the edge set $E$, and integral weights $w_v \in \Z$ for each vertex $v \in V$. Following [@GPPV], we assume that the linking matrix $W$ of $\Gamma$ is negative definite. Then one can define the homological block $\widehat{Z}_\Gamma (q)$ with $q \in \bbC$ and $\abs{q} < 1$. Let $M(\Gamma)$ be the plumed 3-manifold obtained from $S^3$ through the surgery along the diagram defined by $\Gamma$. We also assume that $M(\Gamma)$ is an integral homology sphere. This condition is equivalent to $\det W = \pm 1$ since $H_1(M(\Gamma), \Z) \cong \Z^V / W(\Z^V)$ by use of the Mayer--Vietoris sequence. For a positive integer $k$, let $\mathop{\mathrm{WRT}}_k(M(\Gamma))$ be the WRT invariant of $M(\Gamma)$ normalised as $\mathop{\mathrm{WRT}}_k(S^3) = 1$. We also denote $\zeta_k \coloneqq e^{2\pi\iu/k}$.

In the above setting, we can state the conjecture of Gukov--Pei--Putrov--Vafa [@GPPV] by the following.

::: conj
[]{#conj:GPPV label="conj:GPPV"} $$\mathop{\mathrm{WRT}}_k(M(\Gamma))
    = \frac{1}{2(\zeta_{2k} - \zeta_{2k}^{-1})}
    \lim_{q \to \zeta_k} \widehat{Z}_\Gamma \left( q \right).$$
:::

In this paper, we prove this conjecture for a wide class of plumbing graphs.

::: thm
[]{#thm:main label="thm:main"} [\[conj:GPPV\]](#conj:GPPV){reference-type="ref" reference="conj:GPPV"} is true for plumbing graphs depicted in [1](#fig:main){reference-type="ref" reference="fig:main"}.
:::

<figure id="fig:main">

<figcaption></figcaption>
</figure>

Here we remark that a plumbing graph has the form depicted in [1](#fig:main){reference-type="ref" reference="fig:main"} if and only if $\abs{\overline{v}} + 2 - \deg(v) > 0$ for any vertex $v \in V$, where $\deg(v)$ is the degree of $v$ and $\overline{v} \coloneqq \{ i \in V \mid \{i, v \} \in E, \, \deg(i) = 1 \}$.

In a proof of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, the most difficult point is to prove the vanishing of weighted Gauss sums that appear in coefficients of negative degree in asymptotic expansions of homological blocks. The previous works [@BMM_high_depth; @MM] deal with this difficulty by direct calculations ([@BMM_high_depth Theorem 4.1],[@MM Proposition 4.2]). However, we prove it indirectly by using our asymptotic formula ([\[prop:Euler\--Maclaurin_poly\]](#prop:Euler--Maclaurin_poly){reference-type="ref" reference="prop:Euler--Maclaurin_poly"} and [\[cor:asymp_F(f; t)\]](#cor:asymp_F(f; t)){reference-type="ref" reference="cor:asymp_F(f; t)"}) and holomorphy of a rational function whose radial limits are WRT invariants. In a sense, our technique is a generalisation of the method of Lawrence--Zagier [@LZ pp.98, Proposition] using $L$-funcitons for periodic maps.

This paper will be organised as follows. In [\[sec:fund_data\]](#sec:fund_data){reference-type="ref" reference="sec:fund_data"}, we prepare some notations for plumbing graphs $\Gamma$ which we use throughout this paper. In [\[sec:WRT\]](#sec:WRT){reference-type="ref" reference="sec:WRT"}, we calculate WRT invariants for plumbed homology spheres $M(\Gamma)$. The point of our calculation is to represent WRT invariants as a sum for the submatrix of $W^{-1}$ with vertices whose degrees are greater than $2$. In [\[sec:HB_false\]](#sec:HB_false){reference-type="ref" reference="sec:HB_false"}, we express homological blocks as false theta functions. Then we can study the asymptotic expansions of homological blocks as $q \to \zeta_k$. To calculate asymptotic expansions, we develop a formula in [\[subsec:Euler\--Maclaurin\]](#subsec:Euler--Maclaurin){reference-type="ref" reference="subsec:Euler--Maclaurin"} by the Euler--Maclaurin summation formula based on Zagier [@Zagier_asymptotic Equation (44)].

In [\[subsec:asymp_Gauss\]](#subsec:asymp_Gauss){reference-type="ref" reference="subsec:asymp_Gauss"}, we develop the important asymptotic formula, which plays a central role in proving our main theorem. This formula asserts that the same factors appear in the asymptotic expansions of homological blocks and rational functions whose radial limits are WRT invariants. Finally, we prove our main theorem in [\[sec:proof_main\]](#sec:proof_main){reference-type="ref" reference="sec:proof_main"}.
