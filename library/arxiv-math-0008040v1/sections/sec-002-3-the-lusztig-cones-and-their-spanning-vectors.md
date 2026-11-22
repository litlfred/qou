---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-002-3-the-lusztig-cones-and-their-spanning-vectors
section_title: "The Lusztig cones and their spanning vectors"
section_number: 3
pages: 5-8
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.984
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
Lusztig [@lusztig7] introduced certain regions which, in low rank, give rise to canonical basis elements of a particularly simple form. The *Lusztig cone*, $C_{\mathbf{i}}$, corresponding to $\mathbf{i}\in \chi_n$, is defined to be the set of points ${{\mathbf{a}}}\in {\N}^k$ satisfying the following inequalities:\
(\*) For every pair $s,s'\in [1,k]$ with $s<s'$, $i_s=i_{s'}=i$ and $i_p\not=i$ whenever $s<p<s'$, we have $$(\sum_p a_p)-a_s - a_{s'}\geq 0,$$ where the sum is over all $p$ with $s<p<s'$ such that $i_p$ is joined to $i$ in the Dynkin diagram (we call such a pair $s,s'$ a *minimal pair*).

It was shown by Lusztig [@lusztig7] that if $\mathbf{a}\in C_{\mathbf{i}}$ then the monomial $F_{i_1}^{(a_1)}F_{i_2}^{(a_2)}\cdots
F_{i_k}^{(a_k)}$ lies in the canonical basis ${\B}$, provided $n=1,2,3$. The author [@me7] showed that this remains true if $n=4$. Counter-examples of Xi [@xi4] and Reineke [@reineke2] show that this is not true in general.

**Remark:** It can be shown that, for any $\mathbf{i}\in \chi_n$, we have $C_{\mathbf{i}}\subseteq Y_{\mathbf{i}}$, i.e., the Lusztig cone is contained in the Kashiwara cone. The methods of this paper could be used to do this in type $A_n$, but the author has recently learnt that A. Premat [@premat1] has a more succinct proof for all simply-laced cases.

The reduced expression $\mathbf{i}$ defines an ordering on the set $\Phi^+$ of positive roots of the root system associated to $W$. We write $\alpha^j=s_{i_1}s_{i_2}\cdots s_{i_{j-1}}(\alpha_{i_j})$ for $j=1,2,\ldots ,k$. Then $\Phi^+=\{\alpha^1,\alpha^2,\ldots \alpha^k\}$. For ${{\mathbf{a}}}=(a_1,a_2,\ldots
,a_k)\in {\mathbb{Z}}^k$, write $a_{\alpha^j}=a_j$. If $\alpha=\alpha_{ij}:=\alpha_i+\alpha_{i+1}+\cdots +\alpha_{j-1}$ with $i<j$, we also write $a_{ij}$ for $a_{\alpha_{ij}}$.

We shall need the chamber diagram (chamber ansatz) for $\mathbf{i}$ defined in [@bfz1 §§1.4, 2.3]. We take $n+1$ strings, numbered from top to bottom, and write $\mathbf{i}$ from left to right along the bottom of the diagram. Above a letter $i_j$ in $\mathbf{i}$, the $i_j$th and $(i_j+1)$st strings from the top above $i_j$ cross. Thus, for example, in the case $n=3$ with $\mathbf{i}=(1,3,2,1,3,2)$, the chamber diagram is shown in Figure [1](#chamberdiagram){reference-type="ref" reference="chamberdiagram"}.

<figure id="chamberdiagram">
<p>units &lt;0.5cm,0.3cm&gt; x from -10 to 14, y from -3 to 8</p>
<p>[c] at -0.3 6 [c] at -0.3 4 [c] at -0.3 2 [c] at -0.3 0</p>
<p>[c] at 1.5 -1.5 [c] at 3.5 -1.5 [c] at 5.5 -1.5 [c] at 7.5 -1.5 [c] at 9.5 -1.5 [c] at 11.5 -1.5</p>
<p>0 3 0 / 0 4 2 / 2 5 2 / 2 6 4 / 4 7 4 / 4 8 6 / 6 13 6 /</p>
<p>2 3 2 / 2 4 0 / 0 9 0 / 0 10 2 / 2 11 2 / 2 12 4 / 4 13 4 /</p>
<p>4 1 4 / 4 2 6 / 6 7 6 / 6 8 4 / 4 11 4 / 4 12 2 / 2 13 2 /</p>
<p>6 1 6 / 6 2 4 / 4 5 4 / 4 6 2 / 2 9 2 / 2 10 0 / 0 13 0 /</p>
<p>[c] at 4.5 5 [c] at 8.5 3 [c] at 6.5 1</p>
<figcaption>The Chamber Diagram of <span class="math inline">(1,3,2,1,3,2)</span>.<span id="chamberdiagram" label="chamberdiagram"></span></figcaption>
</figure>

We denote the chamber diagram of $\mathbf{i}$ by CD($\mathbf{i}$). A *chamber* will be defined as a pair $(c,{\mathbf{i}})$, where $c$ is a bounded component of the complement of CD($\mathbf{i}$). Each chamber $(c,{\mathbf{i}})$ can be labelled with the numbers of the strings passing below it, denoted $l(c,{\mathbf{i}})$. Following [@bfz1], we call such a label a chamber set. For example, the chamber sets corresponding to the $3$ bounded chambers in Figure [1](#chamberdiagram){reference-type="ref" reference="chamberdiagram"} are $134,3,13$. Note that the set of chamber sets of $\bf i$ is independent of its commutation class (so we can talk also of the chamber sets of such a commutation class). Every subset of $[1,n+1]$ can arise as a chamber set for some $\bf i$, except for subsets of the form $[1,j]$ and $[j,n+1]$ for $1\leq j\leq n+1$; this is observed in the proof of [@bfz1 Theorem 2.7.1].

We now recall some of the results from [@me8] that we shall need. We have by [@me8 §4] that there is a matrix $P_{\mathbf{i}}\in
GL_k(\mathbb{Z})$ such that $C_{\bf i}=\{{\bf a}\in \mathbb{Z}^k\,:\,P_{\bf i}{\bf a}\geq 0\},$ where, for ${\bf z}\in \mathbb{Z}^k$, $\mathbf{z}\geq 0$ means that each entry in $\bf z$ is nonnegative. It follows that $C_{\bf i}$ is the set of nonnegative linear combinations of the columns of $Q_{\bf i}=P_{\mathbf{i}}^{-1}$. These columns were described in [@me8], using the concept of a *partial quiver*.

A partial quiver $P$ of type $A_n$ is a quiver of type $A_n$ which has some (or none) of its arrows replaced by undirected edges, in such a way that the subgraph obtained by deleting undirected edges and any vertex incident only with undirected edges is connected. We number the edges of a partial quiver from $2$ to $n$, starting at the right hand end. We write $P$ as a sequence of $n-1$ symbols, $L$, $R$ or $-$, where $L$ denotes a leftward arrow, $R$ a rightward arrow, and $-$ an undirected edge. Thus any partial quiver will be of form $---***---$, where the $*$'s denote $L$'s or $R$'s.

If $P,P'$ are partial quivers we write $P'\geq P$ (or $P\leq P'$) if every edge which is directed in $P$ is directed in $P'$ and is oriented in the same way, and say that $P$ is a sub partial quiver of $P'$. For example, $---LRLL-\ \leq RLRLRLLL$.

It is known that if $\bf i$ is compatible with a quiver $Q$ (in the sense of [@lusztig2 §4.7]) then the set of reduced expressions for $w_0$ compatible with $Q$ is precisely the commutation class of $\chi_n$ containing $\bf i$. We say that this commutation class is compatible with $Q$. Berenstein, Fomin and Zelevinsky (see [@bfz1 §4.4]) describe a method for constructing $\bf i\in \chi_n$ compatible with any given quiver $Q$, as follows.

Suppose $Q$ is a quiver of type $A_n$. Let $\Lambda\subseteq [2,n]$ be the set of all edges of $Q$ pointing to the left. Berenstein, Fomin and Zelevinsky construct an arrangement Arr$(\Lambda)$. Consider a square in the plane, with horizontal and vertical sides. Put $n+1$ points onto the left-hand edge of the square, equally spaced, numbered $1$ to $n+1$ from top to bottom, and do the same for the right-hand edge, but number the points from bottom to top. ${\rm Line}_h$ joins point $h$ on the left with point $h$ on the right. For $h=1,n+1$, ${\rm Line}_h$ is a diagonal of the square. For $h\in [2,n]$, ${\rm Line}_h$ is a union of two line segments of slopes $\pi /4$ and $-\pi /4$. There are precisely two possibilities for $\mbox{Line}_h$. If $h\in \Lambda$, the left segment has slope $-\pi/4$, while the right one has slope $\pi/4$; for $h\in [2,n]\setminus \Lambda$, it goes the other way round. Berenstein, Fomin and Zelevinsky give the example of the arrangement for $n=5$ and $\Lambda=\{2,4\}$, which we show in Figure [2](#arrangement){reference-type="ref" reference="arrangement"} (points corresponding to elements of $\Lambda$ are indicated by filled circles). They show that $\bf i\in \chi_n$ is compatible with the quiver $Q$ if and only if the chamber diagram CD($\bf i$) is isotopic to Arr$(\Lambda)$.

<figure id="arrangement">
<div class="center">
<p>units &lt;0.8cm,0.8cm&gt; x from -7 to 7, y from 0 to 7</p>
<p>at 1 1 *5 0 1 / at 6 1 *5 0 1 /</p>
<p>at 1 3 at 1 5 at 6 2 at 6 4</p>
<p>[c] at 0.7 6 [c] at 0.7 5 [c] at 0.7 4 [c] at 0.7 3 [c] at 0.7 2 [c] at 0.7 1</p>
<p>[c] at 6.3 6 [c] at 6.3 5 [c] at 6.3 4 [c] at 6.3 3 [c] at 6.3 2 [c] at 6.3 1</p>
<p>6 6 1 /</p>
<p>5 5 1 / 1 6 2 /</p>
<p>4 3 6 / 6 6 3 /</p>
<p>3 3 1 / 1 6 4 /</p>
<p>2 5 6 / 6 6 5 /</p>
<p>1 6 6 /</p>
</div>
<figcaption>The arrangement Arr<span class="math inline">{2, 4}</span>.<span id="arrangement" label="arrangement"></span></figcaption>
</figure>

If $P$ is a partial quiver, let $l(P)$ be the subset of $[1,n+1]$ defined in the following way. Put $l_1(P)=\{j\in [2,n]\,:\,\mbox{edge\ $j$\ of\ $P$\ is\ an\ 
$L$}\}$. If the rightmost directed edge of $P$ is an $R$, and this is in position $i$, then let $l_2(P)=[1,i-1]$, otherwise the empty set. If the leftmost directed edge of $P$ is an $R$, and this is in position $j$, then let $l_3(P)=[j+1,n+1]$, otherwise the empty set. Then put $l(P)=l_1(P)\cup l_2(P)\cup l_3(P)$. We know from [@me8 §5.4] that $l$ sets up a one-to-one correspondence between chamber sets and partial quivers; for a chamber $(c,{\bf i})$, we denote by $P(c,{\bf i})$ the partial quiver corresponding to $l(c,{\bf i})$. Also, if $\bf i$ is compatible with a quiver $Q$, then the partial quivers corresponding to its chambers are precisely those $P\leq Q$.

Each minimal pair in ${\bf i}$ corresponds naturally to a chamber $(c,{\bf i})$. Thus, given a chamber $(c,{\bf i})$, there is a corresponding row of $P_{\bf i}$ and therefore a corresponding column of $Q_{\bf i}$, that is, a spanning vector of $C_{\bf i}$. We denote this spanning vector by $a(c,{\bf i})$. Similarly, the other $n$ rows of $P_{\bf i}$ correspond to inequalities of the form $a_{\alpha_j}\geq 0$ for $\alpha_j$ a simple root, $1\leq j\leq
n$. We denote the corresponding spanning vectors by $a(j,{\bf i})$.

We consider $a(c,{\bf i})=(a_1,a_2,\ldots ,a_k)$ as a multiset $M(c,{\bf i})$ of positive roots, where each positive root $\alpha_{ij}$ occurs with multiplicity, $a_{ij}$. Similarly we write $M(j,{\bf i})$ for the multiset corresponding to $a(j,{\bf i})$, for $j=1,2,\ldots ,k$. These multisets have been described in [@me8].

::: theorem
(See [@me8 §5.12]). []{#multiset label="multiset"}  \
(a) The multiset spanning vector $M(c,{\bf i})$ depends only upon $P(c,{\bf i})$. For a partial quiver $P$ we choose a chamber $(c,{\bf i})$ such that $P(c,{\bf i})=P$ and write $M(P)=M(c,{\bf i})$.\
(b) The multiset spanning vector $M(j,{\bf i})$ depends only upon $j$; we denote it by $M(j)$.\
(c) For a partial quiver $P$, $M(P)$ is given by the following construction. We say that a sub partial quiver $Y$ of $P$ is a *component* of $P$ if all of its edges are oriented in the same way and it is maximal in length with this property. We say $Y$ has type $L$ if its edges are oriented to the left, and type $R$ if its edges are oriented to the right. For such a component $Y$ of $P$, let $a(Y)$ be the number of the leftmost edge to the right of the component, and let $b(Y)$ be the number of the rightmost edge to the left of the component. Let $M(Y)$ be the set of positive roots $\alpha_{ij}$ satisfying $1\leq i\leq a(Y)\leq b(Y)\leq j
\leq n+1$. Then $M(P)$ is the multiset union (i.e. adding multiplicities) of the $M(Y)$, where $Y$ varies over all components of $P$, with the multiplicity $m_{ij}$ of $\alpha_{ij}$ replaced by $n_{ij}=\lceil\frac{1}{2}m_{ij}\rceil$. Furthermore, for $j=1,2,\ldots n$, $M(j)$ is the set of positive roots $\alpha_{pq}$ satisfying $1\leq p\leq j\leq j+1\leq q\leq n+1$.
:::
