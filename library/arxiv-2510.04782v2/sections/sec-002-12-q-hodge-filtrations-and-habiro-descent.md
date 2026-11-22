---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-002-12-q-hodge-filtrations-and-habiro-descent
section_title: "q-Hodge filtrations and Habiro descent"
section_number: 1.2
pages: 4-7
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.746
latex_coverage_ratio: 0.941
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
Having justified that Question [\[qst:Habiro\]](#qst:Habiro){reference-type="ref" reference="qst:Habiro"} is relevant, let us now summarise the contributions of this paper. As it turns out, Question [\[qst:Habiro\]](#qst:Habiro){reference-type="ref" reference="qst:Habiro"} is closely related to the following much less esoteric question:

::: numpar
[]{#qst:qHodgeFiltration label="qst:qHodgeFiltration"} *Is it possible to equip the $q$-de Rham complex with a $q$-deformation of the Hodge filtration?*
:::

To pose this question more formally, we'll introduce the following notion:

::: defi
[]{#def:qHodgeIntro label="def:qHodgeIntro"} Let $R$ be an animated ring and let $\qdeRham_{R/\IZ}$ be its derived $q$-de Rham complex. A *$q$-Hodge filtration* is a $(q-1)$-complete filtered module $$\fil_{\qHodge}^\star\qdeRham_{R/\IZ}= \Bigl(\fil_{\qHodge}^0\qdeRham_{R/\IZ}\leftarrow\fil_{\qHodge}^0\qdeRham_{R/\IZ}\leftarrow\dotsb\Bigr)$$ over the $(q-1)$-adically filtered ring $(q-1)^\star \IZ\qpower$, such that:

::: alphanumerate
$\fil_{\qHodge}^\star\qdeRham_{R/\IZ}$ is a descending filtration on the derived $q$-de Rham complex. That is,[]{#enum:qHodgeIntroa label="enum:qHodgeIntroa"} $$\fil_{\qHodge}^0\qdeRham_{R/\IZ}\simeq \qdeRham_{R/\IZ}\,.$$

$\fil_{\qHodge}^\star\qdeRham_{R/\IZ}$ is a filtered $q$-deformation of the Hodge filtration on the derived de Rham complex $\deRham_{R/\IZ}$. That is,[]{#enum:qHodgeIntrob label="enum:qHodgeIntrob"} $$\fil_{\qHodge}^\star \qdeRham_{R/\IZ}\lotimes_{(q-1)^\star\IZ\qpower}\IZ\simeq \fil_{\Hodge}^\star\deRham_{R/\IZ}\,.$$

Rationally, $\fil_{\qHodge}^\star$ becomes the combined Hodge and $(q-1)$-adic filtration on $(\deRham_{R/\IZ}\lotimes_\IZ\IQ)\qpower$. That is,[]{#enum:qHodgeIntroc label="enum:qHodgeIntroc"} $$\bigl(\fil_{\qHodge}^\star\qdeRham_{R/\IZ}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\simeq \fil_{(\Hodge,q-1)}^\star\bigl(\deRham_{R/\IZ}\lotimes_\IZ\IQ\bigr)\qpower\,.$$

The same holds true for any prime $p$ if we $p$-complete first and then rationalise. That is,[]{#enum:qHodgeIntrocp label="enum:qHodgeIntrocp"} $$\fil_{\qHodge}^\star\bigl(\qdeRham_{R/\IZ}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\overset{\simeq}{\longrightarrow}\fil_{(\Hodge,q-1)}^\star\bigl(\deRham_{R/\IZ}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower\,.$$
:::

Moreover, the equivalences from [\[enum:qHodgeIntroa\]](#enum:qHodgeIntroa){reference-type="ref" reference="enum:qHodgeIntroa"}--[\[enum:qHodgeIntrocp\]](#enum:qHodgeIntrocp){reference-type="ref" reference="enum:qHodgeIntrocp"} need to satisfy the obvious compatibilities (and compatibilities between compatibilities); the precise data required will be spelled out in [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}.

We also let $\cat{AniAlg}_{\IZ}^{\qHodge}$ denote the $\infty$-category of pairs $(R,\fil_{\qHodge}^\star\qdeRham_{R/\IZ})$, where $R$ is an animated ring and $\fil_{\qHodge}^\star\qdeRham_{R/\IZ}$ is a $q$-Hodge filtration as above. To any such pair, we associate the *$q$-Hodge complex* $$\qHodge_{(R, \fil_{\smash{\qHodge}}^\star )/\IZ}\coloneqq \colimit\Bigl( \fil_{\qHodge}^0\qdeRham_{R/\IZ}\xrightarrow{(q-1)} \fil_{\qHodge}^1\qdeRham_{R/\IZ}\xrightarrow{(q-1)}\dotsb\Bigr)_{(q-1)}^\complete\,.$$ If the $q$-Hodge filtration is clear from the context, we'll often abusingly write just $\qHodge_{R/\IZ}$.
:::

::: rem
We've used the derived de Rham complex in [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"} because we would like to apply the definition in cases where $R$ isn't smooth; [\[subsec:FunctorialqHodgeIntro\]](#subsec:FunctorialqHodgeIntro){reference-type="ref" reference="subsec:FunctorialqHodgeIntro"}. If $S$ is smooth, it doesn't matter whether we put a $q$-Hodge filtration on $\qdeRham_{S/\IZ}$, or a filtration satisfying analogous conditions on the underived $q$-de Rham complex $\qOmega_{S/\IZ}$; see [\[rem:CompleteFiltration\]](#rem:CompleteFiltration){reference-type="ref" reference="rem:CompleteFiltration"} for an argument.
:::

::: rem
The conditions from [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"}[\[enum:qHodgeIntroc\]](#enum:qHodgeIntroc){reference-type="ref" reference="enum:qHodgeIntroc"} and [\[enum:qHodgeIntrocp\]](#enum:qHodgeIntrocp){reference-type="ref" reference="enum:qHodgeIntrocp"} are natural to ask in view of $(\qdeRham_{R/\IZ}\lotimes_\IZ\IQ)_{(q-1)}^\complete\simeq (\deRham_{R/\IZ}\lotimes_\IZ\IQ)\qpower$ and $(\qdeRham_{R/\IZ})_p^\complete[1/p]_{(q-1)}^\complete\simeq (\deRham_{R/\IZ})_p^\complete[1/p]\qpower$; see [\[thm:qDeRhamGlobal\]](#thm:qDeRhamGlobal){reference-type="ref" reference="thm:qDeRhamGlobal"}[\[enum:GlobalqDeRhamRational\]](#enum:GlobalqDeRhamRational){reference-type="ref" reference="enum:GlobalqDeRhamRational"} and [\[lem:RationalisationTechnicalI\]](#lem:RationalisationTechnicalI){reference-type="ref" reference="lem:RationalisationTechnicalI"}. It doesn't seem to be the case that [\[enum:qHodgeIntrocp\]](#enum:qHodgeIntrocp){reference-type="ref" reference="enum:qHodgeIntrocp"} follows from the other conditions and it will be a crucial assumption.
:::

::: numpar
With [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"}, we can rephrase Question [\[qst:qHodgeFiltration\]](#qst:qHodgeFiltration){reference-type="ref" reference="qst:qHodgeFiltration"} more formally as follows: *Does the forgetful functor $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ admit a section?* The answer to this is, provably, *no*! Nevertheless, the forgetful functor does have sections over surprisingly large full subcategories of $\cat{AniAlg}_\IZ$, as we'll see in [\[subsec:FunctorialqHodgeIntro\]](#subsec:FunctorialqHodgeIntro){reference-type="ref" reference="subsec:FunctorialqHodgeIntro"}.

The general non-existence of a section of $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ is known to the experts and we'll reproduce the argument in [\[lem:NoFunctorialqHodgeFiltration\]](#lem:NoFunctorialqHodgeFiltration){reference-type="ref" reference="lem:NoFunctorialqHodgeFiltration"}. In the following, we'll present an essentially equivalent argument in a non-standard way, which will also serve to motivate our first main positive result.
:::

::: numpar
[]{#par:qHodgeFiltrationInCoordinates label="par:qHodgeFiltrationInCoordinates"} Let $(S,\square)$ be a *framed smooth algebra over $\IZ$*. That is, $S$ is smooth over $\IZ$ and $\square \colon \IZ[x_1,\dotsc,x_n]\rightarrow S$ is an étale map. In this case, the $q$-de Rham complex $\qOmega_{S/\IZ}$ can be represented by the explicit complex $$\qOmega_{S/\IZ,\square}^*\coloneqq\left(S\qpower \xrightarrow{\q\nabla}\Omega_{S/\IZ}^1\qpower\xrightarrow{\q\nabla} \dotsb \xrightarrow{\q\nabla} \Omega^n_{S/\IZ}\qpower \right)$$ defined in [@Toulouse [§]{.upright}]. On this explicit complex, we can define a filtration $\fil_{\qHodge,\square}^\star\qOmega_{S/\IZ, \square}^*$, in which $\fil_{\qHodge,\square}^i$ is the subcomplex $$\left((q-1)^iS\qpower\rightarrow(q-1)^{i-1}\Omega_{S/\IZ}^1\qpower\rightarrow\dotsb\rightarrow\Omega_{S/\IZ}^i\qpower\rightarrow\dotsb\rightarrow\Omega_{S/\IZ}^n\qpower\right)\,.$$ Up to the discrepancy between $\qOmega_{S/\IZ}$ and $\qdeRham_{S/\IZ}$, which is easily fixed (see [\[rem:CompleteFiltration\]](#rem:CompleteFiltration){reference-type="ref" reference="rem:CompleteFiltration"}), the pair $(S,\fil_{\qHodge,\square}^\star)$ becomes an object in $\cat{AniAlg}_\IZ^{\qHodge}$.

It's straightforward to check that the associated $q$-Hodge complex in the sense of [\[def:qHodgeIntro\]](#def:qHodgeIntro){reference-type="ref" reference="def:qHodgeIntro"} can be represented by the explicit complex $$\qHodge_{S/\IZ, \square}^*\coloneqq\Bigl(S\qpower \xrightarrow{(q-1)\q\nabla}\Omega_{S/\IZ}^1\qpower\xrightarrow{(q-1)\q\nabla} \dotsb \xrightarrow{(q-1)\q\nabla} \Omega^n_{S/\IZ}\qpower \Bigr)$$ in which all $q$-differentials in $\qOmega_{S/\IZ,\square}$ get multiplied by $(q-1)$. This *coordinate-dependent $q$-Hodge complex* first shows up in Pridham's work [@Pridham] and was extensively studied in previous work of the author. In [@qWitt Theorem ], we showed that for all $m\in\IN$ the cohomology $$\H^*\bigl(\qHodge_{S/\IZ,\square}/(q^m-1)\bigr)\cong \bigl(\qIW_m\Omega_{S/\IZ}^*\bigr)_{(q-1)}^\complete$$ agrees with the $(q-1)$-completion of a certain object $\qIW_m\Omega_{S/\IZ}^*$, which we call the *$m$-truncated $q$-de Rham--Witt complex of $S$* [@qWitt Definition ]. The system $(\qIW_m\Omega_{S/\IZ}^*)_{m\in\IN}$ satisfies a similar universal property as the de Rham--Witt pro-complex and so $\qIW_m\Omega_{S/\IZ}^*$ is functorial in $S$. In particular, the cohomology $\H^*(\qHodge_{S/\IZ,\square}/(q^m-1))$ is independent of the choice of $\square$!

In spite of this promising observation, we show in [@qWitt Theorem ] that it is *impossible* to turn the $q$-Hodge complex into a functor of smooth $\IZ$-algebras, $$\qHodge_{-/\IZ}\colon \cat{Sm}_\IZ \longrightarrow \Dd\bigl(\IZ\qpower\bigr)\,,$$ in such a way that $\H^*(\qHodge_{-/\IZ}/(q^m-1))\cong (\qIW_m\Omega_{-/\IZ}^*)_{(q-1)}^\complete$ becomes functorial as well.

This strange no-go result is a strong objection against the existence of a section of the forgetful functor $\cat{AniAlg}_\IZ^{\qHodge}\rightarrow \cat{AniAlg}_\IZ$ (and it can be turned into a complete proof using [\[thm:HabiroDescentIntro\]](#thm:HabiroDescentIntro){reference-type="ref" reference="thm:HabiroDescentIntro"}[\[enum:qdRWComparisonIntro\]](#enum:qdRWComparisonIntro){reference-type="ref" reference="enum:qdRWComparisonIntro"} below). Nevertheless, the fact that $\H^*(\qHodge_{S/\IZ, \square}^*/(q^m-1))$ is the $(q-1)$-completion of something canonical looks exactly like what we would expect to see if the $q$-Hodge complex were to descend to the Habiro ring!

Our first main result says that this is indeed true: The $q$-Hodge complex, whenever it is defined, is canonically the $(q-1)$-completion of another object defined over the Habiro ring. Moreover, a derived version of the comparison with $q$-de Rham--Witt complexes holds true, even without the $(q-1)$-completion:
:::

::: thm
[]{#thm:HabiroDescentIntro label="thm:HabiroDescentIntro"} Let $\widehat{\Dd}_{(q-1)}(\IZ[q])$ and $\widehat{\Dd}_\Hh(\IZ[q])$ denote the $(q-1)$- and Habiro-complete objects , respectively, in the derived $\infty$-category of $\IZ[q]$.

::: alphanumerate
The $q$-Hodge complex functor $\qHodge_{-/\IZ}\colon \cat{AniAlg}_\IZ^{\qHodge}\rightarrow \widehat{\Dd}_{(q-1)}(\IZ[q])$ admits a non-trivial symmetric monoidal factorisation[]{#enum:HabiroDescentIntro label="enum:HabiroDescentIntro"} $$\begin{tikzcd}[column sep=huge]
                    & \widehat{\Dd}_\Hh\bigl(\IZ[q]\bigr)\dar["(-)_{(q-1)}^\complete"]\\
                    \cat{AniAlg}_\IZ^{\qHodge}\rar["\qHodge_{-/\IZ}"']\urar[dashed,"\qHhodge_{-/\IZ}"] & \widehat{\Dd}_{(q-1)}\bigl(\IZ[q]\bigr)
                \end{tikzcd}$$

For all $m\in\IN$, the quotient $\qHhodge_{-/\IZ}/(q^m-1)$ admits an exhaustive ascending filtration $\fil_\star ^{\qIW_m\Omega}(\qHhodge_{-/\IZ}/(q^m-1))$ with associated graded[]{#enum:qdRWComparisonIntro label="enum:qdRWComparisonIntro"} $$\gr_*^{\qIW_m\Omega}\bigl(\qHhodge_{-/\IZ}/(q^m-1)\bigr)\simeq \Sigma^{-*}\qIW_m\deRham_{-/\IZ}^*\,,$$ where $\qIW_m\deRham_{-/\IZ}^*$ denotes the derived $m$-truncated $q$-de Rham--Witt complex.
:::
:::

::: defi
$\qHhodge_{-/\IZ}$ from [\[thm:HabiroDescent\]](#thm:HabiroDescent){reference-type="ref" reference="thm:HabiroDescent"}[\[enum:HabiroDescentIntro\]](#enum:HabiroDescentIntro){reference-type="ref" reference="enum:HabiroDescentIntro"} will be called *Habiro--Hodge complex*.
:::

::: rem
For objects $(S,\fil_{\qHodge}^\star\qdeRham_{S/\IZ})\in\cat{AniAlg}_\IZ^{\qHodge}$ such that $S$ is smooth over $\IZ$, we'll show in [\[prop:Letaq-1\]](#prop:Letaq-1){reference-type="ref" reference="prop:Letaq-1"} that $\qOmega_{S/\IZ}\simeq \L\eta_{(q-1)}\qHodge_{S/\IZ}$, where $\L\eta_{(q-1)}$ denotes the Berthelot--Ogus décalage functor (see [@BMS1 §] or [@Stacks]). So in this case, the $q$-de Rham complex can be descended to the Habiro ring as well via $\L\eta_{(q-1)}\qHhodge_{S/\IZ}$.

In general, it seems that only the $q$-Hodge complex and not the $q$-de Rham complex admits descent to the Habiro ring. Here's an informal reason why the $q$-Hodge complex is a more canonical candidate for such a descent: In the (coordinate-dependent) $q$-de Rham complex of $\IZ[x]$, the $q$-differential sends $x^m\mapsto [m]_q x^{m-1}\d x$, where $[m]_q=1+q+\dotsb+q^{m-1}$ is the $q$-analogue of $m$. This formula gives "special treatment to $q=1$", whereas the most canonical object to descend to the Habiro ring should "treat all roots of unity equally". So we should look for a complex with differentials that send $x^m\mapsto (q^m-1)x^{m-1}\d x$, which leads to the (coordinate-dependent) $q$-Hodge complex.
:::
