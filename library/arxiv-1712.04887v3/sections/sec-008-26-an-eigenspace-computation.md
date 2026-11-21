---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-008-26-an-eigenspace-computation
section_title: "An eigenspace computation"
section_number: 2.6
pages: 16-17
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.912
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.eigenspace label="sub.eigenspace"}

As in Section [\[sub.intro.bloch\]](#sub.intro.bloch){reference-type="ref" reference="sub.intro.bloch"}, we write $G=\mathrm{Gal}(F_n/F)$, identified with a subgroup of $(\mathbf Z/n\mathbf Z)^\times$ via the map $\chi$ of Equation [\[eq.chi\]](#eq.chi){reference-type="eqref" reference="eq.chi"}. Since $F_n^\times/F_n^{\times n}$ is an $n$-torsion $G$-module, the $\chi^{-1}$ eigenspace makes sense and is given by $$\left(F_n^\times/F_n^{\times n}\right)^{\chi^{-1}}=
\{ x \in F_n^\times/F_n^{\times n} \, | \sigma x = x^{\chi(\sigma^{-1})} \,,
\text{for all} \, \sigma \in G \}\,,$$ where $x^{\chi(\sigma^{-1})}$ is computed using any lift of $\chi(\sigma^{-1}) \in (\mathbf Z/n\mathbf Z)^\times$ to $\mathbf Z$.

In characteristic zero, one can also consider the action of $G$ on $M \otimes_\mathbf ZR$, where $R$ is a $\mathbf Z[G]$ module that contains the eigenvalues of $\sigma \in G$. For example, one can take $M=\mathcal O_n^\times$ and $R=\mathbf C$. If $n=p$ is prime, then one can take $R=\mathbf Z_p$, which contains the $(p-1)$th roots of unity. In particular, if $n=p$, then one can define $\left(M \otimes_\mathbf Z\mathbf Z_p\right)^{\chi^{-1}}$, which will have the property that $$\left(M \otimes_\mathbf Z\mathbf Z_p\right)^{\chi^{-1}} \otimes \mathbf Z/p\mathbf Z= 
\left(M/pM\right)^{\chi^{-1}} \,.$$

::: proposition
[]{#prop.calOm label="prop.calOm"} Suppose that $F$ is disjoint from $\mathbf Q(\zeta_n)$.

1.  []{#parta.calOm label="parta.calOm"} There exists an isomorphism of $G$-modules $$\label{eq.calOm}
    \left(\mathcal O_n^\times \otimes \mathbf C\right)^{\chi^{-1}} =\mathbf C^{r_2(F)} \,.$$

2.  []{#partb.calOm label="partb.calOm"} If $n=p$ is prime, so that $\chi: G \rightarrow (\mathbf Z/p\mathbf Z)^\times$ admits a Teichmüller lift to $\mathbf Z^{\times}_p$, then $$\mathrm{rank}_{\mathbf Z_p} \left(\mathcal O_n^\times \otimes \mathbf Z_p \right)^{\chi^{-1}}
    =r_2(F)\,.$$ If in addition $\chi$ and $\chi^{-1}$ are distinct characters of $G$, then $$\left(\mathcal{O}_p^{\times}/\mathcal{O}_p^{\times p}\right)^{\chi^{-1}} = 
    \left(\mathbf Z/p\mathbf Z\right)^{r_2(F)} \,.$$
:::

::: proof
*Proof.* Part [\[partb.calOm\]](#partb.calOm){reference-type="ref" reference="partb.calOm"} follows easily from part [\[parta.calOm\]](#parta.calOm){reference-type="ref" reference="parta.calOm"} and the above discussion, together with the fact that if $\chi \neq \chi^{-1}$ then the torsion in the unit group (which just comprises roots of unity) is in the $\chi$-eigenspace and not the $\chi^{-1}$-eigenspace.

For [\[parta.calOm\]](#parta.calOm){reference-type="ref" reference="parta.calOm"}, let $\widetilde{F}$ be the Galois closure of $F$ over $\mathbf Q$ and let $\Gamma=\mathrm{Gal}(\widetilde{F}/\mathbf Q)$. By assumption, with $\widetilde{F}_n=\widetilde{F}(\zeta_n)$, we have $\mathrm{Gal}(\widetilde{F}_n/\mathbf Q)=\Gamma\times G=\Gamma\times \left(\mathbf Z/n\mathbf Z\right)^\times$. From the proof of Dirichlet's unit theorem, the unit group of $\widetilde{F}_n$, tensored with $\mathbf C$, decomposes equivariantly as $$\bigoplus_{W} W^{\dim(W|c=1)}\,,$$ where $W$ runs over all the non-trivial irreducible representations of $\Gamma \times G$ and $c \in \Gamma$ is any complex conjugation, which we may take to be $(c,-1) \in G \times \left(\mathbf Z/n\mathbf Z\right)^\times$ for a complex conjugation $c \in \Gamma$. The irreducible representations of $W$ are of the form $U \otimes V$ for irreducible representations $U$ of $\Gamma$ and $V$ of $G=\left(\mathbf Z/n\mathbf Z\right)^\times$. Note that $$\dim(U \otimes V|(c,-1)=1)=\dim(U|c=1)\dim(V|c=1)+
\dim(U|c=-1)\dim(V|c=-1)\,.$$ If we take the $\chi^{-1}$-eigenspace under the action of the second factor, the only representation $V$ of $G$ which occurs is $\chi^{-1}$, on which $-1$ acts by $-1$, and hence we are left with $$\Bigl(\mathcal{O}_{\widetilde{F}_n}^\times \otimes\mathbf C\Bigr)^{\chi^{-1}} \;=\;
\bigoplus_V V^{\dim(V|c=-1)}\,,$$ where the sum runs over all representations $V$ of $\Gamma$. In particular, there is an isomorphism in the Grothendieck group of $G$-modules $$\bigl[\,\bigl(\mathcal{O}_{\widetilde{F}_n}^\times \otimes\mathbf C\bigr)^{\chi^{-1}}\,\bigr] \,+\,
\bigl[ \mathcal{O}_{\widetilde{F}}^\times \otimes\mathbf C\bigr] \,+\, \bigl[ \mathbf C\bigr] 
\;=\; \bigl[\mathbf C[G]\bigr] \,.$$ Now take the $\Delta=\mathrm{Gal}(\widetilde{F}/F)=\mathrm{Gal}(\widetilde{F}_n/F_n)$-invariant part and take dimensions, we obtain the equality $$\dim_\mathbf C\Bigl(\bigl(\mathcal{O}_{F_n}^\times \otimes\mathbf C\bigr)^{\chi^{-1}} \Bigr) 
\,+\, (r_1+r_2-1) \,+\, 1\;=\;r_1+2r_2 \,,$$ where $(r_1,r_2)$ is the signature of $F$. The result follows. ◻
:::
