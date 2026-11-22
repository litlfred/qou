---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-007-23-modules
section_title: "Modules"
section_number: 2.3
pages: 7-9
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.898
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
[]{#sec:mod label="sec:mod"} Now, let $R_{E/F}$ denote the $\prod_{\Gamma_{E/F}}\mathbb{Z}$-graded $L_{E}$-algebra $$\bigoplus_{(b_{\tau})_{\tau} \in \prod_{\Gamma_{E/F}}\mathbb{Z}} (L_{E})_{(b_{\tau})_{\tau}},$$ with addition defined component-wise and multiplication determined by $\ell_{(b_{\tau})_{\tau}} \cdot \ell'_{(c_{\tau})_{\tau}} = (\ell \cdot \ell')_{(b_{\tau} + c_{\tau})_{\tau}}$ for all $\ell, \ell' \in L_{E}$. This ring will also be equipped with an $\mathfrak{f}_{E}$-semilinear action, denoted by $\Phi_{R_{E/F}}$, determined by the semilinearity condition and the identity $\Phi_{R_{E/F}}(1_{(b_{\sigma})}) = \prod_{\gamma \in \Gamma_{E/F}} \gamma(\varpi_{E})^{b_{\gamma}}1_{(b_{\sigma})}$.

::: defn
For a positive integer $s$, we define the category $RP_{E/F,s}$ to have objects given by tuples $(V, \Phi, \mathcal{D})$, consisting of

-   a (not necessarily finite-dimensional) $L_{E}$-vector space $V$ equipped with an $R_{E/F}$-action such that it is finitely generated as an $R_{E/F}$-module,

-   an $\mathfrak{f}_{E}$-semilinear isomorphism $\Phi$,

-   and a $\prod_{\Gamma_{E/F}} \frac{1}{s}\mathbb{Z}$-grading $\mathcal{D}$ such that $V_{(a_{\sigma}/s)}$ has an $L_{E}$-basis on which $\Phi^{s}$ acts by the scalar $\prod_{\sigma \in \Gamma_{E/F}} \sigma(\varpi_{E})^{a_{\sigma}}$.

In addition, we require that the $R_{E/F}$-action is compatible with the $\Phi$-action, in the sense that, for all $v \in V$ and $r \in R$, we have $\Phi(r \cdot v) = \Phi_{R_{E/F}}(r) \cdot \Phi(v)$. Note that this last condition implies that $$1_{(b_{\sigma})} \cdot V_{(a_{\sigma}/s)} \subseteq V_{(\frac{a_{\sigma} + sb_{\sigma}}{s})}.$$

Morphisms in $RP_{E/F,s}$ will be $\Phi$-equivariant morphisms of $R_{E/F}$-modules that preserve the gradings. Note that $RP_{E/F,s}$ is a rigid abelian tensor category over $E$ with identity object $R_{E/F}$ (with the canonical $R_{E/F}$-module structure, and $\Phi = \Phi_{R_{E/F}}$).
:::

We now define a fiber functor for this category. First, note that there is a canonical surjective augmentation map $R_{E/F} \to L_{E}$ defined by sending each $1_{(b_{\sigma})}$ to $1$, whose kernel we will denote by $I$. Note for an object $(V, \Phi, \mathcal{D})$ of $RP_{E/F,s}$, that $V$ is a finitely generated and free, hence flat, $R_{E/F}$-module. Hence, we have an equality of $L_{E}$-vector spaces $V \otimes_{R} R_{E/F}/I = V/IV$. We define a functor $\omega_{RP_{E/F, s}}: RP_{E/F, s} \to \mathrm{Vect}_{L_E}$ by $$(V, \Phi, \mathcal{D}) \mapsto V/IV.$$

Note that $IV$ is exactly the kernel of the natural $L_{E}$-linear surjection $V \to \bigoplus_{(0) \leq (a_{\sigma}/s) < (1)} V_{(a_{\sigma}/s)}$ defined on each $V_{([a_{\sigma}+sb_{\sigma}]/s)}$ by multiplication by $1_{(-b_{\sigma})}$. This defines an $L_{E}$-linear tensor functor.

::: lem
[]{#exactlem1 label="exactlem1"} The above functor is a fiber functor; that is, it is faithful and exact.
:::

::: proof
*Proof.* We first prove faithfulness. Let $f$ and $g$ be two morphisms from $V$ to $W$ (we omit the other structure from our notation for brevity), and suppose that their image under this functor coincides, and let $V_{(b_{\sigma}/s)}$ be a fixed graded component of $V$. Since these categories are additive, we may assume that $g$ equals zero. For any $v \in  V_{(b_{\sigma}/s)}$, we know that $f(v) \in W_{(b_{\sigma}/s)}$, but also that $f(v) \in IW$, and thus conclude by observing that $IW \cap W_{(b_{\sigma}/s)}= 0$ for all tuples $(b_{\sigma}/s)$.

We now prove exactness. By construction, this functor is evidently right-exact, so we only need to prove that it preserves injections. To this end, suppose that $v \in V$ is such that $f(v) \in IW$ for injective $f$. Writing $$v = \sum_{(a_{\sigma}/s)} v_{(a_{\sigma}/s)}$$ in terms of graded components, we note that, since $f$ is $R_{E/F}$-linear, for all $(b_{\sigma})$, we have $$f(v_{([a_{\sigma} + sb_{\sigma}]/s)}) = 1_{(b_{\sigma})} \cdot f(1_{(-b_{\sigma})} \cdot v_{([a_{\sigma} + sb_{\sigma}]/s)}).$$ It follows that $$f(v) = \sum_{(0) \leq (a_{\sigma}/s) < (1)} \sum_{(b_{\sigma})} 1_{(b_{\sigma})} \cdot f(1_{(-b_{\sigma})} \cdot v_{([a_{\sigma} + sb_{\sigma}]/s)}).$$

For this expression to lie in $IW$, it is necessary that, for a fixed $(0) \leq (a_{\sigma}/s) < (1)$, we have $$\sum_{(b_{\sigma}) \neq (0)} f(1_{(-b_{\sigma})} \cdot v_{([a_{\sigma} + sb_{\sigma}]/s)}) = -f(v_{(a_{\sigma}/s)})$$ inside the space $W_{(a_{\sigma}/s)}$. Since $f$ is injective, this means that $$\sum_{(b_{\sigma}) \neq (0)} 1_{(-b_{\sigma})} \cdot v_{([a_{\sigma} + sb_{\sigma}]/s)} = -v_{(a_{\sigma}/s)}$$ in $V_{(a_{\sigma}/s)}$, which implies that $v \in IV$. ◻
:::

It follows from the above Lemma [\[exactlem1\]](#exactlem1){reference-type="ref" reference="exactlem1"} that $RP_{E/F,s}$ is a Tannakian category over $E$. For $s \mid s'$, note that the embedding functor $\iota_{s,s'}$ extends naturally to a functor, also denoted by $\iota_{s,s'}$, from $RP_{E/F,s}$ to $RP_{E/F,s'}$, defined identically (with the $R_{E/F}$-module structure of $\iota_{s,s'}(X)$ being the same as the one associated to $X$). As before, the direct limit of these categories will be denoted by $RP_{E/F}.$

We now want to investigate the band of $RP_{E/F,s}$ (and thus $RP_{E/F}$). There is an "extension of scalars\" functor $q \colon P_{E/F,s} \to RP_{E/F,s}$ given by $V \mapsto R_{E/F} \otimes_{L_{E}} V$ on objects, and by $f \mapsto \text{id}_{R_{E/F}} \otimes f$ on morphisms, which is an $L_{E}$-linear tensor functor. Recall that an exact tensor functor between Tannakian categories $P$ and $Q$ is called a *quotient functor* if every object of $Q$ is a subquotient of an object in the image of the functor.

::: prop
The functor $q \colon P_{E/F,s} \to RP_{E/F,s}$ is a quotient functor.
:::

::: proof
*Proof.* Since $R_{E/F}$ is a flat $L_{E}$-module, the functor $q$ is evidently exact. To show the other condition for quotient functors, let $(V, \Phi, \mathcal{D})$ be an object of $RP_{E/F,s}$, and let $\{e_{i}\}_{i=1}^{n}$ be a set of generators for $V$ as an $R_{E/F}$-module, which we may assume without loss of generality is such that $e_{i} \in V_{(a_{\sigma})_{\sigma}}$ (depending on $i$) on which $\Phi^{s}$ acts in the appropriate way. We then get an object of $P_{E/F,s}$ by taking the $L_{E}$-span of $\{e_{i}\}$, with the obvious inherited grading and $\Phi$-action; denote this object by $(\tilde{V}, \tilde{\Phi}, \tilde{\mathcal{D}})$. Then $R_{E/F} \otimes_{L_{E}} \tilde{V}$ is a free $R_{E/F}$-module, with basis $\{1 \otimes e_{i}\}$, and there is a quotient map $R_{E/F} \otimes_{L_{E}} \tilde{V} \to V$ sending $1 \otimes e_{i}$ to $e_{i}$, which is a morphism in $RP_{E/F,s}$, giving the result. ◻
:::

In the notation of [@MilneQuot §2], recall that $P_{E/F,s}^{q}$ denotes all objects of $P_{E/F,s}$ whose image under $q$ is isomorphic to a direct sum of copies of the identity object in $RP_{E/F, s}$, which is a full Tannakian subcategory over $E$. Observe that an object $(V, \Phi, \mathcal{D})$ in $P_{E/F,s}$ lies in $P_{E/F,s}^{q}$ if and only if the only nonzero graded components $V_{(a_{\sigma}/s)}$ are such that each $a_{\sigma}/s$ is an integer. According to [@MilneQuot §2], the band of the gerbe corresponding to $RP_{E/F,s}$ is canonically isomorphic to all automorphisms of the fiber functor of $P_{E/F,s}$ which restrict trivially to $P_{E/F,s}^{q}$. In order to investigate how the band acts on the restriction of the fiber functor to these objects, it is easiest to use our identification of $P_{E/F,s}$ with $\text{Rep}_{L_{E}}(\mathcal{E}_{(c_{\sigma})_{\sigma}})$ from the previous subsection. We will work not with $P_{E/F,s}$, but instead with $P_{E/F,s,\overline{L}}$, which is the same category as $P_{E/F,s}$ except replacing $L_{E}$-vector spaces with $\overline{L}$-vector spaces and the semilinear $\mathfrak{f}_{E}$-action with a semilinear $W_{\overline{F}/E}$-action that acts on an $\overline{L}$-basis of the graded pieces in the same way (after restricting to $\Gamma_{L_{E}/E}$).

Let $(x_{\sigma}) \in \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(\overline{F})$, which acts on the canonical $\overline{F}$-fiber functor of $\text{Rep}_{\overline{F}}(\mathcal{E}_{(c_{\sigma}),\overline{F}})$ by, for a fixed representation $V$, mapping the $\prod_{\Gamma_{E/F}}\mathbb{Z}$-graded piece $V_{(h_{\sigma})}$ to itself via sending $v$ to $(\prod x_{\sigma}^{h_{\sigma}})v$. The image of the subcategory $P_{E/F,s,\overline{F}}^{q}$ under the above equivalence is all representations whose only nonzero graded pieces have each $h_{\sigma}$ divisible by $s$. These two observations make show that the subgroup of $\prod_{\Gamma_{E/F}} \mathbb{G}_{m}(\overline{F})$ fixing the image of $P_{E/F,s,\overline{F}}^{q}$ is exactly $\prod_{\Gamma_{E/F}} \mu_{s}(\overline{F})$, which implies (since we know that the band is an $E$-subgroup scheme of the band of $\mathcal{E}_{(c_{\sigma})_{\sigma}}$, which is $\prod_{\Gamma_{E/F}} \mathbb{G}_{m})$) that the band of the gerbe over $E$ corresponding to the Tannakian category $RP_{E/F,s}$ may be identified with the $E$-group scheme $\prod_{\Gamma_{E/F}} \mu_{s}$.
