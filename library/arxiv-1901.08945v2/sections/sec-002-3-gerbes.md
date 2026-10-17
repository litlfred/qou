---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-002-3-gerbes
section_title: "Gerbes"
section_number: 3
pages: 13-16
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.951
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
[]{#sec:gerbes-and-twisted label="sec:gerbes-and-twisted"} In this section, we collect some results from the theory on gerbes, bandings by abelian groups and the relation to cohomology. Throughout the section, $S$ will be an arbitrary algebraic stack. By a *stack* we mean a, not necessarily algebraic, stack in groupoids over the big *fppf* site of schemes over $S$. The symbol $\Delta$ will always denote an abelian group in $S_{\operatorname{fppf}}$. Later on, we will specialize to the situation when $\Delta$ is a diagonalizable group. Accordingly, we will use multiplicative notation for $\Delta$ and its cohomology groups $\mathop{\mathrm{H}}^i(S_{\operatorname{fppf}}, \Delta)$.

::: definition
A *gerbe* over $S$ is a stack (in groupoids) $\alpha\colon X \to S$ satisfying the following conditions.

1.  The diagonal $X \to X\times_S X$ is an epimorphism (see [@lmb2000 Definition 3.6]).

2.  []{#def-gerbe-structure label="def-gerbe-structure"} The structure morphism $\alpha\colon X \to S$ is an epimorphism.

A gerbe is called *trivial* if the structure morphism in [\[def-gerbe-structure\]](#def-gerbe-structure){reference-type="ref" reference="def-gerbe-structure"} splits.
:::

The prototypical example of a gerbe is the *classifying stack* $\mathop{\mathrm{B}}G$ for a group $G$ in $S_{\operatorname{fppf}}$. In fact, any gerbe can be viewed as an *fppf*-form of a classifying stack.

For any stack $\alpha\colon X \to S$, we may consider its *inertia stack* $I_{X/S} \to X$ ([@stacks-project [Tag 034I](http://stacks.math.columbia.edu/tag/034I)]), which is a group object in $X_{\operatorname{fppf}}$. Its points over a morphism $x \colon U \to X$ are simply the 2-automorphisms $\gamma$ of $x$ mapping to the identity under the composition $\alpha \circ x$. Any object $\mathcal{F}$ in $X_{\operatorname{fppf}}$ is endowed with a canonical right action by the inertia $I_{X/S}$, called the *inertial action*. Explicitly, it is given on sections over $x$ by $$\label{eq-inertial-action}
\mathcal{F}(x)\times I_{X/S}(x) \to \mathcal{F}(x),\qquad
(s, \gamma) \mapsto \mathcal{F}(\gamma)(s).$$ We recall the following fundamental fact about the inertial action.

::: proposition
[]{#p-gerbe-pb-ff label="p-gerbe-pb-ff"} Let $\alpha\colon X \to S$ be a gerbe. Then the functor $\alpha^{*}\colon S_{\operatorname{fppf}}\to X_{\operatorname{fppf}}$ is fully faithful with essential image consisting of sheaves on which the inertia $I_{X/S}$ acts trivially.
:::

::: proof
*Proof.* See for instance [@lieblich2004 Lemma 2.1.1.17]. ◻
:::

::: definition
A gerbe $\alpha\colon X \to S$ is called *abelian* if the inertia group $I_{X/S} \to X$ is abelian. We denote the full subcategory of stacks over $S$ which are abelian gerbes by ${\mathcal{A}b\mathcal{G}erbe}(S)$.
:::

The inertia acts on itself by conjugation. In particular, Proposition [\[p-gerbe-pb-ff\]](#p-gerbe-pb-ff){reference-type="ref" reference="p-gerbe-pb-ff"} shows that the inertia group of an abelian gerbe $\alpha\colon X \to S$ descends to an abelian group object in $S_{\operatorname{fppf}}$, namely $\alpha_* I_{X/S}$. Furthermore, given any 1-morphism $\rho\colon X \to Y$ of stacks over $S$, we get an induced group homomorphism $I_{X/S} \to \rho^*I_{Y/S}$ in $X_{\operatorname{fppf}}$, and if $X$ and $Y$ are abelian gerbes, this descends to a group homomorphism in $S_{\operatorname{fppf}}$. This association gives a functor $$\label{eq-band-functor}
\mathop{\mathrm{Band}}\colon {\mathcal{A}b\mathcal{G}erbe}(S) \to {\mathcal{A}b\mathcal{G}roup}(S)$$ to the category of abelian group objects in $S_{\operatorname{fppf}}$.

::: definition
[]{#def-banding label="def-banding"} Let $\Delta$ be an abelian group object in $S_{\operatorname{fppf}}$. The essential fiber of the functor [\[eq-band-functor\]](#eq-band-functor){reference-type="eqref" reference="eq-band-functor"} over $\Delta$ is called the *category of gerbes banded by $\Delta$* or *of $\Delta$-gerbes*. Explicitly, a $\Delta$-gerbe is given by a pair $(\alpha, \iota)$ where $\alpha\colon X \to S$ is an abelian gerbe and $\iota\colon \Delta \xrightarrow{\sim} \alpha_*I_{X/S}$ is a group isomorphism called a *banding* of $\alpha$ by $\Delta$. The group $\Delta$ is called the band of $(\alpha,\iota)$. A morphism of $\Delta$-gerbes is simply a morphism of stacks such that corresponding morphism on inertia induces the identity on $\Delta$ via the bandings. By abuse of notation, we usually denote a $\Delta$-gerbe $(\alpha, \iota)$ by $\alpha$ or even $X$.
:::

::: remark
Giraud introduces a more general notion of banding applying to non-abelian gerbes [@giraud1971 Chapter IV]. We will not need this, more complicated, theory here.
:::

Note that a 1-morphism of gerbes over $S$ is always an epimorphism ([@lmb2000 Lemma 3.17]), and that it is an isomorphism if and only if it induces an isomorphism on inertia. In particular, the category of $\Delta$-gerbes is a 2-groupoid.

::: example
[]{#ex:simple-gerbes label="ex:simple-gerbes"} Let $S$ be an algebraic stack, and let $\Delta$ and $\Delta'$ be abelian groups in $S_{\operatorname{fppf}}$.

1.  The classifying stack $\mathop{\mathrm{B}}\Delta$ is endowed with a canonical structure of $\Delta$-gerbe.

2.  Given a pair of abelian gerbes $X$ and $X'$ over $S$, banded by $\Delta$ and $\Delta'$, respectively, the product $X\times_S X'$ has a naturally defined banding by $\Delta\times \Delta'$.
:::

The following example illustrates that it is very natural to consider gerbes over genuine algebraic stacks.

::: example
[]{#ex-gerbes label="ex-gerbes"} Let $S$ be an algebraic stack. Assume that we have a central extension $1 \to \Delta \to G \to H \to 1$ of groups in $S_{\operatorname{fppf}}$. Then the induced morphism of classifying stacks $\mathop{\mathrm{B}}G \to \mathop{\mathrm{B}}H$ has a canonical structure of a $\Delta$-gerbe. The following examples are two important special cases with $S = \mathop{\mathrm{Spec}}\mathbb{Z}$.

1.  []{#it-universal-projective label="it-universal-projective"} The morphism $G \to H$ is the quotient map $\mathop{\mathrm{GL}}_n \to \mathop{\mathrm{PGL}}_n$. In this case we obtain a ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbe $\mathop{\mathrm{B}}\mathop{\mathrm{GL}}_n \to
    \mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$.

2.  []{#it-universal-root label="it-universal-root"} The morphism $G \to H$ is the morphism ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}\to {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ given by $x \mapsto x^n$. In this case the corresponding $\mu_n$-gerbe $\mathop{\mathrm{B}}{\ensuremath{\mathbb{G}_{\operatorname{m}}}}\to \mathop{\mathrm{B}}{\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ can be thought of as the $n$-th root stack of the universal line bundle $[{\mathbb{A}}_1/{\ensuremath{\mathbb{G}_{\operatorname{m}}}}]$ on $\mathop{\mathrm{B}}
    {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ (cf. [@cadman2007 Definition 2.2.6]).
:::

Next we discuss functoriality of banded gerbes with respect to change of group.

::: construction
[]{#cons-gerbe-pf label="cons-gerbe-pf"} Let $\varphi\colon \Delta \to \Delta'$ be a homomorphism of abelian group objects in $S$, and let $\alpha\colon X \to S$ be a gerbe banded by $\Delta$. We construct a gerbe $\varphi_*\alpha\colon \varphi_*  X \to S$ banded by $\Delta'$ together with a morphism $$\label{eq-gerbe-pf}
\rho \colon X \to \varphi_*X$$ of gerbes over $S$ inducing the homomorphism $\varphi$ on the bands as follows.

Consider $X \times \mathop{\mathrm{B}}\Delta'$ with its natural banding by $\Delta \times \Delta'$. We define $\varphi_*X$ as the *rigidification* (see [@aov2008 Appendix A]) of $X \times \mathop{\mathrm{B}}\Delta'$ in the kernel of the epimorphism $\Delta \times \Delta' \to \Delta'$ given by $(a, b) \mapsto \varphi(a) b$. The morphism $\rho$ is the composition of the obvious map $X \to X\times \mathop{\mathrm{B}}\Delta'$ followed by the rigidification map.
:::

The construction above shows that given a gerbe banded by $\Delta$, any morphism $\varphi\colon \Delta \to \Delta'$ lifts to a morphism of banded gerbes. The following proposition, which we surprisingly could not find in the literature, shows that this lift is essentially unique. In particular, Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"} is functorial in a weak sense.

::: proposition
[]{#gerbe-functorial-group label="gerbe-functorial-group"} Let $\Delta$ be an abelian group in $S_{\operatorname{fppf}}$, and let $\alpha\colon X \to S$ be a gerbe banded by $\Delta$. Then the obvious functor $$\mathop{\mathrm{Band}}_{X/} \colon {\mathcal{A}b\mathcal{G}erbe}(S)_{X/} \to {\mathcal{A}b\mathcal{G}roup}(S)_{\Delta/}$$ from the category of abelian gerbes over $S$ under $X$ to the category of abelian groups in $S_{\operatorname{fppf}}$ under $\Delta$ is an equivalence of categories.
:::

::: proof
*Proof.* Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"} shows that the functor $\mathop{\mathrm{Band}}_{X/}$ is essentially surjective on objects. Let $\rho\colon X \rightarrow Y$ and $\rho'\colon X \rightarrow Y'$ be objects of ${\mathcal{A}b\mathcal{G}erbe}(S)_{X/}$, and denote their images in ${\mathcal{A}b\mathcal{G}roup}(S)_{\Delta/}$ by $\varphi\colon \Delta \to \Gamma$ and $\varphi'\colon \Delta \to \Gamma'$, respectively. We need to show that $$\label{eq-band-equivalence}
\mathop{\mathrm{Hom}}_{X/}(\rho, \rho') \to \mathop{\mathrm{Hom}}_{\Delta/}(\varphi, \varphi')$$ is and equivalence of categories. To do so, we first note that [\[eq-band-equivalence\]](#eq-band-equivalence){reference-type="eqref" reference="eq-band-equivalence"} is functorial in $S$, and that we in fact have a morphism of stacks $$\label{eq-band-stacky-equivalence}
\Phi\colon {\mathcal{H}{om}}_{X/}(\rho, \rho') \to {\mathcal{H}{om}}_{\Delta/}(\varphi, \varphi')$$ over $S$. Explicitly, this morphism is constructed as the canonical map in the diagram $$\label{eq-big-and-scary}
\xymatrix{
{\mathcal{H}{om}}_{\Delta/}(\varphi, \varphi')\ar[ddd]\ar[rrr] & & & S \ar[ddd]^{\varphi'}\\
& {\mathcal{H}{om}}_{X/}(\rho, \rho')\ar[d]\ar[r]\ar[ul]_\Phi & S\ar[ur]^{\operatorname{id}}\ar[d]^{\rho'} & \\
& {\mathcal{H}{om}}(Y, Y') \ar[r]^{-\circ\rho}\ar[dl] & {\mathcal{H}{om}}(X, Y')\ar[dr] & \\
{\mathcal{H}{om}}(\Gamma, \Gamma') \ar[rrr]^{-\circ\varphi} & & & {\mathcal{H}{om}}(\Delta, \Gamma'), \\
}$$ where the inner and the outer squares are cartesian.

To verify that $\Phi$ is an isomorphism, we may work locally on $S$. In particular, we may assume that the stacks $X, Y$ and $Y'$ are the classifying stacks $\mathop{\mathrm{B}}\Delta$, $\mathop{\mathrm{B}}\Gamma$ and $\mathop{\mathrm{B}}\Gamma'$, respectively. Furthermore, we may assume that the morphisms $\rho$ and $\rho'$ are given by extension of torsors along $\varphi$ and $\varphi'$, respectively. In this situation, we have ${\mathcal{H}{om}}(X, Y') \cong [{\mathcal{H}{om}}(\Delta, \Gamma')/\Gamma']$, where $\Gamma'$ acts trivially, and the map to ${\mathcal{H}{om}}(\Delta, \Gamma')$ is induced by forgetting the group action (see e.g. Abramovich *et al.* [@aov2008 Lemma 3.9(1)] and its proof). Plugging this into [\[eq-big-and-scary\]](#eq-big-and-scary){reference-type="eqref" reference="eq-big-and-scary"}, together with the similar description for ${\mathcal{H}{om}}(Y, Y')$ and the obvious descriptions for $\rho'$ and $-\circ\rho$, it becomes clear that $\Phi$ is an isomorphism. ◻
:::

::: construction
[]{#cons-gerbe-operations label="cons-gerbe-operations"} Let $\Delta$ be an abelian group in $S_{\operatorname{fppf}}$, and let $\alpha, \beta\colon X \to S$ be $\Delta$-gerbes. Denote the multiplication map on $\Delta$ by $m\colon \Delta \times \Delta \to \Delta$, and the $n$-th power map, for $n\in \mathbb{Z}$, by $p_n\colon \Delta \to \Delta$. Using Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"}, we define $$\label{eq-gerbe-mult-inverse}
\alpha\beta := m_*(\alpha \times \beta), \qquad
\alpha^n := (p_n)_*\alpha.$$
:::

Morally, Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"} gives the 2-groupoid of $\Delta$-gerbes the structure of an abelian group, a statement which presumably could be made precise by use of Proposition [\[gerbe-functorial-group\]](#gerbe-functorial-group){reference-type="ref" reference="gerbe-functorial-group"}. At least, it is clear that the set of isomorphism classes of $\Delta$-gerbes forms an abelian group.

It is easy to see that we also have functoriality with respect to change of stacks. That is, let $f\colon T \to S$ be a morphism of algebraic stacks and let $\alpha\colon X \to S$ be a $\Delta$-gerbe. Then the pull-back $f^*\alpha$ has a natural structure of $f^*\Delta$-gerbe.

::: theorem
[]{#t:gerbes-H2 label="t:gerbes-H2"} Let $S$ be an algebraic stack and let $\Delta$ be an abelian group in $S_{\operatorname{fppf}}$. Then the group $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, \Delta)$ is canonically isomorphic to the set of isomorphism classes of $\Delta$-gerbes over $S_{\operatorname{fppf}}$, with its group structure induced by the operations in Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"}. Given a $\Delta$-gerbe $\alpha$ over $S_{\operatorname{fppf}}$, we denote its class in $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, \Delta)$ by $[\alpha]$. We have the following functorial properties:

1.  Given a morphism $f\colon T \to S$ of algebraic stacks, we have $[f^*\alpha] = f^*[\alpha]$ in $H^2(T_{\operatorname{fppf}}, f^*\Delta)$.

2.  Given a homomorphism of abelian groups $\varphi\colon \Delta \to \Delta'$, we have $[\varphi_\ast \alpha] = \varphi_*[\alpha]$ in $H^2(S_{\operatorname{fppf}}, \Delta')$.
:::

::: proof
*Proof.* This is worked out in various places in [@giraud1971]. Functoriality with respect to change of groups is described in Section IV.3.1. Comparison with usual cohomology is in Section IV.3.4, and functoriality with respect to change of topos in Section V.1. ◻
:::
