---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-000-1-introduction
section_title: "introduction"
section_number: 1
pages: 1-2
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
toc_source: outline
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.984
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained from recur- rences for the summand in Masbaum’s formula of the"
---
The colored Jones polynomial is a one variable polynomial invariant of a knot colored with irreducible finite dimensional representation of $sl(2,\mathbb{C})$ [@Turaev:INVEM88]. The original Jones polynomial [@Jones:link_polynomials] corresponds to the colored Jones polynomial of a knot colored with the irreducible 2-dimensional representation. On the other hand, in [@Cooper/Culler/Gillet/Long/Shalen:INVEM94], D.Cooper, M.Culler, H.Gillet, D.D.Long, and P.R.Shalen introduced a two variable polynomial invariant $A_K(l,m)$ of a knot $K$, called the $A$-polynomial, by using the representations of the fundamental group of the complement of the knot into $SL_2(\mathbb{C})$. In this paper, we prove that for a twist knot, the $A$-polynomial can be obtained from the colored Jones polynomial.

Recently, C.Frohman, R.Gelca, W.Lofaro [@Frohman/Gelca/Lofaro:TAMS01] introduced the peripheral ideal of a knot, and the noncommutative $A$-ideal of a knot as a generalization of the $A$-polynomial, via Kauffman bracket skein theory. A nontrivial element in the peripheral ideal of a knot induces a recursive relation of the Kauffman bracket polynomial of the knot, which essentially equals to the colored Jones polynomial of the knot. It is not yet proved that for a knot except for the $(2,2p+1)$-torus knot and the figure eight knot, the peripheral ideal is nontrivial.

Afterwards, in [@Garoufalidis/Le:math.GT], S.Garoufalidis and T.T.Q.Le proved that the colored Jones polynomial of a knot satisfies a nontrivial recursive relation. Moreover, in [@Garoufalidis:math.GT], Garoufalidis defined the recursion ideal, which is identified with the set of recursive relations of the colored Jones polynomial, and defined the noncommutative $A$-polynomial $A_q(K)$ of a knot $K$ called $A_q$-*polynomial*, as a generator of the ideal. Let us denote by $J_K(n)$ the $n$-colored Jones polynomial associated with irreducible $n$-dimensional representation of $sl(2,\mathbb{C})$. We consider two operators $E$ and $Q$ acting on $J_K(n)$ by $EJ_K(n)=J_K(n+1)$ and $QJ_K(n)=q^nJ_K(n)$. The element $A_q(K)$ is of the form $A_q(K)(E,Q)=\sum_k a_k E^k$ with $a_k$ in $\mathbb{Z}[q,Q]$. Then, Garoufalidis conjectured

::: conj
For every knot $K$ in $S^3$, $A_K(l,m)=\varepsilon A_q(K)(l,m^2)$ , where $\varepsilon$ is the evaluation map at $q=1$.
:::

Furthermore, he showed that the conjecture holds for the trefoil knot and the figure eight knot, by using the mathematica package `qZeil.m` develped by Paul and Riese [@Paule/Riese:FIC97] [@Paule/Riese:qZeil], to find a recursive relation of the colored Jones polynomial.

We focus on twist knots, for which we have the formula of the colored Jones polynomial obtained by G.Masbaum in [@Masbaum:AGT03] and the formula of the $A$-polynomial obtained by J.Hoste and P.D.Shanahan in [@Hoste/Shanahan:JK]. The purpose of this paper is to prove that for a twist knot, the $A$-polynomial can be obtained from recursive relations of the summand in Masbaum's formula of the colored Jones polynomial. Our result supports the AJ conjecture for a twist knot. Moreover, using the mathematica package `qMultisum.m` developed by Reise [@Riese:JSC03], we observe that the $A$-polynomial for the knots $5_2$ and $6_1$ can be obtained from a recursive relation of the colored Jones polynomial. We will also discuss a relation between our result and 'Volume conjecture' due to R.M.Kashaev, H. Murakami and J. Murakami ([@Kashaev:LETMP97],[@Murakami/Murakami:volume]).

This paper is organized as follows. In Section 2, we recall Masbaum's formula of the colored Jones polynomial for a twist knot and state Main theorem (Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}). In Section 3, we prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. In Section 4, we relate our result to the AJ conjecture and give a result about recursive relations of the Jones polynomials for the knots $5_2$ and $6_1$.

The author would like to thank Y. Yokota for helpful conversation.
