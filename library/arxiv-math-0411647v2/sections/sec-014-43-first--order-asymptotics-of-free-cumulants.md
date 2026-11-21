---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-014-43-first--order-asymptotics-of-free-cumulants
section_title: "First--order asymptotics of free cumulants"
section_number: 4.3
pages: 31-33
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.85
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
::: theorem
[]{#theo:pierwszystopien label="theo:pierwszystopien"}

Let integers $k_1,\dots,k_t\geq 2$ be given and let us express $R^{\mathop{\mathrm{JM}}}_{k_1} \cdots R^{\mathop{\mathrm{JM}}}_{k_t}\in\mathfrak{P}$ as a linear combination of normalized conjugacy class indicators $\Sigma$. Then $$\begin{gathered}
\label{eq:highestorde} R^{\mathop{\mathrm{JM}}}_{k_1} \cdots
R^{\mathop{\mathrm{JM}}}_{k_t}=\Sigma_{k_1-1,\dots,k_t-1}+\\ \text{(terms of degree at
most } k_1+\cdots+k_t-2\text{)},
\end{gathered}$$ where the degree is taken with respect to the filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"}.
:::

::: proof
*Proof.* Let us consider the case $t=1$; we set $n=k_1$. Propositions [\[prop:genusowatosc\]](#prop:genusowatosc){reference-type="ref" reference="prop:genusowatosc"} and [\[prop:genuszero\]](#prop:genuszero){reference-type="ref" reference="prop:genuszero"} imply that the highest--order terms in the expansion [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"} correspond to non--crossing partitions and that the degree of all remaining terms will be at most $n-2$; by Theorem [\[theo:wiwatevercrossing\]](#theo:wiwatevercrossing){reference-type="ref" reference="theo:wiwatevercrossing"} a partition contributes in the sum [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"} only if it is evercrossing. In order to find the leading term we need to find all non--crossing partitions of the set $\{1,2,\dots,n\}$ which are at the same time evercrossing. This combination of adjectives sounds oxymoronic which suggests that there should not be too many of such partitions and indeed it is easy to check that the only such partition is the trivial one. Hence $$\begin{gathered}
R^{\mathop{\mathrm{JM}}}_n=\Sigma_{ \{ \{1\},\{2\},\dots,\{n\} \} }+\text{(terms of
degree at most } n-2\text{)} =
\\ \Sigma_{n-1} + \text{(terms of degree at most } n-2\text{)}
\end{gathered}$$ which finishes the proof of the case $t=1$.

The general case follows easily from Corollary [\[cor:filtration\]](#cor:filtration){reference-type="ref" reference="cor:filtration"}. ◻
:::

::: corollary
[]{#cor:algebraicallyfree label="cor:algebraicallyfree"} Elements $(R^{\mathop{\mathrm{JM}}}_k)_{k\geq 2}$ are algebraically free; also elements $(M^{\mathop{\mathrm{JM}}}_k)_{k\geq 2}$ are algebraically free and therefore the gradation [\[eq:gradation\]](#eq:gradation){reference-type="eqref" reference="eq:gradation"} is well--defined.
:::

::: proof
*Proof.* Let $P(x_2,x_3,\dots)\neq 0$ be a polynomial; our goal is to show that $P(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots)\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ is non--zero. In order to show this we express $P(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots)$ as a linear combination of conjugacy class indicators $\Sigma$ and Theorem [\[theo:pierwszystopien\]](#theo:pierwszystopien){reference-type="ref" reference="theo:pierwszystopien"} shows that the highest--order terms do not cancel.

In order to show that $(M^{\mathop{\mathrm{JM}}}_k)_{k\geq 2}$ are algebraically free we consider a polynomial $Q(x_2,x_3,\dots)\neq 0$. We apply [\[eq:momentkumulant\]](#eq:momentkumulant){reference-type="eqref" reference="eq:momentkumulant"} and obtain a polynomial $P(x_2,x_3,\dots)$ such that $Q(M^{\mathop{\mathrm{JM}}}_2,M^{\mathop{\mathrm{JM}}}_3,\dots)=P(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots)$. Equation [\[eq:definicjawolnejkumulanty\]](#eq:definicjawolnejkumulanty){reference-type="eqref" reference="eq:definicjawolnejkumulanty"} implies that $P(x_2,x_3,\dots)\neq 0$. It follows that $Q(M^{\mathop{\mathrm{JM}}}_2,M^{\mathop{\mathrm{JM}}}_3,\dots)=P(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots)\neq 0$. ◻
:::

The following result was proved in [@Biane1998; @IvanovOlshanski2002].

::: theorem
[]{#theo:kontrolastopnia label="theo:kontrolastopnia"} For every tuple $k_1,\dots,k_t$ of positive integers there exists a polynomial $K_{k_1,\dots,k_t}(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots)$, called Kerov polynomial, such that $$\Sigma_{k_1,\dots,k_t}=K_{k_1,\dots,k_t}(R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots).$$ In other words, each of the families $(R^{\mathop{\mathrm{JM}}}_n)_{n\geq 2}$, $(M^{\mathop{\mathrm{JM}}}_n)_{n\geq 2}$ and $(\Sigma_{k_1,\dots,k_m})_{k_1,\dots,k_m\geq 1}$ generates the same commutative algebra $\mathfrak{P}$.

With respect to the gradation [\[eq:gradation\]](#eq:gradation){reference-type="eqref" reference="eq:gradation"} the leading term of the Kerov polynomial is given by $$\begin{gathered}
\label{eq:eksplozjamozgu}
\Sigma_{k_1,\dots,k_t}=R^{\mathop{\mathrm{JM}}}_{k_1+1} \cdots R^{\mathop{\mathrm{JM}}}_{k_t+1} +\\
\text{(terms of degree at most $(k_1+1)+\cdots+(k_t+1)-2$)}
\end{gathered}$$ and $$\deg \Sigma_{k_1,\dots,k_t}=(k_1+1)+\cdots+(k_t+1).$$ In other words, the filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"} is induced by gradation [\[eq:gradation\]](#eq:gradation){reference-type="eqref" reference="eq:gradation"}.
:::

::: proof
*Proof.* We shall prove this theorem by induction over $(k_1+1)+\cdots+(k_t+1)$.

Let us express $\Sigma_{k_1,\dots,k_t}-R^{\mathop{\mathrm{JM}}}_{k_1+1} \cdots
R^{\mathop{\mathrm{JM}}}_{k_t+1}$ as a linear combination of normalized conjugacy class indicators $\Sigma$. Theorem [\[theo:pierwszystopien\]](#theo:pierwszystopien){reference-type="ref" reference="theo:pierwszystopien"} implies that with respect to the filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"} all these terms have degree at most $(k_1+1)+\cdots+(k_t+1)-2$ and hence the inductive hypothesis can be applied: every of these terms can be expressed by the corresponding Kerov polynomial. Observe that from the very definition of free cumulants [\[eq:definicjawolnejkumulanty\]](#eq:definicjawolnejkumulanty){reference-type="eqref" reference="eq:definicjawolnejkumulanty"} it follows that $\deg
R^{\mathop{\mathrm{JM}}}_{k_1+1} \cdots R^{\mathop{\mathrm{JM}}}_{k_t+1}=(k_1+1)+\cdots+(k_t+1)$ with respect to the gradation [\[eq:gradation\]](#eq:gradation){reference-type="eqref" reference="eq:gradation"} and hence the theorem follows. ◻
:::
