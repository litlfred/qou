---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-022-62-comparison-of-non-semisimple-blocks-in-repsd
section_title: "Comparison of non-semisimple blocks in Rep(Sd; F)."
section_number: 6.2
pages: 39-40
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.898
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
In this section we show that for fixed $d\in\mathbb{Z}_{\geq0}$, the non-semisimple blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent as additive categories. Thereafter we conjecture that a restriction functor induces an equivalence of categories between certain non-semisimple blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ and $\underline{\operatorname{Re}}\!\operatorname{p}(S_{d-1}; F)$. First, let us fix some notation. Given a block $\mathcal{B}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$, let $\operatorname{Inc}_\mathcal{B}: \mathcal{B}\to\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ and $\operatorname{Proj}_\mathcal{B}: \underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)\to\mathcal{B}$ denote the inclusion and projection functors respectively.

::: proposition
[]{#blocksfixd label="blocksfixd"} Suppose $\mathcal{B}$ is a nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ which is not minimal with respect to $\prec$. There exists a block $\mathcal{B}'$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with $\mathcal{B}'\precneqq\mathcal{B}$ such that $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}:\mathcal{B}\to\mathcal{B}'$ is an equivalence of additive categories. Hence, all nontrivial blocks in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ are all equivalent as additive categories.
:::

::: proof
*Proof.* First, notice $d\not=0$ as we are assuming a nontrivial block exists in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. Hence, $\operatorname{Lift}_d(L(\Box))=L(\Box)$ (see Example [\[lift1\]](#lift1){reference-type="ref" reference="lift1"}(1)). Let $B=\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ denote the set of Young diagrams corresponding to indecomposable objects in $\mathcal{B}$. Now, let $B'=\{\rho^{(0)}\subset\rho^{(1)}\subset\cdots\}$ be the set of Young diagrams given by Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2), and $\mathcal{B}'$ the corresponding block. By Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"} we have the following $$\begin{array}{rcll}
\operatorname{Lift}_d(L(\lambda^{(0)})) & = & L(\lambda^{(0)}),\\
\operatorname{Lift}_d(L(\lambda^{(i)}))&=&L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})&(i>0),\\
\operatorname{Lift}_d(L(\rho^{(0)}))&=&L(\rho^{(0)}),\\
\operatorname{Lift}_d(L(\rho^{(i)}))&=&L(\rho^{(i)})\oplus L(\rho^{(i-1)})& (i>0).\\
\end{array}$$ Hence, by Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(1) and Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2), $$\begin{array}{rrcll}
\operatorname{Lift}_d(L(\lambda^{(i)})\otimes L(\Box))&=&\operatorname{Lift}_d(L(\lambda^{(i)}))\otimes L(\Box)&=&\operatorname{Lift}_d(L(\rho^{(i)}))\oplus A,\\
\operatorname{Lift}_d(L(\rho^{(i)})\otimes L(\Box))&=&\operatorname{Lift}_d(L(\rho^{(i)}))\otimes L(\Box)&=&\operatorname{Lift}_d(L(\lambda^{(i)}))\oplus B,\\
\end{array}$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ for all $i\geq0$, where $A$ (resp. $B$) is an object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ with no indecomposable summands of the form $L(\rho^{(j)})$ (resp. $L(\lambda^{(j)})$). Thus, by Propositions [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3) and [\[liftsim\]](#liftsim){reference-type="ref" reference="liftsim"}, $L(\lambda^{(i)})\otimes L(\Box)=L(\rho^{(i)})\oplus A'$ and $L(\rho^{(i)})\otimes L(\Box)=L(\lambda^{(i)})\oplus B'$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ for all $i\geq 0$, where $A'$ (resp. $B'$) is an object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ with no indecomposable summands of the form $L(\rho^{(j)})$ (resp. $L(\lambda^{(j)})$). Hence, $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}$ and $\operatorname{Proj}_\mathcal{B}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}'}$ are inverse to one another on objects. Moreover, since $(-\otimes L(\Box))$ is self-adjoint and $\operatorname{Proj}_\mathcal{B}$ is both right and left adjoint to $\operatorname{Inc}_{\mathcal{B}}$, it follows that $\operatorname{Proj}_\mathcal{B}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}'}$ is adjoint to $\operatorname{Proj}_{\mathcal{B}'}\circ(-\otimes L(\Box))\circ\operatorname{Inc}_{\mathcal{B}}$. The result follows. ◻
:::

Next, we use the universal property of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ (see [@Del07 8.3]) to define a restriction functor.

::: definition
Let $\underline{\operatorname{Res}}_{S_{t-1}}^{S_t}:\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)\to\underline{\operatorname{Re}}\!\operatorname{p}(S_{t-1}; F)$ denote the functor given by the universal property of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ which sends $([1], \text{id}_1)\mapsto([1], \text{id}_1)\oplus([0], \text{id}_0)$.
:::

::: conjecture
[]{#conjecture label="conjecture"} For $d\in\mathbb{Z}_{\geq0}$, let $\mathcal{B}_d$ denote the nontrivial block in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$ containing the object $L(\varnothing)$. Then the functor $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ induces an equivalence of additive categories $\mathcal{B}_{d+1}\cong\mathcal{B}_{d}$.
:::

::: remark
It is not hard to show that $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ is bijective on objects. Hence, to prove Conjecture [\[conjecture\]](#conjecture){reference-type="ref" reference="conjecture"} it suffices to show $\operatorname{Proj}_{\mathcal{B}_d}\circ\underline{\operatorname{Res}}_{S_d}^{S_{d+1}}\circ\operatorname{Inc}_{\mathcal{B}_{d+1}}$ is either full or faithful.
:::
