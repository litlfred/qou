---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-067-87-poincare-series
section_title: "Poincare series"
section_number: 8.7
pages: 66-67
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.938
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
In general, Proposition [\[prop:chart\]](#prop:chart){reference-type="ref" reference="prop:chart"} can be used to show

::: proposition
[]{#prop:poincare label="prop:poincare"}

For any standard Young tableau of size $n$, the bigraded Poincaré series of graded algebras $\mathring{\mathcal{A}}_T(*)$ are given by the following formulas: $$\label{eqn:poincare1}
P(\mathring{\mathcal{A}}_T(\mathbb{C}^2)) = (1-q)^{-n} (1-t)^{-n} \prod_{i=1}^{n} \frac{1}{1-z_i^{-1}} \prod_{1\leq i<j \leq n} \zeta \left(\frac {z_i}{z_j}\right)$$ $$\label{eqn:poincare2}
P(\mathring{\mathcal{A}}_T(\mathbb{C})) = (1-q)^{-n} \prod_{i=1}^{n}\frac{1}{1-z_i^{-1}} \prod_{1\leq i<j \leq n} \zeta \left(\frac {z_i}{z_j}\right)$$ $$\label{eqn:poincare3}
P(\mathring{\mathcal{A}}_T(\mathrm{point})) = \prod_{i=1}^{n}\frac{1}{1-z_i^{-1}}  \prod_{i=2}^{n}\frac{1}{1-q t  z_i/z_{i+1}} \prod_{1\leq i<j \leq n} \zeta \left(\frac {z_i}{z_j}\right)$$ where $$\zeta(x) = \frac {(1 - x)(1 - q t x)}{(1 - q x)(1 - t x)}$$ and $z_i$ denotes the weight of the $i$th box in the standard Young tableau $T$.
:::

::: proof
*Proof.* We will prove [\[eqn:poincare1\]](#eqn:poincare1){reference-type="eqref" reference="eqn:poincare1"}, and leave the other two formulas as exercises for the interested reader. In order to prove the formula by induction, one needs to compute the following quotient for any standard Young tableau $T$ of size $n$ and an inner corner $\square \in T$: $$\frac {P(\mathring{\mathcal{A}}_{T \cup \square} (\mathbb{C}^2))}{P(\mathring{\mathcal{A}}_T(\mathbb{C}^2))} = \frac 1{(1-q)(1-t)(1-z_{\square}^{-1})} \prod_{i=1}^{n} \zeta \left(\frac {z_i}{z_{\square}}\right)$$ Since $T$ is a Young tableau, it is easy to show that the product of $\zeta$'s can be simplified to: $$\frac {P(\mathring{\mathcal{A}}_{T \cup \square} (\mathbb{C}^2))}{P(\mathring{\mathcal{A}}_T(\mathbb{C}^2))} = \frac 1{(1-q)(1-t)} \cdot \frac {\prod_{\blacksquare\text{inner corner of }T}^{\blacksquare\neq \square} (1-z_{\blacksquare}/z_{\square})}{\prod_{\blacksquare\text{outer corner of }T} (1-z_{\blacksquare}/z_{\square})}$$ The above formula follows from [\[eqn:genrel\]](#eqn:genrel){reference-type="eqref" reference="eqn:genrel"} and the relation [\[eqn:expectation\]](#eqn:expectation){reference-type="eqref" reference="eqn:expectation"} for the weights. ◻
:::

If we pass to the decategorified setting by substituting $t=q^{-1}$, we see that the Poincaré series depends only on the Young diagram of $T$:

::: corollary
[]{#cor:decat ps label="cor:decat ps"} $\displaystyle
P(\mathring{\mathcal{A}}_T(\mathbb{C}))|_{t=q^{-1}}=\frac{1}{\prod_{\square\in \lambda}(1-q^{h(\square)})}.$
:::

::: proof
*Proof.* If we let $\zeta_{q,q^{-1}}(x) = \zeta(x)|_{t=q^{-1}}$, then clearly $\zeta_{q,q^{-1}}(x)=\zeta_{q,q^{-1}}(x^{-1}).$ It follows that the function $\prod_{i<j}\zeta_{q,q^{-1}}(z_i/z_j)$ is actually symmetric in $z_i$, hence depends only of the shape of the Young diagram. Let us choose the permutation of $z_i$ such that $$(z_1,\ldots,z_n)=(1,q,\ldots,q^{\lambda_1-1},q^{-1},\ldots,q^{\lambda_1-2},\ldots),$$ Given $z_i$ on the vertical boundary of $\lambda$ and $z_j$ on the horizonal boundary such that $i<j$, one can consider the box $\square$ in the same row as $z_i$ and in the same column as $z_j$. We get $(1-qz_i/z_j)=(1-q^{h(\square)})$, where $h(\square)$ denotes the hook-length of $\square$. One can check after all telescopic cancellations $$\prod_{i<j}\zeta_{q,q^{-1}}(z_i/z_j)=\frac{(1-q)^n\prod_{j>1}(1-z_i^{-1})}{\prod_{\square\in \lambda}(1-q^{h(\square)})},$$ so $$P(\mathring{\mathcal{A}}_T)=\prod_{i=1}^{n}\frac{1}{(1-q)(1-z_i^{-1})}\prod_{i<j}\zeta_{q,q^{-1}}(z_i/z_j)=\frac{1}{\prod_{\square\in \lambda}(1-q^{h(\square)})}.$$ ◻
:::

To compute the full endomorphism ring of the projector $P_T$, we should tensor with $\wedge^{\bullet}\mathcal{T}_n^{\vee}$. When we restrict to the affine chart $\mathrm{FHilb}_T \subset \mathrm{FHilb}_n$ the vector space $\mathbb{C}^n$ is endowed with a preferred basis $e_1,...,e_n$, which more abstractly means that the tautological bundle is trivialized: $$\mathcal{T}_n|_{\mathrm{FHilb}_T} \cong \mathcal{O}\cdot e_1 \oplus...\oplus \mathcal{O}\cdot e_n$$ The basis vectors are indexed by boxes $\square$ in the Young diagram of $T$, and the torus $\mathbb{C}^{*} \times \mathbb{C}^*$ acts on the basis vector $e^\square$ by the character $z_\square= q^at^b$ for any box $\square= (a,b)$. We conclude that: $$\wedge^{\bullet}\mathcal{T}_n^{\vee}|_{\mathrm{FHilb}_T} \cong \wedge(\xi_1,\ldots,\xi_n)$$ where the equivariant weights of the symbols $\xi_\square$ are given by $z_\square^{-1} = q^{-a}t^{-b}$. In particular, Conjecture [\[conj:homfly\]](#conj:homfly){reference-type="ref" reference="conj:homfly"} implies that $\mathrm{End}(P_T)$ should be the tensor product of the homology on the "bottom row" with an exterior algebra.

The theorems stated in the introduction can be easily deduced from the results above.

::: proof
*Proof.* (Of Theorem [\[thm:symm antisymm\]](#thm:symm antisymm){reference-type="ref" reference="thm:symm antisymm"} ) The observations in Examples [\[ex:Sym n\]](#ex:Sym n){reference-type="ref" reference="ex:Sym n"} and [\[ex:Lambda n\]](#ex:Lambda n){reference-type="ref" reference="ex:Lambda n"}, together with the remark above, show that the expressions on the right-hand side of equations [\[eqn:antisym\]](#eqn:antisym){reference-type="eqref" reference="eqn:antisym"} and [\[eqn:sym\]](#eqn:sym){reference-type="eqref" reference="eqn:sym"} agree with $\mathcal{A}_T(\mathbb{C}) \otimes \left( \wedge^{\bullet}\mathcal{T}_n^{\vee}|_{\mathring{\mathrm{FHilb}}_T(\mathbb{C})} \right)$. On the other hand, these expressions agree with the known homology of the symmetric projector (computed by Hogancamp in [@Hog]) and the antisymmetric projector (computed by Abel and Hogancamp in [@AbHog].) ◻
:::

::: proof
*Proof.* (of Theorem [\[thm:hecke projector\]](#thm:hecke projector){reference-type="ref" reference="thm:hecke projector"}). From Corollary [\[cor:decat ps\]](#cor:decat ps){reference-type="ref" reference="cor:decat ps"}, we see that $$P\left(\mathring{\mathcal{A}}_T(\mathbb{C}) \otimes \left( \wedge^{\bullet}\mathcal{T}_n^{\vee}|_{\mathring{\mathrm{FHilb}}_T(\mathbb{C})} \right) \right)= 
\prod_{\square\in \lambda}\frac{1-aq^{b(\square)-a(\square)}}{(1-q^{h(\square)})}.$$ This right-hand side is a well-known formula for the $\lambda$-colored HOMFLY-PT polynomial of the unknot, which is by definition the Markov trace of the Jones-Wenzl projector $p_\lambda \in H_n$. ◻
:::
