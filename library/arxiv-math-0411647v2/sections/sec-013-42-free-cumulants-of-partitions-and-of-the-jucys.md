---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-013-42-free-cumulants-of-partitions-and-of-the-jucys
section_title: "Free cumulants of partitions and of the Jucys--Murphy element"
section_number: 4.2
pages: 27-31
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.863
latex_coverage_ratio: 0.72
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
### Moments and cumulants of partitions {#sec:momentypartycji}

Let $X$ be an ordered set. We define the moment $M^{\mathop{\mathrm{P}}}_X$ (where the letter $\mathop{\mathrm{P}}$ stands for partition) by $$M^{\mathop{\mathrm{P}}}_X=\sum_{\sigma\in\mathop{\mathrm{P}}(X)} \sigma,$$ where the sum denotes a formal linear combination and it runs over all partitions of $X$.

Let $\rho=\{\rho_1,\dots,\rho_r\}$ be a non--crossing partition. Motivated by [\[eq:momentmap\]](#eq:momentmap){reference-type="eqref" reference="eq:momentmap"} we define $$M^{\mathop{\mathrm{P}}}_\rho=\prod_{s}  M^{\mathop{\mathrm{P}}}_{\rho_s}=\sum_{\sigma^1,\dots,\sigma^r} \prod_s \sigma^s,$$ where the sum runs over all tuples $(\sigma^1,\dots,\sigma^r)$ such that $\sigma^s$ is a partition of the set $\rho_s$ and products denote $\rho$--ordered products of partitions.

::: proposition
[]{#prop:formulanamomentypartycji label="prop:formulanamomentypartycji"} For every non--crossing partition $\rho$ of the set $X$ we have $$\label{eq:momentpartition} M^{\mathop{\mathrm{P}}}_\rho=\sum_{\sigma\geq
\rho_{{\mathop{\mathrm{comp}}^{-1}}}} \sigma,$$ where the sum runs over all partitions $\sigma$ of the set $X$ such that $\sigma\geq \rho_{{\mathop{\mathrm{comp}}^{-1}}}$.
:::

::: proof
*Proof.* Probably the best way to prove the proposition is to consider the graphical description of the partition multiplication from Section [\[subsec:geometricmultiplication\]](#subsec:geometricmultiplication){reference-type="ref" reference="subsec:geometricmultiplication"}. We present an alternative proof below.

From the very definition of multiplication one can see that every partition $\sigma$ which appears in $M^{\mathop{\mathrm{P}}}_\rho$ must fulfill $\sigma\geq \rho_{{\mathop{\mathrm{comp}}^{-1}}}$.

To any partition $\sigma$ of the set $X$ we can assign a tuple $(\sigma^1,\dots,\sigma^r)$, where $\sigma^s$ (a partition of the set $\rho_s$) is obtained from $\sigma$ by restriction to the set $\rho_s$. Now it is easy to observe that every $\sigma\geq
\rho_{{\mathop{\mathrm{comp}}^{-1}}}$ appears exactly once in $\prod_s M^{\mathop{\mathrm{P}}}_{\rho_s}$, namely in the factor $\prod_s \sigma^s$. ◻
:::

The moment map $M^{\mathop{\mathrm{P}}}$ gives rise to a sequence of free cumulants which will be denoted by $R^{\mathop{\mathrm{P}}}_n$.

### Moments and cumulants of Jucys--Murphy element {#subsec:momentmap}

Inspired by [\[eq:momentmappa\]](#eq:momentmappa){reference-type="eqref" reference="eq:momentmappa"} we shall denote by $M^{\mathop{\mathrm{JM}}}_\rho$ the partition--indexed moments of the Jucys--Murphy element, defined by $$\label{eq:momentmap} M^{\mathop{\mathrm{JM}}}_{\rho}=\prod_{1\leq s\leq r}
M^{\mathop{\mathrm{JM}}}_{|\rho_s|}=\prod_{1\leq s\leq r}
{\mathbb{E}}(J^{|\rho_s|})\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}}),$$ where $\rho=\{\rho_1,\dots,\rho_r\}$ is a non--crossing partition. The moment map $M^{\mathop{\mathrm{JM}}}$ gives rise to a sequence of free cumulants which will be denoted by $R^{\mathop{\mathrm{JM}}}_n$. Please note that $M^{\mathop{\mathrm{JM}}}_1={\mathbb{E}}(J)=0$ and therefore also $R^{\mathop{\mathrm{JM}}}_1=0$.

### The relation between the partitions and the Jucys--Murphy element

The following Claim provides a link between the moments of the Jucys--Murphy element and the moments of partitions.

