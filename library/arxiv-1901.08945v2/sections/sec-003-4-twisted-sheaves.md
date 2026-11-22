---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-003-4-twisted-sheaves
section_title: "Twisted sheaves"
section_number: 4
pages: 16-20
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.959
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
[]{#sec:quasi-coher-sheav label="sec:quasi-coher-sheav"} In this section, $\Delta$ will denote a diagonalizable group scheme (over $\mathop{\mathrm{Spec}}\mathbb{Z}$) with character group $A := \mathop{\mathrm{Hom}}_{\mathop{\mathrm{Spec}}\mathbb{Z}}(\Delta, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$. Recall that $A$ is a finitely generated abelian group. We will usually use multiplicative notation for $A$, except when we identify it with something like the additive group of $\mathbb{Z}$.

Let $S$ be an algebraic stack. By a $\Delta$-gerbe on $S$ we mean a $\Delta_S$-gerbe on $S$. Fix a $\Delta$-gerbe $\alpha\colon X \to S$. Note that $X$ is isomorphic to $\mathop{\mathrm{B}}\Delta_S$ locally on $S$. In particular, $X$ is an algebraic stack, and it is reasonable to talk about quasi-coherent sheaves on $X$.

::: remark
[]{#rem-gerbe-ff label="rem-gerbe-ff"} Let $\alpha\colon X \to S$ be a $\Delta$-gerbe. Note that the structure morphism $\alpha$ is smooth and surjective. Indeed, this is true for any algebraic gerbe [@bergh2017 Proposition A.2]. Moreover, assume that $Y$ is a $\Delta'$-gerbe over $S$ and let $\rho\colon X \to Y$ be a morphism over $S$ with induced morphism $\varphi\colon \Delta_S \to \Delta'_S$ on bands. Then $\rho$ factors as $X \to X\times\mathop{\mathrm{B}}\Delta' \to \varphi_*X \cong Y$ by Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"} combined with Proposition [\[gerbe-functorial-group\]](#gerbe-functorial-group){reference-type="ref" reference="gerbe-functorial-group"}. Note that the first morphism in the factorization is a $\Delta'$-torsor and that the second morphism is a gerbe banded by $\Delta$. In particular, the morphism $\rho$ is faithfully flat. See also Remark [\[rem-gerbe-concentrated\]](#rem-gerbe-concentrated){reference-type="ref" reference="rem-gerbe-concentrated"} for cohomological properties of $\rho$.
:::

::: definition
[]{#def-homogeneous-sheaf label="def-homogeneous-sheaf"} Let $\mathcal{F}$ be an object in ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{fppf}}, \mathcal{O}_X)$, and let $\chi\colon \Delta_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$ be a character. Note that $\Delta_X$ acts on $\mathcal{F}$ from the right via the inertial action [\[eq-inertial-action\]](#eq-inertial-action){reference-type="eqref" reference="eq-inertial-action"} and the banding (see Definition [\[def-banding\]](#def-banding){reference-type="ref" reference="def-banding"}) of $X$, and that ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ acts on $\mathcal{F}$ from the left via the inclusion ${\ensuremath{\mathbb{G}_{\operatorname{m},X}}} \subset \mathcal{O}_X$. We define the *$\chi$-homogeneous subsheaf* $\mathcal{F}_\chi$ of $\mathcal{F}$ by $$\label{eq:chi-subsheaf}
  \mathcal{F}_\chi = \{s \in \mathcal{F} \mid 
  \text{$s\cdot\gamma = \chi(\gamma)s$ for all $\gamma
  \in \Delta_X$}\}.$$ An object $\mathcal{F}$ of ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{fppf}}, \mathcal{O}_X)$ is called *$\chi$-homogeneous* or *homogeneous of degree $\chi$* provided that $\mathcal{F} = \mathcal{F}_\chi$, and we denote the full subcategory of $\chi$-homogeneous objects in ${\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{fppf}}, \mathcal{O}_X)$ by ${\ensuremath{\operatorname{Qcoh}}}_\chi(X_{\operatorname{fppf}}, \mathcal{O}_X)$.
