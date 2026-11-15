---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-011-36-wξ-modules
section_title: "Wξ-modules"
section_number: 3.6
pages: 11-12
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.844
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:cyclic-reps label="sec:cyclic-reps"}

Here we define a local trivialization of the bundle of irreducible representations of $\mathcal{W}_{\xi}$.

::: definition
[]{#def:standard-rep label="def:standard-rep"} Recall that $\omega = \xi^2 = \exp(2\pi i /N)$ and set $\omega^{x} =\exp(2 \pi i x/N)$ for all $x\in \mathbb{C}$. For any $\alpha, \beta, \mu \in \mathbb{C}$, let $\rep{\alpha, \beta, \mu} = (\pi_{\alpha, \beta, \mu}, \mathbb{C}^N)$ be the $\mathcal{W}_\xi$-module defined by $$\label{eq:weight-basis}
    \pi_{\alpha, \beta, \mu}(x) v_n = \omega^{\alpha - n} v_n,
    \quad
    \pi_{\alpha, \beta, \mu}(y) v_n = \omega^{\beta} v_{n-1},
    \quad
    \pi_{\alpha, \beta, \mu}(z) v_n = \omega^{\mu} v_n$$ with indices considered modulo $N$. Since $x = \phi(K)$ and $y$ act diagonalizably on $\rep{\alpha, \beta, \mu}$ we call it a .
:::

$\rep{\alpha, \beta, \mu}$ has character $\hat \chi \in \Wcharhat$ defined by $$\chi(x^{N}) = \omega^{N\alpha}
  \ \ \pi(y^N) = \omega^{N\beta}
  \ \
  \pi(z) = \omega^{\mu}$$ and it is clear that for any integers $k_i$, $$\rep{\alpha + k_1, \beta + k_2, \mu + Nk_3}
  \simeq
  \rep{\alpha , \beta , \mu }$$ so the isomorphism type of $\rep{\alpha, \beta, \mu}$ is completely determined by $\hat \chi$. The parameters $\alpha, \beta, \mu$ are local coordinates on the bundle of modules.

::: theorem
[]{#thm:R-matrix-exists label="thm:R-matrix-exists"} For any admissible characters $(\hat \chi_1, \hat \chi_2)$ an invertible linear operator $$R :
    \rep{\hat{\chi}_{1}} \otimes \rep{\hat{\chi}_{2}}
    \to
    \rep{\hat{\chi}_{1'}} \otimes \rep{\hat{\chi}_{2'}}$$ satisfying ([\[eq:R-mat-module-diagram\]](#eq:R-mat-module-diagram){reference-type="ref" reference="eq:R-mat-module-diagram"}) exists and is unique up to an overall scalar.
:::

::: proof
*Proof.* For each $i$ the module $V(\hat \chi_i)$ is an irreducible $\mathcal{W}_\xi$-module, so its endomorphism algebra is isomorphic to the algebra $$W_\xi/I_{\hat \chi_i}.$$ We see that $\mathcal{R}$ induces an automorphism $$\mathcal{W}_\xi/I_{\hat \chi_1} \otimes \mathcal{W}_\xi/I_{\hat \chi_2} \to
    \mathcal{W}_\xi/I_{\hat \chi_1'} \otimes \mathcal{W}_\xi/I_{\hat \chi_2'}$$ hence an automorphism $$\mathop{\mathrm{End}}( (\mathbb{C}^N)^{\otimes 2}) \to \mathop{\mathrm{End}}( (\mathbb{C}^N)^{\otimes 2})$$ of matrix algebras. Any such automorphism is inner and given by conjugation by some invertible matrix $R$, unique up to an overall scalar. ◻
:::
