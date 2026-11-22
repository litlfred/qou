---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-001-2-the-virtual-sn-characters-n
section_title: "The virtual Sn-characters ,n"
section_number: 2
pages: 1-2
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.983
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
[]{#section2 label="section2"} Let $\nu=(\nu_1,\nu_2,\ldots)\vdash k$, and $n\ge 2k+2$. First form $\nu^{(1)}=(\nu_1+n-k,\nu_2,\nu_3,\ldots)$. This is the diagram $\nu$ with $n-k$ additional boxes attached to its first row. Now pull these added $n-k$ boxes down and left around the diagram $\nu$ as follows. Think of these $n-k$ boxes as a train pulled by the first (i.e. left) cell. And pull it down and left around $\nu$ so that the result is a partition (containing $\nu$). We call this process \"going around $\nu$\", see Example [\[v2\]](#v2){reference-type="ref" reference="v2"}. This process, which is analized in Section [\[section2.1\]](#section2.1){reference-type="ref" reference="section2.1"}, yields an ordered sequence of partitions of $n$: $\nu^{(1)},\nu^{(2)},\ldots\vdash n$.

For example, verify that $\nu^{(2)}=(n-k+\nu_2-1,\nu_1+1,\nu_3,\nu_4,\ldots )$. Note that since $n\ge 2k+2$ and $\nu\vdash k$, it follows that $n-k+\nu_2-1\ge \nu_1+1$, and therefore $\nu^{(2)}$ is indeed a partition.

::: defn
(The virtual character $\psi_{\nu,n}$.) Given $\nu\vdash k$ and $n\ge k$ (we usually require that $n\ge 2k+2$), with the partitions of $n$ obtained by going around $\nu$, these partitions are ordered as first, second, third, etc. We define $\psi_{\nu,n}$ to be the alternating sum of the corresponding irreducible $S_n$ characters.
:::

::: example
[]{#v2 label="v2"} 1.

Going around the empty diagram $\nu=\emptyset$ we get the following sequence of diagrams:

$(n)\to (n-1,1)\to (n-2,1^2)\to\cdots\to (2,1^{n-2})\to (1^n)$.

Thus $$\psi_{\emptyset,n}= \sum_{j=0}^{n-1}(-1)^j\chi^{(n-j,1^j)}.$$

.  Going around $\nu=(1)$. Here $k=1$, so $n\ge 4$. Get the diagrams

$(n)\to (n-2,2)\to (n-3,2,1)\to(n-4,2,1^2) \to\cdots\to (3,2,1^{n-5})\to(2,2,1^{n-4})\to (1^n)$.

Therefore $$\psi_{(1),n}=\chi^{(n)}+\sum_{j=0}^{n-4}(-1)^{j+1}\chi^{(n-2-j,2,1^j)} + (-1)^n\chi^{(1^n)}.$$

.  Going around $(2)$. Here $k=2$ so $n\ge 6$. Get the partitions

$(n)\to(n-3,3)\to (n-4,3,1)\to (n-5,3,1^2)\to (n-6,3,1^3)\to\cdots\to (4,3,1^{n-7})\to \\
\to (3,3,1^{n-6})  \to(2^2,1^{n-4}) \to (2,1^{n-2})$.

Thus $$\begin{aligned}
\label{formula5}
 \psi_{(2),n}=\chi^{(n)}+\sum_{j=0}^{n-6}(-1)^{j+1}\chi^{(n-3-j,3,1^{j})} +
 (-1)^{n-1}\chi^{(2,2,1^{n-4})}+(-1)^n\chi^{(2,1^{n-2})}.
 
\end{aligned}$$
:::
