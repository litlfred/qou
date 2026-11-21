---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.966
doc_brief: "On the Gram determinants of the Specht modules — For every partition λ of a positive integer n, let Sλ be the corresponding Specht module of the symmetric group Sn, and let det(λ) ∈Z denote the Gram"
---
Let $n$ be a positive integer and let $\mathfrak{S}_n$ be the symmetric group of $n$ letters. There is a canonical bilinear form on the Specht module $S^{\lambda}$ for a partition $\lambda$ of $n$, arising from the embedding of the Specht module in a permutation representation. In [@JamesMurphyFormula], James and Murphy introduced the determinant $\det(\lambda) \in \mathbb{Z}$ of the Gram matrix of the canonical bilinear form of $S^{\lambda}$ with respect to the standard basis. For any prime $p$, we define the integer $a_{\lambda}^{(p)}$ such that $$\det(\lambda)=m \cdot p^{a_{\lambda}^{(p)}},$$ where $m$ is coprime to $p$. We further denote $f_{\lambda}:=\dim(S^{\lambda})$ and say that $\lambda$ is *even* (resp. *odd*) if and only if $f_{\lambda}$ is.

A major challenge in representation theory is the determination of the dimensions of the irreducible representations $D^{\lambda}$ of $\mathfrak{S}_n$ in positive characteristic $p$ for $\lambda$ a $p$-regular partition of $n$. Some results are known, for instance by [@james1981representation Theorem 7.3.18] it holds that $$\dim(D^{\lambda}) \geq f_{\lambda}- a_{\lambda}^{(p)}.$$ Now, there is an easy formula for $f_{\lambda}$ given by the hook lengths of the Young diagram $[\lambda]$, leaving open if there is something to be said about $a_{\lambda}^{(p)}$.

In this paper, we will show that for $p=2$, the following statement holds:

::: theorem
[]{#Main-Thm-Symmetric label="Main-Thm-Symmetric"} Let $\lambda$ be an even partition of $n$. Then $a_{\lambda}^{(2)}$ is even.
:::

This confirms a special case of a conjecture of Richard Parker (see [@NebeOrthDisc Conjecture 1.3]) about the Gram determinants (called the *orthogonal determinants* in loc. cit.) of the $\rho(G)$-invariant, non-degenerate, symmetric bilinear forms of the representations $\rho$ affording the *orthogonally stable* characters of $G$, for $G$ an arbitrary finite group.

Note that Theorem [\[Main-Thm-Symmetric\]](#Main-Thm-Symmetric){reference-type="ref" reference="Main-Thm-Symmetric"} fails to hold for some odd partitions; indeed, already $\det((1,1))=2$. This implies that understanding the parity of a partition will be of importance to us.

We now explain our strategy for the proof of Theorem [\[Main-Thm-Symmetric\]](#Main-Thm-Symmetric){reference-type="ref" reference="Main-Thm-Symmetric"}. Let $r$ be the integer such that $2^r \leq n < 2^{r+1}$. In [@HookRemovalNavarro Theorem A] it was shown that for an odd partition $\mu$ of $n$, there is a unique odd partition $D(\mu)$ of $n-2^r$ such that the character $\chi_{D(\mu)}$ of $\mathfrak{S}_{n-2^r}$ is a constituent of odd multiplicity of $\mathrm{Res}^{\mathfrak{S}_n}_{\mathfrak{S}_{n-2^r}}(\chi_{\mu})$. The partition $D(\mu)$ can explicitly be constructed by removing the unique $2^r$-hook from the Young diagram of $\lambda$, see also [@OddLattice]. We extend the definition of $D$ to the set of all partitions, where $D$ in particular preserves the parity. We define the *oddness rank* to be the minimal number of iterations of $D$ until the result becomes stationary, with a partition having maximal oddness rank if and only if it is odd.

The formula given in [@JamesMurphyFormula] for $\det(\lambda)$ uses certain partitions that arise by removing the rim of some cell $(i,j)$ from the Young diagram of $\lambda$ and then wrapping it around some row $k$ with $k<i$. In [@Branches], these partitions were called the *branches* of $\lambda$. We will investigate the *odd branches* $\mathscr{P}_{\lambda}^{\mathrm{odd}}$, for which we introduce an equivalence relation on $\mathscr{P}_{\lambda}^{\mathrm{odd}}$ by saying that $\mu_1 \sim \mu_2$ if and only if $D(\mu_1)=D(\mu_2)$. The desired statement then follows by an induction on the oddness rank of $\lambda$ and the understanding of the arising equivalence classes of $\mathscr{P}_{\lambda}^{\mathrm{odd}}$.

This paper is a slightly modified version of results that have appeared in the author's PhD thesis [@HoyerThesis]. In this thesis, we investigated the orthogonal determinants of the finite groups of Lie type, the finite Coxeter groups and the alternating groups. As it turns out, Theorem [\[Main-Thm-Symmetric\]](#Main-Thm-Symmetric){reference-type="ref" reference="Main-Thm-Symmetric"} has far-reaching consequences for the orthogonal determinants of other classes of groups: Since the characters of the alternating groups and the characters of the Coxeter groups of types $B_n$ and $D_n$ are built from the characters of $\mathfrak{S}_n$, the theorem allows us to extend the result to these groups. With some computer help for the exceptional groups, all finite Coxeter groups can be covered. Moreover, Theorem [\[Main-Thm-Symmetric\]](#Main-Thm-Symmetric){reference-type="ref" reference="Main-Thm-Symmetric"} is essential in proving [@NebeOrthDisc Conjecture 1.3] for the general linear groups $\mathrm{GL}_n(q)$ for an odd prime power $q$; this relies on first reducing to the unipotent characters and then using the formulas of the Gram determinants of the Specht modules of Iwahori--Hecke algebras of type $A_n$ found in [@DeterminantsIwahoriHecke], which will be discussed elsewhere.
