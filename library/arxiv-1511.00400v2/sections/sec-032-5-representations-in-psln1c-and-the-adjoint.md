---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-032-5-representations-in-psln1c-and-the-adjoint
section_title: "Representations in PSLn+1(C) and the adjoint"
section_number: 5
pages: 36-39
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.986
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sec:adj label="sec:adj"}

In [@Memoirs] I considered the torsion corresponding to the adjoint representation as a function on the variety of characters in $\mathrm{SL}_2(\mathbb{C})$, in fact $\mathrm{PSL}_2(\mathbb{C})$. Kitayama and Terashima [@KitayamaTerashima15] considered the analog for $\mathrm{PSL}_{n+1}(\mathbb{C})$, i.e. the torsion for the adjoint representation.

Along the section $M^3$ denotes an oriented finite volume hyperbolic three-manifold with one cusp, the case with more cusps would require further notation, but here it is essentially the same. Consider the composition of the holonomy with $\operatorname{Sym}^{n}$: $$\varrho^{n}\colon\pi_1M^3\to \mathrm{PSL}_{n+1}(\mathbb{C}).$$ As we deal with representations in $\mathrm{PSL}_2(\mathbb{C})$, the holonomy does not need to be lifted to $\mathrm{SL}_2(\mathbb{C})$.

::: thm
[]{#thm:distn+1 label="thm:distn+1"} The character of $\varrho^{n}$ is a smooth point of the variety of characters $X(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$, of local dimension $n$. It is locally parametrized by the symmetric functions on any peripheral curve.
:::

::: cor
There exists a unique irreducible component of the character variety $X(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ that contains the character of $\varrho^{n}$.
:::

This component is called the *distinguished component* and it is denoted by $$X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C})).$$

In the proof of Theorem [\[thm:distn+1\]](#thm:distn+1){reference-type="ref" reference="thm:distn+1"}, one shows that $\mathfrak{sl}_{n+1}(\mathbb{C})^{\operatorname{Ad}\varrho^{n}(\pi_1 T^2)}\cong \mathbb{C}^n$. In addition, if $\{a_1,\ldots, a_{n}\}$ is a basis for $\mathfrak{sl}_{n+1}(\mathbb{C})^{\operatorname{Ad}\varrho^{n}(\pi_1 T^2)}$, then $$\{ a_1\cap [T^2],\ldots, a_{n}\cap [T^2]\}$$ is a basis for $H_2(M^3; \operatorname{Ad}\varrho^n)$ and $$\{ a_1\cap [\gamma],\ldots, a_{n}\cap [\gamma]\}$$ a basis for $H_1(M^3; \operatorname{Ad}\varrho^n)$, here $\gamma$ is a peripheral curve, non-trivial in $H_1(T^2;\mathbb{Z})$. See [@MFP12; @MFP12b; @KitayamaTerashima15] for details. For a generic character $\chi_\rho$ in $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$, $\mathfrak{sl}(n,\mathbb{C})^{\operatorname{Ad}\rho(\pi_1 T^2)}\cong \mathbb{C}^n$ and a similar construction applies to find a basis for $H_i(M^3; Ad\rho)$. Generalizing the construction of [@Memoirs], Kitayama and Terashima [@KitayamaTerashima15] define the torsion. Here we consider the possibility that the function vanishes, but before an exceptional set must be removed.

::: definition
A representation $\rho\colon\pi_1 M^3\to\mathrm{PSL}_{n+1}(\mathbb{C})$ is *exceptional* if:

(a) $\mathfrak{sl}_{n+1}(\mathbb{C})^{\operatorname{Ad}\rho(\pi_1M^3)}\neq 0$ or

(b) $\dim \left(\mathfrak{sl}_{n+1}(\mathbb{C})^{\operatorname{Ad}\rho(\pi_1T^2)}\right)> n$, for the peripheral torus $T^2$.

The set of characters of exceptional representations is denoted by $$\mathrm{E}_{n+1}\subset X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}) ).$$
:::

::: lemma
The set $\mathrm{E}_{n+1}$ is Zariski closed in $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}) )$.
:::

