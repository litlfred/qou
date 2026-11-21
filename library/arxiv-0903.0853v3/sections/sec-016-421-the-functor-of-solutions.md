---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-016-421-the-functor-of-solutions
section_title: "The functor of solutions"
section_number: 4.2.1
pages: 20-22
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.947
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsubsection:functorofsolutions label="subsubsection:functorofsolutions"}

It is customary in ${\mathcal{D}}$-module theory to call *solution* of $M$ a morphism $M \rightarrow \underline{1}$. Indeed, a solution of ${\mathcal{D}}/{\mathcal{D}}P$ is then an element of $\text{Ker~}P$. We took the dual convention, yielding a *covariant* ${\mathbf C}$-linear left exact functor $\Gamma$ for the following reason. To any analytic $q$-difference module $M = ({{\mathbf C}(\{z\})}^{n},\Phi_{A})$, one can associate a holomorphic vector bundle $F_{A}$ over the elliptic curve (or complex torus) ${\mathbf{E}_{q}}:= {\mathbf C}^{*}/q^{{\mathbf Z}}$ in such a way that the space of global sections of $F_{A}$ can be identified with $\Gamma(M)$. We thus think of $\Gamma$ as a functor of global sections, and, the functor $M \leadsto F_{A}$ being exact, the $\Gamma^{i}$ can be defined through sheaf cohomology.\
There is an interesting relationship between the space $\Gamma(M) = \text{Hom}(\underline{1},M)$ of solutions of $M$ and the space $\Gamma(M^{\vee}) = \text{Hom}(M,\underline{1})$ of "cosolutions" of $M$. Starting from a unitary entire (analytic or formal) $q$-difference operator $P = \sigma_q^{n} + a_{1} \sigma_q^{n-1} + \cdots + a_{n} \in {{\mathcal{D}}_{q}}$, one studies the solutions of the $q$-difference equation: $$P.f := \sigma_q^{n} f + a_{1} \sigma_q^{n-1} f + \cdots + a_{n} f = 0$$ by vectorializing it into the form: $$\sigma_qX = A X, \text{~where~} 
X = \begin{pmatrix} f \\ \sigma_qf \\ \vdots \\ 
\sigma_q^{n-2} f \\ \sigma_q^{n-1} f \end{pmatrix}
\text{~and~}
A = \begin{pmatrix}
0 & 1 & 0 & \ldots & 0 \\
0 & 0 & 1 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \ldots & 1 \\
- a_{n} & - a_{n-1} & - a_{n-2} & - \ldots & - a_{1} 
\end{pmatrix}.$$ Solutions of $P$ then correspond to solutions of $M = ({{\mathbf C}(\{z\})}^{n},\Phi_{A})$ or $({{\mathbf C}((z))}^{n},\Phi_{A})$. Now, by lemma [\[lemm:cyclicvector\]](#lemm:cyclicvector){reference-type="ref" reference="lemm:cyclicvector"}, one has $M = {{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}Q$ for some unitary entire $q$-difference operator $Q$. Any such polynomial $Q$ is *dual* to $P$. An explicit formula for a particular dual polynomial is given in [@JSFIL prop. 2.1.10].\
From the derived functors $\Gamma^{i}(M) = \text{Ext}^{i}(\underline{1},M)$, one can recover general Ext-modules:

::: prop
[]{#prop:GammaetExt label="prop:GammaetExt"} There are functorial isomorphisms: $$\text{Ext}^{i}(M,N) \simeq \Gamma^{i}(M^{\vee} \otimes N).$$
:::

::: proof
*Proof.* The covariant functor $N \leadsto \text{Hom}(M,N)$ is obtained by composing the exact covariant functor $N \leadsto M^{\vee} \otimes N$ with the left exact covariant functor $\Gamma$. Moreover, considered as a left exact functor over ${Mod_{{\mathcal{D}}}}$, it is isomorphic to the functor $N \leadsto \underline{\text{Hom}}(M,N)$, which sends injective modules to injective modules. Indeed, the adjunction formula: $$\text{Hom}(P,\underline{\text{Hom}}(M,N)) \simeq \text{Hom}(P \otimes M,N)$$ makes sense and remains valid for arbitrary modules in ${Mod_{{\mathcal{D}}}}$ for definitions of tensor product and internal Hom in ${Mod_{{\mathcal{D}}}}$ similar to the ones given above: see theorem [\[theo:adjunction\]](#theo:adjunction){reference-type="ref" reference="theo:adjunction"} in paragraph [\[subsection:internalhom\]](#subsection:internalhom){reference-type="ref" reference="subsection:internalhom"} of section [\[section:ALDIFF\]](#section:ALDIFF){reference-type="ref" reference="section:ALDIFF"} of the appendix; and it implies that the flatness of $M$ over $K$ is enough to ensure the exactness of $P \leadsto \text{Hom}(P,\underline{\text{Hom}}(M,N))$ whenever $N$ is injective. One can then derive $N \leadsto \text{Hom}(M,N)$ using [@GM chap. III, §7, th. 1]. ◻
:::

::: rema
[]{#rema:fibrefunctors label="rema:fibrefunctors"} For any difference field extension $(K,\sigma)$ of $({{\mathbf C}(\{z\})},\sigma_q)$, the $K^{\sigma}$-vector space of solutions of $M$ in $K$ has dimension $\dim_{K^{\sigma}} \Gamma_{K}(M) \leq \text{rk~}M$: this follows from the $q$-wronskian lemma (*see* [@LDV]). One can show that the functor $\Gamma_{K}$ is a fibre functor if, and only if, $(K,\sigma)$ is a *universal field of solutions*, *i.e.* such that one always have the equality $\dim_{K^{\sigma}} \Gamma_{K}(M) = \text{rk~}M$. The field ${\mathcal{M}}({\mathbf C}^{*})$ of meromorphic functions over ${\mathbf C}^{*}$, with the automorphism $\sigma_q$, is a universal field of solutions, thus providing a fibre functor over ${\mathcal{M}}({\mathbf C}^{*})^{\sigma_q} = {\mathcal{M}}({\mathbf{E}_{q}})$ (field of elliptic functions). Actually, no subfield of ${\mathcal{M}}({\mathbf C}^{*})$ gives a fibre functor over ${\mathbf C}$ (this follows from the argument at the beginning of [@JSGAL 0.3]). In [@vdPS], van der Put and Singer use an algebra of symbolic solutions which is reduced but not integral. A transcendental construction of a fibre functor over ${\mathbf C}$ is described in [@RS1].
:::
