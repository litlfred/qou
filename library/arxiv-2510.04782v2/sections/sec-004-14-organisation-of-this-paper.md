---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-004-14-organisation-of-this-paper
section_title: "Organisation of this paper"
section_number: 1.4
pages: 10-13
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.967
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
In [\[sec:HabiroRingsEtale\]](#sec:HabiroRingsEtale){reference-type="ref" reference="sec:HabiroRingsEtale"}, we'll recall and generalise the construction of *Habiro rings of étale extensions* from [@HabiroRingOfNumberField], and we'll relate them to the rings of *$q$-Witt vectors* from [@qWitt]. This is a special case of our more general results in [\[sec:HabiroDescent\]](#sec:HabiroDescent){reference-type="ref" reference="sec:HabiroDescent"}, but much less technical, so it will be worthwhile to spell out the étale case first.

In [\[sec:HabiroDescent\]](#sec:HabiroDescent){reference-type="ref" reference="sec:HabiroDescent"}, we'll prove our main Habiro descent result. This section is long and technical. It may be helpful to read the proof of [\[lem:qHodgeSymmetricMonoidal\]](#lem:qHodgeSymmetricMonoidal){reference-type="ref" reference="lem:qHodgeSymmetricMonoidal"} first. At the end of [\[subsec:MainResult\]](#subsec:MainResult){reference-type="ref" reference="subsec:MainResult"}, we explain how the proof of [\[thm:HabiroDescent\]](#thm:HabiroDescent){reference-type="ref" reference="thm:HabiroDescent"} proceeds by generalising the arguments from the proof of [\[lem:qHodgeSymmetricMonoidal\]](#lem:qHodgeSymmetricMonoidal){reference-type="ref" reference="lem:qHodgeSymmetricMonoidal"}.

In [\[sec:FunctorialqHodge\]](#sec:FunctorialqHodge){reference-type="ref" reference="sec:FunctorialqHodge"}, we'll show that despite the general non-existence result, it's possible to construct functorial $q$-Hodge filtrations on fairly large full subcategories of rings. Finally, there will be two appendices: In [\[appendix:GlobalqDeRham\]](#appendix:GlobalqDeRham){reference-type="ref" reference="appendix:GlobalqDeRham"}, we explain the gluing argument to obtain the global $q$-de Rham complex from the $p$-complete $q$-de Rham complex of Bhatt--Scholze. In [\[appendix:HabiroCompletion\]](#appendix:HabiroCompletion){reference-type="ref" reference="appendix:HabiroCompletion"}, we study the completion that appears in the Habiro ring and show that it behaves like the usual (derived) completion at an ideal.

::: numpar
[]{#par:Notations label="par:Notations"} Throughout the article, we freely use the language of $\infty$-categories, and we'll adopt the following conventions:

::: alphanumerate
**Graded and filtered objects.** For a stable $\infty$-category $\Cc$, we let $\Gr(\Cc)$ and $\Fil(\Sp)$ denote the $\infty$-categories of *graded* and *filtered objects in $\Cc$*. The shift in graded or filtered objects will be denoted $(-)(1)$. An object with a descending filtration is typically denoted $$\fil^\star X=\Bigl(\dotsb\leftarrow \fil^nX\leftarrow \fil^{n+1}X\leftarrow\dotsb\Bigl)$$ and we let $\gr^*X$ denote the *associated graded*, given by $\gr^nX\coloneqq \cofib(\fil^{n+1}X\rightarrow \fil^nX)$. We mostly work with filtrations that are constant in degrees $\leqslant 0$ (such as the Hodge filtration). In this case we'll abusingly write $\fil^\star X=(\fil^0X\leftarrow \fil^1 X\leftarrow\dotsb)$; this should be interpreted as the constant $\fil^0X$-valued filtration in degrees $\leqslant 0$.

If $\Cc$ is symmetric monoidal and the tensor product $-\otimes-$ commutes with colimits in both variables, we equip $\Gr(\Cc)$ and $\Fil(\Cc)$ with their canonical symmetric monoidal structures given by Day convolution. We'll use the fact that $\Fil(\Cc)\simeq \Mod_{\IUnit_{\Gr}[t]}\Gr(\Cc)$, where $\IUnit_{\Gr}$ denotes the tensor unit in $\Gr(\Cc)$ and $t$ sits in graded degree $-1$; see e.g. [@RaksitFilteredCircle Proposition ]. Under this equivalence, passing to the associated graded corresponds to "modding out $t$", i.e. the base change $\IUnit_{\Gr}\otimes_{\IUnit_{\Gr}[t]}-$.

We say that $\fil^\star X$ is an *exhaustive filtration on $X$* if $X\simeq \colimit_{n\rightarrow -\infty}\fil^nX$. We say that a filtered object $\fil^\star X$ is *complete* if $0\simeq \limit_{n\rightarrow \infty}\fil^nX$. We define the *completion* $\fil^\star \widehat{X}\coloneqq \limit_{n\rightarrow\infty}\cofib(\fil^{\star+n} X\rightarrow\fil^{\star}X)$. By construction, there's a pullback square $$\begin{tikzcd}
                    \fil^\star X\rar\dar\drar[pullback] & \fil^\star \widehat{X}\dar\\
                    X\rar & \widehat{X}
                \end{tikzcd}$$ We'll often refer to this by saying that *every filtration is the pullback of its completion*.

Sometimes we also consider *ascending* filtrations. Ascendingly filtered objects will be denoted $\fil_\star X=(\dotsb\rightarrow \fil_nX\rightarrow \fil_{n+1}X\rightarrow \dotsb)$ and the associated graded by $\gr_*X$, where $\gr_nX\coloneqq \cofib(\fil^{n-1}X\rightarrow \fil^nX)$.

**Animation.** For an ordinary ring $A$, we consider the $\infty$-category of *animated $A$-algebras $\cat{AniAlg}_A$*, which is the $\infty$-category freely generated under sifted colimits (in the sense of [@HTT Proposition ]) by the category $\cat{Poly}_A$ of polynomial $A$-algebras in finitely many variables.

We'll often use the fact that any functor $F\colon \cat{Poly}_A\rightarrow \Dd$ into an $\infty$-category with all sifted colimits can be uniquely extended to a sifted colimits preserving functor $\L F\colon \cat{AniAlg}_A\rightarrow \Dd$. We often call $\L F$ the *animation* or the *derived functor of $F$*. The most important examples for us will be the $q$-de Rham complex (which is only defined in the case where $A$ is a $\Lambda$-ring) and the Hodge-filtered de Rham complex $$\qOmega_{-/A}\colon \cat{Poly}_A\longrightarrow \widehat{\Dd}_{(q-1)}\bigl(A\qpower\bigr)\quad\text{and}\quad \fil_{\Hodge}^\star\Omega_{-/A}^*\colon \cat{Poly}_A\longrightarrow \Fil\Dd(A)$$ (the former is only defined if $A$ is a $\Lambda$-ring), whose animations we'll denote by $\qdeRham_{-/A}$ and $\fil_{\Hodge}^\star\deRham_{-/A}$, respectively.

**Derived categories.** For a ring $R$, we let $\Dd(R)$ denote the derived $\infty$-category of $R$-modules. The shift functor and its inverse in $\Dd(R)$ will always be denoted by $\Sigma$ and $\Sigma^{-1}$, to avoid confusion with shifts in graded or filtered objects, as we'll frequently mix both settings.

For an element $f\in R$ and an object $M\in \Dd(R)$, we let $$M/f\coloneqq \cofib\left(f\colon M\rightarrow M\right)\,.$$ For several elements $f_1,\dotsc,f_r\in R$, we let $M/(f_1,\dotsc,f_r)\coloneqq (\dotsb(M/f_1)/f_2\dotsb)/f_r$. We warn the reader that for ordinary $R$-modules $M$, the derived quotient $M/(f_1,\dotsc,f_r)$ agrees with the usual quotient only if $(f_1,\dotsc,f_r)$ is a Koszul-regular sequence on $M$.

Similarly, if $R^*$ is a graded ring, $f\in R^i$ is a homogeneous element of degree $i$, and $M^*\in\Mod_{R^*}\Gr(\Dd(\IZ))$, we put $M^*/f\coloneqq \cofib(f\colon M(i)\rightarrow M)$ and define $M^*/(f_1,\dotsc,f_r)$ analogously. The same notation will also be used in the filtered setting, by regarding filtered objects as graded $\IUnit_{\Gr}[t]$-modules, as explained above.

**Derived completions.** With notation as above, we define the *$(f_1,\dotsc,f_r)$-adic completion* of $M$ as the limit $$\widehat{M}_{(f_1,\dotsc,f_r)}\coloneqq \lim_{n\geqslant 1}M/(f_1^n,\dotsc,f_r^n)$$ taken in the derived $\infty$-category $\Dd(R)$. Since the completion only depends on the ideal $I=(f_1,\dotsc,f_r)\subseteq R$, we often just write $\widehat{M}_I$ (or $(-)_I^\complete$ for longer arguments). Completion can be analogously defined in the graded or filtered setting and we'll use the same notation in these cases.

In the case where $I=(f)$ is a principal ideal, the following square is always a pullback in $\Dd(R)$: $$\begin{tikzcd}
                    M\rar\dar\drar[pullback] & \widehat{M}_f\dar\\
                    M\bigl[\localise{f}\bigr]\rar & \widehat{M}_f\bigl[\localise{f}\bigr]
                \end{tikzcd}$$ This will be called a *fracture square*. In the special case where $f=N$ is an integer, we'll use the term *arithmetic fracture square*.

For general $I=(f_1,\dotsc,f_r)$, we let $\widehat{\Dd}_{I}(R)\subseteq \Dd(R)$, denote the full sub-$\infty$-category spanned by the *$I$-complete objects*, that is, those $M$ for which $M\simeq \widehat M_{I}$. The following fact will be used countless times: If $M$ is $(f_1,\dotsc,f_r)$-complete, and the homology of $M/(f_1,\dotsc,f_r)$ vanishes in some degree $d$, then also the homology of $M$ must vanish in degree $d$. Analogous conclusions hold true in the graded and filtered settings.

**Perfectly covered $\boldsymbol\Lambda$-rings.** We call a $\Lambda$-ring *perfectly* covered if there exists a faithfully flat $\Lambda$-morphism $A\rightarrow A_\infty$ into a perfect $\Lambda$-ring. Equivalently, the Adams operations $\psi^m\colon A\rightarrow A$ are all faithfully flat (see e.g. [@qWitt Remark ]). This condition is satisfied in many examples of interest; for example, it holds for $\IZ$, for any free $\Lambda$-ring $\IZ\left\{x_i\ \middle|\ i\in I\right\}$, and for any polynomial ring $\IZ\left[x_i\ \middle|\ i\in I\right]$ equipped with the *toric $\Lambda$-structure* in which $\lambda^n(x_i)=0$ for all $n>1$.
:::
:::

::: numpar
First and foremost, I'm grateful to Peter Scholze for suggesting this question and for his support throughout the project. I'm glad that it has paid off to keep working on this question despite the initial upset: Four years after proving that the $q$-Hodge complex isn't functorial, we can now prove that it is. I would also like to thank Stavros Garoufalidis, Quentin Gazda, and Campbell Wheeler for many helpful discussions on Habiro cohomology.

This work was carried out while I was a Ph.D. student at the MPIM/University Bonn, and I would like to thank these institutions for their hospitality. Finally, I'm grateful for the financial support provided by the DFG through Peter Scholze's Leibniz prize.
:::
