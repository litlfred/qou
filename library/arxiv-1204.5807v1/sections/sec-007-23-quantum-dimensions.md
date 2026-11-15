---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-007-23-quantum-dimensions
section_title: "Quantum dimensions"
section_number: 2.3
pages: 7-8
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.932
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
[]{#subsec:qdim label="subsec:qdim"}

The *quantum dimension* of an object $X$ in a spherical category ${\mathcal C}$ is given by $\operatorname{qdim}V := \operatorname{tr}_L(\operatorname{id}_X)$. In particular, if $H$ is a spherical Hopf algebra, then $$\begin{aligned}
\label{eq:qdim-sph-Ha}
\operatorname{qdim}M &= \operatorname{tr}_M(\omega) = \operatorname{tr}_M(\omega^{-1}), & M&\in \operatorname{Rep}H.
\end{aligned}$$

### 

If ${\mathcal C}$ is a spherical tensor category, then $\operatorname{End}({\bf 1})=\Bbbk$, and the function $V\mapsto \operatorname{qdim}V$ is a character of the Grothendieck ring of ${\mathcal C}$. In fact, this map is additive on exact sequences, as in the proof of Proposition [\[prop:reduccion a irreducibles\]](#prop:reduccion a irreducibles){reference-type="ref" reference="prop:reduccion a irreducibles"}; also $$\label{eq:qdim-producto tensorial}
\operatorname{qdim}V{\otimes}W=\operatorname{qdim}V \operatorname{qdim}W, \qquad V,W \in {\mathcal C}.$$ In consequence, the quantum dimension of any object in a *finite* spherical tensor category ${\mathcal C}$ is an algebraic integer in $\Bbbk$, see [@EGNO Corollary 1.38.6].

### 

Let $H$ be a Hopf algebra. Given $L\in \operatorname{Irr}H$, $M\in \operatorname{Rep}H$, we set $(M:L) =$ multiplicity of $L$ in $M$ (i. e. the number of times that $L$ appears as a Jordan-Hölder factor of $M$). Assume that $(H, \omega)$ is spherical. Let $M\in \operatorname{Rep}H$. Then $$\begin{aligned}
\label{eq:qdim-formula}
\operatorname{qdim}M &= \sum_{L\in \operatorname{Irr}H} (M:L)\operatorname{qdim}L.
\end{aligned}$$ Here is a way to compute the quantum dimension of $M$: consider the decomposition $M = \oplus_{\rho \in \operatorname{Irr}G(H)} M_\rho$ into isotypical components of the restriction of $M$ to $G(H)$. Since $\omega \in Z(G(H))$, it acts by a scalar $z_\rho$ on the $G(H)$-module affording $\rho \in \operatorname{Irr}G(H)$. Hence $$\begin{aligned}
\label{eq:qdim-formula-isotypical}
\operatorname{qdim}M &= \sum_{\rho \in \operatorname{Irr}G(H)} z_\rho \dim M_\rho.
\end{aligned}$$ See [@CW08; @CW10] for a Verlinde formula and other information on the computation of the quantum dimension in terms of the Grothendieck ring.

### 

If $H$ is a non-semisimple spherical Hopf algebra, then $\operatorname{qdim}M = 0$ for any $M \in \operatorname{Rep}H$ projective [@BaW-tams Proposition 6.10]. More generally, the following result appears in the proofs of [@EO 2.16], [@EGNO 1.53.1].

::: prop
[]{#prop:qdim-proyectivos label="prop:qdim-proyectivos"} Let ${\mathcal C}$ be a non-semisimple pivotal tensor category. Then $\operatorname{qdim}P=0$ for any projective object $P$. 0◻
:::
