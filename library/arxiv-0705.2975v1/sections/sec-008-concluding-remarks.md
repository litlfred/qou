---
doc_id: arxiv-0705.2975v1
doc_title: "On the Deﬁnitions of Diﬀerence Galois Groups"
section_id: sec-008-concluding-remarks
section_title: "Concluding remarks"
section_number: null
pages: 25-31
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.661
doc_brief: "On the Deﬁnitions of Diﬀerence Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and show, that"
---
[]{#mt4 label="mt4"}

::: remark
**Model-theoretic Galois groups: definition and a bit of history**.

Model-theoretic Galois groups first appeared in a paper by Zilber [@zilber] in the context of $\aleph_1$-categorical theories, and under the name of *binding groups*. Grosso modo, the general situation is as follows: in a saturated model $M$ we have definable sets $D$ and $C$ such that, for some finite tuple $b$ in $M$, $D\subset \dcl(C,b)$ (one then says that $D$ is $C$-internal). The group $\Aut(M/C)$ induces a group of (elementary) permutations of $D$, and it is this group which one calls the *Galois group of $D$ over $C$*. In Zilber's context, this group and its action on $D$ are definable in $M$. One issue is therefore to find the correct assumptions so that these Galois groups and their action are definable, or at least, an intersection of definable groups. Hrushovski shows in his PhD thesis ([@HrPhD]) that this is the case when the ambient theory is stable.

Poizat, in [@poizat], recognized the importance of elimination of imaginaries in establishing the Galois correspondence for these Galois groups. He also noticed that if $M$ is a differentially closed field of characteristic $0$ and $D$ is the set of solutions of some linear differential equation over some differential subfield $K$ of $M$, and $C$ is the field of constants of $M$, then the model-theoretic Galois group coincides with the differential Galois group introduced by Kolchin [@kolchin48]. This connection was further explored by Pillay in a series of papers, see [@pillay]. Note that because the theory of differentially closed fields of characteristic $0$ eliminates quantifiers, this Galois group does coincide with the group of $KC$-automorphisms of the differential field $KC(D)$.
:::

Since then, many authors studied or used Galois groups, under various assumptions on the ambient theory, and in various contexts, either purely model-theoretic (e.g., simple theories) or more algebraic (e.g. fields with Hasse derivations). In the context of generic difference fields, (model-theoretic) Galois groups were investigated in (5.11) of [@ChHr1] (a slight modification in the proof then gives the Galois group described in section 4.1 of this paper). In positive characteristic $p$, the results generalize easily to twisted difference equations of the form $\si(X)=AX^{p^m}$, the field $Fix(\si)$ being then replaced by $Fix(\tau)$, where $\tau:x\mapsto \si(x)^{p^{-m}}$.

Recent work of Kamensky ([@kamensky]) isolates the common ingredients underlying all the definability results on Galois groups, and in particular *very much weakens the assumptions* on the ambient theory (it is not even assumed to be complete). With the correct definition of $C$-internality of the definable set $D$, he is able to show that a certain group of permutations of $D$ is definable in $M$. These are just permutations, do not a priori preserve any relations of the language other than equality. From this group, he is then able to show that subgroups which preserve a (fixed) finite set of relations are also definable, and that the complexity of the defining formula does not increase, or not too much. For details, see section 3 of [@kamensky].

This approach of course applies to the set $D$ of solutions of a linear system of difference equations (over a difference field $K$), and Kamensky also obtains the result that $\Aut(KFix(\si)(D)/KFix(\si))$ is definable (see section 5 in [@kamensky]).

::: remark
A question arises in view of the proof of the general case of Proposition [\[zp4\]](#zp4){reference-type="ref" reference="zp4"}. When $R'$ is not a domain, we found an embedding of the $\si^\ell$-difference ring $R_0$ into a generic $\si^\ell$-difference field $\calu$. It may however happen that $K$ is not relatively algebraically closed in $R_0^*$, even when $D_{R_0}=C_K$. Thus one can wonder: can one always find a generic difference field $\calu$ containing $K$, and such that there is a $K$-embedding of the $\si^\ell$-difference ring $R_0$ into $(\calu,\si^\ell)$? Or are there Picard-Vessiot rings for which this is impossible?
:::

::: remark
**Issues of definability**. It is fairly clear that the algebraic group $\HX$ is defined over $\varphi(KC_L)$. On the other hand, using the saturation of $\calu$ and the fact that $L$ is a regular extension of $K$, we may choose another $K$-embedding $\varphi_1$ of $L$ in $\calu$, and will obtain an algebraic group $\HX_1$, which will be isomorphic to $\HX$ (via some matrix $C\in\GL_n(C_\calu)$). It follows that $\HX$ is $K$-isomorphic to an algebraic group $\HX_0$ defined over the intersections of all possible $\varphi(KC_L)$, i.e., over $K$.
:::

Observe that the isomorphism between $\HX$ and $\HX_1$ yields an isomorphism between $\HX(C_\calu)$ and $\HX_1(C_\calu)$, so that we will also have an isomorphism between $\HX_0(C_\calu)$ and $\HX(C_\calu)$, i.e., $\HX'$ is $K$-isomorphic to an algebraic subgroup of $\HX_0$ which is defined over $\overline{C_K}\cap C_\calu$. Thus when $C_K$ is algebraically closed, it will be defined over $C_K$.\
The Galois duality works as well for subgroups of $\HX(C_\calu)$ defined by equations (i.e., corresponding to algebraic subgroups of $\HX'$, whose irreducible components are defined over $C_\calu$). It works less well for arbitrary definable subgroups of $\HX(C_\calu)$. In order for it to work, we need to replace $K(\calS)$ by its definable closure $\dcl(K\calS)$, i.e., the subfield of $\calu$ which is fixed by all elements of $\Aut_{el}(\calu/K\calS)$. Because the theory of $\calu$ eliminates imaginaries (1.10 in [@ChHr1]), any orbit of an element of $\calS$ under the action of a definable subgroup of $\HX(C_\calu)$ has a "code" inside $\dcl(K\calS)$.

::: remark
**Problems with the algebraic closure**. Assume that $\calu$ is a generic difference field containing $K$, and sufficiently saturated. Then if $K$ is not relatively algebraically closed in the field of fractions of $R_0$, we may not be able to find a $K$-embedding of $R_0$ into the $\si^\ell$-difference field $\calu$. Thus in particular, a priori not all Picard-Vessiot domains $K$-embed into $\calu$. This problem of course does not arise if we assume that $K$ is algebraically closed, or, more precisely, if we assume that\
*All extensions of the automorphism $\si$ to the algebraic closure of $K$ define $K$-isomorphic difference fields.*
:::

This is the case if $K$ has no finite (proper) $\si$-stable extension, for instance when $K=\CX(t)$, with $\si(t)=t+1$ and $\si$ the identity on $\CX$.\
However, in another classical case, this problem does arise: let $q\in \CX$ be non-zero and not a root of unity, and let $K=\CX(t)$, where $\si$ is the identity on $\CX$ and $\si(t)=qt$. Then $K$ has non-trivial finite $\si$-stable extensions, and they are obtained by adding $n$-th roots of $t$.\
Let us assume that, inside $\calu$, we have $\si(\sqrt{t})=\sqrt{q}\sqrt{t}$. Let us consider the system $$\si(Y)=-\sqrt{q}Y,\ \ Y\neq 0$$ over $K$. Then the Picard-Vessiot ring is $R'=K(y)$, where $y^2=t$ and $\si(y)=-\sqrt{q}y$. Clearly $R'$ does not embed in $\calu$. If instead we had considered this system over $K(\sqrt{t})$, then the new Picard-Vessiot ring $R''$ is not a domain anymore, because it will contain a non-zero solution of $\si(X)+X=0$ (namely, $y/\sqrt{t}$). In both cases however the Galois group is $\ZX/2\ZX$. And because $R'$ embeds in $R''$, it also embeds in $K(T)\otimes_{\varphi(C_L)}D'_\calu$.\
This suggests that, when $C_K=D_K$, if one takes $\calM$ to be the subfield of $\calu$ generated over $KC_\calu$ by all tuples of $\calu$ satisfying some linear difference equation over $K$, then $\calM\otimes_{C_\calu}D'_\calu$ is a universal (full) Picard-Vessiot ring of $KD'_\calu$. This ring is not so difficult to describe in terms of $\calM$. Observe that $\calM$ contains $D_\calu$. Thus $\calM\otimes_{C_\calu}D'_\calu$ is isomorphic to $\calM\otimes_{D_\calu}(D_\calu\otimes_{C_\calu}D'_\calu)$. It is a regular ring, with prime spectrum the Cantor space $\calC$ (i.e., the prime spectrum of $D_\calu\otimes_{C_\calu}D'_\calu$), and $\si$ acting on $\calC$. As a ring, it is isomorphic to the ring of locally constant functions from $\calC$ to $\calM$.

It would be interesting to relate this ring to the universal Picard-Vessiot rings defined in [@PuSi].

::: remark
**Saturation hypotheses**. The saturation hypothesis on $\calu$ is not really needed to define the model-theoretic Galois group, since we only need $\calu$ to contain a copy of $L$ to define it. We also used it in the proof of Proposition [\[zp4\]](#zp4){reference-type="ref" reference="zp4"}, when we needed a $K$-embedding of $L$ into $\calu$. Thus, to define the model-theoretic Galois group, we only need $\calu$ to be a generic difference field containing $K$. Its field of constants will however usually be larger than $C_K$. Indeed, the field $C_\calu$ is always a pseudo-finite field (that is, a perfect, pseudo-algebraically closed field, with Galois group isomorphic to $\hat\ZX$). However, one can show that if $F$ is a pseudo-finite field of characteristic $0$, then there is a generic difference field $\calu$ containing $F$ and such that $C_\calu=F$. Thus, the field of constants of $\calu$ does not need to be much larger than $C_K$. In the general case, a general non-sense construction allows one to find a pseudo-finite field $F$ containing $C_K$ and of transcendence degree at most $1$ over $C_K$.
:::

::: remark
**A partial description of the maximal $\si^\ell$-ideal $p$ of $R$**. We keep the notation of the previous subsections, and will first assume that the Picard-Vessiot ring $R'=R/q$ is a domain contained in $\calu$.
:::

We will describe some of the elements of $q$. Write $C_L=C_K(\alpha_1,\ldots,\alpha_m)$, and $\alpha_i=f_i(Y)/g_i(Y)$, where $f_i(Y), g_i(Y)\in K[Y]$ are relatively prime. Then $\si(f_i)(AY)$ and $\si(g_i)(AY)$ are also relatively prime. Looking at the divisors defined by these polynomials, we obtain that there is some $k_i\in K$ such that $\si(f_i)(AY)=k_if_i(Y)$ and $\si(g_i)(AY)=k_ig_i(Y)$. Then $(q,f_i(Y))$ and $(q,g_i(Y))$ are $\si$-ideals. By the maximality of $q$, this implies that either $f_i(Y)$ and $g_i(Y)$ are both in $q$, or else, say if $f_i(Y)\notin q$, that there is some $c_i\in C_{R'}$ such that $g_i(y)=c_if_i(y)$, because $f_i(y)$ is invertible in $R'$. If $P_i(Z)$ is the minimal monic polynomial of $c_i$ over $C_K$ and is of degree $r$, then $g_i(Y)^rP_i(g_i(Y)/f_i(Y))\in q$. In case $C_{R'}=C_K$ (this is the case for instance if $C_K$ is algebraically closed), then $c_i\in C_K$, and $g_i(Y)-c_if_i(Y)$ will belong to $q$. (Note also that if $k_i=k_j$, then also for some $d_j\in C_K$ we will have $f_j(Y)-d_jf_i(Y)\in q$, and $g_j(Y)-c_jd_jf_i(Y)\in q$). The $\si$-ideal $I$ generated by all these polynomials in $R$ could all of $q$. In any case one shows easily that $q$ is a minimal prime ideal containing it (because $KC_L[Y,\det(Y)^{-1}]$ and $R/I$ have the same Krull dimension, which is also the Krull dimension of $R'$).

A better result is obtained by Kamensky in [@kamensky] Proposition 33: if $C_{R'}=C_K$, and instead of looking at a generating set of $C_L$ over $C_K$ one applies the same procedure to all elements of $C_L$, one obtains a generating set of the ideal $q$.

In case $R'$ is not a domain, we reason in the same fashion to get a partial description of the $\si^\ell$-ideal $p$.
