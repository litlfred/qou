---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-009-5-the-drinfeld-center
section_title: "The Drinfel'd center"
section_number: 5
pages: 17-20
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.979
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
[]{#sec:center label="sec:center"}

The goal of this section is to give a proof of part [\[pa:center\]](#pa:center){reference-type="ref" reference="pa:center"} of Theorem [\[thm:detailed\]](#thm:detailed){reference-type="ref" reference="thm:detailed"}, completing the proof of Theorem [\[thm:detailed\]](#thm:detailed){reference-type="ref" reference="thm:detailed"}. Our proof is somewhat unsatisfying since it is indirect and relies on extensive computations from [@MR1832764]. Presumably one could use calculations along the lines of [@MR1832764] to give a more direct proof (specifically by explicitly writing down formulas for the half-braidings which only use scalars in $\Rational(\zeta_{39})$).

First notice that the entries of the $T$-matrix (see below) for $Z(\cH_0^p(\Complex))$ generate $\Rational(\zeta_{39})$ so if there is a complete rational form over a field $k$ as a ribbon category, then $k$ must contain $\zeta_{39}$.

Now we prove the other direction, namely that $Z(\cH_0^p(\Complex))$ has a complete rational form over $\Rational(\zeta_{39})$ as a ribbon category. Explicitly we will prove that $Z(\cH_0^p(\Rational(\zeta_{39})))$ is a complete rational form. The argument will take place in two steps. First we prove a general result that the Drinfel'd center of a rational form is a rational form for the Drinfel'd center. Next, we check that $Z(\cH_0^p(\Rational(\zeta_{39})))$ is split. For both steps of the argument the key element is the induction functor $I: \cC \rightarrow Z(\cC)$ which commutes with base extension.

We quickly recall some key definitions and results concerning the Drinfel'd center and module categories (see [@MR1976459; @MR1976233]). Let $\cD$ be a fusion category and $\cM$ a semisimple finite left module category. If $M_1$ and $M_2$ are objects in $\cM$ then the internal hom $\underline{\operatorname{Hom}}_{\cD \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM}(M_1,M_2)$ is defined to be the object in $\cD$ which represents the functor $X \mapsto \Hom{}{X \otimes M_1}{M_2}$. Define the dual category $\cD^* = \mathrm{Fun}_{\cD}(\cM,\cM)$ of module endofunctors of $\cM$. If $M$ is a simple object in $\cM$, there is a natural algebra structure on the object $A = \underline{\operatorname{Hom}}_{\cD \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM}(M,M)$ and the categories $\cM$, $\cM^{op}$, and $\cD^*$ can be concretely identified with the categories of right $A$-modules in $\cM$, left $A$-modules in $\cM$, and $A$--$A$ bimodules in $\cM$, respectively. Fixing the simple object $M$, there's an induction functor $I: \cM \rightarrow \cD^*$, given by tensoring a right $A$-module on the left with $A$.

The Drinfel'd center $Z(\cC)$ has two equivalent definitions. First, the objects of $Z(\cC)$ are pairs $(X, \{\sigma_{X,Y}\}_Y)$ consisting of an object in $\cC$ and a collection of half-braidings $\sigma_{X,Y}: X \otimes Y \rightarrow Y \otimes X$ satisfying certain naturality conditions. For the second, recall that $\cC$ is a module category over $\cC \boxtimes \cC^{op}$ (with the action $(X\boxtimes Y) \otimes M \rightarrow X \otimes M \otimes Y$). Then, $Z(\cC)$ is the dual of $\cC \boxtimes C^{op}$. Explicitly, we can take $M = 1$, and let $A = \underline{\operatorname{Hom}}_{\cC \boxtimes \cC^{op} \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cC}(1,1)$ be the internal endomorphisms of $1 \in \cC$. Thus $A$ is an algebra object in $\cC \boxtimes \cC^{op}$, and $Z(C)$ is the category of $A$--$A$ bimodule objects in $\cC \boxtimes \cC^{op}$. From this point of view the induction functor $I: \cC \rightarrow Z(\cC)$ is given by $X \mapsto A \otimes X$.

::: rem
It is natural to wonder what $I(X)$ is in terms of the first definition of the center. According to [@MR2183279 Prop. 5.4] for a split fusion category the underlying object of $I(X)$ is $\bigoplus_V V \otimes X \otimes V^*$ (where the sum is taken over all simples). This formula certainly does not work in the non-split case. Notice, however, that an analogous problem occurs when decomposing the adjoint representation of the group ring $k[G]$. Here, in the nonsplit case, the adjoint representation is not $\bigoplus_V V \otimes V^*$ but instead the coinvariants with respect to the the left action of the division ring $\operatorname{End}_G (V)$ on $V$ and its right action on $V^*$. The same modification works for the induction functor: for each $f \in \End{V}$, we have two maps $\bigoplus_V V \otimes X \otimes V^* \rightrightarrows \bigoplus_V V \otimes X \otimes V^*$ given by acting on either $V$ or $V^*$, and the correct value of $I(X)$ is the colimit of the collection of these diagrams where $f$ varies over a basis of $\End{V}$. (This colimit exists because all small colimits exist in an abelian category.) The half-braidings for $I(X)$ in the split case were written down in [@1004.1533 Theorem 2.3]. Their formula can be modified to work in the non-split case, by being careful about normalizations and by quotienting out by the action of $\End{V}$ as above. Indeed, since every object in $Z(\cC)$ is a summand of an induced object, it's possible to prove that the center of a rational form is a rational form of the center explicitly by writing down formulas for the half-braiding on the induced objects following [@1004.1533 Theorem 2.3]. Here, we choose instead to work directly with the second description of the center.
:::

::: lem
[]{#lem:rationalcenter label="lem:rationalcenter"} Suppose that $\cC_k$ is a rational form of $\cC_K$. The natural functor $Z(\cC_k)\otimes_k K \rightarrow Z(\cC_K)$ is full, faithful, commutes with the induction functors, and is dominant. Hence, $Z(\cC_k)$ is a rational form as a braided tensor category of $Z(\cC_K)$.
:::

Lemma [\[lem:rationalcenter\]](#lem:rationalcenter){reference-type="ref" reference="lem:rationalcenter"} follows immediately from the following more general result.

::: lem
Suppose that $\cD_K$ is a fusion category over $K$, that $\cM_K$ is a semisimple module category over $\cD_K$, that $\cD_k$ is a rational form of $\cD_K$ over $k$ (as a fusion category), and that $\cM_k$ is a rational form of $\cM_K$ over $k$ (as a module category over $\cD_k$). Let $\cF$ be the full, faithful and dominant functor $\cF: \cD_k \tensor_k K \rightarrow \cD_K$ guaranteed by the fact that $\cD_k$ is a rational form, and $\cG$ the corresponding functor $\cG:\cM_k \tensor_k K \to \cM_K$. Let $M$ be a simple object in $\cM_k$. Then, $\cF( \underline{\operatorname{Hom}}_{\cD_k \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM_k}(M,M))$ and $\underline{\operatorname{Hom}}_{\cD_K \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM_K}(\cG(M),\cG(M))$ are isomorphic as algebra objects, and there is a functor $\cF^*: D_k^*\otimes_k K \rightarrow D_K^*$ induced by $\cF$ which is full, faithful and dominant. Hence, $D_k^*$ is a rational form of $D_K^*$.
:::

::: proof
*Proof.* Let $A_k = \underline{\operatorname{Hom}}_{\cD_k \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM_k}(M,M)$ in $\cD_k$ and $A_K =\underline{\operatorname{Hom}}_{\cD_K \mathrel{\reflectbox{\rotatebox[origin=c]{90}{$\circlearrowleft $}}}\;\cM_K}(\cG(M),\cG(M))$ in $\cD_K$. First we show that $\cF(A_k) \cong A_K$ as algebra objects. We need only check that $\cF(A_k)$ represents the functor $\cD_K \to \mathrm{Set}$ given by $X \mapsto \Hom{}{X \otimes \cG(M)}{\cG(M)}$, which follows immediately from the fact that $\cM_k$ is a rational form for $\cM_K$.

Since $\cF(A_k) \cong A_K$, the functor $\cF: D_k \otimes_k K \rightarrow D_K$ induces a functor $\cF^*: D_k^* \otimes_k K \rightarrow D_K^*$, which we now describe. Recall we can interpret $\cD^*_k$ as the $A_k$--$A_k$ bimodules in $\cD_k$ (and similarly for $\cD_K$). Given an $A_k$--$A_k$ bimodule in $\cD_k$, we can construct an $A_K$--$A_K$ bimodule in $\cD_K$ simply by applying the functor $\cF$ to the underlying object, as well as to the morphisms making it a bimodule. We now want to prove that $\cF^*$ is full and faithful. Suppose that $X$ and $Y$ are $A_k$--$A_k$ bimodules, then among all maps from $X$ to $Y$ the bimodule maps are picked out by satisfying certain linear equations with coefficients in $k$. Similarly among all maps from $\cF(X)$ to $\cF(Y)$ the bimodule maps are picked out by satisfying the same linear equations with coefficients in $k$. Thus, since $\cF: D_k \otimes_k K \rightarrow D_K$ is an isomorphism on morphism spaces, it follows that $\cF^*: D_k^* \otimes_k K \rightarrow D_K^*$ is as well.

Thus we need only check that $\cF^*: D_k^* \otimes_k K \rightarrow D_K^*$ is dominant (i.e. every object in the target is a summand of an object in the image of the functor). Since $\cF(A_k) \cong A_K$ we see that $\cF \circ I$ and $I \circ \cF$ are naturally isomorphic functors. If $X$ is an arbitrary $A_K$--$A_K$ bimodule, then certainly $X$ is a summand of $I(R(X))$ (where $R$ is the restriction functor which forgets the left action of $A_K$). Since $\cM_k$ is a rational form of $\cM_K$, we see that $R(X)$ is a summand of $\cF(N)$ for some right $A_k$ module $N$. Hence, $X$ is a summand of $I( \cF(N)) \iso \cF(I(N)$, and the functor is dominant. ◻
:::

The center $Z(\cH_0^p(\Complex))$ has previously been described in [@MR1832764] (see [@MR2468378] for further details). The simple objects are $1, \pi_1, \pi_2, \mu_1, \ldots, \mu_6, \sigma_0, \sigma_1, \sigma_2$. Let $I$ be the induction functor $I: \cH_0^p \rightarrow Z(\cH_0^p)$. Over $\Complex$, it is described on the level of objects by the graph in Figure [1](#fig:izumi-induction){reference-type="ref" reference="fig:izumi-induction"}. Note that over $\Complex$ we have $$I(\JW{2}) \cong \pi_1 \oplus \pi_2 \oplus \mu_1 \oplus \ldots \oplus \mu_6 \oplus \sigma_0 \oplus \sigma_1 \oplus \sigma_2,$$ and in particular there is exactly one copy of each simple except $1$.

<figure id="fig:izumi-induction">
<p><span class="math display">$$\inputtikz{inductionfunctor}$$</span></p>
<figcaption>The induction functor for <span class="math inline">$\cH_0^p(\Complex)$</span>, reproduced from Figure 5 of <span class="citation" data-cites="MR1832764"></span>, with <span class="math inline">$\widehat{{}_0\rho}, \widehat{{}_1\rho}, \widehat{{}_2\rho}, \widehat{\alpha_1}$</span> and <span class="math inline">$\widehat{\alpha_2}$</span> renamed to <span class="math inline">$\JW{2}, P, Q, P''$</span> and <span class="math inline"><em>Q</em>″</span> respectively.</figcaption>
</figure>

::: thm
$Z(\cH_0^p(\Rational(\zeta_{39})))$ is a split fusion category over $\Rational(\zeta_{39})$.
:::

::: proof
*Proof.* Since $\JW{2}$ is an object in $\cH_0^p(\Rational(\zeta_{39}))$, we have that $I(\JW{2})$ is an object in $Z(\cH_0^p(\Rational(\zeta_{39})))$. We build explicit projections on to many of its summands. Let $\theta_{I(\JW{2})}$ be the ribbon element acting on $I(\JW{2})$. Over $\Complex$, the ribbon element $\theta_{I(\JW{2})}$ acts on each simple object by the corresponding entry in the $T$-matrix which is diagonal with entries $$(T_{jj}) = (1,1,1, \zeta_{39}^6, \zeta_{39}^{-6}, \zeta_{39}^{15},  \zeta_{39}^{-15}, \zeta_{39}^{18}, \zeta_{39}^{-18}, 1, \zeta_{39}^{13}, \zeta_{39}^{-13}).$$

Consider $\frac{1}{39}\sum_i \zeta_{39}^{m i} \theta_{I(\JW{2})}^i$ for different values of $m$. These give projections onto the eigenspaces of the $T$-matrix Using the values of the $T$-matrix it follows that for these give projections onto each of $\mu_i$, $\sigma_1$, and $\sigma_2$. Hence all of those simples are defined over $\Rational(\zeta_{39})$.

The sum $\sum_i \theta_{I(\JW{2})}^i$ gives a projection onto $\pi_1 \oplus \pi_2 \oplus \sigma_0$. Let $F$ be a single strand labelled by $\pi_1 \oplus \pi_2 \oplus \sigma_0$ with a ring around it labelled by $\sigma_1$. Looking at the corresponding entries in the $S$-matrix (described in [@MR2468378]) we see that $\frac{5 + \sqrt{13}}{18} (\id + F)$ gives a projection onto $\pi_1$ while its complement gives a projection onto $\pi_2 \oplus \sigma_0$.

Consider $I(1) \cong 1\oplus \pi_1 \oplus 2 \pi_2$. Notice that here $\pi_2$ is a summand while $\sigma_0$ is not. In particular, there is a map over $\Complex$ from $I(1)$ to $\pi_2 \oplus \sigma_0$, and hence over $\Rational(\zeta_{39})$ there also must be such a map. Hence by semisimplicity, we must have $\sigma_0$ and $\pi_2$ are objects over $\Rational(\zeta_{39})$. ◻
:::
