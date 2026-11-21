---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-012-51-natural-transformations-of--preserving-functo
section_title: "Natural Transformations of $*$-Preserving Functors"
section_number: 5.1
pages: 25-28
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.957
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
[]{#ss-nattrf label="ss-nattrf"}

::: prop
[]{#p-defprod label="p-defprod"} Let ${\cal D}, {\cal K}$ be $*$-categories and $F: {\cal D}\rightarrow{\cal K}$ a $*$-preserving functor. Let $\mathrm{Nat}\,F$ be the set of all natural transformations from $F$ to itself, viz. $$\mathrm{Nat}\,F= \{ b=(b_X \in \mathrm{End}\,F(X), \ X\in{\cal D} ) \ \ | \ \ 
   F(s)\,\circ\,b_X=b_Y \,\circ\,F(s) \ \ \forall s: X\rightarrow Y\}.$$ Then with the following pointwise operations $\mathrm{Nat}\,F$ is a unital $*$-algebra: $$\begin{aligned}
   (\lambda b +\lambda' b')_X &=& \lambda b_X + \lambda' b'_X,  \\
  (b b')_X &=& b_X \,\circ\,b'_X,  \\
  (b^*)_X &=& (b_X)^*,  \\
  {\bf 1}_X &=& id_{F(X)},
\end{aligned}$$ for $b, b' \in\mathrm{Nat}\,F,\ \lambda,\lambda'\in{\mathbb C}$ and $X\in{\cal D}$.
:::

*Proof. *If $s\in \mathrm{Mor}(X, Y )$, then $$F(s)\,\circ\,(b^* )_X = (b_X \,\circ\,F(s^* ))^* =(F(s^* )\,\circ\,b_Y )^* =(b^* )_Y \,\circ\,F(s),$$ where we have used $F(s^* )=F(s)^*$. Thus $b^*\in\mathrm{Nat}\,F$. Similarly, we get $b b', \ \lambda b + \lambda' b' \in\mathrm{Nat}\,F$, so with these operations $\mathrm{Nat}\,F$ is a $*$-algebra. Obviously ${\bf 1}$ is a unit for $\mathrm{Nat}\,F$.

::: defin
Let $B$ be a $*$-algebra and ${\cal K}$ a $*$-category. Then the category $\mathrm{Rep}_{\cal K}\,B$ of 'representations of $B$ in ${\cal K}$' has as objects the pairs $(X, \pi_X)$, where $X\in\mathrm{Obj}\,{\cal K}$ and $\pi_X$ is a non-degenerate $*$-homomorphism of $B$ into $\mathrm{End}\,X$. The morphisms are given by $$\mathrm{Mor}_{\mathrm{Rep}_{\cal K} B} ((X,\pi_X), (Y,\pi_Y))=\{ s\in\mathrm{Mor}_{\cal K}(X,Y) \ | \ s\,\circ\,\pi_X(b)
   =\pi_Y(b)\,\circ\,s \ \ \forall b\in B\}.$$
:::

Note that if ${\cal K}={\cal H}$, the category of finite dimensional Hilbert spaces, we have $\mathrm{End}\,H=B(H)$. Thus our definition reduces to the usual notion of finite dimensional non-degenerate $*$-representations of $B$: $\mathrm{Rep}_{\cal H}B=\mathrm{Rep}_f\,B$.

::: prop
[]{#p-funct-F label="p-funct-F"} Let ${\cal C}, {\cal K}$ be $*$-categories and $E: {\cal C}\rightarrow{\cal K}$ a $*$-preserving functor. Define a unital $*$-algebra $B=\mathrm{Nat}\,E$. There is a $*$-preserving functor $F: {\cal C}\rightarrow\mathrm{Rep}_{\cal K}\,B$ satisfying $K\,\circ\,F=E$, where $K: \mathrm{Rep}_{\cal K} B\rightarrow{\cal K},\ (X,\pi_X)\mapsto X$ is the forgetful functor.
:::

*Proof. * We set $F(X)=(E(X), \pi_X)$ for $X\in\mathrm{Obj}\,{\cal C}$ and $F(s)=E(s)$ for the morphisms of ${\cal C}$. Here the $*$-representation $\pi_X$ is defined by $$\pi_X: \ B\rightarrow\mathrm{End}\,X, \quad b\mapsto b_X.$$ That $F$ really is a functor follows from $$F(s)\,\circ\,\pi_X(b)=E(s)\,\circ\,b_X=b_Y\,\circ\,E(s)= \pi_Y(b)\circ F(s)
   \quad\quad \forall s:X\rightarrow Y\ \forall b\in B,$$ where we used $b\in B=\mathrm{Nat}\,E$.

::: prop
[]{#p-direct label="p-direct"} Let ${\cal D}$ be a semisimple $*$-category, ${\cal K}$ a $*$-category and $F: {\cal D}\rightarrow{\cal K}$ a $*$-preserving functor. Then there is an isomorphism $$\psi_F: \ \mathrm{Nat}\,F \rightarrow\prod_{i\in I_{\cal D}} \mathrm{End}\,F(X_i)$$ of $*$-algebras.
:::

*Proof. * We define a map $\psi_F :\mathrm{Nat}\,F\rightarrow\prod_{i\in I_{\cal D}} \mathrm{End}\,F(X_i)$ by $$\psi_F (b)=\prod_{i\in I_{\cal D}} b_{X_i}$$ for all $b\in\mathrm{Nat}\,F$. Clearly $\psi_F$ is a unital $*$-algebra homomorphism. We first show that it is injective. Suppose $\psi_F (b)=0$, so $b_{X_i}=0$ for all $i\in I_{\cal D}$. Let $X\in{\cal D}$. We must show that $b_X=0$. Recall that, for any $i\in I_{\cal D},\ \mathrm{Mor}(X_i, X )$ is a Hilbert space with the inner product $(s,t)\mathrm{id}_{X_i}=t^*s$ and that every $s\in\mathrm{Mor}(X_i, X)$ is a multiple of an isometry. Let $s_{i\alpha}\in \mathrm{Mor}(X_i, X ), \ i \in I_{\cal C},\ \alpha=1,\ldots, \dim \mathrm{Mor}(X_i, X )$ be an orthonormal basis w.r.t. this inner product satisfying $\sum_{i\alpha} s_{i\alpha} \,\circ\,s_{i\alpha}^* =\mathrm{id}_{X}$. Hence $$b_X= b_X \,\circ\,F(\mathrm{id}_{X})=\sum_{i\alpha} b_X\,\circ\,F(s_i \,\circ\,s_i^* )
=\sum_{i\alpha} F(s_i )\,\circ\,b_{X_i}\,\circ\,F(s_i^* )=0,$$ and injectivity of $\psi_F$ follows.

Next we prove surjectivity of $\psi_F$. Given $( b_i\in\mathrm{End}\,F(X_i),\ i\in I_{\cal D} )$ we need to construct $b\in\mathrm{Nat}\,F$ such that $\psi_F (b)=\prod_{i\in I_{\cal D}} b_i$. Thus let $X\in{\cal D}$. As above, pick a basis of isometries $s_{i\alpha}\in \mathrm{Mor}(X_i, X )$, $i\in I_{\cal D}$, with $\sum_{i\alpha} s_{i\alpha} \,\circ\,s_{i\alpha}^* =\mathrm{id}_{X}$. Define $b_X\in\mathrm{End}\,F(X)$ by $$b_X =\sum_{i\alpha} F(s_{i\alpha})\,\circ\,b_i\,\circ\,F(s_{i\alpha}^* ).$$ Another choice of orthonormal bases $(s_{i\alpha})$ in $\mathrm{Mor}(X_i, X),\ i\in I_{\cal D}$ does not affect $b_X$ since any two such bases are related by an orthogonal transformation. It remains to show that $b\in\mathrm{Nat}\,F$, viz. $F(s)\,\circ\,b_X=b_Y\,\circ\,F(s) \ \ \forall s: X\rightarrow Y$. To this purpose consider $u\in \mathrm{Mor}(X, Y )$. Pick isometries $t_{j\beta}\in\mathrm{Mor}(Y_j,Y )$, with $\sum_{j\beta} t_{j\beta} \,\circ\,t_{j\beta}^* =\mathrm{id}_{Y}$, and define $b_Y\in\mathrm{End}\,F(Y)$ by $$b_Y=\sum_{j\beta} F(t_{j\beta})\,\circ\,b_j\,\circ\,F(t_{j\beta}^* ).$$ Then $$F(u)\,\circ\,b_X=\sum_{i\alpha} F(u \,\circ\,s_{i\alpha} )\,\circ\,b_i\,\circ\,F(s_{i\alpha}^* )
  =\sum_{i\alpha,j\beta} F(t_{j\beta}\,\circ\,t_{j\beta}^* \,\circ\,u\,\circ\,s_{i\alpha} )\,\circ\,b_i \,\circ\,F(s_{i\alpha}^* ).$$ But $t_{j\beta}^*\,\circ\,u\,\circ\,s_{i\alpha}\in\mathrm{Mor}(X_i,X_j)$ is zero unless $i=j$ and otherwise a scalar multiple of $\mathrm{id}_{X_i}$. Hence $$F(u)\,\circ\,b_X
=\sum_{i\alpha\beta} F(t_{i\beta}\,\circ\,(t_{i\beta}^*\,\circ\,u\,\circ\,s_{i\alpha})) \,\circ\,b_i\,\circ\,F(s_{i\alpha}^*)
=\sum_{i\alpha,j\beta} F(t_{j\beta})\,\circ\,b_j\,\circ\,F(t_{j\beta}^*\,\circ\,u\,\circ\,s_{i\alpha}\,\circ\,s_{i\alpha}^*)
=b_Y\,\circ\,F(u).$$ The last identity in this equation follows by precisely the same sort of argument as used before. This proves the naturality of the family $b\in\mathrm{Nat}\,F$. Obviously we have $b_{X_i}=b_i$ for all $i\in I_{\cal D}$. Thus $\psi_F (b)=\prod_{i\in I_{\cal D}} b_i$, which proves surjectivity of $\psi_F$.

The isomorphism $\psi_F$ depends on the chosen family $X_i, i\in I$ of irreducibles in ${\cal C}$, but is canonical once the latter is fixed. Thus there is no risk in suppressing it and writing $\mathrm{Nat}\,F=\prod_{i\in I_{\cal D}} \mathrm{End}\,F(X_i)$, as will be done in the sequel.

::: example
[]{#e-idfunc label="e-idfunc"} The simplest application of this proposition is to the identity ${\cal D}\rightarrow{\cal D}$, when we get $$\mathrm{Nat}\,(Id)\cong\prod_{i\in I_{\cal D}} {\mathbb C}.$$ Examples of natural transformations of the identity are the 'twists' appearing in the context of braided tensor categories.
:::

::: example
[]{#e-otimes label="e-otimes"} Suppose ${\cal D}$ is a tensor $*$-category with tensor product $\otimes$. A less trivial application of the proposition is the case of the tensor functor $F=\otimes :{\cal D}\times{\cal D}\rightarrow {\cal D}$, where ${\cal D}\times{\cal D}$ is the product $*$-category. Note that the isomorphism classes of irreducible objects in ${\cal D}\times{\cal D}$ are precisely $I_{\cal D}\times I_{\cal D}$. By semisimplicity of ${\cal D}$ we have a finite decomposition $$X_i\otimes X_j\cong \bigoplus_{k\in I_{\cal D}} N_{ij}^k X_k,$$ for any $i,j\in I_{\cal D}$ and thus $\mathrm{End}(X_i\otimes X_j)\cong \bigoplus_{k\in I_{\cal D}} M_{N_{ij}^k}({\mathbb C})$. We therefore obtain $$\mathrm{Nat}\,\otimes\ \cong\ \prod_{\stackrel{i,j,k\in I_{\cal D}}{N_{ij}^k\ne 0}} M_{N_{ij}^k}({\mathbb C}).$$
:::

The following example is a continuation of Example [\[e-idfunc\]](#e-idfunc){reference-type="ref" reference="e-idfunc"}.

::: example
Suppose ${\cal C}$ is a semisimple $*$-category. Consider the $*$-algebra $A=\oplus_{i\in I_{\cal C}}{\mathbb C}$. Then Proposition [\[p-funct-F\]](#p-funct-F){reference-type="ref" reference="p-funct-F"} provides an equivalence $F: {\cal C}\rightarrow\mathrm{Rep}_f\,A$ of categories such that $F(X_i)\cong p_i$ for all $i\in I_{\cal C}$. Let $K:\mathrm{Rep}_f\,A\rightarrow{\cal H}$ be the forgetful functor. Then $K\,\circ\,F$ is an embedding functor for ${\cal C}$ as a $*$-category. By Proposition [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} and Example [\[e-idfunc\]](#e-idfunc){reference-type="ref" reference="e-idfunc"} we also conclude that $$\mathrm{Nat}(K\,\circ\,F)\cong\mathrm{Nat}\,Id\cong\prod_{i\in I_{\cal C}}{\mathbb C}.$$ (Here of course, it does not make sense to say that the functors $Id$ and $K\,\circ\,F$ are unitarily equivalent.) Suppose now that ${\cal C}$ is in addition a tensor category. Then the faithful functor $K\,\circ\,F$ cannot in general be monoidal. To see this let $X_i, X_j$ with $i,j\in I_{\cal C}$. Then $K\,\circ\,F(X_i )\cong K(p_i )\cong{\mathbb C}$, so $K\,\circ\,F(X_i )\otimes K\,\circ\,F(X_j )\cong{\mathbb C}$, whereas $$K\,\circ\,F (X_i\otimes X_j )\cong \bigoplus_{k\in I_{\cal C}}N_{ij}^k\, \, \, K\,\circ\,F(X_k )
\cong\bigoplus_{k\in I_{\cal C}}N_{ij}^k\, \, {\mathbb C},$$ where we used the decomposition $X_i\otimes X_j\cong\oplus_{k\in I_{\cal C}}N_{ij}^k\, \ X_k$.
:::

Given a $*$-preserving functor $E:{\cal C}\rightarrow{\cal K}$ and writing $B=\mathrm{Nat}\,E$ it is natural to ask under which conditions the functor $F: {\cal C}\rightarrow\mathrm{Rep}_{\cal K}B$ defined in Proposition [\[p-funct-F\]](#p-funct-F){reference-type="ref" reference="p-funct-F"} is an equivalence of categories. Instead of pursuing this line further we restrict ourselves to the case where ${\cal C}$ is semisimple and ${\cal K}={\cal H}$. Then $\mathrm{End}\,E(X)$ is a finite dimensional matrix algebra for every $X\in{\cal C}$ and Proposition [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} shows that $\mathrm{Nat}\,E$ is a direct product of matrix algebras. The representation theory of such algebras is quite intricate, cf. [@GT]. There it is shown, among other results, that every irreducible representation of $B=\prod_{i\in I} B(H_i)$ is equivalent to a projection $p_i$ iff the index set $I$ has less than measurable cardinality. In practice, this is no serious restriction but for reasons which will become clear in the next subsection we prefer to work with direct sums instead of direct products.

::: thm
[]{#t-equiv label="t-equiv"} Let ${\cal C}$ be a semisimple $*$-category and $E: {\cal C}\rightarrow{\cal H}$ a $*$-preserving functor. The $*$-algebra $A=\oplus_{i\in I_{\cal C}} B(E(X_i))$ embeds canonically into $\mathrm{Nat}\,E\cong\prod_{i\in I_{\cal C}} B(E(X_i))$. The functor $$F:\ {\cal C}\rightarrow\mathrm{Rep}_f A, \quad F(X)=(E(X),\pi_X),\ \pi_X(a)=a_X\ \forall a\in A, \quad F(s)=E(s)$$ satisfies $K\,\circ\,F=E$. It gives rise to an equivalence of categories iff $E$ is faithful.
:::

*Proof. *$F$ as defined above differs from the functor defined in Proposition [\[p-funct-F\]](#p-funct-F){reference-type="ref" reference="p-funct-F"} only in the restriction of the representations $\pi_X$ to $A\subset\mathrm{Nat}\,E$. Thus it clearly is a $*$-preserving functor. By definition it is clear that $K\,\circ\,F=E$. Since $F$ coincides with $E$ on morphisms, $E$ is faithful if $F$ is an equivalence. Assume now that $E$ is faithful. Let $X\in{\cal C}$ be irreducible. Then $F(X)$ is a representation $\pi_X: a\mapsto a_X$ of $A$ on the Hilbert space $E(X)$. As is clear from the proof of Proposition [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"}, for $X=X_i$ we have $\pi_X=p_i$, which clearly is irreducible. Since $a\in A$ is a natural transformation, $\pi_X: a\mapsto a_X$ is an irreducible $*$-representation whenever $X$ is irreducible. Consider $i\ne j, i,j\in I_{\cal C}$. By Proposition [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"}, the projections $p_i=F(X_i), p_j=F(X_j)$ are inequivalent $*$-representations. By semisimplicity of $\mathrm{Rep}_f A$ this implies that $F$ is full. Since the $p_i, i\in I_{\cal C}$ exhaust the equivalence classes of irreducible $*$-representations of $A$ it is clear that $F$ is essentially surjective, completing the proof.

::: rema
The theorem remains true if one replaces $A$ by the direct product algebra $\mathrm{Nat}\,E$ provided one makes the additional assumption that the set $I_{\cal C}$ of isomorphism classes of ${\cal C}$ has less than measurable cardinality.
:::
