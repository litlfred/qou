---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-022-53-ind-coherent-sheaves-and-d-modules
section_title: "Ind-coherent sheaves and D-modules"
section_number: 5.3
pages: 33-36
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.982
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
[]{#actual sheaf theory label="actual sheaf theory"}

We now apply the results of Gaitsgory-Rozenblyum [@GR] and Drinfeld-Gaitsgory [@finiteness] establishing functoriality properties of categories of ind-coherent sheaves and $\cD$-modules.

We first state a fundamental result of Gaitsgory-Rozenblyum [@GR]:

::: thm
 [@GR Theorem III.3.5.4.3, III.3.6.3] []{#GR sheaf theory label="GR sheaf theory"} There is a uniquely defined right-lax symmetric monoidal functor $\cQ^!$ from the $(\infty,2)$-category whose objects are *laft* (locally almost of finite type) prestacks, morphisms are correspondences with vertical arrow ind-inf-schematic, and 2-morphisms are ind-proper and ind-inf-schematic, to the $(\infty,2)$ category $\ul{dgCat}_k$ of $k$-linear presentable dg categories with continuous morphisms. The functor $\cQ^!$ is strictly symmetric monoidal on the full subcategory of *laft* ind-inf-schemes.
:::

The theorem encodes a tremendous amount of structure in great generality. Let us highlight some salient features useful in practice. The theorem assigns a symmetric monoidal dg category $\cQ^!(X)$ to any stack satisfying a reasonable finite type assumption. The symmetric monoidal structure, the $!$-tensor product, is induced by $!$-pullback along diagonal maps. For an arbitrary morphism $p:X\to Y$ there is a continuous symmetric monoidal pullback functor $f^!:\cQ^!(Y)\to \cQ^!(X)$, while for $f$ schematic (or ind-schematic) there is a continuous pushforward $f_*:\cQ^!(X)\to \cQ^!(Y)$, which satisfies base change with respect to $!$-pullbacks. Moreover for $f$ proper (or ind-proper), $(f_*,f^!)$ form an adjoint pair.

The theorem goes much further through the powerful formalism of *inf-schemes*: prototypical inf-schemes are quotients of schemes by infinitesimal equivalence relation. Thus one can treat on an equal footing ind-coherent sheaves that are equivariant for any formal groupoid. The most important example is the de Rham space $X_{dR}$ of a scheme, and one recovers $\cD$-modules on $X$ as ind-coherent sheaves on the de Rham functor of $X$, $\cD(X)=\cQ^!(X_{dR})$. Thus by first applying the functor $(-)_{dR}$ the theorem encodes the theory of $\cD$-modules, as a functor out of the correspondence 2-category of stacks (or *laft* prestacks) with pullbacks for arbitrary maps and pushforward for (ind-)schematic maps.

::: corollary
The functors $\cQ^!$ and $\cD$ define sheaf theories on *laft* ind-inf-schemes, i.e., define symmetric monoidal functors $$\cQ^!,\cD: \uCorr(ind-inf-Sch_k)^{ind-prop}\longrightarrow \udg_k.$$ Thus the conclusions of Theorem [\[main\]](#main){reference-type="ref" reference="main"} apply in this setting (in particular the Grothendieck-Riemann-Roch theorem for ind-proper maps of ind-inf-schemes).
:::

### The QCA setting. {#QCA section}

We are mostly interested in applications of sheaf theory on stacks, e.g. in an equivariant setting. That requires two features of the theories $\cQ^!$ and $\cD$ that are not encoded in Theorem [\[GR sheaf theory\]](#GR sheaf theory){reference-type="ref" reference="GR sheaf theory"}.

Theorem [\[GR sheaf theory\]](#GR sheaf theory){reference-type="ref" reference="GR sheaf theory"} produces in general a *right-lax* symmetric monoidal functor -- in other words, we have the natural map $$\cQ^!(X)\ot\cQ^!(Y)\longrightarrow \cQ^!(X\times Y)$$ satisfying the expected coherences, but it is not an equivalence in general (though it is for schemes).

Also, while the theorem encodes arbitrary pullbacks, it does not encode a continuous pushforward functor $p_*:\cQ^!(X)\to \cQ^!(Y)$ for non-schematic morphisms (though a generalization to include QCA morphisms has been announced by the authors). This precludes an immediate application of our formalism to traces on stacks.

However, since the full structure of a sheaf theory is far stronger than is needed for the "local\" statements we discuss in this paper, we can get around this issue, by taking advantage of the following compilation of results of Drinfeld and Gaitsgory (specifically, see Section 3.6.1, Corollarys 3.7.14, 4.2.3, and 4.4.7, Proposition 4.4.11, Corollarys 8.3.4 and 8.4.3, Definition 9.3.2 and Proposition 9.3.12).

::: thm
 [@finiteness][]{#DG theorem label="DG theorem"}

1.  For a QCA stack $X$, the categories $\cQ^!(X)$ and $\cD(X)$ are dualizable and canonically self-dual.

2.  The canonical functors define equivalences $$\cQ^!(X)\otimes \cQ^!(Y)\simeq \cQ^!(X\times Y), \hskip.3in \cD(X)\otimes \cD(Y)\simeq \cD(X\times Y)$$

3.  For a morphism $f:X\to Y$ of QCA stack, the "renormalized pushforwards\"[^1] $$f_\bullet:\cQ^!(X)\to\cQ^!(Y), \hskip.3in f_\bullet:\cD(X)\to\cD(Y)$$ defined as the transpose of $f^!$ (by the self-duality of $(1)$) are continuous functors satisfying base-change and the projection formula with respect to pullback.
:::

Let us now briefly indicate how the results of the previous two sections carry over to QCA stacks in the absence of a fully fledged sheaf theory, where we use the renormalized pushforward functors $f_\bullet$ provided by Theorem [\[DG theorem\]](#DG theorem){reference-type="ref" reference="DG theorem"} to carry out non-representable pushforwards. In particular, for $X$ a general QCA stack, so that $pi_X:X\to pt$ is not representable, this means that the notation $\omega(X)$ has to be taken in a renormalized fashion, $$\omega(X):=\pi_{X,\bullet}\pi_X^! k = \pi_{X,\bullet}\omega_X.$$ For the theory of ind-coherent sheaves this produces the usual notion of derived global sections of the dualizing complex, but for the theory of $\cD$-modules this will differ in general from the nonrenormalized version, namely Borel-Moore chains on $X$: $$\omega(X)_{non-renorm}=R\Gamma_{dR}(\omega_X)=C_*^{BM}(X).$$

In Proposition [\[basic integral transforms\]](#basic integral transforms){reference-type="ref" reference="basic integral transforms"}, the self-duality in assertion (1) for QCA stacks is the content of Theorem [\[DG theorem\]](#DG theorem){reference-type="ref" reference="DG theorem"}(1), and $f_\bullet$ is defined so as to make it the transpose of $f^!$. Assertion (2) follows from the sheaf theory construction (i.e. is independent of non-representable morphisms), the projection formula is asserted in item (3) of the theorem and the last two assertions are deduced from the first three. Proposition [\[trace of integral transform\]](#trace of integral transform){reference-type="ref" reference="trace of integral transform"} is also deduced directly from Proposition [\[basic integral transforms\]](#basic integral transforms){reference-type="ref" reference="basic integral transforms"}.

The general trace construction $\int_f$ discussed in Section [\[2-cat\]](#2-cat){reference-type="ref" reference="2-cat"} depends only on the functoriality of proper adjunction (which is part of the [@GR] formalism) and the definition of pullback and (renormalized) pushforward. The identities needed to verify Propositions [\[sheaf unit and counit\]](#sheaf unit and counit){reference-type="ref" reference="sheaf unit and counit"},  [\[dim via integration\]](#dim via integration){reference-type="ref" reference="dim via integration"} and [\[trace via integration\]](#trace via integration){reference-type="ref" reference="trace via integration"} only depend on base change, which is guaranteed by Theorem [\[DG theorem\]](#DG theorem){reference-type="ref" reference="DG theorem"}. We therefore get as a payoff that the conclusions of Theorem [\[main\]](#main){reference-type="ref" reference="main"} hold for QCA stacks, in particular:

::: thm
Let $\cS=\cQ^!$ or $\cS=\cD$ denote either ind-coherent sheaves or $\D$-modules. Let $f:X\to Y$ denote a proper morphism of QCA stacks.

$\bullet$ For any compact object $M\in \cS(X)$ (coherent sheaf or safe coherent $\cD$-module) with character $[M]\in HH_*(\cS(X))\simeq \omega(\cL X)$, there is a canonical identification $$[f_*\cM]\simeq\int_{\cL f}[M]\in HH_*(\cS(Y))\simeq\omega(\cL Y)$$

$\bullet$ Assume $Y=BG$ for an affine group and $X=Z/G$ for $Z$ a proper QCA stack. Then for any compact object $M\in \cS(Z/G)$ ($G$-equivariant coherent sheaf or safely equivariant coherent $\cD$-module on $X$), and element $g\in G$, there is a canonical identification $$[f_*M]|_g \simeq \int_{\cL f} [M]|_{X^g}$$

$\bullet$ For a map $f:(X,Z)\to (Y,W)$ of QCA stacks with self-correspondences, the induced map $Tr(\cS(Z))\to Tr(\cS(W))$ is given by integration along fixed points $Z|_{\Delta_X}\to W_{\Delta_Y}$.
:::

[^1]: We note that for $\cQ^!$ the "renormalized\" pushforward is the standard pushforward functor, while for $\cD$ it differs for non-safe objects from the more familiar, but discontinuous, de Rham pushforward.
