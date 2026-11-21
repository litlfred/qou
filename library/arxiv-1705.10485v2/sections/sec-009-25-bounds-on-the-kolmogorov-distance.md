---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-009-25-bounds-on-the-kolmogorov-distance
section_title: "Bounds on the Kolmogorov distance"
section_number: 2.5
pages: 17-18
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.947
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#sec:berry label="sec:berry"} We are now ready to get an estimate for the Komogorov distance under a zone of control hypothesis.

::: theorem
[]{#thm:kolmogorov label="thm:kolmogorov"} Fix a reference stable distribution $\phi_{c,\alpha,\beta}$ and consider a sequence $(X_n)_{n \in \mathbb{N}}$ of random variables with a zone of control $[-K(t_n)^\gamma,K(t_n)^\gamma]$ of *index* $(v,w)$. Assume in addition that $\gamma \leq \tfrac{v-1}{\alpha}$. As before, we denote $Y$ a random variable with law $\phi_{c,\alpha,\beta}$, and $Y_n$ the renormalization of $X_n$ as in Proposition [\[prop:clt\]](#prop:clt){reference-type="ref" reference="prop:clt"}. Then, there exists a constant $C(\alpha,c,v,K,K_1)$ such that $$d_\mathrm{Kol}(Y_n,Y) \leq C(\alpha,c,v,K,K_1)\,
\frac{1}{(t_n)^{1/\alpha+\gamma}}.$$ The constant $C(\alpha,c,v,K,K_1)$ is explicitly given by $$\min_{\lambda>0} \left(\frac{1+\lambda}{\alpha \pi\,c}\left(\frac{2^\frac{v}{\alpha}\,\Gamma(\frac{v}{\alpha})\,K_1}{c^{v-1}} + \frac{\Gamma(\frac{1}{\alpha})}{\sqrt[3]{\pi}\,K }\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\right).$$
:::

Note that the additional hypothesis $\gamma \leq \tfrac{v-1}{\alpha}$ can always be ensured by decreasing $\gamma$ (but this makes the resulting bound weaker).

::: proof
*Proof.* We apply Proposition [\[prop:zonedistribution\]](#prop:zonedistribution){reference-type="ref" reference="prop:zonedistribution"} with the smooth test distributions $f_n=f_{a,\varepsilon_n}$, with $\varepsilon_n:=\tfrac{1}{K\,(t_n)^{1/\alpha+\gamma}}$; we know that $\|\partial f_n\|_{\mathrm{L}^1}=1$ and that $\widehat{f_n}$ is supported by the zone $[-K(t_n)^{1/\alpha+\gamma},K(t_n)^{1/\alpha+\gamma}]$, so that $$\left|\mathbb{E}[f_{a,\varepsilon_n}(Y_n)]-\mathbb{E}[f_{a,\varepsilon_n}(Y)]\right|\leq C_2(c,\alpha,v)\,\frac{K_1}{(t_n)^{v/\alpha}} \leq \frac{2^\frac{v}{\alpha}\,\Gamma(\frac{v}{\alpha})\,K_1\,K}{\alpha\pi\,c^v}\,\varepsilon_n.$$ This allows to apply Theorem [\[theorem:tao\]](#theorem:tao){reference-type="ref" reference="theorem:tao"} with a constant $$B = \frac{2^\frac{v}{\alpha}\,\Gamma(\frac{v}{\alpha})\,K_1\,K}{\alpha\pi\,c^v},$$ and with $\varepsilon=\varepsilon_n = \tfrac{1}{K\,(t_n)^{1/\alpha+\gamma}}$. Indeed, note that the density of the law of $Y$ is bounded by $$m=\frac{1}{2\pi}\|\E^{\eta(\I\xi)}\|_{\mathrm{L}^1}=\frac{1}{\alpha\pi\,c}\,\,\Gamma\!\left(\frac{1}{\alpha}\right).\qquad\qed$$ ◻
:::

::: remark
Suppose $\alpha=2$, $c = \frac{1}{\sqrt{2}}$ (mod-Gaussian convergence), and $v=w=3$. The maximal value allowed for the exponent $\gamma$ in the size of the zone of control is then $\gamma = 1$, and later we shall encounter many examples of this situation. Then, we obtain $$d_\mathrm{Kol}(Y_n,Y) \leq \frac{1+\lambda}{\sqrt{2 \pi}}\left(2^\frac{3}{2}\,K_1 + \frac{1}{\sqrt[3]{\pi}\,K }\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\frac{1}{(t_n)^{3/2}}.
  \label{eq:dKol_MG}$$ In Section [\[sec:dependency\]](#sec:dependency){reference-type="ref" reference="sec:dependency"}, we shall give conditions on cumulants of random variables that lead to mod-Gaussian convergence with a zone of control of size $O(t_n)$ and with index $(3,3)$, so that [\[eq:dKol_MG\]](#eq:dKol_MG){reference-type="eqref" reference="eq:dKol_MG"} holds. We shall then choose $K$, $K_1$ and $\lambda$ to make the constant in the right-hand side as small as possible.
:::

::: remark
In the general case, taking $\lambda=\frac{1}{2}$ in Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"} leads to the inequality $$d_\mathrm{Kol}(Y_n,Y) \leq C_3(\alpha,c,v,K_1,K)\,\frac{1}{(t_n)^{1/\alpha +\gamma}},$$ where $C_3(\alpha,c,v,K_1,K) = \frac{3}{2\pi\,\alpha\,c}\left(\frac{2^{\frac{v}{\alpha}}\,\Gamma(\frac{v}{\alpha})\,K_1}{c^{v-1}}+\frac{7\,\Gamma(\frac{1}{\alpha})}{K}\right)$.
:::
