---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-008-33-pointed-simplicial-sets-and-modules
section_title: "Pointed simplicial sets and modules"
section_number: 3.3
pages: 22-25
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.971
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
·[]{#SS:modules label="SS:modules"} In this section we quickly explain how to add an $A$-module $M$ to the story developed in Section [\[S:inftyfunctor\]](#S:inftyfunctor){reference-type="ref" reference="S:inftyfunctor"}.

Let $A$ be a CDGA and recall from Example [\[E:Amod\]](#E:Amod){reference-type="ref" reference="E:Amod"} the $(\infty,1)$-category $A\textit{-}Mod_\infty$ induced by the (model category) $A\textit{-}Mod$ of $A$-modules. Similarly, the model category of pointed simplicial sets yields the $(\infty,1)$-category ${sSet_\infty}_*$ of pointed simplicial sets (Example [\[E:hsset\]](#E:hsset){reference-type="ref" reference="E:hsset"}).

Since the inclusion $pt_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ is always a cofibration, the canonical equivalence $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M) \cong M\otimes_{A} CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$ given by Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"} implies that $$\label{eq:Mderivedtensor} CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M) \;\cong \;M\mathop{\otimes}^{\mathbb{L}}_{A} CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A) \;\cong \;  M\!\!\mathop{\otimes}^{\mathbb{L}}_{CH_{pt_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)} CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A).$$ naturally in $A\textit{-}Mod_\infty$ and $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$.

Proposition [\[P:tensor\]](#P:tensor){reference-type="ref" reference="P:tensor"}, Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"}, Proposition [\[P:product\]](#P:product){reference-type="ref" reference="P:product"}, Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"} and its proof imply

::: theorem
[]{#T:Mderivedfunctor label="T:Mderivedfunctor"} The Hochschild chain lifts as a bifunctor of $(\infty,1)$-categories $CH_{(-)}(A,-): {sSet_\infty}_* \times A\textit{-}Mod_\infty \to A\textit{-}Mod_\infty$ which satisfies the following axioms

1.  **value on a point:** there is a natural equivalence $CH_{pt_{\scriptstyle\bullet}}^\bullet(A,M)\cong M$ in $A\textit{-}Mod_\infty$.

2.  **action of $CH$:** $CH^{\scriptstyle\bullet}_{X_{\scriptstyle\bullet}}(A,M)$ is naturally a $CH^{\scriptstyle\bullet}_{X_{\scriptstyle\bullet}}(A)$-module, *i.e.*, the Hochschild chain lifts as an $(\infty,1)$-functor $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,-):A\textit{-}Mod_\infty \to CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$.

3.  **bimonoidal:** there is an natural equivalence $$CH_{X_{\scriptstyle\bullet}\coprod Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)\cong CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M) \otimes CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$$ in $A\textit{-}Mod_\infty$ as well as in $CH_{X_{\scriptstyle\bullet}\coprod Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$, for any pointed simplicial set $X_{\scriptstyle\bullet}$ and simplicial set $Y_{\scriptstyle\bullet}$. For $M\in A\textit{-}Mod_\infty$ and $N\in B\textit{-}Mod_\infty$, there is an natural equivalence $$CH_{X_{\scriptstyle\bullet}}^{\scriptstyle\bullet}(A\otimes B, M\otimes N)\cong CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M) \otimes  CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(B,N)$$ in $A\otimes B\textit{-}Mod_\infty$ and $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A\otimes B)\textit{-}Mod_\infty$.

