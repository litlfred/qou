---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-011-32-multiplication-of-partitions
section_title: "Multiplication of partitions"
section_number: 3.2
pages: 22-26
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.984
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#sec:mnozeniepartycji label="sec:mnozeniepartycji"}

### Definition of multiplication

We will introduce an algebraic structure on the partitions. For any finite ordered set $X$ one can consider a linear space spanned by all partitions of $X$. We will define a 'multiplicative' structure as follows: let $\rho=\{\rho_1,\dots,\rho_r\}$ be a non--crossing partition of a finite ordered set $X$ and for every $1\leq s\leq r$ let $\pi^s$ be a partition of the set $\rho_s$. We define the '$\rho$--ordered product' of partitions $\pi^s$ by $$\label{eq:definicjamnozenia} \prod_{s} \pi^s :=\sum_{\sigma} \sigma,$$ where the sum denotes a formal linear combination and it runs over all partitions $\sigma$ of the set $X$ such that

1.  for any $a,b\in\rho_s$, $1\leq s\leq r$ we have that $a$ and $b$ are connected by $\sigma$ if and only if they are connected by $\pi^s$,

2.  $\sigma\geq \rho_{{\mathop{\mathrm{comp}}^{-1}}}$,

where $\geq$ denotes the order on partitions we introduced in Section [\[subsec:partitions\]](#subsec:partitions){reference-type="ref" reference="subsec:partitions"}.

Above we defined the product of the elements of the basis of the linear space; by requirement that multiplication is distributive the definition extends uniquely to general vectors.

For example, for $$\begin{gathered}
\label{eq:przykladmnozenie} \rho_1=\{1,2,7,8\},\
\rho_2=\{3,4,5,6\},\\  \pi^1=\big\{ \{1,7\}, \{2\},\{8\} \big\},\
\pi^2=\big\{ \{3,5\},\{4,6\} \big\}
\end{gathered}$$ we have $$\begin{gathered}
\pi^1 \cdot \pi^2 =
\big\{ \{1,7\},\{2,4,6\},\{3,5\},\{8\} \big\}+\\
\big\{ \{1,7\},\{2,4,6\},\{3,5,8\} \big\}+ \big\{
\{1,3,5,7\},\{2,4,6\},\{8\} \big\}.
\end{gathered}$$

### Geometric interpretation of partitions multiplication {#subsec:geometricmultiplication}

Suppose for simplicity that $X=\{1,2,\dots,n\}$. On the surface of a large sphere we draw a small circle on which we mark counterclockwise points $1,2,\dots,n$.

Inside the circle we cut $r$ holes; for any $1\leq s\leq r$ the corresponding hole has a shape of a disc, the boundary of which passes through the points from the block $\rho_s$ (it is possible to perform this operation since $\rho$ is non--crossing). For every $1\leq s\leq r$ the partition $\pi^s$ connects some points on the boundary of the hole $\rho_s$ and this situation corresponds exactly to the case we considered in Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"}. We shall glue to the hole $\rho_s$ only the first collection of discs that we considered in Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"}, i.e. the discs which correspond to the blocks of the partition $\pi^s$. Thus we obtained a number of holes with a collection of glued discs (cf Figure [1](#fig:mnozeniepartycji){reference-type="ref" reference="fig:mnozeniepartycji"}).

![Graphical representation of example [\[eq:przykladmnozenie\]](#eq:przykladmnozenie){reference-type="eqref" reference="eq:przykladmnozenie"}.](figure13.eps){#fig:mnozeniepartycji}

When we inflate the original small holes inside the circle we may think about this picture alternatively: instead of $r$ small holes we have a big one (in the shape of the circle) but some arcs on its boundary are glued by extra discs (on Figure [2](#fig:mnozeniepartycji2){reference-type="ref" reference="fig:mnozeniepartycji2"} drawn in black) given by the partition $\rho_{{\mathop{\mathrm{comp}}^{-1}}}\in\mathop{\mathrm{NC}}(1,2,\dots,n)$. Furthermore we still have all discs (on Figure [2](#fig:mnozeniepartycji2){reference-type="ref" reference="fig:mnozeniepartycji2"} drawn in gray) corresponding to partitions $\pi^s$. We merge discs from these two collections if they touch the same vertex. After this merging the collection of discs corresponds to the partition $\rho_{{\mathop{\mathrm{comp}}^{-1}}}
\vee (\pi^1 \cup \cdots \cup\pi^t)$, i.e. the smallest partition which is bigger than both $\rho_{{\mathop{\mathrm{comp}}^{-1}}}$ and $\pi^1\cup\cdots\cup
\pi^t$.

![Figure [1](#fig:mnozeniepartycji){reference-type="ref" reference="fig:mnozeniepartycji"} after inflating small holes.](figure14.eps){#fig:mnozeniepartycji2}

The last step is to consider all ways of merging of the discs (or equivalently: all partitions $\sigma\geq \big( \rho_{{\mathop{\mathrm{comp}}^{-1}}} \vee
(\pi^1 \cup \cdots \cup\pi^t)\big)$) with the property that any two vertices that were lying on the boundary of the same small hole $\rho_s$ if were not connected by a disc from the collection $\pi^s$ then they also cannot be connected after all mergings.

## Map $\Sigma$ is a homomorphism

Since the map $\Sigma=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}$ was defined on the basis of the linear space of partitions, we can extend it linearly in a unique way. It turns out that $\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}$ preserves also the multiplication hence it is a homomorphism. However, since we consider only '$\rho$--ordered' products of partitions, we have to state it in a bit unusual way.

::: claim
[]{#claim:mnozenie label="claim:mnozenie"} Let $\rho=\{\rho_1,\dots,\rho_r\}$ be a non--crossing partition of the set $\{1,2,\dots,n\}$ and for every $1\leq s\leq r$ let $\pi^s$ be a partition of the set $\rho_s$. Then $$\Sigma\Big( \prod_{s} \pi^s \Big)=\prod_{1\leq s\leq r} \Sigma_{\pi^s},$$ where the multiplication on the left hand side should be understood as the $\rho$--ordered product of partitions and on the right hand side it should be understood as the usual product of commuting elements in ${\mathbb{C}}(\widetilde{{{S}}_{\infty}})$.
:::

This Claim will follow from Theorem [\[theo:sigmajesthomomorfizmem\]](#theo:sigmajesthomomorfizmem){reference-type="ref" reference="theo:sigmajesthomomorfizmem"}. Due to distributivity of multiplication the above Claim remains true if we allow $\pi^s$ to be a linear combination of partitions. It would be very interesting to prove Claim [\[claim:mnozenie\]](#claim:mnozenie){reference-type="ref" reference="claim:mnozenie"} directly if one treats Claim [\[claim:definicjasigma\]](#claim:definicjasigma){reference-type="ref" reference="claim:definicjasigma"} as a definition of $\Sigma_{\pi}$.

The following result was proved in [@KerovOlshanski1994; @IvanovKerov1999; @LascouxThibon2001vertex; @BianeCharacters].

::: corollary
[]{#cor:uniwersalnestale label="cor:uniwersalnestale"} For any choice of tuples of positive integers $(k_1,\dots,k_m)$ and $(k'_1,\dots,k'_n)$ there exists a function $f$ with a finite support defined on the set of the tuples of integers such that $$\label{eq:glod}
\Sigma_{k_1,\dots,k_m} \cdot \Sigma_{k'_1,\dots,k'_n} =
\sum_{p_1,\dots,p_r} f_{p_1,\dots,p_r}
\Sigma_{p_1,\dots,p_r}.$$
:::

::: proof
*Proof.* It is enough to find partitions $\pi, \pi'$ such that $\Sigma_{\pi}=\Sigma_{k_1,\dots,k_m}$, $\Sigma_{\pi'}=\Sigma_{k'_1,\dots,k'_n}$ and use the fact that $\Sigma_{\pi} \Sigma_{\pi'}=\Sigma_{\pi \cdot \pi'}$. ◻
:::

More detailed information about the product $\Sigma_{k_1,\dots,k_m}
\cdot \Sigma_{k'_1,\dots,k'_n}$ is provided by the following result which was proved by Ivanov and Olshanski [@IvanovOlshanski2002].

::: corollary
[]{#cor:filtration label="cor:filtration"} For any choice of integers $k_1,\dots,k_m,k'_1,\dots,k'_n\geq 1$ let us express the product $\Sigma_{k_1,\dots,k_m} \cdot
\Sigma_{k'_1,\dots,k'_n}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ as a linear combination of normalized conjugacy class indicators $\Sigma$. Then $$\begin{gathered}
\Sigma_{k_1,\dots,k_m} \cdot \Sigma_{k'_1,\dots,k'_n} =
\Sigma_{k_1,\dots,k_m,k'_1,\dots,k'_n} + \\
\text{(terms of degree at most
$k_1+\cdots+k_m+k'_1+\cdots+k'_n+m+n-2$)}
\end{gathered}$$ and therefore [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"} indeed defines a filtration.
:::

::: proof
*Proof.* Define $l_i=k_i+1$ and $l_i'=k_i'+1$. We set $\pi^1$ to be a partition of the set of consecutive integers $\rho_1=\{1,\dots,l_1+\cdots+l_m\}$ which has only one non--trivial block $\pi^1_1=\{l_1,l_1+l_2,l_1+l_2+l_3,\dots,l_1+\cdots+l_m\}$ and let $\pi^2$ be a partition of the set of consecutive integers $\rho_2=\{l_1+\cdots+l_m+1,l_1+\cdots+l_m+2,\dots,l_1+\cdots+l_m+l'_1+\cdots+l'_n\}$ which has only one non--trivial block $\pi^2_1=\{l_1+\cdots+l_m+l'_1,l_1+\cdots+l_m+l'_1+l'_2,\dots,
l_1+\cdots+l_m+l'_1+\cdots+l'_n\}$; all the other blocks of these partitions consist of single elements.

One can easily check that $\Sigma_{\pi^1}=\Sigma_{k_1,\dots,k_m}$ and $\Sigma_{\pi^2}= \Sigma_{k'_1,\dots,k'_n}$. We set $\rho=\{\rho_1,\rho_2\}$; let us compute the $\rho$--ordered product $\pi^1 \cdot \pi^2$.

Equation [\[eq:genusowatosc\]](#eq:genusowatosc){reference-type="eqref" reference="eq:genusowatosc"} implies that the terms of the maximal degree $l_1+\cdots+l_m+l'_1+\cdots+l'_n$ will correspond to non--crossing partitions (genus equal to zero) and the degree corresponding to any crossing partition cannot exceed $l_1+\cdots+l_m+l'_1+\cdots+l'_n-2$. It is enough to show that there is only one non--crossing partition $\sigma$ which contributes to $\pi^1 \cdot \pi^2$, namely the partition $\tau=(\pi^1 \cup \pi^2)
\vee \rho_{\mathop{\mathrm{comp}}^{-1}}$ which has only one non--trivial block $\pi^1_1\cup\pi^2_1$. This statement is pretty obvious from the geometric interpretation; we provide a more detailed proof below.

Let us consider a partition $\sigma\neq \tau$ which contributes to $\pi^1 \cdot \pi^2$. Of course we have $\sigma\geq\tau$. Let $a,c$ be a pair of elements which are connected by $\sigma$ and are not connected by $\tau$; by the definition of the product of partitions $a$ and $c$ cannot be both elements of $\rho_1$ or both elements of $\rho_2$ so let us assume that $a\in\rho_1$ and $c\in\rho_2$.

Suppose that $a\in\pi^1_1$; then $c\notin\pi^2_1$ (otherwise $a$ and $c$ would be connected by $\tau$). It follows that there is an element of $\rho_2\setminus\pi^2_1$, namely $c$, which is connected by $\sigma$ with $a\in\pi_1^1$, and the latter element must be connected by $\sigma$ with the elements of $\pi^2_1$. This contradicts the definition of $\pi^1 \cdot \pi^2$. Therefore $a\notin\pi^1_1$ and similarly we show that $c\notin\pi^2_1$.

It follows that a tuple $a,b,c,d$ with $b=l_1+\cdots+l_m$, $d=l_1+\cdots+l_m+l'_1+\cdots+l'_n$ is the one required for $\sigma$ to be crossing. ◻
:::
