---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-004-example-trefoil-knot
section_title: "Example – trefoil knot"
section_number: null
pages: 4-5
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.99
doc_brief: "BPS states, knots and quivers — 7 sections: Front matter; BPS states, knots and quivers; Knot invariants, knot homologies"
---
We illustrate the above correspondence in the example of trefoil knot, whose reduced colored HOMFLY-PT polynomials arise by setting $t=-1$ in ([\[Pr-31\]](#Pr-31){reference-type="ref" reference="Pr-31"}). Using the $q$-binomial identity $(z;q)_k=\sum_i {k \brack i} (-z)^i q^{\frac{i(i-1)}{2}}$, the $q$-binomial and the last product in ([\[Pr-31\]](#Pr-31){reference-type="ref" reference="Pr-31"}) take form $${r \brack k} \big(\frac{a^2}{q^2};q^2\big)_k = \sum_{i=0}^k \frac{(q^2;q^2)_r  \big( - \frac{a^2}{q^2} \big)^i q^{i(i-1)} }{(q^2;q^2)_{r-k} (q^2;q^2)_i (q^2;q^2)_{k-i}}.$$ Introducing $r=d_1+d_2+d_3, k=d_2+d_3, i=d_3$ with $d_i\geq 0$, and normalizing $P_r(a,q)$ by $(q^2;q^2)_r$, the generating function ([\[Pz2\]](#Pz2){reference-type="ref" reference="Pz2"}) can be rewritten as in ([\[PxC\]](#PxC){reference-type="ref" reference="PxC"}) $$\begin{aligned}
&P(x) = \sum_{r=0}^{\infty} \frac{P_r(a,q)}{(q^2;q^2)_r} x^r = \nonumber \\
&\sum_{d_1,d_2,d_3\geq 0} \frac{q^{\sum_{i,j} C_{i,j} d_i d_j  -2d_1-3d_3} (-1)^{d_3} a^{2d_1+2d_2+4d_3} x^{\sum_i d_i}  }{(q^2;q^2)_{d_1} (q^2;q^2)_{d_2} (q^2;q^2)_{d_3}}   \label{PxC-31}
\end{aligned}$$ with $C = 
\left[
\begin{tabular}{ccc}
0 & 1 & 1 \\
1 & 2 & 2 \\
1 & 2 & 3 \\
\end{tabular}
\right]$. The corresponding quiver is shown in fig. [\[fig-trefoil\]](#fig-trefoil){reference-type="ref" reference="fig-trefoil"} and, as we claimed above, its vertices correspond to generators of HOMFLY-PT homology. Furthermore, diagonal elements $(0,2,3)$ of matrix $C$ (representing numbers of loops at vertices of the quiver) indeed agree with homological degrees encoded in the uncolored superpolynomial ([\[P1-31\]](#P1-31){reference-type="ref" reference="P1-31"}), coefficients $l_i=-2,0,3$ of linear terms in $d_i$ in the power of $q$ in ([\[PxC-31\]](#PxC-31){reference-type="ref" reference="PxC-31"}) are given by $l_i=q_i-t_i$, coefficients $a_i=2,2,4$ in the power of $a$ agree with $a$-degrees of generators of HOMFLY-PT homology, and additional minus sign $(-1)^{d_3}$ is determined by just one generator with odd $t$-degree $t_3=3$.

We stress that rewriting of the generating function of colored HOMFLY-PT polynomials in the form ([\[PxC-31\]](#PxC-31){reference-type="ref" reference="PxC-31"}) guarantees that it can be written in the product form ([\[PQx-Omega\]](#PQx-Omega){reference-type="ref" reference="PQx-Omega"}), so that LMOV invariants are expressed as combinations (with integer coefficients) of integer motivic Donaldson-Thomas invariants $\Omega_{d_1,d_2,d_3;j}$. This proves the LMOV conjecture for $3_1$ knot, for all symmetric representations.

Analogous calculations can be performed for other knots, e.g. rewriting formulas for colored superpolynomials in [@FGSS]. A general formalism facilitating such computations and their consequences is presented in [@KRSS2].
