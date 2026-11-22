---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-007-31-disk-algebras
section_title: "Disk algebras"
section_number: 3.1
pages: 14-17
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.971
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
::: definition
The $\infty$-category of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$-algebras in $\mathcal V$ $$\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}(\mathcal V)~:=~\mathop{\mathrm{\sf Fun}}^\otimes(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n, \mathcal V)$$ is the $\infty$-category of symmetric monoidal functors.
:::

There is the restricted Yoneda functor $$\mathbb E\colon \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B \longrightarrow  \mathop{\mathrm{\sf PShv}}(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B) \longrightarrow \mathop{\mathrm{\sf PShv}}(\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B)~.$$

::: definition
[]{#coend label="coend"} Let $M$ be a $B$-framed $n$-manifold. Let $A$ be a $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$-algebra in $\mathcal V$. *Factorization homology (of $M$ with coefficients in $A$)* is an object of $\mathcal V$ given by either of the equivalent expressions (provided they exist) $$\begin{aligned}
\nonumber
\int_M A
&
:=
&
\mathop{\mathrm{\sf colim}}\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}^B \to \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \xrightarrow{A} \mathcal V\bigr)
\\
\nonumber
&
\simeq
&
\mathbb E_M\underset{\mathop{\mathrm{{\mathcal D}\sf isk}}_M^B} \bigotimes A~,
\end{aligned}$$ where the latter is the coend.
:::

::: remark
The fact that one describes factorization homology as either a coend or a left Kan extension is exactly analogous to a more familiar fact about the geometric realizations of a simplicial set $X_\bullet$: one can think of geometric realization as a coend (this is the usual definition, given as a quotient of $\coprod_i X_i \times \Delta^i$), or one can think of it as a left Kan extension (the colimit of the overcategory of simplices in $X_\bullet$ of the functor which sends the simplicial $i$-simplex $\Delta[i]$ to the topological $i$-simplex $\Delta^i$).
:::

We will frequently make the following requirement of our target.

::: definition
[]{#ast label="ast"} We say symmetric monoidal $\mathop{\mathrm{\infty}}$-category $\mathcal V$ is *$\otimes$-presentable* if it satisfies both of the following conditions.

-   $\mathcal V$ is presentable: with respect to an understood fixed uncountable cardinal, $\mathcal V$ admits colimits and every object is a filtered colimit of compact objects.

-   The monoidal structure distributes over small colimits: for each object $V\in \mathcal V$, the functor $V\otimes-\colon \mathcal V\to \mathcal V$ carries colimit diagrams to colimit diagrams.
:::

::: example
The Cartesian monoidal $\mathop{\mathrm{\infty}}$-category $(\mathop{\mathrm{\mathsf{Spaces}}},\times)$ is $\otimes$-presentable. Likewise, for $R$ a ring then $\bigl({\sf Mod}_R, \otimes\bigr)$, with tensor product relative $R$, is $\otimes$-presentable (though the opposite $\bigl({\sf Mod}_R^{\mathop{\mathrm{\mathsf{op}}}}, \otimes\bigr)$ is not).
:::

::: remark
The results of Section 3 (in particular, the Eilenberg--Steenrod axioms for factorization homology) only require that the monoidal structure distributes over sifted colimits; these results are established in this generality, though with a smooth structure present, in §2 of [@aft2]. However, the calculations of Section 4 onwards require the monoidal structure to distribute over all colimits, so for simplicity of exposition we enforce this stronger hypothesis throughout.
:::

The fully faithful symmetric monoidal functor $\iota\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \hookrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B$ gives the restriction functor $$\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}(\mathcal V)~\longleftarrow~  \mathop{\mathrm{\sf Fun}}^\otimes\bigl(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathcal V\bigr)\colon \iota^\ast~.$$ The next result identifies factorization homology as a left adjoint to this functor, provided $\mathcal V$ is $\otimes$-presentable.

::: prop
[]{#as-LKE label="as-LKE"} Provided $\mathcal V$ is $\otimes$-presentable, there is a left adjoint $$\iota_!\colon \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}(\mathcal V)~ \rightleftarrows~ \mathop{\mathrm{\sf Fun}}^\otimes\bigl(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathcal V\bigr)\colon \iota^\ast~,$$ and its value on $A$ evaluates as $$\iota_!(A)\colon M\mapsto \int_M A~.$$
:::

::: proof
*Proof.* Presentability of $\mathcal V$ grants the existence of the values $\int_M A$. Lemma 4.3.2.13 of [@topos] states that these expressions define a functor, as indicated. Proposition 4.3.3.7 of [@topos] states that this functor satisfies the universal property of being a left adjoint to the restriction $\iota^\ast$. We thus have the solid diagram among $\infty$-categories $$\xymatrix{
\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}(\mathcal V)  \ar[d] \ar@{-->}[rr]
&&
\mathop{\mathrm{\sf Fun}}^\otimes\bigl(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathcal V\bigr)  \ar[d] 
\\
\mathop{\mathrm{\sf Fun}}(\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B,\mathcal V)  \ar[rr]^-{\iota_!}
&&
\mathop{\mathrm{\sf Fun}}(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathcal V)
}$$ in which the downward functors are restriction to underlying $\infty$-categories, these downward functors are fully faithful. It remains to explain how the $\otimes$-presentability of $\mathcal V$ grants the existence of the dashed horizontal functor making the diagram commute.