4.  **locality:** let $f:Z_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ and $g:Z_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ be maps in $sSet_\infty*$. There is an natural equivalence $$CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}\bigcup^{h}_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}}(A,M\otimes^{\mathbb{L}}_{A} N)\cong CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A,M)\otimes_{CH^{{\scriptstyle\bullet}}_{Z_{\scriptstyle\bullet}}(A)}^{\mathbb{L}} CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,N)$$ in $A\textit{-}Mod_\infty$ and $CH_{X_{\scriptstyle\bullet}\bigcup^{h}_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$. If $N=A$, then only $X_{\scriptstyle\bullet}$ needs to be pointed and the maps may be in $sSet_\infty$.

5.  **product:** Let $X_{\scriptstyle\bullet}$, $Y_{\scriptstyle\bullet}$ be pointed simplicial sets. There is an natural equivalence $$CH_{X_{\scriptstyle\bullet}\times Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M) \stackrel{\sim}\to CH_{X_{\scriptstyle\bullet}}^{\scriptstyle\bullet}\left( CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A), CH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M))\right)$$ in $A\textit{-}Mod_\infty$ and $CH_{X_{\scriptstyle\bullet}\times Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$.
:::

Note that from the point Axiom **(1)** and the locality Axiom **(4)** applied to the canonical maps $pt_{\scriptstyle\bullet}\to pt_{\scriptstyle\bullet}$ and $pt_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ (given by the base point of $X_{\scriptstyle\bullet}$) follows immediately the equivalence [\[eq:Mderivedtensor\]](#eq:Mderivedtensor){reference-type="eqref" reference="eq:Mderivedtensor"} above. This property actually implies that Axioms **(1)**, **(2)** and **(4)** characterize $CH_{(-)}(A,-)$:

::: proposition
[]{#P:Mderiveduniqueness label="P:Mderiveduniqueness"} Let $G: A\textit{-}Mod_\infty \to A\textit{-}Mod_\infty$ be an $(\infty,1)$-functor and let $\mathcal{M}:{sSet_\infty}_* \times A\textit{-}Mod_\infty \to A\textit{-}Mod_\infty$ be any $(\infty,1)$-bifunctor which satisfies the following axioms

i\)

:   **value on a point:** there is a natural equivalence $\mathcal{M}(pt_{\scriptstyle\bullet},M) \cong G(M)$ naturally in $A\textit{-}Mod_\infty$.

ii\)

:   **action of $CH$:** $\mathcal{M}(X_{\scriptstyle\bullet},M)$ is naturally a $CH_{X_{\scriptstyle\bullet}}(A)$-module.

iii\)

:   **locality:** Given maps $f:Z_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ and $g:Z_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ with $X_{\scriptstyle\bullet}$ a pointed simplicial set, There is a natural equivalence ( in $A\textit{-}Mod_\infty$) $$\mathcal{M}(X_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}}^h Y_{\scriptstyle\bullet},M)\cong \mathcal{M}(X_{\scriptstyle\bullet},M)\otimes_{CH^{{\scriptstyle\bullet}}_{Z_{\scriptstyle\bullet}}(A)}^{\mathbb{L}} CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A)$$

Then $\mathcal{M}$ is naturally equivalent to $CH_{(-)}(A,G(-))$ as an $(\infty,1)$-bifunctor.
:::

Note that Axiom **ii)** is needed to make sense of Axiom **iii)**.

