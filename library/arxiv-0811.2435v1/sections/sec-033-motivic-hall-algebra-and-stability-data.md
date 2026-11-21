---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-033-motivic-hall-algebra-and-stability-data
section_title: "Motivic Hall algebra and stability data"
section_number: null
pages: 84-92
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.974
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
In this section the field $\k$ can have arbitrary characteristic.

Let $\CC$ be an ind-constructible triangulated $\A$-category over a field $\k$. We are going to describe a motivic generalization of the derived Hall algebras from [@To].

As usual, we have a constructible countable decomposition $Ob(\CC)=\sqcup_{i\in I}Y_i$ with group $GL(N_i)$ acting on $Y_i$. Let us consider a $Mot(Spec(\k))$-module $\oplus_i Mot_{st}(Y_i,GL(N_i))$ (see section 4.2) and extend it by adding negative powers ${\mathbb L}^n, n<0$ of the motive of the affine line ${\mathbb L}$. We denote the resulting $Mot(Spec(\k))$-module by $H(\CC)$. We understand elements of $H(\CC)$ as *measures* (and not as functions), because in the definition of the product we will use the pushforward maps.

We would like to make $H(\CC)$ into an associative algebra, called the *motivic Hall algebra*. We need some preparations for that. First we observe that if $[\pi_i: Z_i\to Ob(\CC)], i=1,2$ are two elements[^1] of $H(\CC)$ then one has a constructible set $tot((\pi_1\times \pi_2)^{\ast}({\cal EXT}^1))$ which is the total space of the pull-back of the ind-constructible bundle ${\cal EXT}^1$ over $Ob(\CC)\times Ob(\CC)$. Then the map ${{\cal C}one}$ (see Section 3.1) after the shift $[1]$ maps the total space to $Ob(\CC)$.

For any $N\in \Z$ we introduce the "truncated\" Euler characteristic $$(E,F)_{\le N}:=\sum_{i\le N}(-1)^i\dim \op{Ext}^i(E,F)\,\,.$$ In the future we will use the notation $(E,F)_i$ for $\dim \op{Ext}^i(E,F)$, hence $(E,F)_{\le N}=\sum_{i\le N}(-1)^i (E,F)_i$.

With the pair $[\pi_i: Y_i\to X_i], i=1,2$ as above we can associate a collection of constructible sets $$W_n  =\big\{(y_1,y_2,\alpha)\,|\,y_i\in Y_i, \alpha\in \op{Ext}^1(\pi_2(y_2),\pi_1(y_1))\,,\,
 (\pi_2(y_2),\pi_1(y_1))_{\le 0}=n\big\}\,\,,$$ where $n\in \Z$ is arbitrary. Clearly $$[tot((\pi_1\times \pi_2)^{\ast}({\cal EXT}^1))\to Ob(\CC)]=\sum_{n\in \Z}[W_n\to Ob(\CC)]\,\,.$$ We define the product $$[Y_1\to Ob(\CC)]\cdot [Y_2\to Ob(\CC)]=\sum_{n\in \Z}[W_n\to Ob(\CC)]{\mathbb L}^{-n}\,\,,$$ where the map $W_n\to Ob(\CC)$ is given by the formula $$(y_1,y_2,\alpha)\mapsto Cone(\alpha: \pi_2(y_2)[-1]\to \pi_1(y_1))\,\,.$$

::: prp
The above formula makes $H(\CC)$ into an associative algebra.
:::

