---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-022-73-deriving-the-real-borcea-brändén-characteriza
section_title: "Deriving the Real Borcea-Brändén Characterization"
section_number: 7.3
pages: 25-26
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.979
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#Rops_deriv_subsect label="Rops_deriv_subsect"}

As in the complex case, we now obtain the Borcea-Brändén weak real stability characterization as a corollary to our strong real stability characterization given in Theorem [\[Rops_graces\]](#Rops_graces){reference-type="ref" reference="Rops_graces"}. To this end, we start by giving a sort of real stability version of Lemma [\[bb_Clink\]](#bb_Clink){reference-type="ref" reference="bb_Clink"}. The proof of this lemma is similar in spirit to that of the strong real stability characterization given above.

::: lemma
[]{#bb_Rlink label="bb_Rlink"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ such that $T$ restricts to a real linear operator from $V_\mathbb{R}(\lambda)$ to $V_\mathbb{R}(\alpha)$. The following are equivalent.

1.  $T$ preserves weak real stability.

2.  One of the following holds:

    1.  $T$ maps $\overline{\mathcal{H}_+}^m$-stable polynomials to nonzero $\mathcal{H}_+^m$-stable polynomials.

    2.  $T$ maps $\overline{\mathcal{H}_+}^m$-stable polynomials to nonzero $\mathcal{H}_-^m$-stable polynomials.

    3.  $T$ has image of dimension at most two, and is of the form $$T: p \mapsto q \cdot \psi_1(p) + r \cdot \psi_2(p)$$ where $q,r \in V_\mathbb{R}(\alpha)$ are weakly real stable such that $q \ll r$, and $\psi_1,\psi_2$ are real linear functionals.
:::

::: proof
*Proof.* $(i) \Rightarrow (ii)$. By the complex characterization (Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}), we only need to consider evaluation symbols when demonstrating $(a)$ or $(b)$. For any $(z_0:w_0) \in \mathcal{H}_-^m$, Lemma [\[rs_lemma\]](#rs_lemma){reference-type="ref" reference="rs_lemma"} then implies $T[(w_0x-z_0y)^\lambda]$ is either $\mathcal{H}_+^m$-stable, $\mathcal{H}_-^m$-stable, or identically zero. We now show that $(c)$ holds if $(a)$ and $(b)$ do not.

If neither $(a)$ nor $(b)$ holds for evaluation symbols, then there exist $(z_0:w_0),(z_0':w_0') \in \mathcal{H}_-^m$ such that $T[(w_0x-z_0y)^\lambda]$ is $\mathcal{H}_+^m$-stable or zero and $T[(w_0'x-z_0'y)^\lambda]$ is $\mathcal{H}_-^m$-stable or zero. As in the proof of the strong real stability characterization (Theorem [\[Rops_graces\]](#Rops_graces){reference-type="ref" reference="Rops_graces"}), a homotopy argument implies there exists $(z_0'':w_0'') \in \mathcal{H}_-^m$ such that $T[(w_0''x-z_0''y)^\lambda]$ is $(\mathcal{H}_+^m \cup \mathcal{H}_-^m)$-stable or zero. Lemma [\[scal_rs_lemma\]](#scal_rs_lemma){reference-type="ref" reference="scal_rs_lemma"} then implies $T[c_0(w_0''x-z_0''y)^\lambda]$ is real stable or zero, for some complex scalar $c_0 \neq 0$.

For the sake of simplicity, we denote $q_0(x,y) = q_0(x_1,y_1,\ldots,x_m,y_m) := c_0(w_0''x-z_0''y)^\lambda$. Since the set of $\overline{\mathcal{H}_+}^m$-stable polynomials is open in $V(\lambda)$, let $B(0)$ be some open ball centered at $0$ such that $q_0 + iB(0)$ consists of nonzero $\overline{\mathcal{H}_+}^m$-stable polynomials. So, for any $r_0 \in B(0)$, Lemma [\[rs_lemma\]](#rs_lemma){reference-type="ref" reference="rs_lemma"} implies $T(q_0) + iT(r_0)$ is either $\mathcal{H}_+^m$-stable, $\mathcal{H}_-^m$-stable, or zero. Hermite-Biehler then implies $T(r_0)$ is real stable or zero whenever $r_0 \in B(0) \cap V_\mathbb{R}(\lambda)$. Therefore, $T[V_\mathbb{R}(\lambda)]$ consists of real stable polynomials, and $(c)$ follows from Lemma [\[dim_lemma\]](#dim_lemma){reference-type="ref" reference="dim_lemma"}.

$(ii) \Rightarrow (i)$. If $(c)$ holds, then $(i)$ follows from Hermite-Biehler. Otherwise, suppose WLOG that $(a)$ holds. We can then use an argument similar in spirit to that of Lemma [\[bb_Clink\]](#bb_Clink){reference-type="ref" reference="bb_Clink"} to show that $T$ maps $\mathcal{H}_+^m$-stable polynomials to weakly $\mathcal{H}_+^m$-stable polynomials. Since $T$ restricts to a real operator, this implies $(i)$. ◻
:::

As in Lemma [\[bb_Clink\]](#bb_Clink){reference-type="ref" reference="bb_Clink"}, we use the previous lemma to link the characterizations of weak and strong stability preserving operators as follows. Applying the necessary maps to convert $\mathop{\mathrm{Symb}}(T)$ to $\mathop{\mathrm{Symb}}_{BB}(T)$ below gives essentially the characterization of weak real stability preserving operators given in Theorem [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"}.

::: corollary
[]{#bb_Rops label="bb_Rops"} Fix $\lambda,\alpha \in \mathbb{N}_0^m$ and a linear operator $T \in \mathop{\mathrm{Hom}}(V(\lambda),V(\alpha))$ such that $T$ restricts to a real linear operator from $V_\mathbb{R}(\lambda)$ to $V_\mathbb{R}(\alpha)$. The following are equivalent.

1.  $T$ preserves weak real stability.

2.  One of the following holds:

    1.  $\mathop{\mathrm{Symb}}(T)$ is $(\mathcal{H}_-^m \times \mathcal{H}_+^m)$-stable.

    2.  $\mathop{\mathrm{Symb}}(T)$ is $(\mathcal{H}_-^m \times \mathcal{H}_-^m)$-stable.

    3.  $T$ has image of dimension at most two, and is of the form $$T: p \mapsto q \cdot \psi_1(p) + r \cdot \psi_2(p)$$ where $q,r \in V_\mathbb{R}(\alpha)$ are weakly real stable such that $q \ll r$, and $\psi_1,\psi_2$ are real linear functionals.
:::

::: proof
*Proof.* Apply the complex characterization (Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"}) to conditions $(ii)(a)$ and $(ii)(b)$ of Lemma [\[bb_Rlink\]](#bb_Rlink){reference-type="ref" reference="bb_Rlink"} above. ◻
:::