::: proof
*Proof.* Let $Y_{\scriptstyle\bullet}$ be in ${sSet}_*$ and $g:pt_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ be the structure map. The locality axiom for the pushout $pt_{\scriptstyle\bullet}\leftarrow pt_{\scriptstyle\bullet}\stackrel{g}\to Y_{\scriptstyle\bullet}$ (where we take $X_{\scriptstyle\bullet}=pt_{\scriptstyle\bullet}$) gives natural equivalences $$\mathcal{M}(X_{\scriptstyle\bullet},M) \;\cong \;\mathcal{M}(pt_{\scriptstyle\bullet},M) \! \mathop{\otimes}^{\mathbb{L}}_{CH_{pt_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)}  \! CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\;\cong \;G(M) \! \mathop{\otimes}^{\mathbb{L}}_{CH_{pt_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)} \! CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$$ where the last equivalence follows from Axiom **i)**. The result now follows from the natural equivalences [\[eq:Mderivedtensor\]](#eq:Mderivedtensor){reference-type="eqref" reference="eq:Mderivedtensor"}. ◻
:::

One can specialize the locality Axiom **(4)** in Theorem [\[T:Mderivedfunctor\]](#T:Mderivedfunctor){reference-type="ref" reference="T:Mderivedfunctor"} a bit more by considering a pointed simplicial set $Z_{\scriptstyle\bullet}$ and pointed maps $f:Z_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ and $g:Z_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$. In that case, $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$ and $CH_{Y_{\scriptstyle\bullet}}(A,N)$ inherit natural $CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$-modules structures (induced by $f$ and $g$). Then Theorem [\[T:Mderivedfunctor\]](#T:Mderivedfunctor){reference-type="ref" reference="T:Mderivedfunctor"} yields a relative version of the Eilenberg-Moore spectral sequence.

::: corollary
[]{#C:MlocalitySpecSeq label="C:MlocalitySpecSeq"}Let $W_{\scriptstyle\bullet}\cong X_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}}^h Y_{\scriptstyle\bullet}$ be a homotopy pushout, there is an natural equivalence $$CH_{X_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}}^h Y_{\scriptstyle\bullet}}^{\scriptstyle\bullet}\Big(A, M\mathop{\otimes}^{\mathbb{L}}_A N\Big) \;\cong \; CH^{{\scriptstyle\bullet}}_{X_{\scriptstyle\bullet}}(A,M)\mathop{\otimes}_{CH^{{\scriptstyle\bullet}}_{Z_{\scriptstyle\bullet}}(A)}^{\mathbb{L}} CH^{{\scriptstyle\bullet}}_{Y_{\scriptstyle\bullet}}(A,N)$$ in $A\textit{-}Mod_\infty$ and $CH_{X_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}}^h Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\textit{-}Mod_\infty$.

In particular there is a natural strongly convergent spectral sequence of cohomological type of the form $$E_2^{p,q}:= {Tor}_{p,q}^{HH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)}\left(HH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M),HH_{Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,N)\right) \Longrightarrow HH_{W_{\scriptstyle\bullet}}^{p+q}\Big(A, M\mathop{\otimes}_A^{\mathbb{L}} N\Big)$$ where $q$ is the *internal* grading. The spectral sequence is furthermore a spectral sequence of differential $HH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)$-modules.
:::

Recall that we are considering a cohomological grading; thus the spectral sequence lies in the left half-plane with respect to this grading (and $p$ is negative).

