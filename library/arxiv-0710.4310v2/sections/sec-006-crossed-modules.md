---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-006-crossed-modules
section_title: "Crossed modules"
section_number: null
pages: 9-11
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
All Lie groups and Lie algebras are taken to be finite-dimensional.

::: Definition
[]{#LCM label="LCM"} A crossed module ${\Gc= ( \d\colon E \to  G,\tr)}$ is given by a group morphism $\d\colon E \to G$ together with a left action $\tr$ of $G$ on $E$ by automorphisms, such that:

1.  $\d(X \tr e)=X \d(e)X^{-1}; \forall X \in G, \forall e \in E,$

2.  $\d(e) \tr f=efe^{-1};\forall e,f  \in E.$

If both $G$ and $E$ are Lie groups, $\d\colon E \to G$ is a smooth morphism, and the left action of $G$ on $E$ is smooth then $\Gc$ will be called a Lie crossed module.
:::

A morphism $\Gc \to \Gc'$ between the crossed modules ${\Gc= ( \d\colon E \to  G,\tr)}$ and $\Gc'=(\d'\colon E' \to G',\tr')$ is given by a pair of maps $\f\colon G \to G'$ and $\psi\colon E \to E'$ making the diagram:

$$\begin{CD}
  E @>\d>> G \\
 @V \psi VV   @VV \f V \\
  E' @>\d'>> G' \\
   \end{CD}$$ commutative. In addition we must have $\psi(X \tr e)=\f(X) \tr' \psi(e)$ for each $e \in E$ and each $X \in G$.

Given a Lie crossed module ${\Gc= ( \d\colon E \to  G,\tr)}$, then the induced Lie algebra map $\d\colon \le \to \lg$, together with the derived action of $\lg$ on $\le$ (also denoted by $\tr$) is a differential crossed module, in the sense of the following definition - see [@BS; @B; @BC].

::: Definition
A differential crossed module, say ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$, is given by a Lie algebra morphism $\d\colon \le \to \lg$ together with a left action of $\lg$ on the underlying vector space of $\le$, such that:

1.  For any $X \in \lg$ the map $e \in \le \mapsto X \tr e \in \le$ is a derivation of $\le$, in other words $$X \tr [e,f]=[X \tr e,f]+[e, X \tr f];\forall X \in \lg, \forall e ,f\in \le.$$

2.  The map $\lg \to \Der(\le)$ from $\lg$ into the derivation algebra of $\le$ induced by the action of $\lg$ on $\le$ is a Lie algebra morphism. In other words: $$[X,Y] \tr e=X \tr (Y \tr e)-Y \tr(X \tr e); \forall X,Y \in \lg, \forall e\in \le.$$

3.  $\d( X \tr e)= [X,\d(e)];\forall X \in \lg, \forall e\in \le.$

4.  $\d(e) \tr f=[e,f];  \forall e,f\in \le.$
:::

Note that the map $(X,e) \in \lg \times \le \mapsto X \tr e \in \le$ is necessarily bilinear.

Therefore, given a differential crossed module, ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ there exists a unique crossed module of simply connected Lie groups ${\Gc=(\d \colon E \to  G,\tr )}$ whose differential form is $\mathfrak{G}$, up to isomorphism. The proof of this result is standard Lie theory, together with the lift of the Lie algebra action to a Lie group action, which can be found in [@K], Thm 1.102.

::: Example
Let $G$ be a Lie group with a left action $\tr$ on an abelian group $V$ by automorphisms, for example take $V$ to be any representation of $G$ on a vector space. If we put $\d=1_G$ then $( \d \colon V \to G, \tr)$ is a Lie crossed module. Its differential form is given by the derived action of $\lg$ on $V$ and the zero map $V \to \lg$.
:::

::: Example
Let $G$ be any Lie group. Let $\Ad$ denote the adjoint action of $G$ on $G$. Then ${(\id \colon G \to G, \Ad)}$ is a Lie crossed module.
:::

::: Example
[]{#w label="w"} Let $G$ and $E$ be Lie groups, and let $\d \colon E \to G$ be a surjective map such that $\ker(\d)$ is central in $E$. Define a left action of $G$ on $E$ as $g \tr e=g_0 e g_0^{-1}$, where $g_0\in E$ is such that $\d(g_0)=g\in G$, and $e \in E$. Then ${\Gc=(\d \colon E \to  G,\tr )}$ is a Lie crossed module.
:::

::: Example
[]{#r label="r"} In the previous example, we can take the universal covering map ${\rm SU}(2) \to {\rm SO}(3)$, whose kernel is $\{\pm 1\}$. The differential form of this crossed module is given by the adjoint action of ${\frak su}(2)$ on ${\frak su}(2)$ and the identity map.
:::

::: Example
[]{#cv label="cv"} More generally, take the universal cover $\d\colon E \to G$ of the Lie group $G$. Then the construction in example [\[w\]](#w){reference-type="ref" reference="w"} can be applied since the kernel of $\d$ is necessarily central in $E$.
:::

::: Example
[]{#Heis label="Heis"} Let $H$ be the group of upper triangular matrices in $\R$ which only have 1's in the main diagonal. Define a Lie group map $\d\colon H  \to \R^2$ as $$\d \begin{pmatrix}1 & a & b \\ 0 &1 & c \\ 0 &0 &1 \end{pmatrix}=(a,c),$$ where $a,b,c \in \R$. Then the kernel of $\d\colon H\to \R^2$ is central in $H$, and therefore the construction in example [\[w\]](#w){reference-type="ref" reference="w"} can be applied.
:::

::: Example
[]{#q label="q"} Let $E$ be any Lie group. Let $\Aut(E)$ be the group of automorphisms of $E$. Then $\Aut(E)$ is a Lie group, in fact it is a Lie subgroup of ${\rm GL}(\le)$ if $E$ is simply connected. Consider the map $\Ad\colon E \to \Aut(E)$ that sends $e\in E$ to the automorphism $\Ad(e) \colon E \to E$. The group $\Aut(E)$ acts on $E$ as $\f \tr e=\f(e)$ where $\f\in \Aut(E)$ and $e \in E$. Then $({\Ad}\colon E \to \Aut(E),\tr)$ is a Lie crossed module.
:::

The previous construction yields several examples of Lie crossed modules. For instance, example [\[r\]](#r){reference-type="ref" reference="r"} is obtained this way since ${\rm Aut}({\rm SU(2)})={\rm SO(3)}$. To get new examples, however, we need to consider non-semisimple Lie groups.

::: Example
In example [\[q\]](#q){reference-type="ref" reference="q"}, take $E=H$, the group of upper triangular $3\times 3$ matrices in $\R$, which only have 1's in the main diagonal. Then the crossed module ${(\Ad\colon H \to  {{\Aut}}(H),\tr)}$ is highly non-trivial. In fact, $\Ad(E)$ is isomorphic to $\R^2$, whereas the cokernel ${\rm Out}(E)$ of $\Ad$ is isomorphic to ${\rm GL}(2,\R)$, see [@KH]. The kernel of $\Ad$ is a central subgroup of $H$ isomorphic to $\R$; see example [\[Heis\]](#Heis){reference-type="ref" reference="Heis"}.
:::
