---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-007-41-tambarayamagami-categories-and-fiber-functors
section_title: "Tambara–Yamagami categories and fiber functors"
section_number: 4.1
pages: 12-18
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.735
---
For a finite abelian group $A$, a nondegenerate symmetric bicharacter $\chi$, and $\tau^2=|A|^{-1}$, the category $\operatorname{TY}(A,\chi,\tau)$ has simple objects $A\cup\{m\}$ and fusion rules $$a\otimes b=a+b,
\qquad
a\otimes m=m\otimes a=m,
\qquad
m\otimes m=\bigoplus_{a\in A}a;$$ its associator is determined by $(\chi,\tau)$ [@TY98]. In particular, $\operatorname{FPdim}(m)=\sqrt{|A|}$ and $\operatorname{FPdim}(\operatorname{TY}(A,\chi,\tau))=2|A|$.

The form $\chi$ is *hyperbolic* if $A=L\times L'$ with $\chi$ trivial on $L\times L$ and on $L'\times L'$; otherwise it is *elliptic*. For $|A|$ odd, Tambara's classification states that $\operatorname{TY}(A,\chi,\tau)$ admits a fiber functor exactly when $\tau^{-1}$ is a positive integer and $\chi$ is hyperbolic. Its fiber functors are then parametrized by the ordered decompositions $(L,L')$ of this type [@T00 Propositions 4.1 and 4.2].

## The Hopf algebras $H_p$

Let $p$ be an odd prime, $A_p=C_p\times C_p$, and choose a primitive $p$th root of unity $\xi\in{\Bbbk}$. We identify $\mathbb F_p$-valued bilinear forms with bicharacters by exponentiating with $\xi$, and use the convention $$\operatorname{Alt}(\mu)(x,y)=\mu(y,x)\mu(x,y)^{-1},
\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.$$ Set $$\chi_p((x_1,x_2),(y_1,y_2))=\xi^{x_1y_2+y_1x_2},
\qquad
\mathcal{C}_p=\operatorname{TY}(A_p,\chi_p,p^{-1}).$$ The only Lagrangian subgroups of $(A_p,\chi_p)$ are $L_1=C_p\times\{0\}$ and $L_2=\{0\}\times C_p$. Hence $\mathcal{C}_p$ has two fiber functors, represented by the ordered decompositions $(L_1,L_2)$ and $(L_2,L_1)$.

The involution $t(x,y)=(y,x)$ preserves $\chi_p$ and induces a strict $C_2$-action on $\mathcal{C}_p$ with $T_t(a)=t(a)$ and $T_t(m)=m$ [@Nik08 Proposition 2.10]. Nikshych's Hopf algebra $H_p$ is characterized by $$\operatorname{Rep}(H_p)\simeq\mathcal{C}_p^{C_2};$$ see [@CM17 Theorem 1] for an explicit construction.

## Classification of fiber functors for $\operatorname{Rep}(H_p)$

The only subgroups in Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} are $J=\{e\}$ and $J=C_2$. The first gives the $C_2$-orbits of fiber functors on $\mathcal{C}_p$. In the second, Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} requires an indecomposable rank-two $\mathcal{C}_p$-module category with a free transitive $C_2$-action on its simples.

