---
doc_id: arxiv-math-0409593v1
doc_title: "Categorification of sl_2 and braid groups"
section_id: sec-007-33-rigidification
section_title: "Rigidification"
section_number: 3.3
pages: 10-11
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.955
doc_brief: "Categorification of sl_2 and braid groups — 20 sections: Front matter; Introduction; Self-equivalences"
---
The key point here is that the rigidification of the braid relations at the homotopy category level is equivalent to the one at the derived category level, where the problem is trivial, since we have a genuine action of $W$.

### 

Consider the morphism of $A^{\mathrm{en}}$-modules $A\otimes_{A^s}A\to A_s$ that sends $1\otimes 1$ to $1$. It induces a quasi-isomorphism $F_{{\mathbf{s}}^{-1}}(-1)\buildrel \sim\over\to A_s$. We denote its inverse (a morphism in $D^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)$) by $f_{{\mathbf{s}}^{-1}}$.

Now, let $v\in B_W$ and $v=t_1\cdots t_m=u_1\cdots u_n$ be two decompositions in elements of ${\mathbf{S}}\cup{\mathbf{S}}^{-1}$. By Proposition [\[actionuptoiso\]](#actionuptoiso){reference-type="ref" reference="actionuptoiso"}, the invertible objects $F_{t_1}\cdots
F_{t_m}$ and $F_{u_1}\cdots F_{u_n}$ of $K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)$ are isomorphic, hence $$\operatorname{Hom}\nolimits_\Box(F_{t_1}\cdots F_{t_m},
F_{u_1}\cdots F_{u_n})\simeq \operatorname{End}\nolimits_\Box(A)=k,$$ where $\Box\in\{K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits),D^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)\}$. It follows that the canonical morphism $$\operatorname{Hom}\nolimits_{K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)}(F_{t_1}\cdots F_{t_m},
F_{u_1}\cdots F_{u_n})\buildrel \sim\over\to\operatorname{Hom}\nolimits_{D^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)}(F_{t_1}\cdots F_{t_m},
F_{u_1}\cdots F_{u_n})$$ is an isomorphism.

So, we have a unique isomorphism $$\gamma_{t,u}\in \operatorname{Hom}\nolimits_{K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)}(F_{t_1}\cdots F_{t_m},
F_{u_1}\cdots F_{u_n})$$ such that the induced element in $\operatorname{Hom}\nolimits_{D^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)}(F_{t_1}\cdots F_{t_m}, F_{u_1}\cdots F_{u_n})$ corresponds to $$c_{(t_1,\ldots,t_m),(u_1,\ldots,u_n)}:
A_{t_1}\cdots A_{t_m}\buildrel \sim\over\to A_{u_1}\cdots A_{u_n}$$ via the quasi-isomorphisms $f_{t_1}\cdots f_{t_m}$ and $f_{u_1}\cdots f_{u_n}$.

We now define $G_v$ as the limit of the functors $F_{t_1}\cdots F_{t_m}$, where $t=(t_1,\ldots,t_m)$ runs over the decompositions of $v$ in ${\mathbf{S}}\cup{\mathbf{S}}^{-1}$, with the transitive system of isomorphisms $\gamma_{t,u}$.

There are unique isomorphisms $m_{v,v'}:G_vG_{v'}\buildrel \sim\over\to G_{vv'}$ for $v,v'\in B_W$ and $m_1:G_1\buildrel \sim\over\to A$ in $K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)$ that are compatible with the isomorphisms $c_{t,u}$, in $D^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)$. So, we get the following result :

::: thm
[]{#actionbimod label="actionbimod"} The family $(G_v,m_{v,v'},m_1)$ defines an action of $B_W$ on $K^b(A\operatorname{\!-modgr}\nolimits)$.
:::

This means we have a monoidal functor from

-   the strict monoidal category with set of objects $B_W$, with only arrows the identity maps and with tensor product given by multiplication

-   to the strict monoidal category of endofunctors of $K^b(A\operatorname{\!-modgr}\nolimits)$.

::: rem
[]{#rightaction label="rightaction"} Using tensor products on the right, one obtains a right action of $B_W$ on $K^b(A\operatorname{\!-modgr}\nolimits)$. This action commutes trivially with the left action of $B_W$, so, we have an action of $B_W\times B_W^{\operatorname{opp}\nolimits}$ on $K^b(A\operatorname{\!-modgr}\nolimits)$.
:::

### 

We denote by ${\mathcal{B}}_W$ the full subcategory of $K^b(A^{\mathrm{en}}\operatorname{\!-modgr}\nolimits)$ with objects the $G_v$ for $v\in B_W$. The product $G_v\boxtimes G_{v'}=G_{vv'}$ provides ${\mathcal{B}}_W$ with the structure of a strict monoidal category. Define $G_v^*$ as $G_{v^{-1}}$.

We have obtained our "categorification" of the braid group :

::: thm
The category ${\mathcal{B}}_W$ is a strict rigid monoidal category. Its "decategorification" is a quotient of $B_W$.
:::

::: conj
The decategorification of ${\mathcal{B}}_W$ is equal to $B_W$.
:::

::: rem
One can show that the conjecture is true in type $A_n$, as a consequence of [@KhovSei Corollary 1.2].
:::

###  {#coinvariant}

Let $C=A/(A\cdot A^W_+)$ be the coinvariant algebra. Then, we get by restriction of functors an action of $B_W$ on $K^b(C\operatorname{\!-modgr}\nolimits)$ and on $K^b(C\operatorname{\!-mod}\nolimits)$. We get as well monoidal functors from ${\mathcal{B}}_W$ to the category of self-equivalences of $K^b(C\operatorname{\!-modgr}\nolimits)$ or $K^b(C\operatorname{\!-mod}\nolimits)$. Note that we get also right actions, and this gives a monoidal functor from ${\mathcal{B}}_W\times {\mathcal{B}}_W^{\operatorname{opp}\nolimits}$ to the category of self-equivalences of $K^b(C\operatorname{\!-modgr}\nolimits)$ or $K^b(C\operatorname{\!-mod}\nolimits)$.

::: rem
Let ${\mathcal{C}}$ be the smallest full subcategory of $(A\otimes A)\operatorname{\!-modgr}\nolimits$ containing the objects $A\otimes_{A^s}A$ and closed under finite direct sums, direct summands and tensor products. This is a monoidal subcategory of $(A\otimes A)\operatorname{\!-modgr}\nolimits$ which is a categorification of the Hecke algebra of $W$, according to Soergel. The quotient $\bar{{\mathcal{C}}}$ of ${\mathcal{C}}$ by the smallest additive tensor ideal subcategory containing the $A\otimes_{A^{\langle s,t\rangle}}A$, where $s,t\in S$ and $m_{st}\not=\infty$, is a categorification of the Temperley-Lieb quotient of the Hecke algebra.

When $W$ has type $A_n$, an action of $\bar{{\mathcal{C}}}$ on an algebraic triangulated category is the same as the data on an $A_n$-configuration of spherical objects [@SeiTho §2.c].
:::