::: claim
[]{#claim:dobryjurcysmurphy label="claim:dobryjurcysmurphy"} Let $X$ be a finite ordered set, let $\rho$ be a non--crossing partition of a finite ordered set and $n\geq 1$ be an integer. Then $$\begin{aligned}
 \label{eq:claim1} \Sigma(M^{\mathop{\mathrm{P}}}_{X}) &=M^{\mathop{\mathrm{JM}}}_{|X|}, \\
\label{eq:claim2} \Sigma(M^{\mathop{\mathrm{P}}}_\rho)&=M^{\mathop{\mathrm{JM}}}_\rho, \\
\label{eq:claim3} \Sigma(R^{\mathop{\mathrm{P}}}_n)&=R^{\mathop{\mathrm{JM}}}_n, 
\end{aligned}$$ where $\Sigma$ is the map considered in Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"}.
:::

We postpone the proof of [\[eq:claim1\]](#eq:claim1){reference-type="eqref" reference="eq:claim1"} to Theorem [\[theo:zgodnoscpartycjizjurcysiem\]](#theo:zgodnoscpartycjizjurcysiem){reference-type="ref" reference="theo:zgodnoscpartycjizjurcysiem"}. Equation [\[eq:claim1\]](#eq:claim1){reference-type="eqref" reference="eq:claim1"} implies [\[eq:claim2\]](#eq:claim2){reference-type="eqref" reference="eq:claim2"} immediately because $\Sigma$ is a homomorphism. Equation [\[eq:claim3\]](#eq:claim3){reference-type="eqref" reference="eq:claim3"} is an immediate consequence of [\[eq:claim2\]](#eq:claim2){reference-type="eqref" reference="eq:claim2"}.

This result implies that all questions about the moments of the Jucys--Murphy element can be easily translated into questions about moments of partitions and the machinery of Section [\[sec:calculus\]](#sec:calculus){reference-type="ref" reference="sec:calculus"} can be applied.

### Free cumulants of partitions

::: proposition
For every $n\geq 1$ $$\label{eq:kumulantypartycji} R^{\mathop{\mathrm{P}}}_n=\sum_{\pi\in\mathop{\mathrm{P}}(1,2,\dots,n)}
I_{\pi} \  \pi,$$ $$\label{eq:kumulantypartycji2} R^{\mathop{\mathrm{JM}}}_n=\sum_{\pi\in\mathop{\mathrm{P}}(1,2,\dots,n)}
I_{\pi} \  \Sigma_\pi,$$ where $I_{\pi}\in{\mathbb{Z}}$, called free index of $\pi$, is defined by $$\label{eq:formulanakrotnosc}
I_{\pi}=\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(1,2,\dots,n) \\ \rho\leq \pi}}
\mathop{\mathrm{Moeb}}_{\rho}.$$
:::

::: proof
*Proof.* From [\[eq:definicjawolnejkumulanty\]](#eq:definicjawolnejkumulanty){reference-type="eqref" reference="eq:definicjawolnejkumulanty"} and [\[eq:momentpartition\]](#eq:momentpartition){reference-type="eqref" reference="eq:momentpartition"} it follows that $$\begin{gathered}
R^{\mathop{\mathrm{P}}}_n=\sum_{\rho\in\mathop{\mathrm{NC}}(1,2,\dots,n)} \mathop{\mathrm{Moeb}}_{\rho_{\mathop{\mathrm{comp}}}}
\sum_{\substack{\pi\in\mathop{\mathrm{P}}(1,2,\dots,n)\\ \pi\geq \rho_{\mathop{\mathrm{comp}}}} }
\pi=\\
\sum_{\pi\in\mathop{\mathrm{P}}(1,2,\dots,n)} \pi
\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(1,2,\dots,n) \\ \rho_{\mathop{\mathrm{comp}}} \leq \pi}}
\mathop{\mathrm{Moeb}}_{\rho_{\mathop{\mathrm{comp}}}}= \sum_{\pi\in\mathop{\mathrm{P}}(1,2,\dots,n)} \pi
\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(1,2,\dots,n) \\ \rho \leq \pi}}
\mathop{\mathrm{Moeb}}_{\rho},
\end{gathered}$$ where in the last equality we used the fact that $\rho\mapsto\rho_{\mathop{\mathrm{comp}}}$ is a permutation of the set of non--crossing partitions.