*Proof.* We are going to prove the result for the "delta functions\" $$\nu_E=[pt\to Ob(\CC)], pt\mapsto E\,\,,$$ where $E$ is an object of $\CC(\kk)$. The case of equivariant families is similar. In other words, we would like to prove that $$(\nu_{E_1}\cdot\nu_{E_2})\cdot \nu_{E_3}=\nu_{E_1}\cdot(\nu_{E_2}\cdot \nu_{E_3})\,\,.$$ Replacing the category by its minimal model we may replace in all considerations $\op{Hom}^{\bullet}$ by $\op{Ext}^{\bullet}$. Let us also remark that an element $\alpha\in \op{Ext}^1(E,F)$ defines an extension $E_{\alpha}$ which we can interpret as a deformation of the object $E\oplus F$ (the trivial extension). Therefore for any object $G$ the group $\op{Ext}^{\bullet}(G,E_{\alpha})$ is equal to the cohomology of the complex $(\op{Ext}^{\bullet}(G,E\oplus F),d_{\alpha})$, where $d_{\alpha}$ is the operator of multiplication (up to a sign) by $\alpha$.

Notice that $$\nu_{E_1}\cdot\nu_{E_2}={\mathbb L}^{-(E_2,E_1)_{\le 0}}[\op{Ext}^1(E_2,E_1)\to Ob(\CC)]:={\mathbb L}^{-(E_2,E_1)_{\le 0}}\int_{\alpha\in \op{Ext}^1(E_2,E_1)}\nu_{E_{\alpha}}\,\,,$$ where $E_{\alpha}$ is the object corresponding to the extension $\alpha$, i.e. $$E_{\alpha}=Cone(\alpha: E_2[-1]\to E_1)\,\,.$$ It follows that $$(\nu_{E_1}\cdot\nu_{E_2})\cdot \nu_{E_3}={\mathbb L}^{-(E_2,E_1)_{\le 0}}\int_{
\alpha\in \op{Ext}^1(E_2,E_1),\,\beta\in \op{Ext}^1(E_3,E_{\alpha}) }{\mathbb L}^{-(E_3,E_{\alpha})_{\le 0}}\nu_{E_{\beta}}\,\,.$$

We observe that $$(E_3,E_{\alpha})_{\le 0}=(E_3,E_2\oplus E_1)_{\le 0}-l_{\alpha}=(E_3,E_2)_{\le 0}+ (E_3,E_1)_{\le 0}-l_{\alpha}\,\,,$$ where the "error term\" $l_{\alpha}\geqslant 0$ can be computed in terms of the linear map $d_{\alpha}$. Therefore one can write $$(\nu_{E_1}\cdot\nu_{E_2})\cdot \nu_{E_3}={\mathbb L}^{-(E_2,E_1)_{\le 0}-(E_3,E_1)_{\le 0}-(E_3,E_2)_{\le 0}}\int_{\alpha\in \op{Ext}^1(E_2,E_1),\beta\in \op{Ext}^1(E_3,E_{\alpha})}{\mathbb L}^{l_{\alpha}}\nu_{E_{\beta}}\,\,.$$

One can write a similar expression for $\nu_{E_1}\cdot(\nu_{E_2}\cdot \nu_{E_3})$. In this case the "error term\" will be denoted by $r_{\alpha}$ instead of $l_{\alpha}$.

Notice that the differential $$d_{\alpha}: \op{Ext}^0(E_3,E_2)\oplus \op{Ext}^0(E_3,E_1)\to \op{Ext}^1(E_3,E_1)\oplus \op{Ext}^1(E_3,E_2)$$ satisfies the property that the only non-trivial component is the map $\alpha_R: \op{Ext}^0(E_3,E_2)\to \op{Ext}^1(E_3,E_1)$. Here we denote by $\alpha_R$ the linear operator of multiplication by $\alpha\in \op{Ext}^1(E_2,E_1)$ from the right. We will use the same convention for the linear operator $\alpha_R: \op{Ext}^1(E_3,E_2)\to \op{Ext}^2(E_3,E_1)$. Hence we see that $$\dim \op{Ext}^1(E_3,E_{\alpha})= \dim \op{Ker}\left(\alpha_R: \op{Ext}^1(E_3,E_2)\to \op{Ext}^2(E_3,E_1)\right)+$$ $$+\dim \op{Coker}\left(\alpha_R: \op{Ext}^0(E_3,E_2)\to \op{Ext}^1(E_3,E_1)\right)\,\,.$$ Let us now consider the constructible set $$X_{1,2,3}=\{(\alpha,\gamma, \delta)\in \op{Ext}^1(E_2,E_1)\oplus \op{Ext}^1(E_3,E_2)\oplus \op{Ext}^1(E_3,E_1)|\alpha\circ \gamma=0\}\,.$$