::: proof
*Proof.* The defining properties are Zariski closed in $\hom(\pi_1M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ and invariant by conjugation, so the projection to $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ is a Zariski closed subset, see [@VP89] for instance. ◻
:::

::: definition
Let $\chi_\rho\in X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))-\mathrm{E}_{n+1}$, choose $\{a_1,\ldots, 
a_{n}\}$ a basis for $\mathfrak{sl}_{n+1}(\mathbb{C})^{ \operatorname{Ad}\rho(\pi_1 T^2)}$ and let $\gamma$ be a peripheral curve.

(a) If $\{ a_1\cap [\gamma],\ldots, a_{n}\cap [\gamma]\}$ is a basis for $H_1(M^3;\operatorname{Ad}\rho)$, define $$\begin{gathered}
        \mathcal{T}_{(M,\gamma)}(\chi_\rho)= \operatorname{TOR}(M^3, \{ a_1\cap [\gamma],\ldots, a_{n}\cap [\gamma]\}, \\
        \{ a_1\cap [T^2],\ldots, a_{n}\cap [T^2]\});
       
    \end{gathered}$$

(b) otherwise set $$\mathcal{T}_{(M,\gamma)}(\chi_\rho)=0.$$
:::

This yields a function $$\mathcal{T}_{M,\gamma}\colon  X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))-E_{n+1} \to \mathbb{C}\, .$$ It can be checked that it is a well defined regular function, using the ideas of [@Memoirs; @KitayamaTerashima15] and Proposition [\[prop:rational\]](#prop:rational){reference-type="ref" reference="prop:rational"}. For instance, when $\{ a_1\cap [\gamma],\ldots, a_{n}\cap [\gamma]\}$ is a basis for $H_1(M^3;\operatorname{Ad}\rho)$, then $\{ a_1\cap [T^2],\ldots, a_{n}\cap [T^2]\}$ is a basis for $H_2(M^3;\operatorname{Ad}\rho)$ (because $H_2(M^3;\operatorname{Ad}\rho)$ is naturally isomorphic to $H_2(T ^2;\operatorname{Ad}\rho)\cong 
H^0(T ^2 ; \operatorname{Ad}\rho)$). When there may be confusion, the index $n+1$ may be included in the notation:

$$\mathcal{T}_{M,\gamma}^{n+1}\colon  X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))-E_{n+1} \rightarrow \mathbb{C}.$$

The following proposition relates $\mathcal{T}_{M,\gamma}$ with the torsion $\mathbb{T}^{2n}_{(M,\gamma)}$ when we consider symmetric powers of representations in $\mathrm{PSL}_2(\mathbb{C})$.

