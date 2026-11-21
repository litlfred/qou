---
doc_id: arxiv-math-0409393v1
doc_title: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS"
section_id: sec-003-4-the-q-gevrey-filtration-on-the-stokes-sheaf
section_title: "The q-Gevrey filtration on the Stokes sheaf"
section_number: 4
pages: 22-25
source_pdf: 0409393v1.pdf
source_sha256: 2107d961f6065539
toc_source: outline
text_source: latex
latex_prose_ratio: 0.852
latex_coverage_ratio: 0.98
doc_brief: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS — — The local analytic classiﬁcation of irregular linear q-diﬀerence equa- tions has recently been obtained by"
---
The sources of inspiration for the contents of this chapter are [@RamisGevrey], [@BV], [@MLR], [@Varadarajan] and [@Deligne86].

## The filtration for the Stokes sheaf of a tamely irregular module

We stick to the conventions of section [\[subsection:devissage\]](#subsection:devissage){reference-type="ref" reference="subsection:devissage"}, in particular, the notations of [\[equation:forme-canonique\]](#equation:forme-canonique){reference-type="ref" reference="equation:forme-canonique"} and [\[equation:forme-canonique-diagonale\]](#equation:forme-canonique-diagonale){reference-type="ref" reference="equation:forme-canonique-diagonale"}.

### Conditions of flatness

Let $F$ be a section of the sheaf $\Lambda_{I}(M_{0})$. Then, for $1 \leq i < j \leq k$, the block $F_{i,j}$ is solution of the equation: $$\sigma_qF_{i,j} \left(z^{-\mu_{j}} A_{j}\right) = \left(z^{-\mu_{i}} A_{i}\right) F_{i,j}.$$ \>From this and lemma [\[lemma:flatness\]](#lemma:flatness){reference-type="ref" reference="lemma:flatness"}, we draw that $F_{i,j}$ is $(\mu_{i} - \mu_{j})$-flat and that, if it is $t$-flat for some $t > \mu_{i} - \mu_{j}$, then it vanishes.\
We now introduce a filtration of the Stokes sheaf and a filtration of the sheaf of its Lie algebras. For real nonnegative $t$, we call $\lambda_{I}^{t}(M_{0})$ the subsheaf of $\lambda_{I}(M_{0})$ made of $t$-flat sections and $\Lambda_{I}^{t}(M_{0})$ the subsheaf $I_{n} + \lambda_{I}^{t}(M_{0})$ of $\Lambda_{I}(M_{0})$. The latter is a sheaf of unipotent subgroups, while the former is the sheaf of its Lie algebras (see the discussion in section [\[subsection:irregular-theory\]](#subsection:irregular-theory){reference-type="ref" reference="subsection:irregular-theory"}). Both filtrations are decreasing and exhaustive (the $0$-term is the total sheaf, the $t$-term is the trivial sheaf for $t > \mu_{1} - \mu_{k}$).\
\>From the previous argument, we see that $\lambda_{I}^{t}(M_{0})$ has a very simple concrete description in terms of matrices: its sections have non trivial blocks only over the "curved over-diagonal" consisting of those $(i,j)$-blocks such that $\mu_{i} - \mu_{j} = t$. There is a similar description for $\Lambda_{I}^{t}(M_{0})$ (taking in account the block-diagonal of identities). We shall however have use for a more intrinsic definition of these filtrations. We first describe the filtration of $\lambda_{I}(M_{0})$.

::: prop
[]{#prop:Lie=bundle label="prop:Lie=bundle"} (i) The sheaf $\lambda_{I}(M_{0})$ is the sheaf of sections of the vector bundle associated (see section [\[subsection:devissage\]](#subsection:devissage){reference-type="ref" reference="subsection:devissage"}) to the tamely irregular module $\underline{End}^{> 0}(M_{0})$.\
(ii) The above filtration on the sheaf $\lambda_{I}(M_{0})$ is the decreasing filtration associated to the graduation inherited from $\underline{End}^{> 0}(M_{0})$.
:::

We have $M_{0} = P_{1} \oplus \cdots \oplus P_{k}$, whence: $$\underline{End}(M_{0}) = 
\bigoplus_{1 \leq i,j \leq k} \underline{Hom}(P_{j},P_{i}).$$ The internal Hom $\underline{Hom}(P_{j},P_{i})$ is a pure module of slope $\mu_{i} - \mu_{j}$. Therefore, $\underline{End}^{> 0}(M_{0})$ is the sum of those $\underline{Hom}(P_{j},P_{i})$ such that $\mu_{i} > \mu_{j}$, *i.e.* $i < j$.\
On the other hand, the vector bundle associated to $\underline{Hom}(P_{j},P_{i})$ has as sections on an open subset $V$ of ${\mathbf{E}_{q}}$ the morphisms from $P_{j}$ to $P_{i}$ that are holomorphic on the preimage $U$ of $V$ in ${\mathbf C}^{*}$. This implies that the sheaf of sections of the vector bundle associated to the module $\underline{End}^{> 0}(M_{0})$ is indeed $\lambda_{I}(M_{0})$; that it is the direct sum of its subsheaves $\lambda_{I}^{(t)}(M_{0})$, where $\lambda_{I}^{(t)}(M_{0})$ is the sheaf of sections of the pure vector bundle associated to the pure module $$\underline{End}^{(t)}(M_{0}) = 
\bigoplus_{\mu_{i} - \mu_{j} = t} \underline{Hom}(P_{j},P_{i});$$ and that $\lambda_{I}^{t}(M_{0})$ is the direct sum of the $\lambda_{I}^{(t')}(M_{0})$ for all $t' \geq t$. $\Box$\
Actually the whole structure only depends on the filtrations and the properties of internal Homs, so that it can be extended to an arbitrary tannakian category.

::: prop
Let $t$ be a nonnegative integer.\
(i) $\Lambda_{I}^{t}(M_{0})$ is a sheaf of normal subgroups of $\Lambda_{I}(M_{0})$.\
(ii) The map $f \mapsto 1 + f$ induces an isomorphism: $$\lambda_{I}^{(t)}(M_{0}) \simeq 
\frac{\Lambda_{I}^{t}(M_{0})}{\Lambda_{I}^{t+1}(M_{0})}.$$
:::

Actually, these are purely algebraic properties: for a nilpotent two sided ideal $I$ of a non commutative algebra $A$, the subgroups $1 + I^{t}$ of the unit group are normal and their successive quotients are isomorphic to the quotient modules $I^{t}/I^{t+1}$. $\Box$\
We now are in position to reconstruct the Stokes sheaf by successive exact sequences: $$\label{equation:suite-exacte}
1 \rightarrow \Lambda_{I}^{t+1}(M_{0}) \rightarrow
\Lambda_{I}^{t}(M_{0}) \rightarrow \lambda_{I}^{(t)}(M_{0})
\rightarrow 0.$$

Note also that, again from general algebraic considerations, we have a sequence of central extensions: $$\label{equation:extension-centrale}
0 \rightarrow \lambda_{I}^{(t)}(M_{0}) \rightarrow
\frac{\Lambda_{I}(M_{0})}{\Lambda_{I}^{t+1}(M_{0})} \rightarrow
\frac{\Lambda_{I}(M_{0})}{\Lambda_{I}^{t}(M_{0})} \rightarrow 1.$$

## Cohomological consequences

::: lemma
Let $V$ be a proper open subset of ${\mathbf{E}_{q}}$. Then $H^{1}(V,\Lambda_{I}(M_{0}))$ is trivial.
:::

We apply theorem I.2 of [@Frenkel] to the exact sequence [\[equation:suite-exacte\]](#equation:suite-exacte){reference-type="ref" reference="equation:suite-exacte"}. This gives an exact sequence of pointed sets: $$H^{1}(V,\Lambda_{I}^{t+1}(M_{0})) \rightarrow 
H^{1}(V,\Lambda_{I}^{t}(M_{0})) \rightarrow 
H^{1}(V,\lambda_{I}^{t}(M_{0})).$$ If the extreme terms are trivial, so must be the central one (this, by the very definition of an exact sequence of pointed sets). The rightmost term is the first cohomology group of a vector bundle (after proposition [\[prop:Lie=bundle\]](#prop:Lie=bundle){reference-type="ref" reference="prop:Lie=bundle"}) over an open Riemann surface. Such a bundle being a trivial bundle, its $H^{1}$ is trivial. The leftmost term is trivial for $t > \mu_{1} - \mu_{k}$. By descending induction, the inner term is trivial for all $t$, hence for $t = 0$. $\Box$

::: prop
[]{#prop:bon-recouvrement label="prop:bon-recouvrement"} The covering ${\mathfrak{V}}$ is good.
:::

This means that the map from $H^{1}({\mathfrak{V}},\Lambda_{I}(M_{0}))$ to $H^{1}({\mathbf{E}_{q}},\Lambda_{I}(M_{0}))$ is an isomorphism. After [@BV], cor. 1.2.4, p. 113, this follows from the lemma. $\Box$\
Note that this ends the proof of theorem [\[thm:q-Malgrange-Sibuya\]](#thm:q-Malgrange-Sibuya){reference-type="ref" reference="thm:q-Malgrange-Sibuya"}.

## The Stokes sheaf of a general module

We briefly sketch here how the previous results extend to the Stokes sheaf of a module $M$. We take $M$ in the formal class of $M_{0}$ and identify it with $({{\mathbf C}(\{z\})}^{n},A_{U})$, according to the conventions of section [\[subsection:devissage\]](#subsection:devissage){reference-type="ref" reference="subsection:devissage"}.\
The mapping $\Phi \mapsto F_{D}(U) \Phi F_{D}(U)^{-1}$ defines an isomorphism from $\Lambda_{I}(M_{0})$ to $\Lambda_{I}(M)$ over $V_{D}$. Therefore, the two sheaves are locally isomorphic. Actually, the latter is obtained from the former by the operation of twisting by the cocycle $(F_{D,D'}(U))_{D,D'}$, described in [@Frenkel], prop. 4.2 (also see [@BV], II.1 or [@Varadarajan], pp. 30-31). According to the same references, their $H^{1}$ are isomorphic. Moreover, the same operations provide a local isomorphism of the sheaves of Lie algebras, so that $\lambda_{I}(M)$ is a vector bundle. Last, these isomorphisms preserve the filtrations by levels of flatness.\

::: rmk
[]{#rmk:vector-bundle label="rmk:vector-bundle"} One should also note that the mapping $X \mapsto F_{D}(U) X$ defines an isomorphism from the space of solutions of $A_{0}$ holomorphic over $(U_{D},0)$ to the same space for $A_{U}$. This means that their sheaves of solutions are locally isomorphic. Since the former is a vector bundle, so is the latter. This yields an explicit way of associating a vector bundle with an arbitrary module with integral slopes (for arbitrary slopes, see [@JSIRR], [@JSISOMONO]).
:::
