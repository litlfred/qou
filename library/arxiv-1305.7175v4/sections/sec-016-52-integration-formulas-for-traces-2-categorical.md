---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-016-52-integration-formulas-for-traces-2-categorical
section_title: "Integration formulas for traces: 2-categorical consequences"
section_number: 5.2
pages: 31-36
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.954
---
[]{#2-cat label="2-cat"} Now we turn to the functoriality of dimensions and traces. For this we require the 2-categorical enhanced version $\uS$ of a sheaf theory, so as to take advantage of the resulting functorial adjunction $$\xymatrix{\cS(X) \ar@<+.5ex>[r]^{f_*} &
  \ar@<+.5ex>[l]^{f^!}\cS(Y)}$$ for $f:X\to Y$ proper. In particular, applying the functor $\uS$ on two-morphisms we find that

$\bullet$ A proper map $f:Z\to W$ of correspondences $$\xymatrix{
&\ar[dl]_-{p_Z} Z \ar[dd]^-f \ar[dr]^-{q_Z} & \\
X & & Y\\
& \ar[ul]^-{p_W} W\ar[ur]_-{q_W} & 
}$$ induces a canonical integration morphism of integral transforms $$\xymatrix{
\int_f: q_{Z*}p_Z^! \ar[r] & q_{W*} p_W^!
}$$

$\bullet$ In particular, when $X=Y=pt$, it induces a map of global volume forms $$\xymatrix{
\int_f: \omega(Z) \ar[r] & \omega(W)
}$$

$\bullet$ There is a canonical composition identity $$\xymatrix{
 \int_g\circ\int_{f}\simeq \int_{g\circ f}
 }$$

::: prop
[]{#sheaf unit and counit label="sheaf unit and counit"} For $f:X\to Y$ proper, the unit and counit of the $(f_*,f^!)$ adjunction are given respectively by integration along the proper maps of self-correspondences $\Delta_{/Y}:X\to X\times_Y X$ of $X$ and $f_{/Y}:X\to Y$ of $Y$: $$\xymatrix{
&\ar[dl]_-{} X \ar[dd]^-{\Delta_{f}} \ar[dr]^-{} & && &\ar[dl]_-{f} X \ar[dd]^-{f} \ar[dr]^-{f} & \\
X & & X  && Y & & Y\\
& \ar[ul]^-{p_1} X\times_Y X\ar[ur]_-{p_2} & && & \ar[ul]^-{} Y\ar[ur]_-{} & 
}$$
:::

