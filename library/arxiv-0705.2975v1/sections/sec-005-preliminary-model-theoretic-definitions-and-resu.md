---
doc_id: arxiv-0705.2975v1
doc_title: "On the Deﬁnitions of Diﬀerence Galois Groups"
section_id: sec-005-preliminary-model-theoretic-definitions-and-resu
section_title: "Preliminary model-theoretic definitions and results"
section_number: null
pages: 15-18
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.989
doc_brief: "On the Deﬁnitions of Diﬀerence Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and show, that"
---
[]{#mt1 label="mt1"}

::: defin
Let $K$ be a difference field with automorphism $\sigma$.

-   $K$ is *generic* iff

    > $(*)$ every **finite** system of difference equations with coefficients in $K$ and which has a solution in a difference field containing $K$, already has a solution in $K$.

-   A *finite $\si$-stable extension* $M$ of $K$ is a finite separably algebraic extension of $K$ such that $\si(M)=M$.

-   The *core of $L$ over $K$*, denoted by ${\rm Core}(L/K)$, is the union of all finite $\si$-stable extensions of $K$ which are contained in $L$.
:::

One of the difficulties with difference fields, is that there are usually several non-isomorphic ways of extending the automorphism to the algebraic closure of the field. An important result of Babbitt (see [@cohn]) says that once we know the behaviour of $\si$ on ${\rm Core}(\overline{K} /K)$, then we know how $\si$ behaves on the algebraic closure $\overline{K}$ of $K$.

Fix an infinite cardinal $\kappa$ which is larger than all the cardinals of structures considered (e.g., in our case, we may take $\kappa=|\CX|^+=(2^{\aleph_0})^+$). In what follows we will work in a generic difference field $\calu$, which we will assume *sufficiently saturated*, i.e., which has the following properties:

-   $(*)$ *above holds for every system of difference equations **of size** $<\kappa$ (in infinitely many variables).*

-   *(1.5 in [@ChHr1]) If $f$ is an isomorphism between two algebraically closed difference subfields of $\calu$ which are of cardinality $<\kappa$, then $f$ extends to an automorphism of $\calu$.*

-   *Let $K\subset L$ be difference fields of cardinality $<\kappa$, and assume that $K\subset \calu$. If every finite $\si$-stable extension of $K$ which is contained in $L$ $K$-embeds in $\calu$, then there is a $K$-embedding of $L$ in $\calu$.*

Note that the hypotheses of (iii) are always verified if $K$ is an algebraically closed subfield of $\calu$. If $K$ is a difference field containing the algebraic closure $\overline{\QX}$ of $\QX$, then $K$ will embed into $\calu$, if and only if the difference subfield $\overline{\QX}$ of $K$ and the difference subfield $\overline{\QX}$ of $\calu$ are isomorphic. This might not always be the case. However, every difference field embeds into some sufficiently saturated generic difference field.

Let us also recall the following result (1.12 in [@ChHr1]): Let $n$ be a positive integer, and consider the field $\calu$ with the automorphism $\si^n$. Then $(\calu,\si^n)$ is a generic difference field, and satisfies the saturation properties required of $(\calu,\si)$.

**Notation**. We use the following notation. Let $R$ be a difference ring. Then, as in the previous sections, $C_R$ denotes the field of "constants" of $R$, i.e., $C_R=\{a\in R\mid
\si(a)=a\}$. We let $D_R = \{ a \in R \ | \ \sigma^m(a) = a \mbox{
for some }
 m\neq 0\}$. Then $D_R$ is a difference subring of $R$, and if $R$ is a field, $D_R$ is the relative algebraic closure of $C_R$ in $R$. We let $D'_R$ denote the difference ring with same underlying ring as $D_R$ and on which $\si$ acts trivially. Thus $C_\calu$ is a pseudo-finite field (see 1.2 in [@ChHr1]), and $D_\calu$ is its algebraic closure (with the action of $\si$), $D'_\calu$ the algebraic closure of $C_\calu$ on which $\si$ acts trivially.

Later we will work with powers of $\si$, and will write $Fix(\si^n)(R)$ for $\{a\in R\mid \si^n(a)=a\}$ so that no confusion arises. If $R=\calu$, we will simply write $Fix(\si^n)$. Here are some additional properties of $\calu$ that we will use.\
Let $K\subset M$ be difference subfields of $\calu$, with $M$ algebraically closed, and let $a$ be a tuple of $\calu$. By 1.7 in [@ChHr1]:

\(iv\) If the orbit of $a$ under $\Aut(\calu/K)$ is finite, then $a\in\overline{K}$ (the algebraic closure of $K$).\
We already know that every element of $\Aut(M/KC_M)$ extends to an automorphism of $\calu$. More is true: using 1.4, 1.11 and Lemma 1 in the appendix of [@ChHr1]:

\(v\) every element of $\Aut(M/KC_M)$ lifts to an element of $\Aut(\calu/KC_\calu)$.\
Recall that a definable subset $S$ of $\calu^n$ is *stably embedded* if whenever $R\subset \calu^{nm}$ is definable with parameters from $\calu$, then $R\cap S^m$ is definable using parameters from $S$. An important result ([@ChHr1] 1.11)) shows that $C_\calu$ is stably embedded. Let $d\geq 1$. Then, adding parameters from $Fix(\si^d)$, there is a definable isomorphism between $Fix(\si^d)$ and $C_\calu^d$. Hence,

