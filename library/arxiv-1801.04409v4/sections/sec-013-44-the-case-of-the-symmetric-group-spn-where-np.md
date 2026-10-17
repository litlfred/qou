---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-013-44-the-case-of-the-symmetric-group-spn-where-np
section_title: "The case of the symmetric group Sp+n, where n<p"
section_number: 4.4
pages: 18-20
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.983
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
[]{#symgroup label="symgroup"}

If $p=2$ then we have $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_2}=\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_3}=\mathrm{Vec}_\mathbf{k}$. So consider the case $p>2$. Let $G=S_{p+n}$, where $0\le n<p$. Then $P=\Bbb Z/p$, and $N_G(P)=S_n\times \Bbb Z/(p-1)\ltimes \Bbb Z/p$. Thus, by Corollary [\[corro\]](#corro){reference-type="ref" reference="corro"}, $$\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_{p+n}}\cong \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n\boxtimes {\rm Ver}_p^+\boxtimes \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(\Bbb Z/2(p-1),z),$$ where $z$ is the element of order $2$ in $\Bbb Z/2(p-1)$. In particular, for $n\ge 2$ the group of invertible objects of this category is $\Bbb Z/2\times \Bbb Z/2(p-1)$.

In particular, we obtain the following proposition.

::: proposition
[]{#eqi label="eqi"} If $n<p$ then the restriction functor $${\rm Res}: \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_{n+p}\to \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(S_n\times S_p)$$ induces an equivalence $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_{n+p}}\to \overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(S_n\times S_p)}$.
:::

::: proof
*Proof.* The functor ${\rm Res}$ descends to a tensor functor $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_{n+p}}\to \overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(S_n\times S_p)}$ by Corollary [\[desc\]](#desc){reference-type="ref" reference="desc"}, and this tensor functor is an equivalence since the inclusion $S_n\times S_p\hookrightarrow S_{n+p}$ induces an isomorphism of the normalizers of the Sylow $p$-subgroups. ◻
:::

Let us now describe the functor $\bold S$ more explicitly, in the special case $n=0$, i.e., $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_p$, where $p>2$. It is well known that in this case we have a unique non-semisimple block $\mathcal B$ of defect $1$, namely, the block of the trivial representation. The blocks of defect zero consist of objects of dimension $0$, so they are killed by $\bold S$. So let us first consider the images under $\bold S$ of the simple objects of $\mathcal B$. These objects have the form $\wedge^iV_{p-2}$, $i=0,...,p-2$, where $V_{p-2}$ is the $p-2$-dimensional irreducible representation of $S_p$ which is the middle composition factor in the permutation representation. To compute the image $\bold S(V_{p-2})$ of $V_{p-2}$, denote by $L_i$ $i=1,3,5,...,p-2$ the simple objects of ${\rm Ver}_p^+$ (so that $L_1=\bold 1$), and by $\chi$ the generator of $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(\Bbb Z/2(p-1))$. The object $\bold S(V_{p-2})$ has to be simple and has dimension $-2$, so it has the form $L_{p-2}\otimes \chi^m$, where $m$ is even as $\dim \chi=-1$. Moreover, $S^2V_{p-2}$ contains $\bold 1$ as a direct summand, which implies that $m=0$ or $m=p-1$. Finally, $\wedge^{p-2}V_{p-2}={\rm sign}$ is the sign representation of $S_p$, so $\wedge^{p-2}(L_{p-2}\otimes \chi^m)=\chi^{m(p-2)}$ is nontrivial, which implies that $m=p-1$. Thus, $$\bold S(V_{p-2})=L_{p-2}\otimes \chi^{p-1}.$$ This means that $$\bold S(\wedge^i V_{p-2})=L_{p-1-i}\otimes \chi^{p-1}$$ for odd $i\le p-2$, and $$\bold S(\wedge^i V_{p-2})=L_{i+1}$$ for even $i\le p-2$.

Now consider the representation $V_{p-1}$ of $S_p$ on the space of functions on $[1,p]$ modulo constants. Then $\bold S(V_{p-1})$ has dimension $-1$, so it is of the form $\chi^m$ for some odd $m$. Moreover, it is well known that $\wedge^iV_{p-1}$ is indecomposable for $i\le p-1$. Since it is not invertible for $0<i<p-1$, we see that $\chi^{mi}\ne \bold 1,\chi^{p-1}$ for any $0<i<p-1$. Also $\chi^{m(p-1)}=\chi^{p-1}$. This implies that the order of $\chi^m$ is $2(p-1)$, so we may assume that $m=1$ by making a suitable choice of $\chi$. Thus, for a suitable choice of $\chi$ we have $$\bold S( V_{p-1})=\chi.$$ The suitable choice of $\chi$ is well defined only up to the change $\chi\to \chi^p$, since the group $\Bbb Z/2(p-1)$ has an automorphism of order $2$ (sending $1$ to $p$) which acts trivially on $\Bbb Z/(p-1)=\mathop{\mathrm{Aut}}\nolimits(\Bbb Z/p)$. Thus, the well-defined question is to determine $\chi^2$, which is a character of $\mathop{\mathrm{Aut}}\nolimits(\Bbb Z/p)$, naturally identified with $\Bbb F_p^\times$. Then it is easy to show by a direct calculation that $\chi^2$ is the natural inclusion $\Bbb F_p^\times\hookrightarrow \mathbf{k}^\times$ coming from the inclusion of fields $\Bbb F_p\hookrightarrow \mathbf{k}$.

Thus, we obtain

::: proposition
[]{#generat label="generat"} The category $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_p}$ is generated by $\overline{V_{p-2}}$ and $\overline{V_{p-1}}$. In other words, the simple objects of $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_p}$ have the form $\overline{V_{p-1}}^{\otimes m}\otimes \wedge^i \overline V_{p-2}$, where $0\le m\le p-2$ and $0\le i\le p-2$ (so the total number of simple objects is $(p-1)^2$).
:::
