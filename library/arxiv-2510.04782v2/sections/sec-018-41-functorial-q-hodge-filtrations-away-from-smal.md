---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-018-41-functorial-q-hodge-filtrations-away-from-smal
section_title: "Functorial q-Hodge filtrations away from small primes"
section_number: 4.1
pages: 53-60
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.968
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#subsec:CanonicalqHodgeSmooth label="subsec:CanonicalqHodgeSmooth"}

In this subsection, we'll give an elementary construction of a functorial $q$-Hodge filtration on certain smooth $A$-algebras. In the introduction (see [\[par:qHodgeForCurves\]](#par:qHodgeForCurves){reference-type="ref" reference="par:qHodgeForCurves"}), we've already explained the idea in the case of relative dimension $\leqslant1$. The general case follows the same simple idea.

::: numpar
[]{#par:CanonicalqHodgeSmoothI label="par:CanonicalqHodgeSmoothI"} Let $S$ be smooth of arbitrary dimension over $A$ and let $n$ be a positive integer such that all primes $p\leqslant n$ are invertible in $S$. This assumption ensures that the canonical map $\qOmega_{S/A}\rightarrow \Omega_{S/A}$ factors through an $\IE_\infty$-$A\qpower$-algebra map $$\qOmega_{S/A}\longrightarrow \Omega_{S/A}\qpower/(q-1)^n\,.$$ Indeed, by construction of the global $q$-de Rham complex (see [\[con:GlobalqDeRham\]](#con:GlobalqDeRham){reference-type="ref" reference="con:GlobalqDeRham"}), it's enough to check this after completion at any prime $p$. In general, $(\qOmega_{S/A})_p^\complete\rightarrow (\Omega_{S/A})_p^\complete$ factors through $(\qOmega_{S/A})_p^\complete\rightarrow (\Omega_{S/A})_p^\complete\qpower/(q-1)^{p-1}$ by [\[lem:RationalisationTechnicalII\]](#lem:RationalisationTechnicalII){reference-type="ref" reference="lem:RationalisationTechnicalII"}. For primes $p>n$, this does what we want. For $p\leqslant n$, our assumption on $S$ ensures that $(\qOmega_{S/A})_p^\complete$ vanishes, so this case is fine too.

Let us now equip $\Omega_{S/A}\qpower/(q-1)^n$ with the following filtration: We first define $\fil_{(\Hodge,q-1)}^{\star} \Omega_{S/A}\qpower\coloneqq (\fil_{\Hodge}^\star \Omega_{S/A}\lotimes_\IZ(q-1)^\star\IZ\qpower)_{(q-1)}^\complete$ to be the combined Hodge and $(q-1)$-adic filtration, as usual. We then let $\fil_{(\Hodge,q-1)}^{\star} \Omega_{S/A}\qpower/(q-1)^n$ denotes its reduction modulo $(q-1)^n$, which we regard as an element in filtration degree $n$.

[^1]

We may then form the following pullback of filtered objects in degrees $\leqslant n$: $$\begin{tikzcd}
                \fil_{\qHodge,n}^{\star \leqslant n}\qOmega_{S/A}\rar\dar\drar[pullback] & \qOmega_{S/A}\dar\\
                \fil_{(\Hodge,q-1)}^{\star\leqslant n} \Omega_{S/A}\qpower/(q-1)^n\rar & \Omega_{S/A}\qpower/(q-1)^n
            \end{tikzcd}$$ Here $\fil_{(\Hodge,q-1)}^{\star\leqslant n} \Omega_{S/A}\qpower/(q-1)^n$ denotes the restriction of the to degrees $\star\leqslant n$; more precisely, we apply the truncation functor $\tau_n^*$ from [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"} below.

We then wish to extend $\fil_{\qHodge,n}^{\star \leqslant n}\qOmega_{S/A}$ to degrees $\star\geqslant n+1$. Intuitively, this should be done via the $(q-1)$-adic filtration $(q-1)^{\star -n}\fil_{\qHodge,n}^n\qOmega_{S/A}$ as in [\[par:qHodgeForCurves\]](#par:qHodgeForCurves){reference-type="ref" reference="par:qHodgeForCurves"}. To do this formally and make the resulting filtered $(q-1)^\star A\qpower$-module structure apparent, we need to show a technical lemma.
:::

::: lem
[]{#lem:TruncatedFilteredObjects label="lem:TruncatedFilteredObjects"} Let $\Fil^{\geqslant 0}\Dd(\IZ)$ denote the full sub-$\infty$-categories of filtered objects that are constant in filtration degrees $\star\leqslant 0$. Let $\Fil^{[0,n]}\Dd(\IZ)\subseteq \Fil^{\geqslant 0}\Dd(\IZ)$ denote the full sub-$\infty$-category of filtered objects that also vanish in filtration degree $\star\geqslant n+1$.

::: alphanumerate
The inclusion $\Fil^{[0,n]}\Dd(\IZ)\rightarrow\Fil^{\geqslant 0}\Dd(\IZ)$ has a left adjoint $\tau_n^*$, which on objects is given by replacing all filtration degrees $\star\geqslant n+1$ by $0$. Moreover, if $\fil^\star M$ and $\fil^\star N$ are filtered $\IZ$-modules, the canonical map[]{#enum:TruncationSymmetricMonoidal label="enum:TruncationSymmetricMonoidal"} $$\tau_n^*\left(\fil^\star M\lotimes_{\IZ}\tau_n^*(\fil^\star N)\right)\overset{\simeq}{\longrightarrow}\tau_n^*\left(\fil^\star M\lotimes_{\IZ}\fil^\star N\right)$$ is an equivalence. Consequently there's a canonical way to equip $\Fil^{[0,n]}\Dd(\IZ)$ and the functor $\tau_n^*\colon \Fil^{\geqslant 0}\Dd(\IZ)\rightarrow \Fil^{[0,n]}\Dd(\IZ)$ with symmetric monoidal structures.

For any filtered $\IE_\infty$-algebra $T\in\CAlg(\Fil^{\geqslant 0}\Dd(\IZ))$, the induced symmetric monoidal functor $$\tau_n^*\colon \Mod_{T}\bigl(\Fil^{\geqslant 0}\Dd(\IZ)\bigr)\longrightarrow \Mod_{\tau_n^*T}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)$$ admits an oplax symmetric monoidal left adjoint[]{#enum:TruncationLeftAdjoint label="enum:TruncationLeftAdjoint"} $$\tau_{n,!}^T\colon  \Mod_{\tau_n^*T}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)\longrightarrow\Mod_{T}\bigl(\Fil^{\geqslant 0}\Dd(\IZ)\bigr)$$ .

Let $T_1\rightarrow T_2$ be any map in $\CAlg(\Fil^{\geqslant 0}\Dd(\IZ))$ and let $\fil^\star M\in \Mod_{\tau_n^*T}(\Fil^{[0,n]}\Dd(\IZ))$. Then there's a natural equivalence[]{#enum:TruncationProjectionFormula label="enum:TruncationProjectionFormula"} $$\tau_{n,!}^{T_2}\left(\fil^\star M\otimes_{\tau_n^*T_1}\tau_n^*T_2\right)\overset{\simeq}{\longrightarrow}\tau_{n,!}^{T_1}(\fil^\star M)\otimes_{T_1} T_2\,.$$
:::
:::

::: proof
*Proof.* We start with [\[enum:TruncationSymmetricMonoidal\]](#enum:TruncationSymmetricMonoidal){reference-type="ref" reference="enum:TruncationSymmetricMonoidal"}. It's straightforward to see that $\tau_n^*$ exists and is given as claimed. To show the equivalence, since $\tau_n^*$ and the inclusion preserve colimits, it will be enough to check the case where $\fil^\star M\simeq \IZ(i)$ and $\fil^\star N\simeq \IZ(j)$, where $i,j\geqslant 0$. If $j\leqslant n$, then $\tau_n^*\IZ(j)\rightarrow \IZ(j)$ is an equivalence and the claim is clear. If $j\geqslant n+1$, then we must check that $\tau_n^*\IZ(i+j)\rightarrow \tau_n^*\IZ(i+n)$ is an equivalence. This is clear as both sides are just $\IZ(n)$. The final claim in [\[enum:TruncationSymmetricMonoidal\]](#enum:TruncationSymmetricMonoidal){reference-type="ref" reference="enum:TruncationSymmetricMonoidal"} is general abstract nonsense about symmetric monoidal structures on localisations (see [@HA Proposition ] for example).

Let us now prove [\[enum:TruncationLeftAdjoint\]](#enum:TruncationLeftAdjoint){reference-type="ref" reference="enum:TruncationLeftAdjoint"} and [\[enum:TruncationProjectionFormula\]](#enum:TruncationProjectionFormula){reference-type="ref" reference="enum:TruncationProjectionFormula"} simultaneously. For any map $T_1\rightarrow T_2$ in $\CAlg(\Fil^{\geqslant 0}\Dd(\IZ_p))$, the diagram $$\begin{tikzcd}
                \Mod_{T_2}\bigl(\Fil^{\geqslant 0}\Dd(\IZ)\bigr)\rar["\tau_n^*"]\dar & \Mod_{\tau_n^*T_2}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)\dar\\
                \Mod_{T_1}\bigl(\Fil^{\geqslant 0}\Dd(\IZ)\bigr)\rar["\tau_n^*"] & \Mod_{\tau_n^*T_1}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)
            \end{tikzcd}$$ commutes. In the special case where $T_1=\IZ$ is the filtered tensor unit and $T_2=T$, this allows us to show that $\tau_n^*\colon \Mod_T(\Fil^{\geqslant 0}\Dd(\IZ))\rightarrow \Mod_{\tau^*T}(\Fil^{[0,n]}\Dd(\IZ))$ preserves all limits and colimits. Therefore the claimed left adjoint $\tau_{n,!}^T$ exists by Lurie's adjoint functor theorem. By abstract nonsense, $\tau_{n,!}^T$ will automatically acquire an oplax symmetric monoidal structure. This shows [\[enum:TruncationLeftAdjoint\]](#enum:TruncationLeftAdjoint){reference-type="ref" reference="enum:TruncationLeftAdjoint"}. By passing to left adjoints in the diagram above, we immediately obtain [\[enum:TruncationProjectionFormula\]](#enum:TruncationProjectionFormula){reference-type="ref" reference="enum:TruncationProjectionFormula"}. ◻
:::

::: numpar
[]{#par:CanonicalqHodgeSmoothII label="par:CanonicalqHodgeSmoothII"} We resume the discussion from [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"}. As we know now, the pullback defining $\fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}$ can be taken in $\Mod_{\tau_n^*((q-1)^\star A\qpower)}(\Fil^{[0,n]}\Dd(\IZ))$. Applying the functor $\tau_{n,!}$ from [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"}[\[enum:TruncationLeftAdjoint\]](#enum:TruncationLeftAdjoint){reference-type="ref" reference="enum:TruncationLeftAdjoint"}, we obtain a filtered $(q-1)^\star A\qpower$-module $$\fil_{\qHodge,n}^\star\qOmega_{S/A}\coloneqq \tau_{n,!}\left(\fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}\right)_{(q-1)}^\complete\,.$$ We can also take the pullback along $\qdeRham_{S/A}\rightarrow \qOmega_{S/A}$ to construct $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$ (in order to be in line with [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}).
:::

::: rem
If $S$ satisfies the assumptions of [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} and is additionally equipped with an étale framing $\square\colon A[x_1,\dotsc,x_n]\rightarrow S$, then there exists an equivalence of filtered $(q-1)^\star A\qpower$-modules $$\fil_{\qHodge,n}^\star\qOmega_{S/A}\overset{\simeq}{\longrightarrow}\fil_{\qHodge,\square}^\star\qOmega_{S/A, \square}^*$$ between the $q$-Hodge filtration from [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} and the one from [\[exm:HabiroDescentCoordinateCase\]](#exm:HabiroDescentCoordinateCase){reference-type="ref" reference="exm:HabiroDescentCoordinateCase"}. Indeed, we observe $\fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}\simeq \tau_n^*(\fil_{\qHodge,\square}^\star\qOmega_{S/A, \square}^*)$, since both sides fit into the same pullback diagram by construction. Since $\tau_{n,!}$ was defined as a the left adjoint of $\tau_n^*$, we obtain the map above. To see that it is an equivalence, we may reduce modulo $(q-1)$, where we get the identity on $\fil_{\Hodge}^\star\Omega_{S/A}$ by inspection and [\[lem:CanonicalqHodgeSmooth\]](#lem:CanonicalqHodgeSmooth){reference-type="ref" reference="lem:CanonicalqHodgeSmooth"} below.
:::

::: rem
[]{#rem:pTildeDeRham label="rem:pTildeDeRham"} Here's another way to do the construction from [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"} and [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"}. Fix a prime $p$. Recall that Bhatt--Lurie [@BhattLurieI Construction ] have defined a *$\widetilde{p}$-de Rham complex* $\mathop{\widetilde{p}}\!\hspace{-0.1ex}\mhyph\hspace{-0.1ex}\Omega_{\smash{\widehat{S}}_p/\smash{\widehat{A}}_p}$. Explicitly, it is the homotopy-fixed points of the action of $\mu_{p-1}\subseteq \IZ_p^\times$ on $(\qOmega_{S/A})_p^\complete$. Here $u\in\IZ_p^\times$ acts on the prism $(\IZ_p\qpower,[p]_q)$ via $q\mapsto q^u$, which induces an action of $\IZ_p^\times$ on $(\qOmega_{S/A})_p^\complete$ via the comparison with prismatic cohomology ([\[thm:qDeRhamGlobal\]](#thm:qDeRhamGlobal){reference-type="ref" reference="thm:qDeRhamGlobal"}[\[enum:GlobalqDeRhamPrismatic\]](#enum:GlobalqDeRhamPrismatic){reference-type="ref" reference="enum:GlobalqDeRhamPrismatic"}).

We can then define $\fil_{\mathop{\widetilde{p}}\!\hspace{-0.1ex}\mhyph\hspace{-0.1ex}\Hodge,n}^{\star\leqslant n}\mathop{\widetilde{p}}\!\hspace{-0.1ex}\mhyph\hspace{-0.1ex}\Omega_{\smash{\widehat{S}}_p/\smash{\widehat{A}}_p}$ as the pullback of the Hodge filtration along the canonical map $\mathop{\widetilde{p}}\!\hspace{-0.1ex}\mhyph\hspace{-0.1ex}\Omega_{\smash{\widehat{S}}_p/\smash{\widehat{A}}_p}\rightarrow (\Omega_{S/A})_p^\complete$ (no combined Hodge and $(q-1)$-adic filtration is needed here), extend via $\tau_{n,!}$, and then finally base change to $(q-1)^\star\IZ_p\qpower$ to define a $p$-completed $q$-Hodge filtration $\fil_{\qHodge,n}^\star(\qOmega_{S/A})_p^\complete$.

These filtrations for all $p$ can be glued with the combined Hodge and $(q-1)$-adic filtration on $(\Omega_{S/A}\lotimes_\IZ\IQ)\qpower$ to get the same filtration $\fil_{\qHodge,n}^\star\qOmega_{S/A}$ as in [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"}. We prefer the construction in [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"}, since spelling out the gluing argument is a bit of a pain.
:::

::: lem
[]{#lem:CanonicalqHodgeSmooth label="lem:CanonicalqHodgeSmooth"} With notation as in [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"}, assume additionally that $\dim(S/A)\leqslant n$. Then $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$ can naturally be equipped with the structure of a $q$-Hodge filtration as in [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"}.
:::

::: proof
*Proof.* In the following, we'll regard $(q-1)$ as sitting in filtration degree $1$, as per Convention [\[conv:QuotientConvention\]](#conv:QuotientConvention){reference-type="ref" reference="conv:QuotientConvention"}. We first compute $$\begin{aligned}
            \fil_{\qHodge,n}^\star\qOmega_{S/A}/(q-1)&\simeq \tau_{n,!}^{\IZ}\left(\fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}\lotimes_{\tau_n^*((q-1)^\star\IZ\qpower)}\IZ\right)\\
            &\simeq \tau_{n,!}^\IZ\tau_n^*(\fil_{\Hodge}^{\star}\Omega_{S/A})\\
            &\simeq \fil_{\Hodge}^{\star}\Omega_{S/A}\,.
        
\end{aligned}$$ In the first equivalence we apply [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"}[\[enum:TruncationProjectionFormula\]](#enum:TruncationProjectionFormula){reference-type="ref" reference="enum:TruncationProjectionFormula"} to $(q-1)^\star\IZ\qpower\rightarrow \IZ$. The second equivalence follows by construction. To see the third equivalence, first observe that the Hodge filtration $\fil_{\Hodge}^\star\Omega_{S/A}$ is already contained in $\Fil^{[0,n]}\Dd(\IZ)$ because we assume $\dim(S/A)\leqslant n$. Since the right adjoint of $\tau_n^*\colon \Fil^{\geqslant 0}\Dd(\IZ)\rightarrow \Fil^{[0,n]}\Dd(\IZ)$ is fully faithful, so is the left adjoint $\tau_{n,!}^\IZ$, which yields the third equivalence. Similarly, $$\begin{aligned}
            \bigl(\fil_{\qHodge,n}^\star\qOmega_{S/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete&\simeq \tau_{n,!}\left(\bigl(\fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}\lotimes_\IZ\IQ\bigr)_{(q-1)}^\complete\right)\\
            &\simeq \tau_{n,!}\left(\bigl(\fil_{\Hodge}^\star\Omega_{S/A}\lotimes_\IZ\tau_n^*\bigl((q-1)^\star\IQ\qpower\bigr)\bigr)_{(q-1)}^\complete\right)\\ &\simeq \fil_{(\Hodge,q-1)}^\star\bigl(\Omega_{S/A}\lotimes_\IZ\IQ\bigr)\qpower\,.
        
\end{aligned}$$ The first equivalence is [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"}[\[enum:TruncationProjectionFormula\]](#enum:TruncationProjectionFormula){reference-type="ref" reference="enum:TruncationProjectionFormula"} applied to $\IZ\rightarrow \IQ$. For the second equivalence, we apply $(-\lotimes_\IZ\IQ)_{(q-1)}^\complete$ to the pullback defining $\fil_{\qHodge,n}^\star\qOmega_{S/A}$ in [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} and use the fact that $(\qOmega_{S/A}\lotimes_\IZ\IQ)_{(q-1)}^\complete\simeq (\Omega_{S/A}\lotimes_\IZ\IQ)\qpower$. The third equivalence is [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"}[\[enum:TruncationProjectionFormula\]](#enum:TruncationProjectionFormula){reference-type="ref" reference="enum:TruncationProjectionFormula"} applied to $\IZ\rightarrow (q-1)^\star\IQ\qpower$.

In a completely analogus way, we obtain natural equivalences $$\fil_{\qHodge,n}^\star\bigl(\qOmega_{S/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q-1)}^\complete\overset{\simeq}{\longrightarrow}\fil_{(\Hodge,q-1)}^\star\bigl(\Omega_{S/A}\bigr)_p^\complete\bigl[\localise{p}\bigr]\qpower$$ for all primes $p$. Via pullback along $\qdeRham_{S/A}\rightarrow\qOmega_{S/A}$, we obtain analogous equivalences for $\fil_{\qHodge,n}^\star \qdeRham_{S/A}$. The required compatibilities from [\[def:qHodgeFiltration\]](#def:qHodgeFiltration){reference-type="ref" reference="def:qHodgeFiltration"} can all be induced from those for $\qdeRham_{S/A}$, and so $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$ can indeed be equipped with the structure of a $q$-Hodge filtration. ◻
:::

::: lem
With assumptions as in [\[lem:CanonicalqHodgeSmooth\]](#lem:CanonicalqHodgeSmooth){reference-type="ref" reference="lem:CanonicalqHodgeSmooth"}, $\fil_{\qHodge,n}^\star\qOmega_{S/A}$ is automatically the completion of $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$.
:::

::: proof
*Proof.* By [\[prop:Letaq-1\]](#prop:Letaq-1){reference-type="ref" reference="prop:Letaq-1"}, $\qOmega_{S/A}$ is automatically the completion of $\qdeRham_{S/A}$ at the filtration $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$. Since $\fil_{\qHodge,n}^\star\qdeRham_{S/A}$ is defined as the pullback of $\fil_{\qHodge,n}^\star\qOmega_{S/A}$ along $\qdeRham_{S/A}\rightarrow \qOmega_{S/A}$, the desired assertion follows. ◻
:::

We will now make the construction from [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} functorial.

::: numpar
For all non-negative integers $n$ and $d$ let $\cat{Sm}_{A[n!^{-1}]}^{\leqslant d}$ be the category of all smooth $A$-algebras $S$ of relative dimension $\dim(S/A)\leqslant d$ such that all primes $p\leqslant n$ are invertible in $S$. Then [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} and [\[lem:CanonicalqHodgeSmooth\]](#lem:CanonicalqHodgeSmooth){reference-type="ref" reference="lem:CanonicalqHodgeSmooth"} provide us with a functor $$\bigl(-,\fil_{\qHodge,n}^\star\qdeRham_{-/A}\bigr)\colon \cat{Sm}_{A[n!^{-1}]}^{\leqslant n}\longrightarrow \cat{AniAlg}_A^{\qHodge}\,.$$ We let $\cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}\subseteq \cat{Sm}_A$ be the full subcategory spanned by $\bigcup_{d\leqslant n}\cat{Sm}_{A[d!^{-1}]}^{\leqslant d}$ and we put $$\cat{Sm}_{A[\dim!^{-1}]}\coloneqq \bigcup_{n\geqslant 0} \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}\,.$$ Our goal is to show that the functors above for varying $n$ combine into a single functor defined on all of $\cat{Sm}_{A[\dim!^{-1}]}$. This will be achieved by the technical [\[lem:SmoothPushout,lem:CanonicalqHodgeSmoothFunctorial\]](#lem:SmoothPushout,lem:CanonicalqHodgeSmoothFunctorial){reference-type="ref" reference="lem:SmoothPushout,lem:CanonicalqHodgeSmoothFunctorial"} below.
:::

::: lem
[]{#lem:SmoothPushout label="lem:SmoothPushout"} For all $n\geqslant 0$, the following diagram is a pushout of $\infty$-categories: $$\begin{tikzcd}
                \cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n}\rar\dar\drar[pushout] & \cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n+1}\dar\\
                \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}\rar & \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n+1}
            \end{tikzcd}$$
:::

::: proof
*Proof.* Let $\Pp$ denote the pushout. Since the diagram above commutes, we get a functor $\Pp\rightarrow \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n+1}$. This functor is clearly essentially surjective. To show that it is fully faithful, we must show that $$\Hom_\Pp(S_1,S_2)\overset{\simeq}{\longrightarrow} \Hom_{\cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n+1}}(S_1,S_2)$$ is an equivalence for all $S_1,S_2\in \Pp$. We may assume without loss of generality that $S_1$ and $S_2$ are the images of objects in $\cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}$ or $\cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n+1}$.

By an observation of Maxime Ramzi [@RamziPushouts], fully faithful functors are preserved under pushouts. Since both legs of our pushout are fully faithful, the claimed equivalence is clear if $S_1$ and $S_2$ come from the same cofactor. It remains to deal with the following two cases.

*Case 1: $S_1\in \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}$ and $S_2\in \cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n+1}$.* Observe that the fully faithful functor $$\cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n}\longrightarrow \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}$$ has a left adjoint given by localisation at $(n+1)!$. It follows formally that $\cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n+1}\rightarrow\Pp$ also has a left adjoint and that the diagram of left adjoints is still a pushout (and in particular commutative). Indeed, we can simply define unit and counit by taking the pushout of the original unit and counit; the triangle identities will automatically be satisfied. Therefore, we can replace $S_1$ by $S_1[(n+1)!^{-1}]$ and thus reduce to the case where $S_1$ and $S_2$ come from the same cofactor.

*Case 2: $S_1\in \cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n+1}$ and $S_2\in \cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n}$.* We may additionally assume that $(n+1)!$ is not invertible in $S_2$; otherwise we would be in a case already covered. But then $$\Hom_{\cat{Sm}_{A[\dim!^{-1}]}^{\leqslant n+1}}(S_1,S_2)\simeq\emptyset$$ and so the map in question must be an equivalence, since only $\emptyset$ maps to $\emptyset$. ◻
:::

::: lem
[]{#lem:CanonicalqHodgeSmoothFunctorial label="lem:CanonicalqHodgeSmoothFunctorial"} For all $n\geqslant 0$, in the $\infty$-category of functors $\cat{Sm}_{A[(n+1)!^{-1}]}^{\leqslant n}\rightarrow \cat{AniAlg}_A^{\qHodge}$, there exists a natural equivalence $$\bigl(-,\fil_{\qHodge,n}^\star\qdeRham_{-/A}\bigr)\simeq \bigl(-,\fil_{\qHodge,n+1}^\star\qdeRham_{-/A}\bigr)\,.$$
:::

::: proof
*Proof.* First observe that every morphism in $\Fil^{\geqslant 0}\Dd(\IZ)$ that is sent to an equivalence by $\tau_{n+1}^*\colon \Fil^{\geqslant 0}\Dd(\IZ)\rightarrow \Fil^{[0,n]}\Dd(\IZ)$ is also sent to an equivalence by $\tau_n^*$. Since $\tau_{n+1}^*$ is a symmetric monoidal localisation, there exists a unique (up to contractible choice) symmetric monoidal functor $\tau_{n,n+1}^*$ such that $$\begin{tikzcd}
                \Fil^{\geqslant 0}\Dd(\IZ)\dar["\tau_{n+1}^*"']\rar["\tau_n^*"] & \Fil^{[0,n]}\Dd(\IZ)\\
                \Fil^{[0,n+1]}\Dd(\IZ)\urar[dashed,"\tau_{n,n+1}^*"'] &
            \end{tikzcd}$$ commutes. Moreover, arguing as in [\[lem:TruncatedFilteredObjects\]](#lem:TruncatedFilteredObjects){reference-type="ref" reference="lem:TruncatedFilteredObjects"}[\[enum:TruncationLeftAdjoint\]](#enum:TruncationLeftAdjoint){reference-type="ref" reference="enum:TruncationLeftAdjoint"}, we see that for any filtered $\IE_\infty$-algebra $T\in\CAlg(\Fil^{\geqslant 0}\Dd(\IZ))$, the induced symmetric monoidal functor $$\tau_{n,n+1}^*\colon \Mod_{\tau_{n+1}^*T}\bigl(\Fil^{[0,n+1]}\Dd(\IZ)\bigr)\longrightarrow \Mod_{\tau_n^*T}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)$$ admits an oplax symmetric monoidal left adjoint $$\tau_{n,n+1,!}\colon  \Mod_{\tau_n^*T}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)\longrightarrow\Mod_{\tau_{n+1}^*T}\bigl(\Fil^{[0,n+1]}\Dd(\IZ)\bigr)\,.$$ Let us now apply this in the case where $T=(q-1)^\star A\qpower$. Let $S$ be a smooth $A$-algebra such that $\dim(S/A)\leqslant n$ and all primes $p\leqslant n+1$ are invertible in $S$. Plugging the canonical projection $\fil_{(\Hodge,q-1)}^\star(\Omega_{S/A}\qpower/(q-1)^{n+1})\rightarrow \fil_{(\Hodge,q-1)}^\star(\Omega_{S/A}\qpower/(q-1)^{n})$ into the pullback from [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"}, we obtain a morphism $$\tau_{n,n+1}^*\fil_{\qHodge,n+1}^{\star\leqslant n+1}\qOmega_{S/A}\longrightarrow \fil_{\qHodge,n}^{\star\leqslant n}\qOmega_{S/A}\,.$$ Applying $\tau_{n,!}(-)_{(q-1)}^\complete$ on both sides and using the counit $\tau_{n,n+1,!}\circ\tau_{n,n+1}^*\Rightarrow \id$, we obtain a canonical zigzag $$\fil_{\qHodge,n+1}^\star\qOmega_{S/A}\overset{\simeq}{\longleftarrow} \tau_{n,!}\left(\tau_{n,n+1}^*\fil_{\qHodge,n+1}^{\star\leqslant n+1}\qOmega_{S/A}\right)_{(q-1)}^\complete\overset{\simeq}{\longrightarrow} \fil_{\qHodge,n}^\star\qOmega_{S/A}$$ It is now straightforward to check that both morphisms are equivalences. Indeed, everything is filtered $(q-1)$-complete, so we may check this after reduction modulo $(q-1)$. For the outer two terms, the reduction is $\fil_{\Hodge}^\star\Omega_{S/A}$ by the calculation in the proof of [\[lem:CanonicalqHodgeSmooth\]](#lem:CanonicalqHodgeSmooth){reference-type="ref" reference="lem:CanonicalqHodgeSmooth"}. An analogous calculation shows that the inner term also becomes $\fil_{\Hodge}^\star\Omega_{S/A}$ and that the morphisms become the identity.

The zigzag above provides a functorial equivalence $\fil_{\qHodge,n+1}^\star\qOmega_{-/A}\simeq \fil_{\qHodge,n}^\star\qOmega_{-/A}$. Taking the pullback along $\qdeRham_{S/A}\rightarrow \qOmega_{S/A}$, we get what we want. ◻
:::

In total we've shown:

::: thm
[]{#thm:CanonicalqHodgeSmooth label="thm:CanonicalqHodgeSmooth"} Let $A$ be a perfectly covered $\Lambda$-ring and let $S$ be a smooth $A$-algebra such that all primes $p\leqslant \dim(S/A)$ are invertible in $S$. Then $\qdeRham_{S/A}$ admits a canonical $q$-Hodge filtration. More precisely, there exists a functor $$\bigl(-,\fil_{\qHodge}^\star\qdeRham_{-/A}\bigr)\colon \cat{Sm}_{A[\dim!^{-1}]}\longrightarrow \cat{AniAlg}_A^{\qHodge}$$ which is a partial section of the forgetful functor $\cat{AniAlg}_A^{\qHodge}\rightarrow \cat{AniAlg}_A$.
:::

::: proof
*Proof.* This is the quintessence of [\[par:CanonicalqHodgeSmoothI\]](#par:CanonicalqHodgeSmoothI){reference-type="ref" reference="par:CanonicalqHodgeSmoothI"}--. ◻
:::

::: numpar
[]{#par:CanonicalqHodgeSmoothMonoidal label="par:CanonicalqHodgeSmoothMonoidal"} We wish to study to what extent the $q$-Hodge filtrations from [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} can be equipped with multiplicative structures. To this end, it would be nice to equip the functor from [\[thm:CanonicalqHodgeSmooth\]](#thm:CanonicalqHodgeSmooth){reference-type="ref" reference="thm:CanonicalqHodgeSmooth"} with a symmetric monoidal structure. This is made complicated by the following issue:

::: alphanumerate

$\cat{Sm}_{A[\dim!^{-1}]}$ is not closed under tensor products in $\cat{Sm}_A$ and we don't see a way of equipping it with a symmetric monoidal structure.
:::

To address this problem, let $\cat{Sm}_A^{\otimes}\rightarrow \cat{Fin}_*$ be the $\infty$-operad associated with the symmetric monoidal structure on $\cat{Sm}_A$. We define a sub-$\infty$-operad $\cat{Sm}_{A[\dim!^{-1}]}^{\otimes}\subseteq \cat{Sm}_A^{\otimes}$ as follows:

::: alphanumerate
An object $(S_1,\dotsc,S_i)\in\cat{Sm}_A^i$ in the fibre over $\langle i\rangle \in\cat{Fin}_*$ is contained in $\cat{Sm}_{A[\dim!^{-1}]}$ if and only $S_1,\dotsc,S_i$ are all contained in $\cat{Sm}_{A[\dim!^{-1}]}$.[]{#enum:SmOperadA label="enum:SmOperadA"}

A morphism $(S_1,\dotsc,S_i)\rightarrow (S_1',\dotsc,S_{i'}')$ over $\alpha\colon \langle i\rangle \rightarrow \langle i'\rangle$ is contained in $\cat{Sm}_{A[\dim!^{-1}]}$ if and only if both source and target satisfy the condition from [\[enum:SmOperadA\]](#enum:SmOperadA){reference-type="ref" reference="enum:SmOperadA"} and the target of a cocartesian lift of $\alpha$ with source $(S_1,\dotsc,S_i)$ also satisfies the condition from [\[enum:SmOperadA\]](#enum:SmOperadA){reference-type="ref" reference="enum:SmOperadA"}. Equivalently, we only retain those morphisms that factor through a cocartesian lift of their image in $\cat{Fin}_*$.[]{#enum:SmOperadB label="enum:SmOperadB"}
:::

Let us immediately warn the reader that $\cat{Sm}_{A[\dim!^{-1}]}^\otimes$ is *not* the full sub-$\infty$-operad of $\cat{Sm}_A^{\otimes}$ spanned by the full subcategory $\cat{Sm}_{A[\dim!^{-1}]}\subseteq \cat{Sm}_A$, precisely because the condition from [\[enum:SmOperadB\]](#enum:SmOperadB){reference-type="ref" reference="enum:SmOperadB"} yields a *non-full* sub-$\infty$-operad.

Below we'll sketch how to make the functor from [\[thm:CanonicalqHodgeSmooth\]](#thm:CanonicalqHodgeSmooth){reference-type="ref" reference="thm:CanonicalqHodgeSmooth"} into a functor of $\infty$-operads (this wouldn't work if we had used the full sub-$\infty$-operad spanned by $\cat{Sm}_{A[\dim!^{-1}]}$). Let us discuss what kind of multiplicative structures this induces on $\fil_{\qHodge}^\star\qdeRham_{S/A}$. In general, any multiplicative structure on $S$ as an object in $\cat{Sm}_{A[\dim!^{-1}]}$ will induce the same kind of multiplicative structure on $\fil_{\qHodge}^\star\qdeRham_{S/A}$. For arbitrary $S\in \cat{Sm}_{A[\dim!^{-1}]}$ there's nothing we can say. But as soon as all primes $p\leqslant 2\dim(S/A)$ are invertible in $S$, the multiplication map $S\otimes_A S\rightarrow S$ is a morphism in $\cat{Sm}_{A[\dim!^{-1}]}$, and so $S$ will have an $\IA_2$-structure in $\cat{Sm}_{A[\dim!^{-1}]}^\otimes$; that is, a homotopy-unital multiplication. If for some $r\geqslant 3$ all primes $p\leqslant r\dim(S/A)$ are invertible in $S$, then the multiplication will be $\IA_r$; that is, coherently associative for up to $r$ factors. A similar analysis works for commutativity.
:::

We'll now sketch how to make the functor from [\[thm:CanonicalqHodgeSmooth\]](#thm:CanonicalqHodgeSmooth){reference-type="ref" reference="thm:CanonicalqHodgeSmooth"} into a functor of $\infty$-operads. Let us temporarily fix $n\geqslant 0$.

::: lem
[]{#lem:Truncatedq-1Completion label="lem:Truncatedq-1Completion"} Let $\Mod_{\tau_n^*((q-1)^\star A\qpower)}(\Fil^{[0,n]}\Dd(\IZ))$ be as in [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} and equip the full sub-$\infty$-category of $(q-1)$-complete objects $\Mod_{\tau_n^*((q-1)^\star A\qpower)}(\Fil^{[0,n]}\Dd(\IZ))_{(q-1)}^\complete$ with the $(q-1)$-completed tensor product. Then the functor $$\fil_{\qHodge,n}^\star\qdeRham_{-/A}\colon \cat{Sm}_{A[n!^{-1}]}\longrightarrow \Mod_{\tau_n^*((q-1)^\star A\qpower)}\bigl(\Fil^{[0,n]}\Dd(\IZ)\bigr)_{(q-1)}^\complete$$ from [\[par:CanonicalqHodgeSmoothII\]](#par:CanonicalqHodgeSmoothII){reference-type="ref" reference="par:CanonicalqHodgeSmoothII"} can be equipped with a symmetric monoidal structure.
:::

::: proof
*Proof sketch.* From the construction it's straightforward to get a lax symmetric monoidal structure. Whether it is symmetric monoidal can be checked modulo $(q-1)$, where we reduce to the fact that $\tau_n^*(\fil_{\Hodge}^\star\deRham_{-/A})$ is symmetric monoidal. ◻
:::

::: numpar
For every symmetric monoidal $\infty$-category with associated cocartesian fibration $\Cc^\otimes\rightarrow \cat{Fin}_*$, let $(\Cc^\otimes)^\vee\rightarrow\cat{Fin}_*^\op$ denote the dual cartesian fibration. Lax symmetric monoidal functors $\Cc\rightarrow \Dd$ are then encoded as functors $\Cc^\otimes\rightarrow \Dd^\otimes$ in $\Cat_{\infty/\cat{Fin}_*}$ that preserve cocartesian lifts of inert morphisms, whereas oplax symmetric monoidal functors are encoded as functors $(\Cc^\otimes)^\vee\rightarrow (\Dd^\otimes)^\vee$ in $\Cat_{\infty/\cat{Fin}_*^\op}$ that preserve cartesian lifts of inert morphisms.

In general, the dual cartesian fibration $(\Cc^\otimes)^\vee\rightarrow \cat{Fin}_*$ has a very nice description in terms of span $\infty$-categories. This is due to Barwick--Glasman--Nardin; see [@DualFibration]. We will now apply this to the oplax symmetric monoidal structure on $$\bigl(-,\fil_{\qHodge,n}^\star\qdeRham_{-/A}\bigr)\colon \cat{Sm}_{A[n!^{-1}]}\longrightarrow \cat{AniAlg}_A^{\qHodge}$$ that we obtain by composing the symmetric monoidal functor from [\[lem:Truncatedq-1Completion\]](#lem:Truncatedq-1Completion){reference-type="ref" reference="lem:Truncatedq-1Completion"} with the oplax symmetric monoidal functor $\tau_{n,!}(-)_{(q-1)}^\complete$.
:::

::: lem
[]{#lem:CartesianLiftsPreserved label="lem:CartesianLiftsPreserved"} If $\varphi\colon (S_1',\dotsc,S_{i'}')\rightarrow (S_1,\dotsc,S_i)$ is a cartesian morphism in $(\cat{Sm}_{A[n!^{-1}]}^{\otimes})^\vee$ such that $S_1',\dotsc,S_{i'}'$ are all of relative dimension $\leqslant n$ over $A$, then $\varphi$ is sent to a cartesian morphism under $$\bigl(\cat{Sm}_{A[n!^{-1}]}^{\otimes}\bigr)^\vee\longrightarrow \bigl(\cat{AniAlg}_A^{\qHodge,\otimes}\bigr)^\vee\,.$$
:::

::: proof
*Proof sketch.* This essentially reduces to the observation that whenever a tensor product of smooth $A[n!^{-1}]$-algebras $S_1\otimes_A\dotsb\otimes_A S_i$ has relative dimension $\leqslant n$ over $A$, the $q$-Hodge filtration $\fil_{\qHodge,n}^\star \qdeRham_{S_1\otimes_A\dotsb \otimes_AS_i/A}$ will agree with $$\left(\fil_{\qHodge,n}^\star \qdeRham_{S_1/A}\lotimes_{(q-1)^\star A\qpower}\dotsb \lotimes_{(q-1)^\star A\qpower}\fil_{\qHodge,n}^\star \qdeRham_{S_i/A}\right)_{(q-1)}^\complete\,.$$ Indeed, this can be checked modulo $(q-1)$, where the desired claim follows using symmetric monoidality of $\fil_{\Hodge}^\star\deRham_{-/A}$. ◻
:::

::: cor
[]{#cor:CanonicalqHodgeSmoothMonoidal label="cor:CanonicalqHodgeSmoothMonoidal"} The functor from [\[thm:CanonicalqHodgeSmooth\]](#thm:CanonicalqHodgeSmooth){reference-type="ref" reference="thm:CanonicalqHodgeSmooth"} underlies a functor of $\infty$-operads $$\cat{Sm}_{A[\dim!^{-1}]}^{\otimes}\longrightarrow \cat{AniAlg}_A^{\qHodge,\otimes}\,,$$ which preserves all cocartesian lifts that exist in the source.
:::

::: proof
*Proof sketch.* As in [\[par:CanonicalqHodgeSmoothMonoidal\]](#par:CanonicalqHodgeSmoothMonoidal){reference-type="ref" reference="par:CanonicalqHodgeSmoothMonoidal"}, we can define a sub-$\infty$-operad $\cat{Sm}_{A[n!^{-1}]}^{\leqslant n,\otimes}\subseteq \cat{Sm}_{A[n!^{-1}]}^\otimes$ given by those objects whose entries are of dimension $\leqslant n$ and those morphisms that factor through a cocartesian lift of their image in $\cat{Fin}_*$. Analogously, we can define $(\cat{Sm}_{A[n!^{-1}]}^{\leqslant n,\otimes})^\vee\subseteq (\cat{Sm}_{A[n!^{-1}]}^\otimes)^\vee$ given by those objects whose entries are of dimension $\leqslant n$ and those morphisms that factor through a cartesian lift of their image in $\cat{Fin}_*^\op$.

The dualising construction from [@DualFibration] can not only be applied to cartesian fibrations, but also to $(\cat{Sm}_{A[n!^{-1}]}^{\leqslant n,\otimes})^\vee$, and it is straightforward to check that we get back $\cat{Sm}_{A[n!^{-1}]}^{\leqslant n,\otimes}$ in this case. Moreover, by [\[lem:CartesianLiftsPreserved\]](#lem:CartesianLiftsPreserved){reference-type="ref" reference="lem:CartesianLiftsPreserved"}, the functor $$\bigl(\cat{Sm}_{A[n!^{-1}]}^{\leqslant,\otimes}\bigr)^\vee\longrightarrow \bigl(\cat{AniAlg}_A^{\qHodge,\otimes}\bigr)^\vee$$ preserves all cartesian lifts that exist in the source. We may thus dualise via [@DualFibration] to obtain a functor $$\cat{Sm}_{A[n!^{-1}]}^{\leqslant,\otimes}\longrightarrow \cat{AniAlg}_A^{\qHodge,\otimes}\,.$$ Now the $\infty$-operad $\cat{Sm}_{A[\dim!^{-1}]}^{\otimes}$ is built from $\cat{Sm}_{A[n!^{-1}]}^{\leqslant,\otimes}$ for all $n\geqslant 0$ via a sequence of pushouts as in [\[lem:SmoothPushout\]](#lem:SmoothPushout){reference-type="ref" reference="lem:SmoothPushout"}. Combining this with a straightforward analogue of [\[lem:CanonicalqHodgeSmoothFunctorial\]](#lem:CanonicalqHodgeSmoothFunctorial){reference-type="ref" reference="lem:CanonicalqHodgeSmoothFunctorial"}, we can inductively construct the desired map of $\infty$-operads. ◻
:::

[^1]: Said differently, we wish to equip $\IZ\qpower/(q-1)^n$ with the finite filtration given by $(q-1)^i\IZ\qpower/(q-1)^n$ in degree $i$. This is *not* the $(q-1)$-adic filtration in our sense, since the latter would be $\IZ\qpower/(q-1)^n$ in every degree, with transition maps given by multiplication by $(q-1)$.
