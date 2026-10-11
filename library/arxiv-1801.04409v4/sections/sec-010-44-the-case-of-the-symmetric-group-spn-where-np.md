---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-010-44-the-case-of-the-symmetric-group-spn-where-np
section_title: "The case of the symmetric group Sp+n, where n<p"
section_number: 4.4
pages: 18-21
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.93
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

## Application: the semisimplification of the Deligne category $\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n$

Let $n$ be a nonnegative integer, and $\mathbf{k}$ be a field of characteristic zero. Let $\underline{\mathop{\mathrm{Rep}}\nolimits} S_n$ denote the Karoubian Deligne category over $\mathbf{k}$ defined in [@D3] (its main property is that it can be interpolated to non-integer values of $n$ in $\mathbf{k}$). This category has a tensor ideal $I$ such that $\underline{\mathop{\mathrm{Rep}}\nolimits} S_n/I=\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n$. Moreover, it is known (see [@D3],[@CO]) that $\underline{\mathop{\mathrm{Rep}}\nolimits} S_n$ has an abelian envelope $\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n$; in particular, the trace of any nilpotent endomorphism in $\underline{\mathop{\mathrm{Rep}}\nolimits} S_n$ vanishes. Since $I$ consists of morphisms factoring through negligible objects (i.e., direct sums of indecomposable objects of dimension zero), and $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n$ is semisimple, we see that $I=\mathcal{N}(\mathcal{C})$ is the full ideal of negligible morphisms (i.e., every negligible morphism factors through a negligible object), and the semisimplification $\overline{\underline{\mathop{\mathrm{Rep}}\nolimits} S_n}$ coincides with $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n$.

The question of describing the semisimplification of the abelian envelope $\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n$ is more interesting. The answer is given by the following theorem.

::: theorem
[]{#semdel label="semdel"} (i) The restriction functor $${\rm Res}: \underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n\to \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n\boxtimes \underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_0$$ induces an equivalence between the semisimplifications of these categories.

\(ii\) We have an equivalence of symmetric tensor categories $\overline{\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n}\cong \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n\boxtimes \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(GL(1)\times SL(2),(-1,-1))$.
:::

::: proof
*Proof.* We will use the approach of [@Ha] to Deligne categories. Namely, let us take $\mathbf{k}=\Bbb C$. Then, according to [@Ha], Theorem 1.1(b), we have $$\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n=\lim_{p\to \infty} \mathop{\mathrm{Rep}}\nolimits_{\overline{\Bbb F}_p}S_{n+p},$$ where $\lim$ denotes an appropriate ultrafilter limit (i.e., ultraproduct). More precisely, this means that $\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n$ is the tensor subcategory in the appropriate ultrafilter limit tensor generated by the \"permutation\" object $P$ (the analog of the permutation representation). It is easy to see that the ultrafilter limit commutes with the semisimplification, so (i) follows from Proposition [\[eqi\]](#eqi){reference-type="ref" reference="eqi"}.

By virtue of (i), it suffices to check (ii) for $n=0$. In this case, according to Subsection [\[symgroup\]](#symgroup){reference-type="ref" reference="symgroup"}, $\overline{\mathop{\mathrm{Rep}}\nolimits_{\overline{\Bbb F}_p}S_{n+p}}=\overline{\mathop{\mathrm{Rep}}\nolimits_{\overline{\Bbb F}_p}S_{p}}$ is generated by $\overline{V_{p-2}}$ and $\overline{V_{p-1}}$. In the ultrafilter limit, the sequences of representations $V_{p-2}$ and $V_{p-1}$ converge to the objects $V_{-2}$ and $V_{-1}$ of $\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_0$ (of dimensions $-2$ and $-1$, respectively), defined by the (non-split) exact sequences $$0\to \bold 1\to P\to V_{-1}\to 0,\ 0\to V_{-2}\to V_{-1}\to \bold 1\to 0$$ (in particular, $V_{-2}$ is simple). Thus, by Proposition [\[generat\]](#generat){reference-type="ref" reference="generat"}, the category $\overline{\underline{\mathop{\mathrm{Rep}}\nolimits}^{\rm ab} S_n}$ is generated by $\overline{V_{-2}}$ and $\overline{V_{-1}}$. Moreover, since $$\overline{V_{p-2}}=L_{p-2}\otimes \chi^{p-1},$$ we find that $\overline{V_{-2}}$ generates a subcategory with Grothendieck ring of $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}SL(2)$. Since $\dim V_{-2}=-2$, this is the category $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(SL(2),-1)$. Similarly, since $\overline{V_{p-1}}$ is invertible of order $2(p-1)$, we see that $\overline{V_{-1}}$ is invertible of infinite order, so since its dimension is $-1$, it generates $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(GL(1),-1)$. Thus, together these two objects generate the category $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}S_n\boxtimes \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(GL(1)\times SL(2),(-1,-1))$, as claimed. ◻
:::
