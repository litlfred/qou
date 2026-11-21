---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-033-51-local-parameters-and-change-of-curve
section_title: "Local parameters and change of curve"
section_number: 5.1
pages: 39-41
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.975
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Consider $\mathfrak{h}\subset \mathfrak{sl}_{n+1}(\mathbb{C})$ the Cartan subalgebra of diagonal matrices, in particular a diagonal matrix in $\mathrm{PSL}_{n+1}(\mathbb{C})$ lies in $\exp \mathfrak{h}$.

For a generic character $\chi\in X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$, one would like to consider in a neighborhood $U$ of $\chi$: $$\label{eqn:log}
    \begin{array}{rcl}
      \log_\gamma\colon U\subset X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))&\to& \mathfrak{h}\\
      \chi_\rho & \mapsto & \log \rho(\gamma)  
    \end{array}$$ but a priori this may not be well defined. Notice that there are indeterminacies due to the action of the Weyl group (permutation of elements in the diagonal) and indeterminacies due to the complex logarithm. This motivates the following definition.

::: definition
[]{#defn:chamberreg label="defn:chamberreg"} A representation $\rho\in \hom(\pi_1M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ is *chamber regular* is there exists a peripheral element $\gamma\in\pi_1 T^2$ such that $\rho(\gamma)$ has $n+1$ different eigenvalues.
:::

In terms of Lie groups this is a regularity condition: $\rho(\pi_1T^2)$ is contained in a Cartan subgroup and in the interior of the Weyl chamber of $\mathrm{PSL}_{n+1}(\mathbb{C})$.

By [@MFP12b], the symmetric functions on the eigenvalues of $\rho(\gamma)$ define a local biholomorphism in a neighborhood of $\varrho^{n}$, hence all eigenvalues of $\rho(\gamma)$ are different in a Zariski open set. Thus:

::: remark
The set of chamber regular characters is a non-empty Zariski open subset of $X_0(M^3,\mathrm{PSL}_2(\mathbb{C}))$.
:::

For a chamber regular character and a peripheral element $\gamma\in\pi_1 T^2$, there exist a neighborhood $U \subset X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ such that the logarithm $\log_\gamma$ as in [\[eqn:log\]](#eqn:log){reference-type="eqref" reference="eqn:log"} is defined in $U$. Notice that the eigenvalues of the image of $\gamma$ do not need to be different, provided that there is an element in the peripheral group with different eigenvalues.

Next consider a nonzero element $a\in \mathfrak{h}$. Using the Killing form, we define $a^\star\in\mathfrak{h}$ to be the pairing with $a$.

::: lemma
[]{#lemma:pairing label="lemma:pairing"} Let $\rho$ be a chamber regular representation, $\gamma$ a peripheral curve and $a\in\mathfrak{h}$. Viewing $H_1(M^3;\operatorname{Ad}\rho)$ as cotangent space: $$\label{eqn:cotangent}
 a\cap[\gamma] = d ( a^\star\log_\gamma).$$
:::

This must be compared with [@Memoirs Lemma 3.20]. Before proving this lemma, let us discuss its consequences.

::: prop
[]{#prop:localparameter label="prop:localparameter"} Let $\chi_\rho\in X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ be a chamber regular character and $\gamma$ a peripheral curve. Then $\mathcal{T}_{M,\gamma}(\chi_\rho)\neq 0$ if and only if $\chi_\rho$ is a scheme reduced smooth point of $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ and $\log_{\gamma}$ is a local parameter.
:::

The proof follows easily from Lemma [\[lemma:pairing\]](#lemma:pairing){reference-type="ref" reference="lemma:pairing"}, and we just sketch it. Namely, the condition of being scheme reduced and smooth is equivalent to saying that $\dim H^1(M^3;\operatorname{Ad}\rho)=n$. By the standard arguments of the long exact sequence of the pair $(M^3, T^2)$ this implies that $\dim H^0(T^2;\operatorname{Ad}\rho)=n$ and that $\{a_1\cap [T^2],\ldots,a_n\cap [T^2]\}$ is a basis for $H^2(M^3;\operatorname{Ad}\rho)$. Then Lemma [\[lemma:pairing\]](#lemma:pairing){reference-type="ref" reference="lemma:pairing"} yields that $\{a_1\cap [\gamma],\ldots,a_n\cap [\gamma]\}$ is a basis for $H^1(M^3;\operatorname{Ad}\rho)$ iff $\log_{\gamma}$ is a local parameter.

For a chamber regular character, the condition of Proposition [\[prop:localparameter\]](#prop:localparameter){reference-type="ref" reference="prop:localparameter"} is equivalent to the notion of $\gamma$-regularity of [@KitayamaTerashima15 Definition 3.2].

Notice finally that for any non-trivial peripheral curve $\gamma$, for the lift of the holonomy $\varrho$, even if it is not chamber regular, $\mathcal{T}_{M,\gamma}(\chi_{\varrho^n})\neq 0$, by [@KitayamaTerashima15 Theorem 3.4].

::: prop
[]{#prop:change label="prop:change"} Let $\gamma_1, \gamma_ 2$ be two peripheral elements. In a Zariski open domain in $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$ $$\frac{ \mathcal{T}_{(M,\gamma_1)} }{  \mathcal{T}_{(M,\gamma_2)} }
= \pm \operatorname{J} (\log_{\gamma_1} \log_{\gamma_2}^{-1} ).$$
:::

Notice that the Jacobian $\operatorname{J} (\log_{\gamma_1} \log_{\gamma_2}^{-1} )$ is well defined generically on the distinguished component $X_0(M^3,\mathrm{PSL}_{n+1}(\mathbb{C}))$, i.e. in a non-empty open Zariski set, as $\log_{\gamma_2}$ is a local parameter in an open set. In addition, this Jacobian is independent of the parametrization of $\mathfrak{h}$, as any change of parametrization cancels in the quotient. The proof of Proposition [\[prop:change\]](#prop:change){reference-type="ref" reference="prop:change"} is straightforward from Lemma [\[lemma:pairing\]](#lemma:pairing){reference-type="ref" reference="lemma:pairing"} and the formula of change of basis in homology [\[eqn:change\]](#eqn:change){reference-type="eqref" reference="eqn:change"}.

Proposition [\[prop:change\]](#prop:change){reference-type="ref" reference="prop:change"} does not cover $\chi_{\varrho^n}$, the character of $\operatorname{Sym}^n$ of the holonomy of the complete hyperbolic structure, as it is not chamber regular. However, Corollary [\[cor:difrentdims\]](#cor:difrentdims){reference-type="ref" reference="cor:difrentdims"} and Proposition [\[prop:propslift\]](#prop:propslift){reference-type="ref" reference="prop:propslift"}([\[item:ratiocurves\]](#item:ratiocurves){reference-type="ref" reference="item:ratiocurves"}) yield: $${\mathcal{T}_{M,\gamma_2}^{n+1}(\chi_{\varrho^n})}=  \operatorname{cs}(\gamma_2,\gamma_1)^n \, 
{\mathcal{T}_{M,\gamma_1}^{n+1}(\chi_{\varrho^n})},$$ where $\operatorname{cs}(\gamma_2,\gamma_1)$ denotes the cusp shape (Definition [\[def:cs\]](#def:cs){reference-type="ref" reference="def:cs"}).

::: proof
*Proof of Lemma [\[lemma:pairing\]](#lemma:pairing){reference-type="ref" reference="lemma:pairing"}.* Assume that $\rho$ is a generic representation so that $\rho(\gamma)$ is diagonal with different eigenvalues. Let $\mathfrak{h}$ denote the Cartan algebra of diagonal matrices, and choose a non-zero element $a\in\mathfrak{h}$. In particular $a\cap\gamma\in H_1(M^3;\operatorname{Ad}\rho)$. Consider the dual of $a$: $$\begin{array}{rcl}
   a^\star\colon \mathfrak{h} & \to & \mathbb{C}\\
        h & \mapsto & B(a,h)
 \end{array}$$ where $B$ denotes the Killing form. Consider also a first order deformation $\rho_t$ of $\rho$, i.e. $$\label{eqn:firstorder}
\rho_t =(1+t\, \dot{\rho}+O(t^2))\rho$$ where $\dot\rho\colon\pi_1M^3\to \mathfrak{sl}_{n+1}(\mathbb{C})$ is a group cocycle, that we project to $H^1(M^3;\operatorname{Ad}\rho)$.

Consider finally the Kronecker pairing $$\langle\cdot \rangle\colon H^k(M^3;\operatorname{Ad}\rho)\times H_k(M^3;\operatorname{Ad}\rho)\to \mathbb{C}$$ defined as follows. Let $z\in C^k(M^3;\operatorname{Ad}\rho)$ be a cocycle, with $z\colon C_k(\widetilde M^3;\mathbb{Z})\to \mathfrak{sl}_{n+1}(\mathbb{C})$, and let $h\otimes m\in  C_k(M^3;\operatorname{Ad}\rho)$, where $h\in  \mathfrak{sl}_{n+1}(\mathbb{C})$ and $m \in C_k(\widetilde M^3;\mathbb{Z})$. At the (co-)chain level, the Kronecker pairing is $$\label{eqn:kronecker}
\langle z, h\otimes m\rangle = B(h,z(m))$$ where $B$ denotes again the Killing form. This induces a non-degenerate pairing between homology and cohomology [@Memoirs]. After all those preliminaries, to establish the lemma one must prove the following equality $$\label{eqn:pairing}
 \langle \dot\rho, a\cap[\gamma]\rangle = \left.\frac{d\phantom{t}}{dt} 
a^\star\log\rho_t(\gamma)\right\vert_{t=0} \, .$$

To prove [\[eqn:pairing\]](#eqn:pairing){reference-type="eqref" reference="eqn:pairing"}, start with the group cohomology version of [\[eqn:kronecker\]](#eqn:kronecker){reference-type="eqref" reference="eqn:kronecker"} in the current context (see [@Memoirs]): $$\label{eqn:kroneckergroup}
\langle \dot\rho , a\cap [\gamma]\rangle = B(a, \dot\rho(\gamma)).$$ From [\[eqn:firstorder\]](#eqn:firstorder){reference-type="eqref" reference="eqn:firstorder"} evaluated at $\gamma$ and taking logarithms: $$\label{eqn:loga}
 \log \rho_t(\gamma)  =   \log \rho(\gamma) + t\, \dot{\rho}(\gamma)+ 
O(t^2)) \, .$$ Then [\[eqn:pairing\]](#eqn:pairing){reference-type="eqref" reference="eqn:pairing"} follows from $a^\star$ applied to [\[eqn:loga\]](#eqn:loga){reference-type="eqref" reference="eqn:loga"}, then differentiating and applying [\[eqn:kroneckergroup\]](#eqn:kroneckergroup){reference-type="eqref" reference="eqn:kroneckergroup"} to the result. ◻
:::

Lemma [\[lemma:pairing\]](#lemma:pairing){reference-type="ref" reference="lemma:pairing"} may be related to the results of Goldman [@Goldman86].

::: example
[]{#ex:dubois label="ex:dubois"}

In [@Dubois05; @Dubois06] Dubois makes a relevant contribution of torsions as volume form on the variety of characters of a knot in $\operatorname{SU}(2)$. Here the Cartan algebra has dimension one and the logarithm of a matrix in $\operatorname{SU}(2)$ is an angle. Dubois volume form is, up to sign, $$\operatorname{vol}_{\operatorname{tor}}= \pm \frac{d\varphi_\gamma } { \mathcal{T}_{m,\gamma}}$$ where $\varphi_\gamma$ denotes the angle of the representation of the peripheral curve $\gamma$. Notice that by Proposition [\[prop:change\]](#prop:change){reference-type="ref" reference="prop:change"}, this form is independent of the choice of the peripheral curve. In [@Dubois05; @Dubois06], using Turaev's refinement of torsion and a good choice of $\varphi_\gamma$, Dubois avoids the sign indeterminacy. He also shows that it equals to a volume form defined from a Heegaard splitting, à la Johnson (Example [\[ex:Johnson\]](#ex:Johnson){reference-type="ref" reference="ex:Johnson"}). This is related to the construction of an orientation on the space of representations of Heusener [@Heusener03].

Proposition [\[prop:change\]](#prop:change){reference-type="ref" reference="prop:change"} suggests that a similar volume form can be constructed for representations in $\operatorname{SU}(n+1)$, taking a convenient parametrization of the Cartan algebra (i.e. infinitesimal angles). It remains to know also whether the variety of characters of a knot in $\operatorname{SU}(n+1)$ is non-empty and $n$-dimensional. This holds true for instance for two bridge knots. Another issue is to compute explicitly the variety of $\operatorname{SU}(n+1)$ characters for a knot.
:::
