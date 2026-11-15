---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-012-22-kirby-elements-and-quantum-invariants
section_title: "Kirby elements and quantum invariants"
section_number: 2.2
pages: 6-8
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.932
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-kirby label="sect-kirby"} As in the previous section, let $\mathcal{B}$ be a ribbon autonomous category with a coend $C$. In this setting, $\Bbbk=\mathrm{End}_\mathcal{C}(\mathbb{1})$ is a commutative monoid.

Let $L$ be a framed link in $S^3$ with $n$ components. There always exists a (non-unique) ribbon $n$-string link $T$ such that $L$ is isotopic to the closure of $T$. For $\alpha \in \mathrm{Hom}_\mathcal{C}(\mathbb{1},C)$, set $$\tau_\mathcal{B}(L;\alpha)=\phi_{T} \circ \alpha^{\otimes n} \in \Bbbk,$$ where $\phi_{T}\colon C^{\otimes n} \to \mathbb{1}$ is defined as above.

Following [@Vir], by a *Kirby element* of $\mathcal{B}$, we mean a morphism $\alpha \in \mathrm{Hom}_\mathcal{B}(\mathbb{1},C)$ such that, for any framed link $L$, $\tau_\mathcal{B}(L;\alpha)$ is well-defined and invariant under isotopies and 2-handle slides of $L$. A Kirby element $\alpha$ of $\mathcal{B}$ is said to be *normalizable* if $\tau_\mathcal{B}(\bigcirc^{+1};\alpha)$ and $\tau_\mathcal{B}(\bigcirc^{-1};\alpha)$ are invertible in $\Bbbk$, where $\bigcirc^{\pm 1}$ denotes the unknot with framing $\pm
1$.

By universality of the coaction $\delta$ of $C$ on objects of $\mathcal{C}$, we see that the twist $\theta_Y\colon Y \to Y$ of $\mathcal{B}$ and its inverse lead to morphisms $\theta^\pm_C \colon C \to \mathbb{1}$ such that: $$\theta_Y^{\pm 1}=(\mathrm{id}_Y \otimes \theta^\pm_C)\delta_Y.$$a If $\alpha$ is a Kirby element of $\mathcal{B}$, we have: $\tau_\mathcal{B}(\bigcirc^{\pm 1};\alpha)=\theta^\pm_C \alpha$, so that $\alpha$ is normalizable if and only if $\theta^\pm_C \alpha$ are invertible in $\Bbbk$.

Recall (see [@Li]) that every (closed, connected, oriented) 3-manifold can be obtained from $S^3$ by surgery along a framed link $L \subset S^3$. For any framed link $L$ in $S^3$, we will denote by $M_L$ the 3-manifold obtained from $S^3$ by surgery along $L$, by $n_L$ the number of components of $L$, and by $b_-(L)$ the number of negative eigenvalues of the linking matrix of $L$.

An immediate consequence of the Kirby theorem [@Ki] is that if $\alpha$ is a normalizable Kirby element of $\mathcal{B}$, then: $$\tau_\mathcal{B}(M_L;\alpha)=(\theta^+_C \alpha)^{b_-(L)-n_L}\,  (\theta^-_C \alpha)^{-b_-(L)} \; \tau_\mathcal{B}(L;\alpha)$$ is an invariant of 3-manifolds. Furthermore these invariants are multiplicative under the connected sum of 3- manifolds: $\tau_\mathcal{B}(M\# M';\alpha)=\tau_\mathcal{B}(M;\alpha)\,\tau_\mathcal{B}(M';\alpha)$.

Note that if $\alpha$ is a normalizable Kirby element and $k$ is an automorphism of $\mathbb{1}$, then $k\alpha$ is also a normalizable Kirby element. The normalization of the invariant $\tau_\mathcal{B}(M;\alpha)$ has been chosen so that $\tau_\mathcal{B}(M;k\alpha)=\tau_\mathcal{B}(M;\alpha)$.\
The question is now: how to determine the (normalizable) Kirby element of $\mathcal{B}$? A partial answer was given in [@Vir]. Denoting by $m_C$, $\Delta_C$, and $S_C$ respectively the product, coproduct, and antipode of the Hopf algebra $C$, we have:

::: thm
[]{#thmkirbel label="thmkirbel"} Any morphism $\alpha\colon\mathbb{1}\to C$ in $\mathcal{B}$ such that: $$S_C \alpha=\alpha \quad \text{and} \quad (m_C \otimes \mathrm{id}_C)(\mathrm{id}_C \otimes \Delta_C)(\alpha \otimes \alpha)=\alpha \otimes
\alpha$$ is a Kirby element of $\mathcal{B}$.
:::

For instance, the unit $u_C$ of $C$ is a normalizable Kirby element (its associated invariant is the trivial one).

A more interesting example of a a Kirby element is an $S$-invariant integral $\Lambda$ of $C$, that is, a morphism $\Lambda
\colon\mathbb{1}\to C$ such that $S_C(\Lambda)=\Lambda$ and $m_C(\Lambda \otimes \mathrm{id}_C)=\Lambda\, \varepsilon_C=m_C(\mathrm{id}_C \otimes
\Lambda)$, where $\varepsilon_C$ is the counit of $C$. For the existence of such integrals, we refer to [@BKLT]. If $\Lambda$ is normalizable, then the associated invariant is the Lyubashenko's one [@Lyu2], up to a different normalization.

Note that other Kirby elements exist in general (see [@Vir]).

::: rem
[]{#rem-invRT label="rem-invRT"} Assume $\mathcal{B}$ is a modular category in the sense of [@Tur2], that is, a ribbon fusion category with invertible $S$-matrix. Let $\{V_i\}_{i\in I}$ be a representative family of simple objects of $\mathcal{B}$. Then $\mathcal{B}$ admits a coend $C=\bigoplus_{i \in I} \leftidx{^\vee}{\!V}{}_i \otimes V_i$. Let $\phi_X\colon X \to \leftidx{^{\vee\vee}}{\!X}{}$ be the sovereign structure of $\mathcal{B}$ and set: $$\Lambda=\sum_{i \in I} \dim(V_i) \, (\mathrm{id}_{\leftidx{^\vee}{\!V}{}_i} \otimes \phi_i^{-1}) \mathrm{coev}_{V_i} \colon\mathbb{1}\to C,$$ Then $\Lambda$ is a $S_C$-invariant integral of $C$. Furthermore it is normalizable and its associated invariant is the Reshetikhin-Turaev one [@Tur2], up to a different normalization. More precisely, assuming $\dim \mathcal{B}=\sum_{i \in I}
\dim(V_i)^2$ has a square root $D$ in $\Bbbk$ (which is then invertible in this context), setting $\Delta_-=\theta^-_C
\Lambda$, and denoting by $b_1(M)$ the first Betti number of $M$, we have: $$\mathrm{RT}_\mathcal{B}(M) = D^{-1} \Bigl(\frac{D}{\Delta_-}\Bigr)^{b_1(M)} \, \tau_\mathcal{B}(M;\Lambda).$$ We will see in Section [\[sect-RT\]](#sect-RT){reference-type="ref" reference="sect-RT"} that, unlike $\mathrm{RT}_\mathcal{B}(M)$, $\tau_\mathcal{B}(M;\Lambda)$ may be still defined for ribbon categories $\mathcal{B}$ with $\dim \mathcal{B}=0$.
:::
