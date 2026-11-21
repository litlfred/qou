---
doc_id: arxiv-0705.2975v1
doc_title: "On the Deﬁnitions of Diﬀerence Galois Groups"
section_id: sec-007-more-on-picard-vessiot-rings
section_title: "More on Picard-Vessiot rings"
section_number: null
pages: 20-25
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.97
doc_brief: "On the Deﬁnitions of Diﬀerence Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and show, that"
---
[]{#zpvr label="zpvr"}

Throughout the rest of this section, we fix a difference ring $K$, some $A\in \GL_n(K)$, $R=K[Y,\det(Y)^{-1}]$ as above, with $\si(Y)=AY$, and $R'=R/q$ a Picard-Vessiot ring for $\si(X)=AX$ over $K$. We denote the image of $Y$ in $R'$ by $y$. We keep the notation introduced in the previous subsections.\
If $q$ is not a prime ideal, then there exists $\ell$ and a prime $\si^\ell$-ideal $p$ of $R$ which is a maximal $\si^\ell$-ideal of $R$, such that $q=\bigcap_{i=0}^{\ell
  -1}\si^i(p)$, and $R'\simeq \oplus_{i=0}^{\ell -1}R_i$, where $R_i=R/\si^i(p)$ (see Corollary 1.16 of [@PuSi]. One verifies that the second proof does not use the fact that $C_K$ is algebraically closed). Thus the $\si^\ell$-difference ring $R_0$ is a Picard-Vessiot ring for the difference equation $\si^\ell(X)=\si^{\ell-1}(A)\cdots\si(A)AX$ over $K$. We denote $\si^{\ell-1}(A)\cdots\si(A)A$ by $A_\ell$.\
We will identify $R'$ with $\oplus_{i=0}^{\ell
    -1}R_i$, and denote by $e_i$ the primitive idempotent of $R'$ such that $e_iR'=R_i$. Then $e_i=\si^i(e_0)$. We will denote by $R^*$ the ring of quotients of $R'$, i.e., $R^*=\oplus_{i=0}^{\ell -1}R_i^*$, where $R_i^*$ is the field of fractions of $R_i$. The difference ring $R^*$ is also called the *total Picard-Vessiot ring of $\si(X)=AX$ over $K$*. There are two numerical invariants associated to $R'$: the number $\ell=\ell(R')$, and the number $m(R')$ which is the product of $\ell(R')$ with $[D_{R^*_0}:D_KC_{R^*_0}]$. We call $m(R')$ the *$m$-invariant of $R'$*. We will be considering other Picard-Vessiot rings for $\si(X)=AX$, and will use this notation for them as well.\
Recall that the *Krull dimension* of a ring $S$ is the maximal integer $n$ (if it exists) such that there is a (strict) chain of prime ideals of $S$ of length $n$. We denote it by $\Krd(S)$. If $S$ is a domain, and is finitely generated over some subfield $k$, then $\Krd(S)$ equals the transcendence degree over $k$ of its field of fractions. Observe that if $S$ is a domain of finite Krull dimension, and $0\neq I$ is an ideal of $S$, then $\Krd(S)>\Krd(S/I)$. Also, if $S=\oplus_i S_i$, then $\Krd(S)=\sup\{\Krd(S_i)\}$.

::: lem
[]{#zpvlem2 label="zpvlem2"}

-   $C_{R'}$ is a finite algebraic extension of $C_K$, and is linearly disjoint from $K$ over $C_K$ (inside $R'$).

-   If $C_{R'}\otimes_{C_K}D_K$ is a domain, then $R'$ is a Picard-Vessiot ring for $\si(X)=AX$ over $KC_{R'}$.
:::

::: proof
*Proof.* 1. We know by Lemma 1.7 of [@PuSi] that $C_{R'}$ is a field. Assume by way of contradiction that $C_{R'}$ and $K$ are not linearly disjoint over $C_K$, and choose $n$ minimal such that there are $a_1,\ldots,a_n\in C_{R'}$ which are $C_K$-linearly independent, but not $K$-linearly independent. Let $0\neq c_1,\ldots, c_n\in K$ be such that $\sum_{i=1}^n a_ic_i=0$. Multiplying by $c_1^{-1}$, we may assume $c_1=1$. Then $\si(\sum_{i=1}^n a_ic_i)=\sum_{i=1}^n
  a_i\si(c_i)=0$, and therefore $\sum_{i=2}^na_i(\si(c_i)-c_i)=0$. By minimality of $n$, all $(\si(c_i)-c_i)$ are $0$, i.e., all $c_i\in
  C_K$, which gives us a contradiction.

Observe that $e_0C_{R'}\subset Fix(\si^\ell)(R_0)$, and we may therefore replace $R'$ by the domain $R_0$. Since $R_0$ is a finitely generated $K$-algebra, we know that its Krull dimension equals the transcendence degree over $K$ of its field of fractions. Thus $R_0$ cannot contain a subfield which is transcendental over $K$, i.e., the elements of $Fix(\si^\ell)(R_0)$ are algebraic over $K$. his furthermore implies that $Fix(\si^\ell)(R_0)$ is an algebraic extension of $Fix(\si^\ell)(K)$. Since the latter field is an algebraic extension of $C_K$, we have the conclusion.\
2. Our hypothesis implies that $K[C_{R'}]$ is a field. Hence $R'$ is a simple difference ring containing $KC_{R'}$, and is therefore a Picard-Vessiot ring for $\si(X)=AX$ over $KC_{R'}$. ◻
:::

::: lem
[]{#zpvlem1 label="zpvlem1"}

-   $C_{R'}=C_{R^*}$.

-   $Fix(\si^\ell)(e_0R^*)=e_0C_{R'}$.

-   $D_{R^*}=\oplus_{i=0}^{\ell -1}D_{e_iR^*}$.
:::

::: proof
*Proof.* 1. If $c\in C_{R^*}$, then $c$ can be represented by some $\ell$-tuple $(\frac{a_0}{b_0},\ldots,\frac{a_{\ell -1}}{b_{\ell -1}})$, where $a_i,b_i\in R_i$, and $b_i\neq 0$. Thus the ideal $I=\{d\in
  R'\mid dc\in R'\}$ is a $\si$-ideal of $R'$ and contains the element $b=(b_0,\ldots,b_{\ell -1})\neq 0$. Since $R'$ is simple, $1\in I$, i.e., $c\in R'$.

. Assume that $a\in e_0R^*$ satisfies $\si^\ell(a)=a$. Then $a=e_0a$, $\sum_{i=0}^{\ell
  -1}\si^i(e_0a)$ is fixed by $\si$, and therefore belongs to $C_{R'}$. Hence $a\in e_0C_{R'}$.\
3. If $a\in R^*$ satisfies $\si^m(a)=a$ for some $m$, then $\si^{m\ell}(e_ia)=e_ia$. ◻
:::

::: remark
[]{#zpvrem1 label="zpvrem1"} Observe that $\ell$ and the isomorphism type of the $K$-$\si^\ell$-difference algebra $R_0$ completely determine the isomorphism type of the difference algebra $R'$. Indeed, for each $i=1,\ldots,\ell-1$, one chooses a copy $R_i$ of the domain $R_0$, together with an isomorphism $f_i:R_0\to R_i$ which extends $\si^i$ on $K$. This $f_i$ then induces an automorphism $\si^\ell$ of $R_i$. One then defines $\si$ on $\oplus_{i=0}^{\ell -1}R_i$ by setting $\si(a_0,\ldots,a_{\ell-1})=(f_1(a_0),f_2f_1^{-1}(a_1),\ldots,
\si^\ell f_{\ell -1}^{-1}(a_{\ell -1}))$.
:::

::: prop
[]{#zp2 label="zp2"}Let $K\subset K_1$ be difference fields of characteristic $0$ where $K_1=K(C_{K_1})$, and assume that $C_K=D_K$. Then $R'\otimes_KK_1=\oplus _{i=1}^d R'_i$, where each $R'_i$ is a Picard-Vessiot ring for $\si(X)=AX$ over $K_1$, and $d\leq
  [C_{R'}:C_K]$. Moreover, each $R'_i$ has the same Krull-dimension and $m$-invariant as $R'$.
:::

::: proof
*Proof.* Our assumption implies that $K\otimes_{C_K}C_{K_1}$ is a domain. Let $C$ be the relative algebraic closure of $C_K$ in $C_{K_1}$. Then $K(C)=K[C]$, and $R'\otimes_KK(C)\simeq
  R'\otimes_{C_K}C$.

Let $a\in C_{R'}$ be such that $C_{R'}=C_K(a)$ and let $f(X)\in C_{K}[X]$ be its minimal polynomial over $C_K$. Let $g_1(X),\ldots,g_d(X)$ be the irreducible factors of $f(X)$ over $C$. Then $f(X)=\prod_{i=1}^d g_i(X)$, and $C_R'\otimes_{C_K}C\simeq
  \oplus_{i=1}^d C_i$, where $C_i$ is generated over $C$ by a root of $g_i(X)=0$. Indeed, identifying $C$ with $1\otimes C$, every prime ideal of $C_{R'}\otimes_{C_K}C$ must contain some $g_i(a\otimes 1)$; on the other hand, each $g_i(a\otimes 1)$ generates a maximal ideal of $C_{R'}\otimes_{C_K}C$. Thus $$R'\otimes_{C_K}C\simeq R'\otimes_{C_{R'}}
(C_{R'}\otimes_{C_K}C)\simeq \oplus_{i=1}^dR'\otimes_{C_{R'}}C_i.$$ By Lemmas [\[lem1.11\]](#lem1.11){reference-type="ref" reference="lem1.11"} and [\[zpvlem2\]](#zpvlem2){reference-type="ref" reference="zpvlem2"}, each $R'\otimes_{C_{R'}}C_i=R'_i$ is a simple difference ring, with field of constants $C_i$. Hence $R'_i$ is a Picard-Vessiot ring for $\si(X)=AX$ over $KC$ (and also over $KC_i$). Note that $d\leq \deg(f)=[C_{R'}:C_K]$, and that $\Krd(R'_i)=\Krd(R')$ (because $KC$ is algebraic over $K$, and $R'_i$ is finitely generated over $K$).

By Proposition [\[p2\]](#p2){reference-type="ref" reference="p2"}, $R'_i\otimes_{KC_i}K_1C_i$ is a Picard-Vessiot ring. Because $C_i$ and $K_1$ are linearly disjoint over $C$, and $C_i$ is algebraic over $C$, $KC_i\otimes_{KC}K_1\simeq K_1C_i$, and therefore $$R'_i\otimes_{KC}K_1\simeq  R'_i\otimes_{KC_i}K_1C_i.$$ This shows that $R'\otimes_{K}K_1$ is the direct sum of Picard-Vessiot rings over $K_1$.

Identifying $C_{R'}$ with $e_jC_{R'}=C_{R_j}$, we obtain $$R'_i=(\oplus_{j=0}^{\ell-1}R_j)\otimes_{C_{R'}}C_i\simeq
\oplus_{j=0}^{\ell-1}R_j\otimes_{C_{R'}}C_i.$$ Each $R_j$ being a Picard-Vessiot ring for $\si^\ell(X)=A_\ell X$, we know by Proposition [\[p2\]](#p2){reference-type="ref" reference="p2"} that $R_j\otimes_{C_{R'}}C_i$ is also a Picard-Vessiot ring for $\si^\ell(X)=A_\ell X$. Thus $R_0\otimes_{C_{R'}}C_i=\sum_{j=0}^{s-1}S_j$, where each $S_j$ is a simple $\si^{\ell s}$-difference ring, and a domain. Because all rings $R_j$ are isomorphic over $C_{R'}$, and all $S_j$ are isomorphic over $C_{R'}$, $m(R'_i)$ is the product of $\ell s$ with $m(S_0)=[D_{S_0^*}:C_{S_0^*}]$, where $S_0^*$ is the field of fractions of $S_0$. To show that $m(R'_i)=m(R')$, it therefore suffices to show that $sm(S_0)=m(R_0)$. By Lemma [\[zpvlem2\]](#zpvlem2){reference-type="ref" reference="zpvlem2"}.2, $Fix(\si^{\ell
  s})(S_0^*)=Fix(\si^\ell)(R_0^*\otimes_{C_{R'}}C_i)=Fix(\si)(R'\otimes_{C_{R'}}C_i)=C_i$.

We know that $D_{R_0^*}$ is a (cyclic) Galois extension of $C_{R'}=Fix(\si^\ell)(R_0^*)$, and is therefore linearly disjoint from $C_i$ over $D_{R^*_0}\cap C_i=C'_i$. Write $C'_i=C_{R'}(\alpha)$, and let $a,b\in R_0$, $b\neq 0$, be such that (inside $R_0^*$), $C_{R'}(a/b)=C'_i$. The minimal prime ideals of $R_0\otimes_{C_{R'}}C_i$ are the ideals $Q_0,\ldots, Q_{r-1}$, where $r=[C'_i:C_{R'}]$ and $Q_k$ is generated by $\si^{k\ell}(a)\otimes
1 -\si^{k\ell}(b)\otimes \alpha$. This shows that $r=s$, since $s$ is also the number of minimal prime ideals of $R_0\otimes_{C_{R'}}C_i$.

Let $e$ be a primitive idempotent of $R_0\otimes_{C_{R'}}C_i$ such that $S_0=e(R_0\otimes_{C_{R'}}C_i)$. Then $eC_iD_{R_0^*}$ is a subfield of $S_0^*$, contained in $D_{S_0^*}$, and its degree over $eC_i=Fix(\si^{\ell s})(S_0^*)$ is the quotient of $[D_{R_0^*}:C_{R'}]$ by $[C'_i:C_{R'}]$, i.e., equals $m(R_0)/s$. To finish the proof, it therefore suffices to show that $D_{S_0^*}=eC_iD_{R_0}^*$.

Assume that $c\in R^*_0\otimes_{C_{R'}}C_i$ satisfies $\si^m(c)=c$ for some $m\neq 0$. Write $c=\sum_{k}a_k\otimes c_k$, where the $a_k$ are in $R^*_0$, and the $c_k$ are in $C_i$ and are linearly independent over $C_{R'}$. Then $\si^m(c)=c=\sum_k\si^m(a_k)c_k$, which implies $\si^m(a_k)=a_k$ for all $k$, and all $a_k$'s are in $D_{R_0^*}$. As every element of $D_{S_0^*}$ is of the form $ec$ for such a $c$ (Lemma [\[zpvlem1\]](#zpvlem1){reference-type="ref" reference="zpvlem1"}.3), this shows that $D_{S_0^*}=eC_iD_{R_0}^*$. This finishes the proof that $m(R'_i)=m(R')$.

Consider now $R'\otimes_{KC}K_1$. It is the direct sum of $\ell s$ $\si^{\ell s}$-difference rings, each one being isomorphic to $S_0\otimes_{KC}K_1$. Because $K_1$ is a regular extension of $KC$, $S_0\otimes_{KC}K_1$ is a domain, of Krull dimension equal to $\Krd(S_0)=\Krd(R')$. Inside its field of fractions (a $\si^{\ell
s}$-difference field) $K_1$ and $S^*_0$ are linearly disjoint over $KC$, which implies that $C_{K_1}C_i$ is the field of constants of $S_0\otimes _{KC}K_1$, $C_{K_1}D_{S_0^*}$ is the field of elements fixed by some power of $\si$, and $[C_{K_1}D_{S_0^*}:C_{K_1}C_i]=[D_{S_0}^*:C_i]=m(S_0)$. This shows that $m(R'_i\otimes_{KC}K_1)=m(R')$ and finishes the proof. ◻
:::

::: prop
[]{#zp3 label="zp3"}Assume that $C_K=D_K$. Then all Picard-Vessiot rings for $\si(X)=AX$ over $K$ have the same Krull dimension and the same $m$-invariant.
:::

::: proof
*Proof.* Let $C$ be the algebraic closure of $C_K$, and let $R''$ be a Picard-Vessiot ring for $\si(X)=AX$ over $K$. By Proposition [\[zp2\]](#zp2){reference-type="ref" reference="zp2"}, $R'\otimes_{K}KC$ is the direct sum of finitely many Picard-Vessiot rings for $\si(X)=AX$ over $KC$, and each of these rings has the same Krull dimension and $m$-invariant as $R'$. The same statement holds for $R''$. On the other hand, by Proposition 1.9 of [@PuSi], all Picard-Vessiot rings over $KC$ are isomorphic. ◻
:::

::: cor
[]{#zcor1 label="zcor1"}Assume $D_K=C_K$. Let $R''=K[V,\det(V)^{-1}]$, where $\si(V)=AV$, and assume that $\Krd(R'')=\Krd(R')$ and that $R''$ has no nilpotent elements. Then $R''$ is a finite direct sum of Picard-Vessiot rings for $\si(X)=AX$.
:::

::: proof
*Proof.* Because $R''$ has no nilpotent elements and is Noetherian, $(0)$ is the intersection of the finitely many prime minimal ideals of $R''$. Let $\calP$ be the set of minimal prime ideals of $R''$. Then the intersection of any proper subset of $\calP$ is not $(0)$, i.e., no element of $\calP$ contains the intersection of the other elements of $\calP$. Also, if $P\in
  \calP$, then $\si(P)\in \calP$, and there exists $m>0$ such that $\si^m(P)=P$. Then $I_P=\bigcap_{i=0}^{m-1}\si^i(P)$ is a $\si$-ideal, which is proper if the orbit of $P$ under $\si$ is not all of $\calP$. Observe that for each $P\in\calP$, $\Krd(R''/P)\leq {\Krd}(R''/I_P)\leq
  \Krd(R'')={\Krd}(R')$, and that for some $P$ we have equality.

If $I$ is a maximal $\si$-ideal of $R''$, then ${\Krd}(R''/I)=\Krd(R')={\Krd}(R'')$ by Proposition [\[zp2\]](#zp2){reference-type="ref" reference="zp2"}, and this implies that $I$ is contained in some $P\in \calP$. Hence $I=I_P$ and $R''/I_P$ is a Picard-Vessiot ring. If $I=(0)$, then we are finished. Otherwise, $\calP$ contains some element $P_1$ not in the orbit of $P$ under $\si$. Observe that $I_{P_1}$ is contained in some maximal $\si$-ideal of $R''$, and is therefore maximal, by the same reasoning. Since the intersection of any proper subset of $\calP$ is non-trivial, $I_P+I_{P_1}$ is a $\si$-ideal of $R''$ which contains properly $I_P$, and therefore equals $1$. If $P_1, \ldots ,P_r$ are representatives from the $\sigma$-orbits in $\calP$, the Chinese Remainder Theorem then yields $R''\simeq \oplus_{i = 1}^r R''/I_{P_i}$. ◻
:::

::: prop
[]{#zp4 label="zp4"} Assume $C_K=D_K$. Then $KC_L[R]$ is a Picard-Vessiot ring for $\si(X)=AX$ over $KC_L$, $${\Krd}(R')={\rm tr.deg}(L/KC_L),\quad\hbox{and
}[D_L:C_L]=m(R').$$
:::

::: proof
*Proof.* Let us first assume that $R'$ is a domain. There is some generic difference field $\calu$ containing $R'$ and its field of fractions $R^*$, and which is sufficiently saturated. Because $L$ is a regular extension of $K$, there is some $K$-embedding $\varphi$ of $L$ into $\calu$, and we will denote by $T$ the image of $Y$ in $\calu$, and by $y$ the image of $Y$ in $R'$. Then $\varphi(C_L)\subset C_\calu$, and there is some $B\in
  \GL_n(C_{\calu})$ such that $T=yB$. Hence $$KC_\calu[T,\det(T)^{-1}]=KC_\calu[y,\det(y)^{-1}].$$ By Proposition [\[zp2\]](#zp2){reference-type="ref" reference="zp2"}, $R'\otimes_KKC_\calu$ is a direct sum of Picard-Vessiot rings of $\si(X)=AX$ over $KC_\calu$, and clearly one of those is the domain $KC_\calu[y,\det(y)^{-1}]$. Thus $\Krd(R')={\rm tr.deg}(R^*/K)={\rm tr.deg}(L/KC_L)$, $D_{R^*}C_\calu=\varphi(D_L)C_\calu$, and $m(R')=[D_L:C_L]$.

This implies also that $K\varphi(C_L)[T,\det(T)^{-1}]$ is a simple difference ring, and therefore a Picard-Vessiot ring for $\si(X)=AX$ over $K\varphi(C_L)$. Hence $KC_L[R]$ is a Picard-Vessiot extension for $\si(X)=AX$ over $KC_L$.

In the general case, we replace $R'$ by $R_0$, $\si$ by $\si^\ell$, find some generic sufficiently saturated $\si^\ell$-difference field $\calu$ containing $R_0$, and a $K$-embedding $\varphi$ of the $\si^\ell$-difference domain $L$ into $\calu$, and conclude as above that $KFix(\si^\ell)[R_0]=KFix(\si^\ell)[\varphi(R)]$, that the Krull dimension of $R'$ equals ${\rm
  tr.deg}(L/KC_L)$, and that $m(R_0)=[Fix(\si^\ell)(\varphi(D_L)):Fix(\si^\ell)]$.

Because $K$ and $D_L$ are linearly disjoint over $C_K$, $[KD_L:KC_L]=[D_L:C_L]$, whence $D_{KC_L}=KC_L$, and by Corollary [\[zcor1\]](#zcor1){reference-type="ref" reference="zcor1"}, the difference domain $KC_L[R]$ is a simple difference ring, i.e., a Picard-Vessiot ring for $\si(X)=AX$ over $KC_L$. By Proposition [\[zp2\]](#zp2){reference-type="ref" reference="zp2"} $m(R')=[D_L:C_L]$.

We have $m(R')=\ell m(R_0)$, and $m(R_0)$ is the quotient of $[D_L:C_L]$ by the greatest common divisor of $[D_L:C_L]$ and $\ell$. ◻
:::

::: cor
[]{#zcor2 label="zcor2"}Assume that $C_K=D_K$. Let $R''=K[V,\det(V)^{-1}]$ be a difference domain, where $\si(V)=AV$, with field of fractions $L_1$, and assume that $C_{L_1}$ is a finite algebraic extension of $C_K$. Then $R''$ is a Picard-Vessiot ring for $\si(X)=AX$ over $K$.
:::

::: proof
*Proof.* Let $\calu$ be a sufficiently saturated generic difference field containing $R''$, and let $\varphi$ be a $K$-embedding of $L$ into $\calu$. Then $KC_\calu[\varphi(R)]=KC_\calu[R'']$. Hence $\Krd(R'')=\Krd(R')$ and $R''$ is a Picard-Vessiot ring by Corollary [\[zcor1\]](#zcor1){reference-type="ref" reference="zcor1"}. ◻
:::

::: cor
[]{#zcor3 label="zcor3"}Assume that $C_K$ is algebraically closed. Then $\ell(R')=[D_L:C_L]$.
:::

::: proof
*Proof.* Immediate from Proposition [\[zp4\]](#zp4){reference-type="ref" reference="zp4"} and the fact that $D_{R^*}=C_{R'}=C_K$. ◻
:::

::: cor
[]{#zcor4 label="zcor4"}The difference ring $KC_L[R]$ is a Picard-Vessiot ring for $\si(X)=AX$ over $KC_L$. All Picard-Vessiot rings for $\si(X)=AX$ over $K$ have the same Krull dimension, which equals ${\rm tr.deg}(L/KC_L)$.
:::

::: proof
*Proof.* Let $m=[D_K:C_K]$. Note that replacing $\si$ by some power of $\si$ does not change the fields $D_K$ or $D_L$, and that $Fix(\si^m)(K)=D_K$. Therefore we can apply the previous results to the equation $\sigma^m(X) = A_mX$ over $K$. By Corollary [\[zcor2\]](#zcor2){reference-type="ref" reference="zcor2"} and because $KC_L[R]$ is a domain, $KC_L[R]$ is a Picard-Vessiot ring for $\si^m(X)=A_mX$ over $KC_L$, and therefore a simple $\si^m$-difference ring, whence a simple $\si$-difference ring, and finally a Picard-Vessiot ring for $\si(X)=AX$ over $K$.\
Let $R'=R/q$ be a Picard-Vessiot ring for $\si(X)=AX$ over $K$. Assume first that $R'$ is a domain, and let $\calu$ be a generic difference field containing it. Because $L$ is a regular extension of $K$, there is a $K$-embedding $\varphi$ of $L$ into $\calu$, and from $KC_\calu[\varphi(R)]=KC_\calu[R']$ and Lemma [\[zpvlem2\]](#zpvlem2){reference-type="ref" reference="zpvlem2"}.1, we obtain the result. If $R'$ is not a domain, then we reason in the same fashion, replacing $R'$ by $R_0$ and $\si$ by $\si^\ell$, to obtain the result. ◻
:::

::: prop
[]{#zp5 label="zp5"}Assume that $C_{R'}=C_K=D_K$ and $K\subset \calu$. Then $G_{R'}$ and $\HX$ are isomorphic.
:::

::: proof
*Proof.* By Proposition [\[p2\]](#p2){reference-type="ref" reference="p2"}, we may replace $R'$ by $R'\otimes_KKD'_\calu$, and consider the ring $K\varphi(C_L)[T, \det(T)^{-1}]\otimes_{K\varphi(C_L)}KD'_\calu$, which is a Picard-Vessiot ring by Proposition [\[zp4\]](#zp4){reference-type="ref" reference="zp4"} and Corollary [\[zcor1\]](#zcor1){reference-type="ref" reference="zcor1"}. We identify $1\otimes KD'_\calu$ with $KD'_\calu$. These two rings are isomorphic over $KD'_\calu$ by Proposition 1.9 of [@PuSi], and it therefore suffices to show that $$\Aut(\varphi(L)\otimes_{K\varphi(C_L)}KD'_\calu/KD'_\calu)=\HX(D'_\calu).$$ Inside $\varphi(L)\otimes_{K\varphi(C_L)}KD'_\calu$, $\varphi(L)\otimes 1$ and $KD'_\calu$ are linearly disjoint over $K\varphi(C_L)$. Hence, the algebraic loci of $(T,\det(T)^{-1})$ over $K\varphi(C_L)$ and over $KD'_\calu$ coincide. As $\HX$ was described as the subgroup of $\GL_n$ which leaves this algebraic set invariant, we get the result. ◻
:::
