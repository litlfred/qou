---
doc_id: arxiv-0705.2975v1
doc_title: "On the Deﬁnitions of Diﬀerence Galois Groups"
section_id: sec-006-the-galois-group
section_title: "The Galois group"
section_number: null
pages: 18-20
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.994
doc_brief: "On the Deﬁnitions of Diﬀerence Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and show, that"
---
[]{#zpv label="zpv"} From now on, we assume that all fields are of characteristic $0$. Most of the statements below can be easily adapted to the positive characteristic case. Let $K$ be a difference subfield of $\calu$, $A\in \GL_n(K)$, and consider the set $\calS=\calS(\calu)$ of solutions of the equation $$\si(X)=AX,\ \det(X)\neq 0.$$ Consider $H=\Aut(K(\calS)/KC_\calu)$. We will call $H$ the *Galois group of $\si(X)=AX$ over $KC_\calu$*[^1].

Then $H$ is the set of $C_\calu$-points of some algebraic group $\HX$ defined over $KC_\calu$. To see this, we consider the ring $R=K[Y, \det(Y)^{-1}]$ (where $Y=(Y_{i,j})$ is an $n\times n$ matrix of indeterminates), extend $\si$ to $R$ by setting $\si(Y)=AY$, and let $L$ be the field of fractions of $R$. Then $L$ is a regular extension of $K$, and there is a $K$-embedding $\varphi$ of $L$ in $\calu$, which sends $C_L$ to a subfield of $C_\calu$, and $D_L$ to a subfield of $D_\calu$. We let $T=\varphi(Y)$. Then every element $g\in H$ is completely determined by the matrix $M_g=T^{-1}g(T)\in
\GL_n(C_\calu)$, since if $B\in \calS$, then $B^{-1}T\in\GL_n(C_\calu)$. Moreover, since $KC_{\varphi(L)}(T)$ and $KC_\calu$ are linearly disjoint over $KC_{\varphi(L)}$, the algebraic locus $W$ of $T$ over $KC_\calu$ (an algebraic subset of $\GL_n$) is defined over $KC_{\varphi(L)}$, and $H$ is the set of elements of $\GL_n(C_\calu)$ which leave $W$ invariant. It is therefore the set of $C_\calu$-points of an algebraic group $\HX$, defined over $KC_{\varphi(L)}$. We let $\HX'$ denote the Zariski closure of $\HX(C_\calu)$. Then $\HX'$ is defined over $C_\calu$, and it is also clearly defined over $\overline{K\varphi(C_L)}$, so that it is defined over $C_\calu\cap
  \overline{K\varphi(C_L)}=C_\calu\cap \overline{\varphi(C_L)}$.

::: prop
[]{#zggp1 label="zggp1"}Let $\HX^0$ denote the connected component of $\HX$, and let $M_0$ be the relative algebraic closure of $K\varphi(C_L)$ in $\varphi(L)$, $M$ its Galois closure over $K\varphi(C_L)$.

-   $\dim(\HX)={\rm tr.deg}(L/KC_L)$.

-   $M_0$ is a finite $\si$-stable extension of $K\varphi(C_L)$ and $[\HX:\HX^0]$ divides $[M:K\varphi(C_L)]$

-   $[\HX':\HX^0]=[\HX(C_\calu):\HX^0(C_\calu)]$ equals the number of left cosets of $\calG al(M/M_0)$ in $\calG al(M/K\varphi(C_L))$ which are invariant under the action of $\si$ by conjugation.

-   If the algebraic closure of $C_K$ is contained in $C_\calu$, then the element $\si\in \Aut(D_L/C_L)=\calG al(D_L/C_L)$ extends to an element of $\Aut(KC_\calu(T)/KC_\calu)$.
:::

::: proof
*Proof.* 1. Choose another $K$-embedding $\varphi'$ of $L$ into $\calu$ which extends $\varphi$ on the relative algebraic closure of $KC_L$ in $L$, and is such that $\varphi'(L)$ and $\varphi(L)$ are linearly disjoint over $M_0$. Then $B=\varphi'(Y)^{-1}T\in \HX(C_\calu)$, and ${\rm
  tr.deg}(\varphi(KC_L)(B))/\varphi(KC_L))={\rm tr.deg}(L/KC_L)$. Thus $\dim(\HX)={\rm tr.deg}(L/KC_L)$.\
2. As $M_0\subset K\varphi(L)$, we obtain that $[M_0:K\varphi(C_L)]$ is finite and $\si(M_0)=M_0$. Furthermore, $\si(M)=M$ (see Thm 7.16.V in [@cohn]). The algebraic group $\HX$ is defined as the set of matrices of $\GL_n$ which leaves the algebraic set $W$ (the algebraic locus of $T$ over $K\varphi(C_L)$) invariant.

Hence $\HX^0$ is the subgroup of $\HX$ which leaves all absolutely irreducible components of $W$ invariant. Its index in $\HX$ therefore divides $[M:K\varphi(C_L)]$.\
3. The first equality follows from the fact that $\HX^0(C_\calu)$ and $\HX'(C_\calu)$ are Zariski dense in $\HX^0$ and $\HX'$ respectively. Some of the (absolutely irreducible) components of $W$ intersect $\calS$ in the empty set. Indeed, let $W_0$ be the component of $W$ containing $T$, let $W_1$ be another component of $W$ and $\tau\in
  {\calG}al(M/K\varphi(C_L))$ such that $W_1=W_0^\tau$. Then $W_1$ is defined over $\tau(M_0)$. If $\tau$ defines a (difference-field) isomorphism between $M_0$ and $\tau(M_0)$, then $\tau$ extends to an isomorphism between $K\varphi(L)$ and a regular extension of $K\varphi(C_L)\tau(M_0)$, and therefore $W_1\cap \calS\neq \emptyset$. Conversely, if $B\in W_1\cap
  \calS$, then $B^{-1}T\in \HX(C_\calu)$, so that $B$ is a generic of $W_1$. The difference fields $K\varphi(C_L)(B)$ and $K\varphi(L)$ are therefore isomorphic (over $K\varphi(C_L)$), and $\tau(M_0)\subset K\varphi(C_L)(B)$. Hence the difference subfields $M_0$ and $\tau(M_0)$ of $M$ are $K\varphi(C_L)$-isomorphic. One verifies that $M_0$ and $\tau(M_0)$ are isomorphic over $K\varphi(C_L)$ if and only if $\si^{-1} \tau^{-1}
  \si\tau\in \calG al(M/M_0)$, if and only if the coset $\tau\calG
  al(M/M_0)$ is invariant under the action of $\si$ by conjugation.\
4. We know that the algebraic closure $\overline{K}$ of $K$ and $D_\calu$ are linearly disjoint over $C_{\overline{K}}=\overline{C_K}$. Let $a\in \varphi(D_L)$ generates $\varphi(D_L)$ over $\varphi(C_L)$. By [\[mt1\]](#mt1){reference-type="ref" reference="mt1"}(vi), $tp(a/\overline{K}C_\calu)=tp(\si(a)/\overline{K}C_\calu)$, and therefore there is $\theta\in\Aut(\calu/\overline{K}C_\calu)$ such that $\theta(a)=\si(a)$. Thus $T^{-1}\theta(T)\in H$. ◻
:::

::: remarks
[]{#zgprem label="zgprem"}

-   Even when the algebraic closure of $C_K$ is contained in $C_\calu$, we still cannot in general conclude that $\HX'=\HX$.

-   The isomorphism type of the algebraic group $\HX$ only depends on the isomorphism type of the difference field $K$ (and on the matrix $A$). The isomorphism type of the algebraic group $\HX'$ does however depend on the embedding of $K$ in $\calu$, that is, on the isomorphism type of the difference field ${\rm Core}(\overline{K}/K)$. Indeed, while we know the isomorphism type of the difference field $M_0$ over $K\varphi(C_L)$, we do not know the isomorphism type of the difference field $M$ over $K\varphi(C_L)$, and in view of [\[zggp1\]](#zggp1){reference-type="ref" reference="zggp1"}.3, if $\calG
      al(M/K\varphi(C_L))$ is not abelian, it may happen that non-isomorphic extensions of $\si$ to $M$ yield different Galois groups.

-   If the action of $\si$ on $\Gal({\rm
    Core}(\overline{K}/K)/K)$ is trivial and $\Gal({\rm
    Core}(\overline{K}/K)/K)$ is abelian, then $$\HX=\HX'\quad \hbox{and}\quad
    [\HX:\HX^0]=[M_0:K\varphi(C_L)].$$ Indeed, by Lemma [\[zlem1\]](#zlem1){reference-type="ref" reference="zlem1"}, $M_0$ is Galois over $K\varphi(C_L)$ with abelian Galois group $G$ and $\si$ acts trivially on $G$. The result follows by [\[zggp1\]](#zggp1){reference-type="ref" reference="zggp1"}.3. Thus we obtain equality of $\HX$ and $\HX'$ in two important classical cases:

    -   $K=\CX(t)$, $C_K=\CX$ and $\si(t)=t+1$.

    -   $K=\CX(t)$, $C_K=\CX$ and $\si(t)=qt$ for some $0\neq q\in\CX$, $q$ not a root of unity.

-   If $B\in \calS$, then the above construction can be repeated, using $B$ instead of $T$. We then obtain an algebraic group $\HX_1$, with $\HX_1(C_\calu)\simeq \Aut(KC_\calu(\calS)/KC_\calu)$. Since $KC_\calu(B)=KC_\calu(T)$, the algebraic groups $\HX_1$ and $\HX$ are isomorphic (via $B^{-1}T$).

-   In the next subsection, we will show that the algebraic group $\HX$ and the algebraic group $G_{R'}$ introduced in section [\[galoissec\]](#galoissec){reference-type="ref" reference="galoissec"} are isomorphic when $C_{R'}=C_K=D_K$.
:::

[^1]:  Warning: This is not the usual Galois group defined by model theorists, please see the discussion in subsection [\[mt4\]](#mt4){reference-type="ref" reference="mt4"}.