Notice that a triple $(\alpha,\gamma, \delta)\in X_{1,2,3}$ defines the deformation of the object $E_1\oplus E_2\oplus E_3$ preserving the filtration $$E_1\subset E_1\oplus E_2\subset E_1\oplus E_2\oplus E_3\,\,.$$ More precisely, the triple gives rise to a twisted complex, which is defined by the corresponding to $(\alpha,\gamma, \delta)$ solution to the Maurer-Cartan equation (strictly upper-triangular matrix acting on $E_1\oplus E_2\oplus E_3$). The latter observation means that there is an ind-constructible map $X_{1,2,3}\to Ob(\CC)$ which assigns to a point $(\alpha,\gamma, \delta)$ the corresponding twisted complex.

Let us now fix $\alpha\in \op{Ext}^1(E_2,E_1)$ and consider the ind-constructible subset $X_{1,2,3}^{\alpha}\subset X_{1,2,3}$ which consists of the triples with fixed $\alpha$. There is a natural projection $(\alpha,\gamma, \delta)\mapsto (\gamma,\delta)$, which gives rise to the constructible map $X_{1,2,3}^{\alpha}\to \op{Ext}^1(E_3,E_{\alpha})$. This is a constructible affine bundle with the fibers isomorphic to $\op{Im}(\alpha_R: \op{Ext}^0(E_3,E_2)\to \op{Ext}^1(E_3,E_1))$. Also, one can see directly that the dimension of the latter space is $$l_{\alpha}=(E_3,E_2\oplus E_1)_{\le 0}- (E_3,E_\alpha)_{\le 0}\,\,.$$ Hence we have the following identity in $H(\CC)$: $$\int_{  \alpha\in \op{Ext}^1(E_2,E_1),\, \beta\in \op{Ext}^1(E_3,E_{\alpha})}{\mathbb L}^{l_{\alpha}}\nu_{E_{\beta}}=[X_{1,2,3}\to Ob(\CC)]\,\,.$$ Therefore, $$(\nu_{E_1}\cdot\nu_{E_2})\cdot \nu_{E_3}={\mathbb L}^{-(E_2,E_1)_{\le 0}-(E_3,E_1)_{\le 0}-(E_3,E_2)_{\le 0}}\cdot[X_{1,2,3}\to Ob(\CC)]\,\,.$$ Similar considerations show that $$\nu_{E_1}\cdot(\nu_{E_2}\cdot \nu_{E_3})=  {\mathbb L}^{-(E_2,E_1)_{\le 0}-(E_3,E_1)_{\le 0}-(E_3,E_2)_{\le 0}}\cdot[X_{1,2,3}\to Ob(\CC)]\,\,.$$ This proves the associativity of the product in $H(\CC)$. $\blacksquare$

For a constructible stability structure on $\CC$ with an ind-constructible class map $\op{cl}:K_0(\CC)\to \Gamma$, a central charge $Z:\Gamma\to \C$, a strict sector $V\subset \R^2$ and a branch $\op{Log}$ of the logarithm function on $V$ we have the category $\CC_V:=\CC_{V,\op{Log}}$ defined in Section 3.4. Hence we have the *completion* $$\widehat{H}(\CC_V):=\prod_{\gamma\in (\Gamma\cap C(V,Z,Q))\cup\{0\}}H(\CC_V\cap \op{cl}^{-1}(\gamma))\,\,.$$

Then we have an invertible element $A_V^{\op{Hall}}\in \widehat{H}(\CC_V)$ such that $$A_V^{\op{Hall}}:=1+\dots=\sum_{i\in I}  \mathbf{1}_{(Ob(\CC_V)\cap Y_i,GL(N_i))}\,\,,$$ where $\mathbf{1}_{\cal S}$ is the identity function (see 4.2) but interpreted as a counting measure[^2]. In short, element $A_V^{\op{Hall}}$ is given by the counting measure restricted to $\CC_V$. The summand $1$ comes from zero object.

