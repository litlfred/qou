---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-011-32-the-relation-between-étale-cohomology-and-gal
section_title: "The relation between étale cohomology and Galois cohomology"
section_number: 3.2
pages: 18-20
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.933
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#section:relations label="section:relations"}

There are isomorphisms that can be found in Sections 5.2 and 5.4 of [@Weibel] $$\label{useful}
K_{2m-1}(F) \otimes \mathbf Z_p \simeq K_{2m-1}(\mathcal{O}_F[1/p]) \simeq 
K_{2m-1}(\mathcal{O}_F) \otimes \mathbf Z_p$$ for $m > 1$. These isomorphisms are also reflected in the following isomorphism between étale cohomology groups and Galois cohomology groups: $$H^1_{\text{\'{e}t}}(\mathcal{O}_F[1/p],\mathbf Z_p(m) ) \simeq H^1(F,\mathbf Z_p(m) )$$ for $m \ge 2$. In particular, we may also view the Chern class maps considered above as morphisms $$c: K_{2m-1}(F) \otimes \mathbf Z_p \simeq
K_{2m-1}(\mathcal{O}_F) \otimes \mathbf Z_p \rightarrow H^1_{\text{\'{e}t}}(\mathcal{O}_F[1/p],\mathbf Z_p(m) ).$$

::: theorem
[]{#theorem:surjective2 label="theorem:surjective2"} For $p > 2$, there is an isomorphism $$c: K_3(F)  \otimes \mathbf Z_p  \simeq K_3(\mathcal{O}_F) \otimes \mathbf Z_p
\rightarrow H^1_{\text{\emph{\'{e}t}}}(\mathcal{O}_F[1/p],\mathbf Z_p(2)).$$ The rank of $K_3(F)$ is $r_2$.
:::

::: proof
*Sketch.* This follows from the Quillen--Lichtenbaum conjecture, as proven by Voevodsky and Rost (see [@Weibel], [@Voe]). In this case, it can also be deduced from the description of torsion in $K_3(F)$ by Merkurjev and Suslin [@Suslin] (described in terms of $w_2(F)$ above) combined with Borel's theorem for the rank (see also Theorem 6.5 of [@TateK]), and the result of Soulé that the Chern class map is surjective. ◻
:::

::: lemma
[]{#lemma:sahinj2 label="lemma:sahinj2"} Suppose that $p \nmid w_2(F)$ for every prime $p$ with $p^2|n$. Then the map $$\label{eq.cnv1}
c_\zeta: K_3(F) \rightarrow K_3(F)/nK_3(F) \rightarrow
\left(F_n^{\times}/F_n^{\times n}\right)^{\chi^{-1}}$$ is injective on $K_3(F)/nK_3(F)$.
:::

::: proof
*Proof.* By the Chinese Remainder Theorem, it suffices to consider the case $n= p^{m}$. In light of Theorem [\[theorem:surjective2\]](#theorem:surjective2){reference-type="ref" reference="theorem:surjective2"}, it suffices to show that the map $$H^1(F,\mathbf Z_p(2))/{n} \rightarrow H^1(F,\mathbf Z/{n}\mathbf Z(2)) 
\rightarrow F_{{n}}^{\times}/F_{{n}}^{\times {{n}}}$$ is injective. The kernel of the first map is $H^0(F,\mathbf Z_p(2))/{{n}} = 0$. The kernel of the second map is, via inflation--restriction, the group $H^1(\mathrm{Gal}(F_n/F),H^0(F,\mathbf Z/{n}\mathbf Z(2)))$. If $n= p$, then $\mathrm{Gal}(F_n/F)$ has order prime to $p$ and the cohomology group vanishes. If $p^2 | n$, this group is certainly zero unless $$H^0(F,\mathbf Z/{n}\mathbf Z(2)) \subset H^0(F,\mathbf Q_p/\mathbf Z_p(2))$$ is non-zero, or in other words, unless $p$ divides $w_2(F)$. ◻
:::

## Upgrading from $F_n^{\times}$ to $\mathcal{O}_{F_n}[1/S]^{\times}$

The following is a consequence of the finite generation of $K_3(F)$:

::: lemma
[]{#lemma:avoidS label="lemma:avoidS"} For any field $F$, there exists a finite set $S$ of primes which avoids any given finite set of primes not dividing $n$ such that the image of $c_\zeta$ on $K_3(F)/nK_3(F)$ may be realized by an element of $\mathcal{O}^{\times}_{F(\zeta)}[1/S]$.
:::

::: proof
*Proof.* Note that without the requirement that $S$ avoids any given finite set of primes not dividing $n$, the result is a trivial consequence of the fact that $K_3(F)$ is finitely generated. The construction of $c$ as a map to units in $F_n^{\times}$ proceeded via Hilbert $90$. In light of Theorem [\[theorem:surjective2\]](#theorem:surjective2){reference-type="ref" reference="theorem:surjective2"} above, it suffices to do the same with $H^1(F_n,\mu)$ replaced by $H^1_{\text{\'{e}t}}(\mathcal{O}_{F_n}[1/S],\mu)$ for some set $S$ containing $p| n$. However, in this case, the class group intervenes, as there is an exact sequence ([@Milne], p.125): $$\mathcal{O}_{F_n}[1/S]^{\times}/\mathcal{O}_{F_n}[1/S]^{\times n}
\rightarrow H^1_{\text{\'{e}t}}(\mathcal{O}_{F_n}[1/S],\mu)
\rightarrow \mathrm{Pic}(\mathcal{O}_{F_n}[1/S])[n]$$ where $M[n]$ denotes the $n$-torsion of $M$ and $\mathrm{Pic}$ is the Picard group, which may be identified with the class group of $\mathcal{O}_{F_n}[1/S]$. On the other hand, it is well known that one can represent generators in the class group by a set of primes avoiding any given finite set of primes, and hence for a set $S$ including primes for each generator of the class group, the last term vanishes. ◻
:::
