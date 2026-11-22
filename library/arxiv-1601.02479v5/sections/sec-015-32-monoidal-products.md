---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-015-32-monoidal-products
section_title: "Monoidal products"
section_number: 3.2
pages: 28-32
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.97
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson– Thomas theory for Jacobi algebras and"
---
[]{#prodss label="prodss"} In this section we define and introduce the first properties of the categorification of the quantum torus from refined DT theory.

::: definition
[]{#lfDef label="lfDef"} Let $\mathcal{F}\in\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$ for $X$ a scheme. We say that $\mathcal{F}$ is *locally finite* if for each $Z\in \uppi\hspace{0.05em}_0(X)$

1.  for each $n\in\mathbb{Z}$, the element $\bigoplus_{i\in\mathbb{Z}}\mathop{\mathrm{Gr}}^W_{n}(\mathop{\mathrm{\mathcal{H}}}^i(\mathcal{F})|_Z)$ belongs to $\mathcal{D}^{b}(\mathop{\mathrm{MMHM}}(Z))$

2.  For $n\ll 0$, we have $\mathop{\mathrm{Gr}}^W_{n}(\mathop{\mathrm{\mathcal{H}}}^i(\mathcal{F})|_Z)=0$ for all $i\in\mathbb{Z}$.

Denote by $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(X))\subset\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(X))$ the full subcategory of locally finite objects.
:::

The category $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathbb{N}^{Q_0}))$ is going to play the role of the categorification of the motivic quantum torus of [@KS1 Sec.6.2]. For now we remark that this quantum torus is a power series ring with coefficients in $\mathbb{Z}((q^{1/2}))$ and variables $x^{\mathop{\mathrm{\mathbf{d}}}}$ for $\mathop{\mathrm{\mathbf{d}}}\in\mathbb{N}^{Q_0}$, and if $\upzeta$ is a generic stability condition then the subring of power series in variables $x^{\mathop{\mathrm{\mathbf{d}}}}$ for $\mathop{\mathrm{\mathbf{d}}}\in\Uplambda_{\upmu}^{\upzeta}$ is commutative, while the whole quantum torus in general is not. The categorification of this picture, then, should be a monoidal category, for which the monoidal product cannot be upgraded to a symmetric monoidal product, except on fixed subcategories indexed by the slope $\upmu$, for which we should define a symmetric monoidal product.

The moduli scheme $\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}$ carries a symmetric monoidal structure given by the direct sum, and the product $$\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\times \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\xrightarrow{\oplus}\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}$$ is a finite morphism of schemes (see [@Meinhardt14 Lem.2.1]). By Remark [\[convProdDef\]](#convProdDef){reference-type="ref" reference="convProdDef"} the category $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}))$ carries a monoidal product $$\mathcal{F}\boxtimes_{\oplus}\mathcal{G}\colonequals \oplus_*(\uppi\hspace{0.05em}_1^*\mathcal{F}\otimes\uppi\hspace{0.05em}_2^*\mathcal{G})$$ defined as in ([\[simmon\]](#simmon){reference-type="ref" reference="simmon"}).

::: proposition
[]{#biExp label="biExp"} The monoidal product $\boxtimes_{\oplus}$ is biexact and preserves the weight filtration.
:::

::: proof
*Proof.* Let $\mathcal{F}\in\mathop{\mathrm{MMHM}}(X)$ and $\mathcal{G}\in\mathop{\mathrm{MMHM}}(Y)$ for two algebraic varieties $X$ and $Y$. We define their external tensor product $$\mathcal{F}\boxtimes \mathcal{G}\colonequals (p\colon X\times Y\times\mathbb{A}^1\times\mathbb{A}^1\xrightarrow{\mathop{\mathrm{id}}_{X\times Y}\times +} X\times Y\times \mathbb{A}^1)_*(\mathop{\mathrm{pr}}_{1,3}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{2,4}^*\mathcal{G}).$$ as in Remark [\[convProdDef\]](#convProdDef){reference-type="ref" reference="convProdDef"}. Then by [@KS2 Lem.1], there is an isomorphism in $\mathcal{D}(\mathop{\mathrm{MMHM}}(X\times Y))$ $$p_!\left(\mathop{\mathrm{pr}}_{1,3}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{2,4}^*\mathcal{G}\right)\rightarrow p_*\left(\mathop{\mathrm{pr}}_{1,3}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{2,4}^*\mathcal{G}\right)$$ and so since $p_!\colon \mathcal{D}(\mathop{\mathrm{MHM}}(X\times \mathbb{A}^1\times Y\times\mathbb{A}^1))\rightarrow \mathcal{D}(\mathop{\mathrm{MHM}}(X\times Y\times \mathbb{A}^1))$ is left exact, and decreases weights, while $p_*$ is right exact and increases weights, we deduce that the external tensor product $$\boxtimes\colon \mathcal{D}(\mathop{\mathrm{MMHM}}(X))\times\mathcal{D}(\mathop{\mathrm{MMHM}}(Y))\rightarrow \mathcal{D}(\mathop{\mathrm{MMHM}}(X\times Y))$$ is exact and preserves weights. Since the map $\oplus\colon \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\times \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\rightarrow \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}$ is finite, the direct image functor $\oplus_*$ is exact and preserves weights. The result follows. ◻
:::

The monoidal unit in $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}))$ is $\mathbb{Q}_{{\mathcal{M}_0^{\upzeta\mathop{\mathrm{-ss}}}}}$, the constant pure Hodge module supported on $\mathcal{M}_0^{\upzeta\mathop{\mathrm{-ss}}}\cong \mathop{\mathrm{pt}}$, the unit of the monoid $\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}$.

