---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-003-4-canonical-basis-elements-corresponding-to-span
section_title: "Canonical basis elements corresponding to spanning vectors"
section_number: 4
pages: 8-9
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.84
latex_coverage_ratio: 0.988
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
Recall that for $\mathbf{i},\mathbf{i'}\in \chi_n$, the map $T_{\bf i}^{\bf i'}$ is defined by $T_{\bf i}^{\bf i'}({\bf a})=\psi_{\bf i'}\psi_{\bf i}^{-1}({\bf a})$, for ${\bf a}\in Y_{\bf i}$. Define $T_2:\,\mathbb{Z}^2\rightarrow \mathbb{Z}^2$ by $T_2(a,b):=(b,a)$, and $T_3:\,\mathbb{Z}^3\rightarrow \mathbb{Z}^3$ by $T_3(a,b,c):=(\max(c,b-a),a+c,
\min(a,b-c))$. The maps $T_{\bf i}^{\bf i'}$ satisfy the following:

::: prop
[]{#Tdescription label="Tdescription"} (Berenstein and Zelevinsky)\
(a) Suppose ${\bf i,i'}\in \chi_n$ and that $\mathbf{i}=\mathbf{i'}$ except that $(i_s,i_{s+1})=(i,j)$ and $(i'_s,i'_{s+1})=(j,i)$ for some index $s$ and $i,j\in [1,n]$ with $|i-j|>1$. Let $\mathbf{a}\in \mathbb{N}^k$ and write ${\bf a'}=T_{\bf i}^{\bf i'}({\bf a})$. Then we have $a'_r=a_r$ for $r<s$ or $r>s+1$ and $(a'_s,a'_{s+1})=T_2(a_s,a_{s+1})$.\
(b) Suppose ${\bf i,i'}\in \chi_n$, and that $\mathbf{i}=\mathbf{i'}$ except that $(i_s,i_{s+1},i_{s+2})=(i,j,i)$ and $(i'_s,i'_{s+1},i'_{s+2})=(j,i,j)$ for some index $s$ and $i,j\in [1,n]$ with $|i-j|=1$. Let $\mathbf{a}\in \mathbb{N}^k$ and write ${\bf a'}=T_{\bf i}^{\bf i'}({\bf a})$. Then we have $a'_r=a_r$ for $r<s$ or $r>s+2$ and $(a'_s,a'_{s+1},a'_{s+2})=T_3(a_s,a_{s+1},a_{s+2})$.
:::

: See [@bz1 §§2.6, 2.7]. $\square$

We need the following Lemma, which will help us to understand how spanning vectors of Lusztig cones are related.

::: lemma
[]{#shortT label="shortT"} (a) Suppose ${\bf i,i'}\in \chi_n$ and that $\mathbf{i}=\mathbf{i'}$ except that $(i_s,i_{s+1})=(i,j)$ and $(i'_s,i'_{s+1})=(j,i)$ for some index $s$ and $i,j\in [1,n]$ with $|i-j|>1$. Let $\mathbf{a}=a(c,\mathbf{i})$, respectively $a(j,\mathbf{i})$, be a spanning vector of $C_{\mathbf{i}}$, and let $\mathbf{a'}=a(c',\mathbf{i'})$, respectively $\mathbf(j,\mathbf{i'})$, be the corresponding spanning vector of $C_{\mathbf{i'}}$. Here $(c',\mathbf{i'})$ is the chamber that $(c,\mathbf{i})$ becomes when the commutation relation $(i,j)\rightarrow (j,i)$ is applied to $\mathbf{i}$. Then $a'_r=a_r$ for all $r<s$ or $r>s+1$, while $(a'_s,a'_{s+1})=T_2(a_s,a_{s+1})$.\
(b) Suppose ${\bf i,i'}\in \chi_n$ and that $\mathbf{i}=\mathbf{i'}$ except that $(i_s,i_{s+1},i_{s+2})=(i,j,i)$ and $(i'_s,i'_{s+1},i'_{s+2})=
(j,i,j)$ for some index $s$ and $i,j\in [1,n]$ with $|i-j|=1$. Let $\mathbf{a}=a(c,\mathbf{i})$, respectively $a(j,\mathbf{i})$, be a spanning vector of $C_{\mathbf{i}}$. In this case, we suppose further that $(c,\mathbf{i})$ is not the chamber of $CD(\mathbf{i})$ involving the substring $(i,j,i)$, so that there is a chamber $(c',\mathbf{i'})$ with $P(c,\mathbf{i})=P(c',\mathbf{i'})$. Let $\mathbf{a'}=a(c',\mathbf{i'})$, respectively $\mathbf(j,\mathbf{i'})$. Then $a'_r=a_r$ for all $r<s$ or $r>s+1$, while $(a'_s,a'_{s+1},a'_{s+2})=
T_3(a_s,a_{s+1},a_{s+2})$.
:::

: Recall that the spanning vectors of $C_{\bf i}$ are obtained by inverting the defining matrix $P_{\bf i}$ of $C_{\bf i}$. Part (a) follows immediately from the definition of $P_{\bf i}$. Suppose we are in situation (b). Consider the case where ${\bf a}=a(c,{\bf i})$. Since $(c,{\bf i})$ is not the chamber corresponding to $(i,j,i)=(i_s,i_{s+1},i_{s+2})$, we must have that ${\bf a}$ is perpendicular to the row of $P_{\bf i}$ corresponding to this chamber. In the case where ${\bf a}=a(j,{\bf i})$, this is also true. So, in either case, we see that $a_{s+1}=a_s+a_{s+2}$. It follows from the definition of $T_3$ that $T_3(a_s,a_{s+1},a_{s+2})=(a_{s+2},a_{s+1},a_s)$. Since the ordering on the positive roots induced by $\bf i$ agrees with that induced by $\bf i'$ except that the roots in positions $s$ and $s+2$ are exchanged, the fact that $\bf a'$ is as claimed in the statement above follows from Theorem [\[multiset\]](#multiset){reference-type="ref" reference="multiset"} (a) and (b). $\square$

Using Proposition [\[Tdescription\]](#Tdescription){reference-type="ref" reference="Tdescription"} and Lemma [\[shortT\]](#shortT){reference-type="ref" reference="shortT"} we have:

::: cor
Let ${\bf i,i'}\in \chi_n$, and let $(c,{\bf i}),(c',{\bf i'})$ be chambers with $P(c,{\bf i})=P(c',{\bf i'})$. Then $T_{\bf i}^{\bf i'}(a(c,{\bf i}))=
a(c',{\bf i'})$. Also, for $j\in [1,n]$, $T_{\bf i}^{\bf i'}(a(j,{\bf i}))=
a(j,{\bf i'})$.
:::

We therefore have:

::: theorem
[]{#natural label="natural"} Let $\mathbf{i}\in \chi_n$. For $j=1,2,\ldots ,n$ and $P$ a partial quiver associated to $\mathbf{i}$, let $b_j(\mathbf{i})=\psi_{\mathbf{i}}^{-1}(v_j(\mathbf{i}))$ and $b_P(\mathbf{i})=\psi_{\mathbf{i}}^{-1}(v_P(\mathbf{i}))$ be the corresponding canonical basis elements. Then these elements are independent of the reduced expression $\mathbf{i}$. Thus the canonical basis elements arising in this way for at least one reduced expression $\mathbf{i}$ can be labelled $b_j$, $j=1,2,\ldots ,n$, $b_P$, $P$ a partial quiver of type $A_n$.
:::
