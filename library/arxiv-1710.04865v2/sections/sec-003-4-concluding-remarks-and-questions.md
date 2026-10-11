---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-003-4-concluding-remarks-and-questions
section_title: "Concluding remarks and questions"
section_number: 4
pages: 22-23
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.981
---
The work in this paper may be compared with that of Hikami and the first author in [@hikami1; @hikami2; @hl1], where one finds generalized Kontsevich-Zagier functions $F_t(q)$ and generalized $U$-functions $U_t(x;q)$ for torus knots $T_{(2,2t+1)}$. In the context of this family of torus knots, we have $$\label{Ft}
F_t(q) := 
  q^{t}
  \sum_{k_t \geq \dots \geq k_1 \geq 0}^\infty
  (q)_{k_t} \, 
  \prod_{i=1}^{t-1} q^{k_i(k_i+1)} 
  \begin{bmatrix}
    k_{i+1} \\
    k_i
  \end{bmatrix}$$ and $$\label{Ut}
U_t(x;q) :=
  q^{-t}
  \sum_{k_t  \geq \cdots \geq k_1 \geq 1}
  (-xq)_{k_t-1}(-x^{-1}q)_{k_t-1} \,
  q^{k_t}\prod_{i=1}^{t-1} q^{k_i^2}
  \begin{bmatrix}
    k_{i+1} + k_i - i   + 2\sum_{j=1}^{i-1}k_j \\
    k_{i+1} - k_i
  \end{bmatrix}.$$ (Note that $F_1(q) = F_{1,1}(q)$ and $U_1(x;q) = U_{1,1}(x;q)$ since the underlying knot in each case is the trefoil). While both the torus knot and double twist knot families of functions satisfy the duality in Theorem [\[fugeneralthm\]](#fugeneralthm){reference-type="ref" reference="fugeneralthm"}, much more is known in the case of torus knots. For example, the functions $F_t(q)$ have explicit quantum modular properties which were given by Hikami [@hikami2]. For the case of torus knots $T_{(3, 2^t)}$, see Corollary 4.1 in [@go]. As for ([\[Ut\]](#Ut){reference-type="ref" reference="Ut"}), it can be written in terms of indefinite ternary theta series [@hl1]. It is natural to ask whether the $F_{m,p}(q)$ (and/or $\mathcal{F}_{m,p}(q)$) have quantum modularity or other related properties (e.g., asymptotic expansions near roots of unity), and whether the $U_{m,p}(x;q)$ (and/or the $\mathcal{U}_{m,p}(x;q)$) have any nice representation in terms of indefinite theta series.

We close with two further questions. First, for torus knots $T_{(2, 2t+1)}$, the $q$-hypergeometric series expressions for $J_N(T_{(2,2t+1)};q)$ which led to the generalized Kontsevich-Zagier functions $F_t(q)$ were computed in [@hikami1; @hikami2] using difference equations. Can one prove Theorems [\[main1\]](#main1){reference-type="ref" reference="main1"} and [\[main2\]](#main2){reference-type="ref" reference="main2"} using this technique? Second, both $U_{1,1}(x; q)$ and $F_{1,1}(q)$ are interesting combinatorial generating functions and the coefficients of $F_{1,1}(1-q)$ and $U_{1,1}(1; q)$ satisfy intriguing congruences [@ak; @as; @bopr; @garvan; @gkr; @straub]. It would be worthwhile to determine if the same is true for $U_{m,p}(x; q)$ and $F_{m,p}(q)$.