We must show that, for each symmetric monoidal functor $A\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B\to \mathcal V$, and for each based map among finite sets $I_+ \xrightarrow{f} J_+$, the diagram of $\infty$-categories $$\xymatrix{
(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B)^I  \ar[d]_-{f_\ast}  \ar[rr]^-{(\iota_! A)^I}
&&
\mathcal V^I  \ar[d]^-{f_\ast}
\\
(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B)^J  \ar[rr]^-{(\iota_! A)^J}
&&
\mathcal V^J
}$$ commutes. The map $f \colon I_+ \to J_+$ is canonically a composition of a surjective active map $f^{\sf surj}$ followed by an injective active map $f^{\sf inj}$ followed by an *inert* map $f^{\sf inrt}$, and so it is enough to verify commutativity of the above diagram for each such class of maps. The case of inert maps is obvious, because then $f_\ast$ is projection and $(\iota_! A)^K$ is defined as the $K$-fold product of functors, for $K=I,J$. The case of injective active maps amounts to verifying that $\iota_! A$ carries each monoidal unit to a monoidal unit. This follows because $A$ does so and because the over $\infty$-categories $\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/\emptyset}^B = \{\emptyset\} = \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_{n/\emptyset}^B$ consist solely of the empty manifold, which is the monoidal unity.

The case of surjective active maps follows from the case that $f\colon I_+ \to \ast_+$ is given by $+\neq i\mapsto \ast$, so that $f_\ast = \bigotimes^I$ is the $I$-fold tensor product. Well, because $A$ is symmetric monoidal, there is a canonical arrow $\iota_! A \circ \bigotimes^I 
\longrightarrow 
\bigotimes^I\circ (\iota_! A)^I$ between functors $(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B)^I \to \mathcal V$ that we will argue is an equivalence. This arrow evaluates on $(M_i)_{i\in I}$ as the horizontal one in the following natural diagram in $\mathcal V$: $$\xymatrix{
\mathop{\mathrm{\sf colim}}\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/\underset{i\in I}\bigsqcup M_i} \to \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B\xrightarrow{A} \mathcal V\bigr)  \ar[r]
&
\underset{i\in I}\bigotimes \mathop{\mathrm{\sf colim}}\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M_i} \to \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \xrightarrow{A} \mathcal V\bigr) 
\\
\mathop{\mathrm{\sf colim}}\Bigl( \underset{i\in I}\prod \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M_i} \to (\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B)^I \xrightarrow{A^I} \mathcal V^I\xrightarrow{\bigotimes^I} \mathcal V\Bigr) \ar[u]^-{(\ast)}  \ar[ur]_-{(\dagger)}
&
.
}$$ The arrow labeled by ($\dagger$) is an equivalence precisely because $V\otimes- \colon \mathcal V\to \mathcal V$ preserves colimits. By inspection, the $I$-fold disjoint union functor $\bigsqcup^I\colon \prod_{i\in I} \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M_i} \xrightarrow{\simeq} \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/\underset{i\in I}\bigsqcup M_i}$ is an equivalence between $\infty$-categories, for it is essentially surjective and fully faithful. It follows that the arrow labeled by ($\ast$) is an equivalence, after observing the following commutative diagram among $\infty$-categories: $$\xymatrix{
\underset{i\in I} \prod \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M_i}  \ar[rr]^-{\bigsqcup^I}  \ar[d]
&&
\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/\underset{i\in I} \bigsqcup M_i}  \ar[d]
\\
(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n)^I  \ar[rr]^-{\bigsqcup^I}  \ar[d]_-{A^I}
&&
\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n  \ar[d]^-A
\\
\mathcal V^I \ar[rr]^-{\bigotimes^I} 
&&
\mathcal V~.
}$$ ◻
:::

::: remark
Proposition [\[as-LKE\]](#as-LKE){reference-type="ref" reference="as-LKE"} implies factorization homology can be expressed as symmetric monoidal left Kan extension, at least when $\mathcal V$ is $\otimes$-presentable. This is equivalent to operadic left Kan extension (after parsing Definitions 3.1.1.2 and 3.1.2.2 of [@dag]), which is the definition of factorization homology, or topological chiral homology, given by Lurie (Definition 5.5.2.6).
:::

The following justifies the notational omission of the space $B$ from the notation $\int_MA$.

::: prop
[]{#without-B label="without-B"} Given a map $\varphi:B\rightarrow B'$ of spaces over $\mathop{\mathrm{\sf BTop}}(n)$ and $M$ a $B$-framed $n$-manifold and $A$ a $B'$-framed $n$-disk algebra, composition with the map $\varphi$ defines a $B'$-framed $n$-manifold $\varphi M$, and restriction along $\varphi$ defines a $B$-framed $n$-disk algebra $\varphi A$. There is a natural equivalence $$\int_{\varphi M} A\simeq\int_{M} \varphi A$$ between the $B$-framed and $B'$-framed factorization homologies.
:::

::: proof
*Proof.* It suffices to show that the forgetful functor $\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}^B\rightarrow\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}$ is an equivalence. By definition, this functor is the projection from the double overcategory: $$\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}^B~:=~ (\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/B})_{/M} \longrightarrow \mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}.$$ This functor is a pullback of the likewise functor $\bigl((\mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)})_{/B}\bigr)_{/M} \to (\mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)})_{/M}$, which is an equivalence by Lemma [\[slice-slice\]](#slice-slice){reference-type="ref" reference="slice-slice"}. ◻
:::
