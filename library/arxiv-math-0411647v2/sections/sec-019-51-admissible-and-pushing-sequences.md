---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-019-51-admissible-and-pushing-sequences
section_title: "Admissible and pushing sequences"
section_number: 5.1
pages: 42-46
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.973
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
In this article we manipulate with moments of the Jucys--Murphy element $J$ (or with products of such moments) and we need an efficient way to enumerate the summands in sums similar to [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"}. Conceptually the simplest way is to enumerate the summands by sequences $a_1,\dots,a_n\in A$ and which will be called admissible. However, it turns out that manipulating admissible sequences is quite complicated. It turns out that the suitable objects to enumerate summands in [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"} are pushing sequences. We will describe pushing sequences in terms of admissible sequences.

### Admissible sequences. Map $\Phi^{\mathop{\mathrm{as}}}_{\widetilde{{{S}}_{A}}}$

We recall that $\ast\notin A$. We say that a sequence $a_1,\dots,a_n$ is admissible if it contributes in the sum [\[eq:wielkasuma\]](#eq:wielkasuma){reference-type="eqref" reference="eq:wielkasuma"} or equivalently if $a_1,\dots,a_n\in A$ and $$(\ast)=\ast. \label{eq:admissible}$$

The set of admissible sequences is a semigroup if for multiplication we take the concatenation of sequences: $${\mathbf{a}}{\mathbf{b}}=(a_1,\dots,a_n,b_1,\dots,b_o)$$ for admissible sequences ${\mathbf{a}}=(a_1,\dots,a_n)$ and ${\mathbf{b}}=(b_1,\dots,b_o)$. The unit is the empty sequence.

We consider a map $\Phi^{\mathop{\mathrm{as}}}_{{{S}}_{A}}$ from the set of admissible sequences to the symmetric group ${{S}}_{A}$ by setting $$\Phi^{\mathop{\mathrm{as}}}_{{{S}}_{A}}:(a_1,\dots,a_n)\mapsto (a_1 \ast) \cdots (a_n \ast).$$ We can treat the right--hand side as a partial permutation of $A$ with the support $\{a_1,\dots,a_n\}$; in this way we obtain a map $\Phi^{\mathop{\mathrm{as}}}_{\widetilde{{{S}}_{A}}}$ from the set of admissible sequences to the semigroup $\widetilde{{{S}}_{A}}$ of partial permutations. It is easy to check that both maps are homomorphisms of semigroups.

### Pushing sequences

We say that no neighbor elements of a sequence $(p_1,\dots,p_n)$ are equal if $p_l\neq p_{l+1}$ holds for any $1\leq l\leq n$. We should think that the elements of the sequence are arranged in a circle and the successor of $p_n$ is $p_1$, therefore in the above definition the case $l=n$ means that we require $p_n\neq p_1$. In particular, it cannot happen that $n=1$.

We will say that a sequence $(p_1,\dots,p_n)$ is a pushing sequence if $p_1,\dots,p_n\in A\cup\{\ast\}$ and if $p_1=\ast$ and if no neighbor elements of $(p_1,\dots,p_n)$ are equal.

### Commutative diagram

In the following we will construct functions such that the following diagram commutes. Later on we shall equip pushing sequences with a multiplicative structure in such a way that all maps will become homomorphisms of semigroups. $$\includegraphics{xypic01.eps}
\label{eq:diagram}$$

### Map $\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}$ {#subsubsec:fasps}

Let ${\mathbf{a}}=(a_1,\dots,a_n)$, $a_1,\dots,a_n\in A$ be an admissible sequence. We assign to it a sequence of permutations $\sigma_1,\dots,\sigma_{n+1}\in{{S}}_{A\cup\{\ast\}}$ defined by $$\sigma_l= (a_l \ast) (a_{l+1} \ast) \cdots (a_n \ast)
\label{eq:slynnesigma}$$ and a sequence ${\mathbf{p}}=\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}({\mathbf{a}})= (p_1,\dots,p_n)$, $p_1,\dots,p_n\in A\cup\{\ast\}$ defined by $$p_l= \sigma_l^{-1}(\ast). \label{eq:dlaczegopushing}$$ Notice that since ${\mathbf{a}}$ is admissible hence $p_1=\ast$ and $p_1=\ast\neq a_n=p_n$. Furthermore since $\sigma_{l-1}=(a_{l-1}
\ast) \sigma_l$ hence $p_{l-1}=\sigma_l^{-1}(a_{l-1}) \neq
\sigma_l^{-1}(\ast)=p_l$ and ${\mathbf{p}}$ is a pushing sequence.

