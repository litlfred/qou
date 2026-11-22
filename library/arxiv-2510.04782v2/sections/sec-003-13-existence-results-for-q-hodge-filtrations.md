---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-003-13-existence-results-for-q-hodge-filtrations
section_title: "Existence results for q-Hodge filtrations"
section_number: 1.3
pages: 7-10
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.836
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#subsec:FunctorialqHodgeIntro label="subsec:FunctorialqHodgeIntro"}

Even though $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ has no section, the $\infty$-category $\cat{AniAlg}_\IZ^{\qHodge}$ still has many interesting objects. One large class of examples can be construced from topological Hochschild homology over $\ku$; this will be the content of the companion paper [@qdeRhamku].

In this paper, we will describe two elementary constructions of $q$-Hodge filtrations that provide sections of $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ over fairly large full subcategories of $\cat{AniAlg}_\IZ$. Let us begin with a construction in the smooth case.

::: numpar
[]{#par:qHodgeForCurves label="par:qHodgeForCurves"} Let $S$ be smooth over $\IZ$. The most naive idea to equip $\qOmega_{S/\IZ}$ (or rather $\qdeRham_{S/\IZ}$, but this distinction doesn't matter by [\[rem:CompleteFiltration\]](#rem:CompleteFiltration){reference-type="ref" reference="rem:CompleteFiltration"}) with a $q$-Hodge filtration would be to simply take the pullback $$\begin{tikzcd}
                \fil_{\qHodge}^\star\qOmega_{S/\IZ}\dar\rar\drar[pullback] & \qOmega_{S/\IZ}\dar\\
                \fil_{\Hodge}^\star\Omega_{S/\IZ}\rar & \Omega_{S/\IZ}
            \end{tikzcd}$$ This cannot work, of course, because in this pullback each filtration step $\fil_{\qHodge}^\star\qOmega_{S/\IZ}$ will contain all of $(q-1)\qOmega_{S/\IZ}$. In view of [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"}[\[enum:qHodgeIntroc\]](#enum:qHodgeIntroc){reference-type="ref" reference="enum:qHodgeIntroc"} this is only ok for $\star\leqslant 1$.

Now if $S$ has relative dimension $\dim(S/\IZ)\leqslant 1$, then the Hodge filtration $\fil_{\Hodge}^\star \Omega_{S/\IZ}^*$ is trivial in filtration degrees $\star\geqslant 2$. Consequently, if $\fil_{\qHodge}^\star\qOmega_{S/\IZ}$ is any filtered $q$-deformation of the Hodge filtration, then $\fil_{\qHodge}^\star\qOmega_{S/\IZ}$ will necessarily be given by the $(q-1)$-adic filtration $(q-1)^{\star-1}\fil_{\qHodge}^1\qOmega_{S/A}$ in filtration degrees $\geqslant 1$. We may thus define the first filtration step $\fil_{\qHodge}^1\qOmega_{S/A}$ using the pullback above and then construct the rest of the filtration as $$\Bigl(\qOmega_{S/\IZ}\leftarrow\fil_{\qHodge}^1\qOmega_{S/\IZ}\leftarrow (q-1)\fil_{\qHodge}^1\qOmega_{S/\IZ}\leftarrow (q-1)^2\fil_{\qHodge}^1\qOmega_{S/\IZ}\leftarrow\dotsb\Bigr)\,.$$ One can (and we will) check that this satisfies all expected properties. As we'll see in [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"}, a variant of this trick still works for $S$ of arbitrary dimension, as long as all primes $p\leqslant \dim(S/\IZ)$ become invertible in $S$. This will lead to the following theorem:
:::

::: thm
[]{#thm:CanonicalqHodgeSmoothIntro label="thm:CanonicalqHodgeSmoothIntro"} The forgetful functor $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ admits a section over the full subcategory $\cat{Sm}_{\IZ[\dim!^{-1}]}\subseteq \cat{AniAlg}_\IZ$ of smooth $\IZ$-algebras $S$ such that all primes $p\leqslant \dim(S/\IZ)$ become invertible in $S$.
:::

::: numpar
[]{#par:AlgebraicHabiroCohomology label="par:AlgebraicHabiroCohomology"} Combining [\[thm:HabiroDescentIntro,thm:CanonicalqHodgeSmoothIntro\]](#thm:HabiroDescentIntro,thm:CanonicalqHodgeSmoothIntro){reference-type="ref" reference="thm:HabiroDescentIntro,thm:CanonicalqHodgeSmoothIntro"} allows us to define canonical objects $\qHhodge_{X/\IZ}\in\Dd(X,\Hh)$ for any smooth scheme $X$ over $\IZ$ such that all primes $p\leqslant \dim(X/\IZ)$ are invertible on $X$. The sheaf cohomology of $\qHhodge_{X/\IZ}$ then deserves to be called the *algebraic Habiro cohomology of $X$*. It behaves in many ways (but not all; see [\[par:AlgebraicvsAnalytic\]](#par:AlgebraicvsAnalytic){reference-type="ref" reference="par:AlgebraicvsAnalytic"}[\[enum:AlgebraicvsAnalyticC\]](#enum:AlgebraicvsAnalyticC){reference-type="ref" reference="enum:AlgebraicvsAnalyticC"} below) as one would expect from an "algebraic" theory. For example, if $X$ is smooth and proper over $\IZ[1/N]$, where $N$ is also divisible by all primes $p\leqslant \dim(X/\IZ)$, then $\R\Gamma(X,\qHhodge_{X/\IZ})$ will be a perfect complex over the Habiro-completion of $\Hh[1/N]$.

Thus, up to throwing away "small primes", algebraic Habiro cohomology provides a tentative answer to Question [\[qst:Habiro\]](#qst:Habiro){reference-type="ref" reference="qst:Habiro"}.
:::

::: numpar
[]{#par:AlgebraicvsAnalytic label="par:AlgebraicvsAnalytic"} It is not yet known how algebraic Habiro cohomology relates to the sheaf cohomology of Scholze's analytic Habiro stack $X^\mathrm{Hab}$, which we would like to call *analytic Habiro cohomology* for clarity. We expect algebraic and analytic Habiro cohomology to become equal after base change to a suitably completed localisation of Scholze's analytic Habiro ring $\Hh^\mathrm{an}$. Note, however, that this base change erases quite some information on either side, and there are several key differences between the algebraic and the analytic construction:

::: alphanumerate
*Evaluation at "small primes".* By construction, algebraic Habiro cohomology of a smooth scheme $X$ will contain no information at primes $p\leqslant \dim(X/\IZ)$. By contrast, analytic Habiro usually does contain non-trivial information at such primes, as $N$ is *not* invertible everywhere on the Habiro stack $\IZ[1/N]^\mathrm{Hab}$.

*Evaluation at roots of unity.* With the current construction, Scholze's analytic Habiro stack becomes the algebraic de Rham stack if $q$ is specialised to a root of unity. In particular, its cohomology will be Grothendieck's infinitesimal cohomology, which is ill-behaved in characteristic $p$. With algebraic Habiro cohomology, evaluation at roots of unity yields $q$-de Rham--Witt cohomology by [\[thm:HabiroDescentIntro\]](#thm:HabiroDescentIntro){reference-type="ref" reference="thm:HabiroDescentIntro"}[\[enum:qdRWComparisonIntro\]](#enum:qdRWComparisonIntro){reference-type="ref" reference="enum:qdRWComparisonIntro"}, which is much closer to crystalline cohomology in characteristic $p$.

*Stacky approach.* By construction, analytic Habiro cohomology comes with a stacky approach. For algebraic Habiro cohomology, we don't expect a stacky approach to exist. In fact, we don't even expect $\qHhodge_{X/\IZ}$ to carry an $\IE_\infty$-algebra structure! The reason goes roughly as follows: The multiplication ("cup product") on $\qHhodge_{X/\IZ}$ should come from the diagonal embedding $\Delta\colon X\rightarrow X\times X$. Thus, for the multiplication to be defined, we need to invert all primes $p\leqslant \dim(X\times X/\IZ)=2\dim(X/\IZ)$. Similarly, for the multiplication to be homotopy-associative, we should invert all primes up to $p\leqslant 3\dim(X/\IZ)$, and to get it more and more coherent, we need to invert more and more primes.[]{#enum:AlgebraicvsAnalyticC label="enum:AlgebraicvsAnalyticC"}
:::

In the second half of [\[subsec:CanonicalqHodgeSmooth\]](#subsec:CanonicalqHodgeSmooth){reference-type="ref" reference="subsec:CanonicalqHodgeSmooth"} we'll make the considerations from [\[enum:AlgebraicvsAnalyticC\]](#enum:AlgebraicvsAnalyticC){reference-type="ref" reference="enum:AlgebraicvsAnalyticC"} precise, and we'll show a formal monoidality statement in [\[cor:CanonicalqHodgeSmoothMonoidal\]](#cor:CanonicalqHodgeSmoothMonoidal){reference-type="ref" reference="cor:CanonicalqHodgeSmoothMonoidal"}.
:::

There's a second case in which we're able to show the existence of functorial $q$-Hodge filtrations:

::: numpar
[]{#par:CanonicalqHodgeQuasiregular label="par:CanonicalqHodgeQuasiregular"} Let $R$ be a ring satisfying the following conditions:

::: alphanumerate

For all primes $p$, $R$ is $p$-torsion free, the $p$-completed derived de Rham complex $(\deRham_{R/\IZ})_p^\complete$ is static, i.e. an actual ring concentrated in degree $0$, and the Hodge filtration $\fil_{\Hodge}^\star(\deRham_{R/\IZ})_p^\complete$ is a descending filtration of ideals.[]{#enum:RQuasiregular label="enum:RQuasiregular"}
:::

For example, this happens in the following case (see [\[lem:RelativelySemiperfect\]](#lem:RelativelySemiperfect){reference-type="ref" reference="lem:RelativelySemiperfect"}): Let $B$ be a perfect $\Lambda$-ring, let $B'$ be an étale $B$-algebra, and let $R\cong B'/J$, where $J$ is generated by a Koszul-regular sequence. If $R$ is $p$-torsion free, then it will satisfy the other conditions from [\[enum:RQuasiregular\]](#enum:RQuasiregular){reference-type="ref" reference="enum:RQuasiregular"} as well.

If $R$ satisfies these assumptions, then $(\qdeRham_{R/\IZ})_p^\complete$ is static as well, and we can construct a filtration on on it in a very naive way: We define $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ to be the (non-derived!) preimage of the combined Hodge and $(q-1)$-adic filtration $\fil_{(\Hodge,q-1)}^\star(\deRham_{R/\IZ})_p^\complete[1/p]\qpower$ under $$\bigl(\qdeRham_{R/\IZ}\bigr)_p^\complete\longrightarrow\bigl(\qdeRham_{R/\IZ}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\simeq \bigl(\deRham_{R/\IZ}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower\,.$$ A priori, there's no reason to expect that $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ would be well-behaved at all; in particular, it's usually not a $q$-deformation of the Hodge filtration $\fil_{\Hodge}^\star(\deRham_{R/\IZ})_p^\complete$. This is closely related to the non-existence of a section of $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$; see [\[exm:MainSpecialCase\]](#exm:MainSpecialCase){reference-type="ref" reference="exm:MainSpecialCase"}. However, in the following two cases everything works:
:::

::: thm
[]{#thm:qHodgeWellBehavedIntro label="thm:qHodgeWellBehavedIntro"} With assumptions as above, suppose that one of the following two additional conditions is satisfied:

::: alphanumerate
$R\cong B'/J$ as in [\[par:CanonicalqHodgeQuasiregular\]](#par:CanonicalqHodgeQuasiregular){reference-type="ref" reference="par:CanonicalqHodgeQuasiregular"} and $J$ is generated by a Koszul regular sequence of higher powers; that is, $J=(x_1^{\alpha_1},\dotsc,x_r^{\alpha_r})$, where $(x_1,\dotsc,x_r)$ is Koszul-regular and $\alpha_i\geqslant 2$ for all $i$.[]{#enum:RegularSequenceHigherPowersIntro label="enum:RegularSequenceHigherPowersIntro"}

$R$ admits a lift to an $\IE_1$-ring spectrum $\IS_R$ such that $R\simeq \IS_R\otimes\IZ$.[]{#enum:E1LiftIntro label="enum:E1LiftIntro"}
:::

Then the above filtration $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ is a $q$-deformation of the Hodge filtration
:::

Note that [\[thm:qHodgeWellBehavedIntro\]](#thm:qHodgeWellBehavedIntro){reference-type="ref" reference="thm:qHodgeWellBehavedIntro"}[\[enum:E1LiftIntro\]](#enum:E1LiftIntro){reference-type="ref" reference="enum:E1LiftIntro"} is purely an existence condition; the choice of $\IS_R$ doesn't matter! We'll show in [\[con:GlobalqHodge\]](#con:GlobalqHodge){reference-type="ref" reference="con:GlobalqHodge"} that the $p$-complete filtrations $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ can be glued with the combined Hodge and $(q-1)$-adic filtration $\fil_{(\Hodge,q-1)}^\star(\deRham_{R/\IZ}\lotimes_\IZ\IQ)\qpower$ to obtain a filtration $\fil_{\qHodge}^\star\qdeRham_{R/\IZ}$ on the global derived $q$-de Rham complex. This leads to the following result:

::: thm
[]{#thm:CanonicalqHodgeQuasiregularIntro label="thm:CanonicalqHodgeQuasiregularIntro"} Let $\cat{QReg}_\IZ^{\qHodge}$ denote the category of rings $R$ that satisfy the conditions from [\[par:CanonicalqHodgeQuasiregular\]](#par:CanonicalqHodgeQuasiregular){reference-type="ref" reference="par:CanonicalqHodgeQuasiregular"}[\[enum:RQuasiregular\]](#enum:RQuasiregular){reference-type="ref" reference="enum:RQuasiregular"} and such that $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ is a $q$-deformation of the Hodge filtration for all primes $p$. Then the forgetful functor $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ admits a section over the full subcategory $\cat{QReg}_\IZ^{\qHodge}\subseteq \cat{AniAlg}_\IZ$.
:::

::: numpar
It's natural to ask if the sections from [\[thm:CanonicalqHodgeSmoothIntro,thm:CanonicalqHodgeQuasiregularIntro\]](#thm:CanonicalqHodgeSmoothIntro,thm:CanonicalqHodgeQuasiregularIntro){reference-type="ref" reference="thm:CanonicalqHodgeSmoothIntro,thm:CanonicalqHodgeQuasiregularIntro"} are unique. In the quasi-regular case, it will be straightforward to see that the section we construct is terminal among all choices, and then the $q$-deformation condition from [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"}[\[enum:qHodgeIntrob\]](#enum:qHodgeIntrob){reference-type="ref" reference="enum:qHodgeIntrob"} forces it to be unique.

In the smooth case, we need to assume additionally that our $q$-Hodge filtrations are compatible with the morphism $\qOmega_{S/A}\rightarrow \Omega_{S/A}\qpower/(q-1)^n$ from [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"} below, or alternatively, that $\fil_{\qHodge}^\star(\qdeRham_{R/\IZ})_p^\complete$ acquires a $\IZ_p^\times$-action compatible with the one on $p$-completed $q$-de Rham cohomology (see [\[rem:pTildeDeRham\]](#rem:pTildeDeRham){reference-type="ref" reference="rem:pTildeDeRham"}). If this additional compatibility is assumed, it will be straightforward to see that the section we construct is initial among all choices, and thus unique again by [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"}[\[enum:qHodgeIntrob\]](#enum:qHodgeIntrob){reference-type="ref" reference="enum:qHodgeIntrob"}.
:::