\(vi\) for every $d>0$, $Fix(\si^d)$ is stably embedded, and

\(vii\) if $\theta$ defines an automorphism of $D_\calu$ which is the identity on $D_M$, then $\theta$ extends to an automorphism of $\calu$ which is the identity on $M$.\
We also need the following lemma. The proof is rather model-theoretic and we refer to the Appendix of [@ChHr1] for the definitions and results. Recall that if $K$ is a difference subfield of $\calu$, then its definable closure, $\dcl(K)$, is the subfield of $\calu$ fixed by $\Aut(\calu/K)$. It is an algebraic extension of $K$, and is the subfield of the algebraic closure $\overline{K}$ of $K$ which is fixed by the subgroup $\{\tau\in
\calG al(\overline{K}/K)\mid \si^{-1}\tau\si=\tau\}$.

::: lem
[]{#zlem1 label="zlem1"} Let $K$ be a difference field, and $M$ be a finite $\si$-stable extension of $KC_\calu$. Then $M\subset 
\overline{K}D_\calu$, i.e., there is some finite $\si$-stable extension $M_0$ of $K$ such that $M\subset M_0D_\calu$.
:::

::: proof
*Proof.* Fix an integer $d\geq 1$. Then, in the difference field $(\calu,\si^d)$, $Fix(\si^d)$ is stably embedded, $\dcl(\overline{K})=\overline{K}$ and $\dcl(Fix(\si^d))=Fix(\si^d)$. Denoting types in $(\calu,\si^d)$ by $tp_d$, this implies $$tp_d(\overline{K}/\overline{K}\cap
Fix(\si^d))\vdash tp_d(\overline{K}/Fix(\si^d)).\eqno{(\sharp)}$$

Assume by way of contradiction that $KC_\calu$ has a finite $\si$-stable extension $M$ which is not contained in $\overline{K}D_\calu$. We may assume that $M$ is Galois over $\overline{K}C_\calu$ (see Thm 7.16.V in [@cohn]), with Galois group $G$. Choose $d$ large enough so that $\si^d$ commutes with all elements of $G$, and $M=M_0D_\calu$, where $M_0$ is Galois over $\overline{K}Fix(\si^d)$. Then there are several non-isomorphic ways of extending $\si^d$ to $M$. As $tp_d(\overline{K}/Fix(\si^d))$ describes in particular the $\overline{K}Fix(\si^d)$-isomorphism type of the $\si^d$-difference field $M$, this contradicts $(\sharp)$ (see Lemmas 2.6 and 2.9 in [@ChHr1]). ◻
:::