We briefly summarize the results of Maxim, Saito and Schürmann [@MSS11], dealing with exterior products and symmetric group actions on mixed Hodge modules. Let $X_i$, $i\in I$ be a finite set of algebraic varieties, let $\mathcal{L}_i$ be objects of $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MHM}}(X_i))$ for each $i\in I$, and let $f_i\colon X_i\rightarrow Y_i$ be a set of morphisms of algebraic varieties. Set $f=\coprod_{i\in I}f_i$. While [@MSS11] treats the bounded derived category, and certainly it makes no sense to apply their results at the generality of the unbounded derived category, their arguments extend without modification to the case of the categories $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MHM}}(X_i))$. They show that external tensor product commutes with the direct image, that is, there is a natural isomorphism $$\boxtimes_{i\in I}f_{i,*}\mathcal{L}_i\cong f_*\left(\boxtimes_{i\in I}\mathcal{L}_i\right).$$ Furthermore, if $X_i=X$ for all $i$, and $Y_i=Y$ for all $i$, then there is an action of the symmetric group $\mathop{\mathrm{\mathfrak{S}}}_I$ on both external products, which is respected by the above natural isomorphism.

::: remark
This is the usual action, incorporating the Koszul sign rule --- when we consider cohomological Hall algebras later, we will have cause to modify this action, to express commutativity results for the cohomological Hall algebra. However, for the purposes of Theorems [\[ThmA\]](#ThmA){reference-type="ref" reference="ThmA"} and [\[CWCT\]](#CWCT){reference-type="ref" reference="CWCT"} we may equivalently use the default action of [@MSS11] as we are only interested in the isomorphism classes of underlying objects (see Proposition [\[underlying_same\]](#underlying_same){reference-type="ref" reference="underlying_same"}).
:::

Now let $\mathcal{L}_i=\mathcal{L}$ for all $i$, and let $I=\{1,\ldots,n\}$. The authors then define $\mathop{\mathrm{Sym}}^n(\mathcal{L})\colonequals (\varpi_*\boxtimes^n\!\mathcal{L})^{\mathop{\mathrm{\mathfrak{S}}}_n}$, where $\varpi\colon X^n\rightarrow \mathop{\mathrm{Sym}}^nX$ is the natural map, and show that there is a canonical isomorphism $$\mathop{\mathrm{H}}(\mathop{\mathrm{Sym}}^n X,\mathop{\mathrm{Sym}}^n\mathcal{L})\cong \mathop{\mathrm{Sym}}^n(\mathop{\mathrm{H}}(X,\mathcal{L})).$$ Furthermore, they show that the Kunneth isomorphism $$\mathop{\mathrm{H}}(X^n,\boxtimes^n\mathcal{L})\cong \bigotimes^n\mathop{\mathrm{H}}(X,\mathcal{L})$$ is an isomorphism of $\mathop{\mathrm{\mathfrak{S}}}_n$-representations.

Now let $\mathcal{L}\in \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(X))$. Since there is a commutative diagram $$\xymatrix{
(X\times \mathbb{A}^1)^n\ar[d]_{\varpi_{X\times\mathbb{A}^1}}\ar[r]^-{\mathop{\mathrm{id}}_X^n\times +}&X^n\times\mathbb{A}^1\ar[d]^{\varpi_X\times \mathop{\mathrm{id}}_{\mathbb{A}^1}}\\
\mathop{\mathrm{Sym}}^n(X\times\mathbb{A}^1)\ar[r]^r&\mathop{\mathrm{Sym}}^nX\times\mathbb{A}^1
}$$ we obtain a $\mathop{\mathrm{\mathfrak{S}}}_n$-action on $\varpi_{X,*}(\boxtimes^n\mathcal{L})$ by taking $r_*$ of the action defined in [@MSS11], and we can define $\mathop{\mathrm{Sym}}^n\!\mathcal{L}$ to be the $\mathop{\mathrm{\mathfrak{S}}}_n$-invariant summand. Similarly, we define the functor $$\begin{aligned}
\mathop{\mathrm{Sym}}^n_{\boxtimes_{\oplus}}\colon&\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}))\rightarrow \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}))\\
&\mathcal{F}\mapsto (\oplus_*\mathcal{F}^{\boxtimes n})^{\mathop{\mathrm{\mathfrak{S}}}_n}.
\end{aligned}$$ We then define $$\begin{aligned}
\label{symdef}
\mathop{\mathrm{Sym}}_{\boxtimes_{\oplus}}\colon&\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\upmu}\setminus \mathcal{M}_0^{\upzeta\mathop{\mathrm{-ss}}}))\rightarrow \mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\upmu}))\\ \nonumber
&\mathcal{F}\mapsto\bigoplus_{n\geq 0}\mathop{\mathrm{Sym}}^n_{\boxtimes_{\oplus}}\mathcal{F}.
\end{aligned}$$ This functor is well defined, since $$\uppi\hspace{0.05em}_0(\oplus)\colon \uppi\hspace{0.05em}_0(\mathcal{M})\times\uppi\hspace{0.05em}_0(\mathcal{M})\rightarrow\uppi\hspace{0.05em}_0(\mathcal{M})$$ has finite fibers. The same fact implies the following lemma:

::: lemma
[]{#lfRem label="lfRem"} The functor ([\[symdef\]](#symdef){reference-type="ref" reference="symdef"}) restricts to a functor $$\mathop{\mathrm{Sym}}_{\boxtimes_{\oplus}}\colon\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\upmu}\setminus \mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_0))\rightarrow \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\upmu})).$$
:::

::: proposition
[]{#symmPure label="symmPure"} The functor $\mathop{\mathrm{Sym}}_{\boxtimes_{\oplus}}$ takes pure objects to pure objects.
:::

::: proof
*Proof.* Let $\mathcal{F}\in\mathop{\mathrm{MMHM}}(\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}})$ be pure. Let $$\oplus^n\colon \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\times\ldots\times \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}\rightarrow \mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}$$ be the n-fold monoid map. Then $\oplus^n$ is finite by [@Meinhardt14 Lem.2.1], and so $$\mathcal{G}=\oplus^n_*\left(\mathcal{F}\boxtimes\ldots \boxtimes\mathcal{F}\right)\in\mathop{\mathrm{MMHM}}(\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}})$$ is pure. On the other hand, $\mathop{\mathrm{Sym}}_{\boxtimes_{\oplus}}^n\mathcal{F}\subset \mathcal{G}$ is the isotrivial direct summand under the $\mathop{\mathrm{\mathfrak{S}}}_n$-action, and is therefore pure. We deduce that $\mathop{\mathrm{Sym}}_{\boxtimes_{\oplus}}\mathcal{F}$ is a direct sum of pure objects, and is therefore pure. ◻
:::

