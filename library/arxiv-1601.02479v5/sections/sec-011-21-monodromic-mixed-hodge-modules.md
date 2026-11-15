---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-011-21-monodromic-mixed-hodge-modules
section_title: "Monodromic mixed Hodge modules"
section_number: 2.1
pages: 13-20
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.97
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson– Thomas theory for Jacobi algebras and"
---
[]{#MMHMs label="MMHMs"} Let $X$ be a complex variety. Then we define as in [@Saito89; @Saito90] the category $\mathop{\mathrm{MHM}}(X)$ of mixed Hodge modules on $X$. See [@Saito1] for an overview of the theory. There is an exact functor $\mathop{\mathrm{rat}}_X\colon \mathcal{D}(\mathop{\mathrm{MHM}}(X))\rightarrow\mathcal{D}(\mathop{\mathrm{Perv}}(X))$ which takes a complex of mixed Hodge modules $\mathcal{F}$ to its underlying complex of perverse sheaves, and commutes with $f_*,f_!,f^*,f^!,\mathbb{D}_X$ and tensor product. If no remark is made to the contrary, and a non-derived target or domain category is not specified, all these functors, and indeed all functors for the entirety of this paper, will be considered as derived functors, even if their non-derived versions are well-defined. Set $\mathcal{B}$ to be the full subcategory of mixed Hodge modules on $\mathbb{A}^1$ containing those $\mathcal{F}\in\mathop{\mathrm{Ob}}(\mathop{\mathrm{MHM}}(\mathbb{A}^1))$ such that $(\mathbb{G}_m\rightarrow \mathbb{A}^1)^*\mathcal{F}$ is an admissible variation of mixed Hodge structure. Set $\mathcal{C}$ to be the full subcategory of $\mathcal{B}$ for which the objects are the admissible variations of mixed Hodge structure on $\mathbb{A}^1$. Then we define the category of *monodromic mixed Hodge structures* $\mathop{\mathrm{MMHS}}$ to be the Serre quotient $\mathcal{B}/\mathcal{C}$.

Fix $X$ and let $\mathcal{B}_X$ be the full subcategory containing those $\mathcal{F}\in\mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$ such that for each $x\in X$, the total cohomology of $(\{x\}\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)^*\mathcal{F}$ is an admissible variation of mixed Hodge structure on $\mathbb{G}_m$. Via Saito's description of $\mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$, the category $\mathcal{B}_X\subset \mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$ is the full subcategory, closed under extensions, and containing the following types of objects

1.  Mixed Hodge modules $\tilde{\mathcal{IC}}_{Y\times \mathbb{A}^1}(\mathcal{L})[\dim(Y)+1]$, where $Y\subset X$ is an irreducible closed subvariety, and $\mathcal{L}$ is a pure weight $n$ variation of Hodge structure on $Y'\times\mathbb{G}_m$, for $Y'$ an open dense subvariety of $Y_{\mathop{\mathrm{reg}}}$, and $n\in\mathbb{Z}$.

2.  Mixed Hodge modules $\tilde{\mathcal{IC}}_{Y\times \{0\}}(\mathcal{L})[\dim(Y)]$, for $\mathcal{L}$ a pure weight $n$ variation of Hodge structure on $Y'\subset Y_{\mathop{\mathrm{reg}}}\subset X$ as above.

Here $\tilde{\mathcal{IC}}_{Y\times \mathbb{A}^1}(\mathcal{L})[\dim(Y)+1]$ and $\tilde{\mathcal{IC}}_{Y\times \{0\}}(\mathcal{L})[\dim(Y)]$ are the lifts of intersection complexes to mixed Hodge modules defined in [@Saito90 Thm.3.21]. By semisimplicity, any object $\mathcal{P}$ of type (1) splits into a direct sum $\mathcal{P}\cong \mathcal{P}_1\oplus\mathcal{P}_{\neq 1}$, where $$\mathcal{P}_i=\tilde{\mathcal{IC}}_{Y\times \mathbb{A}^1}(\mathcal{L}_i)[\dim(Y)+1]$$ for $\mathcal{L}_1\subset\mathcal{L}$ the maximal pure variation of Hodge structure to have trivial monodromy around $Y\times\{0\}$, and $\mathcal{L}_{\neq 1}$ its complement.

Inside $\mathcal{B}_X$ there is a Serre subcategory $\mathcal{C}_X$ given by the full subcategory of $\mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$ containing those objects $\mathcal{F}$ such that the total cohomology of each $(\{x\}\times\mathbb{A}^1\rightarrow X\times \mathbb{A}^1)^*\mathcal{F}$ is an admissible variation of mixed Hodge structure on $\mathbb{A}^1$. It is generated under extensions by simple objects of the form $\mathcal{P}_1$.

By Schmid's rigidity theorem, the total cohomology of the restriction to the fibres $\{x\}\times\mathbb{A}^1$ of any such mixed Hodge module is constant, and $\mathcal{C}_X$ is the essential image of the functor $\uppi\hspace{0.05em}^*[1]\colon \mathop{\mathrm{MHM}}(X)\rightarrow\mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$, where $$\uppi\hspace{0.05em}\colon X\times\mathbb{A}^1\rightarrow X$$ is the projection. We define following [@KS2 Sec.7] the category of *monodromic mixed Hodge modules* $\mathop{\mathrm{MMHM}}(X)=\mathcal{B}_X/\mathcal{C}_X$. Since the objects of $\mathop{\mathrm{MMHM}}(X)$ are the objects of $\mathcal{B}_X$, we deduce that all isomorphism classes of objects in $\mathop{\mathrm{MMHM}}(X)$ are obtained from iterated extensions of simple objects of type (1) satisfying $\mathcal{L}=\mathcal{L}_{\neq 1}$, and of type (2). We identify $\mathop{\mathrm{MMHS}}$ with $\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}})$.

In [@KS2] the category of monodromic mixed Hodge modules is presented as a subcategory of $\mathop{\mathrm{MHM}}(X\times\mathbb{A}^1)$, whereas for us it is a quotient. We collect together some category theoretic lemmas that clarify this shift in point of view.

::: lemma
[]{#adjLem1 label="adjLem1"} Let $\Psi\colon \mathcal{B}\rightarrow\mathcal{B}$ be a functor, and let $\upnu\colon\mathop{\mathrm{id}}_{\mathcal{B}}\rightarrow \Psi$ be a natural transformation satisfying

1.  $\Psi(\upnu)=\upnu_{\Psi}\colon \Psi\rightarrow \Psi^2$, i.e. $\Psi(\upnu_{\mathcal{F}})=\upnu_{\Psi(\mathcal{F})}$ for all objects $\mathcal{F}$ in $\mathcal{B}$.

2.  $\Psi(\upnu)=\upnu_{\Psi}$ is an isomorphism of functors.

Let $\mathcal{D}\subset \mathcal{B}$ be the full subcategory containing those objects $\mathcal{F}$ of $\mathcal{B}$ such that $\upnu_{\mathcal{F}}\colon\mathcal{F}\rightarrow \Psi(\mathcal{F})$ is an isomorphism. Then the inclusion functor $\iota\colon\mathcal{D}\rightarrow \mathcal{B}$ is right adjoint to $\uppsi$ $$\begin{tikzcd}
\mathcal{B} \arrow[r,shift left=.5ex,"\Psi"]
&
\mathcal{D}. \arrow[l,shift left=.5ex,"\iota"]
\end{tikzcd}$$
:::

Condition (2) implies that $\Psi(\mathcal{F})\in\mathop{\mathrm{ob}}(\mathcal{D})$ for all $\mathcal{F}\in\mathop{\mathrm{ob}}(\mathcal{B})$, and so we obtain a factorization $\Psi\colon\mathcal{B}\rightarrow \mathcal{D}\xrightarrow{\iota}\mathcal{B}$. In the lemma, and from now on, we abuse notation by denoting the resulting functor $\mathcal{B}\rightarrow\mathcal{D}$ also by $\Psi$.

::: proof
*Proof.* Via the above abuse of notation we consider $\upnu$ as a natural transformation $\mathop{\mathrm{id}}_{\mathcal{B}}\rightarrow \iota\circ\Psi$. We claim that this is the unit of the adjunction, while $$\upeta\colonequals(\upnu|_{\mathcal{D}})^{-1}\colon \Psi|_{\mathcal{D}}\rightarrow \mathop{\mathrm{id}}_{\mathcal{D}}=\Psi\circ\iota$$ will be the unit. We need to check that the compositions of morphisms $$\begin{aligned}
\label{cua1}
&\Psi\xrightarrow{\Psi(\upnu)}\Psi\iota\Psi\xrightarrow{\upeta_{\Psi}}\Psi\\
\label{cua2}
&\iota\xrightarrow{\upnu_{\iota}}\iota\Psi\iota\xrightarrow{\iota(\upeta)}\iota
\end{aligned}$$ are the identity. Pick $\mathcal{F}\in\mathop{\mathrm{ob}}(\mathcal{B})$. Then $$\begin{aligned}
\upeta_{\Psi(\mathcal{F})}\circ\Psi(\upnu_{\mathcal{F}})=&\upnu_{\Psi(\mathcal{F})}^{-1}\circ\Psi(\upnu_{\mathcal{F}})\\=&\mathop{\mathrm{id}}_{\Psi(\mathcal{F})}.
\end{aligned}$$ Pick $\mathcal{F}\in\mathop{\mathrm{ob}}(\mathcal{D})$. Then $$\begin{aligned}
\iota(\upeta_{\mathcal{F}})\circ \upnu_{\iota(\mathcal{F})}=&\upnu_{\mathcal{F}}^{-1}\circ \upnu_{\mathcal{F}}\\=&\mathop{\mathrm{id}}_{\mathcal{F}}.
\end{aligned}$$ ◻
:::

::: lemma
[]{#adjLem2 label="adjLem2"} With the assumptions of Lemma [\[adjLem1\]](#adjLem1){reference-type="ref" reference="adjLem1"}, assume also that $\mathcal{B}$ is Abelian, and $\Psi$ is exact. Let $\mathcal{C}$ be the full subcategory of $\mathcal{B}$ containing those objects $\mathcal{F}$ for which $\Psi(\mathcal{F})=0$. Then $\mathcal{C}$ is a Serre subcategory. We denote the Serre quotient $\mathcal{B}/\mathcal{C}$. The functor $\Psi$ induces a functor $\tilde{\Psi}\colon\mathcal{B}/\mathcal{C}\rightarrow \mathcal{B}$, which is right adjoint to the canonical functor $Q\colon \mathcal{B}\rightarrow\mathcal{B}/\mathcal{C}$.
:::

::: proof
*Proof.* The category $\mathcal{C}$ is a Serre subcategory by exactness of $\Psi$. By the universal property of $\mathcal{B}/\mathcal{C}$, $\Psi$ induces a functor $\tilde{\Psi}\colon\mathcal{B}/\mathcal{C}\rightarrow \mathcal{B}$. We claim that $\upnu\colon \mathop{\mathrm{id}}_{\mathcal{B}}\rightarrow \Psi$ provides a unit for the adjunction. Let $\mathcal{F}\in\mathcal{B}/\mathcal{C}$, and consider the map $\upnu_{\mathcal{F}}\colon\mathcal{F}\rightarrow \Psi(\mathcal{F})$. Since $\Psi(\upnu_{\mathcal{F}})$ is an isomorphism, and $\Psi$ is exact, we deduce that $\Psi(\mathrm{ker}(\upnu_{\mathcal{F}}))=\Psi(\mathrm{coker}(\upnu_{\mathcal{F}}))=0$, and so $\upnu_{\mathcal{F}}$ represents an isomorphism $\overline{\upnu_{\mathcal{F}}}$ in $\mathcal{B}/\mathcal{C}$. Arguing as above, $(\overline{\upnu_{\mathcal{F}}})^{-1}$ provides the counit to the adjunction. ◻
:::

The proof of the following lemma is again constructed from the above adjunctions, and is omitted.

::: lemma
With the assumptions of Lemmas ([\[adjLem1\]](#adjLem1){reference-type="ref" reference="adjLem1"}) and ([\[adjLem2\]](#adjLem2){reference-type="ref" reference="adjLem2"}), the induced functor $\tilde{\Psi}\colon \mathcal{B}/\mathcal{C}\rightarrow\mathcal{D}$ is an equivalence of categories, with inverse equivalence the composition of canonical functors $\mathcal{D}\rightarrow \mathcal{B}\rightarrow\mathcal{B}/\mathcal{C}$.
:::

Now we apply these abstractions to certain categories of mixed Hodge modules. We define as in [@KS2] the exact functor $\Psi_X\colon\mathcal{B}_X\rightarrow\mathcal{B}_X$:

$$\Psi_X(\mathcal{F})=(X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathcal{F}\boxtimes (\mathbb{G}_m\rightarrow\mathbb{A}^1)_!\mathbb{Q}_{\mathbb{G}_m}[1]\right).$$ The functor is exact since it sends each of the simple mixed Hodge modules identified at the start of this section to mixed Hodge modules. Consider the distinguished triangle $$\mathbb{Q}_{\mathbb{A}^1}\rightarrow (\{0\}\hookrightarrow \mathbb{A}^1)_*\mathbb{Q}_{\{0\}} \xrightarrow{s}(\mathbb{G}_m\xrightarrow{j} \mathbb{A}^1)_!\mathbb{Q}_{\mathbb{G}_m}[1]$$ We define the natural transfromation $\upnu$, for $\mathcal{F}\in\mathcal{B}_X$, via the following composition of mixed Hodge modules on $X\times\mathbb{A}^1$ $$\begin{aligned}
\mathcal{F}\cong&(X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathcal{F}\boxtimes (\{0\}\hookrightarrow\mathbb{A}^1)_*\mathbb{Q}_{\{0\}}\right)\xrightarrow{s'}\\
&(X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathcal{F}\boxtimes (\mathbb{G}_m\rightarrow\mathbb{A}^1)_!\mathbb{Q}_{\mathbb{G}_m}[1]\right)\cong\Psi(\mathcal{F})
\end{aligned}$$ where $$s'=(X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathop{\mathrm{id}}_{\mathcal{F}}\boxtimes s\right).$$

::: lemma
The pair $(\Psi_X,\upnu)$ satisfies the conditions of Lemma [\[adjLem1\]](#adjLem1){reference-type="ref" reference="adjLem1"}.
:::

::: proof
*Proof.* Consider the commutative diagram $$\label{cdr}
\xymatrix{
X\times\mathbb{A}^1\times\mathbb{A}^1\times\mathbb{A}^1\ar[rr]^-{\mathop{\mathrm{id}}_{X\times\mathbb{A}^1}\times+}\ar[d]^{\mathop{\mathrm{id}}_X\times+\times\mathop{\mathrm{id}}_{\mathbb{A}^1}}&&X\times\mathbb{A}^1\times\mathbb{A}^1\ar[d]^{\mathop{\mathrm{id}}_X\times +}\\
X\times\mathbb{A}^1\times\mathbb{A}^1\ar[rr]^-{\mathop{\mathrm{id}}_X\times +}&&X\times \mathbb{A}^1.
}$$

We have $$\begin{aligned}
\Psi_X(\upnu_{\mathcal{F}})&=(\mathop{\mathrm{id}}_X\times +)_*(\upnu_{\mathcal{F}}\boxtimes\mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]})
\\&=(\mathop{\mathrm{id}}_X\times +)_*(\mathop{\mathrm{id}}_X\times +\times \mathop{\mathrm{id}}_{\mathbb{A}^1})_*(\mathop{\mathrm{id}}_{\mathcal{F}}\boxtimes s\boxtimes \mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]})
\\&=(\mathop{\mathrm{id}}_X\times +)_*(\mathop{\mathrm{id}}_{\mathcal{F}}\boxtimes +_*(s\boxtimes \mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]}))
\end{aligned}$$ where we have used commutativity of ([\[cdr\]](#cdr){reference-type="ref" reference="cdr"}) for the final equality. On the other hand, we have $$\begin{aligned}
\upnu_{\Psi_X(\mathcal{F})}=&(\mathop{\mathrm{id}}_X\times+)_*(\mathop{\mathrm{id}}_{\Psi_X(\mathcal{F})}\boxtimes s)\\
=&(\mathop{\mathrm{id}}_X\times +)_*(\mathop{\mathrm{id}}_X\times +\times \mathop{\mathrm{id}}_{\mathbb{A}^1})_*(\mathop{\mathrm{id}}_{\mathcal{F}}\boxtimes\mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]}\boxtimes s)\\
=&(\mathop{\mathrm{id}}_X\times +)_*(\mathop{\mathrm{id}}_{\mathcal{F}}\boxtimes +_*(\mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]}\boxtimes s))
\end{aligned}$$ and $$+_*(s\boxtimes \mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]})=+_*(\mathop{\mathrm{id}}_{j_!\mathbb{Q}_{\mathbb{G}_m}[1]}\boxtimes s)$$ by commutativity of $+$. We compute $$\begin{aligned}
\mathop{\mathrm{cone}}(\upnu_{\Psi_X(\mathcal{F})})\cong&(\mathop{\mathrm{id}}_X\times +)_*(\mathcal{F}\boxtimes +_*(j_!\mathbb{Q}_{\mathbb{G}_m}[1]\boxtimes \mathop{\mathrm{cone}}(s)))\\
\cong&(\mathop{\mathrm{id}}_X\times +)_*(\mathcal{F}\boxtimes +_*(j_!\mathbb{Q}_{\mathbb{G}_m}[1]\boxtimes \mathbb{Q}_{\mathbb{A}^1}[1]))
\end{aligned}$$ but $$+_*(j_!\mathbb{Q}_{\mathbb{G}_m}[1]\boxtimes \mathbb{Q}_{\mathbb{A}^1}[1]))\cong \mathop{\mathrm{H}}^*(\mathbb{A}^1,j_!\mathbb{Q}_{\mathbb{G}_m})\otimes\mathbb{Q}_{\mathbb{A}^2}[2]=0$$ proving that $\upnu_{\Psi_X(\mathcal{F})}$ is an isomorphism. ◻
:::

