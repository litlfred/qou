---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-015-31-kazhdan-lusztigs-theory
section_title: "Kazhdan-Lusztig's theory"
section_number: 3.1
pages: 12-14
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.969
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
For the basic definitions of Hecke algebras and Kazhdan-Lusztig polynomials we follow [@SoKL]. Let $(W,S)$ be a Coxeter system.

::: defi
The *Hecke algebra* $\mathcal{H}$ of a Coxeter system $(W,S)$ is the $\mathbb{Z}[v,v^{-1}]-$algebra with generators $h_s$ for $s\in S$ and relations

-   $h_s^2= (v^{-1}-v)h_s +1$ (quadratic relation)

-   $\underbrace{h_sh_rh_s\ldots}_{m_{sr}}=\underbrace{h_rh_sh_r\ldots}_{m_{sr}}$ for all $s,r\in S$ (braid relation)
:::

When $v$ is replaced by $1$ in the definition, one obtains the algebra $\mathbb{Z}W$. Thus we can see the Hecke algebra as a deformation of the group algebra.

For any reduced expression $\underline{s}=sr\ldots t$ of an element $x\in W$ define the element $h_{\underline{s}}=h_sh_r\cdots h_t$. By the forementioned result of Matsumoto [@Ma] we know that $h_{\underline{s}}$ does not depend on the reduced expression ${\underline{s}}$, it just depends on $x$. We call this element $h_x$. We define $h_{e}=1$. The following is a basic lemma.

::: lem
[]{#Iwa label="Iwa"} The set $\{h_x\}_{x\in W}$ is a basis of $\mathcal{H}$ as a $\mathbb{Z}[v,v^{-1}]-$algebra, called the *standard basis*.
:::

The element $h_s$ has an inverse, namely $(h_s+v-v^{-1})$ as it is shown in the following calculation.

$$\begin{aligned}
h_s(h_s+v-v^{-1})&=&[(v^{-1}-v)h_s +1]+h_s(v-v^{-1})\nonumber\\
&=&1
\end{aligned}$$

This implies that $h_x$ has an inverse for every $x\in W.$ So we can define a $\mathbb Z$-module morphism $d:\mathcal{H}\rightarrow \mathcal{H}$ by the formula $d(v)=v^{-1}$ and $d(h_x)=(h_{x^{-1}})^{-1}.$ It is an exercice to prove that this is a ring morphism, and we call it the *duality* in the Hecke algebra.

Let us make a short calculation $$\begin{aligned}
\label{bs}
d(h_s+v)&=& (h_s)^{-1} +v^{-1}\nonumber\\
&=&(h_s+v-v^{-1})+v^{-1}\nonumber\\
&=& (h_s+v)
\end{aligned}$$

So we obtain our first example of self-dual element. The following theorem (see [@KL]) is the foundational theorem of Kazhdan-Lusztig theory.

::: thm
[]{#thKL label="thKL"} For every element $x\in W$ there is a unique self-dual element $b_x\in \mathcal{H}$ such that $$b_x\in h_x+\sum_{y\in W}v\Z[v]h_y.$$ The set $\{b_x\}_{x\in W}$ is a $\Z[v,v^{-1}]-$basis of $\mathcal{H},$ called the Kazhdan-Lusztig basis. If we write $b_x= h_x+\sum_{y\in W}h_{y,x}h_y$ then the Kazhdan-Lusztig polynomials $p_{y,x}$ are defined by the formula $p_{y,x}=v^{l(x)-l(y)}h_{y,x}.$
:::

::: remark
[]{#rem1 label="rem1"} We will prove in Section [\[proofth\]](#proofth){reference-type="ref" reference="proofth"} a stronger version of this theorem, namely that $$\label{KL}b_x\in h_x+\sum_{y<x}v\Z[v]h_y,$$ where $<$ refers to the Bruhat order.
:::

Before we prove this theorem we will believe it for a while and calculate the Kazhdan-Lusztig bases in some examples.
