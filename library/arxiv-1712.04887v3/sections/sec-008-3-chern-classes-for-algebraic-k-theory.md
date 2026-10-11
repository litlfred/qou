---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-008-3-chern-classes-for-algebraic-k-theory
section_title: "Chern Classes for algebraic K-theory"
section_number: 3
pages: 17-20
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.784
---
[]{#sec.chern label="sec.chern"}

In this section, we will define the Chern class map [\[eq.cmap\]](#eq.cmap){reference-type="eqref" reference="eq.cmap"}.

## Definitions {#sub.definitions.chern}

In the following discussion, certain isomorphisms will depend on a choice of some primitive $n$th root of unity $\zeta$. In order to make this clear, we shall write (in this section only) either $=_{\zeta}$ or $=$ to denote isomorphisms which respectively do or do not depend on such a choice. Let $F$ be a number field, and let $\mathcal{O}:=\mathcal{O}_F$ denote the ring of integers of $F$. The Tate twist $\mathbf Z_p(1)$ is defined to be the projective limit $\projlim \mu_{p^n}$ of the $p^n$th roots of unity over all $n$, and $\mathbf Z_p(m):= \mathbf Z_p(1)^{\otimes m}$. The Galois group $G_F$ acts on $\mathbf Z_p(m)$ via the $m$th power $\chi^m$ of the cyclotomic character. For all $m\ge1$, there exists a Chern class map: $$c: K_{2m-1}(F) \rightarrow H^1(F,\mathbf Z_p(m))\,.$$ These Chern class maps arise as the boundary map of a spectral sequence, specifically, the Atiyah--Hirzebruch spectral sequence for étale $K$-theory. These maps were originally constructed by Soulé [@Soule2 Section II]. We may compose this map with reduction mod $p^i$ to obtain a map: $$c: K_{2m-1}(F) \rightarrow H^1(F,\mathbf Z/p^i\mathbf Z(m)).$$ By the Chinese remainder theorem, we may also piece these maps together to obtain a map: $$c: K_{2m-1}(F) \rightarrow H^1(F,\mathbf Z/n\mathbf Z(m) )$$ for any integer $n$.

Let $\zeta$ be a primitive $n$th root of unity, $F_n=F(\zeta)$ and write $G$ for the (possibly trivial) Galois group $\mathrm{Gal}(F_n/F)$. Let $\mu$ denote the module of $n$ roots of unity. There is a canonical injection $$\chi: G \rightarrow  \mathrm{Aut}({\mu}) = (\mathbf Z/n\mathbf Z)^{\times} \,.$$ By inflation--restriction, there is a canonical map: $$\label{winj}
H^1(F,\mathbf Z/n\mathbf Z(m) ) \rightarrow H^1(F_n,\mathbf Z/n\mathbf Z(m) )^{G}$$ For $m \ge 1$, there is an invariant $w_m(F)\in\mathbf N$ that we will need. It is defined in terms of Galois cohomology by $$w_m(F) \;=\; \prod_{p} \bigl|H^0(F,\mathbf Q_p/\mathbf Z_p(m) )\bigr|\,,$$ Note that $w_1(F)$ is equal to $w_F$, the number of roots of unity in $F$, and $w_2(F)$ agrees with [\[eq.w2F\]](#eq.w2F){reference-type="eqref" reference="eq.w2F"} because the action of $G_F$ on $\mathbf Z/n\mathbf Z(2) \subset \mathbf Q_p/\mathbf Z_p(2)$ for any $n$ precisely factors through $\mathrm{Gal}(F(\zeta+ \zeta^{-1})/F)$ for a primitive $n$th root of unity $\zeta$. We also define $$\label{wtwiddle}
\widetilde w_F\;=\; \prod_{p} \bigl|H^0(\widetilde{F}(\zeta_p + \zeta^{-1}_p),\mathbf Q_p/\mathbf Z_p(1))\bigr|\,.$$ where $\widetilde{F}$ is the Galois closure of $F$ over $\mathbf Q$. Thus $\widetilde w_F$ is divisible only by the finitely many primes $p$ such $\zeta_p$ belongs to $\widetilde{F}(\zeta_p + \zeta^{-1}_p)$. If $p|\widetilde w_F$ and $p > 2$, then $p$ necessarily ramifies in $F$. Note that $\widetilde w_F$ is always divisible by $w_F$.

::: lemma
[]{#lemma:sahinj label="lemma:sahinj"} The map [\[winj\]](#winj){reference-type="eqref" reference="winj"} is injective for integers $n$ prime to $w_m(F)$.
:::

::: proof
*Proof.* The kernel of this map is $H^1(F_n/F,\mathbf Z/n\mathbf Z(m) )$. Assume that this is non-zero. By Sah's lemma, this group is annihilated by $\chi^m(g) - 1$ for any $g \in G$. Equivalently, the kernel has order divisible by $p | n$ if and only if the elements $a^m - 1$ are divisible by $p$ for all $(a,p) = 1$. Yet this is equivalent to saying that $H^0(F,\mathbf Z/p\mathbf Z(m) ) \subset H^0(F,\mathbf Q_p/\mathbf Z_p(m))$ is non-zero, and hence $p | w_m(F)$. ◻
:::

There is an isomorphism $\mathbf Z/n\mathbf Z(1) = \mu$. A choice of primitive $n$th root of unity $\zeta$ gives a trivialization $t_{\zeta}:  
\mathbf Z/n\mathbf Z(1)   =_{\zeta} \mathbf Z/n\mathbf Z(m)$ defined by sending $\zeta$ to $\zeta^{\otimes n}$. This isomorphism is not, in general, $G$-equivariant, but rather satisfies $$t_{\zeta}(\sigma x) =  \chi^{1-m}(\sigma) \sigma t_{\zeta}(x)$$ The dependence of $t_{\zeta}$ on $\zeta$ is given by $t_{\zeta^k} = k^{m-1} t_{\zeta}$.

By Hilbert $90$, for a number field $L$, there is a canonical isomorphism $H^1(L,\mu) = L^{\times}/L^{\times n}$, and hence (given $\zeta$) an isomorphism $$H^1(F_n,\mathbf Z/n\mathbf Z(m) )^{G}
 =_{\zeta}  H^1(F_n,\mathbf Z/n\mathbf Z(1))^{\chi^{1-m}}
 = \left(F_n^{\times}/F_n^{\times n}\right)^{\chi^{1-m}} \,,$$ where the first isomorphism is induced by $t_{\zeta}$. Thus $c$ and $\zeta$ give rise to a map: $$\label{defc}
c_\zeta: K_{2m-1}(F) \rightarrow 
\left(F_n^{\times}/F_n^{\times n}\right)^{\chi^{1-m}}\,.$$

## The relation between étale cohomology and Galois cohomology {#section:relations}

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