Equation [\[eq:dlaczegopushing\]](#eq:dlaczegopushing){reference-type="eqref" reference="eq:dlaczegopushing"} should explain the name of pushing sequences: imagine that $A\cup\{\ast\}$ is a set of some items and initially every item $x$ is located within a box which carries a label '$x$'. In the process of computing the product $(a_1
\ast) \cdots (a_n \ast)$ (from the right to the left) we obtain a sequence of partial products $\sigma_n,\sigma_{n-1},\dots,\sigma_1$:

permutation $\sigma_{l-1}$ is obtained from $\sigma_l$ by transposition of the item which is in the box labeled by '$\ast$' and the item (which turns out to be the item $p_{l-1}$) from the box labeled by '$a_{l-1}$'. We can think therefore that the item $p_{l-1}$ is pushing out the contents of the box labeled by '$\ast$'.

### Map $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}$ {#subsubsec:fpsas}

Let a pushing sequence ${\mathbf{p}}=(p_1,\dots,p_n)$ be given. By backward induction we will assign to it a unique pair of sequences $(\sigma_1,\dots,\sigma_{n+1})$, $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}({\mathbf{p}})= (a_1,\dots,a_n)$, where $\sigma_1,\dots,\sigma_{n+1}\in{{S}}_{A\cup\{\ast\}}$ and $(a_1,\dots,a_n)$ is an admissible sequence such that [\[eq:slynnesigma\]](#eq:slynnesigma){reference-type="eqref" reference="eq:slynnesigma"} and [\[eq:dlaczegopushing\]](#eq:dlaczegopushing){reference-type="eqref" reference="eq:dlaczegopushing"} are fulfilled.

We start the construction by setting $\sigma_{n+1}=e$ since it is the only choice if we want [\[eq:slynnesigma\]](#eq:slynnesigma){reference-type="eqref" reference="eq:slynnesigma"} to be fulfilled for $l=n+1$. If $\sigma_l$ is already defined we set $a_{l-1}=\sigma_{l} (p_{l-1})$ and $\sigma_{l-1}=(a_{l-1} \ast)
\sigma_l$. Again, it is the only choice that we have since equations [\[eq:slynnesigma\]](#eq:slynnesigma){reference-type="eqref" reference="eq:slynnesigma"} and [\[eq:dlaczegopushing\]](#eq:dlaczegopushing){reference-type="eqref" reference="eq:dlaczegopushing"} imply $$\label{eq:formulanaadmissible} a_{l-1}=(a_{l-1}\ast)(\ast)=
\sigma_{l} \sigma_{l-1}^{-1}(\ast)=\sigma_{l}(p_{l-1}).$$

Since ${\mathbf{p}}$ is pushing hence $\sigma_l^{-1}(a_{l-1})=p_{l-1} \neq
p_l=\sigma_l^{-1}(\ast)$ therefore $a_1,\dots,a_n\neq \ast$; furthermore $[(a_1 \ast) \cdots (a_n
\ast)]^{-1}(\ast)=\sigma_1^{-1}(\ast)=p_{1}=\ast$ hence ${\mathbf{a}}$ is admissible.

Equations [\[eq:slynnesigma\]](#eq:slynnesigma){reference-type="eqref" reference="eq:slynnesigma"} and [\[eq:dlaczegopushing\]](#eq:dlaczegopushing){reference-type="eqref" reference="eq:dlaczegopushing"} are indeed fulfilled by construction, therefore $\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}(\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}({\mathbf{p}}))={\mathbf{p}}$ for every pushing sequence ${\mathbf{p}}$. Furthermore the uniqueness of the pair $(a_1,\dots,a_n)$, $(\sigma_1,\dots,\sigma_{n+1})$ implies that there exists at most one preimage of ${\mathbf{p}}$ with respect to $\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}$. Therefore we proved the following result:

::: proposition
Maps $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}$ and $\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}$ are inverses of each other.
:::

### Map $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$

The bijections between pushing and admissible sequences allow us to define the map $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ in a unique way which makes the diagram [\[eq:diagram\]](#eq:diagram){reference-type="eqref" reference="eq:diagram"} commute.

Let ${\mathbf{p}}$ be a pushing sequence and ${\mathbf{a}}$ be the corresponding admissible sequence. Observe that if $\sigma_1,\dots,\sigma_{n+1}$ is the sequence of permutations which was constructed in Sections [0.0.4](#subsubsec:fasps){reference-type="ref" reference="subsubsec:fasps"} and [0.0.5](#subsubsec:fpsas){reference-type="ref" reference="subsubsec:fpsas"} then $$\label{eq:formulanafpss} \Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{p}})=\Phi^{\mathop{\mathrm{as}}}_{{{S}}_{A}}({\mathbf{a}})=\sigma_1.$$ In order to compute $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$ we need to specify the support of this permutation. It is the support of $\Phi^{\mathop{\mathrm{as}}}_{\widetilde{{{S}}_{A}}}({\mathbf{a}})$, namely $\{a_1,\dots,a_n\}=\{p_1,\dots,p_n\}\setminus\{\ast\}$; the inclusions which imply the latter equality follow directly from the construction of the maps $\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}$ and $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}$. In Section [\[subsec:explicit\]](#subsec:explicit){reference-type="ref" reference="subsec:explicit"} we shall compute $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}$ and $\Phi^{\mathop{\mathrm{ps}}}_{\mathop{\mathrm{as}}}$ more explicitly.

### Multiplication of pushing sequences {#subsec:multiplicationpushing}

The bijections between pushing and admissible sequences allow us to define multiplication of pushing sequences in the unique way which makes arrows of [\[eq:diagram\]](#eq:diagram){reference-type="eqref" reference="eq:diagram"} to be homomorphisms of semigroups in such a way that the diagram commutes.

The exact form of this multiplication is given by the following proposition

::: proposition
[]{#prop:mnozeniepushingsequences label="prop:mnozeniepushingsequences"} Let ${\mathbf{p}}=(p_1,\dots,p_k)$ and ${\mathbf{q}}=(q_1,\dots,q_l)$ be pushing sequences and let $\pi=\Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}(q_1,\dots,q_l)$. Then $${\mathbf{p}}{\mathbf{q}}= \big(\pi^{-1}(p_1),\dots,\pi^{-1}(p_k),q_1,\dots,q_l \big).$$
:::

::: proof
*Proof.* Let ${\mathbf{p}}=\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}({\mathbf{a}})$ and let $\sigma^a_1,\dots,\sigma^a_k$ be the sequence of permutations constructed in Section [0.0.4](#subsubsec:fasps){reference-type="ref" reference="subsubsec:fasps"} for ${\mathbf{a}}$, i.e. $\sigma^a_m=(a_m
\ast)\cdots(a_k\ast)$ for $1\leq m\leq k$. Let ${\mathbf{b}}=\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}({\mathbf{q}})$ and let $\sigma^b_1,\dots,\sigma^b_l$ be the analogous sequence of permutations obtained for ${\mathbf{b}}$.

Let $\sigma_1,\dots,\sigma_{k+l}$ be the sequence of permutations obtained for the concatenated sequence ${\mathbf{a}}{\mathbf{b}}$. Observe that $$\begin{gathered}
\sigma_m=\begin{cases}
(b_{m-k} \ast) \cdots (b_l \ast) & \text{for } m\geq k+1 \\
(a_{m} \ast) \cdots (a_k \ast) (b_1 \ast) \cdots (b_l \ast) &
\text{for } m\leq k \end{cases}  \\ =
\begin{cases} \sigma^b_{m-k}  & \text{for } m\geq k+1 \\
\sigma^a_{m} \pi & \text{for } m\leq k,
\end{cases}
\end{gathered}$$ where $\pi=(b_1 \ast) \cdots (b_l
\ast)=\Phi^{\mathop{\mathrm{as}}}_{{{S}}_{A}}({\mathbf{b}})=\Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{q}})$.

It follows that ${\mathbf{r}}=(r_1,\dots,r_{n+l})= {\mathbf{p}}{\mathbf{q}}=\Phi^{\mathop{\mathrm{as}}}_{\mathop{\mathrm{ps}}}({\mathbf{a}}
{\mathbf{b}})$ is given by $$r_m=\sigma_m^{-1}(\ast)=\begin{cases} q_{m-n} & \text{for } m\geq n+1 \\
\pi^{-1}(p_{m}) & \text{for } m\leq n
\end{cases}$$ which finishes the proof. ◻
:::

### Invariance of the conjugacy class assigned to a pushing sequence

For the purpose of this section let us forget about the set $A$ and the distinguished element $\ast$. Let a sequence ${\mathbf{p}}=(p_1,\dots,p_n)$ be given such that no neighbor elements are equal: $p_l\neq p_{l+1}$ for all $1\leq l\leq n$. Now we can define the distinguished element $\ast$ by setting $\ast=p_1$ and set $A$ by $A=\{p_1,\dots,p_n\}\setminus \{\ast\}$.

Let $f$ be a one to one function defined on the set $\{p_1,\dots,p_n\}$. We set ${\mathbf{p}}'=\big( f(p_1),\dots,f(p_n) \big)$, $\ast'=f(\ast)$, $A'=f(A)$.

Pushing sequence ${\mathbf{p}}$ defines a partial permutation $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})\in \widetilde{{{S}}_{A}}$ and the pushing sequence ${\mathbf{p}}'$ defines a partial permutation $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A'}}}({\mathbf{p}}')\in \widetilde{{{S}}_{A'}}$.

