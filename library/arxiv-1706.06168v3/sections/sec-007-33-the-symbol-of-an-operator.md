---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-007-33-the-symbol-of-an-operator
section_title: "The Symbol of an Operator"
section_number: 3.3
pages: 9-11
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#symb_subsect label="symb_subsect"}

Given representations $V(\lambda)$ and $V(\alpha)$ (for $\lambda \in \mathbb{N}_0^m$ and $\alpha \in \mathbb{N}_0^l$) of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ and $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^l$ respectively, the space of linear maps between $V(\lambda)$ and $V(\alpha)$ can be viewed as a representation of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^{m+l}$ in a standard way. This space of linear maps is denoted $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$. As discussed previously, we will now use the apolarity form defined above to construct a representation isomorphism between $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ and $V(\lambda \sqcup \alpha)$ (which is a space of polynomials in $m+l$ variables). This will lead us to a natural definition for the symbol of an operator.

The significance of this isomorphism will come from the fact that stability results about $V(\lambda \sqcup \alpha)$ will transfer to $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ via the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}) stated below. We will see in §[\[str_Cstab_subsect\]](#str_Cstab_subsect){reference-type="ref" reference="str_Cstab_subsect"} that this lemma and Grace's theorem almost immediately imply a characterization of stability-preserving operators which is similar to that of Borcea and Brändén.

To this end, consider the standard representation isomorphism $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha)) \cong V(\lambda)^* \boxtimes V(\alpha)$, given by $T \mapsto \sum_{\mu \leq \lambda} (x^\mu y^{\lambda-\mu})^* \boxtimes T(x^\mu y^{\lambda-\mu})$, where $V(\lambda)^*$ is the dual representation of $V(\lambda)$. We omit here the details regarding explicit definitions of the action of (products of) $\mathop{\mathrm{SL}}_2(\mathbb{C})$ on $\mathop{\mathrm{Hom}}$ and dual representations. Instead, we utilize the fact that the apolarity form provides an $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$-invariant isomorphism between $V(\lambda)$ and the dual representation $V(\lambda)^*$, as stated in the following result.

::: proposition
For any $\lambda \in \mathbb{N}_0^m$, there is an $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$-invariant isomorphism $V(\lambda)^* \rightarrow V(\lambda)$ given by $(x^\mu y^{\lambda-\mu})^* \mapsto \binom{\lambda}{\mu}(-1)^{\mu} x^{\lambda-\mu} y^\mu$.
:::

::: proof
*Proof.* We use the apolarity form to determine the isomorphism. In particular, up to scalar $(x^\mu y^{\lambda-\mu})^*$ maps to an element $p \in V(\lambda)$ such that $(x^\mu y^{\lambda-\mu})^* = D^\lambda(p \otimes \cdot)$. We compute: $$D^\lambda(p \otimes x^\alpha y^{\lambda-\alpha}) = \alpha!(\lambda-\alpha)! \binom{\lambda}{\alpha} (-1)^{\alpha} \partial_x^{\lambda-\alpha} \partial_y^\alpha p = \lambda! (-1)^{\alpha} \partial_x^{\lambda-\alpha} \partial_y^\alpha p$$ Picking $p(x,y) := (\lambda!)^{-2}\binom{\lambda}{\mu}(-1)^{\mu} x^{\lambda-\mu} y^\mu$ achieves the desired equality exactly, and therefore $(x^\mu y^{\lambda-\mu})^* \mapsto \binom{\lambda}{\mu}(-1)^{\mu} x^{\lambda-\mu} y^\mu$ is an $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$-invariant isomorphism. ◻
:::

