---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-005-6-tilting-modules-for-quantum-groups
section_title: "Tilting modules for quantum groups"
section_number: 6
pages: 16-17
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.952
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
[]{#tilting-quantum label="tilting-quantum"}

We review some results about quantized tilting modules which are needed to show that the category of tilting modules can be obtained as a mod $\mathfrak{m}$ evaluation.

## Lusztig's integral form

We denote by $\mathcal{A} = {\mathbb Z}[v,v^{-1}]$ the Laurent polynomial ring in an indeterminate $v$ and by $U = U_{\mathcal{A}}$ Lusztig's integral form (with divided powers) of the Drinfeld quantized enveloping algebra $U_v$ over ${\mathbb Q}(v)$ [@Lusztig-book]. Any commutative ring $R$ with 1 and a fixed invertible element $\bf{v}$ can be regarded as a commutative $\mathcal{A}$-algebra via the homomorphism $\phi: \mathcal{A} \to R$ such that $\phi(v^n) = {\mathbf{v}}^n$ for all $n \in {\mathbb Z}$. For any $\mathcal{A}$-algebra $R$ we denote $U_R = U_{\mathcal{A}} \otimes_{\mathcal{A}} R$. We apply this for $R = {\mathbb Q}(q)$ and specialize the generic parameter $v$ to a primitive $\ell$-th root of unity $q$ with $\ell$ odd, and assume that $\ell$ is not divisible by $3$ if $\mathfrak{g} \cong \mathfrak{g}_2$. We also assume $\ell > h$, the Coxeter number of $\mathfrak{g}$. Then we denote by $Rep(U_q(\mathfrak{g}))$ the category of finite dimensional representations of $U_q(\mathfrak{g})$ of type $1$ as in [@Andersen-Polo-Wen].

## Quantized tilting modules over ${\mathbb Q}(q)$

In $Rep(U_q(\mathfrak{g}))$ we have analogs of Weyl and induced modules (where the latter can be defined by means of the triangular decomposition of $U_q(\mathfrak{g})$) which we denote again by $V(\lambda)$ and $H^0(\lambda)$, $\lambda \in X^+$. These satisfy exactly the same $Ext$-vanishing conditions as in the modular case. In particular $$Ext^i (V(\lambda), H^0(\lambda)) = 0$$ for $i > 0, \ \lambda \in X^+$ (see [@Andersen-quantized] and the references therein). This uses the quantum variant of Kempf's vanishing theorem. We can then define modules with a good filtration and a Weyl filtration and define tilting modules as in the modular case. The main statement (proposition [\[prop:tilting-ind\]](#prop:tilting-ind){reference-type="ref" reference="prop:tilting-ind"}) about indecomposable tilting modules still holds and we denote by $T(\lambda)$ the indecomposable tilting module attached to $\lambda \in X^+$.

## Quantized tilting modules over $R$

As in the modular case, the entire theory of tilting modules can be developed over a (complete) discrete valuation ring. The crucial ingredient here is that Kempf's vanishing theorem holds over the ground ring $\mathcal{A}$ as well. This follows from work of Ryom-Hansen [@Ryom-Hansen] and Kaneda [@Kaneda-cohom] [@Kaneda-cohom-preprint]. For an $\mathcal{A}$-algebra $R$ we denote by $H^0_R(\lambda)$ and $V_R(\lambda)$ the corresponding induced module and Weyl module. For any base change $\mathcal{A} \to R$ we have $$H^0_{\mathcal{A}}(\lambda) \otimes_{\mathcal{A}} R = H^0_R (\lambda) \ \forall \lambda \in X^+$$ and likewise for $V_R(\lambda)$. Again by Kempf's vanishing theorem over $\mathcal{A}$ and standard facts about $H^i$ we get the vanishing of $Ext^i_{U_{\mathcal{A}}}(\mathcal{A}, H^0_{\mathcal{A}}(\lambda) \otimes H^0_{\mathcal{A}}(\mu) )$ for all $\lambda,\mu \in X^+$ and $i > 0$ (see also [@Kaneda-cohom-preprint]). The remaining arguments are the same as in the modular case. In particular for each $\lambda \in X^+$ there is an indecomposable tilting module $T_R(\lambda)$, $\lambda \in X^+$, such that its $\lambda$-weight space is free of rank 1 [@Kaneda-cohom-preprint Theorem 7.6] and every tilting module decomposes uniquely into a direct sum of the $T_R(\lambda)$.

Since the $\lambda$-weight space is free of rank 1, the arguments of Jantzen [@Jantzen E.20] go through and we obtain

::: corollary
Let $R$ be a complete discrete valuation ring with residue field $R/\mathfrak{m} = \mathbb{Q}(q)$ (or ${\mathbb C}$) of characteristic 0. Then $$\begin{aligned}
 T_R(\lambda) \otimes R/\mathfrak{m}  & \cong T_{R/\mathfrak{m}} (\lambda) \\  End (T_R(\lambda)) \otimes_R R/\mathfrak{m}) & \cong End (T_R(\lambda)) \otimes_R R/\mathfrak{m}.
\end{aligned}$$
:::
