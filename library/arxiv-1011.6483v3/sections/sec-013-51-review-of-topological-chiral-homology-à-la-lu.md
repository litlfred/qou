---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-013-51-review-of-topological-chiral-homology-à-la-lu
section_title: "Review of topological chiral homology à la Lurie"
section_number: 5.1
pages: 40-43
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.979
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:ReviewTCH label="S:ReviewTCH"}

Let $A$ be an $E_n$-algebra and $M$ a manifold of dimension $m$ which is *(stably) $n$-framed*, that is a manifold of dimension $m$ equipped with a framing of $M\times D^{n-m}$. The **topological chiral homology** of $M$ with coefficients in $A$ was defined in [@L-TFT; @L-VI] and [@Francis] and will be denoted $\int_{M} A$. Note that the above definition *does* depend on the framing in general, even though it is not explicit in the notation[^1]. Further $\int_M A$ is an $E_{n-m}$-algebra in general, see [@L-TFT; @L-VI]. We refer to the aforementioned references as well as to[@Francis; @Andrade; @AFT] for a precise definition. If $X$ is a manifold, let $N(\text{Disj}(X))$ be the $\infty$-category associated to the poset given by finite disjoint union of open sets in $X$ homeomorphic to an euclidean disk, ordered by inclusion. According to Lurie [@L-VI Remark 5.3.2.7] we have, roughly, that

