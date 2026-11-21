---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-021-72-strong-real-stability-preservation
section_title: "Strong Real Stability Preservation"
section_number: 7.2
pages: 24-25
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 1.0
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
We state and prove our strong real stability preservation characterization here, and then derive the Borcea-Brändén characterization as a corollary. The proof here takes a bit more work than in the complex case, and will rely on many of the real stability results discussed in §[\[stab_subsect\]](#stab_subsect){reference-type="ref" reference="stab_subsect"}. This extra work is essentially taken from the proof of Theorem [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"} found in [@bb1].

::: theorem
[]{#Rops_graces label="Rops_graces"} Fix $\lambda \in \mathbb{N}_0^m$, $\alpha \in \mathbb{N}_0^l$, and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ such that $T$ restricts to a real linear operator from $V_\mathbb{R}(\lambda)$ to $V_\mathbb{R}(\alpha)$. The following are equivalent.

1.  $T$ preserves strong real stability.

2.  $\mathop{\mathrm{Symb}}(T)$ is either $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_+^l)$-stable or $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_-^l)$-stable.
:::

::: proof
*Proof.* $(i) \Rightarrow (ii)$. Fixing $(z_0:w_0) \in \overline{\mathcal{H}_-}^m$, we have that $(w_0x - z_0y)^\lambda$ is $\mathcal{H}_+^m$-stable. If $(z_0:w_0) \in \overline{\mathbb{R}}^m$, then $T[(w_0x - z_0y)^\lambda]$ is nonzero and real stable by assumption. Combining the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}) and the evaluation symbol lemma (Lemma [\[ev_lemma\]](#ev_lemma){reference-type="ref" reference="ev_lemma"}), this implies $\mathop{\mathrm{Symb}}(T)(z_0,w_0,x,y) = (-1)^\lambda T[(w_0x - z_0y)^\lambda]$ is both $\mathcal{H}_+^l$-stable and $\mathcal{H}_-^l$-stable.

On the other hand, suppose $(z_0:w_0) \not\in \overline{\mathbb{R}}^m$. By Lemma [\[rs_lemma\]](#rs_lemma){reference-type="ref" reference="rs_lemma"}, we have that $T[(w_0x - z_0y)^\lambda]$ is either $\mathcal{H}_+^l$-stable, $\mathcal{H}_-^l$-stable, or zero. Now suppose there are $(z_0:w_0), (z_0':w_0') \in \overline{\mathcal{H}_-}^m \setminus \overline{\mathbb{R}}^m$ such that $T[(w_0x - z_0y)^\lambda]$ is $\mathcal{H}_+^l$-stable and $T[(w_0'x - z_0'y)^\lambda]$ is $\mathcal{H}_-^l$-stable. By a homotopy argument, there exists $(z_0'':w_0'') \in \overline{\mathcal{H}_-}^m \setminus \overline{\mathbb{R}}^m$ such that $T[(w_0''x - z_0''y)^\lambda]$ is $(\mathcal{H}_+^l \cup \mathcal{H}_-^l)$-stable or zero. By Lemma [\[scal_rs_lemma\]](#scal_rs_lemma){reference-type="ref" reference="scal_rs_lemma"}, $T[c_0(w_0''x - z_0''y)^\lambda]$ is either real stable or zero for some complex scalar $c_0 \neq 0$.

Let $c_0(w_0''x - z_0''y)^\lambda = q(x,y) + ir(x,y)$ for $q,r \in V_\mathbb{R}(\lambda)$, which are both real stable or zero by Hermite-Biehler (Proposition [\[hermite-biehler\]](#hermite-biehler){reference-type="ref" reference="hermite-biehler"}). Note further that $r \not\equiv 0$ since $(z_0'':w_0'') \not\in \overline{\mathbb{R}}^m$. However, since $T(q + ir) = T(q) + iT(r)$ is real stable or zero and $T$ restricts to real linear operator, it must be that $T(r) \equiv 0$. This contradicts the fact that $T$ strongly preserves real stability.

So, $\mathop{\mathrm{Symb}}(T)(z_0,w_0,x,y) = (-1)^\lambda T[(w_0x - z_0y)^\lambda]$ is either $\mathcal{H}_+^l$-stable (in the $x,y$ variables) for all $(z_0:w_0) \in \overline{\mathcal{H}_-}^m \setminus \overline{\mathbb{R}}^m$, or $\mathcal{H}_-^l$-stable for all $(z_0:w_0) \in \overline{\mathcal{H}_-}^m \setminus \overline{\mathbb{R}}^m$. Combining this with the $(z_0:w_0) \in \overline{\mathbb{R}}^m$ case, we have that $\mathop{\mathrm{Symb}}(T)$ is either $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_+^l)$-stable or $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_-^l)$-stable.

$(ii) \Rightarrow (i)$. By the complex stability characterization (Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}), $T$ maps $\mathcal{H}_+^m$-stable polynomials to either nonzero $\mathcal{H}_+^l$-stable polynomials or nonzero $\mathcal{H}_-^l$-stable polynomials. Since $T$ restricts to a real linear operator on $V_\mathbb{R}(\lambda)$, $T$ preserves strong real stability. ◻
:::

As a final note, the "homotopy argument" used in the previous proof is not quite that of the proof found in [@bb1], though it is similar. Here, one just needs to be a bit more careful about the precise homotopy with respect to points at infinity.
