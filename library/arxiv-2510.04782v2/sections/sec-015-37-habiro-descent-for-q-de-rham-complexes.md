---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-015-37-habiro-descent-for-q-de-rham-complexes
section_title: "Habiro descent for q-de Rham complexes"
section_number: 3.7
pages: 48-50
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.964
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#subsec:qdeRhamHabiroDescent label="subsec:qdeRhamHabiroDescent"}

In this short subsection, we discuss to what extent the $q$-de Rham complex $\qdeRham_{R/A}$ can or cannot be descended to the Habiro ring. Let's start with the case that works.

::: prop
[]{#prop:Letaq-1 label="prop:Letaq-1"} Let $(S, \fil_{\qHodge}^\star\qdeRham_{S/A})\in \cat{AniAlg}_A^{\qHodge}$ be an object such that $S$ is a smooth $A$-algebra. Then:

::: alphanumerate
$\qOmega_{S/A}\simeq \qhatdeRham_{S/A}$ is the completion of $\qdeRham_{S/A}$ at the $q$-Hodge filtration $\fil_{\qHodge}^\star$.[]{#enum:qHodgeCompletion label="enum:qHodgeCompletion"}

We have $\L\eta_{(q-1)}\qHodge_{S/A}\simeq \qOmega_{R/A}$. In particular, $\L\eta_{(q-1)}\qHhodge_{S/A}$ is a Habiro descent of $\qOmega_{S/A}$.[]{#enum:Letaq-1 label="enum:Letaq-1"}
:::
:::

::: proof
*Proof.* We construct the equivalence $\qOmega_{S/A}\simeq \qhatdeRham_{S/A}$ using an arithmetic fracture square. Let us first construct an equivalence after $p$-completion for any prime $p$. Note that the canonical maps $\qdeRham_{S/A}\rightarrow \qOmega_{S/A}$ and $\qdeRham_{S/A}\rightarrow \qhatdeRham_{S/A}$ become equivalences after $p$-completion for any prime $p$. Indeed, this can be checked modulo $(q-1)$, where we recover the well-known fact $(\Omega_{S/A})_p^\complete\simeq (\deRham_{S/A})_p^\complete\simeq (\hatdeRham_{S/A})_p^\complete$. So we obtain the desired equivalence $(\qOmega_{S/A})_p^\complete\simeq (\qhatdeRham_{S/A})_p^\complete$.

Let us now construct the equivalence rationally. We know that $\deRham_{S/A}\lotimes_\IZ\IQ\rightarrow \Omega_{S/A}\lotimes_\IZ\IQ$ identifies the right-hand side with the completion of the left-hand side at the Hodge filtration. Consequently, $(\deRham_{S/A}\lotimes_\IZ\IQ)\qpower_{(\Hodge,q-1)}^\complete\simeq (\Omega_{S/A}\lotimes_\IZ\IQ)\qpower$, which yields the desired equivalence rationally. The data from [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}[\[enum:qHodgeRationalpComplete\]](#enum:qHodgeRationalpComplete){reference-type="ref" reference="enum:qHodgeRationalpComplete"} ensures that the $p$-complete and rational equivalences glue, which finishes the proof of [\[enum:qHodgeCompletion\]](#enum:qHodgeCompletion){reference-type="ref" reference="enum:qHodgeCompletion"}.

To prove [\[enum:Letaq-1\]](#enum:Letaq-1){reference-type="ref" reference="enum:Letaq-1"}, first observe that the natural map $\qdeRham_{S/A}\rightarrow \qHodge_{S/A}$ factors through the completion at the $q$-Hodge filtration, because each filtration step $\fil_{\qHodge}^i$ becomes divisible by $(q-1)^i$ in $\qHodge_{S/A}$ and $\qHodge_{S/A}$ is $(q-1)$-complete. Now consider the map of filtered objects $$\begin{tikzcd}[column sep=2em]
                \dotsb & \qhatdeRham_{S/A}\dar["(q-1)^2"]\eqar[l] & \qhatdeRham_{S/A}\dar["(q-1)"]\eqar[l] &  \fil_{\qHodge}^0\qhatdeRham_{S/A}\dar\lar["\simeq"'] &  \fil_{\qHodge}^1\qhatdeRham_{S/A}\dar\lar & \dotsb\lar\\
                \dotsb &\qHodge_{S/A}\lar & \qHodge_{S/A}\lar["(q-1)"'] & \qHodge_{S/A}\lar["(q-1)"'] & \qHodge_{S/A}\lar["(q-1)"'] & \dotsb\lar
            \end{tikzcd}$$ We claim that the top row is the connective cover of the bottom row in the Beilinson $t$-structure. If we can prove this, then [@BMS2 Proposition ] will show $\qhatdeRham_{S/A}\simeq \L\eta_{(q-1)}\qHodge_{S/A}$, hence $\qOmega_{S/A}\simeq \L\eta_{(q-1)}\qHodge_{S/A}$ by [\[enum:qHodgeCompletion\]](#enum:qHodgeCompletion){reference-type="ref" reference="enum:qHodgeCompletion"}, as desired. Since $\L\eta_{(q-1)}$ commutes with $(q-1)$-completion [@BMS1 Lemma ], we also deduce that $\L\eta_{(q-1)}\qHhodge_{S/A}$ is indeed a Habiro descent of $\qOmega_{S/A}$.

To show the claim, let us first verify that the top row is indeed connective in the Beilinson $t$-structure. We must show that $\gr_{\qHodge}^n\qdeRham_{S/A}$ is concentrated in cohomological degrees $\leqslant n$ for all $n$. If $n<0$, this is clear as then $\gr_{\qHodge}^n\qdeRham_{S/A}\simeq 0$. If $n\geqslant 0$, we have a finite-length filtration $$0\longrightarrow \gr^0_{\qHodge}\qdeRham_{S/A}\xrightarrow{(q-1)}\gr^1_{\qHodge}\qdeRham_{S/A}\xrightarrow{(q-1)}\dotsb \xrightarrow{(q-1)}\gr^n_{\qHodge}\qdeRham_{S/A}\,.$$ The $i$^th^ graded piece of this filtration is $\Sigma^{-i}\Omega_{S/A}^i$ by [\[lem:ConjugateFiltration\]](#lem:ConjugateFiltration){reference-type="ref" reference="lem:ConjugateFiltration"}, which is concentrated in cohomological degree $i$. Hence $\gr_{\qHodge}^n\qdeRham_{S/A}$ is indeed concentrated in cohomological degrees $\leqslant n$ and so the top row is Beilinson-connective.

Moreover, the argument shows that $\gr_{\qHodge}^n\qdeRham_{S/A}\rightarrow \qHodge_{S/A}/(q-1)$ induces an equivalence $\gr_{\qHodge}^n\qdeRham_{S/A}\simeq \tau^{\leqslant n}(\qHodge_{S/A}/(q-1))$. By [@BMS2 Theorem (2)], this shows that the map from the top row to the Beilinson-connective cover of the bottom row is an equivalence on associated gradeds. As both filtered objects are complete, we're done. ◻
:::

Let us now discuss what probably doesn't work.

::: rem
For an arbitrary object $(R,\fil_{\qHodge}^\star \qdeRham_{R/A})$ in $\cat{AniAlg}_A^{\qHodge}$, without a smoothness assumption on $R$, we don't know how to construct a Habiro descent of $\qdeRham_{R/A}$. A naive guess would be $$\limit_{m\in\IN}\qdeRham_{R/A}^{(m)}\left[\frac{ \fil_{\qHhodge_m}^i}{[m]_q^i}\ \middle|\ i\geqslant 0\right]_{(q^m-1)}^\complete\,,$$ but this object doesn't exist, since $\fil_{\qHhodge_m}^\star\qdeRham_{R/A}^{(m)}$ is only a filtered module over the filtered ring $(q^m-1)^\star A[q]$, but not necessarily over $[m]_q^\star A[q]$.
:::

::: rem
We also don't expect that the Habiro descent of $\qOmega_{S/A}$ in [\[prop:Letaq-1\]](#prop:Letaq-1){reference-type="ref" reference="prop:Letaq-1"} can be constructed without the datum of a $q$-Hodge filtration $\fil_{\qHodge}^\star\qdeRham_{S/A}$, let alone functorially in $S$. While it seems hard to get any definite no-go theorem, let us at least explain why the most natural attempt doesn't work.

In [\[rem:qOmegaHabiroDescent\]](#rem:qOmegaHabiroDescent){reference-type="ref" reference="rem:qOmegaHabiroDescent"}, we've explained an attempt to construct a filtration $\fil_{\L\eta}^\star \qOmega_{S/A}^{(m)}$: Each $\L\eta_{[m/d]_q}$ carries a natural filtration via [@BMS2 Proposition ]. If these filtrations could be glued to give the desired $\fil_{\L\eta}^\star$, we could attempt to construct a Habiro descent of $\qOmega_{S/A}$ via $$\limit_{m\in\IN}\qOmega_{S/A}^{(m)}\left[\frac{ \fil_{\L\eta}^i}{[m]_q^i}\ \middle|\ i\geqslant 0\right]_{(q^m-1)}^\complete\,.$$ However, the filtrations on $\L\eta_{[m/d]_q}$ *do not* glue. This can already be seen in the case $m=p$. In this case we have a pullback diagram $$\begin{tikzcd}
                \qOmega_{S/A}^{(p)}\rar\dar\drar[pullback] & \left(\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q]\right)_{[p]_q}^\complete\dar["\phi_{p/A[q]}"]\\
                \L\eta_{[p]_q}\qOmega_{S/A}\rar & \L\eta_{[p]_q}\left(\qOmega_{S/A}\right)_p^\complete
            \end{tikzcd}$$ The filtration on $\L\eta_{[1]_q}\simeq \id$ is trivial. But the trivial filtration on $(\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q])_{[p]_q}^\complete$ will not be compatible with the natural filtration on $\L\eta_{[p]_q}(\qOmega_{S/A})_p^\complete$, so gluing fails.

To make the gluing work, we should instead equip $(\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q])_{[p]_q}^\complete$ with a global version of the Nygaard filtration. But such a global Nygaard filtration likely doesn't exist. To see this, let's attempt to construct it via an arithmetic fracture square. On the $p$-completion $(\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q])_{(p,[p]_q)}^\complete$, we put the usual Nygaard filtration. In view of [\[lem:NygaardRationalisation\]](#lem:NygaardRationalisation){reference-type="ref" reference="lem:NygaardRationalisation"}, on the rationalisation we should put the combined Hodge and $[p]_q$-adic filtration. But then on the $\ell$-completion $(\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q])_{(\ell,[p]_q)}^\complete$ for any prime $\ell\neq p$, we would need to put a filtration that becomes the combined Hodge and $[p]_q$-adic filtration after $(-)[1/\ell]_{[p]_q}^\complete$.

It is entirely unclear (at least to the author) how to construct such a filtration, unless we're already given a $q$-Hodge filtration $\fil_{\qHodge}^\star\qdeRham_{S/A}$. This explains the need for the additional datum of $\fil_{\qHodge}^\star\qdeRham_{S/A}$.
:::