:::

::: remark
[]{#rem:def-Qcoh-chi label="rem:def-Qcoh-chi"} Note that the expression [\[eq:chi-subsheaf\]](#eq:chi-subsheaf){reference-type="eqref" reference="eq:chi-subsheaf"} does not make sense in the lisse--étale topos unless $\Delta_X$ is smooth over $X$. When we talk about homogeneous sheaves in ${\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$, we implicitly transport the subcategory ${\ensuremath{\operatorname{Qcoh}}}_\chi(X_{\operatorname{fppf}}, \mathcal{O}_X) \subset {\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{fppf}}, \mathcal{O}_X)$ to a subcategory ${\ensuremath{\operatorname{Qcoh}}}_\chi(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X) \subset {\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$ under the equivalence obtained by restriction. We will usually simply write ${\ensuremath{\operatorname{Qcoh}}}_\chi(X)$ for any of these subcategories.
:::

::: definition
[]{#def:twisted label="def:twisted"} Let $\alpha\colon X \to S$ be a ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbe and let ${\operatorname{id}}\colon {\ensuremath{\mathbb{G}_{\operatorname{m}}}}\to {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ be the identity character. An *$\alpha$-twisted quasi-coherent sheaf on $S$* is simply an object of ${\ensuremath{\operatorname{Qcoh}}}_{\operatorname{id}}(X)$. We will often use the notation ${\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S)$ instead of ${\ensuremath{\operatorname{Qcoh}}}_{\operatorname{id}}(X)$.
:::

::: remark
[]{#rem-twisted-abuse label="rem-twisted-abuse"} Since the category ${\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S)$, up to equivalence, obviously depends only on the class of $\alpha$ in $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$, we will sometimes abuse notation and write ${\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S)$ even if $\alpha$ is just a cohomology class in $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$.
:::

::: remark
[]{#rem-twisted-2-cocycle label="rem-twisted-2-cocycle"} Twisted sheaves may also be described using 2-cocycles. This approach was taken by Căldăraru in [@caldararu2000 Definition 1.2.1]. That his definition is essentially equivalent to the definition above was proved by Lieblich in [@lieblich2004 Proposition 2.1.3.11].
:::

We now give a precise formulation of the well-known fact that any quasi-coherent sheaf on a suitable gerbe decomposes into its homogeneous subsheaves (c.f. [@lieblich2004 Proposition 2.2.1.6]).

::: theorem
[]{#t-qc-gerbe-split label="t-qc-gerbe-split"} Let $S$ be an algebraic stack and let $\alpha\colon X \to S$ be a gerbe banded by a diagonalizable group $\Delta$. Then ${\ensuremath{\operatorname{Qcoh}}}_\chi(X)$ is a Serre subcategory (see [@stacks-project [Tag 02MO](http://stacks.math.columbia.edu/tag/02MO)]) of ${\ensuremath{\operatorname{Qcoh}}}(X)$ for any character $\chi$ of $\Delta_S$, and taking the coproduct gives an equivalence $$\label{eq-eq-qc-gerbe}
    \prod_{\chi \in A}{\ensuremath{\operatorname{Qcoh}}}_\chi(X) \xrightarrow[{}]{\sim}{\ensuremath{\operatorname{Qcoh}}}(X),
    \qquad
    (\mathcal{F}_\chi)_\chi \mapsto \bigoplus_{\chi \in A}
    \mathcal{F}_\chi,$$ of abelian categories, where $A$ denotes the character group of $\Delta$.

Furthermore, assume that $\mathcal{F}_\chi$ and $\mathcal{G}_\psi$ are quasi-coherent $\mathcal{O}_X$-modules which are homogeneous for $\Delta_S$-characters $\chi$ and $\psi$, respectively. Then the quasi-coherent $\mathcal{O}_X$-modules $$\label{eq-qc-monoidal}
    \mathcal{F}_\chi \otimes \mathcal{G}_\psi, \qquad
    {\mathcal{H}{om}}(\mathcal{G}_\psi, \mathcal{F}_\chi)$$ are $\chi\psi$- and $\chi\psi^{-1}$-homogeneous, respectively.
:::

::: proof
*Proof.* Throughout the proof, we work with sheaves in $X_{\operatorname{fppf}}$, which we view as the topos of sheaves on the site of affine schemes over $X$. Fix a quasi-coherent sheaf $\mathcal{F}$ of $\mathcal{O}_X$-modules.

Let $x$ be an object of $X$ lying over an affine scheme $\mathop{\mathrm{Spec}}A$. Then $\mathcal{F}(x)$ is an $A$-module with an $A$-linear right action of the group $\Delta(A):=\Delta(\mathop{\mathrm{Spec}}A)$ coming from the inertial action via the banding. Given a morphism $f \colon y \rightarrow x$ in $X$ lying over a morphism $\mathop{\mathrm{Spec}}{\varphi}\colon \mathop{\mathrm{Spec}}B \rightarrow\mathop{\mathrm{Spec}}A$, the corresponding morphism $\mathcal{F}(f) \colon \mathcal{F}(x) \rightarrow\mathcal{F}(y)$ is equivariant with respect to $\Delta(A) \rightarrow\Delta(B)$. Moreover, since $\mathcal{F}$ is quasi-coherent, it induces an isomorphism $B \otimes_{{\varphi}, A} 
  \mathcal{F}(x) \xrightarrow[{}]{\sim}\mathcal{F}(y)$ of $B$-modules.

By restricting $\mathcal{F}$ to $\mathop{\mathrm{Spec}}A$ along $x\colon \mathop{\mathrm{Spec}}A \to X$ (see [@stacks-project [Tag 06W9](http://stacks.math.columbia.edu/tag/06W9)]), we see that the $A$-module $\mathcal{F}(x)$ can be viewed as a right representation of the diagonalizable $A$-group scheme $\Delta_{\mathop{\mathrm{Spec}}A}$ in the sense of [@Jantzen I.2.7]. Hence it decomposes as $\mathcal{F}(x)=\bigoplus_{\chi \in A}\mathcal{F}(x)_\chi$ by [@Jantzen I.2.11].

If the object $x$ varies, all these decompositions are compatible and combine into the decomposition $\mathcal{F}=\bigoplus_{\chi \in A} \mathcal{F}_\chi$ where $\mathcal{F}_\chi$ is the $\chi$-homogeneous subsheaf of $\mathcal{F}$. This shows that the functor [\[eq-eq-qc-gerbe\]](#eq-eq-qc-gerbe){reference-type="eqref" reference="eq-eq-qc-gerbe"} is essentially surjective. Similarly, we get a decomposition of morphisms between pairs of quasi-coherent modules (cf. [@Jantzen I.2.11]), which shows that [\[eq-eq-qc-gerbe\]](#eq-eq-qc-gerbe){reference-type="eqref" reference="eq-eq-qc-gerbe"} is fully faithful. Moreover, any $\Delta_S$-character $\chi$ clearly gives an exact functor $\mathcal{F} \mapsto \mathcal{F}_\chi$. In particular, ${\ensuremath{\operatorname{Qcoh}}}_\chi(X)$ is a Serre subcategory of ${\ensuremath{\operatorname{Qcoh}}}(X)$.

The statement that the tensor product of a $\chi$-homogeneous quasi-coherent module with a $\psi$-homogeneous quasi-coherent module is $(\chi+\psi)$-homogeneous is obvious, and the corresponding claim for the internal Hom-functor is then a formal consequence. ◻
:::

::: remark
[]{#rem-coprod-prod label="rem-coprod-prod"} Note that the canonical morphism $\bigoplus_{\chi\in A} \mathcal{F}_\chi
\to
\prod_{\chi\in A} \mathcal{F}_\chi$ is an isomorphism even if the character group $A$ is not finite. Here the product is taken in ${\ensuremath{\operatorname{Qcoh}}}(X)$. This is a simple consequence of the equivalence [\[eq-eq-qc-gerbe\]](#eq-eq-qc-gerbe){reference-type="eqref" reference="eq-eq-qc-gerbe"} in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}.
:::

::: proposition
[]{#p:pull-back-grading label="p:pull-back-grading"} Let $S$ be an algebraic stack and $\alpha\colon X \to S$ a gerbe banded by a diagonalizable group $\Delta$. Let $f\colon T \to S$ be a morphism of algebraic stacks, and let $g\colon Y \to X$ denote the base change of $f$ along $\alpha$. Then the functors $$g^*\colon {\ensuremath{\operatorname{Qcoh}}}(X) \to {\ensuremath{\operatorname{Qcoh}}}(Y), \qquad
g_*\colon {\ensuremath{\operatorname{Qcoh}}}(Y) \to {\ensuremath{\operatorname{Qcoh}}}(X)$$ respect the decompositions of ${\ensuremath{\operatorname{Qcoh}}}(X)$ and ${\ensuremath{\operatorname{Qcoh}}}(Y)$ into homogeneous objects given in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}.
:::

::: proof
*Proof.* As a formal consequence of adjunction, it is enough to verify that one of the functors $g^*$ and $g_*$ preserves the decomposition. The functor $g^*$ is obtained by restriction of the functor $g^*\colon{\ensuremath{\operatorname{Mod}}}(S_{\operatorname{fppf}}, \mathcal{O}_S) \to {\ensuremath{\operatorname{Mod}}}(T_{\operatorname{fppf}}, \mathcal{O}_T)$, which in turn is just given by restriction of the topos $S_{\operatorname{fppf}}$. In this setting the statement is obvious from the definition of a homogeneous sheaf (see Definition [\[def-homogeneous-sheaf\]](#def-homogeneous-sheaf){reference-type="ref" reference="def-homogeneous-sheaf"}). ◻
:::

::: proposition
[]{#t:equivalence-epi label="t:equivalence-epi"} Let $X$ and $X'$ be gerbes over $S$ banded by diagonalizable groups $\Delta$ and $\Delta'$, respectively, and let $\rho\colon X \to X'$ be a morphism over $S$ with induced morphism $\varphi\colon \Delta_S \to \Delta'_S$ on the bands. Fix a character $\chi'\colon \Delta'_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$, and let $\chi =
  \chi' \circ \varphi$. Then the pull-back functor $\rho^*$ takes $\chi'$-homogeneous objects to $\chi$-homogeneous objects and induces an equivalence $$\label{eq-rho-restricted}
    \rho^*\colon 
    {\ensuremath{\operatorname{Qcoh}}}_{\chi'}(X') \xrightarrow[{}]{\sim}{\ensuremath{\operatorname{Qcoh}}}_{\chi}(X)$$ of categories. In particular, if $X' = S$ then $\rho^*\colon {\ensuremath{\operatorname{Qcoh}}}(S) \to {\ensuremath{\operatorname{Qcoh}}}(X)$ is fully faithful with essential image consisting of those objects that are homogeneous for the trivial character.
:::

::: proof
*Proof.* By a similar argument as in the proof of Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"}, we see that $\rho^*$ takes $\chi'$-homogeneous objects to $\chi$-homogeneous objects. First we note that the special case in the last sentence in the statement of the proposition follows directly from Proposition [\[p-gerbe-pb-ff\]](#p-gerbe-pb-ff){reference-type="ref" reference="p-gerbe-pb-ff"}.

In the general case, we consider the fiber product $X\times_S X'$ and its projections $p$ and $q$ to $X$ and $X'$. Note that $X\times_S X'$ is a $\Delta\times\Delta'$-gerbe over $S$ and that $p$ and $q$ induce the projections to $\Delta$ respectively $\Delta'$ on the bands.

The projection $p$ is a gerbe banded by the kernel of the projection $\Delta\times\Delta' \to \Delta$, which is isomorphic to $\Delta'$. In particular, $p^*$ is fully faithful with essential image consisting of sheaves on which this kernel acts trivially. Similar statements hold for $q$. Hence it follows from the decomposition in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"} that we get equivalences $$\begin{aligned}
  \label{eq:equiv-p}
  p^* \colon {\ensuremath{\operatorname{Qcoh}}}_\chi(X)
  & \rightleftarrows {\ensuremath{\operatorname{Qcoh}}}_{(\chi,e')}(X \times_S X'/S)\colon p_*,\\
  \label{eq:equiv-q}
  q^* \colon {\ensuremath{\operatorname{Qcoh}}}_{\chi'}(X')
  & \rightleftarrows {\ensuremath{\operatorname{Qcoh}}}_{(e, \chi')}(X \times_S X'/S)\colon q_*,
\end{aligned}$$ where $e$ and $e'$ denote the trivial characters of $\Delta$ and $\Delta'$, respectively.

Note that the gerbe $p$ has a trivialization $\tau = ({\operatorname{id}}, \rho)$. In particular, there exists a line bundle $\mathcal{L}$ on $X\times_S X'$ such that

1.  []{#it-cond-1 label="it-cond-1"} $\mathcal{L}$ is $\chi'$-homogeneous with respect to the decomposition induced by $p$;

2.  []{#it-cond-2 label="it-cond-2"} $\tau^*\mathcal{L} \cong \mathcal{O}_X$.

Since $\mathcal{L}$ is a line bundle, it must also be homogeneous for some character $(\psi, \psi')$ of $(\Delta\times\Delta')_S$ with respect to the gerbe $X\times_S X' \to S$. By [\[it-cond-1\]](#it-cond-1){reference-type="ref" reference="it-cond-1"}, we have $\psi' = \chi'$. Furthermore, since $\tau$ induces the morphism $({\operatorname{id}}, \varphi)$ on bands, we have $\tau^*\mathcal{L} \in {\ensuremath{\operatorname{Qcoh}}}_{\psi\chi}(X)$. This forces $\psi = \chi^{-1}$ by [\[it-cond-2\]](#it-cond-2){reference-type="ref" reference="it-cond-2"}, so $\mathcal{L} \in {\ensuremath{\operatorname{Qcoh}}}_{(\chi^{-1}, \chi')}(X\times_S X'/S)$. In particular, it follows from the equivalences [\[eq:equiv-p\]](#eq:equiv-p){reference-type="eqref" reference="eq:equiv-p"} and [\[eq:equiv-q\]](#eq:equiv-q){reference-type="eqref" reference="eq:equiv-q"} and the statement about the monoidal structure in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"} that we get an equivalence $$p_*(\mathcal{L}^\vee\otimes q^*(-))\colon {\ensuremath{\operatorname{Qcoh}}}_{\chi'}(X') \xrightarrow[{}]{\sim}{\ensuremath{\operatorname{Qcoh}}}_{\chi}(X).$$ Furthermore, the restriction of the natural transformation $$\begin{gathered}
p_*(\mathcal{L}^\vee\otimes q^*(-)) \cong \tau^*p^*p_*(\mathcal{L}^\vee\otimes q^*(-)) \to\\
\tau^*(\mathcal{L}^\vee\otimes q^*(-)) \cong \tau^*(\mathcal{L}^\vee)\otimes \tau^*q^*(-) \cong \rho^*
\end{gathered}$$ to ${\ensuremath{\operatorname{Qcoh}}}_{\chi'}(X')$ is an isomorphism, which concludes the proof. ◻
:::

Now the following corollaries are easy consequences of Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}, Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"} and Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}.

::: corollary
[]{#cor:twisted-power label="cor:twisted-power"} Let $S$ be an algebraic stacks and let $\alpha\colon X \to S$ be a gerbe banded by $\Delta$, and choose a character $\chi\colon \Delta_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$. Then we have an equivalence $$\label{eq-pb-character}
{\ensuremath{\operatorname{Qcoh}}}_{\chi_*\alpha}(S)\cong {\ensuremath{\operatorname{Qcoh}}}_\chi(X)$$ of categories, where $\chi_*\alpha$ is defined as in Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"}. In the particular case when $\Delta = {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$, this gives the equivalence $$\label{eq-pb-power}
{\ensuremath{\operatorname{Qcoh}}}_{\alpha^d}(S)\cong {\ensuremath{\operatorname{Qcoh}}}_{d}(X)$$ for any $d \in \mathbb{Z}$, where $\alpha^d$ is defined as in Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"}.
:::

::: proof
*Proof.* The equivalence [\[eq-pb-character\]](#eq-pb-character){reference-type="eqref" reference="eq-pb-character"} is the special case of Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"} where we take $\rho$ to be $X \to \chi_* X$ as in Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"}. The equivalence [\[eq-pb-power\]](#eq-pb-power){reference-type="eqref" reference="eq-pb-power"} is the special case of [\[eq-pb-character\]](#eq-pb-character){reference-type="eqref" reference="eq-pb-character"}, where we take $\chi = p_n$ as in Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"}. ◻
:::

::: corollary
[]{#cor:twisted-tensor label="cor:twisted-tensor"} Let $S$ be an algebraic stack and let $\alpha\colon X \to S$ and $\beta\colon Y \to S$ be ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbes. Then the tensor product and the internal Hom-functor on ${\ensuremath{\operatorname{Qcoh}}}(X\times_S Y)$ induce functors $$\begin{aligned}
\otimes & \colon {\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S) \times {\ensuremath{\operatorname{Qcoh}}}_{\beta}(S) \to {\ensuremath{\operatorname{Qcoh}}}_{\alpha\beta}(S), \\
{\mathcal{H}{om}}& \colon {\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S)^{\operatorname{op}}\times {\ensuremath{\operatorname{Qcoh}}}_{\beta}(S)
\to {\ensuremath{\operatorname{Qcoh}}}_{\alpha^{-1}\beta}(S).
\end{aligned}$$ Furthermore, if $f\colon T \to S$ is an arbitrary morphism of algebraic stacks, then we get an induced pair of adjoint functors $$f^* \colon {\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S) \to {\ensuremath{\operatorname{Qcoh}}}_{f^*\alpha}(T),
  \qquad
  f_* \colon {\ensuremath{\operatorname{Qcoh}}}_{f^*\alpha}(T) \to {\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S).$$ Recall our conventions regarding $f_*$ and ${\mathcal{H}{om}}$ from Notation [\[not-sheaf-op\]](#not-sheaf-op){reference-type="ref" reference="not-sheaf-op"}.
:::

::: proof
*Proof.* The product $X\times_S Y$ has the structure of a ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}\times {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbe such that the projections on the factors $X$ and $Y$ induce the projections on the factors on the bands. By applying Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"} to the two projections ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}\times {\ensuremath{\mathbb{G}_{\operatorname{m}}}}\to {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$, we get equivalences $${\ensuremath{\operatorname{Qcoh}}}_{\alpha}(S) \cong {\ensuremath{\operatorname{Qcoh}}}_{(1, 0)}(X\times_S Y), \qquad
{\ensuremath{\operatorname{Qcoh}}}_{\beta}(S) \cong {\ensuremath{\operatorname{Qcoh}}}_{(0, 1)}(X\times_S Y),$$ where we have identified the character group of ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ with $\mathbb{Z}$. By applying Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"} to the multiplication and inversion maps given in Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"}, we obtain the equivalences $${\ensuremath{\operatorname{Qcoh}}}_{\alpha\beta}(S) \cong {\ensuremath{\operatorname{Qcoh}}}_{(1, 1)}(X\times_S Y), \qquad
{\ensuremath{\operatorname{Qcoh}}}_{\alpha^{-1}\beta}(S) \cong {\ensuremath{\operatorname{Qcoh}}}_{(-1, 1)}(X\times_S Y),$$ respectively. Now the functors $\otimes$ and ${\mathcal{H}{om}}$ are obtained from the monoidal structure of ${\ensuremath{\operatorname{Qcoh}}}(X\times_S Y)$ described in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}. The statement about the functors $f^*$ and $f_*$ is an obvious consequence of Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"}. ◻
:::
