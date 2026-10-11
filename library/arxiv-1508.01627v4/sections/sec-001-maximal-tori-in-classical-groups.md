---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-001-maximal-tori-in-classical-groups
section_title: "Maximal tori in classical groups"
section_number: 2
pages: 2-5
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.984
---
[]{#sec:maxtor label="sec:maxtor"}

In this section we establish the existence of regular semisimple $\ell$-singular elements in suitable tori of classical groups of Lie type. This will be a main ingredient in the proof of the vanishing Theorem [\[thmA:zeroes\]](#thmA:zeroes){reference-type="ref" reference="thmA:zeroes"}. Moreover, we formulate a criterion for collections of maximal tori of simple algebraic groups not to be contained in a common proper reductive subgroup.

## Weyl groups and maximal tori in symplectic and orthogonal groups {#subsec:WeylBCD}

For a prime power $q$ and $K = \overline{{\mathbb{F}}_q}$ we consider the natural representation of ${\mathbf{G}}= {\operatorname{Sp}}_{2n}(K)$ on $V = K^{2n}$ (case $C_n$) and of ${\mathbf{G}}= {\operatorname{SO}}_{2n+1}(K)$ on $V = K^{2n+1}$, and a Steinberg morphism $F$ on ${\mathbf{G}}$ with fixed point group ${\mathbf{G}}^F = {\operatorname{Sp}}_{2n}(q)$, respectively ${\mathbf{G}}^F = {\operatorname{SO}}_{2n+1}(q)$. With respect to an appropriate choice of basis of $V$ we can assume (see [@MT Exmp. 6.7]) that the subgroup ${\mathbf{T}}$ of diagonal matrices forms an $F$-stable maximal torus of ${\mathbf{G}}$, its elements have the form ${\operatorname{diag}}(t_1, \ldots, t_n,t_n^{-1}, \ldots, t_1^{-1})$, respectively ${\operatorname{diag}}(t_1, \ldots, t_n,1,t_n^{-1}, \ldots, t_1^{-1})$, and $F$ acts by raising the diagonal entries to their $q$-th power. The Weyl group $W$ acts on ${\mathbf{T}}$ by its natural permutation action on the diagonal entries. More precisely, $W$ is isomorphic to the wreath product $C_2\wr{\mathfrak{S}}_n$, where the cyclic groups of order $2$ interchange the entries $\{t_i, t_i^{-1}\}$, $i = 1, \ldots, n$, while the symmetric group permutes the $n$ pairs $\{t_i, t_i^{-1}\}$. See [@DM Chap. 15] for more details.

The ${\mathbf{G}}^F$-conjugacy classes of $F$-stable maximal tori of ${\mathbf{G}}$ are parameterised by the conjugacy classes of $W$. An element $t\in {\mathbf{T}}$ is conjugate to an element $t' \in {\mathbf{G}}^F$ if ${}^wF(t)=t$ for some $w \in W$. Then $t'$ lies in an $F$-stable maximal torus parameterised by the class of $w$. Such an element $t'$ is regular semisimple if $w$ is unique.

The conjugacy classes of $W$ are parameterised by pairs of partitions $(\lambda,\mu) \vdash n$ of $n$ as follows: If $w \in W$ permutes entries of a regular diagonal element as above, then a cycle containing entries $t_i$ and $t_i^{-1}$ for some $i$ is of even length $2\mu_j$ and contributes a part $\mu_j$ to $\mu$. Otherwise a cycle of length $\lambda_j$ permutes some diagonal entries and there is another cycle of the same length permuting the inverse diagonal entries in the same way; this contributes a part $\lambda_j$ to $\lambda$.

We can embed an even dimensional orthogonal group ${\mathbf{G}}= {\operatorname{SO}}_{2n}(K)$ (type $D_n$) into $\tilde{\mathbf{G}}= {\operatorname{SO}}_{2n+1}(K)$ such that it is stable under the Steinberg morphism of $\tilde{\mathbf{G}}$ and its fixed points are ${\mathbf{G}}^F =
{\operatorname{SO}}^+_{2n}(q)$. There is a second Steinberg morphism $F'$ on ${\mathbf{G}}$ leading to the twisted groups ${\mathbf{G}}^{F'} = {\operatorname{SO}}^-_{2n}(q)$. The Weyl group $W$ of ${\mathbf{G}}$ is a subgroup of index $2$ in the Weyl group $\tilde{W}$ of $\tilde{\mathbf{G}}$, consisting of the conjugacy classes of $\tilde W$ whose parameter $(\lambda,\mu)$ has an even number of parts in $\mu$. If $\mu$ is empty in $(\lambda,\mu)$ and $\lambda$ has only even parts then the corresponding class in $\tilde W$ splits into two classes in $W$, called *degenerate* classes. The twisted Steinberg morphism $F'$ acts on $W$ like conjugation by the short root generator of $\tilde W$. This way the $F'$-conjugacy classes of $W$ can be parameterised by the conjugacy classes of $\tilde W$ whose parameter $(\lambda, \mu)$ has an odd number of parts in $\mu$. Since ${\mathbf{G}}$ and $\tilde{\mathbf{G}}$ have the same rank, maximal tori of ${\mathbf{G}}$ are also maximal tori of $\tilde{\mathbf{G}}$.

Let $(\la,\mu) = ((\la_1, \ldots, \la_r),(\mu_1,\ldots,\mu_s)) \vdash n$. Then the order of the corresponding maximal torus ${\mathbf{T}}^F$ in ${\mathbf{G}}^F$ is $$|{\mathbf{T}}^F| = \prod_{i=1}^{r}(q^{\la_i}-1) \prod_{i=1}^{s}(q^{\mu_i}+1)$$ and ${\mathbf{T}}^F$ contains cyclic subgroups of orders $q^{\la_i}-1$ and $q^{\mu_i}+1$ for all $i$.

## Regular semisimple elements {#subsec:regss}

We need to know that certain maximal tori contain regular elements. As before, let $q$ be a prime power. For a prime $\ell$ not dividing $q$ we denote by $d_\ell(q)$ the order of $q$ modulo $\ell$, that is the smallest $d\ge1$ with $\ell \mid (q^d-1)$. If $d$ is even then we have $\ell \mid (q^{d/2}+1)$. With these definitions, $\ell \mid (q^k-1)$ if and only if $d \mid k$, and for even $d$ we have $\ell \mid (q^k+1)$ if and only if $k$ is an odd multiple of $d/2$.

::: lem
[]{#lem:regelts label="lem:regelts"} Let ${\mathbf{G}}$ be a simple simply-connected classical group of type $B_n$, $C_n$ or $D_n$ defined over the finite field ${\mathbb{F}}_q$ with corresponding Steinberg morphism $F$.

Let $(\la,\mu) = ((\la_1, \ldots, \la_r),(\mu_1, \ldots, \mu_s))$ be a pair of partitions of $n$, and ${\mathbf{T}}$ a corresponding $F$-stable maximal torus of ${\mathbf{G}}$. Then ${\mathbf{T}}^F$ contains regular elements if one of the following conditions is fulfilled.

-   $q>3$, $\la_1 < \la_2 < \ldots < \la_r$ and $\mu_1 < \mu_2 <
        \ldots < \mu_s$;

-   $q \in \{2,3\}$, $\la_1 < \la_2 < \ldots < \la_r$, $\mu_1 < \mu_2 <
         \ldots < \mu_s$, all $\la_i \neq 2$, and if ${\mathbf{G}}$ is of type $B_n$ or $C_n$ then also all $\la_i \neq 1$; or

-   ${\mathbf{G}}$ is of type $D_n$, $2 < \la_1 < \la_2 < \ldots < \la_r$ and $1 = \mu_1 = \mu_2 < \mu_3 < \ldots < \mu_s$.
:::

::: proof
*Proof.* (a) We use the natural representations of $\tilde{\mathbf{G}}= {\operatorname{Sp}}_{2n}(K)$ and $\tilde{\mathbf{G}}= {\operatorname{SO}}_{2n+1}(K)$ with the natural Steinberg morphism that raises matrix entries to their $q$-th power, and we consider ${\operatorname{SO}}_{2n}^\pm(q)$ as subgroups of ${\operatorname{SO}}_{2n+1}(K)$.

We have described the maximal torus ${\mathbf{T}}$ of diagonal elements in $\tilde{\mathbf{G}}$ in Section [0.1](#subsec:WeylBCD){reference-type="ref" reference="subsec:WeylBCD"}. The connected centraliser $C_{\tilde{\mathbf{G}}}^\circ(t)$ of $t\in{\mathbf{T}}$ equals ${\mathbf{T}}$ if and only if $\alpha(t) = 1$ for all roots $\alpha$ of ${\mathbf{G}}$ with respect to ${\mathbf{T}}$. These roots are explicitly given in [@DM Chap. 15] (for types $C_n$ and $D_n$, but type $B_n$ is very similar): It is enough to describe a set of positive roots. Their values on $t = \textrm{diag}(t_1,
t_2, \ldots, t_n, t_n^{-1}, \ldots, t_1^{-1})$ respectively $t = \textrm{diag}(t_1, t_2, \ldots, t_n, 1, t_n^{-1}, \ldots, t_1^{-1})$ are

(Types $B_n$, $C_n$, $D_n$) $\alpha(t) = t_i t_j^{-1}$ and $\alpha(t) = t_i
t_j$ for $1\leq i < j \leq n$,

(Type $B_n$ only) $\alpha(t) = t_i$ for $1\leq i \leq n$,

(Type $C_n$ only) $\alpha(t) = t_i^2$ for $1\leq i \leq n$.

So, $C_{\tilde{\mathbf{G}}}^\circ(t) = {\mathbf{T}}$ if and only if for all $1 \leq i < j \leq n$ we have $t_i \neq t_j$ and $t_i \neq t_j^{-1}$, and in type $B_n$ we also have $t_i \neq 1$ for $1 \leq i \leq n$, and in type $C_n$ we also have $t_i \neq \pm 1$ for $1 \leq i \leq n$.

\(b\) In type $C_n$ we have ${\mathbf{G}}= \tilde {\mathbf{G}}$, while in types $B_n$ and $D_n$ the groups ${\operatorname{SO}}_{2n+1}(K)$ and ${\operatorname{SO}}_{2n}(K)$ are not simply-connected. But there are isogenies from the simply-connected coverings ${\mathbf{G}}= {\operatorname{Spin}}_m(K) \to {\operatorname{SO}}_m(K) = \tilde{\mathbf{G}}$. If $q$ is even, that is $\textrm{char}(K) = 2$, then this map has a trivial kernel and induces isomorphisms ${\operatorname{Spin}}^\pm_m(q) \to {\operatorname{SO}}_m^\pm(q)$. For odd $q$ the kernel is a central subgroup of order $2$, and the image of the induced map ${\operatorname{Spin}}^\pm_m(q) \to {\operatorname{SO}}_m^\pm(q)$ of the finite groups has index $2$.

To show the existence of regular elements in tori of type $(\la, \mu)$ we construct a $t \in {\mathbf{T}}$ such that $^wF(t) = t$ for some $w\in W$ in the class $(\la,\mu)$ and $C_{\tilde{\mathbf{G}}}^\circ(t) = {\mathbf{T}}$. In cases $B_n$ and $D_n$ and odd $q$ this $t$ will be a square of another element in ${\mathbf{T}}^{wF}$ such that in all cases $t$ has a preimage in a corresponding twisted maximal torus of the simply-connected group ${\mathbf{G}}$. This preimage is regular because centralisers of semisimple elements in a simply-connected group are connected.

\(c\) Now let $(\la,\mu) = ((\la_1, \ldots, \la_r),(\mu_1, \ldots, \mu_s))
\vdash n$ be a pair of partitions. We construct $t \in {\mathbf{T}}$ by describing the entries $t_1, \ldots, t_n \in K$.

First assume that ${\mathbf{G}}$ is of type $C_n$ or that $q$ is even.

For $1 \leq i \leq r$ let $a_i \in {\mathbb{F}}_{q^{\la_i}}$ be of order $q^{\la_i}-1$ and use $a_i, a_i^q, \ldots, a_i^{q^{\la_i-1}}$ as entries of $t$ (note that $a_i^{q^{\la_i}} = a_i$).

For $1 \leq j \leq s$ let $b_j \in {\mathbb{F}}_{q^{2\mu_j}}$ be of order $q^{\mu_j}+1$ and use $b_j, b_j^q, \ldots, b_j^{q^{\mu_j-1}}$ as entries of $t$ (note that then $b_j^{q^{\mu_j}} = b_j^{-1}$).

If ${\mathbf{G}}$ is of type $B_n$ or $D_n$ and $q$ is odd, we use as $t$ the square of the element just described (so $a_i$ is of order $\frac{1}{2}(q^{\la_i}-1)$ and $b_j$ is of order $\frac{1}{2}(q^{\mu_j}+1)$).

It is clear from this construction that the Steinberg morphism $F$ of ${\operatorname{Sp}}_{2n}(K)$, respectively ${\operatorname{SO}}_{2n+1}(K)$ permutes the entries of $t$ such that this can be reversed by an element $w \in W$ of cycle type $(\la,\mu)$, so $t = {}^wF(t)$.

\(d\) We next discuss when $t$ fails to be regular. Let $\la_i,\mu_j>0$ with $q^{\la_i}-1 = q^{\mu_j}+1$. Then $\mu_j < \la_i$ and the assumption is equivalent to $q^{\mu_j}(q^{\la_i-\mu_j}-1) = 2$. It follows that $q=2$, $\mu_j=1$ and $\la_i=2$.

\(e\) Let $k \in {\mathbb{Z}}$, $0 < k < \la_i$ and assume $(q^{\la_i}-1)\mid(q^k \mp 1)$. Then $q^{\la_i}-1 \leq q^k \mp 1$, which holds if and only if $q^k(q^{\la_i-k} -1) \leq 0$ or $2$, respectively. This is only possible for $q=2$, $k=1$ and $\la_i=2$. Similarly, for odd $q$ the condition $\frac{1}{2}(q^{\la_i}-1)\mid (q^k \mp 1)$ implies $q=3$, $k=1$ and $\la_i=2$.

Now let $k \in {\mathbb{Z}}$, $0 < k < \mu_j$. A similar argument as above shows that for all $q$ we have $(q^{\mu_j}+1) \nmid (q^k \mp 1)$ and for odd $q$ we also have $\frac{1}{2}(q^{\mu_j}+1) \nmid (q^k \mp 1)$.

\(f\) Now we prove assertions (1) and (2) of the statement by showing that in those cases the element $t\in{\mathbf{T}}$ constructed in (c) does not lie in the kernel of any root.

First note that the $a_i$ ($1\leq i \leq r$) and $b_j$ ($1 \leq j \leq s$) have pairwise different orders. This follows from (d) since for $q=2$ we assume that all $\la_i \neq 2$.

According to (a) we need to show that for $1\leq i \leq r$ any of the entries $(a_i, a_i^q, \ldots, a_i^{q^{\la_i-1}})$ are not equal or inverse to each other, and similarly for the $(b_j, b_j^q, \ldots, b_j^{q^{\mu_j-1}})$. Since the map $x \mapsto x^q$ permutes these entries of $t$ and their inverses it suffices to show that for $0 <k <\la_i$ we have $a_i^{q^k} \neq
a_i^{\pm 1}$ (equivalently $a_i^{q^k\mp 1} \neq 1$), and similarly for the $b_j$. Now $a_i^{q^k\mp 1} = 1$ implies $(q^{\la_i}-1) \mid (q^k \mp
1)$ or $\frac{1}{2}(q^{\la_i}-1) \mid (q^k \mp 1)$, respectively. Using (e) this implies $\la_i = 2$ and $q\in \{2,3\}$, contradicting the assumptions.

Similarly, step (e) shows that we always have $b_j^{q^k} \neq b_j^{\pm 1}$ for $0 < k < \mu_j$.

For type $C_n$ we also have to show that $a_i^2 \neq 1$ ($1\leq i \leq r$) and $b_j^2 \neq 1$ ($1\leq j\leq s$). This holds because $a_i^2 =1$, i.e., $(q^{\la_i} -1) \mid 2$, implies $\la_i =1$ and $q \in
\{2,3\}$, contradicting the assumption. Note that always $q^{\mu_i}+1 > 2$.

For type $B_n$ we also have to show that $a_i \neq 1$ ($1\leq i \leq r$) and $b_j \neq 1$ ($1\leq j\leq s$). This follows as $q^{\la_i}-1 = 1$ implies $q=2$ and $\la_i=1$, while $\frac{1}{2}(q^{\la_i}-1) = 1$ implies $q=3$ and $\la_i=1$ for odd $q$, and as always $q^{\mu_j}+1 >1$.

\(g\) The argument for statement (3) is very similar. A suitable element $t$ can be defined as before, except that for $\mu_1=1$ we choose $b_1  = 1$. Then the entry for $\mu_2=1$ has order $q+1$ for even $q$ or $\frac{1}{2}(q+1)$ for odd $q$ which is always larger than $1$. ◻
:::

::: rem
[]{#rem:lsingreg label="rem:lsingreg"} Let ${\mathbf{G}}$ be a connected reductive group with Steinberg morphism $F$ and ${\mathbf{T}}$ an $F$-stable maximal torus of ${\mathbf{G}}$. Let $\ell$ be a prime dividing $|{\mathbf{T}}^F|$. If ${\mathbf{T}}^F$ contains a regular element then ${\mathbf{T}}^F$ also contains an $\ell$-singular regular element.
:::

::: proof
*Proof.* Let $t\in {\mathbf{T}}^F$ be an $\ell$-regular (that is of order prime to $\ell$) regular element and $u\in {\mathbf{T}}^F$ be any element of order $\ell$. Then $tu$ has order $\ell |t|$ and some power of $tu$ equals $t$, hence $tu$ is also regular. ◻
:::

## Maximal connected reductive subgroups {#subsec:maxred}

The following lemma will allow us to decide if a collection of classes of maximal tori of a classical group has representatives inside the centraliser of a semisimple element:

::: lem
[]{#lem:maxred label="lem:maxred"} Let ${\mathbf{G}}$ be a simple algebraic group of classical type $B_n,C_n$ (with $n\ge2$) or $D_n$ (with $n\ge4$) with Frobenius endomorphism $F$ such that ${\mathbf{G}}^F$ is a classical group. Let $\Lambda$ be a set of pairs of partitions $(\la,\mu)\vdash n$. Assume the following:

1.  there is no $1\le k\le n-1$ such that all $(\la,\mu)\in\Lambda$ are of the form $(\la_1,\mu_1)\sqcup(\la_2,\mu_2)$ (that is $\la$ contains the parts from $\la_1$ and $\la_2$ and similarly for $\mu$) with $(\la_1,\mu_1)\vdash k$;

2.  the greatest common divisor of all parts of all $(\la,\mu)\in\Lambda$ is 1; and

3.  if ${\mathbf{G}}$ is of type $B_n$, then there exist pairs $(\la,\mu)\in\Lambda$ for which $\mu$ has an odd number of parts, and for which $\mu$ has an even number of parts.

If $s\in{\mathbf{G}}^F$ is semisimple such that $C_{\mathbf{G}}(s)$ contains maximal tori of ${\mathbf{G}}$ corresponding to all $(\la,\mu)\in\Lambda$ then $s$ is central.
:::

::: proof
*Proof.* The types of maximal tori are insensitive to isogeny types, so we may assume that ${\mathbf{G}}$ is a classical matrix group ${\operatorname{Sp}}(V)$ or ${\operatorname{SO}}(V)$. Let $s\in{\mathbf{G}}^F$ be a non-central semisimple element. Then ${\mathbf{H}}:=C_{\mathbf{G}}^\circ(s)$ fixes each eigenspace of $s$ on $V$. Since $s$ is non-central it has at least two different eigenvalues. Since $s$ is $F$-stable, the eigenspaces of $s$ are permuted under the action of $F$. First assume that the set of eigenspaces forms one orbit, of length $f>1$ say, under the action of $F$. Then ${\mathbf{H}}$ is a central product of isomorphic classical groups, ${\mathbf{H}}^F$ is an extension field subgroup and hence its maximal tori have parameters all parts of which are divisible by $f$, contradicting (2).

So there are at least two $F$-orbits of eigenspaces. Let $V_1< V$ be an $F$-stable sum of eigenspaces of minimal possible dimension. Then either $V_1 \cap V_1^\perp \neq 0$ or $V_1$ is non-degenerate and $V = V_1 \perp
V_1^\perp$. The stabilisers of totally singular spaces are contained in maximal parabolic subgroups [@MT Prop. 12.13], but these only have tori of types as excluded by (1). Else, ${\mathbf{H}}$ is contained in the stabiliser of $V_1\perp V_1^\perp$, a central product of classical groups. The latter are of types $C_a+C_b$, respectively $B_a + D_b$ or $D_a + D_b$ with $a+b = n$, $a,b > 0$ for ${\mathbf{G}}$ of type $C_n$, respectively $B_n$, $D_n$. Then the parameters of $F$-stable maximal tori of ${\mathbf{H}}$ are of the form excluded by (1) of the lemma, for $k=a$, unless ${\mathbf{G}}$ is of type $B_n$ and $V_1$ is 1-dimensional, when ${\mathbf{H}}$ could be of type $D_n$. In that case, the number of parts in the second entry of the parameters of $F$-stable maximal tori of ${\mathbf{H}}$ all have a fixed parity (namely even for ${\mathbf{H}}^F$ untwisted, and odd for ${\mathbf{H}}^F$ twisted). This is excluded by (3). ◻
:::
