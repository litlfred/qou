---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-001-11-habiro-cohomology
section_title: "Habiro cohomology"
section_number: 1.1
pages: 3-4
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.985
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
In this paper we'll investigate the following question, which was raised by Peter Scholze:

::: numpar
[]{#qst:Habiro label="qst:Habiro"} *Is there a version of $q$-de Rham cohomology with coefficients not in the power series ring $\IZ\qpower$, but in the Habiro ring $$\Hh\coloneqq \limit_{m\in\IN}\IZ[q]_{(q^m-1)}^\complete\,?$$*
:::

A cohomology theory that provides a positive answer to Question [\[qst:Habiro\]](#qst:Habiro){reference-type="ref" reference="qst:Habiro"} would then deserve the name *Habiro cohomology*. Let us first convince the reader that it should be worthwhile to search for such a cohomology theory.

::: numpar
[]{#par:WhyHabiroCohomology label="par:WhyHabiroCohomology"} *$q$-de Rham cohomology*, which was constructed by Bhatt and Scholze ([@Toulouse; @Prismatic]; see also the review in [\[appendix:GlobalqDeRham\]](#appendix:GlobalqDeRham){reference-type="ref" reference="appendix:GlobalqDeRham"}) is already a very interesting cohomology theory: For every smooth scheme $X$ over $\IZ$, the *$q$-de Rham complex* $\qOmega_{X/\IZ}$ is a $(q-1)$-complete object in the derived $\infty$-category $\Dd(X,\IZ\qpower)$ which *$q$-deforms* the usual de Rham complex in the sense that $\qOmega_{X/\IZ}/(q-1)\simeq \Omega_{X/\IZ}^*$. Moreover, for any prime $p$, the $p$-completion $(\qOmega_{X/\IZ})_p^\complete$ computes the prismatic cohomology of $X\times\Spf \IZ_p[\zeta_p]$ over the prism $(\IZ_p\qpower,[p]_q)$. This makes $q$-de Rham cohomology the only known case (besides de Rham cohomology) in which prismatic cohomology for all primes can be combined into a global object, and so it ought to be important.

Now what do we hope to gain from a version of $q$-de Rham cohomology with coefficients in $\Hh$ instead of $\IZ\qpower$? Besides the general philosophy that whenever one has a deformation at $q=1$, one should look at the other roots of unity as well

[^1]

, here's our main motivation to pursue Question [\[qst:Habiro\]](#qst:Habiro){reference-type="ref" reference="qst:Habiro"}:

::: alphanumerate
A stacky approach to Habiro cohomology is expected to be much more interesting geometrically than a stacky approach to $q$-de Rham cohomology (to the extent that either one exists).[]{#enum:MotivationStackyApproach label="enum:MotivationStackyApproach"}

There's growing evidence that certain $3$-manifold invariants related to Chern--Simons theory take values in Habiro cohomology.[]{#enum:MotivationChernSimons label="enum:MotivationChernSimons"}

[^2]
:::

We'll elaborate on both points below.
:::

::: numpar
The term *stacky approach* refers to the idea that for any reasonable cohomology theory $\R\Gamma_?(X)$ there should be a geometric construction $X\mapsto X^?$ in such a way that $\R\Gamma_?(X)\simeq \R\Gamma(X^?,\Oo)$ is the sheaf cohomology of the geometric object $X^?$. This allows to study algebraic properties of $\R\Gamma_?(X)$ via the geometry of $X^?$, which often holds much richer information.

The first instance of a stacky approach is Simpson's *de Rham stack* for smooth varieties over characteristic $0$ fields [@SimpsonDeRhamStack]. The construction of a stacky approach to prismatic cohomology by Drinfeld and Bhatt--Lurie [@DrinfeldPrismatization; @BhattLurieI; @BhattLurieII] has started a flurry of results in recent years. These include at least the work of Anschütz--Heuer--Le Bras on the *Hodge--Tate stack* [@HodgeTateStack1; @HodgeTateStack2; @HodgeTateStack3], the construction of an *analytic de Rham stack* by Rodríguez Camargo [@AnalyticDeRhamStack], the ongoing work of Anschütz--Bosco--Hauck--Le Bras--Rodríguez Camargo--Scholze on *analytic prismatisation*, the ongoing work of Bhatt--Mathew--Vologodsky--Zhang on *sheared prismatisation*, and the ongoing work of Devalapurkar--Hahn--Raksit--Yuan on recovering prismatisation from their theory of *even stacks* [@EvenStacks].

In [@HabiroCohomologyLecture], Scholze proposes a construction of an *analytic Habiro stack* $X^\mathrm{Hab}$, which gives rise to a cohomology theory with coefficients in an analytic version $\Hh^\mathrm{an}$ of the Habiro ring. We'll remark in [\[par:AlgebraicvsAnalytic\]](#par:AlgebraicvsAnalytic){reference-type="ref" reference="par:AlgebraicvsAnalytic"} on the expected relationship between this cohomology theory and the construction of Habiro cohomology that we propose in this paper. For $q$-de Rham cohomology we don't have a global stacky approach available yet ($p$-adically it works as a special case of prismatisation), but at least an analytic version is expected to exist (compare the discussion in [@qHodge §]).
:::

Let us now explain why a stacky approach to Habiro cohomology should be much more interesting than a stacky approach to $q$-de Rham cohomology by giving a specific example which also nicely illustrates [\[par:WhyHabiroCohomology\]](#par:WhyHabiroCohomology){reference-type="ref" reference="par:WhyHabiroCohomology"}[\[enum:MotivationChernSimons\]](#enum:MotivationChernSimons){reference-type="ref" reference="enum:MotivationChernSimons"}.

::: numpar
Let $F$ be a number field and let $\Delta$ be divisible by $6\operatorname{disc} F$. In [@HabiroRingOfNumberField], Garoufalidis--Scholze--Wheeler--Zagier construct a certain formally étale $\Hh$-algebra $\Hh_{\Oo_F[1/\Delta]}$: the *Habiro ring of the number field $F$* (we'll recall the specific construction in [\[subsec:HabiroRingOfNumberField\]](#subsec:HabiroRingOfNumberField){reference-type="ref" reference="subsec:HabiroRingOfNumberField"}). Moreover, the authors construct a regulator map $$K_3(F)\longrightarrow \Pic\bigl(\Hh_{\Oo_F[1/\Delta]}\bigr)$$ and show that certain $q$-series arising from perturbative Chern--Simons theory naturally form sections of the line bundles in the image of this regulator.

We would like to interpret $\Hh_{\Oo_F[1/\Delta]}$ and its formal spectrum $\Spf \Hh_{\Oo_F[1/\Delta]}$ as the *Habiro cohomology* and the *Habiro stack* of $\Spec \Oo_F[1/\Delta]$, respectively.

[^3]

Already in this special case, the Habiro stack exhibits non-trivial geometry in form of line bundles with interesting sections that come from the regulator $K_3(F)\rightarrow \Pic(\Hh_{\Oo_F[1/\Delta]})$. This geometry would be completely invisible to any $q$-de Rham stack, as the regulator becomes trivial after $(q-1)$-completion!

The construction of Habiro cohomology that we propose in this paper recovers $\Hh_{\Oo_F[1/\Delta]}$ ([\[cor:ComparisonWithGSWZ2\]](#cor:ComparisonWithGSWZ2){reference-type="ref" reference="cor:ComparisonWithGSWZ2"}). It also appears that the connection to Chern--Simons theory extends beyond the étale case. For example, in [@ExplicitClassesInHabiro], Garoufalidis and Wheeler construct certain $(q-1)$-power series with coefficients in de Rham cohomology; these $(q-1)$-power power series are expected to be Habiro cohomology classes. While much of this is still mysterious, it suggests that something highly nontrivial is going on!
:::

[^1]: The Habiro ring can be regared, in a precise sense, as the ring of power series that have a Taylor expansion around each root of unity $\zeta$ with coefficients in $\IZ[\zeta]$. See [\[rem:HTaylorSeries\]](#rem:HTaylorSeries){reference-type="ref" reference="rem:HTaylorSeries"}.

[^2]: In fact, the Habiro ring was introduced by Habiro himself as the target of certain invariants of hyperbolic knots and homology $3$-spheres [@Habiro; @HabiroInvariants].

[^3]: Note that $\Spf \Hh_{\Oo_F[1/\Delta]}$ doesn't precisely match up with Scholze's analytic Habiro stack $(\Spec \Oo_F[1/\Delta])^\mathrm{Hab}$. See the discussion in [\[par:AlgebraicvsAnalytic\]](#par:AlgebraicvsAnalytic){reference-type="ref" reference="par:AlgebraicvsAnalytic"}.
