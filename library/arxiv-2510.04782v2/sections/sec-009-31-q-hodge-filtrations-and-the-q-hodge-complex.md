---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-009-31-q-hodge-filtrations-and-the-q-hodge-complex
section_title: "q-Hodge filtrations and the q-Hodge complex"
section_number: 3.1
pages: 20-25
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.969
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#subsec:qHodgeFiltrations label="subsec:qHodgeFiltrations"}

Let us start by introducing an appropriate $\infty$-category of $A$-algebras equipped with a well-behaved $q$-deformation of the Hodge filtration. Since [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"} below is a bit of a mess, let us informally summarise the key points first: In addition to the obvious $q$-deformation condition [\[enum:qHodgeModq-1\]](#enum:qHodgeModq-1){reference-type="ref" reference="enum:qHodgeModq-1"}, we also wish the filtration to be compatible with the rational equivalence $$\bigl(\qdeRham_{R/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\simeq \bigl(\deRham_{R/A}\lotimes_\IZ\IQ\bigr)\qpower\,,$$ which leads to condition [\[enum:qHodgeRational\]](#enum:qHodgeRational){reference-type="ref" reference="enum:qHodgeRational"}. For technical reasons, we also need to require the same for the rationalisations of the $p$-completed ($q$-)de Rham complexes, which is why we have to include condition [\[enum:qHodgeRationalpComplete\]](#enum:qHodgeRationalpComplete){reference-type="ref" reference="enum:qHodgeRationalpComplete"} below. These conditions need to satisfy some obvious compatibilities; recording those, we end up with the following slightly messy definition:

::: defi
[]{#def:qHodgeFiltration label="def:qHodgeFiltration"} Let $R$ be an animated $A$-algebra. A *$q$-Hodge filtration on $\qdeRham_{R/A}$* is a filtered $(q-1)^\star A[q]$-module $$\fil_{\qHodge}^\star \qdeRham_{R/A}\simeq \Bigl( \fil_{\qHodge}^0\qdeRham_{R/A}\leftarrow \fil_{\qHodge}^1\qdeRham_{R/A}\leftarrow\fil_{\qHodge}^2\qdeRham_{R/A}\leftarrow \dotsb\Bigr)\,,$$ equipped with the following data and compatibilities

[^1]

:

::: alphanumerate
[]{#enum:qHodgeFiltrationOnqdR label="enum:qHodgeFiltrationOnqdR"} An equivalence of $A[q]$-modules $\qdeRham_{R/A}\simeq  \fil_{\qHodge}^0\qdeRham_{R/A}$. In other words, we require that $\fil_{\qHodge}^\star \qdeRham_{R/A}$ defines a descending filtration on the derived $q$-de Rham complex.

[]{#enum:qHodgeModq-1 label="enum:qHodgeModq-1"} An equivalence of filtered $A$-modules $$c_{(q-1)}\colon  \fil_{\qHodge}^\star \qdeRham_{R/A}/(q-1)\overset{\simeq}{\longrightarrow} \fil_{\Hodge}^\star \deRham_{R/A}\,,$$ which in filtered degrees $\leqslant 0$ agrees with the usual equivalence $\qdeRham_{R/A}/(q-1)\simeq \deRham_{R/A}$ under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}. In other words, the filtration $\fil_{\qHodge}^\star \qdeRham_{R/A}$ has to be a $(q-1)$-deformation of the Hodge filtration.

[]{#enum:qHodgeRational label="enum:qHodgeRational"} An equivalence of filtered $(q-1)^\star (A\otimes\IQ)[q]$-modules $$c_\IQ\colon \bigl( \fil_{\qHodge}^\star \qdeRham_{R/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\overset{\simeq}{\longrightarrow}  \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\lotimes_\IZ\IQ\bigr)\qpower\,,$$ where $\fil_{(\Hodge,q-1)}^\star$ denotes the $(q-1)$-completed tensor product of the Hodge filtration on $\deRham_{R/A}$ and the $(q-1)$-adic filtration on $\IQ\qpower$; in the following, we'll often call this the *combined Hodge and $(q-1)$-adic filtration*. In addition, we require that $c_\IQ$ agrees in filtered degrees $\leqslant 0$ with the usual equivalence $(\qdeRham_{R/A}\lotimes_\IZ\IQ)_{(q-1)}^\complete\simeq (\deRham_{R/A}\lotimes_\IZ\IQ)\qpower$ under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}, and that $c_\IQ$ and $c_{(q-1)}$ from [\[enum:qHodgeModq-1\]](#enum:qHodgeModq-1){reference-type="ref" reference="enum:qHodgeModq-1"} fit into a commutative diagram $$\begin{tikzcd}[cramped,column sep=3.5ex]
                    \fil_{\qHodge}^\star \qdeRham_{R/A}\rar\dar\ar[drr,commutes] & \fil_{\qHodge}^\star \qdeRham_{R/A}/(q-1)\rar["\simeq","c_{(q-1)}"'] &  \fil_{\Hodge}^\star \deRham_{R/A}\dar \\
                    \bigl( \fil_{\qHodge}^\star \qdeRham_{R/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\rar["\simeq","c_\IQ"'] &  \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\lotimes_\IZ\IQ\bigr)\qpower \rar &  \fil_{\Hodge}^\star \deRham_{R/A}\lotimes_\IZ\IQ
                \end{tikzcd}$$ which again must agree in filtered degrees $\leqslant 0$ with the corresponding unfiltered diagram under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}.

[]{#enum:qHodgeRationalpComplete label="enum:qHodgeRationalpComplete"} For every prime $p$, an equivalence of filtered $(q-1)^\star \widehat{A}_p[1/p]\qpower$-modules $$c_{\IQ_p}\colon \fil_{\qHodge}^\star \bigl(\qdeRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\overset{\simeq}{\longrightarrow}  \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower\,,$$ which is required to agree in filtered degrees $\leqslant 0$ agrees with the usual equivalence $(\qdeRham_{R/A})_p^\complete[1/p]_{(q-1)}^\complete\simeq (\deRham_{R/A})_p^\complete[1/p]\qpower$ under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}. In addition, we require that $c_\IQ$ and $c_{\IQ_p}$ are compatible in form of a commutative diagram $$\begin{tikzcd}
                    \bigl( \fil_{\qHodge}^\star \qdeRham_{R/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\rar["\simeq","c_\IQ"']\dar\drar[commutes] & \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\lotimes_\IZ\IQ\bigr)\qpower\dar\\
                    \fil_{\qHodge}^\star \bigl(\qdeRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\rar["\simeq","c_{\IQ_p}"'] &  \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower
                \end{tikzcd}$$ which in filtered degrees $\leqslant0$ must agree with the usual compatibility under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}, and that $c_{(q-1)}$ and $c_{\IQ_p}$ fit into a commutative diagram $$\begin{tikzcd}[cramped,column sep=3.5ex]
                    \fil_{\qHodge}^\star \bigl(\qdeRham_{R/A}\bigr)_p^\complete\rar\dar\ar[drr,commutes] & \fil_{\qHodge}^\star \bigl(\qdeRham_{R/A}\bigr)_p^\complete/(q-1)\rar["\simeq","c_{(q-1)}"'] &  \fil_{\Hodge}^\star \bigl(\deRham_{R/A}\bigr)_p^\complete\dar \\
                    \fil_{\qHodge}^\star \bigl(\qdeRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\rar["\simeq","c_{\IQ_p}"'] &  \fil_{(\Hodge,q-1)}^\star \bigl(\deRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower \rar &  \fil_{\Hodge}^\star \bigl(\deRham_{R/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]
                \end{tikzcd}$$ which must agree in filtered degrees $\leqslant 0$ with the corresponding unfiltered diagram under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}. Finally, we require that this diagram is compatible with the diagram from [\[enum:qHodgeRational\]](#enum:qHodgeRational){reference-type="ref" reference="enum:qHodgeRational"} under the previous diagram relating $c_\IQ$ and $c_{\IQ_p}$, and that in filtered degrees $\leqslant 0$ this compatibility agrees with the usual compatibility under the identification from [\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}.
:::

We let $\cat{AniAlg}_A^{\qHodge}$ denote the $\infty$-category of pairs $(R,\fil_{\qHodge}^\star\qdeRham_{R/A})$, where $R$ is an animated $A$-algebra and $\fil_{\qHodge}^\star\qdeRham_{R/A}$ is a $q$-Hodge filtration on $\qdeRham_{R/A}$. Formally, the $\infty$-category $\cat{AniAlg}_A^{\qHodge}$ can be expressed as an iterated pullback of $\cat{AniAlg}_A$ and several $\infty$-categories of filtered modules; this is straightforward, but not very enlightening, so we omit the details.
:::

It is natural to ask whether $q$-Hodge filtrations can be chosen functorially. Surprisingly, this turns out to be false.

::: lem
[]{#lem:NoFunctorialqHodgeFiltration label="lem:NoFunctorialqHodgeFiltration"} If $A$ is not a $\IQ$-algebra, then the forgetful functor $\cat{AniAlg}_A^{\qHodge}\rightarrow \cat{AniAlg}_A$ is not essentially surjective. In particular, it has no section, not even when restricted to the full subcategory $\cat{Sm}_A\subseteq \cat{AniAlg}_A$ of smooth $A$-algebras.
:::

::: proof
*Proof sketch.* As far as the author is aware, this result hasn't been published, but the objection is known among the experts in the field.

Let $p$ be a prime such that $\widehat{A}_p\not\simeq 0$. Let $\widehat{A}_p\{x\}_\infty$ be the free $p$-complete perfect $\delta$-ring on a generator $x$. We'll show that the $q$-de Rham complex of $R\coloneqq \widehat{A}_p\{x\}_\infty/x$ admits no $q$-Hodge filtration. Suppose it does. Note that $(\qdeRham_{R/A})_p^\complete$ is given by the prismatic envelope $$\bigl(\qdeRham_{R/A}\bigr)_p^\complete\simeq \widehat{A}_p\{x\}_\infty\qpower\left\{\frac{\phi(x)}{[p]_q}\right\}_{(p,q-1)}^\complete\,.$$ In particular, it is static. Since the Hodge filtration $\fil_{\Hodge}^\star(\deRham_{R/A})_p^\complete$ is just the divided power filtration of the PD-envelope $(\deRham_{R/A})_p^\complete\simeq D_{\smash{\widehat{A}}_p\{x\}_\infty}(x)$, [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}[\[enum:qHodgeModq-1\]](#enum:qHodgeModq-1){reference-type="ref" reference="enum:qHodgeModq-1"} implies that $\fil_{\qHodge}^\star(\qdeRham_{R/A})_p^\complete$ must also be a descending chain of submodules of $(\qdeRham_{R/A})_p^\complete$. Moreover, we see that $\fil_{\qHodge}^p(\qdeRham_{R/A})_p^\complete$ must contain an element $\widetilde{\gamma}_q(x)$ such that $\widetilde{\gamma}_q(x)\equiv x^p/p\mod (q-1)$. Using [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}[\[enum:qHodgeRationalpComplete\]](#enum:qHodgeRationalpComplete){reference-type="ref" reference="enum:qHodgeRationalpComplete"}, we see that $\widetilde{\gamma}_q$ must also be contained in the ideal $(x,q-1)^p$ after completed rationalisation. But it is straightforward to check that the prismatic envelope above doesn't contain any $\widetilde{\gamma}_q(x)$ with these properties (for the details, see [\[exm:MainSpecialCase\]](#exm:MainSpecialCase){reference-type="ref" reference="exm:MainSpecialCase"} below).

This shows that $\cat{AniAlg}_A^{\qHodge}\rightarrow \cat{AniAlg}_A$ is not essentially surjective. Hence it can't have a section, not even over $\cat{Sm}_A\subseteq \cat{AniAlg}_A$, because we could always animate to extend such a section to all of $\cat{AniAlg}_A$. ◻
:::

::: rem
Despite the general non-existence, it's possible to construct many interesting objects of the $\infty$-category $\cat{AniAlg}_A^{\qHodge}$, and the forgetful functor $\cat{AniAlg}_A^{\qHodge}\rightarrow \cat{AniAlg}_A$ does admit sections when restricted to certain full subcategories of $\cat{AniAlg}_A$. We'll discuss several such examples in [\[sec:FunctorialqHodge\]](#sec:FunctorialqHodge){reference-type="ref" reference="sec:FunctorialqHodge"}.
:::

In the remainder of this subsection, we'll study the following objects:

::: numpar
[]{#par:WellBehavedqHodgeComplex label="par:WellBehavedqHodgeComplex"} Given a $q$-Hodge filtration $\fil^\star\qdeRham_{R/A}$ for $R$ over $A$, we can construct the *$q$-Hodge complex* as $$\qHodge_{(R, \fil_{\smash{\qHodge}}^\star )/A}\coloneqq \colimit\Bigl( \fil_{\qHodge}^0\qdeRham_{R/A}\xrightarrow{(q-1)} \fil_{\qHodge}^1\qdeRham_{R/A}\xrightarrow{(q-1)}\dotsb\Bigr)_{(q-1)}^\complete\,.$$ If the $q$-Hodge filtration is clear from the context, we usually just write $\qHodge_{R/A}$.
:::

::: rem
[]{#rem:CompleteFiltration label="rem:CompleteFiltration"} In the above we've used the derived $q$-de Rham complex since many of our examples later on will be outside of the smooth case. But note that even if $R=S$ is smooth over $A$, the underived $q$-de Rham complex $\qOmega_{S/A}$ usually *doesn't* agree with the derived $q$-de Rham complex $\qdeRham_{S/A}$, because $\Omega_{S/A}^*$ and $\deRham_{S/A}$ usually differ in characteristic $0$. But this is not a problem. If we're given a filtration $\fil_{\qHodge}^\star \qOmega_{S/A}$ that satisfies the obvious analogues of [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}[\[enum:qHodgeFiltrationOnqdR\]](#enum:qHodgeFiltrationOnqdR){reference-type="ref" reference="enum:qHodgeFiltrationOnqdR"}--[\[enum:qHodgeRationalpComplete\]](#enum:qHodgeRationalpComplete){reference-type="ref" reference="enum:qHodgeRationalpComplete"}, then its pullback along the canonical map $\qdeRham_{S/A}\rightarrow \qOmega_{S/A}$ yields a filtration $\fil_{\qHodge}^\star\qdeRham_{R/A}$ as in [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}. Indeed, this follows from the fact that $\Omega_{S/A}^*\simeq \hatdeRham_{S/A}$ always agrees with the Hodge-completed derived de Rham complex and the fact that any filtration is the pullback of its completion (see [\[par:Notations\]](#par:Notations){reference-type="ref" reference="par:Notations"}).

Conversely, we'll show in [\[prop:Letaq-1\]](#prop:Letaq-1){reference-type="ref" reference="prop:Letaq-1"} that for any $(S,\fil_{\qHodge}^\star\qdeRham_{S/A})\in\cat{AniAlg}_A^{\qHodge}$ such that $S$ is smooth over $A$, we have an equivalence $$\qOmega_{S/A}\simeq\qhatdeRham_{S/A}$$ of the underived $q$-de Rham complex and the $q$-Hodge completed derived $q$-de Rham complex. Finally, let us remark that in the definition of the $q$-Hodge complex it doesn't matter whether we use $\fil_{\qHodge}^\star\qdeRham_{R/A}$ or its completion $\fil_{\qHodge}^\star\qhatdeRham_{R/A}$, since every element in $\fil_{\qHodge}^i\qdeRham_{R/A}$ becomes divisible by $(q-1)^i$ in $\qHodge_{R/A}$ and the $q$-Hodge complex is $(q-1)$-complete.
:::

::: prop
[]{#lem:qHodgeSymmetricMonoidal label="lem:qHodgeSymmetricMonoidal"} $\cat{AniAlg}_A^{\qHodge}$ admits a canonical symmetric monoidal structure. The tensor product of two objects $(R_1, \fil_{\qHodge}^\star \qdeRham_{R_1/A})$ and $(R_2, \fil_{\qHodge}^\star \qdeRham_{R_2/A})$ is given by $$\left(R_1\lotimes_AR_2,\bigl( \fil_{\qHodge}^\star \qdeRham_{R_1/A}\lotimes_{(q-1)^\star A[q]} \fil_{\qHodge}^\star \qdeRham_{R_2/A}\bigr)_{(q-1)}^\complete\right)\,,$$ where in the second component we take the derived tensor as filtered modules over the filtered ring $(q-1)^\star A[q]$. Furthermore, the functor $$\qHodge_{-/A}\colon \cat{AniAlg}_A^{\qHodge}\longrightarrow \widehat{\Dd}_{(q-1)}\bigl(A[q]\bigr)$$ can be equipped with a canonical symmetric monoidal structure.
:::

To prove [\[lem:qHodgeSymmetricMonoidal\]](#lem:qHodgeSymmetricMonoidal){reference-type="ref" reference="lem:qHodgeSymmetricMonoidal"}, let us first construct a filtration on $\qHodge_{-/A}/(q-1)$.

::: numpar
[]{#par:ConjugateFiltration label="par:ConjugateFiltration"} Let $(R, \fil_{\qHodge}^\star \qdeRham_{R/A})$ be an object in $\cat{AniAlg}_A^{\qHodge}$. Let's consider the localisation of the filtered $(q-1)^\star A[q]$-module $\fil_{\qHodge}^\star \qdeRham_{R/A}$ at $(q-1)$: $$\fil_{\qHodge}^\star \qdeRham_{R/A}\bigl[\localise{q-1}\bigr]\simeq\colimit\Bigl( \fil_{\qHodge}^{\star }\qdeRham_{R/A}\xrightarrow{(q-1)} \fil_{\qHodge}^{\star +1}\qdeRham_{R/A}\xrightarrow{(q-1)}\dotso\Bigr)\,.$$ Upon completing the filtration, this filtered object becomes the $(q-1)$-adic filtration on the $q$-Hodge complex $\qHodge_{R/A}$.

Before taking the colimit, the diagram above can be regarded as a bifiltered object, with one ascending ("horizontal") filtration, given by the steps in the colimit, and one descending ("vertical") filtration, given by the filtrations on each step $\fil_{\qHodge}^{\star +n}\qdeRham_{R/A}$. If we pass to the associated graded in the vertical direction, we obtain $$\qHodge_{R/A}/(q-1)\simeq\colimit\Bigl(\gr_{\qHodge}^{0}\qdeRham_{R/A}\xrightarrow{(q-1)}\gr_{\qHodge}^{1}\qdeRham_{R/A}\xrightarrow{(q-1)}\dotso\Bigr)\,.$$ This representation as a colimit defines an exhaustive ascending filtration on $\qHodge_{R/A}/(q-1)$, which we define to be the *conjugate filtration* $\fil_\star ^\mathrm{conj}(\qHodge_{R/A}/(q-1))$.
:::

::: lem
[]{#lem:ConjugateFiltration label="lem:ConjugateFiltration"} The associated graded of the conjugate filtration $\fil_\star^\mathrm{conj}\qHodge_{R/A}/(q-1)$ is given by $$\gr_*^{\mathrm{conj}}\bigl(\qHodge_{R/A}/(q-1)\bigr)\simeq \Sigma^{-*}\deRham_{R/A}^*\simeq\gr_{\Hodge}^*\deRham_{R/A}\,.$$
:::

::: proof
*Proof.* To avoid ambiguous notation, let us identify the filtered ring $(q-1)^\star A[q]$ with the graded ring $A[\beta,t]$, where $\abs{\beta}=1$, $\abs{t}=-1$, and $\beta t=q-1$.

[^2]

The filtered structure on $A[\beta,t]$ comes from the $A[t]$-module structure (see [\[par:Notations\]](#par:Notations){reference-type="ref" reference="par:Notations"}), so $t$ can be regarded as the filtration parameter and $\beta$ can be regarded as the element "$(q-1)$ sitting in degree $1$". If we regard $\fil_{\qHodge}^\star\qdeRham_{R/A}$ as a graded $A[\beta,t]$-module, then $$\fil_{\qHodge}^\star\qdeRham_{R/A}/\beta\simeq  \fil_{\Hodge}^\star\deRham_{R/A}\quad\text{and}\quad  \fil_{\qHodge}^\star\qdeRham_{R/A}/t\simeq \gr_{\qHodge}^*\qdeRham_{R/A}$$ as graded $A[t]$- or $A[\beta]$-modules, respectively. The first equivalence follows from [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}[\[enum:qHodgeModq-1\]](#enum:qHodgeModq-1){reference-type="ref" reference="enum:qHodgeModq-1"}, the second follows because modding out $t$ is the same as taking the associated graded (see [\[par:Notations\]](#par:Notations){reference-type="ref" reference="par:Notations"}). Hence also $$\fil_{\qHodge}^\star \qdeRham_{R/A}/(\beta,t)\simeq \gr_{\Hodge}^*\deRham_{R/A}$$ as filtered $A$-modules. Finally, by construction, we can identify $\qHodge_{R/A}/(q-1)$ with $( \fil_{\qHodge}^\star\qdeRham_{R/A}\lotimes_{A[\beta]}A[\beta^{\pm 1}])_0/(\beta t)$, where $(-)_0$ denotes the restriction of a graded object to its degree-$0$ part. Then the desired assertion follows from [\[lem:FiltrationAbstract\]](#lem:FiltrationAbstract){reference-type="ref" reference="lem:FiltrationAbstract"} below. ◻
:::

::: lem
[]{#lem:FiltrationAbstract label="lem:FiltrationAbstract"} Let $M^*$ be a graded module over the graded ring $A[\beta,t]$, where $\abs{\beta}=1$, $\abs{t}=-1$. Then $(M^*\lotimes_{A[\beta]}A[\beta^{\pm 1}])_0/(\beta t)$ admits a canonical exhaustive ascending filtration whose associated graded is $M^*/(\beta,t)$.
:::

::: proof
*Proof.* We formally get $(M^*\lotimes_{A[\beta]}A[\beta^{\pm 1}])_0/(\beta t)\simeq (M^*/t\lotimes_{A[\beta]}A[\beta^{\pm 1}])_0$. Let $\beta^{-\star}A[\beta]$ denote the ascendingly filtered graded ring $$\beta^{-\star}A[\beta]\coloneqq \Bigl(\dotsb\overset{\beta}{\longrightarrow}A[\beta](1)\overset{\beta}{\longrightarrow}A[\beta](0)\overset{\beta}{\longrightarrow}A[\beta](-1)\overset{\beta}{\longrightarrow}\dotsb\Bigr)\,,$$ where $A[\beta](i)$ denotes the shift of the graded object $A[\beta]$ by $i$ (to account for the fact that multiplication by $\beta$ shifts degrees). The colimit of this filtration is $\colimit \beta^{-\star}A[\beta]\simeq A[\beta^{\pm 1}]$. Hence $(M^*/t\lotimes_{A[\beta]}\beta^{-\star}A[\beta])_0$ defines an exhaustive ascending filtration on $(M^*/t\lotimes_{A[\beta]}A[\beta^{\pm 1}])_0$ (by inspection, this is also precisely how the conjugate filtration from [\[par:ConjugateFiltration\]](#par:ConjugateFiltration){reference-type="ref" reference="par:ConjugateFiltration"} arises). Since the associated graded of $\beta^{-\star}A[\beta]$ is $\bigoplus_{i\in\IZ}A(-i)$, the associated graded of the filtration we've just constructed is indeed $$\biggl(\bigoplus_{i\in\IZ}M^*/t\lotimes_{A[\beta]}A(-i)\biggr)_0\simeq \biggl(\bigoplus_{i\in\IZ}M^*/(\beta,t)(-i)\biggr)_0\simeq M^*/(\beta,t)\,.\qedhere$$ ◻
:::

::: proof
*Proof of [\[lem:qHodgeSymmetricMonoidal\]](#lem:qHodgeSymmetricMonoidal){reference-type="ref" reference="lem:qHodgeSymmetricMonoidal"}.* $\cat{AniAlg}_A^{\qHodge}$ can be written as an iterated pullback of symmetric monoidal $\infty$-categories along symmetric monoidal functors, so there's a canonical way to equip it with a symmetric monoidal structure itself. The forgetful functors $$\cat{AniAlg}_A^{\qHodge}\longrightarrow \cat{AniAlg}_A\quad\text{and}\quad\cat{AniAlg}_A^{\qHodge}\longrightarrow \Mod_{(q-1)^\star A[q]}\bigl( \Fil \Dd(A)\bigr)_{(q-1)}^\complete$$ will then be symmetric monoidal, which shows the formula for tensor products.

To construct a symmetric monoidal structure on $\qHodge_{-/A}$, we use [\[par:ConjugateFiltration\]](#par:ConjugateFiltration){reference-type="ref" reference="par:ConjugateFiltration"}. Since localising is symmetric monoidal and passing to the $0$^th^ filtration step is lax symmetric monoidal, we get a lax symmetric monoidal structure on $\qHodge_{-/A}$. Strict symmetric monoidality can then be checked modulo $(q-1)$ because the values of $\qHodge_{-/A}$ are $(q-1)$-complete.

From the proof of [\[lem:FiltrationAbstract\]](#lem:FiltrationAbstract){reference-type="ref" reference="lem:FiltrationAbstract"} above, it is clear that $\fil_\star^\mathrm{conj}(\qHodge_{-/A}/(q-1))$ can be equipped with a lax symmetric monoidal structure compatible with the one on $\qHodge_{-/A}/(q-1)$ (modding out $t$ or $\beta$ as well as $-\lotimes_{A[\beta]}\beta^{-\star}A[\beta]$ are symmetric monoidal and $(-)_0$ is lax symmetric monoidal). Furthermore the equivalence $$\gr_*^\mathrm{conj}\bigl(\qHodge_{-/A}/(q-1)\bigr)\simeq \gr_{\Hodge}^*\deRham_{-/A}$$ is an equivalence of lax symmetric monoidal functors. Strict symmetric monoidality of $\fil_\star^\mathrm{conj}(\qHodge_{-/A}/(q-1))$ can now be checked on the associated graded, so we win since it's well-known that $\gr_{\Hodge}^*\deRham_{-/A}$ is symmetric monoidal. ◻
:::

[^1]: Since we're working with $\infty$-categories, each compatibility is again a datum that needs to be provided.

[^2]: In [@qdeRhamku] we'll recognise $(q-1)^\star \IZ\qpower\cong \IZ[\beta]\llbracket t\rrbracket\cong \pi_{2*}(\ku^{\h S^1})$, where $\beta\in\pi_2(\ku)$ is the Bott element and $t\in \pi_{-2}(\ku^{\h S^1})$ is a suitable complex orientation.
