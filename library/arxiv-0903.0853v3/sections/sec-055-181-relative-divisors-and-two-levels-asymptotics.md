---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-055-181-relative-divisors-and-two-levels-asymptotics
section_title: "Relative divisors and two levels asymptotics"
section_number: 18.1
pages: 95-96
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.953
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:relativedivisorsandtwolevels label="subsection:relativedivisorsandtwolevels"}

Let $\Lambda^\prime$, $\Lambda$ be two divisors. Assume that $\Lambda^\prime < \Lambda$, meaning that $\Lambda^\prime = \sum\limits_{1\le i\le m}\nu_i^\prime[\lambda_i]$, that $\Lambda = \sum\limits_{1\le i\le m}\nu_i[\lambda_i]$, $0 \leq \nu_i^\prime \leq \nu_i$, $\nu_i > 0$ and that $\left |\Lambda \right |> \left |\Lambda^\prime \right |$.

::: defi
[]{#defi:diviseurrelatif label="defi:diviseurrelatif"} []{#not76 label="not76"} Let $\Lambda^\prime < \Lambda$ and let $F$ be a function defined and analytic in a neighborhood of each point of the spirals in the support of $\Lambda$ near $0$.

1.  We call *values of $F$ over the relative divisor $\Lambda/\Lambda^\prime$ at $0$*, and we write $(\Lambda/\Lambda^\prime)F(0)$, the $|\Lambda|-|\Lambda^\prime|$ (germs of) sequences: $$(\Lambda/\Lambda^\prime)F(0) :=
    \left\{\left(F^{(j)}(\lambda_i q^{-n})\right)_{n\gg 0} ~:~ 
    1 \leq i \leq m, \nu^\prime_i \leq j < \nu_i\right\}.$$

2.  We say that *$F$ has $q$-Gevrey order $k$ over $\Lambda/\Lambda^\prime$ at $0$* if all its values there constitute $q$-Gevrey sequences of order $k$.

3.  Let $\Lambda = \Lambda_1 + \Lambda_2$ and $\Lambda^\prime = \Lambda_1$. We write $F \in {\mathbb E}_{(\Lambda_1,\Lambda_2)}^{\Lambda}$ if $F$ is analytic in a neighborhood of $0$ punctured at $0$, has $q$-Gevrey order $|\Lambda|$ at $0$, has $q$-Gevrey order $|\Lambda_2|$ along $\Lambda/\Lambda_2$ at $0$ and has $q$-Gevrey order $0$ along $\Lambda_2$ at $0$.
:::

We get the following generalization of theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}.

::: prop
[]{#prop:deuxniveaux label="prop:deuxniveaux"} Let $\Lambda_1 <\Lambda =\Lambda_1 + \Lambda_2$. One has the following decompositions: $$\begin{aligned}
{\mathbb E}_{(\Lambda_1,\Lambda_2)}^{\Lambda} & = &
{\mathbb E}_0^{\Lambda_2} + \theta_{\Lambda_2}{\mathbb E}_0^{\Lambda_1}, \\
\left(\dfrac{1}{\theta_{\Lambda}}~{\mathbb E}_{(\Lambda_1,\Lambda_2)}^{\Lambda}\right) 
\cap {\mathbb B}^{\Lambda} & = &
{\mathbb A}_{q}^{\Lambda_1} + \dfrac{1}{\theta_{\Lambda_1}}~{\mathbb A}_{q}^{\Lambda_2}.
\end{aligned}$$
:::

::: proof
*Proof.* We shall only check the first decomposition, the second one following immediately with help of theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}.

Let $\Lambda_2 = \sum\limits_{i=1}^m\nu_i[\lambda_i]$, with $[\lambda_i] \not= [\lambda_{i'}]$ for $i \not= i'$. Let $F \in {\mathbb E}_{(\Lambda_1,\Lambda_2)}^\Lambda$. Since $F$ has $q$-Gevrey order $0$ over $\Lambda_2$ at zero, one gets the following Taylor expansion: $$\label{eqn:FTaylor}
F(z) = 
\sum_{n\gg0} \sum_{i=0}^m \sum_{j=0}^{\nu_i-1}
\dfrac{F^{(j)}(\lambda_iq^{-n})}{j!}~(z-\lambda_iq^{-n})^j+R_{\Lambda_2}(z)~,$$ where the convergence of these series for $n \gg 0$ comes from the fact that each sequence $\bigl(F^{(j)}(\lambda_i q^{-n})\bigr)_{n\gg0}$ is bounded. Let $f_2 := \dfrac{F}{\theta_{\Lambda_2}}$ and $F_1 := \dfrac{R_{\Lambda_2}}{\theta_{\Lambda_2}}$ and put $F_2 := \theta_{\Lambda_2}(f_2-F_1)$; one has $F =F_2 + \theta_{\Lambda_2}~F_1$ and $F_2$ is the function represented by the triple summation in the expansion [\[eqn:FTaylor\]](#eqn:FTaylor){reference-type="eqref" reference="eqn:FTaylor"}. After theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}, one has $(f_2 - F_1) \in {\mathbb A}_q^{\Lambda_2}$ and $F_2 \in {\mathbb E}_0^{\Lambda_2}$.

There remains to check that $F_1 \in {\mathbb E}_0^{\Lambda_1}$. First note that $R_{\Lambda_2}$ has order at least $\nu_i$ at each $z = \lambda_iq^{-n}$ for $n \gg 0$, which implies that $F_1$ represents a germ of analytic function in a punctured neighborhood of $z = 0$. Moreover, since the values of $F$ over the relative divisor $\Lambda/\Lambda_2$ at $0$ have $q$-Gevrey order $|\Lambda_2|$, the same is true for the function $R_{\Lambda_2}$ because $F_2$ has $q$-Gevrey order $|\Lambda_2|$ at zero. Using lemma [\[lemm:thetamin\]](#lemm:thetamin){reference-type="ref" reference="lemm:thetamin"}, one finds at last that $F_1 \in {\mathbb E}_0^{\Lambda_1}$, achieving the proof of the theorem. ◻
:::

Note that: $${\mathbb A}_{q}^{\Lambda_1} \subset 
{\mathbb A}_{q}^{\Lambda_1} + \dfrac{1}{\theta_{\Lambda_1}} {\mathbb A}_{q}^{\Lambda_2}~,$$ the inclusion being strict for a non trivial divisor $\Lambda_2$.