::: prp
Elements $A_V^{\op{Hall}}$ satisfy the Factorization Property: $$A_{V}^{\op{Hall}}=A_{V_1}^{\op{Hall}}\cdot A_{V_2}^{\op{Hall}}$$ for a strict sector $V=V_1\sqcup V_2$ (decomposition in the clockwise order).
:::

*Proof.* The proof follows from the following observations:

1\) For any $E_i\in Ob(\CC_{V_i}(\kk)), i=1,2$ one has $(E_2,E_1)_{\le 0}=\dim\op{Ext}^0(E_2,E_1)$ because $\op{Ext}^i(E_2,E_1)=0$ for $i< 0$.

2\) The set $\{[E]\in Iso(\CC_V(\kk))\}$ is in one-to-one correspondence with the set of isomorphisms classes of the triples $(E_1,E_2,\alpha)$ such that $E_i\in Ob(\CC_{V_i}(\kk)), i=1,2$ and $\alpha\in \op{Ext}^1(E_2,E_1)$ (the map between the sets assigns to the triple the extension $E_{\alpha}$).

3\) The automorphism group of the triple $(E_1,E_2,\alpha)$ is the stabilizer of $\alpha$ for the natural action of the group $\op{Aut}(E_2)\times \op{Aut}(E_1)$ on the vector space $\op{Ext}^1(E_2,E_1)$.

4\) There is an exact sequence of groups $$1\to \op{Ext}^0(E_2,E_1)\to \op{Aut}(E_\alpha)\to\op{Aut}( E_1,E_2,\alpha) \to 1$$

In order to apply these observations one uses the fact that an object $E\in \CC_V(\kk)$ contains a unique subobject $E_1\in Ob(\CC_{V_1}(\kk))$ such that the quotient object $E_2$ belongs to $\CC_{V_2}(\kk)$, and then the factor ${\mathbb L}^{-(E_2,E_1)_{\le 0}}$ cancels the ratio between the stabilizer of $\alpha$ and the automorphism group of the extension $E_\alpha$. $\blacksquare$

::: cor
Let us endow $H(\CC)$ with an automorphism $\eta$ given by the shift functor $[1]$. Then the collection $(A_V^{\op{Hall}})$ gives rise to a symmetric stability data on $H(\CC)$ considered as a graded Lie algebra (see Definition 2 and Remark 8 in Section 2.2). Moreover we obtain a local homeomorphism $Stab(\CC,\op{cl})\to Stab(H(\CC))$.
:::

The above considerations can be illustrated in the case of finite fields. Namely, let us assume that $\CC$ is a triangulated category over a finite field ${\bf F}_q$. We define the Hall algebra $H(\CC)$ as an associative unital algebra over $\Q$, which is a $\Q$-vector space spanned by isomorphism classes $[E]$ of objects $E\in Ob(\CC)$. The multiplication is given by the formula $$[E]\cdot[F]=q^{-(F,E)_{\le 0}}\sum_{\alpha\in \op{Ext}^1(F,E)}[E_{\alpha}]\,\,,$$ where $E_{\alpha}$ is the extension corresponding to $\alpha\in \op{Ext}^1(F,E)$.