We define a new monoidal structure on $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}))$ by setting $$\mathcal{F}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{G}\colonequals \bigoplus_{\mathop{\mathrm{\mathbf{d}}}',\mathop{\mathrm{\mathbf{d}}}''\in\mathbb{N}^{Q_0}} \mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}'',\mathop{\mathrm{\mathbf{d}}}'\rangle/2}\otimes\left(\oplus_*(\mathcal{F}_{\mathop{\mathrm{\mathbf{d}}}'}\boxtimes\mathcal{G}_{\mathop{\mathrm{\mathbf{d}}}''})\right),$$ where $\mathcal{F}=\bigoplus_{\mathop{\mathrm{\mathbf{d}}}'\in\mathbb{N}^{Q_0}}\mathcal{F}_{\mathop{\mathrm{\mathbf{d}}}'}$ for $\mathcal{F}_{\mathop{\mathrm{\mathbf{d}}}'}\in\mathcal{D}(\mathop{\mathrm{MMHM}}(\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}'}^{\upzeta\mathop{\mathrm{-ss}}}))$ and $\mathcal{G}=\bigoplus_{\mathop{\mathrm{\mathbf{d}}}''\in\mathbb{N}^{Q_0}}\mathcal{G}_{\mathop{\mathrm{\mathbf{d}}}''}$ for $\mathcal{G}_{\mathop{\mathrm{\mathbf{d}}}''}\in\mathcal{D}(\mathop{\mathrm{MMHM}}(\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}''}^{\upzeta\mathop{\mathrm{-ss}}}))$. Since we are twisting by a pure twist, this monoidal product again preserves weights. If $\upzeta$ is $\upmu$-generic, the restriction of $\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}$ to $\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\upmu}))$ is naturally isomorphic to the untwisted symmetric monoidal product $\boxtimes_{\oplus}$, but in general there is no symmetrizing natural isomorphism of bifunctors making $\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}$ into a symmetric monoidal product.

The associator natural isomorphism for the monoidal structure $\boxtimes_{\oplus}$ is the one induced from the usual monoidal structure on the derived categories of constructible sheaves and $\mathcal{D}$-modules. We have to take some care in defining the signs for the associator for $\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}$. Let $\mathcal{F}^{(h)}\in\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\mathop{\mathrm{\mathbf{d}}}^{(h)}}))$ for $h=1,2,3$. Consider the composition of natural transformations $$\begin{aligned}
\upeta_{\mathcal{F}^{(1)},\mathcal{F}^{(2)},\mathcal{F}^{(3)}}\colon &\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(3)}+\mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle/2}\otimes\left(\mathcal{F}^{(1)}\boxtimes_{\oplus} \left(\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(2)}\rangle/2}\otimes(\mathcal{F}^{(2)}\boxtimes_{\oplus}  \mathcal{F}^{(3)})\right)\right)
\\
\xrightarrow{\cong}&\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(3)}+\mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle/2+\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(2)}\rangle}\otimes\left(\mathcal{F}^{(1)}\boxtimes_{\oplus} \left(\mathcal{F}^{(2)}\boxtimes_{\oplus}  \mathcal{F}^{(3)}\right)\right)
\\
\xrightarrow{\cong}&\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(3)}+\mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle/2+\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(2)}\rangle/2}\otimes\left(\left(\mathcal{F}^{(1)}\boxtimes_{\oplus} \mathcal{F}^{(2)}\right)\boxtimes_{\oplus}  \mathcal{F}^{(3)}\right)
\\
\xrightarrow{\cong}&\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(2)}+\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle/2}\otimes \left(\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle/2}\otimes\left(\mathcal{F}^{(1)}\boxtimes_{\oplus} \mathcal{F}^{(2)}\right)\boxtimes_{\oplus}  \mathcal{F}^{(3)}\right)
\end{aligned}$$ The resulting natural isomorphism $\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}(\mathcal{F}^{(2)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(3)})\rightarrow (\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(2)})\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(3)})$ does *not* satisfy the pentagon identity. We define instead $$\label{AssocSign}
\upeta_{\mathcal{F}^{(1)},\mathcal{F}^{(2)},\mathcal{F}^{(3)}}'\colonequals (-1)^{\langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(3)}\rangle \upchi(\mathop{\mathrm{\mathbf{d}}}^{(1)},\mathop{\mathrm{\mathbf{d}}}^{(1)})}\upeta_{\mathcal{F}^{(1)},\mathcal{F}^{(2)},\mathcal{F}^{(3)}}$$ to produce a valid associator natural isomorphism.

