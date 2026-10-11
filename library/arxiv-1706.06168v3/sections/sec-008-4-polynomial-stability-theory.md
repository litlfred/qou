---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-008-4-polynomial-stability-theory
section_title: "Polynomial Stability Theory"
section_number: 4
pages: 11-11
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.986
---
[]{#stability_sect label="stability_sect"}

Given $\lambda \in \mathbb{N}_0^m$, a polynomial $p(x_1,y_1,\ldots,x_m,y_m) \in V(\lambda)$ is said to be *stable* if it doesn't vanish in $\mathcal{H}_+^m \subset (\mathbb{CP}^1)^m$. More generally, $p$ is said to be *$\Omega$-stable* if it doesn't vanish in $\Omega$. As above, we say $p$ is *weakly $\Omega$-stable* if possibly $p \equiv 0$. Most all results related to zero location of polynomials then can be translated into statements about stability properties of polynomials and stability preservation properties of operations applied to polynomials.

A linear operator $T$ is said to *preserve weak $\Omega$-stability* if $T(p)$ is $\Omega$-stable or identically zero for all $\Omega$-stable $p$. Further, a real linear operator $T$ *preserves weak real stability* if the same holds for real stable polynomials. In [@bb1], Borcea and Brändén were concerned with classifying such weak stability preserving operators. As seen in their main characterization results (Theorems [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} and [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"}), allowing the zero polynomial leads to a degeneracy condition in their characterization.

In order to remove this condition, we define a slightly different notion of stability: we say a linear operator $T$ *preserves (strong) $\Omega$-stability* if $T(p)$ is stable and nonzero for all stable $p$. Similarly, we say a real linear operator $T$ *preserves (strong) real stability* if the same holds for real stable polynomials. Most of the main results of this paper rely on this notion of strong stability preservation, and we will demonstrate how it relates to weak stability preservation in §[\[Cops_deriv_subsect\]](#Cops_deriv_subsect){reference-type="ref" reference="Cops_deriv_subsect"} and §[\[Rops_deriv_subsect\]](#Rops_deriv_subsect){reference-type="ref" reference="Rops_deriv_subsect"}.