::: proposition
[]{#prop:zmianaoznaczen label="prop:zmianaoznaczen"} We use the above notations. Then $$\Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{p}}')=f\circ \Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{p}}) \circ f^{-1}$$ and the support of $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A'}}}({\mathbf{p}}')$ is equal to the image of the support of $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$ under the map $f$.
:::

::: proof
*Proof.* Let $a_1,\dots,a_n$ and $\sigma_1,\dots,\sigma_{n+1}$ be the sequences we considered in Sections [0.0.4](#subsubsec:fasps){reference-type="ref" reference="subsubsec:fasps"} and [0.0.5](#subsubsec:fpsas){reference-type="ref" reference="subsubsec:fpsas"} and let $a'_1,\dots,a_n'$ and $\sigma_1',\dots,\sigma_{n+1}'$ be their analogues obtained for the pushing sequence ${\mathbf{p}}'$.

We leave to the reader to show by backward induction that $a_l'=f(a_l)$ and $\sigma_l'= f\circ \sigma_l \circ f^{-1}$ for every $1\leq l\leq n$. From [\[eq:formulanafpss\]](#eq:formulanafpss){reference-type="eqref" reference="eq:formulanafpss"} (and its analogue for ${\mathbf{p}}'$) it follows that $$\Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{p}}')=f\circ \Phi^{\mathop{\mathrm{ps}}}_{{{S}}_{A}}({\mathbf{p}}) \circ f^{-1}.$$

Now it is enough to observe that the support of $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A'}}}({\mathbf{p}}')$ is equal to $A'$ and the support of $\Phi^{\mathop{\mathrm{ps}}}_{\widetilde{{{S}}_{A}}}({\mathbf{p}})$ is equal to $A$. ◻
:::