::: definition
[]{#Def:TCHasColimit label="Def:TCHasColimit"} Let $M$ be an $n$-framed manifold of dimension $m$ and $A$ an $E_n$-algebra. The *topological chiral homology* $\int_M A$ is the colimit $\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{} \psi_M$ with $\psi_M:N(\emph{\text{Disj}}(M\times D^{n-m}))\to k\textit{-}Mod_\infty$ the diagram given by the formula $$\label{eq:DefTCH}\psi_M(V_1\cup\cdots\cup V_n)=\int_{V_1}A \otimes \cdots \otimes \int_{V_n} A\cong A\otimes \cdots \otimes A$$ where $V_1,\dots, V_n$ are disjoint open sets homeomorphic to a ball (the latter equivalence follows from [@L-VI Example 5.3.2.8]).
:::

For our purpose, among the properties satisfied by $\int_M A$, we will mainly need the gluing property given in Proposition [\[P:TCHpushout\]](#P:TCHpushout){reference-type="ref" reference="P:TCHpushout"} below and the fact that $\int_{pt}A \cong A$. Indeed, the gluing property of topological chiral homology comes from the fact that topological chiral homology defines an (extended) topological field theory in some appropriate monoidal $(\infty,n)$-category. In view of the cobordism hypothesis, the latter property can actually be used as a definition of topological chiral homology [@L-TFT Theorem 4.1.24].

::: remark
[]{#R:Enoperad label="R:Enoperad"} The models for $E_n$-algebras that we are considering are given by $E_n$-($\infty$-)operads as introduced in [@L-VI Section 5.1] in the symmetric monoidal ($(\infty,1)$-)category $(k\textit{-}Mod_\infty,\otimes)$. The category of $E_n$-algebras is symmetric monoidal ([@L-VI Section 5.1.5], [@L-III Section 1.8]) and, furthermore, there is a commutative diagram of operads $$\label{E:EnCom} \xymatrix{E_1 \ar@{^{(}->}[r] \ar[rrd]_{j_1}&  E_2\ar@{^{(}->}[r] \ar[rd]^{j_2}& \dots \dots \ar@{^{(}->}[r]& E_n\ar@{^{(}->}[r] \ar[ld]^{j_n}& \dots \\
 & & \mathop{Com} & & }$$ where $\mathop{Com}$ is the operad of commutative (differential graded) algebras such that all maps are monoidals. Note that most models for $E_n$-algebras come with such monoidal properties and also as nested sequences (for instance, this is the case for the models based on the Barratt-Eccles operad [@BF]). In particular, a commutative differential graded algebra $A$ is naturally an $E_d$-algebra for any integer $d$. We write $j_d^*(A)$ for the $E_d$-algebra structure on $A$ induced by the map of operads $j_d:E_d\to \mathop{Com}$ whenever we want to put emphasis on this $E_d$-algebra structure.

Likewise, any $E_n$-algebra $A$ is naturally an $E_d$ algebra for $d\leq n$. Furthermore, we say that an $A$-module $M$ has a *compatible* structure of $E_d$-algebras ($d\leq n$) if the structure maps of the module structure are maps of $E_d$-algebras, where $A$ is equipped with its natural $E_d$-algebra induced by the diagram of operads [\[E:EnCom\]](#E:EnCom){reference-type="eqref" reference="E:EnCom"}.
:::

::: remark
With the exception of section [\[SEC:En\[M\]-alg\]](#SEC:En[M]-alg){reference-type="ref" reference="SEC:En[M]-alg"}, this paper only deals with a fixed $E_n$-algebra $A$, which, when $M$ is framed, is an example of a locally constant $N(\mathop{\mbox{Disk}}(M))$-algebra in the sense of Lurie [@L-VI], and for which topological chiral homology can be defined, too. In particular, we will show that $A$ also defines canonically a locally constant factorization algebra on $M$ in the sense of Costello and Gwilliam [@CG; @Co]. This also means, that $\int_M A$ computes the global sections of a natural cosheaf defined on the Ran space of $M$ (see [@L-VI Section 5.3.2]).
:::

One of the main consequence of the interpretation [@L-TFT] of topological chiral homology as an invariant produced by an (extended) topological field theory in some appropriate monoidal $(\infty,n)$-category is the following excision property.

::: proposition
[]{#P:TCHpushout label="P:TCHpushout"} Let $M$ be an $n$-framed manifold (possibly with corners) of dimension $m$, (*i.e.* $M\times D^{n-m}$ is framed). Assume that there is a codimension $1$ submanifold (possibly with corners) of $M$ of the form $N\times I^{m-1-j}$ (for some $0\leq j\leq m-1$) with a trivialization $N\times I^{m-j}$ of its neighborhood and that $M$ is decomposable as $M=X\cup_{N\times I^{m-j}}Y$ where $X,Y$ are submanifolds (with corners) of $M$ glued along $N \times I^{m-j}$. We endow $X,Y$ and $N$ with the $n$-framing induced from $M$. Let $A$ be an $E_{n}$-algebra. Then

-   $\int_N A$ is an $E_{n-j}$-algebra.

-   $\int_M A$, $\int_X A$, and $\int_Y A$ are $E_{n-m}$-algebras. Further $\int_X A$ and $\int_Y A$ are also modules over the $E_{n-j}$-algebra $\int_N A$.

-   The above module and algebra structures are compatible. Note that this uses the once and for all fixed telescopic sequence [\[E:EnCom\]](#E:EnCom){reference-type="eqref" reference="E:EnCom"} of models for $E_n$-operads.

-   There is a natural equivalence of $E_{n-m}$-algebras $$\int_X A\, \mathop{\otimes}\limits^{\mathbb{L}}_{\int_N\! A} \, \int_Y A \stackrel{\simeq}\longrightarrow \int_M A.$$
:::

::: proof
*Proof.* This is explained in [@L-VI Section 5.3.4] and [@L-TFT Section 4.1], also see the proof of [@Francis; @AFT]. It is also an immediate consequence of Lemma [\[L:TCHpushout2\]](#L:TCHpushout2){reference-type="ref" reference="L:TCHpushout2"} below, in the case where the manifolds are framed since, for a $n$-framed manifold $X$, an $E_n$-algebra yields canonically an $\mathbb{E}[X]$-algebra. ◻
:::

Let us explain roughly, how the above Proposition can be seen in terms of extended topological field theory and the cobordism hypothesis. Consider the monoidal $(\infty,n)$-category $E_{\leq n}\textit{-}Alg$ which is fully dualizable [@L-TFT]. Each object $A$ is an $E_{n}$-algebra and defines a (unique up to equivalence) *extended topological field theory* $\psi_A: Bord^{fr}_{n} \to  E_{\leq n}\textit{-}Alg$ according to [@L-TFT Theorem 2.4.6] and [@L-TFT Section 4.1]. The objects of the $(\infty,n-1)$-category $\mathop{Hom}_{E_{\leq n}\textit{-}Alg}(A,B))$ of morphisms between two $E_n$-algebras $A$, $B$ are $(A,B)$-bimodules equipped with a compatible $E_{n-1}$-algebra structure (in the sense of the telescopic sequence of $E_k$-operads [\[E:EnCom\]](#E:EnCom){reference-type="eqref" reference="E:EnCom"}). Note that the claims made in Section 4.1 in [@L-TFT] actually essentially follows from [@L-VI Theorem 1.2.2] and Sections 2 of [@L-VI].

The relationship between topological chiral homology with coefficients in $A$ and the field theory $\psi_A$ is as follows. Let $Z$ be an $n$-framed manifold of dimension $d$ (framing of $Z\times D^{n-d}$). Then $Z$ defines a $d$-morphism in $Bord^{fr}_{n}$, thus $\psi_A(Z)$ is an $E_{n-d}$-algebra and there is a natural equivalence $$\psi_A(Z)\cong \int_Z A$$ see [@L-TFT Theorem 4.1.24].

Now assume $M$ is a manifold following the assumption of Proposition [\[P:TCHpushout\]](#P:TCHpushout){reference-type="ref" reference="P:TCHpushout"}. Thus $M\times D^{n-m}$ is framed and we have a decomposition $M=X\cup_{N\times I^{m-j}}Y$ of $M$ where $X,Y$ are submanifolds of $M$ glued along a submanifold $N\times I^{m-1-j}$ of codimension $1$ in $M$. Then $N$ is a $j$-arrow in $Bord^{fr}_{n}$ and $X,Y$ are $m$-arrows. Hence $\psi_A(N)\cong \int_N A$ is a $j$-arrow in $E_{\leq n}\textit{-}Alg$, hence an $E_{n-j}$-algebra. Similarly, $\psi_A(X)$ and $\psi_A(Y)$ are $E_{n-m}$-algebras. Since $N\times I^{m-1-j}$ is in the boundary of $X$ and $Y$, $\psi_A(X)$ and $\psi_A(Y)$ inherits $\psi_A(N)$-modules structures. Further $M$ is equivalent to the composition of $X, Y$ along $N$ in the $(\infty,n)$-category $Bord^{fr}_{n}$. Thus it follows that there is a natural equivalence $\psi_A(X)\otimes_{\psi_A(N)}^{\mathbb{L}} \psi_A(Y)$ in $E_{\leq n}\textit{-}Alg$ since the composition in the $(\infty,n)$-category is induced by derived tensor products.

We finish this Section with the following Lemma.

::: lemma
[]{#L:TCHcoproduct label="L:TCHcoproduct"} Let $A$ be an $E_n$-algebra and $(M_i)_{i\in I}$ a family of $n$-framed manifolds of dimension $m$. There is a natural equivalence of $E_{n-m}$-algebras $$\mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{\small \begin{array}{l}F \subset J \\
   F \mbox{ finite}\end{array}
} \left(\bigotimes_{f \in F} \int_{M_f} A \right) \stackrel{\simeq} \longrightarrow \int_{\coprod_{i\in I} M_i} A  .$$
:::

::: proof
*Proof.* We set $M=\coprod_{i\in I} M_i$ and, for any finite subset $F$ of $I$, we denote $M_F:= \coprod_{f\in F} M_f$. The inclusion $M_F\subset M$ yields a canonical map $N({\text{Disj}}(M_F\times D^{n-m})) \to N({\text{Disj}}(M\times D^{n-m}))$. Since an object in $N({\text{Disj}}(M\times D^{n-m}))$ is a *finite* disjoint union of connected open sets in $M$, every object in $N({\text{Disj}}(M\times D^{n-m}))$ lies in some $N({\text{Disj}}(M_F\times D^{n-m}))$ for a finite $F$. Hence we have an equivalence $N({\text{Disj}}(M\times D^{n-m}))\cong \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{F\text{ finite}}N({\text{Disj}}(M_F\times D^{n-m}))$ of $\infty$-categories and, by Definition [\[Def:TCHasColimit\]](#Def:TCHasColimit){reference-type="ref" reference="Def:TCHasColimit"}, an natural equivalence $$\int_M A \cong \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits\psi_M \cong \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{F\text{ finite}} \psi_{M_F} \cong  \mathop{\lim\limits_{\textstyle\longrightarrow}}\limits_{F\text{ finite}} \int_{M_F} A.$$ Now the lemma follows from [@L-VI Theorem 5.3.3.1] which gives a natural equivalence $\left(\bigotimes_{f \in F} \int_{M_f} A \right) \stackrel{\simeq}\to \int_{M_F} A$ for all finite $F$. ◻
:::

[^1]: note that we also do not write the factor $D^{n-m}$ in the notation
