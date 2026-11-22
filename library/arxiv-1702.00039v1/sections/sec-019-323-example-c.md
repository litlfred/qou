---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-019-323-example-c
section_title: "Example C"
section_number: 3.2.3
pages: 15-17
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.964
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
As one might have conjectured looking at the first two examples, for $x\in I_2(n)$ we have $$\label{excc}b_x= \sum_{y\leq x}v^{l(x)-l(y)}h_y$$ If we would want to play the game we played in the first two examples, this is, if we wanted to express $b_x$ as additions and substractions of *Bott-Samelsons* (i.e. objects of the type $b_sb_r\cdots b_t,$ with $s,r,\ldots, t\in S$) then we obtain the combinatorics appearing in Temperley-Lieb algebras, but this approach is a bit complicated. It is easier to prove directly equation ([\[excc\]](#excc){reference-type="ref" reference="excc"}).

We will prove equation ([\[excc\]](#excc){reference-type="ref" reference="excc"}) by induction on the length of $x$. Let us call for the moment $$\label{exc}c_x:= \sum_{y\leq x}v^{l(x)-l(y)}h_y$$

So our induction hypothesis is that $b_y=c_y$ for all elements $y$ such that $l(y)\leq n$. Let us introduce the following

::: nota
In the group $I_2(n)=\langle s,r \rangle$ we will denote, for any $0\leq i\leq n$, $$s(i):=\underbrace{srs\cdots}_{i\ \mathrm{terms}}\in W \hspace{.3cm}  \mathrm{and} \hspace{.3cm} r(i):=\underbrace{rsr\cdots}_{i\  \mathrm{terms}} \in W$$
:::

We will prove that $$\label{good}
c_{s(n+1)}=b_sc_{r(n)}-c_{s(n-1)}$$ thus mimicking the construction that we will do in the proof of Theorem [\[thKL\]](#thKL){reference-type="ref" reference="thKL"}. Once we have proved this, we are done, because the right-hand side is clearly self-dual (by induction hypothesis), and the left-hand side clearly belongs to $h_{s(n+1)}+\sum_yv\mathbb Z[v]h_y$ and thus $c_{s(n+1)}=b_{s(n+1)}$.

We call $x:=s(n+1).$ If $$A:=\sum_{0\leq i \leq n}v^{n-i}h_{r(i)}$$ and $$B:=\sum_{0< i < n}v^{n-i}h_{s(i)},$$ then $c_{r(n)}=A+B.$

We have that $$\begin{aligned}
b_sA&=\sum_{0\leq i \leq n}v^{n-i}h_{s(i+1)}+\sum_{0\leq i \leq n}v^{(n+1)-i}h_{r(i)}\\
&=  \sum_{1\leq j \leq n+1}v^{(n+1)-j}h_{s(j)} +\sum_{0\leq i \leq n}v^{(n+1)-i}h_{r(i)}\\
&=c_{s(n+1)}.
\end{aligned}$$ On the other hand we have, using the quadratic relation, $$\begin{aligned}
b_sB&=\sum_{0< i < n}v^{n-i}h_{r(i-1)}+\sum_{0< i < n}v^{n-i-1}h_{s(i)}\\
&=   \sum_{0\leq j < n-1}v^{(n-1)-j}h_{r(j)}+\sum_{0< i < n}v^{(n-1)-i}h_{s(i)} \\
&=    c_{s(n-1)}
\end{aligned}$$ thus proving equation ([\[good\]](#good){reference-type="ref" reference="good"}).

::: remark
[]{#univ label="univ"} We can see that the proof of equation ([\[good\]](#good){reference-type="ref" reference="good"}) is independent of the dihedral group in which one is placed, but one knows that in $I_2(n)$ we have $h_{s(n)}=h_{r(n)}$, and thus, by equation ([\[good\]](#good){reference-type="ref" reference="good"}) we have $b_{s(n)}=b_{r(n)}$. This is the basic insight of the following example.
:::
