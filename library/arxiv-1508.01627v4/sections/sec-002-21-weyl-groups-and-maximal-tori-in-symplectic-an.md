---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-002-21-weyl-groups-and-maximal-tori-in-symplectic-an
section_title: "Weyl groups and maximal tori in symplectic and orthogonal groups"
section_number: 2.1
pages: 2-3
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.959
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:WeylBCD label="subsec:WeylBCD"}

For a prime power $q$ and $K = \overline{{\mathbb{F}}_q}$ we consider the natural representation of ${\mathbf{G}}= {\operatorname{Sp}}_{2n}(K)$ on $V = K^{2n}$ (case $C_n$) and of ${\mathbf{G}}= {\operatorname{SO}}_{2n+1}(K)$ on $V = K^{2n+1}$, and a Steinberg morphism $F$ on ${\mathbf{G}}$ with fixed point group ${\mathbf{G}}^F = {\operatorname{Sp}}_{2n}(q)$, respectively ${\mathbf{G}}^F = {\operatorname{SO}}_{2n+1}(q)$. With respect to an appropriate choice of basis of $V$ we can assume (see [@MT Exmp. 6.7]) that the subgroup ${\mathbf{T}}$ of diagonal matrices forms an $F$-stable maximal torus of ${\mathbf{G}}$, its elements have the form ${\operatorname{diag}}(t_1, \ldots, t_n,t_n^{-1}, \ldots, t_1^{-1})$, respectively ${\operatorname{diag}}(t_1, \ldots, t_n,1,t_n^{-1}, \ldots, t_1^{-1})$, and $F$ acts by raising the diagonal entries to their $q$-th power. The Weyl group $W$ acts on ${\mathbf{T}}$ by its natural permutation action on the diagonal entries. More precisely, $W$ is isomorphic to the wreath product $C_2\wr{\mathfrak{S}}_n$, where the cyclic groups of order $2$ interchange the entries $\{t_i, t_i^{-1}\}$, $i = 1, \ldots, n$, while the symmetric group permutes the $n$ pairs $\{t_i, t_i^{-1}\}$. See [@DM Chap. 15] for more details.

The ${\mathbf{G}}^F$-conjugacy classes of $F$-stable maximal tori of ${\mathbf{G}}$ are parameterised by the conjugacy classes of $W$. An element $t\in {\mathbf{T}}$ is conjugate to an element $t' \in {\mathbf{G}}^F$ if ${}^wF(t)=t$ for some $w \in W$. Then $t'$ lies in an $F$-stable maximal torus parameterised by the class of $w$. Such an element $t'$ is regular semisimple if $w$ is unique.

The conjugacy classes of $W$ are parameterised by pairs of partitions $(\lambda,\mu) \vdash n$ of $n$ as follows: If $w \in W$ permutes entries of a regular diagonal element as above, then a cycle containing entries $t_i$ and $t_i^{-1}$ for some $i$ is of even length $2\mu_j$ and contributes a part $\mu_j$ to $\mu$. Otherwise a cycle of length $\lambda_j$ permutes some diagonal entries and there is another cycle of the same length permuting the inverse diagonal entries in the same way; this contributes a part $\lambda_j$ to $\lambda$.

We can embed an even dimensional orthogonal group ${\mathbf{G}}= {\operatorname{SO}}_{2n}(K)$ (type $D_n$) into $\tilde{\mathbf{G}}= {\operatorname{SO}}_{2n+1}(K)$ such that it is stable under the Steinberg morphism of $\tilde{\mathbf{G}}$ and its fixed points are ${\mathbf{G}}^F =
{\operatorname{SO}}^+_{2n}(q)$. There is a second Steinberg morphism $F'$ on ${\mathbf{G}}$ leading to the twisted groups ${\mathbf{G}}^{F'} = {\operatorname{SO}}^-_{2n}(q)$. The Weyl group $W$ of ${\mathbf{G}}$ is a subgroup of index $2$ in the Weyl group $\tilde{W}$ of $\tilde{\mathbf{G}}$, consisting of the conjugacy classes of $\tilde W$ whose parameter $(\lambda,\mu)$ has an even number of parts in $\mu$. If $\mu$ is empty in $(\lambda,\mu)$ and $\lambda$ has only even parts then the corresponding class in $\tilde W$ splits into two classes in $W$, called *degenerate* classes. The twisted Steinberg morphism $F'$ acts on $W$ like conjugation by the short root generator of $\tilde W$. This way the $F'$-conjugacy classes of $W$ can be parameterised by the conjugacy classes of $\tilde W$ whose parameter $(\lambda, \mu)$ has an odd number of parts in $\mu$. Since ${\mathbf{G}}$ and $\tilde{\mathbf{G}}$ have the same rank, maximal tori of ${\mathbf{G}}$ are also maximal tori of $\tilde{\mathbf{G}}$.

Let $(\la,\mu) = ((\la_1, \ldots, \la_r),(\mu_1,\ldots,\mu_s)) \vdash n$. Then the order of the corresponding maximal torus ${\mathbf{T}}^F$ in ${\mathbf{G}}^F$ is $$|{\mathbf{T}}^F| = \prod_{i=1}^{r}(q^{\la_i}-1) \prod_{i=1}^{s}(q^{\mu_i}+1)$$ and ${\mathbf{T}}^F$ contains cyclic subgroups of orders $q^{\la_i}-1$ and $q^{\mu_i}+1$ for all $i$.
