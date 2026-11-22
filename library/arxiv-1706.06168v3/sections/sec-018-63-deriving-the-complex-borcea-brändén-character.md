---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-018-63-deriving-the-complex-borcea-brändén-character
section_title: "Deriving the Complex Borcea-Brändén Characterization"
section_number: 6.3
pages: 22-23
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.977
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#Cops_deriv_subsect label="Cops_deriv_subsect"}

As mentioned above, we hope to obtain the Borcea-Brändén characterization from our strong stability characterization given in Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}. To this end, we state two corollaries to Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}, which look (naively) as close to the Borcea-Brändén characterization as possible. Let $C^c$ denote the complement of $C$ in $\mathbb{CP}^1$.

::: corollary
[]{#naive_CBB_cor1 label="naive_CBB_cor1"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$, a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$, and a Grace pair of the form $(C_1 \times \cdots \times C_m, C_1^c \times \cdots \times C_m^c)$. The following are equivalent.

1.  $T$ preserves strong $(C_1 \times \cdots \times C_m)$-stability.

2.  $\mathop{\mathrm{Symb}}(T)$ is $(C_1^c \times \cdots \times C_m^c) \times (C_1 \times \cdots \times C_m)$-stable.
:::

::: corollary
[]{#naive_CBB_cor2 label="naive_CBB_cor2"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$. $T$ preserves strong stability iff $\mathop{\mathrm{Symb}}(T)$ is $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_+^m)$-stable.
:::

In Theorem [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"}, the analogous "if" direction of the previous corollary is paraphrased as follows: *$T$ preserves weak stability if the Borcea-Brändén symbol of $T$ is stable*. To see how this statement relates, we restate the definition of the Borcea-Brändén symbol: $$\mathop{\mathrm{Symb}}_{BB}(T) := T\left[(z+x)^\lambda\right] = \sum_{\mu \leq \lambda} \binom{\lambda}{\mu} z^{\lambda-\mu} T(x^\mu)$$ Notice that by applying $z \mapsto -z$ and homogenizing, we obtain (up to scalar) the universal symbol $\mathop{\mathrm{Symb}}(T)$ defined in this paper. The crucial difference then is the fact that the Borcea-Brändén "if" direction deals only with *open* upper half-planes, whereas the previous corollary requires *closed* half-plane stability of $\mathop{\mathrm{Symb}}(T)$ in the first $m$ pairs of variables. That is, the required premises of the "if" direction of the previous corollary are strictly stronger than that of the Borcea-Brändén result.

These two results can be reconciled, however, which we now demonstrate. The following result provides the main link to the Borcea-Brändén characterization, and it can be intuitively described as follows: with the exception of having a one-dimensional range, a linear operator which maps $(C_1 \times \cdots \times C_m)$-stable polynomials to weak $(B_1 \times \cdots \times B_m)$-stable polynomials can only have zeros on the boundary of the set of $(C_1 \times \cdots \times C_m)$-stable polynomials.

::: lemma
[]{#bb_Clink label="bb_Clink"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$, a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$, and any open circular regions $C_1,\ldots,C_m,B_1,\ldots,B_m \subseteq \mathbb{CP}^1$. The following are equivalent.

1.  $T$ maps $(C_1 \times \cdots \times C_m)$-stable polynomials to weakly $(B_1 \times \cdots \times B_m)$-stable polynomials.

2.  One of the following holds:

    1.  $T$ maps $(\overline{C_1} \times \cdots \times \overline{C_m})$-stable polynomials to nonzero $(B_1 \times \cdots \times B_m)$-stable polynomials.

    2.  $T \equiv p_0 \cdot \psi$ for some weakly $(B_1 \times \cdots \times B_m)$-stable polynomial $p_0 \in V(\alpha)$ and some linear functional $\psi$.
:::

::: proof
*Proof.* By appropriate $\mathop{\mathrm{SL}}_2(\mathbb{C})$ action, we can assume WLOG that $C_k = B_k = \mathbb{D}$, the unit disc, for all $k \in [m]$.

$(i) \Rightarrow (ii)$. We show that if $(a)$ is not the case, then $(b)$ must hold. It follows from $(i)$ that $T$ maps $\overline{\mathbb{D}}^m$-stable polynomials to (possibly identically zero) $\mathbb{D}^m$-stable polynomials. So, if $(a)$ is not the case, we have that $T(p) \equiv 0$ for some $\overline{\mathbb{D}}^m$-stable polynomial $p \in V(\lambda)$.

The rest of the argument is essentially the proof of necessity found in [@bb1] for Theorem [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"}. Since the set of nonzero $\overline{\mathbb{D}}^m$-stable polynomials is open in $V(\lambda)$, there is some ball $B(p) \subset V(\lambda)$ centered at $p$ such that $B(p)$ contains only $\overline{\mathbb{D}}^m$-stable polynomials. So, $T[B(p)]$ is an open set in the image of $T$ containing 0 and otherwise consisting of $\mathbb{D}^m$-stable polynomials. Therefore, the image of $T$ is a vector space consisting of $\mathbb{D}^m$-stable polynomials. Lemma [\[dim_lemma\]](#dim_lemma){reference-type="ref" reference="dim_lemma"} (and appropriate $\mathop{\mathrm{SL}}_2(\mathbb{C})$ action) then implies the image of $T$ is of dimension $\leq 1$, and $(b)$ follows.

$(ii) \Rightarrow (i)$. If $(b)$ holds, then $(i)$ is immediate. Otherwise, fix $p \in V(\lambda)$ such that $p$ is $\mathbb{D}^m$-stable. For all $n \in \mathbb{N}$, define: $$p_n := p((1-n^{-1})x_1, y_1, (1-n^{-1})x_2, y_2, \ldots, (1-n^{-1})x_m, y_m)$$ So, $p_n$ is $\overline{\mathbb{D}}^m$-stable for all $n$, and $\lim_{n \rightarrow \infty} p_n = p$ coefficient-wise. By $(ii)$, $T(p_n)$ is $\mathbb{D}^m$-stable for all $n$, and by continuity, $T(p) = \lim_{n \rightarrow \infty} T(p_n)$. Hurwitz's theorem then implies $T(p)$ is either identically zero or $\mathbb{D}^m$-stable. ◻
:::

This lemma then yields the following corollaries to Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}. Applying the necessary maps to convert $\mathop{\mathrm{Symb}}$ to $\mathop{\mathrm{Symb}}_{BB}$ as discussed above, these results give precisely the Borcea-Brändén characterization proven in Theorem [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} and more generally in Theorem 6.3 of [@bb1]. In particular, Corollary [\[CBB_cor1\]](#CBB_cor1){reference-type="ref" reference="CBB_cor1"} can be seen as a unification of the complex characterization results of [@bb1].

::: corollary
[]{#CBB_cor1 label="CBB_cor1"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$, a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$, and any open circular regions $C_1, \ldots, C_m$. The following are equivalent.

1.  $T$ preserves weak $(C_1 \times \cdots \times C_m)$-stability.

2.  One of the following holds:

    1.  $\mathop{\mathrm{Symb}}(T)$ is $(\overline{C_1}^c \times \cdots \times \overline{C_m}^c) \times (C_1 \times \cdots \times C_m)$-stable.

    2.  $T \equiv p_0 \cdot \psi$ for some weakly $(C_1 \times \cdots \times C_m)$-stable polynomial $p_0 \in V(\alpha)$ and some linear functional $\psi$.
:::

::: proof
*Proof.* The result follows from the Lemma [\[bb_Clink\]](#bb_Clink){reference-type="ref" reference="bb_Clink"} and Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"} applied to an operator $T$ which maps $(\overline{C_1} \times \cdots \times \overline{C_m})$-stable polynomials to nonzero $(C_1 \times \cdots \times C_m)$-stable polynomials. ◻
:::

::: corollary
[]{#CBB_cor2 label="CBB_cor2"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$. $T$ preserves weak stability iff one of the following holds:

1.  $\mathop{\mathrm{Symb}}(T)$ is $(\mathcal{H}_-^m \times \mathcal{H}_+^m)$-stable.

2.  $T \equiv p_0 \cdot \psi$ for some weakly stable polynomial $p_0 \in V(\alpha)$ and some linear functional $\psi$.
:::

Notice that our naive guess at strong stability results which emulate the Borcea-Brändén characterization (Corollaries [\[naive_CBB_cor1\]](#naive_CBB_cor1){reference-type="ref" reference="naive_CBB_cor1"} and [\[naive_CBB_cor2\]](#naive_CBB_cor2){reference-type="ref" reference="naive_CBB_cor2"}) was incorrect. We actually needed to consider *closed* circular stability regions $\overline{C_k}$, so that their complements in $\mathbb{CP}^1$ would be open (i.e., to ensure Grace pair disjointness, which is required to apply Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}). We see this play out in condition $(ii)(a)$ of Corollary [\[CBB_cor1\]](#CBB_cor1){reference-type="ref" reference="CBB_cor1"}.
