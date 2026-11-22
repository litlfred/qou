---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-013-51-first-reductions-for-small-radical-gaugings
section_title: "First reductions for small radical gaugings"
section_number: 5.1
pages: 21-33
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.98
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
We apply the preceding description to the small radical gaugings classified in [@GNradical]. Table [1](#tab:small_radical_gaugings){reference-type="ref" reference="tab:small_radical_gaugings"}, adapted from [@GNradical Table 3], records the non-pointed nondegenerate entries and the conclusions proved below. We follow the notation and parameter conventions of that reference. Here $D_r$ has order $2r$; the symbols $e$, $h$, and $N$ denote the elliptic, hyperbolic, and norm forms, respectively; and $p,r$ are distinct odd primes except in the final row.

::: {#tab:small_radical_gaugings}
  $\operatorname{FPdim}$   mantle $\mathcal{B}$                                    $G$     generator action     description                                                fiber functors
  ------------------------ ------------------------------------------------------- ------- -------------------- ---------------------------------------------------------- --------------------------
  $\operatorname{FPdim}$   mantle $\mathcal{B}$                                    $G$     generator action     description                                                fiber functors
  $4$                      $\mathcal I_\eta$                                       $1$     --                   Ising                                                      no
  $8$                      $\mathcal I_\eta\boxtimes\mathcal{C}(C_2,q_{\eta^4})$   $1$     --                   Ising $\boxtimes$ pointed                                  no
  $4r$                     $\mathcal{C}(C_r,q_\mu)$                                $C_2$   $x\mapsto-x$         metaplectic                                                no
  $16$                     $\mathcal I_\eta\boxtimes\mathcal{C}(C_2^2,h)$          $1$     --                   Ising $\boxtimes$ pointed                                  no
  $16$                     $\mathcal I_\eta$                                       $C_2$   trivial              Ising $\boxtimes$ pointed                                  no
  $16$                     $\mathcal{C}(C_4,q_\xi)$                                $C_2$   $x\mapsto-x$         two Ising factors                                          no
  $16$                     $\mathcal{C}(C_2,q_i)^{\boxtimes2}$                     $C_2$   swap                 two Ising factors                                          no
  $16$                     $\mathcal{C}(C_2^2,e)$                                  $C_2$   swap                 two Ising factors                                          no
  $16$                     $\mathcal{C}(C_2^2,h)$                                  $C_2$   swap                 two Ising factors                                          no
  $8r$                     $\mathcal{C}(C_{2r},q_{i\mu})$                          $C_2$   $x\mapsto-x$         metaplectic                                                no
  $4r^2$                   $\mathop{\mathrm{Vec}}_{\Bbbk}$                         $D_r$   --                   $\operatorname{Rep}(D^\omega(D_r))$, $\omega|_{C_r}\ne1$   no
  $4r^2$                   $\mathcal{C}(C_r^2,h)$                                  $C_2$   half-turn            $\operatorname{Rep}(D^\omega(D_r))$, $\omega|_{C_r}=1$     yes iff $[\omega]=0$
  $4r^2$                   $\mathcal{C}(C_r^2,h)$                                  $C_2$   signed swap          $\mathcal Z(\operatorname{TY}(A,\chi,\tau))$               no
  $4r^2$                   $\mathcal{C}(C_r^2,e)$                                  $C_2$   half-turn            elliptic gauging                                           no
  $4r^2$                   $\mathcal{C}(C_r^2,e)$                                  $C_2$   signed swap          elliptic gauging                                           no
  $4pr$                    $\mathcal{C}(C_{pr},q_{\zeta\mu})$                      $C_2$   half-turn            metaplectic                                                no
  $4pr$                    $\mathcal{C}(C_{pr},q_{\zeta\mu})$                      $C_2$   mixed signs          metaplectic $\boxtimes$ pointed                            no
  $p^2r^2$, $p\mid r-1$    $\mathcal{C}(C_r^2,h)$                                  $C_p$   order-$p$ rotation   $\operatorname{Rep}(D^\omega(C_r\rtimes C_p))$             yes for every $[\omega]$
  $p^2r^2$, $p\mid r+1$    $\mathcal{C}(C_r^2,e)$                                  $C_p$   order-$p$ rotation   elliptic prime-cyclic gauging                              no
  $36$                     $\mathcal{C}(C_2^2,e)$                                  $C_3$   order-$3$ rotation   elliptic gauging                                           no

  : Non-pointed small radical gaugings from [@GNradical Table 3].
:::

We first exclude the rows whose non-integrality is immediate. If a fusion category admits a fiber functor, finite Tannaka--Krein reconstruction identifies it with the representation category of a semisimple Hopf algebra [@EGNO15 Theorem 5.3.12]; hence Frobenius--Perron dimensions of simple objects are ordinary vector-space dimensions, and therefore integers. This excludes the rows containing an Ising factor, the metaplectic rows, and the metaplectic-times-pointed rows.

::: lemma
[]{#lem:gt_descends_from_equivariantization label="lem:gt_descends_from_equivariantization"} Let a finite group $G$ act on a fusion category $\mathcal{C}$. If the equivariantization $\mathcal{C}^G$ is group-theoretical, then $\mathcal{C}$ is group-theoretical.
:::

::: proof
*Proof.* The forgetful tensor functor $\mathcal{C}^G\to\mathcal{C}$ is dominant, and group-theoretical fusion categories are stable under dominant tensor images [@ENO05 Proposition 8.44]. ◻
:::

The same obstruction applies to the rows described as centers $\mathcal{Z}(\operatorname{TY}(A,\chi,\tau))$, where $A\simeq C_r$ and $r$ is an odd prime. Let $m$ be the non-invertible simple object of $\operatorname{TY}(A,\chi,\tau)$. Then $\operatorname{FPdim}(m)=\sqrt{|A|}=\sqrt r$. The forgetful tensor functor $$\mathcal{Z}(\operatorname{TY}(A,\chi,\tau))\to \operatorname{TY}(A,\chi,\tau)$$ is dominant, and tensor functors between fusion categories preserve Frobenius--Perron dimensions. Hence $m$ appears as a direct summand of the image of some simple central object $Z$. Writing the image of $Z$ in $\operatorname{TY}(A,\chi,\tau)$ as a direct sum of invertible objects and copies of $m$, we get $$\operatorname{FPdim}(Z)=a+b\sqrt r$$ with $a,b\in\mathbb{Z}_{\geq0}$ and $b>0$. This number is not an integer. Thus $\mathcal{Z}(\operatorname{TY}(A,\chi,\tau))$ is itself non-integral.

::: proposition
[]{#prop:twisted_double_test label="prop:twisted_double_test"} Let $K$ be a finite group. Let $\omega\in Z^3(K,{\Bbbk}^\times)$, and choose the group-theoretical presentation $$\mathcal{Z}(\mathop{\mathrm{Vec}}_{K}^{\omega})
\simeq
(\mathop{\mathrm{Vec}}_{K\times K}^{\,\widetilde{\omega}})^*_{\mathcal{M}(\Delta K,\widetilde{\mu})},$$ where $\Delta K\subset K\times K$ is the diagonal subgroup. Then fiber functors on $\mathcal{Z}(\mathop{\mathrm{Vec}}_{K}^{\omega})$ are parameterized by conjugacy classes of pairs $(L,\nu)$, with $\nu$ understood up to multiplication by a $2$-coboundary, such that:

1.  $L\subseteq K\times K$ is a subgroup with $\Delta K\,L=K\times K$;

2.  $\nu\in C^2(L,{\Bbbk}^\times)$ satisfies $d\nu=\widetilde{\omega}|_L$;

3.  the cocycle obtained from $\widetilde{\mu}\nu^{-1}$ on $\Delta K\cap L$ is nondegenerate.

In this model the cohomology class of $\widetilde{\omega}$ is $\operatorname{pr}_1^*[\omega]-\operatorname{pr}_2^*[\omega]$. In particular, if $L$ is a complement to $\Delta K$, the last condition is automatic.
:::

This is the fiber-functor classification for group-theoretical fusion categories [@Nik08 Section 2], applied to Ostrik's group-theoretical model of the center of a pointed fusion category [@Os03 Theorem 3.2, Proposition 3.1, Corollary 3.1 and Corollary 3.2]. Changing $\nu$ by a $2$-coboundary gives an equivalent module category and does not affect the nondegeneracy condition.

For $\omega=1$, the complement $K\times\{e\}$ gives the usual forgetful fiber functor on $\operatorname{Rep}(D(K))$. For non-trivial $\omega$, Proposition [\[prop:twisted_double_test\]](#prop:twisted_double_test){reference-type="ref" reference="prop:twisted_double_test"} reduces the question to the restriction of $\widetilde\omega$ to subgroups transverse to $\Delta K$.

For the dihedral entries, write $$D_r=\langle\rho,s\mid \rho^r=s^2=e,\ s\rho s=\rho^{-1}\rangle,
\qquad R=\langle\rho\rangle,$$ with $r$ an odd prime. The representatives in [@CGR00 Section 6.3, Equation (6.20)] identify $H^3(D_r,{\Bbbk}^\times)\cong\mathbb Z/2r\mathbb Z$; denote the class indexed by $j$ by $[\alpha_j]$. Its restriction to $R$ has parameter $-j\bmod r$, while its restriction to any reflection subgroup $C\cong C_2$ is the class $j\bmod2$. Hence the row $\omega|_{C_r}=1$ consists of $j=0,r$, and the other row consists of $j\not\equiv0\pmod r$.

::: lemma
[]{#lem:dihedral_goursat label="lem:dihedral_goursat"} Let $G=D_r$, with $r$ an odd prime, and put $R=\langle \rho\rangle$. If $L\subseteq G\times G$ is a subgroup such that $\Delta G\,L=G\times G$, then either $L=G\times H$ or $L=H\times G$ for some subgroup $H\subseteq G$, or else $$L=R\times C
\qquad\text{or}\qquad
L=C\times R$$ for a reflection subgroup $C\subseteq G$.
:::

::: proof
*Proof.* The condition $\Delta G\,L=G\times G$ is equivalent to $$G=\{a^{-1}b\mid (a,b)\in L\}.$$ Let $A=\operatorname{pr}_1(L)$ and $B=\operatorname{pr}_2(L)$. Then $AB=G$. Since $r$ is prime, the subgroups of $G$ are $1$, $R$, the reflection subgroups, and $G$. Hence either one of $A,B$ is $G$, or $\{A,B\}=\{R,C\}$ for a reflection subgroup $C$.

In the second case Goursat's lemma gives only the direct product, since $R$ and $C$ have no non-trivial common quotient. Thus $L=R\times C$ or $L=C\times R$.

Assume now that $A=G$. If the quotient appearing in Goursat's lemma is trivial, then $L=G\times B$. Suppose that this quotient is non-trivial. Since the normal subgroups of $G$ are $\{e\}$, $R$, and $G$, the only non-trivial quotients of $G$ are $G/R\cong C_2$ and $G$. In the quotient $G/R$, the relation defining $L$ gives $aR=bR$ for every $(a,b)\in L$. In the quotient $G$ case, necessarily $B=G$ and the relation is the graph of an automorphism of $G$; every automorphism of $D_r$ preserves $R$ and induces the identity on $G/R$, whence again $aR=bR$. Hence $a^{-1}b\in R$ for every $(a,b)\in L$, contradicting the displayed equality above. Thus only $L=G\times B$ can occur. The case $B=G$ is symmetric. ◻
:::

::: proposition
[]{#prop:dihedral_twisted_doubles_no_fiber label="prop:dihedral_twisted_doubles_no_fiber"} Let $G=D_r$, with $r$ an odd prime, and let $\omega=\alpha_j$ be one of the cocycles above. Then $\mathcal{Z}(\mathop{\mathrm{Vec}}_{G}^{\omega})\simeq \operatorname{Rep}(D^\omega(G))$ has a fiber functor if and only if $j=0$.
:::

::: proof
*Proof.* For $j=0$ this is the ordinary double, and the usual forgetful functor is a fiber functor.

Assume $j\ne0$ and suppose that a fiber functor exists. By Proposition [\[prop:twisted_double_test\]](#prop:twisted_double_test){reference-type="ref" reference="prop:twisted_double_test"}, there is a subgroup $L\subseteq G\times G$ with $\Delta G\,L=G\times G$ such that $\widetilde{\omega}|_L$ is a coboundary. By Lemma [\[lem:dihedral_goursat\]](#lem:dihedral_goursat){reference-type="ref" reference="lem:dihedral_goursat"}, either $L=G\times H$ or $L=H\times G$, or $L=R\times C$ or $L=C\times R$ with $C$ a reflection subgroup.

In the first two cases, $L$ contains $G\times\{e\}$ or $\{e\}\times G$. Since $[\widetilde{\omega}]=\operatorname{pr}_1^*[\omega]-\operatorname{pr}_2^*[\omega]$, the restriction of $\widetilde{\omega}$ to one of these subgroups is $\omega$ or $\omega^{-1}$, which is non-trivial because $j\ne0$. This is impossible.

It remains to consider $R\times C$ and $C\times R$. If $j\not\equiv0\pmod r$, the restriction of $\omega$ to $R$ is non-trivial; hence $\widetilde{\omega}|_L$ cannot be a coboundary. If $j\equiv0\pmod r$ and $j\ne0$, then $j=r$; since $r$ is odd, the restriction of $\omega$ to $C\cong C_2$ is the non-trivial class $(-1)^{ABC}$. Again $\widetilde{\omega}|_L$ cannot be a coboundary. Thus no non-trivial class $j$ gives a fiber functor. ◻
:::

::: lemma
[]{#lem:crossed_component_brpic label="lem:crossed_component_brpic"} Let $\mathcal{B}$ be a nondegenerate braided fusion category, and let $$\mathcal{E}=\bigoplus_{g\in G}\mathcal{E}_g$$ be a faithfully graded braided $G$-crossed extension of $\mathcal{B}$. Write $T_g\in\operatorname{Aut}^{\mathrm{br}}_\otimes(\mathcal{B})$ for the crossed action of $g$. Let $$\Phi:\operatorname{BrPic}(\mathcal{B})
   \xrightarrow{\ \simeq\ }
   \operatorname{EqBr}(\mathcal Z(\mathcal{B}))$$ be the canonical equivalence and let $$\iota:\mathcal{B}\boxtimes\mathcal{B}^{\mathrm{rev}}
   \xrightarrow{\ \simeq\ }
   \mathcal Z(\mathcal{B})$$ be the braided equivalence determined by the braiding of $\mathcal{B}$. Then the invertible $\mathcal{B}$-bimodule category $\mathcal{E}_g$ satisfies $$\label{eq:crossed_component_brpic_formula}
\iota^{-1}\Phi([\mathcal{E}_g])\iota
\simeq
\operatorname{id}_{\mathcal{B}}\boxtimes T_g.$$
:::

::: proof
*Proof.* By [@ENO10 Theorem 7.12], the braided $G$-crossed structure determines a morphism of categorical $2$-groups $$G\longrightarrow\operatorname{Pic}(\mathcal{B}),
\qquad
 g\longmapsto[\mathcal{E}_g].$$ Recall that the alpha-induction homomorphism $$\partial:\operatorname{Pic}(\mathcal{B})
   \longrightarrow\operatorname{Aut}^{\mathrm{br}}_\otimes(\mathcal{B})$$ is characterized by $\alpha^-_{\mathcal{M}}\circ\partial_{\mathcal{M}}\simeq\alpha^+_{\mathcal{M}}$ for every invertible $\mathcal{B}$-module category $\mathcal{M}$ [@ENO10 Section 5.4]. For $X\in\mathcal{E}_g$ and $Y\in\mathcal{B}$, the composite of crossed braidings $$Y\otimes X
\xrightarrow{\ c_{Y,X}\ }
X\otimes Y
\xrightarrow{\ c_{X,Y}\ }
T_g(Y)\otimes X$$ is a module-natural isomorphism $\alpha^+_{\mathcal{E}_g}(Y)\simeq\alpha^-_{\mathcal{E}_g}(T_g(Y))$; the crossed hexagon identities give the module-functor compatibility. Hence $$\partial_{\mathcal{E}_g}=T_g.$$ Equivalently, this is the relation between the categorical $2$-group morphism in [@ENO10 Theorem 7.12] and the structural map of the Picard crossed module.

Under the Brauer--Picard equivalence, the image of $\operatorname{Pic}(\mathcal{B})$ consists of the braided autoequivalences of $\mathcal Z(\mathcal{B})$ that are trivializable on the first copy of $\mathcal{B}$, while the restriction to the second copy $\mathcal{B}^{\mathrm{rev}}$ is the map $\partial$; see [@DN13 Lemma 4.4 and Corollary 4.9]. Since $\mathcal{B}$ is nondegenerate, the inverse construction in [@ENO10 Theorem 5.2] sends a braided autoequivalence $T$ of $\mathcal{B}$ to the bimodule category whose center autoequivalence is $\operatorname{id}_{\mathcal{B}}\boxtimes T$. Taking $T=T_g$ proves [\[eq:crossed_component_brpic_formula\]](#eq:crossed_component_brpic_formula){reference-type="eqref" reference="eq:crossed_component_brpic_formula"}.

Finally, in the extension classification of [@ENO10 Theorems 1.3 and 8.9], the homomorphism $$c:G\longrightarrow\operatorname{BrPic}(\mathcal{B}),
\qquad c(g)=[\mathcal{E}_g],$$ is fixed before the final $H^3(G,{\Bbbk}^\times)$-parameter is chosen. The latter changes the associativity coherence but not the classes of the homogeneous components. This is also the convention in [@GPR24 Definition 2.1], where the crossed action is fixed first and the parameter $\alpha$ labels the remaining $H^3$-choices. ◻
:::

::: lemma
[]{#lem:pointed_defect_sector label="lem:pointed_defect_sector"} Let $A$ be a finite abelian group of odd order, let $\mathcal{B}=\mathcal{C}(A,q)$, and let $$\mathcal{E}=\bigoplus_{g\in G}\mathcal{E}_g$$ be a braided $G$-crossed extension of $\mathcal{B}$. Fix $g\in G$, and let $\theta\in O(A,q)$ be the automorphism induced by $g_*$ on $A=\operatorname{Inv}(\mathcal{B})$. Then, for every simple object $X\in\mathcal{E}_g$, the following hold:

1.  $A$ acts transitively on $\operatorname{Irr}(\mathcal{E}_g)$ by left tensor product.

2.  The stabilizer of $X$ is $$\operatorname{St}_A(X):=\{a\in A\mid a\otimes X\simeq X\}=(1-\theta)A.$$

3.  The assignment $$a+(1-\theta)A\longmapsto a\otimes X$$ defines a bijection $$A/(1-\theta)A \xrightarrow{\ \simeq\ } \operatorname{Irr}(\mathcal{E}_g).$$ In particular, $$\#\operatorname{Irr}(\mathcal{E}_g)=|\ker(1-\theta)|.$$

4.  The Frobenius--Perron dimension of $X$ is $$\operatorname{FPdim}(X)=\sqrt{|(1-\theta)A|}.$$
:::

::: proof
*Proof.* By [@ENO10 Theorem 6.1], $\mathcal{E}_g$ is an invertible, hence indecomposable, $\mathcal{B}$-module category. Since the simple objects of $\mathcal{B}$ are the elements of $A$, tensoring by them permutes $\operatorname{Irr}(\mathcal{E}_g)$. Each $A$-orbit spans a $\mathcal{B}$-module direct summand, so indecomposability implies that this action is transitive.

The crossed braiding gives, for $a\in A$ and $X\in\mathcal{E}_g$, isomorphisms $$a\otimes X\xrightarrow{\ c_{a,X}\ }X\otimes a
\xrightarrow{\ c_{X,a}\ }\theta(a)\otimes X.$$ Tensoring on the left by $\theta(a)^{-1}$ shows that $(a-\theta(a))\otimes X\simeq X$. Hence $$(1-\theta)A\subseteq\operatorname{St}_A(X).$$

It remains to compute the number of simple objects. Write $$b_q(a,b)=q(a+b)q(a)^{-1}q(b)^{-1}$$ for the symmetric bicharacter associated with $q$. Since $|A|$ is odd, doubling is an automorphism of $A$; put $$c(a,b):=b_q(a/2,b).$$ Then $c$ is a nondegenerate symmetric bicharacter, $c(a,a)=q(a)$, and $\theta$ preserves $c$. Thus we may use the braided model in which the underlying fusion category of $\mathcal{B}$ is $\mathop{\mathrm{Vec}}_{A}$ and the braiding is $c$. Use $c$ to identify $\widehat A$ with $A$. Under the braided equivalence $$\mathcal{B}\boxtimes\mathcal{B}^{\mathrm{rev}}\simeq\mathcal Z(\mathop{\mathrm{Vec}}_{A}),
\qquad
(x,y)\longmapsto\bigl(x+y,c(x-y,-)\bigr),$$ the autoequivalence $\operatorname{id}_{\mathcal{B}}\boxtimes T_\theta$ is represented on $A\oplus\widehat A\simeq A\oplus A$ by $$g_\theta=
\frac12
\begin{pmatrix}
1+\theta & 1-\theta\\
1-\theta & 1+\theta
\end{pmatrix},$$ where $\frac12$ denotes the inverse of doubling on $A$. Indeed, the coordinates $(u,v)=(x+y,x-y)$ are sent to $(x+\theta(y),x-\theta(y))$. By Lemma [\[lem:crossed_component_brpic\]](#lem:crossed_component_brpic){reference-type="ref" reference="lem:crossed_component_brpic"}, the invertible $\mathop{\mathrm{Vec}}_{A}$-bimodule category underlying $\mathcal{E}_g$ is the one represented by $\operatorname{id}_{\mathcal{B}}\boxtimes T_\theta$, and hence by $g_\theta$ in these coordinates. If $P:A\oplus\widehat A\to A$ is the first projection, then $$P\,g_\theta(0,v)=\frac12(1-\theta)v.$$ Therefore [@ENO10 Proposition 10.8] gives $$\#\operatorname{Irr}(\mathcal{E}_g)
=\bigl|\ker(P\,g_\theta|_{\widehat A})\bigr|
=|\ker(1-\theta)|
=|A/(1-\theta)A|.$$ Transitivity now yields $$|A:\operatorname{St}_A(X)|=|\ker(1-\theta)|,$$ so $$|\operatorname{St}_A(X)|=\frac{|A|}{|\ker(1-\theta)|}=|(1-\theta)A|.$$ Together with the inclusion above, this proves $\operatorname{St}_A(X)=(1-\theta)A$ and the asserted parametrization of simple objects.

Finally, put $I=(1-\theta)A$. For $a\in A$, rigidity gives $$\operatorname{Hom}_{\mathcal{B}}(a,X\otimes X^*)
\simeq
\operatorname{Hom}_{\mathcal{E}_g}(a\otimes X,X).$$ Since $X$ is simple, the latter space is one-dimensional for $a\in I$ and zero for $a\notin I$. Therefore $$X\otimes X^*\simeq\bigoplus_{a\in I}a,$$ and hence $$\operatorname{FPdim}(X)^2=|I|=|(1-\theta)A|.$$ ◻
:::

::: proposition
[]{#prop:elliptic_four_r_squared_no_fiber label="prop:elliptic_four_r_squared_no_fiber"} Let $A=C_r^2$, with $r$ an odd prime. The two rows of Table [1](#tab:small_radical_gaugings){reference-type="ref" reference="tab:small_radical_gaugings"} with mantle $\mathcal{C}(A,e)$ and $G=C_2$ admit no fiber functor.
:::

::: proof
*Proof.* We identify $A$ with a two-dimensional vector space over $\mathbb{F}_r$ and let $\theta$ be the involution defining the action. Lemma [\[lem:pointed_defect_sector\]](#lem:pointed_defect_sector){reference-type="ref" reference="lem:pointed_defect_sector"} applies to the non-trivial homogeneous component.

If $\theta$ is one of the non-central involutions in the row $(x,y)\mapsto(\pm y,\pm x)$, then $1-\theta$ has rank one over $\mathbb{F}_r$; hence $(1-\theta)A$ has order $r$. The defect sector contains simple objects of Frobenius--Perron dimension $\sqrt r$. A simple object in the equivariantization lying over such a defect has dimension $[C_2:\operatorname{St}_{C_2}(X)]\dim(\pi)\sqrt r$, where $\pi$ is the corresponding irreducible projective representation of the stabilizer; this is the orbit--stabilizer construction for simple equivariant objects recalled in [@GP17 Subsection 7.5.1]. Thus its dimension is a positive integer multiple of $\sqrt r$, and the integrality obstruction excludes this row.

It remains to consider the half-turn $\theta=-\operatorname{id}_A$. In this case $(1-\theta)A=A$, so the non-trivial component has a unique simple object $m$ of dimension $r$. Since the grading group has order two, $m^*$ lies in the same component and hence $m^*\simeq m$. Also, every $a\in A$ fixes $m$. Frobenius reciprocity therefore gives $$[m\otimes m^*:a]
=\dim\operatorname{Hom}(a\otimes m,m)=1
\qquad (a\in A).$$ Thus $$m\otimes m\simeq\bigoplus_{a\in A}a,$$ so the crossed extension has the Tambara--Yamagami fusion rules and is a category $\operatorname{TY}(A,\chi,\tau)$. Since the row has elliptic metric group $\mathcal{C}(A,e)$, the associated symmetric form has no Lagrangian; equivalently, the bilinear form $\chi$ in this Tambara--Yamagami category is elliptic. We apply Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} to the equivariantization by the induced action $T_{-\operatorname{id}_A}$.

The subgroup $H=\{e\}$ would give a fiber functor on $\operatorname{TY}(A,\chi,\tau)$ itself, which is impossible by Tambara's criterion [@T00 Propositions 4.1 and 4.2], since $\chi$ is elliptic. Thus a fiber functor would have to come from $H=C_2$. Since $H^2(C_2,{\Bbbk}^\times)=0$, Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} forces an equivariant rank-two $\operatorname{TY}(A,\chi,\tau)$-module category, indecomposable as a $\operatorname{TY}(A,\chi,\tau)$-module category, on which the non-trivial element acts freely on the two simple objects.

To exclude this case, use the classification of module categories over Tambara--Yamagami categories [@MeMu12 Section 9]. In the form used in [@Nik08 Lemma 4.3 and Remark 4.5], such a module category restricts to $\mathop{\mathrm{Vec}}_{A}$ as $$\mathcal{M}(A,\mu)\oplus \mathcal{M}(A,\mu'),$$ where $\mathcal{M}(A,\mu)$ is the pointed $\mathop{\mathrm{Vec}}_{A}$-module category attached to $\mu$, $[\mu]\ne0$ in $H^2(A,{\Bbbk}^\times)$, and $\mu'$ is determined by $\chi$ and $\mu$. By [@MeMu12 Lemma 9.1], the $\sigma$-translate of $\mathcal{M}(H,\psi)$ is $\mathcal{M}(R^\perp,\widetilde\psi)$, where $R=\operatorname{Rad}(\psi)$, $\xi_\psi$ is the alternating bicharacter associated with $\psi$, and $\widetilde\psi(a,b)=\psi(t_b,t_a)$ for elements $t_a$ satisfying $\xi_\psi(t_a,-)=\chi(a,-)$. Specializing this formula to $H=A$ and $R=\{0\}$, and writing the alternating form $\operatorname{Alt}(\mu)$ as $\lambda J$ and $\chi$ as a symmetric matrix $S$, gives the matrix formula used in [@Nik08 Remark 4.5]: $$\operatorname{Alt}(\mu')=\frac{-\det(S)}{\lambda}J.$$ Since cohomology classes in $H^2(A,{\Bbbk}^\times)$ are determined by their alternating forms, $[\mu]=[\mu']$ would imply $\lambda^2=-\det(S)$. Thus $\mathcal{M}(A,\mu)$ and $\mathcal{M}(A,\mu')$ are equivalent only if $-\det(S)$ is a square in $\mathbb{F}_r$, which is exactly the condition that $\chi$ be hyperbolic over $\mathbb{F}_r$. Since $\chi$ is elliptic, the two $\mathop{\mathrm{Vec}}_{A}$-summands are not equivalent.

The automorphism $-\operatorname{id}_A$ acts trivially on $H^2(A,{\Bbbk}^\times)$. If a $C_2$-equivariant structure on the rank-two module category acted freely on simple objects, the corresponding module equivalence $$U:\mathcal{M}\to\mathcal{M}^{T_{-\operatorname{id}_A}}$$ would interchange the two simple objects. After restriction to $\mathop{\mathrm{Vec}}_{A}$, this would force an equivalence $\mathcal{M}(A,\mu)\simeq \mathcal{M}(A,\mu')$, contradicting the preceding paragraph. Hence no such equivariant structure can act transitively on the two simple objects. This contradicts Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"}, and the half-turn row with elliptic mantle has no fiber functor. ◻
:::

::: proposition
[]{#prop:frobenius_prime_cyclic_positive label="prop:frobenius_prime_cyclic_positive"} Let $p,r$ be odd primes with $p\mid r-1$, and let $$K=\langle x,y\mid x^r=y^p=e,\; yxy^{-1}=x^a\rangle$$ where $a$ has order $p$ in $\mathbb{F}_r^\times$. Then $\mathcal{Z}(\mathop{\mathrm{Vec}}_{K}^{\omega})\simeq \operatorname{Rep}(D^\omega(K))$ admits a fiber functor for every $\omega\in Z^3(K,{\Bbbk}^\times)$.
:::

::: proof
*Proof.* Let $R=\langle x\rangle$ and let $\pi:K\to P=K/R\simeq C_p$ be the quotient map. Consider the Lyndon--Hochschild--Serre spectral sequence $$E_2^{s,t}=H^s(P,H^t(R,{\Bbbk}^\times))\Rightarrow H^{s+t}(K,{\Bbbk}^\times).$$ Since $|R|$ and $|P|$ are coprime, and $H^t(R,{\Bbbk}^\times)$ is finite $r$-primary for $t>0$, the mixed terms $E_2^{s,t}$ with $s,t>0$ vanish. Moreover $E_2^{0,3}=H^3(R,{\Bbbk}^\times)^P=0$, because $P$ acts on $H^3(R,{\Bbbk}^\times)\simeq\mathbb{F}_r$ by multiplication by $a^2\ne1$. Hence the only contribution in total degree $3$ is $E_2^{3,0}=H^3(P,{\Bbbk}^\times)$, and inflation gives $$H^3(K,{\Bbbk}^\times)\simeq \pi^*H^3(P,{\Bbbk}^\times).$$ Thus, after changing $\omega$ within its cohomology class, which does not change the monoidal equivalence class of $\mathop{\mathrm{Vec}}_{K}^{\omega}$, we may assume $\omega=\pi^*\eta$ for some $\eta\in Z^3(P,{\Bbbk}^\times)$.

Choose the subgroup $\langle y\rangle\subset K$ as a section of $P$, and let $\iota:P\to P$ be inversion. Put $f:K\to K$ for the homomorphism obtained by composing $\pi$, $\iota$, and this section, and set $$L=\{(k,f(k))\mid k\in K\}\subset K\times K.$$ Then $L$ is a subgroup of order $|K|$. If $(k,f(k))$ lies in $\Delta K$, then $k=f(k)$ belongs to $\langle y\rangle$ and its image in $P$ is fixed by inversion. Since $p$ is odd, this forces $k=e$. Hence $L\cap \Delta K=\{e\}$, and therefore $\Delta K\,L=K\times K$.

By Proposition [\[prop:twisted_double_test\]](#prop:twisted_double_test){reference-type="ref" reference="prop:twisted_double_test"}, it remains only to check that $\widetilde{\omega}|_L$ is cohomologically trivial. In cohomology, $$[\widetilde{\omega}]|_L
=(\pi\circ \operatorname{pr}_1|_L)^*[\eta]
-(\pi\circ \operatorname{pr}_2|_L)^*[\eta]
=\pi^*[\eta]-(\iota\circ\pi)^*[\eta].$$ The inversion automorphism of $P\simeq C_p$ acts trivially on $H^3(P,{\Bbbk}^\times)$: under the identification $H^3(P,{\Bbbk}^\times)\simeq H^4(P,\mathbb{Z})$, inversion acts by multiplication by $(-1)^2=1$. Hence the displayed class vanishes; therefore there is a 2-cochain $\nu$ on $L$ with $d\nu=\widetilde{\omega}|_L$. Since $L\cap\Delta K=\{e\}$, the nondegeneracy condition in Proposition [\[prop:twisted_double_test\]](#prop:twisted_double_test){reference-type="ref" reference="prop:twisted_double_test"} is automatic. Thus $(L,\nu)$ gives a fiber functor. ◻
:::

::: proposition
[]{#prop:elliptic_prime_cyclic_no_fiber label="prop:elliptic_prime_cyclic_no_fiber"} Let $p,q$ be odd primes with $p\mid q+1$. Let $A=\mathbb{F}_{q^2}$, viewed as a two-dimensional vector space over $\mathbb{F}_q$, and let $N:A\to\mathbb{F}_q$ be the norm form, viewed through a fixed non-trivial additive character as a ${\Bbbk}^\times$-valued quadratic form. For $c\in\ker(N)$ of order $p$ and $\alpha\in H^3(C_p,{\Bbbk}^\times)$, let $$\mathcal{E}_\alpha=\mathop{\mathrm{Vec}}_{(A,N)}^{p,\alpha}$$ be the corresponding $C_p$-crossed extension of $\mathcal{C}(A,N)$. Then the gauging $$\mathcal{D}_\alpha=(\mathcal{E}_\alpha)^{C_p}$$ admits no fiber functor.
:::

::: proof
*Proof.* The fusion rules of $\mathcal{E}_\alpha$ are recalled in [@GPR24 Proposition 4.1]. Its trivial component is the pointed category $\mathop{\mathrm{Vec}}_{A}$, and the non-trivial homogeneous components contain one simple object each. We write these non-invertible simples as $X_i$, $i\in C_p^\times$, with $$a\otimes X_i=X_i\otimes a=X_i,\qquad
X_i\otimes X_j=
\begin{cases}
qX_{i+j},& i+j\ne0,\\
\displaystyle\bigoplus_{a\in A}a,& i+j=0.
\end{cases}$$ Lemma [\[lem:gt_descends_from_equivariantization\]](#lem:gt_descends_from_equivariantization){reference-type="ref" reference="lem:gt_descends_from_equivariantization"} shows that if $\mathcal{D}_\alpha$ were group-theoretical, then its de-equivariantization $\mathcal{E}_\alpha$ would be group-theoretical. Thus the non-group-theoreticality of $\mathcal{D}_\alpha$ already follows from [@GPR24 Theorem 4.4]. The fiber-functor assertion is stronger: non-group-theoretical Hopf representation categories can still admit fiber functors. We therefore apply Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"}.

First suppose that the subgroup $H$ in Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"} is trivial. Then a fiber functor on $\mathcal{D}_\alpha$ would come from a fiber functor on $\mathcal{E}_\alpha$. By reconstruction, this would give $\mathcal{E}_\alpha\simeq \operatorname{Rep}(H_0)$ for a semisimple Hopf algebra $H_0$ of dimension $pq^2$. By [@JL09 Corollary 1.2], all semisimple Hopf algebras of dimension $pq^2$ have group-theoretical representation categories. This contradicts [@GPR24 Theorem 4.4], where these elliptic categories $\mathcal{E}_\alpha$ are shown to be non-group-theoretical.

It remains to exclude the case $H=C_p$. In the subcase $S=C_p$ of Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"}, the Clifford datum has an $\mathcal{E}_\alpha$-module category $\widetilde{\mathcal{N}}$ whose restriction to $\mathop{\mathrm{Vec}}_{A}$ is an indecomposable module category $\mathcal{N}$. The number of simple objects is intrinsic to the underlying abelian category; hence $\#\operatorname{Irr}(\widetilde{\mathcal{N}})=\#\operatorname{Irr}(\mathcal{N})$. By the pointed module-category classification [@Nik08 Section 2], such $\mathop{\mathrm{Vec}}_{A}$-module categories are indexed by pairs $(L,[\mu])$, where $L\subseteq A$ and $[\mu]\in H^2(L,{\Bbbk}^\times)$, and have rank $[A:L]$. Hence their ranks are $1$, $q$, or $q^2$, never $p$. Thus this subcase cannot produce a rank-$p$ module category.

Consider now the subcase $S=\{e\}$, and suppose that it produces a fiber functor. Put $$\mathcal{M}=\mathcal{E}_\alpha\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N},
\qquad
\mathcal{M}_t:=\mathcal{E}_{\alpha,t}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}
\quad (t\in C_p),$$ where $\mathcal{E}_{\alpha,t}$ denotes the homogeneous component of degree $t$. By Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"}, $\mathcal{M}$ has rank $p$. The $p$ subcategories $\mathcal{M}_t$ are non-zero indecomposable $\mathop{\mathrm{Vec}}_{A}$-module categories, so each one has rank one. Let $m_t$ be the unique simple object of $\mathcal{M}_t$; in particular, $\mathcal{M}_0=\mathcal{N}$ and its unique simple object is $m_0$.

Let $$U:\mathcal{M}\longrightarrow \mathcal{M}^\tau$$ be the module equivalence attached to a generator $\tau\in C_p$, and write $U(m_0)\simeq m_s$. Restricting $U$ to $\mathcal{N}=\mathcal{M}_0$ and using the convention $X\overline\otimes^{\,\tau}M=\rho_\tau(X)\overline\otimes M$ gives an equivalence of $\mathop{\mathrm{Vec}}_{A}$-module categories $$\label{eq:elliptic_shift_invariance}
\mathcal{N}^{\tau^{-1}}
\simeq \mathcal{M}_s
\simeq \mathcal{E}_{\alpha,s}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}.$$ Indeed, the module-functor constraint for $U$ reads $$U(a\overline\otimes M)\simeq \rho_\tau(a)\overline\otimes U(M),
\qquad a\in A,$$ which is precisely $\mathop{\mathrm{Vec}}_{A}$-linearity after twisting the source by $\tau^{-1}$.

By the classification of indecomposable module categories over $\mathop{\mathrm{Vec}}_{A}$, the rank-one category $\mathcal{N}$ is determined by a class $[\mu]\in H^2(A,{\Bbbk}^\times)$. The restriction of $\rho_\tau$ to $A$ is multiplication by $c$ [@GPR24 Definition 3.1 and the proof of Proposition 4.2], so twisting by $\tau^{-1}$ pulls this class back along multiplication by $c^{-1}$. Since ${\Bbbk}^\times$ is divisible, $$H^2(A,{\Bbbk}^\times)\simeq \operatorname{Hom}(\wedge^2 A,{\Bbbk}^\times),$$ and multiplication by $c$ acts on $\wedge^2 A$ by $$\det_{\mathbb F_q}(c)=N(c)=1.$$ Therefore $\mathcal{N}^{\tau^{-1}}\simeq\mathcal{N}$, and [\[eq:elliptic_shift_invariance\]](#eq:elliptic_shift_invariance){reference-type="eqref" reference="eq:elliptic_shift_invariance"} yields $$\mathcal{E}_{\alpha,s}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}\simeq\mathcal{N}.$$ If $s\ne0$, then $s$ generates $C_p$. Iterating the relative tensor product and using the graded multiplication equivalences shows that the same equivalence holds for every homogeneous component. Moreover, because $A$ is abelian, every rank-one $\mathop{\mathrm{Vec}}_{A}$-module category is pointed. Indeed, a simple $\mathop{\mathrm{Vec}}_{A}$-module endofunctor has the identity as its underlying functor, and its module structure is a character of $A$; hence the simple objects of the dual category are indexed by $\widehat A$ and are invertible. The group-theoretical criterion [@MeMu12 Theorem 16] would then imply that $\mathcal{E}_\alpha$ is group-theoretical, contradicting [@GPR24 Theorem 4.4]. Hence $s=0$ and $U(m_0)\simeq m_0$.

Finally, for each $i\in C_p^\times$, the non-zero object $X_i\overline\otimes m_0$ belongs to the rank-one component $\mathcal{M}_i$. Thus $$X_i\overline\otimes m_0\simeq n_i m_i$$ for some integer $n_i>0$. The crossed action preserves the grading and the non-trivial component of degree $i$ has the unique simple object $X_i$, so $\rho_\tau(X_i)\simeq X_i$. Applying the module-functor constraint gives $$n_iU(m_i)
\simeq U(X_i\overline\otimes m_0)
\simeq \rho_\tau(X_i)\overline\otimes U(m_0)
\simeq X_i\overline\otimes m_0
\simeq n_i m_i.$$ Semisimplicity implies $U(m_i)\simeq m_i$ for every $i$. Hence the generator fixes all simple objects of $\mathcal{M}$ and cannot act as a $p$-cycle. This rules out the last subcase and proves the proposition. ◻
:::

::: lemma
[]{#lem:f4_elliptic_extension_non_gt label="lem:f4_elliptic_extension_non_gt"} Let $A=\mathbb{F}_4$ and let $N:A\to\mathbb{F}_2$ be the norm form, composed with the non-trivial additive character of $\mathbb{F}_2$. For every $\alpha\in H^3(C_3,{\Bbbk}^\times)$, the crossed extension $$\mathcal{E}_\alpha=\mathop{\mathrm{Vec}}_{(A,N)}^{3,\alpha}$$ is non-group-theoretical.
:::

::: proof
*Proof.* Write $q(a)=(-1)^{N(a)}$ and $\mathcal{B}=\mathcal{C}(A,q)$, so that the underlying fusion category of $\mathcal{B}$ is $\mathop{\mathrm{Vec}}_{A}$. Thus $$q(0)=1,
\qquad
q(a)=-1\quad(a\ne0).$$ Let $T_c$ be the braided autoequivalence induced by multiplication by an element $c\in\mathbb{F}_4^\times$ of order three. By [@GPR24 Definition 2.1 and Example 3.3(1)], the category $\mathcal{E}_\alpha$ is the braided $C_3$-crossed extension whose crossed action is generated by $T_c$. There is no additional $H^2$-choice here: multiplication by $3$ is an automorphism of the $2$-group $A$, so $H^2(C_3,A)=0$ for this action.

By Lemma [\[lem:crossed_component_brpic\]](#lem:crossed_component_brpic){reference-type="ref" reference="lem:crossed_component_brpic"}, under the braided equivalence $$\iota:\mathcal{B}\boxtimes\mathcal{B}^{\mathrm{rev}}
\xrightarrow{\ \simeq\ }
\mathcal Z(\mathop{\mathrm{Vec}}_{A}),$$ the Brauer--Picard class of the degree-one component satisfies $$\label{eq:f4_extension_brpic_component}
\iota^{-1}\Phi([\mathcal{E}_{\alpha,1}])\iota
\simeq
\operatorname{id}_{\mathcal{B}}\boxtimes T_c.$$ This formula is independent of $\alpha$: the parameter $\alpha$ changes the final associativity coherence of the extension, but not the homomorphism $C_3\to\operatorname{BrPic}(\mathop{\mathrm{Vec}}_{A})$ represented by its homogeneous components.

The group-theoretical criterion for graded extensions [@MeMu12 Theorem 16 and Remark 17] now says that $\mathcal{E}_\alpha$ is group-theoretical if and only if a Lagrangian subcategory of $\mathcal Z(\mathop{\mathrm{Vec}}_{A})$ is stable under the autoequivalence in [\[eq:f4_extension_brpic_component\]](#eq:f4_extension_brpic_component){reference-type="eqref" reference="eq:f4_extension_brpic_component"}.

The metric group of $\mathcal{B}\boxtimes\mathcal{B}^{\mathrm{rev}}$ is $A\oplus A$ with quadratic form $$Q(x,y)=q(x)q(y)^{-1}.$$ A Lagrangian subgroup $L\subseteq A\oplus A$ has order four and satisfies $Q|_L=1$. If $(x,0)\in L$ with $x\ne0$, then $Q(x,0)=-1$, a contradiction; similarly, $L$ contains no non-zero element of the form $(0,y)$. Hence both coordinate projections $L\to A$ are injective. Since $|L|=|A|$, there is an automorphism $f\in\operatorname{Aut}(A)$ such that $$L=\Gamma_f:=\{(x,f(x)):x\in A\}.$$ Conversely, every such graph is Lagrangian, because $q$ takes the same value on every non-zero element of $A$.

If $\Gamma_f$ were invariant under $\operatorname{id}_A\oplus T_c$, then $$(x,cf(x))\in\Gamma_f
\qquad(x\in A).$$ Comparison of the first coordinates gives $cf(x)=f(x)$ for all $x$. Since $f$ is surjective, this would force $c=1$, contrary to the choice of $c$. Thus no Lagrangian subcategory is $C_3$-stable, and the criterion cited above proves that $\mathcal{E}_\alpha$ is non-group-theoretical. ◻
:::

::: proposition
[]{#prop:dimension36_no_fiber label="prop:dimension36_no_fiber"} Let $A=\mathbb{F}_4$, viewed as an additive group, and let $N:A\to\mathbb{F}_2$ be the norm form, viewed through a fixed non-trivial additive character as a ${\Bbbk}^\times$-valued quadratic form. For every $\alpha\in H^3(C_3,{\Bbbk}^\times)$, the dimension $36$ gauging $$\mathcal{D}_\alpha=\left(\mathop{\mathrm{Vec}}_{(A,N)}^{3,\alpha}\right)^{C_3}$$ admits no fiber functor.
:::

::: proof
*Proof.* Put $\mathcal{E}_\alpha=\mathop{\mathrm{Vec}}_{(A,N)}^{3,\alpha}$. We examine the alternatives in Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"}.

First suppose that $H=C_3$. If $S=C_3$, the Clifford datum contains an $\mathcal{E}_\alpha$-module category $\widetilde{\mathcal{N}}$ whose restriction to $\mathop{\mathrm{Vec}}_{A}$ is an indecomposable module category $\mathcal{N}$. These categories have the same underlying abelian category and therefore the same rank. Indecomposable module categories over $\mathop{\mathrm{Vec}}_{A}$ are parameterized by pairs $(L,[\mu])$, where $L\subseteq A$ and $[\mu]\in H^2(L,{\Bbbk}^\times)$, and their rank is $[A:L]$ [@Nik08 Section 2]. Since $A\simeq C_2^2$, the possible ranks are $1$, $2$, and $4$, never $3$. Hence this subcase is impossible.

Assume next that $S=\{e\}$. Then $$\mathcal{M}=\mathcal{E}_\alpha\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}
     =\bigoplus_{t\in C_3}\mathcal{M}_t,
\qquad
\mathcal{M}_t=\mathcal{E}_{\alpha,t}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}.$$ If this datum produced a fiber functor, Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"} would force every $\mathcal{M}_t$ to have rank one. In particular, $\mathcal{N}=\mathcal{M}_0$ has rank one. Such module categories are parameterized by $$H^2(A,{\Bbbk}^\times)
\simeq \operatorname{Hom}(\wedge^2A,{\Bbbk}^\times)
\simeq C_2,$$ where the first isomorphism uses the divisibility of ${\Bbbk}^\times$. Thus there are exactly two equivalence classes of rank-one $\mathop{\mathrm{Vec}}_{A}$-module categories.

The homogeneous components of $\mathcal{E}_\alpha$ act on equivalence classes of indecomposable $\mathop{\mathrm{Vec}}_{A}$-module categories by $$[\mathcal{N}]\longmapsto
[\mathcal{E}_{\alpha,t}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}].$$ The three classes $[\mathcal{M}_t]$ form the $C_3$-orbit of $[\mathcal{N}]$, and all of them have rank one. This orbit is therefore contained in a set of two elements. Since a $C_3$-orbit has cardinality one or three, the orbit must have cardinality one. Consequently, $$\mathcal{E}_{\alpha,t}\boxtimes_{\mathop{\mathrm{Vec}}_{A}}\mathcal{N}\simeq\mathcal{N}
\qquad(t\in C_3),$$ so $\mathcal{N}$ is $C_3$-stable.

Moreover, every rank-one $\mathop{\mathrm{Vec}}_{A}$-module category is pointed. Indeed, its underlying semisimple category has one simple object, and its simple $\mathop{\mathrm{Vec}}_{A}$-module endofunctors are indexed by the characters of $A$; all of them are invertible. The criterion [@MeMu12 Theorem 16] would therefore make $\mathcal{E}_\alpha$ group-theoretical, contradicting Lemma [\[lem:f4_elliptic_extension_non_gt\]](#lem:f4_elliptic_extension_non_gt){reference-type="ref" reference="lem:f4_elliptic_extension_non_gt"}. Thus the subcase $S=\{e\}$ is also impossible.

It remains to consider $H=\{e\}$. Corollary [\[cor:prime_cyclic_gauging\]](#cor:prime_cyclic_gauging){reference-type="ref" reference="cor:prime_cyclic_gauging"} then requires a fiber functor on $\mathcal{E}_\alpha$ itself. By reconstruction, this would give a semisimple Hopf algebra $H_1$ of dimension $12$ with $\mathcal{E}_\alpha\simeq\operatorname{Rep}(H_1)$. Every semisimple Hopf algebra of dimension $pq^2$, and in particular of dimension $3\cdot2^2$, has a group-theoretical representation category [@JL09 Corollary 1.2]. This again contradicts Lemma [\[lem:f4_elliptic_extension_non_gt\]](#lem:f4_elliptic_extension_non_gt){reference-type="ref" reference="lem:f4_elliptic_extension_non_gt"}. Therefore $\mathcal{D}_\alpha$ admits no fiber functor. ◻
:::

::: corollary
[]{#cor:factorizable_hopf_realizations label="cor:factorizable_hopf_realizations"} Among the non-pointed nondegenerate braided fusion categories in Table [1](#tab:small_radical_gaugings){reference-type="ref" reference="tab:small_radical_gaugings"}, the categories admitting a realization as $\operatorname{Rep}(H)$ for a finite-dimensional semisimple factorizable Hopf algebra $H$ are exactly:

1.  the ordinary dihedral doubles $\operatorname{Rep}(D(D_r))$;

2.  the hyperbolic prime-cyclic twisted doubles $\operatorname{Rep}(D^\omega(C_r\rtimes C_p))$, with $p\mid r-1$, for every $[\omega]\in H^3(C_r\rtimes C_p,{\Bbbk}^\times)$.

All other non-pointed entries in the table admit no fiber functor.
:::

::: proof
*Proof.* The fiber-functor conclusions are assembled in Table [1](#tab:small_radical_gaugings){reference-type="ref" reference="tab:small_radical_gaugings"} from the integrality obstruction and Propositions [\[prop:dihedral_twisted_doubles_no_fiber\]](#prop:dihedral_twisted_doubles_no_fiber){reference-type="ref" reference="prop:dihedral_twisted_doubles_no_fiber"}, [\[prop:elliptic_four_r_squared_no_fiber\]](#prop:elliptic_four_r_squared_no_fiber){reference-type="ref" reference="prop:elliptic_four_r_squared_no_fiber"}, [\[prop:frobenius_prime_cyclic_positive\]](#prop:frobenius_prime_cyclic_positive){reference-type="ref" reference="prop:frobenius_prime_cyclic_positive"}, [\[prop:elliptic_prime_cyclic_no_fiber\]](#prop:elliptic_prime_cyclic_no_fiber){reference-type="ref" reference="prop:elliptic_prime_cyclic_no_fiber"}, and [\[prop:dimension36_no_fiber\]](#prop:dimension36_no_fiber){reference-type="ref" reference="prop:dimension36_no_fiber"}. Finite Tannaka--Krein reconstruction turns fiber functors into semisimple Hopf realizations [@EGNO15 Theorem 5.3.12]; for a nondegenerate braided representation category, the corresponding quasitriangular Hopf algebra is factorizable [@Kas95 Chapter VIII]. ◻
:::