The second identity [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"} follows now from Claim [\[claim:dobryjurcysmurphy\]](#claim:dobryjurcysmurphy){reference-type="ref" reference="claim:dobryjurcysmurphy"}. ◻
:::

### Evercrossing partitions

We say that a partition $\pi$ of a finite ordered set $X$ is evercrossing if for any $a<c$ ($a,c\in X$) such that $a$ is connected with $c$ by $\pi$ there exist $b,d\in X$ such that

1.  elements $a,b,c,d$ are ordered up to a cyclic rotation, i.e. either $a<b<c<d$ or $d<a<b<c$,

2.  elements $b$ and $d$ are connected by $\pi$,

3.  elements $a,b,c,d$ are not elements of the same block of $\pi$.

Up to some technical details, this means that on the graphical representation of $\pi$ every line connecting a pair of elements must be crossed by some other line. For example, partition from Figure [1](#fig:evercrossing){reference-type="ref" reference="fig:evercrossing"} is evercrossing, but partition from Figure [\[fig:przecinajacapartycja\]](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} is not.

![Example of an evercrossing partition](figure16.eps){#fig:evercrossing}

The following result shows that only evercrossing partitions contribute to sums [\[eq:kumulantypartycji\]](#eq:kumulantypartycji){reference-type="eqref" reference="eq:kumulantypartycji"} and [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"}.

::: theorem
[]{#theo:wiwatevercrossing label="theo:wiwatevercrossing"} If a partition $\pi$ is not evercrossing then $I_{\pi}=0$.
:::

In order to prove this result we will need the following lemma.

::: lemma
[]{#lem:fundamentalny label="lem:fundamentalny"} Let $\pi=\{\pi_1,\dots,\pi_r\}$ be a partition of $X$. Let $\sigma=\{\pi_1,\dots,\pi_s\}$, $\tau=\{\pi_{s+1},\dots,\pi_r\}$ be a decomposition of $\pi$ into two partitions of disjoint sets $S=\pi_1\cup\cdots\cup\pi_s$ and $T=\pi_{s+1}\cup\cdots\cup\pi_{r}$ such that $\sigma$ is non--crossing.

For $\rho\in\mathop{\mathrm{NC}}(T)$ we shall denote (with a small abuse of notation) by $\rho_{\mathop{\mathrm{comp}}}\in\mathop{\mathrm{NC}}(S)$ the biggest non--crossing partition with a property that $\rho\cup\rho_{\mathop{\mathrm{comp}}}$ is non--crossing. We denote by $\sigma\wedge\rho_{\mathop{\mathrm{comp}}}\in\mathop{\mathrm{NC}}(S)$ the biggest non--crossing partition which is smaller both than $\sigma$ and $\rho_{\mathop{\mathrm{comp}}}$.

Then the free index of $\pi$ is given by $$\label{eq:uproszczeniekumulanty}
I_{\pi}=\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(T)\\ \rho\leq \tau
\\ (\sigma \wedge \rho_{\mathop{\mathrm{comp}}}) \text{ is trivial}  }}
  \mathop{\mathrm{Moeb}}_{\rho}.$$
:::

::: proof
*Proof.* Since every $\rho\in\mathop{\mathrm{NC}}(X)$, $\rho\leq \pi$ can be decomposed as $\rho=\tilde{\rho}\cup\hat{\rho}$, where $\tilde{\rho}\in\mathop{\mathrm{NC}}(S)$, $\tilde{\rho}\leq \sigma$ and $\hat{\rho}\in\mathop{\mathrm{NC}}(T)$, $\hat{\rho}\leq
\tau$ it follows from [\[eq:formulanakrotnosc\]](#eq:formulanakrotnosc){reference-type="eqref" reference="eq:formulanakrotnosc"} that $$I_{\pi}=\sum_{\substack{\hat{\rho}\in \mathop{\mathrm{NC}}(T)\\ \hat{\rho}\leq \tau}}  \mathop{\mathrm{Moeb}}_{\hat{\rho}}
\Big( \sum_{\substack{  \tilde{\rho}\in \mathop{\mathrm{NC}}(S) \\ \tilde{\rho} \leq
(\sigma\wedge \hat{\rho}_{\mathop{\mathrm{comp}}}) }} \mathop{\mathrm{Moeb}}_{\tilde{\rho}} \Big).$$ We apply Lemma [\[lem:pocomoebius\]](#lem:pocomoebius){reference-type="ref" reference="lem:pocomoebius"} and observe that the second sum is equal to zero unless $\sigma\wedge\hat{\rho}_{\mathop{\mathrm{comp}}}$ is trivial; otherwise it is equal to $1$. ◻
:::

::: proof
*Proof of Theorem [\[theo:wiwatevercrossing\]](#theo:wiwatevercrossing){reference-type="ref" reference="theo:wiwatevercrossing"}.* Let $a,c$ be the vertices which have the property required for $\pi=\{\pi_1,\dots,\pi_r\}$ not to be evercrossing. By a change of numbering of blocks we can always assume that $a,c\in\pi_1$. Following the notation of Lemma [\[lem:fundamentalny\]](#lem:fundamentalny){reference-type="ref" reference="lem:fundamentalny"} we set $S=\pi_1$, $T=\pi_2\cup\cdots\cup\pi_r$, $\sigma=\{\pi_1\}$, $\tau=\{\pi_2,\dots,\pi_r\}$.

Observe that for every ${\rho}\in\mathop{\mathrm{NC}}(T)$ such that ${\rho}\leq
\tau$, we have that the partition ${\rho} \cup \big\{ \{a,c\}
\big\}$ is non--crossing, therefore ${\rho}_{\mathop{\mathrm{comp}}}\geq
\big\{\{a,c\} \big\}$ and ${\rho}_{\mathop{\mathrm{comp}}} \wedge \sigma \geq
\big\{\{a,c\} \big\}$ must contain a non--trivial block and the sum in [\[eq:uproszczeniekumulanty\]](#eq:uproszczeniekumulanty){reference-type="eqref" reference="eq:uproszczeniekumulanty"} contains no summands. ◻
:::

::: remark
The converse implication is not true, as one can see on an example from Figure [2](#fig:kontrprzyklad){reference-type="ref" reference="fig:kontrprzyklad"}.

![Example of an evercrossing partition with the free index equal to $0$.](figure17.eps){#fig:kontrprzyklad}
:::