::: proof
*Proof.* The assertion follows immediately from the geometric description of the unit and counit in the correspondence category, Proposition [\[geometric adjunction\]](#geometric adjunction){reference-type="ref" reference="geometric adjunction"}, upon applying the functor $\uS$. ◻
:::

::: prop
[]{#dim via integration label="dim via integration"} For any proper map $f:X\to Y$, the induced map on dimensions $$\xymatrix{
\dim(f_*):\dim(\cS(X))\ar[r] & \dim(\cS(Y))
}$$ is identified ($S^1$-equivariantly) with integration along the loop map $$\xymatrix{
\dim(f_*)\simeq \int_{\cL f}:\omega(\cL X) \ar[r] & \omega(\cL Y)
}$$
:::

::: proof
*Proof.* According to Definition [\[functorial dim\]](#functorial dim){reference-type="ref" reference="functorial dim"}, we must calculate the composition $$\xymatrix{
\dim(f_*):\Tr(\id_{\cS(X)})\ar[r]^-{\Tr(\eta_f)}& \Tr(f^!f_*) \ar[r]^-{\sim} & \Tr(f_*f^!) \ar[r]^-{\Tr(\epsilon_f)} & \Tr(\id_{\cS(Y)})
}$$ The equivalence of the middle arrow is given by the canonical identifications $$\Tr(f^!f_*)\simeq \omega((X\times_Y X) \times_{X \times X} X) \simeq \omega(X \times_{Y\times Y} Y) \simeq  \Tr(f_*f^!)$$

By Proposition [\[sheaf unit and counit\]](#sheaf unit and counit){reference-type="ref" reference="sheaf unit and counit"}, the unit $\eta_f:\id_{\cS(X)}\to f^! f_*$ is given by the integration morphism $$\xymatrix{\int_{\Delta_{f}}: \Delta_{f *}\omega_X \ar[r] & \omega_{X\times_Y X}
}$$ and hence its trace $\Tr(\eta_f):\Tr(\id_{\cS(X)})\to \Tr(f^! f_*)$ is given by the induced integration map $$\xymatrix{
\int_{\Delta_f}:\omega(\cL X)\ar[r] & \omega((X\times_Y X) \times_{X \times X} X)
}$$

Likewise, the counit $\epsilon_f:f_*f^!\to \id_{\cS(Y)}$ is given by by the integration morphism $$\xymatrix{
\int_f:f_*\omega_X\ar[r] & \omega_Y
}$$ and hence its trace $\Tr(\epsilon_f):\Tr(f_* f^!)\to Tr(\id_{\cS(Y)})$ is given by the induced integration map $$\xymatrix{
\int_{f}:\omega(X \times_{Y\times Y} Y )\ar[r] & \omega(\cL Y)
}$$

Finally, by functoriality, their composition is given by the integration map $$\xymatrix{
\int_{\cL f}:\omega(\cL X)\ar[r] & \omega(\cL Y)
}$$ ◻
:::

Finally, we have the functoriality of traces in parallel with the previous theorem on the functoriality of dimensions. Let us recall the relevant setup. Consider a proper morphism $f:X\to Y$ and endomorphisms $F_Z:X\to X$ and $F_W:Y\to Y$ in $Corr_k$ given by respective self-correspondences $X\leftarrow Z \to X$ and $Y \leftarrow W \to Y$.

By an $f$-morphism from the pair $(X,F_Z)$ to the pair $(Y,F_W)$, we mean an identification $$\xymatrix{
  s:Z  \ar[r]^-\sim &  X\times_Y W
  }$$ of correspondences from $X$ to $Y$. This in turn induces an identification of what might be called relative traces $$\xymatrix{
  Z\times_{Y\times Y} Y\ar[r]^-\sim &  X\times_{Y\times Y} W
  }$$ generalizing the relative loop space $\cL_X Y$ from the case of the identity correspondences $Z=X$, $W=Y$. We thus obtain a map of traces $$\xymatrix{
\tau(f, s):Z|_{\Delta_X}  =   Z\times_{X\times X} X \ar[r] &   Z \times_{Y\times Y} Y \ar[r]^-\sim &  X \times_{Y\times Y} W \ar[r] &  
  Y\times_{Y\times Y} W = W|_{\Delta_Y}
}$$

::: prop
[]{#trace via integration label="trace via integration"} With the preceding setup, the trace map $\Tr(f_*,s):\Tr(F_{X*})\to\Tr(F_{Y*})$ is canonically identified with the integration map $$\xymatrix{
\int_{\tau(f, s)} : \omega( Z|_{\Delta_X}) \ar[r] & \omega(W|_{\Delta_Y} )
}$$
:::

::: proof
*Proof.* The argument is parallel to the proof of Proposition [\[dim via integration\]](#dim via integration){reference-type="ref" reference="dim via integration"}. One calculates $\Tr(f_*,\alpha)$ from Definition [\[functorial trace\]](#functorial trace){reference-type="ref" reference="functorial trace"} using Proposition [\[geometric traces\]](#geometric traces){reference-type="ref" reference="geometric traces"} and the compatibility of Proposition [\[basic integral transforms\]](#basic integral transforms){reference-type="ref" reference="basic integral transforms"} and the integration morphism for integral transforms from Section [\[integration section\]](#integration section){reference-type="ref" reference="integration section"}. ◻
:::

## Ind-coherent sheaves and $\cD$-modules {#actual sheaf theory}

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
