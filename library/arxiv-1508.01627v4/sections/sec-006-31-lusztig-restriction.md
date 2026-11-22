---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-006-31-lusztig-restriction
section_title: "Lusztig restriction"
section_number: 3.1
pages: 6-6
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.973
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:*RLG label="subsec:*RLG"} We consider the following setup: ${\mathbf{G}}$ is a connected reductive algebraic group over an algebraic closure of the finite field ${\mathbb{F}}_p$, and $F:{\mathbf{G}}\rightarrow{\mathbf{G}}$ is a Steinberg endomorphism of ${\mathbf{G}}$, with finite group of fixed points ${\mathbf{G}}^F$. For an $F$-stable Levi subgroup ${\mathbf{L}}\le{\mathbf{G}}$ of ${\mathbf{G}}$ Lusztig defined, via certain $\ell$-adic cohomology constructions, induction and restriction functors $${R_{\mathbf{L}}^{\mathbf{G}}}:{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{L}}^F)\rightarrow{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{G}}^F)\quad\text{ and }\quad
  {\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}:{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{G}}^F)\rightarrow{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{L}}^F)$$ between the respective groups of virtual characters. These are adjoint to one another with respect to the usual scalar product of characters. We need the following connection between Lusztig restriction and ordinary restriction on regular semisimple conjugacy classes:

::: prop
[]{#prop:restr label="prop:restr"} Let ${\mathbf{L}}\le{\mathbf{G}}$ be an $F$-stable Levi subgroup. Let $\chi\in{\operatorname{Irr}}({\mathbf{G}}^F)$ and $s\in {\mathbf{L}}^F$ be regular semisimple. Then ${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\chi)(s)=\chi(s)$.
:::

::: proof
*Proof.* According to the character formula in [@DM Prop. 12.2(ii)] we have $${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\chi)(s)=\frac{|C_{\mathbf{L}}^\circ(s)^F|}{|C_{\mathbf{G}}^\circ(s)^F|}
   \sum_{u\in C_{\mathbf{G}}^\circ(s)^F_u}Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}(u,1)
   \,\chi(s),$$ where the sum runs over unipotent elements in $C_{\mathbf{G}}^\circ(s)^F$, and $Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}$ is a certain 2-parameter Green function. Since $s$ is assumed to be regular semisimple, ${\mathbf{T}}:=C_{\mathbf{G}}^\circ(s)=C_{\mathbf{L}}^\circ(s)$ is a torus. Hence the only term in the sum is the one for $u=1$, and by [@DM p. 98] the Green function takes the value $$Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}(1,1)=Q_{{\mathbf{T}}}^{{\mathbf{T}}}(1,1) =1$$ (again using that $C_{\mathbf{G}}^\circ(s)$ contains no non-trivial unipotent elements). The claim follows. ◻
:::