We define a stability condition on $\CC$ in the same way as in the Introduction (or Section 3.4) without imposing any constructibility condition (since we do not assume that our category is ind-constructible). Inside of the set $Stab(\CC)$ of stability conditions on $\CC$ we consider a subset $Stab^0(\CC)$ consisting of such stability conditions that the set $\{E\in \CC_{\gamma}^{ss}|\op{Arg}(E)=\varphi\}$ is finite for any $\gamma\in \Gamma, \varphi\in [0,2\pi)$. This property is analogous to the one in the ind-constructible setting which says that $\CC_{\gamma}^{ss}$ is a constructible set. Then for any strict sector $V$ and a choice of the branch $\op{Log}$ we have an element $A_V^{\op{Hall}}\in \widehat{H}(\CC_V)$ given by $$A_V^{\op{Hall}}=1+\dots=\sum_{[E]\in Iso(\CC_V)}{[E]\over {\#\op{Aut}(E)}}\,\,.$$ Similarly to the motivic case the collection of elements $(A_V^{\op{Hall}})$ satisfies the Factorization property. Hence it defines a stability data on the space $H(\CC)$ considered as a graded Lie algebra.

The relationship of our version of Hall algebra to the Toën derived Hall algebra from [@To] is described in the following proposition.

::: prp
There is a homomorphism of rings $H(\CC)\to H_{To}(\CC)$, where $H_{To}(\CC)$ is the derived Hall algebra over ${\bf F}_q$ defined by Toën in [@To] (see also [@XiXu]), such that $$[\pi: Y\to Ob(\CC)]\mapsto \sum_{y\in Y({\bf F}_q)}[\pi(y)]\#\op{Aut}(y)({\bf F}_q)\,q^{(y,y)_{<0}}\,\,.$$ Moreover, for any strict sector $V$ the above homomorphism admits a natural extension to the completed Hall algebras such that the element $A_V^{\op{Hall}}\in \widehat{H}(\CC_V)$ is mapped to the element of the completed Hall algebra $\widehat{H}_{To}(\CC_V)$ given by $\sum_{[x]\in Iso(\CC_V)}[x]$.
:::

*Proof.* Straightforward. $\blacksquare$

In fact, in the Toën version of the Hall algebra the factorization property $$A_V^{\op{Hall}}=A_{V_1}^{\op{Hall}}A_{V_2}^{\op{Hall}}$$ is essentially trivial. The reason is that the structure constants in $\widehat{H}_{To}(\CC_V)$ for the elements of the basis corresponding to objects in a heart of a $t$-structure are the usual one, i.e. they count the number of 2-step filtrations of a given object with given isomorphism classes of the associate graded factors. The factorization property means that any object in $\CC_V$ has a unique subobject in $\CC_{V_1}$ with quotient in $\CC_{V_2}$.

::: rmk
One can try to go even further in an attempt to "categorify\" the motivic Hall algebra. Here one has to assume that objects of $\CC$ form not just an ind-constructible stack, but a higher stack of locally finite type in the sense of Toën and Vezzosi (see [@ToVe]). The corresponding category will be the monoidal category of motivic sheaves on $Ob(\CC)$. The motivic Hall algebra is the $K_0$-ring of this category. In the case of the non-commutative variety endowed with polarization one can define (for any strict sector $V$) the subcategory ${\cal F}_V$ of "motivic sheaves with central charges in $V$\". Nevertheless, the Factorization Property could fail since the object $A_V^{\op{Hall}}$ can be non-isomorphic to the object $A_{V_1}^{\op{Hall}}\otimes A_{V_2}^{\op{Hall}}$ (but their images in $K_0$ coincide).
:::

Finally, we explain how to rephrase the factorization property in terms of $t$-structures, without the use of stability conditions. Here we understand a $t$-structure $\alpha$ on a small triangulated category $\cal C$ as a pair of strictly full subcategories (i.e. a pair of sets of equivalence classes of objects) $${\cal C}_{-,\alpha},\,\,{\cal C}_{+,\alpha}\subseteq {\cal C}$$ such that for any $E_-\in {\cal C}_{-,\alpha},\,\,E_+\in {\cal C}_{+,\alpha}$ we have $Ext^{\le 0}(E_-,E_+)=0$, and any object $E\in {\cal C}$ can be represented (uniquely) as an extension $$\tau_{-,\alpha}(E)\to E\to \tau_{+,\alpha}(E),\,\,\,\tau_{\pm,\alpha}(E)\in {\cal C}_{\pm,\alpha}\,\,.$$

Any stability condition on $\cal C$ defines two $t$-structures $\alpha_l,\alpha_r$ such that ${\cal C}_{-,\alpha_l}$ (resp. ${\cal C}_{-,\alpha_r}$) consists of extensions of semistable objects $E$ with $\op{Arg}(E)\geqslant 0$ (resp. with $\op{Arg}(E)>0$). These two $t$-structures do not change under the action of the group $$\left\{\left( 
  \begin{array}
  {cc} a_{11} & 0\\ a_{21} & a_{22}
  \end{array}\right) \bigl|\,\, a_{11},a_{22}>0\bigr.\right\}\subset \widetilde{GL_+}(2,\mathbf{R})$$ of transformations preserving the upper half-plane. In particularly, we see that while a connected component in the $Stab({\cal C})$ is a real $2n$-dimensional manifold for $n:=\op{rank}(\Gamma)$, the set of corresponding $t$-structures is at most $(n-1)$-dimensional.

Introduce an order on the set of $t$-structures by $$\alpha_1\le \alpha_2\,\,\Longleftrightarrow \,\,{\cal C}_{-,\alpha_1}\subseteq {\cal C}_{-,\alpha_2}\,\,\Longleftrightarrow\,\, {\cal C}_{+,\alpha_1}\supseteq {\cal C}_{+,\alpha_2}\,\,.$$ The shift functor acts on $t$-structures, and $\alpha[1]\le \alpha$ for any $t$-structure $\alpha$.

Let now $\cal C$ be an ind-constructible category endowed with an ind-constructible homomorphism $cl:K_0({\cal C}(\overline{\bf k}))\to \Gamma$ and $\alpha_1,\alpha_2$ are two ind-constructible $t$-structures. We say $$\alpha_1\le_{constr}\alpha_2$$ iff

-   $\alpha_1\le \alpha_2\le \alpha_1[-1]\,\,,$

-   $\forall\gamma\in \Gamma\,\,\,\,
        {\cal C}_{+,\alpha_1}\cap{\cal C}_{-,\alpha_2}\cap cl^{-1}(\gamma)$ is constructible,

-   the cone generated by $\{\gamma\in \Gamma\,| \,{\cal C}_{+,\alpha_1}\cap{\cal C}_{-,\alpha_2}\cap cl^{-1}(\gamma)\ne 0\}$ is strict.

If $\alpha_1\le_{constr}\alpha_2$ then we define an element $A_{\alpha_1,\alpha_2}$ of an appropriately completed Hall algebra as the sum of the "counting measure" over the objects in ${\cal C}_{+,\alpha_1}\cap{\cal C}_{-,\alpha_2}$. Obviously, elements $A_V$ (for an open, or a closed, or a semi-open strict sector $V$) are of the form $A_{\alpha_1,\alpha_2}$ for appropriate $t$-structures $\alpha_1,\alpha_2$. The factorization property generalizes to $$A_{\alpha_1,\alpha_3}=A_{\alpha_1,\alpha_2}\cdot A_{\alpha_2,\alpha_3}$$ if $\alpha_1 \le_{constr}\alpha_2,\,\,\alpha_2\le_{constr}\alpha_3,\,\,\alpha_1\le_{constr}\alpha_3$.

Notice that in the case of stability conditions the element $A_V$ is preserved under the action of a subgroup of $\widetilde{GL_+}(2,\mathbf{R})$ conjugated to the group of positive diagonal matrices. This action on $Stab({\cal C})/Aut({\cal C})$ has a good chance to be ergodic, as indicates a similar example with the moduli spaces of curves with abelian differentials (see a review [@Zo]).

[^1]: Here we consider for simplicity the case when the groups acting on $Z_1,Z_2$ are trivial, the generalization to the case of non-trivial groups is straightforward.

[^2]: The same is true if one uses the language of higher stacks because for any $E\in Ob(\CC(V))(\kk)$ one has $\op{Ext}^{<0}(E,E)=0$.
