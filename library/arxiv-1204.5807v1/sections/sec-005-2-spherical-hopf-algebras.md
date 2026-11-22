---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-005-2-spherical-hopf-algebras
section_title: "Spherical Hopf algebras"
section_number: 2
pages: 5-7
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.917
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
[]{#sec:sph-hopf label="sec:sph-hopf"}

## Spherical Hopf algebras

The notion of *spherical Hopf algebra* was introduced in [@BaW-adv]: this is a pair $(H, \omega)$, where $H$ is a Hopf algebra and $\omega\in G(H)$ such that $$\begin{aligned}
\label{eq:omega-square-antipode}
{\mathcal S}^2(x) &= \omega x \omega^{-1}, & x&\in H, \\
\label{eq:omega-traza}
\operatorname{tr}_V(\vartheta \omega) &= \operatorname{tr}_V(\vartheta \omega^{-1}),  & \vartheta &\in \operatorname{End}_H(V), &&
\end{aligned}$$ for all $V\in \operatorname{Rep}H$. We say that $\omega\in G(H)$ is a *pivot* when it satisfies [\[eq:omega-square-antipode\]](#eq:omega-square-antipode){reference-type="eqref" reference="eq:omega-square-antipode"}; pairs $(H, \omega)$ with $\omega$ a pivot are called *pivotal Hopf algebras*. The pivot is not unique but it is determined up to multiplication by an element in the group $G(H) \cap Z(H)$. A *spherical element* is a pivot that fulfills [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"}.

The implementation of the square of the antipode by conjugation by a group-like, condition [\[eq:omega-square-antipode\]](#eq:omega-square-antipode){reference-type="eqref" reference="eq:omega-square-antipode"}, is easy to verify. For instance, $\omega$ should belong to the center of $G(H)$; thus, if this group is centerless, then [\[eq:omega-square-antipode\]](#eq:omega-square-antipode){reference-type="eqref" reference="eq:omega-square-antipode"} does not hold in $H$. Further, the failure of [\[eq:omega-square-antipode\]](#eq:omega-square-antipode){reference-type="eqref" reference="eq:omega-square-antipode"} is not difficult to remedy by adjoining a group-like element [@So Section 2]. Namely, given a Hopf algebra $H$, consider a cyclic group $\Gamma$ of order $\operatorname{ord}{\mathcal S}^2$ with a generator $g$; let $g$ act on $H$ as ${\mathcal S}^2$. Then the corresponding smash product $E(H) := H\# \Bbbk\Gamma$ is a Hopf algebra where [\[eq:omega-square-antipode\]](#eq:omega-square-antipode){reference-type="eqref" reference="eq:omega-square-antipode"} holds[^1].

Condition [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} is less apparent. If $H$ is a finite-dimensional Hopf algebra and $\omega\in H$ a pivot, then [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds in the following instances:

-   $\omega$ is an involution.

-   There exists a Hopf subalgebra $K$ of $H$ such that $\omega \in K$ and $(K, \omega)$ is spherical-- since $\operatorname{End}_H(V) \subset \operatorname{End}_K(V)$.

-   $H$ is ribbon, see Subsection [\[subsec:ribbon\]](#subsec:ribbon){reference-type="ref" reference="subsec:ribbon"}.

-   All finite-dimensional $H$-modules are naturally self-dual.

::: proof
*Proof.* By hypothesis, there exists a natural isomorphism $F:\operatorname{id}\rightarrow {}^*$. Let $V\in\operatorname{Rep}H$ and $\vartheta\in\operatorname{End}_H(V)$. Then $$\begin{aligned}
\operatorname{tr}(\vartheta\omega)&=\sum_i\langle\alpha_i,\vartheta\omega v_i\rangle=\sum_i\langle\vartheta^*\alpha_i,\omega v_i\rangle=\sum_i\langle F_V\vartheta F_V^{-1}\alpha_i,\omega v_i\rangle\\
&=\sum_i\langle F_V\vartheta\omega^{-1} F_V^{-1}\alpha_i, v_i\rangle=\operatorname{tr}(F_V\vartheta\omega^{-1} F_V^{-1})=\operatorname{tr}(\vartheta\omega^{-1}).
\end{aligned}$$ Here $\{v_i\}$ and $\{\alpha_i\}$ are dual basis of $V$ and $V^*$ respectively. ◻
:::

::: prop
[]{#prop:reduccion a irreducibles label="prop:reduccion a irreducibles"} A pivotal Hopf algebra $(H,\omega)$ is spherical if and only if [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds for all $S\in \operatorname{Irr}H$.
:::

::: proof
*Proof.* The Proposition follows from the following two claims.

::: claim
If [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds for $M_1,M_2\in \operatorname{Rep}H$, then it holds for $M_1\oplus M_2$.
:::

Indeed, let $h\in \operatorname{End}_H(M_1\oplus M_2)$. Let $\pi_j:M\to M_j$, $\iota_i:M_i\to
M$ be the projection and the inclusion, for $1\leq i,j\leq 2$. Then $h=\sum_{1\leq i,j\leq
2}h_{ij}$, where $h_{ij}=\pi_i\circ h\circ \iota_j\in \operatorname{Hom}_H(M_j,M_i)$. In particular, $h_{ij}\omega=(h\omega)_{ij}$ as linear maps. Now, we have that $\operatorname{tr}_M(h)=\operatorname{tr}_{M_1}(h_{11})+\operatorname{tr}_{M_2}(h_{22})$ and thus $$\begin{aligned}
 \operatorname{tr}_M(h\omega)&=\operatorname{tr}_{M_1}(h\omega)_{11}+\operatorname{tr}_{M_2}(h\omega)_{22}=\operatorname{tr}_{M_1}(h_{11}\omega)
+\operatorname{tr}_{M_2}(h_{22}\omega)\\
&=\operatorname{tr}_{M_1}(h_{11}\omega^{-1})+\operatorname{tr}_{M_2}(h_{22}\omega^{-1})=\operatorname{tr}_{M_1
}(h\omega^{-1})_{11}+\operatorname{tr}_{M_2}(h\omega^{-1})_{22}\\
&=\operatorname{tr}_M(h\omega^{-1}).
\end{aligned}$$

::: claim
If [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds for every semisimple $H$-module, then $H$ is spherical.
:::

Let $M\in\operatorname{Rep}H$ and let $M_0\subset M_1\subset\dots\subset
M_k=M$ be the *Loewy filtration* of $M$, that is $M_0=\operatorname{Soc}M$, $M_{i+1}/M_i \simeq \operatorname{Soc}(M/M_i)$, $i=0,\dots,
j-1$. In particular, $M_{i+1}/M_i$ is semisimple. We prove the claim by induction on the Loewy length $k$ of $M$. The case $k=0$ is the hypothesis. Assume $k>0$; set $S=\operatorname{Soc}M$ and consider the exact sequence $0\to S\to M\to M/S\to 0$. Hence the Loewy length of $\widetilde M=M/S$ is $k-1$ and thus [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds for it. Also, [\[eq:omega-traza\]](#eq:omega-traza){reference-type="eqref" reference="eq:omega-traza"} holds for $S$ by hypothesis. Let $f\in
\operatorname{End}_H(M)$, then $f(S)\subseteq S$ and thus $f$ induces $f_1=f_{|S}\in\operatorname{End}_H(S)$ by restriction and factorizes through $f_2\in \operatorname{End}_H(\widetilde M)$. Therefore, we can choose a basis of $S$ and complete it to a basis of $M$ in such a way that $f$ in this new basis is represented by $[f]=\left[\begin{smallmatrix}
                                   [f_1]&*\\
                                   0&[f_2]
                                  \end{smallmatrix}\right]$. Also, as $\omega$ preserves $S$ and $f$ is an $H$-morphism, it follows that $[f\omega]=\left[\begin{smallmatrix}
                                   [f_1\omega]&*\\
                                   0&[f_2\omega]
                                  \end{smallmatrix}\right]$ and thus $\operatorname{tr}_M(f\omega)=\operatorname{tr}_M(f\omega^{-1})$. ◻
:::

::: Ex
Let $H$ be a basic Hopf algebra, i. e. all finite-dimensional simple modules have dimension 1; when $H$ itself is finite-dimensional, this amounts to the dual of $H$ being pointed. If $\omega\in G(H)$ is a pivot, then $H$ is spherical if and only if $\chi(\omega) \in \{\pm 1\}$ for all $\chi\in \operatorname{Alg}(H, \Bbbk)$. Assume that $H$ is finite-dimensional; then $H$ is spherical if and only if $\omega$ is involutive. For, $\omega -\omega^{-1}\in \bigcap_{\chi\in \operatorname{Alg}(H, \Bbbk)}\operatorname{Ker}\chi = \operatorname{Rad}H$, and $\operatorname{Rad}H \cap \Bbbk[\omega] = 0$.
:::

[^1]: If $H$ has finite dimension $n\in {\mathbb N}$, then the order of ${\mathcal S}^2$ is finite; in fact, it divides $2n$, by Radford's formula on ${\mathcal S}^4$ and the Nichols-Zöller Theorem.