With this, we consider the following string of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^{m+l}$-invariant isomorphisms: $$\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha)) \rightarrow V(\lambda)^* \boxtimes V(\alpha) \rightarrow V(\lambda) \boxtimes V(\alpha) \rightarrow V(\lambda \sqcup \alpha)$$ The first map is the standard isomorphism discussed above, the second map is induced by the previous proposition, and the third map is given by the discussion of outer tensor products in §[\[SL_action_subsect\]](#SL_action_subsect){reference-type="ref" reference="SL_action_subsect"}. This string of maps is explicitly defined on a given linear operator via: $$\begin{split}
        T &\mapsto \sum_{\mu \leq \lambda} (z^\mu w^{\lambda-\mu})^* \boxtimes T(x^\mu y^{\lambda-\mu}) \\
            &\mapsto \sum_{\mu \leq \lambda} \binom{\lambda}{\mu} (-1)^{\mu} z^{\lambda-\mu} w^{\mu} \boxtimes T(x^\mu y^{\lambda-\mu}) \\
            &\mapsto \sum_{\mu \leq \lambda} \binom{\lambda}{\mu} z^{\lambda-\mu} (-w)^{\mu} \cdot T(x^\mu y^{\lambda-\mu})
    \end{split}$$ Here, $T$ acts only on the $x$ and $y$ variables, and $z$ and $w$ are the $\lambda$ variables in $V(\lambda \sqcup \alpha)$. This gives the desired isomorphism between $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ and $V(\lambda \sqcup \alpha)$, and hence we refer to this map as the $\mathop{\mathrm{Symb}}$ map.

::: definition
[]{#symb_def label="symb_def"} For $\lambda \in \mathbb{N}_0^m$ and $\alpha \in \mathbb{N}_0^l$, we define the following $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^{m+l}$-invariant isomorphism: $$\mathop{\mathrm{Symb}}: \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha)) \rightarrow V(\lambda \sqcup \alpha)$$ $$T \mapsto T\left[(zy-xw)^\lambda\right] = \mathop{\mathrm{Hmg}}_{(\lambda,\alpha)}\left(T[(z-x)^\lambda]\right) = \sum_{\mu \leq \lambda} \binom{\lambda}{\mu} z^{\lambda-\mu} (-w)^{\mu} \cdot T(x^\mu y^{\lambda-\mu})$$ We call $\mathop{\mathrm{Symb}}(T)$ the *(universal) symbol of $T$*.
:::

This expression bears striking resemblance to the symbol used by Borcea and Brändén in [@bb1], which motivates the use of the name "symbol" here. (In fact, $\mathop{\mathrm{Symb}}$ is almost the homogenization of the Borcea-Brändén symbol.) In §[\[Cops_sect\]](#Cops_sect){reference-type="ref" reference="Cops_sect"}, $\mathop{\mathrm{Symb}}$ will allow us to reduce the study of $\mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ to the study of $V(\lambda \sqcup \alpha)$ via the next lemma. We refer to this next result as the symbol lemma, and it demonstrates the fundamental connection between an operator $T$, its symbol, and the apolarity form. Note that the computation done here in the proof of this lemma is in a sense redundant. The operator $\mathop{\mathrm{Symb}}$ was essentially defined such that $\mathop{\mathrm{Symb}}(T)$ acts as $T$ via $D^\lambda$.

::: lemma
[]{#symb_lemma label="symb_lemma"} Fix $\lambda \in \mathbb{N}_0^m$, $\alpha \in \mathbb{N}_0^l$, and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$. For $q \in V(\lambda)$ and $r \in V(\alpha)$, we have: $$D^\lambda(\mathop{\mathrm{Symb}}(T) \otimes q \cdot r) = (\lambda!)^2 T(q) \otimes r$$
:::

::: proof
*Proof.* Letting $q_\mu$ be the coefficient of the $x^\mu y^{\lambda-\mu}$ term of $q$, we compute: $$\begin{split}
            D^\lambda(\mathop{\mathrm{Symb}}(T) \otimes q \cdot r) &= D^\lambda \left(\sum_{\mu \leq \lambda} \binom{\lambda}{\mu} x^{\lambda-\mu} (-y)^{\mu} \cdot T(x^\mu y^{\lambda-\mu}) \otimes q \cdot r\right) \\
                &= \sum_{\mu \leq \lambda} \binom{\lambda}{\mu}^2 (\lambda-\mu)! \mu! \cdot T(x^\mu y^{\lambda-\mu}) \otimes (\partial_x^\mu \partial_y^{\lambda-\mu} q) r \\
                &= (\lambda!)^2 \sum_{\mu \leq \lambda} T(x^\mu y^{\lambda-\mu}) \otimes q_\mu \cdot r \\
                &= (\lambda!)^2 T(q) \otimes r \\
        \end{split}$$ ◻
:::
