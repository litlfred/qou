---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-013-51-group-algebras
section_title: "Group algebras"
section_number: 5.1
pages: 18-19
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.918
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
We first consider group von Neumann algebras. This case was (essentially) discussed in [@NateTaka Section 15], but we include all proofs for reader's convenience.

Let $\Gamma$ be a discrete group. Let $\pi\colon \Gamma \to \mathcal{U}(H)$ be a unitary representation and $b\colon \Gamma \to H$ a 1-cocycle for $\pi$ in the sense that $b(xy)=b(x)+\pi_xb(y)$ for all $x,y\in \Gamma$. Consider left and right actions of $\Gamma$ on $H\otimes \ell^2(\Gamma)$ given by $\pi_x \otimes \lambda_x$ and $1\otimes \rho_y$ for all $x,y\in \Gamma$ respectively. Then using the canonical basis $(\delta_x)_{x\in \Gamma}$ for $\ell^2(\Gamma)$, one can construct a closable derivation by $$\partial\colon \mathbb{C}[\Gamma] \to H\otimes \ell^2(\Gamma); \ \partial(x)=b(x)\otimes e_x, \quad x\in \Gamma.$$ As above, put $\mathcal{A}:=\mathbb{C}[\Gamma]$ and define $S\colon \mathcal{A}\to H\otimes \ell^2(\Gamma)$ by $S e_x := \partial(x)\|\partial(x)\|^{-1}$ (and put $Se_x =\xi\otimes e_x$ for any fixed unit vector $\xi \in H$ if $\partial(x)=0$). Recall that $b$ is **proper** if $\|b(g)\|\to0$ whenever $g\to \infty$. In this setting, we prove the following.

::: prop
Suppose that $b$ is proper and that $\pi$ is weakly contained in the left regular representation. Then $\partial$ and $S$ satisfy all the assumptions in Proposition [\[Prop=Action\]](#Prop=Action){reference-type="ref" reference="Prop=Action"}.
:::

::: proof
*Proof.* Since $S$ is an isometry, Assumption 2 is trivially satisfied. Since $\pi \prec \lambda$, it holds that the representation $\Gamma \times \Gamma \ni (x,y )\mapsto \pi_x\otimes \lambda_x\rho_y$ is weakly contained in the one of $\Gamma \times \Gamma \ni (x,y )\mapsto \lambda_x\otimes \lambda_x\rho_y$, which is in turn unitarily equivalent to $\Gamma \times \Gamma \ni (x,y )\mapsto \pi_x\otimes \rho_y$ via the unitary $e_x\otimes e_y \mapsto e_x \otimes e_{xy}$ on $\ell^2(\Gamma) \otimes \ell^2(\Gamma)$. We conclude that $H\otimes \ell^2(\Gamma)$ is weakly contained in the coarse bimodule as $\mathcal{A}$-$\mathcal{A}$ bimodules.

It remains to show that $T_{x,y}$ is compact for all $x,y\in \mathcal A$. For this we can assume $x,y\in \Gamma$. Using Lemma [\[Lem=OrderEstimate\]](#Lem=OrderEstimate){reference-type="ref" reference="Lem=OrderEstimate"} below and using the properness of $b$, one has $\|T_{x,y} (e_g)\| \to 0$ as $g \to \infty$. Observe that $T_{x,y} (e_g) \in  H\otimes \mathbb{C}e_{xgy}$, hence $T_{x,y}^*T_{x,y} \in \ell^\infty(\Gamma)$, so $T_{x,y}^* T_{x,y} \in c_0(\Gamma)$. We conclude that $T_{x,y}$ is compact. ◻
:::

::: lem
[]{#Lem=OrderEstimate label="Lem=OrderEstimate"} For every $\gamma_1, \gamma_2 \in \Lambda$, there is a constant $C_{\gamma_1,\gamma_2}>0$ such that $$\Vert T_{\gamma_1, \gamma_2}(\mu) \Vert \leqslant C_{\gamma_1, \gamma_2} \Vert \partial(\mu) \Vert^{-1}.$$
:::

::: proof
*Proof.* We have, $$\label{Eqn=TxyEstimate}
    \begin{split}
       T_{\gamma_1, \gamma_2}(\mu) = & \Vert \partial(\mu) \Vert^{-1} \gamma_1 \partial(\mu) \gamma_2 -   \Vert \partial(\gamma_1 \mu \gamma_2) \Vert^{-1}  \partial(\gamma_1 \mu \gamma_2)  \\
            =   &  ( \Vert \partial(\mu) \Vert^{-1}  -
            \Vert \partial(\gamma_1 \mu \gamma_2) \Vert^{-1}) \gamma_1 \partial(\mu) \gamma_2
            -       
            \Vert \partial(\gamma_1 \mu \gamma_2) \Vert^{-1} ( \gamma_1  \partial(\mu) \gamma_2 +  \gamma_1    \mu  \partial(\gamma_2) ). \\
    \end{split}$$ We have that, $$\Vert \partial(\gamma_1 \mu \gamma_2) \Vert -   \Vert \partial( \mu ) \Vert \leqslant   \Vert   \partial( \gamma_2) \Vert + \Vert   \partial( \gamma_1) \Vert,$$ so $$\Vert \partial(\mu) \Vert^{-1}  - \Vert \partial(\gamma_1 \mu \gamma_2) \Vert^{-1} \leqslant \frac{\Vert   \partial( \gamma_2) \Vert + \Vert   \partial( \gamma_1) \Vert }{ \Vert \partial(\gamma_1 \mu \gamma_2) \Vert     \Vert \partial( \mu ) \Vert},$$ converges to 0 with order $O(\Vert \partial(\mu) \Vert^{-2})$ as $\partial$ is proper. We conclude that $\Vert T_{\gamma_1, \gamma_2}(\mu) \Vert$ converges to 0 with order $O(\Vert \partial(\mu) \Vert^{-1})$. ◻
:::