::: proof
*Proof.* Let $\widehat{M}\to M$ be a cofibrant replacement of $M$ in $A\textit{-}Mod$, $\widehat{X}_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ a fibrant replacement of $X_{\scriptstyle\bullet}$ and $\widehat{f}:Z_{\scriptstyle\bullet}\to \widehat{X}_{\scriptstyle\bullet}$ be a cofibration lifting $f$. By Theorem [\[T:Mderivedfunctor\]](#T:Mderivedfunctor){reference-type="ref" reference="T:Mderivedfunctor"}, we have $CH_{W_{\scriptstyle\bullet}}\Big(A,M\mathop{\otimes}^{\mathbb{L}}_A N\Big)\cong CH_{W_{\scriptstyle\bullet}}\Big(A,\widehat{M}\otimes_A N\Big)$ (in $CH_{W_{\scriptstyle\bullet}}(A)\text{-}Mod$) and $$CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)\cong CH_{\widehat{X}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,\widehat{M})\cong \widehat{M}\otimes_A CH_{\widehat{X}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A).$$ Since $\widehat{f}:Z_{\scriptstyle\bullet}\to \widehat{X}_{\scriptstyle\bullet}$ is a degree wise injection, it suffices to prove that $$CH_{\widehat{X}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\mathop{\otimes}_{CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)} CH_{Y_{\scriptstyle\bullet}}(A,N) \cong CH_{\widehat{X}_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,N)$$ as a $CH_{\widehat{X}_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\cong CH_{\widehat{X}_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)\mathop{\otimes}_{CH_{Z_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A)} CH_{Y_{\scriptstyle\bullet}}(A)$-module which is Proposition [\[P:pushout\]](#P:pushout){reference-type="ref" reference="P:pushout"}. Now the spectral sequence is obtained as in the proof of Corollary [\[C:HlocalitySpecSeq\]](#C:HlocalitySpecSeq){reference-type="ref" reference="C:HlocalitySpecSeq"} (using Theorem [\[T:Mderivedfunctor\]](#T:Mderivedfunctor){reference-type="ref" reference="T:Mderivedfunctor"} instead of Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"}). ◻
:::

::: example
If $X_{\scriptstyle\bullet}$, $Y_{\scriptstyle\bullet}$ and $Z_{\scriptstyle\bullet}$ are contractible, the spectral sequence in Corollary [\[C:MlocalitySpecSeq\]](#C:MlocalitySpecSeq){reference-type="ref" reference="C:MlocalitySpecSeq"} boils down to the usual Eilenberg-Moore spectral sequence $${Tor}_{p,q}^{H^{\scriptstyle\bullet}(A)}\Big(H^{\scriptstyle\bullet}(M), H^{{\scriptstyle\bullet}}(N)\Big)\Longrightarrow H^{p+q}\Big(M\otimes_A^{\mathbb{L}} N\Big)$$ of differential $H^{\scriptstyle\bullet}(A)$-modules (see [@KM]).
:::

::: remark
[]{#R:2othersSpecSeq label="R:2othersSpecSeq"} Besides the Eilenberg Moore spectral sequence [\[C:MlocalitySpecSeq\]](#C:MlocalitySpecSeq){reference-type="ref" reference="C:MlocalitySpecSeq"}, there is also an Atiyah-Hirzebruch kind of spectral sequence for higher Hochschild chains: the skeletal filtration of a simplicial set $X_{\scriptstyle\bullet}$ induces a decreasing filtration $\cdots \supset F^{p} \cdots \supset F^{-1} \supset F^{0} \supset \{0\}$ of $CH_{X_{\scriptstyle\bullet}}^{{\scriptstyle\bullet}}(A,M)$, where $F^{p}:=\bigoplus_{n\leq -p} CH_{X_n}^{{\scriptstyle\bullet}}(A,M)$.

This filtration yields a left half-plane spectral sequence of cohomological type with exiting differential and further, the cohomology of the associated graded $\bigoplus_{p} F^p/F^{p+1}$ is the Hochschild chain complex over $X_{\scriptstyle\bullet}$ of the CGA $H^{\scriptstyle\bullet}(A)$ with value in $H^{\scriptstyle\bullet}(M)$. Hence we get from [@Bo]:

::: proposition
[]{#P:AHSpecSeq label="P:AHSpecSeq"} There is a strongly convergent spectral sequence of cohomological type $$E^2_{p,q}:= HH_{X_{\scriptstyle\bullet}}^{p+q}(H^{\scriptstyle\bullet}(A),H^{\scriptstyle\bullet}(M))^q \Longrightarrow HH_{X_{\scriptstyle\bullet}}^{p+q}(A,M)$$ where $q$ is the internal degree. If $M=A$, this is a spectral sequence of CDGAs.
:::

For the sake of completeness, we also mention that there is another spectral sequence to compute higher Hochschild due to Pirashvili which is the Grothendieck spectral sequence associated to the composition of functors $X_{\scriptstyle\bullet}\mapsto k_{X_{\scriptstyle\bullet}}\mapsto k_{X_{\scriptstyle\bullet}}\otimes_{\Gamma}^{\mathbb{L}}\mathcal{L}(A)$ that was defined in Proposition [\[P:homologyinvariance\]](#P:homologyinvariance){reference-type="ref" reference="P:homologyinvariance"}. See [@P Theorem 2.4] for details.
:::
