---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-020-52-pushing-partitions
section_title: "Pushing partitions"
section_number: 5.2
pages: 46-53
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.983
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
In this article we are concerned mostly with conjugacy classes of permutations and not permutations themselves. For this reason we need a method to enumerate in the sums similar to [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"} not the individual summands, but whole classes of summands (summands within each class will be conjugate). Pushing partitions will turn out to be the suitable objects to enumerate such classes.

We say that a partition $\pi$ of a finite ordered set $X$ (by changing the labels we can assume that $X=\{1,\dots,n\}$) is a pushing partition if no neighbors $l$ and $l+1$ are connected by $\pi$ for $1\leq l\leq n$. It is useful to arrange numbers $1,\dots,n$ in a circle, therefore the case $l=n$ should be understood that neighbors $n$ and $1$ are not connected by $\pi$. In particular, it cannot happen that $n=1$.

We say that ${\mathbf{p}}\sim\pi$ if $\pi$ is a partition of $\{1,\dots,n\}$ for some $n\in{\mathbb{N}}$ and ${\mathbf{p}}=(p_1,\dots,p_n)$ is a sequence of length $n$ such that for every $1\leq l,m\leq n$ numbers $l$ and $m$ are connected by $\pi$ iff $p_l=p_m$. For every pushing sequence ${\mathbf{p}}$ there exists a unique pushing partition $\pi$ such that ${\mathbf{p}}\sim\pi$.

### Explicit form of the maps $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ and $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}$ {#subsec:explicit}

Let a pushing partition $\pi=\{\pi_1,\dots,\pi_r\}$ of the set $\{1,2,\dots,n\}$ be given. To every block $\pi_s$ of the partition we assign a label $\min
\pi_s$, i.e. the smallest element of $\pi_s$. To every element of $\{1,2,\dots,n\}$ we assign the label of the block it belongs to. In this way we constructed a sequence ${\mathbf{p}}=(p_1,\dots,p_n)$ such that ${\mathbf{p}}\sim \pi$. We set $\ast=p_1=1$ and $A$ to be the set of the other labels, i.e. $A=\{p_1,\dots,p_n\}\setminus\{\ast\}=\{\min
\pi_s: 1\leq s\leq r\}\setminus \{1\}$. We decorate on the graph of the fat partition $\pi_{\mathop{\mathrm{fat}}}$ all elements of the set $A$ (cf Figure [\[fig:tlustapartycja2\]](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}).

In the following we shall compute $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$ for ${\mathbf{p}}$ defined as above; please note that Proposition [\[prop:zmianaoznaczen\]](#prop:zmianaoznaczen){reference-type="ref" reference="prop:zmianaoznaczen"} allows us to rename the labels and to find $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$ for a general ${\mathbf{p}}$.

As we already mentioned in Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"}, we can view the fat partition $\pi_{\mathop{\mathrm{fat}}}$ as a bijection $\pi_{\mathop{\mathrm{fat}}}:\{1',2',\dots,n'\}\rightarrow\{1,2,\dots,n\}$. We also consider a bijection $c:\{1,2,\dots,n\}\rightarrow\{1',2',\dots,n'\}$ given by $\dots,3\mapsto 2', 2\mapsto 1', 1\mapsto n', n\mapsto
(n-1)',\dots$. We consider the cycle decomposition of the permutation $\pi_{\mathop{\mathrm{fat}}}\circ c\in{{S}}_{\{1,2,\dots,n\}}$ and remove from this decomposition all elements except the elements of $A$. In this way we constructed a permutation $(\pi_{\mathop{\mathrm{fat}}}\circ
c)|_A\in{{S}}_{A}$, called restriction of $\pi_{\mathop{\mathrm{fat}}}\circ c$ to the set $A$. This operation has a nice interpretation: on the graphical representation of $\pi_{\mathop{\mathrm{fat}}}$ and $c$ we travel along the cycles by following the arrows and we write down only decorated vertices. We equip $(\pi_{\mathop{\mathrm{fat}}}\circ c)|_A$ with a structure of a partial permutation by setting its support to be $A$.

For example, for $\pi=\big\{ \{1,3\},\{2,5,7\}, \{4\}, \{6\} \big\}$ depicted on Figure [\[fig:przecinajacapartycja\]](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} we have ${\mathbf{p}}=(1,2,1,4,2,6,2)$, $A=\{2,4,6\}$ and the decorations of $\pi_{\mathop{\mathrm{fat}}}$ are depicted on Figures [\[fig:tlustapartycja2\]](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}, [\[fig:tlustapartycja3\]](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"} and [\[fig:tlustapartycja4\]](#fig:tlustapartycja4){reference-type="ref" reference="fig:tlustapartycja4"}. The composition $\pi_{\mathop{\mathrm{fat}}}\circ c$ has a cycle decomposition $(1,\mathbf{2},3,5,\mathbf{4})(\mathbf{6},7)$.

It follows that $(\pi_{\mathop{\mathrm{fat}}}\circ
c)|_A=(\mathbf{2},\mathbf{4})(\mathbf{6})$.

::: theorem
[]{#theo:ilewynosifpss label="theo:ilewynosifpss"} Let $\pi$ and ${\mathbf{p}}$ be as above. Then $$\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})=(\pi_{\mathop{\mathrm{fat}}} \circ c)|_A.$$
:::

::: proof
*Proof.* The equality of permutations follows easily from Lemma [\[lem:lematoliczniufpss\]](#lem:lematoliczniufpss){reference-type="ref" reference="lem:lematoliczniufpss"} below by setting $l=1$ and the equality of supports is trivial. ◻
:::

::: lemma
[]{#lem:lematoliczniufpss label="lem:lematoliczniufpss"} Let $\pi$ and ${\mathbf{p}}$ be as above, we set $p_{n+1}:=p_1=1=\ast$ and let $\sigma_1,\dots,\sigma_{n+1}$ be as in Sections [\[subsubsec:fasps\]](#subsubsec:fasps){reference-type="ref" reference="subsubsec:fasps"} and [\[subsubsec:fpsas\]](#subsubsec:fpsas){reference-type="ref" reference="subsubsec:fpsas"}. Let $x\in A\cup\{\ast\}$ and let $1\leq l\leq n+1$.

If $x=p_l$ then $\sigma_l(x)=\ast$.

Suppose that $x\neq p_l$; let $m$ be the smallest index such that $l\leq m\leq n+1$ and $x=p_m$. If no such index exist then $\sigma_l(x)=x$. Otherwise we start in the vertex $m$ a walk on the graphical representation of $\pi_{\mathop{\mathrm{fat}}}$ and $c$ by following the arrows until we enter some decorated vertex $y$ (after having made at least one step, i.e. starting in a decorated vertex do not count as entering it). The above walk always stops after a finite number of steps and $\sigma_l(x)=y$.
:::

::: proof
*Proof.* The shall prove the lemma by backward induction. In the case $l=n+1$ it holds trivially.

Suppose that the statement of lemma is true for all $l'>l$. The first part, $\sigma_l(p_l)=\ast$ follows from the very construction of $\sigma_l$ in [\[eq:dlaczegopushing\]](#eq:dlaczegopushing){reference-type="eqref" reference="eq:dlaczegopushing"}.

Observe that for every $r$ we have $\sigma_r=(a_r\ast)
\sigma_{r+1}$ hence $\sigma_r(x)=\sigma_{r+1}(x)$ if $x\notin\{
\sigma_{r}^{-1}(\ast),
\sigma_{r+1}^{-1}(\ast)\}=\{p_{r},p_{r+1}\}$. This has twofold implications.

Firstly, if $x\notin\{p_l,p_{l+1},\dots,p_n,p_{n+1}\}$ then $\sigma_l(x)=\sigma_{l+1}(x)=\cdots=\sigma_{n+1}(x)=x$, which finishes the proof.

Secondly, when the last case in the lemma statement holds then $$\sigma_l(x)=\sigma_{l+1}(x)=\cdots=\sigma_{m-1} (x)=
  \big((a_{m-1} \ast)\circ \sigma_m\big)(x)=a_{m-1},$$ where we used the fact that $p_m=x$ is equivalent to $\sigma_m(x)=\ast$. Equation [\[eq:formulanaadmissible\]](#eq:formulanaadmissible){reference-type="eqref" reference="eq:formulanaadmissible"} implies that $\sigma_l(x)=\sigma_{m}(p_{m-1})$. We denote by $\pi_h$ the block of $\pi=\{\pi_1,\dots,\pi_r\}$ such that the element $m-1$ belongs to it. Let $r$ be the smallest index such that $p_{m-1}=p_r$ and $m\leq r\leq n+1$. If no such index exists then $\sigma_l(x)=\sigma_{m}(p_{m-1})=p_{m-1}$. Otherwise, if such an index exists then $$\sigma_l(x)=\sigma_{m}(p_{m-1})=\sigma_{m+1}(p_{m-1})=\cdots=
\sigma_{r}(p_{m-1})=\sigma_{r}(p_r).$$

We compare the value of $\sigma_l(x)$ computed above with the answer given by the graphical algorithm: we start our trip in vertex $m$ and then go to vertex $(m-1)'$. If the index $r$ considered above does not exist then $m-1$ is the biggest element of $\pi_h$ and therefore $(m-1)'$ is connected by $\pi_{\mathop{\mathrm{fat}}}$ with the smallest element of $\pi_h$ which is therefore decorated (the exceptional case $1\in \pi_h$ is not possible since this would mean that $p_{m-1}=p_1=\ast$ and in this case $p_{m-1}=p_{n+1}$ and the index $r$ would exist) and the algorithm terminates giving the answer $\min \pi_h=p_{m-1}$ which coincides with the correct value. Otherwise, if the index $r$ exists then $(m-1)'$ is connected by $\pi_{\mathop{\mathrm{fat}}}$ with the vertex $r$, $l<m+1\leq r\leq n+1$ (the vertex $n+1$ should be understood as the vertex $1$). From the inductive hypothesis it follows that the algorithm will return the answer $\sigma_{r}(p_r)$ which is again correct. ◻
:::

::: corollary
[]{#cor:formulanaadmissible label="cor:formulanaadmissible"} Let $\pi$ and ${\mathbf{p}}$ be as above, let ${\mathbf{a}}=\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}({\mathbf{p}})$ and let $1\leq l\leq n$. We start in the vertex $l$ a walk on the on the graphical representation of $\pi_{\mathop{\mathrm{fat}}}$ and $c$ by following the arrows until we enter some decorated vertex $y$ (after having made at least one step).

Then $$a_l=y.$$
:::

::: proof
*Proof.* It is a simple application of [\[eq:formulanaadmissible\]](#eq:formulanaadmissible){reference-type="eqref" reference="eq:formulanaadmissible"} and Lemma [\[lem:lematoliczniufpss\]](#lem:lematoliczniufpss){reference-type="ref" reference="lem:lematoliczniufpss"}. ◻
:::

### Maps $\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}$ and $\Sigma=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}$

Let us fix the finite set $A$ and the extra element $\ast$. We consider an algebra of pushing sequences in which the multiplication is as in Section [\[subsec:multiplicationpushing\]](#subsec:multiplicationpushing){reference-type="ref" reference="subsec:multiplicationpushing"} and the addition is understood as an addition of formal sums. The map $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ extends naturally to an algebra homomorphism from the algebra of pushing sequences to the algebra ${\mathbb{C}}(\widetilde{{{S}}_{A}})$ of partial permutations.

We define a map from pushing partitions to the algebra of pushing sequences by $$\label{eq:definicjafppps} \Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(\pi)=\sum_{{\mathbf{p}}\sim\pi} {\mathbf{p}}.$$

We define the map $\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}$ in the unique way which makes the diagram below commute. This map is explicitly given by Claim [\[claim:definicjasigma\]](#claim:definicjasigma){reference-type="ref" reference="claim:definicjasigma"} which will be proved below. $$\label{eq:diagram2}
\includegraphics{xypic02.eps}$$

::: theorem
[]{#theo:stwierdzeniepierwszejestprawda label="theo:stwierdzeniepierwszejestprawda"} Claim [\[claim:definicjasigma\]](#claim:definicjasigma){reference-type="ref" reference="claim:definicjasigma"} is true. In other words: let $\pi$ be a partition of the set $\{1,2,\dots,n\}$ and let numbers $k_1,\dots,k_t$ be given by the above construction. Then $$\Sigma_\pi:=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}(\pi)=\Sigma_{k_1,\dots,k_t},$$ where $\Sigma_{k_1,\dots,k_t}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ on the right--hand side should be understood as in Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"}.
:::

::: proof
*Proof.* Equation [\[eq:definicjafppps\]](#eq:definicjafppps){reference-type="eqref" reference="eq:definicjafppps"} and requirement that [\[eq:diagram2\]](#eq:diagram2){reference-type="eqref" reference="eq:diagram2"} commutes imply that $$\Sigma(\pi)=\sum_{{\mathbf{p}}\sim\pi} \Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}}).$$ By an appropriate renaming of labels Theorem [\[theo:ilewynosifpss\]](#theo:ilewynosifpss){reference-type="ref" reference="theo:ilewynosifpss"} allows us to compute each summand $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$. We decompose $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})=(\pi\circ c)|_A
\in{{S}}_{\{p_1,p_2,\dots,p_n\} \setminus\{p_1\} }$ into a product of disjoint cycles and we denote by $k_1,\dots,k_t$ the lengths of these cycles. It follows that $$\Sigma_{\pi}=\Sigma_{k_1,\dots,k_t},$$ where the right--hand side was defined in [\[eq:definicjasigma\]](#eq:definicjasigma){reference-type="eqref" reference="eq:definicjasigma"}.

From the proof of Theorem [\[theo:ilewynosifpss\]](#theo:ilewynosifpss){reference-type="ref" reference="theo:ilewynosifpss"} it follows that for each $1\leq s\leq t$ the number $k_s$ is equal to the number of decorated elements in the corresponding cycle of the permutation $\pi_{\mathop{\mathrm{fat}}}\circ c$. One can easily see that the original definition of the decorated elements is equivalent to the following one: element $m\in\{1,2,\dots,n\}$ is decorated if and only if going counterclockwise from $m$ to $(\pi_{\mathop{\mathrm{fat}}}\circ c)^{-1}(m)$ one does not cross the line between the marked starting point between $1$ and $1'$ and the central disc (see Figure [\[fig:tlustapartycja2\]](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}). Therefore $k_s$ is equal to the number of elements in the corresponding cycle of $\pi_{\mathop{\mathrm{fat}}}\circ c$ minus the number of times this cycle going clockwise crosses the line between the starting point and the central disc. It follows that the numbers $k_1,\dots,k_t$ defined above coincide with [\[eq:formulanak\]](#eq:formulanak){reference-type="eqref" reference="eq:formulanak"} which finishes the proof. ◻
:::

### Multiplication of pushing partitions

In Section [\[sec:mnozeniepartycji\]](#sec:mnozeniepartycji){reference-type="ref" reference="sec:mnozeniepartycji"} we defined the multiplication of partitions. Diagram [\[eq:diagram2\]](#eq:diagram2){reference-type="eqref" reference="eq:diagram2"} commutes and we shall prove that $\Sigma=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}$ is an algebra homomorphism (we already know that $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ is an algebra homomorphism; we will not need it but one can show that in a certain sense $\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}$ is also a homomorphism).

::: lemma
[]{#lem:mnozeniedwoch label="lem:mnozeniedwoch"} Let $1\leq k< l\leq m$, let $\pi^1$ be a pushing partition of the set $\rho_1=\{l+1,l+2,\dots,m,1,2,\dots,k\}$, let $\pi^2$ be a pushing partition of the set $\rho_2=\{k+1,k+2,\dots,l\}$. We define a non--crossing partition $\rho=\{\rho_1,\rho_2\}$.

Then $$\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}(\pi^1\cdot \pi^2)=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}(\pi^1) \Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}(\pi^2),$$ where $\pi^1 \cdot \pi^2$ denotes the $\rho$--ordered product of partitions $\pi^1$ and $\pi^2$ as defined in Section [\[sec:mnozeniepartycji\]](#sec:mnozeniepartycji){reference-type="ref" reference="sec:mnozeniepartycji"} and the product on the right--hand side is the usual product of the elements of ${\mathbb{C}}(\widetilde{{{S}}_{A}})$.
:::

::: proof
*Proof.* Let us consider a simpler case $\rho'_1=\{1,2,\dots,k+m-l\}$, $\rho'_2=\{k+m-l+1,k+m-l+2,\dots,m\}$. From Proposition [\[prop:mnozeniepushingsequences\]](#prop:mnozeniepushingsequences){reference-type="ref" reference="prop:mnozeniepushingsequences"} it follows that $\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(\pi^1)
\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(\pi^2)$ consists of all pushing sequences $(p_1,\dots,p_m)$ such that $p_1=p_{k+m-l+1}=\ast$ and $(p_1,\dots,p_{k+m-l})\sim
\pi^1$, $(p_{k+m-l+1},\dots,p_m)\sim \pi^2$. On the other hand

the only non--trivial block of $\rho'_{\mathop{\mathrm{comp}}^{-1}}$ is $\{1,k+m-l+1\}$ and therefore

$$\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(\pi^1) \Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(\pi^2) = \Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}( \pi^1
\cdot \pi^2).$$ To both sides of the equation we apply the map $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ and use the fact that it is a homomorphism and the diagram [\[eq:diagram\]](#eq:diagram){reference-type="eqref" reference="eq:diagram"} commutes.

The general case follows from the observation that the partition $\rho$ can be obtained from $\rho'$ by a cyclic rotation. One can easily see that a product of rotated partitions is a rotation of the product of the original partitions. Finally, we apply Proposition [\[prop:rotacjajestok\]](#prop:rotacjajestok){reference-type="ref" reference="prop:rotacjajestok"}. ◻
:::

::: lemma
[]{#lem:associative label="lem:associative"} Multiplication of partitions, as defined in Section [\[sec:mnozeniepartycji\]](#sec:mnozeniepartycji){reference-type="ref" reference="sec:mnozeniepartycji"}, is associative. To be precise: let $\tau=\{\tau_1,\dots,\tau_r\}$ be a non--crossing partition of the set $\{1,2,\dots,n\}$. For each $s$ let $\tilde{\tau}^s=\{\tau_{s,1},\dots,\tau_{s,l_s} \}$ be a non--crossing partition of the set $\tau_s$. We denote by $\hat{\tau}=\tilde{\tau}^1\cup\cdots\cup\tilde{\tau}^r = \{
\tau_{s,k}: 1\leq s\leq r, 1\leq k\leq l_s  \}$ the non--crossing partition of the set $\{1,2,\dots,n\}$. Let furthermore $\pi^{s,k}$ be a pushing partition of the set $\tau_{s,k}$ for each choice of $1\leq s\leq r$ and $1\leq k\leq l_s$.

Then $$\prod_s \Big(  \prod_k   \pi^{s,k}  \Big)= \prod_{s,k}   \pi^{s,k},
\label{eq:nudynapudy}$$ where the left--hand side is a $\tau$--ordered product of $\tilde{\tau}^s$--ordered products and the right--hand side is a $\hat{\tau}$--ordered product.
:::

::: proof
*Proof.* Probably the best way to prove this lemma is to use the graphical description of the partition multiplication from Section [\[subsec:geometricmultiplication\]](#subsec:geometricmultiplication){reference-type="ref" reference="subsec:geometricmultiplication"} since---speaking informally---cutting holes, gluing discs and merging discs are all associative operations. We provide a more detailed proof below.

Observe that every partition $\sigma$ which contributes to the left--hand side has a property that for every $a,b\in \tau_{s,k}$ elements $a$ and $b$ are connected by $\sigma$ if and only if they are connected by $\pi^{s,k}$. Furthermore since every partition $\sigma^s$ which contributes in $\prod_{k} \pi^{s,k}$ must fulfill $\sigma^s \geq (\tilde{\tau}^s)_{\mathop{\mathrm{comp}}^{-1}}$ therefore $\sigma\geq
\tau_{\mathop{\mathrm{comp}}^{-1}}\vee\Big(\bigcup_s
(\tilde{\tau}^s)_{\mathop{\mathrm{comp}}^{-1}}\Big)=\hat{\tau}_{\mathop{\mathrm{comp}}^{-1}}$ (for the last equality see Lemma [\[lem:babel\]](#lem:babel){reference-type="ref" reference="lem:babel"} below). It follows that every partition which appears on the left--hand side of [\[eq:nudynapudy\]](#eq:nudynapudy){reference-type="eqref" reference="eq:nudynapudy"} appears also on the right--hand side.

To show the opposite inclusion, for a summand $\sigma$ which appears on the right--hand side of [\[eq:nudynapudy\]](#eq:nudynapudy){reference-type="eqref" reference="eq:nudynapudy"} we set $\sigma^s\in
\mathop{\mathrm{P}}(\tau_s)$ to be the partition which connects $a,b\in \tau_s$ if and only if $a,b$ are connected by $\sigma$. Lemma [\[lem:babel\]](#lem:babel){reference-type="ref" reference="lem:babel"} implies that $\sigma^s\geq (\tilde{\tau}^s)_{\mathop{\mathrm{comp}}^{-1}}$ hence $\sigma^s$ is one of the summands which appear in the product $\prod_k \pi^{s,k}$. By using a similar argument we see that $\sigma$ is one of the summands which contribute to the product $\prod_s \sigma^s$ and therefore contributes to the left--hand side of [\[eq:nudynapudy\]](#eq:nudynapudy){reference-type="eqref" reference="eq:nudynapudy"}. ◻
:::

::: lemma
[]{#lem:babel label="lem:babel"} We keep the notation from Lemma [\[lem:associative\]](#lem:associative){reference-type="ref" reference="lem:associative"}. Then $$\tau_{\mathop{\mathrm{comp}}^{-1}}\vee\Big(\bigcup_s
(\tilde{\tau}^s)_{\mathop{\mathrm{comp}}^{-1}}\Big)=\hat{\tau}_{\mathop{\mathrm{comp}}^{-1}}.
\label{eq:widzeciemnosc}$$
:::

::: proof
*Proof.* Similarly as in Section [\[subsec:geometricmultiplication\]](#subsec:geometricmultiplication){reference-type="ref" reference="subsec:geometricmultiplication"} we consider a sphere with a collection of holes, each corresponding to one of the blocks of $\tau$. In the second step we replace each initial hole $\tau_s$ by a collection of holes $\tilde{\tau}^s$: in this way we obtained a large sphere with a collection of holes $\tau_{s,k}$. Alternatively we can treat it as one big hole to which was glued a collection of discs; every of these discs corresponds to one of the blocks of $\hat{\tau}_{\mathop{\mathrm{comp}}^{-1}}$ which corresponds to the right--hand side of [\[eq:widzeciemnosc\]](#eq:widzeciemnosc){reference-type="eqref" reference="eq:widzeciemnosc"}.

On the other hand, we can treat the sphere with the first collection of holes as a sphere with a single hole glued with a collection of discs corresponding to $\tau_{\mathop{\mathrm{comp}}^{-1}}$. When we replace the hole $\tau_s$ by $\tilde{\tau}^s$ it corresponds to gluing another collection of discs $(\tilde{\tau}^s)_{\mathop{\mathrm{comp}}^{-1}}$. Therefore the whole collection of discs corresponds to the left--hand side of [\[eq:widzeciemnosc\]](#eq:widzeciemnosc){reference-type="eqref" reference="eq:widzeciemnosc"}. ◻
:::

::: theorem
[]{#theo:sigmajesthomomorfizmem label="theo:sigmajesthomomorfizmem"} Claim [\[claim:mnozenie\]](#claim:mnozenie){reference-type="ref" reference="claim:mnozenie"} is true. In other words: let $\rho=\{\rho_1,\dots,\rho_r\}$ be a non--crossing partition of the set $\{1,2,\dots,n\}$ and for every $1\leq s\leq r$ let $\pi^s$ be a partition of the set $\rho_s$. Then $$\Sigma\Big( \prod_{s} \pi^s \Big)=\prod_{1\leq s\leq r} \Sigma_{\pi^s},$$ where the multiplication on the left hand side should be understood as the $\rho$--ordered product of partitions and on the right hand side it should be understood as the usual product of commuting elements in ${\mathbb{C}}(\widetilde{{{S}}_{\infty}})$.
:::

::: proof
*Proof.* We shall use the induction with respect to $r$, the number of blocks of the partition $\rho$. The case $r=1$ is of course trivial.

Observe that since $\rho$ is non--crossing therefore at least one block $\rho_h$ has a form $\rho_h=\{a,a+1,a+2,\dots,b\}$ (for example, it is one of the blocks for which the expression $(\max
\rho_h- \min \rho_h)$ takes the minimal value).

Lemma [\[lem:associative\]](#lem:associative){reference-type="ref" reference="lem:associative"} implies that $$\prod_s \pi^s = \pi^h \cdot \big( \prod_{s\neq h} \pi^s \big).$$ We apply to both sides the map $\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{A}})}=\Sigma$ and apply Lemma [\[lem:mnozeniedwoch\]](#lem:mnozeniedwoch){reference-type="ref" reference="lem:mnozeniedwoch"} to the right hand side. The inductive hypothesis can be applied to the second factor on the right hand side which finishes the proof. ◻
:::

### Jucys--Murphy element

::: theorem
[]{#theo:zgodnoscpartycjizjurcysiem label="theo:zgodnoscpartycjizjurcysiem"} Claim [\[claim:dobryjurcysmurphy\]](#claim:dobryjurcysmurphy){reference-type="ref" reference="claim:dobryjurcysmurphy"} is true. In other words, let $X$ be a finite ordered set, let $\rho$ be a non--crossing partition of a finite ordered set and $n\geq 1$ be an integer. Then $$\begin{aligned}
 \Sigma(M^{\mathop{\mathrm{P}}}_{X}) &=M^{\mathop{\mathrm{JM}}}_{|X|}, \\
 \Sigma(M^{\mathop{\mathrm{P}}}_\rho)&=M^{\mathop{\mathrm{JM}}}_\rho, \\
 \Sigma(R^{\mathop{\mathrm{P}}}_n)&=R^{\mathop{\mathrm{JM}}}_n, 
\end{aligned}$$ where $\Sigma$ is the map considered in Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"}.
:::

::: proof
*Proof.* Observe that every pushing sequence of length $n$ appears in $\Phi^{\mathop{\mathrm{P}}}_{\mathop{\mathrm{ps}}}(M^{\mathop{\mathrm{P}}}_{\{1,2,\dots,n\}})$ exactly once. The bijection between pushing and admissible sequences together with the definition [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"} finish the proof. ◻
:::
