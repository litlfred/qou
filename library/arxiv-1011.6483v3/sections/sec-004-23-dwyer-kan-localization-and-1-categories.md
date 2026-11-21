---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-004-23-dwyer-kan-localization-and-1-categories
section_title: "Dwyer-Kan localization and (,1)-categories"
section_number: 2.3
pages: 8-10
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.952
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:DKL label="S:DKL"} The $(\infty,1)$-categories that we are concerned about in this paper arise from model categories structures via the Dwyer-Kan localization turning them into simplicial categories. Indeed simplicial categories are model for $(\infty,1)$-categories [@Be1]. We now explain briefly how one gets $(\infty,1)$-categories out of model categories such as those considered in Section [\[S:Delta\]](#S:Delta){reference-type="ref" reference="S:Delta"}, [\[S:CDGA\]](#S:CDGA){reference-type="ref" reference="S:CDGA"} above.

Following [@Re; @L-TFT], by an $(\infty,1)$-category we mean a *complete Segal space*. Rezk has shown that the category of simplicial spaces has a (simplicial closed) model structure, denoted $\mathcal{CS}e\mathcal{S}p$ such that a complete Segal space is precisely a fibrant object for this model structure [@Re Theorem 7.2]. Note that there is also a (simplicial closed) model category structure, denoted $\mathcal{S}e\mathcal{S}p$, on the category of simplicial spaces such that a fibrant object in the $\mathcal{S}e\mathcal{S}p$ structure is precisely a Segal space. We let $\mathbb{R}:\mathcal{S}e\mathcal{S}p\to \mathcal{S}e\mathcal{S}p$ be a fibrant replacement functor. Rezk [@Re] has defined a completion functor $X_\bullet \to \widehat{X_\bullet}$ which, to a Segal space, associates an equivalent complete Segal space. Thus, the composition $X_\bullet \mapsto \widehat{\mathbb{R}(X_\bullet)}$ gives a (fibrant replacement in the model category $\mathcal{CS}e\mathcal{S}p$) functor $L_{\mathcal{CS}e\mathcal{S}p}$ from simplicial spaces to complete Segal spaces.

It remains to explain how to go from a model category to a simplicial space. The standard key idea is to use Dwyer-Kan localization. Let $\mathcal{M}$ be a model category and $\mathcal{W}$ be its subcategory of weak-equivalences. We denote $L^H(\mathcal{M},\mathcal{W})$ its *hammock localization*, see [@DK]. One of the main property of $L^H(\mathcal{M},\mathcal{W})$ is that it is a simplicial category and that the (usual) category $\pi_0(L^H(\mathcal{M},\mathcal{W}))$ is the homotopy category of $\mathcal{M}$. Further, every weak equivalence has a (weak) inverse in $L^H(\mathcal{M},\mathcal{W})$. When $\mathcal{M}$ is further a simplicial model category, then for every pair $(x,y)$ of objects $\mathop{Hom}_{L^H(\mathcal{M},\mathcal{W})}(x,y)$ is naturally homotopy equivalent to the derived mapping space $\mathbb{R}Hom (x,y)$.

It follows that any model category $\mathcal{M}$ gives functorially rise to the simplicial category $L^H(\mathcal{M},\mathcal{W})$. Taking the nerve $N_\bullet(L^H(\mathcal{M},\mathcal{W}))$ we obtain a simplicial space. Composing with the complete Segal Space replacement functor we get a functor $\mathcal{M}\to L_\infty(\mathcal{M}):= L_{\mathcal{CS}e\mathcal{S}p}(N_\bullet(L^H(\mathcal{M},\mathcal{W})))$ from model categories to $(\infty,1)$-categories (that is complete Segal spaces).

::: example
[]{#E:hsset label="E:hsset"}Applying the above procedure to the model category of simplicial sets $sSet$, we obtain the $(\infty,1)$-category $sSet_\infty$. Similarly from the model category $CDGA$ of CDGAs we obtain the $(\infty,1)$-category $CDGA_\infty$. Note that a simplicial set is determined by its $(\infty, 0)$ path groupoid and therefore the category of simplicial sets should be thought of as the $(\infty, 1)$ category of all $(\infty, 0)$ groupoids. Further, the tensor product (over $k$) of algebras is a monoidal functor which gives $CDGA$ a structure of monoidal model category, see [@Ho]. Thus $CDGA_\infty$ also inherits the structure of a symmetric monoidal $(\infty,1)$-category in the sense of [@Re; @L-TFT]. Similarly, the disjoint union of simplicial sets endows $sSet$ and $sSet_\infty$ with symmetric monoidal structures.

The model category of topological spaces yields the $(\infty,1)$-category $\hTop$. Since $sSet$ and $\Top$ are Quillen equivalent [@GoJa; @Ho], the associated $(\infty,1)$-categories are equivalent (as $(\infty,1)$-categories): $sSet_\infty\stackrel{\sim}{\underset{\sim}{\rightleftarrows}} \hTop$, where the left and right equivalences are respectively induced by the singular set and geometric realization functors.

One can also consider the pointed versions ${sSet_\infty}_*$ and ${\hTop}_*$ of the above $(\infty,1)$-categories (using the model categories of these pointed versions [@Ho]).
:::

::: example
[]{#E:Amod label="E:Amod"} As recalled in Section [\[S:CDGA\]](#S:CDGA){reference-type="ref" reference="S:CDGA"}, there are model categories categories $A\textit{-}Mod$ and $A\text{-}CDGA$ of modules and commutative algebras over a CDGA $A$. Thus the above procedure gives us $(\infty,1)$-categories $A\textit{-}Mod_\infty$ and $A\textit{-}CDGA_\infty$ and the base change functor lifts to an $(\infty,1)$-functor. Further, if $f: A\to B$ is a weak equivalence, the natural functor $f_*:B\textit{-}Mod \to A\textit{-}Mod$ induces an equivalence $B\textit{-}Mod_\infty \stackrel{\sim}\to A\textit{-}Mod_\infty$ of $(\infty,1)$-categories since it is a Quillen equivalence.

Moreover, if $f:A\to B$ is a morphism of CDGAs, it induces a natural functor $f^*:A\textit{-}Mod \to B\textit{-}Mod, M\mapsto M\otimes_A B$, which is an equivalence of $(\infty,1)$-categories when $f$ is a quasi-isomorphism, and is a (weak) inverse of $f_*$ (see [@ToVe] or [@KM]). Here we also (abusively) denote $f^*:A\textit{-}Mod_\infty \to B\textit{-}Mod_\infty$ and $f_*:B\textit{-}Mod_\infty \to A\textit{-}Mod_\infty$ the (derived) functors of $(\infty,1)$-categories induced by $f$. Since we are working over a field of characteristic zero, the same results applies to monoids in $A\textit{-}Mod$ and $B\textit{-}Mod$, that is to the categories $A\text{-}CDGA_\infty$ and $B\text{-}CDGA_\infty$. Also note that, if $f:A\to B$, $g:A\to C$ are CDGAs homomorphisms, we can form the (homotopy) pushout $D\cong B\otimes^{\mathbb{L}}_{A} C$.

Let us denote $p: B\to D$ and $q:C\to D$ the natural CDGAs maps. We thus get two natural base change ($(\infty,1)$-)functors $C\textit{-}Mod_\infty \underset{p_*\circ q^*}{\stackrel{f^*\circ g_*}\rightrightarrows} B\textit{-}Mod_\infty$. Given any $M\in C\textit{-}Mod$, the natural map $f^*\circ g_*(M) \to p_*\circ q^*(M)$ is an equivalence [@ToVe Proposition 1.1.0.8].

The $(\infty,1)$-category $CDGA_\infty$ is *tensored* over $sSet_\infty$ (and thus $\hTop$ as well) as follows from [@Lu11 §4.4.4]. We refer to [@Lu11; @L-VI] for tensored $(\infty,1)$-categories (which is the obvious analogue of the classical notion of tensored categories over $\Top$ or $sSet$); we simply recall that an $(\infty,1)$-category $\mathcal{C}$ is tensored over $sSet_\infty$ if there exists an $(\infty,1)$-functor $\mathcal{C} \times sSet_\infty\to \mathcal{C}$, denoted $(C, X_\bullet)\mapsto C\boxtimes X_\bullet$, together with natural equivalences $$Map_{\mathcal{C}}\big(C\boxtimes X_\bullet, D\big) \; \cong \; Map_{sSet_\infty}\big(X_{\scriptstyle\bullet}, Map_{\mathcal{C}}\big(C, D\big)\big).$$ In fact, the tensor $A\boxtimes X_\bullet$ is precisely realized by the Hochschild derived functor, see Theorem [\[T:derivedfunctor\]](#T:derivedfunctor){reference-type="ref" reference="T:derivedfunctor"}.
:::

::: example
[]{#E:EnOperad label="E:EnOperad"} We denote $E_n\textit{-}Alg_\infty$ the $(\infty,1)$-category of $E_n$-algebras which is given by algebras over any $E_n$-($\infty$-)operads as introduced in [@L-VI Section 5.1] in the symmetric monoidal ($(\infty,1)$-)category $(k\textit{-}Mod_\infty,\otimes)$. It is equivalent to the $(\infty,1)$-category associated to model categories (deduced for instance from [@Hi Theorem 4.1.1]) of algebras over the usual operad of singular chains on the little $n$-dimensional disk operad or as algebras over the Barratt-Eccles operad (which is an Hopf operad) [@BF].
:::

::: remark
[]{#R:non-unique label="R:non-unique"} There are other functors that yields a complete Segal space out of a model category. For instance, one can use the classification diagram of Rezk [@Re]. Let again $\mathcal{M}$ be a model category and, for any integer $n$, let $\mathcal{M}^{[n]}$ be the (model) category of $n$-composables morphisms, that is the category fo functors from the poset $[n]$ to $\mathcal{M}$. The *classification diagram* of $\mathcal{M}$ is the simplicial space $n\mapsto N_\bullet(\mathcal{W}e(\mathcal{M}^{[n]}))$ where $\mathcal{W}e(\mathcal{M}^{[n]})$ is the subcategory of weak equivalences of $\mathcal{M}^{[n]}$. Then taking a *Reedy* fibrant replacement yields another complete Segal space $N_\bullet(\mathcal{W}e(\mathcal{M}^{[n]}))^{f}$ [@Be2 Theorem 6.2], [@Re Theorem 8.3]. It is known that the Segal space $N_\bullet(\mathcal{W}e(\mathcal{M}^{[n]}))^{f}$ is equivalent to $L_{\mathcal{CS}e\mathcal{S}p}(N_\bullet(L^H(\mathcal{M},\mathcal{W})))$ [@Be2].

More generally, there are several model for $(\infty,1)$-categories and several equivalent ways to obtain an $(\infty,1)$-category out of a "homotopy theory". We believe the results of this paper can easily be applied to the favorite model of the reader.
:::
