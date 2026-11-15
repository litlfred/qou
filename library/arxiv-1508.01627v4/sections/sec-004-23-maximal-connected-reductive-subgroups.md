---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-004-23-maximal-connected-reductive-subgroups
section_title: "Maximal connected reductive subgroups"
section_number: 2.3
pages: 5-5
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:maxred label="subsec:maxred"} The following lemma will allow us to decide if a collection of classes of maximal tori of a classical group has representatives inside the centraliser of a semisimple element:

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
