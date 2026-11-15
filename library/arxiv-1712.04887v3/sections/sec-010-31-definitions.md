---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-010-31-definitions
section_title: "Definitions"
section_number: 3.1
pages: 17-18
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.956
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.definitions.chern label="sub.definitions.chern"}

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
