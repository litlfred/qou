---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-009-26-the-3-loop-invariant
section_title: "The 3-loop invariant"
section_number: 2.6
pages: 11-11
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 1.0
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.3loop label="sub.3loop"}

For the next invariant $S_{\gamma,3,k}$, all the diagrams of Figure [\[fig.diags2intro\]](#fig.diags2intro){reference-type="ref" reference="fig.diags2intro"} contribute, collecting the coefficient of $\hbar^2$ of their evaluation. In addition, there are $34$ new diagrams that satisfy the inequality [\[eq.LD\]](#eq.LD){reference-type="eqref" reference="eq.LD"}; they are shown in Figures [\[fig.diags3\]](#fig.diags3){reference-type="ref" reference="fig.diags3"} and [\[fig.diags3dot\]](#fig.diags3dot){reference-type="ref" reference="fig.diags3dot"}. Calculations indicate that the 3-loop invariant $S_{\gamma,3,k}$ is well defined, and invariant under 2-3 moves. The invariants $\tau_{\gamma,k}, S_{\gamma,2,k}, S_{\gamma,3,k}$ have been programmed in `Mathematica` as well as in `python` and take as input a Neumann-Zagier datum readily available from `SnapPy` [@snappy].

The number of diagrams that contribute to the $n$-loop invariant is given in Table [1](#tab.diagrams){reference-type="ref" reference="tab.diagrams"}.

For large $n$, we expect that $n!^2 C^n$ diagrams contribute to the $n$-loop invariant. It would be nice to find a more efficient computation.

::: center
::: {#tab.diagrams}
  $n$     $2$   $3$    $4$     $5$      $6$
  ------- ----- ------ ------- -------- ---------
  $g_n$   $6$   $40$   $331$   $3700$   $53758$

  : The number $g_n$ of graphs that contribute to the $n$-loop invariant for $n=2,\dots,6$.
:::
:::
