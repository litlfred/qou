---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-005-31-the-action-of-sl2c
section_title: "The Action of SL2(C)"
section_number: 3.1
pages: 7-8
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.99
---
[]{#SL_action_subsect label="SL_action_subsect"}

Given $(\alpha:\beta) \in \mathbb{CP}^1$ and $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$, we define the usual action of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ on $\mathbb{CP}^1$ via $\phi \cdot (\alpha:\beta) := \phi \binom{\alpha}{\beta}$. That is, $\phi$ acts by matrix multiplication on the vector $\binom{\alpha}{\beta}$. Equivalently, $\phi$ acts as its corresponding Möbius transformation on $\mathbb{CP}^1$. Note that, as with Möbius transformations, $\mathop{\mathrm{SL}}_2(\mathbb{C})$ acts transitively on circular regions in $\mathbb{CP}^1$.

This then induces an action on $V(n)$ by acting on the roots (in $\mathbb{CP}^1$) of polynomials in $V(n)$. Given $p \in V(n)$ and $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$, this action is defined via: $$(\phi \cdot p)(x,y) := p\left(\phi^{-1} \binom{x}{y}\right) \equiv (p \circ \phi^{-1})(x,y)$$ We can define a similar action of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ on $V(\lambda)$, for $\lambda \in \mathbb{N}_0^m$. Specifically, given $p \in V(\lambda)$ and $(\phi_1,\ldots,\phi_m) \in \mathop{\mathrm{SL}}_2(\mathbb{C})^m$, this action is defined via: $$\big((\phi_1,\ldots,\phi_m) \cdot p\big)(x_1,y_1,\ldots,x_m,y_m) := p\left(\phi_1^{-1} \binom{x_1}{y_1}, \ldots, \phi_m^{-1}\binom{x_m}{y_m}\right)$$ These actions turn $V(n)$ and $V(\lambda)$ into representations of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ and $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$, respectively. These are precisely the finite dimensional irreducible representations of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ and $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ (see Lecture 11 of [@fulton2013reptheory]), and so they are the basic building blocks of the $\mathop{\mathrm{SL}}_2(\mathbb{C})$ representation theory. Actions on $V(n)$ and $V(\lambda)$ can be extended to tensor products in the usual way, and in this paper we will make use of both inner and outer tensor products. We now briefly discuss tensor product actions for those less familiar.

The outer tensor product of $V(\lambda_k)$, denoted $V(\lambda_1) \boxtimes \cdots \boxtimes V(\lambda_m)$, is a representation of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ with action by $(\phi_1,\ldots,\phi_m)$ on simple tensors given as follows: $$(\phi_1, \cdots, \phi_m) \cdot (p_1 \boxtimes \cdots \boxtimes p_m) := (\phi_1 \cdot p_1) \boxtimes (\phi_2 \cdot p_2) \boxtimes \cdots \boxtimes (\phi_m \cdot p_m)$$ This implies that $V(\lambda)$ and $V(\lambda_1) \boxtimes \cdots \boxtimes V(\lambda_m)$ are isomorphic as representations, and this fact will be used when we define the symbol in §[\[symb_subsect\]](#symb_subsect){reference-type="ref" reference="symb_subsect"}.

The inner tensor product of $V(\lambda_k)$, denoted $V(\lambda_1) \otimes \cdots \otimes V(\lambda_m)$, is a representation of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ with action by $\phi$ on simple tensors given as follows: $$\phi \cdot (p_1 \otimes \cdots \otimes p_m) := (\phi \cdot p_1) \otimes (\phi \cdot p_2) \otimes \cdots \otimes (\phi \cdot p_m)$$ While $V(\lambda)$ and $V(\lambda_1) \otimes \cdots \otimes V(\lambda_m)$ are isomorphic as vector spaces, they are representations of different groups ($(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ and $\mathop{\mathrm{SL}}_2(\mathbb{C})$ respectively). The inner tensor product relates to invariants of multiple polynomials with respect to a single $\mathop{\mathrm{SL}}_2(\mathbb{C})$ action. For instance, the apolarity form takes two distinct polynomials as input, and it is a classical result that this form is invariant with respect to a single action by Möbius transformation. As it turns out, this form can be viewed as an $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invaiant map on an inner tensor product of polynomial spaces. It will therefore be important for us to understand these inner tensor products in a little more detail.