In a little more detail, the diagram $$\begin{aligned}
\label{pentagon}
\xymatrix{
& ((\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(2)}) \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(3)}) \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(4)}\ar[dl]^{\upalpha}\ar[d]_{\updelta}\\
(\mathcal{F}^{(1)} \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}(\mathcal{F}^{(2)} \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(3)})) \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{F}^{(4)}\ar[d]^{\upbeta}&(\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(2)}) \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}(\mathcal{F}^{(3)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(4)})\ar[d]^{\epsilon}\\
\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} ((\mathcal{F}^{(2)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(3)})\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(4)})\ar[r]^{\upgamma}&\mathcal{F}^{(1)} \boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}(\mathcal{F}^{(2)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} (\mathcal{F}^{(3)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(4)}))
}
\end{aligned}$$ fails to commute if the morphisms are all defined using $\upeta_{\bullet,\bullet,\bullet}$. The trouble is in the definition of $\updelta$: in swapping $\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}^{(4)},\mathop{\mathrm{\mathbf{d}}}^{(3)}\rangle/2}$ with $(\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(2)})$ we pick up an extra sign $(-1)^{\langle \mathop{\mathrm{\mathbf{d}}}^{(4)},\mathop{\mathrm{\mathbf{d}}}^{(3)}\rangle\langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle}$ because of the half Tate twist in the definition of $(\mathcal{F}^{(1)}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}} \mathcal{F}^{(2)})$. Modifying all of the morphisms in ([\[pentagon\]](#pentagon){reference-type="ref" reference="pentagon"}) via the rule ([\[AssocSign\]](#AssocSign){reference-type="ref" reference="AssocSign"}) introduces an overall parity change of $$\begin{aligned}
&\langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(3)}\rangle\upchi(\mathop{\mathrm{\mathbf{d}}}^{(1)},\mathop{\mathrm{\mathbf{d}}}^{(1)})+\langle \mathop{\mathrm{\mathbf{d}}}^{(2)}+\mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(4)}\rangle\upchi(\mathop{\mathrm{\mathbf{d}}}^{(1)},\mathop{\mathrm{\mathbf{d}}}^{(1)})
\\
+&\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(4)}\rangle\upchi(\mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(2)})+\langle \mathop{\mathrm{\mathbf{d}}}^{(3)},\mathop{\mathrm{\mathbf{d}}}^{(4)}\rangle\upchi(\mathop{\mathrm{\mathbf{d}}}^{(1)}+\mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}+\mathop{\mathrm{\mathbf{d}}}^{(2)})\\
+&\langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(3)}+\mathop{\mathrm{\mathbf{d}}}^{(4)}\rangle\upchi(\mathop{\mathrm{\mathbf{d}}}^{(1)},\mathop{\mathrm{\mathbf{d}}}^{(1)})=\langle \mathop{\mathrm{\mathbf{d}}}^{(4)},\mathop{\mathrm{\mathbf{d}}}^{(3)}\rangle \langle \mathop{\mathrm{\mathbf{d}}}^{(2)},\mathop{\mathrm{\mathbf{d}}}^{(1)}\rangle &(\textrm{modulo }2)
\end{aligned}$$ as required. The terms in the sum are the contributions from $\upalpha,\upbeta,\upgamma,\updelta,\epsilon$ respectively. We extend $\upeta'_{\bullet,\bullet,\bullet}$ via linearity to triples of objects in $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}))$ to define the associator natural isomorphism for the monoidal structure $\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}$.

We define the monoidal product on $\mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathbb{N}^{Q_0}))$ by setting $$\label{AssociatorSign}
\mathcal{F}\boxtimes_{+}^{\mathop{\mathrm{tw}}} \mathcal{G}\colonequals \bigoplus_{\mathop{\mathrm{\mathbf{d}}}',\mathop{\mathrm{\mathbf{d}}}''\in\mathbb{N}^{Q_0}}\mathbb{L}^{\langle \mathop{\mathrm{\mathbf{d}}}'',\mathop{\mathrm{\mathbf{d}}}'\rangle/2}\otimes\left(+_*(\mathcal{F}_{\mathop{\mathrm{\mathbf{d}}}'}\boxtimes\mathcal{G}_{\mathop{\mathrm{\mathbf{d}}}''})\right)$$ and constructing the associator natural isomorphism as in ([\[AssociatorSign\]](#AssociatorSign){reference-type="ref" reference="AssociatorSign"}). The map $$\dim_*\colon \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}))\rightarrow \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathbb{N}^{Q_0}))$$ is a monoidal functor, and the restriction $$\dim_{\upmu,*}\colon \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\mathcal{M}_{\upmu}^{\upzeta\mathop{\mathrm{-ss}}}))\rightarrow \mathcal{D}^{\geq, \mathrm{lf}}(\mathop{\mathrm{MMHM}}(\Uplambda^{\upzeta}_{\upmu}))$$ is a symmetric monoidal functor for $\upzeta$-generic $\upmu$.

::: remark
[]{#twDual label="twDual"} By skew symmetry of $\langle \bullet,\bullet\rangle_Q$ and finiteness of the maps of schemes $\oplus$ and $+$, there are natural isomorphisms of bifunctors $$\begin{aligned}
&\mathbb{D}^{\mathop{\mathrm{mon}}}(\mathcal{F}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathcal{G})\cong \mathbb{D}^{\mathop{\mathrm{mon}}}\mathcal{G}\boxtimes_{\oplus}^{\mathop{\mathrm{tw}}}\mathbb{D}^{\mathop{\mathrm{mon}}}\mathcal{F}\\
&\mathbb{D}^{\mathop{\mathrm{mon}}}(\mathcal{F}\boxtimes_{+}^{\mathop{\mathrm{tw}}}\mathcal{G})\cong \mathbb{D}^{\mathop{\mathrm{mon}}}\mathcal{G}\boxtimes_{+}^{\mathop{\mathrm{tw}}}\mathbb{D}^{\mathop{\mathrm{mon}}}\mathcal{F}.
\end{aligned}$$ Note the swap of arguments.
:::
