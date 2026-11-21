---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-003-22-regular-semisimple-elements
section_title: "Regular semisimple elements"
section_number: 2.2
pages: 3-5
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.933
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:regss label="subsec:regss"} We need to know that certain maximal tori contain regular elements. As before, let $q$ be a prime power. For a prime $\ell$ not dividing $q$ we denote by $d_\ell(q)$ the order of $q$ modulo $\ell$, that is the smallest $d\ge1$ with $\ell \mid (q^d-1)$. If $d$ is even then we have $\ell \mid (q^{d/2}+1)$. With these definitions, $\ell \mid (q^k-1)$ if and only if $d \mid k$, and for even $d$ we have $\ell \mid (q^k+1)$ if and only if $k$ is an odd multiple of $d/2$.

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

We have described the maximal torus ${\mathbf{T}}$ of diagonal elements in $\tilde{\mathbf{G}}$ in Section [\[subsec:WeylBCD\]](#subsec:WeylBCD){reference-type="ref" reference="subsec:WeylBCD"}. The connected centraliser $C_{\tilde{\mathbf{G}}}^\circ(t)$ of $t\in{\mathbf{T}}$ equals ${\mathbf{T}}$ if and only if $\alpha(t) = 1$ for all roots $\alpha$ of ${\mathbf{G}}$ with respect to ${\mathbf{T}}$. These roots are explicitly given in [@DM Chap. 15] (for types $C_n$ and $D_n$, but type $B_n$ is very similar): It is enough to describe a set of positive roots. Their values on $t = \textrm{diag}(t_1,
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
