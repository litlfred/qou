---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-012-5-graces-theorem
section_title: "Grace's Theorem"
section_number: 5
pages: 14-15
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.989
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#graces_sect label="graces_sect"}

We now prove the multivariate homogeneous Grace's theorem for some specific projectively convex regions and then derive a few important corollaries. These corollaries will be almost immediate once Grace's theorem has been proven, and yet will quickly yield stronger results regarding linear operators in the next section.

In the usual proof of the classical univariate Grace's theorem, reference to linear factors of $f \in \mathbb{C}^n[x]$ is necessary. This makes generalization to $\mathbb{C}^\lambda[x_1,\ldots,x_m]$ difficult, as multivariate polynomials do not necessarily have any linear factors. In our new proof, we are able avoid reference to linear terms by using particular features of the $D$ map. This means that our proof method works for any $\lambda$.

::: theorem
[]{#graces_thm label="graces_thm"} Fix $\lambda \in \mathbb{N}_0^m$ and $p,q \in V(\lambda)$. Also, denote $C := \mathcal{H}_+\cup \overline{\mathbb{R}_+}$ and $\widetilde{C} := \mathcal{H}_-\cup \overline{\mathbb{R}_-}$, where the closures are considered to be in $\mathbb{CP}^1$. If $p$ is $C^m$-stable and $q$ is $\widetilde{C}^m$-stable, then $D^\lambda(p \otimes q) \neq 0$.
:::

::: proof
*Proof.* We prove the theorem by induction on degree. For $\lambda \equiv 0$, the result is obvious. For $|\lambda| \geq 1$, we can assume WLOG that $\lambda_1 \geq 1$ by permuting the variables. Define $\delta_1 := (1,0,0,\ldots,0) \in \mathbb{N}_0^m$.

Since $C$ and $\widetilde{C}$ are projectively convex, Corollary [\[laguerre_cor\]](#laguerre_cor){reference-type="ref" reference="laguerre_cor"} implies $(a\partial_{x_1} + b\partial_{y_1})p$ is $C^m$-stable for all $(a:b) \in C$ and $(c\partial_{x_1} + d\partial_{y_1})q$ is $\widetilde{C}^m$-stable for all $(c:d) \in \widetilde{C}$. To obtain a contradiction, we assume $D^\lambda(p \otimes q) = 0$. For $\alpha \in \mathcal{H}_+\cup \mathbb{R}_+ \subset C$ (equivalently, $-\alpha \in \mathcal{H}_-\cup \mathbb{R}_- \subset \widetilde{C}$), this gives: $$\begin{split}
            D^{\lambda-\delta_1}\big((\alpha \partial_{x_1} + \partial_{y_1})p \otimes (\alpha \partial_{x_1} - \partial_{y_1})q\big) &= \alpha^2 D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q) - D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q) - \alpha D^\lambda(p \otimes q) \\
                &= \alpha^2 D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q) - D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q)
        \end{split}$$ By induction and the stability properties discussed above, we have $D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q) \neq 0$, $D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q) \neq 0$, and $D^{\lambda-\delta_1}\big((\alpha \partial_{x_1} + \partial_{y_1})p \otimes (\alpha \partial_{x_1} - \partial_{y_1})q\big) \neq 0$. This implies: $$\alpha^2 D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q) - D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q) \neq 0 \Longrightarrow \alpha^2 \neq \frac{D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q)}{D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q)} \in \mathbb{C}\setminus \{0\}$$ However, we can pick $\alpha \in \mathcal{H}_+\cup \mathbb{R}_+$ such that $\alpha^2$ is any value of $\mathbb{C}\setminus \{0\}$ we want, including that of $\frac{D^{\lambda-\delta_1}(\partial_{y_1} p \otimes \partial_{y_1} q)}{D^{\lambda-\delta_1}(\partial_{x_1} p \otimes \partial_{x_1} q)}$. This contradiction gives the result. ◻
:::