::: lemma
[]{#wrapup1 label="wrapup1"} Setting $\Psi=\Psi_X$, $\mathcal{B}=\mathcal{B}_X$ in Lemma ([\[adjLem2\]](#adjLem2){reference-type="ref" reference="adjLem2"}), we have $\mathcal{C}=\mathcal{C}_X$.
:::

::: proof
*Proof.* We denote by $\uppi\hspace{0.05em}\colon X\times\mathbb{A}^1\rightarrow X$ the projection. By definition, $\mathcal{C}$ is the full subcategory containing those objects $\mathcal{F}$ such that $\Psi_X(\mathcal{F})=0$. This is equivalent to the condition that the natural composition $$\uppi\hspace{0.05em}^*\uppi\hspace{0.05em}_*\mathcal{F}=(X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathcal{F}\boxtimes \mathbb{Q}_{\mathbb{A}^1}\right)\rightarrow (X\times\mathbb{A}^2\xrightarrow{\mathop{\mathrm{id}}\times +} X\times \mathbb{A}^1)_*\left(\mathcal{F}\boxtimes \mathbb{Q}_{0}[1]\right)=\mathcal{F}$$ is an isomorphism. It follows that the objects of $\mathcal{C}$ are contained in the objects of $\mathcal{C}_X$. On the other hand, the natural transformation $\uppi\hspace{0.05em}^*\uppi\hspace{0.05em}_*\uppi\hspace{0.05em}^*\rightarrow \uppi\hspace{0.05em}^*$ is an isomorphism and the reverse inclusion holds. ◻
:::

Via the same arguments, we deduce the following Lemma.

::: lemma
Under the assumptions of Lemma [\[wrapup1\]](#wrapup1){reference-type="ref" reference="wrapup1"} and with the terminology of Lemma [\[adjLem1\]](#adjLem1){reference-type="ref" reference="adjLem1"}, $\mathcal{D}$ is the full subcategory of $\mathcal{B}_X$ containing those objects $\mathcal{F}$ satisfying $\uppi\hspace{0.05em}_*\mathcal{F}=0$.
:::

The (sub)category $\mathcal{D}$ is identified as the category of monodromic mixed Hodge modules by Kontsevich and Soibelman; as we have shown, it is equivalent to our (quotient) category of monodromic mixed Hodge modules.

The natural pushforward $(X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)_!\colon \mathop{\mathrm{MHM}}(X\times\mathbb{G}_m)^{\mathop{\mathrm{mon}}}\rightarrow\mathop{\mathrm{MMHM}}(X)$ is an equivalence of categories, where $\mathop{\mathrm{MHM}}(X\times\mathbb{G}_m)^{\mathop{\mathrm{mon}}}$ is the full subcategory of $\mathop{\mathrm{MHM}}(X\times\mathbb{G}_m)$ containing those $\mathcal{F}$ such that the total cohomology of each pullback $(\{x\}\times\mathbb{G}_m\rightarrow X\times\mathbb{G}_m)^*\mathcal{F}$ is an admissible variation of mixed Hodge structure. An explicit inverse equivalence $\Theta_X$ is provided by $$\label{ThetaDef}
\Theta_X\colon\mathcal{F}\mapsto (X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)^*\tilde{\Psi}_X\mathcal{F}.$$ where $\tilde{\Psi}_X$ is functor induced by $\Psi_X$, as above. In terms of the two types of simple mixed Hodge modules identified at the start of the section, we have $$\begin{aligned}
\Theta_X\tilde{\mathcal{IC}}_{Y\times \mathbb{A}^1}(\mathcal{L})[\dim(Y)+1]\cong &\tilde{\mathcal{IC}}_{Y\times \mathbb{G}_m}(\mathcal{L}_{\neq 1})[\dim(Y)+1]\\
\Theta_X\tilde{\mathcal{IC}}_{Y\times \{0\}}(\mathcal{L})[\dim(Y)]\cong &\tilde{\mathcal{IC}}_{Y\times \mathbb{G}_m}(\mathcal{L}\boxtimes \mathbb{Q}_{\mathbb{G}_m})[\dim(Y)+1].
\end{aligned}$$

From the existence of a right adjoint to the functor $\mathcal{B}_X\rightarrow \mathop{\mathrm{MMHM}}(X)$, one can show (see e.g. [@Stackproject 06XM]) that the natural functor $$\mathcal{D}(\mathcal{B}_X)/\mathcal{D}_{\mathcal{C}_X}(\mathcal{B}_X)\rightarrow \mathcal{D}(\mathcal{B}_X/\mathcal{C}_X)=\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$$ is an equivalence of categories, where $\mathcal{D}_{\mathcal{C}_X}(\mathcal{B}_X)$ is the full subcategory of $\mathcal{D}(\mathcal{B}_X)$ consisting of those objects whose cohomology objects lie in $\mathcal{C}_X$. The subcategory $\mathcal{D}_{\mathcal{C}_X}(\mathcal{B}_X)$ is stable under the Verdier duality functor $\mathbb{D}_{X\times\mathbb{A}^1}$, and so we obtain a Verdier duality functor on $\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$ which we denote $\mathbb{D}^{\mathop{\mathrm{mon}}}_X$. The associated graded object $\mathop{\mathrm{Gr}}^W_{\bullet}(\mathcal{F})$ of an object in $\mathcal{C}_X$ with respect to the weight filtration is also in $\mathcal{C}_X$, and so the weight filtration descends to $\mathop{\mathrm{MMHM}}(X)$.

::: definition
Given an element $\mathcal{G}\in\mathop{\mathrm{MMHM}}(X)$, we say it is pure of weight $i$ if $\mathop{\mathrm{Gr}}^W_{j}\mathcal{G}$ is zero for all $j\neq i$. Given an element $\mathcal{F}\in\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$, we say that $\mathcal{F}$ is pure of weight $i$ if each $\mathop{\mathrm{\mathcal{H}}}^j(\mathcal{F})$ is pure of weight $i+j$, or we just say that $\mathcal{F}$ is *pure* if it is pure of weight zero.
:::

::: remark
The equivalence $(X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)_!\colon \mathop{\mathrm{MHM}}(X\times\mathbb{G}_m)^{\mathop{\mathrm{mon}}}\rightarrow\mathop{\mathrm{MMHM}}(X)$ does not preserve the weight filtration; for instance $\mathbb{Q}_{\mathbb{G}_m}[1]$ is a pure variation of Hodge structure of weight 1, while the monodromic mixed Hodge structure $(\mathbb{G}_m\rightarrow\mathbb{A}^1)_!\mathbb{Q}_{\mathbb{G}_m}[1]\cong(\{0\}\hookrightarrow \mathbb{A}^1)_*\mathbb{Q}_{\{0\}}$ is pure of weight zero.
:::

If $f\colon X\rightarrow Y$ is a morphism of varieties, we define the functors $f^!,f^*,f_!,f_*$ between the associated derived categories of monodromic mixed Hodge modules to be those induced by the functors $(f\times\mathop{\mathrm{id}}_{\mathbb{A}^1})^!,(f\times\mathop{\mathrm{id}}_{\mathbb{A}^1})^*,(f\times\mathop{\mathrm{id}}_{\mathbb{A}^1})_!,(f\times\mathop{\mathrm{id}}_{\mathbb{A}^1})_*$ between the associated derived categories of mixed Hodge modules.

::: definition
Assume $X$ is a variety $X\xrightarrow{\uptau}\mathbb{N}^{Q_0}$ over a monoid $\mathbb{N}^{Q_0}$ of dimension vectors for a quiver $Q$.

We define $\mathop{\mathrm{H}}(X,\mathcal{F})$ to be the total cohomology of $\uptau_*\mathcal{F}$. So $\mathop{\mathrm{H}}(X,\mathcal{F})$ may be thought of as a cohomologically graded $\mathbb{N}^{Q_0}$-graded monodromic mixed Hodge module on a point, e.g. the $\mathbb{N}^{Q_0}$-graded monodromic mixed Hodge structure underlying the total hypercohomology of $\mathcal{F}$. Similarly, we define $\mathop{\mathrm{H}}_c(X,\mathcal{F})$ to be the total cohomology of $\uptau_!\mathcal{F}$.
:::

The monoidal structures $\otimes$ on $\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(X))$ and $\mathcal{D}^{\leq}(\mathop{\mathrm{MMHM}}(X))$ are defined by $$\label{simmon}
\mathcal{F}\otimes\mathcal{G}\colonequals (X\times \mathbb{A}^1\times \mathbb{A}^1\xrightarrow{\mathop{\mathrm{id}}\times +}X\times \mathbb{A}^1)_*(\mathop{\mathrm{pr}}_{1,2}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{1,3}^*\mathcal{G})$$ where $\mathop{\mathrm{pr}}_{i,j}\colon X\times\mathbb{A}^1\times\mathbb{A}^1\rightarrow X\times\mathbb{A}^1$ is the projection onto the $i$th and the $j$th component.

::: remark
[]{#convProdDef label="convProdDef"} More generally, let $X$ be a monoid in $\mathop{\mathrm{Sch}}_{Y}$, the category of schemes over $Y$, with finite type monoid map $\oplus\colon X\times_Y X\rightarrow X$. Then define $$\mathcal{F}\boxtimes_{\oplus} \mathcal{G}\colonequals (X\times_Y X\times \mathbb{A}^1\times\mathbb{A}^1\xrightarrow{\oplus\times +} X\times\mathbb{A}^1)_*(\mathop{\mathrm{pr}}_{1,3}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{2,4}^*\mathcal{G}).$$ We recover ([\[simmon\]](#simmon){reference-type="ref" reference="simmon"}) in the special case in which $(X\xrightarrow{\mathop{\mathrm{id}}_X} X)$ is considered as a monoid in $\mathop{\mathrm{Sch}}_{X}$. In addition, for $\mathcal{F},\mathcal{G}$ objects of $\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(X)),\mathcal{D}^{\geq}(\mathop{\mathrm{MMHM}}(Y))$ or $\mathcal{D}^{\leq}(\mathop{\mathrm{MMHM}}(X)),\mathcal{D}^{\leq}(\mathop{\mathrm{MMHM}}(Y))$ respectively, we define $$\mathcal{F}\boxtimes \mathcal{G}\colonequals (X\times Y\times\mathbb{A}^1\times\mathbb{A}^1\xrightarrow{\mathop{\mathrm{id}}_{X\times Y}\times +} X\times Y\times \mathbb{A}^1)_*(\mathop{\mathrm{pr}}_{1,3}^*\mathcal{F}\otimes\mathop{\mathrm{pr}}_{2,4}^*\mathcal{G})\in\mathcal{D}(\mathop{\mathrm{MMHM}}(X\times Y)).$$ This external tensor product is biexact and preserves weight filtrations by [@KS2 Sec.4], [@Da16a Prop.3.2], or the proof of Proposition [\[symmPure\]](#symmPure){reference-type="ref" reference="symmPure"} below.
:::

There is a fully faithful embedding $\mathop{\mathrm{MHM}}(X)\rightarrow \mathop{\mathrm{MMHM}}(X)$ given by $$i_*=(X\xrightarrow{x\mapsto (x,0)} X\times\mathbb{A}^1)_*$$ which is furthermore a monoidal functor, commuting with Verdier duality, as $i$ is proper.

Define $\Theta_X$ as in ([\[ThetaDef\]](#ThetaDef){reference-type="ref" reference="ThetaDef"}). Let $e\colon X\xrightarrow{x\mapsto(x,1)}X\times\mathbb{G}_m$ be the natural inclusion. Then $e^*\Theta_X[-1]\colon \mathop{\mathrm{MMHM}}(X)\rightarrow \mathop{\mathrm{MHM}}(X)$ is also faithful (again using rigidity for variations of mixed Hodge structure [@StZu85 Thm.4.20]), and so we can define an exact faithful (non-derived) functor $$\label{formDef}
\mathop{\mathrm{forg}}^{\mathop{\mathrm{mon}}}_{X}\colon \mathop{\mathrm{MMHM}}(X)\rightarrow \mathop{\mathrm{Perv}}(X)$$ by setting $\mathop{\mathrm{forg}}^{\mathop{\mathrm{mon}}}_{X}\colonequals \mathop{\mathrm{rat}}_Xe^*\Theta_X[-1]$.

Let $f$ be a regular function on a smooth algebraic variety $X$. Define $X_{<0}=f^{-1}(\mathbb{R}_{<0})$ and $X_0=f^{-1}(0)$. We define the functor $\uppsi_f\colon \mathcal{D}(\mathop{\mathrm{Perv}}(X))\rightarrow\mathcal{D}(\mathop{\mathrm{Perv}}(X))$ $$\uppsi_f\colonequals (X_0\rightarrow X)_*(X_0\rightarrow X)^*(X_{<0}\rightarrow X)_*(X_{<0}\rightarrow X)^*$$ and define $\upphi_f\colonequals \mathop{\mathrm{cone}}((X_0\rightarrow X)_*(X_0\rightarrow X)^*\rightarrow\uppsi_f)$; this cone can indeed be made functorial --- see [@KSsheaves] for details, or the proof of Proposition [\[TSeq\]](#TSeq){reference-type="ref" reference="TSeq"} below for a functorial definition of $\upphi_f$. The functors $\uppsi_f$ and $\upphi_f$ have lifts to endofunctors of $\mathcal{D}(\mathop{\mathrm{MHM}}(X))$, forming a key part of Saito's theory.

In the sequel we consider vanishing cycles always as a functor $\mathcal{D}(\mathop{\mathrm{MHM}}(X))\rightarrow\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$ via the definition of [@KS2 Def.27] $$\label{phimdef}
\upphi^{\mathop{\mathrm{mon}}}_{f}\colonequals (X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)_!\upphi_{f/u}(X\times\mathbb{G}_m\rightarrow X)^*.$$ In ([\[phimdef\]](#phimdef){reference-type="ref" reference="phimdef"}), $u$ denotes the coordinate on $\mathbb{G}_m$.

::: example
Let $f=0$. Then $\upphi_f(\mathcal{F})\cong\mathcal{F}[1]$, since $\uppsi_f(\mathcal{F})=0$. Likewise, $\upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{F}=(X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1)_!(X\times\mathbb{G}_m\rightarrow X)^*\mathcal{F}[1]$. We deduce that $\upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{F}=j_!j^*\mathcal{G}[1]$ where $\mathcal{G}=(X\times\mathbb{A}^1\xrightarrow{\uppi\hspace{0.05em}} X)^*\mathcal{F}$ and $j\colon X\times\mathbb{G}_m\rightarrow X\times\mathbb{A}^1$ is the inclusion. Let $i\colon X\times \{0\}\hookrightarrow X\times\mathbb{A}^1$ be the complement to $j$. Since $\mathcal{G}$ is by definition trivial in $\mathop{\mathrm{MMHM}}(X)$, we deduce from the distinguished triangle $j_!j^*\rightarrow \mathop{\mathrm{id}}\rightarrow i_*i^*$ that $\upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{F}\cong i_*\mathcal{F}$ in $\mathop{\mathrm{MMHM}}(X)$. In other words, $\upphi^{\mathop{\mathrm{mon}}}_{0}\mathcal{F}\cong\mathcal{F}$, where we consider $\mathcal{F}$ on the right hand side of the isomorphism as a monodromic mixed Hodge module via pushforward along $X\xrightarrow{i\colon x\mapsto(x,0)} X\times\mathbb{A}^1$.
:::

::: remark
Generalising the above example; in fact it follows from exactness of the functors $\upphi_{f/u}[-1]$ (see [@BBD]), $\uppi\hspace{0.05em}^*[1]$ and $j_!$ that $\upphi^{\mathop{\mathrm{mon}}}_{f}$ is exact in general.
:::

We collect together some useful properties of $\upphi^{\mathop{\mathrm{mon}}}_{f}$.

::: proposition
[]{#basicfacts label="basicfacts"}

1.  []{#monPD label="monPD"}(Verdier duality): There is a natural isomorphism $$\mathbb{D}^{\mathop{\mathrm{mon}}}_X\upphi^{\mathop{\mathrm{mon}}}_{f}\cong \upphi^{\mathop{\mathrm{mon}}}_{f} \mathbb{D}_X\colon \mathcal{D}(\mathop{\mathrm{MHM}}(X))\rightarrow\mathcal{D}(\mathop{\mathrm{MMHM}}(X)),$$ where $\mathbb{D}_X$ is the usual Verdier duality functor.

2.  (Interaction with adjunction):[]{#adjInt label="adjInt"} If $p\colon X\rightarrow Y$ is a map of varieties, and $f$ is a regular function on $Y$, then there is a natural transformation $\upphi^{\mathop{\mathrm{mon}}}_{f}p_*\rightarrow p_*\upphi^{\mathop{\mathrm{mon}}}_{fp}$, which is moreover a natural isomorphism if $p$ is proper.

3.  []{#HomInv label="HomInv"}(Homotopy invariance): Let $X'\rightarrow X$ be an affine fibration with $d$-dimensional fibres. Then the natural map $\upphi^{\mathop{\mathrm{mon}}}_{f} \mathcal{F}\rightarrow p_*\upphi^{\mathop{\mathrm{mon}}}_{fp}p^*\mathcal{F}$ is an isomorphism, as is the natural map $p_!\upphi^{\mathop{\mathrm{mon}}}_{fp}p^*\mathcal{F}\rightarrow \upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{F}\otimes\mathop{\mathrm{H}}_c(\mathbb{A}^d)$.

4.  []{#exFact label="exFact"} (Exactness): The functor $\upphi^{\mathop{\mathrm{mon}}}_{f}\colon \mathcal{D}(\mathop{\mathrm{MHM}}(X))\rightarrow\mathcal{D}(\mathop{\mathrm{MMHM}}(X))$ is exact, i.e. it restricts to an exact functor $\mathop{\mathrm{MHM}}(X)\rightarrow\mathop{\mathrm{MMHM}}(X)$.

5.  (Vanishing cycle decomposition theorem)[]{#vanDec label="vanDec"} Let $\mathcal{F}\in\mathop{\mathrm{MMHM}}(X)$ be pure of weight $m$ for some $m\in\mathbb{Z}$, let $p\colon X\rightarrow Y$ be a proper map, and let $f$ be a regular function on $Y$. Then there is a non-canonical isomorphism $$p_*\upphi^{\mathop{\mathrm{mon}}}_{fp}\mathcal{F}\cong \mathop{\mathrm{\mathcal{H}}}(p_*\upphi^{\mathop{\mathrm{mon}}}_{fp}\mathcal{F}).$$

6.  (Thom--Sebastiani isomorphism): Let $f_j\colon X_j\rightarrow\mathbb{C}$ be regular functions, for $j=1,2$. Then there is a natural ismorphism of bifunctors $\mathop{\mathrm{MHM}}(X)\times\mathop{\mathrm{MHM}}(X)\rightarrow\mathop{\mathrm{MMHM}}(X)$: $$\upphi^{\mathop{\mathrm{mon}}}_{f_1}(\bullet)\boxtimes\upphi^{\mathop{\mathrm{mon}}}_{f_2}(\bullet)\rightarrow\upphi^{\mathop{\mathrm{mon}}}_{f_1\boxplus f_2}(\bullet\boxtimes\bullet)|_{f^{-1}_1(0)\times f^{-1}_2(0)}.$$

7.  (Integral identity): Let $V_+\oplus V_-$ be a $\mathbb{C}^*$-equivariant vector bundle on the space $X$, given a $\mathbb{C}^*$-action, where the weights of the action on $V_+$ are all $1$, and the weights of the action on $V_-$ are all $-1$. Let $f$ be a $\mathbb{C}^*$-invariant function. Below, for a vector bundle $V'$ we denote the total space of $V'$ also by $V'$. Then the natural map $$(V_+\rightarrow X)_!(V_+\rightarrow V_+\oplus V_-)^*\upphi^{\mathop{\mathrm{mon}}}_{f}(\mathbb{Q}_{V_+\oplus V_-}\rightarrow (V_+\rightarrow V_+\oplus V_-)_*\mathbb{Q}_{V_+})$$ is an isomorphism.
:::

The first five statements follow from the corresponding statements for $\upphi_f$. The first of these is proved at the level of perverse sheaves as the main theorem of [@Ma09], and for mixed Hodge modules as the main theorem of [@Sai89duality], see also Schürmann's appendix to [@Br12]. The second statement is given by combining [@Saito90 Thm.2.14, Thm.4.3]. Homotopy invariance then follows from the homotopy invariance statement for perverse sheaves. The hard part of the exactness statement is the statement that the shift of the usual vanishing cycle functor, $\upphi_f[-1]$, is exact. This is a result of Gabber, and can be found in [@BBD]. The version of the decomposition theorem quoted here follows from Saito's version of the decomposition theorem [@Saito90], and statements ([\[exFact\]](#exFact){reference-type="ref" reference="exFact"}) and ([\[adjInt\]](#adjInt){reference-type="ref" reference="adjInt"}). The statement regarding the Thom--Sebastiani isomorphism is in fact false after replacing $\upphi^{\mathop{\mathrm{mon}}}_{f}$ with $\upphi_f[-1]$. The statement involving $\upphi^{\mathop{\mathrm{mon}}}_{f}$ is due to Saito [@Saito10]; again we refer the reader to Schürmann's appendix to [@Br12] for the compatibility between this proof and the proof of Massey [@Ma01] at the level of complexes of perverse sheaves. The integral identity is proved in the above form in [@KS2], and is a central background result in the proof of the integrality conjecture[^1] in [@KS2]. Somewhat surprisingly, given its crucial role in the theory in other treatments of Hall algebras in Donaldson--Thomas theory, it is the only one of the seven facts about vanishing cyclesabove that we will not use.

For ease of exposition we make the following simplification in what follows.

::: assumption
[]{#phicheat label="phicheat"} For all functions $f\colon X\rightarrow \mathbb{C}$ for which we wish to take $\upphi^{\mathop{\mathrm{mon}}}_{f}$, if $X$ is smooth, we assume that $\mathop{\mathrm{crit}}(f)\subset f^{-1}(0)$ as sets.
:::

Under the assumption, the Thom--Sebastiani isomorphism for mixed Hodge modules simplifies to $$\upphi^{\mathop{\mathrm{mon}}}_{f_1}(\mathcal{F})\boxtimes\upphi^{\mathop{\mathrm{mon}}}_{f_2}(\mathcal{G})\rightarrow\upphi^{\mathop{\mathrm{mon}}}_{f_1\boxplus f_2}(\mathcal{F}\boxtimes\mathcal{G}).$$ The assumption can be dropped, with a little care. If it does not hold, one can instead work with the functor $\upphi^{\mathop{\mathrm{mon}},\textrm{fib}}_f\colonequals \bigoplus_{a\in\mathbb{A}_{\mathbb{C}}^1}\upphi^{\mathop{\mathrm{mon}}}_{f-a}$, or with exponential mixed Hodge structures --- see [@DaMe4], [@KS2], respectively.

Consider the embedding $\mathcal{D}^{b}(\mathop{\mathrm{MHM}}(\mathop{\mathrm{pt}}))\xrightarrow{i_*}\mathcal{D}^{b}(\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}}))$. The former category contains the element $$\mathbb{L}\colonequals \mathop{\mathrm{H}}_c(\mathbb{A}^1,\mathbb{Q}),$$ which is pure: it is concentrated entirely in cohomological degree 2, and has weight 2. There is no square root of $\mathbb{L}$ in $\mathcal{D}^{b}(\mathop{\mathrm{MHM}}(\mathop{\mathrm{pt}}))$, i.e. an element $\mathbb{L}^{1/2}$ such that $(\mathbb{L}^{1/2})^{\otimes 2}\cong \mathbb{L}$, but after embedding $\mathcal{D}^{b}(\mathop{\mathrm{MHM}}(\mathop{\mathrm{pt}}))$ in $\mathcal{D}^{b}(\mathop{\mathrm{MMHS}})$ there is a square root. We set $$\mathbb{L}^{1/2}\colonequals \mathop{\mathrm{H}}_c(\mathbb{A}^1,\upphi^{\mathop{\mathrm{mon}}}_{x^2}\mathbb{Q}_{\mathbb{A}^1}),$$ where $x^2\colon \mathbb{A}^1\rightarrow\mathbb{C}$ is considered as a regular function, and $\mathbb{Q}_{\mathbb{A}^1}$ is the constant (cohomologically shifted) mixed Hodge module on $\mathbb{A}^1$. Using the Thom--Sebastiani isomorphism one may show that this is indeed a tensor square root of $\mathbb{L}$. We fix an isomorphism $$l\colon \mathbb{L}^{1/2}\otimes\mathbb{L}^{1/2}\cong\mathbb{L}.$$ This amounts to fixing an isomorphism $r\colon\mathbb{Q}[-2]\cong\mathop{\mathrm{forg}}^{\mathop{\mathrm{mon}}}_{\mathop{\mathrm{pt}}}\mathbb{L}$, since up to sign there is a canonical isomorphism $\mathop{\mathrm{H}}_c(\mathbb{A}^1,\upphi_{x^2}\mathbb{Q}_{\mathbb{A}^1})\cong \mathbb{Q}[-1]$ given by picking one of the two natural basis elements of $\mathop{\mathrm{H}}_c(\mathbb{A}^1,\uppsi_{x^2}\mathbb{Q}_{\mathbb{A}^1})\cong\mathbb{Q}\oplus\mathbb{Q}$. In particular, since $\mathbb{A}^1$ carries a canonical orientation, there is a canonical choice of $r$ and thus of $l$. We set $$\label{tensinv}
\mathbb{L}^{-1/2}\colonequals \mathcal{H}om_{\mathcal{D}^{b}(\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}}))}(\mathbb{L}^{1/2},\mathbb{Q}),$$ so there is a canonical isomorphism $$\mathbb{L}^{1/2}\otimes\mathbb{L}^{-1/2}\cong\mathbb{Q}$$ with target the monoidal unit in $\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}})$.

Since $\mathbb{L}$ is pure, we deduce from Remark [\[convProdDef\]](#convProdDef){reference-type="ref" reference="convProdDef"} that $\mathbb{L}^{1/2}$ is pure, concentrated in cohomological degree 1. Note that due to the definition of the category of monodromic mixed Hodge modules on a point (i.e. monodromic mixed Hodge structures), this cohomological degree is with respect to the perverse t-structure on the underlying derived category of constructible sheaves on $\mathbb{A}^1\cong\mathbb{A}^1\times \mathop{\mathrm{pt}}$.

If $\mathcal{F}\in\mathop{\mathrm{MMHM}}(X)$ and $\mathcal{G}\in\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}})$ we use the abbreviation $$\mathcal{F}\otimes\mathcal{G}\colonequals \mathcal{F}\otimes 
\uptau^*\mathcal{G},$$ where $\uptau\colon X\rightarrow \mathop{\mathrm{pt}}$ is the map to a point.

For $X$ a variety and $d\in\mathbb{Z}$ we define $$\mathbb{L}_X^{d/2}=\mathbb{L}^{d/2}\otimes \mathbb{Q}_X.$$ If $X$ is a smooth equidimensional variety, we define $$\mathcal{IC}_{X}(\mathbb{Q})\colonequals \mathbb{L}_X^{-\dim(X)/2}.$$ This complex of monodromic mixed Hodge modules is pure, and an element of $\mathop{\mathrm{MMHM}}(X)$, again by Remark [\[convProdDef\]](#convProdDef){reference-type="ref" reference="convProdDef"}. If $X$ is not smooth, but is irreducible, we define the monodromic mixed Hodge module $\mathcal{IC}_X(\mathbb{Q})\colonequals \mathbb{L}^{-\dim(X_{\mathop{\mathrm{reg}}})/2}\otimes \tilde{\mathcal{IC}}_X(\mathbb{Q}_{X_{\mathop{\mathrm{reg}}}})$, where $\tilde{\mathcal{IC}}_X(\mathbb{Q}_{X_{\mathop{\mathrm{reg}}}})$ is the usual intersection cohomology mixed Hodge module complex of $X$ given by intermediate extension of $\mathbb{Q}_{X_{\mathop{\mathrm{reg}}}}$. Since $\tilde{\mathcal{IC}}_X(\mathbb{Q}_{X_{\mathop{\mathrm{reg}}}})$ is concentrated in cohomological degree $\dim(X_{\mathop{\mathrm{reg}}})$, it follows that $\mathcal{IC}_X(\mathbb{Q})$ is indeed a monodromic mixed Hodge module. If $X$ is a finite disjoint union of irreducible varieties, we define $$\mathcal{IC}_X(\mathbb{Q})\colonequals \bigoplus_{Z\in\uppi\hspace{0.05em}_0(X)}\mathcal{IC}_Z(\mathbb{Q}).$$

::: remark
[]{#finSD label="finSD"} Because of the shift in the definition of $\mathcal{IC}_X(\mathbb{Q})$, there are natural isomorphisms $\mathbb{D}^{\mathop{\mathrm{mon}}}_X\mathcal{IC}_X(\mathbb{Q})\cong\mathcal{IC}_X(\mathbb{Q})$ and $\mathbb{D}^{\mathop{\mathrm{mon}}}_X\upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{IC}_X(\mathbb{Q})\cong\upphi^{\mathop{\mathrm{mon}}}_{f}\mathcal{IC}_X(\mathbb{Q})$ for $X$ a finite disjoint union of irreducible varieties, and $f$ a regular function on $X$.
:::

For $X$ a smooth equidimensional variety we define $$\begin{aligned}
\mathop{\mathrm{H}}(X,\mathbb{Q})_{\mathop{\mathrm{vir}}}\colonequals &\mathop{\mathrm{H}}(X,\mathcal{IC}_X(\mathbb{Q}))\\\cong&\mathbb{L}^{-\dim(X)/2}\otimes\mathop{\mathrm{H}}(X,\mathbb{Q})\in\mathcal{D}^{b}(\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}})),
\end{aligned}$$ and since in the stack-theoretic sense the dimension of $\dim(\mathop{\mathrm{B\mathbb{C}^*}})$ is $-1$, we extend this notation by defining $$\mathop{\mathrm{H}}(\textrm{B}\mathbb{C}^*,\mathbb{Q})_{\mathop{\mathrm{vir}}}\colonequals \mathbb{L}^{1/2}\otimes \mathop{\mathrm{H}}(\textrm{B}\mathbb{C}^*,\mathbb{Q})\in \mathcal{D}(\mathop{\mathrm{MMHM}}(\mathop{\mathrm{pt}})).$$

[^1]: The similarity between the names of the "integral identity" and the "integrality conjecture" is merely coincidencidental.
