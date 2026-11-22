---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-013-35-proof-of-theorem-15
section_title: "Proof of Theorem 1.5"
section_number: 3.5
pages: 20-21
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.881
latex_coverage_ratio: 0.906
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.thm.c label="sub.thm.c"}

We have all the ingredients to give a proof of Theorem [\[thm.c\]](#thm.c){reference-type="ref" reference="thm.c"}. Fix an odd natural number $n$ and a primitive $n$th root of unity $\zeta$. Consider the Chern class map $$c_\zeta: K_3(F)/nK_3(F) \to 
\left(F_n^{\times}/F_n^{\times n}\right)^{\chi^{-1}} \,.$$ from [\[eq.cnv1\]](#eq.cnv1){reference-type="eqref" reference="eq.cnv1"}. When $n$ is either square-free or if any prime $p^2 | n$ is coprime to $w_2(F)$, the above map is injective by Lemma [\[lemma:sahinj2\]](#lemma:sahinj2){reference-type="ref" reference="lemma:sahinj2"}. When $n$ is furthermore coprime to the discriminant $\Delta_F$ of $F$ and the order of $K_2(\mathcal O_F)$, Lemma [\[lemma:avoidS2\]](#lemma:avoidS2){reference-type="ref" reference="lemma:avoidS2"} implies that the above map factors through a map $$c_\zeta: K_3(F)/nK_3(F) \to 
\left(\mathcal O_n^{\times}/\mathcal O_n^{\times n}\right)^{\chi^{-1}},$$ where $\mathcal O_n$ is the ring of integers of $F_n$. If $p^2 | n$ and $p | w_2(F)$ is odd, then either $p | \Delta_F$ or $p = 3$, hence the assumptions $(n, w_2(F) \Delta_F |K_2(\mathcal{O}_F)|) = 1$ and $n$ odd are equivalent to $(n,6 \Delta_F |K_2(\mathcal{O}_F)|) = 1$, and if $n$ is furthermore not divisible by $9$, they are equivalent to $(n, 2 \Delta_F |K_2(\mathcal{O}_F)|) = 1$, justifying the claims made concerning $M_F$ in Remark [\[quotableremark\]](#quotableremark){reference-type="ref" reference="quotableremark"}. When $n$ is prime (or more generally square-free),

then [\[K3F\]](#K3F){reference-type="eqref" reference="K3F"} and Proposition [\[prop.calOm\]](#prop.calOm){reference-type="ref" reference="prop.calOm"}[\[partb.calOm\]](#partb.calOm){reference-type="ref" reference="partb.calOm"} imply that both sides of the above equation are abelian groups isomorphic to $(\mathbf Z/n\mathbf Z)^{r_2(F)}$. It follows that when $n$ is square-free and coprime to $2 \Delta_F |K_2(\mathcal O_F)|$, then the above map is an injection of finite abelian groups of the same order, and hence an isomorphism. This concludes the proof of Theorem [\[thm.c\]](#thm.c){reference-type="ref" reference="thm.c"}. 0◻