::: lemma
[]{#lem:no_rank_two_invariant_nikshych label="lem:no_rank_two_invariant_nikshych"} The $T_t$-invariant indecomposable rank-two $\mathcal{C}_p$-module categories are as follows. If $p\equiv3\pmod4$, there are none. If $p\equiv1\pmod4$, there is exactly one equivalence class.
:::

::: proof
*Proof.* With the convention fixed above, the map $[\mu]\mapsto\operatorname{Alt}(\mu)$ identifies $H^2(A_p,{\Bbbk}^\times)$ with the alternating bicharacters on $A_p$. Tambara uses the reciprocal convention in [@T00 Proposition 2.6], which gives the same parametrization.

By [@Nik08 Lemma 4.3], every indecomposable rank-two $\mathcal{C}_p$-module category is of the form $$\mathcal{N}_\mu=\operatorname{Mod}_{\mathcal{C}_p}(R(A_p,\mu)),$$ where $[\mu]\ne0$ in $H^2(A_p,{\Bbbk}^\times)$. Since $A_p$ has dimension two, every non-zero alternating form on $A_p$ is nondegenerate. Thus there is a unique $\lambda\in\mathbb F_p^\times$ such that $$\operatorname{Alt}(\mu)=\lambda J.$$

We first determine the equivalence class of $\mathcal{N}_\mu$. By [@Nik08 Remark 4.5], restriction to the pointed subcategory gives $$\mathcal{N}_\mu|_{\mathop{\mathrm{Vec}}_{A_p}}
\simeq
\mathcal{M}(A_p,\mu)\oplus\mathcal{M}(A_p,\mu'),$$ where, if $S$ is the matrix of the symmetric bicharacter $\chi_p$, the automorphism $\iota_\mu$ defined in that remark satisfies $$\lambda J\,\iota_\mu=S,
\qquad
\mu'(x,y)=\mu^{-1}(\iota_\mu(x),\iota_\mu(y)).$$ Since $\iota_\mu=-\lambda^{-1}JS$ and $S^TJS=\det(S)J$, we obtain $$\operatorname{Alt}(\mu')
=\iota_\mu^T(-\lambda J)\iota_\mu
=-\frac{\det(S)}{\lambda}J.$$ This is also the specialization of the translate formula in [@MeMu12 Lemma 9.1]. For the hyperbolic form $\chi_p$, $$S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \det(S)=-1,$$ and hence $$\operatorname{Alt}(\mu')=\lambda^{-1}J.$$

Consequently, the restriction of $\mathcal{N}_\mu$ is encoded by the unordered pair $$\{\lambda,\lambda^{-1}\}.$$ This unordered pair is a complete invariant. Indeed, an equivalence of $\mathcal{C}_p$-module categories restricts to an equivalence of $\mathop{\mathrm{Vec}}_{A_p}$-module categories and therefore identifies the two indecomposable summands, possibly after interchanging them. Conversely, let $x,y$ be the two simple objects of $\mathcal{N}_\mu$, with $\underline{\operatorname{End}}(x)\simeq R(A_p,\mu)$. The restriction formula identifies the neutral part of $\underline{\operatorname{End}}(y)$ with $R(A_p,\mu')$. The fusion rules in [@Nik08 Lemma 4.3] give $m\overline\otimes y\simeq p x$, so the non-trivial graded component of $\underline{\operatorname{End}}(y)$ vanishes. Therefore $$\underline{\operatorname{End}}(y)\simeq R(A_p,\mu').$$ Internal-Hom reconstruction [@Nik08 Section 2.1] now gives $$\mathcal{N}_\mu
\simeq
\operatorname{Mod}_{\mathcal{C}_p}(R(A_p,\mu'))
=\mathcal{N}_{\mu'}.$$ Since the cohomology class of a cocycle on $A_p$ is determined by its alternating form, the unordered pair is both necessary and sufficient. Thus the equivalence classes are parametrized by $$\{\lambda,\lambda^{-1}\},
\qquad \lambda\in\mathbb F_p^\times.$$

The autoequivalence $T_t$, induced by $t(x,y)=(y,x)$, sends $\mathcal{N}_\mu$ to $\mathcal{N}_{t\mu}$. Since $$t^TJt=-J,$$ it sends $\lambda$ to $-\lambda$. Hence $\mathcal{N}_\mu$ is $T_t$-invariant if and only if $$\{\lambda,\lambda^{-1}\}
=
\{-\lambda,-\lambda^{-1}\}.$$ As $p$ is odd and $\lambda\ne0$, this is equivalent to $$\lambda=-\lambda^{-1},
\qquad\text{or equivalently}\qquad
\lambda^2=-1.$$

If $p\equiv3\pmod4$, there is no solution. If $p\equiv1\pmod4$, the two solutions $i$ and $-i$ determine the same unordered pair because $i^{-1}=-i$. Hence there is exactly one $T_t$-invariant equivalence class. ◻
:::

::: lemma
[]{#lem:diagonal_ty_subcategory label="lem:diagonal_ty_subcategory"} Let $s$ denote the non-trivial element of the acting group $C_2$; it acts on $\mathcal{C}_p$ by $T_t$. In the semidirect product $\mathcal{D}=\mathcal{C}_p\rtimes C_2$, let $$\widetilde m=[m,s],
\qquad
\mathcal{E}_\Delta=\langle [a,e]\;(a\in A_p),\widetilde m\rangle.$$ Then $\mathcal{E}_\Delta$ is a Tambara--Yamagami fusion subcategory $$\mathcal{E}_\Delta\simeq \operatorname{TY}(A_p,\widetilde\chi_p,p^{-1}),
\qquad
\widetilde\chi_p(a,b)=\chi_p(a,t(b)).$$ In coordinates, $$\widetilde\chi_p((x_1,x_2),(y_1,y_2))
=
\xi^{x_1y_1+x_2y_2}.$$ Thus $\widetilde\chi_p$ is hyperbolic if and only if $p\equiv1\pmod4$.
:::

::: proof
*Proof.* Using the strict semidirect-product convention $[X,g]\otimes[Y,h]=[X\otimes g_*(Y),gh]$, we obtain $$\begin{aligned}
\bigl[a,e\bigr]\otimes[b,e]&=[a+b,e],\\
\bigl[a,e\bigr]\otimes\widetilde m&\simeq\widetilde m
\simeq\widetilde m\otimes[a,e],\\
\widetilde m\otimes\widetilde m
&\simeq\bigoplus_{a\in A_p}[a,e].
\end{aligned}$$ Moreover, $[a,e]^*=[-a,e]$ and $\widetilde m^*\simeq\widetilde m$. Thus $\mathcal{E}_\Delta$ has Tambara--Yamagami fusion rules.

The action used to form the semidirect product is strict with identity tensor structure [@Nik08 Proposition 2.10], so the relevant associators are inherited from $\mathcal{C}_p$. For $a,b\in A_p$, they are $$\begin{aligned}
\alpha_{\,[a,e],\widetilde m,\,[b,e]}
 &=\chi_p(a,t(b))\,\operatorname{id}_{\widetilde m},\\
\alpha_{\widetilde m,[a,e],\widetilde m}
 &=\bigoplus_{b\in A_p}\chi_p(a,t(b))\,\operatorname{id}_{[b,e]},\\
(\alpha_{\widetilde m,\widetilde m,\widetilde m})_{a,b}
 &=p^{-1}\chi_p(a,t(b))^{-1}.
\end{aligned}$$ Here we used that $t$ preserves $\chi_p$. These are precisely the associativity data of $$\operatorname{TY}(A_p,\widetilde\chi_p,p^{-1}),
\qquad
\widetilde\chi_p(a,b)=\chi_p(a,t(b)).$$

In coordinates, $$\widetilde\chi_p((x_1,x_2),(y_1,y_2))
 =\xi^{x_1y_1+x_2y_2},$$ so $\widetilde\chi_p$ is represented by the identity matrix. It is hyperbolic precisely when $x_1^2+x_2^2=0$ has a nonzero solution, or equivalently when $-1$ is a square in $\mathbb F_p$. This is equivalent to $p\equiv1\pmod4$; if $i^2=-1$, the two Lagrangian lines are $\langle(1,i)\rangle$ and $\langle(1,-i)\rangle$. ◻
:::

::: proposition
[]{#prop:rank_two_equivariant_p_one_mod_four label="prop:rank_two_equivariant_p_one_mod_four"} Assume that $p\equiv1\pmod4$. The unique $T_t$-invariant indecomposable rank-two $\mathcal{C}_p$-module category admits a $C_2$-equivariant structure whose non-trivial element acts freely on its two simple objects. Moreover, the case $J=C_2$ contributes exactly one equivalence class of fiber functors on $\mathcal{C}_p^{C_2}$.
:::

::: proof
*Proof.* Let $$\mathcal{D}=\mathcal{C}_p\rtimes C_2.$$ We use the faithful grading $$K:=\mathbb Z/2\mathbb Z\times C_2,$$ where the first factor is the Tambara--Yamagami grading of $\mathcal{C}_p$ and the second is the semidirect-product grading. Put $$\Delta=\{(0,e),(1,s)\}\subset K,
\qquad
\gamma=(0,s),$$ and let $$\mathcal{E}_\Delta=\mathcal{D}_{(0,e)}\oplus\mathcal{D}_{(1,s)}.$$ By Lemma [\[lem:diagonal_ty_subcategory\]](#lem:diagonal_ty_subcategory){reference-type="ref" reference="lem:diagonal_ty_subcategory"}, $$\mathcal{E}_\Delta\simeq
\operatorname{TY}(A_p,\widetilde\chi_p,p^{-1}),
\qquad
\widetilde\chi_p(a,b)=\chi_p(a,t(b)).$$ Since $p\equiv1\pmod4$, the form $\widetilde\chi_p$ is hyperbolic. If $i^2=-1$ in $\mathbb F_p$, its two Lagrangian lines are $$L_+=\langle(1,i)\rangle,
\qquad
L_-=\langle(1,-i)\rangle.$$ Tambara's classification [@T00 Propositions 4.1 and 4.2] therefore gives exactly two rank-one $\mathcal{E}_\Delta$-module categories, denoted $\mathcal{N}_+$ and $\mathcal{N}_-$, corresponding to the two ordered decompositions $A_p=L_+\times L_-$ and $A_p=L_-\times L_+$. Fix either one and denote it by $\mathcal{N}$.

Consider the induced $\mathcal{D}$-module category $$\widetilde{\mathcal{M}}
:=
\mathop{\mathrm{Ind}}_{\mathcal{E}_\Delta}^{\mathcal{D}}(\mathcal{N})
=
\mathcal{D}\boxtimes_{\mathcal{E}_\Delta}\mathcal{N}.$$ By [@Gal12 Propositions 3.5 and 3.7], the induced category is graded by the two right cosets $\Delta$ and $\gamma\Delta$. Accordingly, as a right $\mathcal{E}_\Delta$-module category, $$\mathcal{D}=\mathcal{E}_\Delta\oplus\mathcal{D}_{\gamma\Delta}.$$ The object $$u=[\mathbf1,s]\in\mathcal{D}_\gamma$$ is invertible, and left tensoring by $u$ gives an equivalence of right $\mathcal{E}_\Delta$-module categories $$\mathcal{E}_\Delta\longrightarrow\mathcal{D}_{\gamma\Delta},
\qquad
X\longmapsto u\otimes X.$$ Consequently, $$\widetilde{\mathcal{M}}
\simeq
\mathcal{N}\oplus\mathcal{N}$$ as a semisimple category. In particular, $\widetilde{\mathcal{M}}$ has exactly two simple objects, one in each coset summand. The invertible object $u$ exchanges these two summands, so $\widetilde{\mathcal{M}}$ is indecomposable as a $\mathcal{D}$-module category.

Let $$H=\mathbb Z/2\mathbb Z\times\{e\}\subset K;
\qquad
\mathcal{D}_H=\mathcal{C}_p.$$ The homogeneous component of degree $(1,e)$ sends the coset $\Delta$ to $(1,e)\Delta=\gamma\Delta$ and conversely. Hence the action of the non-zero object $[m,e]\in\mathcal{D}_{(1,e)}$ sends either simple object of $\widetilde{\mathcal{M}}$ to a non-zero multiple of the other. It follows that $$\mathop{\mathrm{Res}}_{\mathcal{C}_p}^{\mathcal{D}}(\widetilde{\mathcal{M}})$$ is an indecomposable rank-two $\mathcal{C}_p$-module category.

A module category over $\mathcal{C}_p\rtimes C_2$ is equivalently a $C_2$-equivariant $\mathcal{C}_p$-module category. Thus the restricted module category is $T_t$-invariant, and Lemma [\[lem:no_rank_two_invariant_nikshych\]](#lem:no_rank_two_invariant_nikshych){reference-type="ref" reference="lem:no_rank_two_invariant_nikshych"} identifies it with the unique such rank-two $\mathcal{C}_p$-module category. Moreover, the non-trivial element of $C_2$ acts through $u=[\mathbf1,s]$, which exchanges the two simple objects. The action is therefore free and transitive. Since $H^2(C_2,{\Bbbk}^\times)=0$, Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} shows that its equivariantization has rank one, and hence defines a fiber functor on $\mathcal{C}_p^{C_2}$.

It remains to prove uniqueness in the case $J=C_2$. Let $\mathcal{M}$ be any $C_2$-equivariant indecomposable rank-two $\mathcal{C}_p$-module category whose non-trivial element acts freely on simple objects, and regard $\mathcal{M}$ as a $\mathcal{D}$-module category. Let $x,y$ be its two simple objects. By the fusion-rule calculation in [@Nik08 Lemma 4.3], every $a\in A_p$ fixes both $x$ and $y$, whereas the non-invertible component of $\mathcal{C}_p$ interchanges them. Thus the restriction of $\mathcal{M}$ to $$\mathcal{D}_{(0,e)}=\mathop{\mathrm{Vec}}_{A_p}$$ has two indecomposable rank-one summands, generated by $x$ and $y$. The degree $(1,e)$ component interchanges these summands, and so does the degree $(0,s)$ component because the given $C_2$-action is free. Their product degree $(1,s)$ therefore stabilizes each summand. Hence the stabilizer in $K$ of either $\mathop{\mathrm{Vec}}_{A_p}$-summand is precisely $\Delta$.

The Clifford theorem for graded fusion categories [@Gal12 Corollary 4.4] now gives $$\mathcal{M}\simeq
\mathcal{D}\boxtimes_{\mathcal{E}_\Delta}\overline{\mathcal{N}},$$ where $\overline{\mathcal{N}}$ is a $\mathcal{E}_\Delta$-module category whose restriction to $\mathop{\mathrm{Vec}}_{A_p}$ is one of the two rank-one summands above. In particular, $\overline{\mathcal{N}}$ itself has rank one, so it is equivalent to $\mathcal{N}_+$ or $\mathcal{N}_-$.

Finally, the coset degree $\gamma=(0,s)$ normalizes $\Delta$. Conjugation by $u=[\mathbf1,s]$ acts on $\mathcal{E}_\Delta$ by $t$ on $A_p$ and fixes $\widetilde m=[m,s]$. Since $$t(L_+)=L_-,
\qquad
t(L_-)=L_+,$$ the translated module category $$\mathcal{D}_{\gamma\Delta}\boxtimes_{\mathcal{E}_\Delta}\mathcal{N}_+$$ is equivalent to $\mathcal{N}_-$ as an $\mathcal{E}_\Delta$-module category. The equivalence criterion for induced module categories [@Gal12 Proposition 4.6] therefore implies $$\mathcal{D}\boxtimes_{\mathcal{E}_\Delta}\mathcal{N}_+
\simeq
\mathcal{D}\boxtimes_{\mathcal{E}_\Delta}\mathcal{N}_-.$$ Thus the case $J=C_2$ contributes exactly one equivalence class of fiber functors on $\mathcal{C}_p^{C_2}$. ◻
:::

::: theorem
[]{#thm:nikshych_fiber_functors label="thm:nikshych_fiber_functors"} Let $p$ be an odd prime, and let $H_p$ be Nikshych's semisimple Hopf algebra of dimension $4p^2$, so that $$\operatorname{Rep}(H_p)\simeq \mathcal{C}_p^{C_2}$$ as tensor categories. Then $\operatorname{Rep}(H_p)$ has one equivalence class of fiber functors if $p\equiv3\pmod4$, and two equivalence classes of fiber functors if $p\equiv1\pmod4$.
:::

::: proof
*Proof.* Since every subgroup of $C_2$ is cyclic, its second cohomology with coefficients in ${\Bbbk}^\times$ is trivial. Hence Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} applies.

We distinguish the two possible subgroups $J\subseteq C_2$.

First let $J=\{e\}$. In this case the relevant data are the fiber functors of $\mathcal{C}_p$, modulo the action of $C_2$. By Tambara's classification, the two fiber functors of $\mathcal{C}_p=\operatorname{TY}(A_p,\chi_p,p^{-1})$ correspond to the two ordered Lagrangian decompositions $$A_p=L_1\times L_2
\qquad\text{and}\qquad
A_p=L_2\times L_1.$$ The involution $t(x,y)=(y,x)$ exchanges $L_1$ and $L_2$, and hence exchanges these two ordered decompositions. Therefore the case $J=\{e\}$ contributes one equivalence class of fiber functors on $\mathcal{C}_p^{C_2}$.

Now let $J=C_2$. Since $H^2(C_2,{\Bbbk}^\times)=0$, the rank-one condition in Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} requires a $C_2$-equivariant indecomposable $\mathcal{C}_p$-module category whose non-trivial element acts freely and transitively on its simple objects. Thus the underlying $\mathcal{C}_p$-module category must have rank two.

If $p\equiv3\pmod4$, Lemma [\[lem:no_rank_two_invariant_nikshych\]](#lem:no_rank_two_invariant_nikshych){reference-type="ref" reference="lem:no_rank_two_invariant_nikshych"} shows that there is no $T_t$-invariant indecomposable rank-two $\mathcal{C}_p$-module category. Hence the case $J=C_2$ contributes no fiber functor, and the single class from the case $J=\{e\}$ is the whole list.

If $p\equiv1\pmod4$, Proposition [\[prop:rank_two_equivariant_p_one_mod_four\]](#prop:rank_two_equivariant_p_one_mod_four){reference-type="ref" reference="prop:rank_two_equivariant_p_one_mod_four"} shows that the unique $T_t$-invariant indecomposable rank-two $\mathcal{C}_p$-module category admits a $C_2$-equivariant structure whose non-trivial element acts freely on its two simple objects, and that the case $J=C_2$ contributes exactly one equivalence class of fiber functors.

Finally, the two classes just obtained for $p\equiv1\pmod4$ are not identified with each other: they come from the subgroups $\{e\}$ and $C_2$, respectively, and these subgroups are not conjugate in $C_2$. By Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"}, they therefore define distinct equivalence classes. Thus $\operatorname{Rep}(H_p)\simeq\mathcal{C}_p^{C_2}$ has one equivalence class of fiber functors if $p\equiv3\pmod4$, and two if $p\equiv1\pmod4$. ◻
:::
