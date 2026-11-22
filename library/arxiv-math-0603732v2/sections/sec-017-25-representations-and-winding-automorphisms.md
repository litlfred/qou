---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-017-25-representations-and-winding-automorphisms
section_title: "Representations and winding automorphisms"
section_number: 2.5
pages: 8-9
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.973
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.5 label="xxsec2.5"}

Let $G(A^\circ)$ be the group of group-like elements of the Hopf dual $A^\circ$ of the Hopf algebra $A$; that is, $G(A^\circ)$ is the set of algebra homomorphisms from $A$ to $k$, which is a group under multiplication in $A^\circ$, namely, convolution of maps, $\pi\ast \pi':=
m_A (\pi\otimes \pi')\Delta$, with identity element the counit $\epsilon$. When $A$ is noetherian and is known to be AS-Gorenstein, so that the left integral $\textstyle \int^l$ of $A$ exists as explained in ([\[xxsec1.3\]](#xxsec1.3){reference-type="ref" reference="xxsec1.3"}), we denote by $\pi_0 \in
G(A^\circ)$ the canonical map $$\pi_0\; : \; A\to A/\text{r.ann}(\textstyle \int^l).$$ Given $\pi \in G(A^\circ)$, let $\Xi^{\ell}[\pi]$ denote the *left winding automorphism* of $A$ defined by $$\Xi^{\ell}[\pi](a)\; =\; \sum \pi(a_1) a_2$$ for $a\in A$. Similarly, let $\Xi^r[\pi]$ denote the *right winding automorphism* of $A$ defined by $$\Xi^r[\pi](a)\;=\; \sum a_1\pi(a_2).$$ Since the right winding automorphism will not be used often we simplify $\Xi^{\ell}[\pi]$ to $\Xi[\pi]$ and call $\Xi[\pi]$ the winding automorphism associated to $\pi$. It is easy to see that the inverse of $\Xi[\pi]$ is $$(\Xi[\pi])^{-1}\;=\; \Xi[\pi S];$$ moreover, $\Xi[\epsilon] =\operatorname{id}_A$, and the map $\Xi:
\pi \longrightarrow \Xi[\pi]$ is an antihomomorphism of groups $G(A^\circ) \longrightarrow \mathop{\mathrm{Aut}}_{k\text{-}\mathrm{alg}}(A)$. When $\pi_0$ exists, we shall write $$\begin{aligned}
{\xi}\;:=\; \Xi[\pi_0].
\end{aligned}$$

Given an algebra automorphism (or even an algebra endomorphism) $\sigma$ of $A$, we define $\Pi[\sigma]$ to be the map $\epsilon \sigma:A\to k$. Since $\epsilon  S=\epsilon$, $$\Pi[S^2]\;=\; \Pi[\operatorname{id}_A]\;=\; \epsilon.$$ Since, in general, $S^2\neq \operatorname{id}_A,$ it follows that in general $\Xi[\Pi[\sigma]]\neq \sigma$.

Here is a collection of elementary facts about the notations introduced above.

::: lemma
Let $A$ be a Hopf algebra, let $\pi,\phi \in G(A^\circ)$ and let $\sigma \in \mathop{\mathrm{Aut}}_{k\text{-}\mathrm{alg}}(A)$.

1.  $\Pi[\Xi[\pi]]=\pi$. In particular, $\Pi$ is a surjective map from $\mathop{\mathrm{Aut}}_{k\text{-}\mathrm{alg}}(A)$ to $G(A^\circ)$.

2.  $\Xi[\Pi[\Xi[\pi]]]=\Xi[\pi]$.

3.  $\pi  S^2=\pi$ and so $\Xi[\pi S^2]=\Xi[\pi]$.

4.  $\Xi[\pi] S^2=S^2  \Xi[\pi]$. In particular, if the left integral of $A$ exists then ${\xi}S^2=S^2 {\xi}$.
:::

::: proof
*Proof.* These are straightforward calculations, so the proofs are omitted. ◻
:::