::: prop
[]{#prop:product label="prop:product"} For a generic character $\chi_\rho\in X_0(M^3,\mathrm{PSL}_2(\mathbb{C}))$, including the holonomy $\chi_\varrho$, $$\mathcal{T}_{M,\gamma}^{n+1}(\chi_{\rho^n})=\prod_{i=1}^n \mathbb{T}_{M,\gamma}^{2 i}(\chi_\rho).$$
:::

::: cor
[]{#cor:difrentdims label="cor:difrentdims"} For a generic character $\chi_\rho\in X_0(M^3,\mathrm{PSL}_2(\mathbb{C}))$, including the holonomy $\chi_\varrho$, $$\mathcal{T}_{M,\gamma}^{n+1}(\chi_{\rho^n})=\mathcal{T}_{M,\gamma}^{n}(\chi_{\rho^{n-1}})\, \mathbb{T}_{M,\gamma}^{2 n}(\chi_\rho).$$
:::

::: proof
*Proof of Proposition [\[prop:product\]](#prop:product){reference-type="ref" reference="prop:product"}.* The proof is straightforward from Klebsh-Gordan formula: $$\label{eqn:adKG}
  \operatorname{Ad}\circ\operatorname{Sym}^n=\bigoplus_{i=1}^n \operatorname{Sym}^{2i}$$ and multiplicativity of the torsion for sums of representations. ◻
:::

The next theorem due to Weil [@Weil64], see also [@LM85], gives a nice interpretation to $\mathcal{T}_{M,\gamma}$:

::: thm
[]{#thm:Weil label="thm:Weil"} Let $\Gamma$ be a finitely generated group and $\rho$ an irreducible representation with character $\chi_\rho\in X(\Gamma, \mathrm{PSL}_{n+1}(\mathbb{C}) )-\mathrm{E}_{n+1}$. Then there is a natural isomorphism $$T^{Zar}_{\chi_\rho} X(\Gamma, \mathrm{PSL}_{n+1}(\mathbb{C}) )\cong H^1(\Gamma ; \operatorname{Ad}\rho)$$ where $T^{Zar}$ denotes the Zariski tangent space as a scheme.

In particular, if $\phi\colon\Gamma\to\Gamma'$ is a group morphism, then the induced map in cohomology corresponds to the tangent map $$d\phi^* \colon T^{Zar}_{\chi_\rho} X(\Gamma', \mathrm{PSL}_{n+1}(\mathbb{C}) )\to  
T^{Zar}_{\phi^*\chi_\rho} X(\Gamma, \mathrm{PSL}_{n+1}(\mathbb{C}) ).$$
:::

Few comments are in order here. First at all, the condition that $\chi_\rho\not\in\mathrm{E}_{n+1}$ is used to say that the infinitesimal commutator of $\operatorname{Ad}\rho$ is trivial, i.e. $H^0(\pi_1 M^3;\operatorname{Ad}\rho)=0$. Secondly, the variety of characters is not a variety but a scheme: the defining polynomial ideal may be not reduced, thus we must consider the Zariski tangent space of the scheme, perhaps not reduced. Finally, just mention that there are generalizations of this result when $\rho$ is reducible, see [@BenAbdelghani2000; @BenAbdelghani2002].

This interpretation has a nice application for surface bundles over the circle, following again [@Memoirs; @KitayamaTerashima15]. Assume that $M^3$ is a bundle over a circle, with fibre a punctured surface $\Sigma$ and monodromy $\varphi\colon\Sigma\to \Sigma$, i.e. $$M^3=\Sigma\times [0,1]/ (x,1)\sim (\varphi(x),0).$$ It has a natural epimorphism $\pi_1M^3\to \mathbb{Z}$, corresponding to the projection of the fibration $M^3\to S^1$. The induced map on the monodromy is denoted by $$\varphi_*\colon X(\Sigma,\mathrm{PSL}_n(\mathbb{C}))\to X(\Sigma,\mathrm{PSL}_n(\mathbb{C}))$$ and the restriction to $\pi_1\Sigma$ of characters in $X(M^3,PSL_n(\mathbb{C}))$ restrict to the fixed point set of $X(\Sigma,\mathrm{PSL}_n(\mathbb{C}))$. By Weil's theorem, the map induced in $H^1(\Sigma;\operatorname{Ad}\rho)$ can be interpreted as the differential $d\varphi_*$. Thus, using Proposition [\[prop:MapTorus\]](#prop:MapTorus){reference-type="ref" reference="prop:MapTorus"}, the twisted polynomial is $$\det (d \varphi_*- t \operatorname{Id}).$$ Its evaluation at $t=1$ vanishes because $H^*(M^3;\operatorname{Ad}\rho)\neq 0$. The polynomial is divisible by $(t-1)^n$, corresponding to the invariant curve $\gamma=\partial \Sigma$, as $\dim 
H^1(\gamma; \operatorname{Ad}\rho)=n$. An argument using the exact sequences and the basis of homology yields the following result:

::: prop
[@Memoirs; @KitayamaTerashima15] []{#prop:bundleadj label="prop:bundleadj"} If $M^3$ is a punctured surface bundle, and $\gamma$ the boundary of the fibre. Then $$\mathcal{T}_{M,\gamma} =\left.\frac{\det (d \varphi_*- t \operatorname{Id})}{(t-1)^{n}}\right\vert_{t=1}.$$
:::

This result is very useful for computing the torsion, it allows to obtain it from the variety of characters or moduli spaces without knowing the representation. For instance Kitayama and Terashima use cluster algebras to compute it [@KitayamaTerashima15]. In Subsection [\[subsection:eight\]](#subsection:eight){reference-type="ref" reference="subsection:eight"} we recall the method of [@Memoirs] to compute it.
