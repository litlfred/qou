---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-011-5-from-concrete-tensor-categories-to-discrete-qu
section_title: "From Concrete Tensor Categories to Discrete Quantum Groups"
section_number: 5
pages: 25-32
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.973
---
The strategy we adopt in this section was been pursued by J.E. Roberts [@ro] in the discrete Kac algebra case, and has then been adapted to the more algebraic setting of discrete aqg $(A, \Delta)$ by the authors.

## Natural Transformations of $*$-Preserving Functors {#ss-nattrf}

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

## Concrete Tensor $*$-Categories and Discrete Quantum Semigroups

From now on, ${\cal C}$ will be a semisimple strict tensor $*$-category. (As discussed in the Introduction, the strictness assumption does not entail a loss of generality.) We will introduce other requirements as we proceed. By Theorem [\[t-equiv\]](#t-equiv){reference-type="ref" reference="t-equiv"} we have associated a $*$-algebra $A$ to a $*$-preserving functor $E: {\cal C}\rightarrow{\cal H}$. The aim of this subsection is to endow $A$ with the structure of a discrete aqg under suitable conditions on ${\cal C}$ and $E$. To bring out the special rôle of the target category ${\cal H}$, we work in a more general setting as far as seems justifiable.

Let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor into some tensor $*$-category ${\cal D}$. Recall that by Proposition [\[p-defprod\]](#p-defprod){reference-type="ref" reference="p-defprod"}, $\mathrm{Nat}\,E$ is a unital $*$-algebra for every $*$-preserving functor $E: {\cal C}\rightarrow{\cal D}$.

::: prop
Let ${\cal C}, {\cal D}$ be tensor $*$-categories, ${\cal C}$ being strict, and let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor. Then $$\tilde{\Delta}: \mathrm{Nat}\,E\rightarrow\mathrm{Nat}\,E\otimes, \quad b=(b_X) \ \mapsto \ \tilde{\Delta}(b)\ =\ 
   (\tilde{\Delta}(b)_{Y,Z}), \quad \tilde{\Delta}(b)_{Y,Z}=b_{Y\otimes Z}$$ defines a unital $*$-homomorphism.
:::

*Proof. *The morphisms in ${\cal C}\times{\cal C}$ are of the form $s\times t$ where $s: Y\rightarrow Y',\ t: Z\rightarrow Z'$. Then $s\otimes t\in\mathrm{Mor}(Y\otimes Z,Y'\otimes Z')$. We compute $$(E\otimes) (s\times t) \, \,\circ\,\tilde{\Delta}(b)_{Y,Z} = 
   E(s\otimes t) \, \,\circ\,\, b_{Y\otimes Z} = b_{Y'\otimes Z'} \, \,\circ\,E(s\otimes t) = 
   \tilde{\Delta}(b)_{Y',Z'} \,\circ\,(E\otimes) (s\times t),$$ where we used $b=(b_X)\in\mathrm{Nat}\,E$. We conclude that $\tilde{\Delta}(b)\in\mathrm{Nat}\,E\otimes$. That $b\mapsto\tilde{\Delta}(b)$ is a unital $*$-homomorphism follows immediately from Proposition [\[p-defprod\]](#p-defprod){reference-type="ref" reference="p-defprod"}.

We now consider the analogues of $(\Delta\otimes\iota)$, ${\cal C}$ being strict, and $(\iota\otimes\Delta)$ in the present general setting. $\otimes^2$ will denote the functor $\otimes\,\circ\,(\otimes\times Id)=\otimes\,\circ\,(Id\times\otimes):{\cal C}\times{\cal C}\times{\cal C}\rightarrow{\cal C}$, where we have used the strictness of ${\cal C}$.

::: prop
[]{#p-coassoc label="p-coassoc"} Let ${\cal C}, {\cal D}$ be tensor $*$-categories and let $E: {\cal C}\rightarrow{\cal D}$ be a $*$-preserving tensor functor. There are unital $*$-homomorphisms $\widetilde{\Delta\otimes\iota}, \widetilde{\iota\otimes\Delta}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2$ defined by $$\begin{aligned}
   \widetilde{\Delta\otimes\iota}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2, &&  b=(b_{X,Y})\ \mapsto\      (\widetilde{\Delta\otimes\iota})(b)=((\widetilde{\Delta\otimes\iota})(b)_{U,V,W}), \quad
    (\widetilde{\Delta\otimes\iota})(b)_{U,V,W}=b_{U\otimes V,W}, \\
   \widetilde{\iota\otimes\Delta}: \ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E\otimes^2, &&
   b=(b_{X,Y})\ \mapsto\ (\widetilde{\iota\otimes\Delta})(b)=((\widetilde{\iota\otimes\Delta})(b)_{U,V,W}), \quad
    (\widetilde{\iota\otimes\Delta})(b)_{U,V,W}=b_{U,V\otimes W}.
\end{aligned}$$ These morphisms satisfy $(\widetilde{\Delta\otimes\iota})\tilde{\Delta}=(\widetilde{\iota\otimes\Delta})\tilde{\Delta}$.
:::

*Proof. *That $(\widetilde{\Delta\otimes\iota})(b)\in\mathrm{Nat}\,E\otimes^2$ for $b\in\mathrm{Nat}\,E\otimes$ follows from the following computation: $$\begin{aligned}
 \lefteqn{(E\otimes^2) (s\times t\times u) \, \,\circ\,(\widetilde{\Delta\otimes\iota})(b)_{Y,Z,W} = 
   E(s\otimes t\otimes u) \, \,\circ\,\, b_{Y\otimes Z,W}  } \\ 
  && = b_{Y'\otimes Z',W'} \, \,\circ\,E(s\otimes t\otimes u) = (\widetilde{\Delta\otimes\iota})(b)_{Y',Z',W'} \,\circ\,(E\otimes^2) (s\times t\times u), 
\end{aligned}$$ whenever $s: U\rightarrow U', t: V\rightarrow V', u: W\rightarrow W'$. The argument for $(\widetilde{\iota\otimes\Delta})(b)$ is completely analogous. Clearly, both maps $(\widetilde{\Delta\otimes\iota}), (\widetilde{\iota\otimes\Delta})$ are unital $*$-homomorphisms. The coassociativity property follows from $$(\widetilde{\Delta\otimes\iota})\tilde{\Delta}(b)_{U,V,W}=\tilde{\Delta}(b)_{U\otimes V,W}=b_{(U\otimes V)\otimes W}
   =b_{U\otimes (V\otimes W)}=\tilde{\Delta}(b)_{U,V\otimes W}=(\widetilde{\Delta\otimes\iota})\tilde{\Delta}(b)_{U,V,W}$$ with $b\in\mathrm{End}\,E$, where we have used the strictness of ${\cal C}$.

::: prop
[]{#p-ve label="p-ve"} There are unital $*$-homomorphisms $\tilde{\varepsilon}: \ \mathrm{Nat}\,E\rightarrow\mathrm{End}(E({\bf 1}))$ and $\widetilde{\varepsilon\otimes\iota}, \widetilde{\iota\otimes\varepsilon}:\ \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E$ defined by $$\begin{array}{lll}
  \displaystyle\tilde{\varepsilon}: & \mathrm{Nat}\,E\rightarrow\mathrm{End}(E({\bf 1})), & b=(b_X)\ \mapsto\ b_{\bf 1}, \vspace{4pt}\\
  \displaystyle\widetilde{\varepsilon\otimes\iota}: & \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E, & b=(b_{X,Y})\ \mapsto\ (\widetilde{\varepsilon\otimes\iota})(b)=
   ((\widetilde{\varepsilon\otimes\iota})(b)_X), \quad (\widetilde{\varepsilon\otimes\iota})(b)_X=b_{{\bf 1},X},   \vspace{4pt} \\
  \displaystyle\widetilde{\iota\otimes\varepsilon}: & \mathrm{Nat}\,E\otimes\rightarrow\mathrm{Nat}\,E, & b=(b_{X,Y})\ \mapsto\ (\widetilde{\iota\otimes\varepsilon})(b)=
   ((\widetilde{\iota\otimes\varepsilon})(b)_X), \quad (\widetilde{\iota\otimes\varepsilon})(b)_X=b_{X,{\bf 1}}. 
\end{array}$$ They satisfy $(\widetilde{\varepsilon\otimes\iota})\tilde{\Delta}=(\widetilde{\iota\otimes\varepsilon})\tilde{\Delta}=\iota$.
:::

*Proof. *Clearly, the map $\tilde{\varepsilon}: b=(b_X)\ \mapsto\ b_{\bf 1}\in\mathrm{End}\,E({\bf 1})$ is a unital $*$-homomorphism. The proofs that $(\widetilde{\varepsilon\otimes\iota})(b),(\widetilde{\iota\otimes\varepsilon})(b)$ are in fact in $\mathrm{Nat}\,E$ and that the maps $b\mapsto(\widetilde{\varepsilon\otimes\iota})(b), \ b\mapsto(\widetilde{\iota\otimes\varepsilon})(b)$ are $*$-homomorphisms proceed along the same lines as for coproducts and are therefore omitted. For $b\in\mathrm{Nat}\,E$ the computation $$(\widetilde{\varepsilon\otimes\iota})\tilde{\Delta}(b)= \tilde{\Delta}(b)_{{\bf 1},X}=b_{{\bf 1}\otimes X}=b_X
  =b_{X\otimes{\bf 1}}= \tilde{\Delta}(b)_{X,{\bf 1}} = (\widetilde{\iota\otimes\varepsilon})\tilde{\Delta}(b),$$ where we used the strictness of the unit ${\bf 1}$, concludes the proof.

We have thus seen that we can define a 'coproduct' $\tilde{\Delta}: \mathrm{Nat}\,E\rightarrow\mathrm{Nat}\,E\otimes$ and a 'counit' $\tilde{\varepsilon}: \mathrm{Nat}\,E\rightarrow\mathrm{End}E({\bf 1})$ satisfying analogues of the usual properties. A priori, however, $\mathrm{Nat}\,E\otimes$ has nothing to do with $\mathrm{Nat}\,E\otimes\mathrm{Nat}\,E$, regardless of how we interpret the tensor product. The following result indicates how to proceed. We now assume that ${\cal C}$ is semisimple. As before, by $I_{\cal C}$ we denote the set of isomorphism classes of irreducible objects of ${\cal C}$. For every $i\in I_{\cal C}$ we pick a representative $X_i$.

::: defin
Given a tensor $*$-category ${\cal C}$, an embedding functor (for ${\cal C}$) is a faithful $*$-preserving tensor functor $E: {\cal C}\rightarrow{\cal H}$. A concrete tensor $*$-category is a tensor $*$-category together with an embedding functor.
:::

::: prop
[]{#p-canon-isom label="p-canon-isom"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E: {\cal C}\rightarrow{\cal H}$ an embedding functor. With the $*$-algebra $A=\bigoplus_{i\in I_{\cal C}} B(E(X_i))$ we have the following canonical $*$-isomorphisms: $$\begin{array}{lclcl}
  \displaystyle\mathrm{Nat}\,E & \stackrel{\psi_1}{\longrightarrow}& M(A) & = & \prod_{i\in I_{\cal C}}
     B(E(X_i)), \vspace{5pt}\\ 
  \displaystyle\mathrm{Nat}\,E \otimes & \stackrel{\psi_2}{\longrightarrow}& M(A\otimes A) & = & \prod_{i,j\in I_{\cal C}} B(E(X_i))\otimes                   B(E(X_j)), \vspace{5pt}\\
  \displaystyle\mathrm{Nat}\,E\otimes^2 &\stackrel{\psi_3}{\longrightarrow} & M(A\otimes A\otimes A) & =& \prod_{i,j,k\in I_{\cal C}}          B(E(X_i))\otimes B(E(X_j))\otimes B(E(X_k)).
\end{array}$$
:::

*Proof. *The isomorphism $\psi_1$ was established in Propositions [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} and [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} and suppressed subsequently. As to $\psi_2$, we have $$\begin{array}{cclclcc} 
  \displaystyle\mathrm{Nat}\,E\otimes  & = & \prod_{i,j\in I_{\cal C}} \mathrm{End}\,E(X_i\otimes X_j) 
  & \cong & \prod_{i,j\in I_{\cal C}} \mathrm{End}\,(E(X_i)\otimes E(X_j))  \\ 
\displaystyle& = & \prod_{i,j\in I_{\cal C}} B(E(X_i)\otimes E(X_j)) &=& \prod_{i,j \in I_{\cal C}} 
      B(E(X_i))\otimes B(E(X_j))\ &=& M(A\otimes A). 
\end{array}$$ Here we used the identification $B(H\otimes K)\equiv B(H)\otimes B(K)$ for finite dimensional Hilbert spaces and the identifications made after Propositions [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} and [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"}. The isomorphism between $\mathrm{End}\,E(X_i\otimes X_j)$ and $\mathrm{End}\,E(X_i)\otimes E(X_j)$ is induced in the canonical way from the isomorphism $d^E_{X_i,X_j}: E(X_i)\otimes E(X_j)\rightarrow E(X_i\otimes X_j)$ which makes $E$ monoidal. Unitarity of the $d^E_{X_i,X_j}$ implies that $\psi_2$ is $*$-preserving. The argument for $\psi_3$ is completely analogous.

::: rema
In the above proof it was crucial that the canonical $*$-homomorphisms $\otimes: \ \mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y \rightarrow\mathrm{End}(X\otimes Y)$ are $*$-isomorphisms for all $X,Y\in{\cal H}$. A semisimple tensor $*$-category has this property iff every object is a finite direct sum of copies of the tensor unit ${\bf 1}$. \[*Proof.* The 'if' clause is easy. As to the 'only if' part, let $Z$ be irreducible and consider $X\cong Y\cong {\bf 1}\oplus Z$, thus $X\otimes Y\cong{\bf 1}\oplus Z\oplus Z\oplus Z^2$. If $Z\not\cong{\bf 1}$ then $\mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y\cong{\mathbb C}^2\otimes{\mathbb C}^2$ is commutative whereas $\mathrm{End}(X\otimes Y)$ is non-commutative since $X\otimes Y$ contains the irreducible $Z$ with multiplicity at least two. This contradicts $\mathrm{End}\,X\otimes_{\mathbb C}\mathrm{End}\,Y \cong\mathrm{End}(X\otimes Y)$.\] This property is known to characterize the (semisimple) tensor $*$-category ${\cal H}$ uniquely up to equivalence. We thus see that with $E=Id :{\cal C}\rightarrow{\cal C}$, we cannot conclude that $\mathrm{Nat}\,E\otimes \ \cong \ M(A\otimes A)$. This is consistent with the computation of $\mathrm{Nat}\,\otimes$ in Example [\[e-otimes\]](#e-otimes){reference-type="ref" reference="e-otimes"}.
:::

From now on we restrict ourselves to the case we are ultimately interested in.

::: defin
[]{#d-ve-D label="d-ve-D"} Let ${\cal C}$ be a semisimple tensor $*$-category and let $E: {\cal C}\rightarrow{\cal H}$ be an embedding functor. Using the preceding results we define unital $*$-homomorphisms as follows. $$\begin{array}{ll}
  \displaystyle\overline{\varepsilon}: \ M(A)\rightarrow{\mathbb C}, & \quad a\mapsto \tilde{\varepsilon}\,\circ\,\psi_1^{-1}(a), \vspace{4pt}\\
  \displaystyle\overline{\Delta}: \ M(A)\rightarrow M(A\otimes A), & \quad a\mapsto \psi_2\,\circ\,\tilde{\Delta}\,\circ\,\psi_1^{-1}(a).
\end{array}$$ Here we have implicitly used the irreducibility of $E({\bf 1}_{\cal C})\cong{\bf 1}_{\cal H}\cong{\mathbb C}$, giving rise to the isomorphism $\psi_0:\mathrm{End}\,E({\bf 1})\rightarrow{\mathbb C},\ c\,\mathrm{id}_{E({\bf 1})}\mapsto c$.
:::

::: rema
1\. In the sequel we will usually use the isomorphisms $\psi_1, \psi_2$ to identify $M(A)\equiv\mathrm{Nat}\,E,\ M(A\otimes A)\equiv\mathrm{Nat}\,E\otimes$ and suppress the symbols $\psi_1, \psi_2$. Thus for $a\in M(A), i\in I,\  a_i$ will denote both the $i$-component of $a$ in $\prod_{i\in I} B(E(X_i))$ and the action $a_{X_i}$ on $E(X_i)$ of the natural transformation $\psi_1^{-1}(a)\in\mathrm{Nat}\,E$.

2\. Let $a\in M(A)$. As $\Delta(a)_{ij}=a_{X_i\otimes X_j}$ and $(a\otimes a)_{ij}=a_i\otimes a_j$ we find $$\Delta(a)=a\otimes a \quad\Leftrightarrow\quad a_{X_i\otimes X_j}=a_{X_i}\otimes a_{X_j} \quad\forall i,j\in I.$$ Thus the grouplike elements of $M(A)$ are in one-to-one correspondence with those natural transformations of the embedding functor which respect the tensor structure.
:::

::: lem
[]{#l-nondeg label="l-nondeg"} The restriction $\Delta=\overline{\Delta}\upharpoonright A$ is a non-degenerate $*$-homomorphism from $A$ to $M(A\otimes A)$, i.e. $\Delta(A)(A\otimes A)=(A\otimes A)\Delta(A)=(A\otimes A)$.
:::

*Proof. *To simplify the notation we write $H_i=B(E(X_i))$ and use the isomorphisms $\psi_1, \psi_2$ to identify $M(A)$ with $\mathrm{Nat}\,E$ and $M(A\otimes A)$ with $\mathrm{Nat}\,E\otimes$. We will only prove $\Delta(A)(A\otimes A)=(A\otimes A)$, the proof of the other identity being completely analogous. As $A=\oplus_i B(H_i)$, it suffices to show that for every $i,j\in I_{\cal C}$ there is a $c\in A$ with $\Delta(c)(I_i\otimes I_j)=I_i\otimes I_j$, since this implies $a_i\otimes b_j=\Delta(c)(I_i\otimes I_j)(a_i\otimes b_j)\in\Delta(A)(A\otimes A)$ for all $a_i\in B(H_i), b_j\in B(H_j)$. Recall from the Propositions [\[p-canon-isom\]](#p-canon-isom){reference-type="ref" reference="p-canon-isom"} and [\[p-direct\]](#p-direct){reference-type="ref" reference="p-direct"} that $M(A)$ is isomorphic to the $*$-algebra of natural transformations of $E$, and these are uniquely determined by their actions on the irreducibles: $M(A)\ni b\leftrightarrow (b_i)$, where $b_i\equiv b_{X_i}$. Similarly, $M(A\otimes A)\ni b\leftrightarrow (b_{ij})$ with $b_{ij}\equiv b_{X_i,X_j}$. By the definition of $\tilde{\Delta}$ we have $\tilde{\Delta}(b)_{ij}=b_{X_i\otimes X_j}$. As usual, let $(v_{ij}^{k\alpha}, \alpha=1,\ldots,N_{ij}^k)$ be an orthonormal basis in $\mathrm{Mor}(X_k,X_i\otimes X_j)$ for all $i,j,k\in I_{\cal C}$. Since $b\in M(A)\equiv\mathrm{End}\,E$ is a natural transformation we have $$\tilde{\Delta}(b)_{ij}=b_{X_i\otimes X_j}= b_{X_i\otimes X_j}\,\circ\,\mathrm{id}_{E(X_i\otimes X_j)}=
   b_{X_i\otimes X_j}\,\circ\,E\left(\sum_{k\alpha} v_{ij}^{k\alpha}\,\circ\,v_{ij}^{k\alpha*}\right)
   = \sum_{k\alpha} E(v_{ij}^{k\alpha})\,\circ\,b_k\,\circ\,E(v_{ij}^{k\alpha*}).$$ Now fix $i_0, j_0\in I_{\cal C}$ and let $b_k=\mathrm{id}_{E(X_k)}$ if $X_k$ is contained in $X_{i_0}\otimes X_{j_0}$ and $b_k=0$ otherwise. Since $X_k\prec X_{i_0}\otimes X_{j_0}$ only for finitely many $k$ we have $b=(b_k)\in A$ and $$\tilde{\Delta}(b)_{i_0j_0}=\sum_{k\alpha} E(v_{i_0j_0}^{k\alpha})\,\circ\,\mathrm{id}_{E(X_k)}\,\circ\,
   E(v_{i_0j_0}^{k\alpha*}) =\sum_{k\alpha} E(v_{i_0j_0}^{k\alpha}\,\circ\,v_{i_0j_0}^{k\alpha*})
  = E(\mathrm{id}_{X_{i_0}\otimes X_{j_0}}) = \mathrm{id}_{E(X_{i_0}\otimes X_{j_0})}.$$ Having identified $\mathrm{Nat}\,E\otimes\equiv M(A\otimes A)$ this precisely means that the $(i_0,j_0)$-component of $\Delta(b)\in M(A\otimes A)=\prod_{ij} B(H_i)\otimes B(H_j)$ is the identity $I_{i_0}\otimes I_{j_0}$ and therefore $\Delta(b)(I_{i_0}\otimes I_{j_0})=(I_{i_0}\otimes I_{j_0})$ as desired.

::: cor
[]{#c-extens label="c-extens"} Defining $*$-homomorphisms $\varepsilon: A\rightarrow{\mathbb C}$ and $\Delta: A\rightarrow M(A\otimes A)$ by $\varepsilon=\overline{\varepsilon}\upharpoonright A$ and $\Delta=\overline{\Delta}\upharpoonright A$, $\overline{\varepsilon}$ and $\overline{\Delta}$ are the unique extensions of $\varepsilon$ and $\Delta$, respectively, to $M(A)$.
:::

*Proof. *It is clear that $\varepsilon$ is not identically zero, thus non-degenerate. Non-degeneracy of $\Delta$ has been proven in Lemma [\[l-nondeg\]](#l-nondeg){reference-type="ref" reference="l-nondeg"}. Now the claim follows from the fact [@VD2] that a non-degenerate $*$-homomorphism $\phi: A\rightarrow M(B)$ has a unique extension to a unital $*$-homomorphism $\overline{\phi}: M(A)\rightarrow M(B)$.

::: prop
[]{#p-cdisc label="p-cdisc"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E:{\cal C}\rightarrow{\cal H}$ an embedding functor. Then the $*$-algebra $A=\oplus_{i\in I_{\cal C}} B(E(X_i))$ is a discrete quantum semigroup, i.e. has a non-degenerate coproduct $\Delta: A\rightarrow M(A\otimes A)$ in the sense of [@VD2] and a counit $\varepsilon: A\rightarrow{\mathbb C}$.
:::

*Proof. *By Lemma [\[l-nondeg\]](#l-nondeg){reference-type="ref" reference="l-nondeg"}, $\Delta$ is non-degenerate, thus also $\Delta\otimes\iota: A\otimes A\rightarrow M(A\otimes A)\otimes A\subset M(A\otimes A\otimes A)$ is non-degenerate and extends uniquely to $\overline{\Delta\otimes\iota}: M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$. Another unital $*$-homomorphism $M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$ is given by $\psi_3\,\circ\,(\widetilde{\Delta\otimes\iota})\,\circ\,\psi_2^{-1}$. The latter clearly restricts to $\Delta\otimes\iota$ on $A\otimes A$, thus it coincides with $\overline{\Delta\otimes\iota}$ on all of $M(A\otimes A)$. In the same way we make sense of $\overline{\iota\otimes\Delta}: M(A\otimes A)\rightarrow M(A\otimes A\otimes A)$ and see that it coincides with $\psi_3\,\circ\,(\widetilde{\iota\otimes\Delta})\,\circ\,\psi_2^{-1}$. Now, the coassociativity property proved in Proposition [\[p-coassoc\]](#p-coassoc){reference-type="ref" reference="p-coassoc"} implies $$\overline{\Delta\otimes\iota}\,\circ\,\overline{\Delta}= \overline{\iota\otimes\Delta}\,\circ\,\overline{\Delta}:\
    M(A)\rightarrow M(A\otimes A\otimes A),$$ which is the proper formulation of coassociativity for $(A,\Delta)$.

As observed earlier, the $*$-homomorphism $\varepsilon: A\rightarrow{\mathbb C}$ is non-degenerate, thus $\varepsilon\otimes\iota,\, \iota\otimes\varepsilon:\ A\otimes A\rightarrow A$ are non-degenerate too and have unique extensions $\overline{\varepsilon\otimes\iota},\, \overline{\iota\otimes\varepsilon}$ to $M(A\otimes A)$. Again, it is clear that $\overline{\varepsilon\otimes\iota}=\psi_1\,\circ\,(\widetilde{\varepsilon\otimes\iota})\,\circ\,\psi_2^{-1}$ and similarly for $\overline{\iota\otimes\varepsilon}$. Thus with Proposition [\[p-ve\]](#p-ve){reference-type="ref" reference="p-ve"} we conclude $$\overline{\varepsilon\otimes\iota}\,\circ\,\overline{\Delta}=\overline{\iota\otimes\varepsilon}\,\circ\,
   \overline{\Delta}=\mathrm{id}: \ M(A)\rightarrow M(A).$$ We conclude that $(A,\Delta)$ is a discrete quantum semigroup.

::: thm
[]{#t-mon-equiv label="t-mon-equiv"} Let ${\cal C}$ be a semisimple tensor $*$-category and $E:{\cal C}\rightarrow{\cal H}$ an embedding functor. Let $(A,\Delta)$ be the corresponding discrete quantum semigroup. Then the functor $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ defined by $$F(X)=(E(X),\pi_X), \quad \pi_X(a)=a_X \ \forall a\in A, \quad\quad F(s)=E(s)$$ provides an equivalence of tensor $*$-categories such that $K\,\circ\,F= E$.
:::

*Proof. *With $A$ and $F: {\cal C}\rightarrow\mathrm{Rep}_f A$ as defined in Theorem [\[t-equiv\]](#t-equiv){reference-type="ref" reference="t-equiv"} we have an equivalence of categories. It remains to show that $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ is monoidal for the monoidal structure of $\mathrm{Rep}_f(A,\Delta)$ in Definition [\[d-repf\]](#d-repf){reference-type="ref" reference="d-repf"}. Thus we must exhibit isomorphisms $d^F_{X,Y}: F(X)\otimes F(Y)\rightarrow F(X\otimes Y)$ satisfying the conditions of Definition [\[d-mon-func\]](#d-mon-func){reference-type="ref" reference="d-mon-func"}. In view of $F(X)=(E(X),\pi_X)$, an obvious candidate is the isomorphism $d^E_{X,Y}: E(X)\otimes E(Y)\rightarrow E(X\otimes Y)$ which we have by virtue of the assumed monoidality of $E$. If we set $d^F_{X,Y}=d^E_{X,Y}$ for all $X,Y\in {\cal C}$, the equations in Definition [\[d-mon-func\]](#d-mon-func){reference-type="ref" reference="d-mon-func"} are clearly satisfied. It only remains to prove that $d^F_{X,Y}$ is in $\mathrm{Mor}_{\mathrm{Rep}_f(A,\Delta)}(F(X)\otimes F(Y), F(X\otimes Y))$, i.e. $$d^F_{X,Y} \,\circ\,(\pi_X\times\pi_Y)(a)=\pi_{X\otimes Y}(a)\,\circ\,d^F_{X,Y} \quad\forall
   a\in A.$$

Keeping in mind the various identifications we have made so far, we get $$d^F_{X,Y} \,\circ\,(\pi_X\times\pi_Y)(a)=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\Delta(a)
=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\overline{\Delta}(a)$$ $$=d^F_{X,Y} \,\circ\,\overline{(\pi_X\otimes\pi_Y)}\psi_2\tilde{\Delta}(a)
=\pi_{X,Y}\tilde{\Delta}(a)\,\circ\,d^F_{X,Y}
=a_{X\otimes Y}\,\circ\,d^F_{X,Y} =\pi_{X\otimes Y}(a)\,\circ\,d^F_{X,Y}$$ for all $a\in A$. (The reader is invited to check the required identity explicitly for $X=X_i, Y=X_j$, as suffices by naturality of the isomorphisms $d^F$.)
